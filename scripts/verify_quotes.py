#!/usr/bin/env python3
"""
Verify block quotes in SKILL.md and the collected reference corpus against text/.

This is the gating artifact: SKILL.md quotes must be clean before commit. Auxiliary
reference misses are reported for inspection.

Usage:
    python3 scripts/verify_quotes.py              # check default files
    python3 scripts/verify_quotes.py --strict     # also check all references/research/*.md
"""
import argparse
import difflib
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEXT_DIR = REPO / "text"
DEFAULT_FILES = [
    REPO / "SKILL.md",
    REPO / "references" / "research" / "verbatim-corpus.md",
]


def normalize(s: str) -> str:
    """Aggressive normalization for matching: NFKC, strip inline citations, collapse whitespace, lowercase."""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("“", '"').replace("”", '"')   # smart quotes
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("—", "--").replace("–", "-")  # em/en dash
    # Strip inline reference citations like "[ 49 ]", "[49, 50]", "( 13 , 14 )", "[1]"
    s = re.sub(r"\[\s*\d+(?:\s*[,\-]\s*\d+)*\s*\]", "", s)
    s = re.sub(r"\(\s*\d+(?:\s*[,\-]\s*\d+)*\s*\)", "", s)
    # Strip lone bracketed reference markers like " [ 1 , 2 , 3 , 4 ] "
    # (already handled above)
    # Strip non-letter punctuation noise that varies between renderers
    s = re.sub(r"\s*\.\s*", ".", s)             # normalize spaces around periods
    s = re.sub(r"\s*,\s*", ",", s)
    s = re.sub(r"\s+", " ", s)                   # finally collapse whitespace
    return s.strip().lower()


# Match block quotes: lines starting with `> "..."`. Multiline-aware so the
# quote can span continuation lines (each prefixed with `> `).
BLOCK_QUOTE_RE = re.compile(r'^>\s*[“"](.+?)[”"]', re.M | re.S)
# Inline "..." quotes ≥30 chars on a non-block-quote line.
INLINE_QUOTE_RE = re.compile(r'[“"]([^"“”\n]{30,400})[”"]')


def extract_quotes(text: str):
    """
    Yield candidate verbatim quotes from a markdown file (deduped).

    Convention used in this repo:
      - Block-quoted lines like  `> "..."`  are CLAIMED VERBATIM and must verify.
      - Inline `"..."` quotes are scare quotes / illustrative paraphrases /
        user-dialogue examples and are NOT verified.

    Only block quotes are checked by default.
    """
    seen_norm = set()
    for m in BLOCK_QUOTE_RE.finditer(text):
        q = m.group(1).strip()
        if len(q.split()) < 4:
            continue
        n = normalize(q)
        if n in seen_norm:
            continue
        seen_norm.add(n)
        yield q


def load_corpus():
    """Concatenate every text/**/*.md into one normalized blob (with file boundaries)."""
    blobs = []
    for p in sorted(TEXT_DIR.rglob("*.md")):
        blobs.append((p.relative_to(REPO), normalize(p.read_text(encoding="utf-8", errors="replace"))))
    return blobs


def find_match(quote_norm: str, blobs, fuzzy_threshold: float = 0.78):
    """Try exact substring; on miss, anchor-based fuzzy match (≥threshold).

    Performance: anchor on the first 8 words of the quote, find at most 3
    candidate positions in the blob via str.find, run SequenceMatcher on each.
    Bails out fast if the quote can't be located.
    """
    for path, blob in blobs:
        if quote_norm in blob:
            return path, "exact"
    if len(quote_norm) < 40:
        return None, None

    # Anchor: first 6 words. Look for them in each blob; if found, fuzzy-match
    # a window starting there.
    words = quote_norm.split()
    if len(words) < 5:
        return None, None
    anchor = " ".join(words[:6])  # ~30-50 chars
    L = len(quote_norm)

    for path, blob in blobs:
        # Find up to 3 candidate positions of the anchor
        starts = []
        i = 0
        while len(starts) < 3:
            j = blob.find(anchor, i)
            if j < 0:
                break
            starts.append(j)
            i = j + 1
        if not starts:
            # Try a shorter anchor (3 words)
            short_anchor = " ".join(words[:3])
            if len(short_anchor) < 12:
                continue
            j = blob.find(short_anchor)
            if j >= 0:
                starts = [j]
            else:
                continue

        for s in starts:
            window = blob[s : s + int(L * 1.3)]
            r = difflib.SequenceMatcher(None, quote_norm, window).ratio()
            if r >= fuzzy_threshold:
                return path, f"fuzzy({r:.2f})"
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="also check all references/research/*.md")
    ap.add_argument("files", nargs="*",
                    help="explicit files to check (overrides defaults)")
    args = ap.parse_args()

    files = [Path(f).resolve() for f in args.files] if args.files else list(DEFAULT_FILES)
    if args.strict:
        files += list((REPO / "references" / "research").glob("*.md"))

    # Dedupe (--strict re-adds verbatim-corpus.md which is also in DEFAULT_FILES)
    seen_paths = set()
    unique = []
    for f in files:
        rp = f.resolve()
        if rp not in seen_paths:
            seen_paths.add(rp)
            unique.append(rp)
    files = [f for f in unique if f.exists()]
    if not files:
        print("WARN: no input files exist yet (skill not synthesized).", file=sys.stderr)
        return 0

    print(f"Loading text corpus from {TEXT_DIR}…")
    blobs = load_corpus()
    print(f"  {len(blobs)} source files")

    total = 0
    misses = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        quotes = list(extract_quotes(text))
        print(f"\n[{f.relative_to(REPO)}]  {len(quotes)} quotes to verify")
        for q in quotes:
            total += 1
            qn = normalize(q)
            hit, how = find_match(qn, blobs)
            if hit is None:
                misses.append((f.relative_to(REPO), q))
                print(f"  ✗ MISS: {q[:90]}…")
            # else:
            #     print(f"  ✓ {hit}: {q[:60]}…")

    print(f"\n{'='*60}")
    print(f"Total quotes checked : {total}")
    print(f"Verified             : {total - len(misses)}")
    print(f"Misses               : {len(misses)}")

    # Per-file miss aggregation
    from collections import Counter
    miss_by_file = Counter(str(f) for f, _ in misses)
    if miss_by_file:
        print("\nMisses by file:")
        for f, n in miss_by_file.most_common():
            print(f"  {f}: {n}")

    if misses:
        print("\nFirst 20 missing quotes (not found in text/):")
        for f, q in misses[:20]:
            print(f"  {f}: {q[:120]}")

    # Gating logic: SKILL.md must be 100% clean. Auxiliary files may have
    # auxiliary files include collected quotes with occasional renderer or notation
    # drift; emit warnings but keep SKILL.md as the hard gate.
    skill_path = REPO / "SKILL.md"
    skill_misses = [m for m in misses if m[0] == skill_path.relative_to(REPO)]
    if skill_misses:
        print(f"\n✗ FAIL: SKILL.md has {len(skill_misses)} unverified quote(s).")
        return 1
    if misses:
        pct = 100.0 * len(misses) / max(total, 1)
        print(f"\n⚠ WARN: SKILL.md is clean, but auxiliary files have {len(misses)} unverified quotes ({pct:.1f}%).")
        print("        These may be renderer/notation drift or true misses.")
        print("        Inspect the list above before making stronger verification claims.")
        return 0
    print("\nAll quotes verified ✓")
    return 0


if __name__ == "__main__":
    sys.exit(main())
