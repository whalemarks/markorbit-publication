# Common Contract — Idempotency

**Spec ID:** B02-CONTRACT-COMMON-IDEMPOTENCY  
**Spec Type:** Common Contract Specification  
**Contract Name:** Idempotency Contract  
**Contract File:** core-specs/contracts/common/idempotency.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** All Core object specifications where create/update/submit/apply/send/select operations exist  
**Related Service Specs:** All Core service specifications where retry-safe operations exist  
**Related API Specs:** All Core API specifications where retry-safe operations exist  
**Related Event Specs:** All Core event specifications where duplicate event emission must be controlled  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Idempotency Contract defines the canonical idempotency rules used across MarkOrbit Core.

It standardizes how APIs, services, workflows, agents and event-producing operations prevent accidental duplicate creation, duplicate submission, duplicate communication, duplicate workflow application, duplicate task creation, duplicate routing selection and duplicate event emission when clients or systems retry requests.

This contract governs:

```text
idempotency key shape
idempotency scope
idempotency fingerprint
request replay behavior
safe retry behavior
duplicate detection
conflict handling
event emission safety
agent retry safety
workflow retry safety
communication send safety
routing selection safety
Codex implementation rules
```

Idempotency Contract does not define business uniqueness by itself, replace domain validation, replace Permission/Policy checks, or make non-repeatable professional actions safe without owning service rules.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for making retryable operations produce one governed result for the same semantic request.
```

This contract does not mean:

```text
business uniqueness rule
database unique index only
deduplication heuristic
permission grant
policy approval
event replay rule
workflow approval
communication approval
payment approval
```

Core rule:

```text
Idempotency prevents accidental duplicate execution.
Owning services define semantic equality.
Permission and Policy still apply.
Events must not be duplicated by retry.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
idempotency key field naming
idempotency key validation
operation scope
request fingerprint shape
idempotency result behavior
duplicate replay behavior
conflict behavior
retry safety
event emission safety
idempotency errors
Codex implementation expectations
```

This contract is not responsible for:

```text
business object uniqueness
professional approval
permission evaluation
policy evaluation
state transition approval
event creation by itself
payment execution
external communication delivery by itself
routing selection by itself
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related common contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
```

Owning rule:

```text
Idempotency Contract defines retry safety shape. It must not be treated as authorization, approval, business uniqueness or event replay permission.
```

---

# 5. Related Core Objects

Idempotency applies to operations involving:

```text
Identity
Organization
User
Knowledge
Brand
Trademark
Document
Evidence
Customer
Matter
Order
Opportunity
WorkflowContract
Task
Event
Notification
Communication
Agent
ServiceProvider
Routing
Partner
ServiceNetwork
```

High-risk duplicate-sensitive targets include:

```text
Order
Matter
Task
WorkflowContract
Communication
Notification
Routing
Document
Evidence
Event
```

Rules:

```text
- Owning services define which operations require idempotency.
- Duplicate-sensitive operations must require idempotency_key or equivalent governed request reference.
- External side-effect operations must be idempotency-protected.
```

---

# 6. Required References

Idempotency context shape:

```yaml
idempotency_context:
  idempotency_key: string | null
  idempotency_scope: string
  operation_name: string
  operation_category: string
  request_fingerprint: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  correlation_id: string | null
```

Rules:

```text
- idempotency_key is required for duplicate-sensitive operations.
- idempotency_scope is required when idempotency_key is used.
- operation_name is required.
- operation_category is required.
- request_fingerprint is required where conflict detection depends on semantic equality.
- correlation_id must be preserved where provided.
```

---

# 7. Contract Shape

Canonical idempotency context shape:

```yaml
idempotency:
  idempotency_key: string | null
  idempotency_scope: string | null
  operation:
    operation_name: string
    operation_category: string
  request:
    request_fingerprint: string | null
    request_fingerprint_algorithm: string | null
  actor:
    actor_reference_id: string | null
    organization_reference_id: string | null
    agent_reference_id: string | null
  target:
    target_object_type: string | null
    target_object_reference_id: string | null
  result:
    idempotency_status: string | null
    original_result_reference_id: string | null
    replayed: boolean
    conflict_detected: boolean
  trace:
    correlation_id: string | null
    causation_id: string | null
```

Idempotent response extension:

```yaml
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
  original_result_reference_id: string | null
  conflict_detected: boolean
```

Rules:

```text
- idempotency_key must be opaque to business users.
- idempotency_key must not contain personal data, credentials or restricted business data.
- request_fingerprint must be stable for semantically identical requests.
- replayed response must be safe and consistent.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| idempotency_key | string | Contextual | Yes | Required for duplicate-sensitive operations. |
| idempotency_scope | string | Contextual | Yes | Required when key is used. |
| operation_name | string | Yes | No | Must identify operation safely. |
| operation_category | string | Yes | No | Must use controlled value. |
| request_fingerprint | string | Contextual | Yes | Required for mismatch/conflict detection. |
| request_fingerprint_algorithm | string | Contextual | Yes | Must be controlled where provided. |
| actor_reference_id | string | Contextual | Yes | Binds idempotency to actor where required. |
| organization_reference_id | string | Contextual | Yes | Binds idempotency to org scope where required. |
| agent_reference_id | string | Contextual | Yes | Binds idempotency to agent context where applicable. |
| target_object_type | string | Contextual | Yes | Must follow Reference Contract. |
| target_object_reference_id | string | Contextual | Yes | Must match target_object_type. |
| idempotency_status | string | Contextual | Yes | Must use controlled value. |
| original_result_reference_id | string | Contextual | Yes | References original result where safe. |
| replayed | boolean | Contextual | No | True when original result is replayed. |
| conflict_detected | boolean | Contextual | No | True when same key conflicts with different semantic request. |

---

# 9. Controlled Values

## 9.1 operation_category

```text
Create
Update
Delete
Apply
Send
Select
Submit
Import
Export
TransitionState
CreateExternalSideEffect
AgentAction
WorkflowAction
SystemAction
Unknown
```

## 9.2 idempotency_scope

```text
Actor
Organization
Agent
TargetObject
Operation
WorkflowApplication
CommunicationDelivery
NotificationDelivery
RoutingSelection
ExternalSubmission
EventEmission
System
Unknown
```

## 9.3 idempotency_status

```text
New
ExistingReplayed
Conflict
Expired
Invalid
NotRequired
Unknown
```

## 9.4 request_fingerprint_algorithm

```text
CanonicalJsonSha256
CanonicalPayloadSha256
ServiceDefinedStableHash
NotApplicable
Unknown
```

## 9.5 duplicate_sensitive_operation

```text
CreateOrder
CreateMatter
CreateTask
ApplyWorkflowContract
SendCommunication
CreateNotification
SelectRouting
SubmitExternalFiling
UploadDocument
CreateEvidence
EmitEvent
CreateAgentAction
Unknown
```

Rules:

```text
- Unknown is not valid for production idempotency decisions.
- Services may define narrower values in owning contracts.
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] operation_name is present.
[ ] operation_category is controlled.
[ ] idempotency_key is present where operation requires it.
[ ] idempotency_scope is present where key is used.
[ ] idempotency_key format is valid.
[ ] idempotency_key does not contain restricted data.
[ ] request_fingerprint is present where conflict detection requires it.
[ ] request_fingerprint_algorithm is controlled where provided.
[ ] actor/org/agent scope matches operation requirement.
[ ] target object reference follows Reference Contract.
[ ] existing idempotency record is checked before side effect.
[ ] conflict is detected when same key has different fingerprint.
[ ] original result is replayed safely for identical request.
[ ] event emission is not duplicated on replay.
```

---

# 11. Permission Rules

Idempotency does not bypass permission.

Rules:

```text
- Permission must still be evaluated or confirmed according to owning service rules.
- A replayed idempotent response must not expose data the current actor is no longer allowed to see.
- Owning service may return safe replay summary instead of full original response if permission changed.
- PermissionDenied must stop protected behavior even if idempotency_key matches an earlier request.
```

---

# 12. Policy Rules

Idempotency does not bypass policy.

Rules:

```text
- Policy must still be evaluated or confirmed according to owning service rules.
- A replayed response must respect current policy visibility unless owning policy allows frozen response replay.
- Policy may require redaction on replay.
- Policy may require returning conflict or restricted response when context changed.
- PolicyRestricted must stop or downgrade protected behavior.
```

---

# 13. AI Agent Rules

Agent-assisted operations must be idempotency-safe where they may create downstream side effects.

Rules:

```text
- AI Agent suggestions do not require idempotency unless persisted or used to trigger action.
- AI-prepared drafts that create active objects through services may require idempotency.
- Agent context must be included in idempotency scope where agent action is protected.
- AI must not fabricate idempotency_key for actions unless the client/service delegates key generation.
- Agent retry must not create duplicate tasks, communications, workflow applications or routing selections.
```

---

# 14. Event Rules

Event emission must be idempotency-safe.

Rules:

```text
- Event Service owns event recording.
- Owning service must not emit duplicate domain events on idempotent replay.
- Event emission may have its own EventEmission scope.
- Replayed response may include original event_reference_ids where policy allows.
- Event references are trace, not commands.
```

Duplicate event protection applies to:

```text
TaskCreated
WorkflowContractApplied
CommunicationCreated
NotificationCreated
RoutingEvaluated
RoutingSelected
OrderCreated
MatterCreated
DocumentCreated
EvidenceCreated
```

---

# 15. Error Rules

Controlled idempotency errors:

```text
IdempotencyKeyRequired
IdempotencyKeyInvalid
IdempotencyScopeInvalid
IdempotencyConflict
IdempotencyExpired
IdempotencyReplayRestricted
RequestFingerprintInvalid
RequestFingerprintMismatch
DuplicateRejected
DuplicateSideEffectPrevented
```

Safe error shape:

```yaml
error:
  code: string
  category: Idempotency | Conflict | Validation | Policy | Permission
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Conflict errors must not expose restricted original request data.
- ReplayRestricted must not expose hidden original result.
- DuplicateRejected must not reveal restricted object details.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding idempotency_scope values requires revision notes.
- Adding idempotency_status values requires revision notes.
- Changing idempotency key semantics is breaking.
- Changing replay behavior is breaking unless owning contract explicitly versions it.
- Changing request fingerprint algorithm is breaking unless backward compatible.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this Idempotency Contract before implementing duplicate-sensitive operations
require idempotency_key where owning service marks operation duplicate-sensitive
validate key format
compute stable request_fingerprint where required
check idempotency record before side effect
store idempotency result atomically with side effect where possible
return original safe result on identical replay
return IdempotencyConflict on same key with different fingerprint
prevent duplicate event emission on replay
apply Permission and Policy on replay
preserve correlation_id
use Error Contract for idempotency errors
write tests for missing idempotency_key
write tests for identical replay
write tests for fingerprint mismatch
write tests for expired key
write tests for replay after permission change
write tests for replay after policy restriction
write tests that duplicate events are not emitted
write tests that duplicate communications are not sent
write tests that duplicate workflow applications are not created
```

Codex must not:

```text
treat idempotency_key as permission grant
store restricted data inside idempotency_key
use raw request body as public fingerprint
emit duplicate events on retry
send duplicate communications on retry
apply workflow twice on retry
select routing twice on retry
return restricted original response after policy changed
ignore conflict when same key has different semantic request
```

---

# 18. Acceptance Criteria

This Idempotency Contract is accepted only if:

```text
[ ] It defines idempotency purpose.
[ ] It defines idempotency meaning.
[ ] It defines idempotency boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical idempotency context shape.
[ ] It defines idempotent response extension.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Idempotency Contract. Defines idempotency key, scope, fingerprint, replay/conflict behavior, permission/policy interaction, AI retry safety, event duplicate prevention, errors and Codex implementation rules. |

---

**End of Common Contract**
