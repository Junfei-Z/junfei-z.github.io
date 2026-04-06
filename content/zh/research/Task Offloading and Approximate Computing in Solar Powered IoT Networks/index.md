---
title: Task Offloading and Approximate Computing in Solar Powered IoT Networks
summary: 提出了一种新颖的基于 MILP 和 Digital Twin 的控制策略，用于优化近似 IoT 任务执行中的能耗。
date: 2024-01-07
type: docs
tags:
  - IoT
  - Approximate Computing
  - Energy Harvesting
  - Optimization
  - Digital Twin
image:
  caption: '绿色 IoT 系统中基于 Digital Twin 的控制与卸载'
---

本研究提出了一种新颖的框架，通过**任务卸载和近似计算**来最小化太阳能驱动 IoT 网络的**总能耗**。设备可以选择本地执行（精确或近似）或将任务卸载到太阳能驱动的边缘服务器。

## 核心目标
- 在可容忍误差的情况下，通过允许近似任务执行来**降低能耗**。
- **利用 Digital Twin (DT)** 估计未来的能量可用性和信道条件。
- **优化卸载决策**以及跨时隙和信道的资源分配。

## 技术亮点

### MILP 建模
- 设计了**首个 MILP**，联合优化：
  - 任务卸载决策
  - 近似与精确执行
  - 信道分配
  - 虚拟机（VM）分配
- 捕获了能量到达、CPU 周期、近似误差界和 VM 容量等约束条件。

### DT 辅助的滑动窗口控制 (DT-RHC)
- 引入了基于 **DT 的控制算法**，使用：
  - **Gaussian Mixture Models (GMMs)** 预测能量和信道增益
  - 滑动窗口 MILP 优化实现动态调度
- 仅使用**因果（历史）数据**即可实现 MILP 最优值 **1.62 倍**以内的能耗

### 结果与评估
- DT-RHC 在以下指标上显著优于随机策略：
  - 能耗与设备数量的关系
  - 近似比率的影响
  - 扩展时间范围内的任务完成率
- 仿真在 100×100 m² 部署上使用 Python + Gurobi 进行，采用真实的太阳能输入和无线模型。

## 结论
本研究证明了在**可再生能源驱动的 IoT 环境**中集成**近似计算和智能卸载**的可行性。它为未来的**分布式优化和自适应能耗感知网络控制**提供了坚实基础。

[IEEE Paper DOI: 10.1109/LNET.2023.3328893](https://doi.org/10.1109/LNET.2023.3328893)
