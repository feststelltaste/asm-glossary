---
title: Agentic Software Modernization Glossary
description: Definitions of the core concepts, patterns, and practices behind modernizing legacy software systems with AI agents.
hide:
  - toc
---

# Agentic Software Modernization Glossary

**Agentic software modernization** is the practice of using [AI agents](ai-agent.md), LLM-based systems capable of autonomous, multi-step reasoning and [tool use](tool-use.md), to analyze, refactor, and migrate legacy software systems. Rather than relying solely on manual effort or purely rule-based automation, this approach aims for the sweet spot between non-deterministic and deterministic workloads, keeping a high level of automation while preserving controlled autonomy. Agentic modernization acknowledges the limitations of AI agents working with legacy code and applies supporting techniques such as [sprouting](sprouting.md), [seams](seams.md), [incremental improvement](incremental-improvement.md), and [domain-driven refactoring](domain-driven-refactoring.md) to shape the codebase into something agents can meaningfully work with. Within this scaffolding, agents generate transformation plans, execute changes, and verify results, reducing [technical debt](technical-debt.md) without introducing [cognitive debt](cognitive-debt.md), all under human supervision.

The approach combines established modernization patterns (such as [Strangler Fig](strangler-fig.md) and [Anti-Corruption Layer](anti-corruption-layer.md)) with agent-specific capabilities like [agentic search](agentic-search.md), [code knowledge graphs](code-knowledge-graph.md), and [retrieval-augmented generation](rag.md). [Guardrails](guardrails.md), [test harnesses](test-harness.md), and [human-in-the-loop](human-in-the-loop.md) checkpoints keep the process safe and auditable.

---

## Fundamentals

[AI Agent](ai-agent.md) · [Agent Memory](agent-memory.md) · [Agentic Loop](agentic-loop.md) · [Agentic Search](agentic-search.md) · [Attribution](attribution.md) · [Context Poisoning](context-poisoning.md) · [Context Pollution](context-pollution.md) · [Context Pruning](context-pruning.md) · [Context Rot](context-rot.md) · [Context Window](context-window.md) · [Grounding](grounding.md) · [Hallucination](hallucination.md) · [Multi-Step Planning](multi-step-planning.md) · [Prompt Drift](prompt-drift.md) · [Structured Output](structured-output.md) · [Tool Use](tool-use.md) · [Vibe Coding](vibe-coding.md)

## Analysis & Knowledge

[Code Comprehension](code-comprehension.md) · [Code Knowledge Graph](code-knowledge-graph.md) · [Codebase Conditioning](codebase-conditioning.md) · [Dark Code](dark-code.md) · [Drift Detection](drift-detection.md) · [Guided AI](guided-ai.md) · [Semantic Anchors](semantic-anchors.md) · [Software Analytics](software-analytics.md) · [Static Analysis](static-analysis.md)

## Modernization

[Anti-Corruption Layer (ACL)](anti-corruption-layer.md) · [Automated Refactoring](automated-refactoring.md) · [Clean Room Rewrite](clean-room-rewrite.md) · [Cognitive Debt](cognitive-debt.md) · [Comprehension Debt](comprehension-debt.md) · [Conceptual Refactoring](conceptual-refactoring.md) · [Domain-Driven Refactoring](domain-driven-refactoring.md) · [Feature Toggle](feature-toggle.md) · [Horseshoe Model](horseshoe-model.md) · [Idiomatic Transpilation](idiomatic-transpilation.md) · [Incremental Improvement](incremental-improvement.md) · [Intent Debt](intent-debt.md) · [Modernization Case](modernization-case.md) · [Modernization Playbook](modernization-playbook.md) · [Seams](seams.md) · [Slicing](slicing.md) · [Sprouting](sprouting.md) · [Strangler Fig Pattern](strangler-fig.md) · [Technical Debt](technical-debt.md) · [Transitional Architecture](transitional-architecture.md) · [Workload Design](workload-design.md)

## Testing & Verification

[Characterization Test](characterization-test.md) · [Fitness Functions](fitness-functions.md) · [LLM as a Judge](llm-as-a-judge.md) · [Test Harness](test-harness.md)

## Engineering & Control

[Agent Observability](agent-observability.md) · [Blast Radius](blast-radius.md) · [Feedback Loop](feedback-loop.md) · [Guardrails](guardrails.md) · [Harness Engineering](harness-engineering.md) · [Human-in-the-Loop](human-in-the-loop.md) · [Intent Engineering](intent-engineering.md) · [Pattern Diffing](pattern-diffing.md) · [Review Fatigue](review-fatigue.md) · [Session Segmentation](session-segmentation.md) · [Spec-Driven Development](spec-driven-development.md)

## Infrastructure

[Agent Runbook](agent-runbook.md) · [Agent Teams](agent-teams.md) · [Agent Workflow Framework](agent-workflow-framework.md) · [Commands](commands.md) · [Context Engineering](context-engineering.md) · [Dark Factory](dark-factory.md) · [Embeddings](embeddings.md) · [Hooks](hooks.md) · [MCP (Model Context Protocol)](mcp.md) · [Orchestration](orchestration.md) · [Prompt Engineering](prompt-engineering.md) · [RAG (Retrieval-Augmented Generation)](rag.md) · [Skills](skills.md) · [Sub Agent](sub-agent.md)
