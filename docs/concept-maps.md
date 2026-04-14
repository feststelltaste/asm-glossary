# Concept Maps

!!! warning "Experimental"
    These concept maps are auto-generated drafts. They show approximate relationships between glossary terms and may not be complete or fully accurate.

Mermaid diagrams showing how glossary terms relate to each other.

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
    AL -->|involves| MSP[Multi-Step Planning]
    MSP -->|checked by| HITL[Human-in-the-Loop]
    TU -->|calls| SA[Static Analysis]
    TU -->|calls| TH[Test Harness]
    TU -->|calls| AS[Agentic Search]
    GA[Guided AI] -->|targets scope for| AS
    GA -->|prioritizes focus of| AL
    AL -->|bounded by| CW[Context Window]
    CW -->|overcome by| RAG[RAG]
    CW -->|overcome by| CKG[Code Knowledge Graph]
    AM[Agent Memory] -->|persists across| CW
    RAG -->|feeds| AL
    CKG -->|feeds| AL
    AL -->|risk of| H[Hallucination]
    GR[Grounding] -->|reduces| H
    TH -->|detects| H
    CKG -->|detects| H
    AL -->|degraded by| CR[Context Rot]
    AL -->|degraded by| PD[Prompt Drift]
    AL -->|degraded by| CP[Context Poisoning]
    SS[Session Segmentation] -->|mitigates| CR
    AL -->|supervised by| HITL
    GL[Guardrails] -->|constrain| AL
    AO[Agent Observability] -->|monitors| AL
    FL[Feedback Loop] -->|improves| AL
```

---

## 2. Debt Model and Countermeasures

How the three debt types relate and what counters each.

```mermaid
flowchart LR
    AI[AI-generated code] -->|reduces| TD[Technical Debt]
    AI -->|accelerates| CD[Cognitive Debt]
    AI -->|accelerates| ID[Intent Debt]

    AR[Automated Refactoring] -->|reduces| TD
    TH[Test Harness] -->|reduces| TD
    HE[Harness Engineering] -->|makes debt reduction possible| TD
    CR[Conceptual Refactoring] -->|reduces| CD

    IE[Intent Engineering] -->|counters| ID
    ADR[ADRs / Specs] -->|counters| ID

    HITL[Human-in-the-Loop] -->|slows| CD
    CC[Code Comprehension] -->|reduces| CD
    DD[Drift Detection] -->|surfaces| CD
    DD -->|surfaces| ID
    SANA[Software Analytics] -->|informs| DD

    TD -->|blocks| MOD[Modernization]
    CD -->|blocks| MOD
    ID -->|blocks| MOD

    MP[Modernization Playbook] -->|guides| MOD
    TA[Transitional Architecture] -->|structures| MOD
    WD[Workload Design] -->|scopes| MOD
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
    TH[Test Harness] -->|enables safe| AR
    TH -->|enables safe| SF
    FF[Fitness Functions] -->|verify direction of| SF
    FF -->|verify direction of| AR
    ACL[Anti-Corruption Layer] -->|protects new code in| SF
    FT[Feature Toggle] -->|enables gradual rollout in| SF
    SA[Static Analysis] -->|feedback during| AR
    SA -->|feedback during| SF
    DD[Drift Detection] -->|monitors| SF
    DD -->|monitors| AR

    SL[Slicing] -->|decomposes| SF
    SL -->|decomposes| AR
    HM[Horseshoe Model] -->|structures| CRW[Clean Room Rewrite]
    IT[Idiomatic Transpilation] -->|enables| CRW
    CT -->|validates| CRW
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
    AT[Agent Teams] -->|structured by| ORCH
    SA[Sub Agent] -->|part of| AT
    PE[Prompt Engineering] -->|instructs| Agent
    CMD[Commands] -->|trigger| Agent
    SK[Skills] -->|extend| Agent
    HK[Hooks] -->|intercept actions of| Agent
    RAG[RAG] -->|retrieves context for| Agent
    EMB[Embeddings] -->|power| RAG
    CKG[Code Knowledge Graph] -->|provides structure to| RAG
    CKG -->|provides structure to| Agent
    GL[Guardrails] -->|constrain| Agent
    HITL[Human-in-the-Loop] -->|checkpoint within| ORCH
    Agent -->|executes| AL[Agentic Loop]
    AS[Agentic Search] -->|part of| AL
    ARB[Agent Runbook] -->|guides| Agent
    SO[Structured Output] -->|enables coordination in| AT
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
    CBC[Codebase Conditioning] -->|prepares| LC
    SAN[Semantic Anchors] -->|stabilize meaning in| LC
    CR[Conceptual Refactoring] -->|clarifies abstractions in| LC

    LC -->|becomes legible to| AG[AI Agent]

    SP -->|shrinks context needed by| AG
    SM -->|enables local testing for| AG
    DDR -->|improves retrieval quality for| AG
    SAN -->|improve grounding for| AG
    BR[Blast Radius] -->|constrained by| SM
    BR -->|constrained by| II

    AG -->|can then safely apply| SF[Strangler Fig Pattern]
    AG -->|can then safely apply| AR[Automated Refactoring]
```

---

## 6. Full Concept Map (Overview)

All major term clusters and their connections.

```mermaid
mindmap
  root((Agentic Software Modernization))
    Grundlagen
      AI Agent
      Agent Memory
      Agentic Loop
      Agentic Search
      Context Poisoning
      Context Pollution
      Context Pruning
      Context Rot
      Context Window
      Grounding
      Hallucination
      Multi-Step Planning
      Prompt Drift
      Structured Output
      Tool Use
      Vibe Coding
    Infrastruktur
      Agent Runbook
      Agent Teams
      Agent Workflow Framework
      Commands
      Context Engineering
      Dark Factory
      Embeddings
      Hooks
      MCP (Model Context Protocol)
      Orchestration
      Prompt Engineering
      RAG (Retrieval-Augmented Generation)
      Skills
      Sub Agent
    Analysis & Knowledge
      Code Comprehension
      Code Knowledge Graph
      Codebase Conditioning
      Dark Code
      Drift Detection
      Guided AI
      Semantic Anchors
      Software Analytics
      Static Analysis
    Modernization
      Anti-Corruption Layer (ACL)
      Automated Refactoring
      Clean Room Rewrite
      Cognitive Debt
      Comprehension Debt
      Conceptual Refactoring
      Domain-Driven Refactoring
      Feature Toggle
      Horseshoe Model
      Idiomatic Transpilation
      Incremental Improvement
      Intent Debt
      Modernization Playbook
      Seams
      Slicing
      Sprouting
      Strangler Fig Pattern
      Technical Debt
      Transitional Architecture
      Workload Design
    Testing & Verification
      Characterization Test
      Fitness Functions
      LLM as a Judge
      Test Harness
    Engineering & Control
      Agent Observability
      Blast Radius
      Feedback Loop
      Guardrails
      Harness Engineering
      Human-in-the-Loop
      Intent Engineering
      Session Segmentation
      Spec-Driven Development
```
