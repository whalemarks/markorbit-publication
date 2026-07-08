# TASK-003 — Common Contract Tests

**Task ID:** TASK-003  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-003-common-contract-tests.md  
**Task Title:** Common Contract Tests  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Test Contract:** core-specs/contracts/tests/common-contract-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 3 for common contract test verification  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements the Common Contract test suite for MarkOrbit Core.

It verifies that the Common Contract primitives created in TASK-001 and fixtures created in TASK-002 behave according to Book 02 contract governance.

This task is required before API, Workflow, Agent or MVP execution implementation expands.

Common Contract Tests must verify:

```text
Reference Contract behavior
Error Contract behavior
Pagination Contract behavior
Audit Context behavior
Permission Context behavior
Policy Context behavior
AI Context behavior
Human Review Contract behavior
Idempotency Contract behavior
Versioning Contract behavior
Cross-Contract consistency
safe failure behavior
negative cases
```

---

# 2. Core Lock

```text
Common Contract Tests verify shared Core primitives.
Tests must enforce boundaries, not weaken them.
References must not expose database IDs.
Errors must remain safe.
Pagination must respect Policy.
Audit Context must preserve trace without becoming command.
Permission and Policy must fail closed.
AI Context must prevent forbidden AI actions.
Human Review must not execute downstream actions.
Idempotency must prevent duplicate effects.
Versioning must fail closed for unsupported versions.
Codex must write negative tests, not only happy-path tests.
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
core-specs/contracts/common/index.md
core-specs/contracts/tests/index.md
core-specs/contracts/tests/template.md
core-specs/contracts/tests/common-contract-tests.md
```

Codex must also read these Common Contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/pagination.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/versioning.md
```

---

# 4. Scope

This task covers tests for:

```text
Reference validation
Safe Error behavior
Pagination shape and policy count omission
Audit Context shape and event trace behavior
AI Context boundary validation
Human Review gate validation
Permission Context fail-closed behavior
Policy Context restricted/redacted/review-required behavior
Idempotency key/replay/conflict behavior
Versioning supported/unsupported/missing behavior
Cross-Contract consistency
```

This task may also improve TASK-001 implementation if tests reveal gaps.

---

# 5. Out of Scope

This task must not implement:

```text
new domain services
API endpoint behavior
workflow preview/apply behavior
agent runtime
full policy engine
full workflow engine
production event bus
product UI
external integrations
```

This task is for Common Contract verification only.

---

# 6. Suggested Test Structure

Codex may adapt to the repo test framework.

Preferred structure:

```text
tests/
  contracts/
    test_common_contracts.py
    test_reference_contract.py
    test_error_contract.py
    test_pagination_contract.py
    test_audit_context_contract.py
    test_ai_context_contract.py
    test_human_review_contract.py
    test_permission_context_contract.py
    test_policy_context_contract.py
    test_idempotency_contract.py
    test_versioning_contract.py
    test_cross_contract_consistency.py
```

If a single test file is preferred initially:

```text
tests/contracts/test_common_contracts.py
```

is acceptable, but it must remain organized by contract primitive.

---

# 7. Required Fixture Usage

Tests must use fixtures from TASK-002.

Required fixture families:

```text
references
errors
permissions
policies
ai
human_review
idempotency
events
versions
```

Tests must not create hidden ad hoc production-like data.

If additional fixtures are needed:

```text
Add them to the fixture system.
Do not inline large fixtures inside tests.
Do not use production data.
```

---

# 8. Required Test Groups

## 8.1 Reference Contract Tests

Must test:

```text
valid public reference accepted
invalid reference rejected
wrong-type reference rejected
database ID-like reference rejected
hidden object reference does not leak existence
valid reference does not imply permission
```

Expected errors:

```text
ReferenceInvalid
PermissionDenied or NotFound where policy requires non-disclosure
```

## 8.2 Error Contract Tests

Must test:

```text
controlled error code exists
safe message exists
safe_detail is safe
correlation_id preserved
retryable flag present
no stack trace exposed
no database ID exposed
no restricted data exposed
no policy internals exposed
no permission internals exposed
no prompt internals or hidden reasoning exposed
```

Required error codes:

```text
ValidationFailed
ReferenceInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
StateInvalid
InternalError
```

## 8.3 Pagination Contract Tests

Must test:

```text
limit validation
cursor validation
next_cursor behavior
items shape
total_count allowed where policy allows
total_count_omitted where policy restricts
pagination does not leak hidden object count
```

## 8.4 Audit Context Tests

Must test:

```text
correlation_id accepted
causation_event_reference_id accepted
event_reference_ids accepted
event references validated as references
event references do not trigger commands
audit context does not expose restricted fields
```

## 8.5 AI Context Tests

Must test:

```text
valid AI context accepted
missing capability_scope rejected
missing source_scope rejected
policy_omissions_disclosed required where omissions exist
AI forbidden action approve rejected
AI forbidden action send rejected
AI forbidden action submit rejected
AI forbidden action certify rejected
AI output cannot claim professional truth
human_review_required preserved
```

## 8.6 Human Review Contract Tests

Must test:

```text
valid human_review_reference_id accepted
missing human review returns HumanReviewRequired
rejected review not accepted
expired review not accepted where fixture requires freshness
wrong reviewer not accepted where reviewer scope matters
human review does not execute downstream action
```

## 8.7 Permission Context Tests

Must test:

```text
PermissionAllowed accepted
PermissionDenied blocks protected action
UnknownPermission fails closed
MissingPermissionContext fails closed
permission approval alone does not imply policy approval
permission decision internals not exposed
```

## 8.8 Policy Context Tests

Must test:

```text
PolicyAllowed accepted
PolicyRestrictedBlock blocks action
PolicyRestrictedRedact redacts output
PolicyRequiresHumanReview returns HumanReviewRequired
PolicyNonDisclosureNotFound hides existence
UnknownPolicy fails closed
MissingPolicyContext fails closed
policy allowance alone does not imply permission approval
restricted_fields_omitted is true where redaction occurs
```

## 8.9 Idempotency Contract Tests

Must test:

```text
missing idempotency_key rejected
valid first request accepted
same key + same semantic request replays safely
same key + different semantic request returns IdempotencyConflict
replay does not duplicate object marker
replay does not duplicate Task marker
replay does not duplicate Communication marker
replay does not duplicate Event marker
conflict does not leak original restricted payload
```

## 8.10 Versioning Contract Tests

Must test:

```text
supported contract_version accepted
unsupported contract_version returns VersionUnsupported
missing contract_version rejected
supported schema_version accepted
unsupported schema_version rejected
deprecated version not silently rewritten
historical version record preserved where applicable
```

## 8.11 Cross-Contract Consistency Tests

Must test:

```text
ReferenceInvalid uses Error Contract
PermissionDenied uses Error Contract
PolicyRestricted uses Error Contract
HumanReviewRequired uses Error Contract
IdempotencyConflict uses Error Contract
VersionUnsupported uses Error Contract
AI Context respects Policy omissions
Human Review does not bypass Permission
Human Review does not bypass Policy
Idempotency replay respects current Policy visibility
Event references are trace and not commands
```

---

# 9. Negative Test Requirements

The test suite must include negative tests for:

```text
database ID leakage
stack trace leakage
restricted field leakage
policy internals leakage
permission internals leakage
prompt internals leakage
AI forbidden actions
missing human review
permission denied
unknown permission
policy restricted
unknown policy
missing idempotency key
idempotency conflict
unsupported version
event reference treated as command
```

Happy-path tests alone are not acceptable.

---

# 10. Required Assertions

Tests must assert:

```text
no raw database IDs appear in public output
no stack traces appear in errors
no restricted fields appear when redacted
restricted_fields_omitted is true when redaction occurs
policy_omissions_disclosed is true when AI output omits policy-restricted sources
human_review_required is true when review is required
idempotent replay does not duplicate effects
VersionUnsupported appears for unsupported versions
event_reference_id is not used as command
PermissionDenied and PolicyRestricted fail closed
```

---

# 11. Dependency Handling

This task depends on:

```text
TASK-001-common-contract-foundation
TASK-002-contract-fixture-system
```

If TASK-001 is incomplete:

```text
Do not create fake implementation just to pass tests.
Mark runtime tests blocked.
Implement fixture integrity and expected-behavior tests only.
```

If TASK-002 is incomplete:

```text
Do not inline large ad hoc fixtures.
Create missing fixtures in the fixture system.
Update TASK-002 summary accordingly.
```

---

# 12. Forbidden Shortcuts

Codex must not:

```text
skip negative tests
only test happy paths
mock Permission as always allowed
mock Policy as always allowed
ignore UnknownPermission
ignore UnknownPolicy
ignore redaction assertions
ignore human review gates
ignore AI forbidden actions
ignore idempotency conflict
ignore unsupported version
use production data
use raw database IDs except in rejection fixtures
expose stack traces
change architecture to pass tests
```

---

# 13. Acceptance Criteria

This task is complete only if:

```text
[ ] Reference Contract tests exist.
[ ] Error Contract tests exist.
[ ] Pagination Contract tests exist.
[ ] Audit Context tests exist.
[ ] AI Context tests exist.
[ ] Human Review Contract tests exist.
[ ] Permission Context tests exist.
[ ] Policy Context tests exist.
[ ] Idempotency Contract tests exist.
[ ] Versioning Contract tests exist.
[ ] Cross-Contract Consistency tests exist.
[ ] Required fixtures are used.
[ ] Negative tests exist.
[ ] Database ID leakage is tested.
[ ] Safe error behavior is tested.
[ ] Permission and Policy fail-closed behavior is tested.
[ ] AI forbidden actions are tested.
[ ] Human Review gate behavior is tested.
[ ] Idempotency replay/conflict is tested.
[ ] VersionUnsupported is tested.
[ ] Event reference not command behavior is tested.
[ ] Tests pass or blocked tests are explicitly explained.
```

---

# 14. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Common Contract test files added or changed.
- Which contracts are covered.
- Which fixtures were used.
- Which implementation gaps were found and fixed.
- Which tests remain blocked, if any.

Tests
- Commands run.
- Results.

Boundary Confirmation
- References hide database IDs.
- Errors are safe.
- Pagination respects Policy.
- Audit Context preserves trace only.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Permission and Policy fail closed.
- Idempotency replay/conflict verified.
- Unsupported versions fail closed.
- Event references are trace, not commands.

Deferred
- Any tests deferred and why.
- Next task recommended.
```

---

# 15. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-003. Defines Common Contract Tests implementation scope, required sources, fixture usage, test groups, negative tests, required assertions, dependencies, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-003 — Common Contract Tests**
