# CHANGELOG

**Book:** Book 02 — MarkOrbit Core Specification  
**Repository:** `book-02-core`  
**Document:** CHANGELOG.md  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# Release History

This changelog records major architecture, manuscript, repository and specification changes for Book 02 — MarkOrbit Core Specification.

Book 02 is currently in the second canonical draft rewrite stage.

Current state:

```text
Book 02 manuscript chapters 00–31: Draft complete
Second canonical rewrite: In progress
Priority rewritten chapters: Complete
Root metadata rewrite: In progress
Appendices: Pending
indexes/: Hold
core-specs/: Hold
Codex task generation: Hold
MVP implementation: Hold
```

---

# 0.2.0 — Second Canonical Draft Rewrite

**Status:** In Progress  
**Release Type:** Architecture Consolidation / Second Canonical Draft  
**Date:** 2026-07-06  

## Summary

Version 0.2.0 begins the second canonical draft of Book 02.

The first draft established the full architecture direction. The second canonical draft consolidates that architecture into a more stable, appendix-ready and Codex-safe specification system.

This release does not start implementation.

This release prepares the manuscript, root metadata and appendices for executable `core-specs/` generation later.

---

## 0.2.0 Release Decision

```text
SECOND CANONICAL DRAFT IN PROGRESS
PRIORITY REWRITTEN CHAPTERS COMPLETE
APPENDICES PENDING
CORE-SPECS GENERATION REMAINS ON HOLD
CODEX TASK GENERATION REMAINS ON HOLD
MVP IMPLEMENTATION REMAINS ON HOLD
```

---

## 0.2.0 Architecture Locks

The following architecture decisions are locked for the second canonical draft.

```text
Book 02 defines the MarkOrbit Core itself.
Book 02 is not a product PRD.
Book 02 is not a software design document.
Book 02 is not an AI prompt library.
Book 02 is not a Codex task list.
```

The Core principle is locked as:

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

The dependency direction is locked as:

```text
Professional OS
↓
MarkOrbit Core Specification
↓
Appendices and Indexes
↓
core-specs/
↓
Codex Tasks
↓
Software Implementation
↓
Products / Workplace / Network
```

---

## 0.2.0 Canonical Domain Lock

The canonical baseline Core Domain Map remains 26 domains.

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

Capability and Business Responsibility are locked as cross-cutting Core specification systems.

```text
Capability and Business Responsibility may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

---

## 0.2.0 Consumer Classification Lock

Consumers are classified as follows.

```text
MVP Consumers
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
    Codex Implementation

Partial Consumers
    MGSN
    Opportunity Engine baseline
    Brand Asset Vault baseline

Future Consumers
    Partner Center
    Client Portal
    Service Platform
    External Integrations
    Reporting Consumers
```

Future consumers do not automatically expand MVP scope.

---

## 0.2.0 MVP Depth Lock

MVP depth types are locked as:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Core MVP is defined as:

```text
Core MVP is the first executable kernel.
It is not the full MarkOrbit platform.
```

---

## 0.2.0 AI Governance Lock

AI governance is locked as:

```text
AI is a governed capability.
AI is not the Core.
AI is not above the Core.
AI is not a replacement for professional responsibility.
```

AI usage requires:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Structured Context
Allowed Object Access
Permission and Policy
Risk Level
Human Review
AI Events
AI Audit
Failure Behavior
Product Consumer Binding
```

---

## 0.2.0 Event Governance Lock

Event governance is locked as:

```text
A Core Event is a meaningful change.
```

A Core Event is not:

```text
a log
a UI action
an activity feed item
a queue message
an analytics ping
```

Event naming remains:

```text
Event Name: PascalCase
Event File Name: lowercase-kebab-case.md
```

---

## 0.2.0 API Governance Lock

API is now explicitly treated as a contract-bound Core consumption surface.

There is still no standalone API chapter, but Appendix F is mandatory.

Required future artifact:

```text
appendices/B02-APP-F_API_Index.md
core-specs/api/_template.md
```

---

## 0.2.0 Codex Governance Lock

Codex governance is locked as:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

Codex must not invent:

```text
Core domains
Core object meanings
service responsibilities
event semantics
AI authority
product ownership boundaries
workflow states
deferred features
```

Codex task generation remains on hold until Appendix H and indexes exist.

---

# 0.2.0 Rewritten Root Documents

The following root documents have been rewritten or scheduled in the second canonical draft.

| Document | Status | Notes |
|----------|--------|-------|
| README.md | Rewritten | Repository overview, Core position, structure, governance rules and hold rules updated. |
| publication.yaml | Rewritten | Metadata updated for second canonical draft, domain locks, consumer classification, appendices and hold rules. |
| CHANGELOG.md | Rewritten | This document. Version history, architecture locks and next actions updated. |

---

# 0.2.0 Rewritten Priority Chapters

The first priority rewrite batch is complete.

| Chapter | Title | Status | Rewrite Focus |
|---------|-------|--------|---------------|
| B02-CH-03 | Core Position | Rewritten | Core position across Book 01, Workplace, products, AI, Codex and implementation. |
| B02-CH-04 | Core Boundary | Rewritten | Core owns / does not own, cross-layer boundaries and anti-patterns. |
| B02-CH-05 | Core Principles | Rewritten | 13 enforceable Core Principles. |
| B02-CH-08 | Ontology and Domain Classification | Rewritten | 26-domain baseline and cross-cutting systems. |
| B02-CH-13 | Core Domain Architecture | Rewritten | Domain ownership, dependency, MVP depth and Appendix B readiness. |
| B02-CH-22 | Domain Specification | Rewritten | Domain Specification template and domain spec rules. |
| B02-CH-23 | Object Specification | Rewritten | Object Specification template and meaning-before-data rule. |
| B02-CH-24 | Service Specification | Rewritten | Service Specification template and governed capability rule. |
| B02-CH-25 | Event Specification | Rewritten | Event meaning, naming, payload and governance rules. |
| B02-CH-26 | AI Capability and Agent Governance Specification | Rewritten | AI governance, Agent Contract and AI audit rules. |
| B02-CH-27 | Core Consumption Specification | Rewritten | Consumer categories, contracts and boundaries. |
| B02-CH-28 | Core MVP Boundary | Rewritten | MVP scope and deferred scope protection. |
| B02-CH-29 | MVP Domain Priority | Rewritten | 28 priority rows = 26 domains + 2 cross-cutting systems. |
| B02-CH-30 | MVP Execution Matrix | Rewritten | Matrix-to-Codex mapping and execution gates. |
| B02-CH-31 | Codex Implementation Roadmap | Rewritten | Codex Wave 0–7 and pre-Codex gates. |

---

# 0.2.0 Documents Still Requiring Controlled Rewrite

These chapters remain structurally useful but require controlled rewrite or normalization.

```text
B02-CH-09_Core_Kernel_Overview.md
B02-CH-10_Architecture_Layers.md
B02-CH-11_Responsibility_Flow.md
B02-CH-12_Canonical_Models.md
B02-CH-14_Core_Object_Architecture.md
B02-CH-15_Core_Service_Architecture.md
B02-CH-16_Core_Execution_Primitives.md
B02-CH-17_Core_Contract_Architecture.md
B02-CH-18_Identity_Specification.md
B02-CH-19_Capability_Specification.md
B02-CH-20_Knowledge_Specification.md
B02-CH-21_Business_Responsibility_Specification.md
```

---

# 0.2.0 Documents Requiring Light Normalization

These chapters mainly require terminology alignment and final TOC/status synchronization.

```text
B02-CH-00_Preface.md
B02-CH-01_Table_of_Contents.md
B02-CH-02_Why_Core_Exists.md
B02-CH-06_From_Professional_OS_to_Core_Kernel.md
B02-CH-07_Professional_Value_Flow.md
```

---

# 0.2.0 Repository Structure Changes

The repository structure is now defined as:

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
├── assets/
└── releases/
```

`appendices/` is now formally part of the repository structure.

Detailed `core-specs/`, `indexes/` and `codex-tasks/` remain on hold.

---

# 0.2.0 Appendices Status

Appendices are pending generation.

They must be generated before detailed `core-specs/` and Codex implementation tasks.

Required appendix order:

```text
1. B02-APP-A — Glossary
2. B02-APP-B — Core Domain Index
3. B02-APP-C — Core Object Index
4. B02-APP-D — Core Service Index
5. B02-APP-E — Event Index
6. B02-APP-F — API Index
7. B02-APP-G — Agent Index
8. B02-APP-H — Codex Task Index
```

---

# 0.2.0 Hold Rules

## core-specs Hold

Detailed `core-specs/` generation remains on hold until:

```text
Appendices A–H are complete.
Baseline indexes exist.
API Index is complete.
AI Object and Agent indexes are complete.
```

## indexes Hold

`indexes/` remains on hold until appendices are complete.

## Codex Hold

Codex implementation task generation remains on hold until:

```text
Appendix H is complete.
indexes/codex-task-index.md exists.
Codex task template exists.
core-specs/ template scaffold exists.
```

## MVP Implementation Hold

MVP implementation remains on hold until:

```text
Second canonical draft is accepted.
Appendices A–H are complete.
core-specs/ scaffold exists.
Wave 0 Codex tasks are approved.
```

---

# 0.2.0 Acceptance Criteria

Version 0.2.0 can be accepted when:

```text
[ ] README.md is rewritten and aligned.
[ ] publication.yaml is rewritten and aligned.
[ ] CHANGELOG.md is rewritten and aligned.
[ ] Priority rewritten chapters are complete.
[ ] 26-domain baseline is preserved.
[ ] Capability and Business Responsibility are classified as cross-cutting systems.
[ ] MVP / Partial / Future consumer classification is present.
[ ] AI governance rule is present.
[ ] Event governance rule is present.
[ ] API Index requirement is present.
[ ] Codex governance rule is present.
[ ] Appendices A–H are generated.
[ ] indexes/ generation is scheduled after appendices.
[ ] core-specs/ generation remains held until indexes exist.
[ ] Codex tasks remain held until Appendix H and indexes exist.
```

---

# 0.1.0 — Canonical Draft

**Status:** Completed as First Draft  
**Release Type:** Initial Canonical Draft / Manuscript Completion  

## Summary

Version 0.1.0 completed the first full manuscript draft of Book 02.

The first draft established:

```text
Book 02 positioning
Core foundation
Core kernel architecture
Core specification system
Core execution boundary
MVP domain priority
MVP execution matrix
Codex implementation roadmap
```

## Manuscript Completion

The first draft completed all manuscript chapters:

```text
B02-CH-00 through B02-CH-31
```

Round 2 review later confirmed:

```text
manuscript/B02-CH-00 through B02-CH-31 are present
all manuscript paths listed in publication.yaml exist
no manuscript chapter is missing
no extra manuscript chapter was found outside publication.yaml
chapter metadata IDs match file numbers
all manuscript chapters end with “End of Chapter”
```

## 0.1.0 Limitation

The first draft was sufficient to express the architecture, but not sufficient for direct implementation.

It required:

```text
second canonical rewrite
appendices
indexes
core-specs scaffolding
Codex task governance
```

---

# Review History

## Round 1 — Manuscript Architecture Review

Decision:

```text
Book 02 manuscript body is architecturally coherent and ready for Round 1 fixes plus appendices.
```

Key issues:

```text
R1-001 Capability / Business Responsibility cross-layer positioning
R1-002 API Specification scaffold needed
R1-003 Appendices A–H before core-specs/
R1-004 Repository packaging needed
R1-005 MVP / Future consumer classification support
R1-006 AI Agent / AI Audit / AI Output need index confirmation
```

## Round 2 — Packaged Manuscript Review

Decision:

```text
PASS — Manuscript Complete
PASS — Architecture Coherent
PASS WITH FIXES — Repository Metadata
NOT YET — core-specs Generation
NOT YET — Codex Task Generation
```

## Round 3 — Pre-Appendix Gate Review

Decision:

```text
APPROVED FOR APPENDICES
NOT APPROVED FOR CORE-SPECS GENERATION YET
NOT APPROVED FOR CODEX TASK GENERATION YET
```

## Round 4 — Appendix Blueprint and Canonical Index Gate Review

Decision:

```text
APPENDIX GENERATION MAY START.
APPENDIX A — GLOSSARY MUST BE FIRST.
CORE-SPECS GENERATION REMAINS ON HOLD.
CODEX TASK GENERATION REMAINS ON HOLD.
```

---

# Next Actions

Immediate next actions:

```text
1. Generate B02-APP-A_Glossary.md.
2. Generate B02-APP-B_Core_Domain_Index.md.
3. Generate Appendices C–H in sequence.
4. Generate indexes/ after appendices.
5. Scaffold core-specs/ after indexes.
6. Generate Codex Wave 0 tasks only after Appendix H and indexes are complete.
```

---

## Book 02 v0.1 baseline freeze

- PR #22 merged as the content baseline for the Book 02 v0.1 Core specification.
- Content baseline commit: `a0a31c9a784854c8943eee448337cb91ad316bb4`.
- Status/Workflow contract and fixture coverage is accepted.
- Book 02 structural work is closed.
- Book 02 is frozen as the v0.1 Core specification baseline.
- Future non-semantic errata remain allowed through labeled maintenance changes.
- Semantic changes require a Book 02 Change Proposal.
- Implementation architecture moves to Book 04.
- Project-specific work moves to relevant project repositories.
- External protected actions remain unauthorized.

Historical next-action entries remain as publication history
and are superseded by this baseline freeze record.

**End of CHANGELOG**
