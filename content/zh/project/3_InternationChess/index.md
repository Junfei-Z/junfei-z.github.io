---
title: 基于混合 CNN 与 Logistic Regression 的音频材质分类
date: 2024-12-15
external_link: https://github.com/Junfei-Z/audio_based_material_classification
tags:
  - Audio Classification
  - CNN
  - MFCC
  - Logistic Regression
  - Hybrid Model
---

开发了一种混合模型，用于对七种材质（如桌面、玻璃、黑板）的敲击音频录音进行分类。该模型将基于原始音频的 1D CNN、基于 MFCC 特征的 2D CNN 和 Logistic Regression 组合为集成系统，在评估数据上达到了 94% 的准确率和 0.9426 的加权 F1-score。

<!--more-->
使用智能手机录制了 520 个不同敲击力度的真实样本。应用了降噪和特征提取（MFCC、时域特征、频域特征）。在多种 CNN 组合上进行了评估，展示了深度学习与传统方法的有效融合。提出的改进方向包括 Attention 机制、Mixup 数据增强以及扩展数据采集以提升泛化能力。
