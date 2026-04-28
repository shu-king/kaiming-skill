#!/usr/bin/env python3
"""
Aggregate all notes/{id}.json into references/research/verbatim-corpus.md.

Each quote is rendered as a block-quote with full provenance:
  > "verbatim text"
  > — <Title> (arXiv:<id>, §<section>) | theme=<theme> | voice_certain=<bool>

Quotes are grouped by THEME, then sorted by paper year then voice_certain.
"""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTES = REPO / "notes"
SEED = REPO / "assets" / "seed_papers.txt"
OUT = REPO / "references" / "research" / "verbatim-corpus.md"

# Build paper-id → metadata table from the seed file
META = {}
for line in SEED.read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = re.split(r"\s+", line, maxsplit=3)
    if len(parts) < 4:
        continue
    arxiv_id, author_pos, year, title = parts
    META[arxiv_id] = {"author_pos": author_pos, "year": year, "title": title}

# Talks metadata (parsed from seed_talks.txt)
TALK_META = {}
for line in (REPO / "assets" / "seed_talks.txt").read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = re.split(r"\s+", line, maxsplit=4)
    if len(parts) < 5:
        continue
    type_, url, short_id, year, title = parts
    if type_ == "youtube":
        short_id = "yt_" + short_id.removeprefix("yt_")
        # Map to actual notes filename
        if short_id == "yt_yt_mit_dlbootcamp_2024":
            short_id = "yt_mit2024"
        elif short_id == "yt_yt_cvpr2017_tutorial":
            short_id = "yt_cvpr2017"
    TALK_META["talk_" + short_id] = {"year": year, "title": title}
# Manual fix for the YouTube entries since seed file has yt_ prefix already
TALK_META.setdefault("talk_yt_mit2024", {"year": "2024", "title": "Learning Deep Representations (MIT Bootcamp)"})
TALK_META.setdefault("talk_yt_cvpr2017", {"year": "2017", "title": "CVPR 2017 Tutorial Video"})


def render_quote(q):
    sid = q.get("source_id", "?")
    section = q.get("section", "?")
    theme = q.get("theme_guess", "?")
    voice = q.get("voice_certain", False)
    quote = q.get("verbatim_quote", "").strip()
    # Collapse multi-line slide quotes onto one line for verifiability.
    # Real newlines from JSON parsing → space; multiple whitespace → one.
    quote = re.sub(r"\s+", " ", quote.replace("\n", " "))
    if sid in META:
        m = META[sid]
        cite = f'{m["title"]} (arXiv:{sid}, §{section}, {m["year"]}, {m["author_pos"]} author)'
    elif sid in TALK_META:
        m = TALK_META[sid]
        cite = f'{m["title"]} (talk:{sid}, §{section}, {m["year"]})'
    else:
        cite = f'(source_id:{sid}, §{section})'
    voice_tag = "" if voice else "  *[voice_certain: false]*"
    return f'> "{quote}"\n> — {cite}{voice_tag}\n'


# Load all notes
all_quotes = []
for path in sorted(NOTES.glob("*.json")):
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        print(f"BAD: {path}: {e}")
        continue
    for q in data:
        # Inject source_id from filename if missing
        q.setdefault("source_id", path.stem.removeprefix("talk_") if path.stem.startswith("talk_") else path.stem)
        if path.stem.startswith("talk_"):
            q["source_id"] = path.stem
        all_quotes.append(q)

# Group by theme
theme_order = [
    "simplicity",
    "deconstruction",
    "ablation-discipline",
    "generality",
    "scaling",
    "self-supervision",
    "residual",
    "recognition-generation-duality",
    "pixels-over-tokens",
    "research-methodology",
    "other",
]
by_theme = {t: [] for t in theme_order}
for q in all_quotes:
    by_theme.setdefault(q.get("theme_guess", "other"), []).append(q)

# Sort each bucket: voice_certain first, then by year (newest first), then by source_id
def sort_key(q):
    sid = q.get("source_id", "")
    year = META.get(sid, TALK_META.get(sid, {})).get("year", "0")
    try:
        year_int = -int(year)
    except Exception:
        year_int = 0
    return (not q.get("voice_certain", False), year_int, sid)


lines = [
    "# Verbatim Quote Corpus",
    "",
    f"All {len(all_quotes)} verbatim quotes extracted from {len(list(NOTES.glob('*.json')))} primary sources, grouped by theme.",
    "",
    "Quotes are intended to be grounded to `text/{papers,talks}/<id>.md`.",
    "Run `python3 scripts/verify_quotes.py --strict` to inspect exact matches, fuzzy matches, and auxiliary misses before making stronger verification claims.",
    "",
    "**voice_certain** = the quote comes from first/last-author papers or talks where Kaiming He is the primary speaker. False on middle-author papers unless the quote is clearly part of the Kaiming-style paper register ('without bells and whistles', 'we observe', 'simplest thing that works').",
    "",
]

for theme in theme_order:
    bucket = by_theme.get(theme, [])
    if not bucket:
        continue
    lines.append(f"\n## Theme: {theme}  ({len(bucket)} quotes)\n")
    for q in sorted(bucket, key=sort_key):
        lines.append(render_quote(q))

other_themes = set(by_theme.keys()) - set(theme_order)
for theme in sorted(other_themes):
    bucket = by_theme[theme]
    lines.append(f"\n## Theme: {theme}  ({len(bucket)} quotes)\n")
    for q in sorted(bucket, key=sort_key):
        lines.append(render_quote(q))

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT} — {len(all_quotes)} quotes, {sum(1 for q in all_quotes if q.get('voice_certain'))} voice-certain")
