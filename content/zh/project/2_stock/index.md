---
title: 基于 Reinforcement Learning 的接触网络随机疫苗分配策略
date: 2025-03-17
external_link: https://github.com/Junfei-Z/Stochavac_RL
tags:
  - Reinforcement Learning
  - Epidemic Modeling
  - Networked Systems
---

将确定性最优控制与 Reinforcement Learning 相结合，开发了个体级接触网络上的随机疫苗分配策略，实现了鲁棒的疫情响应建模。

<!--more-->

## 项目亮点
- 在接触图上使用高维连续时间马尔可夫过程 (CTMP) 对疫情传播进行建模。
- 设计了基于 Policy Gradient 的 RL 疫苗接种策略，并以 Mean-Field ODE 解作为热启动。
- 在合成和真实世界网络拓扑上评估了策略在死亡率和住院率等指标上的表现。

## 工具
Python, PyTorch, NetworkX, OpenAI Gym
