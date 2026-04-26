# Timeline & Intellectual Lineage

This file is one of the seven research dossiers backing `SKILL.md`. It traces Kaiming He's biographical arc and intellectual genealogy — both who shaped him and who he has shaped in turn.

---

## I. Biographical timeline

| Year | Event |
|---|---|
| 1984 | Born in Guangzhou, Guangdong, China. |
| 2003 | Enters Tsinghua University, Department of Physics (later Information Science). National-level Physics Olympiad gold medal earlier. |
| 2007 | Begins PhD at Chinese University of Hong Kong (CUHK), advised by Xiaoou Tang. |
| 2009 | First-author CVPR Best Paper for *Single Image Haze Removal Using Dark Channel Prior* — first ever Chinese first-author CVPR Best Paper. |
| 2011 | Defends PhD; joins Microsoft Research Asia (MSRA) Beijing as researcher. Works under Jian Sun. |
| 2014 | Co-author on *SRCNN* (ECCV 2014) — first deep-learning super-resolution. Submits ResNet to ImageNet competition. |
| 2015 | First-author *Delving Deep into Rectifiers* (ICCV 2015) introducing PReLU and Kaiming initialization. Co-led MSRA team to ILSVRC + COCO 2015 sweep with ResNet (1st in classification, detection, localization, segmentation). |
| 2016 | First-author CVPR Best Paper for *Deep Residual Learning for Image Recognition* (ResNet). Publishes Identity Mappings (ResNet v2) at ECCV 2016. Joins Facebook AI Research (FAIR) Menlo Park as research scientist. |
| 2017 | First-author Mask R-CNN (ICCV 2017 Marr Prize). Co-author on Focal Loss/RetinaNet (ICCV 2017 Best Student Paper) and FPN (CVPR 2017). |
| 2018–2019 | Co-led FAIR's *Detectron* / *Detectron2* programs. Authored *Rethinking ImageNet Pre-training*, Group Normalization, Non-local NN. PAMI Mark Everingham Prize at ICCV 2021 (with Detectron team). |
| 2019–2020 | First-author MoCo v1 (CVPR 2020 Oral). Last-author SimSiam (CVPR 2021 Oral, Best Paper Honorable Mention). |
| 2021 | First-author MAE (CVPR 2022). Last-author MoCo v3 (ICCV 2021 Oral). |
| 2022–2023 | Last-author ST-MAE, FLIP, ViTDet. RCG (NeurIPS 2024 Oral, last author). |
| 2024 | Joins MIT EECS / CSAIL as tenured Associate Professor (Spring 2024). Last-author l-DAE (ICLR 2025), MAR (NeurIPS 2024 Spotlight), HPT (NeurIPS 2024 Spotlight), *A Decade's Battle on Dataset Bias* (ICLR 2025 Oral). Future Science Prize 2023 (with Sun, Ren, Zhang) presented. Teaches MIT 6.S978 *Deep Generative Models* (Fall 2024). |
| 2025 | Last-author MeanFlow (NeurIPS 2025 Oral), JiT, ARC, Improved Mean Flows, Bidirectional Normalizing Flow, Diffuse and Disperse, Fractal Generative Models, *Is Noise Conditioning Necessary*. Receives **ICCV Helmholtz Test-of-Time** for *Delving Deep into Rectifiers* (PReLU/Kaiming init) and **NeurIPS Test-of-Time** for Faster R-CNN. Teaches MIT 6.7960 *Deep Learning* (Fall 2025). |
| 2026 | First-author *One-step Latent-free Image Generation with Pixel Mean Flows* (Jan), *Generative Modeling via Drifting* (Feb). Teaches MIT 6.S058 *Introduction to Computer Vision* (Spring 2026). |

## II. Career-defining recognitions

- **CVPR 2009 Best Paper** (Dark Channel) — first Chinese 1st-author Best Paper in CVPR history.
- **CVPR 2016 Best Paper** (ResNet).
- **ICCV 2017 Marr Prize** (Mask R-CNN).
- **ICCV 2017 Best Student Paper Honorable Mention** (Focal Loss).
- **PAMI Mark Everingham Prize 2021** (Detectron team).
- **Future Science Prize 2023** (with Sun, Ren, Zhang for ResNet).
- **ICCV 2025 Helmholtz Test-of-Time Award** (PReLU + Kaiming init).
- **NeurIPS 2025 Test-of-Time Award** (Faster R-CNN).

## III. Citation footprint

ResNet alone is the most-cited 21st-century paper. Total Google Scholar count >800,000 by late 2025. Eight papers individually cited >25,000 times: ResNet, Faster R-CNN, Mask R-CNN, Focal Loss, FPN, MAE, MoCo, PReLU.

## IV. Intellectual lineage — influences IN

- **Jian Sun** (1976–2022) — Kaiming's MSRA mentor and the most cited collaborator on his early work. Co-author on Dark Channel, Guided Filter, ResNet, ResNet v2, Faster R-CNN, SPP-Net. The "deep simplicity" temperament — fewer knobs, identity primitives, results-driven choices — has Sun's clear imprint. (Posthumous Future Science Prize together.)
- **Xiaoou Tang** (CUHK PhD advisor) — low-level vision discipline; the "find one observation that breaks the field's assumption" reflex traces here.
- **Shaoqing Ren, Xiangyu Zhang** — co-authors and intellectual partners during the MSRA era (Faster R-CNN, ResNet).

Conceptual ancestors he cites or builds on:
- **Highway Networks** (Srivastava, Schmidhuber 2015) — explicitly contrasted with ResNet to argue the parameter-free identity over learned gates.
- **DenseNet** (Huang 2017) — concurrent residual-connection variant; he is consistently respectful but argues identity beats concatenation on the simplicity axis.
- **GAN** (Goodfellow), **VAE** (Kingma) — foundational generative modeling priors that the MIT-era work systematically deconstructs.
- **Attention is All You Need** (Vaswani 2017) — the universal-tokenizer framing that ViT/MAE adopt.

## V. Intellectual lineage — influences OUT (the school)

The cleanest stylistic heirs (closest "Kaiming-style" writing and method-design):

- **Ross Girshick** — co-author on Mask R-CNN, MoCo, MAE, FPN, RetinaNet, *Detectron*, *Rethinking ImageNet Pre-training*. Writing voice virtually indistinguishable in shared first-pages.
- **Piotr Dollár** — FPN, Mask R-CNN, RegNet, Focal Loss. The design-space methodology in RegNet is a Kaiming-style ablation discipline applied to architecture search.
- **Saining Xie** (NYU) — ResNeXt last-author, then *ConvNeXt* (CVPR 2022) which is explicitly a Kaiming-style "modernize a ResNet ablation by ablation" exercise. The closest stylistic descendant outside FAIR.
- **Xinlei Chen** — co-author on SimSiam (1st author), MoCo v2/v3, MAE (co-1st), l-DAE. Has internalized the "subtraction over addition" reflex most fully.
- **Yuxin Wu** — Group Normalization co-author. The minimal-change BN replacement is canonical Kaiming-style.
- **Christoph Feichtenhofer** — SlowFast, ST-MAE. The video-recognition arm.
- **Haoqi Fan, Yanghao Li, Tete Xiao, Hanzi Mao** — recurring FAIR co-authors.

MIT-era students/postdocs (the current school):

- **Tianhong Li** — most prolific: 1st author on RCG, MAR, FractalGen, JiT. Inherits the rhetoric (paper titles like *"Back to Basics: Let Denoising Generative Models Denoise"* and *"Autoregressive Image Generation without Vector Quantization"*).
- **Mingyang Deng** — MAR, MeanFlow.
- **Keya Hu** — ARC.
- Others: Jake Austin, Xingjian Bai, Zongyi Li.

The most contagious stylistic trait passed downstream is the **deconstruction reflex** — paper titles framing the contribution as removing rather than adding ("without VQ", "without Normalization", "back to basics", "is X necessary?").

## VI. Map position

In an "axis of ML research style":
- **Engineering rigor / empirical** ▲    Kaiming, Girshick, Yann LeCun (engineering era)
- **Theory-first / formal** ▼            Schmidhuber, Bengio
- **Subtraction / minimalist** ◀         Kaiming, Hinton (Capsule simplicity), Schmidhuber (LSTM minimalism)
- **Addition / accretion** ▶             much of NLP (RLHF stacks), some diffusion model lines

Kaiming sits clearly in the **upper-left quadrant** — engineering-rigorous AND minimalist. The closest neighbors are the Girshick/Dollár school he created, with Saining Xie as a satellite.

## VII. Public profile

- Largely private — no Twitter/X presence, no personal blog, no podcast appearances comparable to Karpathy or Sutskever.
- Public communication channel is paper writing + slide decks at people.csail.mit.edu/kaiming/.
- This is itself a Kaiming-style choice: signal through demonstrated work, not commentary on others'.

---

## Cross-references

- For paper-by-paper quotes and design moves, see `01-papers.md`.
- For talk excerpts (esp. NeurIPS 2024 *ML Research, via the Lens of ML*), see `02-talks.md`.
- For sentence-level voice patterns, see `03-expression-dna.md`.
- For external commentary and contrast with peers, see `04-external-views.md`.
- For the MSRA → FAIR → MIT pivots and their drivers, see `05-decisions.md`.
