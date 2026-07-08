# Idempotency Event Tests

**Spec ID:** B02-CONTRACT-TESTS-IDEMPOTENCY-EVENT  
**Spec Type:** Test Contract Specification  
**Contract Name:** Idempotency Event Tests  
**Contract File:** core-specs/contracts/tests/idempotency-event-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Event Contracts  
**Related Common Contracts:** core-specs/contracts/common/idempotency.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/versioning.md  
**Related API Contracts:** core-specs/contracts/api/event-api-contract.md; core-specs/contracts/api/task-api-contract.md; core-specs/contracts/api/communication-api-contract.md; core-specs/contracts/api/workflow-contract-api-contract.md; core-specs/contracts/api/routing-api-contract.md; core-specs/contracts/api/*.md  
**Related Workflow Contracts:** core-specs/contracts/workflows/*.md  
**Related Event Specs:** core-specs/events/*.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md; core-specs/contracts/tests/workflow-contract-tests.md; core-specs/contracts/tests/permission-policy-tests.md  
**Related Service Specs:** core-specs/services/event-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/routing-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Idempotency / Event Trace Verification  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Idempotency Event Tests define acceptance-level testing requirements for duplicate-safe execution and event trace behavior across MarkOrbit Core.

They verify:

```text
idempotency key requirements
semantic replay behavior
idempotency conflict behavior
duplicate object prevention
duplicate task prevention
duplicate communication prevention
duplicate workflow effect prevention
duplicate routing selection prevention
duplicate event prevention
event ownership boundary
event trace visibility
event reference behavior
audit context correlation
permission and policy interaction
safe error behavior
version compatibility
Codex implementation acceptance
```

These tests ensure:

```text
Idempotency prevents accidental duplicate execution.
Events preserve trace.
Events are not commands.
Events are emitted only by owning services.
Event visibility follows Policy.
```

---

# 2. Core Lock

```text
Idempotency Event Tests verify duplicate-safe execution and trace integrity.
Idempotency prevents duplicate effects across retries and replays.
Same key and same semantic request must replay safely.
Same key and different semantic request must fail safely.
Events are emitted only by owning services.
API and Workflow layers must not emit Events directly.
Event references are audit trace, not commands.
Permission and Policy govern event visibility.
Restricted event data must not leak.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing idempotency key requirements
testing idempotent replay behavior
testing idempotency conflict behavior
testing duplicate object prevention
testing duplicate side-effect prevention
testing event emission ownership
testing event reference trace behavior
testing audit context correlation
testing event visibility policy
testing event safe errors
testing event versioning
testing API and Workflow idempotency behavior
testing agent-prepared idempotency behavior
```

This Test Contract is not responsible for:

```text
event storage implementation details
database transaction implementation by itself
message broker selection
event streaming infrastructure by itself
observability vendor selection
production incident replay by itself
```

---

# 4. Related Contracts

This test contract validates:

```text
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/api/event-api-contract.md
core-specs/events/*.md
all duplicate-sensitive API Contracts
all workflow apply contracts
```

Rules:

```text
- Every duplicate-sensitive operation must require idempotency_key.
- Every idempotent replay must prevent duplicate effects.
- Every Event must be owned by an owning service.
- API and Workflow layers must not emit Events directly.
- Event references must not trigger commands.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: IdempotencyEventBoundary
  subject_name: Idempotency and Event Trace Boundary
  owning_service:
    - Event Service
    - owning domain services
  contract_file:
    - core-specs/contracts/common/idempotency.md
    - core-specs/contracts/common/audit-context.md
    - core-specs/contracts/api/event-api-contract.md
  behavior_scope:
    - idempotency key validation
    - semantic replay
    - conflict detection
    - duplicate side-effect prevention
    - event ownership
    - event trace
    - event visibility
    - audit correlation
    - event safe errors
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: idempotent-create-fixture
    fixture_type: Idempotency Fixture
    purpose: same key/same create request and same key/different create request
    contains_production_data: false
    required: true

  - fixture_key: idempotent-workflow-apply-fixture
    fixture_type: Workflow Fixture
    purpose: duplicate workflow apply replay and conflict testing
    contains_production_data: false
    required: true

  - fixture_key: idempotent-task-fixture
    fixture_type: Idempotency Fixture
    purpose: duplicate Task creation prevention
    contains_production_data: false
    required: true

  - fixture_key: idempotent-communication-fixture
    fixture_type: Idempotency Fixture
    purpose: duplicate Communication creation prevention
    contains_production_data: false
    required: true

  - fixture_key: idempotent-routing-fixture
    fixture_type: Idempotency Fixture
    purpose: duplicate RoutingSelected prevention
    contains_production_data: false
    required: true

  - fixture_key: event-ownership-fixture
    fixture_type: Event Trace Fixture
    purpose: owning service emission and API/workflow no-direct-emission testing
    contains_production_data: false
    required: true

  - fixture_key: event-reference-fixture
    fixture_type: Event Trace Fixture
    purpose: event reference as trace, not command
    contains_production_data: false
    required: true

  - fixture_key: audit-correlation-fixture
    fixture_type: Event Trace Fixture
    purpose: correlation_id and causation_event_reference_id preservation
    contains_production_data: false
    required: true

  - fixture_key: event-policy-fixture
    fixture_type: Policy Fixture
    purpose: visible, redacted and hidden event trace testing
    contains_production_data: false
    required: true

  - fixture_key: permission-fixture
    fixture_type: Permission Fixture
    purpose: event read and protected operation permission testing
    contains_production_data: false
    required: true

  - fixture_key: error-fixture
    fixture_type: Error Fixture
    purpose: safe idempotency/event errors
    contains_production_data: false
    required: true

  - fixture_key: version-fixture
    fixture_type: Version Fixture
    purpose: supported and unsupported idempotency/event contract versions
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain production data.
- Fixtures must include replay and conflict cases.
- Fixtures must include duplicate side-effect detection.
- Fixtures must include event visibility restrictions.
- Fixtures must include API, workflow and service boundary cases.
```

---

# 7. Idempotency Key Tests

Idempotency key tests must verify:

```text
idempotency_key required for duplicate-sensitive create operations
idempotency_key required for workflow apply
idempotency_key required for routing selection
idempotency_key required for communication send/preparation where duplicate-sensitive
idempotency_key required for task creation batches
missing idempotency_key fails closed
malformed idempotency_key rejected
idempotency_key scope is explicit
```

Test skeleton:

```yaml
idempotency_key_tests:
  - test_key: idempotency-key-required
    test_title: Duplicate-Sensitive Operation Requires Idempotency Key
    given:
      - duplicate-sensitive operation
      - missing idempotency_key
    when:
      - operation is evaluated
    then:
      - IdempotencyKeyRequired is returned
      - no duplicate-sensitive action occurs
```

---

# 8. Idempotent Replay Tests

Replay tests must verify:

```text
same idempotency_key + same semantic request returns safe replay
safe replay returns same or equivalent reference IDs
safe replay does not create duplicate object
safe replay does not create duplicate Task
safe replay does not create duplicate Communication
safe replay does not create duplicate Event
safe replay preserves correlation where required
```

Test skeleton:

```yaml
replay_tests:
  - test_key: idempotent-replay-same-request
    test_title: Same Key and Same Semantic Request Replays Safely
    given:
      - idempotency_key
      - first successful request
    when:
      - same semantic request is replayed
    then:
      - response is safe replay
      - original reference IDs are returned or linked
      - no duplicate object is created
      - no duplicate event is emitted
```

---

# 9. Idempotency Conflict Tests

Conflict tests must verify:

```text
same idempotency_key + different semantic request returns IdempotencyConflict
conflict does not mutate state
conflict does not emit duplicate event
conflict error is safe
conflict does not expose original restricted payload
```

Test skeleton:

```yaml
conflict_tests:
  - test_key: idempotency-conflict-different-request
    test_title: Same Key with Different Semantic Request Fails Safely
    given:
      - idempotency_key used for previous semantic request
      - different semantic request with same key
    when:
      - operation is evaluated
    then:
      - IdempotencyConflict is returned
      - no protected action occurs
      - no restricted original payload is exposed
```

---

# 10. Duplicate Object Prevention Tests

Duplicate object prevention tests must include:

```text
duplicate create does not duplicate Customer
duplicate create does not duplicate Trademark
duplicate create does not duplicate Matter
duplicate create does not duplicate Order
duplicate create does not duplicate Document
duplicate create does not duplicate Evidence
duplicate create does not duplicate Task
duplicate create does not duplicate Communication
duplicate create does not duplicate Notification
duplicate routing selection does not duplicate selected provider state
```

Test skeleton:

```yaml
duplicate_object_tests:
  - test_key: duplicate-task-not-created
    test_title: Duplicate Request Does Not Duplicate Task
    given:
      - first Task creation request succeeds
      - replay with same idempotency_key
    when:
      - replay is executed
    then:
      - no second Task is created
      - original task_reference_id is returned or linked
      - TaskCreated event is not duplicated
```

---

# 11. Workflow Apply Idempotency Tests

Workflow apply tests must verify:

```text
workflow apply requires idempotency_key
duplicate apply returns safe replay
duplicate apply does not duplicate Tasks
duplicate apply does not duplicate Communications
duplicate apply does not duplicate Documents
duplicate apply does not duplicate Evidence records
duplicate apply does not duplicate Matter or Order
duplicate apply does not duplicate RoutingSelected event
duplicate apply does not duplicate WorkflowContractApplied event
same key + different apply scope returns IdempotencyConflict
```

Test skeleton:

```yaml
workflow_idempotency_tests:
  - test_key: workflow-apply-no-duplicate-effects
    test_title: Duplicate Workflow Apply Does Not Duplicate Effects
    given:
      - first workflow apply succeeds
      - same workflow apply is replayed with same idempotency_key
    when:
      - replay is evaluated
    then:
      - no duplicate Task is created
      - no duplicate Communication is created
      - no duplicate WorkflowContractApplied event is emitted
```

---

# 12. Event Ownership Tests

Event ownership tests must verify:

```text
Event Service owns event records and retrieval behavior
owning domain services emit their own events
TaskCreated emitted only by Task Service
CommunicationCreated emitted only by Communication Service
RoutingEvaluated and RoutingSelected emitted only by Routing Service
WorkflowContractApplied emitted only by Workflow Contract Service
PermissionEvaluated emitted only by Permission Service
PolicyEvaluated emitted only by Policy Service
API layer does not emit Events directly
Workflow layer does not emit domain Events directly
Agent layer does not emit Events directly
```

Test skeleton:

```yaml
event_ownership_tests:
  - test_key: event-emitted-by-owning-service
    test_title: Event Is Emitted by Owning Service
    given:
      - operation that creates a Task
    when:
      - operation completes
    then:
      - Task Service emits TaskCreated
      - API/Workflow/Agent layer does not emit TaskCreated
```

---

# 13. Event Reference Tests

Event reference tests must verify:

```text
event_reference_id follows Reference Contract
event_reference_id does not expose database ID
event_reference_id is audit trace only
event_reference_id does not trigger action
causation_event_reference_id preserves trace
correlation_id groups related operations
event_reference_ids returned only where policy allows
```

Test skeleton:

```yaml
event_reference_tests:
  - test_key: event-reference-not-command
    test_title: Event Reference Is Not a Command
    given:
      - event_reference_id in request or audit context
    when:
      - operation reads event reference
    then:
      - event may be validated as trace
      - no downstream action is triggered by event reference alone
```

---

# 14. Audit Correlation Tests

Audit correlation tests must verify:

```text
correlation_id preserved across API → Service → Event
causation_event_reference_id preserved where allowed
workflow_application_reference_id links workflow events
idempotent replay preserves or links original correlation context
audit context does not expose restricted data
```

Test skeleton:

```yaml
audit_correlation_tests:
  - test_key: correlation-preserved
    test_title: Correlation ID Is Preserved Across Operation
    given:
      - request with correlation_id
    when:
      - operation completes
    then:
      - response preserves correlation_id
      - emitted event trace includes correlation_id where allowed
```

---

# 15. Event Visibility Policy Tests

Event visibility tests must verify:

```text
event read requires Permission
event visibility requires Policy
PolicyAllowed returns allowed event fields
PolicyRestricted redacts event payload fields
restricted_fields_omitted is true where redaction occurs
Policy non-disclosure may return NotFound
hidden events do not affect visible total_count where policy restricts count
event payload does not expose policy internals
```

Test skeleton:

```yaml
event_visibility_tests:
  - test_key: event-policy-redaction
    test_title: Event Payload Is Redacted by Policy
    given:
      - event exists
      - PermissionAllowed
      - PolicyRestricted redaction decision
    when:
      - event is read
    then:
      - restricted event fields are omitted
      - restricted_fields_omitted is true
      - policy internals are not exposed
```

---

# 16. Event API Tests

Event API tests must verify:

```text
event-api read validates event_reference_id
event-api search/list applies Permission and Policy
event-api search/list applies pagination contract
event-api does not create arbitrary events from external callers unless explicitly allowed by Event Service contract
event-api errors are safe
event-api unsupported version fails closed
```

Test skeleton:

```yaml
event_api_tests:
  - test_key: event-api-read-policy
    test_title: Event API Read Applies Permission and Policy
    given:
      - event_reference_id
      - PermissionAllowed
      - PolicyRestricted
    when:
      - Event API read is evaluated
    then:
      - event details are redacted or hidden
      - restricted_fields_omitted is true where redacted
```

---

# 17. Event Non-Duplication Tests

Event non-duplication tests must verify:

```text
idempotent replay does not duplicate Events
duplicate Task creation does not duplicate TaskCreated
duplicate Communication creation does not duplicate CommunicationCreated
duplicate Workflow apply does not duplicate WorkflowContractApplied
duplicate Routing selection does not duplicate RoutingSelected
duplicate Permission/Policy evaluation replay does not create misleading duplicate trace unless explicitly modeled
```

Test skeleton:

```yaml
event_non_duplication_tests:
  - test_key: replay-no-duplicate-event
    test_title: Idempotent Replay Does Not Duplicate Event
    given:
      - first operation emits event
      - replay with same idempotency_key
    when:
      - replay completes
    then:
      - no duplicate event is emitted
      - original event_reference_id is returned or linked where allowed
```

---

# 18. Agent-Prepared Idempotency Tests

Agent-prepared idempotency tests must verify:

```text
agent-prepared downstream action requires idempotency_key
agent output cannot bypass idempotency
duplicate agent-prepared task plan does not duplicate Tasks
duplicate agent-prepared communication draft does not duplicate Communication
duplicate agent-prepared routing recommendation does not duplicate selection
agent cannot emit Events directly
```

Test skeleton:

```yaml
agent_idempotency_tests:
  - test_key: agent-prepared-task-plan-idempotent
    test_title: Agent-Prepared Task Plan Does Not Duplicate Tasks
    given:
      - agent-prepared task plan
      - create_tasks request with idempotency_key
    when:
      - same request is replayed
    then:
      - no duplicate Tasks are created
      - Task Service owns created Tasks
      - TaskCreated event is not duplicated
```

---

# 19. Permission / Policy Interaction Tests

Permission and Policy interaction tests must verify:

```text
PermissionDenied blocks duplicate-sensitive operation before side effect
PolicyRestricted blocks or downgrades before side effect
PolicyRestricted can hide prior idempotency result where non-disclosure required
idempotency replay must not leak restricted prior result
event trace visibility follows current Policy
```

Test skeleton:

```yaml
permission_policy_interaction_tests:
  - test_key: idempotency-replay-does-not-leak-policy-hidden-result
    test_title: Idempotency Replay Does Not Leak Policy-Hidden Result
    given:
      - previous successful request
      - replaying actor now lacks policy visibility
    when:
      - replay is evaluated
    then:
      - response is redacted or hidden according to Policy
      - original restricted result is not exposed
```

---

# 20. Error Safety Tests

Idempotency and Event error tests must verify:

```text
IdempotencyKeyRequired uses safe error shape
IdempotencyConflict uses safe error shape
EventReferenceInvalid uses safe error shape
PermissionDenied uses safe error shape
PolicyRestricted uses safe error shape
VersionUnsupported uses safe error shape
database IDs not exposed
original request payload not exposed
event payload not exposed where restricted
policy internals not exposed
permission internals not exposed
correlation_id preserved
retryable flag present
```

Test skeleton:

```yaml
error_safety_tests:
  - test_key: idempotency-conflict-safe-error
    test_title: Idempotency Conflict Error Is Safe
    given:
      - conflicting idempotency request
      - original request contained restricted fields
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - original payload is not exposed
      - restricted fields are not exposed
```

---

# 21. Versioning Tests

Versioning tests must verify:

```text
supported idempotency contract version accepted
supported event contract version accepted
supported event spec version accepted
missing required version rejected
unsupported idempotency version rejected
unsupported event version rejected
event schema version preserved in trace where required
historical events remain readable with version context
deprecated event version not silently rewritten
```

Test skeleton:

```yaml
versioning_tests:
  - test_key: event-version-unsupported
    test_title: Unsupported Event Version Fails Closed
    given:
      - unsupported event contract version
    when:
      - event operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 22. Contract Coverage Matrix

```yaml
coverage_matrix:
  idempotency_key:
    required: true
    covered_by:
      - idempotency-key-required
  replay:
    required: true
    covered_by:
      - idempotent-replay-same-request
  conflict:
    required: true
    covered_by:
      - idempotency-conflict-different-request
  duplicate_objects:
    required: true
    covered_by:
      - duplicate-task-not-created
  workflow_apply:
    required: true
    covered_by:
      - workflow-apply-no-duplicate-effects
  event_ownership:
    required: true
    covered_by:
      - event-emitted-by-owning-service
  event_reference:
    required: true
    covered_by:
      - event-reference-not-command
  audit_correlation:
    required: true
    covered_by:
      - correlation-preserved
  event_visibility:
    required: true
    covered_by:
      - event-policy-redaction
  event_api:
    required: true
    covered_by:
      - event-api-read-policy
  event_non_duplication:
    required: true
    covered_by:
      - replay-no-duplicate-event
  agent_prepared:
    required: true
    covered_by:
      - agent-prepared-task-plan-idempotent
  permission_policy_interaction:
    required: true
    covered_by:
      - idempotency-replay-does-not-leak-policy-hidden-result
  errors:
    required: true
    covered_by:
      - idempotency-conflict-safe-error
  versioning:
    required: true
    covered_by:
      - event-version-unsupported
```

---

# 23. Codex Implementation Notes

Codex must:

```text
cite this Idempotency Event Tests file
cite Idempotency Contract
cite Audit Context Contract
cite Event API Contract
cite related Event Specs
cite related API Contracts for duplicate-sensitive operations
cite related Workflow Contracts for apply operations
cite Event Service Spec
cite owning Service Specs for event emission
generate deterministic non-production fixtures
write idempotency key tests
write replay tests
write conflict tests
write duplicate object prevention tests
write workflow apply idempotency tests
write event ownership tests
write event reference tests
write audit correlation tests
write event visibility policy tests
write event API tests
write event non-duplication tests
write agent-prepared idempotency tests
write Permission/Policy interaction tests
write safe error tests
write VersionUnsupported tests
assert no direct event emission from API/Workflow/Agent layers
assert event references are trace, not commands
assert restricted event data is not leaked
```

Codex must not:

```text
treat retry tests as optional
allow duplicate side effects on replay
allow same idempotency_key for different semantic requests
emit events from API layer
emit events from Workflow layer
emit events from Agent layer
treat event references as commands
expose original restricted payload on conflict
expose restricted event data
ignore current Policy during replay
ignore event versioning
```

---

# 24. Acceptance Criteria

This Idempotency Event Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Common, API, Workflow and Event Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines Idempotency Key tests.
[ ] It defines Idempotent Replay tests.
[ ] It defines Idempotency Conflict tests.
[ ] It defines Duplicate Object Prevention tests.
[ ] It defines Workflow Apply Idempotency tests.
[ ] It defines Event Ownership tests.
[ ] It defines Event Reference tests.
[ ] It defines Audit Correlation tests.
[ ] It defines Event Visibility Policy tests.
[ ] It defines Event API tests.
[ ] It defines Event Non-Duplication tests.
[ ] It defines Agent-Prepared Idempotency tests.
[ ] It defines Permission / Policy Interaction tests.
[ ] It defines Error Safety tests.
[ ] It defines Versioning tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 25. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Idempotency Event Tests. Defines idempotency key, replay, conflict, duplicate object prevention, workflow apply idempotency, event ownership, event reference, audit correlation, event visibility, event API, event non-duplication, agent-prepared idempotency, permission/policy interaction, safe errors, versioning and Codex expectations. |

---

**End of Idempotency Event Tests**
