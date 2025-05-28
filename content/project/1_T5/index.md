---
title: "MPPI with Control Barrier Functions for F1/10: Robust Safety Under Real-World Uncertainty"
date: 2024-05-30
external_link: https://github.com/vaithak/f1tenth_shield_mppi
tags:
  - Model Predictive Control
  - Control Barrier Functions
  - Autonomous Racing
---

This project implements Shield-MPPI, a novel integration of Control Barrier Functions (CBFs) with Model Predictive Path Integral (MPPI) control, on the F1/10 autonomous racing platform to achieve robust, safe navigation under real-world uncertainty.

<!--more-->

Key contributions include:
- **Safety Assurance**: Enforced via discrete-time CBFs ensuring forward invariance of a predefined safe set.
- **Cost Augmentation and Control Filtering**: Augmented MPPI trajectory costs with CBF penalties and applied gradient-based filtering to guarantee real-time safety.
- **Robustness Evaluation**: Assessed system under disturbances, noise, and model mismatch in simulated and physical racing environments.
- **Computational Feasibility**: Validated Shield-MPPI’s real-time performance on resource-limited platforms.

The approach demonstrates significant improvement over baseline MPPI in terms of collision avoidance, track adherence, and robustness.
