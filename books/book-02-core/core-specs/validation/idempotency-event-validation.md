# Idempotency Event Validation

**Spec ID:** B02-VALIDATION-IDEMPOTENCY-EVENT  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/idempotency-event-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Permission Policy Validation:** core-specs/validation/permission-policy-validation.md  
**Related Common Contracts:** core-specs/contracts/common/idempotency.md; core-specs/contracts/common/audit-context.md  
**Related API Contract:** core-specs/contracts/api/event-api-contract.md  
**Related Test Contract:** core-specs/contracts/tests/idempotency-event-tests.md  
**Related Codex Task:** codex-tasks/TASK-005-idempotency-event-trace.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Idempotency Level 3; Event Trace Level 2/3  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate Idempotency and Event Trace behavior in MarkOrbit Core.

Idempotency Event Validation ensures that duplicate-sensitive operations are safe to retry and that Events remain trace records, not commands.

It validates the rules:

```text
Idempotency prevents duplicate effects.
Events preserve trace.
Events are not commands.
Event references must not trigger downstream actions.
Only owning services emit Events.
Permission and Policy govern Event visibility.
```

This validation is required before API validators, Workflow validators and the MVP execution spine are accepted.

---

# 2. Core Lock

```text
Idempotency prevents duplicate execution.
Same idempotency key and same semantic request must replay safely.
Same idempotency key and different semantic request must fail safely.
Replay must not duplicate objects, Tasks, Communications or Events.
Events preserve trace.
Events are not commands.
Event references are trace only.
Events are emitted only by owning services or approved Event Service integration.
API layer must not emit Events directly.
Workflow layer must not emit Events directly.
Agent layer must not emit Events directly.
Event visibility is governed by Permission and Policy.
Restricted Event data must not leak.
Codex must preserve Idempotency and Event boundaries.
```

---

# 3. Validation Scope

This validation covers:

```text
Idempotency Contract
Audit Context Contract
Event Object
Event Service
Event API Contract
state-changing service actions
duplicate-sensitive API operations
workflow apply operations
Task creation
Communication creation
Event creation
Event visibility
Event references
API no-direct-event-emission
Workflow no-direct-event-emission
Agent no-direct-event-emission
Idempotency/Event tests
Codex task traceability
```

This validation does not cover:

```text
production event streaming infrastructure
Kafka or equivalent event bus
full event sourcing platform
production audit dashboard
external observability platform
payment event integration
official filing event integration
```

---

# 4. Required Source Files

Validation must inspect:

```text
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/versioning.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/tests/idempotency-event-tests.md
codex-tasks/TASK-005-idempotency-event-trace.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/permission-policy-validation.md
```

Validation should also inspect:

```text
core-specs/objects/event-object.md
core-specs/services/event-service.md
core-specs/events/
core-specs/contracts/api/
core-specs/contracts/workflows/
core-specs/workflows/
core-specs/agents/
codex-tasks/
```

---

# 5. Idempotency Scope Checks

Duplicate-sensitive operations must require Idempotency.

Required duplicate-sensitive operations:

```text
create Customer
create Brand
create Trademark
create Matter
create Order
create Document
create Evidence
create Task
create Communication
workflow apply
routing selection stub if exposed
```

Checks:

```text
[ ] Operation is identified as duplicate-sensitive.
[ ] idempotency_key is required.
[ ] Missing key returns IdempotencyKeyRequired.
[ ] Same key + same semantic request replays safely.
[ ] Same key + different semantic request returns IdempotencyConflict.
[ ] Replay does not duplicate objects.
[ ] Replay does not duplicate Tasks.
[ ] Replay does not duplicate Communications.
[ ] Replay does not duplicate Events.
```

Blocked if:

```text
Must Build Now duplicate-sensitive operation has no Idempotency requirement.
```

---

# 6. Semantic Request Validation

Validate semantic request comparison.

Required fingerprint inputs:

```text
operation_key
actor_reference_id where required
organization_reference_id where required
target_reference_id where required
normalized request payload
contract_version
schema_version where applicable
```

Allowed exclusions:

```text
correlation_id
request timestamp
non-semantic client metadata
transient retry metadata
```

Checks:

```text
[ ] Fingerprint or equivalent comparison is deterministic.
[ ] Same semantic payload produces same fingerprint.
[ ] Different semantic payload produces conflict.
[ ] Restricted prior payload is not leaked on conflict.
[ ] Version context is included where required.
```

Architecture violation:

```text
same idempotency_key with different payload is treated as successful replay.
Idempotency conflict reveals original restricted payload.
```

---

# 7. Safe Replay Validation

Safe replay must preserve original effect without creating duplicates.

Validate:

```text
[ ] Same idempotency_key + same semantic request returns same or linked safe response.
[ ] Replay does not create duplicate domain object.
[ ] Replay does not create duplicate active Task.
[ ] Replay does not create duplicate Communication.
[ ] Replay does not create duplicate Event.
[ ] Replay respects current Permission and Policy visibility.
[ ] Replay does not reveal policy-hidden previous result.
```

Required tests:

```text
idempotency_replay_same_request_safe
idempotency_replay_no_duplicate_object
idempotency_replay_no_duplicate_task
idempotency_replay_no_duplicate_communication
idempotency_replay_no_duplicate_event
idempotency_replay_does_not_leak_policy_hidden_result
```

---

# 8. Conflict Validation

Validate:

```text
[ ] Same key + different semantic request returns IdempotencyConflict.
[ ] Conflict creates no side effects.
[ ] Conflict emits no new Event.
[ ] Conflict does not expose original restricted payload.
[ ] Conflict does not expose hidden target existence.
[ ] Conflict error uses Error Contract.
```

Architecture violation:

```text
IdempotencyConflict mutates state.
IdempotencyConflict emits Event.
IdempotencyConflict leaks restricted original request.
```

---

# 9. Event Record Validation

Minimum Event record shape:

```yaml
event_reference_id: string
event_type: string
source_service: string
subject_reference_id: string
actor_reference_id: string | null
organization_reference_id: string | null
correlation_id: string | null
causation_event_reference_id: string | null
idempotency_key: string | null
payload: object
visibility: object
schema_version: string
contract_version: string
created_at: string
```

Validate:

```text
[ ] event_reference_id follows Reference Contract.
[ ] event_type is controlled.
[ ] source_service is present.
[ ] subject_reference_id is present where applicable.
[ ] correlation_id is preserved where provided.
[ ] causation_event_reference_id is a trace reference.
[ ] payload is safe.
[ ] visibility is defined.
[ ] schema_version is present.
[ ] contract_version is present.
```

Blocked if:

```text
MVP Event record shape missing.
Event record exposes raw database ID publicly.
Event record has no visibility metadata.
```

---

# 10. Event Ownership Validation

Events must be emitted only by owning services or approved Event Service integration.

Required ownership examples:

```text
CustomerCreated → Customer Service
BrandCreated → Brand Service
TrademarkCreated → Trademark Service
MatterCreated → Matter Service
OrderCreated → Order Service
DocumentCreated → Document Service
DocumentAttached → Document Service or owning attachment service contract
EvidenceCreated → Evidence Service
WorkflowContractPreviewed → Workflow Contract Service
WorkflowContractApplied → Workflow Contract Service
TaskCreated → Task Service
TaskUpdated → Task Service
CommunicationCreated → Communication Service
CommunicationReviewed → Communication Service
PermissionEvaluated → Permission Service
PolicyEvaluated → Policy Service
RoutingEvaluated → Routing Service
RoutingSelected → Routing Service
```

Validate:

```text
[ ] Event source_service matches owning service.
[ ] API layer does not emit Event directly.
[ ] Workflow layer does not emit Event directly.
[ ] Agent layer does not emit Event directly.
[ ] Event Service records trace and enforces visibility.
```

Architecture violation:

```text
API emits Event directly.
Workflow emits Event directly.
Agent emits Event directly.
Wrong service emits another domain's Event.
```

---

# 11. Event Reference Validation

Event references are trace only.

Validate:

```text
[ ] event_reference_id may be read as trace.
[ ] event_reference_id may be used as causation reference.
[ ] event_reference_id may be used for audit correlation.
[ ] event_reference_id does not trigger commands.
[ ] event_reference_id does not complete Task.
[ ] event_reference_id does not send Communication.
[ ] event_reference_id does not apply Workflow.
[ ] event_reference_id does not mutate domain state.
```

Required test:

```text
event_reference_not_command
```

Architecture violation:

```text
event_reference_id triggers downstream action.
event_reference_id is used as command input.
```

---

# 12. Event Visibility Validation

Event read/search must obey Permission and Policy.

Validate:

```text
[ ] Event read requires Permission where protected.
[ ] Event payload follows Policy.
[ ] PolicyRestrictedRedact omits restricted payload fields.
[ ] restricted_fields_omitted is true where redaction occurs.
[ ] PolicyNonDisclosureNotFound hides event existence where required.
[ ] Pagination does not reveal hidden Event counts.
[ ] Event errors do not expose restricted payload.
[ ] Event visibility applies to idempotent replay responses.
```

Required tests:

```text
event_visibility_policy_allowed
event_visibility_policy_restricted_redact
event_visibility_policy_nondisclosure_notfound
event_pagination_does_not_leak_hidden_count
event_error_does_not_leak_restricted_payload
```

Architecture violation:

```text
restricted Event payload leaks.
hidden Event existence is revealed.
Event search leaks hidden counts.
```

---

# 13. Audit Context Validation

Validate Audit Context:

```text
[ ] correlation_id is accepted and preserved.
[ ] causation_event_reference_id is validated.
[ ] event_reference_ids are validated as references.
[ ] actor_reference_id is preserved where applicable.
[ ] source_service is preserved.
[ ] audit context does not expose restricted data.
[ ] audit context does not convert event references into commands.
```

Required tests:

```text
audit_correlation_preserved
causation_event_reference_validated
audit_event_reference_trace_only
```

---

# 14. API Event Boundary Validation

Validate API behavior:

```text
[ ] API layer does not emit Events directly.
[ ] API response may include event_reference_ids only as trace.
[ ] API does not treat Event references as command.
[ ] API event read/search routes through Event Service.
[ ] Event API uses Permission/Policy.
[ ] Event API uses Error Contract.
[ ] Event API uses Versioning Contract.
```

Architecture violation:

```text
API creates event record directly outside Event Service boundary.
API response event_reference_id triggers workflow or task behavior.
```

---

# 15. Workflow Event Boundary Validation

Validate Workflow behavior:

```text
[ ] Workflow preview emits no Events.
[ ] Workflow apply does not emit Events directly.
[ ] Workflow apply coordinates services that may record Events.
[ ] Workflow task plan is not Event.
[ ] Workflow event_reference_ids are trace only.
[ ] Workflow apply idempotency prevents duplicate Events.
```

Architecture violation:

```text
Workflow preview emits Event.
Workflow apply emits Event directly.
Workflow replay duplicates Events.
```

---

# 16. Agent Event Boundary Validation

Validate Agent behavior:

```text
[ ] Agent layer does not emit Events.
[ ] Agent output may summarize Event trace.
[ ] Agent output may include existing event_reference_ids only as trace.
[ ] Agent cannot alter Event trace.
[ ] Agent cannot delete Events.
[ ] Agent cannot use Event reference as command.
[ ] Agent must respect Event visibility policy.
```

Architecture violation:

```text
Agent emits Event.
Agent modifies Event trace.
Agent reveals restricted Event payload.
Agent uses Event reference to execute action.
```

---

# 17. Task / Communication Event Validation

Validate:

```text
[ ] TaskCreated emitted only through Task Service.
[ ] TaskUpdated emitted only through Task Service.
[ ] CommunicationCreated emitted only through Communication Service.
[ ] CommunicationReviewed emitted only through Communication Service.
[ ] CommunicationSent is out of MVP unless explicitly human-reviewed and service-owned.
[ ] Replay does not duplicate Task Events.
[ ] Replay does not duplicate Communication Events.
```

Architecture violation:

```text
Workflow emits TaskCreated directly.
Agent emits CommunicationSent.
Replay duplicates TaskCreated or CommunicationCreated.
```

---

# 18. Versioning Validation

Validate:

```text
[ ] Event record has schema_version.
[ ] Event record has contract_version.
[ ] Unsupported event schema version fails closed.
[ ] Unsupported event contract version fails closed.
[ ] Historical Event versions are preserved.
[ ] Idempotency fingerprint includes contract_version where required.
[ ] Deprecated versions are not silently rewritten.
```

Required tests:

```text
event_unsupported_version_fails_closed
event_historical_version_preserved
idempotency_fingerprint_includes_version
```

---

# 19. Error Safety Validation

Validate:

```text
[ ] IdempotencyKeyRequired uses Error Contract.
[ ] IdempotencyConflict uses Error Contract.
[ ] Event visibility errors use Error Contract.
[ ] Event version errors use Error Contract.
[ ] Errors do not expose raw database IDs.
[ ] Errors do not expose restricted payload.
[ ] Errors do not expose policy internals.
[ ] Errors do not expose permission internals.
[ ] correlation_id is preserved.
```

Architecture violation:

```text
IdempotencyConflict leaks original restricted payload.
Event error leaks hidden Event data.
Event error exposes stack trace.
```

---

# 20. Test Traceability Validation

Validate:

```text
[ ] idempotency-event-tests.md exists.
[ ] TASK-005 exists.
[ ] Missing idempotency key test exists.
[ ] Safe replay test exists.
[ ] Idempotency conflict test exists.
[ ] No duplicate object test exists.
[ ] No duplicate Task test exists.
[ ] No duplicate Communication test exists.
[ ] No duplicate Event test exists.
[ ] Event record shape test exists.
[ ] Event ownership test exists.
[ ] API no-direct-event-emission test exists.
[ ] Workflow no-direct-event-emission test exists.
[ ] Agent no-direct-event-emission test exists.
[ ] Event reference not command test exists.
[ ] Event visibility tests exist.
[ ] VersionUnsupported tests exist.
[ ] Safe error tests exist.
```

Blocked if:

```text
Idempotency/Event tests missing.
No duplicate-effect tests.
No event boundary tests.
```

---

# 21. Validation Procedure

Perform validation in this order:

```text
1. Confirm required Idempotency and Event source files exist.
2. Validate duplicate-sensitive operation coverage.
3. Validate semantic request comparison.
4. Validate safe replay behavior.
5. Validate conflict behavior.
6. Validate Event record shape.
7. Validate Event ownership.
8. Validate Event reference behavior.
9. Validate Event visibility.
10. Validate Audit Context.
11. Validate API Event boundary.
12. Validate Workflow Event boundary.
13. Validate Agent Event boundary.
14. Validate Task/Communication Event ownership.
15. Validate Versioning.
16. Validate Error safety.
17. Validate test traceability.
18. Classify findings.
19. Produce validation report.
```

---

# 22. Finding Classification

Use:

```text
Pass
Warning
Blocked
Architecture Violation
Out of Scope
Deferred
```

Classification rules:

```text
Blocked = Must Build Now duplicate-sensitive behavior lacks Idempotency or Event trace.
Architecture Violation = duplicate effects, event command behavior or direct emission boundary breach.
Warning = future/stub event coverage incomplete but safe.
Out of Scope = valid but beyond MVP.
Deferred = later event infrastructure item.
Pass = sufficient for current depth.
```

---

# 23. Required Evidence

Every finding must include:

```text
operation or event
source file
affected service/API/workflow/agent
idempotency requirement
event ownership rule
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Workflow apply can replay and create duplicate Task.
Status: Architecture Violation
Area: Workflow Apply / Task / Idempotency
Required Fix: Use Idempotency replay record and Task Service duplicate prevention.
Codex Impact: Block TASK-005, TASK-008 and TASK-010.
```

---

# 24. Architecture Violation Triggers

The following always fail validation:

```text
Duplicate-sensitive operation has no idempotency_key.
Same key + different semantic request succeeds.
Replay creates duplicate object.
Replay creates duplicate Task.
Replay creates duplicate Communication.
Replay creates duplicate Event.
IdempotencyConflict leaks restricted prior payload.
API layer emits Events directly.
Workflow layer emits Events directly.
Agent layer emits Events directly.
Event reference triggers command.
Event reference completes Task.
Event reference sends Communication.
Event reference applies Workflow.
Restricted Event payload leaks.
Hidden Event existence is revealed.
Unsupported Event version is silently accepted.
Historical Event version is silently rewritten.
```

---

# 25. Acceptance Criteria

Idempotency Event Validation passes only if:

```text
[ ] Required source files exist.
[ ] Duplicate-sensitive operations are identified.
[ ] idempotency_key is required where needed.
[ ] Missing idempotency key fails safely.
[ ] Semantic request comparison exists.
[ ] Safe replay behavior is defined.
[ ] Conflict behavior is defined.
[ ] Replay creates no duplicate object.
[ ] Replay creates no duplicate Task.
[ ] Replay creates no duplicate Communication.
[ ] Replay creates no duplicate Event.
[ ] Event record shape is defined.
[ ] Event ownership is defined.
[ ] API layer does not emit Events directly.
[ ] Workflow layer does not emit Events directly.
[ ] Agent layer does not emit Events directly.
[ ] Event references are trace only.
[ ] Event visibility follows Permission/Policy.
[ ] Audit Context is preserved.
[ ] Event versioning fails closed.
[ ] Errors are safe.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now duplicate/event behavior.
```

---

# 26. Validation Report Template

```text
Validation: Idempotency Event
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Idempotency / Event Trace

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Operation / Event:
- Service / API / Workflow / Agent:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 27. Codex Usage

Codex must use this validation:

```text
before implementing TASK-005-idempotency-event-trace
before implementing API validators
before implementing workflow validators
before implementing MVP execution spine
after modifying Event specs
after modifying Idempotency behavior
during PR review
```

Codex must not:

```text
skip idempotency for create/apply
treat same key + different payload as replay
allow replay duplicate effects
emit Events from API/Workflow/Agent layers
treat Events as commands
use Event references as triggers
leak restricted Event payload
skip Event visibility policy
skip VersionUnsupported behavior
```

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Idempotency Event Validation. Defines duplicate-sensitive operation coverage, semantic request comparison, safe replay, conflict behavior, Event record shape, ownership, references, visibility, Audit Context, API/Workflow/Agent boundaries, versioning, error safety and test traceability validation. |

---

**End of Idempotency Event Validation**
