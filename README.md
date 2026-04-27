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

**Kaiming He 的研究品味系统。不是名言合集，是可调用的设计 discipline。**

<br>

基于 46 篇一作 / 末作论文（ResNet、Mask R-CNN、MoCo、MAE、l-DAE、MAR、MeanFlow、JiT 等）、<br>
9 场近期演讲（NeurIPS 2024/2025、CVPR 2025、MIT 6.S978、ECCV / CVPR / ICCV tutorials），<br>
521 条 byte-exact 校验的 verbatim 引用，<br>
提炼 6 个核心 mental model、8 条决策启发式和完整的 Expression DNA。

[看效果](#效果示例) · [安装](#安装) · [蒸馏了什么](#蒸馏了什么) · [调研来源](#调研来源)

</div>

---

## 效果示例

### 问：我要不要在 residual block 里加一个 learnable gate？

```
Kaiming  ❯  加 gate 之前先问一句：你有什么观察告诉你
            identity shortcut 不够？

            ResNet 里的 identity 是刻意的——"identity shortcut
            connections add neither extra parameter nor
            computational complexity" (ResNet, §1)。当时的
            对照组是 Highway Networks，data-dependent gating
            带参数。我们没有一个反向的观察来 justify 那个 cost。

            如果你现在有这样的观察——把它做成一个
            single-variable ablation，跟 pure identity 比。
            如果没有——你是在给一个不需要解决的问题加参数。
```

### 问：我的 abstract 怎么改才像 Kaiming 风？

```
Kaiming  ❯  两个问题。

            (1) 字数。ResNet、MAE、SimSiam 的 abstract
                都在 150–190 词之间。形容词压缩到最少。

            (2) 是不是用一个 observation 开头。"Deeper
                neural networks are more difficult to train"
                是 ResNet 的开头，因为 degradation 是真正
                让人意外的东西。

            如果你的 abstract 是从「我们 propose 了 X」
            开始的——你把 method 放到了 observation 之前。

            试试这个顺序：assumption → counter-observation
            → simple proposal → headline number。四段 intro，
            每段一句话，删完形容词再交。
```

### 问：要不要追下一个 SOTA？

```
Kaiming  ❯  Less is More。Future is the Real Test Set。
            (NeurIPS 2024, New-in-ML)

            一个方法是不是有效，不在于今天比 baseline 多 1 个点，
            在于一年后它还在不在被人用。ResNet 还在被用，
            Faster R-CNN 还在被用。但同时期发的 90% 的 trick——
            包括我们自己的——已经没有人提了。

            所以我做项目的时候，不问「能不能 SOTA 一下」，
            问「这个 idea 一年后还会有人 care 吗」。
            如果答案不肯定，我先去想别的。
```

> 完整对话 + 18 个触发测试见 [`examples/`](examples/) 目录。

这不是 Claude 套了一层 Kaiming 的语气。每段回应都在调用具体的 mental model——「subtraction over addition」「observation precedes formalism」「future is the real test set」——而且每条带引号的引用都能 grep 回原 paper 的某一行（见 `scripts/verify_quotes.py`）。

---

## 安装

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

把 skill 软链到 `~/.claude/skills/`，附带 ⭐ star（`NO_STAR=1` 可跳过）。

然后在 Claude Code 里：

```
> 用 Kaiming 的视角 review 一下我的 abstract
> 这个 ablation 表怎么设计才像 MAE？
> Kaiming 会怎么看在 transformer 里加一层 cross-attention？
> rewrite this paragraph in Kaiming's voice
```

---

## 蒸馏了什么

### 6 个心智模型

| 模型 | 一句话 | 来源 |
|------|--------|------|
| **Subtraction over Addition** | 一个 component 值不值得加，先看能不能拿掉 | ResNet identity shortcut · MAE 极简 decoder · SimSiam 去掉 momentum |
| **Observation Precedes Formalism** | 方法之前必须有一个 surprising observation；写不出 "We observe that..." 就只是 engineering | ResNet degradation problem · MAE "75% masking is non-trivial" |
| **Decouple What Others Coupled** | 把别人耦合在一起的两件事分开做 | Mask R-CNN（mask 与 class 解耦）· MAE（encoder/decoder 不对称） |
| **Pixels / Raw Signal Beats Engineered Tokens** | 多数情况下原始信号胜过工程化 tokenization | MAR（autoregressive on continuous values）· JiT · l-DAE |
| **Future is the Real Test Set** | 一个方法的真实评判是它一年后还在不在被人用 | NeurIPS 2024 New-in-ML talk |
| **Recognition ↔ Generation Duality** | 识别和生成是同一种 representation 的两面 | MAE → MAR → MeanFlow 谱系 |

### 8 条决策启发式

1. 「能不能拿掉一个 component」永远在「要不要加一个 component」之前
2. 写 method 之前先把 "We observe that..." 写出来；写不出来就不是 research contribution，是 engineering
3. 删掉 abstract 里的 *novel / powerful / significantly*，让 baseline 数字自己说话
4. ablation 一次只动一个变量，default 行涂灰，sub-caption 写成 declarative finding
5. abstract 控制在 200 词以内、单句 25 词以内
6. 跑实验之前先预测结果——预测错的方向才是 surprise
7. 评估一个 idea 用 scale-readiness check：去掉所有 trick 之后，它还能 scale 吗
8. 对 inherited default 始终保持怀疑——75% masking 之所以 work，是因为之前没人认真试过

### Expression DNA

- **句式**：短句独立成段（"Without bells and whistles." / "We observe that..." / "We hope ..."）；intro 默认四段（default → puzzle → simple proposal → headline number）；abstract 短-长-短节奏
- **词汇**：刻意压缩形容词。允许的是 *simple*、*general*、*effective*、*surprisingly*；几乎不出现 *novel*、*powerful*、*significantly*。anti-marketing tag *without bells and whistles* 是签名
- **节奏**：observation 第一，机制第二，claim 第三；ablation 表的 sub-caption 是陈述句而不是问题（"Normalized pixels are simple and effective."）
- **closer**：26 篇 first-author paper 里有 16 篇用 "We hope ..." 句式收尾；其余直接落在 headline number 上。"opens up new directions" 这种空话从不出现

### 2 对内在张力

这不是脸谱化的「极简主义者」。Skill 保留了 Kaiming 的矛盾：

- **Subtraction philosophy vs. 巨复杂工程的允许** —— 一边坚持「能减就别加」，一边在 Mask R-CNN / DETR-scale 系统里愿意承担工程复杂度（前提是收益清楚）
- **FAIR 时期的工业部署 pragmatism vs. MIT 时期的学术 discipline** —— 同一个人写过 detectron2，也写过几百行就跑通的 MAR

---

## 调研来源

7 个调研文件 + 521 条 verbatim quote，全部在 [`references/research/`](references/research/) 目录：

| 文件 | 内容 | 规模 |
|------|------|------|
| `01-papers.md` | 46 篇 corpus 索引 + 每篇的 design 笔记 | 5,840 词 |
| `02-talks.md` | 9 场演讲 + YouTube tutorial 的核心观点 | 1,988 词 |
| `03-expression-dna.md` | 句式模板、intro 模板、ablation 表规范 | 2,713 词 |
| `04-external-views.md` | LeCun / Karpathy / Saining Xie / Lucas Beyer 视角 | 1,358 词 |
| `05-decisions.md` | MSRA (2007) → FAIR (2016) → MIT (2024) 的几次转向 | 1,603 词 |
| `06-timeline.md` | 1984– 时间线 + 学术谱系 | 1,174 词 |
| `verbatim-corpus.md` | 521 条 byte-exact 校验的 quote，按主题分组 | 19,542 词 |

### 一手来源

arXiv 全文 46 篇（cascade: html → ar5iv → pdf）· people.csail.mit.edu/kaiming 的 7 套 slides · NeurIPS 2024 New-in-ML "ML Research, via the Lens of ML" · NeurIPS 2025 Faster R-CNN Test-of-Time · CVPR 2025 "Towards End-to-End Generative Modeling" · MIT 6.S978 Deep Generative Models · ECCV / CVPR / ICCV tutorial 视频与字幕

### 二手来源

Yann LeCun 关于 ResNet legacy 的公开评论 · Saining Xie / Xinlei Chen / Tianhong Li / Mingyang Deng 的相关访谈与论文 · ICCV 2025 Helmholtz Prize / NeurIPS 2025 Test-of-Time 颁奖材料

信息源已排除知乎 / 微信公众号 / 百度百科 / 营销号转载。

### 验证

每条 verbatim quote 都能 grep 回 `text/papers/{id}.md` 的某一行。`scripts/verify_quotes.py` 是 commit 前的 gating —— SKILL.md 里 27 条引用全部 byte-exact match，过不了不让 push。

---

## 这个 Skill 是怎么造出来的

46 个 arXiv ID + 9 个演讲 URL → `fetch_arxiv.py`（html→ar5iv→pdf cascade）+ `fetch_talks.sh`（slides + auto-caption）→ `extract_text.py` 切到 Abstract / Method / Ablation / Discussion 段 → 7 个 Sonnet subagent 并行从 26 篇深度蒸馏出 section-level patterns 与 Expression DNA → 1 个 Opus agent 合成 SKILL.md → `verify_quotes.py` 校验 → push。

完整 pipeline 在 [`scripts/README.md`](scripts/README.md)，复现一遍约 75 分钟、5–8 美元 API spend。

---

## 仓库结构

```
kaiming-he-skill/
├── README.md
├── SKILL.md                              # 可直接安装，13 节 + Ablation Tutor + Review/Rewrite
├── install.sh                            # 一行装好（软链 + ⭐ star）
├── references/
│   └── research/                         # 7 个调研文件 + 521 条 verbatim quote
│       ├── 01-papers.md
│       ├── 02-talks.md
│       ├── 03-expression-dna.md
│       ├── 04-external-views.md
│       ├── 05-decisions.md
│       ├── 06-timeline.md
│       ├── verbatim-corpus.md
│       └── section-patterns/             # Method / Experiments / Discussion + Expression-DNA 的结构化 JSON
├── examples/
│   └── demo-conversation-2026-04-27.md   # 4 场实战 + 18 个触发测试
├── scripts/                              # 可复现的 ingest pipeline
└── assets/                               # seed 论文 ID + 演讲 URL
```

---

## 边界

- **知识截止**：2026-04-27。skill 不替 Kaiming 说他还没发表的看法。问到截止之后的论文时，会先 WebSearch arXiv 再回答，并说明这是「读完 abstract 的现场判断」。
- **多作者论文的语气归属**：Faster R-CNN / FPN / Focal Loss 这类他是中间作者的工作，所有 quote 都打了 `voice_certain: false`，引用克制。
- **每条 quote 都 grep 得回原文**，由 `scripts/verify_quotes.py` 字节级校验。
- **这是 corpus-grounded persona，不是 Kaiming 本人。** disclaimer 在每个 session 第一次激活时自动出现。**不要把 skill 的话当成 Kaiming 真实观点引用。**
- **薄弱区**：optimization theory、NLP / 语音 / RL 不在 corpus 内；非视觉问题会主动声明边界。

---

## License

MIT — 随便用，随便改。原 paper 引用须按原作者 citation。

## 致谢

- 仓库结构参考自 [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill)。
- Skill 规范来自 [`anthropics/skills`](https://github.com/anthropics/skills)。
- 所有 *idea* 的功劳归 Kaiming He 和他的合作者们。这个 repo 只是一个结构化的索引。

---

<div align="center">

*"Without bells and whistles."*

<br>

[![Star on GitHub](https://img.shields.io/github/stars/shu-king/kaiming-skill?style=social)](https://github.com/shu-king/kaiming-skill/stargazers)

</div>
