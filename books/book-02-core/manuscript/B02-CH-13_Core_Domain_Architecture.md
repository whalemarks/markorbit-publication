# Book 02

# 13 — Core Domain Architecture

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-13  
**Chapter Title:** Core Domain Architecture  
**Part:** Part II — Core Kernel Architecture  
**Chapter Type:** Architecture  
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

This chapter defines the Core Domain Architecture of MarkOrbit.

Chapter 08 defined the ontology and domain classification model.

This chapter defines how Core Domains are organized, governed, related, prioritized and prepared for executable specifications.

A Core Domain is not a product module.

A Core Domain is not a database schema.

A Core Domain is not a UI section.

A Core Domain is not a team responsibility chart.

A Core Domain is a bounded area of shared professional meaning owned by the Core.

The purpose of this chapter is to make the domain architecture stable enough to support:

```text
Appendix B — Core Domain Index
core-specs/domains/
Core Object Architecture
Core Service Architecture
Event Specification
AI Governance
Core Consumption Contracts
MVP Execution Matrix
Codex Task Generation
```

This chapter therefore acts as the bridge between the conceptual domain map and executable domain specs.

---

# 2. Core Question

This chapter answers one question:

> How should MarkOrbit organize Core Domains so that shared professional meaning remains stable while products, AI agents, Workplaces and Codex implementations can consume the Core safely?

The answer is:

> MarkOrbit shall organize Core Domains into a canonical 26-domain baseline, grouped by architectural responsibility, governed by clear ownership rules, connected through Core Objects, Services, Events and Contracts, and prioritized by MVP execution depth.

---

# 3. Domain Architecture Statement

The MarkOrbit Core Domain Architecture is defined by the following statement:

```text
Core Domains are bounded areas of shared professional meaning.
They organize Core Objects, Services, Events, Contracts, AI usage and product consumption.
They are stable enough to protect architecture and flexible enough to support implementation.
```

The domain architecture must satisfy five requirements.

```text
1. It must preserve the canonical 26-domain baseline.
2. It must separate domains from products, UI, data tables and workflows.
3. It must classify cross-cutting systems without changing the domain count.
4. It must support MVP execution and future expansion.
5. It must be executable through appendices, core-specs and Codex tasks.
```

---

# 4. Canonical Domain Baseline

The canonical baseline Core Domain Map contains 26 domains.

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

This 26-domain map is the baseline domain architecture for Book 02.

It must not be changed silently by implementation, product design, AI agent design, or Codex tasks.

Any change to the baseline domain map requires architecture review.

---

# 5. Cross-Cutting Specification Systems

Book 02 recognizes two important cross-cutting systems:

```text
Capability
Business Responsibility
```

These systems are not counted as additional baseline Core Domains in the 26-domain map.

They are cross-cutting Core specification systems.

They may produce executable specs, objects, services, events and contracts.

They govern multiple domains.

## 5.1 Capability

Capability describes what can be performed, by whom or by what actor.

Capability may apply to:

```text
human users
internal teams
AI agents
foreign agents
service providers
products
workflow roles
network participants
```

Capability may produce artifacts such as:

```text
Capability Object
Capability Provider
Capability Scope
Capability Matching Service
Capability Contract
Capability-related events
```

But Capability remains cross-cutting unless a later architecture release explicitly promotes it into the baseline domain map.

## 5.2 Business Responsibility

Business Responsibility defines accountability for work.

It may apply to:

```text
order ownership
matter ownership
task assignment
review responsibility
AI output approval
routing approval
opportunity follow-up
agent communication
network cooperation
```

Business Responsibility may produce artifacts such as:

```text
Responsibility Assignment
Review Record
ReviewRequired Event
Review Approval Service
Responsibility Contract
```

It is not the same as commercial pricing, commission, margin or revenue attribution.

Business Responsibility governs accountability.

Business policy governs commercial value.

---

# 6. Domain Categories

The 26 domains are grouped into four categories.

Each category answers a different architectural question.

```text
Foundation Domains
    Who can act, under what permission, using what knowledge?

Professional Domains
    What professional objects and rules are being operated?

Business Execution Domains
    How does professional work become orders, matters, tasks, events and notifications?

Collaboration Network Domains
    How does the platform connect partners, agents, providers, routing and communication?
```

The categories are not product modules.

They are architecture layers of professional meaning.

---

# 7. Foundation Domains

Foundation Domains support identity, authority and knowledge.

They are required before professional and execution domains can operate reliably.

## 7.1 Identity

Identity defines who or what an actor is.

It supports:

```text
human user identity
organization identity
AI agent identity
external agent identity
service provider identity
system actor identity
```

Identity is foundational for permission, audit, responsibility and AI governance.

## 7.2 Organization

Organization defines business entities and structural ownership.

It supports:

```text
client companies
agency organizations
service provider organizations
partner organizations
internal teams
```

Organization provides context for users, customers, agents and partners.

## 7.3 User

User defines human actors operating in MarkOrbit.

It supports:

```text
internal users
partner users
client users
agent users
reviewers
operators
administrators
```

User links Identity, Organization, Role, Permission and Responsibility.

## 7.4 Permission

Permission governs what actors may read, create, update, approve, export or invoke.

It supports:

```text
object access
service invocation
AI access
document visibility
workflow action control
external sharing
```

Permission is required before any serious implementation.

## 7.5 Policy

Policy defines rules that influence decisions and constraints.

It supports:

```text
review rules
AI risk rules
data sharing rules
jurisdiction rules
business constraints
workflow constraints
```

Policy is partial in the Core MVP but must be reserved early.

## 7.6 Knowledge

Knowledge defines governed professional knowledge.

It supports:

```text
knowledge sources
knowledge assets
jurisdiction requirements
classification references
document requirements
professional rules
AI-authorized knowledge
knowledge gaps
```

Knowledge is the foundation for AI-assisted professional work.

---

# 8. Professional Domains

Professional Domains define the trademark and brand professional objects MarkOrbit operates.

## 8.1 Brand

Brand defines the business identity or market-facing identity that trademark work protects.

It supports:

```text
brand name
brand owner
brand assets
brand markets
brand portfolio context
```

Brand connects client business intention to trademark execution.

## 8.2 Trademark

Trademark defines mark-related professional meaning.

It supports:

```text
mark text
mark image
serial number
registration number
jurisdiction
status
owner
goods/services
filing/registration lifecycle
```

Trademark is a central professional domain for MarkReg and Lite.

## 8.3 Jurisdiction

Jurisdiction defines country, region or office-specific professional context.

It supports:

```text
country or region
trademark office
filing rules
document requirements
classification constraints
official procedures
local practice differences
```

Jurisdiction prevents global trademark logic from becoming one-size-fits-all.

## 8.4 Classification

Classification defines goods and services classification meaning.

It supports:

```text
Nice classes
local classification rules
goods/services terms
class recommendations
validation
review requirement
AI classification assistance
```

Classification must be governed because it directly affects filing scope and professional risk.

## 8.5 Document

Document defines files and generated materials used in professional service execution.

It supports:

```text
POA
application materials
official documents
evidence files
draft letters
office action documents
certificates
translations
generated documents
```

Document connects professional work to artifacts.

## 8.6 Evidence

Evidence defines proof materials and evidence packages.

It supports:

```text
use evidence
ownership evidence
sales evidence
website screenshots
platform evidence
agent records
documented proof sets
```

Evidence is partial in MVP but must be clearly reserved because it affects high-risk professional judgment.

---

# 9. Business Execution Domains

Business Execution Domains turn professional objects into managed work.

## 9.1 Customer

Customer defines the person or organization receiving service.

It supports:

```text
client identity
client organization
contact context
service relationship
brand/trademark linkage
order linkage
matter linkage
```

Customer is not merely a CRM record.

It is a Core business execution actor.

## 9.2 Matter

Matter defines a managed professional service case.

It supports:

```text
case identity
customer linkage
order linkage
trademark linkage
jurisdiction
service type
status
tasks
documents
events
responsibility
workflow context
```

Matter is central to Workplace and MarkReg.

## 9.3 Order

Order defines a confirmed or pending service request.

It supports:

```text
service request
customer
brand/trademark context
jurisdiction
service type
requirements
commercial readiness
conversion to matter
```

Order connects intake and business commitment to execution.

## 9.4 Opportunity

Opportunity defines potential business value or follow-up opportunity.

It supports:

```text
opportunity signal
customer follow-up
trademark portfolio need
jurisdiction expansion
renewal opportunity
service recommendation
AI opportunity discovery
```

Opportunity is partial in MVP and should not become a full scoring engine early.

## 9.5 Workflow Contract

Workflow Contract defines allowed execution states and transitions.

It supports:

```text
order-to-matter conversion
matter execution baseline
AI recommendation review
document draft review
routing review
opportunity follow-up
```

Workflow Contract is not a product screen flow.

It is Core execution governance.

## 9.6 Task

Task defines work to be performed.

It supports:

```text
assignment
due dates
review
completion
matter linkage
workflow linkage
responsibility
notification
event generation
```

Task is a Core execution primitive.

## 9.7 Event

Event defines meaningful change.

It supports:

```text
state change
task action
matter lifecycle
document generation
AI recommendation
review requirement
routing decision
communication linkage
```

Event is a Core execution primitive, not a log.

## 9.8 Notification

Notification defines baseline user or system alerting.

It supports:

```text
task assignment
review required
deadline reminder
status change
routing decision
communication update
```

Notification is partial in MVP but required as an execution support domain.

---

# 10. Collaboration Network Domains

Collaboration Network Domains prepare MarkOrbit for external agent and service provider collaboration.

## 10.1 Partner

Partner defines business partners participating in service or channel relationships.

It supports:

```text
agency partners
channel partners
cooperation partners
network participants
```

Partner is primarily future/reserved in MVP.

## 10.2 Agent

Agent defines professional agents or law firms that can perform trademark-related work.

It supports:

```text
foreign agents
local associates
jurisdiction coverage
capability
communication
routing
service quality context
```

Agent is needed for MarkReg and MGSN but should be carefully scoped.

## 10.3 Service Provider

Service Provider defines entities providing services inside or outside the network.

It supports:

```text
legal service providers
translation providers
document providers
data providers
AI service providers
technology providers
```

Service Provider is partial in MVP.

## 10.4 Service Network

Service Network defines network-level collaboration structure.

It supports:

```text
network membership
service exchange
provider participation
trust framework
collaboration channels
```

Service Network is reserved in MVP and belongs more fully to Book 06.

## 10.5 Routing

Routing defines how work, matters or recommendations are directed to agents or providers.

It supports:

```text
agent recommendation
service provider selection
jurisdiction routing
capability routing
review-required routing
AI routing assistance
```

Routing should be governed because it affects business responsibility and service quality.

## 10.6 Communication

Communication defines linked professional communication.

It supports:

```text
emails
messages
calls
agent communication
client communication
matter communication
communication summaries
AI-assisted communication review
```

Communication connects professional context to execution records.

---

# 11. Domain Dependency Model

Core Domains are not isolated.

They form a dependency chain.

```text
Identity
↓
Organization / User
↓
Permission / Policy
↓
Knowledge
↓
Brand / Trademark / Jurisdiction / Classification / Document / Evidence
↓
Customer / Order / Matter
↓
Workflow Contract / Task / Event / Notification
↓
Communication / Agent / Service Provider / Routing / Opportunity
↓
Partner / Service Network
```

This dependency chain guides MVP sequencing and Codex implementation.

It also prevents implementation from building high-level network or opportunity features before identity, knowledge, professional objects and execution primitives are stable.

---

# 12. Domain Ownership Rules

Every domain must have an ownership rule.

A domain owns:

```text
its Core meaning
its primary objects
its primary services
its source events
its domain-specific contracts
its MVP depth
its AI usage boundary
its product consumption boundary
```

A domain does not own:

```text
product UI
database implementation details
commercial packaging
vendor adapters
ungoverned AI behavior
external reporting definitions
```

Domain ownership must be stated in `core-specs/domains/`.

---

# 13. Domain Relationship Rules

Domains relate through governed references.

They must not collapse into each other.

Examples:

```text
Customer may reference Identity and Organization.
Trademark may reference Brand and Jurisdiction.
Order may reference Customer, Brand, Trademark, Jurisdiction and Service Type.
Matter may reference Order, Customer, Trademark and Workflow Contract.
Task may reference Matter, User, Responsibility and Event.
Event may reference any related Core Object but keeps its own source domain.
Routing may reference Agent, Service Provider, Jurisdiction and Capability.
Communication may reference Matter, Customer, Agent or Task.
```

The rule is:

```text
Reference does not transfer ownership.
```

For example:

```text
Matter references Trademark.
Matter does not own Trademark meaning.

Task references User.
Task does not own User meaning.

Routing references Agent.
Routing does not own Agent meaning.
```

---

# 14. Domain-to-Object Relationship

Domains organize Core Objects.

Every Core Object must declare:

```text
owning domain
or cross-cutting specification system
object purpose
identity rule
lifecycle rule
relationship rule
permission rule
event rule
AI usage rule
consumer boundary
```

Examples:

```text
Trademark Object
    owning domain: Trademark

Matter Object
    owning domain: Matter

Task Object
    owning domain: Task

Routing Decision Object
    owning domain: Routing

Agent Contract
    owning system: AI Governance / Contract

Capability Object
    owning system: Capability cross-cutting system

Responsibility Assignment
    owning system: Business Responsibility cross-cutting system
```

This protects the domain architecture from unowned objects.

---

# 15. Domain-to-Service Relationship

Domains own service responsibility.

Every Core Service must declare:

```text
owning domain
or cross-cutting system
objects read
objects created or updated
events emitted
contracts required
permission and policy requirements
AI usage
human review requirement
failure behavior
```

Examples:

```text
Trademark Status Normalization Service
    owning domain: Trademark

Classification Recommendation Service
    owning domain: Classification

Order-to-Matter Conversion Service
    owning domains: Order / Matter
    primary owner: Matter or Workflow Contract, depending on final spec decision

Task Assignment Service
    owning domain: Task

Routing Decision Service
    owning domain: Routing

Review Assignment Service
    owning system: Business Responsibility
```

Where a service crosses domains, the spec must name a primary owner.

---

# 16. Domain-to-Event Relationship

Domains produce source events.

Every Core Event must declare:

```text
source domain
trigger
related objects
payload contract
consumer domains
audit requirement
retention/replay rule
```

Examples:

```text
TrademarkCreated
    source domain: Trademark

OrderCreated
    source domain: Order

OrderConvertedToMatter
    source domain: Order or Workflow Contract, depending on final event spec

MatterCreated
    source domain: Matter

TaskAssigned
    source domain: Task

AIRecommendationReviewRequired
    source system: AI Governance / Business Responsibility

RoutingDecisionMade
    source domain: Routing
```

Events may be consumed across domains.

But event source ownership must remain clear.

---

# 17. Domain-to-Contract Relationship

Domains are protected by contracts.

Domain-related contracts may include:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
```

Examples:

```text
Trademark Data Contract
Classification Recommendation API Contract
Document Data Contract
Matter Event Contract
AI Agent Contract
MarkReg Core Consumption Contract
Lite Core Consumption Contract
Workplace Core Consumption Contract
```

Contracts allow other layers to consume domain meaning without redefining it.

---

# 18. Domain-to-AI Relationship

Domains may authorize AI usage.

AI does not own domain meaning.

AI may assist domains through Agent Contracts.

Examples:

```text
Classification domain
    Classification Assistant Agent

Document domain
    Document Draft Assistant Agent

Trademark domain
    Trademark Status Summary Agent

Evidence domain
    Evidence Review Assistant Agent

Communication domain
    Communication Summary Agent

Routing domain
    Routing Assistant Agent

Opportunity domain
    Opportunity Discovery Agent
```

Every AI-domain relationship must define:

```text
authorized knowledge
allowed objects
allowed services
output type
risk level
human review rule
events
audit
product consumers
```

---

# 19. Domain-to-Product Relationship

Products consume domains through contracts.

Products do not own domains.

## 19.1 MarkReg

MarkReg consumes:

```text
Customer
Trademark
Jurisdiction
Classification
Document
Evidence
Order
Matter
Workflow Contract
Task
Event
Agent
Communication
AI Governance
```

## 19.2 MarkOrbit Lite

Lite consumes:

```text
Identity
Customer
Brand
Trademark
Jurisdiction
Classification
Knowledge
Document
Order
AI Governance
```

## 19.3 Workplace

Workplace consumes:

```text
Identity
User
Permission
Matter
Task
Event
Workflow Contract
Business Responsibility
Notification
AI Governance
```

## 19.4 MGSN

MGSN consumes:

```text
Partner
Agent
Service Provider
Service Network
Routing
Communication
Capability
Responsibility
```

In MVP, MGSN remains partial or reserved.

---

# 20. MVP Domain Depth

Domains are implemented at different depths.

Book 02 uses four MVP depth types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 20.1 Must Implement

A domain must be implemented when first consumers cannot operate without it.

Examples:

```text
Identity
Organization
User
Permission
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Customer
Order
Matter
Workflow Contract
Task
Event
```

## 20.2 Partial Implement

A domain or system must be specified and partially implemented when it is needed but not yet complete.

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
Capability
Business Responsibility
```

## 20.3 Reserved Boundary

A domain must be reserved when future architecture depends on it but MVP should not build it deeply.

Examples:

```text
Partner
Service Network
full MGSN operation
advanced network trust
external marketplace behavior
```

## 20.4 Deferred

A domain feature is deferred when it belongs to future releases.

Examples:

```text
full global agent marketplace
advanced provider ranking
full opportunity scoring
full brand asset vault
full external integration platform
advanced analytics
full AI autonomy
```

---

# 21. Domain Governance

Domain governance ensures that the domain architecture does not drift.

A domain change requires review when it:

```text
adds a new baseline domain
renames a baseline domain
changes domain category
moves an object between domains
changes event source ownership
changes service ownership
expands MVP scope
adds AI authority
changes product consumption boundaries
```

Domain governance outputs include:

```text
architecture issue
domain review decision
updated Appendix B
updated core-specs/domain file
updated object/service/event indexes
updated Codex task dependency
```

---

# 22. Domain Anti-Patterns

## 22.1 Product Module as Domain

A product module is treated as a Core Domain.

Correction:

```text
Product modules consume domains.
They are not domains by default.
```

## 22.2 Database Table as Domain

A data table becomes a domain.

Correction:

```text
Domains own meaning, not storage layout.
```

## 22.3 AI Agent as Domain

An AI agent is treated as a domain owner.

Correction:

```text
AI agents consume domain context under Agent Contracts.
```

## 22.4 Workflow Screen as Domain

A workflow screen becomes a domain.

Correction:

```text
Workflow Contract is Core.
Screens belong to product or Workplace.
```

## 22.5 Cross-Cutting System Becomes Hidden Domain

Capability or Business Responsibility silently expands the domain count.

Correction:

```text
Classify them as cross-cutting systems unless architecture release changes the domain map.
```

## 22.6 Future Marketplace Pulls MVP Scope

MGSN marketplace concepts force early implementation.

Correction:

```text
Use Reserved Boundary or Deferred classification.
```

---

# 23. Appendix B Readiness

This chapter prepares Appendix B — Core Domain Index.

Appendix B must include:

```text
domain name
domain category
domain purpose
owning canonical model
primary objects
primary services
primary events
contracts
AI usage
MVP phase
MVP depth
product consumers
deferred scope
```

Appendix B must also include:

```text
26-domain baseline statement
cross-cutting system clarification
domain change governance note
```

---

# 24. Relationship to Other Architecture Chapters

## 24.1 Relationship to Chapter 12 — Canonical Models

Canonical Models define broad architecture meaning.

Domains organize that meaning into bounded areas.

## 24.2 Relationship to Chapter 14 — Core Object Architecture

Domains own Core Objects.

Object Architecture depends on Domain Architecture.

## 24.3 Relationship to Chapter 15 — Core Service Architecture

Domains own service responsibility.

Service Architecture depends on Domain Architecture.

## 24.4 Relationship to Chapter 16 — Core Execution Primitives

Execution primitives such as Task, Event, State and Workflow Contract are domain-governed but cross execution boundaries.

## 24.5 Relationship to Chapter 17 — Core Contract Architecture

Contracts protect domains from uncontrolled consumption.

## 24.6 Relationship to Chapter 30 — MVP Execution Matrix

The execution matrix converts domains into implementable assets.

---

# 25. Specification Output

This chapter produces the following specification outputs:

```text
Canonical 26-domain baseline
Domain category model
Cross-cutting specification system rule
Foundation Domain architecture
Professional Domain architecture
Business Execution Domain architecture
Collaboration Network Domain architecture
Domain dependency model
Domain ownership rules
Domain relationship rules
Domain-to-object mapping rules
Domain-to-service mapping rules
Domain-to-event mapping rules
Domain-to-contract mapping rules
Domain-to-AI mapping rules
Domain-to-product mapping rules
MVP domain depth model
Domain governance rules
Domain anti-patterns
Appendix B readiness requirements
```

---

# 26. Execution Mapping

| Domain Architecture Decision | Execution Impact |
|------------------------------|------------------|
| 26-domain baseline | Appendix B and `core-specs/domains/` must preserve it |
| Cross-cutting systems | Capability and Business Responsibility need special indexing |
| Domain ownership | Objects/services/events must declare owner |
| Domain dependencies | Codex task sequencing follows dependency chain |
| MVP depth | Execution Matrix defines implementation depth |
| Domain-to-AI mapping | Agent Contracts must reference domain context |
| Domain-to-product mapping | Consumption Contracts must protect domain meaning |
| Domain governance | Changes require architecture review |

---

# 27. Relationship to core-specs/

This chapter governs the future `core-specs/domains/` scaffold.

Each domain spec should include:

```text
Domain Purpose
Domain Category
Canonical Model Alignment
MVP Phase
MVP Depth
Primary Objects
Primary Services
Primary Events
Contracts
AI Usage
Workflow Usage
Product Consumers
Out of Scope
Deferred Scope
Acceptance Criteria
Revision Notes
```

`core-specs/domains/` must not become product module documentation.

It must remain Core domain specification.

---

# 28. Exclusions

This chapter does not define:

```text
complete field-level object schemas
complete service input/output contracts
complete event payloads
API endpoint routes
product screens
commercial policies
vendor integrations
full marketplace rules
implementation tickets
```

Those belong to later chapters, appendices, `core-specs/` or product books.

---

# 29. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It preserves the 26 baseline Core Domains.
[ ] It classifies domains into four categories.
[ ] It explains Capability and Business Responsibility as cross-cutting systems.
[ ] It does not silently expand the domain count.
[ ] It distinguishes domain from product module.
[ ] It distinguishes domain from database schema.
[ ] It distinguishes domain from AI agent.
[ ] It defines domain ownership rules.
[ ] It defines domain dependency rules.
[ ] It maps domains to objects, services, events, contracts, AI and products.
[ ] It defines MVP domain depth.
[ ] It protects future network and marketplace scope.
[ ] It prepares Appendix B — Core Domain Index.
[ ] It supports future `core-specs/domains/`.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 30. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 13, defining Core Domain Architecture. |
| 0.2.0 | Draft | Second canonical draft rewrite. Preserved the 26-domain baseline, clarified cross-cutting systems, strengthened domain ownership, dependency, MVP depth, product consumption and `core-specs/domains/` readiness. |

---

**End of Chapter**
