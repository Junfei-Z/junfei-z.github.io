---
title: Task Offloading and Approximate Computing in Solar Powered IoT Networks
summary: Proposed a novel MILP and Digital Twin-based control strategy for optimizing energy use in approximate IoT task execution.
date: 2024-03-01
type: docs
tags:
  - IoT
  - Approximate Computing
  - Energy Harvesting
  - Optimization
  - Digital Twin
image:
  caption: 'DT-based control and offloading in green IoT systems'
---

This research proposes a novel framework for minimizing the **total energy consumption** of solar-powered IoT networks through **task offloading and approximate computing**. Devices can choose between local execution (exact or approximate) or offloading tasks to a solar-powered edge server.

## Core Objectives
- **Reduce energy usage** by allowing approximate task execution when tolerable errors are acceptable.
- **Leverage digital twins (DTs)** to estimate future energy availability and channel conditions.
- **Optimize offloading decisions** and resource allocation across time slots and channels.

## Technical Highlights

### MILP Formulation
- Designed the **first MILP** to jointly optimize:
  - Task offloading decisions
  - Approximate vs. exact execution
  - Channel allocation
  - Virtual machine (VM) assignment
- Captures constraints on energy arrivals, CPU cycles, approximation error bounds, and VM capacity.

### DT-Assisted Receding Horizon Control (DT-RHC)
- Introduced a **DT-based control algorithm** using:
  - **Gaussian Mixture Models (GMMs)** to predict energy and channel gain
  - Sliding-window MILP optimization for dynamic scheduling
- Achieves energy usage within **1.62×** of MILP optimal while requiring only **causal (past) data**

### Results & Evaluation
- DT-RHC significantly outperforms random strategies across metrics such as:
  - Energy consumption vs. number of devices
  - Impact of approximation ratios
  - Task completion within extended time horizons
- Simulations conducted in Python + Gurobi over 100×100 m² deployments using realistic solar input and wireless models.

## Conclusion
This study demonstrates the viability of integrating **approximate computing and intelligent offloading** in **renewable-powered IoT environments**. It provides a robust foundation for future **distributed optimization and adaptive energy-aware network control**.

[IEEE Paper DOI: 10.1109/LNET.2023.3328893](https://doi.org/10.1109/LNET.2023.3328893)
