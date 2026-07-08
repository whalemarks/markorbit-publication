# Event Specification — OrderCreated

**Spec ID:** B02-EVT-ORDER-CREATED  
**Spec Type:** Event  
**Event Name:** OrderCreated  
**Event File:** core-specs/events/order-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Order  
**Producing Service:** core-specs/services/order-service.md  
**Related Object Specs:** core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/matter.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/matter-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/order-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/order-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/order-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

OrderCreated records that a governed Order commercial service request reference has been created by Order Service.

It exists so that Customer, Brand, Trademark, Matter, Workflow Contract, Task, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a service request now exists without treating that Order as Matter, Task, Workflow execution, payment, invoice, price approval, filing instruction, professional acceptance or automatic service delivery commitment.

OrderCreated is required before:

```text
commercial request trace
customer order context
brand/trademark service request context
matter preparation review
workflow contract selection review
task planning context
pricing/payment readiness review
AI-assisted order intake review
API order reference validation
audit trace for order-sensitive actions
```

---

# 2. Event Meaning

OrderCreated means:

```text
a stable Order object reference has been created through governed Order Service operation.
```

OrderCreated does not mean:

```text
a Matter has been created
a Task has been created
a Workflow Contract has started
payment has been received
invoice has been issued
price has been approved
the order is ready for execution
a filing instruction has been approved
the customer relationship is fully verified
AI intake suggestion has been accepted as final commercial truth
```

OrderCreated records commercial service request creation only.

It does not establish execution, payment, professional acceptance, filing readiness or workflow start.

---

# 3. Event Category

OrderCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Order domain.

It is not a Matter event, Task event, Workflow event, Payment event or Invoice event.

---

# 4. Event Producer

Producing service:

```text
Order Service
```

Producing operation:

```text
createOrder
```

Source domain:

```text
Order
```

Source object type:

```text
Order
```

Allowed producer path:

```text
API / Professional user / Customer intake / System / AI-assisted governed operation
        ↓
Order Service createOrder
        ↓
Event Service record OrderCreated
```

Producer rules:

```text
- OrderCreated must be emitted only after Order Service successfully creates the Order reference.
- OrderCreated must not be emitted directly by product UI.
- OrderCreated must not be emitted directly by AI Agent outside governed service operation.
- OrderCreated must not be emitted for failed, duplicate-rejected or unauthorized order creation attempts.
```

---

# 5. Event Trigger

OrderCreated is triggered when:

```text
Order Service successfully creates a new Order object and commits its stable order_reference_id.
```

Required trigger conditions:

```text
createOrder operation completed
order_reference_id created
order_type validated
order_status validated
customer_reference_id captured where applicable
service_request_context captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Customer creation
Opportunity creation
quotation draft
payment received
invoice created
Matter creation
Task creation
Workflow Contract activation
filing instruction
AI order recommendation
failed validation
duplicate rejected Order
```

Related but separate events may include:

```text
CustomerCreated
OpportunityCreated
OrderUpdated
OrderAccepted
MatterCreated
TaskCreated
WorkflowContractApplied
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
event_name: OrderCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Order
source_service: Order Service
source_operation: createOrder
source_object_type: Order
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/order-created-payload.md
safe_summary:
  order_reference_id: string
  order_type: string
  order_status: string
  customer_reference_id: string | null
  source_type: string
restricted_fields_policy: OrderCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
order_reference_id: string
order_type: string
order_status: string
order_source_type: string
customer_reference_id: string | null
brand_reference_id: string | null
trademark_reference_id: string | null
jurisdiction_reference_ids: list[string]
classification_reference_ids: list[string]
matter_reference_id: string | null
workflow_contract_reference_id: string | null
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references rather than embedding confidential commercial terms by default.
- Payload must not include payment credentials, full invoice details, confidential quotation internals or legal strategy.
- Payload must not imply Matter creation, Task creation, payment receipt, invoice issuance or workflow activation.
- Payload must not imply professional acceptance or filing readiness.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
order_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
customer_reference_id
brand_reference_id
trademark_reference_id
jurisdiction_reference_ids
classification_reference_ids
matter_reference_id
workflow_contract_reference_id
task_reference_id
opportunity_reference_id
quotation_reference_id
payment_reference_id
invoice_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal order_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- customer_reference_id must not imply customer verification unless separately governed.
- matter_reference_id must not imply Matter creation unless Matter Service emits MatterCreated.
- workflow_contract_reference_id must not imply workflow activation unless Workflow Contract Service emits its own event.
- payment_reference_id and invoice_reference_id must not imply payment/invoice state unless Finance services emit their own events.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
OrderCreated
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

## 8.4 order_type

```text
TrademarkApplicationOrder
TrademarkRenewalOrder
TrademarkChangeOrder
TrademarkResponseOrder
TrademarkOppositionOrder
TrademarkSearchOrder
ConsultationOrder
DocumentServiceOrder
EvidenceServiceOrder
InternalServiceOrder
Other
Unknown
```

## 8.5 order_status

```text
Draft
Submitted
ReviewRequired
Accepted
Rejected
ReadyForMatter
MatterLinked
Cancelled
Completed
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 order_source_type

```text
ProfessionalInput
CustomerIntake
PartnerSubmission
OpportunityConversion
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
OrderCreated
ProfessionalCreated
CustomerSubmitted
PartnerSubmitted
OpportunityConverted
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 OrderCreated Records Commercial Request Creation

OrderCreated records that an Order reference exists.

It must not be interpreted as execution, payment, invoicing, Matter creation or professional acceptance.

## 9.2 Order Is Not Matter

Matter Service owns professional execution container.

OrderCreated may lead to Matter creation, but does not create Matter automatically.

## 9.3 Order Is Not Task

Task Service owns actionable work units.

Task creation must occur separately.

## 9.4 Order Is Not Workflow Execution

Workflow Contract Service defines allowed execution structure.

OrderCreated does not start workflow automatically unless a governed workflow operation occurs.

## 9.5 Order Is Not Payment or Invoice

Payment, invoice and settlement are separate financial objects/services outside this Order event.

OrderCreated must not be treated as payment receipt or invoice issuance.

## 9.6 OrderCreated Does Not Approve Filing Instruction

A filing instruction requires professional review, workflow readiness and applicable policy/permission checks.

OrderCreated alone does not approve filing.

## 9.7 OrderCreated Must Respect Permission and Policy

Order creation and visibility must respect Permission, Policy, customer confidentiality and organization access context.

## 9.8 OrderCreated Must Be Immutable

OrderCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Customer Service
Brand Service
Trademark Service
Matter Service
Workflow Contract Service
Task Service
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
- Matter Service may create Matter using Order context only through governed operation.
- Workflow Contract Service may evaluate applicable workflow contract but must not activate workflow silently.
- Task Service may prepare task planning only after governed Matter/Workflow context exists.
- Trademark and Brand services may link order context but must not infer filing readiness.
- AI Agents may assist order intake only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Order creation trace.
```

Consumers must not:

```text
treat OrderCreated as MatterCreated
treat OrderCreated as TaskCreated
treat OrderCreated as payment received
treat OrderCreated as invoice issued
treat OrderCreated as workflow activation
treat OrderCreated as filing instruction approval
expose restricted commercial or customer data
```

---

# 11. Relationship to Services

Producing service:

```text
Order Service produces OrderCreated after createOrder succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches OrderCreated.
```

Related services:

```text
Customer Service provides customer context.
Brand and Trademark services provide professional object context.
Matter Service may create execution container based on Order.
Workflow Contract Service may determine applicable execution structure.
Task Service may create work units after Matter/Workflow context.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or act on Order.
Audit Service records accountability trace.
AI Agent Governance controls AI order intake behavior.
```

Boundary reminders:

```text
Order Service owns commercial service request.
Matter Service owns professional execution container.
Task Service owns actionable work unit.
Workflow Contract Service owns execution structure.
Policy Service owns contextual constraints.
Permission Service owns allowed action.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /orders/{order_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create OrderCreated directly.
- API must call Order Service createOrder, which emits the event.
- API must not expose restricted commercial terms, payment data, customer confidential data or legal strategy.
- API must distinguish OrderCreated from MatterCreated, TaskCreated, WorkflowContractApplied, PaymentReceived and InvoiceIssued.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Order reference was created
explain that Order is not Matter, Task, Workflow, payment or invoice
flag missing Customer/Brand/Trademark context for review
flag order requiring professional intake review
suggest next governed intake step
prepare audit-safe Order creation summary
```

AI must not:

```text
fabricate OrderCreated
rewrite OrderCreated
delete OrderCreated
treat OrderCreated as payment or invoice
treat OrderCreated as Matter or Task
treat OrderCreated as filing instruction approval
treat AI intake suggestion as verified commercial fact
hide AI-assisted creation
expose restricted commercial, customer or strategy data
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

OrderCreated is valid only if:

```text
[ ] event_name is OrderCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Order Service.
[ ] producing operation is createOrder.
[ ] source_domain is Order.
[ ] source_object_type is Order.
[ ] source_object_reference_id is present.
[ ] order_reference_id is present.
[ ] source_object_reference_id equals order_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] order_type is controlled.
[ ] order_status is controlled.
[ ] order_source_type is controlled.
[ ] payload does not include restricted commercial terms, payment data, customer data or legal strategy unless allowed.
[ ] Matter, Task, Workflow, payment, invoice and filing approval are not implied.
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
OrderReferenceMissing
OrderReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
OrderTypeInvalid
OrderStatusInvalid
OrderSourceTypeInvalid
RestrictedFieldViolation
ConfidentialOrderPayloadRejected
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownOrderEventError
```

Rejection rules:

```text
- Failed Order creation must not emit OrderCreated.
- Duplicate rejected Order creation must not emit OrderCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Order Service Specification
cite Order Object Specification
cite Event Service Specification
cite Customer/Brand/Trademark/Matter specs where references are used
use exact event_name: OrderCreated
use exact event_category: DomainEvent
validate order_reference_id
validate source_object_reference_id equals order_reference_id
validate actor_reference_id
validate controlled order_type/status/source_type
validate payload contract
write tests that failed createOrder does not emit OrderCreated
write tests that OrderCreated does not create Matter automatically
write tests that OrderCreated does not create Task automatically
write tests that OrderCreated does not activate Workflow automatically
write tests that OrderCreated does not imply payment or invoice
write tests that OrderCreated does not approve filing instruction
write tests that AI-assisted creation is marked where applicable
write tests that restricted order/customer/payment/strategy data is not exposed
```

Codex must not:

```text
emit OrderCreated directly from UI
treat CustomerCreated or OpportunityCreated as OrderCreated
treat OrderCreated as MatterCreated
treat OrderCreated as TaskCreated
create Matter, Task or Workflow silently from OrderCreated
store raw confidential commercial/payment/customer data in event payload by default
allow AI to fabricate OrderCreated
use OrderCreated as command to create Matter, Task, Workflow, payment, invoice or filing submission
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines OrderCreated purpose.
[ ] It defines OrderCreated meaning.
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
| 0.1.0 | Draft | Initial OrderCreated Event specification. Defines governed Order commercial service request creation event and separates OrderCreated from Matter, Task, Workflow, payment, invoice, filing approval and AI intake suggestion. |

---

**End of Event Specification**
