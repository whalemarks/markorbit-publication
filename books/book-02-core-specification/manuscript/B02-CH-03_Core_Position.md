# Book 02

# 03 — Core Position

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-03  
**Chapter Title:** Core Position  
**Part:** Part I — Core Foundation  
**Chapter Type:** Foundation  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the position of the MarkOrbit Core.

Chapter 02 explained why the Core must exist.

This chapter explains where the Core sits in the full MarkOrbit architecture.

The Core must be positioned correctly before its domains, objects, services, events, contracts, AI governance and execution boundaries can be defined.

If the Core is positioned too high, Book 02 becomes philosophy.

If the Core is positioned too low, Book 02 becomes implementation detail.

If the Core is positioned inside one product, the platform fragments.

If the Core is positioned as an AI layer, professional responsibility is weakened.

If the Core is positioned as a database model, professional meaning is lost.

Therefore, this chapter establishes the Core’s architectural position and dependency direction.

The position defined here governs the rest of Book 02.

---

# 2. Core Question

This chapter answers one question:

> Where does the MarkOrbit Core belong in the MarkOrbit ecosystem?

The answer is:

> The MarkOrbit Core sits between the Professional Operating System and all Workplaces, products, AI agents, network services, `core-specs/`, Codex tasks and software implementation.

The Core is the shared specification foundation that turns professional operating philosophy into reusable execution structure.

---

# 3. Core Position Statement

The MarkOrbit Core is:

> the shared specification layer that defines reusable professional meaning, execution primitives and consumption contracts for the MarkOrbit ecosystem.

This position contains six commitments.

```text
1. Core translates professional philosophy into executable architecture.
2. Core defines shared meaning before products consume it.
3. Core provides primitives, contracts and governance before implementation.
4. Core prevents product, AI and workflow layers from redefining common terms.
5. Core connects manuscript-level architecture to core-specs/ and Codex tasks.
6. Core remains below Professional OS and above product implementation.
```

The Core is not a feature set.

The Core is not a user interface.

The Core is not a database schema.

The Core is not an AI prompt layer.

The Core is not a product roadmap.

The Core is the stable kernel that other layers consume.

---

# 4. Position Lock

Book 02 uses the following position lock.

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
core-specs/
        ↓
Codex Tasks
        ↓
Software Implementation
```

This sequence is not only editorial.

It is architectural.

Later layers may reveal the need to extend the Core, but they do not directly redefine it.

Any change to Core meaning must return to Book 02, `core-specs/` and architecture governance.

---

# 5. Scope

## 5.1 In Scope

This chapter defines:

- the Core’s position in the publication series;
- the Core’s position between Professional OS and implementation;
- the Core’s relationship to the Architecture Library;
- the Core’s relationship to Book 03 Workplace;
- the Core’s relationship to Book 04 MarkReg;
- the Core’s relationship to Book 05 MarkOrbit Lite;
- the Core’s relationship to Book 06 MGSN;
- the Core’s relationship to `core-specs/`;
- the Core’s relationship to Codex tasks;
- the Core’s relationship to software implementation;
- the Core’s relationship to AI;
- the Core’s relationship to products, data, knowledge, business responsibility and network collaboration;
- the dependency direction that later chapters must follow.

## 5.2 Out of Scope

This chapter does not define:

- detailed domain specifications;
- detailed object fields;
- service interface definitions;
- event payloads;
- API endpoint details;
- database schemas;
- product screens;
- product user journeys;
- product pricing;
- workplace UI;
- production AI prompts;
- deployment architecture;
- implementation tickets.

Those belong to later chapters, appendices, `core-specs/`, product books or implementation documents.

---

# 6. Position in the Publication Series

The publication series defines the dependency structure of MarkOrbit.

```text
Book 01 — Professional OS
        defines professional operating philosophy

Book 02 — MarkOrbit Core Specification
        defines the shared Core kernel

Book 03 — Workplace Framework
        defines how work is operated through Workplace

Book 04 — MarkReg
        defines trademark service product execution

Book 05 — MarkOrbit Lite
        defines lightweight AI-assisted service delivery

Book 06 — Mark Global Service Network
        defines global service network collaboration
```

Book 02 is the bridge between philosophy and executable systems.

It is not merely a second book in a sequence.

It is the architectural conversion layer.

Book 01 defines professional logic.

Book 02 converts that logic into Core architecture.

Book 03, Book 04, Book 05 and Book 06 consume that Core.

---

# 7. Position in Relation to Book 01 — Professional OS

Book 01 defines the Professional Operating System.

It explains how professional work creates value through:

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

Book 02 does not repeat this philosophy.

Book 02 converts it into Core structure.

For example:

```text
Professional identity
    becomes Identity and User structures.

Professional knowledge
    becomes Knowledge Source, Knowledge Asset and Knowledge rules.

Professional judgment
    becomes Capability, Review and Responsibility structures.

Professional action
    becomes Service, Task, Event and Workflow Contract structures.

Professional coordination
    becomes Matter, Task, Event, Communication and Routing structures.

Professional experience
    becomes something products and Workplace can deliver through Core consumption.
```

Book 01 defines why professional work matters.

Book 02 defines the shared Core required to operate that work.

---

# 8. Position in Relation to Book 03 — Workplace Framework

Book 03 defines the Workplace.

The Workplace is the operating environment where professional work is viewed, assigned, coordinated, reviewed and completed.

Book 02 does not define Workplace UI.

Book 02 defines what Workplace consumes.

```text
Core provides:
    Identity
    Permission
    Knowledge
    Customer
    Matter
    Order
    Task
    Event
    Workflow Contract
    Notification
    Business Responsibility
    AI Governance

Workplace operates:
    queues
    reviews
    assignments
    work views
    operational dashboards
    human collaboration
    execution experience
```

The relationship is:

```text
Core provides.
Workplace operates.
```

Book 03 may design the experience of work.

It shall not redefine Core primitives such as Task, Event, Matter, Review, Workflow Contract or Responsibility.

---

# 9. Position in Relation to Product Books

Book 04, Book 05 and Book 06 are product or network publications.

They consume the Core.

They do not own Core meaning.

## 9.1 Book 04 — MarkReg

MarkReg consumes Core for trademark service execution.

It may consume:

```text
Customer
Trademark
Jurisdiction
Classification
Document
Evidence
Order
Matter
Task
Event
Workflow Contract
Agent
Communication
AI Governance
```

MarkReg may define product screens, service workflows, operation views and case execution processes.

It shall not redefine the Core meaning of Trademark, Matter, Task, Event, Document or Agent.

## 9.2 Book 05 — MarkOrbit Lite

MarkOrbit Lite consumes Core for guided intake, AI-assisted consultation, lightweight order creation and service delivery.

It may consume:

```text
Identity
Customer
Brand
Trademark
Jurisdiction
Classification
Knowledge
Document Requirement
Order
AI Capability
Agent Contract
Core Consumption Contract
```

Lite may simplify user experience.

It shall not simplify Core meaning into conflicting local definitions.

## 9.3 Book 06 — Mark Global Service Network

MGSN consumes Core for network collaboration, service provider discovery, agent routing and cross-border service execution.

It may consume:

```text
Partner
Agent
Service Provider
Service Network
Routing
Communication
Capability
Trust-related contracts
```

MGSN may define membership, service exchange, cooperation rules and network products.

It shall not redefine the Core identity of Partner, Agent, Service Provider, Routing Decision or Communication.

---

# 10. Position in Relation to the Architecture Library

The Architecture Library governs how MarkOrbit architecture is expressed and evolved.

```text
Architecture Library
    MAC — MarkOrbit Architecture Canon
    MAG — MarkOrbit Architecture Governance
    MAS — MarkOrbit Architecture Specifications
        ↓
Book 02 — MarkOrbit Core Specification
```

The distinction is important.

```text
MAC defines architecture meaning.
MAG defines architecture governance.
MAS defines specification representation standards.
Book 02 defines the MarkOrbit Core itself.
```

Book 02 shall conform to MAC, MAG and MAS.

Book 02 shall not duplicate them.

Book 02 is an application of architecture standards to the Core.

---

# 11. Position in Relation to `core-specs/`

Book 02 manuscript and `core-specs/` are different layers of one specification system.

```text
Book 02 manuscript
    defines Core meaning, architecture, boundaries, principles and specification framework.

core-specs/
    defines executable detailed specifications for domains, objects, services, events, contracts, APIs, agents and workflows.
```

The manuscript answers:

```text
What is the Core?
Why does it exist?
Where does it sit?
What boundaries govern it?
What specification systems are required?
How should MVP execution be controlled?
```

`core-specs/` answers:

```text
What fields does an object have?
What service inputs and outputs exist?
What event payload is required?
What contracts govern consumption?
What API surface is available?
What agent may access what knowledge?
What workflow states and transitions are allowed?
```

The manuscript is not a substitute for `core-specs/`.

`core-specs/` is not allowed to redefine manuscript-level meaning.

The relationship is:

```text
Manuscript defines meaning.
Appendices stabilize indexes.
core-specs/ defines executable details.
Codex implements approved specs.
```

---

# 12. Position in Relation to Codex

Codex is an implementation assistant.

Codex is not the Core.

Codex is not an architecture authority.

Codex must consume approved sources.

```text
Book 02 manuscript
        ↓
Appendices
        ↓
indexes/
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Implementation
```

Codex may generate code, templates, tests, scaffolds and task files.

Codex shall not invent:

```text
Core domains
Core object meanings
event semantics
AI authority
product ownership boundaries
workflow responsibility
deferred scope
```

Every Codex implementation task must reference:

```text
source specs
execution matrix row
dependencies
out-of-scope items
acceptance criteria
tests
```

The Core position therefore controls Codex behavior.

---

# 13. Position in Relation to Software Implementation

Software implementation realizes the Core.

It does not define the Core.

Implementation may include:

```text
database schemas
domain models
service modules
API routes
event infrastructure
workflow engines
AI agent invocation
permission checks
audit records
fixtures
tests
product modules
```

But implementation must follow:

```text
Book 02
Appendices
indexes/
core-specs/
Codex task contracts
```

A database table does not define an object.

A route does not define a service.

A queue message does not define an event.

A prompt does not define an AI agent.

A UI state does not define a workflow.

Implementation realizes approved Core specifications.

---

# 14. Position in Relation to Products

Products are consumer layers.

They deliver user-facing functionality.

They may compose Core Objects, call Core Services, subscribe to Core Events, invoke governed AI Agents and present product-specific experiences.

Products may own:

```text
screens
forms
pages
product user journeys
product dashboards
product onboarding
product-specific workflows
product reports
product configuration
commercial packaging
```

Products shall not own:

```text
shared Core Object meaning
shared Core Service definition
shared Event semantics
domain boundaries
AI governance rules
permission foundations
Core consumption contracts
professional truth definitions
```

The relationship is:

```text
Core defines reusable professional foundation.
Products deliver user-facing experiences through Core consumption.
```

This protects MarkOrbit from product-driven fragmentation.

---

# 15. Position in Relation to Workplace

Workplace is a special consumer of Core.

It is not just another product page.

It is the operating context where professional execution happens.

The Workplace consumes Core primitives such as:

```text
Identity
User
Permission
Matter
Task
Event
State
Context
Workflow Contract
Business Responsibility
Notification
Review
AI Output
Audit
```

Workplace may organize work.

Workplace may present queues.

Workplace may support assignment, review and coordination.

Workplace may provide operational experience.

Workplace shall not redefine Core execution primitives.

The relationship remains:

```text
Core provides execution primitives.
Workplace operates professional work.
```

---

# 16. Position in Relation to AI

AI is a governed execution capability.

AI is not positioned above Core.

AI is not positioned outside Core.

AI is not a replacement for professional responsibility.

```text
Core Capability
        ↓
Agent Contract
        ↓
Governed AI Execution
        ↓
Human Review where required
```

AI may assist with:

```text
consultation
classification
knowledge retrieval
document drafting
evidence review
trademark status summary
communication summary
opportunity discovery
routing recommendation
workflow assistance
Codex implementation assistance
```

AI must operate under:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Structured Context
Permission
Policy
Risk Level
Human Review
Events
Audit
Product Consumer Boundary
```

AI output may assist judgment.

AI output shall not become professional truth without review where risk requires it.

---

# 17. Position in Relation to Data

Data is not the Core by itself.

The Core gives data professional meaning.

For example:

```text
a trademark row is data
a Trademark Object is Core meaning
a Trademark Service provides governed use
a Trademark Event makes change observable
a Trademark Contract makes consumption safe
an AI Trademark Summary operates under Agent Contract
```

Therefore:

```text
Data stores facts.
Core defines meaning.
Services operate meaning.
Events expose change.
Products consume governed outputs.
```

Book 02 sits above raw data and below product experience.

---

# 18. Position in Relation to Knowledge

Knowledge is a Core foundation.

A knowledge base is not the Core.

The Core governs how knowledge is sourced, validated, retrieved, consumed and used by humans and AI.

Knowledge must connect to:

```text
domains
jurisdictions
objects
services
contracts
AI agents
workflow context
professional review
```

Knowledge supports professional judgment.

Knowledge does not replace responsibility.

AI-generated content is not automatically validated knowledge.

---

# 19. Position in Relation to Business Responsibility

The Core is not a commercial pricing system.

The Core does not define packages, discounts, commission models or sales tactics.

However, the Core must define business responsibility.

Business Responsibility governs:

```text
who owns work
who may act
who must review
who is accountable
who receives task assignment
who controls order-to-matter conversion
who owns opportunity follow-up
who approves AI output
```

Business Responsibility is a cross-cutting Core specification system.

It may produce executable objects, services, events and contracts.

It should not be confused with product pricing or sales strategy.

---

# 20. Position in Relation to Network Collaboration

The Core provides the shared foundation for network collaboration.

It may define:

```text
Partner
Agent
Service Provider
Service Network
Routing
Communication
Capability
Responsibility
Trust-related primitives
```

But full network operation belongs to Book 06.

The relationship is:

```text
Book 02 defines network-capable Core objects and contracts.
Book 06 defines network operation, participation and service exchange.
```

This prevents the Core MVP from overbuilding the full MGSN marketplace too early.

---

# 21. Consumer Classification

Not all consumers have the same implementation priority.

Book 02 uses the following consumer classification.

## 21.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

These consumers shape the Core MVP.

## 21.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

These consumers require reserved boundaries or partial baseline support.

They should not pull full future product scope into the MVP.

## 21.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

These consumers may be supported by future Core extensions.

They do not define the MVP boundary.

---

# 22. Dependency Direction

The dependency direction must remain stable.

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

The reverse direction is not allowed as a source of Core meaning.

A product feature may expose a missing Core concept.

An implementation problem may expose a specification gap.

An AI use case may expose a governance requirement.

But those findings must return to Core governance before changing Core meaning.

---

# 23. Positioning Rules

The following positioning rules are established.

## Rule 1 — Book 02 defines the Core

Book 02 shall remain the Core Specification.

It shall not become a product PRD, software ticket list or prompt library.

## Rule 2 — Core sits between Professional OS and implementation

Core translates professional philosophy into executable architecture.

## Rule 3 — Products consume Core

Products may design experience.

Products shall not redefine shared Core meaning.

## Rule 4 — Workplace operates work

Workplace consumes execution primitives and contracts.

Workplace shall not redefine those primitives.

## Rule 5 — Architecture Library governs Book 02

Book 02 conforms to MAC, MAG and MAS.

Book 02 does not duplicate them.

## Rule 6 — Appendices stabilize indexes before `core-specs/`

Appendices define canonical glossary and indexes.

`core-specs/` should not be generated before appendices are complete.

## Rule 7 — `core-specs/` carry executable details

The manuscript defines meaning and structure.

`core-specs/` define detailed executable specifications.

## Rule 8 — Codex implements approved specs

Codex tasks must reference approved sources and acceptance criteria.

Codex shall not invent architecture.

## Rule 9 — AI is governed by Core

AI is a governed capability under Agent Contract.

AI is not autonomous professional authority.

## Rule 10 — Future products do not expand MVP scope automatically

MGSN, Brand Asset Vault and Opportunity Engine may require reserved boundaries.

They do not automatically become full MVP implementation.

---

# 24. Positioning Map

The Core’s position can be summarized as follows:

```text
Architecture Library
MAC / MAG / MAS
        ↓

Book 01
Professional OS
        ↓

Book 02
MarkOrbit Core Specification
        ↓
        ├── Appendices and Indexes
        │       ↓
        │   core-specs/
        │       ↓
        │   Codex Tasks
        │       ↓
        │   Software Implementation
        │
        ├── Book 03 — Workplace Framework
        │
        ├── Book 04 — MarkReg
        │
        ├── Book 05 — MarkOrbit Lite
        │
        └── Book 06 — Mark Global Service Network
```

This map shows the Core as the shared source for:

```text
specification
execution
workplace operation
product consumption
AI governance
network foundation
implementation control
```

---

# 25. Specification Output

This chapter produces the following specification outputs:

```text
Core Position Statement
Position Lock
Publication Series Dependency
Core / Architecture Library Boundary
Core / Book 01 Boundary
Core / Book 03 Boundary
Core / Product Book Boundary
Core / core-specs Boundary
Core / Codex Boundary
Core / Implementation Boundary
Core / AI Boundary
Core / Data Boundary
Core / Knowledge Boundary
Core / Business Responsibility Boundary
Core / Network Boundary
Consumer Classification
Dependency Direction Rules
Positioning Rules
```

These outputs govern all later chapters.

---

# 26. Execution Mapping

This chapter does not produce direct implementation files.

It produces positioning constraints that implementation must follow.

| Position Decision | Execution Impact |
|------------------|------------------|
| Products consume Core | Consumption Contracts are required |
| Workplace operates work | Workflow and Task meaning remain Core-owned |
| Appendices precede `core-specs/` | Indexes must be stabilized before spec generation |
| `core-specs/` carry executable details | Detailed implementation specs live outside manuscript |
| Codex implements specs | Codex tasks must reference sources and acceptance criteria |
| AI is governed capability | Agent Contracts, review, events and audit are required |
| Data is not Core by itself | Object meaning must be defined before schema design |
| Future consumers do not define MVP | Reserved boundaries protect future products |

---

# 27. Relationship to Appendices

This chapter directly informs the appendices.

Appendix A shall define the terminology used here.

Appendix B shall preserve the 26-domain baseline and classify cross-cutting systems.

Appendix F shall define API surfaces as contract-bound consumption surfaces.

Appendix G shall define AI agents as governed execution actors.

Appendix H shall ensure Codex tasks follow source specs, indexes and execution boundaries.

---

# 28. Relationship to `core-specs/`

This chapter does not create a specific `core-specs/` file.

It governs how `core-specs/` will later be generated.

Specifically:

```text
Domain specs shall preserve Core boundaries.
Object specs shall define meaning before fields.
Service specs shall not become product button logic.
Event specs shall not become informal activity logs.
Contract specs shall govern consumption.
API specs shall expose governed service surfaces.
Agent specs shall not treat AI as autonomous authority.
Workflow specs shall preserve Core / Workplace distinction.
```

---

# 29. Exclusions

This chapter shall not include:

```text
product requirements
feature lists
UI design
workflow screen designs
database schema details
API endpoint details
prompt templates
deployment architecture
sales strategy
commercial pricing
implementation tickets
```

These belong to later documents.

---

# 30. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It clearly defines where the Core sits.
[ ] It distinguishes Book 02 from Book 01.
[ ] It distinguishes Book 02 from Book 03.
[ ] It distinguishes Book 02 from Book 04, Book 05 and Book 06.
[ ] It distinguishes Book 02 from the Architecture Library.
[ ] It distinguishes manuscript from appendices and core-specs/.
[ ] It distinguishes Core from Codex.
[ ] It distinguishes Core from software implementation.
[ ] It distinguishes Core from Product.
[ ] It distinguishes Core from Workplace.
[ ] It distinguishes Core from AI.
[ ] It distinguishes Core from raw data.
[ ] It distinguishes Knowledge from a knowledge base.
[ ] It clarifies Business Responsibility as a Core responsibility system, not pricing.
[ ] It classifies MVP, Partial and Future consumers.
[ ] It establishes correct dependency direction.
[ ] It states that appendices precede core-specs/.
[ ] It avoids product PRD content.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 03, defining the architectural and publication position of the MarkOrbit Core. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened Core positioning, dependency direction, Core/AI/Codex/Product/Workplace boundaries, consumer classification and appendix-before-core-specs rule. |

---

**End of Chapter**
