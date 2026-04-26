# Decisions — career pivots and their drivers

This file traces the major institutional pivots in Kaiming He's career and the (publicly inferable) reasons behind them. Most of the content is reconstructed from publication patterns, public talks, and what little he has said on record. He does not maintain a personal blog or social media presence, so the analysis here is necessarily inference-from-pattern.

---

## I. The four-era arc

Kaiming's career so far has four distinct institutional eras, each with a different optimization target and a different writing voice.

| Era | Years | Institution | Mode | Optimizing for |
|---|---|---|---|---|
| **PhD / CUHK** | 2007–2011 | Chinese Univ. of Hong Kong (Tang lab) | Low-level vision | Best-paper recognition; methodology grounding |
| **MSRA** | 2011–2016 | Microsoft Research Asia (Sun lab) | Recognition trilogy | Architectural primitives that scale |
| **FAIR** | 2016–2024 | Facebook AI Research (Menlo Park) | Detection / SSL / generative | Field-defining contributions; production codebases |
| **MIT** | 2024–present | MIT EECS / CSAIL faculty | End-to-end generative modeling | Academic depth + student supervision |

Each pivot represents a shift in *what kind of research is being optimized for*, not necessarily a change in research style. The "subtraction over addition" temperament is constant.

---

## II. Pivot 1: CUHK → MSRA (2011)

**The decision.** After defending his PhD at CUHK in 2011 (advisor: Xiaoou Tang), Kaiming joined MSRA Beijing as a researcher under Jian Sun.

**Why this was a natural move.**
- MSRA Beijing was, at the time, the leading industrial research lab in Asia for computer vision.
- Jian Sun (then heading the visual computing group) was a dominant figure in low-level vision and was actively recruiting CUHK PhDs (CUHK and MSRA had close research ties).
- The MSRA model — generous compute, freedom to publish, strong industrial application pipeline — fit Kaiming's research style.

**The bet.** That the next decade of CV progress would be driven by architectural and algorithmic advances within an industrial-scale lab — and that he'd have more impact there than as a postdoc or junior faculty.

**Validated by.** ResNet (2015) was conceived and trained at MSRA. The MSRA team won 1st place in 5 categories of ILSVRC + COCO 2015 simultaneously — only possible with the kind of scale MSRA could provide.

---

## III. Pivot 2: MSRA → FAIR (2016)

**The decision.** August 2016, Kaiming moved from MSRA Beijing to Facebook AI Research Menlo Park as a research scientist.

**Why move at the peak of MSRA success.**

This is the pivot most worth understanding. Consider the timing: He won CVPR 2016 Best Paper for ResNet in June 2016 and joined FAIR ~2 months later. Why leave when MSRA was clearly delivering?

Inferable factors:
1. **Compute scale.** By 2016, deep-learning research's hardware demands were outgrowing even MSRA's resources. FAIR (and DeepMind) had committed to massive compute investments specifically for ML research.
2. **Research orientation.** MSRA's mandate balanced research and product transfer to Microsoft. FAIR explicitly committed to *open* research with no near-term product obligation. For someone whose orientation was "publish the cleanest result," that is a structural advantage.
3. **Collaborator gravity.** Yann LeCun was at FAIR; Ross Girshick had moved from Microsoft Research to FAIR in 2015; the detection community (Piotr Dollár, Tsung-Yi Lin, Kaiming, Girshick) was consolidating there.
4. **Field timing.** The next phase of CV — detection, segmentation, then SSL — was clearly going to require both compute and a tight collaborator network. FAIR offered both.

**The bet.** That the FAIR environment would produce the next round of field-defining work (Mask R-CNN, FPN, MoCo, MAE) more cleanly than continuing at MSRA. Validated emphatically — every one of those papers was authored at FAIR.

**The cost.** Less direct mentorship downstream of Sun; more distance from the Asia-CV ecosystem.

---

## IV. Pivot 3: FAIR → MIT (2024)

**The decision.** Spring 2024, Kaiming joined MIT EECS / CSAIL as a tenured Associate Professor — his first academic position. He retains affiliation with Meta AI for ongoing collaborations.

**Why move at the peak of FAIR productivity.**

In some ways this is the more puzzling pivot. By 2023, his FAIR career had produced ResNet, Mask R-CNN, MoCo, SimSiam, MAE, l-DAE, RCG — a list any professor would build a 30-year career around. Why move?

Inferable factors:
1. **Research direction.** The MIT-era papers (l-DAE, MAR, MeanFlow, JiT, Fractal Generative Models) are explicitly *deconstructive* and *foundational*. They are research-paper-shaped, not production-codebase-shaped. The MIT environment is a natural fit for that mode.
2. **Student supervision.** Kaiming's published work increasingly involves PhD students (Tianhong Li, Mingyang Deng, Keya Hu) as 1st authors with him as senior. Supervising graduate students is structurally an academic role.
3. **Independence from product cycles.** Generative-modeling research at industrial labs is increasingly entangled with product strategy (LLMs, image-generation tools, content moderation). Academic positioning lets him work on the deconstruction-style "what's actually needed?" questions without product constraint.
4. **Teaching as a research instrument.** He has taught MIT 6.S978 *Deep Generative Models* (Fall 2024), 6.7960 *Deep Learning* (Fall 2025), and 6.S058 *Introduction to Computer Vision* (Spring 2026). The pedagogical exposure feeds back into research framing — see how the CVPR 2025 talk *Towards End-to-End Generative Modeling* uses the recognition↔generation duality, which is also a teachable framing.

**The bet.** That the next phase of his work — building the "AlexNet of generative modeling" — is best done with a student lab on academic timescales rather than at industrial cadence.

**Public validation as of 2026.** The MIT-era output (MAR NeurIPS 2024 Spotlight; l-DAE ICLR 2025; *Decade's Battle on Dataset Bias* ICLR 2025 Oral; MeanFlow NeurIPS 2025 Oral; JiT and ARC submissions) suggests the bet is paying off. His students publish at the same cadence and venue tier as he did at FAIR.

---

## V. Cross-pivot patterns

Reading the three pivots together, three constants emerge.

### V.1 Optimize for the next 10-year window, not the next 1

CUHK → MSRA was a bet on industrial compute mattering for CV.
MSRA → FAIR was a bet on the open-research environment producing more compounding work.
FAIR → MIT is a bet on academic depth being the right environment for foundational generative-modeling work.

In each case the decision was made *while the previous environment was still delivering*, not after it had stopped working. That is itself a Kaiming-style move: act on the trajectory, not the snapshot.

### V.2 Move toward simplicity and away from complexity

Each pivot has reduced the *systems* surface area of his daily work:
- MSRA: large product research portfolio.
- FAIR: open research, but still production-codebase responsibilities (Detectron, Detectron2).
- MIT: deliberately minimalist research outputs; small student lab.

The trend is consistent with the philosophical signature of the work: subtract until what remains is essential.

### V.3 Always work with a strong collaborator gravity

- MSRA: Sun, Ren, Zhang, Dai (R-CNN family co-authors).
- FAIR: Girshick, Dollár, Xinlei Chen, Saining Xie (when Xie was an intern), Wu, Feichtenhofer.
- MIT: Tianhong Li, Mingyang Deng, Keya Hu — a tight student lab.

He has not, in 15+ years, worked in an environment where he was the only person doing his kind of CV research. The collaborator network is itself a research instrument.

---

## VI. Decisions NOT made (informative absences)

A few notable career-paths that he visibly did not take, and what their absence implies.

**Did not start a company.** Many of his peers (Andrej Karpathy → Eureka Labs, Ilya Sutskever → SSI, Mira Murati → Thinking Machines, Yi Zhou → recent moves) have founded labs or companies. Kaiming has stayed in research roles. The implication: he optimizes for paper-shaped impact, not product-shaped.

**Did not move into multimodal/foundation-model leadership at FAIR.** Around 2022–2023 there was substantial movement at FAIR (and across all major labs) into LLM and multimodal foundation-model leadership roles. Kaiming did not take such a role. His MIT pivot suggests he sees foundational generative modeling as the next 10-year direction and chose to work on it directly rather than manage a product-oriented team.

**Did not chase NLP / language modeling.** Despite the NLP boom of 2018–2023, Kaiming's corpus is overwhelmingly vision and CV-adjacent. He has co-authored exactly one cross-modal paper (FLIP, 2022 — masked CLIP) where the visual masking innovation is the contribution. The implication: he stays close to the domain where he has accumulated capital, rather than chasing the field that's currently hottest.

---

## VII. What the pivots tell us about advice

When the persona-skill is asked "should I switch [labs / roles / topics]?", the implied Kaiming-style decision rule from this corpus is:

1. **What's the 10-year curve?** Don't move based on current status; move based on where the field will be.
2. **Where is the collaborator gravity?** The right move is usually toward a tighter network of people doing similar work.
3. **What are you optimizing for that the current environment can't deliver?** Be specific. Not "growth" — *what specific thing.*
4. **Are you moving toward simplicity or complexity?** Toward fewer, deeper projects, or toward more, shallower? Default toward the former.
5. **Move while the current environment is still working.** Acting on a trajectory is different from reacting to a failure.

These are inferred from pattern, not stated. Mark them as inference, not quote.

---

## Cross-references

- For paper-level evidence of how the FAIR-era and MIT-era differ stylistically, see `01-papers.md`.
- For the methodology talk where he most explicitly discusses "Future is the Real Test Set" and scalability decisions, see `02-talks.md`.
- For the biographical timeline that anchors these pivots, see `06-timeline.md`.
- For the intellectual lineage and collaborator network, also see `06-timeline.md` §IV–V.
