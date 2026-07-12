# Service Specification — Task Service

**Spec ID:** B02-SVC-TASK-SERVICE  
**Spec Type:** Service  
**Service Name:** Task Service  
**Owning Domain:** Task  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-16 — Core Execution Primitives; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/task.md  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/workflow-contract.md; core-specs/objects/event.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/event-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/task-updated.md; core-specs/events/task-status-changed.md; core-specs/events/task-assigned.md; core-specs/events/task-completed.md; core-specs/events/task-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/task/task-contract.md; core-specs/contracts/task/task-reference-contract.md; core-specs/contracts/task/task-assignment-contract.md; core-specs/contracts/task/task-status-contract.md; core-specs/contracts/task/task-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Task Service defines the Core service boundary for creating, updating, validating, assigning, scheduling and managing Task objects.

It exists so that Matter, Order, Workflow Contract, User, Permission, Policy, Event, Notification, Communication, AI Agents, APIs and product consumers can consistently reference actionable work units without confusing Task with Matter, Workflow Contract, Event, Notification, approval, user permission or product checklist item.

Task Service is required before:

```text
matter task creation
workflow-driven work breakdown
task assignment
task status tracking
task deadline/reference handling
task completion validation
task-to-event emission
AI-assisted task suggestion
professional work queue management
audit trace for task-sensitive actions
```

---

# 2. Core Meaning

Task Service means:

```text
the Core service that manages actionable work units, including assignment, status, priority, due context, workflow relationship, matter relationship and completion trace.
```

Task Service does not mean:

```text
Matter Service
Workflow Contract Service
Event Service
Notification Service
Permission Service
approval system
automation engine by itself
product UI checklist by itself
```

Task Service answers:

```text
Does this Task exist?
Which Matter, Order or Workflow Contract does it relate to?
Who is assigned?
What work action is required?
What status, priority or due context applies?
Can the Task be completed, cancelled, reassigned or reopened?
Can another domain safely reference this Task?
What audit trace is required?
```

---

# 3. Service Category

Task Service is a Business Execution Core Service.

It manages actionable work units.

It does not own Matter lifecycle.

It does not define Workflow Contract transitions.

It does not grant permission.

It does not record Event as source of truth by itself.

---

# 4. Architectural Position

Task Service sits inside execution flow after Matter and Workflow Contract.

```text
Order records commercial request
        ↓
Matter creates execution container
        ↓
Workflow Contract defines allowed execution structure
        ↓
Task Service creates actionable work unit
        ↓
User / AI Agent / System performs or assists work
        ↓
Event Service records meaningful occurrence
        ↓
Notification may alert participants
```

Task executes work.

Matter contains work.

Workflow Contract governs allowed structure.

Event records what happened.

---

# 5. Scope

Task Service includes:

```text
task creation
task update
task status management
task assignment
task reassignment
task priority management
task due context management
task matter linkage
task workflow linkage
task dependency linkage
task completion validation
task reference validation
task audit trace
task event emission
```

MVP scope includes:

```text
create task
get task
update task metadata
change task status
assign task
reassign task
complete task
cancel task
reopen task
link task to matter
link task to workflow contract
validate task reference
emit task events
```

Deferred scope includes:

```text
full project management system
resource capacity planning
automatic scheduling engine
advanced SLA engine
time tracking
task billing
kanban analytics
complex dependency graph engine
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createTask | Create Task object | Yes | TaskCreated |
| getTask | Retrieve Task by ID | Yes | No |
| updateTask | Update governed metadata | Yes | TaskUpdated |
| changeTaskStatus | Change Task lifecycle status | Yes | TaskStatusChanged |
| assignTask | Assign Task to user/actor | Yes | TaskAssigned |
| reassignTask | Reassign Task | Yes | TaskReassigned |
| unassignTask | Remove assignment | Partial | TaskUnassigned |
| linkTaskMatter | Link Task to Matter | Yes | TaskMatterLinked |
| linkTaskWorkflowContract | Link Task to Workflow Contract | Yes | TaskWorkflowContractLinked |
| linkTaskDependency | Link task dependency | Partial | TaskDependencyLinked |
| completeTask | Complete Task | Yes | TaskCompleted |
| cancelTask | Cancel Task | Yes | TaskCancelled |
| reopenTask | Reopen Task | Partial | TaskReopened |
| validateTaskReference | Validate whether Task can be referenced | Yes | TaskReferenceValidated |
| archiveTask | Archive Task reference | Partial | TaskArchived |

---

# 7. Inputs

Task Service accepts:

```text
task_type
task_title_reference
task_description_reference
status
priority
assigned_actor_reference_id
assigned_actor_type
matter_reference_id
order_reference_id
workflow_contract_reference_id
workflow_state_reference
dependency_task_reference_ids
due_reference
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
task_type
task_title_reference
status
source_reference
actor_context
```

Required for assignment:

```text
task_reference_id
assigned_actor_reference_id
assigned_actor_type
assignment_type
actor_context
```

Required for completion:

```text
task_reference_id
completion_context
actor_context
request_context
```

Required for validation:

```text
task_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Task Service returns:

```text
Task object
Task reference
Task validation result
Task assignment result
Task status result
Task completion result
Task dependency result
Task event reference
error result
```

Validation output must include:

```text
is_valid
task_reference_id
task_type
status
assigned_actor_hint where applicable
matter_reference_hint where applicable
workflow_contract_reference_hint where applicable
reason_code
policy_hint where applicable
```

Completion output must include:

```text
completed
task_reference_id
next_status
event_reference_id where emitted
review_required
reason_code
```

Validation output must not expose confidential matter, document, evidence or customer data unnecessarily.

---

# 9. Controlled Values

## 9.1 task_type

```text
IntakeTask
ReviewTask
DraftingTask
FilingTask
OfficialResponseTask
CustomerFollowUpTask
AgentFollowUpTask
DocumentTask
EvidenceTask
ApprovalTask
QualityCheckTask
SystemTask
AITask
GeneralTask
Unknown
```

## 9.2 status

Consumed canonical values from [Task Status Values](../controlled-state-values/task-status-values.md):

```text
Draft
Open
Assigned
InProgress
Waiting
Blocked
ReviewRequired
Completed
Cancelled
Archived
DeletedReferenceOnly
```

The Controlled State Value Specification [Task Status Values](../controlled-state-values/task-status-values.md) is the canonical source for legal Task status values and transition semantics. Task owns current state truth. Task Service validates and performs mutation. The Service must not define an alternate active status list.

### 9.2.1 Reopen Compatibility Note

`Reopened` is an operation/Event concept, not a Task status. Reopen is a governed operation that moves `Completed -> Open` or `Cancelled -> Open` and requires actor, permission, policy, reopen reason, prior status, new status `Open`, audit context, `TaskStatusChanged` trace, `TaskReopened` trace and Workflow Contract validation when applicable. Do not record only `TaskReopened` without updating to canonical `Open`.

## 9.3 priority

```text
Low
Normal
High
Urgent
Critical
Unknown
```

## 9.4 assigned_actor_type

```text
User
Identity
AIAgent
System
ExternalActor
Unassigned
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Blocked
Cancelled
Completed
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Task Is Actionable Work Unit

Task Service manages concrete work units.

A Task must represent work that can be assigned, tracked or completed.

## 10.2 Task Is Not Matter

Task may belong to Matter.

Matter Service owns execution container.

## 10.3 Task Is Not Workflow Contract

Task may be governed by Workflow Contract.

Workflow Contract Service owns allowed states/transitions/guards.

## 10.4 Task Is Not Event

Task status changes may emit Events.

Event Service records meaningful occurrences.

## 10.5 Task Assignment Does Not Grant Permission

Assignment alone does not authorize action.

Permission Service must evaluate whether assigned actor may perform the action.

## 10.6 Task Completion Must Respect Workflow and Policy

Task completion may require Workflow Contract validation, Permission, Policy, review, documents or evidence.

## 10.7 AI-Suggested Task Is Not Active Task Automatically

AI may suggest tasks.

Task creation or assignment must use Task Service and authorized context.

## 10.8 Task Changes Must Be Auditable

Task-sensitive operations must preserve actor, source, assignment, status transition, completion context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Matter Service | Task may belong to Matter | Matter owns execution container. |
| Order Service | Task may relate to Order | Order owns commercial request. |
| Workflow Contract Service | Task may be governed by Workflow | Workflow Contract owns allowed structure. |
| User Service | User may be assignee | User owns account participant. |
| Identity Service | Identity may be actor reference | Identity owns actor recognition. |
| Permission Service | Checks action authorization | Permission grants action. |
| Policy Service | Checks contextual constraints | Policy constrains action. |
| Event Service | Records task events | Event records occurrence. |
| Notification Service | May notify assigned actor | Notification owns awareness intent. |
| Communication Service | Task may require communication | Communication owns message lifecycle. |
| AI Agent Governance | AI may suggest/assist | Agent Contract governs AI use. |
| Audit Service | Records Task-sensitive action | Audit owns accountability trail. |

---

# 12. Event Usage

Task Service emits:

```text
TaskCreated
TaskUpdated
TaskStatusChanged
TaskAssigned
TaskReassigned
TaskUnassigned
TaskMatterLinked
TaskWorkflowContractLinked
TaskDependencyLinked
TaskBlocked
TaskCompleted
TaskCancelled
TaskReopened
TaskArchived
TaskReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Status events must preserve previous and next status.
- Assignment events must reference assigned actor safely.
- Completion events must preserve completion context where allowed.
- Workflow-governed status changes must preserve workflow contract reference.
- AI-suggested task events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /tasks
GET /tasks/{id}
PATCH /tasks/{id}
POST /tasks/{id}/status
POST /tasks/{id}/assign
POST /tasks/{id}/reassign
POST /tasks/{id}/unassign
POST /tasks/{id}/matters
POST /tasks/{id}/workflow-contract
POST /tasks/{id}/dependencies
POST /tasks/{id}/complete
POST /tasks/{id}/cancel
POST /tasks/{id}/reopen
POST /tasks/reference/validate
```

API rules:

```text
- APIs must invoke Task Service operations.
- APIs must not grant Permission from assignment.
- APIs must not bypass Workflow Contract validation.
- APIs must not record final Event directly except through Event Service.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Task Service only under governed Agent Contracts.

Allowed AI use:

```text
suggest tasks from Matter or Workflow context
summarize task list
identify blocked or overdue tasks
draft task description
recommend assignee for review
prepare completion checklist
flag workflow/task mismatch
suggest next task after completion for review
```

AI must not:

```text
create active Task without authorized service
assign Task without authorized service
complete or cancel Task without authorization
grant permission through assignment
bypass Workflow Contract or Policy
create external Communication or filing action directly from Task
expose restricted Matter, Document or Evidence data
```

AI Task use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Task Access Rule
Matter Access Rule where applicable
Workflow Rule
User/Identity Access Rule for assignment
Audit Rule
Human Review Rule for high-risk or external-facing tasks
```

---

# 15. Validation Rules

Task Service must enforce:

```text
[ ] task_type is controlled.
[ ] status is controlled.
[ ] priority is controlled.
[ ] assigned_actor_type is controlled.
[ ] createTask requires task_title_reference.
[ ] createTask produces stable immutable Task ID.
[ ] updateTask does not mutate immutable ID.
[ ] changeTaskStatus follows allowed lifecycle.
[ ] assignTask references valid actor where required.
[ ] assignment does not grant Permission.
[ ] completeTask respects Workflow Contract, Permission and Policy where applicable.
[ ] validateTaskReference rejects missing, cancelled, archived or deleted-reference tasks where not allowed.
[ ] AI suggestion does not become active Task automatically.
[ ] Task Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Task Service should return controlled errors:

```text
TaskNotFound
InvalidTaskType
InvalidTaskStatus
InvalidTaskTransition
InvalidTaskPriority
InvalidTaskReference
TaskTitleRequired
InvalidAssignedActor
AssignmentRequired
TaskBlocked
TaskCancelled
TaskAlreadyCompleted
WorkflowContractNotFound
WorkflowTransitionNotAllowed
PermissionRequired
PolicyRestricted
ReviewRequired
AuditContextMissing
UnknownTaskError
```

Errors must be safe for product display and API consumption.

Sensitive Matter, Customer, Document, Evidence or professional strategy information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite task domain spec
cite task object spec
cite matter and workflow-contract specs where relevant
preserve Task / Matter boundary
preserve Task / Workflow Contract boundary
preserve Task / Event boundary
preserve Task / Permission boundary
implement only Phase 3 MVP operations unless task says otherwise
write tests for createTask requiring task_title_reference
write tests for controlled task_type
write tests for controlled status and priority
write tests preventing assignment from granting Permission
write tests preventing AI suggestion from becoming active Task automatically
write tests preventing Task Service from bypassing Workflow Contract
write tests preventing Task Service from replacing Event Service
write tests for event emission on mutation
```

Codex must not:

```text
invent full project management system inside Task Service
treat Task as Matter
treat Task as Workflow Contract
treat Task as Event
grant Permission through assignment
complete Task without required workflow/policy validation
create external filing or communication actions directly
allow AI to complete/cancel/assign Task without authorization
allow product UI to redefine Task status
```

---

# 18. Acceptance Criteria

This Task Service Specification is accepted only if:

```text
[ ] It defines Task Service purpose.
[ ] It defines Task Service Core meaning.
[ ] It identifies Task Service as Business Execution Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Task Service specification. Establishes Task Service as actionable work unit service, separates Task from Matter, Workflow Contract, Event, Notification and Permission, and defines Phase 3 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
