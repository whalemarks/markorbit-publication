# Event Specification — MatterCreated

**Spec ID:** B02-EVT-MATTER-CREATED  
**Spec Type:** Event  
**Event Name:** MatterCreated  
**Event File:** core-specs/events/matter-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Matter  
**Producing Service:** core-specs/services/matter-service.md  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/matter-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/matter-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/matter-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

MatterCreated records that a governed Matter professional execution container reference has been created by Matter Service.

It exists so that Order, Customer, Brand, Trademark, Workflow Contract, Task, Document, Evidence, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a professional execution container now exists without treating that Matter as Order, Task, Workflow execution, filing submission, payment, invoice, document completion, evidence sufficiency or final professional decision.

MatterCreated is required before:

```text
professional execution container trace
order-to-matter conversion trace
customer/brand/trademark execution context
workflow contract application review
task planning and assignment preparation
document and evidence execution context
AI-assisted matter intake review
policy-controlled matter visibility
API matter reference validation
audit trace for matter-sensitive actions
```

---

# 2. Event Meaning

MatterCreated means:

```text
a stable Matter object reference has been created through governed Matter Service operation.
```

MatterCreated does not mean:

```text
an Order has been created
a Task has been created
a Workflow Contract has started
a filing has been submitted
payment has been received
invoice has been issued
documents are complete
evidence is sufficient
the Matter is ready for all execution steps
AI matter intake suggestion has been accepted as final professional decision
```

MatterCreated records professional execution container creation only.

It does not establish task execution, workflow start, filing readiness, official submission, payment or professional approval.

---

# 3. Event Category

MatterCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Matter domain.

It is not an Order event, Task event, Workflow event, Filing event, Payment event or Invoice event.

---

# 4. Event Producer

Producing service:

```text
Matter Service
```

Producing operation:

```text
createMatter
```

Source domain:

```text
Matter
```

Source object type:

```text
Matter
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Matter Service createMatter
        ↓
Event Service record MatterCreated
```

Producer rules:

```text
- MatterCreated must be emitted only after Matter Service successfully creates the Matter reference.
- MatterCreated must not be emitted directly by product UI.
- MatterCreated must not be emitted directly by AI Agent outside governed service operation.
- MatterCreated must not be emitted for failed, duplicate-rejected or unauthorized matter creation attempts.
```

---

# 5. Event Trigger

MatterCreated is triggered when:

```text
Matter Service successfully creates a new Matter object and commits its stable matter_reference_id.
```

Required trigger conditions:

```text
createMatter operation completed
matter_reference_id created
matter_type validated
matter_status validated
order_reference_id captured where applicable
customer/professional object context captured where applicable
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Order creation
Customer creation
Trademark creation
Task creation
Workflow Contract definition
Workflow Contract application
document upload
evidence registration
filing submission
payment received
invoice issued
AI matter suggestion
failed validation
duplicate rejected Matter
```

Related but separate events may include:

```text
OrderCreated
CustomerCreated
TrademarkCreated
TaskCreated
WorkflowContractApplied
DocumentCreated
EvidenceCreated
TrademarkFiled
PaymentReceived
InvoiceIssued
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: MatterCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Matter
source_service: Matter Service
source_operation: createMatter
source_object_type: Matter
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/matter-created-payload.md
safe_summary:
  matter_reference_id: string
  matter_type: string
  matter_status: string
  order_reference_id: string | null
  customer_reference_id: string | null
  source_type: string
restricted_fields_policy: MatterCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
matter_reference_id: string
matter_type: string
matter_status: string
matter_source_type: string
order_reference_id: string | null
customer_reference_id: string | null
brand_reference_id: string | null
trademark_reference_id: string | null
jurisdiction_reference_ids: list[string]
classification_reference_ids: list[string]
workflow_contract_reference_id: string | null
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references rather than embedding confidential execution strategy by default.
- Payload must not include payment credentials, invoice details, restricted customer information or legal strategy.
- Payload must not imply Task creation, Workflow activation, filing submission, document completion or evidence sufficiency.
- Payload must not imply professional approval of all Matter steps.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
matter_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
order_reference_id
customer_reference_id
brand_reference_id
trademark_reference_id
jurisdiction_reference_ids
classification_reference_ids
workflow_contract_reference_id
task_reference_ids
document_reference_ids
evidence_reference_ids
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal matter_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- order_reference_id must not imply Order creation unless Order Service emits OrderCreated.
- workflow_contract_reference_id must not imply workflow activation unless Workflow Contract Service emits its own event.
- task_reference_ids must not imply Task creation unless Task Service emits TaskCreated.
- document_reference_ids and evidence_reference_ids must not imply completion or sufficiency.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
MatterCreated
```

## 8.2 event_category

```text
DomainEvent
```

## 8.3 event_status

```text
Recorded
Validated
DispatchPending
Dispatched
DispatchFailed
Consumed
Ignored
Archived
DeletedReferenceOnly
```

## 8.4 matter_type

```text
TrademarkApplicationMatter
TrademarkRenewalMatter
TrademarkChangeMatter
TrademarkResponseMatter
TrademarkOppositionMatter
TrademarkSearchMatter
ConsultationMatter
DocumentServiceMatter
EvidenceServiceMatter
InternalMatter
Other
Unknown
```

## 8.5 matter_status

```text
Draft
Opened
ReviewRequired
WorkflowPending
InProgress
OnHold
Completed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 matter_source_type

```text
OrderConversion
ProfessionalInput
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
MatterCreated
OrderConverted
ProfessionalCreated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 MatterCreated Records Execution Container Creation

MatterCreated records that a Matter reference exists.

It must not be interpreted as Task creation, Workflow activation, filing submission, payment, invoice or professional completion.

## 9.2 Matter Is Not Order

Order Service owns commercial service request.

Matter may be created from Order, but MatterCreated does not create or validate Order.

## 9.3 Matter Is Not Task

Task Service owns actionable work units.

MatterCreated does not create tasks automatically.

## 9.4 Matter Is Not Workflow Execution

Workflow Contract Service defines allowed execution structure.

MatterCreated may reference a workflow contract, but does not activate workflow unless governed separately.

## 9.5 Matter Does Not Own Document or Evidence Lifecycle

Document Service and Evidence Service own their own lifecycle.

Matter may reference them as execution context only.

## 9.6 MatterCreated Does Not Approve Filing

Filing requires governed workflow, professional review and applicable permission/policy checks.

MatterCreated alone does not approve submission.

## 9.7 MatterCreated Must Respect Permission and Policy

Matter creation and visibility must respect Permission, Policy, customer confidentiality and organization access context.

## 9.8 MatterCreated Must Be Immutable

MatterCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Order Service
Customer Service
Brand Service
Trademark Service
Workflow Contract Service
Task Service
Document Service
Evidence Service
Policy Service
Permission Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Order Service may link Order to Matter through governed operation.
- Workflow Contract Service may evaluate applicable workflow contract but must not activate workflow silently.
- Task Service may create tasks only through governed Task Service operation.
- Document and Evidence services may link Matter context but must not infer completion or sufficiency.
- AI Agents may assist matter intake only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Matter creation trace.
```

Consumers must not:

```text
treat MatterCreated as OrderCreated
treat MatterCreated as TaskCreated
treat MatterCreated as Workflow activation
treat MatterCreated as filing submission
treat MatterCreated as payment or invoice
treat MatterCreated as Document completion or Evidence sufficiency
expose restricted matter strategy or customer data
```

---

# 11. Relationship to Services

Producing service:

```text
Matter Service produces MatterCreated after createMatter succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches MatterCreated.
```

Related services:

```text
Order Service provides commercial request context.
Customer, Brand and Trademark services provide business/professional object context.
Workflow Contract Service may define allowed execution structure.
Task Service may create actionable work units after Matter exists.
Document Service may link artifacts to Matter context.
Evidence Service may link proof materials to Matter context.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or act on Matter.
Audit Service records accountability trace.
AI Agent Governance controls AI matter intake behavior.
```

Boundary reminders:

```text
Matter Service owns professional execution container.
Order Service owns commercial service request.
Task Service owns actionable work unit.
Workflow Contract Service owns execution structure.
Document Service owns artifacts.
Evidence Service owns proof layer.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /matters/{matter_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create MatterCreated directly.
- API must call Matter Service createMatter, which emits the event.
- API must not expose restricted execution strategy, payment data, customer confidential data or legal strategy.
- API must distinguish MatterCreated from OrderCreated, TaskCreated, WorkflowContractApplied, DocumentCreated, EvidenceCreated and filing events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Matter reference was created
explain that Matter is not Order, Task, Workflow, payment, invoice or filing
flag missing Order/Customer/Trademark context for review
flag Matter requiring workflow contract review
suggest next governed execution setup step
prepare audit-safe Matter creation summary
```

AI must not:

```text
fabricate MatterCreated
rewrite MatterCreated
delete MatterCreated
treat MatterCreated as Task creation or Workflow activation
treat MatterCreated as filing instruction approval
treat MatterCreated as payment or invoice
treat AI matter suggestion as verified professional fact
hide AI-assisted creation
expose restricted matter, customer or strategy data
```

AI-assisted creation requires:

```text
agent_identity_reference_id
agent_contract_reference_id
authorized_knowledge_reference where applicable
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

MatterCreated is valid only if:

```text
[ ] event_name is MatterCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Matter Service.
[ ] producing operation is createMatter.
[ ] source_domain is Matter.
[ ] source_object_type is Matter.
[ ] source_object_reference_id is present.
[ ] matter_reference_id is present.
[ ] source_object_reference_id equals matter_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] matter_type is controlled.
[ ] matter_status is controlled.
[ ] matter_source_type is controlled.
[ ] payload does not include restricted execution strategy, payment data, customer data or legal strategy unless allowed.
[ ] Order, Task, Workflow, payment, invoice, filing, Document completion and Evidence sufficiency are not implied.
[ ] AI assistance is explicitly identified where applicable.
[ ] event is not used as command.
```

---

# 15. Error / Rejection Handling

Controlled rejection reasons:

```text
EventNameInvalid
EventCategoryInvalid
ProducingServiceMissing
ProducingOperationMissing
SourceObjectMissing
MatterReferenceMissing
MatterReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
MatterTypeInvalid
MatterStatusInvalid
MatterSourceTypeInvalid
RestrictedFieldViolation
ConfidentialMatterPayloadRejected
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownMatterEventError
```

Rejection rules:

```text
- Failed Matter creation must not emit MatterCreated.
- Duplicate rejected Matter creation must not emit MatterCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Matter Service Specification
cite Matter Object Specification
cite Event Service Specification
cite Order/Workflow/Task specs where references are used
use exact event_name: MatterCreated
use exact event_category: DomainEvent
validate matter_reference_id
validate source_object_reference_id equals matter_reference_id
validate actor_reference_id
validate controlled matter_type/status/source_type
validate payload contract
write tests that failed createMatter does not emit MatterCreated
write tests that MatterCreated does not create Order automatically
write tests that MatterCreated does not create Task automatically
write tests that MatterCreated does not activate Workflow automatically
write tests that MatterCreated does not imply filing, payment or invoice
write tests that MatterCreated does not imply Document completion or Evidence sufficiency
write tests that AI-assisted creation is marked where applicable
write tests that restricted matter/customer/payment/strategy data is not exposed
```

Codex must not:

```text
emit MatterCreated directly from UI
treat OrderCreated as MatterCreated
treat MatterCreated as TaskCreated
treat MatterCreated as Workflow activation event
create Task or Workflow silently from MatterCreated
store raw confidential matter/payment/customer data in event payload by default
allow AI to fabricate MatterCreated
use MatterCreated as command to create Task, Workflow, filing, payment, invoice, Document approval or Evidence sufficiency
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines MatterCreated purpose.
[ ] It defines MatterCreated meaning.
[ ] It defines Event category.
[ ] It defines producer and trigger.
[ ] It defines payload contract.
[ ] It defines required references.
[ ] It defines controlled values.
[ ] It defines event rules.
[ ] It defines consumer rules.
[ ] It defines service relationships.
[ ] It defines API relationships.
[ ] It defines AI Agent constraints.
[ ] It defines validation rules.
[ ] It defines error/rejection handling.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial MatterCreated Event specification. Defines governed Matter professional execution container creation event and separates MatterCreated from Order, Task, Workflow, filing, payment, invoice, Document completion, Evidence sufficiency and AI matter suggestion. |

---

**End of Event Specification**
