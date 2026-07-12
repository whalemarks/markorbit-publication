# API Specification — Workflow Contract API

**Spec ID:** B02-API-WORKFLOW-CONTRACT  
**Spec Type:** API Specification  
**API Name:** Workflow Contract API  
**API File:** core-specs/api/workflow-contract-api.md  
**Related Domain:** core-specs/domains/workflow-contract.md  
**Related Object Specs:** core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md  
**Related Event Specs:** core-specs/events/workflow-contract-applied.md; core-specs/events/task-created.md; core-specs/events/matter-created.md; core-specs/events/order-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/workflow-contract-api-contract.md; core-specs/contracts/events/workflow-contract-applied-payload.md  
**Related Agent Specs:** core-specs/agents/workflow-contract-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Workflow Contract API exposes governed Workflow Contract operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, preview and apply Workflow Contract references without treating Workflow Contract as workflow execution, Task execution, Matter decision, Order confirmation, professional approval, system automation permission or AI autonomous action.

Workflow Contract API exists to support:

```text
workflow structure definition
reusable workflow pattern governance
matter/order workflow application
task plan preparation
event-driven workflow traceability
policy-controlled workflow visibility
AI-assisted workflow planning under governance
API-safe workflow contract reference validation
```

Workflow Contract API does not execute work by itself, complete tasks, file applications, approve legal work product or authorize AI to act outside governed boundaries.

---

# 2. API Meaning

Workflow Contract API means:

```text
a governed interface for operating Workflow Contract definitions and applications through Workflow Contract Service.
```

Workflow Contract API does not mean:

```text
Task API
Matter API
Order API
workflow engine API
automation runtime API
professional approval API
filing API
AI autonomous execution API
```

Workflow Contract defines executable structure.

Task owns actionable work items.

Matter and Order provide operating context.

Execution requires governed services, permission, policy and event trace.

---

# 3. API Boundary

Workflow Contract API is responsible for:

```text
Workflow Contract create request intake
Workflow Contract read/search/list access
Workflow Contract update request intake
Workflow Contract reference validation
Workflow Contract preview and application request intake
Task plan preparation from Workflow Contract
safe Workflow Contract response shaping
Permission/Policy enforcement for Workflow Contract operations
Workflow Contract-related Event reference exposure where allowed
AI Agent access boundary for Workflow Contract operations
controlled API errors
```

Workflow Contract API is not responsible for:

```text
Task execution
Task assignment finalization unless Task Service accepts it
Matter lifecycle ownership
Order lifecycle ownership
professional legal conclusion
filing execution
automation runtime execution
AI autonomous action approval
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/workflow-contract.md
```

Domain rule:

```text
Workflow Contract defines governed workflow structure and application rules.
Workflow Contract is not Task execution, Matter decision, Order confirmation or automation runtime by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/workflow-contract.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/task.md
core-specs/objects/event.md
core-specs/objects/policy.md
core-specs/objects/permission.md
core-specs/objects/agent.md
```

Object rules:

```text
- Workflow Contract API returns workflow_contract_reference_id.
- Workflow Contract API may reference Matter, Order, Task, Event, Policy and Agent context but must not create or execute them silently.
- Workflow Contract application may prepare task plans but must route Task creation through Task Service.
- Workflow Contract application is not proof that workflow work has been completed.
- Workflow Contract must not expose restricted internal process design by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/workflow-contract-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/task-service.md
core-specs/services/event-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/agent-service.md
```

Service rules:

```text
- Workflow Contract API must invoke Workflow Contract Service for Workflow Contract behavior.
- Workflow Contract API must validate related Matter, Order and Task references through their owning services where required.
- Workflow Contract API must invoke Permission Service where operation requires authorization.
- Workflow Contract API must invoke Policy Service where contextual constraints apply.
- Workflow Contract API must not emit WorkflowContractApplied directly; Workflow Contract Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/workflow-contract-applied.md
core-specs/events/task-created.md
core-specs/events/matter-created.md
core-specs/events/order-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- applyWorkflowContract may result in WorkflowContractApplied.
- creating Tasks from applied workflow must use Task Service and may result in TaskCreated.
- API consumers must not fabricate WorkflowContractApplied.
- WorkflowContractApplied is application trace, not task execution or professional completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Workflow Contract

**Operation Category:** Create  
**Method:** POST  
**Path:** `/workflow-contracts`  
**Owning Service Operation:** `createWorkflowContract`  
**Permission Required:** `workflow-contract:create`  
**Policy Required:** `WorkflowContractCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service May Emit WorkflowContractCreated where event is defined

Meaning:

```text
Create a governed Workflow Contract definition.
```

Non-meaning:

```text
does not apply workflow to Matter or Order
does not create Task
does not execute automation
does not approve professional work
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
Workflow Contract Service createWorkflowContract
  ↓
Event Service record event where applicable
  ↓
Safe API response
```

## 8.2 Operation: Get Workflow Contract

**Operation Category:** Read  
**Method:** GET  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}`  
**Owning Service Operation:** `getWorkflowContract`  
**Permission Required:** `workflow-contract:read`  
**Policy Required:** `WorkflowContractVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Workflow Contract definition view.
```

Non-meaning:

```text
does not expose restricted internal process details automatically
does not expose agent automation rules automatically
does not indicate workflow has been applied or executed
```

## 8.3 Operation: Search Workflow Contracts

**Operation Category:** Search  
**Method:** GET  
**Path:** `/workflow-contracts`  
**Owning Service Operation:** `searchWorkflowContracts`  
**Permission Required:** `workflow-contract:search`  
**Policy Required:** `WorkflowContractVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Workflow Contract references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted internal workflow library access
does not expose restricted automation, agent or process rules by default
```

## 8.4 Operation: Update Workflow Contract

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}`  
**Owning Service Operation:** `updateWorkflowContract`  
**Permission Required:** `workflow-contract:update`  
**Policy Required:** `WorkflowContractUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit WorkflowContractUpdated where event is defined

Meaning:

```text
Update governed Workflow Contract metadata, version, status or structure under Workflow Contract Service rules.
```

Non-meaning:

```text
does not rewrite already-applied workflow history
does not mutate existing Tasks automatically
does not approve automation execution
does not approve professional conclusions
```

## 8.5 Operation: Validate Workflow Contract Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/workflow-contracts/reference/validate`  
**Owning Service Operation:** `validateWorkflowContractReference`  
**Permission Required:** `workflow-contract:validate`  
**Policy Required:** `WorkflowContractReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Workflow Contract reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not approve application
does not create Task
does not execute workflow
does not authorize AI automation
```

## 8.6 Operation: Preview Workflow Contract Application

**Operation Category:** Evaluate  
**Method:** POST  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}/application/preview`  
**Owning Service Operation:** `previewWorkflowContractApplication`  
**Permission Required:** `workflow-contract:application:preview`  
**Policy Required:** `WorkflowContractApplicationPreviewPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit WorkflowContractApplied

Meaning:

```text
Preview how a Workflow Contract would apply to Matter, Order or another governed context.
```

Non-meaning:

```text
does not apply workflow
does not create Tasks
does not execute automation
does not mutate target context
```

## 8.7 Operation: Apply Workflow Contract

**Operation Category:** Action  
**Method:** POST  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}/apply`  
**Owning Service Operation:** `applyWorkflowContract`  
**Permission Required:** `workflow-contract:apply`  
**Policy Required:** `WorkflowContractApplicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service Must Emit WorkflowContractApplied

Meaning:

```text
Apply a governed Workflow Contract to a target Matter, Order or supported Core context.
```

Non-meaning:

```text
does not execute all Tasks
does not complete service delivery
does not approve professional work
does not bypass Task Service
```

## 8.8 Operation: Prepare Tasks from Workflow Contract

**Operation Category:** Action  
**Method:** POST  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}/tasks/prepare`  
**Owning Service Operation:** `prepareTasksFromWorkflowContract`  
**Permission Required:** `workflow-contract:tasks:prepare`  
**Policy Required:** `WorkflowContractTaskPreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit TaskCreated

Meaning:

```text
Prepare a governed Task plan from a Workflow Contract without creating Tasks.
```

Non-meaning:

```text
does not create Task
does not assign work
does not execute workflow
does not complete service delivery
```

## 8.9 Operation: Create Tasks from Workflow Contract

**Operation Category:** Action  
**Method:** POST  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}/tasks/create`  
**Owning Service Operation:** `createTasksFromWorkflowContract`  
**Permission Required:** `workflow-contract:tasks:create`  
**Policy Required:** `WorkflowContractTaskCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated plan  
**Event Behavior:** Must route through Task Service; may emit TaskCreated

Meaning:

```text
Create governed Tasks from an approved Workflow Contract application or task plan.
```

Non-meaning:

```text
does not execute Tasks automatically
does not complete workflow
does not approve professional work
does not bypass Task Service permission and policy
```

## 8.10 Operation: List Workflow Contract Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/workflow-contracts/{workflow_contract_reference_id}/events`  
**Owning Service Operation:** `listWorkflowContractEvents`  
**Permission Required:** `workflow-contract:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Workflow Contract-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Workflow Contract Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  workflow_contract_type: string
  workflow_contract_status: string | optional
  workflow_contract_name: string
  workflow_contract_version: string
  target_context_type: string
  workflow_steps_reference: string | null
  source_type: string
  safe_summary: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Workflow Contract Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  workflow_contract_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  workflow_contract_status: string | optional
  workflow_contract_name: string | optional
  workflow_contract_version: string | optional
  workflow_steps_reference: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Workflow Contract Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  workflow_contract_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Preview / Apply Workflow Contract Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  workflow_contract_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_context_type: string
  target_context_reference_id: string
  application_mode: string
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.5 Prepare / Create Tasks Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  workflow_contract_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  workflow_application_reference_id: string | null
  target_context_type: string
  target_context_reference_id: string
  task_plan_reference_id: string | null
  task_creation_mode: string
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted internal workflow logic, automation secrets or agent credentials by default.
- Requests must use controlled workflow_contract_type, workflow_contract_status, target_context_type, application_mode and task_creation_mode values.
- AI-generated workflow contracts or plans must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Workflow Contract Response

```yaml
status: 200
body:
  workflow_contract_reference_id: string
  workflow_contract_type: string
  workflow_contract_status: string
  workflow_contract_name: string
  workflow_contract_version: string
  target_context_type: string
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    step_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Workflow Contract Response

```yaml
status: 201
body:
  workflow_contract_reference_id: string
  workflow_contract_status: string
  review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Workflow Contract Reference Validation Response

```yaml
status: 200
body:
  workflow_contract_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Workflow Application Preview Response

```yaml
status: 200
body:
  workflow_contract_reference_id: string
  target_context_type: string
  target_context_reference_id: string
  application_preview_reference_id: string | null
  applicable: boolean
  missing_items: list[string]
  blocked_items: list[string]
  task_plan_preview:
    task_count: integer
    task_type_summary: list[string]
  human_review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Workflow Application Response

```yaml
status: 200
body:
  workflow_contract_reference_id: string
  target_context_type: string
  target_context_reference_id: string
  workflow_application_reference_id: string | null
  application_status: string
  related_event_reference_ids:
    - workflow_contract_applied_event_id
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Task Preparation / Creation Response

```yaml
status: 200
body:
  workflow_contract_reference_id: string
  workflow_application_reference_id: string | null
  task_plan_reference_id: string | null
  task_creation_status: string
  created_task_reference_ids: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Task execution, workflow completion, filing, professional approval or AI authority.
- Responses must not expose restricted workflow logic, automation internals, agent prompts or internal process strategy by default.
- Responses must distinguish Workflow Contract, Workflow Application, Task Plan and Task references.
- Responses must identify review requirements for AI-generated or AI-suggested workflow structures.
```

---

# 11. Controlled Values

## 11.1 workflow_contract_type

```text
TrademarkSearchWorkflow
TrademarkFilingWorkflow
RenewalWorkflow
OfficeActionWorkflow
OppositionWorkflow
CancellationWorkflow
RecordalWorkflow
PortfolioWorkflow
ConsultationWorkflow
InternalWorkflow
Unknown
```

## 11.2 workflow_contract_status

```text
Draft
Active
ReviewRequired
Deprecated
Superseded
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 target_context_type

```text
Matter
Order
Task
WorkflowApplication
System
Unknown
```

## 11.4 source_type

```text
ProfessionalInput
SystemTemplate
MatterDerived
OrderDerived
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.5 application_mode

```text
Preview
ApplyOnly
ApplyAndPrepareTasks
ApplyAndCreateTasks
Unknown
```

## 11.6 task_creation_mode

```text
Preview
PrepareOnly
CreateDraftTasks
CreateActiveTasks
Unknown
```

## 11.7 application_status

```text
Previewed
Applied
Denied
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.8 task_creation_status

```text
Previewed
Prepared
Created
Denied
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
Deprecated
ContextMismatch
Unknown
```

## 11.10 intended_use

```text
MatterApplication
OrderApplication
TaskPreparation
TaskCreation
WorkflowPreview
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
workflow-contract:create
workflow-contract:read
workflow-contract:search
workflow-contract:update
workflow-contract:validate
workflow-contract:application:preview
workflow-contract:apply
workflow-contract:tasks:prepare
workflow-contract:tasks:create
workflow-contract:event:read
```

Rules:

```text
- Workflow Contract read/search must be permission-controlled.
- Workflow Contract creation must not imply application or execution.
- Workflow Contract validation must not authorize application or task creation.
- Preview, apply, task preparation and task creation require separate permissions.
- Task creation from Workflow Contract must also satisfy Task Service permissions.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
WorkflowContractCreationPolicy
WorkflowContractUpdatePolicy
WorkflowContractVisibilityPolicy
WorkflowContractReferencePolicy
WorkflowContractApplicationPreviewPolicy
WorkflowContractApplicationPolicy
WorkflowContractTaskPreparationPolicy
WorkflowContractTaskCreationPolicy
EventVisibilityPolicy
AIAgentWorkflowContractAccessPolicy
RestrictedWorkflowContractDataPolicy
CrossOrganizationWorkflowContractPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Workflow Contract fields.
- Policy may require human review for AI-generated Workflow Contracts or task plans.
- Policy may restrict cross-organization Workflow Contract lookup.
- Policy may restrict internal workflow logic, agent prompts, automation rules and process strategy.
- Policy may restrict Workflow Contract application and Task creation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Workflow Contract: Restricted / HumanReviewRequired where AI-generated
Get Workflow Contract: Restricted
Search Workflow Contracts: Restricted
Update Workflow Contract: Restricted / HumanReviewRequired where sensitive
Validate Workflow Contract Reference: Allowed under contract
Preview Workflow Contract Application: Restricted / HumanReviewRequired where AI-suggested
Apply Workflow Contract: Restricted / HumanReviewRequired where AI-suggested
Prepare Tasks from Workflow Contract: Restricted / HumanReviewRequired
Create Tasks from Workflow Contract: Restricted / HumanReviewRequired
List Workflow Contract Events: Restricted
```

AI Agents may:

```text
summarize safe Workflow Contract metadata
suggest workflow structure for human review
validate Workflow Contract references for authorized actions
preview workflow application for human review
prepare task plan draft for human review
flag missing inputs or blocked steps
```

AI Agents must not:

```text
fabricate Workflow Contract
fabricate WorkflowContractApplied events
treat AI-generated Workflow Contract as approved process
apply Workflow Contract without governed permission and policy
create or execute Tasks silently
approve professional work product
bypass Workflow Contract, Task, Permission or Policy rules
expose restricted workflow logic, prompts or automation internals
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

Workflow Contract API may expose:

```text
WorkflowContractApplied
TaskCreated
MatterCreated
OrderCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Workflow Contract events directly.
- WorkflowContractApplied must not be treated as Task execution, workflow completion, filing or professional approval.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] workflow_contract_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] target_context_type is controlled.
[ ] target_context_reference_id is valid where required.
[ ] workflow_contract_type is controlled.
[ ] workflow_contract_status is controlled.
[ ] source_type is controlled.
[ ] application_mode is controlled where applicable.
[ ] task_creation_mode is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted workflow/process/automation/agent fields are omitted or allowed.
[ ] AI-generated workflow data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] Preview operation does not apply Workflow Contract.
[ ] Apply operation emits WorkflowContractApplied after success.
[ ] Task preparation does not create Tasks.
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
WorkflowContractReferenceInvalid
TargetContextReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
TaskReferenceInvalid
ValidationFailed
DuplicateDenied
StateInvalid
ApplicationDenied
TaskPlanInvalid
RestrictedFieldViolation
RestrictedWorkflowContractData
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
- Errors must not expose restricted Workflow Contract data.
- Errors must not expose internal process logic, automation secrets, agent prompts or privileged strategy.
- Errors must not expose unrelated Matter/Order/Task details.
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
- workflow_contract_type, workflow_contract_status, target_context_type, application_mode and task_creation_mode changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI workflow-planning behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Workflow Contract API spec
cite Workflow Contract Service Specification
cite Workflow Contract Object Specification
cite WorkflowContractApplied Event Specification
cite Matter/Order/Task specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid workflow_contract_reference_id
write tests for invalid target context references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Workflow Contract creation does not apply workflow
write tests that preview does not apply Workflow Contract
write tests that apply emits WorkflowContractApplied after success
write tests that task preparation does not create Tasks
write tests that task creation routes through Task Service
write tests for AI Agent Contract and human review requirement
```

Codex must not:

```text
write directly to database bypassing Workflow Contract Service
allow UI to emit WorkflowContractApplied directly
treat Workflow Contract as Task execution
treat Workflow Contract as workflow completion
treat AI-generated Workflow Contract as approved process
create or execute Tasks silently from Workflow Contract operations
expose restricted workflow logic or automation internals for convenience
allow AI to fabricate Workflow Contract references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Workflow Contract API purpose.
[ ] It defines Workflow Contract API meaning.
[ ] It defines Workflow Contract API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, preview, apply, task preparation, task creation and event-list operations.
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
| 0.1.0 | Draft | Initial Workflow Contract API specification. Defines governed Workflow Contract definition/application interface and separates Workflow Contract API from Task execution, workflow completion, Matter/Order decisions, professional approval and AI autonomous execution. |

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

**End of API Specification**
