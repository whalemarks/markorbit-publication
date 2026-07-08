# Book 02

# 22 — Domain Specification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-22  
**Chapter Title:** Domain Specification  
**Part:** Part III — Core Specification System  
**Chapter Type:** Specification  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-08 — Ontology and Domain Classification
- B02-CH-13 — Core Domain Architecture
- B02-CH-14 — Core Object Architecture
- B02-CH-15 — Core Service Architecture
- B02-CH-16 — Core Execution Primitives
- B02-CH-17 — Core Contract Architecture
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-30 — MVP Execution Matrix
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines how Core Domains shall be specified in MarkOrbit.

Chapter 13 defined the Core Domain Architecture.

This chapter defines the required structure, rules and acceptance criteria for every Domain Specification.

A Domain Specification is the formal document that turns a Core Domain from an architectural concept into an executable specification unit.

It is not a product module description.

It is not a database schema.

It is not a UI feature list.

It is not a team ownership chart.

It is the canonical specification for a bounded area of shared professional meaning.

Domain Specifications are required before Core Objects, Services, Events, Contracts, APIs, AI Agents and Codex tasks can be safely generated.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit specify Core Domains so that each domain has clear meaning, boundary, ownership, relationships, execution assets, consumption rules and MVP depth?

The answer is:

> Every Core Domain shall be specified through a standard Domain Specification that defines its purpose, category, ownership, scope, relationships, objects, services, events, contracts, AI usage, product consumers, MVP depth, deferred scope and acceptance criteria.

---

# 3. Domain Specification Statement

A Domain Specification is:

> the canonical specification document for one bounded Core Domain or explicitly declared cross-cutting specification system.

It defines:

```text
what the domain means
why the domain exists
what the domain owns
what the domain does not own
which objects belong to it
which services operate it
which events originate from it
which contracts protect it
which AI capabilities may use it
which products consume it
what MVP depth applies
what remains deferred
```

The Domain Specification is the first executable specification layer after the manuscript and appendices.

---

# 4. Domain Specification Position

Domain Specification sits between Domain Architecture and executable implementation.

```text
Chapter 08 — Ontology and Domain Classification
        ↓
Chapter 13 — Core Domain Architecture
        ↓
Appendix B — Core Domain Index
        ↓
Domain Specification
        ↓
Object / Service / Event / Contract Specifications
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Implementation
```

The domain spec does not replace architecture chapters.

It operationalizes them.

---

# 5. Scope

## 5.1 In Scope

A Domain Specification defines:

```text
Domain identity
Domain purpose
Domain category
Canonical model alignment
Domain boundary
In-scope responsibilities
Out-of-scope responsibilities
Primary objects
Referenced objects
Primary services
Source events
Consumed events
Contracts
Permission and policy requirements
Knowledge dependencies
AI capability usage
Workflow and execution usage
Product consumers
MVP phase
MVP depth
Deferred scope
Acceptance criteria
Revision notes
```

## 5.2 Out of Scope

A Domain Specification does not define:

```text
complete object field schemas
full service implementation code
final event payload schemas
API route details
product UI
commercial pricing
vendor connector details
production prompts
implementation tickets
```

Those belong to Object, Service, Event, API, Agent, Product or Codex task specifications.

---

# 6. Domain Specification Applies To

Domain Specification applies to the canonical 26 baseline Core Domains.

```text
Foundation Domains
    Identity
    Organization
    User
    Permission
    Policy
    Knowledge

Professional Domains
    Brand
    Trademark
    Jurisdiction
    Classification
    Document
    Evidence

Business Execution Domains
    Customer
    Matter
    Order
    Opportunity
    Workflow Contract
    Task
    Event
    Notification

Collaboration Network Domains
    Partner
    Agent
    Service Provider
    Service Network
    Routing
    Communication
```

It may also apply to cross-cutting specification systems when needed.

```text
Capability
Business Responsibility
AI Governance
Core Consumption
```

Cross-cutting systems must be marked explicitly.

They must not silently change the 26-domain baseline.

---

# 7. Standard Domain Specification Template

Every Domain Specification should use the following structure.

```markdown
# [Domain Name] Domain Specification

**Domain ID:** [domain-id]
**Domain Name:** [Domain Name]
**Domain Category:** [Foundation / Professional / Business Execution / Collaboration Network / Cross-Cutting]
**Status:** Draft
**Version:** 0.1.0
**Owner:** MarkOrbit Core Architecture

---

## 1. Domain Purpose
## 2. Domain Definition
## 3. Domain Category
## 4. Canonical Model Alignment
## 5. Core Responsibilities
## 6. In Scope
## 7. Out of Scope
## 8. Domain Boundaries
## 9. Primary Objects
## 10. Referenced Objects
## 11. Core Services
## 12. Source Events
## 13. Consumed Events
## 14. Contracts
## 15. Permission and Policy Rules
## 16. Knowledge Dependencies
## 17. AI Capability Usage
## 18. Workflow and Execution Usage
## 19. Product Consumers
## 20. MVP Phase and Depth
## 21. Deferred Scope
## 22. Anti-Patterns
## 23. Acceptance Criteria
## 24. Revision Notes
```

This template becomes the basis for:

```text
core-specs/domains/_template.md
```

---

# 8. Required Metadata

Each Domain Specification must include stable metadata.

Required metadata:

```text
Domain ID
Domain Name
Domain Category
Domain Type
Status
Version
Owner
Related Chapters
Related Appendices
MVP Phase
MVP Depth
Product Consumers
```

## 8.1 Domain ID

Use lowercase kebab-case.

Examples:

```text
identity
trademark
workflow-contract
service-provider
business-responsibility
```

## 8.2 Domain Category

Allowed baseline categories:

```text
Foundation
Professional
Business Execution
Collaboration Network
```

Allowed special category:

```text
Cross-Cutting Specification System
```

## 8.3 Domain Type

Allowed domain types:

```text
Baseline Core Domain
Cross-Cutting Specification System
Reserved Future Domain
External Integration Boundary
```

## 8.4 MVP Depth

Allowed depth values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

---

# 9. Domain Purpose

The Domain Purpose explains why the domain exists.

It should answer:

```text
What professional meaning does this domain protect?
Why is this domain required by the Core?
Which problems would occur if this domain did not exist?
```

A good Domain Purpose is short, specific and architecture-oriented.

Example:

```text
The Trademark Domain defines shared professional meaning for trademark records, lifecycle status, jurisdictional context and trademark-related execution across MarkOrbit products.
```

A weak Domain Purpose is product-like.

```text
The Trademark Domain provides a page for users to view trademark information.
```

The second example is not acceptable.

---

# 10. Domain Definition

The Domain Definition states what the domain means in the Core.

It should be written as:

```text
[Domain Name] is the Core Domain that defines...
```

Example:

```text
Matter is the Core Domain that defines managed professional service cases created from orders and operated through tasks, events, workflow contracts and responsibility assignments.
```

A Domain Definition must not include:

```text
UI descriptions
sales language
implementation stack
vendor names
unclear product-specific terms
```

---

# 11. Domain Category

Each baseline domain belongs to one of four categories.

```text
Foundation Domains
Professional Domains
Business Execution Domains
Collaboration Network Domains
```

The category defines the domain’s architectural role.

It does not define product menu placement.

## 11.1 Foundation

Foundation domains support identity, authority, policy and knowledge.

## 11.2 Professional

Professional domains define trademark and brand professional meaning.

## 11.3 Business Execution

Business Execution domains turn professional meaning into managed work.

## 11.4 Collaboration Network

Collaboration Network domains support partners, agents, providers, routing and communication.

## 11.5 Cross-Cutting Specification System

Cross-cutting systems govern multiple domains.

They are not counted as ordinary baseline domains unless architecture governance approves a domain map change.

---

# 12. Canonical Model Alignment

Each domain should align with one or more Canonical Models.

Canonical Models include:

```text
Identity Model
Capability Model
Knowledge Model
Business Responsibility Model
Workplace Model
Network Model
```

Examples:

```text
Identity Domain
    aligns with Identity Model

Knowledge Domain
    aligns with Knowledge Model

Task Domain
    aligns with Workplace Model and Business Responsibility Model

Agent Domain
    aligns with Network Model and Capability Model

Classification Domain
    aligns with Knowledge Model and Capability Model
```

Canonical Model alignment helps maintain conceptual consistency across domains.

---

# 13. Core Responsibilities

Core Responsibilities define what the domain owns.

A domain may own:

```text
meaning
primary objects
object lifecycle
core services
source events
contracts
rules
AI usage boundaries
product consumption boundaries
```

Example for Matter:

```text
Matter owns the meaning and lifecycle of managed professional service cases.
Matter owns Matter Object specification.
Matter owns MatterCreated and MatterStatusChanged source events.
Matter owns Matter-related service responsibility.
Matter participates in Workflow Contract and Task execution.
```

Core Responsibilities must be stated clearly enough for Object, Service and Event specs to derive from them.

---

# 14. In Scope

The In Scope section lists what the domain includes.

It should be concrete.

Example:

```text
In Scope:
- Matter identity
- Matter lifecycle
- Matter status
- Matter relationship to Order, Customer and Trademark
- Matter task and event linkage
- Matter responsibility context
- Matter workflow contract usage
```

In Scope should not include product UI or implementation details.

---

# 15. Out of Scope

The Out of Scope section prevents domain expansion.

Example:

```text
Out of Scope:
- product-specific case dashboard design
- pricing and billing logic
- final UI workflow
- external provider marketplace operation
- full analytics dashboard
```

Out of Scope must be included in every domain spec.

It protects MVP boundary and future architecture.

---

# 16. Domain Boundaries

The Domain Boundaries section explains how the domain relates to neighboring domains.

It should include:

```text
what this domain owns
what related domains own
what references are allowed
what ownership transfer is prohibited
```

Example:

```text
Matter references Trademark but does not own Trademark meaning.
Matter references Order but does not own Order creation rules.
Matter uses Task but does not redefine Task meaning.
Matter may publish Matter events but does not own all events related to its tasks.
```

Boundary rules prevent domain collapse.

---

# 17. Primary Objects

The Primary Objects section lists objects owned by the domain.

Each object should later have an Object Specification.

Example:

```text
Primary Objects:
- Matter
- Matter Status
- Matter Context
```

Rules:

```text
Every primary object must have one owning domain or cross-cutting system.
Do not list objects that are only referenced.
Do not list UI objects.
Do not list database tables as objects unless they represent Core meaning.
```

---

# 18. Referenced Objects

The Referenced Objects section lists objects from other domains that this domain uses.

Example:

```text
Referenced Objects:
- Customer
- Order
- Trademark
- Jurisdiction
- Task
- Document
- Event
- Responsibility Assignment
```

Reference does not transfer ownership.

Referenced objects must retain their owning domain.

---

# 19. Core Services

The Core Services section lists services owned or primarily governed by the domain.

Example:

```text
Core Services:
- Matter Creation Service
- Matter Status Update Service
- Matter Context Retrieval Service
- Order-to-Matter Conversion Service
```

For each service, the domain spec should indicate:

```text
service purpose
objects read
objects created or updated
events emitted
permission requirements
AI usage if any
human review if required
```

Detailed service fields belong to Service Specifications.

---

# 20. Source Events

The Source Events section lists events originated by the domain.

Example:

```text
Source Events:
- MatterCreated
- MatterStatusChanged
- MatterClosed
```

A source event must have:

```text
source domain
trigger
related objects
payload contract
downstream consumers
audit requirement
```

Detailed event payloads belong to Event Specifications.

---

# 21. Consumed Events

The Consumed Events section lists events from other domains that this domain may react to.

Example:

```text
Consumed Events:
- OrderConfirmed
- OrderConvertedToMatter
- TaskCompleted
- DocumentUploaded
- ReviewApproved
```

Consumed Events should not imply ownership.

They only describe dependency or reaction.

---

# 22. Contracts

The Contracts section lists contract types required to protect domain consumption.

Possible contracts:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
```

Example:

```text
Contracts:
- Matter Data Contract
- Matter API Contract
- Matter Event Contract
- Workplace Matter Consumption Contract
- MarkReg Matter Consumption Contract
```

A domain without contracts is not ready for product consumption.

---

# 23. Permission and Policy Rules

Every domain must define permission and policy expectations.

Examples:

```text
Who may read domain objects?
Who may create domain objects?
Who may update domain state?
Who may approve or reject related actions?
Which AI agents may access domain objects?
Which external consumers may access domain data?
```

Policy may include:

```text
review rules
AI risk rules
jurisdictional rules
external sharing rules
retention rules
```

Detailed permission implementation may belong to Permission and Policy specs.

But each domain must state its requirements.

---

# 24. Knowledge Dependencies

A domain may depend on knowledge.

Examples:

```text
Jurisdiction depends on official and professional jurisdiction knowledge.
Classification depends on goods/services classification knowledge.
Document depends on document requirement knowledge.
Evidence depends on sufficiency and use evidence knowledge.
AI agents depend on authorized knowledge sources.
```

A Domain Specification should list:

```text
required knowledge types
authorized knowledge sources
knowledge validation requirement
knowledge gaps
AI knowledge access constraints
```

Knowledge dependency must not be hidden inside prompts.

---

# 25. AI Capability Usage

A domain may allow AI capability usage.

AI usage must be governed by Agent Contracts.

A Domain Specification should define:

```text
allowed AI capabilities
prohibited AI capabilities
authorized agents
knowledge sources
object access
output types
risk level
human review requirement
events
audit
```

Example:

```text
Classification Domain may allow Classification Assistant Agent to recommend classes and goods/services terms.
The AI output must include confidence, rationale, knowledge source and review_required flag when risk requires review.
```

AI must not own domain meaning.

---

# 26. Workflow and Execution Usage

A domain may participate in workflow or execution.

Examples:

```text
Order participates in order confirmation and order-to-matter conversion.
Matter participates in matter execution workflow.
Task participates in assignment and completion.
Document participates in draft and review workflow.
AI Output participates in review workflow.
Routing participates in routing review workflow.
```

The Domain Specification should define:

```text
workflow contracts used
states involved
tasks created
events emitted
responsibility requirements
review requirements
```

Detailed workflow states belong to Workflow Contract specs.

---

# 27. Product Consumers

The Product Consumers section defines which products or systems consume the domain.

Consumers may be classified as:

```text
MVP Consumer
Partial Consumer
Future Consumer
```

MVP consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Partial consumers:

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

Future consumers:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

The domain spec should define read/write boundaries for each consumer.

---

# 28. MVP Phase and Depth

Every domain must state its MVP phase and depth.

MVP phases:

```text
Phase 1 — Foundation Core
Phase 2 — Professional Core
Phase 3 — Business Execution Core
Phase 4 — Growth Core
Phase 5 — Network Core
```

MVP depth:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

The domain spec should also explain why the phase and depth were chosen.

---

# 29. Deferred Scope

Every domain must define deferred scope.

Deferred scope prevents overbuilding.

Examples:

```text
Opportunity Domain deferred scope:
- advanced opportunity scoring
- full revenue attribution
- automated campaign execution

Agent Domain deferred scope:
- advanced provider ranking
- full agent marketplace
- automated trust scoring

Evidence Domain deferred scope:
- final legal sufficiency engine
- automatic filing decision
```

Deferred scope is not forgotten.

It is protected for future architecture releases.

---

# 30. Domain Anti-Patterns

Every Domain Specification should include anti-patterns.

Common anti-patterns:

```text
Product module as domain
Database table as domain
UI screen as domain
AI agent as domain owner
Workflow screen as domain
Commercial package as domain
External vendor connector as domain
Reporting metric as domain meaning
Cross-cutting system treated as hidden domain
Future marketplace scope pulled into MVP
```

Anti-patterns must be specific to the domain where possible.

---

# 31. Domain Specification Rules

The following rules apply to every Domain Specification.

## Rule 1 — Each baseline domain must have one domain spec

Every one of the 26 baseline domains should have a Domain Specification.

## Rule 2 — Cross-cutting systems must be marked explicitly

Capability and Business Responsibility must not silently change the domain count.

## Rule 3 — Every domain must define scope and exclusions

In Scope and Out of Scope are mandatory.

## Rule 4 — Every domain must list primary objects

Objects cannot be created without domain ownership.

## Rule 5 — Every domain must list services and events

Services and events must trace back to domains or cross-cutting systems.

## Rule 6 — Every domain must define consumers

Product, AI, Workplace and Codex consumption must be explicit.

## Rule 7 — Every domain must declare MVP depth

Implementation depth must be controlled.

## Rule 8 — Every domain must define deferred scope

Future features must not leak into MVP.

## Rule 9 — Every domain must define AI boundaries where AI is used

AI cannot be prompt-only.

## Rule 10 — Every domain spec must include acceptance criteria

A domain spec is not complete without testable acceptance criteria.

---

# 32. Domain Spec File Naming

Domain spec files should use lowercase kebab-case.

Examples:

```text
core-specs/domains/identity.md
core-specs/domains/organization.md
core-specs/domains/trademark.md
core-specs/domains/workflow-contract.md
core-specs/domains/service-provider.md
core-specs/domains/communication.md
```

Cross-cutting systems may be handled by index classification or future folder design.

MVP recommendation:

```text
Do not create hidden extra baseline domains.
Classify cross-cutting systems in Appendix B and relevant indexes.
Create executable artifacts under objects/, services/, events/ and contracts/ as needed.
```

---

# 33. Domain Specification Acceptance Criteria

A Domain Specification is accepted only if it satisfies the following criteria.

```text
[ ] Domain ID and name are stable.
[ ] Domain category is valid.
[ ] Domain purpose is clear.
[ ] Domain definition is not product-specific.
[ ] Canonical model alignment is stated.
[ ] Core responsibilities are defined.
[ ] In Scope is defined.
[ ] Out of Scope is defined.
[ ] Boundaries with adjacent domains are defined.
[ ] Primary objects are listed.
[ ] Referenced objects are listed.
[ ] Core services are listed.
[ ] Source events are listed.
[ ] Consumed events are listed where relevant.
[ ] Contracts are listed.
[ ] Permission and policy requirements are stated.
[ ] Knowledge dependencies are stated where relevant.
[ ] AI usage is governed or explicitly excluded.
[ ] Workflow/execution usage is stated where relevant.
[ ] Product consumers are classified.
[ ] MVP phase and depth are stated.
[ ] Deferred scope is stated.
[ ] Anti-patterns are included.
[ ] Revision notes are included.
```

---

# 34. Relationship to Appendix B

Appendix B — Core Domain Index is the domain inventory.

Domain Specifications are detailed files generated from that inventory.

The relationship is:

```text
Appendix B lists domains.
Domain Specs define domains.
Object/Service/Event specs execute domain meaning.
```

Appendix B must be completed before detailed domain specs are generated.

---

# 35. Relationship to Object Specification

Object Specification depends on Domain Specification.

Every Object Specification must reference:

```text
owning domain
or cross-cutting system
```

No Core Object should exist without a domain or cross-cutting owner.

---

# 36. Relationship to Service Specification

Service Specification depends on Domain Specification.

Every Service Specification must reference:

```text
owning domain
objects read
objects created or updated
events emitted
contracts required
```

No Core Service should exist without domain or cross-cutting responsibility.

---

# 37. Relationship to Event Specification

Event Specification depends on Domain Specification.

Every Event Specification must reference:

```text
source domain
trigger
related objects
payload contract
consumers
```

No Core Event should exist without source ownership.

---

# 38. Relationship to AI Governance

AI agents consume domain context.

They do not own domain meaning.

Domain Specifications must identify AI usage and risk boundaries before Agent Specs are generated.

The relationship is:

```text
Domain defines context.
Agent Contract defines allowed AI behavior.
Service defines governed execution.
Event and Audit record meaningful output.
Human review controls risk.
```

---

# 39. Relationship to Codex

Codex shall not generate a domain spec without source authority.

Every Codex task creating or modifying a Domain Specification must reference:

```text
Chapter 08
Chapter 13
Appendix B
this Chapter 22
MVP Execution Matrix row
acceptance criteria
```

Codex must not invent new baseline domains.

If a missing domain appears necessary, Codex must create an architecture issue, not implement the domain directly.

---

# 40. Specification Output

This chapter produces the following specification outputs:

```text
Domain Specification definition
Domain Specification position
Standard Domain Specification template
Required domain metadata
Domain purpose rules
Domain definition rules
Domain category rules
Canonical Model alignment rules
Core responsibility rules
Scope and exclusion rules
Boundary rules
Primary and referenced object rules
Service rules
Event rules
Contract rules
Permission and policy rules
Knowledge dependency rules
AI usage rules
Workflow usage rules
Product consumer rules
MVP phase and depth rules
Deferred scope rules
Domain anti-patterns
Domain spec file naming rules
Domain spec acceptance criteria
Relationship to Appendix B
Relationship to Object, Service and Event specs
Relationship to AI Governance
Relationship to Codex
```

---

# 41. Execution Mapping

| Domain Spec Element | Execution Impact |
|--------------------|------------------|
| Domain ID | file name and references |
| Domain Category | architecture classification |
| Domain Purpose | object/service/event meaning |
| In Scope / Out of Scope | prevents scope drift |
| Primary Objects | drives Object Specs |
| Core Services | drives Service Specs |
| Source Events | drives Event Specs |
| Contracts | drives consumption rules |
| Permission / Policy | drives access control |
| Knowledge Dependencies | drives Knowledge usage |
| AI Usage | drives Agent Contracts |
| MVP Depth | drives implementation depth |
| Deferred Scope | protects future scope |
| Acceptance Criteria | drives review and tests |

---

# 42. Relationship to core-specs/

This chapter becomes the source for:

```text
core-specs/domains/_template.md
```

It also governs all files under:

```text
core-specs/domains/
```

No detailed domain spec should be generated until Appendix B is complete.

No Codex task should implement a domain without referencing this chapter and the relevant Domain Specification.

---

# 43. Exclusions

This chapter shall not define:

```text
all final domain specs
complete object schemas
complete service contracts
complete event payloads
API endpoint routes
AI prompt templates
product UI behavior
deployment architecture
implementation code
```

Those belong to appendices, `core-specs/` and implementation documents.

---

# 44. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines Domain Specification clearly.
[ ] It provides a standard Domain Specification template.
[ ] It preserves the 26-domain baseline.
[ ] It handles cross-cutting systems explicitly.
[ ] It requires metadata, purpose, definition and category.
[ ] It requires scope and exclusions.
[ ] It requires primary and referenced objects.
[ ] It requires services, events and contracts.
[ ] It requires permission, policy and knowledge dependency rules.
[ ] It requires AI usage governance where AI is used.
[ ] It requires product consumer classification.
[ ] It requires MVP phase, depth and deferred scope.
[ ] It defines anti-patterns.
[ ] It defines file naming rules.
[ ] It links Domain Specification to Appendix B.
[ ] It links Domain Specification to Object, Service and Event specs.
[ ] It links Domain Specification to AI Governance and Codex.
[ ] It supports future `core-specs/domains/_template.md` generation.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 45. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 22, defining Domain Specification. |
| 0.2.0 | Draft | Second canonical draft rewrite. Converted Domain Specification into a template-ready, Codex-safe, appendix-dependent specification standard with explicit cross-cutting system, MVP depth, AI governance and consumer rules. |

---

**End of Chapter**
