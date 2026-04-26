#!/usr/bin/env python3
"""
Extract text from raw papers/ + talks/ into text/{papers,talks}/{id}.md.
- HTML: bs4 strip nav/script/style/refs/figure-captions, keep main content.
- PDF (papers): pymupdf4llm.to_markdown, then section-selective filter (keep
  Abstract / Intro / Method / Discussion / Conclusion / Ablation; drop Related
  Work / Implementation Details / References / Appendix).
- PDF (talk slides): pymupdf4llm full extraction (slides are short).
- VTT: dedup rolling-window auto-caption lines, write as plaintext.

Idempotent: skips already-extracted files.
"""
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PAPERS = REPO / "papers"
TALKS = REPO / "talks"
OUT_PAPERS = REPO / "text" / "papers"
OUT_TALKS = REPO / "text" / "talks"
OUT_PAPERS.mkdir(parents=True, exist_ok=True)
OUT_TALKS.mkdir(parents=True, exist_ok=True)

# Section heading patterns to KEEP (case-insensitive whole-word matches)
KEEP_SECTIONS = re.compile(
    r"^\s*(?:\d+\.?\s*)?(abstract|introduction|background|approach|method(?:s|ology)?|"
    r"design|architecture|formulation|deconstruction|discussion|conclusion|ablation|"
    r"analysis|study|results|main results|experiments?|finding|observation)s?\b",
    re.I,
)
# Section heading patterns to STOP at (drop everything from here on)
DROP_SECTIONS = re.compile(
    r"^\s*(?:\d+\.?\s*)?(related work|implementation details?|references|"
    r"acknowledg(?:e?ments?)?|appendix|supplement(?:ary)?|broader impact|"
    r"limitations? and broader|datasets? and metrics?|training details?|"
    r"hyperparameters?|computing infrastructure)\b",
    re.I,
)


def extract_html(path: Path) -> str:
    from bs4 import BeautifulSoup

    html = path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")
    # Drop noise
    for sel in ["nav", "script", "style", "header", "footer", "form",
                ".bib", ".references", ".ltx_bibliography", ".ltx_appendix"]:
        for el in soup.select(sel):
            el.decompose()
    # Try article body
    body = soup.find("article") or soup.find("main") or soup.body or soup
    text_parts = []
    for el in body.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
        txt = el.get_text(" ", strip=True)
        if not txt:
            continue
        tag = el.name
        if tag in ("h1", "h2", "h3", "h4"):
            depth = int(tag[1])
            text_parts.append("\n" + ("#" * depth) + " " + txt + "\n")
        else:
            text_parts.append(txt + "\n")
    text = "\n".join(text_parts)
    return _section_filter(text)


def extract_pdf(path: Path, do_section_filter: bool = True) -> str:
    import pymupdf4llm

    md = pymupdf4llm.to_markdown(str(path))
    return _section_filter(md) if do_section_filter else md


def _section_filter(text: str) -> str:
    """
    Drop sections like Related Work / Implementation Details / References.
    Walks line-by-line, toggles keep/drop on each markdown heading.
    """
    out = []
    keep = True
    for line in text.splitlines():
        is_heading = bool(re.match(r"^#{1,4}\s+", line))
        if is_heading:
            heading_text = re.sub(r"^#+\s+", "", line).strip()
            if DROP_SECTIONS.match(heading_text):
                keep = False
                continue
            if KEEP_SECTIONS.match(heading_text):
                keep = True
            elif heading_text.startswith("Appendix") or heading_text.startswith("Supplement"):
                keep = False
                continue
            else:
                # Unknown headings: default to keep (Abstract often has no number)
                keep = True
        if keep:
            out.append(line)
    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip() + "\n"


def extract_vtt(path: Path) -> str:
    """De-duplicate YouTube auto-caption rolling-window lines."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = []
    seen_recent = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        if "-->" in line:  # timestamp line
            continue
        # Strip inline VTT timing tags <00:00:00.000>
        line = re.sub(r"<\d\d:\d\d:\d\d\.\d{3}>", "", line)
        line = re.sub(r"</?c[^>]*>", "", line).strip()
        if not line:
            continue
        # Dedup: skip if line is a substring of the previous accumulated line
        if seen_recent and (line == seen_recent[-1] or line in seen_recent[-1]):
            continue
        seen_recent.append(line)
        if len(seen_recent) > 5:
            seen_recent.pop(0)
        lines.append(line)
    return "\n".join(lines) + "\n"


def main():
    n_html, n_pdf, n_vtt = 0, 0, 0

    # Papers (HTML or PDF)
    for src in sorted(PAPERS.glob("*.html")):
        out = OUT_PAPERS / f"{src.stem}.md"
        if out.exists() and out.stat().st_size > 1000:
            continue
        try:
            md = extract_html(src)
            out.write_text(md, encoding="utf-8")
            print(f"[html] {src.name} → {out.name} ({len(md)} chars)")
            n_html += 1
        except Exception as e:
            print(f"[ERR ] {src.name}: {e}", file=sys.stderr)

    for src in sorted(PAPERS.glob("*.pdf")):
        out = OUT_PAPERS / f"{src.stem}.md"
        if out.exists() and out.stat().st_size > 1000:
            continue
        try:
            md = extract_pdf(src, do_section_filter=True)
            out.write_text(md, encoding="utf-8")
            print(f"[pdf ] {src.name} → {out.name} ({len(md)} chars)")
            n_pdf += 1
        except Exception as e:
            print(f"[ERR ] {src.name}: {e}", file=sys.stderr)

    # Talk slide PDFs (no section filter — slides are short)
    for src in sorted(TALKS.glob("*.pdf")):
        out = OUT_TALKS / f"{src.stem}.md"
        if out.exists() and out.stat().st_size > 500:
            continue
        try:
            md = extract_pdf(src, do_section_filter=False)
            out.write_text(md, encoding="utf-8")
            print(f"[talk] {src.name} → {out.name} ({len(md)} chars)")
            n_pdf += 1
        except Exception as e:
            print(f"[ERR ] {src.name}: {e}", file=sys.stderr)

    # YouTube VTT
    for src in sorted(TALKS.glob("*.vtt")):
        out = OUT_TALKS / f"{src.stem.replace('.en', '')}.md"
        if out.exists() and out.stat().st_size > 500:
            continue
        try:
            md = extract_vtt(src)
            out.write_text(md, encoding="utf-8")
            print(f"[vtt ] {src.name} → {out.name} ({len(md)} chars)")
            n_vtt += 1
        except Exception as e:
            print(f"[ERR ] {src.name}: {e}", file=sys.stderr)

    print(f"\nDone: html={n_html} pdf={n_pdf} vtt={n_vtt}")


if __name__ == "__main__":
    main()
