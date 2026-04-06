---
title: "Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference"
summary: 首次对设备端 VLM 推理进行了系统性的能耗分析，揭示了 autoregressive decoding（而非 visual token 处理）主导了能耗（86–97%），颠覆了将 visual token 缩减作为主要效率优化策略的传统假设。
date: 2026-03-27
type: docs
tags:
  - Vision-Language Models
  - Energy Profiling
  - Edge Inference
  - On-Device AI
  - Embodied AI
image:
  caption: 'VLM 推理流程：输入编码、拼接与两阶段 LLM 推理'
---

Vision-Language Models (VLMs) 是具身智能的感知核心，但其在边缘硬件上的能耗特征仍未被充分理解。现有的效率优化工作主要集中在减少 visual tokens，隐式地将视觉处理视为主要能耗来源。我们通过**首次系统性的设备端 VLM 推理能耗分析**推翻了这一隐含假设，实验涵盖五个模型、三种架构系列、四种输入分辨率，以及两个硬件平台（NVIDIA RTX 3070 和 Jetson Orin NX）。

## 主要发现

我们的分析得出三个核心发现：

### 1. 功率是模型的固有指纹
平均推理功率是**模型固有常量**，不随输入分辨率、图像复杂度和提示类型变化，在所有条件下的变异不超过 5%。这意味着不同输入之间的所有能耗差异必然源于**推理时间**的变化，而非功率消耗的变化。

### 2. Decode 阶段主导能耗
Autoregressive decoding 占据了**总能耗的 86% 至 97%**。由于 prefill 和 decode 阶段之间的计算密集型与内存密集型不对称性，每个输出 token 的时钟时间是每个输入 token 的 **11 至 39 倍**。输出 token 数量是延迟和能耗的主要驱动因素。

### 3. Visual Token 剪枝的假象
即使移除**所有 visual tokens**，对于固定 token 模型最多也只能节省**总能耗的 10%**。相比之下，将输出长度减少 50% 可节省高达 **97%** 的能耗。这些发现揭示了 visual token pruning 的根本局限性：它针对的是 prefill 阶段，而该阶段本身只占总能耗的少数部分。

## 贡献

- **能耗分解**为 prefill 与 decode 阶段，展示了所有配置下 decode 的主导地位
- 对 visual token pruning 节能效果的**理论上界**
- **跨模型能耗预测器** — 一个具有五个特征（模型大小、输入 token 数、输出 token 数及交互项）的线性模型，无需逐模型校准即可解释 **98.6% 的能耗方差**（MAPE = 10.3%）
- **部署指南**：预算应关注输出而非输入；根据部署场景匹配 token 策略；预估内容驱动的能耗变化

## 结论

边缘 VLM 推理的真正能耗瓶颈不在于*看*，而在于*说*：不是模型看到了什么，而是它说了多少。我们的能耗分解框架为资源受限的边缘设备上的节能型 VLM 部署提供了可操作的指导。

[ACM MM 2026 投稿] — 审稿中
