# TASK-005 — Idempotency Event Trace

**Task ID:** TASK-005  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-005-idempotency-event-trace.md  
**Task Title:** Idempotency Event Trace  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Common Contracts:** core-specs/contracts/common/idempotency.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/versioning.md  
**Related API Contract:** core-specs/contracts/api/event-api-contract.md  
**Related Test Contract:** core-specs/contracts/tests/idempotency-event-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Idempotency Level 3; Event Trace Level 2/3  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements duplicate-safe execution primitives and event trace behavior for MarkOrbit Core MVP.

It ensures that duplicate-sensitive operations can be safely retried without creating duplicate objects, Tasks, Communications, routing selections or Events.

It also ensures that Events are treated as trace records, not commands.

This task is required before API validators, Workflow validators and MVP execution spine can safely expand.

---

# 2. Core Lock

```text
Idempotency prevents duplicate effects across retries and replays.
Same key and same semantic request must replay safely.
Same key and different semantic request must fail safely.
Events preserve trace.
Events are not commands.
Events are emitted only by owning services.
API, Workflow and Agent layers must not emit Events directly.
Event references must not trigger downstream actions.
Permission and Policy govern Event visibility.
Restricted Event data must not leak.
Codex implements duplicate safety and trace behavior.
Codex does not create event-driven command execution.
```

---

# 3. Required Source Files

Codex must read these files before implementation:

```text
core-specs/DEVELOPER_START_HERE.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/codex/CODEX-TASK-INDEX.md
codex-tasks/TASK-001-common-contract-foundation.md
codex-tasks/TASK-002-contract-fixture-system.md
codex-tasks/TASK-003-common-contract-tests.md
codex-tasks/TASK-004-permission-policy-hooks.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/versioning.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/services/event-service.md
core-specs/objects/event-object.md
```

Codex must also consult relevant Event Specs:

```text
core-specs/events/*.md
```

and relevant API / Workflow contracts where duplicate-sensitive operations exist:

```text
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
```

---

# 4. Scope

This task covers:

```text
idempotency key validation
idempotency semantic request fingerprinting
safe replay behavior
idempotency conflict behavior
duplicate object effect prevention marker
duplicate Task prevention marker
duplicate Communication prevention marker
duplicate Event prevention marker
audit correlation context
event reference validation
event ownership enforcement
event visibility policy hook
event safe payload shape
event non-duplication tests
event reference not command tests
API/Workflow/Agent no-direct-event-emission tests
```

At MVP level, idempotency may be implemented with an in-memory, file-backed or simple persistence adapter if no production persistence exists yet, but behavior must be deterministic and testable.

---

# 5. Out of Scope

This task must not implement:

```text
full event streaming platform
Kafka or equivalent event bus
event sourcing as system-of-record
distributed workflow orchestration
production audit dashboard
external observability vendor integration
official filing event integration
payment event integration
notification delivery integration
```

This task implements duplicate safety and trace primitives, not a full event infrastructure platform.

---

# 6. Implementation Depth

## 6.1 Idempotency Depth

MVP Idempotency depth:

```text
Level 3 for duplicate-sensitive create/apply operations.
```

Required behavior:

```text
missing idempotency_key rejected where required
same idempotency_key + same semantic request = safe replay
same idempotency_key + different semantic request = IdempotencyConflict
replay returns original or linked reference IDs where allowed
replay creates no duplicate side effects
conflict does not expose original restricted payload
```

## 6.2 Event Trace Depth

MVP Event trace depth:

```text
Level 2 for event records and visibility hooks.
Level 3 for non-duplication and no-direct-emission tests.
```

Required behavior:

```text
Event records are trace.
Event references are not commands.
Events are emitted by owning services only.
Event payloads are safe.
Event visibility follows Permission and Policy.
```

---

# 7. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/contracts/common/idempotency.py
core/contracts/common/audit_context.py
core/events/event_record.py
core/events/event_store.py
core/events/event_visibility.py
core/events/event_ownership.py
core/events/event_reference.py
```

Preferred TypeScript-like shape:

```text
src/core/contracts/common/idempotency.ts
src/core/contracts/common/audit-context.ts
src/core/events/event-record.ts
src/core/events/event-store.ts
src/core/events/event-visibility.ts
src/core/events/event-ownership.ts
src/core/events/event-reference.ts
```

Suggested tests:

```text
tests/contracts/test_idempotency_event_trace.py
tests/contracts/test_idempotency_replay_conflict.py
tests/contracts/test_event_ownership.py
tests/contracts/test_event_visibility.py
tests/contracts/test_event_reference_not_command.py
```

---

# 8. Idempotency Required Behavior

## 8.1 Idempotency Key Requirement

Duplicate-sensitive operations must require:

```text
idempotency_key
```

Duplicate-sensitive MVP operations include:

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

Missing idempotency key must return:

```text
IdempotencyKeyRequired
```

## 8.2 Safe Replay

Safe replay means:

```text
same idempotency_key
same semantic request
same actor/context scope where required
no duplicate side effects
same or linked safe response returned
```

Replay must not create duplicate:

```text
Customer
Brand
Trademark
Matter
Order
Document
Evidence
Task
Communication
Routing selection
Event
```

## 8.3 Conflict

Conflict means:

```text
same idempotency_key
different semantic request
```

Must return:

```text
IdempotencyConflict
```

Conflict must not:

```text
mutate state
emit new event
create duplicate object
expose original restricted payload
expose hidden target existence
```

---

# 9. Semantic Request Fingerprint

Codex must implement a deterministic semantic fingerprint or equivalent comparison.

Fingerprint should consider:

```text
operation_key
actor_reference_id where required
organization_reference_id where required
target_reference_id where required
normalized request payload
contract_version
schema_version where applicable
```

Fingerprint should exclude:

```text
correlation_id
request timestamp
non-semantic client metadata
transient retry metadata
```

Fingerprint rules must be deterministic.

---

# 10. Event Record Required Shape

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

Rules:

```text
event_reference_id must follow Reference Contract.
source_service must be the owning service.
payload must be safe and policy-aware.
visibility must support Permission and Policy restrictions.
schema_version must be present.
```

---

# 11. Event Ownership Rules

Codex must enforce:

```text
TaskCreated emitted only by Task Service.
CommunicationCreated emitted only by Communication Service.
CommunicationReviewed emitted only by Communication Service.
CommunicationSent emitted only by Communication Service.
WorkflowContractPreviewed emitted only by Workflow Contract Service.
WorkflowContractApplied emitted only by Workflow Contract Service.
PermissionEvaluated emitted only by Permission Service.
PolicyEvaluated emitted only by Policy Service.
RoutingEvaluated emitted only by Routing Service.
RoutingSelected emitted only by Routing Service.
```

API layer must not emit Events directly.

Workflow layer must not emit domain Events directly.

Agent layer must not emit Events directly.

---

# 12. Event Reference Rules

Event references must be treated as trace only.

Required behavior:

```text
event_reference_id may be validated
event_reference_id may be used for audit correlation
event_reference_id may be used as causation reference
event_reference_id must not trigger downstream action
event_reference_id must not complete Task
event_reference_id must not send Communication
event_reference_id must not apply Workflow
```

Required test:

```text
event_reference_not_command
```

---

# 13. Event Visibility Rules

Event read/search must check:

```text
Permission
Policy
```

Required behavior:

```text
PolicyAllowed returns allowed fields.
PolicyRestrictedRedact omits restricted payload fields.
restricted_fields_omitted is true where redaction occurs.
PolicyNonDisclosureNotFound hides event existence where required.
event payload does not expose policy internals.
event payload does not expose permission internals.
event payload does not expose restricted source data.
```

Event visibility must also apply to idempotent replay response where prior results are now restricted.

---

# 14. Audit Context Rules

Audit Context must preserve:

```text
correlation_id
causation_event_reference_id
event_reference_ids
actor_reference_id where applicable
source_service
```

Rules:

```text
correlation_id groups related operations.
causation_event_reference_id links event cause.
event_reference_ids are trace only.
audit context must not expose restricted data.
```

---

# 15. Required Fixtures

Use fixtures from TASK-002:

```text
MissingIdempotencyKey
ValidFirstRequest
ReplaySameRequest
ConflictDifferentRequest
DuplicateTaskReplay
DuplicateCommunicationReplay
DuplicateEventReplay
VisibleEvent
RestrictedEvent
RedactedEvent
HiddenEvent
DuplicateEventAttempt
EventReferenceNotCommand
CausationEventReference
CorrelationEventGroup
PermissionAllowed
PermissionDenied
PolicyAllowed
PolicyRestrictedRedact
PolicyNonDisclosureNotFound
SupportedContractVersion
UnsupportedContractVersion
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline ad hoc production-like fixtures.
```

---

# 16. Required Tests

This task must implement tests for:

```text
idempotency_key required
same key + same semantic request safe replay
same key + different semantic request IdempotencyConflict
replay does not duplicate objects
replay does not duplicate Tasks
replay does not duplicate Communications
replay does not duplicate Events
conflict does not expose original restricted payload
event record shape
event ownership by source service
API layer no-direct-event-emission
Workflow layer no-direct-event-emission
Agent layer no-direct-event-emission
event reference not command
event visibility PolicyAllowed
event visibility PolicyRestrictedRedact
event visibility PolicyNonDisclosureNotFound
audit correlation preserved
unsupported event/version failure
safe error behavior
```

Required test source:

```text
core-specs/contracts/tests/idempotency-event-tests.md
```

---

# 17. Integration Points for Later Tasks

This task must expose primitives usable by:

```text
TASK-007-api-validator-scaffold
TASK-008-workflow-validator-scaffold
TASK-010-mvp-execution-spine
```

Expected interfaces should support:

```text
require_idempotency_key(...)
check_idempotency_replay_or_conflict(...)
record_idempotent_result(...)
create_event_record(...)
validate_event_reference(...)
enforce_event_visibility(...)
assert_event_emitted_by_owning_service(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 18. Permission / Policy Interaction

Idempotency and Event behavior must respect Permission and Policy.

Required behavior:

```text
PermissionDenied blocks duplicate-sensitive operation before side effect.
PolicyRestricted blocks or redacts before side effect or output.
Idempotent replay must not leak a prior result that current Policy hides.
Event read/search must obey current Permission and Policy.
Restricted event payload must not leak.
```

Required test:

```text
idempotency_replay_does_not_leak_policy_hidden_result
```

---

# 19. Versioning Interaction

Idempotency and Event behavior must respect Versioning.

Required behavior:

```text
unsupported idempotency contract version fails closed
unsupported event schema version fails closed
event records preserve schema_version
historical event versions are not silently rewritten
idempotency fingerprint includes contract_version where required
```

---

# 20. Forbidden Shortcuts

Codex must not:

```text
allow duplicate effects on replay
use idempotency_key without semantic request comparison
treat same key + different request as safe replay
emit Events from API layer
emit Events from Workflow layer
emit Events from Agent layer
treat Event references as commands
use Event as workflow trigger by itself
expose original restricted payload on conflict
expose restricted event payload
ignore current Policy during replay
skip duplicate event tests
skip no-direct-emission tests
skip event-reference-not-command tests
use production data fixtures
introduce full event streaming infrastructure in MVP
```

---

# 21. Acceptance Criteria

This task is complete only if:

```text
[ ] Idempotency key validation exists.
[ ] Missing idempotency key returns IdempotencyKeyRequired where required.
[ ] Same key + same semantic request replays safely.
[ ] Same key + different semantic request returns IdempotencyConflict.
[ ] Replay creates no duplicate object markers.
[ ] Replay creates no duplicate Task markers.
[ ] Replay creates no duplicate Communication markers.
[ ] Replay creates no duplicate Event markers.
[ ] Semantic fingerprinting or equivalent comparison exists.
[ ] Event record shape exists.
[ ] Event ownership enforcement exists or is testable.
[ ] API layer no-direct-event-emission is tested.
[ ] Workflow layer no-direct-event-emission is tested.
[ ] Agent layer no-direct-event-emission is tested.
[ ] Event reference not command behavior is tested.
[ ] Event visibility follows Permission and Policy.
[ ] Restricted event data does not leak.
[ ] Audit correlation is preserved.
[ ] VersionUnsupported behavior exists.
[ ] Tests pass.
```

---

# 22. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Idempotency/Event primitives implemented.
- Files added or changed.
- Which source specs were used.
- Which behavior is Level 2.
- Which behavior is Level 3.
- Which behavior remains stubbed.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- Idempotency key required.
- Replay is safe.
- Conflict is safe.
- Duplicate effects are prevented.
- Events are emitted only by owning services.
- API/Workflow/Agent layers do not emit Events directly.
- Event references are trace, not commands.
- Event visibility follows Permission and Policy.
- Restricted event data does not leak.
- Unsupported versions fail closed.

Deferred
- Full event streaming remains out of scope.
- Full audit dashboard remains out of scope.
- Next task recommended.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-005. Defines Idempotency and Event Trace implementation scope, duplicate-safe behavior, semantic fingerprinting, event ownership, event visibility, audit context, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-005 — Idempotency Event Trace**
