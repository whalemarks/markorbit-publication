# Domain Specification — Task

**Spec ID:** B02-DOM-TASK  
**Spec Type:** Domain  
**Domain Name:** Task  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/task-type.md; core-specs/objects/task-status.md; core-specs/objects/task-assignment.md; core-specs/objects/task-scope.md; core-specs/objects/task-result.md; core-specs/objects/task-dependency.md  
**Related Service Specs:** core-specs/services/task-creation-service.md; core-specs/services/task-assignment-service.md; core-specs/services/task-status-service.md; core-specs/services/task-result-service.md; core-specs/services/task-dependency-service.md; core-specs/services/task-reference-validation-service.md  
**Related Event Specs:** core-specs/events/task-created.md; core-specs/events/task-assigned.md; core-specs/events/task-status-changed.md; core-specs/events/task-started.md; core-specs/events/task-completed.md; core-specs/events/task-blocked.md; core-specs/events/task-result-submitted.md; core-specs/events/task-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/task/task-contract.md; core-specs/contracts/task/task-assignment-contract.md; core-specs/contracts/task/task-status-contract.md; core-specs/contracts/task/task-result-contract.md; core-specs/contracts/task/task-dependency-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Task Domain defines the Core meaning of an actionable work unit in MarkOrbit.

It exists so that Matters, Orders, Workflow Contracts, Events, Notifications, Communications, Documents, Evidence, AI Agents and product consumers can consistently assign, track, complete, block, review and audit units of work.

Task is required before:

```text
matter execution
workflow task generation
responsibility assignment
document review work
evidence review work
classification review work
customer follow-up
agent follow-up
deadline-sensitive work
AI task suggestion
workload tracking
Codex implementation of execution workflows
```

The Task Domain is a Business Execution Domain because it translates workflow and matter context into concrete work assigned to people, teams, systems or agents.

---

# 2. Core Meaning

Task means:

```text
a Core-recognized actionable work unit with type, scope, assignee, status, dependency, result, due context and audit rules.
```

Task is not merely:

```text
a Matter
a Workflow Contract
a workflow state
an Event
a Notification
a message
a checklist item
a UI card
a calendar event
an AI suggestion
a document review result
```

Task answers:

```text
What work must be done?
Who or what is responsible?
Which Matter, Order, Workflow, Document, Evidence, Trademark or Customer context does it belong to?
What is the expected result?
What is its current status?
What dependencies or blockers exist?
What events and notifications should occur?
What audit trace is required?
```

---

# 3. Domain Category

Task is a Business Execution Domain.

Business Execution Domains provide the Core basis for:

```text
work assignment
execution tracking
responsibility routing
workflow orchestration
review work handling
deadline-sensitive work handling
AI-assisted work suggestion
operational reporting
```

Task is the work unit below Matter and Workflow Contract.

---

# 4. Architectural Position

Task sits after Workflow Contract and Matter in the Business Execution Core.

```text
Order defines commercial scope
        ↓
Matter defines professional execution container
        ↓
Workflow Contract defines allowed execution structure
        ↓
Task defines actionable work unit
        ↓
Event records meaningful changes
        ↓
Notification informs participants
        ↓
Communication carries messages
```

Task executes work.

Workflow Contract governs process.

Matter contains professional execution context.

Task does not replace Matter or Workflow Contract.

---

# 5. Scope

The Task Domain includes:

```text
task definition
task type
task status
task scope
task assignment
task owner
task participant boundary
task dependency
task blocker
task due context
task priority boundary
task result
task review boundary
task relationship to Matter
task relationship to Workflow Contract
task relationship to Document and Evidence
task relationship to Communication
task reference validation
task audit reference
task event emission
task use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Task
Task Type
Task Status
Task Scope
Task Assignment
Task Dependency
Task Result
Task Creation Service
Task Assignment Service
Task Status Service
Task Result Service
Task Dependency Service
Task Reference Validation Service
TaskCreated event
TaskAssigned event
TaskStatusChanged event
TaskStarted event
TaskCompleted event
TaskBlocked event
TaskResultSubmitted event
TaskReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Task Domain owns:

```text
Core Task definition
task scope
task status
task assignment
task dependency
task blocker
task result
task due context reference
task relationship to Matter and Workflow
task reference validation
task event emission
task reference used by execution workflows and products
```

## 6.2 Out of Boundary

The Task Domain does not own:

```text
Matter professional execution container
Workflow state model
Event infrastructure
Notification delivery lifecycle
Communication message lifecycle
Permission assignment
Policy rule definition
Review decision content
Document artifact lifecycle
Evidence proof meaning
calendar scheduling system
team capacity planning engine
project management product UI
AI Agent capability definition
```

Those responsibilities belong to:

```text
Matter Domain
Workflow Contract Domain
Event Domain
Notification Domain
Communication Domain
Permission Domain
Policy Domain
Review and Approval system
Document Domain
Evidence Domain
AI Governance
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Task is the work unit.

Matter is the execution container.

Workflow Contract defines allowed transitions.

Event records state changes.

Notification informs participants.

Communication carries messages.

Task should reference those objects, not absorb their meanings.

---

# 7. Domain Rules

## 7.1 Task Requires Scope

Every Task must have a Task Scope.

Task Scope should describe:

```text
work objective
related Matter or Workflow
target object
expected result
assignee responsibility
due context where applicable
completion criteria
```

## 7.2 Task Requires Assignment or Assignment Rule

Every active Task should have an assignee or assignment rule.

Assignee may be:

```text
User
Team
Organization Unit
System Actor
AI Agent
External Participant Reference
```

AI Agent assignment requires Agent Contract and Permission.

## 7.3 Task Does Not Replace Workflow

Task status is not workflow state.

A Task may influence Workflow transitions, but Workflow Contract governs transitions.

## 7.4 Task Result Must Be Explicit

Completed Tasks should produce a Task Result or explicit no-result reason.

Task completion without result trace is not acceptable for professional or review-sensitive work.

## 7.5 Task Must Support Blockers and Dependencies

Task may depend on other Tasks, Documents, Evidence, Customer input, Agent response, official action or Workflow state.

Dependencies must be explicit and auditable.

## 7.6 Task Must Be Auditable

Task-sensitive actions must preserve audit trace.

Audit-sensitive task actions include:

```text
task creation
task assignment
task status change
task start
task block
task unblock
task result submission
task completion
task cancellation
assignee change
AI task recommendation
AI task execution attempt
```

---

# 8. Primary Objects

The Task Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Task | Task | Must Implement | Core actionable work unit. |
| Task Type | Task | Must Implement | Controlled type of work. |
| Task Status | Task | Must Implement | Controlled status of work unit. |
| Task Scope | Task | Must Implement | Objective, target, expected result and completion criteria. |
| Task Assignment | Task / Business Responsibility | Must Implement | Responsible actor, team, system or agent assignment. |
| Task Dependency | Task | Must Implement | Dependency or prerequisite for task execution. |
| Task Blocker | Task | Must Implement | Condition preventing task progress. |
| Task Due Context | Task / Workflow | Partial Implement | Due date or due rule reference, not full deadline engine. |
| Task Result | Task | Must Implement | Result, output or completion record of Task. |
| Task Review Reference | Task / Review and Approval | Partial Implement | Review requirement or review record reference. |
| Task Audit Reference | Task / Audit | Partial Implement | Audit reference for task-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Matter | Matter | Task usually belongs to Matter. |
| Order | Order | Task may reference Order context, usually through Matter. |
| Workflow Contract | Workflow Contract | Workflow may create or depend on Task. |
| Event | Event | Task changes emit Events. |
| Notification | Notification | Task events may trigger Notifications. |
| Communication | Communication | Task may require communication. |
| Document | Document | Task may involve document work. |
| Evidence | Evidence | Task may involve evidence work. |
| User | User | User may be assignee. |
| AI Agent | AI Governance | AI Agent may be assignee if authorized. |
| Audit Record | Audit | Audit records task-sensitive actions. |

---

# 9. Primary Services

The Task Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Task Creation Service | Task | Must Implement | Create a Core Task. |
| Task Update Service | Task | Must Implement | Update controlled Task fields. |
| Task Assignment Service | Task / Business Responsibility | Must Implement | Assign or reassign Task to actor, team, system or agent. |
| Task Status Service | Task | Must Implement | Update Task Status through governed rules. |
| Task Start Service | Task | Must Implement | Mark Task as started through governed rules. |
| Task Result Service | Task | Must Implement | Submit, update or validate Task Result. |
| Task Dependency Service | Task | Must Implement | Add, remove or resolve Task dependencies. |
| Task Blocker Service | Task | Must Implement | Mark, update or resolve blockers. |
| Task Reference Validation Service | Task | Must Implement | Validate Task references used by other domains. |
| Task Audit Reference Service | Task / Audit | Partial Implement | Produce task audit reference for governed actions. |

Service rules:

```text
- Mutating Task services must emit events.
- Task services must not mutate Workflow state directly.
- Task services must not close Matter directly.
- Task assignment must respect Permission and Policy.
- AI Agent assignment must require Agent Contract.
- Completion must produce Task Result or explicit no-result reason.
```

---

# 10. Primary Events

The Task Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| TaskCreated | Task Creation Service | Must Implement | A Core Task has been created. |
| TaskUpdated | Task Update Service | Must Implement | Controlled Task fields have changed. |
| TaskAssigned | Task Assignment Service | Must Implement | Task has been assigned or reassigned. |
| TaskStatusChanged | Task Status Service | Must Implement | Task Status has changed. |
| TaskStarted | Task Start Service | Must Implement | Task execution has started. |
| TaskBlocked | Task Blocker Service | Must Implement | Task is blocked. |
| TaskUnblocked | Task Blocker Service | Must Implement | Task blocker has been resolved. |
| TaskDependencyAdded | Task Dependency Service | Must Implement | Task dependency has been added. |
| TaskDependencyResolved | Task Dependency Service | Must Implement | Task dependency has been resolved. |
| TaskResultSubmitted | Task Result Service | Must Implement | Task Result has been submitted. |
| TaskCompleted | Task Status Service / Task Result Service | Must Implement | Task has been completed. |
| TaskCancelled | Task Status Service | Partial Implement | Task has been cancelled through governed rules. |
| TaskReferenceValidated | Task Reference Validation Service | Must Implement | Task reference has been validated for governed use. |

Event rules:

```text
- Task events must reference Task.
- Assignment events must reference assignee and assignment source.
- Result events must reference Task Result.
- Dependency events must reference dependent object where applicable.
- Task events must not expose confidential document, evidence or customer details unnecessarily.
```

---

# 11. Primary Contracts

Task requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Task Contract | Task Contract | Must Implement | Defines Task fields, type, status, scope and references. |
| Task Scope Contract | Task Contract | Must Implement | Defines objective, target, expected result and completion criteria. |
| Task Assignment Contract | Task / Business Responsibility Contract | Must Implement | Defines assignee, assignment source, responsibility and status. |
| Task Status Contract | Task Contract | Must Implement | Defines controlled task status and allowed transitions. |
| Task Dependency Contract | Task Contract | Must Implement | Defines dependencies and blocker relationships. |
| Task Result Contract | Task Contract | Must Implement | Defines result submission, output and completion record. |
| Task Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for task-sensitive actions. |

Contract rules:

```text
- Task Contract must not define Workflow state model.
- Task Assignment Contract must reference authorized actor or assignment rule.
- Task Result Contract must distinguish draft, submitted, accepted and rejected results where applicable.
- Task Dependency Contract must support non-task dependencies such as Document, Evidence or Customer input.
```

---

# 12. Relationships to Other Domains

## 12.1 Matter

Task usually belongs to Matter.

Matter owns professional execution container.

Task owns actionable work unit.

## 12.2 Workflow Contract

Workflow may create Tasks or require Task completion for transition.

Workflow owns state transition rules.

Task owns work execution.

## 12.3 Event

Task changes emit Events.

Event owns event identity, payload and routing meaning.

## 12.4 Notification

Task events may trigger Notifications.

Notification owns delivery intent and notification lifecycle.

## 12.5 Communication

Tasks may require communications with Customer, Agent, Service Provider or internal team.

Communication owns message lifecycle.

## 12.6 Document and Evidence

Tasks may request, review or produce Documents and Evidence.

Document and Evidence own their own meanings.

## 12.7 Permission and Policy

Task assignment, visibility, result submission and status changes may require Permission and Policy checks.

## 12.8 Review and Approval

Some Task Results may require review or approval.

Review and Approval systems own final review decision records.

## 12.9 AI Governance

AI may suggest, draft, summarize or execute limited tasks only under Agent Contract.

AI cannot assume professional completion authority by default.

## 12.10 Audit

Audit records should include Task references for task-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Task only under governed Agent Contracts.

Allowed AI use:

```text
suggest task creation from workflow or matter context
summarize task status
identify blocked tasks
draft task result notes
prepare document or evidence review checklist
recommend next task
flag missing assignee or due context
execute low-risk system task if explicitly authorized
```

AI must not:

```text
create Task without authorized service
assign itself to Task without Agent Contract
mark professional task complete without review where required
change Workflow state directly
close Matter directly
approve Task Result by itself
send external communication without review where required
access confidential task context without Permission and Policy
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Task Object Access Rule
Task Service Access Rule
Task Event Access Rule
Matter / Workflow / Document / Evidence Access Rules
Policy Rule
Review Rule
Audit Rule
Human Review Rule for professional completion
```

---

# 14. Workflow Usage

Task participates in execution workflows.

Task-sensitive workflows may include:

```text
task-creation-workflow.md
task-assignment-workflow.md
task-execution-workflow.md
task-result-review-workflow.md
task-dependency-resolution-workflow.md
task-blocker-review-workflow.md
document-review-task-workflow.md
evidence-review-task-workflow.md
ai-task-recommendation-review-workflow.md
```

Workflow rules:

```text
- Task workflows must reference Workflow Contracts.
- Workflow may create Tasks through Task services.
- Task completion may satisfy Workflow guards.
- Task blockers should prevent dependent transitions where configured.
- AI task recommendations must not execute professional work without review.
- Task Result should be reviewed where professional or external use is involved.
```

---

# 15. API Usage

Task APIs expose task creation, assignment, status, result, dependency and blocker functions through governed services.

Potential MVP APIs:

```text
POST /tasks
GET /tasks/{id}
PATCH /tasks/{id}
POST /tasks/{id}/assignments
POST /tasks/{id}/status
POST /tasks/{id}/start
POST /tasks/{id}/results
POST /tasks/{id}/dependencies
POST /tasks/{id}/blockers
POST /tasks/reference/validate
```

Potential partial APIs:

```text
POST /tasks/{id}/cancel
POST /tasks/{id}/review
GET /tasks/{id}/audit-reference
POST /tasks/{id}/ai-draft-result
```

API rules:

```text
- APIs must invoke Task Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not mutate Workflow state directly.
- APIs must not close Matter directly.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Client Portal
Partner Center
Service Platform
Reporting consumers
Admin workbench
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced workload analytics
SLA products
Calendar integrations
Automation products
```

Product rule:

```text
Products consume Task.
Products do not redefine Task.
```

---

# 17. MVP Scope

Task is a Phase 3 / Wave 3 Must Implement domain.

MVP includes:

```text
Task
Task Type
Task Status
Task Scope
Task Assignment
Task Dependency
Task Blocker
Task Result
Task Creation Service
Task Update Service
Task Assignment Service
Task Status Service
Task Start Service
Task Result Service
Task Dependency Service
Task Blocker Service
Task Reference Validation Service
TaskCreated event
TaskUpdated event
TaskAssigned event
TaskStatusChanged event
TaskStarted event
TaskBlocked event
TaskUnblocked event
TaskDependencyAdded event
TaskDependencyResolved event
TaskResultSubmitted event
TaskCompleted event
TaskReferenceValidated event
basic task metadata validation
source traceability to Matter, Workflow, Event, Notification, Document, Evidence and AI systems
```

MVP should support:

```text
basic task creation
task assignment
task status
task dependencies
task blockers
task results
workflow-created tasks
AI-assisted task recommendation with human review
```

MVP does not require full project management suite, calendar scheduling, capacity planning or SLA automation.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full project management suite
capacity planning engine
calendar scheduling integration
SLA automation
automatic workload balancing
task marketplace
complex recurring task templates
advanced task analytics
multi-agent autonomous task execution
external task system synchronization
field-level task permissions
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Task should use stable immutable ID.
Task Scope should be explicit.
Task Status should use controlled values.
Task Assignment should reference User, Team, System Actor or AI Agent through approved contracts.
Task Dependency should support Task and non-Task dependencies.
Task Result should be required for completion unless explicit no-result reason exists.
AI-generated Task Results should remain draft/recommendation output until reviewed where needed.
```

Suggested Task Status values:

```text
Draft
Open
Assigned
InProgress
Blocked
Waiting
ReviewRequired
ResultSubmitted
Completed
Cancelled
Archived
```

MVP controlled Task Status values:

```text
Draft
Open
Assigned
InProgress
Blocked
Waiting
ReviewRequired
ResultSubmitted
Completed
Cancelled
Archived
```

Suggested Task Type values:

```text
DocumentReview
EvidenceReview
ClassificationReview
TrademarkStatusCheck
CustomerFollowUp
AgentFollowUp
OfficeActionReview
FilingPreparation
OrderReview
MatterReview
InternalApproval
AIReview
GeneralExecution
```

MVP controlled Task Type values:

```text
DocumentReview
EvidenceReview
ClassificationReview
TrademarkStatusCheck
CustomerFollowUp
AgentFollowUp
FilingPreparation
OrderReview
MatterReview
GeneralExecution
```

Do not treat a UI card as Core Task meaning.

---

# 20. Codex Implementation Notes

Codex may implement Task only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Task / Matter boundary
preserve Task / Workflow boundary
preserve Task / Event / Notification boundaries
preserve Task / Document / Evidence boundaries
implement only MVP scope unless task says otherwise
write tests for task creation
write tests for task assignment
write tests for task status update
write tests for task dependency and blocker behavior
write tests for task result submission
write tests preventing Task from mutating Workflow state directly
write tests preventing Task from closing Matter directly
write tests preventing AI from marking professional task complete without review
```

Codex must not:

```text
invent full project management suite in MVP
invent workflow states inside Task
invent event storage inside Task
invent notification delivery lifecycle inside Task
close Matter from Task service directly
execute high-risk AI tasks without Agent Contract and review
treat UI card as Task architecture
allow product UI to redefine Task status
```

---

# 21. Validation Rules

Task Domain must pass the following checks.

```text
[ ] Task is classified as Business Execution Domain.
[ ] Task is counted within the 26 baseline Core Domains.
[ ] Task does not change the baseline Core Domain Map.
[ ] Task has MVP Phase 3 / Wave 3 classification.
[ ] Task has MVP Depth = Must Implement.
[ ] Task defines Core meaning.
[ ] Task boundary excludes Matter execution container meaning.
[ ] Task boundary excludes Workflow state model.
[ ] Task boundary excludes Event and Notification infrastructure.
[ ] Task boundary excludes Document and Evidence meanings.
[ ] Task owns Task object.
[ ] Task defines Task Scope.
[ ] Task defines Task Assignment.
[ ] Task defines Task Status.
[ ] Task defines Task Dependency.
[ ] Task defines Task Result.
[ ] Task lists primary services.
[ ] Mutating Task services emit events.
[ ] Task lists primary events.
[ ] Task defines contract requirements.
[ ] Task defines AI Agent usage constraints.
[ ] Task defines workflow usage constraints.
[ ] Task defines API usage constraints.
[ ] Task defines product consumers.
[ ] Task defines MVP and deferred scope.
[ ] Task defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Task into Matter
turn Task into Workflow
turn Task into Event
turn Task into Notification
turn Task into Communication
turn Task into Document or Evidence
turn Task into full project management suite
turn Task into calendar scheduling system
turn Task into SLA engine
mutate Workflow state directly from Task
close Matter directly from Task
treat AI suggestion as completed professional work
allow product UI to redefine Task meaning
allow Codex to define new task architecture
```

---

# 23. Acceptance Criteria

This Task Domain Specification is accepted only if:

```text
[ ] It defines Task purpose.
[ ] It defines Task Core meaning.
[ ] It identifies Task as Business Execution Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Matter, Order, Workflow Contract, Event, Notification, Communication, Document, Evidence, Permission, Policy, Review, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Task Domain specification. Establishes Task as Phase 3 Business Execution Domain, defines Task, Scope, Assignment, Status, Dependency, Blocker, Result, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
