---
title: Can Large Language Models Credibly Stand in for Humans in Game-Theoretic Experiments?
summary: Evaluated LLM alignment with human behavior across strategic social games and proposed PRIME-Router to enhance role consistency and adaptability.
date: 2025-04-17
type: docs
tags:
  - Game Theory
  - Large Language Models
  - Social Simulation
  - Multi-Agent Systems
  - Behavioral AI
image:
  caption: 'Multi-agent LLM framework for simulating human behavior in games'
---

This work investigates the feasibility of using Large Language Models (LLMs) as **proxies for human participants** in behavioral game-theoretic experiments. We evaluated four LLMs—GPT-4o, LLaMA-3.3B/8B, and DeepSeek-R1—across **three canonical games**: the **Prisoner’s Dilemma**, the **Ultimatum Game**, and the **Public Goods Game**.

## Research Objectives

- Evaluate **behavioral alignment**, **persona consistency**, and **strategic adaptability** of LLMs vs. human norms.
- Design a **modular, multi-agent framework (PRIME-Router)** for improved consistency and adaptability.
- Benchmark LLM behavior using **MBTI-based persona prompts**: Diplomat, Analyst, Sentinel, Explorer.

## Core Contributions

### 1. Behavioral Assessment in Canonical Games
LLMs were benchmarked against human behavior using three new metrics:
- **BAM (Behavioral Alignment Measure)**: similarity to human action distributions
- **PCI (Persona Consistency Index)**: adherence to prompted social roles
- **ASP (Adaptive Strategic Profile)**: responsiveness to evolving game contexts

Key findings:
- Most LLMs showed **high initial BAM** but struggled with **adaptive consistency** in repeated games.
- GPT-4o and LLaMA-3.3B demonstrated **excellent persona consistency** in one-shot games.

### 2. PRIME-Router Framework
To overcome adaptation and consistency limitations, we proposed **PRIME-Router**, a modular MoE-style architecture that:
- Spawns **specialized subroles** (e.g., Empathy Enforcer, Strategic Planner)
- Assigns the **most suitable LLM** to each subrole based on empirical performance
- Aggregates multi-agent outputs via **collaboration patterns** (e.g., star, debate, chain)

PRIME-Router improves:
- **PCI** by up to **0.23**
- **ASP** by up to **0.32**
across repeated games.

### 3. Implications and Outlook
- LLMs can **simulate human-like behavior credibly**, but **strategic depth** and **long-horizon persona fidelity** remain challenges.
- PRIME-Router paves the way for **cost-effective AI agents** in **social science experimentation**, **policy modeling**, and **online platform simulation**.

## Conclusion

Our study highlights the promise and limitations of LLMs in behavioral game simulations. Structured multi-agent design like PRIME-Router significantly enhances realism, offering a new paradigm for **AI-driven human modeling** in experimental social science.

📄 [ACM MM 2025 Submission] — Coming Soon
