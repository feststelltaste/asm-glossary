---
title: Confidence-Based Escalation
category: Engineering & Control
translation_de: konfidenzbasierte-eskalation
translation_de_title: Konfidenzbasierte Eskalation
image: assets/images/en/confidence-based-escalation.png
---

# Confidence-Based Escalation

![confidence-based-escalation](assets/images/en/confidence-based-escalation.png)

> A control pattern in which an agent's decisions are routed by certainty: clear-cut cases execute autonomously while borderline ones escalate to a human reviewer. This creates a tiered system that balances throughput against risk and reserves the human review queue for cases where judgment genuinely adds value. Thresholds belong per decision type, since the cost of a wrong autonomous action differs between renaming a variable and deleting a module, and they hold up best when tied to verifiable signals such as tests or static analysis rather than to the model's self-reported confidence alone.

**See also:** [Human-in-the-Loop](human-in-the-loop.md) · [Guardrails](guardrails.md) · [Feedback Loop](feedback-loop.md)
{ .see-also }
