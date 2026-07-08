# Test Contracts — Index

**Spec ID:** B02-CONTRACT-TESTS-INDEX  
**Spec Type:** Test Contract Index  
**Contract File:** core-specs/contracts/tests/index.md  
**Contract Category:** Test Contracts  
**Related Files:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md  
**Related Test Contracts:** core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md; core-specs/contracts/tests/workflow-contract-tests.md; core-specs/contracts/tests/agent-boundary-tests.md; core-specs/contracts/tests/permission-policy-tests.md; core-specs/contracts/tests/idempotency-event-tests.md; core-specs/contracts/tests/error-versioning-tests.md  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Agent Contracts; Event Contracts  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Cross-Cutting Quality Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This index provides the canonical inventory and governance map for all Test Contracts under:

```text
core-specs/contracts/tests/
```

It defines:

```text
test contract file inventory
test contract priority
test contract coverage boundary
test-to-contract-layer mapping
test-to-service-boundary mapping
test-to-risk mapping
common required fixtures
common test principles
MVP implementation order
Codex implementation checklist
acceptance criteria
```

This index is a navigation and governance artifact. It is not a test implementation file and does not replace individual Test Contract files.

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
Unsupported versions fail closed.
```

This lock applies to every Test Contract listed in this index.

---

# 3. Canonical Test Contract Inventory

| No. | Test Contract | File | MVP Depth | Status |
|---:|---|---|---|---|
| 1 | Test Contracts README | core-specs/contracts/tests/README.md | Must Implement | Draft |
| 2 | Test Contract Template | core-specs/contracts/tests/template.md | Must Maintain | Draft |
| 3 | Common Contract Tests | core-specs/contracts/tests/common-contract-tests.md | Must Implement | Draft |
| 4 | API Contract Tests | core-specs/contracts/tests/api-contract-tests.md | Must Implement | Draft |
| 5 | Workflow Contract Tests | core-specs/contracts/tests/workflow-contract-tests.md | Must Implement | Draft |
| 6 | Agent Boundary Tests | core-specs/contracts/tests/agent-boundary-tests.md | Should Implement | Draft |
| 7 | Permission Policy Tests | core-specs/contracts/tests/permission-policy-tests.md | Must Implement | Draft |
| 8 | Idempotency Event Tests | core-specs/contracts/tests/idempotency-event-tests.md | Must Implement | Draft |
| 9 | Error Versioning Tests | core-specs/contracts/tests/error-versioning-tests.md | Must Implement | Draft |
| 10 | Test Contracts Index | core-specs/contracts/tests/index.md | Must Maintain | Draft |

---

# 4. Test Contract Priority

## 4.1 Must Implement

```text
README.md
common-contract-tests.md
api-contract-tests.md
workflow-contract-tests.md
permission-policy-tests.md
idempotency-event-tests.md
error-versioning-tests.md
```

Reason:

```text
These files form the minimum acceptance layer for Core:
- shared contract primitives
- API boundary behavior
- workflow coordination behavior
- permission/policy governance
- idempotency and event trace
- safe errors and version compatibility
```

## 4.2 Should Implement

```text
agent-boundary-tests.md
```

Reason:

```text
Agent boundary tests are essential before AI-assisted execution expands.
They may be staged after base API/workflow/permission/idempotency/error tests, but must exist before AI-driven production behavior is trusted.
```

## 4.3 Must Maintain

```text
template.md
index.md
```

Reason:

```text
Template and index preserve consistency, navigation and governance for future Test Contracts.
```

---

# 5. Test Contract Boundary Matrix

| Test Contract | Verifies | Must Not Become |
|---|---|---|
| Common Contract Tests | shared primitives, fail-closed behavior, safe context reuse | domain business logic tests |
| API Contract Tests | request/response, API boundary, service delegation | service implementation replacement |
| Workflow Contract Tests | preview/apply, coordination, step boundaries | workflow engine implementation |
| Agent Boundary Tests | AI capability scope, forbidden actions, source/policy disclosure | generic model-quality benchmark |
| Permission Policy Tests | access and contextual restriction matrix | permission grant or policy approval mechanism |
| Idempotency Event Tests | duplicate prevention and trace integrity | event streaming infrastructure design |
| Error Versioning Tests | safe failures and compatibility behavior | logging framework or incident playbook |

---

# 6. Test-to-Contract-Layer Mapping

```text
Common Contract Tests
  Common Contracts
  API Contracts
  Workflow Contracts

API Contract Tests
  API Contracts
  Common Contracts
  Service Specs
  Agent Specs where applicable

Workflow Contract Tests
  Workflow Contracts
  Workflow Contract API
  Common Contracts
  Service Specs
  Agent Specs where applicable

Agent Boundary Tests
  Agent Specs
  AI Context Contract
  Permission Context Contract
  Policy Context Contract
  Human Review Contract
  API and Workflow Contracts where agents are used

Permission Policy Tests
  Permission Context Contract
  Policy Context Contract
  Permission API
  Policy API
  All protected API/Workflow/Agent behaviors

Idempotency Event Tests
  Idempotency Contract
  Audit Context Contract
  Event API Contract
  Event Specs
  Duplicate-sensitive API/Workflow behaviors

Error Versioning Tests
  Error Contract
  Versioning Contract
  API Contracts
  Workflow Contracts
  Event Specs
  Agent Specs
```

---

# 7. Test-to-Service Boundary Mapping

| Test Contract | Required Service Boundary Assertions |
|---|---|
| Common Contract Tests | Common contracts do not own domain behavior |
| API Contract Tests | API layer delegates mutation/behavior to owning services |
| Workflow Contract Tests | Workflow Contract Service coordinates; owning services mutate; Task Service creates Tasks |
| Agent Boundary Tests | Agent Service governs capability; downstream actions route through owning services |
| Permission Policy Tests | Permission Service evaluates Permission; Policy Service evaluates Policy |
| Idempotency Event Tests | owning services emit events; Event Service owns retrieval; duplicate effects prevented |
| Error Versioning Tests | every service returns safe errors and respects version compatibility |

---

# 8. Test-to-Risk Mapping

| Risk | Required Test Coverage |
|---|---|
| Database ID leakage | Common, API, Error Versioning |
| Restricted data leakage | Policy, Error, Event, Agent tests |
| Permission bypass | Permission Policy, API, Workflow, Agent tests |
| Policy bypass | Permission Policy, API, Workflow, Agent tests |
| AI autonomous execution | Agent Boundary, Workflow, API tests |
| Missing human review | Workflow, API, Agent, Permission Policy tests |
| Duplicate execution | Idempotency Event, API, Workflow tests |
| Duplicate events | Idempotency Event tests |
| API mutating directly | API Contract Tests |
| Workflow mutating directly | Workflow Contract Tests |
| Agent mutating directly | Agent Boundary Tests |
| Unsafe errors | Common, Error Versioning, all boundary tests |
| Unsupported version accepted | Error Versioning, API, Workflow, Agent, Event tests |
| Historical trace rewritten | Error Versioning, Workflow, Event tests |
| Event treated as command | Idempotency Event, Common, Agent tests |

---

# 9. Common Required Fixtures

All Test Contracts may reuse these fixture families:

```text
Reference Fixture
Permission Fixture
Policy Fixture
AI Context Fixture
Human Review Fixture
Idempotency Fixture
Event Trace Fixture
Version Fixture
Error Fixture
Domain Object Fixture
Workflow Fixture
API Request Fixture
API Response Fixture
Agent Registry Fixture
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain production data.
- Fixtures must include positive and negative cases.
- Fixtures must include permission-allowed, permission-denied and unknown-permission cases.
- Fixtures must include policy-allowed, policy-restricted, redacted and non-disclosure cases.
- Fixtures must include AI-assisted and non-AI-assisted cases where applicable.
- Fixtures must include human-review-present and missing-review cases where applicable.
- Fixtures must include idempotent replay and conflict cases.
- Fixtures must include supported, missing, unsupported and deprecated version cases.
```

---

# 10. Common Test Principles

Every Test Contract must enforce:

```text
Core boundary first
Fail closed by default
No silent permission bypass
No silent policy bypass
No AI autonomous protected action
No direct event emission from API/Workflow/Agent layers
No duplicate effects on replay
No database ID leakage
No restricted-field leakage
No hidden human-review requirement
No silent version rewrite
No production data fixtures
```

---

# 11. Required Global Test Categories

Every implementation acceptance suite must include:

```text
Positive path tests
Negative path tests
Reference validation tests
PermissionDenied tests
PolicyRestricted tests
Redaction tests
Non-disclosure tests
AI forbidden-action tests where applicable
HumanReviewRequired tests where applicable
Idempotency replay tests where applicable
Idempotency conflict tests where applicable
Event ownership tests
Event non-duplication tests
Safe error tests
VersionUnsupported tests
Historical version trace tests where applicable
```

---

# 12. MVP Implementation Order

Recommended Codex implementation order:

```text
1. Test Contracts README
2. Test Contract Template
3. Common Contract Tests
4. Permission Policy Tests
5. Error Versioning Tests
6. Idempotency Event Tests
7. API Contract Tests
8. Workflow Contract Tests
9. Agent Boundary Tests
10. Test Contracts Index
```

Reasoning:

```text
- README and template establish the testing system.
- Common contract tests establish shared primitives.
- Permission/Policy and Error/Versioning tests establish fail-closed governance.
- Idempotency/Event tests establish duplicate-safe trace behavior.
- API and Workflow tests validate operational boundaries.
- Agent Boundary tests validate AI expansion after base governance is in place.
- Index closes the test layer as a navigable contract system.
```

---

# 13. Contract Coverage Matrix

```yaml
coverage_matrix:
  common_contracts:
    required: true
    covered_by:
      - core-specs/contracts/tests/common-contract-tests.md
  api_contracts:
    required: true
    covered_by:
      - core-specs/contracts/tests/api-contract-tests.md
  workflow_contracts:
    required: true
    covered_by:
      - core-specs/contracts/tests/workflow-contract-tests.md
  agent_boundaries:
    required: true
    covered_by:
      - core-specs/contracts/tests/agent-boundary-tests.md
  permission_policy:
    required: true
    covered_by:
      - core-specs/contracts/tests/permission-policy-tests.md
  idempotency_events:
    required: true
    covered_by:
      - core-specs/contracts/tests/idempotency-event-tests.md
  errors_versioning:
    required: true
    covered_by:
      - core-specs/contracts/tests/error-versioning-tests.md
```

---

# 14. Codex Implementation Notes

Codex must:

```text
read this Test Contracts Index before implementing test suites
read Test Contracts README before implementing test suites
use Test Contract Template for new Test Contracts
cite the specific Test Contract being implemented
cite the source contracts being tested
generate deterministic non-production fixtures
write positive and negative tests
write PermissionDenied tests
write PolicyRestricted tests
write redaction and non-disclosure tests
write AI forbidden-action tests where applicable
write HumanReviewRequired tests where applicable
write idempotency replay and conflict tests where applicable
write event ownership and non-duplication tests
write safe error tests
write VersionUnsupported tests
assert no database IDs are exposed
assert restricted_fields_omitted where redaction occurs
assert policy_omissions_disclosed for AI omissions
assert no direct event emission from API/Workflow/Agent layers
assert no silent historical version rewrite
```

Codex must not:

```text
treat happy-path tests as sufficient
skip negative tests
skip permission/policy tests
skip idempotency tests for duplicate-sensitive behavior
skip version tests
use production data
mock away Permission or Policy without asserting invocation
allow API/Workflow/Agent layers to own domain mutation
allow AI to execute protected actions
allow event references to become commands
expose restricted data through expected outputs
silently accept unsupported versions
```

---

# 15. Acceptance Criteria

This Test Contracts Index is accepted only if:

```text
[ ] It lists all canonical Test Contract files.
[ ] It identifies MVP depth for each Test Contract.
[ ] It defines Test Contract priority.
[ ] It defines boundary matrix.
[ ] It defines test-to-contract-layer mapping.
[ ] It defines test-to-service-boundary mapping.
[ ] It defines test-to-risk mapping.
[ ] It defines common required fixtures.
[ ] It defines common test principles.
[ ] It defines required global test categories.
[ ] It defines MVP implementation order.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 16. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Test Contracts Index. Defines canonical test inventory, priority, boundary matrix, contract/service/risk mappings, common fixtures, global test principles, implementation order, coverage matrix and Codex expectations. |

---

**End of Test Contracts Index**
