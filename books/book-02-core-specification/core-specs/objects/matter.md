# Object Specification — Matter

**Spec ID:** B02-OBJ-MATTER  
**Spec Type:** Object  
**Object Name:** Matter  
**Owning Domain:** Matter  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/matter.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/matter-participant.md; core-specs/objects/matter-scope.md; core-specs/objects/matter-reference.md
**Related Service Specs:** core-specs/services/matter-registration-service.md; core-specs/services/matter-status-service.md; core-specs/services/matter-scope-service.md; core-specs/services/matter-participant-service.md; core-specs/services/matter-workflow-service.md; core-specs/services/matter-reference-validation-service.md  
**Related Event Specs:** core-specs/events/matter-created.md; core-specs/events/matter-updated.md; core-specs/events/matter-status-changed.md; core-specs/events/matter-participant-linked.md; core-specs/events/matter-workflow-linked.md; core-specs/events/matter-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/matter/matter-contract.md; core-specs/contracts/matter/matter-scope-contract.md; core-specs/contracts/matter/matter-status-contract.md; core-specs/contracts/matter/matter-participant-contract.md; core-specs/contracts/matter/matter-workflow-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Matter object defines the Core-recognized professional execution container for trademark-related work in MarkOrbit.

It exists so that Orders, Customers, Brands, Trademarks, Jurisdictions, Classifications, Documents, Evidence, Tasks, Workflow Contracts, Communications, Notifications, AI Agents, Services, APIs and product consumers can consistently coordinate professional execution without confusing Matter with commercial order, task unit, workflow definition, trademark record or document package.

Matter is required before:

```text
professional execution tracking
trademark filing matter
office action matter
renewal matter
change/assignment matter
opposition/cancellation matter
document and evidence coordination
task generation
workflow execution
agent/service-provider collaboration
client progress tracking
AI matter summary
audit trace for professional execution
```

---

# 2. Core Meaning

Matter means:

```text
a Core-recognized professional execution container that groups scope, participants, workflow, tasks, documents, evidence, communications and status around a defined service or trademark-related professional work item.
```

Matter is not:

```text
Order
Task
Workflow Contract
Trademark
Brand
Document
Evidence
Customer
Communication
Notification
Invoice
Payment
AI Output
```

Matter answers:

```text
What professional work is being executed?
Which Customer, Order, Brand or Trademark does it relate to?
Which jurisdiction, classification, document or evidence scope applies?
Which workflow governs the execution?
Which tasks and participants are involved?
What current execution status applies?
Which communications, notifications and audit events belong to it?
```

---

# 3. Object Category

Matter is a Business Execution Object owned by the Matter Domain.

It is the professional execution container.

Order is the commercial service request.

Task is the actionable work unit.

Workflow Contract governs allowed state transitions.

Matter must preserve these boundaries.

---

# 4. Architectural Position

Matter sits between commercial commitment and operational execution.

```text
Customer expresses demand
        ↓
Order records commercial service request
        ↓
Matter becomes professional execution container
        ↓
Workflow Contract governs execution structure
        ↓
Task executes work units
        ↓
Document / Evidence / Communication support execution
        ↓
Event and Audit preserve trace
```

Matter coordinates execution context.

It does not replace Order, Task or Workflow.

---

# 5. Scope

The Matter object includes:

```text
matter id
matter type
matter status
matter title/reference
customer reference
order reference
brand reference
trademark reference
jurisdiction reference
classification reference
matter scope
workflow contract reference
task references
participant references
responsibility references
document references
evidence references
communication references
notification references
agent/service-provider references
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
matter id
matter type
matter status
title/reference
customer reference
order reference
brand reference
trademark reference
jurisdiction reference
classification reference
workflow contract reference
task references
participant references
document references
evidence references
communication references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Matter ID. |
| matter_type | enum | Yes | Yes | Controlled matter type. |
| title_reference | string | Yes | Yes | Human-readable matter title/reference. |
| status | enum | Yes | Yes | Controlled Matter status. |
| customer_reference_id | string | No | Yes | Related Customer reference. |
| order_reference_id | string | No | Yes | Related Order reference. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| jurisdiction_reference_id | string | No | Yes | Related Jurisdiction reference. |
| classification_reference_ids | array | No | Yes | Related Classification references. |
| workflow_contract_reference_id | string | No | Yes | Governing Workflow Contract reference. |
| task_reference_ids | array | No | Yes | Related Task references. |
| participant_references | array | No | Yes | Users, teams, agents, providers or roles. |
| responsibility_reference_ids | array | No | Partial | Business Responsibility references. |
| document_reference_ids | array | No | Yes | Related Document references. |
| evidence_reference_ids | array | No | Partial | Related Evidence references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| notification_reference_ids | array | No | Partial | Related Notification references. |
| agent_reference_ids | array | No | Partial | Related Agent references. |
| service_provider_reference_ids | array | No | Partial | Related Service Provider references. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 matter_type

MVP controlled values:

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
EvidenceReview
DocumentReview
GeneralConsultation
Other
Unknown
```

## 7.2 status

Matter Status is a parent-owned Controlled State Value Specification of Matter, not an independent identity-bearing Core Object. Only the Matter owning Service may mutate `status`; each status change requires an Event trace, and `core-specs/controlled-state-values/matter-status-values.md` is the canonical semantic and transition source. AI and Product UI may display or summarize allowed status values but must not define new Matter statuses or directly change them.

MVP controlled values:

```text
Draft
Open
InProgress
WaitingForCustomer
WaitingForAgent
WaitingForOffice
ReviewRequired
Blocked
Completed
Cancelled
Archived
DeletedReferenceOnly
```

## 7.3 participant_role

Suggested controlled values:

```text
MatterOwner
ProcessOwner
ProfessionalReviewer
TaskAssignee
CustomerContact
AgentContact
ServiceProviderContact
AIAssistant
Observer
Unknown
```

---

# 8. Object Rules

## 8.1 Matter Requires Type, Title and Status

Every Matter must define:

```text
matter_type
title_reference
status
```

A Matter without type or title is not Core-valid.

## 8.2 Matter Is Not Order

Order represents commercial service request.

Matter represents professional execution container.

A Matter may be created from or linked to an Order, but it must not own pricing, payment, invoice or commercial commitment lifecycle.

## 8.3 Matter Is Not Task

Task is the actionable work unit.

Matter groups tasks and execution context.

Matter must not be reduced to a single task.

## 8.4 Matter Is Not Workflow Contract

Workflow Contract defines allowed transitions.

Matter references or instantiates execution under a Workflow Contract.

Matter must not define workflow architecture by itself.

## 8.5 Matter Does Not Own Trademark

Matter may execute work for Trademark.

Trademark remains legal/procedural protection object.

## 8.6 Matter Must Support Execution Trace

Matter should provide traceability across tasks, documents, evidence, communications, notifications, events and participants.

## 8.7 Matter Must Be Auditable

Matter-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
matter creation
matter scope update
matter status change
workflow contract linkage
task linkage
participant linkage
document/evidence linkage
agent/service-provider linkage
matter completion
matter cancellation
AI matter summary or recommendation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Matter may belong to Customer | Customer remains demand-side party. |
| Order | Matter may be created from Order | Order remains commercial request. |
| Brand | Matter may involve Brand | Brand remains commercial identity. |
| Trademark | Matter may involve Trademark | Trademark remains protection object. |
| Jurisdiction | Matter may be jurisdiction-scoped | Jurisdiction remains procedural context. |
| Classification | Matter may involve Classification | Classification remains goods/services scope. |
| Workflow Contract | Matter may reference workflow | Workflow owns transition rules. |
| Task | Matter groups Tasks | Task remains actionable work unit. |
| Document | Matter may link Documents | Document remains artifact. |
| Evidence | Matter may link Evidence | Evidence remains proof layer. |
| Communication | Matter may link Communications | Communication remains message lifecycle. |
| Notification | Matter may trigger Notifications | Notification remains awareness intent. |
| Agent | Matter may involve Agent | Agent remains collaborator. |
| Service Provider | Matter may involve Provider | Provider remains capability profile. |
| Business Responsibility | Matter may assign responsibility | Responsibility remains accountability system. |
| Event | Matter changes emit Events | Event remains signal. |
| Audit Record | Audit may reference Matter | Audit remains accountability system. |

---

# 10. Lifecycle

Matter lifecycle states:

```text
Draft
Open
InProgress
WaitingForCustomer
WaitingForAgent
WaitingForOffice
ReviewRequired
Blocked
Completed
Cancelled
Archived
DeletedReferenceOnly
```

Lifecycle rules are governed by Workflow Contract.

General lifecycle examples:

```text
Draft → Open
Open → InProgress
InProgress → WaitingForCustomer
InProgress → WaitingForAgent
InProgress → WaitingForOffice
WaitingForCustomer → InProgress
WaitingForAgent → InProgress
WaitingForOffice → InProgress
InProgress → ReviewRequired
ReviewRequired → InProgress
InProgress → Blocked
Blocked → InProgress
InProgress → Completed
Open → Cancelled
InProgress → Cancelled
Completed → Archived
Cancelled → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Draft → Completed without workflow/task trace
Cancelled → InProgress without restoration/reopen service
Archived → InProgress without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Matter object is created and managed through:

```text
Matter Registration Service
Matter Update Service
Matter Status Service
Matter Scope Service
Matter Participant Service
Matter Workflow Service
Matter Task Link Service
Matter Document Link Service
Matter Evidence Link Service
Matter Reference Validation Service
Matter Audit Reference Service
```

Service rules:

```text
- Services must validate matter_type.
- Services must validate status transitions against Workflow Contract where applicable.
- Services must emit events for mutating actions.
- Services must not mutate Order commercial lifecycle.
- Services must not execute Task directly.
- Services must not define Workflow Contract.
- Services must not create Trademark, Document or Evidence directly unless their services are invoked.
```

---

# 12. Event Usage

Matter object emits or participates in:

```text
MatterCreated
MatterUpdated
MatterStatusChanged
MatterScopeUpdated
MatterWorkflowLinked
MatterParticipantLinked
MatterTaskLinked
MatterDocumentLinked
MatterEvidenceLinked
MatterCommunicationLinked
MatterCompleted
MatterCancelled
MatterArchived
MatterReferenceValidated
```

Event rules:

```text
- Matter events must reference Matter ID.
- Status events must preserve previous and new status.
- Workflow link events must reference Workflow Contract.
- Task/document/evidence link events must preserve related object reference.
- Events must not expose protected document/evidence content unnecessarily.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /matters
GET /matters/{id}
PATCH /matters/{id}
POST /matters/{id}/status
POST /matters/{id}/workflow
POST /matters/{id}/participants
POST /matters/{id}/tasks
POST /matters/{id}/documents
POST /matters/{id}/evidence
POST /matters/reference/validate
```

API rules:

```text
- APIs must invoke Matter Services.
- APIs must not mutate Order pricing/payment lifecycle.
- APIs must not execute Task directly outside Task services.
- APIs must not create Workflow Contract.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Matter only under governed Agent Contracts.

Allowed AI use:

```text
summarize matter status
identify missing matter scope
identify missing task/document/evidence links
suggest next action for review
draft matter progress note
flag blocked or waiting status
prepare agent/customer follow-up draft
detect workflow/status mismatch
```

AI must not:

```text
close Matter without governed service and review where required
mutate Order commercial lifecycle
create official filing result
change workflow transition without Workflow Contract
send external communication without Communication service
treat summary as professional final decision
expose confidential matter data outside authorized scope
```

AI Matter use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Matter Access Rule
Workflow Rule
Task Rule
Communication Rule where applicable
Audit Rule
Human Review Rule for completion, cancellation or external commitment
```

---

# 15. Validation Rules

Matter object must pass:

```text
[ ] id is present and immutable.
[ ] matter_type is controlled.
[ ] title_reference is present.
[ ] status is controlled.
[ ] Matter does not equal Order.
[ ] Matter does not equal Task.
[ ] Matter does not equal Workflow Contract.
[ ] Matter does not own Trademark.
[ ] Workflow-sensitive status transitions are governed.
[ ] Related references point to valid objects where required.
[ ] Mutating services emit events.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite matter domain spec
preserve Matter / Order boundary
preserve Matter / Task boundary
preserve Matter / Workflow Contract boundary
preserve Matter / Trademark boundary
preserve Matter / Document / Evidence boundaries
implement only MVP fields unless task says otherwise
write tests for required title_reference
write tests for controlled matter_type
write tests for controlled status
write tests preventing Matter from mutating Order commercial lifecycle
write tests preventing Matter from executing Task directly
write tests preventing Matter from defining Workflow Contract
write tests for event emission on mutation
```

Codex must not:

```text
invent full case management system beyond approved MVP
treat Matter as Order
treat Matter as Task
treat Matter as Workflow Contract
create Trademark/Document/Evidence directly from Matter service
close Matter without workflow/status validation
allow AI to complete or cancel Matter without governed service
allow product UI to redefine Matter status
```

---

# 17. Acceptance Criteria

This Matter Object Specification is accepted only if:

```text
[ ] It defines Matter purpose.
[ ] It defines Matter Core meaning.
[ ] It identifies Matter as Business Execution Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Matter object specification. Establishes Matter as professional execution container, separates Matter from Order, Task, Workflow Contract, Trademark, Document and Evidence, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
