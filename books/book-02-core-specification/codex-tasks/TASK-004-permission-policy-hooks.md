# TASK-004 — Permission Policy Hooks

**Task ID:** TASK-004  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-004-permission-policy-hooks.md  
**Task Title:** Permission Policy Hooks  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Common Contracts:** core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/references.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contract:** core-specs/contracts/tests/permission-policy-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Permission Level 2/3; Policy Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements Permission and Policy hooks for MarkOrbit Core MVP protected behavior.

It ensures that protected actions and policy-controlled outputs do not proceed unless both access governance layers are satisfied.

This task is required before API validators, Workflow validators and MVP execution spine can safely expand.

It implements the rule:

```text
Permission decides whether an actor may act.
Policy decides whether the context allows, restricts, redacts, downgrades or requires review.
Permission approval is not Policy approval.
Policy allowance is not Permission approval.
```

---

# 2. Core Lock

```text
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Permission approval alone is never enough where Policy restricts.
Policy allowance alone is never enough where Permission is denied.
Unknown Permission must fail closed.
Unknown Policy must fail closed for policy-controlled behavior.
Policy may block, redact, downgrade or require human review.
Restricted data must not leak through responses, errors, events or AI output.
Codex implements Permission and Policy hooks.
Codex does not create permission grants or policy rules outside the specs.
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
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/references.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/versioning.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
```

Codex must also consult:

```text
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/agent-boundary-tests.md
```

---

# 4. Scope

This task covers:

```text
Permission Context validation
Policy Context validation
Permission evaluation hook
Policy evaluation hook
Permission / Policy matrix behavior
PermissionDenied behavior
PolicyRestricted behavior
PolicyRestrictedRedact behavior
PolicyRequiresHumanReview behavior
UnknownPermission fail-closed behavior
UnknownPolicy fail-closed behavior
cross-organization restriction hook
redaction and restricted_fields_omitted behavior
NotFound substitution for non-disclosure policy
AI output policy omission support
HumanReviewRequired policy support
safe error integration
tests for protected MVP actions
```

---

# 5. Out of Scope

This task must not implement:

```text
full role administration UI
full permission grant lifecycle
full policy authoring engine
full policy approval workflow
complex ABAC/RBAC engine unless already present
production compliance audit dashboard
product-specific access UI
external identity provider integration
automatic legal/professional approval
```

This task creates enforcement hooks and MVP-level fail-closed behavior. It does not build the final enterprise policy platform.

---

# 6. Implementation Depth

## 6.1 Permission Depth

MVP Permission depth:

```text
Level 2 for general Permission hook.
Level 3 for protected MVP actions.
```

Required protected MVP actions:

```text
create or update Customer
create or update Brand
create or update Trademark
create or update Matter
create or update Order
create or attach Document
create or update Evidence
create Task through Task Service
create or review Communication
workflow preview where protected
workflow apply
read restricted Event trace
AI-assisted preparation using restricted sources
```

## 6.2 Policy Depth

MVP Policy depth:

```text
Level 1 for policy context schema validation.
Level 2 for contextual restriction hook.
```

Required policy outcomes:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
```

Full policy rule authoring is not required.

---

# 7. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/contracts/common/permission_context.py
core/contracts/common/policy_context.py
core/governance/permission_hooks.py
core/governance/policy_hooks.py
core/governance/access_matrix.py
core/governance/redaction.py
```

Preferred TypeScript-like shape:

```text
src/core/contracts/common/permission-context.ts
src/core/contracts/common/policy-context.ts
src/core/governance/permission-hooks.ts
src/core/governance/policy-hooks.ts
src/core/governance/access-matrix.ts
src/core/governance/redaction.ts
```

Suggested tests:

```text
tests/contracts/test_permission_policy_hooks.py
tests/contracts/test_permission_policy_matrix.py
tests/contracts/test_redaction_and_nondisclosure.py
```

---

# 8. Permission / Policy Matrix

Codex must implement and test the following matrix:

```text
PermissionAllowed + PolicyAllowed = may proceed
PermissionDenied + PolicyAllowed = blocked
PermissionAllowed + PolicyRestrictedBlock = blocked
PermissionAllowed + PolicyRestrictedRedact = redacted or downgraded safe output
PermissionAllowed + PolicyRequiresHumanReview = HumanReviewRequired unless valid review exists
PermissionDenied + PolicyRestricted = blocked
UnknownPermission + AnyPolicy = blocked
AnyPermission + UnknownPolicy for policy-controlled behavior = blocked
MissingPermission + AnyPolicy = blocked
AnyPermission + MissingPolicy for policy-controlled behavior = blocked
```

The implementation must not treat either layer as sufficient by itself.

---

# 9. Required Hook Behavior

## 9.1 Permission Hook

Must accept:

```text
actor_reference_id
organization_reference_id
required_permission_keys
target_reference_id where applicable
action_key
context
```

Must return controlled decision:

```text
PermissionAllowed
PermissionDenied
UnknownPermission
MissingPermissionContext
```

Must fail closed when:

```text
actor missing
required_permission_keys missing for protected action
permission evaluator unavailable
permission decision unknown
permission denied
```

## 9.2 Policy Hook

Must accept:

```text
actor_reference_id
organization_reference_id
required_policy_scopes
target_reference_id where applicable
action_key
output_fields where applicable
context
```

Must return controlled decision:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
```

Must fail closed when:

```text
policy-controlled action has missing policy context
policy evaluator unavailable
policy decision unknown
policy restricts the action
```

---

# 10. Redaction Behavior

When PolicyRestrictedRedact applies:

```text
restricted fields must be omitted
restricted_fields_omitted must be true
safe fields may remain
nested restricted fields must be omitted
errors must not expose redacted fields
event payload must not expose redacted fields
AI output must disclose policy omissions
```

Required output indicators:

```text
restricted_fields_omitted: true
policy_omissions_disclosed: true where AI output is affected
```

Redaction must not become a silent partial truth.

---

# 11. Non-Disclosure Behavior

When PolicyNonDisclosureNotFound applies:

```text
object existence must not be revealed
NotFound or equivalent safe error must be returned
safe_detail must not reveal existence
pagination totals must not reveal hidden objects
event trace must not reveal hidden objects
idempotency replay must not reveal hidden prior result
```

This is required for sensitive cross-organization or restricted visibility cases.

---

# 12. Human Review Interaction

When PolicyRequiresHumanReview applies:

```text
HumanReviewRequired must be returned if no valid review exists
valid human_review_reference_id may satisfy the gate only if owning service accepts it
human review must not bypass Permission
human review must not bypass Policy
human review must not execute downstream action by itself
```

Required test:

```text
PermissionAllowed + PolicyRequiresHumanReview + missing review = HumanReviewRequired
PermissionDenied + valid review = PermissionDenied
PolicyRestrictedBlock + valid review = PolicyRestricted unless policy specifically allows review override
```

---

# 13. AI Interaction

AI-assisted behavior must respect Permission and Policy.

Required behavior:

```text
agent identity does not imply Permission
agent capability does not imply Permission
PolicyRestricted redacts AI input/output
policy_omissions_disclosed is true where AI output omits restricted sources
AI must not infer hidden restricted facts as truth
AI must not expose hidden source existence
AI must not execute protected actions even if PermissionAllowed
```

Required tests:

```text
AI draft with restricted source redacts source content.
AI summary discloses policy omissions.
AI forbidden action remains blocked even when PermissionAllowed.
```

---

# 14. Cross-Organization Rules

Cross-organization behavior must be policy-controlled.

Required behavior:

```text
same organization access follows Permission and Policy
cross-organization access requires explicit Policy allowance
Partner / Service Provider / Service Network access requires relationship policy
Customer data visibility is restricted by Policy
provider commercial terms are restricted by Policy
```

Required tests:

```text
PermissionAllowed without cross-organization Policy = PolicyRestricted
PolicyNonDisclosureNotFound hides cross-organization object existence where required
```

---

# 15. Required Fixtures

Use fixtures from TASK-002:

```text
PermissionAllowed
PermissionDenied
UnknownPermission
MissingPermissionContext
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
CrossOrganizationPolicyRestricted
ValidHumanReview
MissingHumanReview
ValidAIContext
AIPolicyOmissions
VisibleEvent
RestrictedEvent
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
PermissionAllowed + PolicyAllowed
PermissionDenied + PolicyAllowed
PermissionAllowed + PolicyRestrictedBlock
PermissionAllowed + PolicyRestrictedRedact
PermissionAllowed + PolicyRequiresHumanReview
UnknownPermission fail-closed
UnknownPolicy fail-closed
MissingPermissionContext fail-closed
MissingPolicyContext fail-closed
redaction behavior
NotFound non-disclosure behavior
HumanReviewRequired behavior
cross-organization restriction
AI policy omission behavior
safe error behavior
permission/policy internal non-disclosure
```

Required test source:

```text
core-specs/contracts/tests/permission-policy-tests.md
```

---

# 17. Integration Points for Later Tasks

This task must expose hooks usable by:

```text
TASK-007-api-validator-scaffold
TASK-008-workflow-validator-scaffold
TASK-009-agent-boundary-tests
TASK-010-mvp-execution-spine
```

Expected interfaces should support:

```text
check_permission(...)
check_policy(...)
enforce_permission_policy(...)
redact_by_policy(...)
require_human_review_if_policy_requires(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 18. Forbidden Shortcuts

Codex must not:

```text
treat PermissionAllowed as sufficient when Policy restricts
treat PolicyAllowed as sufficient when Permission denies
default unknown Permission to allowed
default unknown Policy to allowed
ignore cross-organization restrictions
skip redaction tests
skip non-disclosure tests
skip AI policy omission tests
allow agent identity to imply Permission
allow human review to bypass Permission
allow human review to bypass Policy
expose policy internals in errors
expose permission internals in errors
expose restricted fields through event payloads
expose restricted fields through AI output
use production data fixtures
```

---

# 19. Acceptance Criteria

This task is complete only if:

```text
[ ] Permission hook exists.
[ ] Policy hook exists.
[ ] Permission / Policy matrix is implemented.
[ ] PermissionDenied blocks protected actions.
[ ] UnknownPermission fails closed.
[ ] MissingPermissionContext fails closed.
[ ] PolicyRestrictedBlock blocks policy-restricted actions.
[ ] PolicyRestrictedRedact omits restricted fields.
[ ] restricted_fields_omitted is true where redaction occurs.
[ ] PolicyRequiresHumanReview returns HumanReviewRequired when review is missing.
[ ] PolicyNonDisclosureNotFound hides object existence.
[ ] UnknownPolicy fails closed.
[ ] MissingPolicyContext fails closed.
[ ] Cross-organization restriction is tested.
[ ] AI policy omissions are tested.
[ ] Safe error behavior is tested.
[ ] Permission/Policy internals are not exposed.
[ ] Hooks are reusable by API and Workflow tasks.
[ ] Tests pass.
```

---

# 20. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Permission/Policy hooks implemented.
- Files added or changed.
- Which source specs were used.
- Which behaviors are Level 2.
- Which behaviors are Level 3.
- Which behaviors remain stubs.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- PermissionDenied blocks protected actions.
- UnknownPermission fails closed.
- PolicyRestricted blocks or redacts.
- UnknownPolicy fails closed.
- HumanReviewRequired preserved.
- Cross-organization policy enforced.
- AI policy omissions disclosed.
- Restricted data does not leak.
- Permission/Policy internals do not leak.

Deferred
- Full policy engine remains out of scope.
- Full permission administration remains out of scope.
- Next task recommended.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-004. Defines Permission/Policy hook implementation scope, matrix behavior, redaction, non-disclosure, human review, AI interaction, cross-organization rules, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-004 — Permission Policy Hooks**
