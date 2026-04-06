---
title: RL-Enhanced Disturbance-Aware MPC for Robust UAV Trajectory Tracking
summary: 开发了一种混合控制框架，将强化学习和滑模观测器集成到 MPC 中，实现扰动感知的 UAV 轨迹跟踪。
date: 2025-05-07
type: docs
tags:
  - UAV
  - Model Predictive Control
  - Reinforcement Learning
  - Disturbance Observer
  - Sliding Mode Control
image:
  caption: '通过 RL-MPC 与 AST-SMO 集成实现鲁棒轨迹跟踪'
---
<a href="https://junfei-z.github.io/uav_control.pdf" target="_blank">
  <img src="https://img.shields.io/badge/View%20Full%20Paper-PDF-red?logo=adobeacrobatreader&logoColor=white" alt="PDF">
</a>

[已被 IEEE SMC 2025 录用] — 即将发表

本研究提出了 **ROAM**，一种新颖的 RL 增强、扰动感知的 MPC 框架，用于不确定和动态环境中的**精确 UAV 轨迹跟踪**。该方法结合了 MPC 的预测优势、reinforcement learning (RL) 的快速响应能力以及自适应 sliding mode observer (SMO) 的鲁棒性。

## 问题与动机

使用 MPC 的传统 UAV 控制器在**模型失配**、**风扰动**和**计算延迟**下表现不佳，导致残余跟踪误差和收敛缓慢。本工作通过两项创新解决这些挑战：
- **离线训练的 RL 热启动策略**以加速 MPC 收敛
- **Adaptive Super-Twisting Sliding Mode Observer (AST-SMO)** 以估计和抑制实时扰动

## 技术贡献

### 1. 基于 RL 的热启动
- 通过在专家 MPC 轨迹上进行模仿学习，训练了一个**方向条件策略**。
- 在实时控制中，它为 MPC 求解器提供**与轨迹一致的初始猜测**，将早期跟踪误差降低了 **16.9%**，计算时间减少了 **38.7%**。

### 2. 用于扰动估计的 AST-SMO
- SMO 使用平滑双曲函数实时估计外部扰动，以避免抖振。
- 自适应增益调节机制动态调整灵敏度以实现更好的收敛。

### 3. 扰动感知 MPC
- MPC 被重新构建以纳入来自 AST-SMO 的实时估计：
  \[
  x_{k+1} = Ax_k + Bu_k + E(\hat{d}_k)
  \]
- 目标：最小化跟踪误差和控制能耗，同时维持系统约束。

## 仿真结果

- 在正弦和噪声扰动下的 12 自由度四旋翼模型上进行了评估。
- ROAM 实现了：
  - 早期跟踪精度提升 16.9%
  - 计算时间减少 38.7%
  - 在强外部扰动下相比经典 MPC 具有更优的轨迹跟随性能

## 结论

ROAM 表明，**RL、观测器与 MPC 的深度集成**可产生具有更快收敛速度、更好稳定性和更高韧性的控制系统。其轻量化和模块化设计使其非常适合在嵌入式 UAV 平台上进行**实时部署**。



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
