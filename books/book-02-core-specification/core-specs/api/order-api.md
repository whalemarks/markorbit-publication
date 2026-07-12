# API Specification — Order API

**Spec ID:** B02-API-ORDER  
**Spec Type:** API Specification  
**API Name:** Order API  
**API File:** core-specs/api/order-api.md  
**Related Domain:** core-specs/domains/order.md  
**Related Object Specs:** core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/opportunity.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/opportunity-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/order-created.md; core-specs/events/matter-created.md; core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/order-api-contract.md; core-specs/contracts/events/order-created-payload.md  
**Related Agent Specs:** core-specs/agents/order-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Order API exposes governed Order operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and prepare Order references without treating Order as Matter, payment settlement, invoice, official filing, workflow execution, task completion, customer legal instruction, professional conclusion, service-provider routing decision or AI-approved transaction.

Order API exists to support:

```text
commercial service order context
customer-to-service purchase/engagement structure
matter preparation and linkage
service scope reference
jurisdiction and trademark order context
workflow contract application preparation
task creation preparation
policy-controlled order visibility
AI-assisted order intake and review under governance
event trace access
API-safe order reference validation
```

Order API does not settle payment, issue invoices, file applications, execute tasks, approve legal work or replace business confirmation.

---

# 2. API Meaning

Order API means:

```text
a governed interface for operating commercial service order context through Order Service.
```

Order API does not mean:

```text
Matter API
Payment API
Invoice API
Filing API
Task API
Workflow execution API
Routing API
legal instruction API
professional conclusion API
AI transaction approval API
```

Order owns commercial/execution order context.

Matter owns professional case context.

Task owns work execution.

Workflow Contract defines executable workflow structure.

---

# 3. API Boundary

Order API is responsible for:

```text
Order create request intake
Order read/search/list access
Order update request intake
Order reference validation
Order context preparation
Order link request intake where explicitly governed
safe Order response shaping
Permission/Policy enforcement for Order operations
Order-related Event reference exposure where allowed
AI Agent access boundary for Order operations
controlled API errors
```

Order API is not responsible for:

```text
payment settlement
invoice issuance
Matter professional conclusion
Task execution
Workflow Contract definition
official filing execution
service provider routing decision
customer legal instruction approval
communication delivery
AI final transaction decision
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/order.md
```

Domain rule:

```text
Order represents commercial service order context.
Order is not Matter, payment, invoice, filing, Task execution or professional conclusion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/order.md
core-specs/objects/customer.md
core-specs/objects/matter.md
core-specs/objects/opportunity.md
core-specs/objects/trademark.md
core-specs/objects/brand.md
core-specs/objects/jurisdiction.md
core-specs/objects/classification.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/workflow-contract.md
core-specs/objects/task.md
core-specs/objects/event.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Order API returns order_reference_id.
- Order API may reference Customer, Opportunity, Matter, Trademark, Brand, Jurisdiction, Classification, Document, Evidence, Workflow Contract or Task context but must not create them silently unless explicitly defined by a governed operation.
- Order API must not treat Order as paid or invoiced unless separate finance/payment state exists.
- Order API must not treat Order as official filing or completed work.
- Order API must not expose restricted pricing, commercial terms, customer strategy or internal work notes by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/order-service.md
core-specs/services/customer-service.md
core-specs/services/matter-service.md
core-specs/services/opportunity-service.md
core-specs/services/trademark-service.md
core-specs/services/brand-service.md
core-specs/services/jurisdiction-service.md
core-specs/services/classification-service.md
core-specs/services/document-service.md
core-specs/services/evidence-service.md
core-specs/services/workflow-contract-service.md
core-specs/services/task-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Order API must invoke Order Service for Order behavior.
- Order API must validate related references through their owning services where required.
- Order API must invoke Permission Service where operation requires authorization.
- Order API must invoke Policy Service where contextual constraints apply.
- Order API must not emit Order events directly; Order Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/order-created.md
core-specs/events/matter-created.md
core-specs/events/task-created.md
core-specs/events/workflow-contract-applied.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createOrder may result in OrderCreated.
- creating Matter must use Matter Service and may result in MatterCreated.
- applying Workflow Contract must use Workflow Contract Service and may result in WorkflowContractApplied.
- creating Tasks must use Task Service and may result in TaskCreated.
- API consumers must not fabricate OrderCreated.
- OrderCreated is commercial order-context trace, not payment, invoice, filing, workflow execution or task completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Order

**Operation Category:** Create  
**Method:** POST  
**Path:** `/orders`  
**Owning Service Operation:** `createOrder`  
**Permission Required:** `order:create`  
**Policy Required:** `OrderCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-prepared  
**Event Behavior:** Service Must Emit OrderCreated

Meaning:

```text
Create a governed Order commercial service context.
```

Non-meaning:

```text
does not settle payment
does not issue invoice
does not create Matter automatically unless explicit operation does so
does not file application
does not execute workflow
does not create Task automatically unless explicit operation does so
does not approve professional conclusion
does not grant Permission
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Order Service createOrder
  ↓
Event Service record OrderCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Order

**Operation Category:** Read  
**Method:** GET  
**Path:** `/orders/{order_reference_id}`  
**Owning Service Operation:** `getOrder`  
**Permission Required:** `order:read`  
**Policy Required:** `OrderVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Order view.
```

Non-meaning:

```text
does not expose restricted pricing or commercial terms automatically
does not expose customer strategy automatically
does not expose payment credentials or invoices automatically
does not assert official filing or work completion automatically
```

## 8.3 Operation: Search Orders

**Operation Category:** Search  
**Method:** GET  
**Path:** `/orders`  
**Owning Service Operation:** `searchOrders`  
**Permission Required:** `order:search`  
**Policy Required:** `OrderVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Order references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted order database access
does not expose restricted commercial, payment, customer or strategy data by default
```

## 8.4 Operation: Update Order

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/orders/{order_reference_id}`  
**Owning Service Operation:** `updateOrder`  
**Permission Required:** `order:update`  
**Policy Required:** `OrderUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit OrderUpdated where event is defined

Meaning:

```text
Update governed Order metadata, status or commercial context under Order Service rules.
```

Non-meaning:

```text
does not settle payment automatically
does not issue invoice automatically
does not update official filing status automatically
does not execute workflow or tasks automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Order Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/orders/reference/validate`  
**Owning Service Operation:** `validateOrderReference`  
**Permission Required:** `order:validate`  
**Policy Required:** `OrderReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Order reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not prove payment
does not authorize filing
does not approve service delivery
does not approve task execution
does not prove customer legal instruction
```

## 8.6 Operation: Link Order to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/orders/{order_reference_id}/links`  
**Owning Service Operation:** `linkOrderToObject`  
**Permission Required:** `order:link`  
**Policy Required:** `OrderLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit OrderUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Order and a target Core object.
```

Non-meaning:

```text
does not create target object
does not settle payment
does not file or submit anything
does not approve professional decision
```

## 8.7 Operation: Prepare Order from Opportunity

**Operation Category:** Action  
**Method:** POST  
**Path:** `/orders/prepare-from-opportunity`  
**Owning Service Operation:** `prepareOrderFromOpportunity`  
**Permission Required:** `order:opportunity:prepare`  
**Policy Required:** `OrderOpportunityPreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit OrderCreated unless createOrder succeeds separately

Meaning:

```text
Prepare a governed Order draft context from Opportunity context.
```

Non-meaning:

```text
does not create Order automatically
does not accept commercial terms
does not create Matter
does not settle payment
```

## 8.8 Operation: Create Matter from Order

**Operation Category:** Action  
**Method:** POST  
**Path:** `/orders/{order_reference_id}/matters/create`  
**Owning Service Operation:** `createMatterFromOrder`  
**Permission Required:** `order:matter:create`  
**Policy Required:** `OrderMatterCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Matter Service; may emit MatterCreated

Meaning:

```text
Create governed Matter context from an approved Order context.
```

Non-meaning:

```text
does not execute workflow
does not file application
does not approve professional conclusion
does not settle payment
```

## 8.9 Operation: Apply Workflow Contract to Order

**Operation Category:** Action  
**Method:** POST  
**Path:** `/orders/{order_reference_id}/workflow-contracts/{workflow_contract_reference_id}/apply`  
**Owning Service Operation:** `applyWorkflowContractToOrder`  
**Permission Required:** `order:workflow-contract:apply`  
**Policy Required:** `OrderWorkflowContractPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Must route through Workflow Contract Service; may emit WorkflowContractApplied

Meaning:

```text
Apply a governed Workflow Contract to an Order context.
```

Non-meaning:

```text
does not execute all tasks automatically
does not approve legal work product
does not bypass workflow policy
does not create payment obligation
```

## 8.10 Operation: Create Tasks from Order Plan

**Operation Category:** Action  
**Method:** POST  
**Path:** `/orders/{order_reference_id}/tasks/create-from-plan`  
**Owning Service Operation:** `createTasksFromOrderPlan`  
**Permission Required:** `order:tasks:create`  
**Policy Required:** `OrderTaskCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated plan  
**Event Behavior:** Must route through Task Service; may emit TaskCreated

Meaning:

```text
Create governed Tasks from an approved Order plan.
```

Non-meaning:

```text
does not execute Tasks automatically
does not complete service delivery
does not bypass assignee/permission rules
```

## 8.11 Operation: List Order Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/orders/{order_reference_id}/events`  
**Owning Service Operation:** `listOrderEvents`  
**Permission Required:** `order:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Order-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Order Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_type: string
  order_status: string | optional
  customer_reference_id: string
  opportunity_reference_id: string | null
  matter_reference_id: string | null
  trademark_reference_id: string | null
  brand_reference_id: string | null
  jurisdiction_reference_id: string | null
  service_scope_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_prepared: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Order Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  order_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_status: string | optional
  order_type: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Order Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Order to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  order_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Prepare Order from Opportunity Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  opportunity_reference_id: string
  customer_reference_id: string | null
  intended_service_type: string
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.6 Create Matter from Order Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  order_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  matter_creation_mode: string
  request_context: object
```

## 9.7 Apply Workflow Contract to Order Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  order_reference_id: string
  workflow_contract_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  apply_mode: string
  request_context: object
```

## 9.8 Create Tasks from Order Plan Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  order_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  order_plan_reference_id: string | null
  task_creation_mode: string
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted payment data, customer secrets, privileged notes, raw document content or evidence content by default.
- Requests must use controlled order_type, order_status, source_type, link_type, matter_creation_mode, apply_mode and task_creation_mode values.
- AI-prepared order context must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Order Response

```yaml
status: 200
body:
  order_reference_id: string
  order_type: string
  order_status: string
  customer_reference_id: string
  opportunity_reference_id: string | null
  matter_reference_id: string | null
  trademark_reference_id: string | null
  brand_reference_id: string | null
  jurisdiction_reference_id: string | null
  service_scope_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    commercial_context_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Order Response

```yaml
status: 201
body:
  order_reference_id: string
  order_status: string
  review_required: boolean
  related_event_reference_ids:
    - order_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Order Reference Validation Response

```yaml
status: 200
body:
  order_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Order Preparation Response

```yaml
status: 200
body:
  order_draft_reference_id: string | null
  usable_for_order_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Matter Creation from Order Response

```yaml
status: 200
body:
  order_reference_id: string
  matter_reference_id: string | null
  matter_creation_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Workflow Contract Application Response

```yaml
status: 200
body:
  order_reference_id: string
  workflow_contract_reference_id: string
  workflow_contract_applied_reference_id: string | null
  application_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply payment, invoice issuance, official filing, task execution or professional conclusion.
- Responses must not expose restricted pricing, commercial, payment, customer, strategy, document or evidence fields by default.
- Responses must distinguish Order references from Matter, Task and Workflow Contract references.
- Responses must identify review requirements for AI-prepared or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 order_type

```text
TrademarkSearchOrder
TrademarkFilingOrder
RenewalOrder
OfficeActionOrder
OppositionOrder
CancellationOrder
RecordalOrder
PortfolioOrder
ConsultationOrder
InternalOrder
Unknown
```

## 11.2 order_status

```text
Draft
Prepared
ReviewRequired
Confirmed
Active
OnHold
Completed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
CustomerIntake
OpportunityDerived
MatterDerived
CommunicationDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
PrimaryOrderObject
SupportingObject
SourceObject
RelatedObject
WorkflowObject
TaskSource
ReferenceOnly
Unknown
```

## 11.5 intended_service_type

```text
TrademarkSearch
TrademarkFiling
Renewal
OfficeAction
Opposition
Cancellation
Recordal
PortfolioManagement
Consultation
Unknown
```

## 11.6 matter_creation_mode

```text
Preview
CreateDraftMatter
CreateActiveMatter
Unknown
```

## 11.7 apply_mode

```text
Preview
ApplyWithoutTaskCreation
ApplyAndPrepareTasks
ApplyAndCreateTasks
Unknown
```

## 11.8 task_creation_mode

```text
Preview
CreateDraftTasks
CreateActiveTasks
Unknown
```

## 11.9 application_status

```text
Previewed
Applied
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.10 matter_creation_status

```text
Previewed
Created
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.11 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
ContextMismatch
Unknown
```

## 11.12 intended_use

```text
MatterPreparation
TaskPreparation
WorkflowContractApplication
PaymentPreparation
DocumentContext
EvidenceContext
CustomerContext
TrademarkContext
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
order:create
order:read
order:search
order:update
order:validate
order:link
order:opportunity:prepare
order:matter:create
order:workflow-contract:apply
order:tasks:create
order:event:read
```

Rules:

```text
- Order read/search must be permission-controlled.
- Order creation must not imply payment, invoice issuance, filing or task execution.
- Order validation must not authorize payment, filing or task execution.
- Order-to-object linking requires separate permission.
- Matter creation, Workflow Contract application and Task creation require separate permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
OrderCreationPolicy
OrderUpdatePolicy
OrderVisibilityPolicy
OrderReferencePolicy
OrderLinkPolicy
OrderOpportunityPreparationPolicy
OrderMatterCreationPolicy
OrderWorkflowContractPolicy
OrderTaskCreationPolicy
EventVisibilityPolicy
AIAgentOrderAccessPolicy
RestrictedOrderDataPolicy
CrossOrganizationOrderPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Order fields.
- Policy may require human review for AI-prepared Order data.
- Policy may restrict cross-organization Order lookup.
- Policy may restrict pricing, payment, commercial terms, customer strategy, internal notes, document/evidence details and privileged work product.
- Policy may restrict Matter creation, Workflow Contract application and Task creation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Order: Restricted / HumanReviewRequired where AI-prepared
Get Order: Restricted
Search Orders: Restricted
Update Order: Restricted / HumanReviewRequired where sensitive
Validate Order Reference: Allowed under contract
Link Order to Object: Restricted / HumanReviewRequired where AI-suggested
Prepare Order from Opportunity: Restricted / HumanReviewRequired
Create Matter from Order: Restricted / HumanReviewRequired where AI-assisted
Apply Workflow Contract to Order: Restricted / HumanReviewRequired where AI-suggested
Create Tasks from Order Plan: Restricted / HumanReviewRequired where AI-generated plan
List Order Events: Restricted
```

AI Agents may:

```text
summarize safe Order metadata
flag missing order context items
validate Order references for authorized actions
suggest Order-to-object links for human review
prepare Order draft context for human review
suggest Matter creation for human review
suggest Workflow Contract application for human review
prepare Task plan draft for human review
```

AI Agents must not:

```text
fabricate Order
fabricate OrderCreated events
treat AI-prepared Order as confirmed commercial transaction
settle payment or issue invoice
file application or submit documents
execute tasks without governed Task Service
approve professional conclusions
bypass Permission or Policy
expose restricted pricing/payment/customer strategy
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Order API may expose:

```text
OrderCreated
MatterCreated
TaskCreated
WorkflowContractApplied
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Order events directly.
- OrderCreated must not be treated as payment, invoice issuance, filing, workflow execution or task execution.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] order_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] customer_reference_id is valid where required.
[ ] opportunity_reference_id is valid where provided.
[ ] matter_reference_id is valid where provided.
[ ] trademark_reference_id is valid where provided.
[ ] brand_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid where provided.
[ ] workflow_contract_reference_id is valid for apply operation.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] order_type is controlled.
[ ] order_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] matter_creation_mode is controlled where applicable.
[ ] apply_mode is controlled where applicable.
[ ] task_creation_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted pricing/payment/customer/order/strategy/document/evidence fields are omitted or allowed.
[ ] AI-prepared order data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] OrderCreated is emitted after createOrder succeeds.
[ ] Order preparation does not create Order automatically.
[ ] Matter creation routes through Matter Service.
[ ] Workflow Contract application routes through Workflow Contract Service.
[ ] Task creation routes through Task Service.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
OrderReferenceInvalid
CustomerReferenceInvalid
OpportunityReferenceInvalid
MatterReferenceInvalid
TrademarkReferenceInvalid
BrandReferenceInvalid
JurisdictionReferenceInvalid
WorkflowContractReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedOrderData
PaymentDataRestricted
AgentContractRequired
HumanReviewRequired
EventEmissionFailed
InternalError
```

Error response:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Error rules:

```text
- Errors must not expose restricted Order data.
- Errors must not expose pricing, payment, customer strategy, privileged notes, document content or evidence content.
- Errors must not expose unrelated Matter details.
- Errors must not expose permission or policy internals.
- Errors must be safe for product/API consumers.
```

---

# 18. Versioning Rules

API version:

```text
v0.1.0
```

Versioning rules:

```text
- Breaking changes require new version or explicit migration rule.
- order_type, order_status, source_type, link_type, matter_creation_mode, apply_mode and task_creation_mode changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI order-preparation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Order API spec
cite Order Service Specification
cite Order Object Specification
cite OrderCreated Event Specification
cite Customer/Opportunity/Matter/Trademark/Workflow Contract/Task specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid order_reference_id
write tests for invalid customer/opportunity/matter/workflow contract references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Order creation does not settle payment or issue invoice
write tests that Order preparation does not create Order automatically
write tests that Order creation does not file application or execute workflow
write tests that Matter creation routes through Matter Service
write tests that Workflow Contract application routes through Workflow Contract Service
write tests that Task creation routes through Task Service
write tests for AI Agent Contract and human review requirement
write tests for OrderCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Order Service
allow UI to emit OrderCreated directly
treat Order as Matter
treat Order as payment or invoice
treat Order as official filing
treat Order as Task execution
treat AI-prepared Order as confirmed commercial transaction
create Matter, Task or Workflow execution silently from Order operations
expose restricted pricing/payment/customer strategy for convenience
allow AI to fabricate Order references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Order API purpose.
[ ] It defines Order API meaning.
[ ] It defines Order API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, opportunity preparation, matter creation, workflow contract application, task creation and event-list operations.
[ ] It defines request contracts.
[ ] It defines response contracts.
[ ] It defines controlled values.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent access rules.
[ ] It defines Event access rules.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Order API specification. Defines governed Order commercial service-context interface and separates Order API from Matter, payment, invoice, filing, Task execution, Workflow execution, customer legal instruction and AI transaction approval. |

---


## State Boundary Reference

Order API status requests route to Order Service and consume `core-specs/controlled-state-values/order-status-values.md`; requests cannot define Order statuses or bypass Order transition validation.


## Accept Action Status Boundary

`POST /orders/{id}/accept` is a compatibility action endpoint. It returns canonical status `Confirmed` on success, never `Accepted`; denied confirmation does not create `Rejected` status. Endpoint path is unchanged and no new endpoint is added.

**End of API Specification**
