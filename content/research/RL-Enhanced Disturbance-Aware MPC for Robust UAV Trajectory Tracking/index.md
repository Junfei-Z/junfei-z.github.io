---
title: RL-Enhanced Disturbance-Aware MPC for Robust UAV Trajectory Tracking
summary: Developed a hybrid control framework integrating reinforcement learning and sliding mode observer into MPC for disturbance-aware UAV tracking.
date: 2025-05-07
type: docs
tags:
  - UAV
  - Model Predictive Control
  - Reinforcement Learning
  - Disturbance Observer
  - Sliding Mode Control
image:
  caption: 'Robust trajectory tracking via RL-MPC and AST-SMO integration'
---

This research introduces **ROAM**, a novel RL-enhanced, disturbance-aware MPC framework for **precise UAV trajectory tracking** in uncertain and dynamic environments. The method combines the predictive strengths of MPC with the fast response of reinforcement learning (RL) and the robustness of an adaptive sliding mode observer (SMO).

## Problem and Motivation

Traditional UAV controllers using MPC struggle under **model mismatch**, **wind disturbances**, and **computational delays**, resulting in residual tracking errors and slow convergence. This work addresses those challenges via two innovations:
- An **offline-trained RL warm-start policy** to accelerate MPC convergence
- An **Adaptive Super-Twisting Sliding Mode Observer (AST-SMO)** to estimate and reject real-time disturbances

## Technical Contributions

### 1. RL-Based Warm Start
- A **direction-conditioned policy** is trained via imitation learning on expert MPC trajectories.
- During real-time control, it provides **trajectory-consistent initial guesses** to the MPC solver, reducing early-stage tracking error by **16.9%** and computation time by **38.7%**.

### 2. AST-SMO for Disturbance Estimation
- The SMO estimates external disturbances in real time using a smooth hyperbolic function to avoid chattering.
- An adaptive gain tuning mechanism adjusts sensitivity dynamically for better convergence.

### 3. Disturbance-Aware MPC
- MPC is reformulated to incorporate real-time estimates from AST-SMO:
  \[
  x_{k+1} = Ax_k + Bu_k + E(\hat{d}_k)
  \]
- Objective: minimize both tracking error and control effort, while maintaining system constraints.

## Simulation Results

- Evaluated on a 12-DOF quadrotor model under sinusoidal and noisy disturbances.
- ROAM achieved:
  - 16.9% improvement in early-stage tracking accuracy
  - 38.7% reduction in computation time
  - Superior trajectory adherence under heavy external disturbances compared to classical MPC

## Conclusion

ROAM demonstrates that **deep integration of RL, observers, and MPC** yields a control system with faster convergence, better stability, and higher resilience. Its lightweight and modular design makes it highly suitable for **real-time deployment** on embedded UAV platforms.

📄 [IEEE SMC 2025 Submission] — Coming Soon

<!-- [Hugo Blox Builder](https://hugoblox.com) is designed to give technical content creators a seamless experience. You can focus on the content and the Hugo Blox Builder which this template is built upon handles the rest.

**Embed videos, podcasts, code, LaTeX math, and even test students!**

On this page, you'll find some examples of the types of technical content that can be rendered with Hugo Blox.

## Video

Teach your course by sharing videos with your students. Choose from one of the following approaches:

{{< youtube D2vj0WcvH5c >}}

**Youtube**:

    {{</* youtube w7Ft2ymGmfc */>}}

**Bilibili**:

    {{</* bilibili id="BV1WV4y1r7DF" */>}}

**Video file**

Videos may be added to a page by either placing them in your `assets/media/` media library or in your [page's folder](https://gohugo.io/content-management/page-bundles/), and then embedding them with the _video_ shortcode:

    {{</* video src="my_video.mp4" controls="yes" */>}}

## Podcast

You can add a podcast or music to a page by placing the MP3 file in the page's folder or the media library folder and then embedding the audio on your page with the _audio_ shortcode:

    {{</* audio src="ambient-piano.mp3" */>}}

Try it out:

{{< audio src="ambient-piano.mp3" >}}

## Test students

Provide a simple yet fun self-assessment by revealing the solutions to challenges with the `spoiler` shortcode:

```markdown
{{</* spoiler text="👉 Click to view the solution" */>}}
You found me!
{{</* /spoiler */>}}
```

renders as

{{< spoiler text="👉 Click to view the solution" >}} You found me 🎉 {{< /spoiler >}}

## Math

Hugo Blox Builder supports a Markdown extension for $\LaTeX$ math. You can enable this feature by toggling the `math` option in your `config/_default/params.yaml` file.

To render _inline_ or _block_ math, wrap your LaTeX math with `{{</* math */>}}$...${{</* /math */>}}` or `{{</* math */>}}$$...$${{</* /math */>}}`, respectively.

{{% callout note %}}
We wrap the LaTeX math in the Hugo Blox _math_ shortcode to prevent Hugo rendering our math as Markdown.
{{% /callout %}}

Example **math block**:

```latex
{{</* math */>}}
$$
\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}
$$
{{</* /math */>}}
```

renders as

{{< math >}}
$$\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}$$
{{< /math >}}

Example **inline math** `{{</* math */>}}$\nabla F(\mathbf{x}_{n})${{</* /math */>}}` renders as {{< math >}}$\nabla F(\mathbf{x}_{n})${{< /math >}}.

Example **multi-line math** using the math linebreak (`\\`):

```latex
{{</* math */>}}
$$f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
1-p_{0}^{*} & \text{if }k=0.\end{cases}$$
{{</* /math */>}}
```

renders as

{{< math >}}

$$
f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
1-p_{0}^{*} & \text{if }k=0.\end{cases}
$$

{{< /math >}}

## Code

Hugo Blox Builder utilises Hugo's Markdown extension for highlighting code syntax. The code theme can be selected in the `config/_default/params.yaml` file.


    ```python
    import pandas as pd
    data = pd.read_csv("data.csv")
    data.head()
    ```

renders as

```python
import pandas as pd
data = pd.read_csv("data.csv")
data.head()
```

## Inline Images

```go
{{</* icon name="python" */>}} Python
```

renders as

{{< icon name="python" >}} Python

## Did you find this page helpful? Consider sharing it 🙌 -->
