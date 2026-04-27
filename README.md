<div align="center">

# kaiming-he-skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Papers Distilled](https://img.shields.io/badge/papers%20distilled-46-orange.svg)](references/research/01-papers.md)
[![Verbatim Quotes](https://img.shields.io/badge/verbatim%20quotes-521-purple.svg)](references/research/verbatim-corpus.md)
[![Cutoff](https://img.shields.io/badge/research%20cutoff-2026--04--27-lightgrey.svg)](#)

<br>

**A study guide for clean research writing, restrained claims, and experiment design patterns from Kaiming He's public work.**

<br>

Built from 46 first/last-author papers, 9 public talks and tutorials, and 521 verified verbatim quotes.

The repo organizes recurring patterns in problem framing, paper structure, ablation design, baseline comparison, and research writing into practical notes and checklists for students and early-stage researchers.

[Install](#install) · [Who can benefit](#who-can-benefit) · [What this repo can do](#what-this-repo-can-do) · [What's included](#whats-included) · [Sources](#sources)

</div>

---

## Motivation

Many students begin research by reading strong papers, but the useful design choices are often hidden in plain sight: how the paper frames the problem, how the method stays simple, how the experiments are staged, and how the claims avoid over-selling.

Kaiming He's public work is a useful corpus for studying these habits. His papers often show clear problem framing, simple baselines, careful comparisons, and concise writing. This repo collects recurring patterns from that corpus and turns them into notes, checklists, and examples that can be used when drafting or revising a research paper.

The goal is practical. The repo helps users inspect whether a draft has a clear observation, a clean structure, a fair experimental setup, and claims that are supported by evidence.

---

## Who can benefit

This repo is mainly useful for people who are learning how to turn research ideas into clear papers and convincing experiments.

| User | How this repo helps |
|---|---|
| **Students starting research** | Learn how strong papers frame problems, introduce methods, and avoid unnecessary claims. |
| **Early-stage PhD students** | Use the checklists to revise abstracts, introductions, ablations, and experiment plans. |
| **Researchers writing a first paper** | Compare a draft against concrete patterns from a strong computer-vision research corpus. |
| **Advisors and mentors** | Use the prompts and checklists as teaching material for paper revision and experiment design. |
| **LLM / agent builders** | Use the structured notes as a reference for research-writing review tools. |

The repo is most helpful when the user already has a draft, idea, experiment plan, or paper section to revise.

---

## What this repo can do

**Keywords:** `problem framing` · `paper structure` · `abstract revision` · `claim calibration` · `ablation design` · `baseline selection` · `experiment planning` · `writing cleanup` · `overclaim removal`

| Task | What the repo provides |
|---|---|
| **Clarify the core idea** | Helps turn a vague motivation into a specific observation, question, or hypothesis. |
| **Improve paper structure** | Provides patterns for abstracts, introductions, method sections, experiments, and discussions. |
| **Reduce overclaiming** | Flags inflated wording and suggests more precise, evidence-backed claims. |
| **Plan cleaner experiments** | Encourages one-variable-at-a-time ablations, stronger baselines, and clearer comparisons. |
| **Review ablation tables** | Helps make ablation rows, captions, and takeaways easier to interpret. |
| **Check baseline fairness** | Prompts users to ask whether the comparison is strong, simple, and relevant. |
| **Study writing style** | Extracts recurring sentence patterns, vocabulary choices, and section-level structure from the corpus. |
| **Support revision workflows** | Works as a second reader for drafts, rebuttals, experiment plans, and paper outlines. |

A good use case looks like this:

```text
Here is my abstract / introduction / ablation plan.
Please review it using the kaiming-he-skill checklist.
Make the claims more precise and suggest missing experiments.
```

---

## Install

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

This symlinks the skill into `~/.claude/skills/`.

A complete usage transcript lives at [`examples/demo-conversation-2026-04-27.md`](examples/demo-conversation-2026-04-27.md).

---

## How to use it well

The repo works best as a revision aid. It is meant to support thinking, not replace it.

Use it with concrete material:

- a draft abstract;
- an introduction outline;
- a method description;
- an ablation table;
- a baseline comparison;
- an experiment plan;
- a reviewer-response draft.

The more specific the input, the more useful the feedback.

---

## Clear limits

This repo has clear limits:

- it cannot judge whether a research idea is important;
- it cannot guarantee technical correctness;
- it cannot predict paper acceptance or long-term impact;
- it cannot replace advisor feedback, peer review, or domain expertise;
- it should not be cited as Kaiming He's personal opinion;
- it is strongest for computer vision and visual representation learning;
- it is weaker for optimization theory, NLP, speech, and RL.

For papers or talks after the cutoff date, the skill should search for current sources and disclose that the answer is formed at read time.

---

## What's included

### 5 recurring research patterns

| Pattern | Practical question | Example sources |
|---|---|---|
| **Subtraction over Addition** | Can a component be removed before adding a new one? | ResNet identity shortcut · MAE minimal decoder · SimSiam without momentum |
| **Decouple What Others Coupled** | Are two decisions being bundled together unnecessarily? | Mask R-CNN mask/class heads · MAE asymmetric encoder/decoder |
| **Raw Signal over Engineered Tokens** | Is the representation adding unnecessary assumptions? | MAR · JiT · l-DAE |
| **Future Use as a Test** | Will the method still be useful after the current benchmark cycle? | NeurIPS 2024 New-in-ML talk |
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

The repo also tracks recurring writing patterns:

- short declarative sentences;
- observation before mechanism;
- restrained adjectives;
- concise abstracts;
- introduction structure;
- ablation table captions written as findings;
- discussion sections that avoid overclaiming.

These patterns are meant as reference material for revision, not fixed rules.

---

## Sources

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

### Primary sources

The corpus includes:

- 46 arXiv papers fetched through an html → ar5iv → pdf cascade;
- 7 slide decks from `people.csail.mit.edu/kaiming`;
- NeurIPS 2024 New-in-ML talk;
- NeurIPS 2025 Faster R-CNN Test-of-Time talk;
- CVPR 2025 talk on end-to-end generative modeling;
- MIT 6.S978 Deep Generative Models material;
- ECCV, CVPR, and ICCV tutorial videos and captions.

### Secondary sources

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

## Repository layout

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

## Use cases

### Paper revision

Use the skill to review:

- abstract structure;
- introduction flow;
- claim strength;
- ablation design;
- baseline choice;
- discussion wording.

### Experiment planning

Use the skill to ask:

- What is the simplest baseline?
- Which component should be ablated first?
- What inherited default should be questioned?
- Which result would actually support the claim?
- Which comparison would make the paper more convincing?

### Writing cleanup

Use the skill to reduce:

- inflated adjectives;
- unclear motivation;
- vague contribution statements;
- overloaded introductions;
- unsupported claims.

---

## License

MIT — use, modify, and redistribute.

Citations to the underlying papers should follow the original authors' conventions.

---

## Acknowledgements

- Repository structure adapted from [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill).
- Skill specification: [`anthropics/skills`](https://github.com/anthropics/skills).
- All credit for the original research ideas belongs to Kaiming He and his collaborators.
