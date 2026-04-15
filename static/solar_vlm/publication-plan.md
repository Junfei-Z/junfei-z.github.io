# Publication Plan: Solar-Powered LEO VLM Inference

## Overview

Two papers from one research line, with clear separation of contributions.

---

## Paper 1: Main Paper (arXiv first, then conference/journal)

### Title (working)
**Online Collaborative VLM Inference over Solar-Powered LEO Satellite Networks via Robust Lyapunov Optimization**

### Core Contribution
- Joint optimization of VLM model deployment, task offloading, scheduling, and energy management over solar-powered LEO constellations
- Max-min quality fairness objective across all sensing sources
- Two-timescale decomposition: offline ILP for VLM deployment + online Lyapunov per-slot scheduling
- Robust extension for eclipse periods (relaxed drift condition)
- Three virtual queues: Q^E (energy), Q^P (power cap), Q^U (quality deficit)

### Key Technical Elements
- Energy model: HSMM-based power parameterization from real hardware measurements (RTX 3070 / Jetson Orin)
- +Grid ISL topology with dynamic inter-plane connectivity
- Calibrated power bounds P_cap from HSMM high quantile
- Per-slot subproblem reducible to lightweight assignment (not full MILP)

### Supplementary
- Interactive 3D demo website: junfei-z.github.io/solar_vlm/
- Two-level visualization: solar system → LEO constellation drill-down
- Satellite detail panel, ISL links, VLM inference flows, battery indicators

### Timeline
1. Finalize experiments and writing
2. Post to arXiv (establish priority + get citable reference)
3. Submit to target venue (conference or journal TBD)

---

## Paper 2: WCL Short Letter (4 pages)

### Title (working)
**LEO-VLM-Sim: An Open Simulation Platform for Energy-Aware VLM Inference over Solar-Powered Satellite-Terrestrial Networks**

### Motivation
- No standardized simulation environment exists for solar-powered LEO VLM inference
- Existing works each build ad-hoc simulators, making cross-paper comparison impossible
- Need a unified platform with plug-and-play algorithm interface

### Core Contribution
1. **Open simulation platform** with Gym-like interface (obs → action → reward)
2. **Satellite-terrestrial architecture** — extends beyond pure LEO to include ground base stations, adding the dimension of on-board vs. downlink offloading
3. **Physically grounded models** — SGP4 orbit propagation (real TLE data), solar energy with eclipse, measured VLM energy profiles
4. **Built-in baselines** for standardized comparison

### Scenario Extension: Ground Base Stations
Compared to Paper 1 (pure LEO constellation), this platform adds:
- Ground stations with stable power but limited satellite contact windows (overpass-only communication)
- Three-way offloading decision per task: process on-board, relay via ISL to neighbor satellite, or downlink to ground station
- Trade-off: ground station has unlimited energy + stronger compute, but downlink bandwidth is scarce and contact window is short (~5-10 min per overpass)
- This makes the scheduling problem richer and the platform more general

### Platform Architecture
```
┌─────────────────────────────────────┐
│         Web Frontend (Three.js)      │
│   3D visualization + live dashboard │
└──────────────┬──────────────────────┘
               │ WebSocket / REST API
┌──────────────▼──────────────────────┐
│       Simulation Engine (Python)     │
│                                      │
│  ┌────────────┐ ┌─────────────────┐ │
│  │ Environment │ │ Algorithm API   │ │
│  │ - SGP4 orbit│ │ (Gym-like)      │ │
│  │ - Solar/EH  │ │                 │ │
│  │ - ISL topo  │ │ obs:            │ │
│  │ - Channel   │ │  battery, solar,│ │
│  │ - VLM energy│ │  queues, ISL,   │ │
│  │ - Ground BS │ │  pending tasks, │ │
│  └────────────┘ │  contact windows │ │
│                 │                 │ │
│                 │ action:          │ │
│                 │  offload target, │ │
│                 │  VLM config,     │ │
│                 │  execute/defer   │ │
│                 │                 │ │
│                 │ reward:          │ │
│                 │  inference qual  │ │
│                 └─────────────────┘ │
│                                      │
│  ┌────────────────────────────────┐  │
│  │ Built-in Baselines             │  │
│  │ - Greedy (best quality first)  │  │
│  │ - Round-Robin                  │  │
│  │ - EDF (earliest deadline)      │  │
│  │ - Lyapunov (Paper 1 algorithm) │  │
│  └────────────────────────────────┘  │
│                                      │
│  ┌────────────────────────────────┐  │
│  │ Standard Scenarios              │  │
│  │ - Small: 6 planes × 10 sats   │  │
│  │ - Medium: 12 × 20             │  │
│  │ - Large: 24 × 40 (Starlink)   │  │
│  │ - With/without ground stations │  │
│  └────────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Paper Structure (4 pages)
| Section | Pages | Content |
|---------|-------|---------|
| I. Introduction | 0.6 | Gap: no standardized LEO VLM sim; our contribution |
| II. Platform Design | 1.5 | Architecture, Gym interface spec, physical models (SGP4, solar, VLM energy from real measurements, ground station contact model) |
| III. Experiments | 1.5 | 4 baselines on 3 scenarios, metrics: min quality, avg quality, energy violation rate, task completion rate, ground offload ratio |
| IV. Conclusion | 0.4 | Summary + open-source link |

### Evaluation Metrics
- **Min-source quality** (fairness) — the worst-performing sensing source
- **Average inference quality** across all sources
- **Energy violation rate** — fraction of slots where battery drops below threshold
- **Task completion rate** — fraction of tasks processed within deadline
- **Ground offload ratio** — how often tasks are sent to ground vs. processed on-orbit

### Differentiation from Paper 1
| Aspect | Paper 1 | Paper 2 (WCL) |
|--------|---------|---------------|
| Focus | Algorithm design + theory | Platform + benchmark |
| Scenario | Pure LEO constellation | LEO + ground stations |
| Contribution | Lyapunov optimization, convergence proof | Gym interface, standardized comparison |
| Novelty | Theoretical | Engineering + extensibility |
| Code | Experiment scripts | Full open-source platform |

---

## Timeline

```
Phase 1: Main paper → arXiv
  - Finalize experiments with Jetson Orin measurements
  - Polish writing, add demo website as supplementary
  - Upload to arXiv

Phase 2: WCL preparation (can overlap with Phase 1 review)
  - Build Python simulation engine with Gym interface
  - Add SGP4 orbit propagation + ground station model
  - Implement 4 baselines
  - Run standardized benchmark experiments
  - Write 4-page letter

Phase 3: WCL submission
  - Cite Paper 1 arXiv version
  - Open-source the platform on GitHub
  - Submit to IEEE Wireless Communications Letters
```

---

## Key Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| WCL reviewer says "just a simulator, no novelty" | Emphasize: (1) first standardized LEO VLM benchmark, (2) satellite-terrestrial extension with ground stations, (3) real hardware energy data |
| Overlap concern between two papers | Clear separation: Paper 1 = algorithm, Paper 2 = platform. Different contribution types. |
| SGP4/TLE accuracy questioned | Use recent TLE from CelesTrak, validate against STK for a few test cases |
| Ground station model too simplistic | Model real overpass geometry: elevation angle > threshold, Doppler-aware link budget |
