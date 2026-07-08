# Event Specification — PermissionEvaluated

**Spec ID:** B02-EVT-PERMISSION-EVALUATED  
**Spec Type:** Event  
**Event Name:** PermissionEvaluated  
**Event File:** core-specs/events/permission-evaluated.md  
**Event Category:** DomainEvent  
**Owning Domain:** Permission  
**Producing Service:** core-specs/services/permission-service.md  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/permission-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/permission-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/permission-evaluated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

PermissionEvaluated records that Permission Service evaluated whether an actor may perform a requested action in a given context.

It exists so that Identity, User, Organization, Policy, Task, Workflow, Event, Audit, AI Agents, APIs and product consumers can safely recognize that an authorization decision was evaluated without treating Identity, User, Organization membership, assignment, AI suggestion or Policy evaluation as permission by itself.

PermissionEvaluated is required before:

```text
authorization decision trace
actor action eligibility trace
API access decision trace
task action authorization
workflow transition authorization
AI agent action authorization
audit accountability trace
policy-dependent permission checks
product UI safe action enablement
```

---

# 2. Event Meaning

PermissionEvaluated means:

```text
Permission Service has evaluated a requested action for a given actor, object and context, and produced a governed permission decision.
```

PermissionEvaluated does not mean:

```text
the action was executed
the action succeeded
Policy was passed unless explicitly linked
the actor owns the object
the actor belongs to an Organization
the actor has permanent access
the actor may perform all related actions
the User assignment itself granted permission
AI may act without Agent Contract
```

PermissionEvaluated records an authorization evaluation result only.

It does not execute the requested business operation.

---

# 3. Event Category

PermissionEvaluated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Permission domain.

It may support audit and workflow decisions, but it is not a WorkflowEvent or TaskEvent by itself.

---

# 4. Event Producer

Producing service:

```text
Permission Service
```

Producing operation:

```text
evaluatePermission
```

Source domain:

```text
Permission
```

Source object type:

```text
PermissionEvaluation
```

Allowed producer path:

```text
API / Core Service / AI-governed operation / System Process
        ↓
Permission Service evaluatePermission
        ↓
Event Service record PermissionEvaluated
```

Producer rules:

```text
- PermissionEvaluated must be emitted only after Permission Service completes a governed permission evaluation.
- PermissionEvaluated must not be emitted directly by product UI.
- PermissionEvaluated must not be emitted directly by AI Agent outside governed service operation.
- PermissionEvaluated must not be used as the execution record of the requested action.
```

---

# 5. Event Trigger

PermissionEvaluated is triggered when:

```text
Permission Service completes evaluatePermission and produces a controlled permission decision for a requested actor/action/object/context.
```

Required trigger conditions:

```text
evaluatePermission operation completed
actor reference validated
requested action reference captured
target object reference captured where applicable
organization/context reference captured where applicable
decision produced
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Identity creation
User creation
Organization membership creation
Task assignment
Policy evaluation alone
AI suggestion
UI button visibility check without governed Permission Service evaluation
failed permission evaluation infrastructure error
business operation execution
```

Related but separate events may include:

```text
PolicyEvaluated
TaskAssigned
WorkflowTransitionValidated
UserCreated
OrganizationCreated
ActionExecuted
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: PermissionEvaluated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Permission
source_service: Permission Service
source_operation: evaluatePermission
source_object_type: PermissionEvaluation
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/permission-evaluated-payload.md
safe_summary:
  permission_evaluation_reference_id: string
  requested_action: string
  decision: string
  target_object_type: string | null
  target_object_reference_id: string | null
  reason_code: string
restricted_fields_policy: PermissionEvaluatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
permission_evaluation_reference_id: string
subject_identity_reference_id: string
subject_user_reference_id: string | null
organization_reference_id: string | null
requested_action: string
target_object_type: string | null
target_object_reference_id: string | null
decision: string
reason_code: string
policy_decision_reference_id: string | null
permission_rule_reference_ids: list[string]
is_ai_actor: boolean
agent_contract_reference_id: string | null
```

Payload rules:

```text
- Payload must include decision but must not expose restricted rule internals unnecessarily.
- Payload must reference actor, action and target context.
- Payload must not include credentials, tokens, secrets or raw authentication material.
- Payload must not include confidential policy logic unless explicitly allowed.
- Payload must distinguish Permission decision from Policy decision.
- AI actor evaluation must include Agent Contract reference where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
permission_evaluation_reference_id
source_object_reference_id
actor_reference_id
subject_identity_reference_id
requested_action
decision
payload_contract_reference_id
```

Optional references:

```text
subject_user_reference_id
organization_reference_id
target_object_reference_id
target_object_type
permission_rule_reference_ids
policy_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal permission_evaluation_reference_id.
- actor_reference_id identifies who/what requested the evaluation.
- subject_identity_reference_id identifies whose permission was evaluated.
- subject_user_reference_id must not be assumed unless User context is present.
- policy_decision_reference_id must be included only when Policy Service was invoked or linked.
- permission_rule_reference_ids must be safe references, not full rule internals.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
PermissionEvaluated
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

## 8.4 decision

```text
Allowed
Denied
ReviewRequired
PolicyRequired
PermissionRuleMissing
ContextMissing
NotApplicable
Unknown
```

## 8.5 requested_action_type

```text
Create
Read
Update
Delete
Assign
Approve
Reject
Submit
Export
Import
Send
Execute
Validate
Administer
Unknown
```

## 8.6 reason_code

```text
PermissionAllowed
PermissionDenied
PermissionRuleMatched
PermissionRuleMissing
PolicyRequired
ContextMissing
ActorInvalid
TargetInvalid
ReviewRequired
AgentContractRequired
Unknown
```

---

# 9. Event Rules

## 9.1 PermissionEvaluated Records Authorization Evaluation

PermissionEvaluated records that an authorization evaluation occurred.

It must not be treated as execution of the requested action.

## 9.2 PermissionEvaluated Does Not Replace Policy

Policy Service owns contextual constraints.

PermissionEvaluated may reference PolicyEvaluated, but does not replace it.

## 9.3 Assignment Does Not Equal Permission

Task assignment, organization membership or role label must not be treated as PermissionEvaluated unless Permission Service evaluated the action.

## 9.4 Identity or User Does Not Equal Permission

Identity and User references provide actor context.

They do not grant action permission by themselves.

## 9.5 Permission Decision Is Contextual

PermissionEvaluated applies to the specific actor/action/object/context captured in payload.

It must not be generalized to all actions or objects.

## 9.6 AI Actor Requires Agent Governance

If the evaluated actor is AI, the event must include Agent Contract context where applicable.

## 9.7 PermissionEvaluated Must Be Immutable

PermissionEvaluated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
API Layer
Workflow Contract Service
Task Service
Matter Service
Document Service
Evidence Service
Communication Service
Notification Service
Policy Service
Audit Service
AI Agent Governance
Product UI read model
Integration services under contract
```

Consumer rules:

```text
- API Layer may use PermissionEvaluated to allow/deny a requested API action.
- Workflow Contract Service may use PermissionEvaluated for transition guard decisions.
- Task Service may use PermissionEvaluated to authorize assignment/completion actions.
- Communication Service may use PermissionEvaluated before outbound communication.
- Audit may preserve permission decision trace.
- AI Agents may summarize permission evaluation only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat PermissionEvaluated as business operation execution
reuse decision outside captured context
treat PermissionEvaluated as Policy approval unless linked
expose restricted permission rule internals
let AI bypass denied/review-required decisions
```

---

# 11. Relationship to Services

Producing service:

```text
Permission Service produces PermissionEvaluated after evaluatePermission completes.
```

Event Service:

```text
Event Service records, validates and dispatches PermissionEvaluated.
```

Related services:

```text
Identity Service provides subject identity reference.
User Service may provide user context.
Organization Service may provide operating context.
Policy Service may provide linked policy decision.
Workflow Contract Service may consume it as guard evidence.
Task, Matter, Document, Evidence and Communication services may consume it before sensitive actions.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for AI action authorization.
```

Boundary reminders:

```text
Permission Service owns allowed action decision.
Policy Service owns contextual constraints.
Identity Service owns actor recognition.
User Service owns account participant.
Organization Service owns operating context.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /permissions/evaluations/{evaluation_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not fabricate PermissionEvaluated directly.
- API must call Permission Service evaluatePermission, which emits the event.
- API must not expose restricted permission rule internals.
- API must distinguish PermissionEvaluated from PolicyEvaluated and action execution events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize whether an action was allowed, denied or review-required
explain that Permission decision is contextual
flag missing Policy evaluation where decision is PolicyRequired
flag missing Agent Contract for AI actor
prepare audit-safe permission evaluation summary
```

AI must not:

```text
fabricate PermissionEvaluated
rewrite PermissionEvaluated
delete PermissionEvaluated
treat PermissionEvaluated as action execution
reuse PermissionEvaluated outside captured context
override Denied or ReviewRequired decisions
expose restricted permission rule internals
```

AI-originated evaluation requires:

```text
agent_identity_reference_id where AI requested evaluation
agent_contract_reference_id where AI is evaluated actor or requester
authorized_knowledge_reference
permission_rule_reference_ids where safe
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

PermissionEvaluated is valid only if:

```text
[ ] event_name is PermissionEvaluated.
[ ] event_category is DomainEvent.
[ ] producing service is Permission Service.
[ ] producing operation is evaluatePermission.
[ ] source_domain is Permission.
[ ] source_object_type is PermissionEvaluation.
[ ] source_object_reference_id is present.
[ ] permission_evaluation_reference_id is present.
[ ] source_object_reference_id equals permission_evaluation_reference_id.
[ ] actor_reference_id is present.
[ ] subject_identity_reference_id is present.
[ ] requested_action is present.
[ ] decision is controlled.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] target object context is present where required by requested_action.
[ ] policy_decision_reference_id is present where decision depends on Policy.
[ ] Agent Contract reference is present where AI actor governance requires it.
[ ] restricted rule internals are not exposed.
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
PermissionEvaluationReferenceMissing
PermissionEvaluationReferenceMismatch
ActorReferenceMissing
SubjectIdentityReferenceMissing
RequestedActionMissing
DecisionInvalid
TargetContextMissing
PayloadContractMissing
RestrictedFieldViolation
PermissionRuleRestricted
PolicyReferenceRequired
AgentContractRequired
PolicyRestricted
DuplicateEventRejected
UnknownPermissionEventError
```

Rejection rules:

```text
- Failed permission evaluation infrastructure errors must not emit PermissionEvaluated unless a separate failure event is defined.
- Missing actor/action/decision must reject PermissionEvaluated.
- Restricted rule internals must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Permission Service Specification
cite Permission Object Specification
cite Event Service Specification
cite Policy Service Specification where policy_decision_reference_id is involved
use exact event_name: PermissionEvaluated
use exact event_category: DomainEvent
validate permission_evaluation_reference_id
validate source_object_reference_id equals permission_evaluation_reference_id
validate subject_identity_reference_id
validate requested_action
validate controlled decision
validate payload contract
write tests that PermissionEvaluated does not execute requested action
write tests that Assignment/User/Identity does not equal Permission
write tests that restricted permission rule internals are not exposed
write tests for PolicyRequired decision where applicable
write tests for AI Agent Contract requirements where applicable
```

Codex must not:

```text
emit PermissionEvaluated directly from UI
treat UI button visibility as PermissionEvaluated unless Permission Service is invoked
treat PolicyEvaluated as PermissionEvaluated
treat PermissionEvaluated as action execution
reuse PermissionEvaluated outside captured context
include restricted rule internals in payload by default
allow AI to fabricate or override PermissionEvaluated
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines PermissionEvaluated purpose.
[ ] It defines PermissionEvaluated meaning.
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
| 0.1.0 | Draft | Initial PermissionEvaluated Event specification. Defines governed permission evaluation event and separates PermissionEvaluated from Policy, Identity, User, Organization membership, assignment and action execution. |

---

**End of Event Specification**
