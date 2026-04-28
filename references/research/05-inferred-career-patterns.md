# Inferred Career Patterns

This file is not a biography and does not claim to explain Kaiming He's personal motives. It summarizes public timeline facts and cautious corpus-level patterns that may be useful for research-writing advice.

Use these notes only as inference from public outputs. Do not present them as Kaiming He's private views, career advice, or stated reasons for institutional moves.

---

## I. Public Timeline Facts

| Period | Public affiliation | Observable research surface |
|---|---|---|
| 2007-2011 | PhD, Chinese University of Hong Kong | Low-level vision, image priors, filtering, matting, haze removal. |
| 2011-2016 | Microsoft Research Asia | SPP-Net, PReLU/Kaiming initialization, ResNet, Faster R-CNN, ResNet v2. |
| 2016-2024 | Facebook AI Research / Meta AI | Detection and segmentation systems, GroupNorm, MoCo, SimSiam, MAE, ST-MAE, ViTDet, RCG. |
| 2024-present | MIT EECS / CSAIL; public MIT page also lists part-time Google DeepMind Distinguished Scientist | Visual representation learning and generative-modeling work including l-DAE, MAR, MeanFlow, JiT, and related student-led papers. |

Safe wording: "The public publication record shifts from low-level vision to recognition/detection, then self-supervised learning, then generative modeling."

Unsafe wording: "He moved because he wanted X."

---

## II. Corpus-Level Patterns

These are patterns in the public record, not explanations of intent.

### II.1 Work Often Moves Toward Reusable Primitives

Across eras, many highly visible papers introduce or clarify reusable primitives: dark channel prior, guided filtering, residual connections, initialization, RoIAlign, GroupNorm, momentum contrast, masked autoencoding, and recent one-step generation targets.

Use this as a research-writing lesson: durable work often becomes a tool others can reuse. Do not infer personal career motivation from this pattern.

### II.2 Later Work Often Re-Examines Inherited Defaults

Several papers ask whether a field-default component is necessary: ImageNet pre-training, batch-dependent normalization, negative pairs, momentum encoders, vector quantization, noise conditioning, latent-space generation, or analytic invertibility.

Use this as a drafting checklist: identify the inherited default and test it directly.

### II.3 Recent Work Is Often Student-Led And Generative-Modeling-Focused

The MIT-era public record contains many senior-author papers with students or postdocs as first authors, especially around end-to-end or one-step generative modeling.

Safe wording: "The recent public corpus emphasizes generative modeling and student-led work."

Unsafe wording: "He left industry to do X."

---

## III. How To Use This In The Skill

When a user asks for career or topic advice, do not answer as if Kaiming He has a known private decision rule. Instead:

1. State that the public corpus cannot reveal personal motives.
2. Extract a general research-planning principle from the papers or talks.
3. Mark it as an inference.
4. Bring the answer back to the user's concrete research problem.

Example safe response:

```text
This is inference from the public corpus, not a stated view. A recurring pattern is to choose problems where a simple primitive can become reusable. For your project, the question is: what component would still be useful if today's benchmark changed?
```

---

## IV. Phrases To Avoid

Avoid these because they overstate private motivation:

- "He moved to FAIR because..."
- "He left MSRA because..."
- "He joined MIT because..."
- "He prefers academia over industry."
- "He did not start a company because..."
- "He believes career decisions should..."

Prefer these:

- "The public timeline shows..."
- "The publication record after this move emphasizes..."
- "A cautious inference from the corpus is..."
- "This is useful as a research-planning analogy, not as biographical evidence."

---

## Cross-references

- For source papers and design notes, see `01-papers.md`.
- For public talks, especially the methodology talk, see `02-talks.md`.
- For dated public facts, see `06-timeline.md`.
