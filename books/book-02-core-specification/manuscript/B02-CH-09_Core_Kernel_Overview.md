# Book 02

# 09 — Core Kernel Overview

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-09

**Chapter Title:** Core Kernel Overview

**Part:** Part II — Core Kernel Architecture

**Chapter Type:** Architecture

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

**Related Planning Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template

---

# 1. Chapter Purpose

This chapter provides the architectural overview of the MarkOrbit Core Kernel.

Part I established the foundation of the Core:

- why the Core exists;
- where the Core sits;
- what the Core owns and excludes;
- which principles govern Core design;
- how the Professional OS becomes the Core Kernel;
- how professional value flows through the Core;
- how ontology and domains are classified.

Part II begins by defining the structure of the Core Kernel itself.

This chapter does not define every domain, object, service, event or contract in detail.

It defines how those components fit together.

The purpose of this chapter is to give Book 02 a clear architectural center.

Without a Core Kernel overview, later chapters may become separate discussions of layers, models, domains, objects, services, events and contracts.

With this chapter, those pieces can be understood as one coherent Core architecture.

---

# 2. Core Question

This chapter answers one question:

> What is the overall structure of the MarkOrbit Core Kernel?

The answer is:

> The Core Kernel is the stable internal architecture of the MarkOrbit Core, composed of canonical models, Core Domains, Core Objects, Core Services, execution primitives, Core Contracts and consumption rules.

The Core Kernel is not a product.

It is not a runtime engine.

It is not a workflow engine.

It is not an AI agent.

It is the architectural center of shared professional meaning and reusable capability.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- the meaning of Core Kernel;
- the Core Kernel component structure;
- the relationship among models, domains, objects, services, primitives, contracts and consumption;
- the high-level Core architecture;
- how the Core Kernel supports products;
- how the Core Kernel relates to `core-specs/`;
- how the Core Kernel becomes executable;
- architecture rules for later Part II chapters.

## 3.2 Out of Scope

This chapter does not define:

- detailed domain specifications;
- detailed object fields;
- service input/output contracts;
- event payloads;
- API endpoint details;
- AI prompt templates;
- product UI;
- workflow execution;
- deployment architecture;
- vendor-specific implementation.

Those belong to later chapters, `core-specs/`, product publications or implementation documents.

---

# 4. Core Kernel Definition

In Book 02, Core Kernel means:

> the stable inner architecture of the MarkOrbit Core that defines shared professional meaning, reusable capabilities, execution primitives and consumption contracts for all MarkOrbit products and implementations.

This definition contains six meanings.

## 4.1 Stable

The Core Kernel should change slowly.

Products may evolve quickly.

The Core Kernel must preserve continuity.

## 4.2 Inner Architecture

The Core Kernel is not the full product ecosystem.

It is the inner structure that products consume.

## 4.3 Shared Professional Meaning

The Core Kernel defines meanings that must remain consistent across products.

Examples include Trademark, Brand, Matter, Order, Opportunity, Agent, Service Provider, Task and Event.

## 4.4 Reusable Capability

The Core Kernel exposes capabilities that can be reused across products.

Examples include search, classification recommendation, document generation, evidence packaging, opportunity discovery, routing and knowledge retrieval.

## 4.5 Execution Primitives

The Core Kernel provides primitives such as events, tasks, states, contexts and workflow contracts.

It does not own workflow execution.

## 4.6 Consumption Contracts

The Core Kernel defines how products, Workplaces, AI agents and services consume Core capabilities without redefining Core meaning.

---

# 5. Core Kernel Is an Explanatory Concept

“Core Kernel” is used in Book 02 as an explanatory concept.

It helps describe the inner structure of the Core.

It is not the official book title.

The official title remains:

```text
Book 02 — MarkOrbit Core Specification
```

The Core Kernel is not a technical operating system kernel.

It is not a single software service.

It is not a database.

It is not a framework.

It is the architectural center of the MarkOrbit Core.

This distinction matters.

Book 02 defines the MarkOrbit Core.

The Core Kernel helps explain how the Core is internally organized.

---

# 6. High-Level Core Kernel Structure

The Core Kernel is organized as follows:

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

This structure is directional.

Each layer depends on the layers above it for meaning.

Each layer enables the layers below it to become executable and consumable.

The structure is not a product module list.

It is an architectural chain.

---

# 7. Component 1 — Canonical Models

Canonical Models define the fundamental conceptual models of the Core.

They answer:

> What stable models does the MarkOrbit ecosystem require?

The initial Canonical Models are:

- Identity Model;
- Capability Model;
- Knowledge Model;
- Business Responsibility Model;
- Workplace Model;
- Network Model.

Canonical Models are more abstract than domains.

They define the conceptual logic that domains implement.

For example:

- Identity Model informs Identity, Organization, User, Partner, Agent and Service Provider.
- Knowledge Model informs Knowledge, Jurisdiction, Classification, Document, Evidence and AI Capability.
- Business Responsibility Model informs Customer, Order, Matter, Opportunity and Policy.
- Network Model informs Partner, Agent, Service Provider, Service Network, Routing and Communication.

Canonical Models prevent domains from being designed in isolation.

---

# 8. Component 2 — Core Domains

Core Domains define stable responsibility boundaries.

They answer:

> Which executable business boundaries does the Core own?

Book 02 recognizes four categories of Core Domains:

- Foundation Domains;
- Professional Domains;
- Business Execution Domains;
- Collaboration Network Domains.

A Core Domain is not a page, module or table.

It is a boundary of responsibility.

For example:

- Trademark Domain owns trademark lifecycle meaning.
- Matter Domain owns professional service matter execution meaning.
- Agent Domain owns professional agent representation and capability meaning.
- Routing Domain owns routing decision meaning.

Detailed domain specifications belong in:

```text
core-specs/domains/
```

---

# 9. Component 3 — Core Objects

Core Objects represent persistent and reusable entities inside domains.

They answer:

> What stable things must the Core represent, reference, audit and expose?

Examples include:

- Identity;
- Organization;
- User;
- Brand;
- Trademark;
- Jurisdiction;
- Document;
- Evidence;
- Customer;
- Matter;
- Order;
- Opportunity;
- Workflow Contract;
- Task;
- Event;
- Partner;
- Agent;
- Service Provider;
- Route;
- Conversation.

Core Objects are not only database rows.

A Core Object has meaning, ownership, lifecycle, relationships and consumption rules.

Detailed object specifications belong in:

```text
core-specs/objects/
```

---

# 10. Component 4 — Core Services

Core Services expose reusable capabilities.

They answer:

> What can the Core do for products, Workplaces, AI agents and services?

Examples include:

- Identity Resolution;
- Organization Search;
- Permission Evaluation;
- Knowledge Retrieval;
- Brand Portfolio Mapping;
- Trademark Search;
- Jurisdiction Lookup;
- Deadline Calculation;
- Classification Recommendation;
- Document Generation;
- Evidence Packaging;
- Matter Creation;
- Order-to-Matter Conversion;
- Opportunity Discovery;
- Agent Matching;
- Routing Decision;
- Notification Dispatch;
- Communication Search.

A Core Service is not a product button.

A product may call a Core Service.

A Workplace may compose Core Services.

An AI agent may use a Core Service under governance.

Detailed service specifications belong in:

```text
core-specs/services/
```

---

# 11. Component 5 — Execution Primitives

Execution Primitives make work traceable and interoperable.

They answer:

> What basic execution structures does the Core provide?

The initial execution primitives include:

- Event Primitive;
- Task Primitive;
- State Primitive;
- Context Primitive;
- Notification Contract;
- Workflow Contract.

The Core provides execution primitives.

The Core does not own workflow execution.

The boundary is:

```text
Core
    provides execution primitives and contracts

Workplace
    operates workflows and professional work

Products
    deliver user-facing workflow experience
```

Detailed execution specifications belong in:

```text
core-specs/events/
core-specs/workflows/
```

---

# 12. Component 6 — Core Contracts

Core Contracts govern consumption and integration.

They answer:

> How may products, Workplaces, AI agents and implementations consume the Core?

Core Contracts include:

- Data Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Consumption Contract.

Contracts protect the Core from informal integration.

Without contracts, products may consume Core inconsistently.

With contracts, products can evolve while preserving shared meaning.

Detailed contract specifications belong in:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
core-specs/workflows/
```

---

# 13. Component 7 — Core Consumption

Core Consumption defines how downstream systems use the Core.

It answers:

> How do Book 03, Book 04, Book 05, Book 06 and future products consume the Core without redefining it?

Core consumers include:

- Book 03 — Workplace Framework;
- Book 04 — MarkReg;
- Book 05 — MarkOrbit Lite;
- Book 06 — Mark Global Service Network;
- Brand Asset Vault;
- Opportunity Engine;
- future products;
- AI agents;
- Codex-generated implementation tasks.

Consumers may:

- read Core Objects;
- call Core Services;
- subscribe to Core Events;
- use AI Capabilities;
- implement product experience;
- compose workflows under Workplace rules.

Consumers shall not:

- redefine Core Objects;
- bypass Core Contracts;
- create conflicting domain meanings;
- modify Core semantics locally;
- treat AI output as unguided professional truth.

---

# 14. Core Kernel Component Relationship

The components of the Core Kernel are connected.

```text
Canonical Models
    provide conceptual structure for
Core Domains

Core Domains
    own responsibility for
Core Objects and Core Services

Core Objects
    preserve stable meaning and state for
Core Services and Core Events

Core Services
    perform reusable capabilities using
Core Objects, Knowledge and Policies

Execution Primitives
    make action, state and coordination traceable through
Tasks, Events, Contexts and Workflow Contracts

Core Contracts
    govern how all components are consumed by
Products, Workplaces, AI Agents and Implementation

Core Consumption
    allows products to specialize experience without redefining Core
```

The Core Kernel is therefore not a pile of components.

It is a dependency structure.

---

# 15. Core Kernel and Professional Value Flow

The Core Kernel supports the Professional Value Flow.

```text
Reality
        ↓
Core Objects

Facts
        ↓
Data, Records and Events

Understanding
        ↓
Knowledge Model and Knowledge Services

Judgment
        ↓
Rules, Policies, AI Capability and Human Review

Action
        ↓
Core Services and Execution Primitives

Coordination
        ↓
Tasks, Events, Routing, Communication and Workflow Contracts

Experience
        ↓
Workplace and Product Consumption
```

This mapping ensures that the Core Kernel does not become only a technical structure.

It remains connected to professional value creation.

Each Core Kernel component should help move professional value forward.

---

# 16. Core Kernel and Ontology

The Core Kernel depends on the ontology defined in Chapter 08.

Ontology clarifies what kind of concept is being handled.

The Core Kernel then defines how that concept is represented and consumed.

For example:

- Reality Ontology concepts may become Core Objects.
- System Ontology concepts may become Canonical Models, Permissions, Policies, Services or Contracts.
- Execution Ontology concepts may become Tasks, Events, States and Workflow Contracts.
- Collaboration Ontology concepts may become Partner, Agent, Service Provider, Routing and Communication domains.

Ontology prevents concept confusion.

Core Kernel architecture turns ontology into a reusable system structure.

---

# 17. Core Kernel and Domain Map

The Core Domain Map is the primary expression of the Core Kernel at the domain level.

The initial Domain Map includes 26 Core Domains.

```text
Foundation Domains
    ├── Identity
    ├── Organization
    ├── User
    ├── Permission
    ├── Policy
    └── Knowledge

Professional Domains
    ├── Brand
    ├── Trademark
    ├── Jurisdiction
    ├── Classification
    ├── Document
    └── Evidence

Business Execution Domains
    ├── Customer
    ├── Matter
    ├── Order
    ├── Opportunity
    ├── Workflow Contract
    ├── Task
    ├── Event
    └── Notification

Collaboration Network Domains
    ├── Partner
    ├── Agent
    ├── Service Provider
    ├── Service Network
    ├── Routing
    └── Communication
```

The Domain Map is not a product roadmap.

It is the domain-level structure of the Core Kernel.

---

# 18. Core Kernel and Execution Matrix

The Core Execution Matrix maps Core Domains to executable assets.

For each domain, the matrix identifies:

- database tables;
- domain models;
- domain services;
- API surface;
- events;
- AI capability usage;
- workflow or execution usage;
- product consumers;
- Codex tasks;
- acceptance criteria.

The relationship is:

```text
Core Kernel
        ↓
Core Domain Map
        ↓
Core Execution Matrix
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Implementation
```

This chain prevents implementation from becoming disconnected from architecture.

---

# 19. Core Kernel and `core-specs/`

The Core Kernel is defined in the manuscript.

Its details are specified in `core-specs/`.

The boundary is:

| Content | Location |
|---------|----------|
| Core Kernel meaning | manuscript/ |
| Core architecture | manuscript/ |
| Domain Map | planning/ and manuscript summary |
| Detailed Domain specs | core-specs/domains/ |
| Detailed Object specs | core-specs/objects/ |
| Detailed Service specs | core-specs/services/ |
| Detailed Event specs | core-specs/events/ |
| Detailed Agent specs | core-specs/agents/ |
| API surface | core-specs/api/ |
| Workflow contracts | core-specs/workflows/ |

The manuscript shall not duplicate every detail.

`core-specs/` shall not redefine the Core Kernel independently.

---

# 20. Core Kernel and Products

Products consume the Core Kernel.

They do not own it.

The relationship is:

```text
Core Kernel
        ↓
Core Consumption
        ↓
Products
```

Product examples:

## 20.1 MarkReg

Consumes Core for trademark filing, matter management, document handling and agent coordination.

## 20.2 MarkOrbit Lite

Consumes Core for guided consultation, brand asset handling, opportunity discovery and AI-assisted service delivery.

## 20.3 MGSN

Consumes Core for partner, agent, service provider, routing, trust and communication.

## 20.4 Brand Asset Vault

Consumes Core for brand, trademark, evidence, document and knowledge continuity.

## 20.5 Opportunity Engine

Consumes Core for opportunity discovery, scoring, routing, notification and follow-up.

Products may add experience.

They shall not redefine the Core Kernel.

---

# 21. Core Kernel and AI

AI is not the Core Kernel.

AI is a governed execution form of Core Capability.

Within the Core Kernel, AI connects to:

- Knowledge Model;
- Capability Model;
- Permission;
- Policy;
- Context;
- Event;
- Audit;
- Human Review;
- Agent Contract;
- Consumption Contract.

AI may assist:

- extraction;
- classification;
- recommendation;
- drafting;
- summarization;
- monitoring;
- routing;
- opportunity discovery.

AI shall not:

- define Core ontology;
- redefine domain meaning;
- bypass permission;
- bypass knowledge validation;
- silently modify critical Core data;
- issue high-risk professional conclusions without review.

AI capability belongs inside Core governance.

AI autonomy does not.

---

# 22. Core Kernel and Workplace

Workplace is a consumer and operator of Core execution structures.

Core provides:

- Objects;
- Services;
- Tasks;
- Events;
- Contexts;
- Workflow Contracts;
- Notifications;
- Consumption Rules.

Workplace operates:

- work composition;
- task surfaces;
- workflow execution;
- collaboration environment;
- human and AI co-working experience;
- operational context.

The Core Kernel must not absorb Workplace architecture.

Book 03 owns the Workplace Framework.

Book 02 defines what Workplace may consume.

---

# 23. Core Kernel and Network

The Core Kernel provides the foundation for network collaboration.

It defines:

- Partner;
- Agent;
- Service Provider;
- Service Network;
- Routing;
- Communication;
- related objects, services, events and contracts.

Book 06 defines the Mark Global Service Network in detail.

The Core Kernel provides shared collaboration meaning.

MGSN operationalizes that meaning in a network product and business system.

This preserves the boundary:

```text
Book 02
    Core collaboration foundation

Book 06
    Global service network operation
```

---

# 24. Core Kernel and MVP

The Core Kernel is broad, but MVP implementation must be staged.

The MVP should not attempt to implement the entire ecosystem.

It should establish a minimal executable skeleton.

The default phase sequence is:

```text
Phase 1 — Foundation Core
Phase 2 — Professional Core
Phase 3 — Business Execution Core
Phase 4 — Growth Core
Phase 5 — Network Core
```

The Core Kernel overview supports this staged execution.

The MVP must preserve the structure of the Core Kernel even if not every domain is implemented immediately.

A partial Core should still follow the full architecture.

---

# 25. Core Kernel Integrity

Core Kernel Integrity means that the seven components remain connected.

A violation occurs when one component is implemented without the others.

Examples of broken integrity:

- a table exists without Core Object meaning;
- a service exists without domain ownership;
- an AI agent operates without knowledge or permission governance;
- a product page consumes data without Core Contract;
- an event is emitted without domain semantics;
- a workflow operates without Workflow Contract;
- a product redefines a Core Object locally.

Core Kernel Integrity requires every implementation asset to trace back to:

```text
Model → Domain → Object / Service → Event / Contract → Consumer
```

---

# 26. Core Kernel Traceability

Every Core asset should be traceable.

Traceability means that a concept can be followed from architecture to implementation.

For example:

```text
Professional Value Flow
        ↓
Ontology
        ↓
Canonical Model
        ↓
Core Domain
        ↓
Core Object
        ↓
Core Service
        ↓
Core Event
        ↓
Core Contract
        ↓
Product Consumption
        ↓
Codex Task
        ↓
Implementation
```

This traceability is important for review, testing, Codex development and future governance.

Without traceability, the Core becomes documentation.

With traceability, the Core becomes executable architecture.

---

# 27. Core Kernel Review Questions

When reviewing a proposed Core concept, reviewers should ask:

1. Which Canonical Model does it relate to?
2. Which Core Domain owns it?
3. Is it a Core Object, Core Service, Event, Contract, AI Capability or product feature?
4. Which Professional Value Flow stage does it support?
5. Which ontology layer does it belong to?
6. Which products consume it?
7. Which `core-specs/` file should define it in detail?
8. What execution assets will it require?
9. What permission, policy or governance rules apply?
10. Does it preserve the Core / Workplace / Product boundary?
11. Does it preserve Core Kernel Integrity?
12. Can Codex implement it from approved specifications?

These questions shall guide later Part II and Part III chapters.

---

# 28. Core Kernel Anti-Patterns

## 28.1 Product-First Kernel

A product page or feature becomes the source of Core meaning.

Result:

- Core becomes unstable;
- other products cannot reuse it cleanly.

## 28.2 Data-First Kernel

Database tables are created before domain and object meaning.

Result:

- implementation defines architecture;
- semantic consistency is weak.

## 28.3 AI-First Kernel

AI agents define knowledge, domains or actions through prompts.

Result:

- AI becomes uncontrolled source of meaning;
- professional accountability is weak.

## 28.4 Workflow-First Kernel

Operational workflows define Core architecture.

Result:

- Book 02 absorbs Book 03;
- product workflows become difficult to reuse.

## 28.5 Integration-First Kernel

APIs are created before contracts and domain meanings.

Result:

- products integrate informally;
- long-term compatibility suffers.

## 28.6 Index-Only Kernel

The Core becomes only a list of domains, objects and services.

Result:

- no architectural relationship;
- implementation lacks guidance.

The Core Kernel must remain relational, governed and traceable.

---

# 29. Core Kernel Rules

The following rules are established by this chapter.

## Rule 1 — Core Kernel SHALL remain the architectural center of Book 02

All Part II architecture chapters shall align with the Core Kernel structure.

## Rule 2 — Core Kernel SHALL contain seven components

Canonical Models, Core Domains, Core Objects, Core Services, Execution Primitives, Core Contracts and Core Consumption form the Core Kernel.

## Rule 3 — Products SHALL consume the Core Kernel

Products shall not redefine Core Kernel meanings.

## Rule 4 — `core-specs/` SHALL detail the Core Kernel

The manuscript defines architecture.

`core-specs/` defines executable details.

## Rule 5 — AI SHALL operate under Core Kernel governance

AI shall use authorized knowledge, permissions, context, events and human review rules.

## Rule 6 — Workplace SHALL operate execution

Core provides primitives and contracts.

Workplace operates workflows.

## Rule 7 — Core Kernel Integrity SHALL be preserved

Implementation assets shall trace back to Core architecture.

## Rule 8 — Core Kernel SHALL support MVP execution without becoming a PRD

Part IV shall map the Core Kernel to MVP execution assets, not product feature plans.

---

# 30. Specification Output

This chapter produces the following specification output:

- Core Kernel definition;
- Core Kernel component structure;
- seven-component architecture;
- relationship among models, domains, objects, services, primitives, contracts and consumption;
- Core Kernel relationship to Professional Value Flow;
- Core Kernel relationship to ontology and domain classification;
- Core Kernel relationship to `core-specs/`;
- Core Kernel relationship to products, AI, Workplace and network;
- Core Kernel integrity rule;
- Core Kernel traceability rule;
- Core Kernel review questions;
- Core Kernel anti-patterns;
- Core Kernel rules.

These outputs guide Chapters 10 through 17.

---

# 31. Execution Mapping

This chapter does not directly define database tables or API endpoints.

It defines the architectural chain that execution assets must follow.

| Core Kernel Component | Execution Mapping |
|-----------------------|-------------------|
| Canonical Models | model specifications and conceptual ownership |
| Core Domains | domain specs and domain services |
| Core Objects | object specs, domain models and database tables |
| Core Services | service specs, service implementations and APIs |
| Execution Primitives | events, tasks, states, contexts and workflow contracts |
| Core Contracts | data, API, event, agent, workflow and consumption contracts |
| Core Consumption | product integration, Workplace consumption and Codex tasks |

Implementation shall preserve this chain.

---

# 32. Relationship to core-specs/

This chapter governs the top-level structure of `core-specs/`.

Every detailed specification should identify which Core Kernel component it belongs to.

For example:

- Domain specs belong to Core Domains.
- Object specs belong to Core Objects.
- Service specs belong to Core Services.
- Event specs belong to Execution Primitives and Core Contracts.
- Agent specs belong to AI Capability governance and Agent Contracts.
- API specs belong to Core Contracts.
- Workflow specs belong to Execution Primitives and Workflow Contracts.

No `core-specs/` file should exist without a clear relationship to the Core Kernel.

---

# 33. Exclusions

This chapter shall not include:

- detailed domain specifications;
- detailed object fields;
- service input/output contracts;
- event payloads;
- API endpoint definitions;
- product UI;
- product-specific workflows;
- deployment architecture;
- vendor-specific implementation;
- production AI prompts;
- full product PRDs.

---

# 34. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Core Kernel clearly.
- It keeps Core Kernel as an explanatory concept, not a new official title.
- It identifies the seven Core Kernel components.
- It explains relationships among components.
- It connects Core Kernel to Professional Value Flow.
- It connects Core Kernel to ontology and domain classification.
- It distinguishes Core Kernel from product, Workplace, network, AI and implementation.
- It defines Core Kernel integrity and traceability.
- It prepares Chapters 10 through 17.
- It supports Book 02 TOC v1.2.
- It does not become a PRD or implementation guide.

---

# 35. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 09, defining the Core Kernel overview and seven-component architecture. |

---

**End of Chapter**
