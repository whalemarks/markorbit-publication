# TASK-001 — Common Contract Foundation

**Task ID:** TASK-001  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-001-common-contract-foundation.md  
**Task Title:** Common Contract Foundation  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Contract Layer:** core-specs/contracts/common/  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 1–3 by primitive  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements the Common Contract foundation required by all later MarkOrbit Core implementation tasks.

It creates the shared primitives used by:

```text
API Contracts
Workflow Contracts
Service boundaries
Agent boundaries
Event trace
Permission and Policy governance
Idempotency
Safe errors
Versioning
Contract tests
```

This task is the first Codex task because later API, Workflow, Agent and MVP execution tasks must not implement their own versions of common primitives.

---

# 2. Core Lock

```text
Common Contracts provide shared Core primitives.
References must hide database IDs.
Errors must be safe.
Pagination must respect Policy.
Audit Context preserves trace.
Permission and Policy contexts govern protected behavior.
AI Context bounds AI-assisted output.
Human Review records accountable review.
Idempotency prevents duplicate execution.
Versioning protects compatibility.
Common Contracts do not own domain behavior.
Codex implements the specified primitives.
Codex does not redefine Core architecture.
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
core-specs/contracts/README.md
core-specs/contracts/index.md
core-specs/contracts/common/index.md
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

Codex must also read:

```text
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
```

---

# 4. Scope

This task covers implementation scaffolding and validation helpers for:

```text
Reference Contract
Error Contract
Pagination Contract
Audit Context Contract
AI Context Contract
Human Review Contract
Permission Context Contract
Policy Context Contract
Idempotency Contract
Versioning Contract
```

This task should produce reusable primitives that later tasks can import.

---

# 5. Out of Scope

This task must not implement:

```text
full domain services
full API endpoints
full workflow engine
full policy engine
full permission administration UI
full agent runtime
external integrations
product UI
official filing submission
payment execution
provider marketplace behavior
```

This task must not create business-specific behavior.

---

# 6. Implementation Depth by Primitive

| Primitive | MVP Depth | Required Behavior |
|---|---:|---|
| References | Level 3 | Validate public reference IDs; reject database IDs; validate reference type. |
| Errors | Level 3 | Safe controlled errors; no stack traces or restricted data leakage. |
| Pagination | Level 2 | Basic list/search pagination shape; count omission hook. |
| Audit Context | Level 2 | Validate correlation_id, causation_event_reference_id and event_reference_ids. |
| AI Context | Level 1 | Validate source scope, capability scope, policy omissions and output metadata. |
| Human Review | Level 2 | Validate human_review_reference_id and HumanReviewRequired gate shape. |
| Permission Context | Level 2 / 3 | Validate permission context; fail closed for unknown or denied protected actions. |
| Policy Context | Level 1 / 2 | Validate policy context; support block/redact/review-required placeholders. |
| Idempotency | Level 3 | Required key, safe replay, conflict detection primitive. |
| Versioning | Level 1 | Validate contract_version/schema_version; reject unsupported versions. |

---

# 7. Suggested Implementation Shape

Codex may adapt to the repo structure, but should prefer clear modules similar to:

```text
core/contracts/common/references.py
core/contracts/common/errors.py
core/contracts/common/pagination.py
core/contracts/common/audit_context.py
core/contracts/common/ai_context.py
core/contracts/common/human_review.py
core/contracts/common/permission_context.py
core/contracts/common/policy_context.py
core/contracts/common/idempotency.py
core/contracts/common/versioning.py
core/contracts/common/__init__.py
```

If the project uses TypeScript instead of Python, use equivalent files:

```text
src/core/contracts/common/references.ts
src/core/contracts/common/errors.ts
src/core/contracts/common/pagination.ts
src/core/contracts/common/audit-context.ts
src/core/contracts/common/ai-context.ts
src/core/contracts/common/human-review.ts
src/core/contracts/common/permission-context.ts
src/core/contracts/common/policy-context.ts
src/core/contracts/common/idempotency.ts
src/core/contracts/common/versioning.ts
src/core/contracts/common/index.ts
```

Codex must not change the architecture merely to fit a preferred framework.

---

# 8. Required Primitive Behaviors

## 8.1 Reference Primitive

Must support:

```text
create or validate public reference ID shape
validate expected reference type
reject raw database IDs
reject malformed references
return ReferenceInvalid safely
```

Must not:

```text
treat valid reference as permission
reveal whether hidden object exists when Policy requires non-disclosure
```

## 8.2 Error Primitive

Must support:

```text
controlled error code
safe message
safe_detail
correlation_id
retryable flag
optional restricted_fields_omitted flag
```

Must prevent leakage of:

```text
database IDs
stack traces
restricted data
policy internals
permission internals
prompt internals
hidden reasoning
secrets or tokens
```

## 8.3 Pagination Primitive

Must support:

```text
limit
cursor
next_cursor
items
total_count where allowed
total_count_omitted where policy restricts counts
safe validation errors
```

## 8.4 Audit Context Primitive

Must support:

```text
correlation_id
causation_event_reference_id
event_reference_ids
actor_reference_id where applicable
source_service
```

Must preserve:

```text
event references are trace
event references are not commands
```

## 8.5 AI Context Primitive

Must support:

```text
agent_reference_id
capability_scope
source_scope
policy_omissions_disclosed
ai_assisted flag
human_review_required flag where applicable
```

Must reject:

```text
AI action outside capability scope
AI output claiming approval
AI output claiming certified professional truth
```

## 8.6 Human Review Primitive

Must support:

```text
human_review_required
human_review_reference_id
review_status
reviewer_reference_id
reviewed_at where applicable
```

Must preserve:

```text
Human Review records accountable review.
Human Review does not execute downstream action by itself.
```

## 8.7 Permission Context Primitive

Must support:

```text
required_permission_keys
actor_reference_id
organization_reference_id
permission_decision
permission_decision_reference_id where allowed
fail-closed UnknownPermission
```

Must block:

```text
PermissionDenied
UnknownPermission
missing permission for protected action
```

## 8.8 Policy Context Primitive

Must support:

```text
required_policy_scopes
policy_decision
policy_decision_reference_id where allowed
restricted_fields_omitted
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
NotFound substitution where required
```

Must preserve:

```text
Policy allowance is not Permission approval.
Permission approval is not Policy allowance.
```

## 8.9 Idempotency Primitive

Must support:

```text
idempotency_key required for duplicate-sensitive operation
same key + same semantic request = safe replay
same key + different semantic request = IdempotencyConflict
no duplicate effect marker
```

At this task level, implementation may be in-memory or fixture-backed if no persistence layer exists yet, but the behavior must be testable.

## 8.10 Versioning Primitive

Must support:

```text
contract_version
schema_version where applicable
supported version allowlist
VersionUnsupported error
historical version field preservation where a record is created
```

---

# 9. Required Fixtures

This task may create minimal fixtures needed for its own tests, but the full fixture system belongs to TASK-002.

Minimum fixtures:

```text
valid_reference
invalid_reference
database_id_like_reference
permission_allowed
permission_denied
permission_unknown
policy_allowed
policy_restricted_block
policy_restricted_redact
policy_requires_human_review
valid_ai_context
invalid_ai_context
valid_human_review_context
missing_human_review_context
valid_idempotency_key
idempotency_conflict_case
supported_version
unsupported_version
safe_error_context
```

Fixtures must be:

```text
deterministic
small
non-production
safe to commit
```

---

# 10. Required Tests

This task must add or prepare tests for:

```text
Reference validation
Database ID rejection
Safe error shape
Restricted leakage prevention
Pagination shape
Audit context shape
AI context boundary validation
Human review gate shape
PermissionAllowed
PermissionDenied
UnknownPermission fail-closed
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
IdempotencyKeyRequired
Idempotency safe replay
IdempotencyConflict
VersionUnsupported
```

Minimum test files may be:

```text
tests/contracts/test_common_contract_foundation.py
```

or equivalent in the repo’s test framework.

---

# 11. Forbidden Shortcuts

Codex must not:

```text
treat all permissions as allowed
treat all policies as allowed
skip fail-closed behavior
skip negative tests
expose database IDs
expose stack traces
expose restricted data
ignore idempotency conflict
ignore version validation
allow AI output to approve/send/select/submit/certify/complete
make Human Review execute downstream action
treat event references as commands
use production data fixtures
```

---

# 12. Acceptance Criteria

This task is complete only if:

```text
[ ] Common Contract primitives exist.
[ ] Reference validation rejects database IDs.
[ ] Error helper returns safe controlled errors.
[ ] Pagination helper supports safe list/search shape.
[ ] Audit Context helper validates trace context.
[ ] AI Context helper validates capability and policy omission metadata.
[ ] Human Review helper validates review gate context.
[ ] Permission Context helper fails closed.
[ ] Policy Context helper supports allowed, restricted, redacted and review-required outcomes.
[ ] Idempotency helper supports required key, replay and conflict behavior.
[ ] Versioning helper rejects unsupported versions.
[ ] Minimal deterministic fixtures exist.
[ ] Negative tests exist.
[ ] Tests pass.
[ ] No domain business behavior is implemented in this task.
```

---

# 13. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Common Contract primitives implemented.
- Files added or changed.
- Which source specs were used.
- Which primitives are Level 1, Level 2 and Level 3.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- References do not expose database IDs.
- Errors are safe.
- Permission fails closed.
- Policy restrictions are represented.
- AI forbidden outputs are blocked at context level.
- Human Review does not execute downstream action.
- Idempotency replay/conflict works.
- Unsupported versions fail closed.

Deferred
- Full fixture system remains TASK-002.
- Full API validators remain TASK-007.
- Full workflow validators remain TASK-008.
```

---

# 14. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-001. Defines Common Contract foundation implementation scope, required source files, primitive behaviors, fixtures, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-001 — Common Contract Foundation**
