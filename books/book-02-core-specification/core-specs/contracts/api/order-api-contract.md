# API Contract — Order API

**Spec ID:** B02-CONTRACT-API-ORDER  
**Spec Type:** API Contract Specification  
**Contract Name:** Order API Contract  
**Contract File:** core-specs/contracts/api/order-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/order-api.md  
**Related Domain:** Order  
**Related Object Specs:** core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related API Specs:** core-specs/api/order-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/document-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/task-api.md; core-specs/api/event-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md  
**Related Event Specs:** core-specs/events/order-created.md; core-specs/events/matter-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Order API Contract defines the implementation-facing request and response contract for Order API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and prepare Order records through governed API boundaries without bypassing Order Service, Customer Service, Matter Service, professional object services, Workflow Contract Service, Task Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Order API versioning
Order create request
Order update request
Order read response
Order search/list response
Order reference validation
Order customer and matter linkage
Order subject linkage
Order workflow preparation context
Order task preparation context
Order status transition context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Order API Contract does not approve payment, create official filings, complete professional work, select providers, apply workflows, create active tasks, replace Order Service, evaluate Permission/Policy, or authorize AI output as final business/professional action.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Order Service through governed API boundaries.
```

This contract does not mean:

```text
payment contract
invoice contract
official filing submission
provider selection
workflow execution by itself
task completion
legal representation approval
professional conclusion
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Order API receives governed order requests.
Order Service owns Order behavior.
Customer, Matter, Brand, Trademark, Document, Workflow and Task references are validated by owning services.
Permission and Policy govern access.
Order execution requires governed workflow/task/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Order reference fields
Customer/Matter/professional object linkage fields
Workflow and Task preparation fields
status transition request fields
pagination shape for list/search
permission/policy context requirements
AI and human-review context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Order lifecycle ownership outside Order Service
payment execution
invoice issuance
provider routing selection
workflow application by itself
task creation by itself
filing execution
external communication delivery
Permission evaluation logic
Policy evaluation logic
Event emission implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/order-api.md
```

Owning service spec:

```text
core-specs/services/order-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Order API and Order Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Order
```

Related objects:

```text
Customer
Matter
Brand
Trademark
Document
WorkflowContract
Task
Event
Permission
Policy
Agent
```

Reference rules:

```text
- order_reference_id identifies Order.
- customer_reference_id links Order to Customer where Order Service allows.
- matter_reference_ids link Order to Matters where Matter Service allows.
- brand/trademark/document references must be validated by owning services.
- workflow_contract_reference_id and task_reference_ids must be validated by owning services.
- Order linkage does not create, complete or approve downstream workflow/task/provider/payment actions by itself.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  idempotency_key: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Order target context:

```yaml
target:
  order_reference_id: string | null
  target_object_type: Order
  target_object_reference_id: string | null
```

Rules:

```text
- order_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/orders
GET    /v1/orders/{order_reference_id}
PATCH  /v1/orders/{order_reference_id}
GET    /v1/orders
POST   /v1/orders/validate-reference
POST   /v1/orders/{order_reference_id}/link-business-objects
POST   /v1/orders/{order_reference_id}/prepare-workflow
POST   /v1/orders/{order_reference_id}/prepare-task-plan
POST   /v1/orders/{order_reference_id}/transition-status
```

Endpoint ownership:

```text
API layer validates request contract.
Order Service executes Order behavior.
Customer/Matter/Brand/Trademark/Document services validate business object references.
Workflow Contract Service validates workflow context.
Task Service validates task context.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Order Request Contract

Endpoint:

```text
POST /v1/orders
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null

permission_context:
  required_permission_keys:
    - order:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - order:create:policy
  policy_decision_reference_id: string | null

payload:
  order_type: string
  order_status: string | null
  order_title_safe: string
  customer_reference_id: string | null
  matter_reference_ids:
    - string
  brand_reference_ids:
    - string
  trademark_reference_ids:
    - string
  document_reference_ids:
    - string
  jurisdiction_reference_id: string | null
  requested_service_scope_safe: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- order_type and order_title_safe are required.
- customer_reference_id must be validated by Customer Service where provided.
- matter_reference_ids must be validated by Matter Service where provided.
- professional object references must be validated by owning services where provided.
- Order Service assigns order_reference_id.
```

---

# 9. Create Order Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  order_type: string
  order_status: string
  order_title_safe: string
  customer_reference_id: string | null
  matter_reference_ids_visible:
    - string
  priority_level: string | null
  due_date: date | null
  created_at: datetime
  updated_at: datetime | null
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- Response must not expose database IDs.
- OrderCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate OrderCreated event.
```

---

# 10. Read Order Contract

Endpoint:

```text
GET /v1/orders/{order_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  order_type: string
  order_status: string
  order_title_safe: string
  customer_reference_id: string | null
  matter_reference_ids_visible:
    - string
  brand_reference_ids_visible:
    - string
  trademark_reference_ids_visible:
    - string
  document_reference_ids_visible:
    - string
  workflow_contract_reference_ids_visible:
    - string
  task_reference_ids_visible:
    - string
  jurisdiction_reference_id: string | null
  requested_service_scope_safe: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate order:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Linked references, service scope and metadata may be omitted where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Order Contract

Endpoint:

```text
PATCH /v1/orders/{order_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  order_status: string | null
  order_title_safe: string | null
  requested_service_scope_safe: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - order:update
policy_context:
  required_policy_scopes:
    - order:update:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  order_status: string
  order_title_safe: string
  priority_level: string | null
  due_date: date | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Order Service.
- Order status transitions must follow Order Service rules.
- Restricted metadata must not be patched unless policy allows it.
- Human review may be required for cancellation, completion or scope-changing updates.
```

---

# 12. Search/List Order Contract

Endpoint:

```text
GET /v1/orders
```

Query parameters:

```yaml
order_type: string | null
order_status: string | null
customer_reference_id: string | null
matter_reference_id: string | null
trademark_reference_id: string | null
jurisdiction_reference_id: string | null
priority_level: string | null
safe_query: string | null
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  items:
    - order_reference_id: string
      order_type: string
      order_status: string
      order_title_safe: string
      customer_reference_id: string | null
      priority_level: string | null
      due_date: date | null
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
```

Rules:

```text
- Pagination must follow Pagination Contract.
- total_count must be omitted where policy or security requires it.
- Search must not reveal restricted Order existence.
- safe_query must not be treated as unrestricted search over private order notes or commercial terms.
```

---

# 13. Validate Order Reference Contract

Endpoint:

```text
POST /v1/orders/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  order_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  order_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Order.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or order type.
```

---

# 14. Link Business Objects Contract

Endpoint:

```text
POST /v1/orders/{order_reference_id}/link-business-objects
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  business_object_links:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - order:business-object:link
policy_context:
  required_policy_scopes:
    - order:business-object:link:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  linked_business_objects_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Order Service.
- Linked target references must be validated by owning services.
- Link operation does not create or mutate linked objects.
- Human review may be required where linkage affects order scope or responsibility.
```

---

# 15. Prepare Workflow Contract

Endpoint:

```text
POST /v1/orders/{order_reference_id}/prepare-workflow
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - order:workflow:prepare
policy_context:
  required_policy_scopes:
    - order:workflow:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  workflow_purpose: string
  workflow_contract_reference_id: string | null
  requested_task_scope: string | null
  include_existing_matters: boolean
  include_existing_tasks: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  workflow_preparation_status: string
  proposed_workflow_contract_reference_id: string | null
  proposed_matter_plan_safe: object | null
  proposed_task_plan_safe: object | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Workflow preparation is assistance, not workflow application.
- Applying workflow must route through Workflow Contract Service.
- Matter creation must route through Matter Service.
- Task creation must route through Task Service.
- Human review may be required before downstream workflow application.
```

---

# 16. Prepare Task Plan Contract

Endpoint:

```text
POST /v1/orders/{order_reference_id}/prepare-task-plan
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - order:task-plan:prepare
policy_context:
  required_policy_scopes:
    - order:task-plan:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  task_plan_purpose: string
  requested_task_scope: string | null
  due_date_basis: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  task_plan_status: string
  proposed_tasks_safe:
    - task_title_safe: string
      task_type: string
      suggested_due_date: date | null
      source_reason_safe: string | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Task plan preparation is assistance, not Task creation.
- Creating active Tasks must route through Task Service.
- Human review may be required before creating tasks or assigning responsibility.
```

---

# 17. Transition Status Contract

Endpoint:

```text
POST /v1/orders/{order_reference_id}/transition-status
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  requested_status: string
  transition_reason_safe: string | null
permission_context:
  required_permission_keys:
    - order:status:transition
policy_context:
  required_policy_scopes:
    - order:status:transition:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  order_reference_id: string
  previous_status: string
  current_status: string
  transitioned_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Status transition must route through Order Service.
- Protected transitions may require human_review_reference_id.
- Completing an Order must not imply Task completion, Matter completion, provider payment, invoice issuance or official filing completion unless owning services confirm them.
```

---

# 18. Controlled Values

## 18.1 order_type

```text
TrademarkApplicationOrder
TrademarkSearchOrder
OfficeActionResponseOrder
RenewalOrder
AssignmentOrder
ChangeRecordalOrder
OppositionOrder
CancellationOrder
ConsultationOrder
InternalOrder
Other
Unknown
```

## 18.2 order_status

```text
Draft
Submitted
Accepted
InProgress
WaitingForCustomer
WaitingForAgent
WaitingForPayment
UnderReview
Blocked
Completed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 18.3 priority_level

```text
Low
Normal
High
Urgent
Unknown
```

## 18.4 relationship_type

```text
PrimarySubject
SupportingSubject
RelatedObject
SourceObject
OutputObject
BillingReference
HistoricalReference
Unknown
```

## 18.5 target_object_type

```text
Customer
Matter
Brand
Trademark
Document
WorkflowContract
Task
Unknown
```

## 18.6 workflow_preparation_status

```text
Completed
Partial
NoApplicableWorkflow
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 18.7 task_plan_status

```text
Completed
Partial
NoTaskSuggested
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 18.8 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 18.9 sort.field

```text
created_at
updated_at
due_date
order_title_safe
order_status
order_type
priority_level
```

---

# 19. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] order_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] order_type is controlled.
[ ] order_status is controlled where provided.
[ ] priority_level is controlled where provided.
[ ] customer/matter/professional object references are validated where provided.
[ ] workflow/task references are validated where provided.
[ ] relationship_type is controlled.
[ ] link_operation is controlled.
[ ] AI Context is present for AI-assisted workflow/task preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 20. Permission Rules

Required permission keys:

```text
order:create
order:read
order:search
order:update
order:validate
order:business-object:link
order:workflow:prepare
order:task-plan:prepare
order:status:transition
```

Rules:

```text
- Order API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 21. Policy Rules

Required policy scopes may include:

```text
order:create:policy
order:read:policy
order:search:policy
order:update:policy
order:reference:policy
order:visibility:policy
order:business-object:link:policy
order:workflow:prepare:policy
order:task-plan:prepare:policy
order:status:transition:policy
order:commercial-terms:visibility:policy
cross-organization:order
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact linked objects, task/workflow context, commercial terms, private notes, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before transitions, workflow application or task creation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 22. AI and Human Review Rules

AI rules:

```text
- AI may summarize Order context and prepare workflow/task plans only within Permission and Policy limits.
- AI must not apply workflows, create active tasks, close orders, approve payments, select providers, approve filings or decide professional completion.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Order output is used for workflow application, task creation, status transition, provider routing, external communication, payment-impacting action or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 23. Idempotency and Event Rules

Idempotency:

```text
POST /v1/orders requires idempotency_key.
PATCH /v1/orders/{order_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link and transition endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
OrderCreated may be emitted by Order Service after successful creation.
MatterCreated, WorkflowContractApplied and TaskCreated may only be emitted by their owning services, not this API.
Order update/transition events may be reserved for later if event specs exist.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 24. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
OrderReferenceInvalid
CustomerReferenceInvalid
MatterReferenceInvalid
BusinessObjectReferenceInvalid
WorkflowReferenceInvalid
TaskReferenceInvalid
RelationshipTypeInvalid
WorkflowPreparationUnavailable
TaskPlanUnavailable
StatusTransitionInvalid
HumanReviewRequired
StateInvalid
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose database IDs, restricted order data, commercial terms, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 25. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 26. Codex Implementation Notes

Codex must:

```text
cite Order API Spec
cite Order Service Spec
cite this Order API Contract
use Reference Contract for order_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted workflow/task preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link/transition operations
use Versioning Contract for version validation
route all Order mutation through Order Service
invoke Customer/Matter/Brand/Trademark/Document/Workflow/Task services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing linked objects, workflow/task context, commercial terms or private order details
return safe errors only
write tests for create/read/update/search/validate-reference/link-business-objects/prepare-workflow/prepare-task-plan/transition-status
write tests for linked reference validation
write tests that workflow preparation does not apply workflow
write tests that task plan preparation does not create tasks
write tests for protected status transition requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Order directly in API layer
query database directly from API contract implementation
use generic id where order_reference_id is required
expose database IDs, commercial terms or private order notes without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
create Matter, Task or Workflow application from Order API preparation endpoints
select providers or approve payments from this API contract
complete Order as a proxy for Task/Matter/filing/payment completion
treat AI workflow/task preparation as execution approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 27. Acceptance Criteria

This Order API Contract is accepted only if:

```text
[ ] It defines Order API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Order API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link business objects contract.
[ ] It defines prepare workflow contract.
[ ] It defines prepare task plan contract.
[ ] It defines transition status contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Order API Contract. Defines governed create, read, update, search, validate-reference, business-object-link, workflow preparation, task-plan preparation and status transition payloads, linked reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---


## Canonical Status Contract Consumption

Order API Contract consumes `core-specs/controlled-state-values/order-status-values.md`. Requests cannot define new Order statuses, cannot bypass Order Service, cannot use PATCH or generic update to bypass invalid transitions, and responses/errors must preserve actor, reason, permission, policy and review requirement context without adding endpoints or changing endpoint paths.


## Accept Action Status Boundary

`POST /orders/{id}/accept` calls Order Service compatibility action semantics. Success returns canonical `Confirmed`; denial returns reason/requirement context and does not create `Rejected` status. Endpoint path remains unchanged and no endpoint is added.

**End of API Contract**
