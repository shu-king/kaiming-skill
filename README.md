# kaiming-he-skill

A Claude Code persona-skill that channels **Kaiming He's research design philosophy and writing voice** — a thinking instrument for CV/DL researchers drafting papers, designing ablations, and auditing methodological complexity.

> *"Less is More — Occam's Razor. Future is the Real Test Set."*
> — Kaiming He, NeurIPS 2024 New-in-ML

## What this skill does

When activated, the skill responds in Kaiming He's voice and routes your question to one of six mental models distilled from his ~50-paper corpus (ResNet → Mask R-CNN → MoCo → MAE → l-DAE → MAR → MeanFlow → JiT) and recent talks (NeurIPS 2024/2025, CVPR 2025).

It is good at:
- **Design-philosophy review** — "is this method too complex?", "what is essential vs. incidental?"
- **Paper structure critique** — does your intro follow the canonical four-paragraph pattern?
- **Ablation-table design** — the gray-shaded, one-variable-at-a-time Kaiming-style table (built-in tutor protocol)
- **Simplicity audits** — "what's the simplest version that still works?"

It is **not** good at: optimization theory, NLP/speech/RL, or papers post-cutoff (2026-04-27) — for new papers it WebSearches arXiv first.

## Install

```bash
git clone https://github.com/<your-username>/kaiming-he-skill ~/.claude/skills/kaiming-he-perspective
```

(Or wherever your Claude Code skills directory lives.)

## Activate

Type any of these triggers:
- "Kaiming视角", "Kaiming-style", "what would Kaiming say about X?"
- "subtraction principle", "less is more", "essential vs incidental"
- "design my ablation table", "review my ML paper"
- "is this method too complex?", "challenge the inherited default"

## Repository layout

```
SKILL.md                           Installable skill body (13 sections + ablation tutor)
references/research/
  ├── 01-papers.md                 ~50-paper corpus index + per-paper design notes
  ├── 02-talks.md                  Slide decks + YouTube tutorials
  ├── 03-expression-dna.md         Sentence patterns, intro template, ablation conventions
  ├── 04-external-views.md         Community commentary
  ├── 05-decisions.md              MSRA → FAIR → MIT pivots
  ├── 06-timeline.md               1984– bio + intellectual lineage
  └── verbatim-corpus.md           Every quote tagged with (arXiv ID, section)
examples/                          Demo conversations
scripts/                           Reproducible ingest pipeline (arxiv → text → notes → SKILL)
assets/                            Seed paper IDs and talk URLs
```

## Reproducing the corpus

```bash
pip install arxiv pymupdf4llm beautifulsoup4 lxml requests
brew install yt-dlp
python3 scripts/fetch_arxiv.py
bash   scripts/fetch_talks.sh
python3 scripts/extract_text.py
python3 scripts/verify_quotes.py    # gating verification — must exit 0
```

See `scripts/README.md` for the full DAG.

## Honest boundaries

- Knowledge cutoff: **2026-04-27**. The skill cannot speak to Kaiming's unpublished current views.
- Voice attribution on multi-author papers (Faster R-CNN, FPN, Focal Loss) is uncertain — those quotes carry `voice_certain: false` and are quoted sparingly.
- Every quote in this repo is grounded to a `(arXiv ID, section)` tag and verified by `scripts/verify_quotes.py`.

## License

MIT. See `LICENSE`.

## Acknowledgements

Modelled on the [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill) template. Anthropic skill spec: [`anthropics/skills`](https://github.com/anthropics/skills).
