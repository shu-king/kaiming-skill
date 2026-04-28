# Talks — corpus inventory

## Overview

This dossier covers 9 talk artifacts spanning 2017–2025: two CVPR tutorials (2017, 2018), one ECCV tutorial (2018), one ICCV tutorial (2017), two keynotes/workshops from 2024–2025, one NeurIPS Test-of-Time lecture (2025), and two YouTube auto-caption sources (MIT Bootcamp 2024 and CVPR 2017 video). Together they form a longitudinal record of how Kaiming He communicates his ideas — the tutorials provide dense technical reasoning and slide-text verbatim, while the two methodology talks (NeurIPS 2024 and CVPR 2025) offer philosophical framing that never appears in papers.

The two methodology talks are categorically different from everything else in the corpus. Papers report findings; tutorials drill into technical detail; but the NeurIPS 2024 New-in-ML keynote and the CVPR 2025 MeanFlow workshop talk are the only places where Kaiming explicitly theorizes about the nature of ML research, the structure of the field's progress, and the open questions he finds most compelling. They are the primary sources for replicating his voice on research strategy, intellectual risk-taking, and cross-domain analogies. No paper in the corpus says "Future is the Real Test Set" or asks "Are we still in the pre-AlexNet era of generative modeling?" — those frames exist only here.

---

## NeurIPS 2024 New-in-ML — "ML Research, via the Lens of ML" (THE methodology talk)

This is the single most important source in the entire corpus for understanding Kaiming's research philosophy. Delivered at the NeurIPS 2024 New-in-ML workshop, the talk systematically applies ML concepts — optimization landscapes, bias-variance tradeoff, train/test split, Occam's razor, Moore's law — as metaphors for how research itself should be conducted. The effect is a unified worldview, not a collection of aphorisms.

The central claim is that research behaves like SGD operating in a chaotic non-convex landscape: you cannot see the global optimum, you are exploring under noise, and large learning-rate jumps (risky, unconventional ideas) are sometimes necessary to escape local minima.

> "Research is SGD in a chaotic landscape"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Slide 16)

The talk draws a sharp distinction between what ML systems optimize (expected value over the training distribution) and what research should pursue (deviation from that expectation):

> "ML concerns 'Expectation'; Research looks for 'Surprise'"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Slide 146)

He unpacks surprise further: it is not mere novelty but the combination of an unexpected attempt and a genuinely novel possibility:

> "\"surprise\" :\nunexpected attempt\n\n\n\n\" what if ?\":\n\nnovel possibility"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Slide 183)

The train/test split metaphor drives one of the talk's most quotable lines — current benchmarks are the training set; the only honest evaluation is what the community does with your work years later:

> "Future is the Real Test Set"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Slide 247)

Complexity in research design is treated as overfitting. Simplicity is not an aesthetic preference but a regularizer:

> "Reduce \"overfitting\" of your research\n\nLess is More - Occam's Razor"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Slide 346)

The takeaways slide crystallizes the full framework in three lines, and adds the scalability dimension:

> "Research is SGD in a chaotic landscape Look for 'surprise' Future is the real test set"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Takeaways)

> "Scalability: Your research vs. Moore's law"
> — NeurIPS 2024 New-in-ML (talk_neurips2024_newinml, §Takeaways)

The scalability point is a warning: if your contribution will be made obsolete simply by hardware progress, it is not a research contribution — it is an engineering footnote. Real contributions are those that scale with, rather than are erased by, compute growth.

---

## CVPR 2025 Workshop — "Towards End-to-End Generative Modeling"

Delivered at a CVPR 2025 workshop, this talk introduces the MeanFlow method while situating it inside a larger historical analogy: just as recognition was stuck in the layer-wise pre-training era before AlexNet made end-to-end training standard, generative modeling today may be in an analogous pre-AlexNet moment.

The talk opens with a history lesson on recognition: end-to-end training became the norm after AlexNet, and the community never looked back. The argument is that generative modeling has not yet made that transition:

> "Since AlexNet, **recognition** models have been generally **end-to-end** ..."
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §A Bit of History)

> "Today's generative models are conceptually like \"layer-wise training\""
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §History Repeating in Generative Models?)

The talk then proposes a symmetric framing of recognition and generation as dual flows between distributions:

> "**Recognition** \"Flow\" from data to embeddings"
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §Recognition vs. Generation: Two Sides of the Same Coin?)

> "**Generation** : \"Flow\" from embeddings to data"
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §Recognition vs. Generation: Two Sides of the Same Coin?)

The MeanFlow identity is presented as the key technical insight enabling single-step generation — replacing an intractable integral with a differentiable identity:

> "**Integral** is intractable. **Differentiate** it instead."
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §The MeanFlow Identity)

The closing question frames the talk's ambition most directly:

> "Are we still in the **pre-AlexNet** era of generative modeling?"
> — CVPR 2025 Workshop (talk_cvpr2025_meanflow, §Looking ahead)

This "pre-AlexNet" framing is a signature Kaiming move: locating the present moment inside a historical arc and implying that the conceptual unlock has not yet happened — but is close.

---

## NeurIPS 2025 Test-of-Time — "A Brief History of Visual Object Detection"

This lecture, delivered upon receiving the NeurIPS Test-of-Time Award for Faster R-CNN, is retrospective in tone. Kaiming traces detection from handcrafted features through R-CNN, Fast R-CNN, and Faster R-CNN, identifying the conceptual shifts each represented.

The Faster R-CNN slides are notable for framing the system not just as a detection method but as an instance of differentiable programming and a catalyst for better software abstractions:

> "Among first real usages of **differentiable programming**"
> — NeurIPS 2025 Test-of-Time (talk_neurips2025_fasterrcnn, §Faster R-CNN slide)

> "A conceptual shift in CV from \" **architectures** \" to \" \"\n**programs**"
> — NeurIPS 2025 Test-of-Time (talk_neurips2025_fasterrcnn, §Faster R-CNN slide)

The closing "Age of Discoveries" slide captures the exploratory uncertainty Kaiming associates with research at the frontier — echoing the NeurIPS 2024 "chaotic landscape" framing but in more evocative language:

> "• **Into the fog** • **No oracle map** • **Is there even a destination?** • **What's on the other side of the land?** • **And: what will it mean for us?**"
> — NeurIPS 2025 Test-of-Time (talk_neurips2025_fasterrcnn, §Age of Discoveries)

---

## Earlier tutorials (ECCV/CVPR/ICCV 2017–2018)

### CVPR 2017 — Deep Learning for Objects & Scenes

The CVPR 2017 tutorial is the most detailed of the earlier tutorials, covering AlexNet through ResNeXt. Kaiming frames the entire arc as a "Revolution of Depth" and treats ResNets as the engine that made deep features general:

> "Engine of Visual Recognition ResNets/extensions are leading models on popular benchmarks"
> — CVPR 2017 tutorial (talk_cvpr2017, §Slide: Engine of Visual Recognition)

The degradation problem motivating ResNets is introduced by contradiction: a deeper plain net should, by construction, be at least as good as a shallower one if it can simply learn identity mappings — but empirically it cannot:

> "A deeper model should not have **higher** **training error** - A solution _by construction_ :"
> — CVPR 2017 tutorial (talk_cvpr2017, §Slide: Simply stacking layers?)

The residual reformulation is explained as a change in what the network must learn, not a change in representational capacity:

> "If identity were optimal, easy to set weights as 0 If optimal mapping is closer to identity, easier to find small fluctuations"
> — CVPR 2017 tutorial (talk_cvpr2017, §Slide: Deep Residual Learning)

The conclusion is characteristically direct:

> "**Deep features** empower amazing visual recognition results"
> — CVPR 2017 tutorial (talk_cvpr2017, §Slide: Conclusion: Features Matter!)

### CVPR 2018 — Visual Recognition Tutorial

The CVPR 2018 tutorial is structurally similar to the CVPR 2017 version but tighter. The opening thesis is stated plainly:

> "Deep Learning is Representation Learning"
> — CVPR 2018 tutorial (talk_cvpr2018, §Title slide)

The modular design philosophy appears explicitly:

> "Generic components, less domain knowledge Repeat **elementary** layers: going deeper"
> — CVPR 2018 tutorial (talk_cvpr2018, §Learning to represent)

### ECCV 2018 — Visual Recognition Tutorial

The ECCV 2018 tutorial adds a practical caution absent from the CVPR version — a candid note about Batch Normalization bugs from personal experience:

> "**Caution** : make sure your BN usage is correct! (this causes many of my bugs in my research experience!)"
> — ECCV 2018 tutorial (talk_eccv2018, §Batch Normalization (BN))

It also previews Group Normalization as a BN replacement that is independent of batch size, foreshadowing the GN paper:

> "• Independent of batch size • Robust to small batches • Enable new scenarios: e.g.: 41 AP on COCO trained from scratch"
> — ECCV 2018 tutorial (talk_eccv2018, §Teaser : Group Normalization (GN))

### ICCV 2017 — Mask R-CNN Tutorial

The ICCV 2017 tutorial centers entirely on Mask R-CNN. The key conceptual contribution highlighted is the invariance/equivariance distinction: classification wants invariant representations, instance segmentation demands equivariant ones — and RoIPool breaks equivariance:

> "_Instance Seg._ desires _equivariant_ representations: Translated object => translated mask Scaled object => scaled mask _Big and small_ objects are equally important (due to AP metric)"
> — ICCV 2017 tutorial (talk_iccv2017, §Invariance vs. Equivariance)

> "RoIPool _breaks_ pixel-to-pixel translation-equivariance"
> — ICCV 2017 tutorial (talk_iccv2017, §RoIAlign vs. RoIPool)

---

## YouTube auto-captions (MIT Bootcamp 2024, CVPR 2017 video)

These two files contain speech transcribed by YouTube's automatic captioning system. The text is noisy — punctuation is absent, homophones appear, and sentence boundaries are unreliable. Only the cleanest, most semantically stable extractions should be used in SKILL.md responses; they are best treated as secondary corroboration rather than primary quotation.

The MIT Bootcamp 2024 capture (talk_yt_mit2024) contains a clear statement of the deep learning compositionality principle:

> "a key idea of deep learning is to compose a simple set of General modules into highly complex functions for us to solve highly complex problems"
> — MIT Bootcamp 2024 (talk_yt_mit2024, §Speech)

It also contains the most explicit statement of generality as a value:

> "again this demonstrate the generality of the deep learning methodology that is to say if we develop a very effective and very general component from from one application then it is likely that you are going to enjoy the benefit in some other applications"
> — MIT Bootcamp 2024 (talk_yt_mit2024, §Speech)

The CVPR 2017 video capture (talk_yt_cvpr2017) corroborates the degradation argument:

> "a deeper model has a richer solution space and a deeper model should not have higher trending error than its shallower counterparts"
> — CVPR 2017 video (talk_yt_cvpr2017, §Speech)

> "in my understanding the success of deep learning is the success of feature learning so in the case of uh visual recognition features uh still matter"
> — CVPR 2017 video (talk_yt_cvpr2017, §Speech)

When using auto-caption quotes, prefer paraphrasing the idea and citing the source over quoting verbatim, unless the quote is among those flagged above as clean.

---

## How to use this dossier

When generating SKILL.md responses through the Kaiming-style lens, use the NeurIPS 2024 talk (talk_neurips2024_newinml) as the primary source for any question about research methodology, intellectual risk, simplicity versus complexity, or long-term research strategy — it is the only source where these views are developed at length in Kaiming He's slide text. Use the CVPR 2025 talk (talk_cvpr2025_meanflow) for questions about generative modeling, the recognition-generation duality, or flow-based methods. Use the NeurIPS 2025 Test-of-Time talk (talk_neurips2025_fasterrcnn) for retrospective framing of detection history and the "differentiable programming" reframe of Faster R-CNN. Use the 2017–2018 tutorials for technical depth on ResNets, Mask R-CNN, normalization, and instance segmentation; these are the densest slide-text sources for those topics. Treat YouTube auto-captions as secondary and flag them as such when citing.

---

## Cross-references

- [01-papers.md](01-papers.md) — primary paper corpus; talks frequently gloss ideas first published there
- [03-expression-dna.md](03-expression-dna.md) — recurring linguistic patterns extracted from both papers and talks
- [06-timeline.md](06-timeline.md) — chronological overview of papers and talks together
- [verbatim-corpus.md](verbatim-corpus.md) — full verbatim quote collection across all sources
