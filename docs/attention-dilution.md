---
title: Attention Dilution
category: Fundamentals
translation_de: aufmerksamkeitsverwaesserung
translation_de_title: Aufmerksamkeitsverwässerung
image: assets/images/en/attention-dilution.png
---

# Attention Dilution

![attention-dilution](assets/images/en/attention-dilution.png)

> The quality loss that sets in when one agent must give equal care to many items inside a single context: a review of a 14-file pull request, a scan across dozens of modules, a batch of flagged posts. The failure shows up as sequential decay and inconsistency, with early items analyzed deeply, later ones handled superficially, and identical patterns judged differently in different places. Unlike Lost in the Middle, which concerns where content sits in the input, dilution concerns how many items compete for analysis, so reordering does not help. The fix is architectural: per-item passes plus one cross-item integration pass, or delegation to scoped subagents, rather than a larger context window.

**See also:** [Lost in the Middle](lost-in-the-middle.md) · [Multi-Pass Review](multi-pass-review.md) · [Sub Agent](sub-agent.md)
{ .see-also }
