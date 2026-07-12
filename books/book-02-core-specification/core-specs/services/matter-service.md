# Service Specification — Matter Service

**Spec ID:** B02-SVC-MATTER-SERVICE  
**Spec Type:** Service  
**Service Name:** Matter Service  
**Owning Domain:** Matter  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/matter.md  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/document.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md  
**Related Event Specs:** core-specs/events/matter-created.md; core-specs/events/matter-updated.md; core-specs/events/matter-status-changed.md; core-specs/events/matter-order-linked.md; core-specs/events/matter-workflow-linked.md; core-specs/events/matter-task-linked.md; core-specs/events/matter-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/matter/matter-contract.md; core-specs/contracts/matter/matter-reference-contract.md; core-specs/contracts/matter/matter-order-link-contract.md; core-specs/contracts/matter/matter-workflow-contract.md; core-specs/contracts/matter/matter-task-contract.md; core-specs/contracts/matter/matter-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Matter Service defines the Core service boundary for creating, updating, validating, linking and managing Matter objects.

It exists so that Order, Customer, Brand, Trademark, Workflow Contract, Task, Document, Evidence, Communication, AI Agents, APIs and product consumers can consistently reference the professional execution container without confusing Matter with Order, Task, Workflow Contract, Event, Document, Evidence, Customer request or product UI case card.

Matter Service is required before:

```text
professional case execution
order-to-matter conversion
matter lifecycle management
matter-to-workflow linkage
matter-to-task linkage
matter document and evidence context
trademark matter handling
customer matter tracking
AI-assisted matter summary
audit trace for matter-sensitive actions
```

---

# 2. Core Meaning

Matter Service means:

```text
the Core service that manages professional execution containers and their governed relationships to orders, customers, trademarks, workflow contracts, tasks, documents, evidence and communication context.
```

Matter Service does not mean:

```text
Order Service
Task Service
Workflow engine
Workflow Contract Service
Event Service
Document Service
Evidence Service
billing service
product UI case board
```

Matter Service answers:

```text
Does this Matter exist?
Which Order, Customer, Brand or Trademark does it relate to?
Which Workflow Contract governs it?
Which Tasks, Documents, Evidence and Communications are attached or referenced?
What lifecycle status applies?
Can another domain safely reference this Matter?
What audit trace is required?
```

---

# 3. Service Category

Matter Service is a Business Execution Core Service.

It manages professional execution containers.

It does not own commercial commitment.

It does not execute task work by itself.

It does not define workflow rules by itself.

---

# 4. Architectural Position

Matter Service sits between commercial request and operational execution.

```text
Customer creates demand context
        ↓
Order records commercial service request
        ↓
Matter Service creates professional execution container
        ↓
Workflow Contract defines allowed execution structure
        ↓
Task Service manages actionable work units
        ↓
Document / Evidence / Communication support delivery
```

Order is commercial request.

Matter is execution container.

Task is work unit.

Workflow Contract governs allowed transitions.

---

# 5. Scope

Matter Service includes:

```text
matter creation
matter update
matter status management
matter order linkage
matter customer linkage
matter brand/trademark linkage
matter workflow-contract linkage
matter task linkage
matter document/evidence linkage
matter communication linkage
matter reference validation
matter audit trace
matter event emission
```

MVP scope includes:

```text
create matter
get matter
update matter metadata
change matter status
link matter to order
link matter to customer
link matter to brand/trademark
link matter to workflow contract
link matter to task
link matter to document/evidence
validate matter reference
emit matter events
```

Deferred scope includes:

```text
full workflow execution engine
resource scheduling
billing and invoicing
advanced case analytics
automatic matter strategy generation
external docketing sync
deadline calculation engine
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createMatter | Create Matter object | Yes | MatterCreated |
| getMatter | Retrieve Matter by ID | Yes | No |
| updateMatter | Update governed metadata | Yes | MatterUpdated |
| changeMatterStatus | Change Matter lifecycle status | Yes | MatterStatusChanged |
| linkMatterOrder | Link Matter to Order | Yes | MatterOrderLinked |
| linkMatterCustomer | Link Matter to Customer | Yes | MatterCustomerLinked |
| linkMatterBrand | Link Matter to Brand | Partial | MatterBrandLinked |
| linkMatterTrademark | Link Matter to Trademark | Yes | MatterTrademarkLinked |
| linkMatterWorkflowContract | Link Matter to Workflow Contract | Yes | MatterWorkflowContractLinked |
| linkMatterTask | Link Matter to Task | Yes | MatterTaskLinked |
| linkMatterDocument | Link Matter to Document | Yes | MatterDocumentLinked |
| linkMatterEvidence | Link Matter to Evidence | Partial | MatterEvidenceLinked |
| linkMatterCommunication | Link Matter to Communication | Partial | MatterCommunicationLinked |
| validateMatterReference | Validate whether Matter can be referenced | Yes | MatterReferenceValidated |
| archiveMatter | Archive Matter reference | Partial | MatterArchived |

---

# 7. Inputs

Matter Service accepts:

```text
matter_type
matter_title_reference
status
order_reference_id
customer_reference_id
brand_reference_id
trademark_reference_id
jurisdiction_reference_id
classification_reference_ids
workflow_contract_reference_id
task_reference_ids
document_reference_ids
evidence_reference_ids
communication_reference_ids
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
matter_type
matter_title_reference
status
source_reference
actor_context
```

Required for order linkage:

```text
matter_reference_id
order_reference_id
link_type
actor_context
```

Required for workflow linkage:

```text
matter_reference_id
workflow_contract_reference_id
actor_context
```

Required for validation:

```text
matter_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Matter Service returns:

```text
Matter object
Matter reference
Matter validation result
Matter order link result
Matter workflow link result
Matter task link result
Matter document/evidence link result
Matter status result
Matter event reference
error result
```

Validation output must include:

```text
is_valid
matter_reference_id
matter_type
status
order_reference_hint where applicable
workflow_contract_reference_hint where applicable
reason_code
policy_hint where applicable
```

Validation output must not expose unnecessary confidential customer, document, evidence or strategy data.

---

# 9. Controlled Values

## 9.1 matter_type

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
Monitoring
Consultation
DocumentReview
EvidenceReview
GeneralMatter
Unknown
```

## 9.2 status

```text
Draft
Open
ReadyToStart
InProgress
WaitingForClient
WaitingForAgent
WaitingForOfficialAction
ReviewRequired
Completed
Cancelled
Suspended
Archived
DeletedReferenceOnly
```

## 9.3 order_link_type

```text
CreatedFromOrder
RelatedOrder
SupplementalOrder
HistoricalOrder
Unknown
```

## 9.4 matter_link_type

```text
Primary
Related
Supporting
Historical
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
NotOpen
Suspended
Cancelled
Completed
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Matter Is Professional Execution Container

Matter Service manages professional execution context.

It must not be reduced to a product UI case card.

## 10.2 Matter Is Not Order

Matter may be created from or linked to Order.

Order Service owns commercial service request.

## 10.3 Matter Is Not Task

Matter may contain or reference Tasks.

Task Service owns actionable work units.

## 10.4 Matter Is Not Workflow Contract

Matter may reference a Workflow Contract.

Workflow Contract defines allowed execution structure and transitions.

## 10.5 Matter Does Not Own Document or Evidence Lifecycle

Matter may link Documents and Evidence.

Document Service and Evidence Service own their respective lifecycles.

## 10.6 Matter Status Must Respect Workflow Contract

Where a Workflow Contract is linked, Matter status changes must comply with allowed transitions or require review/exception.

## 10.7 Matter Changes Must Be Auditable

Matter-sensitive operations must preserve actor, source, request context, linked object trace and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Order Service | Matter may be created from Order | Order owns commercial request. |
| Customer Service | Matter may reference Customer | Customer owns demand-side party. |
| Brand Service | Matter may reference Brand | Brand owns commercial identity. |
| Trademark Service | Matter may reference Trademark | Trademark owns protection object. |
| Jurisdiction Service | Matter may reference Jurisdiction | Jurisdiction owns where context. |
| Classification Service | Matter may reference Classification | Classification owns goods/services scope. |
| Workflow Contract Service | Matter may use Workflow Contract | Workflow Contract owns allowed structure. |
| Task Service | Matter may contain Tasks | Task owns work units. |
| Document Service | Matter may link Documents | Document owns artifact lifecycle. |
| Evidence Service | Matter may link Evidence | Evidence owns proof layer. |
| Communication Service | Matter may link Communications | Communication owns message lifecycle. |
| Event Service | Records Matter events | Event records occurrence. |
| Audit Service | Records Matter-sensitive action | Audit owns accountability trail. |

---

# 12. Event Usage

Matter Service emits:

```text
MatterCreated
MatterUpdated
MatterStatusChanged
MatterOrderLinked
MatterCustomerLinked
MatterBrandLinked
MatterTrademarkLinked
MatterWorkflowContractLinked
MatterTaskLinked
MatterDocumentLinked
MatterEvidenceLinked
MatterCommunicationLinked
MatterCompleted
MatterCancelled
MatterSuspended
MatterArchived
MatterReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Status events must preserve previous and next status.
- Workflow-linked status changes must preserve workflow contract reference.
- Task link events must reference Task ID.
- Document and Evidence link events must not expose restricted content.
- AI-generated matter summary events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /matters
GET /matters/{id}
PATCH /matters/{id}
POST /matters/{id}/status
POST /matters/{id}/orders
POST /matters/{id}/customers
POST /matters/{id}/brands
POST /matters/{id}/trademarks
POST /matters/{id}/workflow-contract
POST /matters/{id}/tasks
POST /matters/{id}/documents
POST /matters/{id}/evidence
POST /matters/{id}/communications
POST /matters/reference/validate
```

API rules:

```text
- APIs must invoke Matter Service operations.
- APIs must not create Order automatically unless Order Service is invoked.
- APIs must not create Task automatically unless Task Service is invoked.
- APIs must not bypass Workflow Contract transition rules.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Matter Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Matter context
identify missing Order/Trademark/Workflow links
suggest Matter type for review
draft matter intake note
identify stalled Matter status for review
prepare task suggestions for Task Service review
summarize linked Documents/Evidence where authorized
flag workflow/status mismatch
```

AI must not:

```text
create Matter without authorized service
close, cancel or suspend Matter without authorized service
bypass Workflow Contract
create Order or Task automatically from Matter
make final professional conclusion
submit filings or external communications directly
expose restricted customer/document/evidence data
```

AI Matter use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Matter Access Rule
Customer/Trademark Access Rule where applicable
Document/Evidence Access Rule where applicable
Workflow Rule
Audit Rule
Human Review Rule for professional status changes and external actions
```

---

# 15. Validation Rules

Matter Service must enforce:

```text
[ ] matter_type is controlled.
[ ] status is controlled.
[ ] createMatter requires matter_title_reference.
[ ] createMatter produces stable immutable Matter ID.
[ ] updateMatter does not mutate immutable ID.
[ ] changeMatterStatus follows allowed lifecycle.
[ ] linked Workflow Contract governs allowed status transitions where present.
[ ] linkMatterOrder references valid Order.
[ ] linkMatterTask references valid Task where implemented.
[ ] validateMatterReference rejects missing, cancelled, suspended, archived or deleted-reference matters where not allowed.
[ ] Matter Service does not create Order automatically.
[ ] Matter Service does not create Task automatically.
[ ] Matter Service does not own Document/Evidence lifecycle.
[ ] Matter Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Matter Service should return controlled errors:

```text
MatterNotFound
InvalidMatterType
InvalidMatterStatus
InvalidMatterTransition
InvalidMatterReference
MatterTitleRequired
OrderNotFound
CustomerNotFound
BrandNotFound
TrademarkNotFound
WorkflowContractNotFound
TaskNotFound
DocumentNotFound
EvidenceNotFound
CommunicationNotFound
WorkflowTransitionNotAllowed
MatterSuspended
MatterCancelled
MatterCompleted
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownMatterError
```

Errors must be safe for product display and API consumption.

Sensitive customer, document, evidence and professional strategy information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite matter domain spec
cite matter object spec
cite order, workflow-contract and task specs where relevant
preserve Matter / Order boundary
preserve Matter / Task boundary
preserve Matter / Workflow Contract boundary
preserve Matter / Document / Evidence boundaries
implement only Phase 3 MVP operations unless task says otherwise
write tests for createMatter requiring matter_title_reference
write tests for controlled matter_type
write tests for controlled status
write tests preventing Matter Service from creating Order automatically
write tests preventing Matter Service from creating Task automatically
write tests preventing Matter Service from bypassing Workflow Contract
write tests preventing Matter Service from owning Document/Evidence lifecycle
write tests for event emission on mutation
```

Codex must not:

```text
invent full workflow engine inside Matter Service
treat Matter as Order
treat Matter as Task
treat Matter as Workflow Contract
create Order or Task directly from Matter Service
bypass Workflow Contract transitions
own Document or Evidence lifecycle
allow AI to close/cancel Matter without authorization
allow product UI to redefine Matter status
```

---

# 18. Acceptance Criteria

This Matter Service Specification is accepted only if:

```text
[ ] It defines Matter Service purpose.
[ ] It defines Matter Service Core meaning.
[ ] It identifies Matter Service as Business Execution Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Matter Service specification. Establishes Matter Service as professional execution container service, separates Matter from Order, Task, Workflow Contract, Document and Evidence, and defines Phase 3 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
