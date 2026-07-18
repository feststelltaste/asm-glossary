---
title: Stratified Review Sampling
category: Engineering & Control
translation_de: stratifizierte-review-stichprobe
translation_de_title: Stratifizierte Review-Stichprobe
image: assets/images/en/stratified-review-sampling.png
---

# Stratified Review Sampling

![stratified-review-sampling](assets/images/en/stratified-review-sampling.png)

> Allocating human review effort across agent output by risk tier instead of uniformly: everything in the highest-risk category gets reviewed, moderate-risk categories get a meaningful sample, and low-risk categories get a light sample that can still catch systematic errors. This makes review tractable when output volume exceeds reviewer capacity, without leaving any category entirely unwatched. It deliberately avoids two failure modes: uniform random sampling, which underrepresents the critical few, and trusting the agent's self-reported confidence to decide what deserves a look.

**See also:** [Human-in-the-Loop](human-in-the-loop.md) · [Review Fatigue](review-fatigue.md) · [Confidence-Based Escalation](confidence-based-escalation.md)
{ .see-also }
