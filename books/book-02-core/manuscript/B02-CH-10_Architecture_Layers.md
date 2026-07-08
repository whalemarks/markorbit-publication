# Book 02

# 10 — Architecture Layers

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-10

**Chapter Title:** Architecture Layers

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

This chapter defines the architecture layers of the MarkOrbit Core.

Chapter 09 introduced the Core Kernel as the stable internal architecture of the MarkOrbit Core.

This chapter defines the layered structure that governs how responsibility is distributed across the MarkOrbit ecosystem.

Architecture layers are necessary because MarkOrbit is not a single application.

It includes:

- operating philosophy;
- Core architecture;
- business responsibility;
- execution primitives;
- integration contracts;
- products;
- Workplaces;
- AI capabilities;
- global collaboration networks;
- implementation assets.

If these responsibilities are not separated into layers, the system will become difficult to govern.

Products may redefine Core meaning.

Workflow execution may be pushed into Core.

AI agents may bypass knowledge and permission rules.

Implementation may define semantics before architecture.

Product UI may be confused with Core Objects.

This chapter prevents these problems by defining a layered architecture.

---

# 2. Core Question

This chapter answers one question:

> What architecture layers organize the MarkOrbit Core and its downstream consumers?

The answer is:

> The MarkOrbit Core is organized through six architecture layers: Principles, Core, Business Responsibility, Execution Primitives, Integration Contracts and Products.

These layers form a responsibility structure.

They are not merely technical tiers.

They define ownership, dependency and boundary.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- the purpose of architecture layers;
- the six Book 02 architecture layers;
- the responsibility of each layer;
- the dependency direction among layers;
- what each layer owns;
- what each layer must not own;
- how layers relate to Core Kernel components;
- how layers relate to Book 01, Book 03, Book 04, Book 05 and Book 06;
- layer boundary rules;
- layer violation patterns;
- how layers guide `core-specs/` and Codex implementation.

## 3.2 Out of Scope

This chapter does not define:

- deployment layers;
- infrastructure layers;
- cloud architecture;
- microservice topology;
- database schema;
- front-end architecture;
- API endpoint details;
- product UI;
- product-specific workflows;
- full implementation architecture.

Those belong to implementation documents, product documents or later technical specifications.

---

# 4. Architecture Layer Definition

An architecture layer is:

> a responsibility level that defines what kind of architectural meaning is owned at that level and what must be consumed from other levels.

A layer is not simply a software tier.

For example:

- Product is a layer because it owns user-facing functionality.
- Core is a layer because it owns shared professional meaning and reusable capability.
- Integration Contracts is a layer because it owns how Core is consumed.
- Business Responsibility is a layer because it owns responsibility, delegation and value creation boundaries.

A layer answers:

- What does this level own?
- What does this level consume?
- What must this level not redefine?
- What must be specified before implementation?
- Which downstream layers depend on it?

---

# 5. Why Layers Matter

Without layers, responsibilities collapse into each other.

Common failures include:

- products defining Core Objects locally;
- workflow screens defining workflow contracts;
- database tables defining domain meaning;
- AI prompts defining professional rules;
- user interface flows defining business responsibility;
- network products redefining agents and service providers;
- implementation code defining architecture.

These failures may not be visible at the beginning.

They become serious when multiple products need to share meaning.

Architecture layers prevent these failures by making responsibility explicit.

Each layer has a role.

Each layer has boundaries.

Each layer depends on the layers above it and enables the layers below it.

---

# 6. Layer Overview

Book 02 uses six architecture layers.

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

This is the official layer structure for Book 02.

It is designed to support the MarkOrbit Core without turning Book 02 into a product PRD or implementation manual.

---

# 7. Layer 1 — Principles

## 7.1 Definition

The Principles Layer defines the operating logic and architectural rules that govern the Core.

It includes:

- Professional OS logic from Book 01;
- Core design principles;
- boundary rules;
- ontology rules;
- value flow rules;
- architecture governance principles.

The Principles Layer answers:

> Why should the Core be designed this way?

## 7.2 Owns

The Principles Layer owns:

- operating philosophy reference;
- Core principles;
- professional value flow;
- ontology logic;
- responsibility rules;
- boundary rules;
- governance logic;
- human responsibility rules;
- AI governance principles.

## 7.3 Does Not Own

The Principles Layer does not own:

- domains;
- object fields;
- services;
- API contracts;
- product features;
- database schemas;
- implementation code.

## 7.4 Consumers

The Principles Layer is consumed by:

- Core Layer;
- Business Responsibility Layer;
- Execution Primitives Layer;
- Integration Contracts Layer;
- Product Layer;
- `core-specs/`;
- Codex implementation tasks.

## 7.5 Example

The principle “Domain Before Feature” does not define the Trademark Domain directly.

It governs how Trademark is later defined.

The principle “Governance Before Automation” does not define an AI agent directly.

It governs how AI agent specifications must be written.

---

# 8. Layer 2 — Core

## 8.1 Definition

The Core Layer defines shared professional meaning and reusable capability.

It is the central layer of Book 02.

It includes:

- Canonical Models;
- Core Domains;
- Core Objects;
- Core Services;
- Knowledge foundations;
- shared semantic rules.

The Core Layer answers:

> What shared concepts and capabilities must remain consistent across the ecosystem?

## 8.2 Owns

The Core Layer owns:

- canonical models;
- Core Domain architecture;
- Core Object architecture;
- Core Service architecture;
- Knowledge architecture;
- Capability architecture;
- shared domain semantics;
- reusable service capabilities.

## 8.3 Does Not Own

The Core Layer does not own:

- product UI;
- product-specific workflow execution;
- commercial packaging;
- deployment mechanics;
- prompt libraries;
- vendor-specific implementation.

## 8.4 Consumers

The Core Layer is consumed by:

- Business Responsibility Layer;
- Execution Primitives Layer;
- Integration Contracts Layer;
- Workplaces;
- Products;
- AI agents;
- implementation assets.

## 8.5 Example

Trademark, Brand, Knowledge, Matter, Order, Agent and Service Provider may be Core concepts.

Their product presentation belongs downstream.

Their shared meaning belongs to the Core Layer.

---

# 9. Layer 3 — Business Responsibility

## 9.1 Definition

The Business Responsibility Layer defines ownership, delegation, authorization, responsibility and value creation.

It connects Core meaning to business accountability.

This layer answers:

> Who owns, authorizes, delegates, acts, receives value or bears responsibility?

This layer is necessary because professional services are not only data and workflow.

They involve responsibility.

## 9.2 Owns

The Business Responsibility Layer owns:

- business ownership;
- customer responsibility;
- opportunity ownership;
- matter responsibility;
- order responsibility;
- delegation;
- authorization;
- commercial responsibility;
- value creation relationships;
- responsibility transfer;
- human review responsibility.

## 9.3 Does Not Own

The Business Responsibility Layer does not own:

- product pricing plans;
- membership packages;
- marketing bundles;
- sales scripts;
- commission schedules;
- product commercialization strategy.

## 9.4 Consumers

The Business Responsibility Layer is consumed by:

- Order;
- Matter;
- Opportunity;
- Routing;
- Permission;
- Policy;
- AI Capability governance;
- Product Consumption;
- Codex implementation tasks.

## 9.5 Example

Book 02 may define that a Matter has a responsible owner, assigned executor and review authority.

Book 02 shall not define the price of a matter package.

Book 02 may define order-to-matter responsibility conversion.

Book 02 shall not define subscription membership pricing.

---

# 10. Layer 4 — Execution Primitives

## 10.1 Definition

The Execution Primitives Layer defines the basic structures that make professional work traceable, stateful and interoperable.

It answers:

> How does work move, change state, trigger action and remain observable?

This layer does not operate workflow execution.

It defines the primitives and contracts required for execution.

## 10.2 Owns

The Execution Primitives Layer owns:

- Event Primitive;
- Task Primitive;
- State Primitive;
- Context Primitive;
- Notification Contract;
- Workflow Contract;
- execution lifecycle concepts;
- event-driven coordination rules;
- task responsibility structures.

## 10.3 Does Not Own

The Execution Primitives Layer does not own:

- product-specific workflow screens;
- day-to-day workflow operation;
- Workplace user experience;
- operational SOPs;
- product journey steps.

## 10.4 Consumers

The Execution Primitives Layer is consumed by:

- Workplace Framework;
- MarkReg;
- MarkOrbit Lite;
- MGSN;
- AI agents;
- notification systems;
- routing services;
- event infrastructure;
- Codex implementation tasks.

## 10.5 Example

The Core may define a Workflow Contract for trademark filing matter progression.

Workplace operates that workflow.

MarkReg displays it to users.

The Core does not own the MarkReg filing wizard.

---

# 11. Layer 5 — Integration Contracts

## 11.1 Definition

The Integration Contracts Layer defines how the Core is consumed by downstream systems.

It answers:

> How do products, Workplaces, AI agents, services and implementations safely consume Core without redefining it?

Contracts are required because MarkOrbit is an ecosystem.

Informal integration will not scale.

## 11.2 Owns

The Integration Contracts Layer owns:

- Data Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Consumption Contract;
- version compatibility rules;
- contract validation rules;
- contract ownership rules.

## 11.3 Does Not Own

The Integration Contracts Layer does not own:

- product UI;
- product-specific implementation;
- vendor-specific API clients;
- deployment configuration;
- unofficial data access patterns;
- prompt libraries.

## 11.4 Consumers

The Integration Contracts Layer is consumed by:

- all products;
- Workplace;
- AI agents;
- Codex tasks;
- service implementations;
- external integrations where applicable.

## 11.5 Example

A product may call a Trademark Search API.

The API Contract defines input, output, permission, error behavior and semantic meaning.

The product may design any search page it wants.

It may not reinterpret what a Trademark means.

---

# 12. Layer 6 — Products

## 12.1 Definition

The Products Layer delivers user-facing functionality.

It answers:

> How is Core value experienced by users, clients, partners and service providers?

Products consume the Core.

They do not define it.

Products include:

- MarkReg;
- MarkOrbit Lite;
- MGSN;
- Brand Asset Vault;
- Opportunity Engine;
- future products.

## 12.2 Owns

The Products Layer owns:

- product features;
- user interfaces;
- user journeys;
- product-specific workflows;
- product reports;
- product dashboards;
- onboarding flows;
- product packaging;
- product-specific configuration;
- product-specific experience.

## 12.3 Does Not Own

The Products Layer does not own:

- Core Domain meanings;
- Core Object semantics;
- Core Service definitions;
- cross-product event semantics;
- Core AI governance;
- Core permission rules;
- Core contract meanings.

## 12.4 Consumers

The Products Layer consumes:

- Core Objects;
- Core Services;
- Core Events;
- AI Capabilities;
- Workflow Contracts;
- API Contracts;
- Consumption Contracts.

## 12.5 Example

MarkOrbit Lite may provide a guided AI filing experience.

That product experience may consume:

- Brand;
- Trademark;
- Jurisdiction;
- Classification;
- Knowledge;
- Goods Recommendation Service;
- AI Capability;
- Order;
- Matter.

Lite may simplify the user experience.

It shall not simplify Core meaning into conflicting local definitions.

---

# 13. Layer Dependency Direction

Layer dependency is directional.

```text
Principles
        define
Core
        provides
Business Responsibility
        owns
Execution Primitives
        coordinate
Integration Contracts
        connect
Products
        consume
```

The downstream layers depend on upstream layers.

Products depend on Contracts.

Contracts depend on Primitives.

Primitives depend on Business Responsibility and Core Objects.

Business Responsibility depends on Core identity, domains and policies.

Core depends on Principles.

The reverse direction may provide feedback but shall not define meaning directly.

---

# 14. Reverse Dependency Rule

Downstream needs may reveal missing upstream architecture.

For example:

- a product feature may reveal the need for a new Core Service;
- a workflow requirement may reveal the need for a new Event;
- an AI use case may reveal the need for a Knowledge Source;
- an integration requirement may reveal the need for an API Contract.

But downstream needs shall not directly define upstream meaning.

The correct process is:

```text
Downstream need
        ↓
Architecture review
        ↓
Core extension or contract update
        ↓
core-specs update
        ↓
Implementation
```

This preserves architectural governance.

---

# 15. Layer and Core Kernel Relationship

The architecture layers and Core Kernel components are related but not identical.

Core Kernel components describe what the Core contains.

Architecture layers describe where responsibility belongs.

The relationship can be summarized as follows.

| Architecture Layer | Related Core Kernel Components |
|--------------------|--------------------------------|
| Principles | Core Principles, Value Flow, Ontology |
| Core | Canonical Models, Core Domains, Core Objects, Core Services |
| Business Responsibility | Business Responsibility Model, Policy, Permission, Ownership |
| Execution Primitives | Events, Tasks, States, Contexts, Workflow Contracts |
| Integration Contracts | Data, API, Event, Agent, Workflow, Consumption Contracts |
| Products | Core Consumption, Product Specialization |

This distinction prevents confusion.

A component is part of the kernel.

A layer is a responsibility level.

---

# 16. Layer and Professional Value Flow Relationship

Architecture layers support the Professional Value Flow.

| Value Flow Stage | Supporting Layers |
|------------------|------------------|
| Reality | Core |
| Facts | Core, Execution Primitives |
| Understanding | Core, Principles |
| Judgment | Core, Business Responsibility, AI Governance |
| Action | Core Services, Execution Primitives |
| Coordination | Execution Primitives, Integration Contracts |
| Experience | Products, Workplace, Core Consumption |

The Products Layer delivers experience, but it depends on upstream layers for meaning and capability.

The Core Layer represents reality and facts.

The Business Responsibility Layer governs judgment and accountability.

The Execution Primitives Layer makes action and coordination traceable.

The Integration Contracts Layer makes consumption safe.

---

# 17. Layer and Ontology Relationship

The ontology layers from Chapter 08 interact with the architecture layers.

| Ontology Layer | Primary Architecture Layers |
|----------------|-----------------------------|
| Reality Ontology | Core |
| System Ontology | Principles, Core, Integration Contracts |
| Execution Ontology | Business Responsibility, Execution Primitives |
| Collaboration Ontology | Core, Execution Primitives, Integration Contracts, Products |

Ontology answers what kind of thing a concept is.

Architecture layer answers where responsibility belongs.

For example:

- Agent may be a reality and collaboration concept.
- Agent Domain belongs to the Core Layer.
- Agent Matching may be a Core Service.
- Agent routing may use Execution Primitives.
- MGSN displays Agent through the Products Layer.

---

# 18. Layer and Domain Category Relationship

Core Domain categories map to layers.

| Domain Category | Primary Layer |
|-----------------|---------------|
| Foundation Domains | Core |
| Professional Domains | Core |
| Business Execution Domains | Business Responsibility and Execution Primitives |
| Collaboration Network Domains | Core, Execution Primitives and Integration Contracts |

The mapping is not exclusive.

For example:

- Knowledge is a Foundation Domain but supports AI governance and product consumption.
- Matter is a Business Execution Domain but has Core Object meaning.
- Routing is a Collaboration Network Domain but may use Policy, Events and AI.

Layering clarifies primary responsibility.

It does not prevent cross-layer collaboration.

---

# 19. Layer and `core-specs/` Relationship

`core-specs/` should preserve layer responsibility.

A `core-specs/` file should identify which layer it primarily belongs to.

Examples:

- `core-specs/domains/trademark.md` belongs primarily to the Core Layer.
- `core-specs/objects/matter.md` belongs to Core and Business Responsibility.
- `core-specs/events/matter-created.md` belongs to Execution Primitives and Integration Contracts.
- `core-specs/agents/classification-assistant.md` belongs to Core Capability and AI Governance.
- `core-specs/api/trademarks.md` belongs to Integration Contracts.
- `core-specs/workflows/trademark-filing.md` belongs to Execution Primitives and Workflow Contracts.

This helps prevent specification files from absorbing responsibilities that belong elsewhere.

---

# 20. Layer and Codex Relationship

Codex implementation tasks shall respect layers.

Codex may generate implementation assets such as:

- database tables;
- domain models;
- services;
- APIs;
- events;
- tests;
- agent scaffolds;
- workflow contract scaffolds.

But Codex shall not decide layer responsibility.

Codex tasks should specify:

- source chapter;
- source domain;
- source object or service;
- target layer;
- related contracts;
- boundary rules;
- acceptance criteria.

For example:

A Codex task to implement `MatterCreated` should reference:

- Matter Domain;
- Event Specification;
- Execution Primitives Layer;
- Event Contract;
- related `core-specs/events/` file;
- expected tests.

It should not create a product workflow screen unless the product document requests it.

---

# 21. Layer Boundary Rules

The following rules govern layer boundaries.

## Rule 1 — Principles define, but do not implement

The Principles Layer provides rules.

It does not create schemas or APIs.

## Rule 2 — Core provides shared meaning

The Core Layer defines reusable models, domains, objects and services.

It does not define product UI.

## Rule 3 — Business Responsibility owns accountability

Business Responsibility defines ownership, delegation, authorization and value responsibility.

It does not define product pricing packages.

## Rule 4 — Execution Primitives coordinate work

Execution Primitives define events, tasks, states, contexts and workflow contracts.

They do not operate product workflows.

## Rule 5 — Integration Contracts connect consumers

Integration Contracts define safe consumption.

They do not replace product implementation.

## Rule 6 — Products deliver experience

Products deliver user-facing functionality.

They do not redefine Core meaning.

## Rule 7 — AI follows layer rules

AI capabilities must respect Core, Business Responsibility, Execution Primitives and Integration Contracts.

AI does not bypass layers.

---

# 22. Layer Violation Patterns

## 22.1 Product Defines Core

A product page defines the meaning of a Core Object.

Example:

> MarkReg defines Trademark differently from Lite.

Violation:

- Product Layer redefines Core Layer.

Correction:

- Trademark meaning belongs to Core.
- Products consume it.

## 22.2 Workflow Operation Enters Core

A detailed product workflow is written into Book 02.

Violation:

- Execution operation absorbs Workplace and Product responsibilities.

Correction:

- Book 02 defines Workflow Contract.
- Workplace operates workflow.
- Products deliver experience.

## 22.3 Database Defines Domain

Implementation tables are treated as domain definitions.

Violation:

- Implementation defines Core.

Correction:

- Domain specification defines meaning.
- Database implements it.

## 22.4 AI Defines Professional Truth

AI prompt output is treated as authoritative professional judgment.

Violation:

- AI bypasses Core governance and human responsibility.

Correction:

- AI is governed capability.
- Human review applies where risk is high.

## 22.5 API Bypasses Contract

A product reads or writes Core data directly without API or contract.

Violation:

- Product bypasses Integration Contracts.

Correction:

- Product consumes Core through explicit contracts.

## 22.6 Business Package Enters Core

A product sales package is written into Business Responsibility Specification.

Violation:

- Product commercialization enters Core.

Correction:

- Core defines business responsibility.
- Product documents define pricing and packages.

---

# 23. Layer Review Questions

When reviewing any proposal, reviewers shall ask:

1. Which layer owns this concept?
2. Which layer consumes it?
3. Does it redefine a concept from an upstream layer?
4. Does it belong to Core, Workplace, Product or implementation?
5. Is it a principle, model, domain, object, service, primitive, contract or product feature?
6. Does it require business responsibility?
7. Does it require execution primitives?
8. Does it require integration contracts?
9. Does AI interact with it under governance?
10. Does Codex have approved source specifications?
11. Would implementing it in the wrong layer cause fragmentation?
12. Does it preserve the Core / Workplace / Product boundary?

---

# 24. Layer Decision Matrix

| Proposed Concept | Likely Layer | Notes |
|------------------|--------------|-------|
| Domain Before Feature | Principles | Design rule |
| Trademark | Core | Professional Domain / Core Object |
| Trademark Search Service | Core | Reusable Core Service |
| Trademark Search Page | Products | Product UI |
| Matter Owner | Business Responsibility | Accountability |
| MatterCreated Event | Execution Primitives | Event primitive and contract |
| Trademark API | Integration Contracts | Core API consumption |
| MarkReg Filing Wizard | Products | Product feature |
| Workflow Contract | Execution Primitives / Integration Contracts | Core contract |
| Workflow Operation Board | Workplace / Product | Not Core |
| AI Classification Assistant | Core Capability under Governance | Requires Agent Contract |
| AI Prompt Template | Implementation | Not Book 02 manuscript |
| Pricing Plan | Product Business Document | Not Core |
| Permission Evaluation | Core / Business Responsibility | Shared governance |
| Deployment Script | Implementation | Not Book 02 |

---

# 25. Layer Traceability

Layer traceability means that an implementation asset can be traced back to its correct architecture layer.

Example:

```text
Professional Meaning
        ↓
Core Domain
        ↓
Core Object
        ↓
Core Service
        ↓
Execution Event
        ↓
API Contract
        ↓
Product Feature
        ↓
Implementation Task
```

Traceability prevents code, UI and AI agents from becoming disconnected from architecture.

Every significant implementation asset should be traceable to:

- a layer;
- a domain;
- an object or service;
- a contract;
- a product consumer;
- an acceptance criterion.

---

# 26. Layer Compatibility

Layer changes must be evaluated for downstream impact.

For example:

- changing a Core Object may affect products, APIs, AI agents and events;
- changing an Event may affect notifications, opportunity detection and audit;
- changing a Contract may affect multiple products;
- changing a Business Responsibility rule may affect permissions, routing and human review;
- changing a Workflow Contract may affect Workplace and product workflows.

Architecture layers therefore require compatibility review.

A layer should not be changed only to satisfy a local product need.

---

# 27. Layer and MVP

The MVP shall implement layers in a disciplined way.

The MVP does not need to complete every domain.

But it must preserve layer structure.

A healthy MVP should include:

- enough Principles to govern development;
- enough Core to define Identity, Knowledge, Brand, Trademark and Matter;
- enough Business Responsibility to define ownership and authorization;
- enough Execution Primitives to support Task and Event;
- enough Integration Contracts to support product consumption;
- enough Product consumption to validate Core usefulness.

MVP shall not become only a product prototype.

It must create an executable Core skeleton.

---

# 28. Layer Rules

The following rules are established by this chapter.

## Rule 1 — Architecture layers SHALL define responsibility

Layers are responsibility boundaries, not only software tiers.

## Rule 2 — Dependency SHALL flow downward

Principles define Core.

Core provides capability.

Business Responsibility owns accountability.

Execution Primitives coordinate work.

Integration Contracts connect consumers.

Products consume Core.

## Rule 3 — Downstream layers SHALL NOT redefine upstream meaning

Products may reveal needs but shall not directly redefine Core semantics.

## Rule 4 — Core SHALL NOT absorb Workplace

Core defines primitives and contracts.

Workplace operates workflow.

## Rule 5 — Products SHALL NOT bypass Integration Contracts

Products shall consume Core through explicit contracts.

## Rule 6 — AI SHALL NOT bypass layer governance

AI must respect identity, permission, knowledge, policy, events and review.

## Rule 7 — Implementation SHALL NOT define architecture

Implementation realizes approved specifications.

It shall not create Core meaning independently.

## Rule 8 — MVP SHALL preserve layer integrity

Even partial implementation must respect layer boundaries.

---

# 29. Specification Output

This chapter produces the following specification output:

- six-layer architecture model;
- layer definitions;
- layer ownership rules;
- layer exclusion rules;
- layer dependency direction;
- reverse dependency rule;
- layer relationship to Core Kernel components;
- layer relationship to value flow;
- layer relationship to ontology;
- layer relationship to domain categories;
- layer relationship to `core-specs/`;
- layer relationship to Codex;
- layer boundary rules;
- layer violation patterns;
- layer review questions;
- layer decision matrix;
- layer traceability rules;
- layer compatibility rules;
- layer MVP rules.

These outputs shall guide Chapters 11 through 17 and all later `core-specs/`.

---

# 30. Execution Mapping

This chapter does not directly define database tables or API endpoints.

It controls how execution assets are assigned to layers.

| Layer | Execution Mapping |
|-------|-------------------|
| Principles | editorial rules, governance rules, review questions |
| Core | domain specs, object specs, service specs |
| Business Responsibility | ownership, delegation, permission, policy and review specs |
| Execution Primitives | events, tasks, states, contexts, workflow contracts |
| Integration Contracts | APIs, event contracts, agent contracts, data contracts |
| Products | product features, UI, product workflows and user experience |

Implementation shall preserve layer ownership.

---

# 31. Relationship to core-specs/

This chapter governs layer assignment for `core-specs/`.

Every detailed specification should identify its primary layer and any secondary layers.

For example:

```text
core-specs/domains/trademark.md
    Primary Layer: Core

core-specs/events/matter-created.md
    Primary Layer: Execution Primitives
    Secondary Layer: Integration Contracts

core-specs/agents/classification-assistant.md
    Primary Layer: Core Capability
    Secondary Layer: Business Responsibility / Integration Contracts

core-specs/api/trademarks.md
    Primary Layer: Integration Contracts
```

No `core-specs/` file should mix layer responsibilities without stating the boundary.

---

# 32. Exclusions

This chapter shall not include:

- infrastructure layering;
- microservice architecture;
- database physical design;
- front-end component hierarchy;
- API endpoint details;
- product user journeys;
- workflow operation manuals;
- AI prompt libraries;
- deployment topology;
- sales and pricing strategy.

These belong elsewhere.

---

# 33. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines the six Book 02 architecture layers.
- It explains what each layer owns and excludes.
- It establishes layer dependency direction.
- It distinguishes layers from Core Kernel components.
- It connects layers to value flow, ontology and domain categories.
- It preserves the Core / Workplace / Product boundary.
- It defines layer violation patterns.
- It gives layer review questions and decision matrix.
- It explains how layers guide `core-specs/` and Codex.
- It supports MVP execution without becoming a product PRD.
- It supports Book 02 TOC v1.2.

---

# 34. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 10, defining the six architecture layers of the MarkOrbit Core. |

---

**End of Chapter**
