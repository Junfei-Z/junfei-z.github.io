---
title: Minimizing Maximum Age of Service in Virtualized Green IoT Networks
summary: Developed optimization and control strategies to reduce service latency in renewable-powered IoT networks
date: 2024-12-01
type: docs
tags:
  - IoT
  - Optimization
  - Renewable Energy
  - Model Predictive Control
image:
  caption: 'AoS optimization for DAG-based services in green networks'
---

This project addresses the challenge of embedding and scheduling applications in solar-powered green IoT networks, with the goal of minimizing the **maximum Age of Service (AoS)** — a freshness metric indicating the delay between data generation and service completion.

## Objectives
The research focuses on virtualized, computation-enabled IoT infrastructures powered by **renewable energy** (solar). The applications are modeled as **Directed Acyclic Graphs (DAGs)** with **Virtual Network Functions (VNFs)** that must be executed under fluctuating energy and computational constraints.

## Key Contributions

### Mixed Integer Linear Programming (MILP) Formulation
- Proposed the **first MILP model** to jointly optimize:
  - Device selection and sampling time
  - DAG request embedding decision
  - Energy consumption at devices, gateways, and servers
- Objective: minimize the **maximum AoS** across all DAG requests.

### Heuristic and Predictive Control Solutions
- Developed **GreedyOL**, a fast heuristic that embeds DAGs based on current AoS.
- Proposed **RHCOP**, a **Receding Horizon Control Optimization** framework:
  - Utilizes **Gaussian Mixture Models (GMMs)** to predict solar energy arrivals and wireless channel gains.
  - Enables real-time scheduling using only causal (non-future) information.

### Results & Insights
- RHCOP achieves a **1.07×** and GreedyOL a **1.13×** min-max AoS compared to optimal MILP.
- More gateways and servers reduce AoS due to enhanced redundancy and flexibility.
- Equal numbers of **VNF-Cs** (collection) and **VNF-Ps** (processing) yield optimal freshness.

## Broader Impact
The proposed system lays groundwork for **energy-aware, delay-sensitive IoT applications**, especially in **remote or energy-constrained environments**. The results provide insights into the tradeoffs between **computation freshness**, **resource allocation**, and **green network deployment** strategies.
