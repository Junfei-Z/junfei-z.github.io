---
title: "Bridging Optimal Control And Reinforcement Learning For Node-Level Vaccine Allocation: A Regime-Based Comparative Analysis"
summary: "硕士毕业论文。一个面向异质接触网络的可扩展逐人疫苗分配框架，在随机 SEPAILHRVD 模拟器上对比「群体级最优控制 + 度数启发式」与端到端强化学习。"
date: 2026-04-23
type: docs
tags:
  - Reinforcement Learning
  - Optimal Control
  - Epidemic Modeling
  - Contact Networks
  - Vaccine Allocation
image:
  caption: "Barabási–Albert 接触网络上的节点级随机模拟器"
---

<a href="https://junfei-z.github.io/vaccine_rl/" target="_blank">
  <img src="https://img.shields.io/badge/Interactive%20Demo-Open-2563eb?logo=googlechrome&logoColor=white" alt="Demo">
</a>

📄 *硕士毕业论文，宾夕法尼亚大学（2026 年）。导师：Prof. Saswati Sarkar*

疫情爆发的最初几周，疫苗必须在大规模、异质的人群中分配，每日剂量预算严格受限，决策周期跨越数周到数月。任何可部署的策略最终都必须**指名具体的个体**——而不是给出群体层面的比例——并且要同时应对三大结构性难题：长时序的延迟奖励、C(N, K) 量级的组合动作空间、以及节点在网络中的位置和它的人口学群体身份同样重要。

## 交互式 Demo

配套 demo 用可视化方式串起整篇论文：

1. **三组人口模型** —— 普通基线 (X)、高危老年 (Y)、高接触 hub (Z)，每组各自有出现症状、住院、致死的分支概率。
2. **10 状态 SEPAILHRVD 疾病模型** —— 潜伏期、症状前、无症状、有症状、晚期、住院、康复、接种、死亡。
3. **Barabási–Albert 网络生长** —— 看 preferential attachment 一步步生成无标度接触图，幂律 degree 长尾自然涌现。
4. **随机模拟器** —— 自定义任意比例的初始感染种子，看不接种疫苗时疫情逐日演变，给出"什么都不做"的死亡基线。
5. **四方法对比** —— OC-Random、OC-high、Naive RL、Node RL 在同一 seed 下的实测结果。

👉 [**点击打开交互式 Demo**](https://junfei-z.github.io/vaccine_rl/)

## 主要贡献

- **C1 — 随机节点级模拟器**：一个高保真模拟环境，将显式 Barabási–Albert 接触网络与 10 状态 SEPAILHRVD 模型结合，刻画感染事件的内在随机性与个体层面的风险异质性。
- **C2 — OC-high**：用"组内度数最高优先"的节点级启发式增强群体级最优控制，连接聚合策略与个体行为。
- **C3 — Node RL**：端到端 actor–critic，使用共享参数的打分 MLP 加 Gumbel-Top-$K$ 重参数化采样，把策略梯度方差从独立 Bernoulli 的 $\Theta(N)$ 压到 $O(K)$。
- **C4 — Regime Map**：在人口规模、时间窗、初始感染比三轴上系统对比，绘出每种方法的最优适用区，明确何时 Node RL 的额外算力值得花。

## 核心结论

- 在大多数实战场景下，**OC-high 的死亡数和 Node RL 持平甚至更优**，且训练成本只有它的约 **1/70**（9 秒 vs. 625 秒）。
- Node RL 的优势真实存在但**很有限**：仅在短时间窗、或者初始感染中 hub 比例很高时才赢——这两种情形正好是 OC-high 背后的均场假设结构性失效的地方。
- 仅"组内度数最高优先"这一条启发式就贡献了平均 **5–10% 的死亡数下降**，量级和"群体级 OC 速率"本身相当。
