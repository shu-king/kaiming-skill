# scripts/

Reproducible ingest pipeline for `kaiming-he-skill`.

## Pipeline overview (DAG)

```
seed_papers.txt   ─┐
                   ├──▶  fetch_arxiv.py    ──▶  papers/{id}.{html|pdf}
seed_talks.txt    ─┘     fetch_talks.sh    ──▶  talks/{id}.{pdf|vtt}
                                                       │
                                                       ▼
                                              extract_text.py
                                                       │
                                                       ▼
                                              text/{papers,talks}/{id}.md
                                                       │
                                                       ▼
                                       per-doc subagent fan-out (manual)
                                                       │
                                                       ▼
                                              notes/{id}.json
                                                       │
                                                       ▼
                                          cluster + synthesize (manual)
                                                       │
                                                       ▼
                                              SKILL.md + references/
                                                       │
                                                       ▼
                                              verify_quotes.py
                                                  (SKILL.md must be clean)
```

## Re-running the pipeline

```bash
# 0. Install deps (one-time)
pip install arxiv pymupdf4llm beautifulsoup4 lxml requests
brew install yt-dlp ffmpeg
yt-dlp -U                         # nsig pre-flight (April 2026 risk)

# 1. Fetch raw corpus (~3 min wall-clock, mostly I/O wait)
python3 scripts/fetch_arxiv.py    # 46 papers, html→ar5iv→pdf cascade
bash    scripts/fetch_talks.sh    # 7 slide PDFs + 2 YouTube auto-captions

# 2. Extract text (~30s)
python3 scripts/extract_text.py   # section-selective filter on PDFs

# 3. Per-doc quote extraction (manual; uses Claude Code subagent fan-out)
#    Spawn ~7 subagents in parallel, each emitting notes/{id}.json
#    See plan: /Users/kk/.claude/plans/memoized-painting-waffle.md

# 4. Synthesize SKILL.md + references/research/*.md (manual; Opus)

# 5. Verify SKILL.md quotes (gating)
python3 scripts/verify_quotes.py
python3 scripts/verify_quotes.py --strict  # inspect auxiliary reference warnings
```

## Files

| Script | Purpose |
|---|---|
| `fetch_arxiv.py` | arXiv API + html→ar5iv→pdf cascade. Polite UA, 3s sleep, idempotent. |
| `fetch_talks.sh` | `curl` slide PDFs from people.csail.mit.edu + `yt-dlp --write-auto-sub` |
| `extract_text.py` | `bs4` for HTML, `pymupdf4llm` for PDFs, section-selective filter |
| `verify_quotes.py` | Grep block quotes in `SKILL.md` and the collected reference corpus against `text/**/*.md`. Fails on `SKILL.md` misses and reports auxiliary reference warnings. |

## Idempotence

All scripts skip files that are already downloaded/extracted. Safe to re-run after a partial failure.

## Sizes

| Stage | Size |
|---|---|
| `papers/` (raw) | ~150 MB |
| `talks/` (raw) | ~80 MB (mostly slide PDFs) |
| `text/` (extracted) | ~3 MB |
| `notes/` (quotes JSON) | ~200 KB |
| Final committed repo | ~5 MB |

Raw `papers/`, `talks/`, `text/`, `notes/` are gitignored — reproducible from seeds.
