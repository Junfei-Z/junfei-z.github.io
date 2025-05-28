title: Audio-based Material Classification Using Hybrid CNN and Logistic Regression
date: 2024-12-15
external_link: https://github.com/Junfei-Z/audio_based_material_classification
tags:
  - Audio Classification
  - CNN
  - MFCC
  - Logistic Regression
  - Hybrid Model
---

Developed a hybrid model for classifying audio recordings of knocking sounds from seven materials (e.g., table, glass, blackboard). The model combines 1D CNN on raw audio, 2D CNN on MFCC features, and logistic regression into an ensemble system. Achieved 94% accuracy and a weighted F1-score of 0.9426 on evaluation data.

<!--more-->
Collected 520 real-world samples using smartphone recordings with varying knock strengths. Applied noise reduction and feature extraction (MFCC, temporal, spectral features). Evaluated over diverse CNN combinations, demonstrating effective integration of deep learning with traditional methods. Proposed improvements include attention mechanisms, mixup augmentation, and expanded data collection for better generalization.
