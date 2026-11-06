---
title: "DSH Phone Remote — 用手机远程控制 DeepSeek Harness"
date: 2026-11-06
external_link: https://github.com/Junfei-Z/dsh-phone-remote
tags:
  - Node.js
  - Cloudflare 隧道
  - 远程访问
  - 开发者工具
---

零成本把跑在本机的 **DeepSeek Harness（DSH）** 搬到手机浏览器：Cloudflare 快速隧道 + 一个零依赖的密码网关，手机端不装 App、不开 VPN，也不占 iPhone 唯一的 VPN 槽位。

<!--more-->

- **两种上游，一个开关**：连桌面版**正在用的那个实例**（同一工作区、同一批会话、同一份实时状态），或托管一个独立的 `dsh web`（3080 端口）。`./install.sh --desktop` / `--web` 随时切换。
- **适配 DSH 0.2 的认证**：每个 DSH 进程会随机生成 launch token，且只印在启动 URL 里。网关改用本机持久化的 `client-connection/browser-session` 密钥现场签一张会话 cookie 注入，token 这道门槛就绕过去了。
- **过浏览器信任围栏**：把 `Host` / `Origin` 改写成 loopback，DSH 认为请求来自本机，**本体零改动**。
- **常驻可用**：launchd / systemd 守着隧道和网关，崩溃和重启都能自动恢复；手机端签名 cookie 180 天有效，密码错 8 次锁 5 分钟。

[查看 GitHub 源码](https://github.com/Junfei-Z/dsh-phone-remote)
