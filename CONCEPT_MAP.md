# Concept Maps: Agentic Software Modernization

Mermaid diagrams showing how glossary terms relate to each other.
These are source files — rendered visualizations can be generated from these.

---

## 1. The Agentic Loop and Its Dependencies

How the core agent cycle connects to the supporting infrastructure.

```mermaid
flowchart TD
    HE[Harness Engineering] -->|enables| AL[Agentic Loop]
    IE[Intent Engineering] -->|provides goals to| AL
    PE[Prompt Engineering] -->|instructs| AL
    ORCH[Orchestration] -->|coordinates multiple| AL
    MCP[MCP] -->|connects| TU[Tool Use]
    AL -->|uses| TU
    TU -->|calls| SA[Static Analysis]
    TU -->|calls| TH[Test Harness]
    TU -->|calls| AS[Agentic Search]
    SWA[Software Analytics] -->|feeds| GA[Guided AI]
    GA -->|targets scope for| AS
    GA -->|prioritizes focus of| AL
    AL -->|bounded by| CW[Context Window]
    CW -->|overcome by| RAG[RAG]
    CW -->|overcome by| CKG[Code Knowledge Graph]
    RAG -->|feeds| AL
    CKG -->|feeds| AL
    AL -->|risk of| H[Hallucination]
    AL -->|suffers from| CR[Context Rot]
    AL -->|susceptible to| CP[Context Poisoning]
    AL -->|degraded by| CPL[Context Pollution]
    CPL -->|overlaps with| CP
    AL -->|drifts via| PD[Prompt Drift]
    PD -->|accelerates| CR
    CP -->|increases risk of| H
    CR -->|increases risk of| H
    GR[Grounding] -->|reduces| H
    GR -->|counteracts| CP
    TH -->|detects| H
    CKG -->|detects| H
    AL -->|supervised by| HITL[Human-in-the-Loop]
    GL[Guardrails] -->|constrain| AL
    FL[Feedback Loop] -->|connects| TH
    FL -->|enables self-correction in| AL
    SS[Session Segmentation] -->|prevents| CR
    SS -->|prevents| PD
    SS -->|creates checkpoints for| HITL
    AO[Agent Observability] -->|diagnoses| CR
    AO -->|diagnoses| PD
    AO -->|surfaces| H
    BR[Blast Radius] -->|controlled by| SS
    BR -->|controlled by| GL
    MSP[Multi-Step Planning] -->|structures work for| AL
    MSP -->|supervised by| HITL
    ORCH -->|enables| MSP
    AM[Agent Memory] -->|extends reach of| CW
    AM -->|backed by| RAG
    AM -->|backed by| CKG
    CPR[Context Pruning] -->|removes noise from| CW
    CPR -->|counteracts| CPL
    CPR -->|counteracts| CR
```

---

## 2. Debt Model and Countermeasures

How the three debt types relate and what counters each.

```mermaid
flowchart LR
    AI[AI-generated code] -->|reduces| TD[Technical Debt]
    AI -->|accelerates| CD[Cognitive Debt]
    AI -->|accelerates| ID[Intent Debt]
    AI -->|produces| DC[Dark Code]
    DC -->|amplifies| CD
    CC[Code Comprehension] -->|reduces| DC

    AR[Automated Refactoring] -->|reduces| TD
    TH[Test Harness] -->|reduces| TD
    HE[Harness Engineering] -->|makes debt reduction possible| TD

    IE[Intent Engineering] -->|counters| ID
    ADR[ADRs / Specs] -->|counters| ID

    HITL[Human-in-the-Loop] -->|slows| CD
    CC[Code Comprehension] -->|reduces| CD
    DD[Drift Detection] -->|surfaces| CD
    DD -->|surfaces| ID

    TD -->|blocks| MOD[Modernization]
    CD -->|blocks| MOD
    ID -->|blocks| MOD
```

---

## 3. Modernization Patterns and Safety Net

How modernization patterns interact with verification mechanisms.

```mermaid
flowchart TD
    CC[Code Comprehension] -->|required before applying| SF[Strangler Fig Pattern]
    CC -->|required before applying| AR[Automated Refactoring]
    CKG[Code Knowledge Graph] -->|feeds| CC
    CKG -->|informs pattern selection for| SF

    CT[Characterization Test] -->|creates baseline for| SF
    TH[Test Harness / Safety Net] -->|enables safe| AR
    TH -->|enables safe| SF
    FF[Fitness Functions] -->|verify direction of| SF
    FF -->|verify direction of| AR
    ACL[Anti-Corruption Layer] -->|protects new code in| SF
    SA[Static Analysis] -->|feedback during| AR
    SA -->|feedback during| SF
    DD[Drift Detection] -->|monitors| SF
    DD -->|monitors| AR
```

---

## 4. Infrastructure Overview

How agent infrastructure components fit together.

```mermaid
flowchart TD
    HE[Harness Engineering] -->|assembles| INFRA[Agent Infrastructure]
    MCP[MCP] -->|connects agent to| Tools[Tools & Data Sources]
    Tools -->|IDE, Git, Build, DB| Agent[AI Agent]
    ORCH[Orchestration] -->|coordinates| Agent
    AWF[Agent Workflow Framework] -->|implements| ORCH
    PE[Prompt Engineering] -->|instructs| Agent
    RAG[RAG] -->|retrieves context for| Agent
    CKG[Code Knowledge Graph] -->|provides structure to| RAG
    CKG -->|provides structure to| Agent
    GL[Guardrails] -->|constrain| Agent
    HITL[Human-in-the-Loop] -->|checkpoint within| ORCH
    Agent -->|executes| AL[Agentic Loop]
    AS[Agentic Search] -->|part of| AL
    EMB[Embeddings] -->|powers| RAG
    EMB -->|enables semantic search in| AS
    SUB[Sub Agent] -->|orchestrated by| ORCH
    SUB -->|executes| AL
    AT[Agent Teams] -->|composed of| SUB
    AT -->|coordinated by| ORCH
    SO[Structured Output] -->|enables reliable handoff in| AT
    SO -->|enables| Tools
```

---

## 5. Supporting Techniques for Agent-Legible Code

How classic legacy-code techniques prepare a codebase so that agents can work within it effectively.

```mermaid
flowchart LR
    SP[Sprouting] -->|isolates new logic from| LC[Legacy Code]
    SM[Seams] -->|creates safe change points in| LC
    II[Incremental Improvement] -->|bounds blast radius of changes in| LC
    DDR[Domain-Driven Refactoring] -->|aligns structure and names in| LC

    LC -->|becomes legible to| AG[AI Agent]

    SP -->|shrinks context needed by| AG
    SM -->|enables local testing for| AG
    DDR -->|improves retrieval quality for| AG

    AG -->|can then safely apply| SF[Strangler Fig Pattern]
    AG -->|can then safely apply| AR[Automated Refactoring]
```

---

## 6. Full Concept Map (Overview)

All major term clusters and their connections.

```mermaid
mindmap
  root((Agentic Software Modernization))
    Agent Fundamentals
      AI Agent
      Agentic Loop
      Agentic Search
      Tool Use
      Context Window
      Agent Memory
      Multi-Step Planning
      Hallucination
      Context Rot
      Context Poisoning
      Context Pollution
      Context Pruning
      Prompt Drift
      Grounding
      Vibe Coding
    Infrastructure
      MCP
      Orchestration
      Agent Workflow Framework
      Sub Agent
      Agent Teams
      Structured Output
      Embeddings
      Prompt Engineering
      Context Engineering
      RAG
      Agent Runbook
      Dark Factory
    Analysis & Knowledge
      Code Comprehension
      Code Knowledge Graph
      Static Analysis
      Drift Detection
      Guided AI
      Codebase Conditioning
      Semantic Anchors
      Software Analytics
      Dark Code
    Modernization
      Technical Debt
      Cognitive Debt
      Comprehension Debt
      Intent Debt
      Strangler Fig Pattern
      Anti-Corruption Layer
      Automated Refactoring
      Sprouting
      Seams
      Incremental Improvement
      Domain-Driven Refactoring
      Slicing
      Feature Toggle
      Transitional Architecture
      Modernization Playbook
      Workload Design
      Conceptual Refactoring
      Clean Room Rewrite
      Horseshoe Model
      Idiomatic Transpilation
    Testing & Verification
      Test Harness
      Characterization Test
      Fitness Functions
      LLM as a Judge
    Engineering & Control
      Harness Engineering
      Intent Engineering
      Spec-Driven Development
      Guardrails
      Human-in-the-Loop
      Feedback Loop
      Session Segmentation
      Agent Observability
      Blast Radius
```
