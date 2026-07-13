# API Contract — Matter API

**Spec ID:** B02-CONTRACT-API-MATTER  
**Spec Type:** API Contract Specification  
**Contract Name:** Matter API Contract  
**Contract File:** core-specs/contracts/api/matter-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/matter-api.md  
**Related Domain:** Matter  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/workflow-contract.md; core-specs/objects/task.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/matter-service.md; core-specs/services/customer-service.md; core-specs/services/order-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/matter-api.md; core-specs/api/customer-api.md; core-specs/api/order-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/task-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/matter-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Matter API Contract defines the implementation-facing request and response contract for Matter API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and prepare Matter records through governed API boundaries without bypassing Matter Service, Customer Service, Order Service, professional object services, Workflow Contract Service, Task Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Matter API versioning
Matter create request
Matter update request
Matter read response
Matter search/list response
Matter reference validation
Matter business/professional object linkage
Matter workflow preparation context
Matter task preparation context
Matter status transition context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Matter API Contract does not create orders by itself, approve engagement, submit filings, complete professional work, replace Matter Service, evaluate Permission/Policy, or authorize AI output as final professional action.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Matter Service through governed API boundaries.
```

This contract does not mean:

```text
order contract
workflow execution by itself
task completion
filing submission
legal representation approval
professional conclusion
billing approval
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Matter API receives governed matter requests.
Matter Service owns Matter behavior.
Customer, Order, Brand, Trademark, Document, Evidence, Workflow and Task references are validated by owning services.
Permission and Policy govern access.
Matter execution requires governed workflow/task/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Matter reference fields
Customer/Order/professional object linkage fields
Workflow and Task relationship fields
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
Matter lifecycle ownership outside Matter Service
order creation
workflow application by itself
task creation by itself
filing execution
external communication delivery
professional approval
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
core-specs/api/matter-api.md
```

Owning service spec:

```text
core-specs/services/matter-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Matter API and Matter Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Matter
```

Related objects:

```text
Customer
Order
Brand
Trademark
Document
Evidence
WorkflowContract
Task
Permission
Policy
Event
Agent
```

Reference rules:

```text
- matter_reference_id identifies Matter.
- customer_reference_id links Matter to Customer where Matter Service allows.
- order_reference_id links Matter to Order where Order Service allows.
- brand/trademark/document/evidence references must be validated by owning services.
- workflow_contract_reference_id and task_reference_ids must be validated by Workflow Contract Service and Task Service.
- Matter linkage does not create, complete or approve downstream workflow/task actions by itself.
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

Matter target context:

```yaml
target:
  matter_reference_id: string | null
  target_object_type: Matter
  target_object_reference_id: string | null
```

Rules:

```text
- matter_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/matters
GET    /v1/matters/{matter_reference_id}
PATCH  /v1/matters/{matter_reference_id}
GET    /v1/matters
POST   /v1/matters/validate-reference
POST   /v1/matters/{matter_reference_id}/link-business-objects
POST   /v1/matters/{matter_reference_id}/prepare-workflow
POST   /v1/matters/{matter_reference_id}/prepare-task-plan
POST   /v1/matters/{matter_reference_id}/transition-status
```

Endpoint ownership:

```text
API layer validates request contract.
Matter Service executes Matter behavior.
Customer/Order/Brand/Trademark/Document/Evidence services validate business object references.
Workflow Contract Service validates workflow context.
Task Service validates task context.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Matter Request Contract

Endpoint:

```text
POST /v1/matters
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
    - matter:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - matter:create:policy
  policy_decision_reference_id: string | null

payload:
  matter_type: string
  matter_status: string | null
  matter_title_safe: string
  customer_reference_id: string | null
  order_reference_id: string | null
  brand_reference_ids:
    - string
  trademark_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  jurisdiction_reference_id: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- matter_type and matter_title_safe are required.
- customer_reference_id must be validated by Customer Service where provided.
- order_reference_id must be validated by Order Service where provided.
- professional object references must be validated by owning services where provided.
- Matter Service assigns matter_reference_id.
```

---

# 9. Create Matter Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  matter_reference_id: string
  matter_type: string
  matter_status: string
  matter_title_safe: string
  customer_reference_id: string | null
  order_reference_id: string | null
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
- MatterCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate MatterCreated event.
```

---

# 10. Read Matter Contract

Endpoint:

```text
GET /v1/matters/{matter_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  matter_reference_id: string
  matter_type: string
  matter_status: string
  matter_title_safe: string
  customer_reference_id: string | null
  order_reference_id: string | null
  brand_reference_ids_visible:
    - string
  trademark_reference_ids_visible:
    - string
  document_reference_ids_visible:
    - string
  evidence_reference_ids_visible:
    - string
  workflow_contract_reference_ids_visible:
    - string
  task_reference_ids_visible:
    - string
  jurisdiction_reference_id: string | null
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
- Read must evaluate matter:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Linked references may be omitted where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Matter Contract

Endpoint:

```text
PATCH /v1/matters/{matter_reference_id}
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
  matter_status: string | null
  matter_title_safe: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - matter:update
policy_context:
  required_policy_scopes:
    - matter:update:policy
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
  matter_reference_id: string
  matter_status: string
  matter_title_safe: string
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
- Update must route through Matter Service.
- Matter status transitions must follow Matter Service rules.
- Restricted metadata must not be patched unless policy allows it.
- Human review may be required for closure, cancellation or responsibility-changing updates.
```

---

# 12. Search/List Matter Contract

Endpoint:

```text
GET /v1/matters
```

Query parameters:

```yaml
matter_type: string | null
matter_status: string | null
customer_reference_id: string | null
order_reference_id: string | null
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
    - matter_reference_id: string
      matter_type: string
      matter_status: string
      matter_title_safe: string
      customer_reference_id: string | null
      order_reference_id: string | null
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
- Search must not reveal restricted Matter existence.
- safe_query must not be treated as unrestricted search over private notes.
```

---

# 13. Validate Matter Reference Contract

Endpoint:

```text
POST /v1/matters/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  matter_reference_id: string
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
  matter_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  matter_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Matter.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or matter type.
```

---

# 14. Link Business Objects Contract

Endpoint:

```text
POST /v1/matters/{matter_reference_id}/link-business-objects
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
    - matter:business-object:link
policy_context:
  required_policy_scopes:
    - matter:business-object:link:policy
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
  matter_reference_id: string
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
- Link operation must route through Matter Service.
- Linked target references must be validated by owning services.
- Link operation does not create or mutate linked objects.
- Human review may be required where linkage affects responsibility or professional scope.
```

---

# 15. Prepare Workflow Contract

Endpoint:

```text
POST /v1/matters/{matter_reference_id}/prepare-workflow
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
    - matter:workflow:prepare
policy_context:
  required_policy_scopes:
    - matter:workflow:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  workflow_purpose: string
  workflow_contract_reference_id: string | null
  requested_task_scope: string | null
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
- Task creation must route through Task Service.
- Human review may be required before downstream workflow application.
```

---

# 16. Prepare Task Plan Contract

Endpoint:

```text
POST /v1/matters/{matter_reference_id}/prepare-task-plan
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
    - matter:task-plan:prepare
policy_context:
  required_policy_scopes:
    - matter:task-plan:prepare:policy
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
POST /v1/matters/{matter_reference_id}/transition-status
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
    - matter:status:transition
policy_context:
  required_policy_scopes:
    - matter:status:transition:policy
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
  matter_reference_id: string
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
- Status transition must route through Matter Service.
- Protected transitions may require human_review_reference_id.
- Closing a Matter must not imply Task completion, Order completion or official filing completion unless owning services confirm them.
```

---

# 18. Controlled Values

## 18.1 matter_type

```text
TrademarkApplication
TrademarkSearch
OfficeActionResponse
Renewal
Assignment
ChangeRecordal
Opposition
Cancellation
EvidenceReview
CustomerConsultation
InternalMatter
Other
Unknown
```

## 18.2 matter_status

```text
Draft
Open
InProgress
WaitingForCustomer
WaitingForAgent
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
HistoricalReference
Unknown
```

## 18.5 target_object_type

```text
Customer
Order
Brand
Trademark
Document
Evidence
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
matter_title_safe
matter_status
matter_type
priority_level
```

---

# 19. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] matter_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] matter_type is controlled.
[ ] matter_status is controlled where provided.
[ ] priority_level is controlled where provided.
[ ] customer/order/professional object references are validated where provided.
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
matter:create
matter:read
matter:search
matter:update
matter:validate
matter:business-object:link
matter:workflow:prepare
matter:task-plan:prepare
matter:status:transition
```

Rules:

```text
- Matter API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 21. Policy Rules

Required policy scopes may include:

```text
matter:create:policy
matter:read:policy
matter:search:policy
matter:update:policy
matter:reference:policy
matter:visibility:policy
matter:business-object:link:policy
matter:workflow:prepare:policy
matter:task-plan:prepare:policy
matter:status:transition:policy
cross-organization:matter
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact linked objects, task/workflow context, private notes, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before transitions, workflow application or task creation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 22. AI and Human Review Rules

AI rules:

```text
- AI may summarize Matter context and prepare workflow/task plans only within Permission and Policy limits.
- AI must not apply workflows, create active tasks, close matters, approve filings or decide professional completion.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Matter output is used for workflow application, task creation, status transition, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 23. Idempotency and Event Rules

Idempotency:

```text
POST /v1/matters requires idempotency_key.
PATCH /v1/matters/{matter_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link and transition endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
MatterCreated may be emitted by Matter Service after successful creation.
WorkflowContractApplied and TaskCreated may only be emitted by their owning services, not this API.
Matter update/transition events may be reserved for later if event specs exist.
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
MatterReferenceInvalid
CustomerReferenceInvalid
OrderReferenceInvalid
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
- Errors must not expose database IDs, restricted matter data, private notes, policy internals or permission internals.
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
cite Matter API Spec
cite Matter Service Spec
cite this Matter API Contract
use Reference Contract for matter_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted workflow/task preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link/transition operations
use Versioning Contract for version validation
route all Matter mutation through Matter Service
invoke Customer/Order/Brand/Trademark/Document/Evidence/Workflow/Task services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing linked objects, workflow/task context or private matter details
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
create Matter directly in API layer
query database directly from API contract implementation
use generic id where matter_reference_id is required
expose database IDs or private matter notes
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
create Order, Task or Workflow application from Matter API preparation endpoints
complete Matter as a proxy for Task/Order/filing completion
treat AI workflow/task preparation as execution approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 27. Acceptance Criteria

This Matter API Contract is accepted only if:

```text
[ ] It defines Matter API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Matter API and Service specs.
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
| 0.1.0 | Draft | Initial Matter API Contract. Defines governed create, read, update, search, validate-reference, business-object-link, workflow preparation, task-plan preparation and status transition payloads, linked reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---


## Canonical Status Contract Consumption

Matter API Contract consumes `core-specs/controlled-state-values/matter-status-values.md`. Requests cannot define new Matter statuses, cannot bypass Matter Service or linked Workflow Contract validation, cannot use PATCH or generic update to bypass invalid transitions, and responses/errors must preserve reason, blocker/review and requirement context without changing endpoint paths.


## Suspended Status Boundary

Matter API Contract does not define `Suspended` as canonical status. Legacy suspension semantics require governed migration or Human Review before any canonical status transition. Endpoint paths remain unchanged.

## Status Transition Contract Consumption

Related Contracts: [Matter Status Contract](../status/matter-status-contract.md) and [Status Transition Contract](../status/status-transition-contract.md).

Status Transition request validation consumes the shared `status_transition_request` shape. API validation responses consume `status_transition_decision`. Owner Service execution is required before a performed `status_transition_result` can exist. Generic PATCH or update semantics must not bypass the status contract, endpoint paths do not change, no endpoint is added, API does not directly mutate status, and responses must not return legacy statuses that conflict with the canonical status list.

**End of API Contract**
