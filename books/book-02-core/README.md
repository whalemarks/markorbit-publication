# Book 02 — MarkOrbit Core Specification

**Repository:** `book-02-core`  
**Project:** MarkOrbit / 有标国际商标平台  
**Book Title:** MarkOrbit Core Specification  
**Book Type:** Core Architecture and Execution Specification  
**Draft Stage:** Second Canonical Draft  
**Status:** Canonical Draft — Rewrite in Progress  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Repository Purpose

This repository contains **Book 02 — MarkOrbit Core Specification**.

Book 02 defines the MarkOrbit Core.

The MarkOrbit Core is the shared specification kernel that turns professional operating philosophy into reusable execution architecture for products, Workplaces, AI agents, network services, `core-specs/`, Codex tasks and software implementation.

This repository is not a product PRD.

It is not a UI design document.

It is not a database-only design.

It is not a prompt library.

It is not a deployment guide.

It is the canonical source for Core meaning, Core boundary, Core principles, Core domains, Core objects, Core services, Core events, Core contracts, AI governance, Core consumption rules and MVP execution control.

---

# 2. Repository Position

Book 02 sits between Book 01 and all executable or product layers.

```text
Book 01 — Professional OS
        ↓
Book 02 — MarkOrbit Core Specification
        ↓
Book 03 — Workplace Framework
        ↓
Book 04 — MarkReg
Book 05 — MarkOrbit Lite
Book 06 — Mark Global Service Network
        ↓
Appendices and Indexes
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Software Implementation
```

Book 02 converts professional operating philosophy into executable Core architecture.

Later products may consume the Core.

Later implementation may realize the Core.

Neither products nor implementation may redefine the Core.

---

# 3. Core Position Statement

The MarkOrbit Core is:

> the shared specification layer that defines reusable professional meaning, execution primitives and consumption contracts for the MarkOrbit ecosystem.

The Core sits between Professional OS and implementation.

```text
Professional OS
        ↓
Core Specification
        ↓
Appendices and Indexes
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Software Implementation
        ↓
Product Experience
```

The dependency direction must not be reversed.

A product feature may expose a missing Core concept.

An implementation problem may expose a specification gap.

An AI use case may expose a governance requirement.

But those findings must return to Core governance before changing Core meaning.

---

# 4. Core Principle Statement

Book 02 is governed by the following principle statement:

```text
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
AI assists under governance.
Codex implements approved specifications.
```

This statement means:

```text
Principles define the architecture.
Core provides shared primitives and contracts.
Business owns commercial and professional responsibility.
Execution coordinates work through tasks, events, states and workflows.
Integration connects external systems through contracts.
Products consume Core to deliver experiences.
AI assists through governed Agent Contracts.
Codex implements only approved specifications.
```

No later layer may reverse this order.

---

# 5. Core Boundary

The MarkOrbit Core owns:

```text
canonical professional meaning
baseline domain classification
Core Object meaning
Core Service responsibility
Core Event semantics
Core Contract types
Core Execution Primitives
Identity and permission foundations
Knowledge governance
AI capability governance
Core consumption rules
MVP execution boundaries
Codex implementation constraints
```

The MarkOrbit Core does not own:

```text
product user interfaces
product-specific user journeys
commercial pricing packages
sales tactics
full workplace experience
complete global service marketplace
vendor-specific integrations
deployment architecture
production prompt libraries
full data warehouse implementation
final professional judgment without human responsibility
```

Boundary rule:

```text
Core owns shared meaning.
Business owns commercial responsibility.
Workplace owns operating experience.
Products own user-facing delivery.
Network owns collaboration operation.
AI assists under governance.
Codex implements approved specifications.
Infrastructure runs the system.
```

---

# 6. Core Principles

Book 02 uses thirteen Core Principles.

```text
P1 — Core Before Product
P2 — Meaning Before Data
P3 — Boundary Before Detail
P4 — Domain Before Object
P5 — Object Before Service
P6 — Service Before Automation
P7 — Event Before Coordination
P8 — Contract Before Consumption
P9 — Governance Before AI
P10 — Responsibility Before Delegation
P11 — Appendix Before core-specs
P12 — Specification Before Codex
P13 — MVP Before Expansion
```

These principles apply to:

```text
manuscript chapters
appendices
indexes
core-specs/
Codex tasks
implementation
product books
AI agents
workflow design
integration design
```

---

# 7. Repository Structure

Canonical repository structure:

```text
book-02-core/
├── README.md
├── publication.yaml
├── CHANGELOG.md
├── planning/
├── editorial/
├── manuscript/
├── appendices/
├── core-specs/
│   ├── domains/
│   ├── objects/
│   ├── services/
│   ├── events/
│   ├── contracts/
│   ├── api/
│   ├── agents/
│   └── workflows/
├── indexes/
├── codex-tasks/
│   ├── wave-0/
│   ├── wave-1/
│   ├── wave-2/
│   ├── wave-3/
│   ├── wave-4/
│   ├── wave-5/
│   ├── wave-6/
│   └── wave-7/
├── assets/
└── releases/
```

---

# 8. Directory Responsibilities

## 8.1 `planning/`

Stores planning documents and architecture decisions.

Canonical files:

```text
B02-PLN-0001_Core_Positioning.md
B02-PLN-0002_Architecture_Blueprint_v2.0.md
B02-PLN-0003_Core_Domain_Map_v1.0.md
B02-PLN-0004_Core_Execution_Matrix_v1.0.md
```

Planning files are source traces.

They do not override the second canonical draft.

## 8.2 `editorial/`

Stores editorial protocol, review documents, fix plans and rewrite control documents.

Current editorial streams include:

```text
B02-EDT-0001_Editorial_Protocol_and_Chapter_Writing_Template.md
B02-REV-R1_Round1_Manuscript_Architecture_Review.md
B02-REV-R2_Round2_Packaged_Manuscript_Review.md
B02-REV-R3_Round3_PreAppendix_Gate_Review.md
B02-REV-R4_Round4_Appendix_Blueprint_and_Index_Gate_Review.md
B02-REV-R1-FIXPLAN_Round1_Fix_Plan.md
B02-REV-R2-FIXPLAN_Round2_Repository_and_Appendix_Fix_Plan.md
B02-REWRITE-0001_Book_02_Rewrite_Plan_and_Document_List.md
```

## 8.3 `manuscript/`

Stores Book 02 manuscript chapters.

Canonical range:

```text
B02-CH-00_Preface.md
...
B02-CH-31_Codex_Implementation_Roadmap.md
```

The manuscript defines Core meaning, architecture, boundaries, principles and execution control.

## 8.4 `appendices/`

Stores canonical reference appendices.

Required files:

```text
B02-APP-A_Glossary.md
B02-APP-B_Core_Domain_Index.md
B02-APP-C_Core_Object_Index.md
B02-APP-D_Core_Service_Index.md
B02-APP-E_Event_Index.md
B02-APP-F_API_Index.md
B02-APP-G_Agent_Index.md
B02-APP-H_Codex_Task_Index.md
```

Appendices stabilize canonical lists before detailed `core-specs/` generation.

## 8.5 `core-specs/`

Stores executable Core specifications.

This directory should be generated only after appendices and baseline indexes are ready.

```text
core-specs/domains/      Core Domain specs
core-specs/objects/      Core Object specs
core-specs/services/     Core Service specs
core-specs/events/       Core Event specs
core-specs/contracts/    Data/API/Event/Agent/Workflow/Consumption contracts
core-specs/api/          API surface specs
core-specs/agents/       AI Agent and Agent Contract specs
core-specs/workflows/    Workflow Contract specs
```

## 8.6 `indexes/`

Stores searchable indexes generated from appendices and `core-specs/`.

Expected files:

```text
domain-index.md
object-index.md
service-index.md
event-index.md
contract-index.md
api-index.md
agent-index.md
workflow-index.md
consumer-index.md
mvp-execution-matrix.md
codex-task-index.md
```

## 8.7 `codex-tasks/`

Stores Codex implementation task files grouped by roadmap wave.

Codex tasks must not be generated before Appendix H and baseline indexes are complete.

## 8.8 `assets/`

Stores diagrams, tables and supporting visuals.

## 8.9 `releases/`

Stores release notes, release candidate reports and versioned snapshots.

---

# 9. Book 02 Manuscript Contents

## Part I — Core Foundation

```text
00 Preface
01 Table of Contents
02 Why Core Exists
03 Core Position
04 Core Boundary
05 Core Principles
06 From Professional OS to Core Kernel
07 Professional Value Flow
08 Ontology and Domain Classification
```

## Part II — Core Kernel Architecture

```text
09 Core Kernel Overview
10 Architecture Layers
11 Responsibility Flow
12 Canonical Models
13 Core Domain Architecture
14 Core Object Architecture
15 Core Service Architecture
16 Core Execution Primitives
17 Core Contract Architecture
```

## Part III — Core Specification System

```text
18 Identity Specification
19 Capability Specification
20 Knowledge Specification
21 Business Responsibility Specification
22 Domain Specification
23 Object Specification
24 Service Specification
25 Event Specification
26 AI Capability and Agent Governance Specification
27 Core Consumption Specification
```

## Part IV — Core Execution Boundary

```text
28 Core MVP Boundary
29 MVP Domain Priority
30 MVP Execution Matrix
31 Codex Implementation Roadmap
```

## Appendices

```text
Appendix A — Glossary
Appendix B — Core Domain Index
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
```

---

# 10. Second Canonical Draft Rewrite Status

The first manuscript draft has completed architecture discovery.

The second canonical draft is a consolidation rewrite.

It focuses on:

```text
terminology consistency
boundary clarity
domain classification
cross-chapter alignment
appendix readiness
index readiness
Codex readiness
```

Priority rewritten chapters include:

```text
B02-CH-03_Core_Position.md
B02-CH-04_Core_Boundary.md
B02-CH-05_Core_Principles.md
B02-CH-08_Ontology_and_Domain_Classification.md
B02-CH-13_Core_Domain_Architecture.md
B02-CH-22_Domain_Specification.md
B02-CH-23_Object_Specification.md
B02-CH-24_Service_Specification.md
B02-CH-25_Event_Specification.md
B02-CH-26_AI_Capability_and_Agent_Governance_Specification.md
B02-CH-27_Core_Consumption_Specification.md
B02-CH-28_Core_MVP_Boundary.md
B02-CH-29_MVP_Domain_Priority.md
B02-CH-30_MVP_Execution_Matrix.md
B02-CH-31_Codex_Implementation_Roadmap.md
```

Remaining work before second canonical draft release:

```text
Generate Appendices A–H
Normalize root metadata
Generate release candidate report
Hold core-specs/ until appendices are complete
Hold Codex tasks until Appendix H and indexes are complete
```

---

# 11. Baseline Core Domains

The canonical baseline Core Domain Map contains 26 domains.

```text
Foundation Domains
    Identity
    Organization
    User
    Permission
    Policy
    Knowledge

Professional Domains
    Brand
    Trademark
    Jurisdiction
    Classification
    Document
    Evidence

Business Execution Domains
    Customer
    Matter
    Order
    Opportunity
    Workflow Contract
    Task
    Event
    Notification

Collaboration Network Domains
    Partner
    Agent
    Service Provider
    Service Network
    Routing
    Communication
```

This 26-domain baseline must not be changed silently.

Any change to the baseline domain map requires architecture review.

---

# 12. Cross-Cutting Specification Systems

Book 02 recognizes two cross-cutting Core specification systems:

```text
Capability
Business Responsibility
```

They are not counted as additional baseline Core Domains.

They may produce executable specs, objects, services, events and contracts.

They govern multiple domains.

Canonical clarification:

```text
Capability and Business Responsibility are cross-cutting Core specification systems.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

This clarification resolves the distinction between:

```text
26 baseline Core Domains
28 MVP priority rows = 26 domains + 2 cross-cutting systems
```

---

# 13. MVP Depth Types

Each Core Domain or cross-cutting system must be classified by MVP depth.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Definitions:

```text
Must Implement
    required for the first executable Core kernel

Partial Implement
    requires stable spec and minimal implementation if needed by first consumers

Reserved Boundary
    not deeply implemented yet, but future boundary must be protected

Deferred
    outside MVP and not implemented unless explicitly approved
```

---

# 14. Consumer Classification

Book 02 classifies consumers as MVP, Partial or Future.

## 14.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

These consumers shape the Core MVP.

## 14.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

These require reserved or partial Core support but must not pull full future product scope into MVP.

## 14.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

These may be supported by future Core extensions.

They do not define MVP scope.

---

# 15. Core Consumption Rule

Canonical consumption rules:

```text
Consume, do not redefine.
Contract before consumption.
Read and write boundaries must be explicit.
Services mediate state change.
Events communicate meaningful change.
AI requires Agent Contract.
Codex requires source specifications.
Future consumers do not expand MVP scope automatically.
```

Consumer categories:

```text
Product Consumer
Workplace Consumer
AI Agent Consumer
Internal Service Consumer
External Integration Consumer
Data / Reporting Consumer
Codex Implementation Consumer
```

---

# 16. AI Governance Rule

AI is governed by the Core.

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

AI execution requires:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Structured Context
Allowed Object Access
Allowed Services
Permission and Policy
Risk Level
Human Review
AI Events
AI Audit
Failure Behavior
Product Consumer Binding
```

Prompt-only AI is outside the Core boundary.

No Agent Contract means no AI Core consumption.

---

# 17. Event Rule

A Core Event is a meaningful change in Core state, professional execution, review requirement, AI output, routing decision, communication linkage or workflow progress.

An Event is not merely:

```text
a log line
a UI click
an activity feed row
a queue message
an analytics ping
```

Meaningful state changes must emit Events where downstream coordination, audit, workflow or review depends on them.

---

# 18. API Rule

An API is a governed exposure of Core Services, Core Objects or Core Events.

An API is not simply a route.

API consumption requires:

```text
API name
owning domain/service
consumer
input contract
output contract
permission requirement
policy requirement
event side effects
audit requirement
MVP status
```

Appendix F — API Index must be generated before detailed `core-specs/api/` expansion.

---

# 19. Codex Implementation Waves

Codex implementation follows eight waves.

```text
Wave 0 — Repository and Spec Scaffold
Wave 1 — Foundation Core
Wave 2 — Professional Core
Wave 3 — Business Execution Core
Wave 4 — AI Governance and Review
Wave 5 — Product Consumption Baseline
Wave 6 — Growth Core Baseline
Wave 7 — Validation, Hardening and Release
```

Codex must implement from approved specs and matrix rows.

Codex does not define Core architecture.

---

# 20. Codex Rules

```text
Specs Before Code
Matrix Before Task
Small Tasks Before Large Tasks
Domain Ownership Before Model Creation
Contracts Before Product Integration
Events Before Automation
Agent Contract Before AI Feature
Tests Before Acceptance
Deferred Scope Must Stay Deferred
Architecture Review Before Semantic Change
```

Every Codex task must include:

```text
Task ID
Wave
Source Specs
Matrix Row
Dependencies
In Scope
Out of Scope
Expected Outputs
Tests Required
Acceptance Criteria
Prohibited Overreach
Status
```

---

# 21. Status Vocabulary

Status values must be separated by layer.

## 21.1 Publication Status

```text
draft
canonical_draft
reviewing
approved
released
deprecated
superseded
archived
```

## 21.2 Chapter Status

```text
Draft
Reviewing
Approved
Revised
Deprecated
Superseded
Archived
```

## 21.3 Spec Status

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

## 21.4 Codex Task Status

```text
Draft
Ready
In Progress
Blocked
Implemented
Tested
Accepted
Rejected
Deferred
Superseded
```

## 21.5 Implementation Status

```text
Not Started
Planned
In Progress
Implemented
Tested
Accepted
Deferred
Blocked
Deprecated
```

## 21.6 Release Status

```text
planning
manuscript_draft_completed
appendix_in_progress
spec_scaffold_ready
implementation_in_progress
release_candidate
released
archived
```

---

# 22. Current Repository Status

Current state:

```text
Book 02 manuscript chapters 00–31: Draft complete
Second canonical rewrite: In progress
Priority rewritten chapters: Complete
Appendices: Pending
core-specs/: Hold
indexes/: Hold
Codex task index: Hold
MVP implementation: Hold
```

Hold rules:

```text
Do not generate detailed core-specs/ until Appendices A–H are complete.
Do not generate Codex implementation tasks until Appendix H and indexes exist.
```

---

# 23. Acceptance Standard

Book 02 second canonical draft is acceptable when:

```text
README.md, publication.yaml and CHANGELOG.md are aligned
Appendices A–H are generated
26-domain baseline is preserved
Capability and Business Responsibility are clarified as cross-cutting systems
API Index exists
AI Agent / AI Output / AI Audit are indexed
Consumers are classified as MVP / Partial / Future
priority rewritten chapters are accepted
planning file B02-PLN-0003 is normalized
execution boundary reflects review findings
core-specs/ generation remains held until appendices are complete
Codex tasks remain held until Appendix H and indexes are ready
```

Core MVP is acceptable only when:

```text
core-specs/ structure exists
MVP domain specs exist
MVP object specs exist
MVP service specs exist
MVP event specs exist
MVP contract specs exist
MVP agent specs exist
MarkReg, Lite and Workplace have consumption contracts
AI agents operate under Agent Contracts
meaningful actions emit Events
high-risk AI output creates ReviewRequired
Core Object changes are auditable where risk exists
Codex tasks reference specs and acceptance criteria
deferred domains have reserved boundaries
```

---

# 24. Prohibited Shortcuts

Do not:

```text
build product screens before Core meaning
create database tables without Object specs
implement AI prompts without Agent Contracts
create services without domain ownership
change state without Events
consume Core without contracts
let products redefine Core meanings
let Codex invent architecture
let reporting redefine Event or status meanings
implement deferred marketplace or analytics features early
```

---

# 25. Recommended Workflow

Recommended repository workflow:

```text
1. Read Chapters 03, 04 and 05 for position, boundary and principles.
2. Read Chapters 08 and 13 for ontology and domain architecture.
3. Read Chapters 22–27 for specification rules.
4. Read Chapters 28–31 for MVP and Codex execution boundary.
5. Generate Appendix A — Glossary.
6. Generate Appendix B — Core Domain Index.
7. Generate Appendix C — Core Object Index.
8. Generate Appendix D — Core Service Index.
9. Generate Appendix E — Event Index.
10. Generate Appendix F — API Index.
11. Generate Appendix G — Agent Index.
12. Generate Appendix H — Codex Task Index.
13. Generate baseline indexes/ from appendices.
14. Scaffold core-specs/.
15. Generate Codex Wave 0 tasks.
16. Implement through Codex waves.
17. Validate contracts, events, AI governance and consumption rules.
18. Prepare release candidate report.
```

---

# 26. Immediate Next Steps

```text
1. Generate Appendix A — Glossary
2. Generate Appendix B — Core Domain Index
3. Generate Appendix C — Core Object Index
4. Generate Appendix D — Core Service Index
5. Generate Appendix E — Event Index
6. Generate Appendix F — API Index
7. Generate Appendix G — Agent Index
8. Generate Appendix H — Codex Task Index
9. Update publication.yaml to version 0.2.0
10. Update CHANGELOG.md for second canonical draft rewrite
```

---

**End of README**
