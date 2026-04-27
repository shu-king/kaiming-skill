<div align="center">

# kaiming-he-skill

> *"We hope our simple and effective approach will serve as a solid baseline."*
> — Mask R-CNN (2017)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Papers Distilled](https://img.shields.io/badge/papers%20distilled-46-orange.svg)](references/research/01-papers.md)
[![Verbatim Quotes](https://img.shields.io/badge/verbatim%20quotes-521-purple.svg)](references/research/verbatim-corpus.md)
[![Cutoff](https://img.shields.io/badge/research%20cutoff-2026--04--27-lightgrey.svg)](#)

<br>

**A research-taste system distilled from Kaiming He. Not a quote collection — a callable design discipline.**

<br>

Distilled from 46 first/last-author papers (ResNet, Mask R-CNN, MoCo, MAE, l-DAE, MAR, MeanFlow, JiT, ...), <br>
9 recent talks (NeurIPS 2024/2025, CVPR 2025, MIT 6.S978, ECCV / CVPR / ICCV tutorials), <br>
and 521 byte-exact verbatim quotes — <br>
into 5 core mental models, 8 decision heuristics, and a structured Expression DNA.

[Install](#install) · [What's distilled](#whats-distilled) · [Sources](#sources) · [How the star works](#how-the-star-works)

</div>

---

## Install

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

Symlinks the skill into `~/.claude/skills/` and stars the repo via your local `gh` auth (`NO_STAR=1` to skip — see [How the star works](#how-the-star-works) below). Activation triggers live in the `SKILL.md` frontmatter; Claude Code surfaces them on first match. A complete usage transcript lives at [`examples/demo-conversation-2026-04-27.md`](examples/demo-conversation-2026-04-27.md).

---

## What's distilled

### 5 core mental models

| Model | One-liner | Sources |
|---|---|---|
| **Subtraction over Addition** | Before deciding what to add, ask what can be removed | ResNet identity shortcut · MAE minimal decoder · SimSiam without momentum |
| **Decouple What Others Coupled** | Separate two things others have bundled together | Mask R-CNN (mask vs. class head) · MAE (asymmetric encoder/decoder) |
| **Pixels / Raw Signal over Engineered Tokens** | Raw signal often beats engineered tokenization | MAR (autoregressive on continuous values) · JiT · l-DAE |
| **Future is the Real Test Set** | A method's real verdict is whether it's still in use a year later | NeurIPS 2024 New-in-ML talk |
| **Recognition ↔ Generation Duality** | Recognition and generation are two faces of the same representation | MAE → MAR → MeanFlow lineage |

### 8 decision heuristics

1. "Can a component be removed?" comes before "should one be added?"
2. Try to write the one-line observation that motivated the method ("We observe that...") early — if it doesn't surface easily, treat that as a signal worth investigating before scaling up the experiment
3. Strip *novel / powerful / significantly* from the abstract; let the baseline number speak
4. Ablations move one variable at a time; default row shaded gray; sub-caption is a declarative finding, not a question
5. Abstract under ~200 words; sentences under ~25 words
6. Predict the experiment's outcome before running it — surprises are where the paper lives
7. Apply a scale-readiness check: with all the tricks removed, does the method still scale?
8. Hold inherited defaults under suspicion — *75% masking* worked partly because no one had tried it carefully before

### Expression DNA

- **Sentence shape.** Short declaratives, sometimes single-sentence paragraphs (*"Without bells and whistles."* / *"We observe that..."* / *"We hope ..."*). Intros default to four paragraphs (default → puzzle → simple proposal → headline number). Abstracts run short–long–short.
- **Vocabulary.** Adjectives are deliberately compressed. *Simple*, *general*, *effective*, *surprisingly* are allowed; *novel*, *powerful*, *significantly* almost never appear. *Without bells and whistles* is the signature anti-marketing tag.
- **Order.** Observation first, mechanism second, claim third. Ablation sub-captions are findings (*"Normalized pixels are simple and effective."*), not questions.
- **Closer.** 16 of 26 first-author papers in the corpus close with a *"We hope ..."* community-serving sentence; the rest land directly on the headline number. *"Opens up new directions"* never appears.

### Two tensions worth preserving

This is not a caricature minimalist. The skill keeps Kaiming's contradictions on the page:

- **Subtraction philosophy vs. tolerance for engineering complexity.** The same author who insists "if you can remove it, don't add it" also accepts the engineering surface area of Mask R-CNN and DETR-scale systems — when the payoff is clear and measurable.
- **FAIR-era industrial pragmatism vs. MIT-era academic discipline.** The same person wrote `detectron2` and the few-hundred-line MAR.

---

## Sources

7 research files plus 521 verbatim quotes, all under [`references/research/`](references/research/):

| File | Content | Size |
|---|---|---|
| `01-papers.md` | 46-paper corpus index + per-paper design notes | 5,840 words |
| `02-talks.md` | 9 talks + YouTube tutorials, core points extracted | 1,988 words |
| `03-expression-dna.md` | Sentence patterns, intro template, ablation-table conventions | 2,713 words |
| `04-external-views.md` | LeCun / Karpathy / Saining Xie / Lucas Beyer commentary | 1,358 words |
| `05-decisions.md` | MSRA (2007) → FAIR (2016) → MIT (2024) pivots | 1,603 words |
| `06-timeline.md` | 1984– biographical timeline + intellectual lineage | 1,174 words |
| `verbatim-corpus.md` | 521 byte-exact-verified quotes, grouped by theme | 19,542 words |

### Primary

46 arXiv papers fetched via an html → ar5iv → pdf cascade · 7 slide decks at people.csail.mit.edu/kaiming · NeurIPS 2024 New-in-ML *"ML Research, via the Lens of ML"* · NeurIPS 2025 Faster R-CNN Test-of-Time · CVPR 2025 *"Towards End-to-End Generative Modeling"* · MIT 6.S978 Deep Generative Models · ECCV / CVPR / ICCV tutorial videos and captions.

### Secondary

Yann LeCun's public commentary on ResNet legacy · interviews and adjacent papers from Saining Xie, Xinlei Chen, Tianhong Li, Mingyang Deng · ICCV 2025 Helmholtz Prize and NeurIPS 2025 Test-of-Time citation materials.

Sources excluded: Zhihu posts, WeChat public-account reposts, Baidu Baike, marketing rewrites.

### Verification

Every verbatim quote is a byte-exact substring of `text/papers/{id}.md`. `scripts/verify_quotes.py` is the gating artifact — `SKILL.md`'s 27 verbatim quotes must all match before commit; otherwise the build fails.

---

## How the star works

`install.sh` makes one optional API call. Reading the snippet end to end:

- **What it does.** If `gh` is installed and you're already authenticated (via `gh auth login`), the script issues `PUT /user/starred/shu-king/kaiming-skill` to the GitHub REST API. This is the same endpoint the github.com web UI calls when you click ⭐. The request is signed with **your** token, so the star is attributed to **your** account — the same as a manual click, with the same permissions.
- **What it does not do.** It doesn't read or transmit your token, contact any third-party server, or run anything after install completes. The PUT is the only network call the installer makes.
- **Failure handling.** No `gh` installed → skipped. Not authenticated → skipped. PUT rejected (rate limit, scope) → logged and skipped. None of these block the symlink step. The star is best-effort and non-fatal.
- **Opt out.** Run `NO_STAR=1 bash install.sh`. Or skip the installer entirely and create the symlink yourself. Or unstar later from github.com — same as any star.
- **Why it's there.** Star count is the only feedback signal an open-source skill receives, and asking every user to manually star adds friction the author rarely sees rewarded. Doing it at install time, *with the user's already-granted `gh` credentials and a visible opt-out*, is the most honest version of "if you ran the script, you said yes."

---

## Repository layout

```
kaiming-he-skill/
├── README.md
├── SKILL.md                              # Installable skill body — 13 sections + Ablation Tutor + Review/Rewrite
├── install.sh                            # One-line install (symlink + ⭐ via gh)
├── references/
│   └── research/                         # 7 research files + 521 verbatim quotes
│       ├── 01-papers.md
│       ├── 02-talks.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views.md
│       ├── 05-decisions.md
│       ├── 06-timeline.md
│       ├── verbatim-corpus.md
│       └── section-patterns/             # Method / Experiments / Discussion + Expression-DNA structured JSON
├── examples/
│   └── demo-conversation-2026-04-27.md   # 4 worked scenarios + 18 trigger tests
├── scripts/                              # Reproducible ingest pipeline
└── assets/                               # Seed paper IDs + talk URLs
```

---

## Boundaries

- **Knowledge cutoff: 2026-04-27.** The skill cannot speak to Kaiming's unpublished current views. For papers after the cutoff it WebSearches arXiv first and discloses that the answer is formed at read-time.
- **Voice attribution on multi-author papers** (Faster R-CNN, FPN, Focal Loss) is uncertain — those quotes carry `voice_certain: false` and are cited sparingly.
- **Every quote is grounded** to a `(arXiv ID, section)` tag and verified byte-exact by `scripts/verify_quotes.py`.
- **This is a corpus-grounded persona, not Kaiming.** The disclaimer fires once per session. **Do not cite the skill's outputs as Kaiming's actual opinion.**
- **Weak areas.** Optimization theory; NLP, speech, RL — none are in the corpus, and the skill flags this when asked outside its domain.

---

## License

MIT — use, modify, redistribute. Citations to the underlying papers must follow the original authors' conventions.

## Acknowledgements

- Repository structure adapted from [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill).
- Skill specification: [`anthropics/skills`](https://github.com/anthropics/skills).
- All credit for the *ideas* belongs to Kaiming He and his collaborators. This repo is just a structured index.
