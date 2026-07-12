# API Contract — Workflow Contract API

**Spec ID:** B02-CONTRACT-API-WORKFLOW-CONTRACT  
**Spec Type:** API Contract Specification  
**Contract Name:** Workflow Contract API Contract  
**Contract File:** core-specs/contracts/api/workflow-contract-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/workflow-contract-api.md  
**Related Domain:** Workflow Contract  
**Related Object Specs:** core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md  
**Related API Specs:** core-specs/api/workflow-contract-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/task-api.md; core-specs/api/event-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/agent-api.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Workflow Contract API Contract defines the implementation-facing request and response contract for Workflow Contract API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, preview and apply Workflow Contracts through governed API boundaries without bypassing Workflow Contract Service, Task Service, Permission Service, Policy Service, Agent governance or Event Service.

This contract governs:

```text
Workflow Contract API versioning
Workflow Contract create request
Workflow Contract update request
Workflow Contract read response
Workflow Contract search/list response
Workflow Contract reference validation
Workflow preview request/response
Workflow application request/response
Task creation plan context
Matter and Order target context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Workflow Contract API Contract does not execute business workflow by itself, create active Tasks without Task Service, complete Tasks, close Matters or Orders, send communications, or authorize AI output as execution approval.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Workflow Contract Service through governed API boundaries.
```

This contract does not mean:

```text
workflow engine by itself
task execution
task completion
matter completion
order completion
communication delivery
professional approval
permission grant
policy approval
event emitter
UI workflow designer
```

Core rule:

```text
Workflow Contract API receives governed workflow requests.
Workflow Contract Service owns Workflow Contract behavior.
Task Service owns active Task creation.
Permission and Policy govern access.
Workflow application requires explicit governed execution and trace.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Workflow Contract reference fields
workflow template and step fields
preview result fields
application result fields
task plan fields
target object context fields
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
workflow execution engine internals
active task execution
task completion
business object lifecycle completion
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
core-specs/api/workflow-contract-api.md
```

Owning service spec:

```text
core-specs/services/workflow-contract-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Workflow Contract API and Workflow Contract Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
WorkflowContract
```

Related objects:

```text
Matter
Order
Task
Event
Permission
Policy
Agent
```

Reference rules:

```text
- workflow_contract_reference_id identifies Workflow Contract.
- target_object_type and target_object_reference_id identify the object to which workflow may be applied.
- matter_reference_id and order_reference_id must be validated by owning services where used.
- task_reference_ids identify active tasks only after Task Service creates them.
- Workflow preview does not create Tasks.
- Workflow application does not complete Tasks.
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

Workflow target context:

```yaml
target:
  workflow_contract_reference_id: string | null
  target_object_type: WorkflowContract
  target_object_reference_id: string | null
```

Rules:

```text
- workflow_contract_reference_id is required for read/update/apply/validate-by-reference operations.
- idempotency_key is required for create and apply operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- target object references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/workflow-contracts
GET    /v1/workflow-contracts/{workflow_contract_reference_id}
PATCH  /v1/workflow-contracts/{workflow_contract_reference_id}
GET    /v1/workflow-contracts
POST   /v1/workflow-contracts/validate-reference
POST   /v1/workflow-contracts/{workflow_contract_reference_id}/preview
POST   /v1/workflow-contracts/{workflow_contract_reference_id}/apply
POST   /v1/workflow-contracts/{workflow_contract_reference_id}/prepare-task-plan
```

Endpoint ownership:

```text
API layer validates request contract.
Workflow Contract Service executes Workflow Contract behavior.
Matter/Order services validate target context.
Task Service creates active Tasks where application requires them.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preview/preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Workflow Contract Request Contract

Endpoint:

```text
POST /v1/workflow-contracts
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
    - workflow-contract:create
policy_context:
  required_policy_scopes:
    - workflow-contract:create:policy
payload:
  workflow_contract_type: string
  workflow_contract_status: string | null
  workflow_contract_title_safe: string
  applicable_target_types:
    - string
  workflow_steps:
    - step_key: string
      step_title_safe: string
      step_type: string
      required: boolean
      suggested_task_type: string | null
      depends_on_step_keys:
        - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- workflow_contract_type and workflow_contract_title_safe are required.
- workflow_steps must be valid and acyclic.
- applicable_target_types must be controlled.
- Workflow Contract Service assigns workflow_contract_reference_id.
```

---

# 9. Create Workflow Contract Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  workflow_contract_reference_id: string
  workflow_contract_type: string
  workflow_contract_status: string
  workflow_contract_title_safe: string
  applicable_target_types:
    - string
  step_count: integer
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
- Workflow contract creation events may be returned only if event specs exist and service emits them.
- Replayed idempotent response must not duplicate events.
```

---

# 10. Read Workflow Contract

Endpoint:

```text
GET /v1/workflow-contracts/{workflow_contract_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  workflow_contract_reference_id: string
  workflow_contract_type: string
  workflow_contract_status: string
  workflow_contract_title_safe: string
  applicable_target_types:
    - string
  workflow_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
      required: boolean
      suggested_task_type: string | null
      depends_on_step_keys:
        - string
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
- Read must evaluate workflow-contract:read permission.
- Policy may downgrade response to metadata-only.
- Restricted workflow steps may be omitted where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Workflow Contract

Endpoint:

```text
PATCH /v1/workflow-contracts/{workflow_contract_reference_id}
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
  workflow_contract_status: string | null
  workflow_contract_title_safe: string | null
  workflow_steps_patch:
    - step_key: string
      operation: Add | Update | Remove | Replace
      step_payload: object | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - workflow-contract:update
policy_context:
  required_policy_scopes:
    - workflow-contract:update:policy
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
  workflow_contract_reference_id: string
  workflow_contract_status: string
  workflow_contract_title_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Workflow Contract Service.
- Workflow step graph must remain valid and acyclic.
- Human review may be required for changes affecting executable workflow behavior.
```

---

# 12. Search/List Workflow Contracts

Endpoint:

```text
GET /v1/workflow-contracts
```

Query parameters:

```yaml
workflow_contract_type: string | null
workflow_contract_status: string | null
applicable_target_type: string | null
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
    - workflow_contract_reference_id: string
      workflow_contract_type: string
      workflow_contract_status: string
      workflow_contract_title_safe: string
      step_count: integer
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
- Search must not reveal restricted Workflow Contract existence.
```

---

# 13. Validate Workflow Contract Reference

Endpoint:

```text
POST /v1/workflow-contracts/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  workflow_contract_reference_id: string
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
  workflow_contract_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  workflow_contract_type: string | null
  applicable: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to apply workflow.
- Applicability must be evaluated against target context where provided.
- Policy may hide safe_label or applicability detail.
```

---

# 14. Preview Workflow Contract

Endpoint:

```text
POST /v1/workflow-contracts/{workflow_contract_reference_id}/preview
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
    - workflow-contract:preview
policy_context:
  required_policy_scopes:
    - workflow-contract:preview:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  target_object_type: string
  target_object_reference_id: string
  preview_scope: string | null
  include_task_plan: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  preview_status: string
  workflow_contract_reference_id: string
  target_object_type: string
  target_object_reference_id: string
  applicable: boolean
  proposed_steps_visible:
    - step_key: string
      step_title_safe: string
      step_type: string
      proposed_task_type: string | null
  proposed_task_plan_safe: object | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Preview is assistance and does not apply workflow.
- Preview must not create Tasks.
- AI-assisted preview must follow Workflow Agent governance.
- Human review may be required before application.
```

---

# 15. Apply Workflow Contract

Endpoint:

```text
POST /v1/workflow-contracts/{workflow_contract_reference_id}/apply
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
    - workflow-contract:apply
policy_context:
  required_policy_scopes:
    - workflow-contract:apply:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
payload:
  target_object_type: string
  target_object_reference_id: string
  apply_scope: string
  create_tasks: boolean
  task_creation_mode: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  workflow_application_reference_id: string
  workflow_contract_reference_id: string
  target_object_type: string
  target_object_reference_id: string
  application_status: string
  created_task_reference_ids:
    - string
  skipped_steps:
    - step_key: string
      reason_safe: string | null
  applied_at: datetime
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
- Apply requires idempotency_key.
- Apply must route through Workflow Contract Service.
- Active Task creation must route through Task Service.
- Human review may be required before application.
- WorkflowContractApplied event may be emitted by Workflow Contract Service.
- TaskCreated events may be emitted only by Task Service.
```

---

# 16. Prepare Task Plan Contract

Endpoint:

```text
POST /v1/workflow-contracts/{workflow_contract_reference_id}/prepare-task-plan
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
    - workflow-contract:task-plan:prepare
policy_context:
  required_policy_scopes:
    - workflow-contract:task-plan:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  target_object_type: string
  target_object_reference_id: string
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
    - step_key: string
      task_title_safe: string
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
- Human review may be required before task creation or assignment.
```

---

# 17. Controlled Values

## 17.1 workflow_contract_type

```text
TrademarkApplicationWorkflow
OfficeActionResponseWorkflow
RenewalWorkflow
AssignmentWorkflow
ChangeRecordalWorkflow
OppositionWorkflow
EvidenceReviewWorkflow
CustomerIntakeWorkflow
OrderFulfillmentWorkflow
InternalWorkflow
Other
Unknown
```

## 17.2 workflow_contract_status

```text
Draft
Active
Deprecated
Suspended
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 step_type

```text
Intake
Review
PrepareDocument
CollectEvidence
ExternalCommunication
InternalApproval
ProviderRouting
FilingPreparation
SubmissionPreparation
StatusCheck
CustomerConfirmation
TaskGroup
Other
Unknown
```

## 17.4 applicable_target_type

```text
Matter
Order
Trademark
Customer
Opportunity
InternalObject
Unknown
```

## 17.5 preview_status

```text
Completed
Partial
NotApplicable
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.6 application_status

```text
Applied
PartiallyApplied
NotApplied
PolicyRestricted
PermissionDenied
RequiresHumanReview
Conflict
Error
Unknown
```

## 17.7 task_creation_mode

```text
CreateAll
CreateRequiredOnly
PreviewOnly
ManualSelection
Unknown
```

## 17.8 task_plan_status

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

## 17.9 validation_status

```text
Valid
Invalid
NotFound
NotApplicable
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Deprecated
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 17.10 sort.field

```text
created_at
updated_at
workflow_contract_title_safe
workflow_contract_status
workflow_contract_type
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] workflow_contract_reference_id is valid where required.
[ ] idempotency_key is present for create and apply.
[ ] workflow_contract_type is controlled.
[ ] workflow_contract_status is controlled where provided.
[ ] workflow_steps are valid and acyclic.
[ ] applicable_target_types are controlled.
[ ] target object reference is validated where provided.
[ ] task_creation_mode is controlled where provided.
[ ] AI Context is present for AI-assisted preview/task-plan preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 19. Permission Rules

Required permission keys:

```text
workflow-contract:create
workflow-contract:read
workflow-contract:search
workflow-contract:update
workflow-contract:validate
workflow-contract:preview
workflow-contract:apply
workflow-contract:task-plan:prepare
```

Rules:

```text
- Workflow Contract API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
workflow-contract:create:policy
workflow-contract:read:policy
workflow-contract:search:policy
workflow-contract:update:policy
workflow-contract:reference:policy
workflow-contract:preview:policy
workflow-contract:apply:policy
workflow-contract:task-plan:prepare:policy
workflow-contract:visibility:policy
cross-organization:workflow-contract
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact workflow steps, task plans, target context, private notes or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before apply or task creation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may preview workflow and prepare task plans only within Permission and Policy limits.
- AI must not apply workflows, create active tasks, complete tasks, close matters/orders or approve professional execution.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Workflow Contract output is used for applying workflow, creating tasks, changing responsibility or customer-facing explanation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/workflow-contracts requires idempotency_key.
POST /v1/workflow-contracts/{workflow_contract_reference_id}/apply requires idempotency_key.
PATCH endpoints may require idempotency_key where owning service marks the operation duplicate-sensitive.
Preview and prepare-task-plan endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
WorkflowContractApplied may be emitted by Workflow Contract Service after successful application.
TaskCreated may be emitted only by Task Service.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate workflow application or task creation.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 23. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
WorkflowContractReferenceInvalid
WorkflowStepInvalid
WorkflowGraphInvalid
TargetReferenceInvalid
WorkflowNotApplicable
WorkflowPreviewUnavailable
WorkflowApplyConflict
TaskCreationFailed
TaskPlanUnavailable
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
- Errors must not expose database IDs, restricted workflow steps, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 24. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
workflow_contract_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Workflow application must record workflow_contract_version used.
- Response payloads must preserve version fields.
```

---

# 25. Codex Implementation Notes

Codex must:

```text
cite Workflow Contract API Spec
cite Workflow Contract Service Spec
cite Task Service Spec for active task creation
cite this Workflow Contract API Contract
use Reference Contract for workflow_contract_reference_id and target references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted preview/task plans
use Human Review Contract where policy requires review
use Idempotency Contract for create and apply
use Versioning Contract for version validation
route all Workflow Contract mutation/application through Workflow Contract Service
route active Task creation through Task Service
invoke Matter/Order services for target validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing workflow steps, target context or task plans
return safe errors only
write tests for create/read/update/search/validate-reference/preview/apply/prepare-task-plan
write tests for workflow graph validation
write tests that preview does not create Tasks
write tests that apply requires idempotency_key
write tests that duplicate apply does not duplicate tasks or events
write tests that active Task creation is owned by Task Service
write tests for protected apply requiring human review
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Workflow Contract directly in API layer
query database directly from API contract implementation
use generic id where workflow_contract_reference_id is required
expose database IDs, restricted workflow steps or private workflow notes
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
create active Tasks from preview or prepare-task-plan endpoints
complete Task, Matter or Order from Workflow Contract API
treat AI workflow preview as execution approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Workflow Contract API Contract is accepted only if:

```text
[ ] It defines Workflow Contract API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Workflow Contract API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines preview contract.
[ ] It defines apply contract.
[ ] It defines prepare task plan contract.
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

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contract API Contract. Defines governed create, read, update, search, validate-reference, preview, apply and prepare-task-plan payloads, target validation, Task Service boundary, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---


## Workflow Transition Decision Vocabulary

Active canonical workflow transition decisions are:

```text
Allowed
Denied
Blocked
ReviewRequired
ApprovalRequired
PermissionRequired
PolicyRequired
InvalidState
InvalidTransition
Unknown
```

Legacy terms are compatibility-only and must not be returned as active workflow transition decisions.

**End of API Contract**
