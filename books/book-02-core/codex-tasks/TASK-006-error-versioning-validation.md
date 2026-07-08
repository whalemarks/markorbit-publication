# TASK-006 — Error Versioning Validation

**Task ID:** TASK-006  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-006-error-versioning-validation.md  
**Task Title:** Error Versioning Validation  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md; codex-tasks/TASK-005-idempotency-event-trace.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Common Contracts:** core-specs/contracts/common/errors.md; core-specs/contracts/common/versioning.md; core-specs/contracts/common/references.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md  
**Related Test Contract:** core-specs/contracts/tests/error-versioning-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Error Level 3; Versioning Level 1  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements safe error behavior and version validation for MarkOrbit Core MVP.

It ensures that every failure path returns a controlled, safe, traceable error and that unsupported or missing versions fail closed.

This task is required before API validators, Workflow validators and MVP execution spine can safely expand.

It implements the rule:

```text
Errors must be safe.
Unsupported versions must fail closed.
Historical versions must not be silently rewritten.
```

---

# 2. Core Lock

```text
Errors must be controlled, safe and traceable.
Errors must not expose restricted data, database IDs, stack traces, policy internals, permission internals, prompt internals or hidden reasoning.
Unsupported versions must fail closed.
Missing required versions must fail safely.
Breaking changes require version bumps.
Historical objects, workflow applications, events and agent outputs must preserve the version used.
Deprecated versions must not be silently rewritten.
Codex implements error and version validation.
Codex does not weaken safe failure behavior for convenience.
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
codex-tasks/TASK-005-idempotency-event-trace.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/versioning.md
core-specs/contracts/common/references.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/tests/error-versioning-tests.md
```

Codex must also consult:

```text
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/agent-boundary-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
```

---

# 4. Scope

This task covers:

```text
safe error shape
controlled error codes
safe_detail validation
correlation_id preservation
retryable flag behavior
restricted data leakage prevention
database ID leakage prevention
stack trace leakage prevention
policy/permission internal leakage prevention
AI prompt and hidden reasoning leakage prevention
NotFound substitution support
VersionUnsupported behavior
missing version behavior
version mismatch behavior
deprecated version behavior
historical version preservation
error/version test coverage
```

---

# 5. Out of Scope

This task must not implement:

```text
production incident management
logging vendor integration
full observability platform
full migration engine
backward compatibility service
deprecation lifecycle automation
API gateway version routing
release management process
security monitoring dashboard
```

This task implements safe error and MVP version validation primitives.

---

# 6. Implementation Depth

## 6.1 Error Depth

MVP Error depth:

```text
Level 3 — real enforcement.
```

Required behavior:

```text
every known failure path uses controlled error shape
unsafe internal errors are sanitized
restricted data is not leaked
database IDs are not leaked
correlation_id is preserved
retryable flag is present
```

## 6.2 Versioning Depth

MVP Versioning depth:

```text
Level 1 — schema validation and fail-closed unsupported version behavior.
```

Required behavior:

```text
contract_version validation
schema_version validation where applicable
supported version allowlist
unsupported version returns VersionUnsupported
missing required version fails safely
historical version field preserved where a record is created
```

---

# 7. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/contracts/common/errors.py
core/contracts/common/versioning.py
core/errors/safe_error.py
core/errors/error_codes.py
core/errors/leakage_guard.py
core/versioning/version_registry.py
core/versioning/version_validator.py
```

Preferred TypeScript-like shape:

```text
src/core/contracts/common/errors.ts
src/core/contracts/common/versioning.ts
src/core/errors/safe-error.ts
src/core/errors/error-codes.ts
src/core/errors/leakage-guard.ts
src/core/versioning/version-registry.ts
src/core/versioning/version-validator.ts
```

Suggested tests:

```text
tests/contracts/test_error_versioning_validation.py
tests/contracts/test_safe_errors.py
tests/contracts/test_error_leakage_prevention.py
tests/contracts/test_version_validation.py
tests/contracts/test_historical_version_trace.py
```

---

# 8. Error Shape Requirements

Every safe error must support:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: object | string | null
  correlation_id: string | null
  retryable: boolean
  restricted_fields_omitted: boolean | null
```

Required rules:

```text
error.code must be controlled.
error.category must be controlled.
error.message must be safe.
error.safe_detail must be safe.
error.correlation_id must preserve request correlation_id where provided.
error.retryable must be explicit.
restricted_fields_omitted must be true where redaction affects error output.
```

---

# 9. Required Controlled Error Codes

Codex must support the following controlled error codes:

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
NotFound
Conflict
InternalError
```

Each code must map to:

```text
safe category
safe default message
retryable default
allowed safe_detail shape
```

InternalError must not expose stack traces or internal exception content.

---

# 10. Leakage Prevention Requirements

Errors must not expose:

```text
database IDs
raw customer data
restricted trademark data
restricted documents
evidence content
provider commercial terms
private notes
policy rule internals
permission rule internals
agent prompt internals
hidden chain-of-thought
raw stack traces
secrets or tokens
connector credentials
production file paths
```

Required guard behavior:

```text
detect and block raw database ID-like values where possible
strip stack trace fields
strip internal exception class details from public response
strip restricted fields when policy requires
sanitize model/tool/provider raw errors
```

---

# 11. Non-Disclosure Error Behavior

When Policy requires non-disclosure:

```text
NotFound may replace PolicyRestricted.
Object existence must not be revealed.
safe_detail must not reveal hidden existence.
pagination totals must not reveal hidden objects.
event trace must not reveal hidden events.
idempotency replay must not leak hidden prior result.
```

Required test:

```text
policy_nondisclosure_returns_notfound_without_existence_leak
```

---

# 12. Permission / Policy Error Behavior

Required behavior:

```text
PermissionDenied must be safe.
PolicyRestricted must be safe.
PermissionDenied must not expose permission rule internals.
PolicyRestricted must not expose policy rule internals.
Decision references may be returned only where Policy allows.
Restricted object data must not appear in the error.
```

Required tests:

```text
permission_denied_error_safe
policy_restricted_error_safe
permission_policy_internals_not_exposed
```

---

# 13. AI Error Safety Behavior

AI-related errors must not expose:

```text
system prompts
developer prompts
hidden reasoning
tool raw payloads with restricted data
restricted source contents
provider raw error text containing sensitive context
policy-omitted source details
```

Required behavior:

```text
sanitize AI/tool/model error output
preserve correlation_id
return controlled error code
do not expose hidden reasoning
do not convert AI failure into professional truth
```

Required tests:

```text
ai_error_no_prompt_leakage
ai_error_no_hidden_reasoning_leakage
ai_error_no_restricted_source_leakage
```

---

# 14. Correlation and Retryability

Required behavior:

```text
correlation_id must be preserved in errors where provided
retryable must be true only for safe retry cases
retryable must be false for ValidationFailed, PermissionDenied, PolicyRestricted, HumanReviewRequired, IdempotencyConflict and VersionUnsupported unless a contract explicitly says otherwise
InternalError may be retryable only if safe
```

Required tests:

```text
error_correlation_preserved
non_retryable_governance_errors
```

---

# 15. Version Validation Requirements

Codex must implement validation for:

```text
contract_version
schema_version
api_version where applicable
workflow_contract_version where applicable
event_version or event schema_version where applicable
agent_contract_version where applicable
```

MVP minimum:

```text
contract_version required
schema_version required where applicable
supported version accepted
unsupported version returns VersionUnsupported
missing required version returns VersionUnsupported or ValidationFailed according to contract
version mismatch fails safely where incompatible
```

---

# 16. Supported Version Registry

Codex should create a simple supported version registry or equivalent.

Minimum registry behavior:

```text
list supported contract versions
list supported schema versions where applicable
validate requested version
return VersionUnsupported for unsupported version
```

MVP supported version:

```text
v0.1.0
```

If existing specs use another version form, Codex must preserve consistency and document the mapping.

---

# 17. Deprecated Version Behavior

Deprecated version support is not full MVP scope, but the behavior must not be unsafe.

Required MVP behavior:

```text
deprecated version must not be silently upgraded
deprecated version must not be silently rewritten
warning may be returned if contract supports it
historical records preserve original version
```

Required test:

```text
deprecated_version_not_silently_rewritten
```

---

# 18. Historical Version Preservation

Where records are created, version context must be preserved.

Required records:

```text
Event records
Workflow application records
AI-assisted output records where applicable
created object records where applicable
idempotent result records where applicable
```

Required fields may include:

```text
contract_version
schema_version
workflow_contract_version
agent_contract_version
event_schema_version
```

Required test:

```text
historical_version_preserved
```

---

# 19. Required Fixtures

Use fixtures from TASK-002:

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
InternalErrorSafe
policy_nondisclosure_notfound
ai_error_prompt_leak_attempt
ai_error_hidden_reasoning_attempt
supported_contract_version
unsupported_contract_version
missing_contract_version
supported_schema_version
unsupported_schema_version
deprecated_version
historical_version_record
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline ad hoc production-like fixtures.
```

---

# 20. Required Tests

This task must implement tests for:

```text
safe error shape
controlled error codes
database ID leakage prevention
stack trace leakage prevention
restricted data leakage prevention
policy internals leakage prevention
permission internals leakage prevention
AI prompt leakage prevention
hidden reasoning leakage prevention
correlation_id preservation
retryable flag behavior
non-disclosure NotFound substitution
PermissionDenied safe error
PolicyRestricted safe error
supported version accepted
unsupported version rejected
missing version rejected
version mismatch rejected
deprecated version not silently rewritten
historical version preserved
```

Required test source:

```text
core-specs/contracts/tests/error-versioning-tests.md
```

---

# 21. Integration Points for Later Tasks

This task must expose primitives usable by:

```text
TASK-007-api-validator-scaffold
TASK-008-workflow-validator-scaffold
TASK-009-agent-boundary-tests
TASK-010-mvp-execution-spine
```

Expected interfaces should support:

```text
make_safe_error(...)
sanitize_error_detail(...)
assert_no_leakage(...)
validate_contract_version(...)
validate_schema_version(...)
require_supported_version(...)
preserve_version_context(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 22. Permission / Policy Interaction

Error and version behavior must preserve Permission and Policy boundaries.

Required behavior:

```text
PermissionDenied does not expose target details if Policy hides them.
PolicyRestricted does not expose policy rule internals.
NotFound substitution hides object existence where required.
Version errors must not expose restricted payload.
Validation errors must not echo restricted fields.
```

---

# 23. Idempotency / Event Interaction

Error and version behavior must preserve Idempotency and Event boundaries.

Required behavior:

```text
IdempotencyConflict does not expose original restricted payload.
Event read errors do not expose hidden event payload.
Event version unsupported errors are safe.
Historical event schema version is preserved.
Event references do not expose database IDs.
```

---

# 24. Forbidden Shortcuts

Codex must not:

```text
return raw exceptions to API callers
return stack traces
return database IDs
echo full invalid payloads that may contain restricted data
expose policy rule internals
expose permission rule internals
expose prompt internals
expose hidden reasoning
treat unsupported versions as allowed
silently upgrade deprecated versions
silently rewrite historical versions
skip negative leakage tests
skip VersionUnsupported tests
mock errors as strings only
use production data fixtures
```

---

# 25. Acceptance Criteria

This task is complete only if:

```text
[ ] Safe error helper exists.
[ ] Controlled error code registry exists.
[ ] Error leakage guard exists or equivalent tests enforce leakage prevention.
[ ] Database ID leakage is tested.
[ ] Stack trace leakage is tested.
[ ] Restricted data leakage is tested.
[ ] Policy/permission internals leakage is tested.
[ ] AI prompt/hidden reasoning leakage is tested.
[ ] correlation_id is preserved.
[ ] retryable flag is present.
[ ] NotFound substitution behavior is supported where policy requires.
[ ] Version validation helper exists.
[ ] Supported version registry or equivalent exists.
[ ] Unsupported versions return VersionUnsupported.
[ ] Missing versions fail safely.
[ ] Deprecated versions are not silently rewritten.
[ ] Historical version preservation is tested.
[ ] Tests pass.
```

---

# 26. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Error/Versioning primitives implemented.
- Files added or changed.
- Which source specs were used.
- Which behavior is Level 3.
- Which behavior is Level 1.
- Which behavior remains stubbed.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- Errors are safe.
- Database IDs do not leak.
- Stack traces do not leak.
- Restricted data does not leak.
- Policy/Permission internals do not leak.
- AI prompt and hidden reasoning do not leak.
- NotFound substitution supported.
- Unsupported versions fail closed.
- Deprecated versions are not silently rewritten.
- Historical versions are preserved.

Deferred
- Full migration engine remains out of scope.
- Full deprecation lifecycle tooling remains out of scope.
- Next task recommended.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-006. Defines Error and Versioning implementation scope, safe error shape, controlled error codes, leakage prevention, non-disclosure, AI error safety, version validation, historical preservation, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-006 — Error Versioning Validation**
