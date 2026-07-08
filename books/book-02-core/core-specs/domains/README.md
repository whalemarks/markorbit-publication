# core-specs/domains/

**Repository:** `book-02-core`  
**Directory:** `core-specs/domains/`  
**Document:** `core-specs/domains/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/domains/` directory contains detailed Domain Specification files for the baseline MarkOrbit Core Domain Map.

A Domain Specification defines a bounded area of Core professional meaning.

It explains what the domain owns, what it does not own, what objects and services belong to it, what events it may emit or consume, what contracts it requires, and how it is consumed by products, workflows, AI agents and Codex tasks.

This directory exists to turn the domain architecture from Book 02 into implementation-ready specifications.

It does not redefine the architecture.

It implements the domain map already approved by:

```text
B02-CH-08 — Ontology and Domain Classification
B02-CH-13 — Core Domain Architecture
B02-CH-22 — Domain Specification
B02-APP-B — Core Domain Index
indexes/domain-index.md
```

---

# 2. Canonical Domain Rule

Book 02 uses the following canonical rule:

```text
The baseline Core Domain Map contains 26 domains.
Capability and Business Responsibility are cross-cutting Core specification systems.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

Therefore, this directory should contain Domain Specification files for the 26 baseline Core Domains.

Capability and Business Responsibility should not be silently added here as ordinary domain files.

They should be handled through:

```text
core-specs/cross-cutting/
core-specs/objects/
core-specs/services/
core-specs/contracts/
```

unless an explicit architecture release changes their classification.

---

# 3. Domain Specification Definition

A Domain Specification is the canonical implementation-facing specification for one bounded Core Domain.

A Domain Specification must answer:

```text
What professional meaning does this domain own?
What is inside the domain boundary?
What is outside the domain boundary?
Which Core Objects belong to this domain?
Which Core Services operate this domain?
Which Core Events are emitted or consumed?
Which contracts are required?
Which products or agents may consume this domain?
What is MVP scope?
What is deferred?
What must Codex not implement?
```

---

# 4. Directory Boundary

## 4.1 domains/ Owns

This directory owns:

```text
Domain Specification files
domain purpose
domain boundary
domain ownership
domain relationships
domain object list
domain service list
domain event list
domain contract list
domain MVP depth
domain consumer classification
domain AI usage boundary
domain workflow usage boundary
domain deferred scope
domain acceptance criteria
```

## 4.2 domains/ Does Not Own

This directory does not own:

```text
Core architecture decisions
new domain creation
domain renaming
cross-cutting system reclassification
object lifecycle details
service input/output contracts
event payload schemas
API endpoint design
AI Agent Contracts
product UI
database schema
Codex implementation code
```

Those belong to other specification layers.

---

# 5. Source Chain

Every Domain Specification file must cite its source chain.

Required source chain:

```text
B02-CH-08
B02-CH-13
B02-CH-22
B02-APP-B
indexes/domain-index.md
core-specs/domains/{domain}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
B02-CH-28 — Core MVP Boundary
B02-CH-29 — MVP Domain Priority
B02-CH-30 — MVP Execution Matrix
B02-CH-31 — Codex Implementation Roadmap
```

---

# 6. Required Domain Spec Files

This directory should contain one file for each baseline Core Domain.

## 6.1 Foundation Domains

```text
identity.md
organization.md
user.md
permission.md
policy.md
knowledge.md
```

## 6.2 Professional Domains

```text
brand.md
trademark.md
jurisdiction.md
classification.md
document.md
evidence.md
```

## 6.3 Business Execution Domains

```text
customer.md
matter.md
order.md
opportunity.md
workflow-contract.md
task.md
event.md
notification.md
```

## 6.4 Collaboration Network Domains

```text
partner.md
agent.md
service-provider.md
service-network.md
routing.md
communication.md
```

This equals:

```text
6 Foundation Domains
6 Professional Domains
8 Business Execution Domains
6 Collaboration Network Domains
=
26 baseline Core Domains
```

---

# 7. Excluded from domains/

The following should not be placed in `core-specs/domains/` as ordinary baseline domain files:

```text
capability.md
business-responsibility.md
ai-governance.md
codex-task-system.md
specification-governance.md
product.md
workplace.md
markreg.md
markorbit-lite.md
mgsn.md
database.md
ui.md
pricing.md
billing.md
```

Some of these may appear in other directories:

```text
core-specs/cross-cutting/capability.md
core-specs/cross-cutting/business-responsibility.md
core-specs/agents/
core-specs/contracts/
core-specs/workflows/
codex-tasks/
```

---

# 8. Domain Spec Metadata

Each Domain Specification file must begin with metadata.

```text
# Domain Specification — {Domain Name}

**Spec ID:** B02-DOM-{DOMAIN}
**Spec Type:** Domain
**Domain Name:** {Domain Name}
**Domain Category:** Foundation | Professional | Business Execution | Collaboration Network
**Source Appendix:** B02-APP-B — Core Domain Index
**Source Index:** indexes/domain-index.md
**Related Chapter:** B02-CH-22 — Domain Specification
**Status:** Draft
**Version:** 0.1.0
**MVP Phase:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Domain Spec Required Sections

Every Domain Specification must include the following sections.

```text
1. Purpose
2. Core Meaning
3. Domain Category
4. Scope
5. Domain Boundary
6. Owns
7. Does Not Own
8. Primary Objects
9. Primary Services
10. Primary Events
11. Primary Contracts
12. Relationships to Other Domains
13. AI Usage
14. Workflow Usage
15. API Usage
16. Product Consumers
17. MVP Scope
18. Deferred Scope
19. Data and Implementation Notes
20. Codex Implementation Notes
21. Validation Rules
22. Prohibited Overreach
23. Acceptance Criteria
24. Revision Notes
```

---

# 10. Domain Category Rules

## 10.1 Foundation Domain

Foundation Domains provide identity, organization, user, permission, policy and knowledge foundations.

They must be specified before professional and execution domains.

## 10.2 Professional Domain

Professional Domains define trademark service meaning, including brands, marks, jurisdictions, classification, documents and evidence.

They must preserve professional review and legal responsibility boundaries.

## 10.3 Business Execution Domain

Business Execution Domains convert professional meaning into orders, matters, workflows, tasks, events and notifications.

They must preserve responsibility and state transition rules.

## 10.4 Collaboration Network Domain

Collaboration Network Domains support agents, providers, routing, communication, partners and service networks.

They must not overbuild marketplace logic in MVP.

---

# 11. MVP Phase Rules

Domain specs must follow this MVP phase mapping.

## Phase 1 — Foundation Core

```text
Identity
Organization
User
Permission
Knowledge
Policy: Partial
Capability: Cross-cutting Partial
```

## Phase 2 — Professional Core

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence: Partial
```

## Phase 3 — Business Execution Core

```text
Customer
Order
Matter
Workflow Contract
Task
Event
Notification: Partial
Business Responsibility: Cross-cutting Partial
```

## Phase 4 — Growth and Collaboration Baseline

```text
Communication
Agent
Service Provider
Routing
Opportunity
```

## Phase 5 — Reserved Network Boundary

```text
Partner
Service Network
```

---

# 12. Domain Ownership Rules

## 12.1 One Primary Domain

Each baseline domain must have one clear primary responsibility.

## 12.2 Domain Owns Meaning, Not UI

A domain owns professional meaning and Core boundaries.

It does not own product screens.

## 12.3 Domain Owns Boundaries, Not Implementation Convenience

A domain is not created because engineering finds a module convenient.

## 12.4 Cross-Cutting Systems Are Not Silent Domains

Capability and Business Responsibility must remain explicitly marked as cross-cutting systems.

## 12.5 Product Consumers Do Not Redefine Domains

MarkReg, MarkOrbit Lite, Workplace and MGSN may consume Core Domains.

They must not redefine Core Domain meaning.

---

# 13. Domain-to-Object Rule

Every Domain Specification must list its primary Core Objects.

Examples:

```text
Identity
    Identity
    Actor
    System Identity
    AI Agent Identity

Trademark
    Trademark
    Trademark Owner
    Trademark Status
    Trademark GoodsServices
    Trademark Lifecycle Record

Order
    Order
    Order Item
    Order Requirement
    Order Status
    Order-to-Matter Link
```

Object detail belongs to:

```text
core-specs/objects/
```

The domain spec lists object ownership and boundary.

---

# 14. Domain-to-Service Rule

Every Domain Specification must list primary Core Services.

Examples:

```text
Identity
    Identity Registration Service
    Identity Resolution Service
    Actor Identity Lookup Service

Classification
    Classification Recommendation Service
    Classification Validation Service
    GoodsServices Term Lookup Service
    Classification Review Service

Order
    Order Creation Service
    Order Validation Service
    Order Confirmation Service
    Order-to-Matter Conversion Service
```

Service detail belongs to:

```text
core-specs/services/
```

The domain spec lists service ownership and purpose.

---

# 15. Domain-to-Event Rule

Every Domain Specification must list primary Core Events.

Examples:

```text
Identity
    IdentityCreated
    IdentityUpdated
    IdentityLinked

Trademark
    TrademarkCreated
    TrademarkStatusChanged
    TrademarkLinkedToMatter

Task
    TaskCreated
    TaskAssigned
    TaskCompleted
    TaskReviewRequired
```

Event detail belongs to:

```text
core-specs/events/
```

The domain spec lists event responsibility and meaning.

---

# 16. Domain-to-Contract Rule

Every Domain Specification must identify required contract types.

Contract examples:

```text
Data Contract
API Contract
Event Contract
Workflow Contract
Review Contract
Agent Contract
Permission Contract
Policy Contract
```

Detailed contract specs belong to:

```text
core-specs/contracts/
```

---

# 17. AI Usage Rules

Domain specs must define AI usage where relevant.

AI usage must state:

```text
allowed AI assistance
prohibited AI behavior
Agent Contract requirement
authorized knowledge requirement
review requirement
audit requirement
related AI events
```

Domains with high AI relevance include:

```text
Knowledge
Trademark
Classification
Document
Evidence
Matter
Task
Communication
Routing
Opportunity
```

Domain specs must not allow AI to replace professional responsibility.

---

# 18. Workflow Usage Rules

Domain specs must define workflow usage where relevant.

Workflow-related domains include:

```text
Order
Matter
Workflow Contract
Task
Event
Notification
Business Responsibility
Classification
Document
Routing
Communication
```

Workflow usage must reference:

```text
Workflow Contract
Task
Review Record
Approval Record
Event
Responsibility Assignment
```

---

# 19. Product Consumer Rules

Domain specs must classify product consumers.

Consumer categories:

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

Future consumers may include:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

Products may consume domain specs.

Products must not redefine domain meaning.

---

# 20. Codex Implementation Rules

Codex tasks generated from domain specs must:

```text
cite the domain spec
cite indexes/domain-index.md
cite related object/service/event indexes
define expected outputs
define tests
define prohibited overreach
preserve MVP depth
preserve deferred scope
```

Codex must not:

```text
invent new domains
rename domains
merge domains
split domains
promote cross-cutting systems into ordinary domains
implement future marketplace scope
implement product UI
define database schema before object specs
```

---

# 21. Domain Spec Generation Order

Generate domain specs in this order.

## 21.1 First Priority

```text
identity.md
organization.md
user.md
permission.md
knowledge.md
```

## 21.2 Second Priority

```text
brand.md
trademark.md
jurisdiction.md
classification.md
document.md
```

## 21.3 Third Priority

```text
customer.md
order.md
matter.md
workflow-contract.md
task.md
event.md
```

## 21.4 Fourth Priority

```text
policy.md
evidence.md
notification.md
communication.md
agent.md
service-provider.md
routing.md
opportunity.md
```

## 21.5 Reserved Boundary

```text
partner.md
service-network.md
```

---

# 22. Validation Rules

The `core-specs/domains/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] It contains one file for each of the 26 baseline Core Domains when complete.
[ ] It does not contain Capability as an ordinary baseline domain.
[ ] It does not contain Business Responsibility as an ordinary baseline domain.
[ ] Every domain spec has metadata.
[ ] Every domain spec references indexes/domain-index.md.
[ ] Every domain spec has domain category.
[ ] Every domain spec has MVP phase.
[ ] Every domain spec has MVP depth.
[ ] Every domain spec lists primary objects.
[ ] Every domain spec lists primary services.
[ ] Every domain spec lists primary events.
[ ] Every domain spec lists primary contracts.
[ ] Every domain spec defines deferred scope.
[ ] Every domain spec defines prohibited overreach.
[ ] Every domain spec has acceptance criteria.
```

---

# 23. Prohibited Behavior

This directory must not:

```text
change the 26-domain baseline
add product names as domains
add database tables as domains
add AI agents as domains
silently add Capability as a baseline domain
silently add Business Responsibility as a baseline domain
merge domains for implementation convenience
split domains without architecture release
rename domains without architecture release
define detailed object lifecycle
define detailed service contracts
define detailed event payloads
define detailed API endpoints
define product UI
define physical database schema
```

---

# 24. Acceptance Criteria

The `core-specs/domains/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/domains/.
[ ] It preserves the 26-domain baseline.
[ ] It states that Capability and Business Responsibility are cross-cutting systems.
[ ] It defines the directory boundary.
[ ] It defines source chain requirements.
[ ] It lists all required domain files.
[ ] It excludes non-domain files.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines domain category rules.
[ ] It defines MVP phase rules.
[ ] It defines ownership rules.
[ ] It defines domain-to-object rules.
[ ] It defines domain-to-service rules.
[ ] It defines domain-to-event rules.
[ ] It defines domain-to-contract rules.
[ ] It defines AI usage rules.
[ ] It defines workflow usage rules.
[ ] It defines product consumer rules.
[ ] It defines Codex implementation rules.
[ ] It defines generation order.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 25. Next Action

After this README is accepted, generate:

```text
core-specs/domains/_template.md
```

Do not generate detailed domain specs before the template exists.

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/domains/. Defines directory purpose, canonical 26-domain baseline, required files, domain spec structure, validation rules and Codex handoff. |

---

**End of README**
