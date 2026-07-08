# Book 02

# 08 — Ontology and Domain Classification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-08  
**Chapter Title:** Ontology and Domain Classification  
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

This chapter defines the ontology and domain classification of the MarkOrbit Core.

The previous chapters established why the Core exists, where it sits, what its boundary is and what principles govern it.

This chapter defines how the Core classifies reality into reusable architectural meaning.

Ontology answers:

```text
What kinds of things exist in the MarkOrbit Core?
What does each thing mean?
How are things related?
Which layer owns each meaning?
How should domains be classified?
What is a domain and what is not a domain?
How should cross-cutting systems be handled?
```

Domain classification answers:

```text
Which Core Domains exist?
Why are they grouped this way?
Which domains belong to MVP?
Which domains are reserved for future expansion?
How do products consume domains without redefining them?
```

This chapter is the foundation for:

```text
Chapter 13 — Core Domain Architecture
Chapter 22 — Domain Specification
Appendix A — Glossary
Appendix B — Core Domain Index
core-specs/domains/
Codex domain scaffold tasks
```

If the ontology is unclear, every downstream specification becomes unstable.

---

# 2. Core Question

This chapter answers one question:

> How should the MarkOrbit Core classify professional reality into stable domains, objects, services, events, contracts and cross-cutting systems?

The answer is:

> The MarkOrbit Core uses a layered ontology that separates professional meaning, domain responsibility, object identity, service behavior, event semantics, contract boundaries, AI governance and product consumption. The baseline Core Domain Map contains 26 domains, grouped into four domain categories, while Capability and Business Responsibility are treated as cross-cutting Core specification systems rather than additional baseline domains.

---

# 3. Ontology Statement

The MarkOrbit Core ontology is the formal classification of what exists inside the Core and how each concept should be interpreted.

The Core ontology defines:

```text
Canonical Models
Core Domains
Cross-Cutting Specification Systems
Core Objects
Core Services
Core Events
Core Contracts
Execution Primitives
AI Agents
Consumers
MVP Depth Types
```

The ontology must remain stable across:

```text
manuscript chapters
appendices
indexes
core-specs/
Codex tasks
software implementation
product books
AI agents
external integrations
```

A concept should not change meaning depending on which product uses it.

---

# 4. Ontology Principles

The ontology follows the Core Principles from Chapter 05.

```text
Core Before Product
Meaning Before Data
Boundary Before Detail
Domain Before Object
Object Before Service
Service Before Automation
Event Before Coordination
Contract Before Consumption
Governance Before AI
Responsibility Before Delegation
Appendix Before core-specs
Specification Before Codex
MVP Before Expansion
```

The most important ontology rule is:

```text
Meaning must be classified before implementation begins.
```

A product screen does not define ontology.

A database table does not define ontology.

A prompt does not define ontology.

A Codex task does not define ontology.

The Core defines ontology.

---

# 5. Ontology Layer Model

The MarkOrbit Core uses the following ontology layer model.

```text
Professional Reality
        ↓
Canonical Models
        ↓
Core Domains
        ↓
Cross-Cutting Specification Systems
        ↓
Core Objects
        ↓
Core Services
        ↓
Core Events
        ↓
Core Contracts
        ↓
Execution Primitives
        ↓
AI Governance
        ↓
Core Consumption
```

Each layer has a different responsibility.

| Layer | Responsibility |
|------|----------------|
| Professional Reality | What happens in real professional work |
| Canonical Models | The highest reusable meaning patterns |
| Core Domains | Stable responsibility areas |
| Cross-Cutting Systems | Governance systems that span domains |
| Core Objects | Meaningful entities and records |
| Core Services | Governed capabilities that operate objects |
| Core Events | Meaningful changes and coordination signals |
| Core Contracts | Boundaries for data, API, events, agents, workflows and consumers |
| Execution Primitives | Task, state, context, workflow and review mechanisms |
| AI Governance | Rules for AI capability and agent behavior |
| Core Consumption | How products, Workplace, AI, integrations and Codex consume Core |

---

# 6. From Professional Reality to Core Ontology

Professional trademark and brand service work contains many real-world phenomena.

Examples:

```text
a client asks whether a brand should be filed overseas
a logo is uploaded
a jurisdiction is selected
goods and services are classified
a quotation is prepared
an order is confirmed
a matter is created
foreign agent documents are requested
a filing document is generated
a task is assigned
a review is required
an office action is received
AI drafts a recommendation
human review approves or rejects it
a provider is routed
a communication is linked
a business opportunity is identified
```

The Core should not treat these as isolated features.

It classifies them into shared ontology.

Example:

```text
Client asks question
    → Customer / Knowledge / AI Capability / Consultation context

Logo uploaded
    → Brand / Trademark / Document / Evidence

Goods classified
    → Classification / Knowledge / AI Agent / Review

Order confirmed
    → Order / Event / Workflow Contract

Matter created
    → Matter / Task / Responsibility / Event

AI drafts recommendation
    → AI Agent / Agent Contract / AI Output / ReviewRequired / Audit
```

Ontology turns professional reality into reusable Core structure.

---

# 7. Canonical Models

Canonical Models are the highest-level reusable models in the Core.

They are not product modules.

They are not database schemas.

They organize professional meaning across domains.

Book 02 recognizes the following Canonical Models:

```text
Identity Model
Capability Model
Knowledge Model
Business Responsibility Model
Workplace Model
Network Model
```

## 7.1 Identity Model

The Identity Model governs who or what exists and may act.

It supports:

```text
Identity
Organization
User
Permission
Agent identity
AI Agent identity
external actor identity
```

## 7.2 Capability Model

The Capability Model governs what can be done and by whom or by what actor.

It supports:

```text
human capability
AI capability
agent capability
service provider capability
product capability
workflow capability
```

Capability is cross-cutting.

It is not counted as an additional baseline Core Domain.

## 7.3 Knowledge Model

The Knowledge Model governs professional knowledge sources, validation, retrieval and usage.

It supports:

```text
Knowledge Source
Knowledge Asset
Knowledge Rule
Knowledge Validation
Knowledge Retrieval
Knowledge Gap
AI authorized knowledge
```

## 7.4 Business Responsibility Model

The Business Responsibility Model governs who is accountable for work, review, approval, delegation and follow-up.

It supports:

```text
responsibility assignment
review record
approval responsibility
task ownership
matter ownership
AI output review
routing approval
opportunity ownership
```

Business Responsibility is cross-cutting.

It is not counted as an additional baseline Core Domain.

## 7.5 Workplace Model

The Workplace Model governs how professional work is operated through tasks, events, states, workflow contracts, reviews and notifications.

Book 03 expands the Workplace.

Book 02 defines the Core primitives it consumes.

## 7.6 Network Model

The Network Model governs collaboration among partners, agents, service providers, routing paths and communication.

Book 06 expands network operation.

Book 02 defines the Core network-capable primitives.

---

# 8. Core Domain Definition

A Core Domain is:

> a stable responsibility area inside the MarkOrbit Core that owns a set of meanings, objects, services, events, contracts and governance rules.

A Core Domain must have:

```text
a clear purpose
an owning responsibility
scope boundaries
primary objects
primary services
primary events
related contracts
consumer boundaries
MVP classification
```

A Core Domain is not:

```text
a product feature
a UI module
a database table
a menu item
a workflow step
a department name
a prompt category
an implementation package
```

A domain exists because a stable area of professional meaning must be governed across products.

---

# 9. Domain Classification Criteria

A concept may be classified as a Core Domain only if it satisfies most of the following criteria.

```text
1. It represents a stable area of professional or platform responsibility.
2. It owns Core Objects or governs object meaning.
3. It requires services that operate its meaning.
4. It may emit or consume Core Events.
5. It needs contracts for consumption or integration.
6. It must be reusable across multiple products or Workplaces.
7. It is not merely a product screen or implementation detail.
8. It is stable enough to appear in appendices and core-specs/.
9. It may be governed independently.
10. It has MVP, partial, reserved or deferred implementation depth.
```

If a concept spans many domains and governs behavior across them, it may be a cross-cutting specification system instead of a domain.

---

# 10. Baseline Core Domain Map

The canonical baseline Core Domain Map contains 26 domains.

They are grouped into four categories.

```text
Foundation Domains
Professional Domains
Business Execution Domains
Collaboration Network Domains
```

This 26-domain baseline is frozen for the second canonical draft unless a future architecture release explicitly changes it.

---

# 11. Foundation Domains

Foundation Domains define the minimum platform foundation required before professional, execution and network domains can operate.

The Foundation Domains are:

```text
Identity
Organization
User
Permission
Policy
Knowledge
```

## 11.1 Identity

Identity defines who or what exists as an identifiable actor or entity.

It supports users, organizations, agents, AI agents, customers and external actors.

## 11.2 Organization

Organization defines structured legal, business or operational entities.

It supports company ownership, customer organizations, provider organizations and internal teams.

## 11.3 User

User defines human platform users and their connection to identity, organization, roles and permissions.

## 11.4 Permission

Permission defines who may access, read, write, act or invoke services.

Permission protects Core objects and services from unauthorized use.

## 11.5 Policy

Policy defines rules that constrain access, sharing, review, AI usage, external exposure and risk behavior.

Policy is a foundation domain because governance cannot be deferred entirely to products.

## 11.6 Knowledge

Knowledge defines sources, assets, validation, retrieval and knowledge gaps.

Knowledge is foundational because professional service depends on trusted knowledge.

---

# 12. Professional Domains

Professional Domains define the trademark and brand-related professional meaning that MarkOrbit must manage.

The Professional Domains are:

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
```

## 12.1 Brand

Brand defines brand identity, brand assets and brand-related service context.

## 12.2 Trademark

Trademark defines trademark records, mark identity, application/registration status and trademark lifecycle context.

## 12.3 Jurisdiction

Jurisdiction defines countries, regions, offices, filing systems and jurisdiction-specific rules.

## 12.4 Classification

Classification defines classes, goods/services items, recommendations, validation and classification logic.

## 12.5 Document

Document defines uploaded, generated, parsed and linked documents used in professional service execution.

## 12.6 Evidence

Evidence defines materials used to support professional claims, use, response, review or enforcement.

Evidence may be partially implemented in MVP but should not become a full sufficiency engine too early.

---

# 13. Business Execution Domains

Business Execution Domains define how professional service demand becomes managed execution.

The Business Execution Domains are:

```text
Customer
Matter
Order
Opportunity
Workflow Contract
Task
Event
Notification
```

## 13.1 Customer

Customer defines the client or customer context that receives services or owns business demand.

## 13.2 Matter

Matter defines the professional work container created from confirmed orders or other approved initiation paths.

## 13.3 Order

Order defines a commercial or service request that may become executable work.

## 13.4 Opportunity

Opportunity defines business or service opportunities discovered from events, data, AI suggestions or professional review.

Opportunity should remain baseline or partial in MVP.

## 13.5 Workflow Contract

Workflow Contract defines states, transitions, execution rules and responsibility points for repeatable work.

## 13.6 Task

Task defines assigned work units, ownership, status and execution responsibilities.

## 13.7 Event

Event defines meaningful changes in Core or execution state.

Events enable coordination and downstream responses.

## 13.8 Notification

Notification defines alerts or notices created from events, tasks, reviews or workflow conditions.

Notification should begin as baseline in MVP, not as a full preference system.

---

# 14. Collaboration Network Domains

Collaboration Network Domains define the foundations for global service collaboration.

The Collaboration Network Domains are:

```text
Partner
Agent
Service Provider
Service Network
Routing
Communication
```

## 14.1 Partner

Partner defines cooperating business entities or platform partners.

Partner is mostly reserved for future network expansion in MVP.

## 14.2 Agent

Agent defines professional agents or law firms that participate in service execution.

Agent may be partially implemented for routing and communication support.

## 14.3 Service Provider

Service Provider defines external providers that deliver services, capabilities or execution support.

## 14.4 Service Network

Service Network defines the structured collaboration network among partners, agents and providers.

Service Network is largely reserved in MVP.

## 14.5 Routing

Routing defines how matters, tasks, opportunities or requests are matched to agents or providers.

Routing should be baseline or partial in MVP.

## 14.6 Communication

Communication defines conversations, messages, records and links among customers, agents, providers and internal users.

Communication may be baseline in MVP, especially for Matter and Agent context.

---

# 15. Cross-Cutting Specification Systems

Some Core systems are not ordinary baseline domains because they cut across multiple domains.

Book 02 recognizes at least two cross-cutting Core specification systems:

```text
Capability
Business Responsibility
```

These systems are essential.

They may produce objects, services, contracts, events and indexes.

However, they do not silently increase the baseline Core Domain count.

The canonical rule is:

```text
The baseline Core Domain Map contains 26 domains.
Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

---

# 16. Capability as Cross-Cutting System

Capability describes what can be done and by whom or by what actor.

It may apply to:

```text
human users
internal teams
AI agents
foreign agents
service providers
products
workflow roles
integration actors
```

Capability may produce Core artifacts such as:

```text
Capability Object
Capability Provider
Capability Scope
Capability Matching Service
Capability Contract
AI Capability Registry
```

Capability connects to many domains:

```text
Identity
User
Permission
Knowledge
Agent
Service Provider
Routing
Workflow Contract
AI Governance
```

It is cross-cutting because it governs ability across the Core, not one isolated domain area.

---

# 17. Business Responsibility as Cross-Cutting System

Business Responsibility describes who is accountable for work, review, approval, delegation and follow-up.

It may apply to:

```text
Order
Matter
Task
AI Output
Document Draft
Evidence Review
Routing Decision
Communication
Opportunity
Network Collaboration
```

Business Responsibility may produce Core artifacts such as:

```text
Responsibility Assignment
Review Record
Approval Service
ReviewRequired Event
ReviewApproved Event
ReviewRejected Event
Responsibility Contract
```

Business Responsibility is not the same as business pricing or commission policy.

It governs accountability.

It is cross-cutting because responsibility applies across many execution contexts.

---

# 18. What Is Not a Core Domain

The following should not be classified as Core Domains unless a future architecture release explicitly changes the map.

```text
Dashboard
Page
Form
Button
Report
Prompt
Chat
File Upload UI
Payment Page
Email Template
Sales Package
Price Plan
Marketing Campaign
Vendor Connector
Database Table
API Route
Codex Task
```

These may be implementation artifacts, product features, templates or consumer surfaces.

They are not baseline Core Domains.

---

# 19. Domain vs Object

A domain owns responsibility.

An object carries meaning inside a domain or cross-cutting system.

Examples:

```text
Trademark Domain
    owns Trademark Object

Order Domain
    owns Order Object

Task Domain
    owns Task Object

AI Governance / Agent System
    owns AI Agent and Agent Contract concepts

Business Responsibility System
    owns Responsibility Assignment and Review Record concepts
```

The rule is:

```text
Domain before Object.
```

Every object must have an owning domain or cross-cutting specification system.

---

# 20. Domain vs Service

A domain owns meaning.

A service operates meaning.

Examples:

```text
Classification Domain
    Classification Recommendation Service
    Goods/Services Validation Service

Order Domain
    Order Creation Service
    Order Confirmation Service

Matter Domain
    Matter Creation Service
    Order-to-Matter Conversion Service

Routing Domain
    Routing Decision Service
```

The rule is:

```text
Object before Service.
```

A service should not operate undefined objects or unclear domain meaning.

---

# 21. Domain vs Event

A domain may produce events when meaningful changes occur.

Examples:

```text
Trademark Domain
    TrademarkCreated
    TrademarkStatusChanged

Order Domain
    OrderCreated
    OrderConfirmed
    OrderConvertedToMatter

Task Domain
    TaskCreated
    TaskAssigned
    TaskCompleted

AI Governance
    AIRecommendationGenerated
    AIRecommendationReviewRequired
```

Events are not logs.

Events are semantic change signals with source domains and payload contracts.

---

# 22. Domain vs Product

Products consume domains.

Products do not become domains merely because they have screens or workflows.

Examples:

```text
MarkReg consumes Trademark, Matter, Document, Task, Event and Agent.
MarkOrbit Lite consumes Customer, Brand, Jurisdiction, Classification, Knowledge and Order.
Workplace consumes Task, Event, Workflow Contract, Review and Notification.
MGSN consumes Partner, Agent, Service Provider, Routing and Communication.
```

Product differences do not justify redefining Core domain meaning.

---

# 23. Domain vs Workplace

Workplace operates professional work.

Core Domains define the primitives that Workplace consumes.

Workplace may present:

```text
task queues
matter views
review queues
notification panels
event timelines
AI output review screens
```

But Task, Matter, Event, Review and Workflow Contract remain Core-owned.

---

# 24. Domain vs AI

AI is not a domain by itself.

AI is governed through:

```text
AI Capability
AI Agent Identity
Agent Contract
Authorized Knowledge
Object Access
Permission
Policy
Risk Level
Review
Event
Audit
```

AI-related artifacts may be indexed under AI Governance or Agent Index.

AI must not redefine professional domains.

For example:

```text
Classification Assistant supports Classification Domain.
Document Draft Assistant supports Document Domain.
Trademark Status Summary Agent supports Trademark Domain.
Routing Assistant supports Routing Domain.
Codex Implementation Agent supports implementation tasks.
```

The domain owns the professional meaning.

The AI agent assists under governance.

---

# 25. Domain vs API

An API is a consumption surface.

It is not a domain by itself.

API surfaces expose domain services through contracts.

Examples:

```text
Classification Recommendation API
    exposes Classification Recommendation Service
    under API Contract and Permission rules

Order API
    exposes Order Creation and Order Confirmation Services

Task API
    exposes Task Creation, Assignment and Completion Services

AI Invocation API
    exposes governed AI Agent invocation
```

Appendix F shall define API surfaces and template expectations.

---

# 26. Domain vs Integration

External integration is not a domain by itself unless it represents stable Core responsibility.

A trademark office connector, email connector, payment connector or AI model provider connector is an implementation adapter.

Core may define:

```text
Integration Contract
Data Contract
API Contract
Event Contract
Permission rules
Audit requirements
```

The connector implementation belongs to implementation or integration layers.

---

# 27. Domain Classification Matrix

The baseline domain map can be summarized as follows.

| Category | Domain | Core Role | MVP Direction |
|----------|--------|-----------|---------------|
| Foundation | Identity | actor/entity identity | Must Implement |
| Foundation | Organization | organization structure | Must Implement |
| Foundation | User | human user context | Must Implement |
| Foundation | Permission | access and action control | Must Implement |
| Foundation | Policy | governance rules | Partial Implement |
| Foundation | Knowledge | validated knowledge foundation | Must Implement |
| Professional | Brand | brand context | Must Implement |
| Professional | Trademark | trademark lifecycle meaning | Must Implement |
| Professional | Jurisdiction | country/office context | Must Implement |
| Professional | Classification | goods/services classification | Must Implement |
| Professional | Document | document lifecycle | Must Implement |
| Professional | Evidence | supporting evidence | Partial Implement |
| Business Execution | Customer | service recipient / client context | Must Implement |
| Business Execution | Matter | professional work container | Must Implement |
| Business Execution | Order | service request / commercial trigger | Must Implement |
| Business Execution | Opportunity | business opportunity signal | Partial Implement |
| Business Execution | Workflow Contract | state and transition contract | Must Implement |
| Business Execution | Task | assigned work unit | Must Implement |
| Business Execution | Event | semantic change signal | Must Implement |
| Business Execution | Notification | alert/notice baseline | Partial Implement |
| Collaboration Network | Partner | business collaboration entity | Reserved Boundary |
| Collaboration Network | Agent | professional agent/law firm | Partial Implement |
| Collaboration Network | Service Provider | external capability provider | Partial Implement |
| Collaboration Network | Service Network | collaboration network structure | Reserved Boundary |
| Collaboration Network | Routing | matching and routing decisions | Partial Implement |
| Collaboration Network | Communication | linked conversations/messages | Partial Implement |

This table is a summary.

Appendix B is the canonical domain index.

---

# 28. MVP Domain Classification

MVP domain classification uses four depth types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 28.1 Must Implement

A domain must be implemented when the first executable Core cannot function without it.

Examples:

```text
Identity
User
Permission
Knowledge
Trademark
Classification
Customer
Order
Matter
Task
Event
Workflow Contract
```

## 28.2 Partial Implement

A domain or system is partially implemented when MVP needs baseline representation but not full capability.

Examples:

```text
Policy
Evidence
Notification
Communication
Agent
Service Provider
Routing
Opportunity
```

## 28.3 Reserved Boundary

A domain is reserved when its future meaning must be protected, but MVP should not implement it deeply.

Examples:

```text
Partner
Service Network
full MGSN marketplace
advanced provider network
```

## 28.4 Deferred

A feature or capability is deferred when it belongs outside the Core MVP.

Examples:

```text
full global agent marketplace
advanced price automation
advanced opportunity scoring
full external integration platform
full AI autonomy
full analytics suite
```

---

# 29. Consumer-Based Domain Priority

Domains are prioritized according to first consumers.

## 29.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

These consumers shape the Core MVP.

## 29.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

These consumers require boundaries and partial foundations.

They should not pull full product scope into MVP.

## 29.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Future consumers may influence reserved boundaries, but they do not define the first Core MVP.

---

# 30. Domain Dependency Flow

Domain implementation should follow dependency direction.

```text
Identity
    ↓
Organization / User
    ↓
Permission / Policy
    ↓
Knowledge / Capability
    ↓
Brand / Trademark / Jurisdiction / Classification / Document
    ↓
Customer / Order / Matter
    ↓
Workflow Contract / Task / Event
    ↓
Business Responsibility / Notification
    ↓
Communication / Agent / Service Provider / Routing / Opportunity
    ↓
Partner / Service Network
```

This flow does not change the 26-domain baseline.

It shows implementation dependency and cross-cutting system usage.

---

# 31. Domain Governance Rules

## Rule 1 — The 26-domain baseline is canonical

Do not add domains casually.

## Rule 2 — Domains must own responsibility

A domain must govern meaning, objects, services, events or contracts.

## Rule 3 — Product features are not domains

A screen, journey or dashboard is not a domain.

## Rule 4 — Data tables are not domains

A schema may implement a domain object, but it does not define a domain.

## Rule 5 — AI is governed, not domain-owning

AI agents assist domains under Agent Contracts.

## Rule 6 — Cross-cutting systems must be labeled

Capability and Business Responsibility must be explicitly marked as cross-cutting.

## Rule 7 — MVP depth must be declared

Each domain must have MVP depth.

## Rule 8 — Product consumers must be declared

A domain must state which consumers rely on it.

## Rule 9 — Deferred scope must remain protected

Future features should not enter MVP through domain ambiguity.

## Rule 10 — Appendix B becomes canonical index

This chapter defines the model.

Appendix B lists the canonical domain index.

---

# 32. Domain Classification Anti-Patterns

## 32.1 Feature as Domain

Example:

```text
Quote Page Domain
```

Problem:

```text
A page is a product feature, not a Core Domain.
```

## 32.2 Table as Domain

Example:

```text
tm_application_table Domain
```

Problem:

```text
A table is implementation, not ontology.
```

## 32.3 Prompt as Domain

Example:

```text
Classification Prompt Domain
```

Problem:

```text
AI prompt is implementation detail; Classification is the domain.
```

## 32.4 Product as Domain

Example:

```text
Lite Domain
```

Problem:

```text
Lite is a product consumer, not a Core Domain.
```

## 32.5 Cross-Cutting System as Hidden Domain

Example:

```text
Adding Capability as the 27th baseline domain without release decision.
```

Problem:

```text
It creates domain count drift.
```

## 32.6 Future Marketplace as MVP Domain

Example:

```text
Full Agent Marketplace Domain in Core MVP.
```

Problem:

```text
It violates MVP Before Expansion.
```

---

# 33. Specification Output

This chapter produces the following specification outputs:

```text
Ontology Statement
Ontology Layer Model
Canonical Model Summary
Core Domain Definition
Domain Classification Criteria
26 Baseline Core Domain Map
Foundation Domain Classification
Professional Domain Classification
Business Execution Domain Classification
Collaboration Network Domain Classification
Cross-Cutting Specification System Rule
Capability Cross-Cutting Rule
Business Responsibility Cross-Cutting Rule
Domain vs Object distinction
Domain vs Service distinction
Domain vs Event distinction
Domain vs Product distinction
Domain vs Workplace distinction
Domain vs AI distinction
Domain vs API distinction
Domain vs Integration distinction
MVP Domain Classification
Consumer-Based Domain Priority
Domain Dependency Flow
Domain Governance Rules
Domain Classification Anti-Patterns
```

These outputs shall be used by Appendix B and `core-specs/domains/`.

---

# 34. Execution Mapping

| Ontology Decision | Execution Impact |
|------------------|------------------|
| 26 baseline domains | Appendix B and core-specs/domains/ must preserve domain count |
| Cross-cutting systems | Capability and Business Responsibility must be labeled explicitly |
| Domain before Object | Appendix C must map objects to owning domains/systems |
| Object before Service | Appendix D must map services to objects |
| Event as semantic change | Appendix E must map events to source domains |
| API as consumption surface | Appendix F must map APIs to services/contracts |
| AI as governed assistant | Appendix G must map agents to Agent Contracts |
| MVP depth types | Chapter 28–30 and Appendix H must protect scope |
| Consumer classification | Product consumption contracts must declare consumer status |
| Appendix before core-specs | Detailed domain specs must wait for Appendix B |

---

# 35. Relationship to Appendices

This chapter directly governs Appendix B.

Appendix B shall include:

```text
26 baseline domains
four domain categories
domain purpose
domain owning canonical model
domain MVP depth
primary objects
primary services
primary events
AI usage
product consumers
deferred scope
cross-cutting systems note
```

Appendix A shall define all ontology terms.

Appendix C shall use domain ownership to index objects.

Appendix D shall use domain ownership to index services.

Appendix E shall use source domains to index events.

Appendix F shall treat APIs as consumption surfaces.

Appendix G shall treat AI agents as governed assistants.

Appendix H shall map Codex tasks to domains, cross-cutting systems and execution matrix rows.

---

# 36. Relationship to core-specs/

This chapter governs `core-specs/domains/`.

Every domain spec should include:

```text
Domain Purpose
Domain Responsibility
Domain Category
Owning Canonical Model
In Scope
Out of Scope
Primary Objects
Primary Services
Primary Events
Contracts
Permissions and Policies
AI Usage
Workflow Usage
Product Consumers
MVP Depth
Deferred Scope
Acceptance Criteria
```

`core-specs/domains/` must not create product-driven or implementation-driven domains outside the canonical baseline without architecture approval.

---

# 37. Exclusions

This chapter does not define:

```text
complete object fields
complete service inputs and outputs
final event payloads
API endpoints
AI prompts
workflow screens
product-specific journeys
pricing packages
deployment architecture
```

Those belong to later appendices, `core-specs/`, product books or implementation documents.

---

# 38. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines ontology clearly.
[ ] It distinguishes ontology from implementation.
[ ] It defines Core Domain clearly.
[ ] It preserves the 26 baseline Core Domains.
[ ] It groups domains into four categories.
[ ] It defines Foundation Domains.
[ ] It defines Professional Domains.
[ ] It defines Business Execution Domains.
[ ] It defines Collaboration Network Domains.
[ ] It clarifies Capability as cross-cutting.
[ ] It clarifies Business Responsibility as cross-cutting.
[ ] It distinguishes Domain from Object.
[ ] It distinguishes Domain from Service.
[ ] It distinguishes Domain from Event.
[ ] It distinguishes Domain from Product.
[ ] It distinguishes Domain from Workplace.
[ ] It distinguishes Domain from AI.
[ ] It distinguishes Domain from API.
[ ] It distinguishes Domain from Integration.
[ ] It defines MVP depth classification.
[ ] It defines consumer-based domain priority.
[ ] It defines domain dependency flow.
[ ] It defines domain governance rules.
[ ] It includes domain anti-patterns.
[ ] It supports Appendix B generation.
[ ] It supports second canonical draft rewrite plan.
```

---

# 39. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 08, defining ontology and domain classification. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened ontology layers, 26-domain baseline, cross-cutting system clarification, domain vs object/service/event/product/AI/API boundaries, MVP depth and Appendix B readiness. |

---

**End of Chapter**
