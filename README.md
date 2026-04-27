<div align="center">

# kaiming-he-skill

> *"Less is More — Occam's Razor. Future is the Real Test Set."*
> — Kaiming He, NeurIPS 2024 New-in-ML

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.4-brightgreen.svg)](#)
[![Papers Distilled](https://img.shields.io/badge/papers%20distilled-46-orange.svg)](references/research/01-papers.md)
[![Verbatim Quotes](https://img.shields.io/badge/verbatim%20quotes-521-purple.svg)](references/research/verbatim-corpus.md)
[![Cutoff](https://img.shields.io/badge/research%20cutoff-2026--04--27-lightgrey.svg)](#)
[![Built for Claude Code](https://img.shields.io/badge/built%20for-Claude%20Code-black.svg)](https://claude.com/claude-code)

**写完 abstract 心里没底，不知道哪句是废话？**
**看了一晚上 Kaiming 的论文，还是写不出那个 *empirical* 的调调？**

**kaiming-he-skill 把 Kaiming 那套写论文的眼光打包成 Claude Code 里一句话能调出来的工具，让他在你 submit 之前先把 paper 过一遍。**

</div>

---

## ✨ 一行装好

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

装完会把 skill 软链到 `~/.claude/skills/`，然后顺手帮 repo 点个 ⭐（如果你登过 `gh auth`）。不想 star 就 `NO_STAR=1 bash ...`。

---

## 谁需要这个 skill

<table>
<tr>
<td width="33%">

### 🎓 在投顶会的 PhD

abstract 改了三遍，reviewer 还是说「**看不出 contribution**」？

让 skill 跑一遍 12 步 Kaiming-style review，**逐段告诉你哪句是 marketing、哪个 component 该砍、closer 是不是空话**。

> *"投 NeurIPS 前让它扫了一遍 abstract，第二天 reviewer 没再喷我方法写得花哨。"*

</td>
<td width="33%">

### ✍️ 第一次写英文论文的本科 / 硕士

idea 不错，写出来却像翻译腔？老板让你**重写第三遍**了？

skill 给你 four-paragraph intro template + rewrite mode，把「We propose a novel and powerful method」这种句子直接改成 Kaiming 一作论文里的语气。

> *"原来一句『We observe that...』就能让 intro 不再 student-style。"*

</td>
<td width="33%">

### 🔍 想要 design 级品味的 reviewer / 资深研究者

审稿只会挑数字、挑实验细节，提不出 **design-level 意见**？

借 Kaiming 六大 mental model（subtraction / decoupling / duality / pixels-over-tokens / ...）给你的审稿意见做骨架。

> *"审稿意见从『请补充实验』升级到『这个 component 是否经得起 subtraction』。"*

</td>
</tr>
</table>

---

## 它能做什么

| 模式                       | 干什么                                                                                                                                                       | 触发示例                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| 📝 **Review mode**          | 对 abstract / intro / method / ablation / discussion 逐段挑刺：标 marketing 词、找缺失的 *surprising observation*、检查 closer 是不是空话                    | *"review my paper Kaiming-style"*                     |
| ✍️ **Rewrite mode**         | 把营销话术 / 翻译腔的句子重写成 Kaiming 风：删 *novel / powerful / significantly*，插 *we observe*，加 *without bells and whistles*                          | *"rewrite this paragraph in Kaiming's voice"*         |
| 🔬 **Ablation Tutor**       | 设计 gray-shaded、one-variable-at-a-time 的 Kaiming 式 ablation 表，sub-caption 写成 declarative finding（*"Normalized pixels are simple and effective."*）  | *"design my ablation table"*                          |
| 🪒 **Subtraction audit**    | 给 method 做组件级减法：哪个 component 是 load-bearing？哪三个该被降级到 §3？                                                                                | *"is this method too complex?"*                       |
| 🎓 **Mental-model routing** | 把任意 design 问题路由到 Kaiming 六大 mental model 之一，并以 in-voice 方式回答                                                                              | *"what would Kaiming say about adding gates here?"*   |

> 不是改字 —— 它在帮你找**「没写出来的那句话」和「不该写的那一句话」**。

---

## 数据源

每条建议背后都有可追溯的来源，**不是我凭印象编的**：

| 来源                       | 覆盖范围                                                                                          | 数量                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 📄 **一作 / 末作论文**       | ResNet, Mask R-CNN, MoCo, MAE, l-DAE, MAR, MeanFlow, JiT 等                                       | **46 篇 corpus，26 篇深度蒸馏**         |
| 🎤 **Talks / 演讲**         | NeurIPS 2024 New-in-ML, CVPR 2025, NeurIPS 2025 Test-of-Time, MIT 6.S978, ECCV / CVPR / ICCV tutorials | 7 套 slides + 2 个 YouTube tutorial   |
| 💬 **Verbatim 引用库**       | 每条 quote 带 (arXiv ID, section) tag，byte-exact grep 校验                                       | **521 条**，467 条 voice-certain      |
| 🧬 **Section patterns**    | Method / Experiments / Discussion / Limitations / Conclusion 的写作模板                            | 4 个结构化 JSON                       |
| 🔤 **Expression DNA**      | sentence templates / opener / transition / closer / vocabulary 频次表                              | 16 + 10 + 8 + 6 + 22 项               |

> **绝不幻觉** —— 每条 quote 都能 grep 回 `text/papers/{id}.md` 的某一行。`scripts/verify_quotes.py` 是 commit 前的 gating，过不了不让 push。

---

## 🔌 怎么用

装好之后，在 Claude Code 里直接打这些就能触发：

| 你打这句                                          | skill 做什么                       |
| ------------------------------------------------- | ---------------------------------- |
| *"review my paper Kaiming-style"*                 | §15.A 12 步 per-section review     |
| *"rewrite this paragraph in Kaiming's voice"*     | §15.B rewrite mode                 |
| *"design my ablation table"*                      | §14 ablation tutor                 |
| *"is this method too complex?"*                   | Subtraction over Addition          |
| *"what would Kaiming say about X?"*               | Mental-model routing               |
| *"strip the marketing language from my intro"*    | Rewrite mode                       |
| *"challenge the inherited default"*               | Observation Precedes Formalism     |

要 review 整篇论文：直接把 arXiv 链接或 PDF 路径甩进去，Claude Code 自带的 `Read` / `WebFetch` 会处理。

---

## 📁 仓库结构

```
SKILL.md                            可安装的 skill 主体（13 节 + Ablation Tutor + Review / Rewrite）
install.sh                          一行安装脚本（软链 + ⭐ star）
references/research/
  ├── 01-papers.md                  46 篇 corpus 索引 + 每篇的 design 笔记
  ├── 02-talks.md                   slides + YouTube tutorials
  ├── 03-expression-dna.md          句式模板、intro 模板、ablation 表规范
  ├── 04-external-views.md          社区评论
  ├── 05-decisions.md               MSRA → FAIR → MIT 的几次转向
  ├── 06-timeline.md                1984– 时间线 + 学术谱系
  ├── verbatim-corpus.md            521 条 verbatim quote，每条带 (arXiv ID, section) tag
  └── section-patterns/             Method / Experiments / Discussion / Expression-DNA 的结构化 JSON
examples/                           4 个示例对话 + 18 个触发测试
scripts/                            可复现的 ingest pipeline（arxiv → text → notes → SKILL）
assets/                             seed 论文 ID + 演讲 URL
```

---

## 🔬 自己复现一遍

```bash
pip install arxiv pymupdf4llm beautifulsoup4 lxml requests
brew install yt-dlp
python3 scripts/fetch_arxiv.py                         # html → ar5iv → pdf 三级 cascade
bash    scripts/fetch_talks.sh                         # slide PDF + YouTube 自动字幕
python3 scripts/extract_text.py                        # → text/{papers,talks}/*.md
python3 scripts/build_verbatim_corpus.py               # → verbatim-corpus.md
python3 scripts/verify_quotes.py --strict              # gating，过不了不让 commit
```

完整 DAG 见 [`scripts/README.md`](scripts/README.md)。

---

## ⚖️ 边界 / Honest boundaries

- **知识截止：2026-04-27。** skill 没法替 Kaiming 说他还没发表的看法。
- **多作者论文的语气归属不确定**（Faster R-CNN / FPN / Focal Loss 这类他是中间作者的工作）—— 这些 quote 都打了 `voice_certain: false`，引用克制。
- **每条 quote 都 grep 得回原文**，由 `scripts/verify_quotes.py` 字节级校验。
- **这是 corpus-grounded persona，不是 Kaiming 本人。** disclaimer 在每个 session 的第一次激活时自动出现。**不要把 skill 的话当成 Kaiming 真实观点引用。**

---

## 📜 License

MIT. See [`LICENSE`](LICENSE).

## 🙏 致谢 / Acknowledgements

- 仓库结构参考自 [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill)。
- Skill 规范来自 [`anthropics/skills`](https://github.com/anthropics/skills)。
- 所有 *idea* 的功劳归 Kaiming He 和他的合作者们。这个 repo 只是一个结构化的索引。

---

<div align="center">

**觉得有用就给个 ⭐ 吧 —— 这是我唯一能收到的反馈。**
*If this helped your writing, drop a star — it's the only feedback signal I get.*

[![Star on GitHub](https://img.shields.io/github/stars/shu-king/kaiming-skill?style=social)](https://github.com/shu-king/kaiming-skill/stargazers)

</div>
