# API Specification — Task API

**Spec ID:** B02-API-TASK  
**Spec Type:** API Specification  
**API Name:** Task API  
**API File:** core-specs/api/task-api.md  
**Related Domain:** core-specs/domains/task.md  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/user.md; core-specs/objects/agent.md; core-specs/objects/event.md; core-specs/objects/notification.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/user-service.md; core-specs/services/agent-service.md; core-specs/services/event-service.md; core-specs/services/notification-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/notification-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/task-api-contract.md; core-specs/contracts/events/task-created-payload.md  
**Related Agent Specs:** core-specs/agents/task-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Task API exposes governed Task operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, assign, start, complete and observe Task references without treating Task as Workflow Contract, Matter, Order, professional approval, filing completion, communication delivery, notification delivery, AI autonomous work or final business/legal decision.

Task API exists to support:

```text
actionable work item creation
matter/order work breakdown
workflow-contract-derived task creation
assignee and responsibility context
task state management
task execution trace
notification and communication preparation
policy-controlled task visibility
AI-assisted task planning and drafting under governance
event trace access
API-safe task reference validation
```

Task API does not complete professional work by itself, file applications, submit documents, approve legal conclusions, deliver communications or authorize AI autonomous execution.

---

# 2. API Meaning

Task API means:

```text
a governed interface for operating actionable work items through Task Service.
```

Task API does not mean:

```text
Workflow Contract API
Matter API
Order API
professional approval API
filing API
Communication API
Notification API
automation runtime API
AI autonomous execution API
```

Task is an actionable work item.

Workflow Contract defines work structure.

Matter and Order provide context.

Communication and Notification are separate execution channels.

---

# 3. API Boundary

Task API is responsible for:

```text
Task create request intake
Task read/search/list access
Task update request intake
Task reference validation
Task assignment request intake
Task state transition request intake
Task completion request intake
safe Task response shaping
Permission/Policy enforcement for Task operations
Task-related Event reference exposure where allowed
AI Agent access boundary for Task operations
controlled API errors
```

Task API is not responsible for:

```text
Workflow Contract definition
Matter lifecycle ownership
Order lifecycle ownership
professional legal conclusion
official filing execution
communication delivery
notification delivery
user identity lifecycle
AI autonomous action approval
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/task.md
```

Domain rule:

```text
Task represents actionable work.
Task is not Workflow Contract, Matter, Order, filing, communication delivery, professional approval or AI autonomous execution by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/task.md
core-specs/objects/workflow-contract.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/user.md
core-specs/objects/agent.md
core-specs/objects/event.md
core-specs/objects/notification.md
core-specs/objects/communication.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Task API returns task_reference_id.
- Task API may reference Matter, Order, Workflow Contract, User, Agent, Notification or Communication context but must not create or execute them silently.
- Task assignment is not User creation.
- Task completion is not professional approval unless a separate professional decision is recorded.
- Task completion is not communication delivery, filing completion or official result.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/task-service.md
core-specs/services/workflow-contract-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/user-service.md
core-specs/services/agent-service.md
core-specs/services/event-service.md
core-specs/services/notification-service.md
core-specs/services/communication-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
```

Service rules:

```text
- Task API must invoke Task Service for Task behavior.
- Task API must validate related Matter, Order, Workflow Contract, User and Agent references through their owning services where required.
- Task API must invoke Permission Service where operation requires authorization.
- Task API must invoke Policy Service where contextual constraints apply.
- Task API must not emit Task events directly; Task Service and Event Service govern events.
- Task API must route communication and notification actions through their owning services.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/task-created.md
core-specs/events/workflow-contract-applied.md
core-specs/events/notification-created.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createTask may result in TaskCreated.
- notification actions must use Notification Service and may result in NotificationCreated.
- communication actions must use Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate TaskCreated.
- TaskCreated is actionable work-item trace, not execution or completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Task

**Operation Category:** Create  
**Method:** POST  
**Path:** `/tasks`  
**Owning Service Operation:** `createTask`  
**Permission Required:** `task:create`  
**Policy Required:** `TaskCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service Must Emit TaskCreated

Meaning:

```text
Create a governed Task work-item reference.
```

Non-meaning:

```text
does not execute Task
does not complete work
does not file application
does not send communication
does not create notification unless explicit operation does so
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
Task Service createTask
  ↓
Event Service record TaskCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Task

**Operation Category:** Read  
**Method:** GET  
**Path:** `/tasks/{task_reference_id}`  
**Owning Service Operation:** `getTask`  
**Permission Required:** `task:read`  
**Policy Required:** `TaskVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Task view.
```

Non-meaning:

```text
does not expose restricted work notes automatically
does not expose customer or matter strategy automatically
does not expose communication content automatically
does not assert completed professional result automatically
```

## 8.3 Operation: Search Tasks

**Operation Category:** Search  
**Method:** GET  
**Path:** `/tasks`  
**Owning Service Operation:** `searchTasks`  
**Permission Required:** `task:search`  
**Policy Required:** `TaskVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Task references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted work queue access
does not expose restricted assignee, customer, strategy or work-product data by default
```

## 8.4 Operation: Update Task

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/tasks/{task_reference_id}`  
**Owning Service Operation:** `updateTask`  
**Permission Required:** `task:update`  
**Policy Required:** `TaskUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit TaskUpdated where event is defined

Meaning:

```text
Update governed Task metadata, priority, due date, status or context under Task Service rules.
```

Non-meaning:

```text
does not execute Task automatically
does not complete Task automatically unless completion operation is used
does not update Matter or Order state automatically
does not approve professional conclusions
```

## 8.5 Operation: Validate Task Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/tasks/reference/validate`  
**Owning Service Operation:** `validateTaskReference`  
**Permission Required:** `task:validate`  
**Policy Required:** `TaskReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Task reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not authorize work execution
does not approve completion
does not prove assignee responsibility
does not prove professional result
```

## 8.6 Operation: Assign Task

**Operation Category:** Action  
**Method:** POST  
**Path:** `/tasks/{task_reference_id}/assign`  
**Owning Service Operation:** `assignTask`  
**Permission Required:** `task:assign`  
**Policy Required:** `TaskAssignmentPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit TaskUpdated or future TaskAssigned where event is defined

Meaning:

```text
Assign or reassign a governed Task to a User, Agent, role or queue context.
```

Non-meaning:

```text
does not create User or Agent
does not prove assignee accepted work
does not execute Task
does not approve professional result
```

## 8.7 Operation: Start Task

**Operation Category:** StateTransition  
**Method:** POST  
**Path:** `/tasks/{task_reference_id}/start`  
**Owning Service Operation:** `startTask`  
**Permission Required:** `task:start`  
**Policy Required:** `TaskStateTransitionPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit TaskUpdated where event is defined

Meaning:

```text
Move a Task into an active work state under governed transition rules.
```

Non-meaning:

```text
does not complete work
does not submit filing
does not send communication
does not approve output
```

## 8.8 Operation: Complete Task

**Operation Category:** StateTransition  
**Method:** POST  
**Path:** `/tasks/{task_reference_id}/complete`  
**Owning Service Operation:** `completeTask`  
**Permission Required:** `task:complete`  
**Policy Required:** `TaskCompletionPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-produced output  
**Event Behavior:** Service May Emit TaskCompleted where event is defined; otherwise audit state transition

Meaning:

```text
Mark a governed Task as completed with required completion context.
```

Non-meaning:

```text
does not approve professional work automatically
does not file application automatically
does not send communication automatically
does not mark Matter or Order complete automatically
does not verify official result
```

## 8.9 Operation: Prepare Task Notification

**Operation Category:** Action  
**Method:** POST  
**Path:** `/tasks/{task_reference_id}/notifications/prepare`  
**Owning Service Operation:** `prepareTaskNotification`  
**Permission Required:** `task:notification:prepare`  
**Policy Required:** `TaskNotificationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Notification Service if notification is created

Meaning:

```text
Prepare a governed Notification draft or request related to a Task.
```

Non-meaning:

```text
does not create Notification unless Notification Service accepts it
does not deliver message
does not bypass notification policy
```

## 8.10 Operation: Prepare Task Communication

**Operation Category:** Action  
**Method:** POST  
**Path:** `/tasks/{task_reference_id}/communications/prepare`  
**Owning Service Operation:** `prepareTaskCommunication`  
**Permission Required:** `task:communication:prepare`  
**Policy Required:** `TaskCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if communication is created

Meaning:

```text
Prepare a governed Communication draft or request related to a Task.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not approve external wording
does not bypass communication review
```

## 8.11 Operation: List Task Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/tasks/{task_reference_id}/events`  
**Owning Service Operation:** `listTaskEvents`  
**Permission Required:** `task:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Task-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Task Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  task_type: string
  task_status: string | optional
  task_priority: string | optional
  title: string
  safe_summary: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
  workflow_application_reference_id: string | null
  assignee_type: string | null
  assignee_reference_id: string | null
  due_at: datetime | null
  source_type: string
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Task Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  task_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  task_status: string | optional
  task_priority: string | optional
  title: string | optional
  safe_summary: string | optional
  due_at: datetime | optional
  request_context: object
```

## 9.3 Validate Task Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  task_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Assign Task Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  task_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  assignee_type: string
  assignee_reference_id: string
  assignment_reason: string | null
  request_context: object
```

## 9.5 Start / Complete Task Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  task_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  state_transition_reason: string | null
  completion_context:
    result_summary: string | null
    output_document_reference_id: string | null
    communication_reference_id: string | null
    human_review_reference_id: string | null
  request_context: object
```

## 9.6 Prepare Task Notification / Communication Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  preparation_purpose: string
  draft_mode: string
  target_recipient_context:
    recipient_type: string | null
    recipient_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted customer strategy, privileged notes, communication content, secrets or raw document content by default.
- Requests must use controlled task_type, task_status, task_priority, assignee_type, source_type and draft_mode values.
- AI-generated Task plans or communication drafts must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Task Response

```yaml
status: 200
body:
  task_reference_id: string
  task_type: string
  task_status: string
  task_priority: string
  title: string
  matter_reference_id: string | null
  order_reference_id: string | null
  workflow_contract_reference_id: string | null
  workflow_application_reference_id: string | null
  assignee_type: string | null
  assignee_reference_id: string | null
  due_at: datetime | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    work_summary: string | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Task Response

```yaml
status: 201
body:
  task_reference_id: string
  task_status: string
  review_required: boolean
  related_event_reference_ids:
    - task_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Task Reference Validation Response

```yaml
status: 200
body:
  task_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Task Assignment Response

```yaml
status: 200
body:
  task_reference_id: string
  assignee_type: string
  assignee_reference_id: string
  assignment_status: string
  review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Task State Transition Response

```yaml
status: 200
body:
  task_reference_id: string
  from_status: string
  to_status: string
  transition_status: string
  human_review_required: boolean
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Prepared Notification / Communication Response

```yaml
status: 200
body:
  task_reference_id: string
  draft_reference_id: string | null
  preparation_status: string
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Task execution where only creation, assignment or preparation occurred.
- Responses must not imply professional approval, filing, communication delivery or notification delivery.
- Responses must not expose restricted work notes, customer strategy, communication content or internal assignee data by default.
- Responses must distinguish Task references from Matter, Order, Workflow Contract, Notification and Communication references.
```

---

# 11. Controlled Values

## 11.1 task_type

```text
IntakeTask
ReviewTask
SearchTask
ClassificationTask
DocumentTask
EvidenceTask
FilingPreparationTask
OfficeActionTask
CommunicationTask
NotificationTask
RoutingTask
PaymentPreparationTask
QualityCheckTask
InternalTask
Unknown
```

## 11.2 task_status

```text
Draft
Open
Assigned
InProgress
Blocked
ReviewRequired
Completed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 task_priority

```text
Low
Normal
High
Urgent
Unknown
```

## 11.4 assignee_type

```text
User
Agent
Role
Queue
System
ExternalIntegration
Unknown
```

## 11.5 source_type

```text
ProfessionalInput
WorkflowContractDerived
MatterDerived
OrderDerived
CommunicationDerived
SystemGenerated
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.6 draft_mode

```text
Preview
CreateDraft
CreateAndRequestReview
Unknown
```

## 11.7 preparation_purpose

```text
Reminder
ClientUpdate
AgentInstruction
InternalNotice
TaskEscalation
CompletionNotice
AIAssistedDraft
Unknown
```

## 11.8 assignment_status

```text
Assigned
Reassigned
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.9 transition_status

```text
Accepted
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.10 validation_status

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

## 11.11 intended_use

```text
WorkExecution
MatterContext
OrderContext
WorkflowContext
NotificationPreparation
CommunicationPreparation
AIAgentAction
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
task:create
task:read
task:search
task:update
task:validate
task:assign
task:start
task:complete
task:notification:prepare
task:communication:prepare
task:event:read
```

Rules:

```text
- Task read/search must be permission-controlled.
- Task creation must not imply execution or completion.
- Task validation must not authorize work execution or completion.
- Assignment, start and completion require separate permissions.
- Notification and Communication preparation require separate permissions and downstream service rules.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
TaskCreationPolicy
TaskUpdatePolicy
TaskVisibilityPolicy
TaskReferencePolicy
TaskAssignmentPolicy
TaskStateTransitionPolicy
TaskCompletionPolicy
TaskNotificationPolicy
TaskCommunicationPolicy
EventVisibilityPolicy
AIAgentTaskAccessPolicy
RestrictedTaskDataPolicy
CrossOrganizationTaskPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Task fields.
- Policy may require human review for AI-generated Task plans or outputs.
- Policy may restrict cross-organization Task lookup.
- Policy may restrict assignee details, internal notes, customer strategy, communication drafts and privileged work product.
- Policy may restrict Task state transitions and completion.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Task: Restricted / HumanReviewRequired where AI-generated
Get Task: Restricted
Search Tasks: Restricted
Update Task: Restricted / HumanReviewRequired where sensitive
Validate Task Reference: Allowed under contract
Assign Task: Restricted / HumanReviewRequired where AI-suggested
Start Task: Restricted
Complete Task: Restricted / HumanReviewRequired where AI-produced output
Prepare Task Notification: Restricted / HumanReviewRequired where AI-drafted
Prepare Task Communication: Restricted / HumanReviewRequired where AI-drafted
List Task Events: Restricted
```

AI Agents may:

```text
summarize safe Task metadata
flag missing Task inputs or blocked state
validate Task references for authorized actions
suggest assignment for human review
prepare Task plans for human review
prepare notification or communication drafts for human review
summarize completion context where allowed
```

AI Agents must not:

```text
fabricate Task
fabricate TaskCreated events
treat AI-generated Task as approved work plan
complete Task without governed permission and review where required
file application or submit documents
send communication or notification directly through Task API
approve professional conclusions
bypass Permission or Policy
expose restricted work notes or communication content
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

Task API may expose:

```text
TaskCreated
WorkflowContractApplied
NotificationCreated
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Task events directly.
- TaskCreated must not be treated as Task execution, professional completion, filing, notification delivery or communication delivery.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] task_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] matter_reference_id is valid where provided.
[ ] order_reference_id is valid where provided.
[ ] workflow_contract_reference_id is valid where provided.
[ ] workflow_application_reference_id is valid where provided.
[ ] assignee_reference_id is valid where required.
[ ] task_type is controlled.
[ ] task_status is controlled.
[ ] task_priority is controlled.
[ ] assignee_type is controlled.
[ ] source_type is controlled.
[ ] draft_mode is controlled where applicable.
[ ] state transition is allowed from current status.
[ ] completion context is present where required.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted task/customer/matter/communication/work-product fields are omitted or allowed.
[ ] AI-generated task data or outputs are marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] TaskCreated is emitted after createTask succeeds.
[ ] Notification preparation routes through Notification Service if notification is created.
[ ] Communication preparation routes through Communication Service if communication is created.
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
TaskReferenceInvalid
MatterReferenceInvalid
OrderReferenceInvalid
WorkflowContractReferenceInvalid
WorkflowApplicationReferenceInvalid
AssigneeReferenceInvalid
StateTransitionInvalid
CompletionContextInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedTaskData
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
- Errors must not expose restricted Task data.
- Errors must not expose customer strategy, privileged notes, communication content or work product.
- Errors must not expose unrelated Matter, Order, User or Agent details.
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
- task_type, task_status, task_priority, assignee_type, source_type and state transition changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI task-operation behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Task API spec
cite Task Service Specification
cite Task Object Specification
cite TaskCreated Event Specification
cite Matter/Order/Workflow Contract/User/Agent specs where references are used
cite Notification and Communication specs where downstream preparation is used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid task_reference_id
write tests for invalid matter/order/workflow/assignee references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Task creation does not execute or complete Task
write tests that Task completion does not approve professional output automatically
write tests that Notification preparation does not deliver notification directly
write tests that Communication preparation does not send communication directly
write tests for AI Agent Contract and human review requirement
write tests for TaskCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Task Service
allow UI to emit TaskCreated directly
treat Task as Workflow Contract
treat Task as professional approval
treat Task as filing completion
treat AI-generated Task as approved work plan
send communications or notifications directly through Task API
expose restricted work notes or customer strategy for convenience
allow AI to fabricate Task references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Task API purpose.
[ ] It defines Task API meaning.
[ ] It defines Task API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, assign, start, complete, notification preparation, communication preparation and event-list operations.
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
| 0.1.0 | Draft | Initial Task API specification. Defines governed Task work-item interface and separates Task API from Workflow Contract, Matter, Order, filing, Communication delivery, Notification delivery, professional approval and AI autonomous execution. |

---

**End of API Specification**
