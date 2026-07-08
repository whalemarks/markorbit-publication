# Event Specification — WorkflowContractApplied

**Spec ID:** B02-EVT-WORKFLOW-CONTRACT-APPLIED  
**Spec Type:** Event  
**Event Name:** WorkflowContractApplied  
**Event File:** core-specs/events/workflow-contract-applied.md  
**Event Category:** DomainEvent  
**Owning Domain:** Workflow Contract  
**Producing Service:** core-specs/services/workflow-contract-service.md  
**Related Object Specs:** core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/notification-service.md  
**Related API Specs:** core-specs/api/workflow-contract-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/workflow-contract-applied-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

WorkflowContractApplied records that a governed Workflow Contract has been applied to a target execution context by Workflow Contract Service.

It exists so that Matter, Order, Task, Event, Notification, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that an allowed execution structure has been attached to a target object without treating that application as task creation, task assignment, workflow transition, professional completion, filing submission, approval or automation execution.

WorkflowContractApplied is required before:

```text
matter workflow structure trace
order-to-workflow preparation
allowed execution structure validation
task generation planning
workflow gate validation
AI-assisted workflow planning review
policy-controlled workflow visibility
API workflow contract reference validation
audit trace for workflow-sensitive actions
```

---

# 2. Event Meaning

WorkflowContractApplied means:

```text
a stable Workflow Contract reference has been applied to a target object under governed Workflow Contract Service operation.
```

WorkflowContractApplied does not mean:

```text
a Task has been created
a Task has been assigned
a Workflow transition has occurred
automation has executed
a filing has been submitted
a professional review has been completed
an approval has been granted
Permission has been granted
AI workflow recommendation has been accepted as final execution plan
```

WorkflowContractApplied records the application of an allowed execution structure only.

It does not execute workflow steps, create tasks automatically, grant permission or complete professional work.

---

# 3. Event Category

WorkflowContractApplied is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Workflow Contract domain.

It is not a Task event, Event execution log, Notification event or workflow transition event.

---

# 4. Event Producer

Producing service:

```text
Workflow Contract Service
```

Producing operation:

```text
applyWorkflowContract
```

Source domain:

```text
Workflow Contract
```

Source object type:

```text
WorkflowContractApplication
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Workflow Contract Service applyWorkflowContract
        ↓
Event Service record WorkflowContractApplied
```

Producer rules:

```text
- WorkflowContractApplied must be emitted only after Workflow Contract Service successfully applies the Workflow Contract to a target object.
- WorkflowContractApplied must not be emitted directly by product UI.
- WorkflowContractApplied must not be emitted directly by AI Agent outside governed service operation.
- WorkflowContractApplied must not be emitted for failed, duplicate-rejected or unauthorized application attempts.
```

---

# 5. Event Trigger

WorkflowContractApplied is triggered when:

```text
Workflow Contract Service successfully applies a Workflow Contract to a target object and commits the workflow_contract_application_reference_id.
```

Required trigger conditions:

```text
applyWorkflowContract operation completed
workflow_contract_reference_id validated
workflow_contract_application_reference_id created
target_object_type captured
target_object_reference_id validated
application_status validated
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Workflow Contract definition
Matter creation
Order creation
Task creation
Task assignment
workflow transition
notification creation
permission evaluation
policy evaluation
AI workflow suggestion
failed validation
duplicate rejected application
```

Related but separate events may include:

```text
MatterCreated
OrderCreated
TaskCreated
TaskAssigned
WorkflowTransitionRequested
WorkflowTransitionCompleted
PermissionEvaluated
PolicyEvaluated
NotificationCreated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: WorkflowContractApplied
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Workflow Contract
source_service: Workflow Contract Service
source_operation: applyWorkflowContract
source_object_type: WorkflowContractApplication
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/workflow-contract-applied-payload.md
safe_summary:
  workflow_contract_application_reference_id: string
  workflow_contract_reference_id: string
  target_object_type: string
  target_object_reference_id: string
  application_status: string
  source_type: string
restricted_fields_policy: WorkflowContractAppliedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
workflow_contract_application_reference_id: string
workflow_contract_reference_id: string
workflow_contract_version: string
application_status: string
target_object_type: string
target_object_reference_id: string
matter_reference_id: string | null
order_reference_id: string | null
initial_step_reference_id: string | null
created_task_reference_ids: list[string]
created_event_reference_ids: list[string]
applied_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding restricted workflow rule internals by default.
- Payload must not imply Task creation unless created_task_reference_ids were created by governed Task Service operations and related TaskCreated events exist.
- Payload must not imply workflow transition, approval, filing, execution completion or Permission grant.
- Payload must not expose restricted customer data, matter strategy, legal strategy or automation secrets.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
workflow_contract_application_reference_id
workflow_contract_reference_id
source_object_reference_id
target_object_type
target_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
matter_reference_id
order_reference_id
initial_step_reference_id
created_task_reference_ids
created_event_reference_ids
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal workflow_contract_application_reference_id.
- workflow_contract_reference_id must reference a valid governed Workflow Contract.
- target_object_reference_id must reference a valid target object.
- target_object_type must be controlled.
- created_task_reference_ids must not imply task assignment or completion.
- permission_decision_reference_id must not imply broad Permission grant beyond captured context.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
WorkflowContractApplied
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

## 8.4 target_object_type

```text
Matter
Order
Task
Trademark
Customer
InternalProcess
Unknown
```

## 8.5 application_status

```text
Draft
Applied
ReviewRequired
Blocked
Rejected
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 source_type

```text
ProfessionalInput
MatterGenerated
OrderGenerated
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
WorkflowContractApplied
MatterWorkflowApplied
OrderWorkflowApplied
SystemApplied
MigrationApplied
AIAssistedApplied
ReviewRequired
Blocked
Unknown
```

---

# 9. Event Rules

## 9.1 WorkflowContractApplied Records Structure Application

WorkflowContractApplied records that an allowed execution structure was applied to a target object.

It must not be interpreted as execution of workflow steps.

## 9.2 Workflow Contract Is Not Task

Task Service owns actionable work units.

WorkflowContractApplied may lead to TaskCreated events, but does not silently create or complete tasks.

## 9.3 Workflow Contract Is Not Event Execution

Event Service records occurrences.

WorkflowContractApplied is not an event bus command or runtime automation log.

## 9.4 Workflow Contract Application Does Not Grant Permission

Permission Service owns allowed action decisions.

Applying a Workflow Contract does not grant users permission to execute steps.

## 9.5 Workflow Contract Application Does Not Approve Filing

Filing or submission requires separate governed operation, professional review and applicable permission/policy checks.

## 9.6 AI Workflow Suggestion Is Not Applied Contract Automatically

AI may recommend workflow structure.

A Workflow Contract is applied only through Workflow Contract Service and applicable review rules.

## 9.7 WorkflowContractApplied Must Respect Permission and Policy

Application and visibility must respect Permission, Policy, matter confidentiality and organization access context.

## 9.8 WorkflowContractApplied Must Be Immutable

WorkflowContractApplied must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Matter Service
Order Service
Task Service
Event Service
Notification Service
Permission Service
Policy Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Matter Service may display applied workflow structure but must not infer Matter completion.
- Order Service may display workflow readiness but must not infer acceptance or payment.
- Task Service may create tasks only through governed Task Service operation.
- Notification Service may create awareness intent under policy but must not be assumed delivered.
- Permission Service must evaluate step/action execution where required.
- AI Agents may assist workflow planning only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Workflow Contract application trace.
```

Consumers must not:

```text
treat WorkflowContractApplied as TaskCreated
treat WorkflowContractApplied as TaskAssigned
treat WorkflowContractApplied as workflow transition
treat WorkflowContractApplied as Permission grant
treat WorkflowContractApplied as filing approval
treat WorkflowContractApplied as automation execution
expose restricted workflow internals or matter strategy
```

---

# 11. Relationship to Services

Producing service:

```text
Workflow Contract Service produces WorkflowContractApplied after applyWorkflowContract succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches WorkflowContractApplied.
```

Related services:

```text
Matter Service provides execution container context.
Order Service provides commercial request context.
Task Service may create work units according to applied contract.
Event Service records workflow-related occurrences.
Notification Service may create awareness intent.
Permission Service controls who may apply or execute workflow steps.
Policy Service controls visibility and AI use.
Audit Service records accountability trace.
AI Agent Governance controls AI workflow planning behavior.
```

Boundary reminders:

```text
Workflow Contract Service owns allowed execution structure.
Task Service owns actionable work units.
Matter Service owns professional execution container.
Event Service records occurrence.
Notification Service owns awareness intent.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /workflow-contract-applications/{application_id}/events
GET /matters/{matter_id}/workflow/events
POST /events/reference/validate
```

API rules:

```text
- API must not create WorkflowContractApplied directly.
- API must call Workflow Contract Service applyWorkflowContract, which emits the event.
- API must not expose restricted workflow internals, automation secrets, matter strategy or customer confidential data.
- API must distinguish WorkflowContractApplied from TaskCreated, TaskAssigned, WorkflowTransitionCompleted and NotificationCreated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Workflow Contract was applied
explain that application is not execution, task assignment, permission or completion
flag missing Matter/Order target context for review
flag workflow application requiring human review
suggest next governed task setup step
prepare audit-safe Workflow Contract application summary
```

AI must not:

```text
fabricate WorkflowContractApplied
rewrite WorkflowContractApplied
delete WorkflowContractApplied
treat WorkflowContractApplied as workflow execution
treat WorkflowContractApplied as task assignment or completion
treat WorkflowContractApplied as Permission grant
treat AI workflow suggestion as applied workflow contract
hide AI-assisted application
expose restricted workflow, matter or customer data
```

AI-assisted application requires:

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

WorkflowContractApplied is valid only if:

```text
[ ] event_name is WorkflowContractApplied.
[ ] event_category is DomainEvent.
[ ] producing service is Workflow Contract Service.
[ ] producing operation is applyWorkflowContract.
[ ] source_domain is Workflow Contract.
[ ] source_object_type is WorkflowContractApplication.
[ ] source_object_reference_id is present.
[ ] workflow_contract_application_reference_id is present.
[ ] source_object_reference_id equals workflow_contract_application_reference_id.
[ ] workflow_contract_reference_id is present and valid.
[ ] target_object_type is controlled.
[ ] target_object_reference_id is present and valid.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] application_status is controlled.
[ ] payload does not include restricted workflow internals, automation secrets, matter strategy or customer data unless allowed.
[ ] Task creation, assignment, completion, workflow transition, Permission grant, filing and automation execution are not implied.
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
WorkflowContractApplicationReferenceMissing
WorkflowContractApplicationReferenceMismatch
WorkflowContractReferenceMissing
WorkflowContractReferenceInvalid
TargetObjectTypeInvalid
TargetObjectReferenceMissing
TargetObjectReferenceInvalid
ApplicationStatusInvalid
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
RestrictedFieldViolation
ConfidentialWorkflowPayloadRejected
AutomationSecretPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownWorkflowContractEventError
```

Rejection rules:

```text
- Failed Workflow Contract application must not emit WorkflowContractApplied.
- Unauthorized application attempt must not emit WorkflowContractApplied.
- Duplicate rejected application must not emit WorkflowContractApplied unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Workflow Contract Service Specification
cite Workflow Contract Object Specification
cite Event Service Specification
cite Matter/Order/Task specs where references are used
use exact event_name: WorkflowContractApplied
use exact event_category: DomainEvent
validate workflow_contract_application_reference_id
validate source_object_reference_id equals workflow_contract_application_reference_id
validate workflow_contract_reference_id
validate target_object_type and target_object_reference_id
validate actor_reference_id
validate controlled application_status/source_type
validate payload contract
write tests that failed applyWorkflowContract does not emit WorkflowContractApplied
write tests that WorkflowContractApplied does not create Task automatically unless Task Service creates TaskCreated
write tests that WorkflowContractApplied does not assign or complete Task
write tests that WorkflowContractApplied does not grant Permission
write tests that WorkflowContractApplied does not imply filing approval or automation execution
write tests that AI-assisted application is marked where applicable
write tests that restricted workflow/matter/customer content is not exposed
```

Codex must not:

```text
emit WorkflowContractApplied directly from UI
treat Workflow Contract definition as WorkflowContractApplied
treat TaskCreated as WorkflowContractApplied
treat WorkflowContractApplied as workflow transition or automation execution
create Task, Notification or Permission silently from WorkflowContractApplied
store restricted workflow internals or automation secrets in event payload by default
allow AI to fabricate WorkflowContractApplied
use WorkflowContractApplied as command to create tasks, assign tasks, complete workflow, file application or grant permission
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines WorkflowContractApplied purpose.
[ ] It defines WorkflowContractApplied meaning.
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
| 0.1.0 | Draft | Initial WorkflowContractApplied Event specification. Defines governed Workflow Contract application event and separates WorkflowContractApplied from Task creation, assignment, completion, workflow transition, Permission grant, filing approval, automation execution and AI workflow suggestion. |

---

**End of Event Specification**
