# Papers — corpus inventory

## Overview

This file inventories the 46-paper corpus that anchors the Kaiming He persona skill. The papers span 2014–2025 and trace a single intellectual arc: stripping complexity until the essential mechanism is exposed, then showing that simplicity scales. The corpus divides naturally into four eras. The MSRA early era (2014) contains SPP-Net, where Kaiming first diagnosed an unnecessary architectural constraint and removed it. The MSRA/FAIR recognition trilogy era (2015–2017) covers the three papers—PReLU+Kaiming init, ResNet, ResNet v2—that established depth as the dominant variable in recognition, followed immediately by Mask R-CNN and the detection family that showed the same residual backbone generalized to every structured-output task. The FAIR era (2017–2024) is the widest band: detection infrastructure (FPN, Focal Loss, Non-local, Group Norm), then the entire self-supervised arc from MoCo v1 through MAE and ST-MAE, plus the critical ablation papers (Rethinking Pre-training, MoCo v3, SimSiam) that audited what the community thought it knew. The MIT era (2024–2026) is a deliberate return to first principles in generative modeling: l-DAE deconstructs diffusion, MAR removes VQ, Fluid/RCG/Fractal rebuild generation from scratch, and MeanFlow/JiT/BiFlow establish a new theory of one-step generation.

Reading order matters. The corpus is not chronological in importance. The residual papers (1512.03385, 1603.05027) and the init paper (1502.01852) establish Kaiming's core method: find the hidden obstacle, remove it, measure the gap. MAE (2111.06377) is the bridge paper between the recognition era and the generative era, because it uses the same "remove the obvious thing" logic in an encoder. Everything in the MIT era is best read after MAE. The deconstruction papers (1811.08883, 2401.14404, 2502.13129) are companion reads that show the ablation discipline applied to received wisdom rather than to architecture choices.

The 46 papers are organized below as: 31 papers with arxiv IDs across four eras (Tiers 1–2), plus five Tier 3 pre-DL MSRA papers listed by name only (no arxiv). Voice certainty is high (first or last author) for 31 papers; the remaining 15 are middle-author supporting works. Quotes are drawn only from high-certainty papers unless a middle-author line is unmistakably Kaiming's register.

---

## Reading priority

For a reader new to Kaiming, read these ~15 papers in order:

- **1502.01852 — Delving Deep into Rectifiers** (2015): The method paper. Understand how Kaiming thinks about initialization before reading anything else—every later paper uses this analytical habit.
- **1512.03385 — ResNet** (2015): The central result. Degradation problem, residual formulation, 1st-place ILSVRC. Required.
- **1603.05027 — Identity Mappings in Deep Residual Networks** (2016): The follow-up that shows what ResNet actually needs: clean information paths, not just skip connections.
- **1406.4729 — SPP-Net** (2014): Read to understand Kaiming's pre-ResNet habits—locate the fixed-size constraint, remove it, measure the gain.
- **1703.06870 — Mask R-CNN** (2017): Shows how the residual philosophy extends to multi-task structured output; introduces RoIAlign and class-agnostic mask decoupling.
- **1803.08494 — Group Normalization** (2018): A clean example of the "decouple from the batch" move; shows how BN's batch dependence is an unnecessary constraint.
- **1811.08883 — Rethinking ImageNet Pre-training** (2018): The ablation paper that asks whether the canonical pre-train/fine-tune paradigm is necessary. Answer: no.
- **1911.05722 — MoCo v1** (2019): The contrastive SSL paper. Reframes the problem as dictionary lookup; introduces the momentum encoder to decouple consistency from batch size.
- **2011.10566 — SimSiam** (2020): Strips MoCo to its skeleton—no negatives, no momentum encoder—and isolates stop-gradient as the essential mechanism.
- **2111.06377 — MAE** (2021): The pivot paper. Takes BERT-style masking to vision; shows 75% masking ratio works because images are spatially redundant; scales ViT-L cleanly.
- **2401.14404 — l-DAE (Deconstructing DDM)** (2024): The first MIT-era deconstruction. Peels modern diffusion back to a classical denoising autoencoder; finds the tokenizer is the only critical ingredient.
- **2406.11838 — MAR** (2024): Removes the VQ tokenizer from autoregressive generation; replaces categorical distribution with diffusion loss over continuous tokens.
- **2502.13129 — Is Noise Conditioning Necessary** (2025): Challenges whether noise-level conditioning is indispensable for diffusion; finds it is not, and that flow-based models can improve without it.
- **2505.13447 — MeanFlow** (2025, NeurIPS Oral): Derives a ground-truth target field for one-step generation; closes the multi-step/one-step quality gap without distillation.
- **2511.13720 — JiT** (2025): Returns diffusion to pixel space and true denoising; shows a plain ViT on raw pixels is sufficient once the network is asked to predict clean data, not noise.

---

## By era

### MSRA early (2014) — pre-deep-learning roots and early DL

| Title | arXiv | Year | Author | Characterization |
|---|---|---|---|---|
| SPP-Net | 1406.4729 | 2014 | 1st | Removes the fixed-input-size constraint from CNNs via spatial pyramid pooling; first Kaiming paper to preview the "locate the unnecessary constraint, remove it" move |
| Single Image Haze Removal (Dark Channel Prior) | — | 2009 | 1st | CVPR Best Paper; statistical prior over haze; shows the early investment in low-level signal analysis |
| Guided Image Filtering | — | 2010/2012 | 1st | Edge-aware filter via local linear model; generalizes bilateral filtering with guaranteed linearity |
| Statistics of Patch Offsets for Image Completion | — | 2012 | 1st | Non-parametric texture synthesis for inpainting via patch offset statistics |
| Optimized Product Quantization | — | 2013 | 2nd | Nearest-neighbor search at scale; efficient code allocation in quantized feature spaces |

---

### MSRA / FAIR (2015–2017) — recognition trilogy

| Title | arXiv | Year | Author | Characterization |
|---|---|---|---|---|
| Delving Deep into Rectifiers (PReLU + Kaiming init) | 1502.01852 | 2015 | 1st | Derives initialization for ReLU networks; introduces PReLU; first work to surpass human-level ImageNet top-5 |
| Deep Residual Learning (ResNet) | 1512.03385 | 2015 | 1st | Residual connections solve the degradation problem; 152-layer network wins ILSVRC 2015 by large margin |
| Identity Mappings in Deep Residual Networks (ResNet v2) | 1603.05027 | 2016 | 1st | Pre-activation redesign cleans the information path; 1001-layer ResNet trains stably |
| Faster R-CNN | 1506.01497 | 2015 | 2nd | Region proposal network shares convolutional features with detection head; unifies proposal and detection |
| ResNeXt | 1611.05431 | 2016 | last | Grouped convolutions as cardinality dimension; aggregated residual transformations generalize Inception and ResNet |
| R-FCN | 1605.06409 | 2016 | middle | Position-sensitive score maps enable almost all computation to be shared across proposals |
| FPN (Feature Pyramid Networks) | 1612.03144 | 2016 | middle | Multi-scale feature pyramid with lateral connections; becomes the standard detection backbone neck |
| Focal Loss / RetinaNet | 1708.02002 | 2017 | middle | Focal loss down-weights easy negatives in dense detection; one-stage accuracy reaches two-stage |
| Mask R-CNN | 1703.06870 | 2017 | 1st | Adds instance segmentation branch to Faster R-CNN; RoIAlign fixes quantization; decouples mask from class |

---

### FAIR (2017–2024) — detection family + SSL + scaling

| Title | arXiv | Year | Author | Characterization |
|---|---|---|---|---|
| Non-local Neural Networks | 1711.07971 | 2017 | last | Long-range space-time dependencies via non-local means as a plug-in block |
| Accurate, Large Minibatch SGD (1-Hour ImageNet) | 1706.02677 | 2017 | last | Linear LR scaling rule + warmup enables 256-GPU ImageNet training in 1 hour |
| Feature Denoising for Adversarial Robustness | 1812.03411 | 2018 | last | Non-local means as denoising operator improves robustness to adversarial perturbations |
| Group Normalization | 1803.08494 | 2018 | last | Normalizes within channel groups; removes batch-size dependency; uniform performance across batch sizes |
| Rethinking ImageNet Pre-training | 1811.08883 | 2018 | 1st | Detection from random init matches pre-trained counterparts given enough data and compute |
| SlowFast Networks | 1812.03982 | 2018 | last | Two-pathway video model: slow pathway for spatial semantics, fast pathway for motion at fine temporal resolution |
| Panoptic Segmentation | 1801.00868 | 2018 | middle | Defines and benchmarks the panoptic task unifying semantic and instance segmentation |
| Panoptic FPN | 1901.02446 | 2019 | middle | Adds semantic segmentation head to FPN; single network for panoptic in one pass |
| VoteNet | 1904.09664 | 2019 | middle | Hough voting in point clouds for 3D object detection; adapts deep learning to sparse 3D data |
| PointRend | 1912.08193 | 2019 | middle | Renders segmentation masks at high resolution via adaptive point sampling; framed as rendering problem |
| MoCo v1 | 1911.05722 | 2019 | 1st | Contrastive SSL as dictionary lookup; momentum encoder + queue decouple dictionary size from batch size |
| MoCo v2 | 2003.04297 | 2020 | last | MLP projection head + stronger augmentation added to MoCo; establishes accessible SSL baselines |
| RegNet (Designing Network Design Spaces) | 2003.13678 | 2020 | middle | Parametric model family design via population statistics; quantized linear width schedules dominate |
| SimSiam | 2011.10566 | 2020 | last | Siamese networks without negatives or momentum encoder; stop-gradient prevents collapse; EM interpretation |
| Graph Structure of Neural Networks | 2007.06559 | 2020 | last | Relational graph structure predicts neural network accuracy; connects network topology to generalization |
| Large-Scale Spatiotemporal SSL Study | 2104.14558 | 2021 | last | Systematic study of SSL methods on video; masking-based approaches outperform contrastive with less domain knowledge |
| MoCo v3 | 2104.02057 | 2021 | last | Extends MoCo to ViT; identifies training instability as hidden accuracy killer; patch projection trick stabilizes |
| MAE (Masked Autoencoders) | 2111.06377 | 2021 | 1st | 75% random masking + asymmetric encoder-decoder; pixel reconstruction; scales ViT-L/H cleanly |
| ViTDet (Plain ViT for detection) | 2203.16527 | 2022 | last | Uses a plain non-hierarchical ViT as detection backbone; window attention + global blocks; no FPN hierarchy needed |
| FLIP (Masked CLIP) | 2212.00794 | 2022 | last | Applies masking to CLIP training; large masking ratio (50%) speeds training 2–3x with minimal accuracy loss |
| ST-MAE (Spatiotemporal MAE) | 2205.09113 | 2022 | last | Extends MAE to video with 90% masking; spacetime-agnostic random masking; minimal domain knowledge |
| RCG (Return of Unconditional Generation) | 2312.03701 | 2023 | last | Generates semantic representations first, then conditions image generator; closes unconditional vs. class-conditional gap |
| l-DAE (Deconstructing DDM) | 2401.14404 | 2024 | last | Systematically removes modern DDM components; finds tokenizer is the only critical ingredient; other designs are nonessential |
| Decade's Battle on Dataset Bias | 2403.08632 | 2024 | last | Modern networks classify which dataset an image belongs to with high accuracy; bias is latent and transferable |
| MAR (Autoregressive without VQ) | 2406.11838 | 2024 | last | Removes VQ requirement from autoregressive image generation; diffusion loss over continuous tokens |
| Fluid (Continuous-token T2I) | 2410.13863 | 2024 | last | Continuous tokens + random-order generation unlock scaling in visual autoregressive models |
| HPT (Heterogeneous Pre-trained Transformers) | 2409.20537 | 2024 | last | Pre-trains across heterogeneous visual tasks; scales representation learning beyond a single modality |

---

### MIT (2024–2026) — generative deconstruction

| Title | arXiv | Year | Author | Characterization |
|---|---|---|---|---|
| Is Noise Conditioning Necessary | 2502.13129 | 2025 | last | Removes noise-level conditioning from diffusion models; most methods degrade only modestly; flow models can improve |
| Fractal Generative Models | 2502.17437 | 2025 | last | Decomposes joint pixel distribution recursively via atomic generative modules; pixel generation without tokenizers |
| Diffuse and Disperse | 2506.09027 | 2025 | last | Dispersive loss enables representation learning inside the generative model; positive-free contrastive regularization |
| Transformers without Normalization (DyT) | 2503.10622 | 2025 | middle | Dynamic Tanh replaces all normalization layers in Transformers; comparable or better performance without BN/LN |
| MeanFlow (NeurIPS 2025 Oral) | 2505.13447 | 2025 | last | Mean velocity field provides ground-truth training target for one-step flow generation; closes multi-step quality gap |
| JiT (Back to Basics: Let DGM Denoise) | 2511.13720 | 2025 | last | Revisits true denoising in pixel space; plain ViT on raw pixels; no tokenizer, perceptual loss, or adversarial training |
| ARC Is a Vision Problem! | 2511.14761 | 2025 | last | Reframes ARC reasoning as image-to-image translation; visual priors (locality, invariance) are sufficient |
| Improved Mean Flows | 2512.02012 | 2025 | last | Fixes two issues in MeanFlow: network-dependent target and fixed guidance; standard regression formulation |
| Bidirectional Normalizing Flow (BiFlow) | 2512.10953 | 2025 | last | Decouples forward/reverse processes; learned reverse outperforms analytic inverse; 1-NFE generation with full flexibility |

---

## Per-paper design notes

### Deep Residual Learning — arXiv:1512.03385 (2015, 1st author)

**The puzzle:** Deeper plain networks produce *higher* training error than shallower ones—not because of overfitting, but because the optimizer cannot learn identity mappings through stacked nonlinear layers.

**The move:** Reformulate each layer as learning a residual F(x) rather than the full mapping H(x). If identity is optimal, F collapses to zero rather than requiring the network to construct identity through composition.

**Headline result:** A 152-layer ResNet wins ILSVRC 2015 classification, detection, and localization; 3.57% top-5 error on ImageNet.

**Best representative quote:**

> "We hypothesize that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping"
> — §Introduction

---

### Identity Mappings in Deep Residual Networks — arXiv:1603.05027 (2016, 1st author)

**The puzzle:** The original ResNet skip connection is not a true identity—BN and ReLU after the addition corrupt the signal path.

**The move:** Move BN and ReLU to before the weight layers (pre-activation), keeping the skip connection algebraically clean.

**Headline result:** A 1001-layer pre-activation ResNet trains stably and outperforms the original on CIFAR-10/100; multiplicative shortcuts (gating, 1×1 conv) hurt.

**Best representative quote:**

> "Multiplicative manipulations (scaling, gating, 1 × 1 convolutions, and dropout) on the shortcuts can hamper information propagation and lead to optimization problems."
> — §Method

---

### Delving Deep into Rectifiers — arXiv:1502.01852 (2015, 1st author)

**The puzzle:** Xavier initialization assumes symmetric activations; it fails for ReLU/PReLU networks because half the inputs are gated to zero.

**The move:** Derive a variance-preserving initialization for rectifier networks; introduce PReLU to learn the negative slope.

**Headline result:** First result to surpass reported human-level performance on ImageNet top-5; initialization enables training of very deep rectifier networks.

**Best representative quote:**

> "A proper initialization method should avoid reducing or magnifying the magnitudes of input signals exponentially"
> — §Method

---

### SPP-Net — arXiv:1406.4729 (2014, 1st author)

**The puzzle:** CNNs require fixed-size input not because of convolutions, but only because the fully-connected layers demand it—a localized and removable constraint.

**The move:** Insert a spatial pyramid pooling layer between the last convolutional layer and the FC layers; pool at multiple scales so any input size produces a fixed-length vector.

**Headline result:** 24–102× speedup over R-CNN on test images by avoiding repeated convolutional computation; competitive accuracy on Pascal VOC 2007.

**Best representative quote:**

> "the fixed-size constraint comes only from the fully-connected layers"
> — §Introduction

---

### Mask R-CNN — arXiv:1703.06870 (2017, 1st author)

**The puzzle:** Instance segmentation seems to require a complex specialized pipeline, yet the community expected more components to yield more accuracy.

**The move:** Add a third output head (binary mask per class) to Faster R-CNN; fix RoIPool's quantization with RoIAlign; decouple mask prediction from classification so mask branch is class-agnostic.

**Headline result:** Surpasses all existing single-model entries on every COCO task, including 2016 challenge winners, without special tricks.

**Best representative quote:**

> "we found it essential to decouple mask and class prediction: we predict a binary mask for each class independently, without competition among classes"
> — §Introduction

---

### MoCo v1 — arXiv:1911.05722 (2019, 1st author)

**The puzzle:** Contrastive SSL needs a large and consistent negative dictionary, but end-to-end training limits dictionary size to mini-batch size, and using a memory bank allows keys to become stale.

**The move:** Maintain a queue of keys encoded by a momentum-updated encoder (no gradient through key encoder); this decouples dictionary size from batch size and keeps keys consistent.

**Headline result:** MoCo ResNet-50 outperforms its supervised pre-training counterpart on 7 detection/segmentation tasks on PASCAL VOC and COCO.

**Best representative quote:**

> "From this perspective, we hypothesize that it is desirable to build dictionaries that are: (i) large and (ii) consistent as they evolve during training."
> — §Introduction

---

### MoCo v2 — arXiv:2003.04297 (2020, last author)

**The puzzle:** SimCLR improved over MoCo but required large batches (4096+); it was unclear whether the gains came from the projection head, stronger augmentation, or the large-batch contrastive setup.

**The move:** Ablate SimCLR's improvements in isolation on the MoCo framework; show that MLP head and stronger augmentation are orthogonal to the contrastive mechanism, and work without large batches.

**Headline result:** MoCo v2 matches SimCLR accuracy without requiring 4096-batch training; strong baselines made accessible.

**Best representative quote:**

> "two design improvements used in SimCLR, namely, an MLP projection head and stronger data augmentation, are orthogonal to the frameworks of MoCo and SimCLR"
> — §Introduction

---

### SimSiam — arXiv:2011.10566 (2020, last author)

**The puzzle:** MoCo uses negatives and a momentum encoder; BYOL removes negatives but keeps the momentum encoder. What is actually preventing collapse?

**The move:** Remove both negatives and momentum encoder; isolate the stop-gradient operation as the single essential component; interpret the remaining procedure as EM with two alternating sets of variables.

**Headline result:** Siamese network without negatives, large batches, or momentum encoder learns competitive ImageNet representations; collapse does not occur with stop-gradient.

**Best representative quote:**

> "In a nutshell, our method can be thought of as 'BYOL without the momentum encoder'."
> — §Introduction

---

### MoCo v3 — arXiv:2104.02057 (2021, last author)

**The puzzle:** Applying standard MoCo/contrastive SSL to ViT yields surprisingly modest results; training seems fine but accuracy lags unexpectedly.

**The move:** Diagnose training instability as the cause—small accuracy drops (1–3%) hide in noise but compound; stabilize with a frozen patch projection layer; ablate batch size, optimizer, and learning rate systematically.

**Headline result:** Stable ViT self-supervised training consistently improves with model size, unlike supervised ViT whose accuracy degrades at scale.

**Best representative quote:**

> "Interestingly, we observe that unstable ViT training may not result in catastrophic failure (e.g., divergence); instead, it can cause mild degradation in accuracy (e.g., 1 ∼ 3%). Such a degree of degradation may not be noticeable, unless a more stable counterpart is available for comparison."
> — §Introduction

---

### MAE (Masked Autoencoders) — arXiv:2111.06377 (2021, 1st author)

**The puzzle:** BERT-style masked prediction works for text; it was unclear whether the same approach would work for images, since images lack the same semantic tokenization and have heavy spatial redundancy.

**The move:** Mask 75% of image patches randomly; encode only visible patches (asymmetric encoder); decode in pixel space with a shallow decoder; predict raw pixel values, not discrete tokens.

**Headline result:** MAE ViT-L fine-tunes to 85.9% ImageNet top-1; training is 3× faster than supervised ViT; linear probing and fine-tuning are largely uncorrelated.

**Best representative quote:**

> "Simple algorithms that scale well are the core of deep learning."
> — §Discussion

---

### ST-MAE (Spatiotemporal MAE) — arXiv:2205.09113 (2022, last author)

**The puzzle:** MAE works for images with 75% masking; for video, temporal redundancy should allow even more aggressive masking, but the optimal strategy was unclear.

**The move:** Apply spacetime-agnostic random masking at 90%; use the same asymmetric encoder-decoder design as image MAE; introduce no motion-specific inductive biases.

**Headline result:** ST-MAE achieves state-of-the-art on Kinetics-400 and AVA; 90% masking ratio is optimal; minimal domain knowledge yields strong representations.

**Best representative quote:**

> "Our study suggests that the general framework of masked autoencoding (BERT, MAE, etc.) can be a unified methodology for representation learning with minimal domain knowledge."
> — §Abstract

---

### Rethinking ImageNet Pre-training — arXiv:1811.08883 (2018, 1st author)

**The puzzle:** The entire field assumed ImageNet pre-training was necessary for detection/segmentation; no one had carefully tested training from scratch with appropriate schedule length.

**The move:** Match training iterations rather than epochs; show that random-init models require longer training but converge to the same accuracy; test across 10% data subsets, deeper/wider models, and multiple tasks.

**Headline result:** Training from random initialization on COCO matches ImageNet pre-trained models in detection and segmentation across all tested conditions.

**Best representative quote:**

> "These observations challenge the conventional wisdom of ImageNet pre-training for dependent tasks and we expect these discoveries will encourage people to rethink the current de facto paradigm of 'pre-training and fine-tuning' in computer vision."
> — §Abstract

---

### Group Normalization — arXiv:1803.08494 (2018, last author)

**The puzzle:** Batch Normalization statistics degrade at small batch sizes (required by detection/video tasks with high memory demands); no good alternative preserved BN's optimization benefits.

**The move:** Normalize within groups of channels rather than across the batch dimension; group size G=32 works well across a wide range of architectures and tasks.

**Headline result:** GN matches BN on ImageNet with large batches; outperforms BN significantly at batch size 2; robustly improves detection, segmentation, and video tasks.

**Best representative quote:**

> "Despite its great success, BN exhibits drawbacks that are also caused by its distinct behavior of normalizing along the batch dimension."
> — §Introduction

---

### Non-local Neural Networks — arXiv:1711.07971 (2017, last author)

**The puzzle:** Local operations (convolution, recurrence) require many layers to capture long-range dependencies; increasing depth alone does not capture them efficiently.

**The move:** Generalize non-local means to a plug-in attention block computing a weighted sum over all positions; insert as a residual block anywhere in the network.

**Headline result:** Non-local blocks improve video action recognition on Kinetics by 2–3 points over strong baselines without optical flow or any bells and whistles.

**Best representative quote:**

> "we present non-local operations as an efficient, simple, and generic component for capturing long-range dependencies with deep neural networks."
> — §Introduction

---

### l-DAE (Deconstructing DDM) — arXiv:2401.14404 (2024, last author)

**The puzzle:** Denoising diffusion models involve many design choices (noise schedules, class conditioning, continuous noise levels, transformer architectures, latent tokenizers); it was unclear which were essential.

**The move:** Systematically remove modern DDM components one by one, transforming the model toward a classical denoising autoencoder (DAE); test what remains after each removal.

**Headline result:** Only the tokenizer is critical; removing class conditioning *improves* self-supervised linear probe accuracy; even a PCA tokenizer (no gradient training) works.

**Best representative quote:**

> "We observe that only a very few modern components are critical for learning good representations, while many others are nonessential."
> — §Abstract

---

### RCG (Return of Unconditional Generation) — arXiv:2312.03701 (2023, last author)

**The puzzle:** Unconditional image generation lagged far behind class-conditional; the gap was attributed to the difficulty of modeling a complex distribution without semantic guidance.

**The move:** Generate semantic representations first using a self-supervised encoder, then condition the image generator on those representations; decomposes the joint problem into two simpler sub-problems.

**Headline result:** RCG-conditioned models outperform their class-conditional counterparts on ImageNet 256×256 generation; unconditional generation is no longer a harder problem.

**Best representative quote:**

> "Surprisingly, with RCG, these generative models consistently outperform their class-conditional versions by a noticeable margin. This demonstrates that the rich semantic information from the unconditionally generated representations can guide the generative process even more effectively than class labels."
> — §Experiments

---

### MAR (Autoregressive without VQ) — arXiv:2406.11838 (2024, last author)

**The puzzle:** Autoregressive image generation universally used VQ tokenizers because categorical distributions require discrete tokens; the coupling between autoregression and discretization was treated as necessary.

**The move:** Decouple autoregression (predicting next token given previous) from discretization; use diffusion loss to model the per-token continuous distribution; no VQ required.

**Headline result:** MAR with diffusion loss matches or exceeds VQ-based autoregressive models on ImageNet 256×256; scales with model size similarly to language models.

**Best representative quote:**

> "In this work, we aim to address the following question: Is it necessary for autoregressive models to be coupled with vector-quantized representations? We note that the autoregressive nature, i.e., 'predicting next tokens based on previous ones', is independent of whether the values are discrete or continuous."
> — §Introduction

---

### Fluid (Continuous-token T2I) — arXiv:2410.13863 (2024, last author)

**The puzzle:** Visual autoregressive models did not scale as well as language models; raster-order generation with discrete tokens reached an accuracy plateau around 1B parameters.

**The move:** Compare discrete vs. continuous tokens and raster-order vs. random-order generation; show that VQ information loss and fixed raster order both limit scaling.

**Headline result:** Continuous tokens + random-order generation continue to scale past 1B parameters; raster-order discrete-token models plateau in both FID and GenEval.

**Best representative quote:**

> "simply using a GPT-like language model for images in a straightforward way may not scale well. To improve scaling for visual data, further adaptations such as continuous tokens and random-order generation are needed."
> — §Experiments

---

### Is Noise Conditioning Necessary — arXiv:2502.13129 (2025, last author)

**The puzzle:** Noise-level conditioning (timestep t) is universally believed to be indispensable for denoising diffusion models; it is present in every major method.

**The move:** Remove t-conditioning; measure degradation; identify which model families are robust and which are sensitive; derive a theoretical bound on the cost.

**Headline result:** Most models degrade only modestly without noise conditioning; flow-based models can actually improve; single energy function alignment with classical EBM is now possible.

**Best representative quote:**

> "It is widely believed that noise conditioning is indispensable for denoising diffusion models to work successfully. This work challenges this belief."
> — §Abstract

---

### Fractal Generative Models — arXiv:2502.17437 (2025, last author)

**The puzzle:** Pixel-by-pixel autoregressive generation lacks a natural sequential order and scales poorly because joint distributions over high-dimensional pixel grids are intractable.

**The move:** Abstract generative models into atomic modules; recursively decompose the joint pixel distribution via a fractal hierarchy of modules, each handling a local sub-problem.

**Headline result:** Fractal autoregressive model generates ImageNet 256×256 without tokenizers; FID improves from 11.80 to 6.15 scaling from 186M to 848M parameters.

**Best representative quote:**

> "Modularization is a cornerstone of computer science, abstracting complex functions into atomic building blocks. In this paper, we introduce a new level of modularization by abstracting generative models into atomic generative modules."
> — §Abstract

---

### MeanFlow — arXiv:2505.13447 (2025, last author, NeurIPS 2025 Oral)

**The puzzle:** Consistency models and flow distillation enable one-step generation but rely on behavioral constraints imposed on the network rather than on a ground-truth target field; training is unstable.

**The move:** Define the mean velocity as the average instantaneous velocity along a trajectory; derive the MeanFlow Identity as a natural regression target from this definition alone; no distillation or curriculum needed.

**Headline result:** MeanFlow closes the multi-step/one-step FID gap; trained entirely from scratch; outperforms distillation-based one-step models of comparable size.

**Best representative quote:**

> "Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning."
> — §Abstract

---

### JiT (Back to Basics: Let DGM Denoise) — arXiv:2511.13720 (2025, last author)

**The puzzle:** Modern diffusion models predict noise (or a mixture), not the clean image directly; the networks are optimized for a high-dimensional noisy target, requiring architectural complexity to avoid information bottlenecks.

**The move:** Reformulate so the network predicts clean data directly; operate in pixel space; use a plain ViT on large raw-pixel patches with a dimension-reducing bottleneck inside the network.

**Headline result:** JiT ViT trained from scratch on ImageNet 256×256 with no tokenizer, no perceptual loss, no adversarial loss, and no pre-trained encoder achieves competitive FID.

**Best representative quote:**

> "Today's denoising diffusion models do not 'denoise' in the classical sense, i.e., they do not directly predict clean images."
> — §Abstract

---

### ARC Is a Vision Problem! — arXiv:2511.14761 (2025, last author)

**The puzzle:** ARC-AGI tasks are typically solved with language model token sequences; the puzzles are presented visually but rarely treated as visual learning problems.

**The move:** Reframe ARC as image-to-image translation; apply visual inductive biases (2D locality, translation invariance, scale invariance); use a ViT with appropriate augmentations and test-time fine-tuning.

**Headline result:** Vision-centric ARC formulation achieves strong few-shot generalization; scale augmentation provides substantial gains because ViT lacks scale-invariance inductive bias.

**Best representative quote:**

> "Abstraction and inference can arise directly from visual learning, without explicit linguistic intermediates."
> — §Introduction

---

### Decade's Battle on Dataset Bias — arXiv:2403.08632 (2024, last author)

**The puzzle:** The 2011 Torralba & Efros paper exposed dataset bias; the field assumed progress in dataset curation had reduced the problem over a decade.

**The move:** Train a modern network to classify which dataset an image comes from; measure how easily even tiny models can detect dataset-specific patterns.

**Headline result:** Modern networks classify dataset origin with high accuracy; even a 7K-parameter ConvNeXt achieves 72.4% on YCD; dataset bias is not diminished—it is more detectable.

**Best representative quote:**

> "the ability to capture dataset bias may be inherent in deep neural networks, rather than enabled by specific components."
> — §Dataset Classification

---

### Bidirectional Normalizing Flow — arXiv:2512.10953 (2025, last author)

**The puzzle:** Normalizing flows require the reverse process to be the analytic inverse of the forward process; this hard-couples the two and constrains architecture choice.

**The move:** Decouple forward and reverse: train a normalizing flow as the forward process; train a separate learned reverse network supervised by the forward model; the reverse can use arbitrary architecture (e.g., bidirectional Transformer).

**Headline result:** Learned reverse model outperforms the analytic inverse; one-step generation achieves competitive FID; perceptual loss becomes applicable because the reverse predicts clean images.

**Best representative quote:**

> "We challenge the conventional wisdom that the reverse process must be the exact analytic inverse of the forward process, and demonstrate that the long-held constraint is unnecessary."
> — §Conclusion

---

### Improved Mean Flows — arXiv:2512.02012 (2025, last author)

**The puzzle:** Original MeanFlow has two issues: the regression target depends on the network's own outputs (non-standard), and classifier-free guidance is baked in at a fixed training-time scale.

**The move:** Reformulate training target to be network-independent; add an auxiliary head for guidance at inference time that introduces no extra parameters or compute at test time.

**Headline result:** Improved MeanFlow surpasses the original; flexible guidance scale at inference; training-from-scratch one-step model is competitive with multi-step distillation approaches.

**Best representative quote:**

> "Our reformulation yields a more standard regression problem and improves the training stability."
> — §Abstract

---

### Diffuse and Disperse — arXiv:2506.09027 (2025, last author)

**The puzzle:** Representation learning has driven progress in recognition but has been largely absent from generative modeling; existing approaches either require pre-trained encoders or external data.

**The move:** Introduce a dispersive loss inside the diffusion model itself—a contrastive regularizer without positive pairs—applied to the model's own intermediate representations during training.

**Headline result:** Dispersive loss improves generation quality across multiple model families without pre-training, extra parameters, or external data; the improvement is robust to temperature choice.

**Best representative quote:**

> "our method requires no pre-training, no additional model parameters, and no external data. With a self-contained and minimalist design, our method clearly demonstrates that representation learning can benefit generative modeling without relying on external sources of information."
> — §Introduction

---

## Tier 2 / supporting papers (no extended design notes)

| Title | arXiv | Year | Author | Characterization |
|---|---|---|---|---|
| Faster R-CNN | 1506.01497 | 2015 | 2nd | Region proposal network fused with detector; canonical two-stage detection baseline |
| FPN | 1612.03144 | 2016 | middle | Feature pyramid with lateral connections; standard multi-scale detection neck |
| Focal Loss / RetinaNet | 1708.02002 | 2017 | middle | Focal loss rebalances foreground/background in dense detection; one-stage reaches two-stage accuracy |
| ResNeXt | 1611.05431 | 2016 | last | Cardinality as a new network dimension; aggregated grouped convolutions |
| RegNet | 2003.13678 | 2020 | middle | Quantized linear width schedules from network design space analysis |
| R-FCN | 1605.06409 | 2016 | middle | Position-sensitive score maps for nearly-fully-shared computation in detection |
| Panoptic Segmentation | 1801.00868 | 2018 | middle | Defines and benchmarks the panoptic task |
| Panoptic FPN | 1901.02446 | 2019 | middle | Adds a semantic head to FPN for joint panoptic segmentation |
| PointRend | 1912.08193 | 2019 | middle | Adaptive point-based rendering for high-resolution segmentation |
| Large-Scale ST SSL Study | 2104.14558 | 2021 | last | Systematic comparison of SSL approaches for video representation learning |
| FLIP (Masked CLIP) | 2212.00794 | 2022 | last | 50% masking during CLIP training; 2–3× training speedup with minimal accuracy loss |
| ViTDet | 2203.16527 | 2022 | last | Plain ViT backbone for detection without hierarchical feature pyramid |
| SlowFast Networks | 1812.03982 | 2018 | last | Dual-pathway slow/fast video model for spatial+temporal understanding |
| Accurate Large Minibatch SGD | 1706.02677 | 2017 | last | Linear LR scaling + warmup for distributed ImageNet training in 1 hour |
| Feature Denoising | 1812.03411 | 2018 | last | Non-local denoising as adversarial defense; robust to PGD attacks |
| VoteNet | 1904.09664 | 2019 | middle | Hough voting in 3D point clouds for object detection |
| DyT (Transformers without Normalization) | 2503.10622 | 2025 | middle | Dynamic Tanh replaces all LayerNorm in Transformers; matches or exceeds LN performance |
| Graph Structure of Neural Networks | 2007.06559 | 2020 | last | Relational graph topology of a network predicts its accuracy |
| HPT | 2409.20537 | 2024 | last | Heterogeneous pre-trained Transformers across diverse visual task modalities |

---

## Cross-references

- **02-talks.md** — Kaiming's CVPR 2017, CVPR 2018, ECCV 2018, ICCV 2017, NeurIPS 2024, NeurIPS 2025, and YouTube talks. Cross-reference talks against the papers in the recognition trilogy and generative deconstruction eras; the talks reveal which design decisions he considers most important retrospectively.
- **03-expression-dna.md** — Recurring linguistic patterns extracted across all papers: "surprisingly", "we hypothesize", "without bells and whistles", "self-contained", "from scratch", "necessary", "essential". Read alongside the design notes above to calibrate voice register.
- **04-themes.md** (or verbatim-corpus.md) — All 521 quotes organized by theme (simplicity, residual, self-supervision, deconstruction, scaling, generality, ablation-discipline, pixels-over-tokens, recognition-generation-duality). Use to find additional illustrative quotes for any paper listed above.
- **05-ablation-style.md** — Documents the structured ablation discipline: isolate one variable, hold everything else constant, report both the positive result and the null result. The SimSiam stop-gradient ablation and the l-DAE component removal are the canonical examples.
- **SKILL.md** — The master persona document. The reading priority list in this file maps directly onto SKILL.md's "core commitments" section.

---

## Conventions

- All quotes are byte-exact substrings copied verbatim from `notes/{id}.json`. No paraphrasing.
- For middle/2nd-author papers, extended design notes are omitted; quotes would only be included if voice_certain=true and the line is unmistakably Kaiming's register.
- Each design-note entry targets ~80 words across the puzzle/move/headline fields combined.
- Author position (1st/last/middle/2nd) follows `assets/seed_papers.txt` exactly.
- Tier 3 pre-DL papers (CVPR 2009, ECCV 2010/2012, CVPR 2013, ECCV 2014) have no arxiv IDs; they are accessible from people.csail.mit.edu/kaiming/ and referenced by title only.
