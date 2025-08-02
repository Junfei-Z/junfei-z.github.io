---
title : PRISM: Privacy-Aware Routing for Adaptive Cloud–Edge LLM Inference with Semantic Sketch Collaboration

summary : Designed a privacy-aware routing framework that dynamically selects execution paths across cloud and edge for LLM inference, combining adaptive LDP and semantic sketching

date : 2025-07-30

type : docs

tags :
  - Privacy
  - LLM Inference
  - Cloud–Edge Collaboration
  - Differential Privacy
  - Routing

image :
  caption: 'Semantic-sensitive routing and collaboration pipeline in PRISM'



This project introduces **PRISM**, a context-aware cloud–edge inference framework that balances privacy, utility, and efficiency for **Large Language Model (LLM)** services. It addresses the key limitations of uniform privacy mechanisms by adapting protection based on **semantic sensitivity** of user inputs.

## Objectives

The primary goal is to enable **privacy-preserving LLM inference** in real-world deployments, where sensitive user prompts are routed intelligently between edge devices and the cloud. PRISM is designed to:
- Avoid unnecessary noise for benign inputs
- Preserve semantic coherence in sensitive prompts
- Reduce latency and energy consumption without compromising utility

## Key Contributions

### Semantic-Sensitive Execution Routing

- A **soft gating controller** on the edge scores entity-level risk using contextual features (e.g., named entities, first-person references)
- Routes prompts to one of three execution paths:
  - **Edge-only** for high-risk prompts
  - **Cloud-only** for low-risk prompts
  - **Cloud–Edge Collaboration** for mid-sensitivity prompts

### Adaptive Two-Layer Local Differential Privacy (LDP)

- Each sensitive entity is obfuscated through:
  - Category-level perturbation (e.g., masking "Diagnosis")
  - Value-level perturbation (e.g., replacing "HIV" with "Flu")
- Privacy budget allocation is guided by a sensitivity weight model ensuring **fine-grained protection without semantic collapse**

### Semantic Sketch Collaboration Protocol

- Noisy prompts are processed in the cloud to generate **semantic sketches** (e.g., high-level abstract responses)
- The edge-side **Small Language Model (SLM)** refines these sketches using the original context
- Enables **high-utility responses under strong privacy constraints**

## Results & Insights

- PRISM achieves **up to 3× lower latency** and **2.5× lower energy consumption** than baselines like Uniform and Selective LDP
- Delivers **higher LLM-Judge scores (up to 7.2)** under strong privacy budgets
- Outperforms state-of-the-art methods (e.g., Split-and-Denoise, DP-Forward) in terms of both utility and efficiency
- Robust across **8 different model combinations** (e.g., GPT-4o + StableLM)

| Method        | Ct.(s) | Ec.(J) | IQ.   |
|---------------|--------|--------|-------|
| PRISM         | 7.92   | 687.2  | 6.88  |
| Uniform LDP   | 20.56  | 1707.6 | 5.72  |
| Selective LDP | 21.22  | 1770.8 | 5.94  |
| Edge-Only     | 17.84  | 1573.9 | 5.09  |
| Cloud-Only    | **5.13**   | **296.3**  | **8.14**  |

## Broader Impact

PRISM enables **selective privacy-preserving inference** for sensitive domains such as **medical, financial, and personal assistants**, paving the way for:
- Deploying LLMs responsibly in **privacy-critical environments**
- Reducing energy costs in **cloud-edge infrastructure**
- Bridging the tradeoff between **privacy and inference quality**

📄 [AAAI 2026 Submission] — In Review

