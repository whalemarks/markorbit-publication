# Test Contracts — README

**Spec ID:** B02-CONTRACT-TESTS-README  
**Spec Type:** Test Contract Index / README  
**Contract File:** core-specs/contracts/tests/README.md  
**Contract Category:** Test Contracts  
**Related Core Specs:** core-specs/contracts/README.md; core-specs/contracts/template.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Contract Layers:** API Contracts; Workflow Contracts; Common Contracts; Agent Contracts  
**Related Core Domains:** Identity; Organization; User; Permission; Policy; Knowledge; Brand; Trademark; Jurisdiction; Classification; Document; Evidence; Customer; Matter; Order; Opportunity; Workflow Contract; Task; Event; Notification; Partner; Agent; Service Provider; Service Network; Routing; Communication  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Cross-Cutting Quality Governance  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Test Contracts define how MarkOrbit Core specifications must be verified before implementation is accepted.

They provide a governed testing layer for:

```text
common contract behavior
API contract behavior
workflow contract behavior
service boundary enforcement
reference validation
permission enforcement
policy enforcement
AI boundary enforcement
human review gating
idempotency behavior
event trace behavior
version compatibility
safe error behavior
restricted-field omission
Codex implementation acceptance
```

Test Contracts are not generic test plans. They are Core acceptance contracts.

---

# 2. Core Lock

```text
Test Contracts verify Core behavior.
Tests must enforce boundaries, not weaken them.
Owning services own behavior.
Permission and Policy must fail closed.
AI must stay inside governed capability scope.
Human review gates protected actions.
Idempotency prevents duplicate execution.
Events preserve trace.
Safe errors protect restricted information.
```

This lock applies to every file under:

```text
core-specs/contracts/tests/
```

---

# 3. What Test Contracts Are

Test Contracts are specification-level acceptance rules that Codex must use to implement and validate MarkOrbit Core.

They define:

```text
what must be tested
which boundary must be protected
which service owns behavior
which inputs are valid or invalid
which outputs are safe
which events may exist
which operations must be idempotent
which AI actions are forbidden
which human review gates are required
```

They are designed to be converted into:

```text
unit tests
contract tests
integration tests
workflow tests
permission/policy tests
AI boundary tests
idempotency tests
event trace tests
regression tests
fixture tests
```

---

# 4. What Test Contracts Are Not

Test Contracts are not:

```text
implementation code
test framework selection
database migration tests by themselves
UI tests by themselves
load tests by default
manual QA scripts only
generic checklist documents
permission grants
policy approvals
AI evaluation prompts only
```

They may inform those artifacts, but they do not replace implementation-specific tests.

---

# 5. Required Test Contract Files

Recommended initial files:

```text
core-specs/contracts/tests/README.md
core-specs/contracts/tests/template.md
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/agent-boundary-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
core-specs/contracts/tests/index.md
```

MVP priority:

```text
Must Implement:
  common-contract-tests.md
  api-contract-tests.md
  workflow-contract-tests.md
  permission-policy-tests.md
  idempotency-event-tests.md
  error-versioning-tests.md

Should Implement:
  agent-boundary-tests.md

Must Maintain:
  index.md
```

---

# 6. Test Contract Naming Rules

Test contract files use:

```text
core-specs/contracts/tests/{test-area}-tests.md
```

Rules:

```text
- File names must be lowercase.
- Words must be separated by hyphens.
- Files must end with -tests.md, except README.md, template.md and index.md.
- Every test contract must identify related contract layers.
- Every test contract must define acceptance criteria.
```

---

# 7. Required Sections for Test Contracts

Each Test Contract must include:

```text
1. Purpose
2. Core Lock
3. Test Boundary
4. Related Contracts
5. Test Subject
6. Required Fixtures
7. Positive Test Rules
8. Negative Test Rules
9. Permission Tests
10. Policy Tests
11. AI Boundary Tests
12. Human Review Tests
13. Idempotency Tests
14. Event Trace Tests
15. Error Safety Tests
16. Versioning Tests
17. Codex Implementation Notes
18. Acceptance Criteria
19. Revision Notes
```

Optional sections:

```text
Contract Coverage Matrix
Fixture Data Shape
Test Case Table
Regression Rules
Traceability Matrix
```

---

# 8. Global Test Principles

All Test Contracts must enforce:

```text
Core boundary first
Fail closed by default
No silent permission bypass
No silent policy bypass
No AI autonomous protected action
No direct event emission from API/workflow layer
No duplicate effects on retry
No database ID leakage
No restricted-field leakage
No hidden human-review requirement
No silent version rewrite
```

---

# 9. Common Test Categories

## 9.1 Reference Tests

Must verify:

```text
valid reference accepted
invalid reference rejected
missing required reference rejected
reference validation does not imply read permission
database IDs not exposed
cross-domain references validated by owning service
```

## 9.2 Permission Tests

Must verify:

```text
required permission key present
Permission Service invoked
PermissionDenied stops protected behavior
permission approval does not bypass Policy
permission decision not exposed where policy forbids
```

## 9.3 Policy Tests

Must verify:

```text
required policy scope present
Policy Service invoked
PolicyRestricted blocks or downgrades safely
policy redaction applied
restricted_fields_omitted is true where fields are omitted
NotFound may replace PolicyRestricted where policy requires non-disclosure
```

## 9.4 AI Boundary Tests

Must verify:

```text
AI context required for AI-assisted behavior
AI cannot approve
AI cannot send
AI cannot select provider
AI cannot submit filings
AI cannot certify deadlines
AI cannot certify authority
AI cannot decide evidence sufficiency
AI output discloses source scope and policy omissions
```

## 9.5 Human Review Tests

Must verify:

```text
human review required before protected action
missing review blocks or downgrades action
review record does not execute downstream action by itself
owning service decides whether review satisfies requirements
review trace preserved
```

## 9.6 Idempotency Tests

Must verify:

```text
required idempotency_key exists for duplicate-sensitive operations
duplicate request returns safe replay or conflict
duplicate request does not duplicate tasks
duplicate request does not duplicate events
duplicate request does not duplicate communication
duplicate request does not duplicate routing selection
semantic conflict fails safe
```

## 9.7 Event Trace Tests

Must verify:

```text
events emitted only by owning services
API layer does not emit events directly
workflow layer does not emit events directly
event references are audit trace, not commands
idempotent replay does not duplicate events
restricted event visibility follows Policy
```

## 9.8 Error Safety Tests

Must verify:

```text
errors follow Error Contract
errors are safe
errors do not expose database IDs
errors do not expose restricted data
errors do not expose policy internals
errors do not expose permission internals
VersionUnsupported fails closed
```

---

# 10. Required Fixture Strategy

Test Contracts should define fixture requirements without depending on production data.

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must avoid real customer data.
- Fixtures must include valid and invalid references.
- Fixtures must include permission-allowed and permission-denied contexts.
- Fixtures must include policy-allowed, policy-redacted and policy-blocked contexts.
- Fixtures must include AI-assisted and non-AI-assisted cases.
- Fixtures must include human-review-present and human-review-missing cases.
- Fixtures must include duplicate idempotency cases.
- Fixtures must include version-supported and version-unsupported cases.
```

Fixture types:

```text
Reference Fixture
Permission Fixture
Policy Fixture
AI Context Fixture
Human Review Fixture
Idempotency Fixture
Event Trace Fixture
Version Fixture
Domain Object Fixture
Workflow Fixture
```

---

# 11. API Contract Test Requirements

Every API Contract must have tests for:

```text
request schema validation
response schema validation
required references
reference validation by owning service
Permission Context
Policy Context
safe redaction
idempotency where required
safe errors
version validation
event trace references where returned
AI Context where applicable
Human Review where applicable
```

API tests must prove:

```text
API layer receives governed requests.
Owning Service owns behavior.
API layer does not bypass Permission or Policy.
API layer does not emit Events directly.
API layer does not expose restricted information.
```

---

# 12. Workflow Contract Test Requirements

Every Workflow Contract must have tests for:

```text
preview behavior
apply behavior
preview creates no active Tasks
preview emits no domain Events directly
apply requires idempotency_key
apply routes task creation through Task Service
apply routes domain mutation through owning services
AI-assisted steps cannot execute protected actions
human review gates protected actions
PermissionDenied stops or downgrades safely
PolicyRestricted stops or downgrades safely
duplicate apply does not duplicate effects
```

Workflow tests must prove:

```text
Workflow Contract coordinates execution.
Workflow Contract Service owns preview/apply behavior.
Task Service owns active Task creation.
Owning domain services own domain state.
AI cannot execute protected actions.
Events preserve trace.
```

---

# 13. Common Contract Test Requirements

Common Contract tests must cover:

```text
Reference Contract
Error Contract
Pagination Contract
Audit Context Contract
Permission Context Contract
Policy Context Contract
AI Context Contract
Human Review Contract
Idempotency Contract
Versioning Contract
```

Common tests must prove:

```text
common contracts are stable
common contracts are reused consistently
common contracts fail closed
common contracts do not expand domain ownership
```

---

# 14. Agent Boundary Test Requirements

Agent Boundary tests must verify:

```text
agent registry validation
agent capability scope enforcement
agent source scope disclosure
agent evaluated data access scope
AI output cannot become professional truth by itself
AI output cannot execute downstream action directly
AI output must preserve human review requirements
AI output must preserve policy omissions
```

Forbidden AI action tests must include:

```text
approve communication
send communication
select provider
submit filing
certify deadline
certify authority
decide registrability
decide evidence sufficiency
approve payment
complete task
```

---

# 15. Permission / Policy Test Requirements

Permission and Policy tests must be cross-cutting.

They must verify:

```text
Permission approval alone is insufficient where Policy restricts.
Policy approval alone is insufficient where Permission is denied.
PermissionDenied stops protected behavior.
PolicyRestricted blocks, redacts or downgrades safely.
Permission and Policy decisions are traceable where allowed.
Permission and Policy internals are not leaked.
```

Core matrix:

```text
PermissionAllowed + PolicyAllowed = action may proceed
PermissionDenied + PolicyAllowed = blocked
PermissionAllowed + PolicyRestricted = blocked or downgraded
PermissionDenied + PolicyRestricted = blocked
UnknownPermission + AnyPolicy = blocked
AnyPermission + UnknownPolicy for policy-controlled action = blocked
```

---

# 16. Idempotency / Event Test Requirements

Idempotency and Event tests must verify:

```text
duplicate create does not duplicate object
duplicate workflow apply does not duplicate tasks
duplicate communication preparation does not duplicate communication
duplicate routing selection does not duplicate RoutingSelected event
duplicate event reference does not cause action
event trace is preserved
event visibility follows Policy
```

Core rule:

```text
Idempotency prevents accidental duplicate execution.
Events preserve trace.
Events are not commands.
```

---

# 17. Error / Versioning Test Requirements

Error tests must verify:

```text
safe error shape
controlled error code
no restricted leakage
correlation_id preserved
retryable flag where applicable
NotFound substitution where policy requires non-disclosure
```

Versioning tests must verify:

```text
supported version accepted
unsupported version rejected
missing required version rejected
breaking change requires contract bump
historical workflow application records version used
deprecated version not silently rewritten
```

---

# 18. Codex Implementation Notes

Codex must:

```text
read this README before implementing test contracts
generate tests from contract files, not assumptions
cite the contract being tested
cite related common contracts
cite related API/service/workflow/agent specs
write positive and negative tests
write PermissionDenied tests
write PolicyRestricted tests
write AI forbidden-action tests
write HumanReviewRequired tests
write idempotency replay tests
write event non-duplication tests
write safe error tests
write version unsupported tests
keep fixtures deterministic and non-production
```

Codex must not:

```text
treat passing happy-path tests as sufficient
skip negative tests
mock away Permission and Policy behavior without asserting invocation
allow AI tests to pass protected execution
assert event emission from API/workflow layer
use production data as fixtures
expose database IDs in expected outputs
ignore restricted_fields_omitted
ignore historical version trace
```

---

# 19. Acceptance Criteria

This Test Contracts README is accepted only if:

```text
[ ] It defines Test Contract purpose.
[ ] It defines Core Lock.
[ ] It defines what Test Contracts are.
[ ] It defines what Test Contracts are not.
[ ] It defines required Test Contract files.
[ ] It defines naming rules.
[ ] It defines required sections.
[ ] It defines global test principles.
[ ] It defines common test categories.
[ ] It defines fixture strategy.
[ ] It defines API Contract test requirements.
[ ] It defines Workflow Contract test requirements.
[ ] It defines Common Contract test requirements.
[ ] It defines Agent Boundary test requirements.
[ ] It defines Permission / Policy test requirements.
[ ] It defines Idempotency / Event test requirements.
[ ] It defines Error / Versioning test requirements.
[ ] It defines Codex implementation notes.
```

---

# 20. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Test Contracts README. Defines testing purpose, contract file inventory, naming rules, required sections, global test principles, fixture strategy, API/workflow/common/agent/permission-policy/idempotency-event/error-versioning test requirements and Codex implementation expectations. |

---

**End of Test Contracts README**
