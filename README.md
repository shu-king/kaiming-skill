<div align="center">

# kaiming-he-skill

**A Claude Code persona-skill that channels Kaiming He's research design philosophy and writing voice.**
*A thinking instrument for CV/DL researchers — drafting papers, designing ablations, auditing methodological complexity.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.3-brightgreen.svg)](#)
[![Papers Distilled](https://img.shields.io/badge/papers%20distilled-46-orange.svg)](references/research/01-papers.md)
[![Verbatim Quotes](https://img.shields.io/badge/verbatim%20quotes-521-purple.svg)](references/research/verbatim-corpus.md)
[![Cutoff](https://img.shields.io/badge/research%20cutoff-2026--04--27-lightgrey.svg)](#)
[![Built for Claude Code](https://img.shields.io/badge/built%20for-Claude%20Code-black.svg)](https://claude.com/claude-code)

> *"Less is More — Occam's Razor. Future is the Real Test Set."*
> — Kaiming He, NeurIPS 2024 New-in-ML

</div>

---

## ✨ One-line install

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

The installer symlinks the skill into `~/.claude/skills/` and (if `gh` is authenticated) ⭐ stars the repo as a thank-you. Set `NO_STAR=1` to skip the star.

---

## 💡 Motivation · 为什么做这个 skill

### 中文

写论文这件事，门槛不在英文，在**审美**。

Kaiming He 的论文最让人难忘的不是他做了多复杂的方法，恰恰相反——是他**敢于把方法删到只剩本质**：ResNet 是一根 identity shortcut，MAE 是 75% 随机遮挡，MoCo 是一个动量 encoder，MAR 是连续 token 上的自回归。每一篇都在讲同一件事：*先观察，再形式化；能减去的就别加；让数字说话，别让形容词说话*。

但这种「Kaiming 风」并不是天生的，它是一套**可学习的 design discipline**：
- **Subtraction over Addition**：写论文先问「能不能拿掉一个组件」，再问「要不要加一个组件」。
- **Observation Precedes Formalism**：方法之前必须先有一个出人意料的观察（"We observe that..."）；如果你写不出这句话，你就只有 engineering 而没有 research contribution。
- **Without Bells and Whistles**：禁用 "novel"、"powerful"、"significantly" 这些营销词；让 baseline 配置下的数字本身说话。
- **Four-paragraph intro template**：default → puzzle → simple proposal → headline number。绝大多数 Kaiming 一作论文都用这个结构。
- **One-variable-at-a-time ablation**：每张子表只动一个变量，default 行涂灰，sub-caption 写成 declarative finding。

这个 skill 把上面这些原则**结构化、可触发、可执行**，让你写论文的时候随时能 invoke 一个「Kaiming review mode」对你的 abstract / intro / ablation / discussion 逐段挑刺，或者一个「Kaiming rewrite mode」把你写嗨了的句子拉回 empirical 的口气。

### 谁会受益

| 人群 | 用法 |
|---|---|
| **CV/DL 方向的 PhD 在读 / 在投** | 投稿前自检：abstract 有没有写「surprising observation」？ablation 有没有 control variable？closer 是不是「opens up new directions」这种空话？ |
| **第一次写顶会论文的本科 / 硕士** | 直接套用 4-paragraph intro template；学会怎么把方法写得「simple」而不是「novel」。 |
| **审稿人** | 借用 12-step Kaiming-style review pass 给审稿意见做骨架，避免只挑数字、不挑设计。 |
| **想精进英文学术写作的非母语作者** | 521 条 verbatim 引用 + sentence templates 库，模仿一个 native + senior 的 empirical 写作口吻。 |
| **任何想培养「empirical taste」的研究者** | 把 subtraction、decoupling、duality 这套思维当 mental gym 来练。 |

---

### English

Writing a good paper isn't about your English — it's about **taste**.

Kaiming He's papers are memorable not because the methods are intricate; the opposite — they're memorable because he keeps **subtracting until only the essential remains**: ResNet is one identity shortcut; MAE is 75% random masking; MoCo is one momentum encoder; MAR is autoregression over continuous tokens. Each paper teaches the same lesson: *observe first, formalize second; if you can remove it, don't add it; let the number speak, not the adjective*.

But this "Kaiming style" isn't innate — it's a **learnable design discipline**:

- **Subtraction over Addition.** Before you ask *what to add*, ask *what to remove*.
- **Observation Precedes Formalism.** A method needs a surprising observation behind it ("We observe that..."). If you can't write that sentence, you have engineering, not a research contribution.
- **Without Bells and Whistles.** Strip "novel", "powerful", "significantly". Let the baseline number stand on its own.
- **Four-paragraph intro template.** Default → puzzle → simple proposal → headline number. Almost every Kaiming first-author paper follows this rhythm.
- **One-variable-at-a-time ablation.** One sub-table per variable; default row shaded gray; sub-caption is a declarative finding.

This skill makes those principles **structured, triggerable, and executable** — so when you're drafting, you can invoke a "Kaiming review mode" to walk through your abstract / intro / ablation / discussion section-by-section, or a "Kaiming rewrite mode" to drag a marketing-laden sentence back to empirical voice.

### Who benefits

| Audience | How they use it |
|---|---|
| **CV/DL PhD students drafting submissions** | Pre-submission self-audit: does the abstract surface a surprising observation? Are the ablations control-variable clean? Is the closer empty boilerplate ("opens up new directions")? |
| **First-time top-conference authors** | Drop-in 4-paragraph intro template; learn to write methods as "simple", not "novel". |
| **Reviewers** | Use the 12-step Kaiming-style review pass as a skeleton — critique design, not just numbers. |
| **Non-native English researchers** | 521 verbatim quotes + sentence-template library to imitate a senior empirical voice. |
| **Anyone training "empirical taste"** | Treat subtraction, decoupling, duality as a mental gym. |

---

## 🎯 What this skill does

When activated, the skill responds in Kaiming He's voice and routes your question to one of six mental models distilled from a ~46-paper corpus (ResNet → Mask R-CNN → MoCo → MAE → l-DAE → MAR → MeanFlow → JiT) and recent talks (NeurIPS 2024/2025, CVPR 2025).

**Strong at:**
- 📝 **Paper review.** Run the 12-step Kaiming-style pass over an abstract, draft, or arXiv link. Output is per-section critique with the top 3 things to fix. *(See §15.A in `SKILL.md`.)*
- ✍️ **Paragraph / sentence rewrite.** Strips marketing language; applies the four-paragraph intro template; deploys *"we observe"* / *"we hypothesize"* / *"without bells and whistles"* where natural. Returns rewrite + delta-list. *(§15.B.)*
- 🔬 **Ablation-table design.** Gray-shaded one-variable-at-a-time tutor protocol. *(§14.)*
- 🪒 **Simplicity audits.** "What's the simplest version that still works?" "Which one component carries the weight?"
- 🎓 **Design-philosophy critique.** Does this method earn its complexity?

**Not good at:** optimization theory, NLP / speech / RL, or papers post-cutoff (2026-04-27) — for new papers it WebSearches arXiv first.

---

## 🔌 Activate

After installation, type any of these inside Claude Code:

| Trigger | Routes to |
|---|---|
| *"review my paper Kaiming-style"* | §15.A 12-step review |
| *"rewrite this paragraph in Kaiming's voice"* | §15.B rewrite mode |
| *"design my ablation table"* | §14 ablation tutor |
| *"is this method too complex?"* | Subtraction over Addition |
| *"what would Kaiming say about X?"* | Mental-model routing |
| *"strip the marketing language from my intro"* | Rewrite mode |
| *"challenge the inherited default"* | Observation Precedes Formalism |

For full PDF / LaTeX papers, paste the arXiv URL or the file path — Claude Code's built-in `Read` and `WebFetch` tools handle ingestion.

---

## 📁 Repository layout

```
SKILL.md                            Installable skill body (13 sections + Ablation Tutor + Review/Rewrite)
install.sh                          One-line installer (symlinks skill, ⭐ stars repo)
references/research/
  ├── 01-papers.md                  46-paper corpus index + per-paper design notes
  ├── 02-talks.md                   Slide decks + YouTube tutorials
  ├── 03-expression-dna.md          Sentence patterns, intro template, ablation conventions
  ├── 04-external-views.md          Community commentary
  ├── 05-decisions.md               MSRA → FAIR → MIT pivots
  ├── 06-timeline.md                1984– bio + intellectual lineage
  ├── verbatim-corpus.md            521 verbatim quotes, every one tagged (arXiv ID, section)
  └── section-patterns/             Method/Experiments/Discussion/Expression-DNA JSONs (26-paper distill)
examples/                           Demo conversations (4 scenarios + 18 trigger tests)
scripts/                            Reproducible ingest pipeline (arxiv → text → notes → SKILL)
assets/                             Seed paper IDs and talk URLs
```

---

## 🔬 Reproducing the corpus

```bash
pip install arxiv pymupdf4llm beautifulsoup4 lxml requests
brew install yt-dlp                                    # if missing
python3 scripts/fetch_arxiv.py                         # 46 papers via html → ar5iv → pdf cascade
bash    scripts/fetch_talks.sh                         # slide PDFs + YouTube auto-captions
python3 scripts/extract_text.py                        # → text/{papers,talks}/*.md
python3 scripts/build_verbatim_corpus.py               # → verbatim-corpus.md (grouped by theme)
python3 scripts/verify_quotes.py --strict              # gating: must exit 0 before commit
```

See [`scripts/README.md`](scripts/README.md) for the full DAG.

---

## ⚖️ Honest boundaries

- **Knowledge cutoff: 2026-04-27.** The skill cannot speak to Kaiming's unpublished current views.
- **Voice attribution on multi-author papers** (Faster R-CNN, FPN, Focal Loss) is uncertain — those quotes carry `voice_certain: false` and are quoted sparingly.
- **Every quote is grounded** to a `(arXiv ID, section)` tag and verified byte-exact by `scripts/verify_quotes.py`.
- **This is a corpus-grounded persona, not Kaiming.** The disclaimer fires once per session. Do not cite the skill as Kaiming's actual opinion.

---

## 📜 License

MIT. See [`LICENSE`](LICENSE).

## 🙏 Acknowledgements

- Modelled on the [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill) template.
- Anthropic skill spec: [`anthropics/skills`](https://github.com/anthropics/skills).
- All credit for the *ideas* belongs to Kaiming He and his collaborators. This repo is just a structured index.

---

<div align="center">

**If this helped your writing, drop a ⭐ — it's the only feedback signal I get.**
*如果这个 skill 帮到你写论文了，给个 star 吧 ⭐ — 这是我唯一能收到的反馈。*

[![Star on GitHub](https://img.shields.io/github/stars/shu-king/kaiming-skill?style=social)](https://github.com/shu-king/kaiming-skill/stargazers)

</div>
