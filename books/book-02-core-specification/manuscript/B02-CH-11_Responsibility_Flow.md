# Book 02

# 11 — Responsibility Flow

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-11

**Chapter Title:** Responsibility Flow

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

This chapter defines the responsibility flow of the MarkOrbit Core.

Chapter 10 defined the architecture layers.

This chapter explains how responsibility moves across those layers.

Architecture layers define where responsibility belongs.

Responsibility flow defines how those responsibilities relate to each other.

This distinction matters because MarkOrbit is an ecosystem, not a single application.

A Core Object may be defined in the Core Layer.

A business owner may be determined in the Business Responsibility Layer.

A task may be created in the Execution Primitives Layer.

An API may expose it through the Integration Contracts Layer.

A product may display it in the Products Layer.

An AI agent may assist with it under governance.

If responsibility flow is unclear, products may redefine the Core, AI may bypass governance, workflows may absorb product behavior, or implementation may define architecture accidentally.

This chapter prevents those failures by defining the official responsibility flow of Book 02.

---

# 2. Core Question

This chapter answers one question:

> How should responsibility flow through the MarkOrbit Core architecture?

The answer is:

> Principles define, Core provides, Business owns, Execution coordinates, Integration connects, and Products consume.

The responsibility flow is:

```text
Principles define
        ↓
Core provides
        ↓
Business owns
        ↓
Execution coordinates
        ↓
Integration connects
        ↓
Products consume
```

This flow is directional.

Downstream layers may reveal needs.

They shall not redefine upstream meaning directly.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- the responsibility flow of Book 02;
- the meaning of each responsibility verb;
- the direction of responsibility;
- the difference between ownership, provision, coordination, connection and consumption;
- responsibility boundaries among Core, Business, Execution, Integration and Product;
- how responsibility flow applies to domains, objects, services, events, AI capabilities and Codex tasks;
- how responsibility violations are detected;
- how downstream needs become governed upstream changes.

## 3.2 Out of Scope

This chapter does not define:

- organization chart;
- team responsibilities;
- personnel assignments;
- product management workflow;
- sales responsibility;
- operational SOPs;
- detailed workflow execution;
- database schema;
- API endpoint design;
- implementation code.

This chapter defines architectural responsibility, not internal company management.

---

# 4. Responsibility Flow Definition

Responsibility Flow is defined as:

> the directional structure that determines which architectural layer defines, provides, owns, coordinates, connects or consumes a concept, capability or execution asset.

Responsibility Flow is not a project management chart.

It is not a team assignment chart.

It is not a task board.

It is an architectural control mechanism.

It answers:

- who defines meaning;
- who provides capability;
- who owns business responsibility;
- who coordinates execution;
- who connects systems;
- who consumes the Core;
- who may request change;
- who may not redefine upstream concepts.

---

# 5. Official Responsibility Flow

The official Book 02 responsibility flow is:

```text
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
```

This can also be expressed as:

```text
Principles
    define rules and meaning constraints

Core
    provides shared models, domains, objects and services

Business Responsibility
    owns accountability, delegation and value responsibility

Execution Primitives
    coordinate action, state, events and tasks

Integration Contracts
    connect consumers through explicit contracts

Products
    consume Core to deliver user-facing functionality
```

This flow shall govern all Book 02 chapters and all related `core-specs/`.

---

# 6. Principles Define

## 6.1 Meaning

Principles define the rules that govern the system.

They answer:

> What must remain true?

Principles define:

- Core design rules;
- boundary rules;
- professional value flow;
- ontology rules;
- AI governance rules;
- human responsibility rules;
- product consumption rules;
- specification-before-implementation rules.

## 6.2 Responsibility

The Principles layer is responsible for defining:

- why Core exists;
- what Core must protect;
- what belongs to Core;
- what does not belong to Core;
- how Core should evolve;
- how AI should be governed;
- how products should consume Core.

## 6.3 Does Not Do

Principles do not implement.

Principles do not create database tables.

Principles do not define UI.

Principles do not directly create product features.

Principles guide later responsibilities.

## 6.4 Example

The principle:

```text
Domain Before Feature
```

does not define the Trademark Domain by itself.

It controls how the Trademark Domain should be defined and prevents a product feature from becoming the domain source.

---

# 7. Core Provides

## 7.1 Meaning

Core provides shared professional meaning and reusable capability.

It answers:

> What shared foundation does the ecosystem need?

Core provides:

- Canonical Models;
- Core Domains;
- Core Objects;
- Core Services;
- Knowledge structures;
- Capability structures;
- shared semantic rules;
- reusable service capabilities.

## 7.2 Responsibility

The Core layer is responsible for providing stable and reusable foundations.

It provides the objects and services that downstream layers use.

Examples:

- Trademark;
- Brand;
- Matter;
- Order;
- Opportunity;
- Agent;
- Service Provider;
- Task;
- Event;
- Knowledge Retrieval Service;
- Classification Recommendation Service;
- Routing Decision Service.

## 7.3 Does Not Do

Core does not operate product workflows.

Core does not design user interfaces.

Core does not define product pricing.

Core does not own product-specific behavior.

Core does not replace human professional responsibility.

## 7.4 Example

Core provides `Trademark`.

MarkReg consumes `Trademark`.

Lite consumes `Trademark`.

Opportunity Engine consumes `Trademark`.

No product may redefine what `Trademark` means locally.

---

# 8. Business Owns

## 8.1 Meaning

Business Responsibility owns accountability.

It answers:

> Who is responsible, authorized, delegated, accountable or entitled to value?

This layer connects Core meaning to professional and commercial responsibility.

## 8.2 Responsibility

Business owns:

- customer responsibility;
- matter responsibility;
- order responsibility;
- opportunity ownership;
- delegation;
- authorization;
- review authority;
- commercial responsibility;
- value creation relationship;
- responsibility transfer.

## 8.3 Does Not Do

Business Responsibility does not define product pricing.

It does not define sales packages.

It does not define marketing copy.

It does not define commission schedules.

It defines responsibility, not commercialization.

## 8.4 Example

A Matter may have:

- customer owner;
- responsible operator;
- review authority;
- assigned agent;
- approving user;
- escalation owner.

These are business responsibility concepts.

They are not UI concepts.

---

# 9. Execution Coordinates

## 9.1 Meaning

Execution coordinates action, state and change.

It answers:

> How does work move forward and remain traceable?

Execution does not own professional meaning.

It coordinates work using primitives and contracts.

## 9.2 Responsibility

Execution coordinates through:

- Event;
- Task;
- State;
- Context;
- Notification;
- Workflow Contract;
- Assignment;
- Routing trigger;
- lifecycle transition.

## 9.3 Does Not Do

Execution does not own product screens.

Execution does not own workflow user experience.

Execution does not define professional truth.

Execution does not redefine Core Objects.

Execution does not replace Workplace operation.

## 9.4 Example

When an Order is converted into a Matter, Execution may coordinate:

- `OrderConvertedToMatter` event;
- `MatterCreated` event;
- initial Task creation;
- Notification;
- Workflow Contract activation.

The product decides how users see this.

Workplace decides how work is operated.

Core defines the primitives and contracts.

---

# 10. Integration Connects

## 10.1 Meaning

Integration connects consumers to Core through explicit contracts.

It answers:

> How may downstream systems safely consume Core?

Integration does not create meaning.

It protects meaning during consumption.

## 10.2 Responsibility

Integration connects through:

- Data Contracts;
- API Contracts;
- Event Contracts;
- Agent Contracts;
- Workflow Contracts;
- Consumption Contracts;
- version rules;
- compatibility rules;
- validation rules.

## 10.3 Does Not Do

Integration does not define product UI.

Integration does not bypass Core semantics.

Integration does not allow direct informal data manipulation.

Integration does not allow products to create conflicting meanings.

## 10.4 Example

MarkReg may use a Trademark API.

The API Contract defines:

- input;
- output;
- permission;
- semantic meaning;
- error behavior;
- event side effects.

MarkReg may design the search page.

It may not reinterpret the Trademark object.

---

# 11. Products Consume

## 11.1 Meaning

Products consume Core capabilities to deliver user-facing functionality.

They answer:

> How does the user experience Core value?

Products may specialize experience.

They shall not redefine Core meaning.

## 11.2 Responsibility

Products own:

- user interface;
- product features;
- product-specific workflows;
- user journeys;
- dashboards;
- reports;
- onboarding;
- product packaging;
- product configuration;
- product-specific experience.

## 11.3 Does Not Do

Products do not own:

- Core Domain meanings;
- Core Object semantics;
- Core Service definitions;
- Core Event semantics;
- AI governance rules;
- shared permission rules;
- contract meanings.

## 11.4 Example

Lite may provide a guided filing assistant.

It may consume:

- Brand;
- Trademark;
- Jurisdiction;
- Classification;
- Knowledge;
- AI Capability;
- Order;
- Matter.

The product experience is Lite-specific.

The underlying meanings are Core.

---

# 12. Directional Responsibility

Responsibility flow is directional.

```text
Principles → Core → Business → Execution → Integration → Products
```

This means:

- Principles govern Core.
- Core provides shared meaning to Business.
- Business defines responsibility for Execution.
- Execution produces observable state and action.
- Integration exposes execution and Core safely.
- Products consume what Integration exposes.

Downstream layers may request changes.

They may not directly redefine upstream layers.

---

# 13. Feedback Without Redefinition

Downstream feedback is allowed.

Downstream redefinition is not.

For example, MarkReg may discover that trademark filing requires a new document status.

This feedback may trigger:

```text
Product need
        ↓
Architecture review
        ↓
Core / Domain / Object / Event update
        ↓
core-specs update
        ↓
Implementation task
        ↓
Product consumption
```

The product does not directly redefine `Document`.

It requests an upstream extension.

This preserves architecture while allowing evolution.

---

# 14. Responsibility Flow and Core Kernel

The responsibility flow maps to the Core Kernel components.

| Responsibility Flow | Core Kernel Component |
|---------------------|-----------------------|
| Principles define | Core Principles, Value Flow, Ontology |
| Core provides | Canonical Models, Core Domains, Core Objects, Core Services |
| Business owns | Business Responsibility Model, Permission, Policy, Ownership |
| Execution coordinates | Events, Tasks, States, Contexts, Workflow Contracts |
| Integration connects | Data, API, Event, Agent, Workflow and Consumption Contracts |
| Products consume | Core Consumption and Product Specialization |

This mapping connects Chapter 11 with Chapter 09.

---

# 15. Responsibility Flow and Architecture Layers

The responsibility flow is the active form of the architecture layers from Chapter 10.

Architecture Layers:

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

Responsibility Flow:

```text
Principles define
        ↓
Core provides
        ↓
Business owns
        ↓
Execution coordinates
        ↓
Integration connects
        ↓
Products consume
```

The layers define positions.

The flow defines behavior.

---

# 16. Responsibility Flow and Professional Value Flow

Responsibility flow supports the Professional Value Flow.

| Professional Value Stage | Responsibility Flow |
|--------------------------|---------------------|
| Reality | Core provides representation |
| Facts | Core provides records; Execution coordinates events |
| Understanding | Core provides Knowledge; Principles define knowledge governance |
| Judgment | Business owns accountability; AI is governed |
| Action | Core Services act; Execution coordinates |
| Coordination | Execution coordinates; Integration connects |
| Experience | Products consume |

Professional value cannot flow correctly if responsibility is broken.

For example, if Product defines judgment without Business Responsibility, accountability is unclear.

If AI acts without Principles and Core Knowledge, output is unsafe.

If Execution coordinates without Events, coordination is invisible.

---

# 17. Responsibility Flow and Ontology

Ontology determines what kind of thing a concept is.

Responsibility flow determines what that concept does in the architecture.

Example:

```text
Trademark
    Ontology: Reality Ontology
    Layer: Core
    Responsibility Flow: Core provides

Matter Owner
    Ontology: System / Business Responsibility concept
    Layer: Business Responsibility
    Responsibility Flow: Business owns

MatterCreated
    Ontology: Execution Ontology
    Layer: Execution Primitives
    Responsibility Flow: Execution coordinates

Trademark API
    Ontology: System / Contract concept
    Layer: Integration Contracts
    Responsibility Flow: Integration connects

MarkReg Trademark Page
    Ontology: Product concept
    Layer: Products
    Responsibility Flow: Product consumes
```

Ontology and responsibility flow work together.

---

# 18. Responsibility Flow and Domain Categories

Domain categories participate in responsibility flow differently.

| Domain Category | Responsibility Flow Role |
|-----------------|--------------------------|
| Foundation Domains | Core provides basic structure |
| Professional Domains | Core provides professional meaning |
| Business Execution Domains | Business owns and Execution coordinates |
| Collaboration Network Domains | Core provides collaboration meaning; Integration connects network consumers |

Examples:

- Identity is provided by Core.
- Permission supports Business ownership and governance.
- Trademark is provided by Core as professional meaning.
- Matter participates in Business ownership and Execution coordination.
- Event coordinates execution.
- Routing connects collaboration and execution.
- Communication supports coordination and product consumption.

---

# 19. Responsibility Flow and AI

AI must follow responsibility flow.

AI may assist in many layers, but it does not own them.

AI may help:

- apply Principles through checks;
- retrieve Core Knowledge;
- recommend actions;
- summarize facts;
- draft documents;
- assist routing;
- monitor events;
- explain product status.

But AI shall not:

- define Core meaning;
- own Business Responsibility;
- bypass Execution controls;
- bypass Integration Contracts;
- replace Product governance;
- define professional truth.

AI is governed execution of capability.

AI is not a responsibility owner above the Core.

---

# 20. Responsibility Flow and Human Review

Human review belongs to the responsibility flow when professional risk is high.

High-risk actions include:

- legal advice;
- official filing submission;
- deadline-sensitive action;
- evidence sufficiency conclusion;
- office action strategy;
- final client communication;
- payment-sensitive decision;
- routing decision with material responsibility impact.

In those cases:

- Principles define review requirement.
- Core provides facts, knowledge and services.
- Business owns accountability.
- Execution coordinates review task and event.
- Integration connects review result.
- Product displays or acts on approved result.

Human review is not an external manual exception.

It is part of governed responsibility flow.

---

# 21. Responsibility Flow and Codex

Codex must also respect responsibility flow.

Codex may generate code quickly.

But it shall not decide responsibility.

A Codex task should state:

- source layer;
- source domain;
- source object or service;
- related responsibility;
- related contract;
- related acceptance criteria;
- boundary rules;
- prohibited overreach.

Example:

A task to implement Opportunity Scoring should not invent product sales strategy.

It should reference:

- Opportunity Domain;
- Knowledge dependencies;
- Policy rules;
- Business ownership;
- Event outputs;
- AI governance;
- product consumers;
- tests.

Codex follows responsibility flow.

Codex does not create it.

---

# 22. Responsibility Ownership Types

Book 02 distinguishes several responsibility ownership types.

## 22.1 Semantic Ownership

Defines meaning.

Usually belongs to Core.

Example:

- Trademark meaning;
- Agent meaning;
- Matter meaning.

## 22.2 Business Ownership

Defines responsibility, authorization and value accountability.

Usually belongs to Business Responsibility.

Example:

- customer owner;
- matter owner;
- opportunity owner;
- review authority.

## 22.3 Execution Ownership

Defines coordination responsibility for tasks, events and transitions.

Usually belongs to Execution Primitives and Workplace operation.

Example:

- task assignee;
- workflow transition trigger;
- event source.

## 22.4 Contract Ownership

Defines how consumers interact with Core.

Usually belongs to Integration Contracts.

Example:

- API owner;
- event contract owner;
- agent contract owner.

## 22.5 Experience Ownership

Defines user-facing experience.

Usually belongs to Products or Workplace.

Example:

- dashboard;
- wizard;
- user journey;
- product-specific workflow view.

These ownership types must not be mixed.

---

# 23. Responsibility Assignment Rules

The following assignment rules shall be used.

## Rule 1 — Meaning belongs upstream

Shared meaning belongs to Core.

## Rule 2 — Accountability belongs to Business Responsibility

Professional and commercial accountability shall be explicit.

## Rule 3 — Coordination belongs to Execution Primitives and Workplace

The Core defines primitives and contracts.

Workplace operates workflow.

## Rule 4 — Access belongs to Integration Contracts

Products consume Core through contracts.

## Rule 5 — Experience belongs downstream

Products and Workplace own user-facing experience.

## Rule 6 — AI does not own responsibility

AI assists under governance.

Responsibility remains assigned to human, business, domain or contract owners.

---

# 24. Responsibility Flow Examples

## 24.1 Example — Trademark Filing Matter

```text
Principles define
    domain-before-feature and governance-before-automation

Core provides
    Trademark, Jurisdiction, Classification, Document, Matter

Business owns
    customer responsibility, matter owner, review authority

Execution coordinates
    MatterCreated, TaskAssigned, DocumentRequested, DeadlineReminder

Integration connects
    APIs, events, workflow contract and agent contract

Products consume
    MarkReg filing workflow, Lite guided filing experience
```

## 24.2 Example — AI Goods Recommendation

```text
Principles define
    knowledge-before-response and human responsibility before AI autonomy

Core provides
    Classification, Jurisdiction, Knowledge, Recommendation Service

Business owns
    approval responsibility and client advice responsibility

Execution coordinates
    recommendation event, review task, acceptance record

Integration connects
    agent contract, API contract and consumption contract

Products consume
    class selection wizard or AI chat interface
```

## 24.3 Example — Agent Routing

```text
Principles define
    governance before automation and contract before integration

Core provides
    Agent, Service Provider, Jurisdiction, Service Network

Business owns
    matter assignment responsibility and service responsibility

Execution coordinates
    RoutingDecisionMade, TaskAssigned, NotificationCreated

Integration connects
    routing API, event contract and communication contract

Products consume
    MarkReg assignment view or MGSN routing experience
```

---

# 25. Responsibility Flow Violations

## 25.1 Product Redefines Core

A product defines a local `Trademark` meaning that conflicts with Core.

Violation:

```text
Products redefine Core.
```

Correction:

```text
Product consumes Core Trademark.
Core extension requires architecture review.
```

## 25.2 AI Owns Judgment

An AI agent issues final legal advice without review.

Violation:

```text
AI bypasses Business Responsibility and human review.
```

Correction:

```text
AI provides recommendation.
Business owns review and approval.
Execution records review event.
```

## 25.3 Workflow Screen Defines Contract

A product workflow screen becomes the source of Workflow Contract.

Violation:

```text
Product experience defines Execution Contract.
```

Correction:

```text
Core defines Workflow Contract.
Workplace operates workflow.
Product displays workflow.
```

## 25.4 Implementation Defines Meaning

A database schema is created first and later treated as the Core Object definition.

Violation:

```text
Implementation defines Core semantics.
```

Correction:

```text
Core Object Specification defines meaning.
Database implements it.
```

## 25.5 Integration Bypasses Permission

A product reads or changes Core data directly without permission checks.

Violation:

```text
Product bypasses Integration and Business Responsibility.
```

Correction:

```text
Product uses contract.
Contract enforces permission and policy.
```

---

# 26. Responsibility Flow Review Questions

When reviewing a concept, chapter, specification or Codex task, reviewers shall ask:

1. What responsibility does this concept carry?
2. Which layer owns that responsibility?
3. Is this semantic, business, execution, contract or experience responsibility?
4. Does it redefine an upstream concept?
5. Does it bypass Core, Business Responsibility, Execution or Integration?
6. Does it assign accountability clearly?
7. Does it involve AI? If yes, who reviews and who is accountable?
8. Does it produce or consume events?
9. Does it require an API, event, agent or workflow contract?
10. Which product consumes it?
11. Which `core-specs/` file should define it?
12. Can Codex implement it without inventing responsibility?

---

# 27. Responsibility Decision Matrix

| Proposed Item | Responsibility Type | Owner Layer | Notes |
|---------------|--------------------|-------------|-------|
| Trademark meaning | Semantic | Core | Shared Core Object |
| Brand portfolio | Semantic | Core | Shared professional meaning |
| Matter owner | Business | Business Responsibility | Accountability |
| Opportunity owner | Business | Business Responsibility | Value ownership |
| Task assignment | Execution | Execution Primitives / Workplace | Coordination |
| MatterCreated event | Execution / Contract | Execution Primitives / Integration | Observable change |
| Trademark API | Contract | Integration Contracts | Consumption path |
| MarkReg detail page | Experience | Products | Product UI |
| AI draft recommendation | Capability / Governance | Core + Business Review | Requires governance |
| Prompt template | Implementation | Agent Implementation | Not manuscript |
| Pricing plan | Commercial Product | Product Business Docs | Not Core |
| Workflow operation board | Experience / Operation | Workplace / Product | Not Core execution definition |
| Permission check | Governance | Core / Business Responsibility | Shared access control |

---

# 28. Responsibility Traceability

Responsibility traceability means that every important system action can be traced to its responsible layer and owner.

Example:

```text
AI recommends goods/services
        ↓
Principle: Knowledge Before Response
        ↓
Core: Classification + Knowledge
        ↓
Business: Review responsibility
        ↓
Execution: Review task + Recommendation event
        ↓
Integration: Agent Contract + API Contract
        ↓
Product: Lite recommendation UI
        ↓
Implementation: Codex task and tests
```

Traceability prevents hidden responsibility.

It also supports audit, governance and professional accountability.

---

# 29. Responsibility Compatibility

Responsibility changes must be reviewed for downstream impact.

Examples:

- changing Matter ownership may affect workflow, permission and product status;
- changing Agent responsibility may affect routing, service network and communication;
- changing Event responsibility may affect notification and opportunity discovery;
- changing AI review responsibility may affect product speed and professional risk;
- changing API contract responsibility may affect product integrations.

Responsibility is not just documentation.

It affects system behavior.

---

# 30. Responsibility Flow and MVP

The MVP shall preserve responsibility flow even if implementation is incomplete.

A minimal MVP should still include:

- principles that govern implementation;
- Core Objects with stable meaning;
- Business Responsibility for ownership and authorization;
- Execution Primitives for task and event coordination;
- Integration Contracts for product consumption;
- at least one product or workflow consumer that validates the flow.

An MVP that only builds product screens without Core responsibility flow is not a Core MVP.

An MVP that only builds database tables without responsibility ownership is not a Core MVP.

An MVP that only builds AI chat without governed responsibility is not a Core MVP.

---

# 31. Responsibility Flow Rules

The following rules are established by this chapter.

## Rule 1 — Responsibility SHALL flow from Principles to Products

Downstream layers consume upstream meaning.

## Rule 2 — Products SHALL NOT redefine Core meaning

Products may request Core extension.

They shall not create conflicting local semantics.

## Rule 3 — AI SHALL NOT own professional responsibility

AI assists under governance.

Human, business or domain owners retain accountability.

## Rule 4 — Business responsibility SHALL be explicit

Ownership, delegation, authorization and review authority shall not remain hidden.

## Rule 5 — Execution SHALL be observable

Meaningful action and change shall be represented through tasks, events, states or workflow contracts where appropriate.

## Rule 6 — Integration SHALL enforce contracts

Products and agents shall consume Core through explicit contracts.

## Rule 7 — Implementation SHALL preserve responsibility traceability

Codex and implementation tasks shall reference approved specifications and ownership.

## Rule 8 — MVP SHALL preserve responsibility flow

Partial implementation shall still respect responsibility direction.

---

# 32. Specification Output

This chapter produces the following specification output:

- official responsibility flow;
- meaning of define, provide, own, coordinate, connect and consume;
- responsibility ownership types;
- responsibility assignment rules;
- responsibility flow examples;
- responsibility violation patterns;
- responsibility review questions;
- responsibility decision matrix;
- responsibility traceability rule;
- responsibility compatibility rule;
- MVP responsibility rule.

These outputs shall guide later chapters and `core-specs/`.

---

# 33. Execution Mapping

This chapter does not directly define database tables or API endpoints.

It controls how execution assets must assign and preserve responsibility.

| Responsibility Flow | Execution Mapping |
|---------------------|-------------------|
| Principles define | review rules, governance checks, chapter rules |
| Core provides | domain specs, object specs, service specs |
| Business owns | ownership fields, permission rules, review authority |
| Execution coordinates | tasks, events, states, notifications, workflow contracts |
| Integration connects | APIs, event contracts, agent contracts, consumption contracts |
| Products consume | product modules, UI, workflow experience |

Implementation assets shall not be accepted if responsibility cannot be traced.

---

# 34. Relationship to core-specs/

This chapter governs how responsibility should appear in `core-specs/`.

Every relevant `core-specs/` file should identify responsibility.

Examples:

```text
core-specs/domains/matter.md
    Semantic owner: Matter Domain
    Business owner: configured by Matter Responsibility rules
    Execution owner: Task / Event / Workflow Contract

core-specs/events/matter-created.md
    Source responsibility: Matter Domain
    Execution responsibility: Event Domain
    Contract responsibility: Event Contract

core-specs/agents/classification-assistant.md
    Capability responsibility: Classification / Knowledge
    Review responsibility: Business Responsibility
    Contract responsibility: Agent Contract
```

No specification should leave responsibility implicit when professional or system risk exists.

---

# 35. Exclusions

This chapter shall not include:

- company job descriptions;
- team management roles;
- product roadmap ownership;
- sales responsibility matrix;
- operational SOPs;
- detailed workflow operation;
- detailed API endpoints;
- database schema;
- UI design;
- deployment architecture;
- implementation code.

This chapter defines architectural responsibility only.

---

# 36. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines official responsibility flow.
- It explains each responsibility verb.
- It distinguishes responsibility flow from architecture layers.
- It connects responsibility flow to Core Kernel, Value Flow and Ontology.
- It distinguishes semantic, business, execution, contract and experience responsibility.
- It preserves Core / Business / Execution / Integration / Product boundaries.
- It defines AI responsibility limits.
- It defines responsibility review questions and decision matrix.
- It supports `core-specs/` writing and Codex implementation.
- It supports MVP execution without becoming a management SOP.
- It supports Book 02 TOC v1.2.

---

# 37. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 11, defining responsibility flow across MarkOrbit Core architecture layers. |

---

**End of Chapter**
