---
title: Minimizing Maximum Age of Service in Virtualized Green IoT Networks
summary: 开发了优化与控制策略，以降低可再生能源驱动的 IoT 网络中的服务延迟
date: 2024-12-07
type: docs
tags:
  - IoT
  - Optimization
  - Renewable Energy
  - Model Predictive Control
image:
  caption: '绿色网络中基于 DAG 服务的 AoS 优化'
---

本项目解决了在太阳能驱动的绿色 IoT 网络中嵌入和调度应用的挑战，目标是最小化**最大 Age of Service (AoS)** — 一个表示数据生成到服务完成之间延迟的新鲜度指标。

## 目标
本研究聚焦于由**可再生能源**（太阳能）驱动的虚拟化、具备计算能力的 IoT 基础设施。应用被建模为包含 **Virtual Network Functions (VNFs)** 的 **Directed Acyclic Graphs (DAGs)**，需要在波动的能量和计算约束下执行。

## 主要贡献

### Mixed Integer Linear Programming (MILP) 建模
- 提出了**首个 MILP 模型**，联合优化：
  - 设备选择与采样时间
  - DAG 请求嵌入决策
  - 设备、网关和服务器的能耗
- 目标：最小化所有 DAG 请求的**最大 AoS**。

### 启发式与预测控制方案
- 开发了 **GreedyOL**，一种基于当前 AoS 嵌入 DAG 的快速启发式算法。
- 提出了 **RHCOP**，一种 **Receding Horizon Control Optimization** 框架：
  - 利用 **Gaussian Mixture Models (GMMs)** 预测太阳能到达量和无线信道增益。
  - 仅使用因果（非未来）信息实现实时调度。

### 结果与洞察
- RHCOP 实现了最优 MILP 的 **1.07 倍** min-max AoS，GreedyOL 为 **1.13 倍**。
- 更多的网关和服务器由于增强的冗余性和灵活性而降低了 AoS。
- **VNF-C**（采集）和 **VNF-P**（处理）数量相等时可获得最优新鲜度。

## 更广泛的影响
所提出的系统为**能耗感知、延迟敏感的 IoT 应用**奠定了基础，尤其适用于**偏远或能源受限的环境**。研究结果揭示了**计算新鲜度**、**资源分配**与**绿色网络部署**策略之间的权衡关系。

[IEEE Transactions on Services Computing 投稿] — 即将发表
