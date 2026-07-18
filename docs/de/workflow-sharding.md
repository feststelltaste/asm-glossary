---
title: Workflow-Sharding
category: Infrastruktur
translation_en: workflow-sharding
translation_en_title: Workflow Sharding
image: assets/images/workflow-sharding.png
---

# Workflow-Sharding

![workflow-sharding](assets/images/workflow-sharding.png)

> Ein Muster, um viele Agenten mit minimaler Koordination an einer Transformation arbeiten zu lassen: Die Arbeitslast wird in unabhängige Shards aufgeteilt, jeder Shard erhält einen isolierten Worktree, und die Agenten innerhalb eines Shards arbeiten, ohne je mit einem anderen Shard sprechen zu müssen. Weil die Shards nichts teilen, muss kein Orchestrator zwischen ihnen vermitteln, und der Gesamtdurchsatz skaliert ungefähr mit der Anzahl der Shards, bis Merge-Konflikte und Reviewkapazität zum Engpass werden. Eingesetzt in großen agentengetriebenen Portierungen wie der Bun-Neuimplementierung in Rust.

**Siehe auch:** [Slicing](slicing.md) · [Agententeams](agententeams.md) · [Portierungsleitfaden](portierungsleitfaden.md)
{ .see-also }
