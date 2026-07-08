# Book 02

# B02-PLN-0001 — Core Positioning

**Document ID:** B02-PLN-0001

**Title:** Core Positioning

**Version:** 1.0.0

**Status:** Canonical Draft

**Category:** Planning

**Owner:** MarkOrbit Publications Editorial Board

**Applies To:** Book 02 — *MarkOrbit Core Specification*

**Related Documents:**

- Book 01 — *The Operating System for Global Brand Services*
- Book 02 TOC v1.2 — Frozen
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template
- MAC — MarkOrbit Architecture Canon
- MAG — MarkOrbit Architecture Governance
- MAS — MarkOrbit Architecture Specifications

---

# 1. Purpose

This document defines the positioning of the MarkOrbit Core within the MarkOrbit ecosystem.

It establishes what the Core is, why it exists, what it owns, what it does not own, and how later publications, products and implementations shall relate to it.

This document is a planning document for Book 02.

It is not part of the main manuscript.

It guides the writing of Book 02 and protects the Core Specification from becoming:

- a product requirements document;
- a user interface design document;
- an API tutorial;
- an AI prompt manual;
- a deployment guide;
- a marketing publication.

Book 02 shall define the MarkOrbit Core.

Products shall consume the MarkOrbit Core.

Implementations shall realize the MarkOrbit Core.

---

# 2. Positioning Statement

The MarkOrbit Core is the permanent shared operating core of the MarkOrbit ecosystem.

It provides the stable models, domains, objects, services, execution primitives and contracts that allow future products to share one professional foundation.

The Core is not a product.

The Core is not a workplace.

The Core is not a user interface.

The Core is not an AI assistant.

The Core is the shared specification layer from which products, workplaces, agents, services and networks are implemented.

---

# 3. Primary Question

Book 02 answers one primary question:

> What is the MarkOrbit Core that every future product shall consume?

This question shall guide every chapter of Book 02.

If a chapter does not help answer this question, it does not belong in Book 02.

---

# 4. Why Core Exists

MarkOrbit is not intended to become a collection of disconnected tools.

Without a shared Core:

- MarkReg may define trademarks one way;
- MarkOrbit Lite may define brands another way;
- MGSN may define agents and service providers independently;
- AI agents may use inconsistent knowledge;
- opportunities may be generated from fragmented data;
- customers, partners and service providers may be duplicated;
- workflows may become product-specific and hard to reuse;
- events may not be shared across products;
- future development may require repeated reconstruction.

The Core exists to prevent this fragmentation.

It allows all products to share:

- identity;
- knowledge;
- professional objects;
- domain services;
- business rules;
- events;
- execution primitives;
- AI capability governance;
- consumption contracts.

The Core turns the MarkOrbit ecosystem from a set of products into a shared professional operating foundation.

---

# 5. Relationship to Book 01

Book 01 defines the operating philosophy.

Book 02 defines the operating core.

Book 01 explains why global brand services require a Professional Operating System.

Book 02 specifies the Core that makes such an operating system executable.

The relationship is:

```text
Book 01
The Operating System for Global Brand Services
        ↓
Book 02
MarkOrbit Core Specification
```

Book 02 shall not repeat Book 01.

Book 02 shall translate Book 01 into Core models, domains, objects, services, execution primitives and contracts.

---

# 6. Relationship to Publication Series

The MarkOrbit Publication Series is organized as follows:

```text
Book 01 — The Operating System for Global Brand Services
        ↓
Book 02 — MarkOrbit Core Specification
        ↓
Book 03 — Workplace Framework
        ↓
Book 04 — MarkReg
Book 05 — MarkOrbit Lite
Book 06 — Mark Global Service Network
```

Book 02 occupies the central architectural position.

It defines the Core that later publications consume.

Later publications may extend, specialize or operationalize the Core.

They shall not redefine it.

---

# 7. Relationship to Architecture Library

The Architecture Library defines general architectural standards.

Book 02 applies these standards to the MarkOrbit Core.

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
- MAS defines how architectural specifications are represented.
- Book 02 defines the MarkOrbit Core using these standards.

Book 02 shall not duplicate MAC, MAG or MAS.

Book 02 shall conform to them.

---

# 8. Relationship to Software Implementation

Software implementation realizes the Core.

Implementation includes:

- database schemas;
- domain models;
- services;
- APIs;
- events;
- AI agents;
- workflows;
- product modules;
- tests;
- deployment.

Book 02 does not contain full implementation code.

Book 02 defines the specification that implementation shall follow.

The execution chain is:

```text
Book 02 Manuscript
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Software Implementation
```

---

# 9. Core Identity

The Core has one identity:

> The shared professional operating core for global brand services.

This identity contains four meanings.

## 9.1 Shared

The Core is not built for one product.

It is shared by all MarkOrbit products and future extensions.

## 9.2 Professional

The Core is designed for professional service work, especially international trademark and global brand services.

It is not a generic CRM, generic workflow system or generic AI platform.

## 9.3 Operating

The Core is intended to support real work.

It is not merely a knowledge base or documentation system.

It provides objects, services, events and contracts that can be executed.

## 9.4 Core

The Core must remain stable while products evolve.

It should change only through governed architectural evolution.

---

# 10. Core Ownership

Book 02 owns the following Core responsibilities.

## 10.1 Core Models

Book 02 owns the canonical models that define the ecosystem.

Examples:

- Identity Model;
- Capability Model;
- Knowledge Model;
- Business Model;
- Workplace Model;
- Network Model.

## 10.2 Core Domains

Book 02 owns the domain architecture of the Core.

Examples:

- Foundation Domains;
- Professional Domains;
- Execution Domains;
- Collaboration Domains.

Detailed domain specifications belong in `core-specs/domains/`.

## 10.3 Core Objects

Book 02 defines the rules for Core Objects.

Core Objects are persistent, referable, auditable and product-consumable representations of stable business or system entities.

Examples:

- Trademark;
- Brand;
- Organization;
- Matter;
- Order;
- Opportunity;
- Document;
- Event;
- Task;
- Agent.

Detailed object specifications belong in `core-specs/objects/`.

## 10.4 Core Services

Book 02 defines the rules for Core Services.

Core Services are reusable capabilities exposed by the Core.

Examples:

- Search;
- Discovery;
- Recommendation;
- Matching;
- Routing;
- Validation;
- Knowledge Retrieval.

Detailed service specifications belong in `core-specs/services/`.

## 10.5 Execution Primitives

Book 02 defines execution primitives and contracts.

Examples:

- Event Primitive;
- Task Primitive;
- State Primitive;
- Context Primitive;
- Workflow Contract;
- Notification Contract.

Book 02 does not own workflow execution.

Workplace owns operational execution.

## 10.6 Core Contracts

Book 02 owns the contract architecture.

Examples:

- Data Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Consumption Contract.

Detailed contract specifications belong in `core-specs/contracts/`, `core-specs/api/`, `core-specs/events/`, `core-specs/agents/` and `core-specs/workflows/`.

---

# 11. What Core Does Not Own

The Core shall not own the following.

## 11.1 Product Features

Product features belong to product publications or product PRDs.

Examples:

- MarkReg dashboard layout;
- Lite onboarding flow;
- MGSN member portal feature;
- product-specific search pages;
- commercial landing pages.

## 11.2 User Interface Design

User interface belongs to Workplace or product design.

Book 02 may define objects and services that UI consumes.

Book 02 shall not define screens, buttons, layout, visual style or interaction details.

## 11.3 Product Workflows

Book 02 may define Workflow Contracts.

Book 03 and product publications define workflow operation and composition.

## 11.4 Pricing and Commercial Packages

Book 02 may define business responsibility.

It shall not define product pricing, membership plans, commission rates or sales packages.

## 11.5 Prompt Libraries

Book 02 may define AI capability governance.

It shall not define production prompt libraries.

## 11.6 Deployment and Operations

Book 02 shall not define deployment scripts, infrastructure vendors, runtime environments or operational runbooks.

---

# 12. Core vs Workplace

The boundary between Core and Workplace is mandatory.

```text
Core
    provides models, objects, services, primitives and contracts

Workplace
    operates work through composition, workflow and experience
```

Book 02 may define:

- Task Primitive;
- Event Primitive;
- State Primitive;
- Context Primitive;
- Workflow Contract;
- Notification Contract.

Book 02 shall not define:

- workplace screens;
- daily operation interfaces;
- product-specific workflow composition;
- user experience details;
- workplace interaction models.

Workplace architecture belongs to Book 03.

---

# 13. Core vs Product

The boundary between Core and Product is mandatory.

```text
Core
    defines reusable professional foundation

Product
    delivers user-facing functionality
```

Products may:

- read Core Objects;
- call Core Services;
- subscribe to Core Events;
- use AI Capabilities;
- extend user experience;
- compose workflows through Workplace rules.

Products shall not:

- redefine Core Objects;
- change Core meanings locally;
- bypass Core Contracts;
- create conflicting domain semantics;
- replace Core permission, identity or event rules.

---

# 14. Core vs AI

AI is not the Core.

AI is one execution form of Core Capability.

The Core governs AI through:

- identity;
- permissions;
- knowledge sources;
- context;
- event logging;
- auditability;
- human review;
- risk classification.

AI shall enhance professional work.

AI shall not define professional truth.

High-risk professional actions shall require human review.

---

# 15. Core vs Knowledge Base

The Core is not merely a knowledge base.

Knowledge is one part of the Core.

A knowledge base stores information.

The Core defines how knowledge becomes professional capability.

The Core connects knowledge with:

- identity;
- domains;
- objects;
- services;
- events;
- AI agents;
- workflow contracts;
- product consumption.

---

# 16. Core vs Data Platform

The Core is not merely a data platform.

Data is one input to Core capability.

The Core defines the meaning, ownership, relationships and execution use of data.

A data platform may store and process data.

The Core specifies which data becomes Core Object, Core Event, Core Knowledge or Core Service input.

---

# 17. Core vs Workflow Engine

The Core is not a workflow engine.

The Core defines execution primitives and workflow contracts.

Workplace and products operate workflow execution.

This distinction prevents Book 02 from absorbing Book 03.

The correct relationship is:

```text
Core
    defines workflow contracts and execution primitives

Workplace
    composes and operates workflows

Products
    deliver workflow experience
```

---

# 18. Core vs CRM

The Core is not a CRM.

CRM is a product pattern.

The Core may define customers, organizations, opportunities, communication records and relationships.

But it does not become a sales management product.

MarkOrbit products may build CRM-like experiences by consuming Core.

The Core remains the shared professional operating foundation.

---

# 19. Positioning Principles

The following principles govern Core positioning.

## Principle 1 — Core Before Product

The Core shall define shared meaning before products define features.

## Principle 2 — Domain Before Module

The Core shall be organized around stable domains rather than product modules.

## Principle 3 — Capability Before Feature

The Core shall own reusable capabilities.

Products shall own product-specific features.

## Principle 4 — Contract Before Integration

Products shall integrate with Core through explicit contracts.

## Principle 5 — Governance Before Automation

Automation shall be governed by identity, permission, knowledge, event and human review rules.

## Principle 6 — Reuse Before Duplication

Shared objects, services and events shall be reused across products.

## Principle 7 — Evolution Without Replacement

The Core shall evolve through governed extension, not replacement.

---

# 20. Core Consumers

The primary consumers of the Core include the following.

## 20.1 Book 03 — Workplace Framework

Consumes:

- Core Objects;
- Core Services;
- Execution Primitives;
- Workflow Contracts;
- Consumption Rules.

## 20.2 Book 04 — MarkReg

Consumes:

- Trademark;
- Matter;
- Document;
- Evidence;
- Agent;
- Workflow Contract;
- Task;
- Event.

## 20.3 Book 05 — MarkOrbit Lite

Consumes:

- Brand;
- Trademark;
- Knowledge;
- Classification;
- Opportunity;
- Order;
- AI Capability.

## 20.4 Book 06 — Mark Global Service Network

Consumes:

- Partner;
- Agent;
- Service Provider;
- Routing;
- Communication;
- Trust;
- Service Network.

## 20.5 Future Products

Future products shall consume Core through the same contract model.

They shall not create isolated object definitions.

---

# 21. Core Positioning Map

The Core occupies the central position between operating philosophy and product implementation.

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

The Core is the shared specification layer.

It is not optional infrastructure.

It is the foundation that prevents the ecosystem from fragmenting.

---

# 22. Positioning Decisions

The following decisions are adopted.

| Decision ID | Decision |
|------------|----------|
| B02-POS-001 | Book 02 shall remain titled *MarkOrbit Core Specification*. |
| B02-POS-002 | Core Kernel may be used as an explanatory concept, but not as the official book title. |
| B02-POS-003 | Book 02 shall define Core, not product features. |
| B02-POS-004 | Detailed executable specifications shall live in `core-specs/`. |
| B02-POS-005 | Core shall provide execution primitives, not own workflow execution. |
| B02-POS-006 | Products shall consume Core through contracts. |
| B02-POS-007 | AI shall be governed as a Core Capability execution form, not treated as an autonomous authority. |

---

# 23. Acceptance Criteria

This positioning is accepted only if future Book 02 chapters satisfy the following criteria.

- The chapter defines or supports Core.
- The chapter does not become a product PRD.
- The chapter distinguishes Core from Workplace and Product.
- The chapter identifies whether details belong in manuscript or `core-specs/`.
- The chapter does not duplicate Book 01.
- The chapter does not duplicate MAC, MAG or MAS.
- The chapter supports future software implementation.
- The chapter avoids unsupported AI autonomy.
- The chapter preserves the publication series dependency structure.

---

# 24. Editorial Implications

The positioning defined in this document has the following editorial implications.

## 24.1 Manuscript Chapters

Manuscript chapters shall define Core meaning, architecture, boundaries and specification frameworks.

They shall not contain full executable detail.

## 24.2 core-specs

`core-specs/` shall contain detailed domain, object, service, event, API, agent and workflow specifications.

## 24.3 Planning Documents

Planning documents shall define blueprint, domain maps, execution matrices and implementation roadmaps.

## 24.4 Product Documents

Product documents shall define product-specific behavior, workflows, UI and user experience.

---

# 25. Revision Policy

Changes to this positioning document shall be reviewed before they affect the Book 02 manuscript.

Any change that redefines the relationship between Core, Workplace and Product requires editorial approval.

Any change that allows Book 02 to define product-specific features requires rejection unless the Book 02 scope is formally revised.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical Draft | Initial Core Positioning document for Book 02. |

---

**End of Document**
