---
title: Stochastic Power Modeling and Constrained MDP Optimization for On-Device SLM Inference
summary: Proposed a unified stochastic framework combining HSMM-based power modeling and constrained MDP optimization to enable sustainable deployment of small language models (SLMs) on edge devices.
date: 2025-09-22
type: docs
tags:
  - Small Language Models
  - On-Device Inference
  - Hidden Semi-Markov Models
  - Constrained MDP
  - Energy–Quality Trade-off
image:
  caption: 'Energy-aware SLM inference with HSMM-driven CMDP optimization'
---

📄 [ICASSP 2026 Submission] — In Review

This research introduces a **stochastic and interpretable framework** for sustainable **on-device inference of small language models (SLMs)** under strict energy and hardware constraints. By capturing fine-grained CPU/GPU power dynamics and optimizing inference scheduling with constrained MDPs, the work provides a principled foundation for **adaptive, resource-aware AI at the edge**.

## Problem and Motivation

Running SLMs locally on smartphones, laptops, or IoT nodes promises **low-latency and privacy-preserving AI services**, but these devices face **finite battery budgets** and **strict power caps**. Traditional energy models fail to capture the stochastic, phase-wise CPU/GPU behaviors of SLM inference, making them unsuitable for **multi-task adaptive deployment**.

## Technical Contributions

### 1. HSMM-Based Energy Modeling
- Conducted fine-grained power measurements of **Gemma2-2B** and **Qwen3-4B** on MT-Bench.
- Modeled CPU and GPU traces separately with **Hidden Semi-Markov Models (HSMMs)**:
  - GPU: ramp-up, plateau, decay phases.
  - CPU: low-load and high-load bursts.
- Achieved **higher fidelity than HMM and TCN baselines** in predicting power fluctuations.

### 2. Constrained MDP Formulation
- Defined a **CMDP** where each inference task selects an SLM configuration (model + quantization).
- State: remaining energy budget.
- Actions: candidate SLM setups.
- Reward: **LLM-as-a-Judge quality scores**.
- Constraints: **finite energy budget** and **instantaneous device-level power cap**.

### 3. Policy Optimization with Q-Learning
- Constructed cost–reward pairs for six candidate actions.
- Solved CMDP with tabular Q-learning:
  - Improved average reward from **~9 to ~15** over 300 episodes.
  - Maintained energy usage within **85–90% of budget**.
  - Guaranteed no violation of power caps.

## Results and Insights

- HSMMs effectively capture **piecewise-stationary phases** in edge inference.
- CMDP optimization reveals clear **energy–quality trade-offs**.
- Learned policies significantly improve cumulative inference quality while **respecting real-world constraints**.

## Conclusion

This study establishes the first **unified mathematical framework** linking SLM parameters, stochastic energy consumption, and inference quality. By integrating HSMM-based cost modeling with CMDP optimization, it enables **sustainable, adaptive deployment** of SLMs in edge and IoT environments, paving the way for future extensions with deep RL and collaborative multi-device scheduling.

