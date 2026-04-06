---
title: Can Large Language Models Credibly Stand in for Humans in Game-Theoretic Experiments?
summary: 评估了 LLM 在策略性社会博弈中与人类行为的一致性，并提出 PRIME-Router 以增强角色一致性和适应性。
date: 2025-04-17
type: docs
tags:
  - Game Theory
  - Large Language Models
  - Social Simulation
  - Multi-Agent Systems
  - Behavioral AI
image:
  caption: '用于模拟博弈中人类行为的多智能体 LLM 框架'
---

本研究探讨了使用 Large Language Models (LLMs) 作为行为博弈论实验中**人类参与者代理**的可行性。我们评估了四个 LLM——GPT-4o、Llama-3.3-70B-Instruct、Llama-3.3-8B-Instruct 和 DeepSeek-R1，涵盖**三个经典博弈**：**Prisoner’s Dilemma**、**Ultimatum Game** 和 **Public Goods Game**。

## 研究目标

- 评估 LLM 相对于人类规范的**行为一致性**、**角色一致性**和**策略适应性**。
- 设计一个**模块化多智能体框架（PRIME-Router）**以提高一致性和适应性。
- 使用**基于 MBTI 的角色提示**对 LLM 行为进行基准测试：Diplomat、Analyst、Sentinel、Explorer。

## 核心贡献

### 1. 经典博弈中的行为评估
使用三个新指标对 LLM 进行了与人类行为的对标：
- **BAM (Behavioral Alignment Measure)**：与人类行为分布的相似度
- **PCI (Persona Consistency Index)**：对提示的社会角色的遵循程度
- **ASP (Adaptive Strategic Profile)**：对不断变化的博弈情境的响应能力

主要发现：
- 大多数 LLM 表现出**较高的初始 BAM**，但在重复博弈中的**适应性一致性**方面表现不佳。
- GPT-4o 和 LLaMA-3.3-70B 在单次博弈中展现了**优秀的角色一致性**。

### 2. PRIME-Router 框架
为克服适应性和一致性的局限，我们提出了 **PRIME-Router**，一种模块化 MoE 风格的架构：
- 生成**专业化子角色**（例如 Empathy Enforcer、Strategic Planner）
- 根据经验性能为每个子角色分配**最合适的 LLM**
- 通过**协作模式**（例如 star、debate、chain）聚合多智能体输出

PRIME-Router 的提升效果：
- **PCI** 最高提升 **0.23**
- **ASP** 最高提升 **0.32**
（在重复博弈中）。

### 3. 启示与展望
- LLM 能够**可信地模拟类人行为**，但**策略深度**和**长期角色保真度**仍是挑战。
- PRIME-Router 为**社会科学实验**、**政策建模**和**在线平台模拟**中的**高性价比 AI 智能体**铺平了道路。

## 结论

本研究揭示了 LLM 在行为博弈模拟中的潜力与局限。像 PRIME-Router 这样的结构化多智能体设计显著增强了真实性，为实验社会科学中的**AI 驱动人类建模**提供了新范式。

[AAAI 2026 投稿] — 审稿中
