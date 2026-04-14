# Concept Maps

!!! warning "Experimentell"
    Diese Concept Maps sind automatisch generierte Entwürfe. Sie zeigen ungefähre Zusammenhänge zwischen Glossarbegriffen und sind möglicherweise nicht vollständig oder in allen Details korrekt.

Mermaid-Diagramme, die zeigen, wie die Glossarbegriffe zueinander in Beziehung stehen.

---

## 1. Der agentische Zyklus und seine Abhängigkeiten

Wie der zentrale Agentenzyklus mit der unterstützenden Infrastruktur zusammenhängt.

```mermaid
flowchart TD
    HE[Harness Engineering] -->|ermöglicht| AL[Agentischer Zyklus]
    IE[Intent Engineering] -->|liefert Ziele für| AL
    PE[Prompt Engineering] -->|instruiert| AL
    ORCH[Orchestrierung] -->|koordiniert mehrere| AL
    MCP[MCP] -->|verbindet| TU[Tool Use]
    AL -->|nutzt| TU
    TU -->|ruft| SA[Statische Analyse]
    TU -->|ruft| TH[Test Harness]
    TU -->|ruft| AS[Agentische Suche]
    SWA[Software Analytics] -->|speist| GA[Guided AI]
    GA -->|fokussiert Scope für| AS
    GA -->|priorisiert Fokus von| AL
    AL -->|begrenzt durch| CW[Kontextfenster]
    CW -->|überwunden durch| RAG[RAG]
    CW -->|überwunden durch| CKG[Code Knowledge Graph]
    RAG -->|speist| AL
    CKG -->|speist| AL
    AL -->|Risiko von| H[Halluzination]
    AL -->|leidet unter| CR[Context Rot]
    AL -->|anfällig für| CP[Context Poisoning]
    AL -->|driftet durch| PD[Prompt Drift]
    PD -->|beschleunigt| CR
    CP -->|erhöht Risiko von| H
    CR -->|erhöht Risiko von| H
    GR[Grounding] -->|reduziert| H
    GR -->|wirkt gegen| CP
    TH -->|erkennt| H
    CKG -->|erkennt| H
    AL -->|überwacht durch| HITL[Human-in-the-Loop]
    GL[Leitplanken] -->|beschränken| AL
    FL[Feedback Loop] -->|verbindet| TH
    FL -->|ermöglicht Selbstkorrektur in| AL
    SS[Session Segmentation] -->|verhindert| CR
    SS -->|verhindert| PD
    SS -->|schafft Checkpoints für| HITL
    AO[Agent Observability] -->|diagnostiziert| CR
    AO -->|diagnostiziert| PD
    AO -->|deckt auf| H
    BR[Blast Radius] -->|kontrolliert durch| SS
    BR -->|kontrolliert durch| GL
```

---

## 2. Schuldenmodell und Gegenmaßnahmen

Wie die drei Schuldenarten zusammenhängen und was ihnen entgegenwirkt.

```mermaid
flowchart LR
    AI[KI-generierter Code] -->|reduziert| TD[Technische Schulden]
    AI -->|beschleunigt| CD[Kognitive Schulden]
    AI -->|beschleunigt| ID[Intent Debt]

    AR[Automatisiertes Refactoring] -->|reduziert| TD
    TH[Test Harness] -->|reduziert| TD
    HE[Harness Engineering] -->|ermöglicht Schuldenabbau bei| TD

    IE[Intent Engineering] -->|wirkt gegen| ID
    ADR[ADRs / Specs] -->|wirken gegen| ID

    HITL[Human-in-the-Loop] -->|bremst| CD
    CC[Code-Verständnis] -->|reduziert| CD
    DD[Drift Detection] -->|deckt auf| CD
    DD -->|deckt auf| ID

    TD -->|blockiert| MOD[Modernisierung]
    CD -->|blockiert| MOD
    ID -->|blockiert| MOD
```

---

## 3. Modernisierungsmuster und Sicherheitsnetz

Wie Modernisierungsmuster mit Verifikationsmechanismen zusammenwirken.

```mermaid
flowchart TD
    CC[Code-Verständnis] -->|Voraussetzung für| SF[Strangler Fig Pattern]
    CC -->|Voraussetzung für| AR[Automatisiertes Refactoring]
    CKG[Code Knowledge Graph] -->|speist| CC
    CKG -->|informiert Musterwahl für| SF

    GM[Golden Master Testing] -->|erstellt Baseline für| SF
    TH[Test Harness / Sicherheitsnetz] -->|ermöglicht sicheres| AR
    TH -->|ermöglicht sicheres| SF
    FF[Fitnessfunktionen] -->|verifizieren Richtung von| SF
    FF -->|verifizieren Richtung von| AR
    ACL[Anti-Corruption Layer] -->|schützt neuen Code in| SF
    SA[Statische Analyse] -->|Feedback während| AR
    SA -->|Feedback während| SF
    DD[Drift Detection] -->|überwacht| SF
    DD -->|überwacht| AR
```

---

## 4. Infrastrukturübersicht

Wie die Komponenten der Agenteninfrastruktur zusammenpassen.

```mermaid
flowchart TD
    HE[Harness Engineering] -->|baut auf| INFRA[Agenteninfrastruktur]
    MCP[MCP] -->|verbindet Agent mit| Tools[Tools & Datenquellen]
    Tools -->|IDE, Git, Build, DB| Agent[KI-Agent]
    ORCH[Orchestrierung] -->|koordiniert| Agent
    AWF[Agent Workflow Framework] -->|implementiert| ORCH
    PE[Prompt Engineering] -->|instruiert| Agent
    RAG[RAG] -->|beschafft Kontext für| Agent
    CKG[Code Knowledge Graph] -->|liefert Struktur für| RAG
    CKG -->|liefert Struktur für| Agent
    GL[Leitplanken] -->|beschränken| Agent
    HITL[Human-in-the-Loop] -->|Checkpoint innerhalb| ORCH
    Agent -->|führt aus| AL[Agentischer Zyklus]
    AS[Agentische Suche] -->|Teil von| AL
```

---

## 5. Unterstützende Techniken für agentenlesbaren Code

Wie klassische Legacy-Code-Techniken eine Codebasis vorbereiten, damit Agenten effektiv darin arbeiten können.

```mermaid
flowchart LR
    SP[Sprouting] -->|isoliert neue Logik von| LC[Legacy Code]
    SM[Seams] -->|schafft sichere Änderungspunkte in| LC
    II[Inkrementelle Verbesserung] -->|begrenzt Auswirkungsradius in| LC
    DDR[Domain-Driven Refactoring] -->|gleicht Struktur und Namen an in| LC

    LC -->|wird lesbar für| AG[KI-Agent]

    SP -->|reduziert benötigten Kontext für| AG
    SM -->|ermöglicht lokales Testen für| AG
    DDR -->|verbessert Retrieval-Qualität für| AG

    AG -->|kann dann sicher anwenden| SF[Strangler Fig Pattern]
    AG -->|kann dann sicher anwenden| AR[Automatisiertes Refactoring]
```

---

## 6. Gesamtübersicht

Alle wichtigen Begriffscluster und ihre Verbindungen.

```mermaid
mindmap
  root((Agentische Softwaremodernisierung))
    Grundlagen
      KI-Agent
      Agentischer Zyklus
      Agentische Suche
      Tool Use
      Kontextfenster
      Halluzination
      Context Rot
      Context Poisoning
      Prompt Drift
      Grounding
    Infrastruktur
      MCP
      Orchestrierung
      Agent Workflow Framework
      Prompt Engineering
      RAG
      Agent Runbook
    Analyse & Wissen
      Code-Verständnis
      Code Knowledge Graph
      Statische Analyse
      Drift Detection
      Guided AI
      Codebase Conditioning
      Semantic Anchors
      Software Analytics
    Modernisierung
      Technische Schulden
      Kognitive Schulden
      Intent Debt
      Strangler Fig Pattern
      Anti-Corruption Layer
      Automatisiertes Refactoring
      Sprouting
      Seams
      Inkrementelle Verbesserung
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
    Testing & Verifikation
      Test Harness
      Golden Master Testing
      Fitnessfunktionen
    Engineering & Control
      Harness Engineering
      Intent Engineering
      Leitplanken
      Human-in-the-Loop
      Feedback Loop
      Session Segmentation
      Agent Observability
      Blast Radius
```
