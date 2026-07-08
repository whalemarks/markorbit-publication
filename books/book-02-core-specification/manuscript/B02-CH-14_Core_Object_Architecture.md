# Book 02

# 14 — Core Object Architecture

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-14

**Chapter Title:** Core Object Architecture

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

This chapter defines the Core Object Architecture of MarkOrbit.

Chapter 13 defined Core Domains as executable responsibility boundaries.

This chapter defines Core Objects as the stable representations owned by those domains.

Domains own responsibility.

Objects represent the things that responsibility applies to.

For example:

- Trademark Domain owns trademark lifecycle meaning.
- Trademark Object represents a specific trademark.
- Matter Domain owns professional service matter execution meaning.
- Matter Object represents a specific matter.
- Agent Domain owns professional agent identity and capability meaning.
- Agent Object represents a specific agent.

Core Objects are central because professional work cannot become executable unless the system has stable things to reference, relate, audit, update, consume and reason over.

If objects are not defined clearly, products will create their own local records.

AI agents will operate on inconsistent context.

Events will lack stable sources.

Services will not know what they act on.

APIs will expose data without shared meaning.

This chapter prevents those failures by defining how Core Objects are identified, owned, structured, governed and consumed.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit define and govern Core Objects?

The answer is:

> A Core Object is a persistent, referable, traceable, auditable and product-consumable representation of stable professional, system, business execution or collaboration meaning owned by a Core Domain.

A Core Object is not merely a database row.

A Core Object is not a UI component.

A Core Object is not a product-specific record.

A Core Object is a shared architectural representation.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Core Object definition;
- object responsibility;
- object ownership;
- object identity;
- object lifecycle;
- object state;
- object relationships;
- object auditability;
- object persistence;
- object versioning;
- object governance;
- object relation to domains, services, events, contracts, AI and products;
- object specification structure;
- object inclusion and exclusion rules;
- object review questions;
- object anti-patterns;
- object mapping to `core-specs/objects/`;
- object mapping to Codex implementation tasks.

## 3.2 Out of Scope

This chapter does not define:

- complete field schemas for all Core Objects;
- database physical design;
- ORM implementation;
- API endpoint details;
- product UI;
- product-specific object views;
- full workflow operation;
- AI prompt templates;
- deployment architecture;
- vendor-specific implementation.

Detailed Core Object specifications belong in:

```text
core-specs/objects/
```

---

# 4. Core Object Definition

A Core Object is:

> a persistent, referable, traceable, auditable and product-consumable representation of stable professional, system, business execution or collaboration meaning owned by a Core Domain.

This definition contains seven parts.

## 4.1 Persistent

A Core Object must have durable representation.

It should not exist only as temporary screen state or transient prompt context.

## 4.2 Referable

A Core Object must be identifiable and referenceable by services, events, contracts, products and AI agents.

## 4.3 Traceable

A Core Object should support traceability across lifecycle, relationships, events and actions.

## 4.4 Auditable

A Core Object should support audit where professional, business, permission or legal risk exists.

## 4.5 Product-Consumable

A Core Object should be consumable by one or more products through contracts.

## 4.6 Stable Meaning

A Core Object represents meaning that should remain stable across products.

## 4.7 Domain-Owned

A Core Object must have one primary owning Core Domain.

---

# 5. What a Core Object Is Not

A Core Object is not:

- a product page;
- a product card;
- a form section;
- a dashboard widget;
- a database table alone;
- a temporary API response;
- a local UI state;
- a prompt variable;
- a workflow step;
- a report row;
- an imported raw row without normalization;
- a vendor-specific data structure.

For example:

- `Trademark` may be a Core Object.
- `Trademark Search Result Card` is a product UI object.
- `Matter` may be a Core Object.
- `Matter Dashboard Row` is a product or Workplace view.
- `Agent` may be a Core Object.
- `Agent Recommendation Tile` is product experience.
- `Document` may be a Core Object.
- `POA Upload Form` is product workflow UI.

---

# 6. Object Architecture Position

Core Objects sit inside the Core Kernel.

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

Domains define responsibility.

Objects represent stable things inside domains.

Services act on objects.

Events make object changes observable.

Contracts expose objects safely.

Products consume objects without redefining them.

AI agents use objects as governed context.

This position makes Core Objects the main bridge between domain meaning and executable data.

---

# 7. Object Responsibility

Every Core Object must answer:

> What stable thing does this object represent?

Examples:

- Trademark represents a trademark record, lifecycle and professional status context.
- Brand represents a brand identity and asset portfolio context.
- Matter represents a professional service matter.
- Order represents a service purchase and conversion context.
- Opportunity represents a business opportunity signal and follow-up context.
- Agent represents a professional agent and its collaboration capability.
- Event represents a meaningful change in the system.
- Task represents an assigned unit of responsibility.
- Document represents a professional document and its metadata.
- Evidence represents supporting material for use, claim or professional conclusion.

An object without stable representational responsibility should not be a Core Object.

---

# 8. Object Ownership

Every Core Object shall have one primary owning Core Domain.

Ownership means semantic responsibility.

It does not mean only one domain may reference the object.

For example:

```text
Trademark Object
    Primary owner: Trademark Domain
    Referenced by: Matter, Order, Opportunity, Document, Evidence

Agent Object
    Primary owner: Agent Domain
    Referenced by: Matter, Routing, Communication, Service Network

Document Object
    Primary owner: Document Domain
    Referenced by: Matter, Order, Evidence, Communication
```

A referenced object remains owned by its primary domain.

A consuming domain may not redefine it.

---

# 9. Object Categories

Book 02 recognizes six practical Core Object categories.

```text
1. Identity Objects
2. Professional Objects
3. Business Execution Objects
4. Execution Primitive Objects
5. Collaboration Network Objects
6. Contract and Governance Objects
```

These categories are not the same as domain categories.

They classify object behavior and usage.

---

# 10. Identity Objects

Identity Objects represent actors, organizations and identity-linked entities.

Examples include:

- Identity;
- Person;
- Organization;
- User;
- Customer;
- Partner;
- Agent;
- Service Provider;
- Contact Point;
- Role;
- Account.

Identity Objects support:

- responsibility;
- permission;
- communication;
- audit;
- network collaboration;
- customer relationship;
- agent and provider management.

Identity Objects must preserve the Identity Model defined in Chapter 12.

---

# 11. Professional Objects

Professional Objects represent the subject matter of global brand and trademark service work.

Examples include:

- Brand;
- Brand Asset;
- Trademark;
- Trademark Application;
- Trademark Registration;
- Jurisdiction;
- Trademark Office;
- Classification Item;
- Goods/Services Item;
- Document;
- Evidence;
- Deadline;
- Office Action.

Professional Objects support:

- professional memory;
- knowledge application;
- filing logic;
- lifecycle tracking;
- legal and procedural context;
- client advice;
- AI-assisted analysis.

Professional Objects distinguish MarkOrbit from generic SaaS systems.

---

# 12. Business Execution Objects

Business Execution Objects represent commercial and professional execution.

Examples include:

- Customer Profile;
- Matter;
- Matter Responsibility;
- Order;
- Quote;
- Payment Record;
- Opportunity;
- Opportunity Signal;
- Opportunity Score;
- Responsibility Assignment;
- Review Record.

Business Execution Objects support:

- order-to-matter conversion;
- customer ownership;
- opportunity follow-up;
- business responsibility;
- review authority;
- professional accountability.

These objects are not merely CRM records.

They connect business execution to professional work.

---

# 13. Execution Primitive Objects

Execution Primitive Objects represent work movement, state and coordination.

Examples include:

- Task;
- Event;
- State;
- Transition;
- Context;
- Notification;
- Workflow Contract;
- Workflow Step;
- Assignment;
- Timeline Entry.

Execution Primitive Objects support:

- traceable action;
- lifecycle visibility;
- task responsibility;
- workflow interoperability;
- notification;
- audit;
- automation;
- AI monitoring.

The Core defines these objects and contracts.

Workplace operates workflow execution.

---

# 14. Collaboration Network Objects

Collaboration Network Objects represent multi-party professional collaboration.

Examples include:

- Partner;
- Agent;
- Service Provider;
- Service Network;
- Service Coverage;
- Jurisdiction Coverage;
- Agent Capability;
- Provider Capability;
- Route;
- Routing Decision;
- Communication;
- Conversation;
- Message;
- Thread;
- Trust Record;
- Reliability Record.

These objects support MarkOrbit’s global collaboration model.

Book 02 defines their Core foundation.

Book 06 operationalizes them through MGSN.

---

# 15. Contract and Governance Objects

Contract and Governance Objects represent rules for safe consumption, permission, policy and interoperability.

Examples include:

- Permission Rule;
- Policy Rule;
- Consumption Contract;
- API Contract;
- Event Contract;
- Agent Contract;
- Workflow Contract;
- Data Contract;
- Review Requirement;
- Audit Record;
- Knowledge Source Authority.

These objects support:

- governance;
- integration;
- versioning;
- AI control;
- permission enforcement;
- product consumption;
- auditability.

They should not become informal configuration records without architectural meaning.

---

# 16. Core Object Identity

Every Core Object must have identity.

Object identity answers:

> How does the system recognize this object as itself over time?

Object identity may include:

- stable object ID;
- external reference ID;
- source system ID;
- jurisdiction-specific ID;
- owner identity;
- normalized name;
- version identifier;
- relationship to other identities.

Examples:

- a U.S. trademark may have a serial number and registration number;
- a Chinese trademark may have an application number;
- a customer may have organization identity and contact identities;
- an agent may have firm identity, attorney contacts and jurisdiction coverage;
- a document may have file identity, document type and matter relationship.

Identity should not be treated as only an internal database primary key.

A Core Object may need both internal and external identity.

---

# 17. Core Object Lifecycle

Every important Core Object should define lifecycle.

Lifecycle answers:

> What states may this object move through over time?

Examples:

```text
Matter
    Draft
    Active
    Waiting for Client
    Waiting for Agent
    Under Review
    Completed
    Closed
    Archived

Order
    Created
    Quoted
    Confirmed
    Paid
    Converted to Matter
    Cancelled
    Refunded

Document
    Requested
    Uploaded
    Verified
    Rejected
    Submitted
    Archived

Task
    Created
    Assigned
    In Progress
    Blocked
    Completed
    Cancelled
```

Lifecycle does not mean product workflow.

Lifecycle is the object’s state structure.

Product workflows may display or operate lifecycle differently.

---

# 18. Object State

Object state represents the current condition of a Core Object.

State should be:

- defined by the owning domain;
- controlled through services or governed transitions;
- observable through events where meaningful;
- auditable where risk exists;
- consumable through contracts.

State should not be modified informally by products.

For example:

- Matter status should change through Matter Service or Workflow Contract.
- Trademark status should be updated through Trademark status normalization or verified update.
- Task status should change through Task Service.
- Document status should change through Document Service or review process.

Informal state mutation creates fragmentation and weak auditability.

---

# 19. Object Relationships

Core Objects rarely stand alone.

Relationships define how objects connect.

Examples:

```text
Customer owns Brand
Brand includes Trademark
Trademark belongs to Jurisdiction
Matter references Customer and Trademark
Order converts into Matter
Matter contains Document and Task
Task produces Event
Agent is assigned to Matter
Communication relates to Matter and Agent
Opportunity references Customer, Brand and Trademark
Routing Decision references Agent and Service Provider
```

Object relationships should be explicit.

Hidden relationships create operational risk.

Relationship types may include:

- ownership;
- assignment;
- reference;
- derivation;
- conversion;
- dependency;
- participation;
- communication;
- evidence support;
- responsibility;
- audit link.

---

# 20. Object Source and Provenance

Core Objects should record source and provenance where relevant.

Provenance answers:

> Where did this object or fact come from?

Examples of sources:

- manual user input;
- official trademark database;
- imported dataset;
- email;
- uploaded document;
- foreign agent reply;
- AI extraction;
- integration;
- historical system migration;
- user correction.

Source quality affects trust.

A record imported from an official database may have different reliability from an AI-extracted fact.

A human-reviewed correction may have different authority from raw import.

Provenance is especially important for trademark data, documents, evidence, deadlines, AI extraction and agent capability records.

---

# 21. Object Auditability

Core Objects should support audit where professional or business risk exists.

Audit may include:

- who created the object;
- who updated it;
- when it changed;
- what changed;
- why it changed;
- source of change;
- related event;
- related task;
- related AI output;
- review record;
- approval record.

Not every object requires heavy audit.

But objects affecting legal rights, deadlines, client advice, payments, permission, routing or AI output require stronger audit.

Auditability supports professional responsibility.

---

# 22. Object Versioning

Some Core Objects require versioning.

Versioning is needed when historical meaning must be preserved.

Examples:

- Document version;
- Evidence package version;
- Knowledge rule version;
- Classification recommendation version;
- AI-generated draft version;
- Contract version;
- Policy version;
- Workflow Contract version;
- Trademark status history;
- Matter responsibility history.

Versioning prevents current state from overwriting professional history.

A versioned object should define:

- version identity;
- version source;
- effective time;
- author or generator;
- review status;
- superseded version;
- rollback or reference rules.

---

# 23. Object Normalization

Many Core Objects may be imported from external or messy sources.

Normalization turns source records into Core Objects.

Examples:

- trademark office data into Trademark;
- email sender into Contact Point or Communication;
- agent spreadsheet into Agent and Agent Capability;
- document file into Document with type and lifecycle;
- goods/services text into Classification Item;
- client request into Opportunity or Order.

Normalization must preserve source provenance.

Normalized objects should not hide uncertainty.

If a record is unverified, inferred or incomplete, the object should reflect that.

---

# 24. Object Quality

Object quality describes whether a Core Object is reliable enough for professional use.

Quality dimensions may include:

- completeness;
- source authority;
- verification status;
- freshness;
- consistency;
- duplication risk;
- conflict status;
- human review status;
- AI extraction confidence;
- external reference match.

Object quality affects downstream services and AI.

For example:

- routing should not rely on stale agent capability data without warning;
- evidence review should distinguish verified documents from unreviewed uploads;
- opportunity scoring should know whether trademark data is current;
- AI advice should know whether facts are confirmed.

---

# 25. Object Permissions

Object access and mutation should be governed.

Permission questions include:

- who can view this object;
- who can create it;
- who can update it;
- who can delete or archive it;
- who can link it to another object;
- who can approve it;
- who can expose it to AI;
- who can share it with external parties.

Permission rules may depend on:

- identity;
- organization;
- role;
- matter responsibility;
- customer ownership;
- policy;
- jurisdiction;
- risk level;
- product context.

Object permission is not only UI access.

It is Core governance.

---

# 26. Object and Services

Core Services act on Core Objects.

A service should declare:

- input objects;
- output objects;
- created objects;
- updated objects;
- referenced objects;
- permission checks;
- events emitted;
- failure behavior;
- audit behavior.

Examples:

```text
Order-to-Matter Conversion Service
    Input: Order
    Output: Matter
    Events: OrderConvertedToMatter, MatterCreated

Classification Recommendation Service
    Input: Brand, Trademark, Goods/Services Text, Jurisdiction
    Output: Recommendation Result
    Events: ClassificationRecommendationGenerated

Agent Matching Service
    Input: Matter, Jurisdiction, Service Type
    Output: Agent Match Result / Routing Decision
    Events: RoutingDecisionMade
```

Services should not mutate objects informally.

Object state changes should be explicit.

---

# 27. Object and Events

Events make object changes observable.

An object lifecycle change, responsibility change, status change or important relationship change may emit an event.

Examples:

- `TrademarkStatusChanged`;
- `MatterCreated`;
- `MatterOwnerAssigned`;
- `OrderConvertedToMatter`;
- `DocumentUploaded`;
- `DocumentVerified`;
- `EvidencePackageCreated`;
- `TaskAssigned`;
- `TaskCompleted`;
- `AgentCapabilityUpdated`;
- `RoutingDecisionMade`;
- `CommunicationLinkedToMatter`.

Events should reference object identity.

Events should not duplicate full object meaning unnecessarily.

Events should make change visible and consumable.

---

# 28. Object and Contracts

Core Objects are consumed through contracts.

Contracts may define:

- object schema;
- allowed fields;
- read permissions;
- write permissions;
- API input/output;
- event payload references;
- versioning;
- error behavior;
- privacy and sensitivity rules;
- product consumption limits.

Products should not directly consume database tables.

They should consume Core Objects through contracts.

AI agents should not access raw objects without governance.

They should operate under Agent Contracts and permission rules.

---

# 29. Object and AI Capability

AI Capability uses Core Objects as context.

Examples:

- Classification Assistant uses Brand, Trademark, Jurisdiction and Classification Items.
- Document Assistant uses Document, Matter, Jurisdiction and Knowledge.
- Evidence Assistant uses Evidence, Trademark, Goods/Services and Knowledge.
- Routing Assistant uses Matter, Agent, Service Provider and Service Network.
- Opportunity Assistant uses Customer, Brand, Trademark and Event history.

AI usage should declare:

- which objects it may access;
- which fields are allowed;
- which knowledge sources are required;
- whether output may update objects;
- whether human review is required;
- which events are recorded;
- what audit trace is stored.

AI shall not silently create or modify critical Core Objects without governed service or human review.

---

# 30. Object and Product Consumption

Products consume Core Objects through views, workflows, dashboards, forms and AI interactions.

A product may:

- display a Core Object;
- present a simplified view;
- request service actions on an object;
- subscribe to object events;
- attach product-specific metadata;
- create product-specific view models.

A product shall not:

- redefine Core Object meaning;
- bypass Core permissions;
- mutate Core state directly without service or contract;
- create conflicting duplicate objects;
- hide important object changes from Core events;
- treat product-specific view models as Core Objects.

For example:

Lite may display a simplified Trademark card.

MarkReg may show full matter-linked trademark details.

Brand Asset Vault may show portfolio-level trademark status.

All consume the same Core Trademark meaning.

---

# 31. Object Specification Structure

Every detailed Core Object specification shall follow a standard structure.

```text
# Object Name

1. Object Purpose
2. Owning Domain
3. Ontology Layer
4. Object Category
5. Canonical Model Dependencies
6. Core Meaning
7. In Scope
8. Out of Scope
9. Identity Rules
10. Lifecycle / State Rules
11. Relationship Rules
12. Source and Provenance
13. Quality Rules
14. Permission Rules
15. Audit Rules
16. Versioning Rules
17. Related Services
18. Events Published or Referenced
19. Contracts
20. AI Usage
21. Product Consumers
22. Persistence Notes
23. MVP Priority
24. Acceptance Criteria
25. Revision Notes
```

This structure belongs to:

```text
core-specs/objects/
```

---

# 32. Object Inclusion Test

A concept may become a Core Object only if it satisfies most of the following conditions:

1. It represents stable professional, system, business execution or collaboration meaning.
2. It belongs to a Core Domain.
3. It needs durable persistence or reference.
4. It may be used by more than one product or service.
5. It participates in lifecycle, state, relationship or audit.
6. It may be acted on by Core Services.
7. It may produce or be referenced by Events.
8. It requires permission, policy or governance.
9. It may be used as AI context.
10. Fragmentation would occur if products created separate versions.

If a concept fails this test, it may be a product view, temporary record, implementation structure or prompt variable rather than a Core Object.

---

# 33. Object Exclusion Test

A concept shall be excluded from Core Object status if it is primarily:

- a UI card;
- a form section;
- a dashboard row;
- a product-specific filter;
- a temporary chat variable;
- a prompt placeholder;
- an API response wrapper;
- a database join table without semantic meaning;
- a report export row;
- a one-product-only display object;
- a cache object;
- a vendor-specific payload.

Excluded objects may exist in implementation or products.

They should not be promoted to Core Object status.

---

# 34. Object Naming Rules

Core Object names shall be stable and meaning-oriented.

## Rule 1 — Use professional or system meaning

Correct:

```text
Trademark
Matter
Order
Document
Task
Agent
Routing Decision
Communication
```

Incorrect:

```text
TrademarkCard
MatterRow
OrderWidget
DocumentUploadModal
TaskPanel
```

## Rule 2 — Avoid database-only names

Correct:

```text
Agent Capability
```

Incorrect:

```text
agent_capability_rel
```

## Rule 3 — Avoid prompt or UI names

Correct:

```text
Classification Recommendation
```

Incorrect:

```text
AIClassSuggestOutputBox
```

Object names should remain meaningful across products and technologies.

---

# 35. Object Boundary Rules

Every Core Object shall define boundaries.

A boundary statement should answer:

- what the object represents;
- what it does not represent;
- which domain owns it;
- which domains may reference it;
- which services may act on it;
- which events may change it;
- which products consume it;
- which AI capabilities may use it.

Examples:

## 35.1 Trademark vs Brand

Trademark represents legal trademark protection context.

Brand represents brand identity and brand asset context.

They are related but not the same.

## 35.2 Document vs Evidence

Document represents a professional file or procedural document.

Evidence represents material used to support a claim, use, argument or professional conclusion.

Evidence may reference Document.

Document does not absorb Evidence.

## 35.3 Agent vs Service Provider

Agent represents a professional representative or foreign associate role.

Service Provider represents a broader external provider of services.

One organization may be both.

The objects should be linked through Identity and Network Models, not collapsed.

## 35.4 Task vs Workflow Contract

Task represents an assigned unit of work.

Workflow Contract defines allowed states, steps and transitions.

Tasks may be created under Workflow Contracts.

They are not the same object.

---

# 36. Object Extension Rule

New Core Objects may be added only through governed extension.

An object extension proposal shall include:

- proposed object name;
- owning domain;
- object category;
- Canonical Model dependencies;
- reason existing objects are insufficient;
- identity rules;
- lifecycle or state rules;
- relationships;
- services;
- events;
- contracts;
- AI usage;
- product consumers;
- persistence notes;
- MVP relevance;
- acceptance criteria.

No product may add a Core Object directly.

A product may request Core Object review.

---

# 37. Object Versioning Rule

Core Object semantic changes must be versioned when they affect:

- object identity;
- lifecycle;
- state meanings;
- relationship rules;
- service behavior;
- event semantics;
- contracts;
- permissions;
- AI usage;
- product consumption.

Minor editorial clarifications do not require version change.

Semantic changes do.

---

# 38. Object Review Questions

When reviewing a Core Object, reviewers shall ask:

1. What stable thing does this object represent?
2. Which Core Domain owns it?
3. Which ontology layer and object category does it belong to?
4. Which Canonical Models does it depend on?
5. What is its identity rule?
6. What lifecycle or state does it have?
7. What objects does it relate to?
8. What source or provenance must be recorded?
9. What quality rules apply?
10. What permissions apply?
11. What audit rules apply?
12. What services act on it?
13. What events reference or change it?
14. What contracts expose it?
15. What AI capabilities may use it?
16. Which products consume it?
17. Would products fragment if this object were not Core?
18. Can Codex implement it from approved specifications?

---

# 39. Object Anti-Patterns

## 39.1 Table-First Object

A database table is created first and becomes the object definition.

Correction:

```text
Object meaning comes first.
Tables implement object specifications.
```

## 39.2 UI-First Object

A product card or dashboard row becomes the object.

Correction:

```text
Product views display Core Objects.
They do not define them.
```

## 39.3 Prompt-First Object

AI prompt variables define object meaning.

Correction:

```text
AI consumes Core Objects under governance.
Prompts do not define objects.
```

## 39.4 Duplicate Product Objects

Each product creates its own version of Customer, Trademark, Agent or Matter.

Correction:

```text
Shared meaning belongs to Core.
Products may create product-specific views.
```

## 39.5 Overloaded Object

One object absorbs unrelated meanings.

Example:

```text
Matter stores customer, order, document, evidence, agent, communication and task meanings without references.
```

Correction:

```text
Matter references related objects.
It does not own all meanings.
```

## 39.6 Untraceable Object

An object has no source, audit, lifecycle or relationship information despite professional importance.

Correction:

```text
Important Core Objects require source, lifecycle, relationships and audit rules.
```

---

# 40. Core Object Inventory Baseline

The initial Core Object inventory shall be derived from the Core Domain Map.

A baseline inventory includes, but is not limited to:

```text
Identity Objects
    Identity
    Person
    Organization
    User
    Role
    Contact Point

Professional Objects
    Brand
    Brand Asset
    Trademark
    Trademark Application
    Trademark Registration
    Jurisdiction
    Trademark Office
    Classification Item
    Goods/Services Item
    Document
    Evidence
    Deadline
    Office Action

Business Execution Objects
    Customer
    Matter
    Matter Responsibility
    Order
    Quote
    Payment Record
    Opportunity
    Opportunity Signal
    Review Record

Execution Primitive Objects
    Workflow Contract
    Task
    Event
    State
    Transition
    Context
    Notification
    Timeline Entry

Collaboration Network Objects
    Partner
    Agent
    Agent Capability
    Service Provider
    Provider Capability
    Service Network
    Route
    Routing Decision
    Communication
    Conversation
    Message
    Trust Record
    Reliability Record

Contract and Governance Objects
    Permission Rule
    Policy Rule
    API Contract
    Event Contract
    Agent Contract
    Data Contract
    Consumption Contract
    Audit Record
```

The full object inventory shall be maintained in:

```text
Appendix C — Core Object Index
core-specs/objects/
```

---

# 41. Object and MVP Priority

Objects should be implemented according to Core MVP priorities.

A minimal MVP object set may include:

```text
Phase 1 — Foundation Core
    Identity
    Organization
    User
    Role
    Permission Rule
    Knowledge Source

Phase 2 — Professional Core
    Brand
    Trademark
    Jurisdiction
    Classification Item
    Document

Phase 3 — Business Execution Core
    Customer
    Matter
    Order
    Workflow Contract
    Task
    Event

Phase 4 — Growth Core
    Opportunity
    Notification
    Policy Rule
    Evidence
    Agent
    Routing Decision

Phase 5 — Network Core
    Partner
    Service Provider
    Service Network
    Communication
    Trust Record
```

The MVP should prioritize objects that create an executable professional chain.

It should not implement attractive UI objects before Core Objects.

---

# 42. Object and Codex

Codex tasks shall implement objects from approved object specifications.

A Codex object task should include:

- object name;
- owning domain;
- object category;
- Canonical Model dependencies;
- identity rules;
- lifecycle and state rules;
- relationship rules;
- permission rules;
- audit rules;
- services that act on the object;
- events involving the object;
- API or contract exposure;
- AI usage restrictions;
- tests;
- acceptance criteria;
- prohibited overreach.

Codex shall not invent Core Object meaning from product prompts.

---

# 43. Core Object Rules

The following rules are established by this chapter.

## Rule 1 — Core Objects SHALL have one primary owning domain

Object ownership must be explicit.

## Rule 2 — Core Objects SHALL represent stable meaning

A product view, UI card or temporary variable shall not become a Core Object.

## Rule 3 — Core Objects SHALL be referable

Core Objects must support stable identity.

## Rule 4 — Core Objects SHALL define lifecycle or state where relevant

Important objects should not have ambiguous states.

## Rule 5 — Core Object relationships SHALL be explicit

Hidden relationships create operational and AI risk.

## Rule 6 — Core Objects SHALL preserve source and provenance where needed

Imported, extracted or inferred objects must record source quality.

## Rule 7 — Core Objects SHALL support audit where professional risk exists

Legal, business, permission and AI-sensitive objects require audit rules.

## Rule 8 — Core Objects SHALL be consumed through contracts

Products and AI agents shall not consume objects informally.

## Rule 9 — AI SHALL not redefine Core Objects

AI may use objects as governed context.

It shall not silently create or mutate critical objects without governance.

## Rule 10 — Core Object changes SHALL be governed and versioned

Semantic changes require review and versioning.

---

# 44. Specification Output

This chapter produces the following specification output:

- Core Object definition;
- Core Object exclusions;
- object responsibility model;
- object ownership rules;
- object categories;
- object identity rules;
- lifecycle and state rules;
- relationship rules;
- source and provenance rules;
- object quality rules;
- permission rules;
- audit rules;
- versioning rules;
- object relationship to services, events, contracts, AI and products;
- object specification structure;
- inclusion and exclusion tests;
- naming and boundary rules;
- extension and versioning rules;
- review questions;
- anti-patterns;
- baseline Core Object inventory;
- MVP object priority;
- Codex implementation rules.

These outputs guide Chapters 15 through 17 and Part III.

---

# 45. Execution Mapping

This chapter does not directly define database tables or API endpoints.

It controls how Core Objects become executable assets.

| Object Architecture Element | Execution Mapping |
|-----------------------------|------------------|
| Object Meaning | object spec and acceptance criteria |
| Owning Domain | domain model ownership |
| Object Identity | IDs, external references, identity resolution |
| Lifecycle / State | state fields, transition rules, events |
| Relationships | relational models, references, graph links |
| Source / Provenance | source metadata and verification records |
| Quality Rules | validation and confidence fields |
| Permission Rules | access control and mutation control |
| Audit Rules | audit logs and event links |
| Versioning Rules | version tables or versioned records |
| Related Services | service implementations |
| Events | event specs and event infrastructure |
| Contracts | API, data and event contracts |
| AI Usage | agent context rules and review requirements |
| Product Consumers | product view models and integration |

Implementation shall preserve Core Object meaning, ownership and governance.

---

# 46. Relationship to core-specs/

This chapter governs `core-specs/objects/`.

Every file in `core-specs/objects/` shall follow the object specification structure defined in this chapter.

Each object file shall reference:

```text
core-specs/domains/
core-specs/services/
core-specs/events/
core-specs/api/
core-specs/agents/
core-specs/workflows/
core-specs/contracts/
```

where relevant.

No object spec shall redefine domain boundaries.

No product document shall override a Core Object specification.

No implementation task shall create a Core Object without an approved object spec or explicit architecture approval.

---

# 47. Exclusions

This chapter shall not include:

- full object schemas for all objects;
- database DDL;
- ORM implementation;
- API endpoint definitions;
- product UI components;
- product view models;
- product workflows;
- AI prompt templates;
- deployment architecture;
- vendor-specific implementation.

These belong elsewhere.

---

# 48. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Core Object clearly.
- It distinguishes Core Objects from tables, UI components, product views and prompt variables.
- It defines object ownership by domain.
- It defines object categories.
- It explains identity, lifecycle, state, relationship, provenance, quality, permission, audit and versioning.
- It maps objects to services, events, contracts, AI and product consumption.
- It provides an object specification structure for `core-specs/objects/`.
- It defines inclusion, exclusion, naming, boundary, extension and versioning rules.
- It provides review questions and anti-patterns.
- It supports MVP object sequencing.
- It guides Codex implementation.
- It supports Book 02 TOC v1.2.

---

# 49. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 14, defining Core Object Architecture and object governance rules. |

---

**End of Chapter**
