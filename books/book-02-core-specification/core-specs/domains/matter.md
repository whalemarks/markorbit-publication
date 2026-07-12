# Domain Specification — Matter

**Spec ID:** B02-DOM-MATTER  
**Spec Type:** Domain  
**Domain Name:** Matter  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/matter-type.md; core-specs/objects/matter-scope.md; core-specs/objects/matter-party.md; core-specs/objects/matter-assignment.md; core-specs/objects/matter-professional-context.md
**Related Service Specs:** core-specs/services/matter-creation-service.md; core-specs/services/matter-status-service.md; core-specs/services/matter-scope-service.md; core-specs/services/matter-assignment-service.md; core-specs/services/matter-reference-validation-service.md; core-specs/services/order-to-matter-conversion-service.md  
**Related Event Specs:** core-specs/events/matter-created.md; core-specs/events/matter-updated.md; core-specs/events/matter-status-changed.md; core-specs/events/matter-scope-updated.md; core-specs/events/matter-assigned.md; core-specs/events/matter-reference-validated.md; core-specs/events/order-converted-to-matter.md  
**Related Contract Specs:** core-specs/contracts/matter/matter-contract.md; core-specs/contracts/matter/matter-scope-contract.md; core-specs/contracts/matter/matter-assignment-contract.md; core-specs/contracts/matter/order-to-matter-conversion-contract.md; core-specs/contracts/matter/matter-audit-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Matter Domain defines the Core meaning of a professional service execution container in MarkOrbit.

It exists so that Orders, Customers, Brands, Trademarks, Jurisdictions, Classifications, Documents, Evidence, Tasks, Workflows, Communications, AI Agents and product consumers can consistently refer to the professional work being performed.

Matter is required before:

```text
professional service execution
order fulfillment
task creation
workflow coordination
document preparation
evidence review
classification review
trademark status follow-up
client communication tracking
agent communication tracking
deadline-sensitive execution
AI matter summary
professional responsibility assignment
Codex implementation of execution workflows
```

The Matter Domain is a Business Execution Domain because it turns commercial service requests into managed professional execution.

---

# 2. Core Meaning

Matter means:

```text
a Core-recognized professional execution container that groups the scope, parties, objects, tasks, workflow, responsibility and status of a trademark-related service engagement.
```

Matter is not merely:

```text
an Order
a Customer
a Trademark
a Brand
a Task
a Workflow
a sales opportunity
a communication thread
a document folder
a billing item
a project UI card
a ticket
```

Matter answers:

```text
What professional work is being executed?
For which customer or party?
For which Brand, Trademark, Jurisdiction, Classification, Document or Evidence context?
What is the scope of work?
Who is responsible?
What status is the professional execution in?
Which tasks, workflows, events and communications belong to this execution?
What must be reviewed, approved or audited?
```

---

# 3. Domain Category

Matter is a Business Execution Domain.

Business Execution Domains provide the Core basis for:

```text
professional work containment
order fulfillment
scope control
responsibility assignment
task coordination
workflow execution
communication context
document and evidence execution
AI-assisted execution support
client-facing progress explanation
```

Matter connects commercial Orders to operational professional work.

---

# 4. Architectural Position

Matter sits after Customer and Order in the Business Execution Core.

```text
Customer defines the demand-side party
        ↓
Order defines the commercial service request
        ↓
Matter defines the professional execution container
        ↓
Workflow Contract coordinates execution
        ↓
Task assigns work
        ↓
Event records meaningful changes
        ↓
Notification and Communication coordinate participants
```

Matter owns execution context.

Order owns commercial transaction context.

Task owns actionable unit of work.

Workflow owns state transition contract.

Matter does not replace any of them.

---

# 5. Scope

The Matter Domain includes:

```text
matter definition
matter type
matter status
matter scope
matter party boundary
matter relationship to Customer
matter relationship to Order
matter relationship to Brand
matter relationship to Trademark
matter relationship to Jurisdiction
matter relationship to Classification
matter relationship to Document
matter relationship to Evidence
matter assignment
matter professional context
matter workflow reference boundary
matter task reference boundary
matter communication reference boundary
matter reference validation
matter audit reference
matter event emission
matter use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Matter
Matter Type
Matter Status
Matter Scope
Matter Party
Matter Assignment
Matter Professional Context
Matter Creation Service
Matter Status Service
Matter Scope Service
Matter Assignment Service
Order-to-Matter Conversion Service
Matter Reference Validation Service
MatterCreated event
MatterStatusChanged event
MatterScopeUpdated event
MatterAssigned event
OrderConvertedToMatter event
MatterReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Matter Domain owns:

```text
Core Matter definition
matter execution scope
matter type
matter status
matter parties
matter assignment
matter professional context
matter relationship to Order and Customer
matter relationship to Professional Core objects
matter relationship to Task and Workflow references
matter reference validation
matter event emission
matter reference used by execution workflows and products
```

## 6.2 Out of Boundary

The Matter Domain does not own:

```text
Customer lifecycle
Order commercial transaction lifecycle
payment lifecycle
invoice lifecycle
pricing policy
Brand commercial identity
Trademark protection-record meaning
Jurisdiction rule meaning
Classification goods/services meaning
Document artifact lifecycle
Evidence proof meaning
Task lifecycle
Workflow state model
Communication message lifecycle
deadline calculation engine
official filing submission automation
external agent relationship
```

Those responsibilities belong to:

```text
Customer Domain
Order Domain
Brand Domain
Trademark Domain
Jurisdiction Domain
Classification Domain
Document Domain
Evidence Domain
Task Domain
Workflow Contract system
Communication Domain
Agent Domain
Service Provider Domain
Finance/Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Matter is the execution container.

Order is the commercial commitment.

Task is the work unit.

Workflow Contract governs transitions.

Communication carries messages.

Document and Evidence provide artifacts and proof.

Matter should reference those objects, not absorb their meanings.

---

# 7. Domain Rules

## 7.1 Matter Requires Scope

Every Matter must have a defined Matter Scope.

Matter Scope should state:

```text
service type
professional objective
related Brand or Trademark
jurisdiction context
classification context if applicable
document/evidence context if applicable
expected execution boundary
out-of-scope items
```

A Matter without scope is not implementation-ready.

## 7.2 Matter Should Derive from Order or Approved Internal Need

Most Matters should be created from an Order.

Internal review or internal professional maintenance matters may be created without an Order only through explicit approved service rules.

## 7.3 Matter Does Not Replace Order

Matter must not own pricing, payment, invoice, refund or commercial package meaning.

Those belong to Order or Finance/Product implementation.

## 7.4 Matter Must Support Responsibility Assignment

A Matter must be assignable to responsible actors or teams.

Responsibility may include:

```text
matter owner
professional reviewer
process owner
document owner
customer communication owner
agent communication owner
AI review owner
```

Responsibility rules may be governed by Business Responsibility cross-cutting system.

## 7.5 Matter Must Be Workflow-Aware

Matter should reference Workflow Contracts for execution.

Matter status must not become arbitrary product UI status.

State transitions should be governed by Workflow Contract and Services.

## 7.6 Matter Must Be Auditable

Matter-sensitive actions must preserve audit trace.

Audit-sensitive matter actions include:

```text
matter creation
order-to-matter conversion
matter scope change
matter status change
matter assignment
professional review completion
matter closure
matter cancellation
document/evidence use in matter
AI matter summary
external communication linked to matter
```

---

# 8. Primary Objects

The Matter Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Matter | Matter | Must Implement | Core professional execution container. |
| Matter Type | Matter | Must Implement | Controlled type of professional service execution. |
| Matter Status | Matter | Must Implement | Controlled execution status of Matter. |
| Matter Scope | Matter | Must Implement | Professional execution boundary and objective. |
| Matter Party | Matter / Customer / Agent | Must Implement | Party participating in Matter. |
| Matter Assignment | Matter / Task / Business Responsibility | Must Implement | Responsible actor or team assignment for Matter. |
| Matter Professional Context | Matter | Must Implement | Professional context connecting Matter to Brand, Trademark, Jurisdiction, Classification, Document and Evidence. |
| Matter-Order Link | Matter / Order | Must Implement | Relationship between Order and Matter. |
| Matter Workflow Reference | Matter / Workflow Contract | Must Implement | Workflow Contract or workflow instance reference used by Matter. |
| Matter Task Reference | Matter / Task | Must Implement | Task reference associated with Matter execution. |
| Matter Communication Reference | Matter / Communication | Partial Implement | Communication context associated with Matter. |
| Matter Audit Reference | Matter / Audit | Partial Implement | Audit reference for matter-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Customer | Customer | Matter is executed for or related to Customer. |
| Order | Order | Matter may be created from Order. |
| Brand | Brand | Matter may be related to Brand service. |
| Trademark | Trademark | Matter may be related to Trademark service. |
| Jurisdiction | Jurisdiction | Matter may be jurisdiction-specific. |
| Classification | Classification | Matter may include classification review. |
| Document | Document | Matter may require or produce Documents. |
| Evidence | Evidence | Matter may require or review Evidence. |
| Task | Task | Matter creates or contains Tasks. |
| Workflow Contract | Workflow Contract | Matter execution is coordinated by Workflow. |
| Event | Event | Matter changes emit Events. |
| Communication | Communication | Matter may link messages and threads. |
| AI Output | AI Governance | AI may summarize or assist Matter execution. |
| Audit Record | Audit | Audit records matter-sensitive actions. |

---

# 9. Primary Services

The Matter Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Matter Creation Service | Matter | Must Implement | Create a Core Matter. |
| Order-to-Matter Conversion Service | Matter / Order | Must Implement | Convert approved Order scope into one or more Matters. |
| Matter Update Service | Matter | Must Implement | Update controlled Matter fields. |
| Matter Status Service | Matter | Must Implement | Update Matter Status through governed rules. |
| Matter Scope Service | Matter | Must Implement | Create or update Matter Scope. |
| Matter Assignment Service | Matter / Business Responsibility | Must Implement | Assign responsible actor or team to Matter. |
| Matter Professional Context Service | Matter | Must Implement | Link Matter to Brand, Trademark, Jurisdiction, Classification, Document or Evidence context. |
| Matter Workflow Reference Service | Matter / Workflow Contract | Must Implement | Attach or validate Workflow Contract reference. |
| Matter Reference Validation Service | Matter | Must Implement | Validate Matter references used by other domains. |
| Matter Audit Reference Service | Matter / Audit | Partial Implement | Produce matter audit reference for governed actions. |

Service rules:

```text
- Mutating Matter services must emit events.
- Matter services must not create Order commercial lifecycle.
- Matter services must not define Task lifecycle directly.
- Matter services must not bypass Workflow Contracts for status transitions.
- Order-to-Matter conversion must be idempotent.
- Matter assignment must preserve responsibility and audit trace.
```

---

# 10. Primary Events

The Matter Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| MatterCreated | Matter Creation Service | Must Implement | A Core Matter has been created. |
| OrderConvertedToMatter | Order-to-Matter Conversion Service | Must Implement | Order scope has been converted into Matter. |
| MatterUpdated | Matter Update Service | Must Implement | Controlled Matter fields have changed. |
| MatterStatusChanged | Matter Status Service | Must Implement | Matter Status has changed. |
| MatterScopeUpdated | Matter Scope Service | Must Implement | Matter Scope has changed. |
| MatterAssigned | Matter Assignment Service | Must Implement | Responsible actor or team has been assigned to Matter. |
| MatterProfessionalContextLinked | Matter Professional Context Service | Must Implement | Professional object context has been linked to Matter. |
| MatterWorkflowLinked | Matter Workflow Reference Service | Must Implement | Workflow reference has been linked to Matter. |
| MatterReferenceValidated | Matter Reference Validation Service | Must Implement | Matter reference has been validated for governed use. |
| MatterReviewRequired | Matter Status Service / Scope Service | Partial Implement | Matter change or status requires review. |
| MatterClosed | Matter Status Service | Partial Implement | Matter has been closed through governed rules. |
| MatterCancelled | Matter Status Service | Partial Implement | Matter has been cancelled through governed rules. |

Event rules:

```text
- Matter events must reference Matter.
- OrderConvertedToMatter must reference Order and Matter.
- Matter status events must preserve previous and new status.
- Assignment events must reference responsible actor or team.
- Workflow events must reference Workflow Contract where applicable.
- Matter events must not expose confidential customer or document details unnecessarily.
```

---

# 11. Primary Contracts

Matter requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Matter Contract | Matter Contract | Must Implement | Defines Matter fields, type, status, scope and references. |
| Matter Scope Contract | Matter Contract | Must Implement | Defines professional execution boundary and out-of-scope rules. |
| Matter Assignment Contract | Matter / Business Responsibility Contract | Must Implement | Defines responsible actor, team, role and assignment status. |
| Matter Professional Context Contract | Matter Contract | Must Implement | Defines relationships to Brand, Trademark, Jurisdiction, Classification, Document and Evidence. |
| Order-to-Matter Conversion Contract | Matter / Order / Workflow Contract | Must Implement | Defines conversion rules, idempotency and expected outputs. |
| Matter Workflow Reference Contract | Matter / Workflow Contract | Must Implement | Defines workflow reference and transition boundary. |
| Matter Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for matter-sensitive actions. |

Contract rules:

```text
- Matter Contract must not define Order pricing or payment meaning.
- Matter Scope Contract must distinguish in-scope and out-of-scope work.
- Order-to-Matter Conversion Contract must be idempotent.
- Matter Workflow Reference Contract must not define workflow state model itself.
```

---

# 12. Relationships to Other Domains

## 12.1 Customer

Matter is executed for or related to Customer.

Customer owns demand-side party meaning.

Matter owns execution container meaning.

## 12.2 Order

Matter may be created from Order.

Order owns commercial transaction scope.

Matter owns professional execution scope.

## 12.3 Brand

Matter may execute services related to Brand.

Brand owns commercial identity.

## 12.4 Trademark

Matter may execute services related to Trademark records, applications, registrations or status.

Trademark owns protection-record meaning.

## 12.5 Jurisdiction

Matter may be jurisdiction-specific.

Jurisdiction owns where the procedure applies.

## 12.6 Classification

Matter may include classification review or goods/services drafting.

Classification owns goods/services and class meaning.

## 12.7 Document

Matter may require or produce Documents.

Document owns artifact lifecycle.

## 12.8 Evidence

Matter may require or review Evidence.

Evidence owns proof meaning.

## 12.9 Task

Matter creates or contains Tasks.

Task owns actionable work unit lifecycle.

## 12.10 Workflow Contract

Matter execution should be coordinated by Workflow Contracts.

Workflow owns state model and transitions.

## 12.11 Communication

Matter may link communications with customers, agents or service providers.

Communication owns message lifecycle.

## 12.12 AI Governance

AI may summarize or support Matter execution, but cannot close, approve or decide professional matters without governed review.

## 12.13 Audit

Audit records should include Matter references for execution-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Matter only under governed Agent Contracts.

Allowed AI use:

```text
summarize matter status
identify missing matter scope
suggest next task based on workflow state
flag missing document or evidence requirement
prepare draft client update
prepare draft internal review note
summarize linked communications if authorized
flag mismatch between Order scope and Matter scope
recommend review when scope changes
```

AI must not:

```text
create Matter without authorized service
convert Order to Matter without governed service
change Matter Status directly
close or cancel Matter by itself
approve professional completion
send client-facing matter update without review where required
modify Order pricing or payment scope
create official filing submission
infer confidential facts beyond approved context
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Matter Object Access Rule
Matter Service Access Rule
Matter Event Access Rule
Customer / Order / Trademark / Document Access Rules
Policy Rule
Workflow Rule
Review Rule
Audit Rule
Human Review Rule for professional or external outputs
```

---

# 14. Workflow Usage

Matter is workflow-sensitive.

Matter workflows may include:

```text
order-to-matter-conversion-workflow.md
matter-intake-workflow.md
matter-assignment-workflow.md
matter-scope-review-workflow.md
matter-execution-workflow.md
matter-document-review-workflow.md
matter-evidence-review-workflow.md
matter-status-review-workflow.md
matter-closure-workflow.md
ai-matter-summary-review-workflow.md
```

Workflow rules:

```text
- Matter workflows must reference Workflow Contracts.
- Order-to-Matter conversion must be idempotent.
- Matter status changes must be governed by workflow transition rules.
- Scope changes should require review when they affect professional responsibility or order scope.
- AI matter summaries must require review before client-facing use where high-risk.
- Matter closure must preserve task, document, evidence and audit references.
```

---

# 15. API Usage

Matter APIs expose matter creation, conversion, scope, status, assignment and context through governed services.

Potential MVP APIs:

```text
POST /matters
GET /matters/{id}
PATCH /matters/{id}
POST /orders/{id}/convert-to-matter
POST /matters/{id}/status
POST /matters/{id}/scope
POST /matters/{id}/assignments
POST /matters/{id}/professional-context
POST /matters/{id}/workflow-reference
POST /matters/reference/validate
```

Potential partial APIs:

```text
POST /matters/{id}/review
POST /matters/{id}/close
POST /matters/{id}/cancel
GET /matters/{id}/audit-reference
POST /matters/{id}/ai-summary
```

API rules:

```text
- APIs must invoke Matter Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not mutate Order commercial scope except through approved Order services.
- APIs must not bypass Workflow Contract for status transition.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Client Portal
Partner Center
Service Platform
Reporting consumers
Opportunity Engine baseline
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced analytics
Case management products
Official connector products
```

Product rule:

```text
Products consume Matter.
Products do not redefine Matter.
```

---

# 17. MVP Scope

Matter is a Phase 3 / Wave 3 Must Implement domain.

MVP includes:

```text
Matter
Matter Type
Matter Status
Matter Scope
Matter Party
Matter Assignment
Matter Professional Context
Matter-Order Link
Matter Workflow Reference
Matter Task Reference
Matter Creation Service
Order-to-Matter Conversion Service
Matter Update Service
Matter Status Service
Matter Scope Service
Matter Assignment Service
Matter Professional Context Service
Matter Workflow Reference Service
Matter Reference Validation Service
MatterCreated event
OrderConvertedToMatter event
MatterUpdated event
MatterStatusChanged event
MatterScopeUpdated event
MatterAssigned event
MatterProfessionalContextLinked event
MatterWorkflowLinked event
MatterReferenceValidated event
basic matter metadata validation
source traceability to Customer, Order, Brand, Trademark, Workflow, Task and AI systems
```

MVP should support:

```text
basic matter creation
order-to-matter conversion
matter scope
matter assignment
matter status
professional context linking
workflow reference
task reference
AI-assisted matter summary with human review
```

MVP does not require full case management suite, external official filing workflow or advanced litigation matter management.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full litigation case management
opposition/cancellation matter suite
automatic official filing workflow
advanced deadline engine
multi-provider matter marketplace
matter profitability analytics
automatic matter staffing
complex matter splitting/merging automation
external case management integrations
advanced client portal matter collaboration
cross-border associate workbench
matter risk scoring
matter SLA automation
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Matter should use stable immutable ID.
Matter Scope should be explicit and version-aware if changed.
Matter Status should use controlled values.
Order-to-Matter conversion should be idempotent.
Matter Assignment should reference Identity/User/Organization through approved contracts.
Matter Professional Context should link to Brand, Trademark, Jurisdiction, Classification, Document and Evidence without owning their meanings.
Matter Workflow Reference should point to approved Workflow Contract or workflow instance.
AI-generated matter summaries should remain draft/recommendation output until reviewed where needed.
```

Suggested Matter Status values:

```text
Draft
Opened
Intake
Assigned
InProgress
WaitingForCustomer
WaitingForAgent
WaitingForOffice
ReviewRequired
Completed
Closed
Cancelled
Suspended
Archived
```

MVP controlled Matter Status values:

```text
Draft
Opened
Assigned
InProgress
WaitingForCustomer
WaitingForAgent
ReviewRequired
Completed
Closed
Cancelled
Archived
```

Suggested Matter Type values:

```text
TrademarkApplication
TrademarkOfficeAction
TrademarkRenewal
TrademarkChange
TrademarkAssignment
TrademarkOpposition
TrademarkCancellation
TrademarkSearch
TrademarkMonitoring
ClassificationReview
DocumentReview
EvidenceReview
GeneralConsultation
```

MVP controlled Matter Type values:

```text
TrademarkApplication
TrademarkOfficeAction
TrademarkRenewal
TrademarkChange
TrademarkAssignment
TrademarkSearch
ClassificationReview
DocumentReview
EvidenceReview
GeneralConsultation
```

Do not treat a project board card as Core Matter meaning.

---

# 20. Codex Implementation Notes

Codex may implement Matter only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Matter / Order boundary
preserve Matter / Customer boundary
preserve Matter / Task / Workflow boundaries
preserve Matter / Professional Core object boundaries
implement only MVP scope unless task says otherwise
write tests for matter creation
write tests for order-to-matter conversion idempotency
write tests for matter scope update
write tests for matter assignment
write tests for matter status transition through governed service
write tests preventing Matter from owning Order pricing/payment
write tests preventing direct workflow state mutation outside Workflow Contract
```

Codex must not:

```text
invent Order pricing or payment inside Matter
invent full case management suite in MVP
invent official filing automation inside Matter
invent Task lifecycle inside Matter
invent Workflow state model inside Matter
close or complete Matter without governed service and required review
allow AI to change Matter status directly
allow product UI to redefine Matter status
```

---

# 21. Validation Rules

Matter Domain must pass the following checks.

```text
[ ] Matter is classified as Business Execution Domain.
[ ] Matter is counted within the 26 baseline Core Domains.
[ ] Matter does not change the baseline Core Domain Map.
[ ] Matter has MVP Phase 3 / Wave 3 classification.
[ ] Matter has MVP Depth = Must Implement.
[ ] Matter defines Core meaning.
[ ] Matter boundary excludes Customer lifecycle.
[ ] Matter boundary excludes Order pricing and payment lifecycle.
[ ] Matter boundary excludes Task lifecycle.
[ ] Matter boundary excludes Workflow state model.
[ ] Matter boundary excludes Professional Core object meanings.
[ ] Matter owns Matter object.
[ ] Matter defines Matter Scope.
[ ] Matter defines Matter Status.
[ ] Matter defines Matter Assignment.
[ ] Matter defines Matter Professional Context.
[ ] Matter defines Order-to-Matter conversion boundary.
[ ] Matter lists primary services.
[ ] Mutating Matter services emit events.
[ ] Matter lists primary events.
[ ] Matter defines contract requirements.
[ ] Matter defines AI Agent usage constraints.
[ ] Matter defines workflow usage constraints.
[ ] Matter defines API usage constraints.
[ ] Matter defines product consumers.
[ ] Matter defines MVP and deferred scope.
[ ] Matter defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Matter into Order
turn Matter into Customer
turn Matter into Task
turn Matter into Workflow
turn Matter into Document or Evidence
turn Matter into full case management suite
turn Matter into official filing automation
turn Matter into billing or payment lifecycle
turn Matter into pricing policy
invent workflow states inside Matter
close or complete Matter without governed rules
allow AI to change Matter status directly
allow product UI to redefine Matter meaning
allow Codex to define new matter architecture
```

---

# 23. Acceptance Criteria

This Matter Domain Specification is accepted only if:

```text
[ ] It defines Matter purpose.
[ ] It defines Matter Core meaning.
[ ] It identifies Matter as Business Execution Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Customer, Order, Brand, Trademark, Jurisdiction, Classification, Document, Evidence, Task, Workflow, Communication, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Matter Domain specification. Establishes Matter as Phase 3 Business Execution Domain, defines Matter, Scope, Status, Assignment, Professional Context, Order-to-Matter conversion, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
