# Book 02

# Appendix A — Glossary

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-A  
**Appendix Title:** Glossary  
**Appendix Type:** Canonical Reference  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-08 — Ontology and Domain Classification
- B02-CH-13 — Core Domain Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-CH-31 — Codex Implementation Roadmap
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Purpose

This appendix defines the canonical glossary for Book 02 — MarkOrbit Core Specification.

The glossary is not a casual word list.

It is a control document.

It stabilizes the language used by:

```text
manuscript chapters
appendices
indexes
core-specs/
Codex tasks
implementation documents
product books
AI Agent Contracts
Workplace specifications
integration contracts
```

The glossary prevents the same term from being redefined differently by products, Workplaces, AI agents, data models, Codex tasks or implementation teams.

Its core purpose is:

```text
Define terms before indexes.
Stabilize indexes before core-specs/.
Stabilize core-specs/ before Codex implementation.
```

---

# 2. Glossary Rules

## 2.1 Rule 1 — Canonical Meaning Prevails

If a term appears in this glossary, this appendix controls its canonical meaning for Book 02.

A product, service, AI agent, Codex task or implementation document may add context, but it may not redefine the term.

## 2.2 Rule 2 — Core Terms Are Not Product Labels

Core terms define shared professional meaning.

They must not be reduced to product screen names, menu labels, database table names or workflow UI labels.

## 2.3 Rule 3 — Implementation Names Must Follow Core Meaning

Implementation may use technical naming conventions, but technical names must preserve Core meaning.

A table, class, API route, queue topic or prompt may not become the source of Core meaning.

## 2.4 Rule 4 — Cross-Cutting Systems Must Be Declared

Capability and Business Responsibility are cross-cutting Core specification systems.

They may produce executable specs, objects, services, events and contracts.

They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.

## 2.5 Rule 5 — AI Terms Require Governance

AI-related terms must be interpreted through AI governance.

AI is a governed capability.

AI is not the Core.

AI is not above the Core.

AI is not a replacement for professional responsibility.

## 2.6 Rule 6 — Codex Implements, It Does Not Define

Codex-related terms must be interpreted as implementation terms.

Codex may generate implementation artifacts.

Codex may not invent Core architecture.

---

# 3. Canonical Architecture Terms

## 3.1 MarkOrbit

MarkOrbit is the architecture and product ecosystem for global brand and trademark service operations.

It includes Core, Workplace, product systems, AI capabilities, service network concepts and implementation artifacts.

MarkOrbit is broader than any single product.

## 3.2 Professional OS

Professional OS is the professional operating philosophy defined in Book 01.

It explains how professional service work creates value through:

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

Book 02 does not replace Professional OS.

Book 02 converts Professional OS into Core architecture.

## 3.3 Core

Core is the shared specification foundation of MarkOrbit.

It defines reusable professional meaning, execution primitives, governance rules and consumption contracts.

Core sits between Professional OS and all products, Workplaces, AI agents, `core-specs/`, Codex tasks and implementation.

Core is not:

```text
a product PRD
a user interface
a database schema
an AI prompt layer
a workflow app
a pricing system
a Codex task list
```

## 3.4 Core Kernel

Core Kernel is the stable inner structure of the Core.

It contains the minimum shared architecture required for MarkOrbit to operate consistently.

It includes:

```text
canonical models
domains
objects
services
events
contracts
execution primitives
AI governance
consumption rules
MVP boundaries
```

## 3.5 Canonical Model

A Canonical Model is a high-level architecture model that defines a stable kind of meaning across the Core.

Examples:

```text
Identity Model
Capability Model
Knowledge Model
Business Responsibility Model
Workplace Model
Network Model
```

A Canonical Model may influence multiple domains.

It is not always the same as a Core Domain.

## 3.6 Architecture Layer

An Architecture Layer is a position in the dependency structure of MarkOrbit.

Book 02 uses this dependency order:

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
Products / Workplace / Network
```

Later layers may reveal gaps, but they may not directly redefine earlier layers.

## 3.7 Responsibility Flow

Responsibility Flow defines how responsibility moves across principles, Core, business, execution, integration and products.

Canonical flow:

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

## 3.8 Professional Value Flow

Professional Value Flow is the professional sequence from reality to experience.

Canonical flow:

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

Book 02 converts this flow into Core objects, services, events, tasks, contracts and governance.

## 3.9 Core Boundary

Core Boundary defines what the Core owns and what it does not own.

Core owns shared meaning, execution primitives, governance and contracts.

Core does not own product UI, full Workplace experience, pricing policy, vendor adapters, production prompts or full marketplace execution.

## 3.10 Product

A Product is a consumer of Core that delivers user-facing functionality.

Examples:

```text
MarkReg
MarkOrbit Lite
Partner Center
Client Portal
Service Platform
Brand Asset Vault
Opportunity Engine
MGSN product surfaces
```

A Product may own experience.

A Product may not redefine Core meaning.

## 3.11 Workplace

Workplace is the professional operating environment where work is viewed, assigned, coordinated, reviewed and completed.

Workplace consumes Core execution primitives such as Matter, Task, Event, Workflow Contract, Review, Notification and Audit.

Workplace operates work.

Core provides the primitives.

## 3.12 Network

Network refers to the collaboration layer connecting partners, agents, service providers, routing, communication and service network structures.

The Core defines network-capable primitives.

Book 06 defines full network operation.

## 3.13 Implementation

Implementation is the software realization of approved Core specifications.

It may include code, schemas, services, APIs, tests, fixtures, event infrastructure and deployment artifacts.

Implementation does not define Core meaning.

## 3.14 Architecture Library

Architecture Library refers to the architecture governance and representation system used by MarkOrbit.

It includes:

```text
MAC — MarkOrbit Architecture Canon
MAG — MarkOrbit Architecture Governance
MAS — MarkOrbit Architecture Specifications
```

Book 02 conforms to these standards but defines the MarkOrbit Core itself.

---

# 4. Core Kernel Terms

## 4.1 Identity Model

Identity Model defines who or what an actor is.

It applies to human users, organizations, AI agents, external agents, service providers and system actors.

Identity is foundational for permission, responsibility, audit and AI governance.

## 4.2 Capability Model

Capability Model defines what can be performed and by whom or what actor.

Capability is cross-cutting.

It may apply to users, teams, AI agents, external agents, service providers, products and workflow roles.

Capability is not counted as an additional baseline Core Domain.

## 4.3 Knowledge Model

Knowledge Model defines how professional knowledge is sourced, validated, retrieved, consumed and governed.

It supports human work and AI-assisted work.

A knowledge base is not the whole Knowledge Model.

## 4.4 Business Responsibility Model

Business Responsibility Model defines accountability for work.

It answers who owns, reviews, approves, follows up, escalates or is accountable for an action or output.

Business Responsibility is cross-cutting.

It is not the same as pricing, commission or revenue attribution.

## 4.5 Workplace Model

Workplace Model defines how professional work is operated through tasks, queues, reviews, assignments, events and coordination views.

Workplace Model consumes Core primitives.

It does not redefine them.

## 4.6 Network Model

Network Model defines how partners, agents, service providers, routing and communication can be represented in Core.

Full network marketplace operation belongs to Book 06.

## 4.7 Domain

A Domain is a bounded area of shared professional meaning.

A Domain is not a product module, database schema, UI section, AI agent or team chart.

## 4.8 Core Domain

A Core Domain is a Domain owned by the MarkOrbit Core.

The canonical baseline Core Domain Map contains 26 domains.

## 4.9 Object

An Object is a stable unit of meaning.

In Book 02, Object usually means Core Object unless otherwise specified.

## 4.10 Core Object

A Core Object is professional meaning before data structure.

A Core Object defines identity, meaning, lifecycle, relationships, state, permissions, audit, services, events, AI usage and product consumption boundaries.

A Core Object is not merely a database table.

## 4.11 Service

A Service is a capability that performs work.

In Book 02, Service usually means Core Service unless otherwise specified.

## 4.12 Core Service

A Core Service is a governed capability that operates Core meaning.

It reads, validates, creates, updates, routes, reviews, recommends, transforms or publishes Core Objects and Events.

A Core Service is not a UI button, helper function or vendor wrapper.

## 4.13 Event

An Event is a meaningful change.

In Book 02, Event usually means Core Event unless otherwise specified.

## 4.14 Core Event

A Core Event is a meaningful change in Core state, professional execution, review requirement, AI output, routing decision, communication linkage or workflow progress.

A Core Event is not a log, UI click, activity feed row, queue message or analytics ping.

## 4.15 Execution Primitive

An Execution Primitive is a basic Core structure used to coordinate work.

Examples:

```text
Task
Event
State
Context
Workflow Contract
Review
Notification
Audit
```

## 4.16 Contract

A Contract is a governed specification boundary that controls how something may be consumed, invoked, exposed, exchanged or implemented.

Contracts protect the Core from uncontrolled use.

## 4.17 Core Contract

A Core Contract is a contract type owned or governed by the Core.

Examples:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
Integration Contract
Codex Task Contract
```

---

# 5. Domain Map Terms

## 5.1 Canonical Baseline Core Domain Map

The Canonical Baseline Core Domain Map is the 26-domain baseline used by Book 02.

It contains:

```text
6 Foundation Domains
6 Professional Domains
8 Business Execution Domains
6 Collaboration Network Domains
```

This baseline shall not be changed silently.

## 5.2 Foundation Domain

A Foundation Domain supports identity, authority, permission, policy or knowledge.

Foundation Domains answer:

```text
Who can act, under what authority, using what knowledge?
```

## 5.3 Professional Domain

A Professional Domain defines professional trademark and brand service meaning.

Professional Domains answer:

```text
What professional objects, rules and materials are being operated?
```

## 5.4 Business Execution Domain

A Business Execution Domain turns professional meaning into managed work.

Business Execution Domains answer:

```text
How does professional work become orders, matters, tasks, events and notifications?
```

## 5.5 Collaboration Network Domain

A Collaboration Network Domain supports partner, agent, service provider, routing, communication and service network concepts.

Collaboration Network Domains answer:

```text
How does the platform connect people, agents, providers and network services?
```

## 5.6 Identity

Identity defines who or what an actor is.

It supports users, organizations, AI agents, external agents, service providers and system actors.

## 5.7 Organization

Organization defines business entities, teams or structural ownership contexts.

It supports customers, agencies, partners, providers and internal teams.

## 5.8 User

User defines a human actor operating in MarkOrbit.

A User links identity, organization, permission, role, responsibility and audit.

## 5.9 Permission

Permission defines what an actor may read, create, update, approve, export or invoke.

Permission applies to objects, services, AI usage, documents, workflows and integrations.

## 5.10 Policy

Policy defines rules that influence decisions and constraints.

Policy may govern review, AI risk, data sharing, jurisdiction requirements, workflow behavior or business constraints.

## 5.11 Knowledge

Knowledge defines governed professional knowledge.

It includes knowledge sources, knowledge assets, jurisdiction requirements, classification references, document requirements and AI-authorized knowledge.

## 5.12 Brand

Brand defines a business or market-facing identity that trademark work protects.

Brand connects customer intention to trademark service execution.

## 5.13 Trademark

Trademark defines mark-related professional meaning.

It includes mark information, owner, jurisdiction, goods/services, status, filing lifecycle and registration lifecycle.

## 5.14 Jurisdiction

Jurisdiction defines country, region or office-specific professional context.

It includes official procedures, local rules, requirements and practice differences.

## 5.15 Classification

Classification defines goods and services classification meaning.

It includes Nice classes, local classification rules, goods/services terms, recommendations, validation and review.

## 5.16 Document

Document defines files and generated materials used in professional service execution.

Examples include POA, application materials, official documents, certificates, evidence files, translations and draft letters.

## 5.17 Evidence

Evidence defines proof materials and evidence packages.

Evidence may support use, ownership, sales, online presence, office action responses, oppositions or other professional claims.

## 5.18 Customer

Customer defines the person or organization receiving service.

Customer is a Core business execution actor, not merely a CRM record.

## 5.19 Matter

Matter defines a managed professional service case.

Matter connects customer, order, trademark, jurisdiction, workflow, tasks, documents, events and responsibility.

## 5.20 Order

Order defines a confirmed or pending service request.

Order connects intake, customer intention, service request and execution readiness.

## 5.21 Opportunity

Opportunity defines a potential business value or follow-up signal.

Opportunity may come from trademark lifecycle, portfolio gaps, jurisdiction expansion, renewal timing or AI-assisted discovery.

## 5.22 Workflow Contract

Workflow Contract defines allowed execution states, transitions, actors, review points and event rules.

Workflow Contract is Core governance, not a product screen flow.

## 5.23 Task

Task defines work to be performed.

Task may include assignment, due date, status, matter linkage, responsibility, review and event generation.

## 5.24 Event

Event is both a domain and an execution primitive.

As a domain, it governs event definitions, event source ownership, payload contracts, consumers and audit.

## 5.25 Notification

Notification defines baseline alerting and communication of required attention.

It may support task assignment, review requirement, deadline reminder or status change.

## 5.26 Partner

Partner defines a business partner participating in service, channel or cooperation relationships.

Partner is primarily reserved for later network development.

## 5.27 Agent

Agent defines a professional agent or law firm that can perform trademark-related work.

Agent is not the same as AI Agent unless explicitly stated.

## 5.28 Service Provider

Service Provider defines an entity providing services within or around the MarkOrbit ecosystem.

It may include legal service providers, translation providers, document providers, data providers, AI service providers or technology providers.

## 5.29 Service Network

Service Network defines network-level collaboration structure.

It supports membership, service exchange, participation and trust concepts.

Full Service Network operation belongs to Book 06.

## 5.30 Routing

Routing defines how work, matters, recommendations or service requests are directed to agents, providers, users or workflow paths.

Routing may use capability, jurisdiction, responsibility, availability and policy.

## 5.31 Communication

Communication defines linked professional communication.

It may include email, message, call, agent communication, client communication, matter communication and AI-assisted summaries.

---

# 6. Cross-Cutting Terms

## 6.1 Cross-Cutting Core Specification System

A Cross-Cutting Core Specification System governs multiple domains and may produce executable specs, objects, services, events and contracts.

It is not counted as an additional baseline Core Domain unless a later architecture release explicitly changes the domain map.

## 6.2 Capability

Capability is a cross-cutting Core specification system that defines what can be performed by whom or what actor.

Capability may apply to users, teams, AI agents, agents, service providers, products and workflow roles.

Capability is not counted as an additional baseline Core Domain.

## 6.3 Business Responsibility

Business Responsibility is a cross-cutting Core specification system that defines accountability for work.

It may apply to order ownership, matter ownership, task assignment, review responsibility, AI output approval, opportunity follow-up and routing approval.

Business Responsibility is not pricing, commission or revenue attribution.

## 6.4 AI Governance

AI Governance defines how AI capabilities and AI agents are authorized, constrained, reviewed and audited.

AI Governance requires Agent Contracts, authorized knowledge, risk level, human review rules and audit records.

## 6.5 Canonical Cross-Cutting Clarification

The following clarification is mandatory across Book 02:

```text
The baseline Core Domain Map contains 26 domains.
Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

---

# 7. Specification Terms

## 7.1 Specification

A Specification is a structured document that defines meaning, rules, boundaries, relationships, acceptance criteria and implementation constraints.

In Book 02, a Specification is not only descriptive.

It is intended to become executable through `core-specs/` and Codex tasks.

## 7.2 Domain Specification

A Domain Specification is the canonical specification document for one bounded Core Domain or explicitly declared cross-cutting specification system.

It defines domain purpose, scope, ownership, objects, services, events, contracts, AI usage, consumers, MVP depth and exclusions.

## 7.3 Object Specification

An Object Specification defines a Core Object’s professional meaning, identity, lifecycle, relationships, fields, permissions, events, services, AI usage and consumer boundaries.

## 7.4 Service Specification

A Service Specification defines a Core Service’s purpose, ownership, inputs, outputs, object effects, events, contracts, permissions, policies, AI usage, failure behavior and acceptance criteria.

## 7.5 Event Specification

An Event Specification defines a Core Event’s semantic meaning, source domain, trigger, payload contract, consumers, permissions, audit and retention rules.

## 7.6 Agent Contract

An Agent Contract defines what an AI Agent may do.

It includes purpose, identity, owning domain or system, allowed capabilities, prohibited capabilities, authorized knowledge, object access, service access, output types, risk level, human review, events, audit and failure behavior.

## 7.7 Consumption Contract

A Consumption Contract defines how a product, Workplace, AI agent, integration, reporting system or Codex task may consume Core.

It protects Core meaning from consumer redefinition.

## 7.8 Data Contract

A Data Contract defines what data may be read, exchanged, exported or exposed.

It includes fields, permissions, privacy, redaction, validation and audit rules.

## 7.9 API Contract

An API Contract defines a governed API surface.

It includes input contract, output contract, permission requirement, policy requirement, service relationship and event side effects.

## 7.10 Event Contract

An Event Contract defines how an event is published, consumed, retained, replayed and audited.

## 7.11 Workflow Contract Specification

A Workflow Contract Specification defines workflow states, transitions, actors, review points, events, notifications and failure behavior.

## 7.12 Acceptance Criteria

Acceptance Criteria define the conditions that must be met before a chapter, appendix, spec, task or implementation is accepted.

Acceptance Criteria are binding in Codex tasks and implementation review.

## 7.13 Exclusions

Exclusions define what is intentionally outside the scope of a chapter, appendix, spec or task.

Exclusions protect MVP boundaries and prevent scope creep.

---

# 8. Execution Terms

## 8.1 Task

Task is a Core execution primitive representing work to be performed.

A Task may have an owner, assignee, status, due date, related Matter, events, review rules and responsibility rules.

## 8.2 State

State is the current condition of an object, workflow, task, review or AI output.

State changes should be governed by services, workflows and events.

## 8.3 Context

Context is structured information required to perform or interpret an action.

AI agents, services, Workplaces and Codex tasks must use structured context rather than unbounded assumptions.

## 8.4 Workflow Contract

Workflow Contract is a Core contract that defines allowed workflow states, transitions, actors, responsibilities, review points, events and notifications.

It is not a UI flow.

## 8.5 Review

Review is a controlled evaluation step performed by an authorized human, role, system or process.

AI output may require review before becoming accepted professional output.

## 8.6 Audit

Audit is the record of who or what acted, when, on what object, under what authority, with what result.

AI usage, service execution, state changes and external data exchange may require audit.

## 8.7 Notification

Notification is a controlled alert or message indicating that attention, review, action or awareness is required.

Notification should be event- or workflow-driven.

## 8.8 Event Publishing

Event Publishing is the act of emitting a Core Event according to its Event Specification and Event Contract.

## 8.9 Event Subscription

Event Subscription is the governed consumption of a Core Event by an authorized consumer.

## 8.10 Order-to-Matter Conversion

Order-to-Matter Conversion is the governed transition from a service request or order into a managed professional Matter.

It should be controlled by service, workflow, event and responsibility rules.

## 8.11 Matter Execution

Matter Execution is the managed performance of professional service work through tasks, documents, events, reviews, communication and responsibility.

## 8.12 Responsibility Assignment

Responsibility Assignment records who is accountable for an object, action, review, AI output, task, matter or decision.

It belongs to the Business Responsibility cross-cutting system.

---

# 9. AI Governance Terms

## 9.1 AI Capability

AI Capability is a governed ability of AI to assist with a defined type of work.

Examples include classification recommendation, document drafting, evidence review, status summary, communication summary, routing suggestion and Codex implementation assistance.

## 9.2 AI Agent

AI Agent is a governed AI actor with identity, purpose, allowed capabilities, prohibited capabilities, authorized knowledge, object access, review rules and audit requirements.

An AI Agent is not merely a prompt.

## 9.3 AI Agent Identity

AI Agent Identity defines who or what the AI actor is within Core governance.

It supports permission, audit, review and accountability.

## 9.4 Authorized Knowledge

Authorized Knowledge is the knowledge an AI Agent is allowed to use.

It may include jurisdiction rules, classification references, document requirements, official data, internal policies or approved knowledge assets.

## 9.5 Structured Context

Structured Context is the controlled input context provided to an AI Agent or service.

It should include only authorized, relevant and bounded information.

## 9.6 AI Output

AI Output is any content, recommendation, summary, draft, classification, review note or implementation suggestion produced by an AI Agent.

AI Output must have status, source context, risk level and audit where required.

## 9.7 AI Recommendation

AI Recommendation is an AI Output that proposes an action, classification, routing, response, review result or decision support.

It is not final professional judgment unless accepted through required review.

## 9.8 AI Audit Record

AI Audit Record records AI usage, including agent identity, input context, knowledge used, output, risk level, review status, actor and timestamp.

## 9.9 Risk Level

Risk Level classifies the professional, legal, operational or business risk of AI output or service action.

Risk Level determines review, audit and permission requirements.

## 9.10 Human Review

Human Review is the required human evaluation of AI output or service action before acceptance, use or state mutation where risk requires it.

## 9.11 ReviewRequired

ReviewRequired is a status or event indicating that an output, recommendation, document, decision or action cannot proceed without review.

## 9.12 ReviewApproved

ReviewApproved indicates that an authorized reviewer has approved the output, recommendation or action.

## 9.13 ReviewRejected

ReviewRejected indicates that an authorized reviewer has rejected the output, recommendation or action.

## 9.14 Codex Implementation Agent

Codex Implementation Agent is the AI-assisted implementation actor that consumes approved specifications and produces implementation artifacts.

It may not define Core architecture.

---

# 10. Core Consumption Terms

## 10.1 Core Consumer

A Core Consumer is any product, Workplace, AI agent, internal service, external integration, reporting system or Codex task that consumes the Core.

## 10.2 Product Consumer

A Product Consumer is a product that uses Core to deliver user-facing functionality.

Examples include MarkReg and MarkOrbit Lite.

## 10.3 Workplace Consumer

A Workplace Consumer is an operating environment that consumes Core execution primitives to coordinate professional work.

## 10.4 AI Agent Consumer

An AI Agent Consumer is a governed AI actor that consumes Core context and produces controlled outputs.

## 10.5 Internal Service Consumer

An Internal Service Consumer is a platform service that consumes Core Objects, Services, Events or Contracts to perform internal operations.

## 10.6 External Integration Consumer

An External Integration Consumer is an external system or connector that exchanges data or actions with MarkOrbit through contracts.

## 10.7 Data / Reporting Consumer

A Data or Reporting Consumer uses Core data, events or audit records to produce dashboards, reports, metrics or analysis.

Reporting consumes Core.

Reporting does not define Core.

## 10.8 Codex Implementation Consumer

Codex Implementation Consumer is the implementation actor that consumes approved specifications and produces code, tests, scaffolds or documentation.

## 10.9 Read Boundary

Read Boundary defines what a consumer may see.

It includes readable objects, fields, events, knowledge, documents, AI outputs, permissions and redaction rules.

## 10.10 Write Boundary

Write Boundary defines what a consumer may change.

It includes writable objects, allowed state transitions, required services, emitted events, permissions, policies, review and audit.

## 10.11 Product Extension

Product Extension is a product-specific addition that extends experience or presentation without redefining Core meaning.

## 10.12 Prohibited Redefinition

Prohibited Redefinition is any consumer behavior that changes Core meaning without Core governance.

Examples include product-local definitions of Matter, Task, Event, AI Output or Trademark.

## 10.13 MVP Consumer

An MVP Consumer is a consumer that shapes the first executable Core kernel.

Canonical MVP Consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## 10.14 Partial Consumer

A Partial Consumer requires reserved or partial Core support but shall not pull full future product scope into MVP.

Canonical Partial Consumers:

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

## 10.15 Future Consumer

A Future Consumer may be supported by future Core extensions but does not define MVP scope.

Canonical Future Consumers:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

---

# 11. MVP and Roadmap Terms

## 11.1 MVP

MVP means Minimum Viable Product in ordinary product contexts.

In Book 02, MVP usually means Core MVP unless otherwise specified.

## 11.2 Core MVP

Core MVP is the first executable Core kernel.

It is not the full MarkOrbit platform.

## 11.3 Must Implement

Must Implement means a domain, object, service, event, contract or system is required for the first executable Core kernel.

## 11.4 Partial Implement

Partial Implement means the concept must be specified and partially implemented, but not fully expanded.

## 11.5 Reserved Boundary

Reserved Boundary means future architecture depends on the concept, but MVP should not build it deeply.

## 11.6 Deferred

Deferred means the concept or feature is intentionally excluded from the current MVP scope.

Deferred scope must remain deferred unless architecture review approves a change.

## 11.7 Codex Wave

Codex Wave is a staged implementation phase for Codex tasks.

Book 02 defines Waves 0–7.

## 11.8 Wave 0 — Repository and Spec Scaffold

Wave 0 creates repository structure, templates and scaffolds after appendices and indexes are ready.

## 11.9 Wave 1 — Foundation Core

Wave 1 implements foundation domains such as Identity, Organization, User, Permission, Knowledge and partial Policy/Capability.

## 11.10 Wave 2 — Professional Core

Wave 2 implements professional domains such as Brand, Trademark, Jurisdiction, Classification, Document and partial Evidence.

## 11.11 Wave 3 — Business Execution Core

Wave 3 implements Customer, Order, Matter, Workflow Contract, Task, Event and partial Business Responsibility/Notification.

## 11.12 Wave 4 — AI Governance and Review

Wave 4 implements AI governance, Agent Contracts, AI Output, review and audit foundations.

## 11.13 Wave 5 — Product Consumption Baseline

Wave 5 implements baseline consumption contracts for MarkReg, MarkOrbit Lite, Workplace and AI Agents.

## 11.14 Wave 6 — Growth Core Baseline

Wave 6 implements partial growth baseline such as Communication, Agent, Service Provider, Routing and Opportunity.

## 11.15 Wave 7 — Validation, Hardening and Release

Wave 7 validates, hardens and prepares release.

## 11.16 Execution Matrix

Execution Matrix converts domain priority into implementable rows containing specs, objects, services, events, contracts, AI usage, workflow usage, consumers, Codex tasks and acceptance criteria.

## 11.17 Codex Task

Codex Task is a controlled implementation instruction that tells Codex what to generate, from which source specs, under what constraints and with what acceptance criteria.

## 11.18 Fixture

Fixture is test or preview data used to validate specs, services, workflows or implementation behavior.

Fixtures must not be confused with production data.

## 11.19 Gate

Gate is a review checkpoint that must be passed before the next workstream proceeds.

Examples:

```text
Pre-Appendix Gate
Appendix Completion Gate
Pre-core-specs Gate
Pre-Codex Gate
Release Candidate Gate
```

## 11.20 Release

Release is an approved publication or implementation stage.

A release may be manuscript, appendix, spec scaffold, implementation or production oriented.

---

# 12. Status Terms

## 12.1 Publication Status

Publication Status describes the whole publication package.

Allowed values:

```text
draft
canonical_draft
second_canonical_draft_in_progress
reviewing
approved
released
deprecated
superseded
archived
```

## 12.2 Chapter Status

Chapter Status describes a manuscript chapter.

Allowed values:

```text
Draft
Reviewing
Approved
Revised
Deprecated
Superseded
Archived
```

## 12.3 Rewrite Status

Rewrite Status describes whether a document has been rewritten for the second canonical draft.

Allowed values:

```text
not_started
light_rewrite_required
controlled_rewrite_required
full_rewrite_required
rewritten_second_canonical_draft
accepted_unchanged
deferred
```

## 12.4 Appendix Status

Appendix Status describes appendix generation state.

Allowed values:

```text
pending
drafting
reviewing
approved
revised
deprecated
```

## 12.5 Spec Status

Spec Status describes `core-specs/` files.

Allowed values:

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

## 12.6 Codex Task Status

Codex Task Status describes implementation task state.

Allowed values:

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

## 12.7 Implementation Status

Implementation Status describes software implementation state.

Allowed values:

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

## 12.8 Release Status

Release Status describes release stage.

Allowed values:

```text
planning
manuscript_draft_completed
second_canonical_rewrite_in_progress
appendix_in_progress
spec_scaffold_ready
implementation_in_progress
release_candidate
released
archived
```

---

# 13. Terms Not To Confuse

## 13.1 Core ≠ Product

Core defines shared professional foundation.

Product delivers user-facing experience.

## 13.2 Domain ≠ Feature

Domain defines a bounded area of shared meaning.

Feature defines product functionality.

## 13.3 Domain ≠ Module

A module may implement part of a domain.

A domain is not a code module by default.

## 13.4 Domain ≠ Table

A table stores data.

A domain owns meaning.

## 13.5 Object ≠ Table

A Core Object defines professional meaning.

A database table stores implementation data.

## 13.6 Object ≠ DTO

A DTO transports data.

A Core Object defines meaning, lifecycle, relationships and governance.

## 13.7 Object ≠ UI Record

A UI record displays information.

A Core Object governs meaning.

## 13.8 Service ≠ Button

A button triggers interaction.

A Core Service operates governed Core meaning.

## 13.9 Service ≠ Helper Function

A helper function supports implementation.

A Core Service has ownership, contracts, permissions, events and acceptance criteria.

## 13.10 Service ≠ Vendor Wrapper

A vendor wrapper adapts an external API.

A Core Service defines platform meaning and responsibility.

## 13.11 Event ≠ Log

A log records technical or operational information.

A Core Event represents meaningful change.

## 13.12 Event ≠ UI Action

A UI action is user interaction.

A Core Event is semantic change.

## 13.13 Event ≠ Activity Feed

An activity feed displays activity.

A Core Event governs change semantics and downstream consumption.

## 13.14 Event ≠ Queue Message

A queue message transports work.

A Core Event defines meaningful change and payload contract.

## 13.15 Agent ≠ Prompt

An AI Agent is governed by identity, purpose, Agent Contract, knowledge, permissions, review and audit.

A prompt is only an implementation artifact.

## 13.16 Agent ≠ Model Provider

An AI model provider supplies model capability.

An AI Agent is a governed actor in MarkOrbit.

## 13.17 Consumption ≠ Redefinition

Consumption means using Core under contract.

It does not allow changing Core meaning.

## 13.18 MVP ≠ Full Platform

Core MVP is the first executable kernel.

It is not the full MarkOrbit platform, full marketplace, full analytics system or full AI autonomy.

## 13.19 Knowledge ≠ AI Output

Knowledge is governed and validated professional material.

AI Output is generated content that may require review.

## 13.20 Business Responsibility ≠ Pricing

Business Responsibility governs accountability.

Pricing governs commercial value.

---

# 14. Deprecated or Forbidden Meanings

The following meanings are deprecated or forbidden in Book 02.

```text
Core as product PRD
Core as database schema
Core as UI design
Core as prompt library
Core as Codex task list
Domain as product module
Object as table only
Service as helper function only
Event as log only
AI as autonomous professional authority
Codex as architecture owner
MVP as full MarkOrbit platform
MGSN full marketplace as Core MVP
Capability as hidden 27th domain
Business Responsibility as hidden 28th domain
```

If any document uses these meanings, it must be revised.

---

# 15. Relationship to Appendices B–H

This glossary is the anchor for the remaining appendices.

## 15.1 Appendix B — Core Domain Index

Appendix B must use the domain terms defined here and preserve the 26-domain baseline.

## 15.2 Appendix C — Core Object Index

Appendix C must use the object terms defined here and must not confuse objects with database tables.

## 15.3 Appendix D — Core Service Index

Appendix D must use the service terms defined here and must not confuse services with helper functions or UI actions.

## 15.4 Appendix E — Event Index

Appendix E must use the event terms defined here and must not confuse events with logs or activity feeds.

## 15.5 Appendix F — API Index

Appendix F must use the contract and consumption terms defined here.

## 15.6 Appendix G — Agent Index

Appendix G must use AI governance terms defined here.

## 15.7 Appendix H — Codex Task Index

Appendix H must use Codex, MVP, wave, execution matrix and acceptance terms defined here.

---

# 16. Acceptance Criteria

This appendix is accepted only if it satisfies the following criteria.

```text
[ ] It defines canonical architecture terms.
[ ] It defines Core Kernel terms.
[ ] It defines all 26 baseline Core Domain terms.
[ ] It states the 26-domain baseline clearly.
[ ] It defines Capability as a cross-cutting Core specification system.
[ ] It defines Business Responsibility as a cross-cutting Core specification system.
[ ] It defines specification terms.
[ ] It defines execution terms.
[ ] It defines AI governance terms.
[ ] It defines Core consumption terms.
[ ] It defines MVP and roadmap terms.
[ ] It defines status vocabularies by layer.
[ ] It includes terms not to confuse.
[ ] It includes deprecated or forbidden meanings.
[ ] It prepares Appendix B–H generation.
[ ] It prevents product, AI, data, Codex and implementation layers from redefining Core meaning.
```

---

# 17. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial second-canonical-draft glossary. Establishes canonical terminology, 26-domain baseline, cross-cutting systems, AI governance vocabulary, consumer classification, MVP terms and status vocabulary. |

---

**End of Appendix**
