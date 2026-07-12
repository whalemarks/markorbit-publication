# Service Specification — Workflow Contract Service

**Spec ID:** B02-SVC-WORKFLOW-CONTRACT-SERVICE  
**Spec Type:** Service  
**Service Name:** Workflow Contract Service  
**Owning Domain:** Workflow Contract  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-16 — Core Execution Primitives; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/workflow-contract.md  
**Related Object Specs:** core-specs/objects/workflow-contract.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md  
**Related Event Specs:** core-specs/events/workflow-contract-created.md; core-specs/events/workflow-contract-updated.md; core-specs/events/workflow-contract-status-changed.md; core-specs/events/workflow-transition-validated.md; core-specs/events/workflow-transition-blocked.md; core-specs/events/workflow-contract-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/workflow-contract/workflow-contract.md; core-specs/contracts/workflow-contract/workflow-state-contract.md; core-specs/contracts/workflow-contract/workflow-transition-contract.md; core-specs/contracts/workflow-contract/workflow-guard-contract.md; core-specs/contracts/workflow-contract/workflow-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Workflow Contract Service defines the Core service boundary for creating, updating, validating and managing Workflow Contract objects and their allowed state/transition structures.

It exists so that Matter, Order, Task, Event, Policy, Permission, AI Agents, APIs and product consumers can consistently reference governed execution structures without confusing Workflow Contract with Task execution, Event recording, Matter status list, product UI board, automation engine or workflow runtime implementation.

Workflow Contract Service is required before:

```text
matter workflow governance
allowed state definition
allowed transition validation
workflow guard validation
task creation rules
event emission contract
review and approval requirement enforcement
product status normalization
AI-assisted workflow explanation
audit trace for workflow-sensitive actions
```

---

# 2. Core Meaning

Workflow Contract Service means:

```text
the Core service that manages allowed execution structures, states, transitions, guards and validation rules for workflow-governed business execution.
```

Workflow Contract Service does not mean:

```text
Task Service
Matter Service
Event Service
automation engine
runtime workflow orchestrator
product UI status board
approval system by itself
BPMN engine by itself
```

Workflow Contract Service answers:

```text
Does this Workflow Contract exist?
Which states are allowed?
Which transitions are allowed?
Which guards, permissions, policies, reviews or events apply?
Can a Matter, Order or Task use this contract?
Is a requested transition valid, blocked or review-required?
Can another domain safely reference this Workflow Contract?
What audit trace is required?
```

---

# 3. Service Category

Workflow Contract Service is a Business Execution Core Service.

It manages execution structure contracts.

It does not execute work.

It does not record events by itself.

It does not replace Task, Matter, Policy or Approval services.

---

# 4. Architectural Position

Workflow Contract Service sits between execution container and actionable work.

```text
Order creates commercial request
        ↓
Matter creates execution container
        ↓
Workflow Contract Service provides allowed execution structure
        ↓
Task Service creates actionable work units
        ↓
Event Service records meaningful occurrences
        ↓
Policy and Permission guard allowed actions
```

Workflow Contract defines structure.

Task performs work.

Event records what happened.

Matter holds execution context.

---

# 5. Scope

Workflow Contract Service includes:

```text
workflow contract creation
workflow contract update
workflow contract status management
state definition management
transition definition management
guard definition management
transition validation
workflow reference validation
workflow applicability validation
workflow audit trace
workflow event emission
```

MVP scope includes:

```text
create workflow contract
get workflow contract
update workflow contract metadata
change workflow contract status
define states
define transitions
define guards
validate transition
validate workflow contract reference
validate applicability to matter/order/task context
emit workflow contract events
```

Deferred scope includes:

```text
full workflow runtime engine
visual workflow designer
BPMN import/export
automatic task orchestration engine
advanced SLA engine
complex parallel workflow execution
external workflow system sync
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createWorkflowContract | Create Workflow Contract object | Yes | WorkflowContractCreated |
| getWorkflowContract | Retrieve Workflow Contract by ID | Yes | No |
| updateWorkflowContract | Update governed metadata | Yes | WorkflowContractUpdated |
| changeWorkflowContractStatus | Change lifecycle status | Yes | WorkflowContractStatusChanged |
| defineWorkflowState | Add/update allowed state definition | Yes | WorkflowStateDefined |
| defineWorkflowTransition | Add/update allowed transition definition | Yes | WorkflowTransitionDefined |
| defineWorkflowGuard | Add/update transition guard | Yes | WorkflowGuardDefined |
| validateWorkflowTransition | Validate requested transition | Yes | WorkflowTransitionValidated / WorkflowTransitionBlocked |
| validateWorkflowApplicability | Validate contract may govern target context | Yes | WorkflowApplicabilityValidated |
| validateWorkflowContractReference | Validate whether contract can be referenced | Yes | WorkflowContractReferenceValidated |
| archiveWorkflowContract | Archive contract reference | Partial | WorkflowContractArchived |

---

# 7. Inputs

Workflow Contract Service accepts:

```text
workflow_contract_type
name_reference
status
applicable_domain
applicable_object_type
state_definitions
transition_definitions
guard_definitions
permission_reference_ids
policy_reference_ids
review_requirement_reference_ids
event_requirement_references
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
workflow_contract_type
name_reference
status
applicable_domain
applicable_object_type
state_definitions
transition_definitions
source_reference
actor_context
```

Required for transition validation:

```text
workflow_contract_reference_id
current_state
requested_state
target_object_type
target_object_reference_id
actor_context
request_context
```

Required for reference validation:

```text
workflow_contract_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Workflow Contract Service returns:

```text
Workflow Contract object
Workflow Contract reference
Workflow transition validation result
Workflow applicability validation result
Workflow status result
Workflow contract event reference
error result
```

Transition validation output must include:

```text
is_allowed
workflow_contract_reference_id
current_state
requested_state
decision
reason_code
permission_required
policy_required
review_required
event_required
blocked_by_guard_reference where applicable
```

Validation output must not expose restricted policy, permission or internal workflow rule details unnecessarily.

---

# 9. Controlled Values

## 9.1 workflow_contract_type

```text
MatterWorkflow
OrderWorkflow
TaskWorkflow
DocumentWorkflow
EvidenceWorkflow
CommunicationWorkflow
ReviewWorkflow
ApprovalWorkflow
GeneralWorkflow
Unknown
```

## 9.2 status

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

## 9.3 transition_decision

```text
Allowed
Denied
Blocked
ReviewRequired
ApprovalRequired
PermissionRequired
PolicyRequired
InvalidTransition
Unknown
```

## 9.4 guard_type

```text
PermissionGuard
PolicyGuard
StateGuard
ReviewGuard
ApprovalGuard
DocumentGuard
EvidenceGuard
EventGuard
TimeGuard
ExternalGuard
Unknown
```

## 9.5 applicability_result

```text
Applicable
NotApplicable
ReviewRequired
Deprecated
Archived
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Workflow Contract Defines Allowed Structure

Workflow Contract Service defines allowed states, transitions and guards.

It must not execute work by itself.

## 10.2 Workflow Contract Is Not Task

Task Service owns actionable work units.

Workflow Contract may define when tasks may be created, required or completed.

## 10.3 Workflow Contract Is Not Event

Event Service records meaningful occurrences.

Workflow Contract may require events but must not replace Event Service.

## 10.4 Workflow Contract Is Not Matter Status List

Matter may use Workflow Contract.

Product UI status lists must consume Workflow Contract and not redefine it.

## 10.5 Workflow Contract Does Not Bypass Permission or Policy

Transitions may require Permission and Policy checks.

Workflow Contract validation must not grant permission or ignore policy.

## 10.6 Workflow Contract May Require Review or Approval

Workflow Contract may output review_required or approval_required.

Review/Approval execution is handled by relevant services or governed workflows.

## 10.7 Workflow Contract Changes Must Be Auditable

Workflow-sensitive operations must preserve actor, source, request context, state/transition diff and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Matter Service | Matter may reference Workflow Contract | Matter owns execution container. |
| Order Service | Order may use workflow contract | Order owns commercial request. |
| Task Service | Task behavior may be governed | Task owns work unit. |
| Event Service | Required events may be emitted downstream | Event records occurrence. |
| Permission Service | Guards may require permission | Permission grants action. |
| Policy Service | Guards may require policy | Policy constrains context. |
| Document Service | Guards may require documents | Document owns artifact lifecycle. |
| Evidence Service | Guards may require evidence | Evidence owns proof layer. |
| AI Agent Governance | AI may explain/suggest | Agent Contract governs AI use. |
| Audit Service | Records workflow-sensitive action | Audit owns accountability trail. |

---

# 12. Event Usage

Workflow Contract Service emits:

```text
WorkflowContractCreated
WorkflowContractUpdated
WorkflowContractStatusChanged
WorkflowStateDefined
WorkflowTransitionDefined
WorkflowGuardDefined
WorkflowTransitionValidated
WorkflowTransitionBlocked
WorkflowApplicabilityValidated
WorkflowContractArchived
WorkflowContractReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Transition validation events may be emitted where audit requires.
- Blocked transition events should preserve reason code where allowed.
- Guard definition events must preserve guard type.
- Events must not expose restricted policy/permission rule internals unnecessarily.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /workflow-contracts
GET /workflow-contracts/{id}
PATCH /workflow-contracts/{id}
POST /workflow-contracts/{id}/status
POST /workflow-contracts/{id}/states
POST /workflow-contracts/{id}/transitions
POST /workflow-contracts/{id}/guards
POST /workflow-contracts/{id}/transitions/validate
POST /workflow-contracts/{id}/applicability/validate
POST /workflow-contracts/reference/validate
```

API rules:

```text
- APIs must invoke Workflow Contract Service operations.
- APIs must not execute Task work directly.
- APIs must not record Event directly except through Event Service.
- APIs must not bypass Permission or Policy.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Workflow Contract Service only under governed Agent Contracts.

Allowed AI use:

```text
explain workflow states and transitions
suggest next allowed transition for review
identify invalid status transition
flag missing guard, event or review requirement
summarize workflow contract for product or professional use
draft workflow contract proposal for human review
```

AI must not:

```text
execute transition without authorized service
bypass Permission or Policy
create final Workflow Contract without review where required
rewrite workflow guards silently
treat product UI status list as contract truth
close Matter or Task directly
alter Workflow Contract status without authorized service
```

AI Workflow Contract use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Workflow Contract Access Rule
Matter/Task Access Rule where applicable
Audit Rule
Human Review Rule for contract creation, guard changes and high-risk transitions
```

---

# 15. Validation Rules

Workflow Contract Service must enforce:

```text
[ ] workflow_contract_type is controlled.
[ ] status is controlled.
[ ] createWorkflowContract requires name_reference.
[ ] createWorkflowContract requires applicable_domain and applicable_object_type.
[ ] createWorkflowContract requires state_definitions and transition_definitions.
[ ] createWorkflowContract produces stable immutable Workflow Contract ID.
[ ] updateWorkflowContract does not mutate immutable ID.
[ ] changeWorkflowContractStatus follows allowed lifecycle.
[ ] validateWorkflowTransition rejects undefined current/requested state pairs.
[ ] validateWorkflowTransition distinguishes Allowed, Denied, ReviewRequired, ApprovalRequired, PermissionRequired and PolicyRequired.
[ ] Workflow Contract Service does not execute Task or Matter work.
[ ] Workflow Contract Service does not replace Event Service.
[ ] Workflow Contract Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Workflow Contract Service should return controlled errors:

```text
WorkflowContractNotFound
InvalidWorkflowContractType
InvalidWorkflowContractStatus
InvalidWorkflowContractTransition
WorkflowContractNameRequired
ApplicableDomainRequired
ApplicableObjectTypeRequired
StateDefinitionsRequired
TransitionDefinitionsRequired
InvalidStateDefinition
InvalidTransitionDefinition
InvalidGuardDefinition
InvalidWorkflowTransition
TransitionBlocked
PermissionRequired
PolicyRequired
ReviewRequired
ApprovalRequired
DeprecatedWorkflowContract
ArchivedWorkflowContract
AuditContextMissing
UnknownWorkflowContractError
```

Errors must be safe for product display and API consumption.

Restricted policy, permission or internal workflow logic must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite workflow-contract domain spec
cite workflow-contract object spec
cite matter, task, event, permission and policy specs where relevant
preserve Workflow Contract / Task boundary
preserve Workflow Contract / Matter boundary
preserve Workflow Contract / Event boundary
preserve Workflow Contract / Permission / Policy boundaries
implement only Phase 3 MVP operations unless task says otherwise
write tests for createWorkflowContract requiring state_definitions
write tests for createWorkflowContract requiring transition_definitions
write tests for controlled workflow_contract_type
write tests for controlled status
write tests preventing undefined transitions
write tests preventing Workflow Contract Service from executing Task/Matter work
write tests preventing Workflow Contract Service from replacing Event Service
write tests for PermissionRequired and PolicyRequired outputs
write tests for event emission on mutation
```

Codex must not:

```text
invent full workflow runtime engine inside Workflow Contract Service
treat Workflow Contract as Task
treat Workflow Contract as Matter
treat Workflow Contract as Event
let product UI redefine contract states
bypass Permission or Policy during transition validation
execute external actions directly
allow AI to silently rewrite workflow guards
allow product UI to redefine Workflow Contract status
```

---

# 18. Acceptance Criteria

This Workflow Contract Service Specification is accepted only if:

```text
[ ] It defines Workflow Contract Service purpose.
[ ] It defines Workflow Contract Service Core meaning.
[ ] It identifies Workflow Contract Service as Business Execution Core Service.
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
| 0.1.0 | Draft | Initial Workflow Contract Service specification. Establishes Workflow Contract Service as allowed execution structure service, separates Workflow Contract from Task, Matter, Event, UI status board and runtime automation, and defines Phase 3 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**


## PUB-TASK-B02-002 Transition Decision Vocabulary

`validateWorkflowTransition` must use `Allowed`, `Denied`, `Blocked`, `ReviewRequired`, `ApprovalRequired`, `PermissionRequired`, `PolicyRequired`, `InvalidState`, `InvalidTransition`, and `Unknown` as the active canonical decision vocabulary from `core-specs/workflows/components/workflow-transition-definition.md`. Historical compatibility mapping is maintained only in the component specification. Workflow Contract Service validates structure and transitions, returns a decision, references owning Service action, and must not directly mutate domain objects or execute protected external actions.
