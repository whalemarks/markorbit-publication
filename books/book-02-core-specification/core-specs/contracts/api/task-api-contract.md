# API Contract — Task API

**Spec ID:** B02-CONTRACT-API-TASK  
**Spec Type:** API Contract Specification  
**Contract Name:** Task API Contract  
**Contract File:** core-specs/contracts/api/task-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/task-api.md  
**Related Domain:** Task  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/workflow-contract.md; core-specs/objects/user.md; core-specs/objects/communication.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/user-service.md; core-specs/services/communication-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/task-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/user-api.md; core-specs/api/communication-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Task API Contract defines the implementation-facing request and response contract for Task API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, assign, transition and prepare Task records through governed API boundaries without bypassing Task Service, related owning services, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Task API versioning
Task create request
Task update request
Task read response
Task search/list response
Task reference validation
Task assignment context
Task status transition context
Task completion draft context
Matter, Order and Workflow linkage
Document, Evidence and Communication linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Task API Contract does not complete professional work by itself, approve legal conclusions, send communications, submit filings, close Matters or Orders, replace Task Service, evaluate Permission/Policy, or authorize AI output as final task completion.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Task Service through governed API boundaries.
```

This contract does not mean:

```text
professional completion
legal approval
workflow execution engine
communication delivery
filing submission
matter completion
order completion
permission grant
policy approval
event emitter
UI task board
```

Core rule:

```text
Task API receives governed task requests.
Task Service owns Task behavior.
Linked Matter, Order, Workflow, User, Communication, Document and Evidence references are validated by owning services.
Permission and Policy govern access.
Task completion requires governed state transition and review where required.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Task reference fields
assignment fields
status transition fields
completion draft fields
linked object fields
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
Task lifecycle ownership outside Task Service
professional work completion by itself
external communication sending
official filing submission
matter/order closure
workflow application
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
core-specs/api/task-api.md
```

Owning service spec:

```text
core-specs/services/task-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Task API and Task Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Task
```

Related objects:

```text
Matter
Order
WorkflowContract
User
Communication
Document
Evidence
Permission
Policy
Event
Agent
```

Reference rules:

```text
- task_reference_id identifies Task.
- matter_reference_id and order_reference_id scope Task where applicable.
- workflow_contract_reference_id and workflow_application_reference_id explain origin where applicable.
- assignee_user_reference_id must be validated by User Service.
- linked communication/document/evidence references must be validated by owning services.
- Task completion does not imply Matter, Order, Communication or filing completion unless owning services confirm them.
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

Task target context:

```yaml
target:
  task_reference_id: string | null
  target_object_type: Task
  target_object_reference_id: string | null
```

Rules:

```text
- task_reference_id is required for read/update/assign/transition/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/tasks
GET    /v1/tasks/{task_reference_id}
PATCH  /v1/tasks/{task_reference_id}
GET    /v1/tasks
POST   /v1/tasks/validate-reference
POST   /v1/tasks/{task_reference_id}/assign
POST   /v1/tasks/{task_reference_id}/transition-status
POST   /v1/tasks/{task_reference_id}/prepare-completion
POST   /v1/tasks/{task_reference_id}/link-objects
```

Endpoint ownership:

```text
API layer validates request contract.
Task Service executes Task behavior.
Matter/Order/Workflow/User/Communication/Document/Evidence services validate references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted completion preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Task Request Contract

Endpoint:

```text
POST /v1/tasks
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
    - task:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - task:create:policy
  policy_decision_reference_id: string | null

payload:
  task_type: string
  task_status: string | null
  task_title_safe: string
  task_description_safe: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
  workflow_application_reference_id: string | null
  assignee_user_reference_id: string | null
  priority_level: string | null
  due_date: date | null
  linked_object_refs:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- task_type and task_title_safe are required.
- matter/order/workflow/user references must be validated where provided.
- linked object references must be validated by owning services where provided.
- Task Service assigns task_reference_id.
```

---

# 9. Create Task Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  task_reference_id: string
  task_type: string
  task_status: string
  task_title_safe: string
  matter_reference_id: string | null
  order_reference_id: string | null
  assignee_user_reference_id: string | null
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
- TaskCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate TaskCreated event.
```

---

# 10. Read Task Contract

Endpoint:

```text
GET /v1/tasks/{task_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  task_reference_id: string
  task_type: string
  task_status: string
  task_title_safe: string
  task_description_safe: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
  workflow_application_reference_id: string | null
  assignee_user_reference_id: string | null
  priority_level: string | null
  due_date: date | null
  linked_object_refs_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  completion_summary_safe: string | null
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  completed_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate task:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Linked references, descriptions and completion summaries may be omitted by policy.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Task Contract

Endpoint:

```text
PATCH /v1/tasks/{task_reference_id}
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
  task_title_safe: string | null
  task_description_safe: string | null
  priority_level: string | null
  due_date: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - task:update
policy_context:
  required_policy_scopes:
    - task:update:policy
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
  task_reference_id: string
  task_status: string
  task_title_safe: string
  priority_level: string | null
  due_date: date | null
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Task Service.
- Restricted metadata or descriptions must not be patched unless policy allows it.
- Human review may be required for responsibility-changing or professional-impacting updates.
```

---

# 12. Search/List Task Contract

Endpoint:

```text
GET /v1/tasks
```

Query parameters:

```yaml
task_type: string | null
task_status: string | null
matter_reference_id: string | null
order_reference_id: string | null
assignee_user_reference_id: string | null
workflow_contract_reference_id: string | null
priority_level: string | null
due_before: date | null
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
    - task_reference_id: string
      task_type: string
      task_status: string
      task_title_safe: string
      matter_reference_id: string | null
      order_reference_id: string | null
      assignee_user_reference_id: string | null
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
- Search must not reveal restricted Task existence.
- safe_query must not be treated as unrestricted search over private task notes.
```

---

# 13. Validate Task Reference Contract

Endpoint:

```text
POST /v1/tasks/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  task_reference_id: string
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
  task_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  task_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read or complete Task.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or task type.
```

---

# 14. Assign Task Contract

Endpoint:

```text
POST /v1/tasks/{task_reference_id}/assign
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
  assignee_user_reference_id: string | null
  assignment_reason_safe: string | null
permission_context:
  required_permission_keys:
    - task:assign
policy_context:
  required_policy_scopes:
    - task:assign:policy
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
  task_reference_id: string
  previous_assignee_user_reference_id: string | null
  current_assignee_user_reference_id: string | null
  assigned_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Assignment must route through Task Service.
- assignee_user_reference_id must be validated by User Service.
- Assignment does not imply acceptance, start or completion of work.
- Human review may be required for responsibility-sensitive assignment.
```

---

# 15. Transition Status Contract

Endpoint:

```text
POST /v1/tasks/{task_reference_id}/transition-status
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
  completion_summary_safe: string | null
permission_context:
  required_permission_keys:
    - task:status:transition
policy_context:
  required_policy_scopes:
    - task:status:transition:policy
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
  task_reference_id: string
  previous_status: string
  current_status: string
  transitioned_at: datetime
  completed_at: datetime | null
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Status transition must route through Task Service.
- Completing a Task may require human_review_reference_id.
- Completing a Task must not imply Matter, Order, Communication or filing completion unless owning services confirm them.
```

---

# 16. Prepare Completion Contract

Endpoint:

```text
POST /v1/tasks/{task_reference_id}/prepare-completion
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
    - task:completion:prepare
policy_context:
  required_policy_scopes:
    - task:completion:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  completion_purpose: string
  include_linked_context: boolean
  requested_output_scope: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  completion_preparation_status: string
  proposed_completion_summary_safe: string | null
  proposed_next_actions_safe:
    - string
  missing_context_safe:
    - string
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
- Completion preparation is assistance, not Task completion.
- AI must not mark Task complete.
- Human review may be required before completion transition.
```

---

# 17. Link Objects Contract

Endpoint:

```text
POST /v1/tasks/{task_reference_id}/link-objects
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  linked_object_refs:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - task:object:link
policy_context:
  required_policy_scopes:
    - task:object:link:policy
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
  task_reference_id: string
  linked_object_refs_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Task Service.
- Linked object references must be validated by owning services.
- Link operation does not mutate linked object lifecycle directly.
```

---

# 18. Controlled Values

## 18.1 task_type

```text
IntakeTask
ReviewTask
DocumentPreparationTask
EvidenceCollectionTask
ClassificationTask
ExternalCommunicationTask
CustomerConfirmationTask
ProviderRoutingTask
FilingPreparationTask
StatusCheckTask
InternalApprovalTask
FollowUpTask
Other
Unknown
```

## 18.2 task_status

```text
Draft
Open
Assigned
InProgress
Waiting
Blocked
UnderReview
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

## 18.4 target_object_type

```text
Matter
Order
WorkflowContract
Communication
Document
Evidence
Trademark
Brand
Customer
Opportunity
Unknown
```

## 18.5 relationship_type

```text
PrimaryContext
SupportingContext
InputObject
OutputObject
EvidenceSource
CommunicationDraft
WorkflowOrigin
HistoricalReference
Unknown
```

## 18.6 completion_preparation_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 18.7 validation_status

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

## 18.8 sort.field

```text
created_at
updated_at
due_date
task_title_safe
task_status
task_type
priority_level
assignee_user_reference_id
```

---

# 19. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] task_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] task_type is controlled.
[ ] task_status is controlled where provided.
[ ] priority_level is controlled where provided.
[ ] assignee_user_reference_id is validated where provided.
[ ] linked object references are validated where provided.
[ ] relationship_type is controlled.
[ ] link_operation is controlled.
[ ] AI Context is present for AI-assisted completion preparation.
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
task:create
task:read
task:search
task:update
task:validate
task:assign
task:status:transition
task:completion:prepare
task:object:link
```

Rules:

```text
- Task API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 21. Policy Rules

Required policy scopes may include:

```text
task:create:policy
task:read:policy
task:search:policy
task:update:policy
task:reference:policy
task:visibility:policy
task:assign:policy
task:status:transition:policy
task:completion:prepare:policy
task:object:link:policy
cross-organization:task
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact linked objects, private notes, completion summaries, assignee details or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before completion or responsibility-sensitive transitions.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 22. AI and Human Review Rules

AI rules:

```text
- AI may summarize Task context and prepare completion drafts only within Permission and Policy limits.
- AI must not create active tasks outside Task Service, assign tasks, complete tasks, approve work, send communications or close matters/orders.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Task output is used for completion, assignment, external communication, professional decision or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 23. Idempotency and Event Rules

Idempotency:

```text
POST /v1/tasks requires idempotency_key.
PATCH /v1/tasks/{task_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Assign, transition and link endpoints may require idempotency_key for duplicate-sensitive operations.
Prepare-completion endpoint does not normally require idempotency unless result is persisted.
```

Events:

```text
TaskCreated may be emitted by Task Service after successful creation.
Task update/assignment/transition events may be reserved for later if event specs exist.
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
TaskReferenceInvalid
AssigneeReferenceInvalid
LinkedObjectReferenceInvalid
RelationshipTypeInvalid
AssignmentInvalid
StatusTransitionInvalid
CompletionPreparationUnavailable
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
- Errors must not expose database IDs, restricted task data, private notes, policy internals or permission internals.
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
cite Task API Spec
cite Task Service Spec
cite this Task API Contract
use Reference Contract for task_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted completion preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive assign/transition/link operations
use Versioning Contract for version validation
route all Task mutation through Task Service
invoke User Service for assignee validation
invoke linked owning services for object reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing linked objects, assignee details, private notes or completion summaries
return safe errors only
write tests for create/read/update/search/validate-reference/assign/transition-status/prepare-completion/link-objects
write tests for assignee validation
write tests for linked object validation
write tests that prepare-completion does not complete Task
write tests for completion requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Task directly in API layer
query database directly from API contract implementation
use generic id where task_reference_id is required
expose database IDs or private task notes without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
complete Matter, Order, Communication or filing from Task API
send communication from Task API
treat AI completion preparation as completion approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 27. Acceptance Criteria

This Task API Contract is accepted only if:

```text
[ ] It defines Task API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Task API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines assign contract.
[ ] It defines transition status contract.
[ ] It defines prepare completion contract.
[ ] It defines link objects contract.
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
| 0.1.0 | Draft | Initial Task API Contract. Defines governed create, read, update, search, validate-reference, assignment, status transition, completion preparation and object-link payloads, linked reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---


## Canonical Status Contract Consumption

Task API Contract consumes `core-specs/controlled-state-values/task-status-values.md`. Requests cannot define new Task statuses, cannot bypass Task Service, cannot silently reopen through generic update, and responses/errors must preserve reason, assignment, completion, reopen and requirement context without adding endpoints or changing endpoint paths.


## Reopen Status Boundary

Task API Contract treats reopen as governed operation returning canonical `Open` and requiring Task Service validation plus status/event trace. `Reopened` is not a Task status. Endpoint paths remain unchanged.

**End of API Contract**


# PUB-TASK-B02-003 Status Transition Contract Consumption

Status mutation requests MUST consume `../status/status-transition-contract.md` and `../status/task-status-contract.md`. PATCH or generic update MUST NOT bypass transition validation. Responses distinguish validation decision from performed owner-Service result. The API does not perform mutation; it calls the owning Service. Endpoint paths are unchanged and no endpoint is added.
