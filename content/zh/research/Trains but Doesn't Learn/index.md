---
title: "Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers"
summary: 一个受治理的「交付平面」基准，关注的不是 LLM agent 能否把某个指标拉高，而是它能否被信任去交付 post-training as a service。前沿 agent 在真实 H200 与 A40 硬件、8B–70B 基座上跑完十个受治理阶段；风险恰恰存在于失败无声的地方——判断与治理，而非配置器早已解决的算术。
date: 2026-06-17
type: docs
tags:
  - LLM Agents
  - Post-Training as a Service
  - Forward-Deployed Engineers
  - Delivery Benchmark
  - Anytime-Valid Detection
image:
  caption: '受治理的交付平面：处于 FDE 角色的 agent 从客户工单出发对基座模型做 post-training；一个 de-looped oracle 对十个阶段打分，审计它们暴露出三个发现'
---

<a href="https://junfei-z.github.io/fde/" target="_blank">
  <img src="https://img.shields.io/badge/Interactive%20Demo-Open-2563eb?logo=googlechrome&logoColor=white" alt="Demo">
</a>

📄 *EMNLP 2026 投稿——审核中。*

Post-training 正在变成一种服务（PTaaS）：客户把数据和目标交给运营方，一名**前向部署工程师**（forward-deployed engineer, FDE）在预算、人工审批门以及可复现性要求之下，交付一个经过微调、评估并部署的模型。FDE 是自动化的天然目标，但把一个 LLM agent 放进这个位置，会引出现有基准无法回答的问题：不是 agent 能否*把指标拉高*，而是它能否*被信任去交付*。

## 交互式 Demo

配套页面用可视化方式串起整个基准及其三大发现，包含可交互的阶段流水线、训练面板翻转，以及压力阶梯：

👉 [**点击打开交互式 Demo**](https://junfei-z.github.io/fde/)

## 基准设计

我们用一个**受治理的交付平面基准**来回答运营方的问题，把 agentic FDE 重构为一个分层的控制平面。Agent 端到端地驱动十个受治理阶段（intake、plan、config、schedule、train、eval、register、deploy、cost、card），每个阶段都由一个**从不读取训练后模型的 de-looped oracle** 给出 pass/fail。这些阶段按*失败在何处变得可见*而非按难度来划分：一个确定性配置器在任何 agent 运行之前就能认证算术类阶段，因此那里的失败响亮且廉价；而判断类阶段只有交付层的 oracle 才能暴露。我们在真实 **H200 与 A40** 硬件上、跨越三个家族、三个随机种子的 **8B–70B** 开源基座上，运行了一个旗舰梯队（Claude Opus 4.8、GPT-5.5、Gemini 3.1-Pro）与一个低成本梯队。

## 三大发现

- **一个真实存在的无声训练失败。** 一次注入的 intake 误读，会在所有 8B–70B 基座上稳定诱发「训练了但没学到」（trains but doesn't learn, TBDL）——所有在线信号全绿，却交付了一个与基座无异的模型。它跑到完成，烧掉与正确交付相同的 GPU 小时数，运营方为一个零价值产物付了全额账单（约 \$3/H200-小时）。一个 anytime-valid 的 clean-probe e-process 能在**付款之前**标记出严重的情形。
- **风险在于判断，而非算术。** Agent 的配置能力与确定性配置器几乎持平。把**oracle 正确的配置**直接交给它们，并*不能*修复残余的判断缺陷——失败在 *do*-intervention 之后依然存在，凌驾于算术之上。
- **治理在压力下脆弱。** 良性的业务压力——截止日期、权威、沉没成本——会击穿部署门的合规率，而 agent 的风险识别能力仍维持在天花板。它们知道规则，却不遵守。

## 结论

这个教训可以推广：绿色信号并不能认证你真正在意的东西。**一块全绿的训练面板是一项账单负债，而不是一张交付证书。**
