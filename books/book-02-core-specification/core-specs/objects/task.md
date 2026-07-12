# Object Specification — Task

**Spec ID:** B02-OBJ-TASK  
**Spec Type:** Object  
**Object Name:** Task  
**Owning Domain:** Task  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-16 — Core Execution Primitives; B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/task.md  
**Related Object Specs:** core-specs/objects/matter.md; core-specs/objects/workflow-contract.md; core-specs/objects/event.md; core-specs/objects/notification.md; core-specs/objects/task-assignment.md; core-specs/objects/task-scope.md; core-specs/objects/task-dependency.md
**Related Service Specs:** core-specs/services/task-registration-service.md; core-specs/services/task-assignment-service.md; core-specs/services/task-status-service.md; core-specs/services/task-dependency-service.md; core-specs/services/task-workflow-service.md; core-specs/services/task-reference-validation-service.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/task-updated.md; core-specs/events/task-assigned.md; core-specs/events/task-status-changed.md; core-specs/events/task-completed.md; core-specs/events/task-blocked.md; core-specs/events/task-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/task/task-contract.md; core-specs/contracts/task/task-assignment-contract.md; core-specs/contracts/task/task-status-contract.md; core-specs/contracts/task/task-dependency-contract.md; core-specs/contracts/task/task-workflow-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Task object defines the Core-recognized actionable work unit used to coordinate concrete execution inside MarkOrbit.

It exists so that Matters, Workflow Contracts, Business Responsibility, Users, Teams, AI Agents, Documents, Evidence, Communications, Notifications, Events, Services, APIs and product consumers can consistently create, assign, track, complete, block or review work units without confusing Task with Matter, Workflow, Event, Notification, Communication or professional final decision.

Task is required before:

```text
matter execution work breakdown
task assignment
task status tracking
document request handling
evidence request handling
customer input request
agent follow-up
review and approval work
AI-assisted task suggestion
workflow-driven work unit generation
notification triggering
audit trace for work execution
```

---

# 2. Core Meaning

Task means:

```text
a Core-recognized actionable work unit with defined scope, assignee or responsibility reference, status, dependency, workflow context and execution trace.
```

Task is not:

```text
Matter
Workflow Contract
Event
Notification
Communication
Order
Document
Evidence
Business Responsibility
AI plan
Product UI checkbox only
```

Task answers:

```text
What concrete work needs to be done?
Who or what is assigned or responsible?
Which Matter, Order, Document, Evidence, Communication or Workflow context applies?
What status does the work hold?
What dependencies or blockers exist?
What completion, review or cancellation event applies?
What audit trace is required?
```

---

# 3. Object Category

Task is a Business Execution Object owned by the Task Domain.

It is the actionable work unit.

Matter is the execution container.

Workflow Contract governs allowed execution structure.

Event records meaningful occurrences.

Notification informs recipients.

Task must preserve these boundaries.

---

# 4. Architectural Position

Task sits inside Matter and under Workflow Contract control.

```text
Matter groups professional execution
        ↓
Workflow Contract defines allowed execution structure
        ↓
Task represents concrete actionable work
        ↓
User / Team / Agent / System may be assigned
        ↓
Event records task changes
        ↓
Notification informs relevant recipients
```

Task executes work units.

It does not own Matter lifecycle.

It does not define Workflow.

It does not replace Event or Notification.

---

# 5. Scope

The Task object includes:

```text
task id
task type
task title/reference
task description/reference
task status
task priority
task scope
matter reference
order reference
workflow contract reference
workflow state reference
assignee reference
responsibility reference
dependency references
due date reference
document reference
evidence reference
communication reference
notification reference
AI suggestion reference
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
task id
task type
title/reference
status
priority
matter reference
order reference
workflow contract reference
assignee reference
responsibility reference
dependency references
due date
document/evidence/communication references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Task ID. |
| task_type | enum | Yes | Yes | Controlled task type. |
| title_reference | string | Yes | Yes | Human-readable task title/reference. |
| description_reference | string | No | Yes | Description or instruction reference. |
| status | enum | Yes | Yes | Controlled Task status. |
| priority | enum | No | Yes | Task priority. |
| matter_reference_id | string | No | Yes | Related Matter reference. |
| order_reference_id | string | No | Partial | Related Order reference. |
| workflow_contract_reference_id | string | No | Yes | Governing Workflow Contract reference. |
| workflow_state_reference | string | No | Partial | Workflow state reference where applicable. |
| assignee_type | enum | No | Yes | User, Team, Agent, ServiceProvider, SystemActor, AIAgent, Unassigned. |
| assignee_reference_id | string | No | Yes | Assignee reference where applicable. |
| responsibility_reference_id | string | No | Partial | Business Responsibility reference. |
| dependency_reference_ids | array | No | Partial | Other Task references or dependency objects. |
| due_at | datetime | No | Yes | Due date/time where applicable. |
| document_reference_ids | array | No | Partial | Related Document references. |
| evidence_reference_ids | array | No | Partial | Related Evidence references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| notification_reference_ids | array | No | Partial | Related Notification references. |
| ai_suggestion_reference_id | string | No | Partial | AI suggestion reference where applicable. |
| source_reference | string | No | Yes | Intake/import/system/workflow source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 task_type

MVP controlled values:

```text
GeneralTask
ReviewTask
ApprovalTask
DocumentRequest
DocumentReview
EvidenceRequest
EvidenceReview
CustomerInputRequest
AgentFollowUp
ServiceProviderFollowUp
FilingPreparation
StatusCheck
CommunicationDraft
CommunicationReview
SystemTask
AIAssistedTask
Other
Unknown
```

## 7.2 status

Task Status is a parent-owned Controlled State Value Specification of Task, not an independent identity-bearing Core Object. Only the Task owning Service may mutate `status`; each status change requires an Event trace, and `core-specs/controlled-state-values/task-status-values.md` is the canonical semantic and transition source. AI and Product UI may display or summarize allowed status values but must not define new Task statuses or directly change them.

MVP controlled values:

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

## 7.3 priority

MVP controlled values:

```text
Low
Normal
High
Urgent
Unknown
```

## 7.4 assignee_type

MVP controlled values:

```text
User
Team
Agent
ServiceProvider
SystemActor
AIAgent
Unassigned
Unknown
```

---

# 8. Object Rules

## 8.1 Task Requires Type, Title and Status

Every Task must define:

```text
task_type
title_reference
status
```

A task without actionable title or status is not Core-valid.

## 8.2 Task Is Not Matter

Task is a work unit.

Matter is the execution container.

Task must not close, cancel or complete Matter directly.

## 8.3 Task Is Not Workflow Contract

Task may reference Workflow Contract.

Task must not define workflow states or transitions.

## 8.4 Task Is Not Event

Task changes may emit Events.

Task itself is not an Event.

## 8.5 Task Is Not Notification

Task assignment or status change may trigger Notification.

Task is not Notification.

## 8.6 Task Assignment Does Not Grant Permission

Assignee reference or responsibility reference does not grant action permission.

Permission and Policy must still be evaluated.

## 8.7 AI-Suggested Task Is Not Approved Task Automatically

AI may suggest a task.

A task becomes Core-valid only through Task Registration Service and governed review where required.

## 8.8 Task Must Be Auditable

Task-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
task creation
task assignment
task status change
task priority change
task dependency update
task completion
task cancellation
task blocker update
document/evidence/communication linkage
AI task suggestion
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Matter | Task may belong to Matter | Matter remains execution container. |
| Order | Task may support Order through Matter | Order remains commercial request. |
| Workflow Contract | Task may reference workflow | Workflow owns transition rules. |
| Business Responsibility | Task may reference responsibility | Responsibility remains accountability system. |
| User | User may be assignee | User remains account participant. |
| Agent | Agent may be assignee/collaborator | Agent remains collaborator. |
| Service Provider | Provider may be assignee/collaborator | Provider remains capability profile. |
| Document | Task may request/review Document | Document remains artifact. |
| Evidence | Task may request/review Evidence | Evidence remains proof layer. |
| Communication | Task may require communication | Communication remains message lifecycle. |
| Notification | Task may trigger Notification | Notification remains awareness intent. |
| Event | Task changes emit Events | Event remains signal. |
| AI Output | AI may suggest Task | AI Output is not approved Task. |
| Audit Record | Audit may reference Task | Audit remains accountability system. |

---

# 10. Lifecycle

Task lifecycle states:

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

Lifecycle rules may be governed by Workflow Contract.

General lifecycle examples:

```text
Draft → Open
Open → Assigned
Assigned → InProgress
InProgress → Waiting
Waiting → InProgress
InProgress → Blocked
Blocked → InProgress
InProgress → ReviewRequired
ReviewRequired → Completed
InProgress → Completed
Open → Cancelled
Assigned → Cancelled
Completed → Archived
Cancelled → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Draft → Completed without execution trace
Cancelled → InProgress without restoration/reopen service
Archived → InProgress without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Task object is created and managed through:

```text
Task Registration Service
Task Update Service
Task Assignment Service
Task Status Service
Task Dependency Service
Task Workflow Service
Task Document Link Service
Task Evidence Link Service
Task Communication Link Service
Task Reference Validation Service
Task Audit Reference Service
```

Service rules:

```text
- Services must validate task_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not close or cancel Matter directly.
- Services must not define Workflow Contract.
- Services must not grant Permission.
- AI-suggested tasks must remain draft/review-required where required.
```

---

# 12. Event Usage

Task object emits or participates in:

```text
TaskCreated
TaskUpdated
TaskAssigned
TaskUnassigned
TaskStatusChanged
TaskPriorityChanged
TaskDependencyAdded
TaskDependencyRemoved
TaskBlocked
TaskUnblocked
TaskReviewRequired
TaskCompleted
TaskCancelled
TaskArchived
TaskReferenceValidated
```

Event rules:

```text
- Task events must reference Task ID.
- Status events must preserve previous and new status.
- Assignment events must reference assignee type and reference where allowed.
- Dependency events must reference dependency object.
- AI task events must identify AI source where applicable.
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
POST /tasks/{id}/dependencies
DELETE /tasks/{id}/dependencies/{dependencyId}
POST /tasks/{id}/documents
POST /tasks/{id}/evidence
POST /tasks/{id}/communications
POST /tasks/reference/validate
```

API rules:

```text
- APIs must invoke Task Services.
- APIs must not close or cancel Matter directly.
- APIs must not define Workflow Contract.
- APIs must not grant Permission.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Task only under governed Agent Contracts.

Allowed AI use:

```text
suggest task creation
summarize task status
identify overdue or blocked tasks
suggest assignee for review
draft task instructions
identify missing document/evidence/communication links
detect task/matter/workflow mismatch
prepare task completion note for review
```

AI must not:

```text
create final task without authorized service
assign itself high-risk task without review
complete task without governed service
close or cancel Matter through task action
bypass Permission or Policy
send external communication from Task service
treat AI task suggestion as approved task automatically
```

AI Task use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Task Access Rule
Matter Access Rule
Workflow Rule
Audit Rule
Human Review Rule for high-risk assignment/completion
```

---

# 15. Validation Rules

Task object must pass:

```text
[ ] id is present and immutable.
[ ] task_type is controlled.
[ ] title_reference is present.
[ ] status is controlled.
[ ] priority is controlled where present.
[ ] assignee_type is controlled where present.
[ ] Task does not equal Matter.
[ ] Task does not define Workflow Contract.
[ ] Task is not Event or Notification.
[ ] Assignment does not grant Permission.
[ ] AI suggestion is not approved Task automatically.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite task domain spec
preserve Task / Matter boundary
preserve Task / Workflow Contract boundary
preserve Task / Event boundary
preserve Task / Notification boundary
implement only MVP fields unless task says otherwise
write tests for required title_reference
write tests for controlled task_type
write tests for controlled status
write tests for controlled assignee_type
write tests preventing Task from closing Matter directly
write tests preventing Task from defining Workflow Contract
write tests preventing AI suggestion from becoming approved Task automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full project management system beyond approved MVP
treat Task as Matter
treat Task as Workflow Contract
treat Task as Event or Notification
grant permission through assignment
complete high-risk task by AI without review
send external communication directly from Task service
allow product UI to redefine Task status
```

---

# 17. Acceptance Criteria

This Task Object Specification is accepted only if:

```text
[ ] It defines Task purpose.
[ ] It defines Task Core meaning.
[ ] It identifies Task as Business Execution Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Task object specification. Establishes Task as actionable work unit, separates Task from Matter, Workflow Contract, Event and Notification, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
