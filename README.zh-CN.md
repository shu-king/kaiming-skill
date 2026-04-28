<div align="center">

# kaiming-he-skill

[English](README.md) · 简体中文

<br>

**一个基于 Kaiming He 公开论文、公开演讲和教程整理出来的研究写作参考 skill。**

<br>

这是一个基于Kaiming He的公开论文和演讲语料整理出来的的写作skill，它可以帮你检查你论文的每个子模块是否符合kaiming的科研写作理念然后给出初步审稿意见，并提供kaiming-style rewrite的版本。

<br>

基于 **46 篇论文（重点覆盖一作/末作工作）**、**9 个公开 talks / tutorials**，以及 **519 条按主题整理的原文摘录参考语料**。`SKILL.md` 里直接使用的 quote 已经用本地原始文本做过验证。

<br>

[为什么需要这个skill](#为什么需要这个skill) · [适用人群](#适用人群) · [它能做什么](#它能做什么) · [限制](#限制) · [安装](#安装) · [资料来源](#资料来源)

</div>

---

## 为什么需要这个skill

作为科研刚起步的研究生，我们的论文写作很多时候可能会面临无人指导的情况。有些老师会默认这些东西我们本来就会，或者期望我们自学成才，但是其实很多时候我们就像无头苍蝇一样，没有清晰的方向来指导自己的写作。个人认为kaiming在DL/CV领域是一个很好的学习对象，虽然我们无法拥有kaiming的最强大脑，但是我们可以从他paper的字里行间里感受到他优雅的科研理念，以及明晰的写作风格。所以我让claude学习了kaiming近50篇重要的paper来学习他的写作pattern，来帮助我们理清文章结构、逻辑，以及如何让每个句子表达更清晰、更reader friendly。

---

## 适用人群

这个 repo 比较适合：

- 刚开始做研究、想学强论文怎么组织问题的学生；
- 正在写第一篇 paper 的 PhD / master 学生；
- 需要改 abstract、intro、method 或 ablation table 的研究人员；
- 想把 review 变得更具体的 mentor / advisor；
- 想做 research-writing agent 的 LLM / agent builder。

它所擅长的场景不是从0生成一个idea，而是当你已经有一个初稿、想法、实验计划、表格或审稿回复，需要一个更具体的检查框架的情况。

---

## 它能做什么

它主要帮你检查这些问题：

| 方向 | 具体会看什么 |
|---|---|
| 问题定义 | 核心 observation 是否先于方法出现？ |
| 论文结构 | abstract、intro、method、experiments 是否顺着一个清楚的逻辑展开？ |
| claim 校准 | 结论有没有数据支持，有没有过度包装？ |
| ablation 设计 | 是否一次只改变一个变量，结果是否能解释？ |
| baseline 选择 | 对比对象是否简单、强、相关？ |
| 实验计划 | 哪个实验应该先做，哪个结果才能真正支撑 claim？ |
| 写作清理 | 是否能删掉空泛形容词、过长句子和夸大的 contribution？ |

你可以这样问：

```text
这是我的 abstract 和 ablation plan。
请用 kaiming-he-skill 的 checklist 帮我 review 一下。
重点看 claim 是否过度、实验是否缺少关键对比。
```

也可以这样问：

```text
请把这段 introduction 改得更 Kaiming-style：
更短，更清楚，先讲 observation，再讲方法。
```

---

## 限制

请把它当作论文修改辅助，而不是权威。

几个明确边界：

- 它不代表 Kaiming He 本人的观点；
- 它不应该被引用为 Kaiming He 的个人意见；
- 它不能保证技术正确、论文录用或长期影响力；
- 它不能替代 advisor、peer review 或领域专家判断；
- 最擅长的领域是 computer vision 和 visual representation learning；
- 对 optimization theory、NLP、speech、RL 等方向覆盖力较弱；
- cutoff 之后的新论文或新 talk 需要重新查源再判断。

如果问题涉及私人动机、行业判断、对某个人的看法，skill 应该保持沉默，或者明确标注“这是从公开语料推出来的保守解释，不是 quote，也不是本人观点”。

---

## 安装

```bash
git clone https://github.com/shu-king/kaiming-skill ~/kaiming-skill && bash ~/kaiming-skill/install.sh
```

这会把 skill 以 symlink 的方式安装到：

```text
~/.claude/skills/
```

默认情况下，`install.sh` 还会尝试通过你本机已经登录的 `gh` CLI 给这个 repo 点一个 star。如果没有安装或登录 `gh`，会自动跳过。

如果你不想自动 star，可以这样安装：

```bash
NO_STAR=1 bash ~/kaiming-skill/install.sh
```

也可以手动创建 symlink，或者直接删掉 `install.sh` 里的 star 逻辑。

---

## 怎么触发

安装后，可以在 Claude Code 里用类似这些请求触发：

```text
review my paper Kaiming-style
rewrite this paragraph in a Kaiming-style register
design my ablation table
give me a corpus-grounded Kaiming-style critique of X
```

完整示例见：

[`examples/demo-conversation-2026-04-27.md`](examples/demo-conversation-2026-04-27.md)

---

## 里面有什么

这个 repo 整理了几类反复出现的模式：

1. **Subtraction over Addition**
   加一个组件之前，先问能不能删掉一个组件。

2. **Decouple What Others Coupled**
   如果大家把两个决定绑在一起，先检查它们是否真的必须耦合。

3. **Raw Signal over Engineered Tokens**
   不要过早把输入变成复杂 token；先问原始信号是否已经足够。

4. **Long-term Usefulness**
   一个方法是否能成为别人继续使用的 primitive，而不只是当前 benchmark 上的组合拳。

5. **Recognition and Generation Together**
   从 representation 的角度看 recognition 和 generation 的连接。

这些不是固定规则，而是整理出来的研究写作参考。真正的判断仍然要回到你的问题、实验和数据。

---

## 资料来源

主要资料在 [`references/research/`](references/research/)：

| 文件 | 内容 |
|---|---|
| `01-papers.md` | 46 篇论文的 corpus index 和设计笔记 |
| `02-talks.md` | 公开 talks / tutorials 的摘录和使用建议 |
| `03-expression-dna.md` | 句式、intro 模板、ablation table 写法 |
| `04-external-views.md` | 保守的外部语境和 contested interpretations |
| `05-inferred-career-patterns.md` | 明确标注为 inference 的 career-pattern 笔记 |
| `06-timeline.md` | 公开 timeline 和 intellectual lineage |
| `verbatim-corpus.md` | 519 条原文摘录，按主题整理 |

主要材料包括：

- 46 篇 arXiv / paper corpus；
- 7 个来自 `people.csail.mit.edu/kaiming` 的 slide decks；
- NeurIPS 2024 New-in-ML talk；
- NeurIPS 2025 Faster R-CNN Test-of-Time talk；
- CVPR 2025 generative modeling talk；
- MIT Deep Learning Bootcamp recording / captions；
- ECCV、CVPR、ICCV tutorials 和 captions。

排除的来源包括：

- Zhihu posts；
- 微信公众号转载；
- 百度百科；
- marketing rewrite；
- 没有 attribution 的二手总结。

---

## 验证说明

`SKILL.md` 里直接使用的 quote 会通过：

```bash
python3 scripts/verify_quotes.py
```

更广的 quote corpus 是 reference corpus。运行：

```bash
python3 scripts/verify_quotes.py --strict
```

会额外检查 references 里的 quote，并报告一些辅助文件中的未命中。这些未命中可能来自 PDF/HTML 渲染、公式符号或字幕差异，也可能是真正需要修的 quote。因此这个 repo 不把整个 reference corpus 宣称为“完全验证”；更准确的说法是：

> `SKILL.md` 里直接使用的 quote 是验证过的；更大的 quote corpus 是参考材料，在做更强的验证声明前需要人工检查。

---

## Star

如果这个 repo 对你有帮助，可以考虑点一个 star。它能帮助更多学生和研究者发现这个项目，也会给维护者很多继续改进的动力。

---

## License

MIT — 你可以使用、修改和再分发。

引用底层论文时，请遵循原论文作者的 citation 方式。

---

## Acknowledgements

- 这个 repo 主要使用 Claude Code 构建。
- repo 结构参考了 [`alchaincyf/karpathy-skill`](https://github.com/alchaincyf/karpathy-skill)。
- skill 规范来自 [`anthropics/skills`](https://github.com/anthropics/skills)。
- 原始研究思想归功于 Kaiming He 和他的合作者。
