---
title: "Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference"
summary: Conducted the first systematic energy profiling of on-device VLM inference, revealing that autoregressive decoding—not visual token processing—dominates energy consumption (86–97%), overturning conventional assumptions about visual token reduction as the primary efficiency strategy.
date: 2026-03-27
type: docs
tags:
  - Vision-Language Models
  - Energy Profiling
  - Edge Inference
  - On-Device AI
  - Embodied AI
image:
  caption: 'VLM inference pipeline: input encoding, concatenation, and two-phase LLM inference'
---
<a href="https://arxiv.org/abs/2607.09520" target="_blank">
  <img src="https://img.shields.io/badge/arXiv%20Preprint-2607.09520-b31b1b?logo=arxiv&logoColor=white" alt="arXiv PDF">
</a>
<a href="https://junfei-z.github.io/vlm/" target="_blank">
  <img src="https://img.shields.io/badge/Project%20Page-Interactive%20Demo-blue?logo=googlechrome&logoColor=white" alt="Project Page">
</a>

📄 [Accepted at ACM MM 2026] — To appear. The camera-ready version is not yet online; please refer to the [arXiv preprint](https://arxiv.org/abs/2607.09520) and the [interactive project page](https://junfei-z.github.io/vlm/).

Vision-Language Models (VLMs) are the perceptual backbone of embodied AI, but their energy footprint on edge hardware remains poorly understood. Existing efficiency efforts focus predominantly on reducing visual tokens, implicitly treating visual processing as the dominant energy cost. We overturn this implicit assumption through the **first systematic energy profiling** of on-device VLM inference, spanning five models across three architecture families, four input resolutions, and two hardware platforms (NVIDIA RTX 3070 and Jetson Orin NX).

## Key Findings

Our analysis yields three core findings:

### 1. Power is a Model Fingerprint
Average inference power is a **model-intrinsic constant**, invariant to input resolution, image complexity, and prompt type, with less than 5% variation across all conditions. This means that all energy variation across inputs must arise from variation in **inference time**, not from variation in power draw.

### 2. Decode Dominates Energy
Autoregressive decoding accounts for **86 to 97% of total energy**. Each output token costs **11 to 39x more** wall-clock time than each input token due to the compute-bound and memory-bound asymmetry between prefill and decode phases. Output token count is the dominant driver of both latency and energy.

### 3. The Visual Token Pruning Illusion
Even removing **all visual tokens** saves at most **10% of total energy** for fixed-token models. In contrast, controlling output length by 50% saves up to **97%**. These findings expose a fundamental limitation of visual token pruning: it targets prefill, which is already a minority of total energy.

## Contributions

- **Energy decomposition** into prefill vs. decode phases, showing decode dominance across all configurations
- **Theoretical upper bound** on energy savings from visual token pruning
- **Cross-model energy predictor** — a linear model with five features (model size, input token count, output token count, and interaction terms) that explains **98.6% of energy variance** without per-model calibration (MAPE = 10.3%)
- **Deployment guidelines**: budget output not input; match token strategy to deployment scenario; anticipate content-driven energy variation

## Conclusion

The true energy bottleneck in edge VLM inference is not *seeing* but *speaking*: not what the model sees, but how much it says. Our energy decomposition framework provides actionable guidelines for energy-aware VLM deployment on resource-constrained edge devices.

## Citation

The paper is accepted at ACM MM 2026 and the proceedings version is not yet online. Please cite the arXiv preprint:

```bibtex
@misc{zhan2026seeing,
  title         = {Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference},
  author        = {Zhan, Junfei and Shen, Haoxun and Guo, Mingang and Huang, Zixuan and He, Tengjiao},
  year          = {2026},
  eprint        = {2607.09520},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  url           = {https://arxiv.org/abs/2607.09520},
  note          = {Accepted to the 34th ACM International Conference on Multimedia (ACM MM 2026)}
}
```
