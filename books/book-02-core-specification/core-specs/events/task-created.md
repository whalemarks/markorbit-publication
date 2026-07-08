# Event Specification — TaskCreated

**Spec ID:** B02-EVT-TASK-CREATED  
**Spec Type:** Event  
**Event Name:** TaskCreated  
**Event File:** core-specs/events/task-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Task  
**Producing Service:** core-specs/services/task-service.md  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/workflow-contract.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/notification-service.md  
**Related API Specs:** core-specs/api/task-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/task-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/task-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

TaskCreated records that a governed Task actionable work unit reference has been created by Task Service.

It exists so that Matter, Order, Workflow Contract, User, Permission, Policy, Notification, AI Agents, APIs and product consumers can safely recognize that a work unit now exists without treating that Task as Matter, Workflow, Event, Notification, Permission grant, assignment acceptance, execution completion or final professional decision.

TaskCreated is required before:

```text
work unit trace
matter task planning
workflow task generation
task assignment preparation
task status tracking
permission-controlled work execution
notification preparation
AI-assisted task drafting review
API task reference validation
audit trace for task-sensitive actions
```

---

# 2. Event Meaning

TaskCreated means:

```text
a stable Task object reference has been created through governed Task Service operation.
```

TaskCreated does not mean:

```text
the Task has been assigned
the Task has been accepted
the Task has been completed
the Task grants Permission
a Matter has been created
a Workflow Contract has started
a Notification has been sent
the underlying professional action has been executed
AI task suggestion has been accepted as final professional plan
```

TaskCreated records actionable work unit creation only.

It does not establish assignment, permission, workflow transition, execution result or professional completion.

---

# 3. Event Category

TaskCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Task domain.

It is not a WorkflowEvent, NotificationEvent, PermissionEvent or execution-completion event.

---

# 4. Event Producer

Producing service:

```text
Task Service
```

Producing operation:

```text
createTask
```

Source domain:

```text
Task
```

Source object type:

```text
Task
```

Allowed producer path:

```text
API / Professional user / Workflow Contract / System / AI-assisted governed operation
        ↓
Task Service createTask
        ↓
Event Service record TaskCreated
```

Producer rules:

```text
- TaskCreated must be emitted only after Task Service successfully creates the Task reference.
- TaskCreated must not be emitted directly by product UI.
- TaskCreated must not be emitted directly by AI Agent outside governed service operation.
- TaskCreated must not be emitted for failed, duplicate-rejected or unauthorized task creation attempts.
```

---

# 5. Event Trigger

TaskCreated is triggered when:

```text
Task Service successfully creates a new Task object and commits its stable task_reference_id.
```

Required trigger conditions:

```text
createTask operation completed
task_reference_id created
task_type validated
task_status validated
task_scope captured
matter_reference_id captured where applicable
workflow_contract_reference_id captured where applicable
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Matter creation
Order creation
Workflow Contract definition
Workflow transition
Task assignment
Task completion
Notification creation
Permission evaluation
Policy evaluation
AI task suggestion
failed validation
duplicate rejected Task
```

Related but separate events may include:

```text
MatterCreated
OrderCreated
WorkflowContractApplied
TaskAssigned
TaskStarted
TaskCompleted
NotificationCreated
PermissionEvaluated
PolicyEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: TaskCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Task
source_service: Task Service
source_operation: createTask
source_object_type: Task
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/task-created-payload.md
safe_summary:
  task_reference_id: string
  task_type: string
  task_status: string
  matter_reference_id: string | null
  workflow_contract_reference_id: string | null
  source_type: string
restricted_fields_policy: TaskCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
task_reference_id: string
task_type: string
task_status: string
task_priority: string
task_source_type: string
matter_reference_id: string | null
order_reference_id: string | null
workflow_contract_reference_id: string | null
workflow_step_reference_id: string | null
parent_task_reference_id: string | null
assigned_user_reference_id: string | null
assigned_role_reference_id: string | null
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding confidential work instructions by default.
- Payload must not include restricted customer data, legal strategy, credentials or raw document/evidence content.
- Payload may include assigned_user_reference_id only when initial assignment is part of governed task creation, but TaskCreated is not TaskAssigned unless assignment event is emitted separately.
- Payload must not imply Permission grant, Notification delivery, workflow transition or task completion.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
task_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
matter_reference_id
order_reference_id
workflow_contract_reference_id
workflow_step_reference_id
parent_task_reference_id
assigned_user_reference_id
assigned_role_reference_id
permission_decision_reference_id
policy_decision_reference_id
notification_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal task_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- matter_reference_id must not imply Matter creation unless Matter Service emits MatterCreated.
- workflow_contract_reference_id must not imply workflow activation unless Workflow Contract Service emits its own event.
- assigned_user_reference_id must not imply Permission grant.
- notification_reference_id must not imply Notification delivery unless Notification Service emits its own event.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
TaskCreated
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

## 8.4 task_type

```text
ReviewTask
PreparationTask
FilingTask
ResponseTask
EvidenceTask
DocumentTask
CommunicationTask
ApprovalTask
MonitoringTask
RoutingTask
InternalTask
SystemTask
Other
Unknown
```

## 8.5 task_status

```text
Draft
Open
ReviewRequired
Assigned
InProgress
Blocked
Completed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 task_priority

```text
Low
Normal
High
Urgent
Critical
Unknown
```

## 8.7 task_source_type

```text
ProfessionalInput
WorkflowGenerated
MatterGenerated
OrderGenerated
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.8 reason_code

```text
TaskCreated
ProfessionalCreated
WorkflowGenerated
MatterGenerated
OrderGenerated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 TaskCreated Records Work Unit Creation

TaskCreated records that a Task reference exists.

It must not be interpreted as assignment, start, completion, workflow transition or professional execution result.

## 9.2 Task Is Not Matter

Matter Service owns professional execution container.

Task may reference Matter, but TaskCreated does not create Matter.

## 9.3 Task Is Not Workflow Contract

Workflow Contract Service defines allowed execution structure.

Task may be generated from workflow, but TaskCreated does not define or activate workflow.

## 9.4 Task Assignment Does Not Grant Permission

Assignment is not authorization.

Permission Service must evaluate allowed action separately where required.

## 9.5 TaskCreated Is Not Notification

Notification Service owns awareness intent and delivery.

TaskCreated may trigger notification intent, but it is not notification delivery.

## 9.6 AI Task Suggestion Is Not Approved Task Automatically

AI may draft or suggest tasks.

A Task becomes governed only through Task Service and applicable review rules.

## 9.7 TaskCreated Must Respect Permission and Policy

Task creation and visibility must respect Permission, Policy, matter confidentiality and organization access context.

## 9.8 TaskCreated Must Be Immutable

TaskCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Matter Service
Order Service
Workflow Contract Service
User Service
Permission Service
Policy Service
Notification Service
Communication Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Matter Service may display or aggregate Task context but must not infer Matter state automatically.
- Workflow Contract Service may validate generated Task against allowed workflow structure.
- User Service may provide participant context but must not infer authorization.
- Permission Service must evaluate task actions where required.
- Notification Service may create notification intent under policy but must not be assumed delivered.
- AI Agents may assist task planning only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Task creation trace.
```

Consumers must not:

```text
treat TaskCreated as TaskAssigned
treat TaskCreated as TaskCompleted
treat TaskCreated as Permission grant
treat TaskCreated as Workflow activation
treat TaskCreated as Notification delivery
treat TaskCreated as professional execution result
expose restricted task instructions or matter data
```

---

# 11. Relationship to Services

Producing service:

```text
Task Service produces TaskCreated after createTask succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches TaskCreated.
```

Related services:

```text
Matter Service provides execution container context.
Order Service may provide commercial request context.
Workflow Contract Service may define allowed task structure.
User Service provides account participant references.
Permission Service controls who may create, view, assign or complete Task.
Policy Service controls visibility and AI use.
Notification Service may create awareness intent.
Audit Service records accountability trace.
AI Agent Governance controls AI task planning behavior.
```

Boundary reminders:

```text
Task Service owns actionable work units.
Matter Service owns professional execution container.
Workflow Contract Service owns execution structure.
Notification Service owns awareness intent.
Permission Service owns allowed action.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /tasks/{task_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create TaskCreated directly.
- API must call Task Service createTask, which emits the event.
- API must not expose restricted task instructions, customer confidential data, matter strategy or raw document/evidence content.
- API must distinguish TaskCreated from TaskAssigned, TaskCompleted, WorkflowContractApplied, NotificationCreated and PermissionEvaluated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Task reference was created
explain that Task is not Matter, Workflow, Permission, Notification or completion
flag missing Matter/Workflow/User context for review
flag task requiring human review
suggest next governed task setup step
prepare audit-safe Task creation summary
```

AI must not:

```text
fabricate TaskCreated
rewrite TaskCreated
delete TaskCreated
treat TaskCreated as assignment, permission or completion
treat TaskCreated as Workflow activation
treat TaskCreated as Notification delivery
treat AI task suggestion as verified work plan
hide AI-assisted creation
expose restricted task, matter or customer data
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

TaskCreated is valid only if:

```text
[ ] event_name is TaskCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Task Service.
[ ] producing operation is createTask.
[ ] source_domain is Task.
[ ] source_object_type is Task.
[ ] source_object_reference_id is present.
[ ] task_reference_id is present.
[ ] source_object_reference_id equals task_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] task_type is controlled.
[ ] task_status is controlled.
[ ] task_priority is controlled.
[ ] task_source_type is controlled.
[ ] payload does not include restricted task instructions, matter strategy, customer data or raw document/evidence content unless allowed.
[ ] Matter, Workflow, Permission, Notification, assignment and completion are not implied.
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
TaskReferenceMissing
TaskReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
TaskTypeInvalid
TaskStatusInvalid
TaskPriorityInvalid
TaskSourceTypeInvalid
RestrictedFieldViolation
ConfidentialTaskPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownTaskEventError
```

Rejection rules:

```text
- Failed Task creation must not emit TaskCreated.
- Duplicate rejected Task creation must not emit TaskCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Task Service Specification
cite Task Object Specification
cite Event Service Specification
cite Matter/Workflow/User specs where references are used
use exact event_name: TaskCreated
use exact event_category: DomainEvent
validate task_reference_id
validate source_object_reference_id equals task_reference_id
validate actor_reference_id
validate controlled task_type/status/priority/source_type
validate payload contract
write tests that failed createTask does not emit TaskCreated
write tests that TaskCreated does not create Matter automatically
write tests that TaskCreated does not activate Workflow automatically
write tests that TaskCreated does not grant Permission
write tests that TaskCreated does not imply Notification delivery
write tests that TaskCreated does not imply assignment or completion
write tests that AI-assisted creation is marked where applicable
write tests that restricted task/matter/customer content is not exposed
```

Codex must not:

```text
emit TaskCreated directly from UI
treat MatterCreated as TaskCreated
treat WorkflowContractApplied as TaskCreated unless Task Service creates Task
treat TaskCreated as TaskAssigned or TaskCompleted
create Notification silently as if already delivered from TaskCreated
store raw confidential task instructions in event payload by default
allow AI to fabricate TaskCreated
use TaskCreated as command to assign, complete, notify, activate workflow or grant permission
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines TaskCreated purpose.
[ ] It defines TaskCreated meaning.
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
| 0.1.0 | Draft | Initial TaskCreated Event specification. Defines governed Task work unit creation event and separates TaskCreated from Matter, Workflow, Permission, Notification, assignment, completion and AI task suggestion. |

---

**End of Event Specification**
