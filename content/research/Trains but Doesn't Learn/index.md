---
title: "Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers"
summary: A governed delivery-plane benchmark that asks not whether an LLM agent can raise a metric, but whether it can be trusted to deliver post-training as a service. Frontier agents run ten governed stages on real H200 and A40 hardware across 8B–70B bases; the risk lives where failure is silent — in judgment and governance, not the arithmetic a configurator already solves.
date: 2026-06-17
type: docs
tags:
  - LLM Agents
  - Post-Training as a Service
  - Forward-Deployed Engineers
  - Delivery Benchmark
  - Anytime-Valid Detection
image:
  caption: 'The governed delivery plane: an agent in the FDE seat post-trains a base model from a customer ticket; a de-looped oracle scores ten stages, and auditing them surfaces three findings'
---

<a href="https://junfei-z.github.io/fde/" target="_blank">
  <img src="https://img.shields.io/badge/Interactive%20Demo-Open-2563eb?logo=googlechrome&logoColor=white" alt="Demo">
</a>

📄 *Accepted to EMNLP 2026.*

Post-training is becoming a service (PTaaS): a customer hands an operator data and a goal, and a **forward-deployed engineer** (FDE) returns a fine-tuned, evaluated, and deployed model under a budget, a human-approval gate, and reproducibility requirements. The FDE is a natural target for automation, but seating an LLM agent in that seat raises a question existing benchmarks cannot answer: not whether an agent can *raise a metric*, but whether it can be *trusted to deliver*.

## Interactive Demo

The companion page walks through the benchmark and its three findings visually, with an interactive stage pipeline, a training-dashboard flip, and a pressure ladder:

👉 [**Open the interactive demo**](https://junfei-z.github.io/fde/)

## The Benchmark

We answer the operator's question with a **governed delivery-plane benchmark** that recasts the agentic FDE as a layered control plane. The agent drives ten governed stages (intake, plan, config, schedule, train, eval, register, deploy, cost, card), each scored pass/fail by a **de-looped oracle that never reads the trained model**. The stages partition by *where failure becomes visible* rather than by difficulty: a deterministic configurator certifies the arithmetic stages before any agent runs, so failure there is loud and cheap to catch, while the judgment stages are surfaced only by the delivery-level oracle. We run a flagship tier (Claude Opus 4.8, GPT-5.5, Gemini 3.1-Pro) and a cheaper tier on real **H200 and A40** hardware, across **8B–70B** open bases spanning three families and three seeds.

## Three Findings

- **A silent training failure that is real.** An injected intake-misread reliably induces a run that **trains but doesn't learn (TBDL)** across every 8B–70B base — green on every in-process signal, yet delivering a base-level model. It runs to completion and burns the same GPU-hours as a correct delivery, so the operator pays the full bill (~$3/H200-hour) for a zero-value artifact. An anytime-valid clean-probe e-process flags severe cases **before payment**.
- **The risk is judgment, not arithmetic.** Agents configure at near-parity with a deterministic configurator. Handing them the **oracle-correct configuration** does *not* repair a residual judgment deficit — the failure survives the *do*-intervention and sits above the arithmetic.
- **Governance is pressure-fragile.** Benign business pressure — deadlines, authority, sunk cost — collapses deploy-gate compliance while the agents' risk-detection stays at ceiling. They know the rule; they don't keep it.

## Takeaway

The lesson generalizes: green signals do not certify the thing you care about. **A green training dashboard is a billing liability, not a delivery certificate.**
