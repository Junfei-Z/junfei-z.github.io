---
title: Stochastic Power Modeling and Constrained MDP Optimization for On-Device SLM Inference
summary: 提出了一个统一的随机框架，结合基于 HSMM 的功耗建模和约束 MDP 优化，以实现 small language models (SLMs) 在边缘设备上的可持续部署。
date: 2025-09-22
type: docs
tags:
  - Small Language Models
  - On-Device Inference
  - Hidden Semi-Markov Models
  - Constrained MDP
  - Energy–Quality Trade-off
image:
  caption: '基于 HSMM 驱动的 CMDP 优化的能耗感知 SLM 推理'
---

[ICASSP 2026 投稿] — 审稿中

本研究提出了一个**随机且可解释的框架**，用于在严格的能耗和硬件约束下实现 **small language models (SLMs)** 的可持续**设备端推理**。通过捕获细粒度的 CPU/GPU 功耗动态，并利用约束 MDP 优化推理调度，本工作为**边缘端自适应、资源感知的 AI** 提供了原则性基础。

## 问题与动机

在智能手机、笔记本电脑或 IoT 节点上本地运行 SLM 可提供**低延迟和隐私保护的 AI 服务**，但这些设备面临**有限的电池预算**和**严格的功率上限**。传统能耗模型无法捕获 SLM 推理中随机的、分阶段的 CPU/GPU 行为，使其不适用于**多任务自适应部署**。

## 技术贡献

### 1. 基于 HSMM 的能耗建模
- 对 **Gemma2-2B** 和 **Qwen3-4B** 在 MT-Bench 上进行了细粒度功耗测量。
- 分别使用 **Hidden Semi-Markov Models (HSMMs)** 对 CPU 和 GPU 功耗轨迹建模：
  - GPU：上升、平稳、衰减阶段。
  - CPU：低负载和高负载突发。
- 在预测功耗波动方面**优于 HMM 和 TCN 基线**。

### 2. 约束 MDP 建模
- 定义了一个 **CMDP**，其中每个推理任务选择一种 SLM 配置（模型 + 量化方案）。
- 状态：剩余能量预算。
- 动作：候选 SLM 配置。
- 奖励：**LLM-as-a-Judge 质量评分**。
- 约束：**有限能量预算**和**瞬时设备级功率上限**。

### 3. 基于 Q-Learning 的策略优化
- 为六个候选动作构建了成本-奖励对。
- 使用表格式 Q-learning 求解 CMDP：
  - 在 300 个回合中将平均奖励从 **约 9 提升至约 15**。
  - 将能耗维持在**预算的 85–90%**。
  - 保证不违反功率上限。

## 结果与洞察

- HSMM 有效捕获了边缘推理中的**分段平稳阶段**。
- CMDP 优化揭示了清晰的**能耗-质量权衡**。
- 学习到的策略在**遵守现实约束**的同时显著提升了累计推理质量。

## 结论

本研究建立了首个**统一数学框架**，将 SLM 参数、随机能耗和推理质量联系起来。通过将基于 HSMM 的成本建模与 CMDP 优化相结合，实现了 SLM 在边缘和 IoT 环境中的**可持续、自适应部署**，为未来基于 deep RL 和多设备协同调度的扩展奠定了基础。

