---
title: "PRISM: Privacy-Aware Routing for Adaptive Cloud–Edge LLM Inference with Semantic Sketch Collaboration"
summary: "设计了一个隐私感知的路由框架，为 LLM 推理在云端和边缘之间动态选择执行路径，结合自适应 LDP 和语义草图协作"
date: 2025-07-30
type: docs
tags:
  - Privacy
  - LLM Inference
  - Cloud–Edge Collaboration
  - Differential Privacy
  - Routing
image:
  caption: "PRISM 中的语义敏感路由与协作流程"
---
<a href="https://junfei-z.github.io/prism_full.pdf" target="_blank">
  <img src="https://img.shields.io/badge/View%20Full%20Paper-PDF-red?logo=adobeacrobatreader&logoColor=white" alt="PDF">
</a>

[已被 2026 AAAI Conference on Artificial Intelligence 录用] — 即将发表

本项目提出了 **PRISM**，一个上下文感知的云-边推理框架，为 **Large Language Model (LLM)** 服务在隐私、效用和效率之间取得平衡。它通过根据用户输入的**语义敏感度**自适应调整保护策略，解决了统一隐私机制的关键局限。

## 目标

主要目标是在实际部署中实现**隐私保护的 LLM 推理**，将敏感的用户提示智能地路由到边缘设备和云端之间。PRISM 旨在：
- 避免对无害输入添加不必要的噪声
- 保持敏感提示的语义连贯性
- 在不损害效用的前提下降低延迟和能耗

## 主要贡献

### 语义敏感的执行路由

- 边缘端的**软门控控制器**利用上下文特征（例如命名实体、第一人称引用）评估实体级风险
- 将提示路由到三条执行路径之一：
  - **仅边缘**：用于高风险提示
  - **仅云端**：用于低风险提示
  - **云-边协作**：用于中等敏感度提示

### 自适应两层 Local Differential Privacy (LDP)

- 每个敏感实体通过以下方式进行混淆：
  - 类别级扰动（例如掩蔽"诊断"）
  - 值级扰动（例如将"HIV"替换为"Flu"）
- 隐私预算分配由敏感度权重模型引导，确保**细粒度保护且不造成语义崩塌**

### 语义草图协作协议

- 带噪声的提示在云端处理，生成**语义草图**（例如高层次的抽象回复）
- 边缘端的 **Small Language Model (SLM)** 利用原始上下文精化这些草图
- 在**强隐私约束下实现高效用回复**

## 结果与洞察

- PRISM 相比 Uniform 和 Selective LDP 等基线方法，实现了**最高 3 倍的延迟降低**和 **2.5 倍的能耗降低**
- 在强隐私预算下提供**更高的 LLM-Judge 评分（最高 7.2）**
- 在效用和效率方面均优于现有最先进方法（例如 Split-and-Denoise、DP-Forward）
- 在 **8 种不同模型组合**（例如 GPT-4o + StableLM）上表现稳健

| Method        | Ct.(s) | Ec.(J) | IQ.   |
|---------------|--------|--------|-------|
| PRISM         | 7.92   | 687.2  | 6.88  |
| Uniform LDP   | 20.56  | 1707.6 | 5.72  |
| Selective LDP | 21.22  | 1770.8 | 5.94  |
| Edge-Only     | 17.84  | 1573.9 | 5.09  |
| Cloud-Only    | **5.13**   | **296.3**  | **8.14**  |

## 更广泛的影响

PRISM 为**医疗、金融和个人助理**等敏感领域提供了**选择性隐私保护推理**，为以下方向铺平了道路：
- 在**隐私关键环境**中负责任地部署 LLM
- 降低**云-边基础设施**的能耗成本
- 弥合**隐私与推理质量**之间的权衡



