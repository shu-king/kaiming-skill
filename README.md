<div align="center">

# kaiming-he-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Papers Distilled](https://img.shields.io/badge/papers%20distilled-46-orange.svg)](references/research/01-papers.md)
[![Verbatim Quotes](https://img.shields.io/badge/verbatim%20quotes-521-purple.svg)](references/research/verbatim-corpus.md)
[![Cutoff](https://img.shields.io/badge/research%20cutoff-2026--04--27-lightgrey.svg)](#)

<br>

**A corpus-based study guide for clean research writing, calibrated claims, and experiment design patterns from Kaiming He's public work.**

<br>

Built from **46 first/last-author papers**, **9 public talks and tutorials**, and **521 verified verbatim quotes**.

Designed for researchers who want concrete references for paper revision, ablation design, baseline comparison, and experiment planning.

<br>

**Keywords**  
`problem framing` · `paper structure` · `abstract revision` · `claim calibration` · `ablation design` · `baseline selection` · `experiment planning` · `writing cleanup`

<br>

[Why](#why-this-repo-exists) · [Who](#who-can-benefit) · [Capabilities](#what-this-repo-can-help-with) · [Limits](#scope-and-limits) · [Install](#install) · [Contents](#whats-included) · [Sources](#sources) · [Star](#star-and-build-note)

</div>

---

<a id="why-this-repo-exists"></a>
## 🎯 Why this repo exists

Many students begin research by reading strong papers, but the useful design choices are often hidden in plain sight: how the paper frames the problem, how the method stays simple, how the experiments are staged, and how the claims avoid over-selling.

Kaiming He's public work is a useful corpus for studying these habits. His papers often show clear problem framing, simple baselines, careful comparisons, and concise writing. This repo collects recurring patterns from that corpus and turns them into notes, checklists, and examples that can be used when drafting or revising a research paper.

The goal is practical. The repo helps users inspect whether a draft has a clear observation, a clean structure, a fair experimental setup, and claims that are supported by evidence.

---

<a id="who-can-benefit"></a>
## 👥 Who can benefit

| User | How this repo helps |
|---|---|
| **Students starting research** | Learn how strong papers frame problems, structure claims, and present experiments. |
| **Early-stage PhD students** | Use checklists to revise abstracts, introductions, method descriptions, and ablations. |
| **Researchers writing a first paper** | Compare a draft against concrete patterns from a strong computer-vision research corpus. |
| **Advisors and mentors** | Use the prompts as teaching material for paper revision and experiment design. |
| **LLM / agent builders** | Use the structured notes as a reference for research-writing review workflows. |

The repo is most useful when the user already has a draft, idea, experiment plan, table, or outline to revise.

---

<a id="what-this-repo-can-help-with"></a>
## 🧰 What this repo can help with

| Keyword | What it helps inspect |
|---|---|
| **Problem framing** | Is the central observation clear before the method is introduced? |
| **Paper structure** | Does the abstract, introduction, method, experiment, and discussion flow logically? |
| **Claim calibration** | Are the claims supported by the actual evidence? |
| **Ablation design** | Does each ablation move one variable at a time and produce an interpretable takeaway? |
| **Baseline selection** | Are the comparisons strong, simple, and relevant? |
| **Experiment planning** | Which experiment should be run first, and which result would actually support the claim? |
| **Writing cleanup** | Can vague adjectives, overloaded sentences, and inflated contribution statements be removed? |
| **Revision workflow** | Can a draft be reviewed as a structured checklist rather than as vague writing feedback? |

Good inputs include:

```text
- a draft abstract
- an introduction outline
- a method description
- an ablation table
- a baseline comparison
- an experiment plan
- a reviewer-response draft
```

Example prompt:

```text
Here is my abstract and ablation plan.
Please review them using the kaiming-he-skill checklist.
Make the claims more precise and suggest missing comparisons.
```

---

<a id="scope-and-limits"></a>
## ⚠️ Scope and limits

Use this repo as a revision aid rather than a source of authority.

Clear limits:

- no claim about Kaiming He's private views or current unpublished opinions;
- no guarantee of technical correctness, paper acceptance, or long-term impact;
- no replacement for advisor feedback, peer review, or domain expertise;
- strongest coverage in computer vision and visual representation learning;
- weaker coverage in optimization theory, NLP, speech, and RL;
- papers or talks after the cutoff date require fresh source lookup.

The skill output should not be cited as Kaiming He's personal opinion.

---

<a id="install"></a>
## 🚀 Install

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

This symlinks the skill into `~/.claude/skills/`.

A complete usage transcript lives at [`examples/demo-conversation-2026-04-27.md`](examples/demo-conversation-2026-04-27.md).

---

<a id="whats-included"></a>
## 📦 What's included

### 5 recurring pattern families

| Pattern | Practical question | Example sources |
|---|---|---|
| **Subtraction over Addition** | Can a component be removed before adding a new one? | ResNet identity shortcut · MAE minimal decoder · SimSiam without momentum |
| **Decouple What Others Coupled** | Are two decisions being bundled together unnecessarily? | Mask R-CNN mask/class heads · MAE asymmetric encoder/decoder |
| **Raw Signal over Engineered Tokens** | Is the representation adding unnecessary assumptions? | MAR · JiT · l-DAE |
| **Long-term Usefulness** | Will the method remain useful beyond the current benchmark cycle? | NeurIPS 2024 New-in-ML talk |
| **Recognition and Generation Together** | Can recognition and generation be studied through the same representation lens? | MAE → MAR → MeanFlow lineage |

### 8 practical checks

1. Before adding a component, ask whether one can be removed.
2. Write the one-line observation behind the method early.
3. Remove vague adjectives such as *novel*, *powerful*, and *significant* unless the evidence supports them.
4. Move one variable at a time in ablations.
5. Keep the abstract short and specific.
6. Predict the experiment outcome before running it.
7. Check whether the method still works after removing tricks.
8. Question inherited defaults instead of copying them automatically.

### Writing patterns

The repo tracks recurring writing patterns such as:

- short declarative sentences;
- observation before mechanism;
- restrained adjectives;
- concise abstracts;
- introduction structure;
- ablation captions written as findings;
- discussion sections that avoid overclaiming.

These patterns are reference material for revision, not fixed rules.

---

<a id="sources"></a>
## 📚 Sources

The research notes live under [`references/research/`](references/research/):

| File | Content | Size |
|---|---|---|
| `01-papers.md` | 46-paper corpus index and per-paper design notes | 5,840 words |
| `02-talks.md` | 9 talks and tutorials with extracted points | 1,988 words |
| `03-expression-dna.md` | Sentence patterns, intro templates, and ablation-table conventions | 2,713 words |
| `04-external-views.md` | Public commentary from adjacent researchers | 1,358 words |
| `05-decisions.md` | Career and research pivots from MSRA to FAIR to MIT | 1,603 words |
| `06-timeline.md` | Biographical timeline and intellectual lineage | 1,174 words |
| `verbatim-corpus.md` | 521 verified quotes grouped by theme | 19,542 words |

### Primary material

The corpus includes:

- 46 arXiv papers fetched through an html → ar5iv → pdf cascade;
- 7 slide decks from `people.csail.mit.edu/kaiming`;
- NeurIPS 2024 New-in-ML talk;
- NeurIPS 2025 Faster R-CNN Test-of-Time talk;
- CVPR 2025 talk on end-to-end generative modeling;
- MIT 6.S978 Deep Generative Models material;
- ECCV, CVPR, and ICCV tutorial videos and captions.

### Secondary material

The secondary material includes public commentary and adjacent work from researchers such as Yann LeCun, Andrej Karpathy, Saining Xie, Xinlei Chen, Tianhong Li, and Mingyang Deng.

Excluded sources:

- Zhihu posts;
- WeChat public-account reposts;
- Baidu Baike;
- marketing rewrites;
- unattributed summaries.

### Verification

Every verbatim quote is grounded to a source tag and checked against the local paper text.

`scripts/verify_quotes.py` is the gating artifact. The verified quotes in `SKILL.md` must match the source text before commit.

---

## 🗂️ Repository layout

```text
kaiming-he-skill/
├── README.md
├── SKILL.md                              # Installable skill body
├── install.sh                            # Symlink install
├── references/
│   └── research/
│       ├── 01-papers.md
│       ├── 02-talks.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views.md
│       ├── 05-decisions.md
│       ├── 06-timeline.md
│       ├── verbatim-corpus.md
│       └── section-patterns/
├── examples/
│   └── demo-conversation-2026-04-27.md
├── scripts/
└── assets/
```

---

<a id="star-and-build-note"></a>
## ⭐ Star

If this repo is useful to you, please consider giving it a ⭐. It helps other students and researchers discover the project, and it gives the maintainer strong motivation to keep improving it.

---

## License

MIT — use, modify, and redistribute.

Citations to the underlying papers should follow the original authors' conventions.

---

## Acknowledgements
- This repo was mainly built with Claude Code.
- Repository structure adapted from [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill).
- Skill specification: [`anthropics/skills`](https://github.com/anthropics/skills).
- All credit for the original research ideas belongs to Kaiming He and his collaborators.
