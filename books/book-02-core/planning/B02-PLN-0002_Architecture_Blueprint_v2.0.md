# Book 02

# B02-PLN-0002 — Architecture Blueprint v2.0

**Document ID:** B02-PLN-0002

**Title:** Architecture Blueprint v2.0

**Version:** 2.0.0

**Status:** Canonical Draft

**Category:** Planning

**Owner:** MarkOrbit Publications Editorial Board

**Applies To:** Book 02 — *MarkOrbit Core Specification*

**Related Documents:**

- Book 01 — *The Operating System for Global Brand Services*
- Book 02 TOC v1.2 — Frozen
- B02-PLN-0001 — Core Positioning
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template
- MAC — MarkOrbit Architecture Canon
- MAG — MarkOrbit Architecture Governance
- MAS — MarkOrbit Architecture Specifications

---

# 1. Purpose

This document defines the architecture blueprint of Book 02 — *MarkOrbit Core Specification*.

It establishes the permanent architectural structure that Book 02 shall specify.

It does not replace the manuscript.

It does not replace `core-specs/`.

It does not define product-specific requirements.

Its purpose is to align:

- the Book 02 manuscript;
- Core planning documents;
- Core executable specifications;
- future products;
- Codex implementation tasks.

Every chapter, model, specification, domain, object, service, event, AI capability and implementation task related to Book 02 shall ultimately align with this blueprint.

---

# 2. Blueprint Statement

Book 02 defines the MarkOrbit Core.

The MarkOrbit Core is the shared professional operating core for global brand services.

It provides the stable models, domains, objects, services, execution primitives and contracts that later publications, products and implementations consume.

Book 02 is therefore the specification of the Core.

It is not the specification of any single product.

---

# 3. Architectural Objective

The objective of Book 02 is to make the MarkOrbit Core executable without turning Book 02 into a product PRD.

Book 02 shall define:

- what the Core is;
- where the Core sits;
- what the Core owns;
- what the Core does not own;
- how the Core is structured;
- how Core concepts are specified;
- how Core details move into `core-specs/`;
- how Core becomes executable through MVP and Codex.

The central architectural objective is:

```text
Stable Core
        ↓
Executable Specifications
        ↓
Reusable Products
```

---

# 4. Architectural Position

Book 02 sits between Book 01 and all later implementation.

```text
Book 01
Operating Philosophy
        ↓
Book 02
Core Specification
        ↓
Book 03
Workplace Framework
        ↓
Book 04 / Book 05 / Book 06
Product and Network Publications
        ↓
Software Implementation
```

Book 01 defines why MarkOrbit exists.

Book 02 defines the Core that makes MarkOrbit executable.

Book 03 defines how professional work is organized in Workplace.

Book 04, Book 05 and Book 06 define how specific products and networks consume the Core.

Software implementation realizes the Core through code, databases, APIs, events, AI agents, workflows and product modules.

---

# 5. Relationship to Architecture Library

The Architecture Library provides architecture standards.

Book 02 applies those standards to the MarkOrbit Core.

```text
Architecture Library
    ├── MAC — Architecture Canon
    ├── MAG — Architecture Governance
    └── MAS — Architecture Specifications
        ↓
Book 02 — MarkOrbit Core Specification
```

The relationship is:

- MAC defines architectural meaning.
- MAG governs architectural evolution.
- MAS defines how architecture specifications are represented.
- Book 02 defines the MarkOrbit Core using those standards.

Book 02 shall conform to MAC, MAG and MAS.

Book 02 shall not duplicate them.

---

# 6. Relationship to Book 01

Book 01 defines the Professional Operating System.

Book 02 defines the Core that makes the Professional Operating System executable.

The transition is:

```text
Professional OS
        ↓
Core Specification
```

Book 02 shall not repeat Book 01.

It shall translate Book 01 into:

- Core Models;
- Core Domains;
- Core Objects;
- Core Services;
- Execution Primitives;
- Core Contracts;
- Core Consumption Rules;
- MVP Execution Boundaries.

---

# 7. Professional OS to Core Mapping

Book 02 shall preserve the conceptual structure of Book 01 while translating it into Core architecture.

```text
Book 01 Professional OS
        ↓
Book 02 Core

Persistence
        ↓
Data, Records and Core Objects

Brain
        ↓
Knowledge Model and Knowledge Services

Intelligence
        ↓
AI Capability and Agent Governance

Capability
        ↓
Core Services and Reusable Capabilities

Workflow
        ↓
Execution Primitives and Workflow Contracts

Guide
        ↓
Workplace Consumption and Product Experience
```

This mapping protects continuity between Book 01 and Book 02.

It also prevents Book 02 from becoming a disconnected technical model.

---

# 8. Professional Value Flow

The MarkOrbit Core shall support the professional value flow defined by the operating philosophy.

```text
Reality
        ↓
Facts
        ↓
Understanding
        ↓
Judgment
        ↓
Action
        ↓
Coordination
        ↓
Experience
```

Book 02 translates this flow into architecture.

```text
Reality
        ↓
Core Objects

Facts
        ↓
Data and Knowledge

Understanding
        ↓
Knowledge Services

Judgment
        ↓
AI Capability and Professional Rules

Action
        ↓
Core Services and Execution Primitives

Coordination
        ↓
Contracts, Events and Routing

Experience
        ↓
Workplace and Product Consumption
```

The Core shall not stop at data storage.

The Core shall support professional judgment, action and coordination.

---

# 9. Core Architecture Overview

The MarkOrbit Core is organized into seven architectural components.

```text
Canonical Models
        ↓
Core Domains
        ↓
Core Objects
        ↓
Core Services
        ↓
Execution Primitives
        ↓
Core Contracts
        ↓
Core Consumption
```

These components form the Core Kernel of MarkOrbit.

“Core Kernel” is an explanatory concept.

The official publication title remains:

```text
Book 02 — MarkOrbit Core Specification
```

---

# 10. Architecture Layers

Book 02 uses the following architecture layers.

```text
Principles
        ↓
Core
        ↓
Business Responsibility
        ↓
Execution Primitives
        ↓
Integration Contracts
        ↓
Products
```

Each layer owns one primary responsibility.

## 10.1 Principles Layer

Defines the architectural logic and operating philosophy inherited from Book 01 and the Architecture Library.

## 10.2 Core Layer

Defines the shared models, domains, objects and services.

## 10.3 Business Responsibility Layer

Defines ownership, delegation, authorization, value creation and commercial responsibility.

It does not define pricing, packages or product commercial policies.

## 10.4 Execution Primitives Layer

Defines events, tasks, states, contexts, notification contracts and workflow contracts.

It does not own workflow execution.

## 10.5 Integration Contracts Layer

Defines data, API, event, agent, workflow and consumption contracts.

## 10.6 Products Layer

Consumes the Core.

Products deliver user-facing functionality.

Products shall not redefine the Core.

---

# 11. Responsibility Flow

Book 02 adopts the following responsibility flow.

```text
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
```

Responsibilities shall not flow in the opposite direction.

Products may request extensions.

Products shall not redefine Core meaning.

Workplaces may operate work.

Workplaces shall not redefine Core Objects or Core Services.

AI agents may execute capabilities.

AI agents shall not define professional truth.

---

# 12. Canonical Models

Book 02 owns the canonical models required by the Core.

## 12.1 Identity Model

Defines persistent identity across persons, organizations, users, partners, agents, service providers and workplaces.

## 12.2 Capability Model

Defines reusable capabilities that can be consumed by products, services, workflows and AI agents.

## 12.3 Knowledge Model

Defines how professional knowledge becomes searchable, linked, validated and executable.

## 12.4 Business Responsibility Model

Defines ownership, delegation, authorization, responsibility and value creation.

## 12.5 Workplace Model

Defines the Core-level relationship between Core and Workplace.

Detailed Workplace architecture belongs to Book 03.

## 12.6 Network Model

Defines the Core-level relationship between Core and global collaboration networks.

Detailed network architecture belongs to Book 06.

---

# 13. Core Domain Architecture

Book 02 defines the architecture of Core Domains.

A Core Domain is an executable business boundary.

A Core Domain is not merely:

- a database table;
- a UI page;
- a product module;
- a feature group.

Every Core Domain shall define:

- responsibility;
- boundary;
- primary objects;
- services;
- events;
- permissions;
- AI capability usage;
- product consumers;
- MVP priority.

Detailed domain specifications shall live in:

```text
core-specs/domains/
```

---

# 14. Domain Classification

Core Domains are classified into four categories.

```text
Foundation Domains
        ↓
Professional Domains
        ↓
Execution Domains
        ↓
Collaboration Domains
```

## 14.1 Foundation Domains

Provide shared structural foundations.

Examples:

- Identity;
- Organization;
- User;
- Permission;
- Policy;
- Knowledge.

## 14.2 Professional Domains

Represent the professional subject matter of international trademark and global brand services.

Examples:

- Trademark;
- Brand;
- Jurisdiction;
- Classification;
- Evidence;
- Document.

## 14.3 Execution Domains

Coordinate business execution.

Examples:

- Matter;
- Order;
- Opportunity;
- Workflow Contract;
- Task;
- Event;
- Notification.

## 14.4 Collaboration Domains

Enable cooperation among clients, partners, agents and service providers.

Examples:

- Partner;
- Agent;
- Service Provider;
- Service Network;
- Routing;
- Communication.

---

# 15. Core Object Architecture

Book 02 defines the rules for Core Objects.

A Core Object is a persistent, referable, traceable, auditable and product-consumable representation of a stable business or system entity.

A Core Object shall:

- belong to one primary Core Domain;
- have stable semantic meaning;
- have lifecycle rules where applicable;
- produce or receive events where applicable;
- be governed by identity and permission rules;
- be consumable through Core Contracts.

Detailed object specifications shall live in:

```text
core-specs/objects/
```

---

# 16. Core Service Architecture

Book 02 defines the rules for Core Services.

A Core Service is a reusable capability exposed by the Core.

A Core Service shall define:

- responsibility;
- input;
- output;
- context;
- permission requirements;
- consumers;
- events;
- failure handling;
- acceptance criteria.

Examples:

- Search Service;
- Discovery Service;
- Recommendation Service;
- Matching Service;
- Routing Service;
- Validation Service;
- Knowledge Retrieval Service.

Detailed service specifications shall live in:

```text
core-specs/services/
```

---

# 17. Execution Primitives Architecture

Book 02 defines execution primitives and contracts.

It does not define workflow execution.

This boundary is mandatory.

```text
Core
    provides execution primitives and workflow contracts

Workplace
    operates workflows and composes work

Products
    deliver workflow experience
```

Core Execution Primitives include:

- Event Primitive;
- Task Primitive;
- State Primitive;
- Context Primitive;
- Notification Contract;
- Workflow Contract.

Detailed execution specifications shall live in:

```text
core-specs/events/
core-specs/workflows/
```

---

# 18. Core Contract Architecture

Book 02 defines the contract architecture of the Core.

Core Contracts include:

- Data Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Consumption Contract.

Contracts protect the Core from informal integration.

A product shall consume the Core through explicit contracts.

Detailed contract specifications shall live in:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

---

# 19. AI Capability Architecture

Book 02 defines AI as a governed form of Core Capability execution.

AI is not an autonomous authority.

AI shall be governed by:

- identity;
- permissions;
- authorized knowledge sources;
- context;
- event logging;
- auditability;
- human review;
- risk classification.

AI capability specifications shall define:

- capability responsibility;
- agent role;
- knowledge dependency;
- context requirements;
- output format;
- audit requirements;
- human review rules;
- prohibited actions.

Detailed AI specifications shall live in:

```text
core-specs/agents/
```

---

# 20. Core Consumption Architecture

Book 02 defines how products consume the Core.

Products may:

- read Core Objects;
- call Core Services;
- subscribe to Core Events;
- use AI Capabilities;
- implement product-specific experience;
- compose workflows under Workplace rules.

Products shall not:

- redefine Core Objects;
- change Core semantic meanings locally;
- bypass Core Contracts;
- create conflicting domain definitions;
- override identity, permission or event rules.

Detailed product-specific specifications belong to later publications or product documents.

Book 02 defines only consumption rules.

---

# 21. Book 02 Manuscript Architecture

The Book 02 manuscript is organized according to the frozen table of contents.

```text
00 Preface
01 Table of Contents

Part I — Core Foundation
Part II — Core Kernel Architecture
Part III — Core Specification System
Part IV — Core Execution Boundary

Appendices
```

The manuscript defines Core meaning, architecture, boundaries and specification frameworks.

It does not contain full executable detail.

---

# 22. Part I Architecture

Part I defines the foundation of the Core.

It answers:

- why Core exists;
- where Core sits;
- what Core owns;
- what Core excludes;
- how Book 01 becomes Book 02;
- how professional value flows through Core;
- how domains are classified.

Part I produces architectural decisions and boundary rules.

It is not required to produce database tables or API endpoints.

---

# 23. Part II Architecture

Part II defines the Core architecture.

It answers:

- what the Core Kernel contains;
- how layers are organized;
- how responsibilities flow;
- what canonical models exist;
- how domains, objects, services, primitives and contracts are architected.

Part II produces architecture models and specification boundaries.

---

# 24. Part III Architecture

Part III defines the Core Specification System.

It answers how MarkOrbit Core specification units shall be written.

It covers:

- Identity Specification;
- Capability Specification;
- Knowledge Specification;
- Business Responsibility Specification;
- Domain Specification;
- Object Specification;
- Service Specification;
- Event Specification;
- AI Capability and Agent Governance Specification;
- Core Consumption Specification.

Part III is not MAS.

MAS defines architecture representation generally.

Part III defines MarkOrbit Core specification units specifically.

---

# 25. Part IV Architecture

Part IV defines the execution boundary of the Core.

It answers:

- what belongs to Core MVP;
- which domains should be implemented first;
- how MVP domains map to execution assets;
- how Codex should read Book 02 and `core-specs/`.

Part IV is not a full project management plan.

It defines the execution boundary and implementation roadmap logic.

---

# 26. Repository Mapping

Book 02 shall be organized as follows.

```text
book-02-core/

├── README.md
├── publication.yaml
├── CHANGELOG.md
│
├── planning/
│   ├── B02-PLN-0001_Core_Positioning.md
│   ├── B02-PLN-0002_Architecture_Blueprint_v2.0.md
│   ├── B02-PLN-0003_Core_Domain_Map_v1.0.md
│   └── B02-PLN-0004_Core_Execution_Matrix_v1.0.md
│
├── editorial/
│   └── B02-EDT-0001_Editorial_Protocol_and_Chapter_Writing_Template.md
│
├── manuscript/
│   ├── 00_Preface.md
│   ├── 01_Table_of_Contents.md
│   ├── part-01-core-foundation/
│   ├── part-02-core-kernel-architecture/
│   ├── part-03-core-specification-system/
│   └── part-04-core-execution-boundary/
│
├── core-specs/
│   ├── domains/
│   ├── objects/
│   ├── services/
│   ├── contracts/
│   ├── events/
│   ├── agents/
│   ├── api/
│   └── workflows/
│
├── indexes/
│   ├── domain-index.md
│   ├── object-index.md
│   ├── service-index.md
│   ├── event-index.md
│   ├── api-index.md
│   ├── agent-index.md
│   └── codex-task-index.md
│
├── assets/
└── releases/
```

---

# 27. Manuscript vs core-specs Boundary

The boundary between manuscript and `core-specs/` is mandatory.

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
| Codex tasks | indexes/ or planning/ |

The manuscript shall not duplicate all executable details.

`core-specs/` shall not redefine Core meaning independently from the manuscript.

---

# 28. Product Consumption Map

The primary product consumers of the Core are:

| Consumer | Core Consumption |
|----------|------------------|
| Book 03 — Workplace Framework | Core Objects, Services, Execution Primitives, Workflow Contracts |
| Book 04 — MarkReg | Trademark, Matter, Document, Evidence, Agent, Workflow Contract, Task, Event |
| Book 05 — MarkOrbit Lite | Brand, Trademark, Knowledge, Classification, Opportunity, Order, AI Capability |
| Book 06 — MGSN | Partner, Agent, Service Provider, Routing, Communication, Trust, Service Network |
| Brand Asset Vault | Brand, Trademark, Evidence, Document, Knowledge |
| Opportunity Engine | Opportunity, Trademark, Brand, Knowledge, Routing, Notification |

This map is directional.

Consumers consume the Core.

Consumers shall not redefine the Core.

---

# 29. MVP Architecture

The MVP shall establish the executable skeleton of the Core.

The MVP shall not attempt to implement the entire ecosystem.

MVP priority shall follow the domain sequence defined in B02-PLN-0003 and B02-PLN-0004.

The default priority is:

```text
Phase 1 — Foundation Core
Phase 2 — Professional Core
Phase 3 — Execution Core
Phase 4 — Growth Core
Phase 5 — Network Core
```

Part IV of Book 02 shall define how this priority becomes executable.

---

# 30. Codex Architecture

Codex shall use Book 02 as a specification source.

Codex shall not infer product requirements beyond the Core specification.

Codex implementation tasks shall be generated from:

```text
Book 02 manuscript
        ↓
core-specs/
        ↓
indexes/
        ↓
planning/
        ↓
implementation tasks
```

Codex tasks shall preserve:

- Core boundaries;
- domain ownership;
- object semantics;
- service contracts;
- event contracts;
- AI governance rules;
- MVP priority.

---

# 31. Architectural Invariants

The following invariants are permanently true for Book 02.

## Invariant 1

Book 02 defines the MarkOrbit Core.

## Invariant 2

Book 02 does not define product-specific features.

## Invariant 3

Core provides execution primitives and contracts.

## Invariant 4

Workplace operates work.

## Invariant 5

Products consume Core.

## Invariant 6

AI executes governed capabilities.

AI does not define professional truth.

## Invariant 7

Detailed executable specifications belong in `core-specs/`.

## Invariant 8

Book 02 shall conform to MAC, MAG and MAS.

---

# 32. Success Criteria

This architecture blueprint is successful only if:

- every Book 02 chapter maps to the frozen table of contents;
- every chapter has one primary Core responsibility;
- Core, Workplace and Product boundaries remain clear;
- Part III does not duplicate MAS;
- AI capability remains governed;
- detailed executable specifications are moved to `core-specs/`;
- MVP execution is supported without turning Book 02 into a PRD;
- Codex can use the resulting structure to generate implementation tasks.

---

# 33. Exclusions

This blueprint does not define:

- product UI;
- product pricing;
- marketing copy;
- prompt libraries;
- full API tutorials;
- deployment architecture;
- vendor-specific technology choices;
- product onboarding flows;
- product-specific operational SOPs.

These belong to product documents, implementation documents or operations documents.

---

# 34. Revision Policy

Changes to this blueprint shall be reviewed before they affect Book 02 manuscript structure.

Any change that redefines the relationship between Core, Workplace and Product requires editorial approval.

Any change that expands Book 02 into product-specific PRD content shall be rejected unless Book 02 scope is formally revised.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Draft | Initial Architecture Blueprint created before TOC freeze. |
| 2.0.0 | Canonical Draft | Rewritten to align with Book 02 TOC v1.2, Core Positioning, Editorial Protocol and manuscript/core-specs boundary. |

---

**End of Document**
