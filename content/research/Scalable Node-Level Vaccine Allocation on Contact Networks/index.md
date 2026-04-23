---
title: "Scalable Node-Level Vaccine Allocation on Contact Networks: Bridging Optimal Control and Reinforcement Learning"
summary: "Master's thesis. A scalable framework for per-individual vaccine allocation on heterogeneous contact networks, comparing group-level optimal control with hub-aware heuristics against end-to-end reinforcement learning on a stochastic SEPAILHRVD simulator."
date: 2026-04-23
type: docs
tags:
  - Reinforcement Learning
  - Optimal Control
  - Epidemic Modeling
  - Contact Networks
  - Vaccine Allocation
image:
  caption: "Node-level stochastic simulator on a Barabási–Albert contact network"
---

<a href="https://junfei-z.github.io/vaccine_rl/" target="_blank">
  <img src="https://img.shields.io/badge/Interactive%20Demo-Open-2563eb?logo=googlechrome&logoColor=white" alt="Demo">
</a>

📄 *Master's Thesis, University of Pennsylvania (2026). Advisor: Prof. Saswati Sarkar.*

In the first weeks of a pandemic, vaccines must be allocated across a large, heterogeneous population under a tight daily dose budget and over a horizon of weeks to months. A deployable policy must name specific individuals — not group-level proportions — and cope with three structural difficulties: sequential decisions over a long horizon with a delayed reward signal, a combinatorial daily action space of size $\binom{N}{K}$, and individual network position that matters as much as demographic group.

## Interactive Demo

The companion demo walks through the thesis visually:

1. **Three-group population model** — baseline (X), high-risk elderly (Y), and high-contact hubs (Z), each with group-specific symptomatic, hospitalisation, and case-fatality rates.
2. **10-compartment SEPAILHRVD disease model** — latent, pre-symptomatic, asymptomatic, symptomatic, late-stage, hospitalised, recovered, vaccinated, and dead.
3. **Barabási–Albert network construction** — watch preferential attachment grow a scale-free contact graph and the characteristic power-law degree tail emerge.
4. **Stochastic simulator** — seed infections in any group mix and watch an unvaccinated outbreak unfold day by day, reporting cumulative deaths as the no-intervention baseline.
5. **Method comparison** *(coming soon)* — OC-Random, OC-high, Naive RL, and Node RL on identical seeds.

👉 [**Open the interactive demo**](https://junfei-z.github.io/vaccine_rl/)

## Contributions

- **C1 — Stochastic node-level simulator**: a high-fidelity environment integrating an explicit Barabási–Albert contact network with a 10-compartment SEPAILHRVD model, capturing intrinsic stochasticity of infection events and individual-level risk heterogeneity.
- **C2 — OC-high**: augments principled group-level optimal control with a high-degree-first intra-group heuristic, bridging aggregate policy and individual action.
- **C3 — Node RL**: an end-to-end actor–critic with a shared-parameter scoring MLP and Gumbel-Top-$K$ reparameterised sampling, yielding $O(K)$ gradient variance versus $\Theta(N)$ for independent Bernoulli baselines.
- **C4 — Regime map**: systematic benchmarking across population size, horizon, and initial-infection ratio identifying when each method is preferable — and when the additional compute of node-level RL is justified.

## Headline Findings

- OC-high matches or beats Node RL in most regimes at roughly **two orders of magnitude** less preparation cost.
- Node RL's advantage is real but **confined** to short horizons and hub-heavy initial infections, where the mean-field assumption underlying OC-high structurally breaks down.
- The intra-group high-degree heuristic alone accounts for a **5–10% reduction in deaths** on average, comparable to the contribution of the group-level OC rates themselves.
