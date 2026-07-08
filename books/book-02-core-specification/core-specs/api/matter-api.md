# API Specification — Matter API

**Spec ID:** B02-API-MATTER  
**Spec Type:** API Specification  
**API Name:** Matter API  
**API File:** core-specs/api/matter-api.md  
**Related Domain:** core-specs/domains/matter.md  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/matter-service.md; core-specs/services/customer-service.md; core-specs/services/order-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/matter-created.md; core-specs/events/order-created.md; core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/matter-api-contract.md; core-specs/contracts/events/matter-created-payload.md  
**Related Agent Specs:** core-specs/agents/matter-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Matter API exposes governed Matter operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and prepare Matter references without treating Matter as Order, payment, legal filing, official application, task execution, workflow execution, customer instruction approval, professional decision or AI case judgment.

Matter API exists to support:

```text
professional case context creation
customer-to-service case organization
trademark/brand/jurisdiction/classification context binding
document and evidence preparation context
workflow contract application preparation
task planning context
order execution context separation
policy-controlled matter visibility
AI-assisted matter intake and review under governance
event trace access
API-safe matter reference validation
```

Matter API does not create payment obligations, file applications, execute workflow, assign tasks automatically or replace professional review.

---

# 2. API Meaning

Matter API means:

```text
a governed interface for operating professional case context through Matter Service.
```

Matter API does not mean:

```text
Order API
Task API
Workflow execution API
filing API
payment API
official registry API
Customer instruction approval API
professional legal conclusion API
AI case decision API
```

Matter organizes professional case context.

Order owns commercial/execution order context.

Workflow Contract defines executable workflow structure.

Task owns actionable work items.

---

# 3. API Boundary

Matter API is responsible for:

```text
Matter create request intake
Matter read/search/list access
Matter update request intake
Matter reference validation
Matter context preparation
Matter link request intake where explicitly governed
safe Matter response shaping
Permission/Policy enforcement for Matter operations
Matter-related Event reference exposure where allowed
AI Agent access boundary for Matter operations
controlled API errors
```

Matter API is not responsible for:

```text
Order lifecycle ownership
payment or invoice ownership
Task execution
Workflow Contract definition
official filing execution
professional legal conclusion
customer instruction approval
service provider routing
communication delivery
AI final case judgment
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/matter.md
```

Domain rule:

```text
Matter represents professional case context.
Matter is not Order, payment, Task, workflow execution, filing or professional conclusion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/matter.md
core-specs/objects/customer.md
core-specs/objects/order.md
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
- Matter API returns matter_reference_id.
- Matter API may reference Customer, Order, Trademark, Brand, Jurisdiction, Classification, Document, Evidence, Workflow Contract or Task context but must not create them silently unless explicitly defined by a governed operation.
- Matter API must not treat Matter as paid Order.
- Matter API must not treat Matter as official filing or official status.
- Matter API must not expose restricted customer strategy, document/evidence content or internal work notes by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/matter-service.md
core-specs/services/customer-service.md
core-specs/services/order-service.md
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
- Matter API must invoke Matter Service for Matter behavior.
- Matter API must validate related references through their owning services where required.
- Matter API must invoke Permission Service where operation requires authorization.
- Matter API must invoke Policy Service where contextual constraints apply.
- Matter API must not emit Matter events directly; Matter Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/matter-created.md
core-specs/events/order-created.md
core-specs/events/task-created.md
core-specs/events/workflow-contract-applied.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createMatter may result in MatterCreated.
- applying Workflow Contract must use Workflow Contract Service and may result in WorkflowContractApplied.
- creating Tasks must use Task Service and may result in TaskCreated.
- creating Orders must use Order Service and may result in OrderCreated.
- API consumers must not fabricate MatterCreated.
- MatterCreated is professional case context trace, not Order, payment, filing or workflow execution.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Matter

**Operation Category:** Create  
**Method:** POST  
**Path:** `/matters`  
**Owning Service Operation:** `createMatter`  
**Permission Required:** `matter:create`  
**Policy Required:** `MatterCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-prepared  
**Event Behavior:** Service Must Emit MatterCreated

Meaning:

```text
Create a governed Matter professional case context.
```

Non-meaning:

```text
does not create Order
does not create payment obligation
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
Matter Service createMatter
  ↓
Event Service record MatterCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Matter

**Operation Category:** Read  
**Method:** GET  
**Path:** `/matters/{matter_reference_id}`  
**Owning Service Operation:** `getMatter`  
**Permission Required:** `matter:read`  
**Policy Required:** `MatterVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Matter view.
```

Non-meaning:

```text
does not expose restricted customer strategy automatically
does not expose internal work notes automatically
does not expose document/evidence raw content automatically
does not assert official filing status automatically
```

## 8.3 Operation: Search Matters

**Operation Category:** Search  
**Method:** GET  
**Path:** `/matters`  
**Owning Service Operation:** `searchMatters`  
**Permission Required:** `matter:search`  
**Policy Required:** `MatterVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Matter references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted case database access
does not expose restricted customer, strategy, document or evidence data by default
```

## 8.4 Operation: Update Matter

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/matters/{matter_reference_id}`  
**Owning Service Operation:** `updateMatter`  
**Permission Required:** `matter:update`  
**Policy Required:** `MatterUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit MatterUpdated where event is defined

Meaning:

```text
Update governed Matter metadata, status or context under Matter Service rules.
```

Non-meaning:

```text
does not update Order payment status automatically
does not update official filing status automatically
does not execute workflow or tasks automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Matter Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/matters/reference/validate`  
**Owning Service Operation:** `validateMatterReference`  
**Permission Required:** `matter:validate`  
**Policy Required:** `MatterReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Matter reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize filing
does not prove payment
does not approve task execution
does not prove customer instruction
```

## 8.6 Operation: Link Matter to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/matters/{matter_reference_id}/links`  
**Owning Service Operation:** `linkMatterToObject`  
**Permission Required:** `matter:link`  
**Policy Required:** `MatterLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit MatterUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Matter and a target Core object.
```

Non-meaning:

```text
does not create target object
does not execute order
does not file or submit anything
does not approve professional decision
```

## 8.7 Operation: Prepare Matter from Customer Intake

**Operation Category:** Action  
**Method:** POST  
**Path:** `/matters/prepare-from-customer-intake`  
**Owning Service Operation:** `prepareMatterFromCustomerIntake`  
**Permission Required:** `matter:intake:prepare`  
**Policy Required:** `MatterIntakePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit MatterCreated unless createMatter succeeds separately

Meaning:

```text
Prepare a governed Matter draft context from Customer intake context.
```

Non-meaning:

```text
does not create Matter automatically
does not create Order
does not approve customer instruction
does not execute workflow
```

## 8.8 Operation: Apply Workflow Contract to Matter

**Operation Category:** Action  
**Method:** POST  
**Path:** `/matters/{matter_reference_id}/workflow-contracts/{workflow_contract_reference_id}/apply`  
**Owning Service Operation:** `applyWorkflowContractToMatter`  
**Permission Required:** `matter:workflow-contract:apply`  
**Policy Required:** `MatterWorkflowContractPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Must route through Workflow Contract Service; may emit WorkflowContractApplied

Meaning:

```text
Apply a governed Workflow Contract to a Matter context.
```

Non-meaning:

```text
does not execute all tasks automatically
does not approve legal work product
does not bypass workflow policy
does not create Order or payment obligation
```

## 8.9 Operation: Create Tasks from Matter Plan

**Operation Category:** Action  
**Method:** POST  
**Path:** `/matters/{matter_reference_id}/tasks/create-from-plan`  
**Owning Service Operation:** `createTasksFromMatterPlan`  
**Permission Required:** `matter:tasks:create`  
**Policy Required:** `MatterTaskCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated plan  
**Event Behavior:** Must route through Task Service; may emit TaskCreated

Meaning:

```text
Create governed Tasks from an approved Matter plan.
```

Non-meaning:

```text
does not execute Tasks automatically
does not approve professional work
does not bypass assignee/permission rules
```

## 8.10 Operation: List Matter Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/matters/{matter_reference_id}/events`  
**Owning Service Operation:** `listMatterEvents`  
**Permission Required:** `matter:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Matter-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Matter Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  matter_type: string
  matter_status: string | optional
  customer_reference_id: string
  order_reference_id: string | null
  trademark_reference_id: string | null
  brand_reference_id: string | null
  jurisdiction_reference_id: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_prepared: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Matter Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  matter_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  matter_status: string | optional
  matter_type: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Matter Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  matter_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Matter to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  matter_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Prepare Matter from Customer Intake Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  customer_reference_id: string
  intake_context_reference_id: string | null
  intended_service_type: string
  target_context:
    brand_reference_id: string | null
    trademark_reference_id: string | null
    jurisdiction_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Apply Workflow Contract to Matter Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  matter_reference_id: string
  workflow_contract_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  apply_mode: string
  request_context: object
```

## 9.7 Create Tasks from Matter Plan Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  matter_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  matter_plan_reference_id: string | null
  task_creation_mode: string
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted customer strategy, privileged notes, payment data, raw document content or evidence content by default.
- Requests must use controlled matter_type, matter_status, source_type, link_type, apply_mode and task_creation_mode values.
- AI-prepared matter context must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Matter Response

```yaml
status: 200
body:
  matter_reference_id: string
  matter_type: string
  matter_status: string
  customer_reference_id: string
  order_reference_id: string | null
  trademark_reference_id: string | null
  brand_reference_id: string | null
  jurisdiction_reference_id: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    context_summary: string | null
  linked_object_references:
    - target_object_type: string
      target_object_reference_id: string
      link_type: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Matter Response

```yaml
status: 201
body:
  matter_reference_id: string
  matter_status: string
  review_required: boolean
  related_event_reference_ids:
    - matter_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Matter Reference Validation Response

```yaml
status: 200
body:
  matter_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Matter Preparation Response

```yaml
status: 200
body:
  matter_draft_reference_id: string | null
  usable_for_matter_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Workflow Contract Application Response

```yaml
status: 200
body:
  matter_reference_id: string
  workflow_contract_reference_id: string
  workflow_contract_applied_reference_id: string | null
  application_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Order creation, payment, official filing, task execution or professional conclusion.
- Responses must not expose restricted customer, strategy, document or evidence fields by default.
- Responses must distinguish Matter references from Order, Task and Workflow Contract references.
- Responses must identify review requirements for AI-prepared or AI-suggested content.
```

---

# 11. Controlled Values

## 11.1 matter_type

```text
TrademarkSearchMatter
TrademarkFilingMatter
RenewalMatter
OfficeActionMatter
OppositionMatter
CancellationMatter
RecordalMatter
PortfolioMatter
ConsultationMatter
InternalMatter
Unknown
```

## 11.2 matter_status

```text
Draft
Active
ReviewRequired
Prepared
InProgress
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
OrderDerived
CommunicationDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.4 link_type

```text
PrimaryMatterObject
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

## 11.6 apply_mode

```text
Preview
ApplyWithoutTaskCreation
ApplyAndPrepareTasks
ApplyAndCreateTasks
Unknown
```

## 11.7 task_creation_mode

```text
Preview
CreateDraftTasks
CreateActiveTasks
Unknown
```

## 11.8 application_status

```text
Previewed
Applied
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.9 validation_status

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

## 11.10 intended_use

```text
OrderPreparation
TaskPreparation
WorkflowContractApplication
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
matter:create
matter:read
matter:search
matter:update
matter:validate
matter:link
matter:intake:prepare
matter:workflow-contract:apply
matter:tasks:create
matter:event:read
```

Rules:

```text
- Matter read/search must be permission-controlled.
- Matter creation must not imply Order creation, payment, filing or task execution.
- Matter validation must not authorize filing, payment or task execution.
- Matter-to-object linking requires separate permission.
- Workflow Contract application and task creation require separate permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
MatterCreationPolicy
MatterUpdatePolicy
MatterVisibilityPolicy
MatterReferencePolicy
MatterLinkPolicy
MatterIntakePolicy
MatterWorkflowContractPolicy
MatterTaskCreationPolicy
EventVisibilityPolicy
AIAgentMatterAccessPolicy
RestrictedMatterDataPolicy
CrossOrganizationMatterPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Matter fields.
- Policy may require human review for AI-prepared Matter data.
- Policy may restrict cross-organization Matter lookup.
- Policy may restrict customer strategy, internal notes, document/evidence details and privileged work product.
- Policy may restrict Workflow Contract application and Task creation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Matter: Restricted / HumanReviewRequired where AI-prepared
Get Matter: Restricted
Search Matters: Restricted
Update Matter: Restricted / HumanReviewRequired where sensitive
Validate Matter Reference: Allowed under contract
Link Matter to Object: Restricted / HumanReviewRequired where AI-suggested
Prepare Matter from Customer Intake: Restricted / HumanReviewRequired
Apply Workflow Contract to Matter: Restricted / HumanReviewRequired where AI-suggested
Create Tasks from Matter Plan: Restricted / HumanReviewRequired where AI-generated plan
List Matter Events: Restricted
```

AI Agents may:

```text
summarize safe Matter metadata
flag missing intake or context items
validate Matter references for authorized actions
suggest Matter-to-object links for human review
prepare Matter draft context for human review
suggest workflow contract application for human review
prepare task plan draft for human review
```

AI Agents must not:

```text
fabricate Matter
fabricate MatterCreated events
treat AI-prepared Matter as confirmed professional case
create Order or payment obligation silently
file application or submit documents
execute tasks without governed Task Service
approve professional conclusions
bypass Permission or Policy
expose restricted customer/matter strategy
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

Matter API may expose:

```text
MatterCreated
OrderCreated
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
- API clients must not create Matter events directly.
- MatterCreated must not be treated as Order creation, payment, filing, workflow execution or task execution.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] matter_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] customer_reference_id is valid where required.
[ ] order_reference_id is valid where provided.
[ ] trademark_reference_id is valid where provided.
[ ] brand_reference_id is valid where provided.
[ ] jurisdiction_reference_id is valid where provided.
[ ] workflow_contract_reference_id is valid for apply operation.
[ ] target_object_type and target_object_reference_id are valid for link operation.
[ ] matter_type is controlled.
[ ] matter_status is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] apply_mode is controlled where applicable.
[ ] task_creation_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted customer/matter/strategy/document/evidence fields are omitted or allowed.
[ ] AI-prepared matter data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] MatterCreated is emitted after createMatter succeeds.
[ ] Matter preparation does not create Matter automatically.
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
MatterReferenceInvalid
CustomerReferenceInvalid
OrderReferenceInvalid
TrademarkReferenceInvalid
BrandReferenceInvalid
JurisdictionReferenceInvalid
WorkflowContractReferenceInvalid
TargetObjectReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedMatterData
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
- Errors must not expose restricted Matter data.
- Errors must not expose customer strategy, privileged notes, document content or evidence content.
- Errors must not expose payment data or unrelated Order details.
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
- matter_type, matter_status, source_type, link_type, apply_mode and task_creation_mode changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI matter-preparation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Matter API spec
cite Matter Service Specification
cite Matter Object Specification
cite MatterCreated Event Specification
cite Customer/Order/Trademark/Workflow Contract/Task specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid matter_reference_id
write tests for invalid customer/order/trademark/workflow contract references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Matter creation does not create Order or payment obligation
write tests that Matter preparation does not create Matter automatically
write tests that Matter creation does not file application or execute workflow
write tests that Workflow Contract application routes through Workflow Contract Service
write tests that Task creation routes through Task Service
write tests for AI Agent Contract and human review requirement
write tests for MatterCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Matter Service
allow UI to emit MatterCreated directly
treat Matter as Order or payment
treat Matter as official filing
treat Matter as Task execution
treat AI-prepared Matter as confirmed professional case
create Order, Task or Workflow execution silently from Matter operations
expose restricted customer/matter strategy for convenience
allow AI to fabricate Matter references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Matter API purpose.
[ ] It defines Matter API meaning.
[ ] It defines Matter API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, intake preparation, workflow contract application, task creation and event-list operations.
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
| 0.1.0 | Draft | Initial Matter API specification. Defines governed Matter professional case-context interface and separates Matter API from Order, payment, filing, Task execution, Workflow execution, customer instruction approval and AI case judgment. |

---

**End of API Specification**
