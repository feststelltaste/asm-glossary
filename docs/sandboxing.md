---
title: Sandboxing
category: Engineering & Control
translation_de: sandboxing
translation_de_title: Sandboxing
image: assets/images/en/sandboxing.png
---

# Sandboxing

![sandboxing](assets/images/en/sandboxing.png)

> Running an agent's actions, its shell commands, code execution, and file operations, inside an isolated environment such as a container or restricted filesystem, so that even a destructive or manipulated action cannot reach the host system, production data, or the network beyond an allowlist. Where guardrails define what an agent should not do, sandboxing removes the ability to do it: the policy is enforced by the environment, not by instructions. This makes it the mechanism of last resort that holds even when prompts fail, tools misfire, or the model is manipulated by hostile input.

**See also:** [Guardrails](guardrails.md) · [Blast Radius](blast-radius.md) · [Harness Engineering](harness-engineering.md)
{ .see-also }
