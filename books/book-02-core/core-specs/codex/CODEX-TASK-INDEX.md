# Codex Task Index

**Spec ID:** B02-CODEX-TASK-INDEX  
**Spec Type:** Codex Task Index  
**Spec File:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Task Folder:** codex-tasks/  
**Status:** Draft  
**Version:** 0.1.0  
**Task Index Version:** v0.1.0  
**MVP Phase:** Phase 0–1 — Codex Task Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines the canonical Codex task index for implementing Book 02 — MarkOrbit Core Specification.

It breaks implementation into small, reviewable, testable tasks.

The purpose is to prevent Codex from:

```text
implementing the whole Core at once
creating architecture by assumption
building unscoped product behavior
deepening implementation beyond MVP scope
skipping negative tests
bypassing Permission or Policy
allowing AI to execute protected actions
creating shallow stubs with no test value
```

This index is the entry point for all Codex implementation tasks under:

```text
codex-tasks/
```

---

# 2. Core Lock

```text
Codex implements traced Core specifications.
Codex does not define Core architecture.
Every Codex task must cite source specs.
Every Codex task must stay inside MVP Cut and Implementation Depth.
Every Codex task must preserve owning service boundaries.
Every Codex task must include tests or explain why tests are not applicable.
Permission and Policy must fail closed.
AI must remain bounded by Agent Governance.
Events preserve trace and are not commands.
```

---

# 3. Required Reading Before Any Codex Task

Before starting any task, Codex must read:

```text
core-specs/DEVELOPER_START_HERE.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/contracts/README.md
core-specs/contracts/index.md
core-specs/contracts/MANIFEST.md
core-specs/contracts/tests/index.md
```

For contract-related tasks, Codex must additionally read:

```text
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
```

For agent-related tasks, Codex must additionally read:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
core-specs/contracts/tests/agent-boundary-tests.md
```

---

# 4. Task Naming Rules

Codex task files must use this naming pattern:

```text
codex-tasks/TASK-###-short-kebab-name.md
```

Examples:

```text
codex-tasks/TASK-001-common-contract-foundation.md
codex-tasks/TASK-002-contract-fixture-system.md
codex-tasks/TASK-003-common-contract-tests.md
```

Task numbers are stable once assigned.

Rules:

```text
- Do not reuse task numbers.
- Do not rename completed task files without an explicit review note.
- Do not combine unrelated tasks.
- Do not create open-ended tasks.
- Every task must have acceptance criteria.
```

---

# 5. Task Status Values

Allowed task status values:

```text
Draft
Ready
In Progress
Blocked
Implemented
Verified
Deferred
Cancelled
```

Definitions:

| Status | Meaning |
|---|---|
| Draft | Task is proposed but not ready for implementation. |
| Ready | Task has clear scope, inputs, outputs and tests. |
| In Progress | Codex or developer is implementing. |
| Blocked | Required source or dependency is missing. |
| Implemented | Code/spec changes were produced. |
| Verified | Tests and review passed. |
| Deferred | Valid task but not in current MVP scope. |
| Cancelled | Task should not be implemented. |

---

# 6. Task Dependency Rules

Codex must respect task dependencies.

Core rule:

```text
Foundation before workflow.
Contracts before product behavior.
Fixtures before broad tests.
Tests before production confidence.
MVP cut before implementation expansion.
```

Dependency sequence:

```text
TASK-001 → TASK-002 → TASK-003
TASK-003 → TASK-004
TASK-004 → TASK-005
TASK-005 → TASK-006
TASK-006 → TASK-007
TASK-007 → TASK-008
TASK-008 → TASK-009
TASK-009 → TASK-010
```

Codex must not start later tasks if earlier boundary tasks are missing unless the task explicitly states a safe stub dependency.

---

# 7. Canonical MVP Codex Task List

| Task ID | Task File | Title | MVP Category | Depends On | Status |
|---|---|---|---|---|---|
| TASK-001 | codex-tasks/TASK-001-common-contract-foundation.md | Common Contract Foundation | Must Build Now | none | Draft |
| TASK-002 | codex-tasks/TASK-002-contract-fixture-system.md | Contract Fixture System | Must Build Now | TASK-001 | Draft |
| TASK-003 | codex-tasks/TASK-003-common-contract-tests.md | Common Contract Tests | Must Build Now | TASK-001; TASK-002 | Draft |
| TASK-004 | codex-tasks/TASK-004-permission-policy-hooks.md | Permission Policy Hooks | Must Build Now | TASK-001; TASK-002; TASK-003 | Draft |
| TASK-005 | codex-tasks/TASK-005-idempotency-event-trace.md | Idempotency Event Trace | Must Build Now | TASK-001; TASK-002; TASK-003 | Draft |
| TASK-006 | codex-tasks/TASK-006-error-versioning-validation.md | Error Versioning Validation | Must Build Now | TASK-001; TASK-002; TASK-003 | Draft |
| TASK-007 | codex-tasks/TASK-007-api-validator-scaffold.md | API Validator Scaffold | Must Build Now | TASK-001 to TASK-006 | Draft |
| TASK-008 | codex-tasks/TASK-008-workflow-validator-scaffold.md | Workflow Validator Scaffold | Must Build Now | TASK-001 to TASK-007 | Draft |
| TASK-009 | codex-tasks/TASK-009-agent-boundary-tests.md | Agent Boundary Tests | Must Build Now | TASK-001 to TASK-008 | Draft |
| TASK-010 | codex-tasks/TASK-010-mvp-execution-spine.md | MVP Execution Spine | Must Build Now | TASK-001 to TASK-009 | Draft |

---

# 8. Task Group A — Contract Foundation

## TASK-001 — Common Contract Foundation

Task file:

```text
codex-tasks/TASK-001-common-contract-foundation.md
```

Purpose:

```text
Implement the common contract primitives required by every later task.
```

Scope:

```text
Reference Contract
Error Contract
Versioning Contract
Audit Context Contract
Permission Context Contract
Policy Context Contract
AI Context Contract
Human Review Contract
Idempotency Contract
Pagination Contract
```

Expected output:

```text
common validators/helpers
safe reference helpers
safe error helpers
version validation helpers
context validation helpers
idempotency helper skeleton
unit tests for primitive shapes
```

Do not implement:

```text
full policy engine
full permission administration
full workflow engine
product UI
```

---

# 9. Task Group B — Fixtures and Base Tests

## TASK-002 — Contract Fixture System

Task file:

```text
codex-tasks/TASK-002-contract-fixture-system.md
```

Purpose:

```text
Create deterministic non-production fixtures for contract tests.
```

Required fixtures:

```text
valid reference
invalid reference
wrong-type reference
PermissionAllowed
PermissionDenied
UnknownPermission
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
AI-assisted context
invalid AI context
valid human review
missing human review
idempotent replay
idempotency conflict
visible event
restricted event
supported version
unsupported version
missing version
deprecated version
```

Forbidden:

```text
production data
real customer data
real provider data
real official filing data
secrets or tokens
```

## TASK-003 — Common Contract Tests

Task file:

```text
codex-tasks/TASK-003-common-contract-tests.md
```

Purpose:

```text
Implement tests for Common Contracts.
```

Required test source:

```text
core-specs/contracts/tests/common-contract-tests.md
```

Required coverage:

```text
Reference Contract Tests
Error Contract Tests
Pagination Contract Tests
Audit Context Tests
Permission Context Tests
Policy Context Tests
AI Context Tests
Human Review Contract Tests
Idempotency Contract Tests
Versioning Contract Tests
Cross-Contract Consistency Tests
```

---

# 10. Task Group C — Governance Enforcement

## TASK-004 — Permission Policy Hooks

Task file:

```text
codex-tasks/TASK-004-permission-policy-hooks.md
```

Purpose:

```text
Implement Permission and Policy hooks and fail-closed behavior for MVP protected actions.
```

Required source:

```text
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/implementation/implementation-depth-matrix.md
```

Required behavior:

```text
PermissionAllowed
PermissionDenied
UnknownPermission
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
NotFound substitution where policy requires non-disclosure
```

## TASK-005 — Idempotency Event Trace

Task file:

```text
codex-tasks/TASK-005-idempotency-event-trace.md
```

Purpose:

```text
Implement duplicate-safe execution primitives and event trace behavior.
```

Required source:

```text
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/tests/idempotency-event-tests.md
```

Required behavior:

```text
idempotency_key required for duplicate-sensitive operations
same key + same semantic request safe replay
same key + different semantic request IdempotencyConflict
no duplicate objects
no duplicate Tasks
no duplicate Communications
no duplicate Events
Events are trace, not commands
API / Workflow / Agent layers do not emit Events directly
```

## TASK-006 — Error Versioning Validation

Task file:

```text
codex-tasks/TASK-006-error-versioning-validation.md
```

Purpose:

```text
Implement safe error and version validation behavior.
```

Required source:

```text
core-specs/contracts/common/errors.md
core-specs/contracts/common/versioning.md
core-specs/contracts/tests/error-versioning-tests.md
```

Required behavior:

```text
controlled error codes
safe error shape
no database ID leakage
no restricted data leakage
no policy/permission internals leakage
no prompt or hidden reasoning leakage
VersionUnsupported
historical version preservation where records are created
```

---

# 11. Task Group D — API and Workflow Scaffolds

## TASK-007 — API Validator Scaffold

Task file:

```text
codex-tasks/TASK-007-api-validator-scaffold.md
```

Purpose:

```text
Create API validator scaffolds for all 26 API Contracts, with MVP APIs at stronger depth.
```

Required source:

```text
core-specs/contracts/api/index.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
```

MVP APIs require stronger implementation:

```text
identity
organization
user
permission
policy
customer
brand
trademark
jurisdiction
classification
document
evidence
matter
order
workflow-contract
task
event
communication
```

Stub APIs:

```text
knowledge
notification
opportunity
partner
agent
service-provider
service-network
routing
```

## TASK-008 — Workflow Validator Scaffold

Task file:

```text
codex-tasks/TASK-008-workflow-validator-scaffold.md
```

Purpose:

```text
Create workflow preview/apply validator scaffolds.
```

Required source:

```text
core-specs/workflows/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/implementation/mvp-cut-v0.1.md
```

MVP workflows:

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Stub workflows:

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

---

# 12. Task Group E — Agent and MVP Spine

## TASK-009 — Agent Boundary Tests

Task file:

```text
codex-tasks/TASK-009-agent-boundary-tests.md
```

Purpose:

```text
Implement agent forbidden-action and boundary tests.
```

Required source:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
core-specs/contracts/tests/agent-boundary-tests.md
```

Required behavior:

```text
Agents may prepare, summarize, draft, suggest, compare and identify gaps.
Agents must not approve, send, select, submit, certify, complete, mutate protected state or emit Events.
```

## TASK-010 — MVP Execution Spine

Task file:

```text
codex-tasks/TASK-010-mvp-execution-spine.md
```

Purpose:

```text
Implement the minimum executable MarkOrbit Core spine after contract, fixture, governance, API and workflow foundations are in place.
```

MVP spine:

```text
Customer
↓
Brand / Trademark
↓
Matter / Order
↓
Document / Evidence
↓
Workflow Contract
↓
Task
↓
Communication
↓
Event
↓
Permission / Policy
↓
Tests
```

Must not begin until:

```text
TASK-001 through TASK-006 are complete or explicitly stubbed with passing tests.
TASK-007 and TASK-008 have at least scaffold coverage.
TASK-009 has AI forbidden-action coverage.
```

---

# 13. Deferred Task Candidates

These are not MVP tasks, but may become future tasks.

```text
TASK-011-validation-specs
TASK-012-workflow-specs-production-draft
TASK-013-renewal-workflow-production
TASK-014-assignment-workflow-production
TASK-015-office-action-response-production
TASK-016-provider-routing-production
TASK-017-evidence-review-production
TASK-018-notification-delivery-integration
TASK-019-document-storage-integration
TASK-020-client-portal-api
TASK-021-partner-portal-api
TASK-022-service-provider-onboarding
TASK-023-policy-engine-v0.2
TASK-024-agent-runtime-v0.2
TASK-025-workflow-engine-v0.2
```

Deferred task rule:

```text
Deferred tasks must not block MVP.
Deferred tasks must not be implemented before MVP acceptance unless explicitly moved into scope.
```

---

# 14. Forbidden Codex Shortcuts

Codex must not:

```text
implement without reading source specs
create new architecture concepts casually
rename Core concepts without review
skip negative tests
treat happy-path tests as sufficient
mock Permission/Policy without asserting invocation
let valid references imply read permission
leak database IDs
leak restricted data
allow AI to approve/send/select/submit/certify/complete
allow Human Review to execute downstream action by itself
emit Events from API/Workflow/Agent layers
treat Event references as commands
silently accept unsupported versions
silently rewrite historical versions
use production data fixtures
build full workflow engine before MVP spine
build full policy engine before MVP spine
build full agent runtime before MVP spine
```

---

# 15. Required Task File Sections

Every Codex task file must include:

```text
Task ID
Task Type
Task File
Status
Version
Purpose
Core Lock
Required Source Files
Scope
Out of Scope
Implementation Steps
Required Fixtures
Required Tests
Forbidden Shortcuts
Acceptance Criteria
Final Summary Format
Revision Notes
```

---

# 16. Final Summary Format

Every Codex task result must include:

```text
Summary
- What was implemented.
- Which specs were used.
- Which files changed.
- Which behavior is real enforcement.
- Which behavior remains stubbed.

Tests
- Commands run.
- Results.

Boundary Confirmation
- Permission/Policy fail closed.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Idempotency replay/conflict verified.
- Events are trace, not commands.
- Errors are safe.
- Unsupported versions fail closed.

Deferred
- What remains out of scope.
- What should be implemented next.
```

---

# 17. Task Index Acceptance Criteria

This Codex Task Index is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines required reading before any Codex task.
[ ] It defines task naming rules.
[ ] It defines task status values.
[ ] It defines dependency rules.
[ ] It defines canonical MVP Codex task list.
[ ] It defines Task Group A — Contract Foundation.
[ ] It defines Task Group B — Fixtures and Base Tests.
[ ] It defines Task Group C — Governance Enforcement.
[ ] It defines Task Group D — API and Workflow Scaffolds.
[ ] It defines Task Group E — Agent and MVP Spine.
[ ] It defines deferred task candidates.
[ ] It defines forbidden Codex shortcuts.
[ ] It defines required task file sections.
[ ] It defines final summary format.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex Task Index. Defines MVP Codex task sequence, dependencies, scope, task groups, deferred candidates, forbidden shortcuts, required task sections and final summary format. |

---

**End of Codex Task Index**
