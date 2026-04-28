#!/usr/bin/env python3
"""
Fetch ~50 Kaiming He papers from arXiv with HTML→ar5iv→PDF fallback.

Reads assets/seed_papers.txt, writes papers/{arxiv_id}.{html|pdf}.
Idempotent: skips already-downloaded files.
"""
import os
import re
import sys
import time
from pathlib import Path
from typing import Optional, Tuple

import requests

REPO = Path(__file__).resolve().parent.parent
SEED = REPO / "assets" / "seed_papers.txt"
OUT = REPO / "papers"
OUT.mkdir(exist_ok=True)

UA = "kaiming-he-skill/1.0 (research; contact: ireneyu1024@gmail.com)"
HEADERS = {"User-Agent": UA}
SESSION = requests.Session()
SESSION.headers.update(HEADERS)


def parse_seeds(path: Path):
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = re.split(r"\s+", line, maxsplit=3)
        if len(parts) < 4:
            continue
        arxiv_id, author_pos, year, title = parts
        rows.append({"id": arxiv_id, "author_pos": author_pos, "year": year, "title": title})
    return rows


def try_fetch(url: str, timeout: int = 30) -> Optional[requests.Response]:
    try:
        r = SESSION.get(url, timeout=timeout, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 1000:
            return r
    except Exception as e:
        print(f"   error: {e}", file=sys.stderr)
    return None


def fetch_one(arxiv_id: str) -> Optional[Tuple[str, str]]:
    """Cascade html → ar5iv → pdf. Returns (path_relative, format)."""
    html_path = OUT / f"{arxiv_id}.html"
    pdf_path = OUT / f"{arxiv_id}.pdf"
    if html_path.exists() and html_path.stat().st_size > 5000:
        return (str(html_path.relative_to(REPO)), "html")
    if pdf_path.exists() and pdf_path.stat().st_size > 50000:
        return (str(pdf_path.relative_to(REPO)), "pdf")

    # 1. arxiv.org/html/{id}  (post-Dec 2023, MathML)
    url1 = f"https://arxiv.org/html/{arxiv_id}"
    print(f"  → {url1}")
    r = try_fetch(url1)
    if r is not None and "<html" in r.text.lower() and "abstract" in r.text.lower():
        html_path.write_bytes(r.content)
        return (str(html_path.relative_to(REPO)), "html")

    time.sleep(1)
    # 2. ar5iv.labs.arxiv.org/html/{id}  (legacy)
    url2 = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
    print(f"  → {url2}")
    r = try_fetch(url2)
    if r is not None and "<html" in r.text.lower():
        html_path.write_bytes(r.content)
        return (str(html_path.relative_to(REPO)), "html")

    time.sleep(1)
    # 3. export.arxiv.org/pdf/{id}.pdf
    url3 = f"https://export.arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  → {url3}")
    r = try_fetch(url3, timeout=60)
    if r is not None and r.content[:4] == b"%PDF":
        pdf_path.write_bytes(r.content)
        return (str(pdf_path.relative_to(REPO)), "pdf")

    return None


def main():
    rows = parse_seeds(SEED)
    print(f"Parsing {len(rows)} seed papers from {SEED}\n")
    manifest = []
    for i, row in enumerate(rows, 1):
        print(f"[{i}/{len(rows)}] {row['id']}  ({row['author_pos']}, {row['year']}) — {row['title']}")
        result = fetch_one(row["id"])
        if result is None:
            print(f"   FAILED: {row['id']}")
            manifest.append({**row, "path": None, "format": None})
        else:
            path, fmt = result
            print(f"   ok: {path} ({fmt})")
            manifest.append({**row, "path": path, "format": fmt})
        time.sleep(3)  # arxiv rate limit

    # Write manifest
    import json
    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=2))
    n_ok = sum(1 for m in manifest if m["path"])
    print(f"\nDone: {n_ok}/{len(manifest)} fetched")
    print(f"Manifest: {OUT}/_manifest.json")
    return 0 if n_ok == len(manifest) else 1


if __name__ == "__main__":
    sys.exit(main())
