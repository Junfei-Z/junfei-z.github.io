---
title: "MPPI with Control Barrier Functions for F1/10：真实世界不确定性下的鲁棒安全控制"
date: 2025-05-07
external_link: https://github.com/vaithak/f1tenth_shield_mppi
tags:
  - Model Predictive Control
  - Control Barrier Functions
  - Autonomous Racing
---

本项目在 F1/10 自主赛车平台上实现了 Shield-MPPI，这是一种将 Control Barrier Functions (CBFs) 与 Model Predictive Path Integral (MPPI) 控制相结合的新方法，旨在实现真实世界不确定性条件下的鲁棒安全导航。

<!--more-->

主要贡献包括：
- **安全保障**：通过离散时间 CBFs 确保预定义安全集的前向不变性。
- **代价增强与控制滤波**：在 MPPI 轨迹代价中加入 CBF 惩罚项，并应用基于梯度的滤波方法以保证实时安全性。
- **鲁棒性评估**：在仿真和实际赛车环境中评估了系统在扰动、噪声和模型失配下的表现。
- **计算可行性**：验证了 Shield-MPPI 在资源受限平台上的实时性能。

该方法在碰撞避免、赛道跟踪和鲁棒性方面较基准 MPPI 有显著提升。
