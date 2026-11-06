---
title: "DSH Phone Remote — Control DeepSeek Harness from Your Phone"
date: 2026-11-06
external_link: https://github.com/Junfei-Z/dsh-phone-remote
tags:
  - Node.js
  - Cloudflare Tunnel
  - Remote Access
  - Developer Tools
---

A zero-cost way to drive the **DeepSeek Harness (DSH)** running on your machine from a phone browser: a Cloudflare quick tunnel plus a small zero-dependency password gate — no app and no VPN on the phone.

<!--more-->

- **Two upstream modes:** attach to the desktop app you are actually using (same workspace, same sessions, same live state), or host a standalone `dsh web` on port 3080. One installer flag switches between them.
- **Works with DSH 0.2 authentication:** each DSH process mints a random launch token and only prints it in the startup URL. The gate mints the equivalent browser-session cookie from the local `client-connection/browser-session` secret and injects it, so the token is no longer a dead end.
- **Fence-friendly:** `Host` and `Origin` are rewritten to a loopback authority, so DSH's browser-trust fence sees a local request — zero changes to DSH itself.
- **Always on:** launchd / systemd keeps the tunnel and gate alive across reboots and crashes; a signed cookie keeps the phone logged in for 180 days, and eight wrong passwords lock an IP for five minutes.

[View the source on GitHub](https://github.com/Junfei-Z/dsh-phone-remote)
