# Verbatim Quote Corpus

All 519 verbatim quotes extracted from 55 primary sources, grouped by theme.

Every quote is a byte-exact substring of `text/{papers,talks}/<id>.md`. 
Verification gating: `python3 scripts/verify_quotes.py --strict`.

**voice_certain** = the quote can be confidently attributed to Kaiming's voice (1st/last-author papers and talks where he's primary speaker). False on middle-author papers unless the quote sounds clearly Kaiming-style ('without bells and whistles', 'we observe', 'simplest thing that works').


## Theme: simplicity  (104 quotes)

> "Modularization is a cornerstone of computer science, abstracting complex functions into atomic building blocks. In this paper, we introduce a new level of modularization by abstracting generative models into atomic generative modules."
> — Fractal Generative Models (arXiv:2502.17437, §Abstract, 2025, last author)

> "By recursively decomposing the joint distribution, our fractal autoregressive architecture not only significantly reduces computational costs compared to a single large autoregressive model but also captures the intrinsic hierarchical structure within the data."
> — Fractal Generative Models (arXiv:2502.17437, §Method, 2025, last author)

> "We believe that fractal generative models are particularly well-suited for modeling data with intrinsic structures beyond one-dimensional sequential orders. We hope that the simplicity and effectiveness of our method will inspire the research community to explore novel designs and applications of fractal generative models."
> — Fractal Generative Models (arXiv:2502.17437, §Discussion and Conclusion, 2025, last author)

> "Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Abstract, 2025, last author)

> "The existence of the ground-truth target field ensures that the optimal solution is, in principle, independent of the specific network, which in practice can lead to more robust and stable training."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Introduction, 2025, last author)

> "Overall, our method is conceptually simple: it behaves similarly to Flow Matching, with the key difference that the matching target is modified"
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Method, 2025, last author)

> "Notably, our method is self-contained and trained entirely from scratch . It achieves the strong results without using any pre-training, distillation, or the curriculum learning adopted in"
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Experiments, 2025, last author)

> "Developing a self-contained and minimalist approach to representation-based generative modeling is still an essential topic in this line of research."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "Dispersive Loss behaves like a "contrastive loss without positive pairs"—and as such, unlike contrastive learning, it requires neither two-view sampling, specialized data augmentation, nor an additional encoder."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "our method requires no pre-training, no additional model parameters, and no external data. With a self-contained and minimalist design, our method clearly demonstrates that representation learning can benefit generative modeling without relying on external sources of information."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "Within this context, our method can be interpreted as "positive-free" contrastive learning, which is an underexplored direction in standard self-supervised learning."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "A key principle guiding our design is to introduce minimal or no interference with the sampling process of the original training objective."
> — Diffuse and Disperse (arXiv:2506.09027, §Conclusion, 2025, last author)

> "Our approach is self-contained and does not rely on any pre-training or auxiliary loss — no latent tokenizer, no adversarial loss, no perceptual loss (thus no pre-trained classifier), and no representation alignment (thus no self-supervised pre-training)."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Introduction, 2025, last author)

> "By doing so, we show that a plain Vision Transformer (ViT), operating on large image patches consisting of raw pixels, can be effective for diffusion modeling."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Introduction, 2025, last author)

> "Our work adopts a minimalist and self-contained design. By reducing domain-specific inductive biases, we hope our approach can generalize to other domains where tokenizers are difficult to obtain."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Discussion and Conclusion, 2025, last author)

> "Our reformulation yields a more standard regression problem and improves the training stability."
> — Improved Mean Flows (arXiv:2512.02012, §Abstract, 2025, last author)

> "This reformulation provides a regression target v that does not depend on the network."
> — Improved Mean Flows (arXiv:2512.02012, §Introduction, 2025, last author)

> "We suggest that fixing the guidance compromises the flexibility at inference time, and that the optimal value depends on the model's capability."
> — Improved Mean Flows (arXiv:2512.02012, §Introduction, 2025, last author)

> "This auxiliary head introduces no extra parameters or compute at inference time."
> — Improved Mean Flows (arXiv:2512.02012, §Experiments, 2025, last author)

> "As adaLN-zero is parameter-heavy, removing it yields a substantial 1/3 reduction in model size, from 133M to 89M. Such a reduction is highly attractive for larger models."
> — Improved Mean Flows (arXiv:2512.02012, §Experiments, 2025, last author)

> "In our framework, the designs of the forward and reverse processes are decoupled: the forward process can be any NF model that is computable, tractable, and easy to learn"
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Introduction, 2025, last author)

> "Such a "what-you-see-is-what-you-get" property further enables the use of perceptual loss, which is impossible or difficult to leverage with an explicit inverse."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Introduction, 2025, last author)

> "**Integral** is intractable. **Differentiate** it instead."
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §The MeanFlow Identity, 2025)

> "We hope our study will rekindle interest in a family of classical methods within the realm of modern self-supervised learning."
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Abstract, 2024, last author)

> "What we actually need are a loss function and its corresponding sampler for distribution modeling."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Method, 2024, last author)

> "The concept of autoregression is orthogonal to network architectures: autoregression can be done by RNNs, CNNs, and Transformers."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Method, 2024, last author)

> "This can be thought of as tokenizing each embodiment using neural networks and alleviating the need to unify embodiments into a homogeneous data form in standard training procedures."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Method, 2024, last author)

> "To avoid overfitting, the stem only has a small number of parameters (one MLP and one attention layer)."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Method, 2024, last author)

> "Reduce "overfitting" of your research Less is More - Occam's Razor"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 346, 2024)

> "a key idea of deep learning is to compose a simple set of General modules into highly complex functions for us to solve highly complex problems"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "the VG architecture is very simple it is just the idea about how can we build a very deep neur Network architectures without bells and withs"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "RCG is conceptually simple, flexible, yet highly effective for unconditional generation."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Introduction, 2023, last author)

> "Directly modeling a complex high-dimensional image distribution is a challenging task. RCG decomposes it into two much simpler sub-tasks: first modeling the distribution of a compact low-dimensional representation, and then modeling the image distribution conditioned on this representation distribution."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Method, 2023, last author)

> "We explore the plain, non-hierarchical Vision Transformer (ViT) as a backbone network for object detection."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Abstract, 2022, last author)

> "Surprisingly, we observe: (i) it is sufficient to build a simple feature pyramid from a single-scale feature map (without the common FPN design) and (ii) it is sufficient to use window attention (without shifting) aided with very few cross-window propagation blocks."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Abstract, 2022, last author)

> "In our study, we do not aim to develop new components; instead, we make minimal adaptations that are sufficient to overcome the aforementioned challenges."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Method, 2022, last author)

> "we show that our MAE method can learn strong representations with almost no inductive bias on spacetime (only except for patch and positional embeddings), and spacetime-agnostic random masking performs the best."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Abstract, 2022, last author)

> "Our method is simple: we randomly mask out spacetime patches in videos and learn an autoencoder to reconstruct them. Our method has minimal domain knowledge"
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Introduction, 2022, last author)

> "The autoencoding nature of our method (i.e., predicting pixels) provides a self-contained solution."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Experiments, 2022, last author)

> "Our pixel-based method is simpler and performs better"
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Experiments, 2022, last author)

> "We present Fast Language-Image Pre-training (FLIP), a simple and more efficient method for training CLIP."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Abstract, 2022, last author)

> "Our method does not perform reconstruction and is not a form of autoencoding."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Introduction, 2022, last author)

> "to strive for simplicity, we decide not to use the reconstruction loss. Waiving the reconstruction head also helps simplify the system and improves the accuracy/time trade-off."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Experiments, 2022, last author)

> "In this work, we go back to basics and investigate the fundamental components of training deep neural networks: the batch size, learning rate, and optimizer."
> — MoCo v3 (arXiv:2104.02057, §Introduction, 2021, last author)

> "We abandon the memory queue, which we find has diminishing gain if the batch is sufficiently large"
> — MoCo v3 (arXiv:2104.02057, §Method, 2021, last author)

> "Coupling these two designs enables us to train large models efficiently and effectively: we accelerate training (by"
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Abstract, 2021, 1st author)

> "Our pixel -based MAE is much simpler than tokenization."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Ablation, 2021, 1st author)

> "With simple modifications to MoCo—namely, using an MLP projection head and more data augmentation—we establish stronger baselines that outperform SimCLR and do not require large training batches."
> — MoCo v2 (arXiv:2003.04297, §Abstract, 2020, last author)

> "We hope this will make state-of-the-art unsupervised learning research more accessible."
> — MoCo v2 (arXiv:2003.04297, §Abstract, 2020, last author)

> "The improvements we investigate require only a few lines of code changes to MoCo v1, and we will make the code public to facilitate future research."
> — MoCo v2 (arXiv:2003.04297, §Experiments, 2020, last author)

> "The stop-gradient operation is a natural consequence , because the gradient does not back-propagate to"
> — SimSiam (arXiv:2011.10566, §Method, 2020, last author)

> "The competitiveness of our minimalist method suggests that the Siamese shape of the recent methods can be a core reason for their effectiveness"
> — SimSiam (arXiv:2011.10566, §Conclusion, 2020, last author)

> "we use Panoptic FPN with a ResNet-101 backbone and without bells-and-whistles."
> — Panoptic FPN (arXiv:1901.02446, §Experiments, 2019, middle author)

> "GN can be easily implemented by a few lines of code in modern libraries."
> — Group Normalization (arXiv:1803.08494, §Abstract, 2018, last author)

> "We notice that many classical features like SIFT and HOG are group-wise features and involve group-wise normalization."
> — Group Normalization (arXiv:1803.08494, §Introduction, 2018, last author)

> "Our model involves (i) a Slow pathway, operating at low frame rate, to capture spatial semantics, and (ii) a Fast pathway, operating at high frame rate, to capture motion at fine temporal resolution."
> — SlowFast Networks (arXiv:1812.03982, §Abstract, 2018, last author)

> "Despite its high temporal rate, this pathway is made very lightweight, e.g., ∼ 20% of total computation."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "We present a conceptually simple, flexible, and general framework for object instance segmentation"
> — Mask R-CNN (arXiv:1703.06870, §Abstract, 2017, 1st author)

> "Without bells and whistles, Mask R-CNN outperforms all existing, single-model entries on every task, including the COCO 2016 challenge winners."
> — Mask R-CNN (arXiv:1703.06870, §Abstract, 2017, 1st author)

> "Given this, one might expect a complex method is required to achieve good results. However, we show that a surprisingly simple, flexible, and fast system can surpass prior state-of-the-art instance segmentation results."
> — Mask R-CNN (arXiv:1703.06870, §Introduction, 2017, 1st author)

> "Despite being a seemingly minor change, RoIAlign has a large impact: it improves mask accuracy by relative 10% to 50%, showing bigger gains under stricter localization metrics. S"
> — Mask R-CNN (arXiv:1703.06870, §Introduction, 2017, 1st author)

> "Mask R-CNN is conceptually simple: Faster R-CNN has two outputs for each candidate object, a class label and a bounding-box offset; to this we add a third branch that outputs the object mask. M"
> — Mask R-CNN (arXiv:1703.06870, §Method, 2017, 1st author)

> "We note that our mask branches have a straightforward structure. More complex designs have the potential to improve performance but are not the focus of this work."
> — Mask R-CNN (arXiv:1703.06870, §Method, 2017, 1st author)

> "we employ a simple and hyper-parameter-free linear scaling rule to adjust the learning rate."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Introduction, 2017, last author)

> "we have found it to simplify migrating algorithms from a single-GPU to a multi-GPU implementation without requiring hyper-parameter search."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Introduction, 2017, last author)

> "We emphasize that our simple detector achieves top results not based on innovations in network design but due to our novel loss."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §Introduction, 2017, middle author)

> "even without any bells and whistles, our non-local models can compete or outperform current competition winners on both Kinetics and Charades datasets."
> — Non-local Neural Networks (arXiv:1711.07971, §Abstract, 2017, last author)

> "Without using optical flow and without any bells and whistles, our method is on par with the heavily engineered results of the 2017 competition winner."
> — Non-local Neural Networks (arXiv:1711.07971, §Experiments, 2017, last author)

> "in my opinion the key design of uh the V networks are the uh modular modularization designs so in this case they just stack a lot of uh 3x3 convolutions uh following some very simple rules"
> — CVPR 2017 Tutorial Video (talk:talk_yt_cvpr2017, §Speech, 2017)

> "We note that we do not specially tailor the network width or filter sizes, nor use regularization techniques (such as dropout) which are very effective for these small datasets. We obtain these results via a simple but essential concept — going deepe"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Results, 2016, 1st author)

> "our method is simpler and adds no bells and whistles such as context or iterative box regression that were used by [9], and is faster for both training and testing."
> — R-FCN (arXiv:1605.06409, §Experiments, 2016, middle author)

> "We present a simple, highly modularized network architecture for image classification."
> — ResNeXt (arXiv:1611.05431, §Abstract, 2016, last author)

> "This simple rule reduces the free choices of hyper-parameters, and depth is exposed as an essential dimension in neural networks."
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "we argue that the simplicity of this rule may reduce the risk of over-adapting the hyper-parameters to a specific dataset."
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "we present a simple architecture which adopts VGG/ResNets' strategy of repeating layers, while exploiting the split-transform-merge strategy in an easy, extensible way."
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "Using FPN in a basic Faster R-CNN system, our method achieves state-of-the-art single-model results on the COCO detection benchmark without bells and whistles, surpassing all existing single-model entries including those from the COCO 2016 challenge winners."
> — FPN (Feature Pyramid Networks) (arXiv:1612.03144, §Abstract, 2016, middle author)

> "Simplicity is central to our design and we have found that our model is robust to many design choices."
> — FPN (Feature Pyramid Networks) (arXiv:1612.03144, §Method, 2016, middle author)

> "Identity shortcut connections add neither extra parameter nor computational complexity"
> — ResNet (arXiv:1512.03385, §Introduction, 2015, 1st author)

> "the small differences among A/B/C indicate that projection shortcuts are not essential for addressing the degradation proble"
> — ResNet (arXiv:1512.03385, §Ablation, 2015, 1st author)

> "we perform some information "aggregation" at a deeper stage of the network hierarchy (between convolutional layers and fully-connected layers) to avoid the need for cropping or warping at the beginning."
> — SPP-Net (arXiv:1406.4729, §Introduction, 2014, 1st author)

> "Our method avoids repeatedly computing the convolutional features. In processing test images, our method is 24-102 × faster than the R-CNN method, while achieving better or comparable accuracy on Pascal VOC 2007."
> — SPP-Net (arXiv:1406.4729, §Abstract, 2014, 1st author)

> "Generic components/"layers", less domain knowledge Repeat **elementary** layers: going deeper"
> — (source_id:talk_cvpr2017, §Slide: Learning Deep Features)

> "Simply "Very Deep"! Modularized design"
> — (source_id:talk_cvpr2017, §Slide: VGG-16/19)

> "Generic components, less domain knowledge Repeat **elementary** layers: going deeper"
> — (source_id:talk_cvpr2018, §Learning to represent)

> "Simply "Very Deep"! • Modularized design"
> — (source_id:talk_cvpr2018, §VGG-16/19)

> "Generic components, less domain knowledge Repeat **elementary** layers: going deeper"
> — (source_id:talk_eccv2018, §Learning to represent)

> "Simply "Very Deep"! • Modularized design"
> — (source_id:talk_eccv2018, §VGG-16/19)

> "Notably, unlike normalization layers, it achieves both effects without the need to compute activation statistics."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §Introduction, 2025, middle author)  *[voice_certain: false]*

> "Unlike previous approaches, DyT requires minimal modifications to both the architecture and the training recipe. Despite its simplicity, DyT achieves stable training and comparable performance."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §Discussion, 2025, middle author)  *[voice_certain: false]*

> "The core insight of the RegNet parametrization is surprisingly simple: widths and depths of good networks can be explained by a quantized linear function."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Abstract, 2020, middle author)  *[voice_certain: false]*

> "Surprisingly, we find that fixed-depth networks can match the performance of variable depth networks for all flop regimes, in both the average and best case."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "Surprisingly, this simple baseline not only remains effective for instance segmentation, but also yields a lightweight, top-performing method for semantic segmentation."
> — Panoptic FPN (arXiv:1901.02446, §Abstract, 2019, middle author)  *[voice_certain: false]*

> "we show that a simple, flexible, and effective architecture that can match accuracy for both tasks using a single network that simultaneously generates region-based outputs (for instance segmentation) and dense-pixel outputs (for semantic segmentation)."
> — Panoptic FPN (arXiv:1901.02446, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "Our model achieves state-of-the-art 3D detection on two large datasets of real 3D scans, ScanNet and SUN RGB-D with a simple design, compact model size and high efficiency. Remarkably, VoteNet outperforms previous methods by using purely geometric information without relying on color images."
> — VoteNet (arXiv:1904.09664, §Abstract, 2019, middle author)  *[voice_certain: false]*

> "While there can be many ways to cluster the votes, we opt for a simple strategy of uniform sampling and grouping according to spatial proximity."
> — VoteNet (arXiv:1904.09664, §VoteNet Architecture, 2019, middle author)  *[voice_certain: false]*

> "PointRend is a general module that admits many possible implementations. Viewed abstractly, a PointRend module accepts one or more typical CNN feature maps f(x_i, y_i) that are defined over regular grids, and outputs high-resolution predictions p(x′_i, y′_i) over a finer grid. Instead of making excessive predictions over all points on the output grid, PointRend makes predictions only on carefully selected points."
> — PointRend (arXiv:1912.08193, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "We will present a simple and effective PointRend implementation."
> — PointRend (arXiv:1912.08193, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "The task format we adopt for panoptic segmentation is simple: each pixel of an image must be assigned a semantic label and an instance id."
> — Panoptic Segmentation (arXiv:1801.00868, §Introduction, 2018, middle author)  *[voice_certain: false]*

> "We believe that the use of disjoint metrics is one of the primary reasons the community generally studies stuff and thing segmentation in isolation."
> — Panoptic Segmentation (arXiv:1801.00868, §Introduction, 2018, middle author)  *[voice_certain: false]*

> "In this work, we identify class imbalance as the primary obstacle preventing one-stage object detectors from surpassing top-performing, two-stage methods. To address this, we propose the focal loss which applies a modulating term to the cross entropy loss in order to focus learning on hard negative examples. Our approach is simple and highly effective."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §Conclusion, 2017, middle author)  *[voice_certain: false]*

> "There is no learnable layer after the RoI layer, enabling nearly cost-free region-wise computation and speeding up both training and inference."
> — R-FCN (arXiv:1605.06409, §Our approach, 2016, middle author)  *[voice_certain: false]*

> "In this paper, we show that an algorithmic change—computing proposals with a deep convolutional neural network—leads to an elegant and effective solution where proposal computation is nearly cost-free given the detection network's computation."
> — Faster R-CNN (arXiv:1506.01497, §Introduction, 2015, 2nd author)  *[voice_certain: false]*

> "Using the recently popular terminology of neural networks with 'attention' [ 31 ] mechanisms, the RPN module tells the Fast R-CNN module where to look."
> — Faster R-CNN (arXiv:1506.01497, §Method, 2015, 2nd author)  *[voice_certain: false]*

> "We have presented RPNs for efficient and accurate region proposal generation. By sharing convolutional features with the down-stream detection network, the region proposal step is nearly cost-free."
> — Faster R-CNN (arXiv:1506.01497, §Conclusion, 2015, 2nd author)  *[voice_certain: false]*


## Theme: deconstruction  (77 quotes)

> "It is widely believed that noise conditioning is indispensable for denoising diffusion models to work successfully. This work challenges this belief."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Abstract, 2025, last author)

> "We hope our findings will inspire the community to revisit the foundations and formulations of denoising generative models."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Abstract, 2025, last author)

> "Our experimental findings highlight that noise conditioning, though often helpful for improving quality, is not essential for the fundamental functionality of denoising generative models."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Experiments, 2025, last author)

> "Our study suggests that it is possible to pursue a single energy function E ​ ( x ) E(x) , aligning with the goal of classical EBM."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Discussion and Conclusion, 2025, last author)

> "In summary, noise conditioning has been predominant in modern denoising-based generative models and related approaches. We encourage the community to explore new models that are not constrained by this design."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Discussion and Conclusion, 2025, last author)

> "Nonetheless, it is still surprising to us that the actual non-linear transformation is highly similar to a scaled tanh function."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §What Do Normalization Layers Do?, 2025, middle author)

> "Despite encouraging results, the consistency constraint is imposed as a property of the network's behavior, while the properties of the underlying ground-truth field that should guide learning remain unknown."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Introduction, 2025, last author)

> "In contrast, our method is solely driven by the definition of average velocity, and the MeanFlow Identity ( Eq. 6 ) used for training is naturally derived from this definition, with no extra assumption."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Method, 2025, last author)

> "Today's denoising diffusion models do not "denoise" in the classical sense, i.e . , they do not directly predict clean images."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Abstract, 2025, last author)

> "In pursuit of a self-contained principle, there has been strong focus on advancing diffusion modeling in the pixel space. In general, these methods explicitly or implicitly avoid the information bottleneck in the networks. We suggest that these designs may stem from the demand to predict high-dimensional noised quantities."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Introduction, 2025, last author)

> "Noise is inherently different from natural data . Over the years, the development of diffusion models has focused primarily on probabilistic formulations, while paying less attention to the capabilities (and limitations) of the neural networks used."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Discussion and Conclusion, 2025, last author)

> "We challenge the conventional wisdom that the reverse process must be the exact analytic inverse of the forward process, and demonstrate that the long-held constraint is unnecessary."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Conclusion, 2025, last author)

> "A notable property of NFs is that the underlying flow trajectories from data to noise are learned rather than imposed. This differs from their modern continuous-time counterparts, such as Flow Matching, whose ground-truth trajectories are predetermined via time-scheduling."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Introduction, 2025, last author)

> "Learning the reverse model is not merely a form of distillation, even though we use a pre-trained forward model: in fact, our learned reverse model can outperform the explicit inverse"
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Introduction, 2025, last author)

> "Our findings indicate that the NF principle of learning the forward trajectories, rather than pre-scheduling them, can be advantageous and need not introduce inference-time limitations."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Introduction, 2025, last author)

> "We hypothesize this behavior may be related to overfitting, as evidenced by an increase in FID during training."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Experiments, 2025, last author)

> "Our philosophy is to deconstruct a DDM, gradually transforming it into a classical Denoising Autoencoder (DAE)"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Abstract, 2024, last author)

> "We observe that only a very few modern components are critical for learning good representations, while many others are nonessential."
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Abstract, 2024, last author)

> "At the core of our philosophy is to deconstruct a DDM, changing it step-by-step into a classical DAE."
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Introduction, 2024, last author)

> "Surprisingly, we discover that the main critical component is a tokenizer"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Introduction, 2024, last author)

> "Surprisingly, removing class-conditioning substantially improves the linear probe accuracy from 57.5% to 62.1%"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "To our further surprise, even the PCA tokenizer works well. Unlike the VAE or AE counterparts, the PCA tokenizer does not require gradient-based training. W"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "We undo many of the modern designs and conceptually retain only two designs inherited from modern DDM"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "Surprisingly, we observe that modern neural networks can achieve excellent accuracy in classifying which dataset an image is from"
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Abstract, 2024, last author)

> "We hope our discovery will inspire the community to rethink issues involving dataset bias."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Abstract, 2024, last author)

> "Our study is driven by the tension between building less biased datasets versus developing more capable models—the latter was less prominent at the time of Torralba & Efros (2011). While efforts to reduce bias in data may lead to progress, the development of advanced models could better exploit dataset bias and thus counteract the promise."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Introduction, 2024, last author)

> "To our (and many of our initial readers') surprise, modern neural networks can achieve excellent accuracy on such a dataset classification task."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Introduction, 2024, last author)

> "More surprisingly to us, we observe that self-supervised learning models are also highly capable of capturing certain bias among different datasets."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Introduction, 2024, last author)

> "the ability to capture dataset bias may be inherent in deep neural networks, rather than enabled by specific components."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Dataset Classification, 2024, last author)

> "Adding data augmentation makes it more difficult to memorize the training images, while we observe that using stronger data augmentation consistently improves the dataset classification accuracy."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Dataset Classification, 2024, last author)

> "We have discovered that such bias may contain some generalizable and transferrable patterns, and that it may not be easily noticed by human beings."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Conclusion, 2024, last author)

> "Conventional wisdom holds that autoregressive models for image generation are typically accompanied by vector-quantized tokens. We observe that while a discrete-valued space can facilitate representing a categorical distribution, it is not a necessity for autoregressive modeling."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Abstract, 2024, last author)

> "In this work, we aim to address the following question: Is it necessary for autoregressive models to be coupled with vector-quantized representations? We note that the autoregressive nature, i.e . , "predicting next tokens based on previous ones", is independent of whether the values are discrete or continuous."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Introduction, 2024, last author)

> "Our approach eliminates the need for discrete-valued tokenizers. Vector-quantized tokenizers are difficult to train and are sensitive to gradient approximation strategies."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Introduction, 2024, last author)

> "We propose several hypotheses for the performance gap. First, the vector quantization step, which is required for most visual autoregressive models, may introduce significant information loss, ultimately limiting model performance."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Introduction, 2024, last author)

> "while all models scale effectively in terms of validation loss, their evaluation performance—measured by FID, GenEval score, and visual quality—follows different trends."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Abstract, 2024, last author)

> "This paper does not describe a novel method. Instead, it studies a straightforward, incremental, yet must-know baseline given the recent progress in computer vision: self-supervised learning for Vision Transformers (ViT)."
> — MoCo v3 (arXiv:2104.02057, §Abstract, 2021, last author)

> "This indicates that linear classification accuracy is not monotonically related to transfer performance in detection."
> — MoCo v2 (arXiv:2003.04297, §Experiments, 2020, last author)

> "despite their wide use, there is currently little understanding of the relationship between the graph structure of the neural network and its predictive performance."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Abstract, 2020, last author)

> "there is currently little systematic understanding on the relation between a neural network's accuracy and its underlying graph structure."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Introduction, 2020, last author)

> "lack of generality: Computational graphs are constrained by the allowed graph properties, e.g., these graphs have to be directed and acyclic (DAGs), bipartite at the layer level, and single-in-single-out at the network level."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Introduction, 2020, last author)

> "In a nutshell, our method can be thought of as “BYOL without the momentum encoder”."
> — SimSiam (arXiv:2011.10566, §Introduction, 2020, last author)

> "Despite its great success, BN exhibits drawbacks that are also caused by its distinct behavior of normalizing along the batch dimension."
> — Group Normalization (arXiv:1803.08494, §Introduction, 2018, last author)

> "But the concept of "batch" is not always present, or it may change from time to time."
> — Group Normalization (arXiv:1803.08494, §Introduction, 2018, last author)

> "These issues lead to inconsistency at training, transferring, and testing time."
> — Group Normalization (arXiv:1803.08494, §Introduction, 2018, last author)

> "BN has been so influential that many state-of-the-art systems and their hyper-parameters have been designed for it, which may not be optimal for GN-based models."
> — Group Normalization (arXiv:1803.08494, §Discussion, 2018, last author)

> "We report competitive results on object detection and instance segmentation on the COCO dataset using standard models trained from random initialization . The results are no worse than their ImageNet pre-training counterparts"
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Abstract, 2018, 1st author)

> "Training from random initialization is surprisingly robust; our results hold even when: (i) using only 10% of the training data, (ii) for deeper and wider models, and (iii) for multiple tasks and metrics."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Abstract, 2018, 1st author)

> "Experiments show that ImageNet pre-training speeds up convergence early in training, but does not necessarily provide regularization or improve final target task accuracy."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Abstract, 2018, 1st author)

> "These observations challenge the conventional wisdom of ImageNet pre-training for dependent tasks and we expect these discoveries will encourage people to rethink the current de facto paradigm of 'pre-training and fine-tuning' in computer vision."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Abstract, 2018, 1st author)

> "these results are surprising and challenge our understanding of the effects of ImageNet pre-training. These observations hint that ImageNet pre-training is a historical workaround (and will likely be so for some time) for when the community does not have enough target data or computational resources"
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Introduction, 2018, 1st author)

> "ImageNet pre-training does not automatically give better regularization. When training with fewer images (down to 10% of COCO), we find that new hyper-parameters must be selected for fine-tuning (from pre-training) to avoid overfitting."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Introduction, 2018, 1st author)

> "The Two-Stream method has not explored the potential of different temporal speeds, a key concept in our method."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "it is methodologically unsatisfactory given that optical flow is a hand-designed representation, and two-stream methods are often not learned end-to-end jointly with the flow."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "Repeating local operations has several limitations. First, it is computationally inefficient. Second, it causes optimization difficulties that need to be carefully addressed."
> — Non-local Neural Networks (arXiv:1711.07971, §Introduction, 2017, last author)

> "This comparison shows that non-local dependency has not been sufficiently captured by existing models despite increased depth/capacity."
> — Non-local Neural Networks (arXiv:1711.07971, §Experiments, 2017, last author)

> "although careful combinations of these components yield excellent neural network recipes, it is in general unclear how to adapt the Inception architectures to new datasets/tasks"
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "So why do CNNs require a fixed input size? A CNN mainly consists of two parts: convolutional layers, and fully-connected layers that follow. The convolutional layers operate in a sliding-window manner and output feature maps which represent the spatial arrangement of the activations. In fact, convolutional layers do not require a fixed image size and can generate feature maps of any sizes. On the other hand, the fully-connected layers need to have fixed-size/length input by their definition. Hence, the fixed-size constraint comes only from the fully-connected layers"
> — SPP-Net (arXiv:1406.4729, §Introduction, 2014, 1st author)

> "It is worth noticing that the gain of multi-level pooling is not simply due to more parameters; rather, it is because the multi-level pooling is robust to the variance in object deformations and spatial layout."
> — SPP-Net (arXiv:1406.4729, §SPP-net for Image Classification, 2014, 1st author)

> "Note that the above single/multi-size solutions are for training only. At the testing stage, it is straightforward to apply SPP-net on images of any sizes."
> — SPP-Net (arXiv:1406.4729, §Deep Networks with Spatial Pyramid Pooling, 2014, 1st author)

> "Our exploration starts with the observation that LN layers map their inputs to outputs with tanh-like, S-shaped curves, scaling the input activations while squashing the extreme values."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §Introduction, 2025, middle author)  *[voice_certain: false]*

> "in recent years, novel architectures often seek to replace attention or convolution layers, but almost always retain the normalization layers."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §Introduction, 2025, middle author)  *[voice_certain: false]*

> "We hypothesize this non-linear and disproportional squashing effect on extreme values is what makes normalization layers important and indispensable."
> — Transformers without Normalization (DyT) (arXiv:2503.10622, §What Do Normalization Layers Do?, 2025, middle author)  *[voice_certain: false]*

> "we analyze the RegNet design space and arrive at interesting findings that do not match the current practice of network design."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Abstract, 2020, middle author)  *[voice_certain: false]*

> "we find that the depth of the best models is stable across compute regimes (∼20 blocks) and that the best models do not use either a bottleneck or inverted bottleneck."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Introduction, 2020, middle author)  *[voice_certain: false]*

> "the depth of best models is stable across regimes (top-left), with an optimal depth of ∼20 blocks (60 layers). This is in contrast to the common practice of using deeper models for higher flop regimes."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "we observe that the inverted bottleneck degrades the EDF slightly and depthwise conv performs even worse relative to b=1 and g≥1"
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "Contrary to [29], we find that for RegNetX a fixed resolution of 224×224 is best, even at higher flops."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "As depth sensors only capture surfaces of objects, 3D object centers are likely to be in empty space, far away from any point. As a result, point based networks have difficulty aggregating scene context in the vicinity of object centers."
> — VoteNet (arXiv:1904.09664, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "A regular grid will unnecessarily oversample the smooth areas while simultaneously undersampling object boundaries. The result is excess computation in smooth regions and blurry contours."
> — PointRend (arXiv:1912.08193, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "machine RQ is dramatically lower than human RQ, especially on ADE20k and Vistas. This implies that recognition, i.e., classification, is the main challenge for current methods."
> — Panoptic Segmentation (arXiv:1801.00868, §Machine Performance Baselines, 2018, middle author)  *[voice_certain: false]*

> "We discover that the extreme foreground-background class imbalance encountered during training of dense detectors is the central cause."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §Abstract, 2017, middle author)  *[voice_certain: false]*

> "rather than addressing outliers, our focal loss is designed to address class imbalance by down-weighting inliers (easy examples) such that their contribution to the total loss is small even if their number is large. In other words, the focal loss performs the opposite role of a robust loss: it focuses training on a sparse set of hard examples."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §Focal Loss, 2017, middle author)  *[voice_certain: false]*

> "while we use the focal loss definition above, its precise form is not crucial. In the appendix we consider other instantiations of the focal loss and demonstrate that these can be equally effective."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §Focal Loss, 2017, middle author)  *[voice_certain: false]*

> "We argue that the aforementioned unnatural design is caused by a dilemma of increasing translation invariance for image classification vs. respecting translation variance for object detection."
> — R-FCN (arXiv:1605.06409, §Introduction, 2016, middle author)  *[voice_certain: false]*

> "this naïve solution turns out to have considerably inferior detection accuracy that does not match the network's superior classification accuracy"
> — R-FCN (arXiv:1605.06409, §Introduction, 2016, middle author)  *[voice_certain: false]*

> "The good performance of sharing parameters indicates that all levels of our pyramid share similar semantic levels."
> — FPN (Feature Pyramid Networks) (arXiv:1612.03144, §Method, 2016, middle author)  *[voice_certain: false]*


## Theme: ablation-discipline  (59 quotes)

> "Contrary to common belief, we find that many denoising generative models perform robustly even in the absence of noise conditioning. In this scenario, most methods exhibit only a modest degradation in generation performance."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Introduction, 2025, last author)

> "More surprisingly, we find that some relevant methods—particularly flow-based ones, which originated from different perspectives—can even produce improved generation results without noise conditioning."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Introduction, 2025, last author)

> "Table 2 shows that when using independent noise, the contrastive loss fails to improve generation quality in all cases studied."
> — Diffuse and Disperse (arXiv:2506.09027, §Experiments, 2025, last author)

> "Notably, we compare a wide range of temperature values τ and find that the results are surprisingly robust: this is in contrary to contrastive self-supervised learning, where performance degrades significantly when deviating from the optimal temperature."
> — Diffuse and Disperse (arXiv:2506.09027, §Experiments, 2025, last author)

> "Even more surprisingly, we find that, conversely, introducing a bottleneck that reduces dimensionality in the network can be beneficial."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Method, 2025, last author)

> "Unlike translation invariance, which can be partially addressed by patchification (i.e., a special form of convolution), the ViT architecture has little to no inductive bias about scale invariance. This can explain why scale augmentation yields a substantial gain."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Experiments, 2025, last author)

> "We hypothesize that overtraining on the test tasks may cause the model to forget the knowledge acquired during offline training."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Experiments, 2025, last author)

> "Despite the encouraging results of the original MF, we identify two major issues that remain unresolved: (i) the training target in the original MF is network-dependent and therefore does not constitute a standard regression problem; (ii) MF handles the classifier-free guidance (CFG) using a fixed training-time guidance scale, which sacrifices flexibility."
> — Improved Mean Flows (arXiv:2512.02012, §Introduction, 2025, last author)

> "This comparison may look counterintuitive, because the form of V θ (z t , e − x) seems to "leak" the regression target."
> — Improved Mean Flows (arXiv:2512.02012, §Method, 2025, last author)

> "We hypothesize that when the model has more capacity, it can better leverage the capacity to learn v θ by u θ (z t , t, t), and therefore benefits more from this formulation."
> — Improved Mean Flows (arXiv:2512.02012, §Experiments, 2025, last author)

> "The naive distillation approach, trained with a simple MSE objective, already outperforms the exact inverse baseline, indicating that a learned reverse model is a practical and competitive alternative to the analytic inverse."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Experiments, 2025, last author)

> "Directly mapping pure noise to data in one step is highly under-constrained, making it difficult for the reverse network to learn a reliable inverse from a single reconstruction loss."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Method, 2025, last author)

> "This behavior suggests that the neural network attempts to discover dataset-specific patterns—a form of bias–to solve the dataset classification task."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Introduction, 2024, last author)

> "this game even becomes way easier given today's capable neural networks. In this sense, the issue involving dataset bias has not been relieved."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Introduction, 2024, last author)

> "Even very small models can achieve strong accuracy for the dataset classification task. A ConvNeXt with as few as 7K parameters (3/10000 of ResNet-50) achieves 72.4% accuracy on classifying YCD."
> — Decade's Battle on Dataset Bias (arXiv:2403.08632, §Dataset Classification, 2024, last author)

> "the token generation order and the associated attention mechanism primarily influence the global structure of the generated image."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Introduction, 2024, last author)

> "We find that the FPN design is not necessary in the case of a plain ViT backbone and its benefit can be effectively gained by a simple pyramid built from a large-stride (16), single-scale map."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Method, 2022, last author)

> "Our ablation reveals that the set of pyramidal feature maps, rather than the top-down/lateral connections, is the key to effective multi-scale detection."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Experiments, 2022, last author)

> "The optimal masking ratio we observe is 90%. This is in line with the common assumption that natural videos are more information-redundant than images because of temporal coherence."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Method, 2022, last author)

> "While masking creates a distribution shift between training and inference, simply ignoring this shift works surprisingly well, even under the zero-shot setting where no training is ever done on full images."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Experiments, 2022, last author)

> "We hypothesize that masking as a form of noise and regularization can improve robustness."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Experiments, 2022, last author)

> "even spending more computation by schedule scaling gives diminishing returns. These comparisons suggest that large-scale data are beneficial mainly because they provide richer information."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Experiments, 2022, last author)

> "We observe that instability is a major issue that degrades accuracy, and it can be hidden by apparently good results. We reveal that these results are indeed partial failure, and they can be improved when training is made more stable."
> — MoCo v3 (arXiv:2104.02057, §Abstract, 2021, last author)

> "Interestingly, we observe that unstable ViT training may not result in catastrophic failure ( e.g . , divergence); instead, it can cause mild degradation in accuracy ( e.g . , 1 ∼ 3%). Such a degree of degradation may not be noticeable, unless a more stable counterpart is available for comparison."
> — MoCo v3 (arXiv:2104.02057, §Introduction, 2021, last author)

> "This behavior is harmful to explorative research: unlike catastrophic failure that is easily noticeable, the small degradation can be fully hidden."
> — MoCo v3 (arXiv:2104.02057, §Method, 2021, last author)

> "Surprisingly, the model works decently even with no position embedding (74.9%). The capability to encode positions contributes only 1.6%. We believe this data point reveals both strengths and limitations of the current model."
> — MoCo v3 (arXiv:2104.02057, §Experiments, 2021, last author)

> "We hope this work will provide useful data points and experience for future research."
> — MoCo v3 (arXiv:2104.02057, §Abstract, 2021, last author)

> "There is no clear performance difference between contrastive/non-contrastive methods. This indicates that learning space-time persistence within a video is key for the methods, but learning in-persistence across videos is not."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Experiments, 2021, last author)

> "There is a clear difference of ∼ 4% on K400 between methods that employ momentum encoders (MoCo, BYOL), vs these that do not (SimCLR, SwAV)."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Experiments, 2021, last author)

> "we discover that encouraging long-spanned persistency can be effective even if the timespan is 60 seconds."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Abstract, 2021, last author)

> "Table 1 shows that linear probing and fine-tuning results are largely uncorrelated ."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Ablation, 2021, 1st author)

> "two design improvements used in SimCLR, namely, an MLP projection head and stronger data augmentation, are orthogonal to the frameworks of MoCo and SimCLR"
> — MoCo v2 (arXiv:2003.04297, §Introduction, 2020, last author)

> "the MLP head and data augmentation are orthogonal to how contrastive learning is instantiated."
> — MoCo v2 (arXiv:2003.04297, §Background, 2020, last author)

> "The existence of the collapsing solutions implies that it is insufficient for our method to prevent collapsing solely by the architecture design"
> — SimSiam (arXiv:2011.10566, §Ablation, 2020, last author)

> "we have seen no evidence that they are related to collapse prevention. It is mainly the stop-gradient operation that plays an essential role."
> — SimSiam (arXiv:2011.10566, §Ablation, 2020, last author)

> "Figure 4 (left) shows that GN has lower training error than BN, indicating that GN is effective for easing optimization. The slightly higher validation error of GN implies that GN loses some regularization ability of BN."
> — Group Normalization (arXiv:1803.08494, §Experiments, 2018, last author)

> "Our goal is to ablate the role of ImageNet pre-training via controlled experiments that can be done without ImageNet pre-training. Given this goal, architectural improvements are not our purpose"
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Method, 2018, 1st author)

> "It is unrealistic and unfair to expect models trained from random initialization to converge similarly fast as those initialized from ImageNet pre-training. Overlooking this fact one can draw incomplete or incorrect conclusions about the true capability of models that are trained from scratch."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Method, 2018, 1st author)

> "the extra parameters are not the main reason for our accuracy improvements; feature denoising appears to be a general approach particularly useful for adversarial robustness."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Experiments, 2018, last author)

> "we observe that the SlowFast network is empirically more effective."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "the Fast pathway alone has only 51.7% accuracy (Table 5a). But it brings in up to 3.0% improvement to the Slow pathway, showing that the underlying representation modeled by the Fast pathway is largely complementary."
> — SlowFast Networks (arXiv:1812.03982, §Experiments, 2018, last author)

> "we found it essential to decouple mask and class prediction: we predict a binary mask for each class independently, without competition among classes"
> — Mask R-CNN (arXiv:1703.06870, §Introduction, 2017, 1st author)

> "This suggests that once the instance has been classified as a whole (by the box branch), it is sufficient to predict a binary mask without concern for the categories, which makes the model easier to train."
> — Mask R-CNN (arXiv:1703.06870, §Ablation, 2017, 1st author)

> "our comprehensive experiments show that optimization difficulty is the main issue with large minibatches, rather than poor generalization (at least on ImageNet), in contrast to some recent studies."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Introduction, 2017, last author)

> "The random variation of ImageNet models has generally not been reported in previous work (largely due to resource limitations). We emphasize that ignoring random variation may cause unreliable conclusions, especially if results are from a single trial, or the best of many."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Experiments, 2017, last author)

> "if the optimization issues are addressed, there is no apparent generalization degradation observed using large minibatch training, even if the minibatch size goes from 256 to 8k."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Experiments, 2017, last author)

> "Interestingly, we will show by experiments (Table 2a) that our non-local models are not sensitive to these choices, indicating that the generic non-local behavior is the main reason for the observed improvements."
> — Non-local Neural Networks (arXiv:1711.07971, §Method, 2017, last author)

> "the improvement of non-local blocks is not just because they add depth to the baseline model."
> — Non-local Neural Networks (arXiv:1711.07971, §Experiments, 2017, last author)

> "the 32×4d ResNeXt also has a much lower training error than the ResNet counterpart, suggesting that the gains are not from regularization but from stronger representations."
> — ResNeXt (arXiv:1611.05431, §Experiments, 2016, last author)

> "Our studies also show that many time-proven techniques/insights in computer vision can still play important roles in deep-networks-based recognition."
> — SPP-Net (arXiv:1406.4729, §Conclusion, 2014, 1st author)

> "**Caution** : make sure your BN usage is correct! (this causes many of my bugs in my research experience!)"
> — (source_id:talk_cvpr2017, §Slide: Batch Normalization (BN))

> "**2 AP better** than SOTA w/ R101, without bells and whistles **200ms / img**"
> — (source_id:talk_iccv2017, §Instance Segmentation Results on COCO)

> "comparing distributions is more robust and informative than using search (manual or automated) and comparing the best found models from two design spaces."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "as our focus is on evaluating network architectures, we perform carefully controlled experiments under the same training setup. In particular, to provide fair comparisons to classic work, we do not use any training-time enhancements."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Experiments, 2020, middle author)  *[voice_certain: false]*

> "We have observed that the losses from these two branches have different scales and normalization policies. Simply adding them degrades the final performance for one of the tasks."
> — Panoptic FPN (arXiv:1901.02446, §Panoptic Feature Pyramid Network, 2019, middle author)  *[voice_certain: false]*

> "voting boosts the performance by a significant margin of ∼ 5 mAP on SUN RGB-D and > 13 mAP on ScanNet."
> — VoteNet (arXiv:1904.09664, §Experiments, 2019, middle author)  *[voice_certain: false]*

> "In general we note that it is robust to the exact design of the point head MLP. Changes of its depth or width do not show any significant difference in our experiments."
> — PointRend (arXiv:1912.08193, §Experiments: Instance Segmentation, 2019, middle author)  *[voice_certain: false]*

> "We found these higher-level design decisions to be more important than specific values of hyperparameters."
> — Focal Loss / RetinaNet (arXiv:1708.02002, §RetinaNet Detector, 2017, middle author)  *[voice_certain: false]*

> "We show by experiments that the results are insensitive to λ in a wide range."
> — Faster R-CNN (arXiv:1506.01497, §Method, 2015, 2nd author)  *[voice_certain: false]*


## Theme: generality  (54 quotes)

> "We hope this work could open a new paradigm in generative modeling and provide a fertile ground for future research."
> — Fractal Generative Models (arXiv:2502.17437, §Abstract, 2025, last author)

> "pixel-by-pixel generation represents a broader class of important generative problems: modeling non-sequential data with intrinsic structures, which is particularly important for many data types beyond images, such as molecular structures, proteins, and biological neural networks."
> — Fractal Generative Models (arXiv:2502.17437, §Introduction, 2025, last author)

> "the regularizer improves over the baseline by a substantial margin in all cases studied, showing the generality of our approach."
> — Diffuse and Disperse (arXiv:2506.09027, §Experiments, 2025, last author)

> "The strength of a general-purpose Transformer is partly in that, when its design is decoupled from the specific task, it can benefit from architectural advances developed in other applications."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Method, 2025, last author)

> "By minimizing domain-specific designs, we hope that the general "Diffusion + Transformer" paradigm originated from computer vision will find broader applicability."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Introduction, 2025, last author)

> "We demonstrate that incorporating visual priors is crucial. These priors include 2D spatial locality, translation invariance, and scale invariance."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Introduction, 2025, last author)

> "A patch on the canvas can consist of exponentially many color combinations, which helps reduce overfitting and encourages the model to learn spatial priors rather than merely memorize."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Method, 2025, last author)

> "In image recognition, even highly capable network architectures still benefit greatly from translation and scale augmentations. We draw similar observations in ARC."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Experiments, 2025, last author)

> "our reverse model 𝒢 ϕ is not constrained by explicit invertibility. As a result, this allows us to design the reverse model with arbitrary architectures (e.g., bidirectional attention-based Transformers) and training objectives."
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Method, 2025, last author)

> "BiFlow provides a flexible supervised-learning framework for tackling the generation problem. This flexibility stems from two key properties of BiFlow: (i) 1-NFE generation — the learned reverse model produces a sample x′ in a single forward pass"
> — Bidirectional Normalizing Flow (arXiv:2512.10953, §Method, 2025, last author)

> "We hope this work will motivate the use of autoregressive generation in other continuous-valued domains and applications."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Abstract, 2024, last author)

> "These models do not need to be constrained by vector-quantized representations. We hope our work will motivate the research community to explore sequence models with continuous-valued representations in other domains."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Discussion and Conclusion, 2024, last author)

> "we want to pre-train task-agnostic and embodiment-agnostic foundational models that can map raw sensor signals from individual embodiments into a shared latent space."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Introduction, 2024, last author)

> "pre-training on additional embodiment datasets such as simulation and human video datasets can be possible, despite the large embodiment gaps with real robots."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Experiments, 2024, last author)

> "these pre-training procedures and models can simplify building reliable robotic policies for new embodiments and new tasks in terms of data requirements and generalized performance."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Introduction, 2024, last author)

> "this discovery of transfer learning is so influential that its impact is far beyond just computer vision"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "again this demonstrate the generality of the deep learning methodology that is to say if we develop a very effective and very general component from from one application then it is likely that you are going to enjoy the benefit in some other applications"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "We believe this approach has the potential to liberate image generation from the constraints of human annotations, enabling it to fully harness the vast amounts of unlabeled data and even generalize to modalities that are beyond the scope of human annotation capabilities."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Discussion, 2023, last author)

> "If this direction is successful, it will enable the use of original ViT backbones for object detection; this will decouple the pre-training design from the fine-tuning demands, maintaining the independence of upstream vs. downstream tasks."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Introduction, 2022, last author)

> "it becomes reasonable to pursue a backbone that involves fewer inductive biases, since the backbone may be trained effectively using large-scale data and/or self-supervision."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Method, 2022, last author)

> "Our exploration has demonstrated that plain-backbone detection is a promising research direction. This methodology largely maintains the independence of the general-purpose backbones and the downstream task-specific designs."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Conclusion, 2022, last author)

> "Towards unifying methodologies, less domain knowledge ("fewer inductive biases") is introduced for a specific problem, which urges the models to learn useful knowledge almost purely from data."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Introduction, 2022, last author)

> "It is practically valuable for self-supervised learning methods to be less dependent on data augmentation. There are a variety of applications in which augmentation is not valid or is hard to induce"
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Experiments, 2022, last author)

> "We find that it is possible to learn strong representations with minimal domain knowledge or inductive biases. This follows the spirit of the ViT paper."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Conclusion, 2022, last author)

> "our results indicate that unsupervised pre-training can be a new paradigm for all of these downstream tasks, for which supervised pre-training is the de-facto standard to achieve best performance."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Experiments, 2021, last author)

> "a fixed-width MLP is a special case under a much more general model family, where the message function, aggregation function, and most importantly, the relation graph structure can vary."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Method, 2020, last author)

> "our findings are consistent across many different tasks and datasets"
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Abstract, 2020, last author)

> "our work offers a unified view of GNNs and general neural architecture design, which we hope can bridge the two communities and inspire new innovations."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Discussion, 2020, last author)

> "Notably, we achieve competitive results using a standard ResNet-50 and require no specific architecture designs"
> — MoCo v1 (arXiv:1911.05722, §Ablation, 2019, 1st author)

> "The usage of BN often requires these systems to compromise between the model design and batch sizes."
> — Group Normalization (arXiv:1803.08494, §Introduction, 2018, last author)

> "The robust results of GN in Table 2 demonstrate GN's strength. It allows to remove the batch size constraint imposed by BN, which can give considerably more memory."
> — Group Normalization (arXiv:1803.08494, §Experiments, 2018, last author)

> "Mean filters reduce noise but also smooth structures, so it is reasonable to expect them to perform worse than the above weighted means. However, somewhat surprisingly, experiments show that denoising blocks using mean filters as the denoising operation can still improve adversarial robustness."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "Median filters are known to be good at removing salt-and-pepper noise and outliers of similar kind. Training convolutional networks that contain median filters is an open problem, but we find experimentally that using median filters as a denoising operation can also improve adversarial robustness."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "We note that minimal domain knowledge for human pose is exploited by our system, as the experiments are mainly to demonstrate the generality of the Mask R-CNN framework."
> — Mask R-CNN (arXiv:1703.06870, §Method, 2017, 1st author)

> "Given the effectiveness of Mask R-CNN for extracting object bounding boxes, masks, and keypoints, we expect it be an effective framework for other instance-level tasks."
> — Mask R-CNN (arXiv:1703.06870, §Method, 2017, 1st author)

> "we observed no generalization issues when transferring across datasets (from ImageNet to COCO) and across tasks (from classification to detection/segmentation) using models trained with large minibatches."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Experiments, 2017, last author)

> "we present non-local operations as an efficient, simple, and generic component for capturing long-range dependencies with deep neural networks."
> — Non-local Neural Networks (arXiv:1711.07971, §Introduction, 2017, last author)

> "non-local operations maintain the variable input sizes and can be easily combined with other operations."
> — Non-local Neural Networks (arXiv:1711.07971, §Introduction, 2017, last author)

> "Together with the evidence on videos, these image experiments show that non-local operations are generally useful and can become a basic building block in designing deep neural networks."
> — Non-local Neural Networks (arXiv:1711.07971, §Introduction, 2017, last author)

> "On all tasks, a simple addition of non-local blocks provides solid improvement over baselines."
> — Non-local Neural Networks (arXiv:1711.07971, §Conclusion, 2017, last author)

> "Our network is constructed by repeating a building block that aggregates a set of transformations with the same topology."
> — ResNeXt (arXiv:1611.05431, §Abstract, 2016, last author)

> "This strong evidence shows that the residual learning principle is generic, and we expect that it is applicable in other vision and non-vision problems"
> — ResNet (arXiv:1512.03385, §Introduction, 2015, 1st author)

> "This gain is solely due to the learned representations."
> — ResNet (arXiv:1512.03385, §Ablation, 2015, 1st author)

> "The advantages of SPP are orthogonal to the specific CNN designs. In a series of controlled experiments on the ImageNet 2012 dataset, we demonstrate that SPP improves four different CNN architectures in existing publications (or their modifications), over the no-SPP counterparts. These architectures have various filter numbers/sizes, strides, depths, or other designs."
> — SPP-Net (arXiv:1406.4729, §Introduction, 2014, 1st author)

> "SPP is a flexible solution for handling different scales, sizes, and aspect ratios. These issues are important in visual recognition, but received little consideration in the context of deep networks."
> — SPP-Net (arXiv:1406.4729, §Conclusion, 2014, 1st author)

> "Engine of Visual Recognition ResNets/extensions are leading models on popular benchmarks"
> — (source_id:talk_cvpr2017, §Slide: Engine of Visual Recognition)

> "**Search "ResNet" on ILSVRC2016** **result page returns 226 entries**"
> — (source_id:talk_cvpr2017, §Slide: Engine of Visual Recognition)

> "**Feature still matters!**"
> — (source_id:talk_cvpr2017, §Slide: ResNeXt for Mask R-CNN)

> "our aim is to find simple models that are easy to understand, build upon, and generalize."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Introduction, 2020, middle author)  *[voice_certain: false]*

> "We show that without changes, FPN can also be highly effective for semantic segmentation."
> — Panoptic FPN (arXiv:1901.02446, §Introduction, 2019, middle author)  *[voice_certain: false]*

> "panoptic segmentation is not a multitask problem but rather a single, unified view of image segmentation. Specifically, the multitask setting allows for independent and potentially inconsistent outputs for stuff and things, while PS requires a single coherent scene segmentation."
> — Panoptic Segmentation (arXiv:1801.00868, §Introduction, 2018, middle author)  *[voice_certain: false]*

> "We intentionally keep the R-FCN system presented in the paper simple. There have been a series of orthogonal extensions of FCNs that were developed for semantic segmentation, as well as extensions of region-based methods for object detection. We expect our system will easily enjoy the benefits of the progress in the field."
> — R-FCN (arXiv:1605.06409, §Conclusion and Future Work, 2016, middle author)  *[voice_certain: false]*

> "The resulting Feature Pyramid Network is general-purpose and in this paper we focus on sliding window proposers (Region Proposal Network, RPN for short) [ 29 ] and region-based detectors (Fast R-CNN) [ 11 ]."
> — FPN (Feature Pyramid Networks) (arXiv:1612.03144, §Method, 2016, middle author)  *[voice_certain: false]*

> "An important property of our approach is that it is translation invariant , both in terms of the anchors and the functions that compute proposals relative to the anchors."
> — Faster R-CNN (arXiv:1506.01497, §Method, 2015, 2nd author)  *[voice_certain: false]*


## Theme: scaling  (40 quotes)

> "We further observe a promising scaling trend: increasing the model size from 186M to 848M parameters substantially improves the FID from 11.80 to 6.15 and the Recall from 0.29 to 0.46."
> — Fractal Generative Models (arXiv:2502.17437, §Experiments, 2025, last author)

> "Consistent with the behavior of Transformer-based diffusion/flow models (DiT [ 34 ] and SiT [ 33 ] ), MeanFlow models exhibit promising scalability for 1-NFE generation."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Ablation, 2025, last author)

> "training from scratch can produce highly competitive fastforward models."
> — Improved Mean Flows (arXiv:2512.02012, §Experiments, 2025, last author)

> "Similar to autoregressive language models, we observe encouraging scaling behavior. Further investigation into scaling could be promising."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Experiments, 2024, last author)

> "A historical lesson that has revolutionized machine learning is that pre-training on large-scale, high-quality, and diverse data can bring general models that usually outperform specific models."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Introduction, 2024, last author)

> "Analogous to the scaling laws, we found that to some extent, HPT scales with the dataset quantity and diversity as well as the model and training compute."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Introduction, 2024, last author)

> "We do not find a significant difference between scaling depth or scaling width."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Experiments, 2024, last author)

> "Scaling up autoregressive models in vision has not proven as beneficial as in large language models."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Abstract, 2024, last author)

> "We hope our findings and results will encourage future efforts to further bridge the scaling gap between vision and language models."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Abstract, 2024, last author)

> "We hypothesize that power-law scaling applies to (a) for autoregressive models on vision data, but not necessarily to (b)."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Introduction, 2024, last author)

> "simply using a GPT-like language model for images in a straightforward way may not scale well. To improve scaling for visual data, further adaptations such as continuous tokens and random-order generation are needed."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Experiments, 2024, last author)

> "raster-order models with discrete tokens (blue line) reach a plateau in both FID and GenEval scores around 1B parameters."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Experiments, 2024, last author)

> "ML research should adapt to the growth of compute"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 414, 2024)

> "today's gigantic models can be future's daily routine"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 426, 2024)

> "Scalability: Your research vs. Moore's law"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Takeaways, 2024)

> "The scale of data we have explored is orders of magnitudes smaller than the language counterparts. While our method has largely improved the efficiency of self-supervised learning, the high-dimensional video data still present a major challenge for scaling up."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Conclusion, 2022, last author)

> "This design introduces a trade-off between "how carefully we look at a sample pair" vs. "how many sample pairs we can process"."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Introduction, 2022, last author)

> "Empirically, the benefits of processing more sample pairs greatly outweigh the degradation of per-sample encoding, resulting in a favorable trade-off."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Introduction, 2022, last author)

> "CLIP is an outstanding example of "simple algorithms that scale well". The simple design of CLIP allows it to be relatively easily executed at substantially larger scales."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Discussion, 2022, last author)

> "Language provides rich information for supervision. Therefore, scaling, which can involve increasing capacity (model scaling) and increasing information (data scaling), is essential for attaining good results in language-supervised training."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Discussion, 2022, last author)

> "data scaling is a favored scaling dimension, given that it can improve accuracy with no extra cost at training or inference time."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Discussion, 2022, last author)

> "a larger model desires more data to unleash its potential."
> — FLIP (Masked CLIP) (arXiv:2212.00794, §Experiments, 2022, last author)

> "Simple algorithms that scale well are the core of deep learning."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Discussion, 2021, 1st author)

> "Self-supervised learning in vision may now be embarking on a similar trajectory as in NLP."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Discussion, 2021, 1st author)

> "the MoCo framework can process a large set of negative samples without requiring large training batches"
> — MoCo v2 (arXiv:2003.04297, §Introduction, 2020, last author)

> "Table 2 and 3 suggest that large batches are not necessary for good accuracy, and state-of-the-art results can be made more accessible."
> — MoCo v2 (arXiv:2003.04297, §Experiments, 2020, last author)

> "MoCo’s improvement from IN-1M to IG-1B is consistently noticeable but relatively small, suggesting that the larger-scale data may not be fully exploited."
> — MoCo v1 (arXiv:1911.05722, §Discussion, 2019, 1st author)

> "Scale matters. We are in an unprecedented era in AI research history in which the increasing data and model scale is rapidly improving accuracy in computer vision, speech, and natural language processing."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Introduction, 2017, last author)

> "larger datasets and neural network architectures consistently yield improved accuracy across all tasks that benefit from pre-training."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Introduction, 2017, last author)

> "the training curves can be used as a reliable proxy for success well before training finishes."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Experiments, 2017, last author)

> "the deeper the model is the lower the training and uh validation areas are"
> — CVPR 2017 Tutorial Video (talk:talk_yt_cvpr2017, §Speech, 2017)

> "These results suggest that there is much room to exploit the dimension of network depth , a key to the success of modern deep learning."
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Introduction, 2016, 1st author)

> "increasing cardinality is more effective than going deeper or wider when we increase the capacity."
> — ResNeXt (arXiv:1611.05431, §Abstract, 2016, last author)

> "we emphasize that while it is relatively easy to increase accuracy by increasing capacity (going deeper or wider), methods that increase accuracy while maintaining (or reducing) complexity are rare in the literature."
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "Experiments demonstrate that increasing cardinality is a more effective way of gaining accuracy than going deeper or wider, especially when depth and width starts to give diminishing returns for existing models."
> — ResNeXt (arXiv:1611.05431, §Introduction, 2016, last author)

> "The performance on ImageNet-1K appears to saturate. But we argue that this is not because of the capability of the models but because of the complexity of the dataset."
> — ResNeXt (arXiv:1611.05431, §Experiments, 2016, last author)

> "Our focus is on the behaviors of extremely deep networks, but not on pushing the state-of-the-art results, so we intentionally use simple architectures as follows."
> — ResNet (arXiv:1512.03385, §Ablation, 2015, 1st author)

> "Revolution of Depth"
> — (source_id:talk_cvpr2017, §Slide: Revolution of Depth)

> "**Deep features** empower amazing visual recognition results"
> — (source_id:talk_cvpr2017, §Slide: Conclusion: Features Matter!)

> "for EfficientNet, activations scale linearly with flops (due to the scaling of both resolution and depth), compared to activations scaling with the square-root of flops for RegNets. This leads to slow GPU training and inference times for EfficientNet."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Experiments, 2020, middle author)  *[voice_certain: false]*


## Theme: self-supervision  (35 quotes)

> "We observe that the representations produced by a strong self-supervised encoder can also capture a lot of semantic attributes without human supervision, as reflected by their transfer learning performance in the literature."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Introduction, 2023, last author)

> "This potentially enables pre-training of the self-supervised encoder and image generator on large-scale unlabeled datasets, and task-specific training of conditional representation generator on a small-scale labeled dataset."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Experiments, 2023, last author)

> "MAE pre-training on IN-1K (without labels) shows massive gains, increasing AP box by 3.1 for ViT-B and 4.6 for ViT-L."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Experiments, 2022, last author)

> "the plain ViT backbone may benefit more from MAE pre-training than the hierarchical backbone, suggesting that the lack of inductive biases on scales could be compensated by the self-supervised training of MAE."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Experiments, 2022, last author)

> "Our study suggests that the general framework of masked autoencoding (BERT, MAE, etc.) can be a unified methodology for representation learning with minimal domain knowledge."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Abstract, 2022, last author)

> "Despite minimal inductive biases, our method achieves strong empirical results, suggesting that useful knowledge can be learned from data."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Introduction, 2022, last author)

> "We hypothesize that the higher-dimensional video data are more complex and thus require higher decoding capacity."
> — ST-MAE (Spatiotemporal MAE) (arXiv:2205.09113, §Experiments, 2022, last author)

> "Moreover, as a promising signal, our bigger self-supervised ViT can achieve better accuracy, unlike the ImageNet-supervised ViT in [ 16 ] whose accuracy degrades if getting bigger."
> — MoCo v3 (arXiv:2104.02057, §Introduction, 2021, last author)

> "These comparisons suggest that self-supervised learning as a tool for generic representation learning is less prone to over-fitting."
> — MoCo v3 (arXiv:2104.02057, §Experiments, 2021, last author)

> "we study a simple objective that can easily generalize all these methods to space-time."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Abstract, 2021, last author)

> "in spite of its simplicity, it works surprisingly well across: (i) different unsupervised frameworks, (ii) pre-training datasets, (iii) downstream datasets, and (iv) backbone architectures."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Abstract, 2021, last author)

> "we report a few promising cases in which unsupervised pre-training can outperform its supervised counterpart."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Abstract, 2021, last author)

> "Our hypothesis is that the visual content is often temporally-persistent along a timespan in the video."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Introduction, 2021, last author)

> "Our objective is a natural generalization of crops in images to clips in videos. This allows us to make use of the recent unsupervised learning frameworks with minimal modifications."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Introduction, 2021, last author)

> "unsupervised pre-training can achieve competitive performance in videos, and it can surpass the supervised pre-training counterparts in a few cases."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Introduction, 2021, last author)

> "Our MAE approach is simple: we mask random patches of the input image and reconstruct the missing pixels."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Abstract, 2021, 1st author)

> "Images, on the contrary, are natural signals with heavy spatial redundancy"
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Introduction, 2021, 1st author)

> "The optimal ratios are surprisingly high. The ratio of 75% is good for both linear probing and fine-tuning."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Ablation, 2021, 1st author)

> "Surprisingly, our MAE behaves decently even if using no data augmentation (only center-crop, no flipping)."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Ablation, 2021, 1st author)

> "In MAE, the role of data augmentation is mainly performed by random masking (ablated next). The masks are different for each iteration and so they generate new training samples regardless of data augmentation."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Ablation, 2021, 1st author)

> "We hypothesize that this behavior occurs by way of a rich hidden representation inside the MAE."
> — MAE (Masked Autoencoders) (arXiv:2111.06377, §Discussion, 2021, 1st author)

> "we report surprising empirical results that simple Siamese networks can learn meaningful representations even using none of the following: (i) negative sample pairs, (ii) large batches, ("
> — SimSiam (arXiv:2011.10566, §Abstract, 2020, last author)

> "Our experiments show that collapsing solutions do exist for the loss and structure, but a stop-gradient operation plays an essential role in preventing collapsing. W"
> — SimSiam (arXiv:2011.10566, §Abstract, 2020, last author)

> "Our simple baseline suggests that the Siamese architectures can be an essential reason for the common success of the related methods"
> — SimSiam (arXiv:2011.10566, §Introduction, 2020, last author)

> "Our hypothesis is that SimSiam is an implementation of an Expectation-Maximization (EM) like algorithm. It implicitly involves two sets of variables,"
> — SimSiam (arXiv:2011.10566, §Method, 2020, last author)

> "We emphasize that all these methods are highly successful for transfer learning"
> — SimSiam (arXiv:2011.10566, §Discussion, 2020, last author)

> "From this perspective, we hypothesize that it is desirable to build dictionaries that are: (i) large and (ii) consistent as they evolve during training."
> — MoCo v1 (arXiv:1911.05722, §Introduction, 2019, 1st author)

> "Our hypothesis is that good features can be learned by a large dictionary that covers a rich set of negative sample"
> — MoCo v1 (arXiv:1911.05722, §Method, 2019, 1st author)

> "The introduction of a queue decouples the dictionary size from the mini-batch size. Our dictionary size can be much larger than a typical mini-batch size, a"
> — MoCo v1 (arXiv:1911.05722, §Method, 2019, 1st author)

> "We hypothesize that such failure is caused by the rapidly changing encoder that reduces the key representation"
> — MoCo v1 (arXiv:1911.05722, §Method, 2019, 1st author)

> "a relatively large momentum ( e.g . , m 𝑚 m = = 0.999 , our default) works much better than a smaller value"
> — MoCo v1 (arXiv:1911.05722, §Method, 2019, 1st author)

> "The model appears to “cheat” the pretext task and easily finds a low-loss solution. This is possibly because the intra-batch communication among samples (caused by BN) leaks information."
> — MoCo v1 (arXiv:1911.05722, §Method, 2019, 1st author)

> "This paper’s focus is on a mechanism for general contrastive learning; we do not explore orthogonal factor"
> — MoCo v1 (arXiv:1911.05722, §Ablation, 2019, 1st author)

> "MoCo can outperform its supervised pre-training counterpart in 7 detection/segmentation tasks on PASCAL VOC, COCO, and other datasets, sometimes surpassing it by large margins. T"
> — MoCo v1 (arXiv:1911.05722, §Abstract, 2019, 1st author)

> "our study suggests that the community should be more careful when evaluating pre-trained features ( e.g . , for self-supervised learning), as now we learn that even random initialization could produce excellent results."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Discussion, 2018, 1st author)


## Theme: residual  (27 quotes)

> "the introduction of this simple component can enable neural networks with hundreds of layers to train from scratch and to achieve better accuracy"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "The residual connection allows us to insert a new non-local block into any pre-trained model, without breaking its initial behavior."
> — Non-local Neural Networks (arXiv:1711.07971, §Method, 2017, last author)

> "a deeper model has a richer solution space and a deeper model should not have higher trending error than its shallower counterparts"
> — CVPR 2017 Tutorial Video (talk:talk_yt_cvpr2017, §Speech, 2017)

> "the degradation problem uh observed in experiment indicate that there might be some optimization difficulties in the current servers so the servers cannot just find a solution when we uh create deeper and deeper models"
> — CVPR 2017 Tutorial Video (talk:talk_yt_cvpr2017, §Speech, 2017)

> "Our experiments empirically show that training in general becomes easier when the architecture is closer to the above two conditions."
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Introduction, 2016, 1st author)

> "whereas skip connections of scaling, gating [ 5 , 6 , 7 ] , and 1 × \times 1 convolutions all lead to higher training loss and error. T"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Introduction, 2016, 1st author)

> "These experiments suggest that keeping a “clean” information path (indicated by the grey arrows in Fig. 1 , 2 , and 4 ) is helpful for easing optimization. T"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Introduction, 2016, 1st author)

> "This implies that the gradient of a layer does not vanish even when the weights are arbitrarily small"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Method, 2016, 1st author)

> "It is noteworthy that the gating and 1 × \times 1 convolutional shortcuts introduce more parameters, and should have stronger representational abilities than identity shortcuts."
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Method, 2016, 1st author)

> "Multiplicative manipulations (scaling, gating, 1 × \times 1 convolutions, and dropout) on the shortcuts can hamper information propagation and lead to optimization problems."
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Method, 2016, 1st author)

> "Our derivations imply that identity shortcut connections and identity after-addition activation are essential for making information propagation smooth"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Conclusion, 2016, 1st author)

> "These comparisons suggest that the residual connections are helpful for optimization, whereas aggregated transformations are stronger representations."
> — ResNeXt (arXiv:1611.05431, §Experiments, 2016, last author)

> "We hypothesize that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping"
> — ResNet (arXiv:1512.03385, §Introduction, 2015, 1st author)

> "Unexpectedly, such degradation is not caused by overfitting , and adding more layers to a suitably deep model leads to higher training error , as"
> — ResNet (arXiv:1512.03385, §Introduction, 2015, 1st author)

> "The degradation problem suggests that the solvers might have difficulties in approximating identity mappings by multiple nonlinear layer"
> — ResNet (arXiv:1512.03385, §Method, 2015, 1st author)

> "If the optimal function is closer to an identity mapping than to a zero mapping, it should be easier for the solver to find the perturbations with reference to an identity mapping,"
> — ResNet (arXiv:1512.03385, §Method, 2015, 1st author)

> "These results support our basic motivation (Sec. 3.1 ) that the residual functions might be generally closer to zero than the non-residual functions. W"
> — ResNet (arXiv:1512.03385, §Ablation, 2015, 1st author)

> "_Plain_ nets: stacking 3x3 conv layers… 56-layer net has **higher training error** and test error than 20-layer net"
> — (source_id:talk_cvpr2017, §Slide: Simply stacking layers?)

> "A deeper model should not have **higher** **training error** - A solution _by construction_ :"
> — (source_id:talk_cvpr2017, §Slide: Simply stacking layers?)

> "If identity were optimal, easy to set weights as 0 If optimal mapping is closer to identity, easier to find small fluctuations"
> — (source_id:talk_cvpr2017, §Slide: Deep Residual Learning)

> "Deep ResNets can be trained without difficulties Deeper ResNets have **lower training error**, and also lower test error"
> — (source_id:talk_cvpr2017, §Slide: CIFAR-10 experiments)

> "A deeper model should not have **higher** **training error**"
> — (source_id:talk_cvpr2018, §Simply stacking layers?)

> "If identity were optimal, easy to set weights as 0 If optimal mapping is closer to identity, easier to find small fluctuations"
> — (source_id:talk_cvpr2018, §Deep Residual Learning)

> "Deep ResNets can be trained without difficulties • Deeper ResNets have lower training error, and also lower test error"
> — (source_id:talk_cvpr2018, §CIFAR-10 experiments)

> "A deeper model should not have **higher** **training error**"
> — (source_id:talk_eccv2018, §Simply stacking layers?)

> "If identity were optimal, easy to set weights as 0 If optimal mapping is closer to identity, easier to find small fluctuations"
> — (source_id:talk_eccv2018, §Deep Residual Learning)

> "Deep ResNets can be trained without difficulties • Deeper ResNets have lower training error, and also lower test error"
> — (source_id:talk_eccv2018, §CIFAR-10 experiments)


## Theme: recognition-generation-duality  (18 quotes)

> "The development of diffusion-based generative models over the past decade has largely proceeded independently of progress in representation learning."
> — Diffuse and Disperse (arXiv:2506.09027, §Abstract, 2025, last author)

> "This paradigm for image generation stands in contrast to its counterpart in image recognition, where representation learning has been a core topic and a driving force over the past decade."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "It is difficult to disentangle whether the improvements from representation alignment arise from a self-supervised objective or primarily from increased compute and access to external data."
> — Diffuse and Disperse (arXiv:2506.09027, §Introduction, 2025, last author)

> "Since AlexNet, **recognition** models have been generally **end-to-end** ..."
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §A Bit of History, 2025)

> "Today's generative models are conceptually like "layer-wise training""
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §History Repeating in Generative Models?, 2025)

> "**Recognition: Abstraction** **Genera5on: Concre5za5on**"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Recognition vs. Generation: Two Sides of the Same Coin?, 2025)

> "**Recognition** "Flow" from data to embeddings"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Recognition vs. Generation: Two Sides of the Same Coin?, 2025)

> "**Generation** : "Flow" from embeddings to data"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Recognition vs. Generation: Two Sides of the Same Coin?, 2025)

> "Recognition vs. Generation: **flows** between distributions Flow Matching: builds **ground-truth** fields for training"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Key takeaways so Far, 2025)

> "We want **integral**, but in practice we do **finite sum**"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Key takeaways so Far, 2025)

> "Towards **feedforward** **end-to-end** , generative modeling?"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Key takeaways so Far, 2025)

> "What's a good formulation for **end-to-end** generative modeling?"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Looking ahead, 2025)

> "The effectiveness of Diffusion Loss on various autoregressive models suggests new opportunities: modeling the interdependence of tokens by autoregression, jointly with the per-token distribution by diffusion."
> — MAR (Autoregressive without VQ) (arXiv:2406.11838, §Discussion and Conclusion, 2024, last author)

> "Random-order models can readjust the global structure at every prediction step, whereas raster-order models cannot. This suggests that the token generation order plays a crucial role in achieving better text-to-image alignment."
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Introduction, 2024, last author)

> "We show that one can close this gap by generating semantic representations in the representation space produced by a self-supervised encoder. These representations can be used to condition the image generator."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Abstract, 2023, last author)

> "We hypothesize that such a performance gap is because human-annotated conditioning introduces rich semantic information to simplify the generative process."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Introduction, 2023, last author)

> "Surprisingly, with RCG, these generative models consistently outperform their class-conditional versions by a noticeable margin. This demonstrates that the rich semantic information from the unconditionally generated representations can guide the generative process even more effectively than class labels."
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Experiments, 2023, last author)

> "Computer vision has entered a new era where learning from extensive, unlabeled datasets is becoming increasingly common. Despite this trend, the training of image generation models still mostly relies on labeled datasets"
> — RCG (Return of Unconditional Generation) (arXiv:2312.03701, §Discussion, 2023, last author)


## Theme: pixels-over-tokens  (10 quotes)

> "Existing methods that directly model the pixel sequence do not achieve satisfactory results in both likelihood estimation and generation quality, as images do not embody a clear sequential order."
> — Fractal Generative Models (arXiv:2502.17437, §Introduction, 2025, last author)

> "Unlike models that rely on tokenizers, our method is free from the reconstruction errors introduced by tokenization, suggesting the potential for uncapped performance gains with larger model capacities."
> — Fractal Generative Models (arXiv:2502.17437, §Experiments, 2025, last author)

> "In contrast, a limited-capacity network can still predict the clean data, as it only needs to retain the low-dimensional information while filtering out the noise."
> — JiT (Back to Basics: Let DGM Denoise) (arXiv:2511.13720, §Introduction, 2025, last author)

> "we formulate ARC within a vision paradigm, framing it as an image-to-image translation problem."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Abstract, 2025, last author)

> "although the ARC puzzles are typically presented visually, existing research has rarely framed ARC as a vision-centric problem."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Introduction, 2025, last author)

> "Abstraction and inference can arise directly from visual learning, without explicit linguistic intermediates."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Introduction, 2025, last author)

> "Previous methods on ARC generally operate in the space of discrete-valued tokens, motivated by the design of language models. In our formulation of image-to-image translation, we explore native designs developed for vision."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Method, 2025, last author)

> "Our work explores a previously overlooked perspective in the ARC task by framing it as an image-to-image translation problem. It naturally enables the adaptation of visual frameworks and yields strong few-shot generalization"
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Conclusion, 2025, last author)

> "This opens up a new possibility of treating ARC as a vision-centric problem, emphasizing abstraction and reasoning emerging directly from image pixels."
> — ARC Is a Vision Problem! (arXiv:2511.14761, §Conclusion, 2025, last author)

> "The visual quality of models using discrete tokens is significantly worse than that of models using continuous tokens"
> — Fluid (Continuous-token T2I) (arXiv:2410.13863, §Experiments, 2024, last author)


## Theme: research-methodology  (12 quotes)

> "Are we still in the **pre-AlexNet** era of generative modeling?"
> — Towards End-to-End Generative Modeling (CVPR 2025 Workshop) (talk:talk_cvpr2025_meanflow, §Looking ahead, 2025)

> "• **Into the fog** • **No oracle map** • **Is there even a destination?** • **What's on the other side of the land?** • **And: what will it mean for us?**"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §Age of Discoveries, 2025)

> "Research is SGD in a chaotic landscape"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 16, 2024)

> "Research is about : risk taking bias/var tradeoff explore vs. exploit"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 51, 2024)

> "ML concerns 'Expectation'; Research looks for 'Surprise'"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 146, 2024)

> ""surprise" : unexpected attempt " what if ?": novel possibility"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 183, 2024)

> "Challenging common wisdom Extending the horizon of knowledge "Surprise" will become new "expectation"; repeat Research is SGD, w/ large or small lr"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 235, 2024)

> "Future is the Real Test Set"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 247, 2024)

> "Your "state-of-the-art" is about the past Help the community to achieve the next "sota""
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Slide 362, 2024)

> "Research is SGD in a chaotic landscape Look for 'surprise' Future is the real test set"
> — ML Research, via the Lens of ML (NeurIPS 2024 New-in-ML) (talk:talk_neurips2024_newinml, §Takeaways, 2024)

> "deep learning is representation learning"
> — Learning Deep Representations (MIT Bootcamp) (talk:talk_yt_mit2024, §Speech, 2024)

> "in my understanding the success of deep learning is the success of feature learning so in the case of uh visual recognition features uh still matter"
> — CVPR 2017 Tutorial Video (talk:talk_yt_cvpr2017, §Speech, 2017)


## Theme: other  (83 quotes)

> "Remarkably, the bound estimation can be computed without training the neural networks: it can be evaluated solely based on the schedules and the dataset."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Method, 2025, last author)

> "We hope that rethinking the role of noise conditioning will open up new opportunities."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Discussion and Conclusion, 2025, last author)

> "Our study also reveals that certain families of models, e.g ., Flow Matching, can be more robust to the removal of t t -conditioning. Although these models are closely related to diffusion, they can be formulated from a substantially different perspective—estimating a flow field between two distributions."
> — Is Noise Conditioning Necessary (arXiv:2502.13129, §Discussion and Conclusion, 2025, last author)

> "This approach is motivated by the observation that much of this data exhibits a near-fractal structure: images are composed of sub-images, molecules are composed of sub-molecules, and biological neural networks are composed of sub-networks."
> — Fractal Generative Models (arXiv:2502.17437, §Method, 2025, last author)

> "Our study largely closes the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will inspire future work to reconsider the foundations of these powerful models."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Introduction, 2025, last author)

> "Our formulation involves describing the underlying quantity at coarsened levels of granularity, a common theme that underlies many important applications in physics."
> — MeanFlow (NeurIPS 2025 Oral) (arXiv:2505.13447, §Conclusion, 2025, last author)

> "We hope this encouraging result represents a solid step towards stand-alone fastforward generation."
> — Improved Mean Flows (arXiv:2512.02012, §Conclusion, 2025, last author)

> "the use of a tokenizer begins to incur a non-negligible cost at inference time. While our work focuses on advancing fast-forward models and is orthogonal to tokenizer design, from a practical standpoint, reducing or removing the tokenizer is becoming increasingly valuable."
> — Improved Mean Flows (arXiv:2512.02012, §Conclusion, 2025, last author)

> "**What Is Object Detection?** recognition + localization"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §What Is Object Detection?, 2025)

> "**Faster R-CNN: Everything in Deep Learning**"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §Faster R-CNN slide, 2025)

> "Among first real usages of **differentiable programming**"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §Faster R-CNN slide, 2025)

> "A conceptual shift in CV from " **architectures** " to " " **programs**"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §Faster R-CNN slide, 2025)

> "Urged software to adopt better **abstractions** (e.g., PyTorch)"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §Faster R-CNN slide, 2025)

> "**What's the missing piece?** hand-crafted regions"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §What's the missing piece?, 2025)

> "• Write object detection papers and win Test of Time Awards :)"
> — Brief History of Visual Object Detection (NeurIPS 2025 Test-of-Time) (talk:talk_neurips2025_fasterrcnn, §What Have We Learned Over the Past Decades?, 2025)

> "Overall, the results in Tab. 1 reveal that self-supervised learning performance is not correlated to generation quality ."
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "We hypothesize that directly conditioning the model on class labels may reduce the model’s demands on encoding the information related to class labels."
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "Using multiple levels of noise is analogous to a form of data augmentation in DAE: it is beneficial, but not an enabling factor. T"
> — l-DAE (Deconstructing DDM) (arXiv:2401.14404, §Method, 2024, last author)

> "One of the roadblocks for training generalist robotic models today is heterogeneity."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Abstract, 2024, last author)

> "Different from other fields, robotics has less data quantity and diversity but much more heterogeneity."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Related Works, 2024, last author)

> "the trainable parameters (stem and head) can be as few as 2% of the parameters."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Experiments, 2024, last author)

> "robot learning is still limited by its generality because of the heterogeneity, including different embodiments, tasks, and environments where the robots are operated."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Conclusion, 2024, last author)

> "We hypothesize that training with more embodiments contributes to the generalization of the trunk."
> — HPT (Heterogeneous Pre-trained Transformers) (arXiv:2409.20537, §Experiments, 2024, last author)

> "We hypothesize that this is because ViT can rely on positional embedding for encoding locations and also because the high-dimensional ViT patch embeddings do not necessarily discard information."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Method, 2022, last author)

> "We hypothesize that the way for a plain backbone to achieve scale equivariance is to learn the prior knowledge from data, analogous to how it learns translation equivariance and locality without convolutions."
> — ViTDet (Plain ViT for detection) (arXiv:2203.16527, §Method, 2022, last author)

> "There is no benefit from restricting the time window of positives, which can be interpreted as the objective of learning extremely-slow features that do not change over 60 seconds of video."
> — Large-Scale Spatiotemporal SSL Study (arXiv:2104.14558, §Experiments, 2021, last author)

> "top-performing neural networks have graph structure surprisingly similar to those of real biological neural networks."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Abstract, 2020, last author)

> "Surprisingly, models trained after 3 epochs already have a high correlation (0.93), which means that good relational graphs perform well even at the early training epochs."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Results, 2020, last author)

> "after training to convergence, the extracted graphs are no longer E-R random graphs and move towards the sweet spot region we found"
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Discussion, 2020, last author)

> "the U-shape correlation in Figure 4(b)(d) might indicate a trade-off between message exchange efficiency and capability of learning distributed representations."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Results, 2020, last author)

> "there are a few special cases where learning the graph structure can be superior (i.e., when the task is simple and the network capacity is abundant)."
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Discussion, 2020, last author)

> "even though a ResNet-34 has much higher complexity than a 5-layer MLP, and ImageNet is a much more challenging dataset than CIFAR-10, a fixed set relational graphs would perform similarly in both settings"
> — Graph Structure of Neural Networks (arXiv:2007.06559, §Results, 2020, last author)

> "The channels of visual representations are not entirely independent."
> — Group Normalization (arXiv:1803.08494, §Method, 2018, last author)

> "it is not necessary to think of deep neural network features as unstructured vectors."
> — Group Normalization (arXiv:1803.08494, §Method, 2018, last author)

> "applying BN to the box head (that has 512 RoIs per image) does not provide satisfactory result and is ∼ 9 AP worse — in detection, the batch of RoIs are sampled from the same image and their distribution is not i.i.d."
> — Group Normalization (arXiv:1803.08494, §Experiments, 2018, last author)

> "Is ImageNet pre-training necessary? No—if we have enough target data (and computation). Our experiments show that ImageNet can help speed up convergence, but does not necessarily improve accuracy unless the target dataset is too small"
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Discussion, 2018, 1st author)

> "Looking forward, when the community will proceed with more data and faster computation, our study suggests that collecting data and training on the target tasks is a solution worth considering, especially when there is a significant gap between the source pre-training task and the target task."
> — Rethinking ImageNet Pre-training (arXiv:1811.08883, §Introduction, 2018, 1st author)

> "adversarial perturbations on images lead to noise in the features constructed by these networks"
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Abstract, 2018, last author)

> "the perturbation of the features induced by an adversarial image gradually increases as the image is propagated through the network, and non-existing activations in the feature maps are hallucinated."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "the transformations performed by the layers in the network exacerbate the perturbation, and the hallucinated activations can overwhelm the activations due to the true signal, which leads the network to make wrong predictions."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "only the non-local means operation in the denoising block is actually doing the denoising; the 1×1 convolutions and the residual connection are mainly for feature combination."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "denoising features in itself is not sufficient. As suppressing noise may also remove useful signals, it appears essential to properly combine the denoised features with the input features in denoising blocks."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Experiments, 2018, last author)

> "By contrast, feature denoising leads to consistent improvements in white-box settings, suggesting that feature denoising blocks make it more difficult to fool networks."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Experiments, 2018, last author)

> "there are certain architecture designs (viz., denoising blocks) that are particularly good for adversarial robustness, even though they do not lead to accuracy improvements compared to baseline models in "clean" training and testing scenarios."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Discussion, 2018, last author)

> "it is difficult to quantitatively measure this noise. We found it is nontrivial to compare feature noise levels between different models"
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "Interestingly, we find that it is unnecessary to embed x in the dot-product version of non-local means for the model to work well. This is unlike the Gaussian non-local means, in which embedding is essential."
> — Feature Denoising for Adversarial Robustness (arXiv:1812.03411, §Method, 2018, last author)

> "The categorical spatial semantics of the visual content often evolve slowly."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "If all spatiotemporal orientations are not equally likely, then there is no reason for us to treat space and time symmetrically."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "this pathway is designed to have fewer channels and weaker ability to process spatial information, while such information can be provided by the first pathway in a less redundant manner."
> — SlowFast Networks (arXiv:1812.03982, §Introduction, 2018, last author)

> "The good results of our model suggest that it is a desired tradeoff for the Fast pathway to weaken its spatial modeling ability while strengthening its temporal modeling ability."
> — SlowFast Networks (arXiv:1812.03982, §Method, 2018, last author)

> "The time axis is a special dimension."
> — SlowFast Networks (arXiv:1812.03982, §Conclusion, 2018, last author)

> "the minibatch size n over which the BN statistics are computed is a key component of the loss: if the per-worker minibatch sample size n is changed, it changes the underlying loss function L that is optimized."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Method, 2017, last author)

> "the BN statistics should not be computed across all workers, not only for the sake of reducing communication, but also for maintaining the same underlying loss function being optimized."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Method, 2017, last author)

> "Setting γ=0 in the last BN of each residual block causes the forward/backward signal initially to propagate through the identity shortcut of ResNets, which we found to ease optimization at the start of training."
> — Accurate, Large Minibatch SGD (1-Hour ImageNet) (arXiv:1706.02677, §Experiments, 2017, last author)

> "it is more likely that the non-local behavior is important, and it is insensitive to the instantiations."
> — Non-local Neural Networks (arXiv:1711.07971, §Experiments, 2017, last author)

> "Somehow surprisingly, when BN and ReLU are both used as pre-activation, the results are improved by healthy margins"
> — Identity Mappings (ResNet v2) (arXiv:1603.05027, §Ablation, 2016, 1st author)

> "PReLU improves model fitting with nearly zero extra computational cost and little overfitting ris"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Abstract, 2015, 1st author)

> "Glorot and Bengio [ 7 ] proposed to adopt a properly scaled uniform distribution for initialization. This is called “ Xavier ” initialization in [ 14 ] . I"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "A proper initialization method should avoid reducing or magnifying the magnitudes of input signals exponentially"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "If the forward/backward signal is inappropriately scaled by a factor β 𝛽 \beta in each layer, then the final propagated signal will be rescaled by a f"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "In this paper, we investigate neural networks from two aspects particularly driven by the rectifiers"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Introduction, 2015, 1st author)

> "the learned model tends to keep more information in earlier stages and becomes more discriminative in deeper stages"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "Though our attempts of extremely deep models have not shown benefits, our initialization method paves a foundation for further study on increasing dept"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "We choose to increase the model width instead of depth, because deeper models have only diminishing improvement or even degradation on accuracy"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Method, 2015, 1st author)

> "While our algorithm produces a superior result on this particular dataset, this does not indicate that machine vision outperforms human vision on object recognition in general. O"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Ablation, 2015, 1st author)

> "This improvement is obtained with almost no computational cost"
> — PReLU + Kaiming init (Delving Deep into Rectifiers) (arXiv:1502.01852, §Ablation, 2015, 1st author)

> "We conjecture that the deep plain nets may have exponentially low convergence rates, which impact the reducing of the training error"
> — ResNet (arXiv:1512.03385, §Ablation, 2015, 1st author)

> "Deep Learning is Representation Learning"
> — (source_id:talk_cvpr2018, §Title slide)

> "**Caution** : make sure your BN usage is correct! (this causes many of my bugs in my research experience!)"
> — (source_id:talk_cvpr2018, §Batch Normalization (BN))

> "• Deep Learning is Representation Learning • Represent data for machines to perform tasks (this talk) • Represent data for machines to perform tasks (next talks)"
> — (source_id:talk_cvpr2018, §Conclusion)

> "Deep Learning is Representation Learning"
> — (source_id:talk_eccv2018, §Title slide)

> "**Caution** : make sure your BN usage is correct! (this causes many of my bugs in my research experience!)"
> — (source_id:talk_eccv2018, §Batch Normalization (BN))

> "• Deep Learning is Representation Learning • Represent data for machines to perform tasks (this talk) • Represent data for machines to perform tasks (next talks)"
> — (source_id:talk_eccv2018, §Conclusion)

> "• Independent of batch size • Robust to small batches • Enable new scenarios: e.g.: 41 AP on COCO trained from scratch"
> — (source_id:talk_eccv2018, §Teaser : Group Normalization (GN))

> "**Goals** of Mask R-CNN üGood speed üGood accuracy ü Intuitive ü Easy to use"
> — (source_id:talk_iccv2017, §Instance Segmentation)

> "**Equivariance** : changes in input lead to corresponding changes in output _Classification_ desires _invariant_ representations: output a label"
> — (source_id:talk_iccv2017, §Invariance vs. Equivariance)

> "_Instance Seg._ desires _equivariant_ representations: Translated object => translated mask Scaled object => scaled mask _Big and small_ objects are equally important (due to AP metric)"
> — (source_id:talk_iccv2017, §Invariance vs. Equivariance)

> "Easy, fast to implement and train"
> — (source_id:talk_iccv2017, §Parallel Heads)

> "RoIPool _breaks_ pixel-to-pixel translation-equivariance"
> — (source_id:talk_iccv2017, §RoIAlign vs. RoIPool)

> "Mask R-CNN üGood speed üGood accuracy ü Intuitive ü Easy to use ü Equivariance matters"
> — (source_id:talk_iccv2017, §Conclusion)

> "RegNet models are surprisingly effective in this regime considering the substantial body of work on finding better mobile networks via both manual design and NAS."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Experiments, 2020, middle author)  *[voice_certain: false]*

> "Interestingly, if g is restricted to be 1 (depthwise conv), Swish performs much better than ReLU. This suggests that depthwise conv and Swish interact favorably, although the underlying reason is not at all clear."
> — RegNet (Designing Network Design Spaces) (arXiv:2003.13678, §Method, 2020, middle author)  *[voice_certain: false]*

> "By analogizing classical computer graphics methods for efficient rendering with over- and undersampling challenges faced in pixel labeling tasks, we develop a unique perspective of image segmentation as a rendering problem."
> — PointRend (arXiv:1912.08193, §Abstract, 2019, middle author)  *[voice_certain: false]*
