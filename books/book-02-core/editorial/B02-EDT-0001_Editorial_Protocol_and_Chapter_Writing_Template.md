# Book 02

# B02-EDT-0001 — Editorial Protocol and Chapter Writing Template

**Document ID:** B02-EDT-0001

**Title:** Editorial Protocol and Chapter Writing Template

**Version:** 1.0.0

**Status:** Canonical Draft

**Category:** Editorial Standard

**Owner:** MarkOrbit Publications Editorial Board

**Applies To:** Book 02 — *MarkOrbit Core Specification*

**Depends On:**

- Book 02 TOC v1.2 — Frozen
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- MAC — MarkOrbit Architecture Canon
- MAG — MarkOrbit Architecture Governance
- MAS — MarkOrbit Architecture Specifications

---

# Purpose

This protocol defines how chapters of Book 02 shall be written.

Book 02 is not a general architecture essay.

Book 02 is not a product requirements document.

Book 02 is not an API manual.

Book 02 is the Core Specification of MarkOrbit.

Every chapter shall therefore contribute to one of the following outcomes:

- define a Core concept;
- establish a Core boundary;
- define a Core model;
- define a Core specification structure;
- define a Core contract;
- support MVP execution;
- guide Codex implementation.

If a chapter does not contribute to one of these outcomes, it shall not be included in Book 02.

---

# Editorial Position

Book 02 exists between Book 01 and implementation.

```text
Book 01
Operating Philosophy

        ↓

Book 02
Core Specification

        ↓

core-specs/
Executable Specifications

        ↓

Software Implementation
```

Book 02 explains and defines the Core.

`core-specs/` describes executable details.

Product documents define product-specific behavior.

Implementation documents define code, deployment and operations.

---

# Scope

This protocol applies to all manuscript chapters in Book 02.

It governs:

- chapter structure;
- writing responsibility;
- scope boundaries;
- specification output;
- execution mapping;
- exclusions;
- acceptance criteria.

It does not govern:

- product PRDs;
- UI design;
- API tutorials;
- prompt libraries;
- deployment guides;
- marketing copy;
- sales materials.

---

# Core Editorial Principle

Each chapter shall follow one primary responsibility.

```text
One Chapter
    =
One Core Responsibility
```

A chapter may reference many concepts, but it shall own only one core responsibility.

---

# Book 02 Writing Rules

## Rule 1 — Core Before Product

A chapter shall define Core responsibilities before discussing products.

Products consume Core.

Products shall not redefine Core.

---

## Rule 2 — Boundary Before Detail

A chapter shall first define what belongs to Core and what does not.

Details without boundaries shall not be written.

---

## Rule 3 — Specification Before Implementation

A chapter shall define what must exist before describing how it may be implemented.

Implementation examples are allowed only when they clarify the specification.

---

## Rule 4 — Contract Before Integration

Integration shall be defined through contracts.

A chapter shall not describe integration as informal connection.

---

## Rule 5 — Governance Before Automation

Automation, including AI automation, shall be governed by Core rules.

AI shall not bypass identity, permission, knowledge, audit or human review requirements.

---

## Rule 6 — Manuscript Before core-specs

The manuscript defines the Core logic.

`core-specs/` contains executable details.

The manuscript shall not duplicate all `core-specs/` content.

---

# Chapter Types

Every chapter belongs to one of four editorial types.

| Type | Purpose | Example Chapters |
|------|---------|------------------|
| Foundation Chapter | Establishes why, where and how Core exists | 02–08 |
| Architecture Chapter | Defines Core architecture and responsibility structure | 09–17 |
| Specification Chapter | Defines how Core entities are specified | 18–27 |
| Execution Chapter | Defines MVP and implementation boundary | 28–31 |

Each type uses the same base template but emphasizes different sections.

---

# Standard Chapter Structure

Every chapter shall follow this structure unless explicitly exempted.

```text
# Chapter XX — Chapter Title

1. Chapter Purpose
2. Core Question
3. Scope
4. Core Definition
5. Architectural Position
6. Core Rules
7. Boundary Rules
8. Specification Output
9. Execution Mapping
10. Relationship to core-specs/
11. Exclusions
12. Acceptance Criteria
13. Revision Notes
```

---

# Chapter Writing Template

```markdown
# Chapter XX — [Chapter Title]

**Chapter ID:** B02-CH-XX

**Part:** [Part Name]

**Chapter Type:** Foundation / Architecture / Specification / Execution

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

**Related Planning Documents:**

- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0

**Related Core Specs:**

- core-specs/[domain/object/service/event/agent/api]/...

---

# 1. Chapter Purpose

This section explains why this chapter exists.

It shall answer:

- What Core responsibility does this chapter define?
- Why is this responsibility necessary?
- What problem would occur if this chapter did not exist?
- What later chapters or specs depend on this chapter?

This section shall not include product features or implementation details.

---

# 2. Core Question

This section states the central question of the chapter.

Example:

> What is a Core Domain?

or:

> How shall products consume Core without redefining it?

The chapter shall answer this question directly.

---

# 3. Scope

This section defines what the chapter governs.

## In Scope

- [Item 1]
- [Item 2]
- [Item 3]

## Out of Scope

- [Item 1]
- [Item 2]
- [Item 3]

Out-of-scope items shall be explicitly redirected to the correct location.

Example:

- Product UI belongs to product specifications.
- Detailed API endpoints belong to `core-specs/api/`.
- Prompt templates belong to agent implementation documents.

---

# 4. Core Definition

This section defines the primary Core concept of the chapter.

The definition shall be stable, reusable and implementation-independent.

Example:

> A Core Object is a persistent, referable and auditable representation of a stable business or system entity within the MarkOrbit Core.

Definitions shall not depend on a specific product, database table, UI page or AI model.

---

# 5. Architectural Position

This section explains where the concept belongs in the MarkOrbit architecture.

It shall clarify:

- which architectural layer owns it;
- which later layers consume it;
- whether it belongs to Core, Business, Workplace, Network or Product;
- what must not redefine it.

Example:

```text
Core provides execution primitives.
Workplace operates execution.
Products consume execution contracts.
```

---

# 6. Core Rules

This section defines the rules that must always apply.

Rules shall be written as normative statements.

Use:

- SHALL
- SHALL NOT
- SHOULD
- MAY

Example:

- A Core Object SHALL belong to one primary Core Domain.
- A Product SHALL NOT redefine the semantic meaning of a Core Object.
- AI output SHALL be auditable when used in professional work.

---

# 7. Boundary Rules

This section defines boundaries.

It shall answer:

- What belongs to Core?
- What belongs to Workplace?
- What belongs to Product?
- What belongs to `core-specs/`?
- What belongs to implementation?

Boundary rules are required for every chapter.

---

# 8. Specification Output

This section states what specification asset the chapter produces.

Examples:

- Domain Specification Template
- Object Specification Template
- Service Contract Template
- Event Specification Rules
- AI Capability Governance Rules
- Core Consumption Contract

If the chapter does not produce a specification output, it shall produce an architectural decision or boundary rule.

---

# 9. Execution Mapping

This section maps the chapter to implementation only at the appropriate level.

For Foundation Chapters, execution mapping may be indirect.

For Specification and Execution Chapters, execution mapping shall be explicit.

Possible outputs include:

- Domain Model
- Database Table
- Service
- API
- Event
- AI Agent
- Workflow Contract
- Codex Task
- Product Consumption Rule

This section shall not contain full implementation code.

---

# 10. Relationship to core-specs/

This section defines what shall be moved into `core-specs/`.

Example:

```text
This chapter defines the structure of Domain Specification.

Detailed domain specifications shall be stored under:

core-specs/domains/
```

The manuscript shall not duplicate detailed executable specifications.

---

# 11. Exclusions

This section lists what this chapter shall not include.

Common exclusions:

- UI design;
- product-specific workflows;
- marketing content;
- pricing policy;
- deployment details;
- prompt templates;
- full API tutorials;
- implementation code;
- unsupported AI automation.

---

# 12. Acceptance Criteria

A chapter is accepted only if it satisfies all required criteria.

Example:

- The chapter defines one Core responsibility.
- The chapter distinguishes Core from Product.
- The chapter identifies related `core-specs/` assets.
- The chapter includes boundary rules.
- The chapter avoids implementation overreach.
- The chapter supports Book 02 TOC v1.2.
- The chapter does not conflict with Book 01, MAC, MAG or MAS.

---

# 13. Revision Notes

This section records editorial decisions, unresolved issues and future review points.

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial chapter draft. |
```

---

# Chapter Type Guidance

## Foundation Chapter Guidance

Foundation Chapters include:

- 02 Why Core Exists
- 03 Core Position
- 04 Core Boundary
- 05 Core Principles
- 06 From Professional OS to Core Kernel
- 07 Professional Value Flow
- 08 Ontology and Domain Classification

Foundation Chapters shall focus on:

- purpose;
- position;
- principles;
- conceptual boundaries;
- value flow;
- ontology;
- architectural decisions.

Foundation Chapters are not required to map directly to database tables or APIs.

They must, however, produce clear architectural decisions.

---

## Architecture Chapter Guidance

Architecture Chapters include:

- 09 Core Kernel Overview
- 10 Architecture Layers
- 11 Responsibility Flow
- 12 Canonical Models
- 13 Core Domain Architecture
- 14 Core Object Architecture
- 15 Core Service Architecture
- 16 Core Execution Primitives
- 17 Core Contract Architecture

Architecture Chapters shall focus on:

- architectural structure;
- responsibility allocation;
- ownership;
- dependency;
- layer boundaries;
- invariants;
- reusable models.

They shall avoid product-specific behavior.

---

## Specification Chapter Guidance

Specification Chapters include:

- 18 Identity Specification
- 19 Capability Specification
- 20 Knowledge Specification
- 21 Business Responsibility Specification
- 22 Domain Specification
- 23 Object Specification
- 24 Service Specification
- 25 Event Specification
- 26 AI Capability and Agent Governance Specification
- 27 Core Consumption Specification

Specification Chapters shall define how Core specification units are written.

Each chapter shall produce a reusable specification framework or template.

They shall not become generic tutorials.

They shall not duplicate MAS.

They shall be specific to MarkOrbit Core.

---

## Execution Chapter Guidance

Execution Chapters include:

- 28 Core MVP Boundary
- 29 MVP Domain Priority
- 30 MVP Execution Matrix
- 31 Codex Implementation Roadmap

Execution Chapters shall define how Book 02 becomes executable.

They shall focus on:

- MVP inclusion;
- MVP exclusion;
- priority;
- execution assets;
- Codex task generation;
- validation;
- acceptance criteria.

They shall not become full project management plans.

---

# Manuscript vs core-specs Boundary

The following boundary is mandatory.

| Content | Location |
|---------|----------|
| Core meaning | manuscript/ |
| Core architecture | manuscript/ |
| Core principles | manuscript/ |
| Specification framework | manuscript/ |
| Detailed Domain specs | core-specs/domains/ |
| Detailed Object specs | core-specs/objects/ |
| Detailed Service specs | core-specs/services/ |
| Detailed Event specs | core-specs/events/ |
| Detailed Agent specs | core-specs/agents/ |
| API surface | core-specs/api/ |
| Workflow contracts | core-specs/workflows/ |
| Codex tasks | indexes/codex-task-index.md or planning/ |

---

# Forbidden Content

The following content shall not be included in Book 02 manuscript chapters.

- Product UI details
- Product pricing
- Marketing positioning
- Sales copy
- Deployment scripts
- Framework-specific code
- Prompt libraries
- Unreviewed AI legal opinions
- Full product PRDs
- Product onboarding manuals
- Operational SOPs not reusable by Core
- Vendor-specific implementation details

---

# AI Writing Rules

AI-related chapters shall follow these rules.

## Rule 1

AI shall enhance professional work.

AI shall not define professional truth.

---

## Rule 2

AI shall use authorized knowledge sources.

AI shall not invent legal rules, filing requirements or professional conclusions.

---

## Rule 3

AI output used in professional work shall be auditable.

---

## Rule 4

High-risk professional actions shall require human review.

---

## Rule 5

AI Agents shall not bypass identity, permission, workflow, event or knowledge governance.

---

# Core / Workplace / Product Boundary

Book 02 shall maintain the following boundary.

```text
Core
    provides models, objects, services, primitives and contracts

Workplace
    operates work through composition, workflow and experience

Product
    delivers user-facing functionality
```

Book 02 may define:

- Task Primitive;
- Event Primitive;
- State Primitive;
- Context Primitive;
- Workflow Contract;
- Notification Contract.

Book 02 shall not define:

- product workflow screens;
- daily operation UI;
- product-specific user journeys;
- workplace interaction design.

---

# Chapter Completion Checklist

Before a chapter can move from Draft to Review, it must satisfy the following checklist.

- [ ] The chapter owns one primary responsibility.
- [ ] The chapter aligns with Book 02 TOC v1.2.
- [ ] The chapter defines its Core scope.
- [ ] The chapter defines what is out of scope.
- [ ] The chapter distinguishes manuscript content from `core-specs/`.
- [ ] The chapter avoids product-specific PRD content.
- [ ] The chapter avoids implementation overreach.
- [ ] The chapter includes Core boundary rules.
- [ ] The chapter includes acceptance criteria.
- [ ] The chapter does not conflict with Book 01.
- [ ] The chapter does not conflict with MAC, MAG or MAS.
- [ ] The chapter can guide future development.

---

# Chapter Review Questions

Reviewers shall ask the following questions.

1. Does this chapter define Core, or merely describe a product?
2. Does this chapter introduce a stable architectural decision?
3. Does this chapter preserve the boundary between Core, Workplace and Product?
4. Does this chapter duplicate content that belongs in `core-specs/`?
5. Does this chapter duplicate Book 01?
6. Does this chapter conflict with MAC, MAG or MAS?
7. Does this chapter support MVP execution?
8. Can Codex use this chapter directly or indirectly?
9. Are AI-related claims governed and auditable?
10. Should any section be moved out of the manuscript?

---

# Definition of Done

A Book 02 chapter is done only when:

- it is structurally complete;
- it has one primary responsibility;
- it establishes clear Core boundaries;
- it produces a specification, rule, model or execution decision;
- related `core-specs/` assets are identified;
- exclusions are explicit;
- review checklist is satisfied;
- no product-specific overreach remains.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical Draft | Initial editorial protocol and chapter writing template for Book 02. |

---

**End of Document**