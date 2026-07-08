# Book 02

# 28 — Core MVP Boundary

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-28  
**Chapter Title:** Core MVP Boundary  
**Part:** Part IV — Core Execution Boundary  
**Chapter Type:** Execution  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-13 — Core Domain Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-CH-31 — Codex Implementation Roadmap
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the MVP boundary of the MarkOrbit Core.

The Core MVP is the first executable kernel of MarkOrbit.

It is not the full MarkOrbit platform.

It is not the complete product suite.

It is not the full global service network.

It is not the complete AI automation layer.

It is not the final business operating system.

The purpose of this chapter is to decide what must be implemented first, what must be partially specified, what must be reserved, and what must remain deferred.

Without an MVP boundary, Book 02 would pull the entire MarkOrbit vision into the first implementation cycle.

That would make Codex tasks too broad, `core-specs/` too large, and product delivery too slow.

Therefore, this chapter protects the Core MVP from overbuild.

---

# 2. Core Question

This chapter answers one question:

> What is the minimum executable Core required to support the first MarkOrbit products and workflows without overbuilding future architecture?

The answer is:

> The Core MVP must implement the foundation, professional objects, business execution primitives, governed AI baseline and consumption contracts required by MarkReg, MarkOrbit Lite, Workplace, AI Agents and Codex Implementation, while reserving or deferring full network, marketplace, advanced analytics, brand asset and opportunity-engine scope.

---

# 3. Core MVP Definition

Core MVP is defined as:

> the first executable kernel of shared Core Domains, Objects, Services, Events, Contracts and AI governance required for initial MarkOrbit products to consume Core safely.

The Core MVP must be:

```text
small enough to implement
stable enough to govern products
complete enough to support first workflows
bounded enough to prevent future-scope leakage
structured enough for Codex to execute
```

The Core MVP is not a prototype without architecture.

It is a deliberately limited executable Core.

---

# 4. Core MVP Statement

Book 02 uses the following Core MVP statement.

```text
Core MVP is the first executable kernel.
It is not the full MarkOrbit platform.
```

This statement creates four obligations.

```text
1. Implement only what first consumers require.
2. Specify partially what future execution needs to reference.
3. Reserve boundaries for future products without building them fully.
4. Defer advanced scope until architecture and product readiness exist.
```

---

# 5. MVP Consumer Baseline

The Core MVP is shaped by first consumers.

## 5.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

These consumers require executable Core foundations.

They are allowed to influence the MVP boundary.

## 5.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

These consumers require partial specification or reserved boundaries.

They must not pull full future product scope into MVP.

## 5.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

These consumers may be supported by future releases.

They do not define the first Core MVP.

---

# 6. MVP Depth Types

Book 02 uses four MVP depth types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Each domain, object, service, event, contract, API and agent must be assigned a depth type before implementation.

## 6.1 Must Implement

A Core asset is Must Implement when the first executable kernel cannot operate without it.

Must Implement means:

```text
specify
model
implement baseline behavior
test
expose to first consumers where needed
include in Codex task plan
```

## 6.2 Partial Implement

A Core asset is Partial Implement when it is required for architecture continuity but should not be built in full.

Partial Implement means:

```text
define boundary
define minimal fields or contracts
implement only required baseline behavior
reserve future expansion
avoid product-level overbuild
```

## 6.3 Reserved Boundary

A Core asset is Reserved Boundary when future architecture depends on it but MVP should not implement it deeply.

Reserved Boundary means:

```text
define name
state purpose
state exclusion
state future relationship
avoid implementation unless required by first consumers
```

## 6.4 Deferred

A Core asset is Deferred when it belongs to a future release.

Deferred means:

```text
exclude from MVP implementation
document as future scope
prevent Codex tasks from implementing it
require later architecture approval
```

---

# 7. Must Implement Scope

The following Core assets are Must Implement in the Core MVP.

## 7.1 Foundation Core

```text
Identity
Organization
User
Permission
Knowledge Source
Knowledge Asset
```

Foundation Core is required because no product, AI agent, task, event or workflow can operate safely without identity, organization context, user representation, permission and governed knowledge.

## 7.2 Professional Core

```text
Brand
Trademark
Jurisdiction
Classification
Document
```

Professional Core is required because MarkReg and MarkOrbit Lite depend on trademark, jurisdiction, classification and document meaning.

## 7.3 Business Execution Core

```text
Customer
Order
Matter
Workflow Contract
Task
Event
```

Business Execution Core is required because professional service work must move from customer intake to order, matter, task, event and workflow coordination.

## 7.4 AI Governance Core

```text
AI Agent Identity
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Review Record
```

AI Governance Core is required because AI assistance is part of MarkOrbit from the beginning, but must be governed from the beginning.

## 7.5 Consumption Core

```text
Core Consumption Contract
Data Contract baseline
API Contract baseline
Event Contract baseline
Workflow Contract baseline
Agent Contract baseline
Codex Task Contract baseline
```

Consumption Core is required because products, AI agents, internal services and Codex must not consume Core without contracts.

---

# 8. Partial Implement Scope

The following areas require partial implementation.

## 8.1 Capability

Capability is a cross-cutting Core specification system.

It should be partially implemented to support:

```text
AI capability control
service capability classification
agent capability matching baseline
future provider capability mapping
```

It should not become a full product package, service marketplace or provider ranking system in MVP.

## 8.2 Business Responsibility

Business Responsibility is a cross-cutting Core specification system.

It should be partially implemented to support:

```text
matter ownership
task responsibility
review responsibility
AI output approval
routing review baseline
```

It should not become full commission, pricing, revenue attribution or sales incentive logic in MVP.

## 8.3 Policy

Policy should be partially implemented to support:

```text
permission constraints
AI risk constraints
review requirement rules
basic jurisdiction or document rules where needed
```

It should not become a full rules engine in MVP.

## 8.4 Evidence

Evidence should be partially implemented to support:

```text
documented proof references
basic evidence object meaning
future evidence review
AI evidence review boundary
```

It should not become a full evidence scoring or litigation-grade evidence management system in MVP.

## 8.5 Notification

Notification should be partially implemented to support:

```text
task assignment notification
review required notification
deadline reminder baseline
important event notification
```

It should not become a full omnichannel notification platform in MVP.

## 8.6 Agent

Agent should be partially implemented to support:

```text
foreign agent identity
jurisdiction coverage
communication linkage
routing baseline
```

It should not become a full agent marketplace in MVP.

## 8.7 Service Provider

Service Provider should be partially implemented to support:

```text
provider identity baseline
service capability reference
future network provider model
```

It should not become full service provider management in MVP.

## 8.8 Routing

Routing should be partially implemented to support:

```text
manual routing record
AI-assisted routing suggestion
review-required routing
agent selection context
```

It should not become full automated provider ranking or marketplace allocation in MVP.

## 8.9 Communication

Communication should be partially implemented to support:

```text
matter-linked communication
agent communication reference
customer communication reference
AI communication summary boundary
```

It should not become a full email, messaging or CRM communication platform in MVP.

## 8.10 Opportunity

Opportunity should be partially implemented to support:

```text
basic opportunity signal
customer follow-up reference
AI opportunity discovery boundary
future opportunity engine
```

It should not become full opportunity scoring, pipeline automation or revenue prediction in MVP.

---

# 9. Reserved Boundary Scope

The following areas should be reserved but not deeply implemented.

## 9.1 Partner

Partner should be reserved for future partner center and channel collaboration.

MVP may define the name and boundary but should avoid full partner lifecycle implementation.

## 9.2 Service Network

Service Network should be reserved for Book 06 and future MGSN execution.

MVP may define the baseline concept but should not implement full network operation.

## 9.3 Brand Asset Vault

Brand Asset Vault should be reserved as a future product consumer.

MVP may support Brand and Trademark foundations but should not build full brand asset management.

## 9.4 Opportunity Engine

Opportunity Engine should be reserved as a future product consumer.

MVP may support basic Opportunity signals but should not build full scoring, prioritization or campaign automation.

## 9.5 External Integration Platform

External integrations should be contract-aware but not broadly implemented in MVP.

MVP may define integration boundaries and selected connectors later, but the full integration platform is reserved.

## 9.6 Reporting Platform

Reporting consumers should be recognized, but full reporting and analytics remain reserved.

MVP may produce events and audit records that future reporting can consume.

---

# 10. Deferred Scope

The following scope is explicitly deferred from Core MVP.

```text
full global agent marketplace
full MGSN service exchange
advanced provider ranking
trust scoring engine
full opportunity scoring engine
full brand asset vault
advanced portfolio analytics
full external integration platform
complete reporting/BI suite
full pricing automation
commission and revenue attribution engine
full document automation library
full evidence scoring system
full autonomous AI workflow execution
full AI professional decision authority
advanced AI memory and self-learning governance
full public developer API
full webhook platform
full client portal
full partner center
full service platform
```

Deferred scope must not appear in Codex implementation tasks unless a later architecture release explicitly changes its status.

---

# 11. MVP Domain Boundary

The MVP boundary must preserve the 26-domain baseline.

The baseline domain map remains:

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

Capability and Business Responsibility remain cross-cutting specification systems.

They may be partially implemented.

They do not silently change the baseline domain count.

---

# 12. MVP Object Boundary

MVP objects must be limited to what first consumers need.

## 12.1 Must Implement Objects

```text
Identity
Organization
User
Permission Rule
Knowledge Source
Knowledge Asset
Brand
Trademark
Jurisdiction
Classification Term
Document
Customer
Order
Matter
Workflow Contract
Task
Event
AI Agent
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Review Record
Core Consumption Contract
```

## 12.2 Partial Objects

```text
Policy Rule
Evidence
Notification
Capability
Capability Provider
Responsibility Assignment
Agent
Service Provider
Routing Decision
Communication Record
Opportunity
```

## 12.3 Reserved Objects

```text
Partner
Service Network
Network Membership
Provider Ranking
Trust Score
Brand Asset Vault Item
Opportunity Score
External Integration Profile
Reporting Metric Definition
```

The object boundary will be finalized in Appendix C.

---

# 13. MVP Service Boundary

MVP services must support first execution without overbuilding future workflows.

## 13.1 Must Implement Service Families

```text
Identity and User Services
Permission Check Services
Knowledge Retrieval Services
Trademark Management Services
Jurisdiction Requirement Services
Classification Recommendation and Validation Services
Document Management Services
Customer Management Services
Order Management Services
Order-to-Matter Conversion Services
Matter Management Services
Task Management Services
Event Publishing Services
Workflow Contract Validation Services
AI Agent Invocation Services
AI Output Review Services
Core Consumption Validation Services
```

## 13.2 Partial Service Families

```text
Policy Evaluation Services
Evidence Reference Services
Notification Dispatch Services
Capability Matching Baseline Services
Responsibility Assignment Services
Agent Reference Services
Routing Suggestion Services
Communication Linkage Services
Opportunity Signal Services
```

## 13.3 Deferred Service Families

```text
Marketplace Matching Services
Provider Ranking Services
Trust Scoring Services
Advanced Opportunity Scoring Services
Brand Asset Vault Automation Services
Advanced Analytics Services
Full External Integration Services
Pricing Automation Services
Commission Calculation Services
Autonomous AI Execution Services
```

The service boundary will be finalized in Appendix D.

---

# 14. MVP Event Boundary

MVP events must cover meaningful changes required for first execution.

## 14.1 Must Implement Event Families

```text
Identity events
Customer events
Trademark events
Document events
Order events
Matter events
Task events
Workflow events
Review events
AI output events
Consumption events
```

## 14.2 Example MVP Events

```text
CustomerCreated
TrademarkCreated
TrademarkStatusChanged
DocumentUploaded
DocumentGenerated
OrderCreated
OrderConfirmed
OrderConvertedToMatter
MatterCreated
MatterStatusChanged
TaskCreated
TaskAssigned
TaskCompleted
ReviewRequired
ReviewApproved
ReviewRejected
AIRecommendationGenerated
AIRecommendationReviewRequired
CoreConsumptionApproved
CoreConsumptionRejected
```

## 14.3 Deferred Event Families

```text
network marketplace events
provider ranking events
trust scoring events
advanced opportunity scoring events
brand vault automation events
advanced reporting events
full integration webhook events
```

The event boundary will be finalized in Appendix E.

---

# 15. MVP API Boundary

MVP APIs should expose only contract-bound Core surfaces.

## 15.1 MVP API Surfaces

```text
Identity API
Knowledge Retrieval API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Customer API
Order API
Matter API
Task API
Event API
AI Invocation API
Core Consumption API baseline
```

## 15.2 Deferred API Surfaces

```text
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
```

API details must wait for Appendix F and `core-specs/api/`.

---

# 16. MVP AI Boundary

AI is part of MVP only as governed capability.

## 16.1 MVP AI Capabilities

```text
consultation support
classification recommendation
document requirement assistance
document drafting assistance
trademark status summary
evidence review assistance
communication summary
routing suggestion
opportunity signal suggestion
workflow assistance
Codex implementation assistance
```

## 16.2 MVP AI Governance Requirements

Every MVP AI capability requires:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Allowed Object Access
Allowed Services
Risk Level
Human Review Rule
AI Output Status
AI Events
AI Audit Record
Failure Behavior
Product Consumer Binding
```

## 16.3 Deferred AI Scope

```text
autonomous professional decision-making
autonomous filing decisions
autonomous evidence sufficiency decisions
autonomous legal strategy decisions
autonomous agent selection without review
self-modifying AI agents
unbounded knowledge access
ungoverned long-term memory
```

AI remains governed by Chapter 26 and Appendix G.

---

# 17. MVP Workflow Boundary

MVP workflow must focus on first execution primitives.

## 17.1 MVP Workflow Contracts

```text
Guided Intake to Order
Order Confirmation
Order-to-Matter Conversion
Matter Execution Baseline
Task Assignment and Completion
Document Draft Review
AI Recommendation Review
Routing Review Baseline
Opportunity Follow-up Baseline
```

## 17.2 Deferred Workflow Scope

```text
full multi-party marketplace workflow
full service provider bidding workflow
full cross-organization settlement workflow
full advanced CRM workflow
autonomous AI workflow execution
full client portal workflow
full partner center workflow
```

Workflow Contract must remain Core-governed.

Product UI must not own hidden workflow rules.

---

# 18. MVP Knowledge Boundary

Knowledge is required in MVP, but knowledge scope must be controlled.

## 18.1 MVP Knowledge Scope

```text
jurisdiction requirement baseline
classification reference baseline
document requirement baseline
trademark status explanation baseline
service workflow guidance baseline
AI authorized knowledge baseline
```

## 18.2 Partial Knowledge Scope

```text
office procedure details
country-specific advanced rules
agent practice notes
evidence rules
opposition and refusal strategy notes
pricing-related knowledge
```

## 18.3 Deferred Knowledge Scope

```text
complete global law database
complete office procedure automation
complete case law intelligence
complete agent performance intelligence
complete dynamic commercial knowledge graph
```

Knowledge must be governed as Core Knowledge, not treated as arbitrary content.

---

# 19. MVP Product Boundary

MVP product support is limited.

## 19.1 MarkReg

MarkReg may consume Core MVP for:

```text
customer management
trademark records
jurisdiction/classification/document support
order-to-matter execution
tasks/events/workflows
agent communication baseline
AI assistance under governance
```

## 19.2 MarkOrbit Lite

Lite may consume Core MVP for:

```text
guided intake
AI-assisted consultation
classification recommendation
document requirement explanation
order creation
basic review and handoff
```

## 19.3 Workplace

Workplace may consume Core MVP for:

```text
matter queues
task assignment
review workflow
events
notifications
AI output review
responsibility visibility
```

## 19.4 MGSN

MGSN is partial/reserved in MVP.

It may consume baseline Agent, Service Provider, Routing, Communication and Capability references.

It should not become full marketplace.

---

# 20. MVP Repository Boundary

The MVP repository sequence must remain controlled.

```text
Book 02 rewritten manuscript
        ↓
Appendices A–H
        ↓
indexes/
        ↓
core-specs/ scaffold
        ↓
Codex task scaffold
        ↓
Wave 0 Codex tasks
        ↓
implementation
```

Detailed `core-specs/` must not be generated before appendices and indexes are complete.

Codex tasks must not be generated before Appendix H and task templates are ready.

---

# 21. MVP Acceptance Gate

A Core asset may enter MVP only if it passes this gate.

```text
[ ] It is required by an MVP Consumer.
[ ] It has a clear owning domain or cross-cutting system.
[ ] It has clear object/service/event/contract relationships.
[ ] It has a defined MVP depth.
[ ] It does not duplicate product UI.
[ ] It does not implement deferred scope.
[ ] It has permission/policy/audit requirements where needed.
[ ] It has AI governance rules where AI is involved.
[ ] It can be tested.
[ ] It can be assigned to Codex without architecture invention.
```

If an asset fails this gate, it should become Partial, Reserved or Deferred.

---

# 22. MVP Anti-Patterns

## 22.1 Full Platform MVP

The MVP tries to implement the whole MarkOrbit vision.

Correction:

```text
Limit MVP to the first executable Core kernel.
```

## 22.2 Product Feature Pulls Core Expansion

A product idea expands Core scope without architecture review.

Correction:

```text
Use Core governance and MVP depth classification.
```

## 22.3 Marketplace Too Early

MGSN marketplace behavior enters MVP before Agent, Routing and Responsibility are stable.

Correction:

```text
Reserve network boundaries and defer marketplace execution.
```

## 22.4 AI Autonomy Too Early

AI is allowed to make final professional decisions.

Correction:

```text
Use Agent Contract, review, audit and responsibility rules.
```

## 22.5 Reporting Drives Core Meaning

Reporting demands redefine statuses or events.

Correction:

```text
Reporting consumes Core events and requests extensions through governance.
```

## 22.6 Codex Implements Deferred Scope

Codex creates files or features for deferred areas.

Correction:

```text
Codex tasks must include prohibited overreach and MVP depth.
```

---

# 23. Relationship to Chapter 29 — MVP Domain Priority

This chapter defines the boundary.

Chapter 29 defines domain priority within that boundary.

The relationship is:

```text
Chapter 28 decides what may enter MVP.
Chapter 29 decides in what order MVP domains should be addressed.
```

Chapter 29 must follow the depth types and consumer classifications defined here.

---

# 24. Relationship to Chapter 30 — MVP Execution Matrix

Chapter 30 converts the boundary into execution rows.

The matrix must include:

```text
Core Domain
MVP Depth
Required Specs
Objects
Services
Events
Contracts
AI Usage
Workflow Usage
Product Consumers
Codex Tasks
Acceptance Criteria
```

The MVP Boundary defines the control rules that the matrix must enforce.

---

# 25. Relationship to Chapter 31 — Codex Implementation Roadmap

Chapter 31 defines Codex waves.

The Codex roadmap must not implement deferred scope.

Every Codex task must reference:

```text
MVP depth
source specs
execution matrix row
acceptance criteria
prohibited overreach
```

Codex should implement the MVP kernel, not the full future platform.

---

# 26. Relationship to Appendices

This chapter directly informs the appendices.

Appendix A must define MVP depth terms.

Appendix B must classify domain MVP phase and depth.

Appendix C must classify object MVP depth.

Appendix D must classify service MVP depth.

Appendix E must classify event MVP status.

Appendix F must classify API MVP and future surfaces.

Appendix G must classify AI agents by MVP status.

Appendix H must map Codex tasks to MVP-approved scope.

---

# 27. Relationship to core-specs/

Future `core-specs/` must preserve MVP boundaries.

Each spec should include:

```text
MVP phase
MVP depth
consumer classification
out of scope
deferred scope
acceptance criteria
prohibited overreach
```

This applies to:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
```

---

# 28. Specification Output

This chapter produces the following specification outputs:

```text
Core MVP Definition
Core MVP Statement
MVP Consumer Baseline
MVP Depth Types
Must Implement Scope
Partial Implement Scope
Reserved Boundary Scope
Deferred Scope
MVP Domain Boundary
MVP Object Boundary
MVP Service Boundary
MVP Event Boundary
MVP API Boundary
MVP AI Boundary
MVP Workflow Boundary
MVP Knowledge Boundary
MVP Product Boundary
MVP Repository Boundary
MVP Acceptance Gate
MVP Anti-Patterns
Appendix Requirements
core-specs Requirements
Codex Scope Constraints
```

---

# 29. Execution Mapping

| MVP Boundary Decision | Execution Impact |
|----------------------|------------------|
| Must Implement | Requires specs, tests and Codex tasks |
| Partial Implement | Requires minimal spec and reserved expansion |
| Reserved Boundary | Requires name, boundary and exclusion note |
| Deferred | Must not be implemented in MVP |
| MVP Consumers | Shape first implementation scope |
| Partial Consumers | May receive baseline support only |
| Future Consumers | Do not define MVP scope |
| AI in MVP | Requires Agent Contract, review and audit |
| API in MVP | Requires Appendix F and API contracts |
| Codex implementation | Requires Appendix H and execution matrix |

---

# 30. Exclusions

This chapter does not define:

```text
final domain priority order
complete execution matrix
full object schemas
full service interfaces
full event payloads
API endpoint details
product UI
full network marketplace
full opportunity engine
full brand asset vault
full reporting platform
implementation tickets
```

Those belong to Chapter 29, Chapter 30, Chapter 31, appendices, `core-specs/` or product books.

---

# 31. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core MVP as the first executable kernel.
[ ] It states that Core MVP is not the full platform.
[ ] It defines MVP Consumers, Partial Consumers and Future Consumers.
[ ] It defines Must Implement, Partial Implement, Reserved Boundary and Deferred.
[ ] It lists Must Implement scope.
[ ] It lists Partial Implement scope.
[ ] It lists Reserved Boundary scope.
[ ] It lists Deferred scope.
[ ] It preserves the 26-domain baseline.
[ ] It clarifies Capability and Business Responsibility as cross-cutting systems.
[ ] It defines MVP object, service, event, API, AI, workflow and knowledge boundaries.
[ ] It protects MGSN, Opportunity Engine and Brand Asset Vault from overbuild.
[ ] It defines repository sequence before Codex tasks.
[ ] It defines an MVP acceptance gate.
[ ] It defines MVP anti-patterns.
[ ] It prepares Chapter 29, Chapter 30 and Chapter 31.
[ ] It prepares Appendices A–H.
[ ] It supports future `core-specs/` MVP depth fields.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 32. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 28, defining the Core MVP boundary. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened Core MVP definition, depth types, consumer classification, must/partial/reserved/deferred scope, AI/API/workflow/knowledge boundaries and Codex scope protection. |

---

**End of Chapter**
