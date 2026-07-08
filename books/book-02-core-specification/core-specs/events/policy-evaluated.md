# Event Specification — PolicyEvaluated

**Spec ID:** B02-EVT-POLICY-EVALUATED  
**Spec Type:** Event  
**Event Name:** PolicyEvaluated  
**Event File:** core-specs/events/policy-evaluated.md  
**Event Category:** DomainEvent  
**Owning Domain:** Policy  
**Producing Service:** core-specs/services/policy-service.md  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md  
**Related Service Specs:** core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/policy-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/policy-evaluated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

PolicyEvaluated records that Policy Service evaluated contextual constraints for a requested action, object, actor, workflow, API or AI operation.

It exists so that Permission, Identity, User, Organization, Task, Workflow Contract, Document, Evidence, Communication, Event, Audit, AI Agents, APIs and product consumers can safely recognize that a policy constraint decision was evaluated without treating Policy as Permission, execution, approval, legal judgment or final professional decision.

PolicyEvaluated is required before:

```text
contextual constraint trace
confidentiality and visibility checks
AI agent governance checks
API policy enforcement trace
workflow guard policy context
document/evidence visibility policy trace
communication outbound policy trace
audit accountability trace
professional review requirement trace
```

---

# 2. Event Meaning

PolicyEvaluated means:

```text
Policy Service has evaluated one or more contextual constraints and produced a governed policy decision for a specific context.
```

PolicyEvaluated does not mean:

```text
Permission was granted
the requested action was executed
the requested action succeeded
legal or professional review was completed
the actor has permanent access
all related policies passed
the object is safe for all contexts
AI may act without Agent Contract
```

PolicyEvaluated records a contextual constraint evaluation result only.

It does not grant permission and does not execute business operations.

---

# 3. Event Category

PolicyEvaluated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Policy domain.

It may support workflow, audit, API and AI guard decisions, but it is not a WorkflowEvent or AIAgentEvent by itself unless a separate AI-specific policy event is defined.

---

# 4. Event Producer

Producing service:

```text
Policy Service
```

Producing operation:

```text
evaluatePolicy
```

Source domain:

```text
Policy
```

Source object type:

```text
PolicyEvaluation
```

Allowed producer path:

```text
API / Core Service / AI-governed operation / System Process
        ↓
Policy Service evaluatePolicy
        ↓
Event Service record PolicyEvaluated
```

Producer rules:

```text
- PolicyEvaluated must be emitted only after Policy Service completes a governed policy evaluation.
- PolicyEvaluated must not be emitted directly by product UI.
- PolicyEvaluated must not be emitted directly by AI Agent outside governed service operation.
- PolicyEvaluated must not be used as execution record of the requested action.
```

---

# 5. Event Trigger

PolicyEvaluated is triggered when:

```text
Policy Service completes evaluatePolicy and produces a controlled policy decision for a requested actor/object/action/context.
```

Required trigger conditions:

```text
evaluatePolicy operation completed
policy scope identified
actor reference captured where applicable
target object reference captured where applicable
context reference captured
decision produced
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Permission evaluation alone
Identity creation
User creation
Organization creation
Task assignment
Workflow transition request
AI suggestion
UI visibility check without governed Policy Service evaluation
failed policy evaluation infrastructure error
business operation execution
```

Related but separate events may include:

```text
PermissionEvaluated
WorkflowTransitionValidated
TaskAssigned
CommunicationSent
DocumentCreated
EvidenceCreated
AIAgentActionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: PolicyEvaluated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Policy
source_service: Policy Service
source_operation: evaluatePolicy
source_object_type: PolicyEvaluation
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/policy-evaluated-payload.md
safe_summary:
  policy_evaluation_reference_id: string
  policy_scope: string
  decision: string
  target_object_type: string | null
  target_object_reference_id: string | null
  reason_code: string
restricted_fields_policy: PolicyEvaluatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
policy_evaluation_reference_id: string
policy_scope: string
policy_reference_ids: list[string]
subject_identity_reference_id: string | null
subject_user_reference_id: string | null
organization_reference_id: string | null
requested_action: string | null
target_object_type: string | null
target_object_reference_id: string | null
decision: string
reason_code: string
review_required: boolean
permission_evaluation_reference_id: string | null
is_ai_actor: boolean
agent_contract_reference_id: string | null
```

Payload rules:

```text
- Payload must include decision but must not expose restricted policy internals unnecessarily.
- Payload must reference policy scope and target context.
- Payload must not include confidential policy logic unless explicitly allowed.
- Payload must not include credentials, tokens, secrets or raw authentication material.
- Payload must distinguish Policy decision from Permission decision.
- AI actor evaluation must include Agent Contract reference where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
policy_evaluation_reference_id
source_object_reference_id
actor_reference_id
policy_scope
decision
payload_contract_reference_id
```

Optional references:

```text
policy_reference_ids
subject_identity_reference_id
subject_user_reference_id
organization_reference_id
target_object_reference_id
target_object_type
permission_evaluation_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal policy_evaluation_reference_id.
- actor_reference_id identifies who/what requested the evaluation.
- policy_reference_ids must be safe references, not full policy internals.
- permission_evaluation_reference_id must be included only when Permission Service was invoked or linked.
- agent_contract_reference_id is required where AI Agent governance requires it.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
PolicyEvaluated
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

## 8.4 policy_scope

```text
AccessPolicy
VisibilityPolicy
ConfidentialityPolicy
WorkflowPolicy
AIAgentPolicy
APIPolicy
CommunicationPolicy
DocumentPolicy
EvidencePolicy
DataRetentionPolicy
CompliancePolicy
Unknown
```

## 8.5 decision

```text
Passed
Failed
ReviewRequired
PermissionRequired
ContextMissing
PolicyMissing
NotApplicable
Blocked
Unknown
```

## 8.6 reason_code

```text
PolicyPassed
PolicyFailed
ReviewRequired
PermissionRequired
ContextMissing
PolicyMissing
ConfidentialityRestricted
VisibilityRestricted
AgentContractRequired
APIAccessRestricted
CommunicationRestricted
DocumentRestricted
EvidenceRestricted
Unknown
```

---

# 9. Event Rules

## 9.1 PolicyEvaluated Records Contextual Constraint Evaluation

PolicyEvaluated records that contextual constraints were evaluated.

It must not be treated as execution of the requested action.

## 9.2 PolicyEvaluated Does Not Grant Permission

Permission Service owns allowed action decisions.

PolicyEvaluated may require or reference PermissionEvaluated but does not replace it.

## 9.3 Policy Decision Is Contextual

PolicyEvaluated applies only to the captured scope, actor, object, action and context.

It must not be generalized to all objects, users, products or actions.

## 9.4 PolicyEvaluated May Require Review

Policy decision may be ReviewRequired.

ReviewRequired is not approval.

Review execution must be governed by relevant workflow or service.

## 9.5 Policy Internals Are Restricted

PolicyEvaluated may expose safe reason codes.

It must not expose restricted policy logic, rule internals or sensitive thresholds unless explicitly allowed.

## 9.6 AI Agent Policy Must Be Explicit

If the evaluation involves AI action or AI actor, payload must identify AI context and Agent Contract where required.

## 9.7 PolicyEvaluated Must Be Immutable

PolicyEvaluated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Permission Service
API Layer
Workflow Contract Service
Task Service
Matter Service
Document Service
Evidence Service
Communication Service
Notification Service
Audit Service
AI Agent Governance
Product UI read model
Integration services under contract
```

Consumer rules:

```text
- Permission Service may consume PolicyEvaluated where policy is part of authorization context.
- API Layer may use PolicyEvaluated to enforce visibility, access or operation constraints.
- Workflow Contract Service may use PolicyEvaluated as transition guard evidence.
- Document and Evidence services may use it for visibility and use constraints.
- Communication Service may use it before outbound communication.
- Audit may preserve policy decision trace.
- AI Agents may summarize policy evaluation only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat PolicyEvaluated as Permission grant
treat PolicyEvaluated as business operation execution
reuse decision outside captured context
expose restricted policy internals
let AI bypass failed/review-required policy decisions
```

---

# 11. Relationship to Services

Producing service:

```text
Policy Service produces PolicyEvaluated after evaluatePolicy completes.
```

Event Service:

```text
Event Service records, validates and dispatches PolicyEvaluated.
```

Related services:

```text
Permission Service may link PolicyEvaluated to authorization decisions.
Identity, User and Organization services provide actor/context references.
Workflow Contract Service may consume PolicyEvaluated for guard validation.
Task, Matter, Document, Evidence and Communication services may consume PolicyEvaluated before sensitive operations.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for AI policy guard trace.
```

Boundary reminders:

```text
Policy Service owns contextual constraints.
Permission Service owns allowed action.
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
GET /policy/evaluations/{evaluation_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not fabricate PolicyEvaluated directly.
- API must call Policy Service evaluatePolicy, which emits the event.
- API must not expose restricted policy rule internals or sensitive thresholds.
- API must distinguish PolicyEvaluated from PermissionEvaluated and action execution events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize whether policy passed, failed, blocked or requires review
explain that Policy decision is contextual
flag missing Permission evaluation where decision is PermissionRequired
flag missing Agent Contract for AI actor/action
prepare audit-safe policy evaluation summary
```

AI must not:

```text
fabricate PolicyEvaluated
rewrite PolicyEvaluated
delete PolicyEvaluated
treat PolicyEvaluated as Permission grant
treat PolicyEvaluated as action execution
reuse PolicyEvaluated outside captured context
override Failed, Blocked or ReviewRequired decisions
expose restricted policy rule internals
```

AI-originated evaluation requires:

```text
agent_identity_reference_id where AI requested evaluation
agent_contract_reference_id where AI is evaluated actor or requester
authorized_knowledge_reference
policy_reference_ids where safe
permission_evaluation_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

PolicyEvaluated is valid only if:

```text
[ ] event_name is PolicyEvaluated.
[ ] event_category is DomainEvent.
[ ] producing service is Policy Service.
[ ] producing operation is evaluatePolicy.
[ ] source_domain is Policy.
[ ] source_object_type is PolicyEvaluation.
[ ] source_object_reference_id is present.
[ ] policy_evaluation_reference_id is present.
[ ] source_object_reference_id equals policy_evaluation_reference_id.
[ ] actor_reference_id is present.
[ ] policy_scope is controlled.
[ ] decision is controlled.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] target object context is present where required by policy_scope.
[ ] permission_evaluation_reference_id is present where decision depends on Permission.
[ ] Agent Contract reference is present where AI Agent governance requires it.
[ ] restricted policy internals are not exposed.
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
PolicyEvaluationReferenceMissing
PolicyEvaluationReferenceMismatch
ActorReferenceMissing
PolicyScopeMissing
PolicyScopeInvalid
DecisionInvalid
TargetContextMissing
PayloadContractMissing
RestrictedFieldViolation
PolicyRuleRestricted
PermissionReferenceRequired
AgentContractRequired
DuplicateEventRejected
UnknownPolicyEventError
```

Rejection rules:

```text
- Failed policy evaluation infrastructure errors must not emit PolicyEvaluated unless a separate failure event is defined.
- Missing policy scope or decision must reject PolicyEvaluated.
- Restricted policy internals must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Policy Service Specification
cite Policy Object Specification
cite Event Service Specification
cite Permission Service Specification where permission_evaluation_reference_id is involved
use exact event_name: PolicyEvaluated
use exact event_category: DomainEvent
validate policy_evaluation_reference_id
validate source_object_reference_id equals policy_evaluation_reference_id
validate policy_scope
validate controlled decision
validate payload contract
write tests that PolicyEvaluated does not execute requested action
write tests that PolicyEvaluated does not grant Permission
write tests that restricted policy internals are not exposed
write tests for PermissionRequired decision where applicable
write tests for AI Agent Contract requirements where applicable
```

Codex must not:

```text
emit PolicyEvaluated directly from UI
treat UI visibility checks as PolicyEvaluated unless Policy Service is invoked
treat PermissionEvaluated as PolicyEvaluated
treat PolicyEvaluated as action execution
reuse PolicyEvaluated outside captured context
include restricted policy internals in payload by default
allow AI to fabricate or override PolicyEvaluated
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines PolicyEvaluated purpose.
[ ] It defines PolicyEvaluated meaning.
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
| 0.1.0 | Draft | Initial PolicyEvaluated Event specification. Defines governed contextual policy evaluation event and separates PolicyEvaluated from Permission, action execution, approval and final professional decision. |

---

**End of Event Specification**
