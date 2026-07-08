# Test Contract Template

**Spec ID:** B02-CONTRACT-TESTS-TEMPLATE  
**Spec Type:** Test Contract Template  
**Contract File:** core-specs/contracts/tests/template.md  
**Contract Category:** Test Contracts  
**Template Version:** v0.1.0  
**Contract Version:** v0.1.0  
**Status:** Draft  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 0. How to Use This Template

Use this template for every file under:

```text
core-specs/contracts/tests/
```

Target file naming:

```text
core-specs/contracts/tests/{test-area}-tests.md
```

This template must be copied and completed, not referenced as a final test contract by itself.

Core rule:

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

---

# 1. Metadata

```yaml
spec_id: B02-CONTRACT-TESTS-{TEST-AREA}
spec_type: Test Contract Specification
contract_name: "{Test Area} Test Contract"
contract_file: "core-specs/contracts/tests/{test-area}-tests.md"
contract_category: Test Contracts
related_contract_layers:
  - Common Contracts
  - API Contracts
  - Workflow Contracts
  - Agent Contracts
related_common_contracts:
  - core-specs/contracts/common/references.md
  - core-specs/contracts/common/errors.md
  - core-specs/contracts/common/pagination.md
  - core-specs/contracts/common/audit-context.md
  - core-specs/contracts/common/permission-context.md
  - core-specs/contracts/common/policy-context.md
  - core-specs/contracts/common/ai-context.md
  - core-specs/contracts/common/human-review.md
  - core-specs/contracts/common/idempotency.md
  - core-specs/contracts/common/versioning.md
related_api_contracts:
  - core-specs/contracts/api/{api-name}-api-contract.md
related_workflow_contracts:
  - core-specs/contracts/workflows/{workflow-name}-workflow-contract.md
related_agent_specs:
  - core-specs/agents/{agent-name}.md
related_service_specs:
  - core-specs/services/{service-name}-service.md
status: Draft
version: 0.1.0
contract_version: v0.1.0
test_contract_version: v0.1.0
mvp_phase: "{Phase}"
mvp_depth: "{Must Implement | Should Implement | Must Maintain}"
owner: MarkOrbit Publications Editorial Board
```

---

# 2. Purpose

This Test Contract defines acceptance-level testing requirements for:

```text
{test area}
```

It standardizes how Codex and implementation teams verify:

```text
contract behavior
service ownership boundary
reference validation
permission enforcement
policy enforcement
AI boundary enforcement
human review gating
idempotency behavior
event trace behavior
safe error behavior
version compatibility
restricted-field handling
```

This Test Contract does not implement the tests by itself, choose a test framework, or replace the source contract being tested.

---

# 3. Core Lock

```text
{Test Area} tests verify governed Core behavior.
Tests must fail closed where behavior is unsafe or ambiguous.
Owning services own behavior.
Permission and Policy must be explicitly evaluated.
AI must not execute protected actions.
Human review must gate protected actions where required.
Idempotency must prevent duplicate execution.
Events must preserve trace without becoming commands.
Errors must remain safe.
```

---

# 4. Test Boundary

This Test Contract is responsible for:

```text
defining required test subjects
defining required fixtures
defining positive test rules
defining negative test rules
defining Permission tests
defining Policy tests
defining AI boundary tests
defining Human Review tests
defining Idempotency tests
defining Event Trace tests
defining Error Safety tests
defining Versioning tests
defining Codex implementation expectations
```

This Test Contract is not responsible for:

```text
implementation code
test framework selection
production data preparation
UI-only test scripts
load/performance testing unless explicitly added
permission grant
policy approval
contract behavior expansion
```

---

# 5. Related Contracts

List all source contracts that this test contract validates:

```text
core-specs/contracts/{layer}/{contract-file}.md
```

Rules:

```text
- Every tested behavior must trace to a source contract.
- Test contracts must not invent behavior that source contracts do not require.
- Where multiple contracts overlap, stricter boundary rule wins.
```

---

# 6. Test Subject

Define what is tested:

```yaml
test_subject:
  subject_type: string
  subject_name: string
  owning_service: string | null
  contract_file: string
  behavior_scope:
    - string
```

Allowed subject types:

```text
CommonContract
APIContract
WorkflowContract
AgentBoundary
PermissionPolicyBoundary
IdempotencyEventBoundary
ErrorVersioningBoundary
CrossContractBehavior
Unknown
```

---

# 7. Required Fixtures

Fixture shape:

```yaml
fixtures:
  - fixture_key: string
    fixture_type: string
    purpose: string
    contains_production_data: false
    required: true
    fixture_contract_refs:
      - string
```

Required fixture types:

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
Error Fixture
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain real customer data.
- Fixtures must include positive and negative cases.
- Fixtures must include valid and invalid references.
- Fixtures must include PermissionAllowed and PermissionDenied cases.
- Fixtures must include PolicyAllowed, PolicyRestricted and redacted-output cases.
- Fixtures must include AI-assisted and non-AI-assisted cases where applicable.
- Fixtures must include human-review-present and human-review-missing cases where applicable.
- Fixtures must include duplicate idempotency cases where applicable.
- Fixtures must include supported and unsupported version cases.
```

---

# 8. Positive Test Rules

Positive tests must verify expected valid behavior.

Canonical positive test case shape:

```yaml
positive_tests:
  - test_key: string
    test_title: string
    given:
      - string
    when:
      - string
    then:
      - string
    required_contract_refs:
      - string
```

Positive tests should prove:

```text
valid request accepted
valid reference validated by owning service
required Permission Context accepted
required Policy Context accepted
allowed fields returned
safe output shape preserved
version supported
idempotent replay safe
event trace returned where allowed
```

---

# 9. Negative Test Rules

Negative tests must verify unsafe behavior is blocked.

Canonical negative test case shape:

```yaml
negative_tests:
  - test_key: string
    test_title: string
    given:
      - string
    when:
      - string
    then:
      - string
    expected_error_code: string | null
    required_contract_refs:
      - string
```

Negative tests should prove:

```text
missing required reference rejected
invalid reference rejected
database ID rejected or hidden
missing Permission Context blocked
PermissionDenied blocked
missing Policy Context blocked for policy-controlled actions
PolicyRestricted blocked or downgraded safely
AI forbidden action blocked
missing human review blocked
duplicate conflicting idempotency request rejected
unsupported version rejected
unsafe error data not exposed
```

---

# 10. Reference Tests

Reference tests must include:

```text
valid reference accepted
invalid reference rejected
missing required reference rejected
wrong-type reference rejected
cross-domain reference validated by owning service
reference validation does not imply read permission
database ID not exposed in response or error
```

Reference test case skeleton:

```yaml
reference_tests:
  - test_key: reference-valid
    given:
      - valid reference fixture
    when:
      - operation validates reference
    then:
      - response uses *_reference_id
      - owning service validation is invoked
      - database id is not exposed
```

---

# 11. Permission Tests

Permission tests must include:

```text
required permission key present
Permission Service invoked
PermissionAllowed permits next policy evaluation
PermissionDenied stops protected behavior
PermissionDenied does not leak protected content
Permission approval does not bypass Policy
permission decision visibility follows Policy
```

Permission matrix:

```text
PermissionAllowed + PolicyAllowed = action may proceed
PermissionDenied + PolicyAllowed = blocked
UnknownPermission + AnyPolicy = blocked
```

---

# 12. Policy Tests

Policy tests must include:

```text
required policy scope present
Policy Service invoked
PolicyAllowed permits allowed output
PolicyRestricted blocks or downgrades safely
redacted output sets restricted_fields_omitted = true
restricted total_count omitted where required
NotFound may replace PolicyRestricted where non-disclosure is required
policy internals not exposed
```

Policy matrix:

```text
PermissionAllowed + PolicyAllowed = action may proceed
PermissionAllowed + PolicyRestricted = blocked or downgraded
AnyPermission + UnknownPolicy for policy-controlled action = blocked
```

---

# 13. AI Boundary Tests

AI boundary tests must include where applicable:

```text
AI Context required for AI-assisted operation
agent reference validated
agent capability scope enforced
source scope disclosed
policy omissions disclosed
human_review_required preserved
AI cannot approve
AI cannot send
AI cannot select provider
AI cannot submit filing
AI cannot certify deadline
AI cannot certify authority
AI cannot decide registrability
AI cannot decide evidence sufficiency
AI cannot approve payment
AI cannot complete task
```

AI forbidden action test skeleton:

```yaml
ai_boundary_tests:
  - test_key: ai-forbidden-action
    given:
      - AI-assisted request
      - protected action requested
    when:
      - operation is evaluated
    then:
      - action is blocked
      - safe error or human_review_required is returned
      - no downstream protected state change occurs
```

---

# 14. Human Review Tests

Human Review tests must include:

```text
human review required before protected action
missing review blocks or downgrades action
valid review reference accepted
review record does not execute downstream action by itself
owning service decides whether review satisfies requirements
review trace preserved where policy allows
```

Human Review test skeleton:

```yaml
human_review_tests:
  - test_key: human-review-required
    given:
      - protected action request
      - missing human_review_reference_id
    when:
      - operation is evaluated
    then:
      - HumanReviewRequired is returned
      - no protected downstream action occurs
```

---

# 15. Idempotency Tests

Idempotency tests must include:

```text
idempotency_key required for duplicate-sensitive operations
same key and same semantic request returns safe replay
same key and different semantic request returns conflict
duplicate request does not duplicate object
duplicate request does not duplicate task
duplicate request does not duplicate communication
duplicate request does not duplicate routing selection
duplicate request does not duplicate events
```

Idempotency test skeleton:

```yaml
idempotency_tests:
  - test_key: duplicate-safe-replay
    given:
      - idempotency_key
      - first successful request
    when:
      - same request is replayed
    then:
      - replayed response is safe
      - no duplicate object is created
      - no duplicate event is emitted
```

---

# 16. Event Trace Tests

Event tests must include:

```text
events emitted only by owning services
API layer does not emit events directly
workflow layer does not emit events directly
event references returned only where allowed
event reference is audit trace, not command
duplicate replay does not duplicate events
event visibility follows Policy
```

Event trace test skeleton:

```yaml
event_trace_tests:
  - test_key: no-direct-api-event-emission
    given:
      - API operation request
    when:
      - operation completes
    then:
      - owning service emits event if required
      - API layer does not emit event directly
      - event_reference_ids are trace only
```

---

# 17. Error Safety Tests

Error tests must include:

```text
controlled error code returned
safe error shape preserved
correlation_id preserved
retryable flag present
database IDs not exposed
restricted fields not exposed
private notes not exposed
policy internals not exposed
permission internals not exposed
NotFound substitution applied where required
```

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

---

# 18. Versioning Tests

Versioning tests must include:

```text
supported api_version accepted
supported contract_version accepted
missing required version rejected
unsupported version rejected
breaking change requires version bump
historical workflow application records workflow_contract_version
deprecated version not silently rewritten
```

Versioning test skeleton:

```yaml
versioning_tests:
  - test_key: unsupported-version-fails-closed
    given:
      - unsupported contract_version
    when:
      - operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 19. Contract Coverage Matrix

Use this matrix to show coverage.

```yaml
coverage_matrix:
  references:
    required: true
    covered_by:
      - reference-valid
      - reference-invalid
  permission:
    required: true
    covered_by:
      - permission-allowed
      - permission-denied
  policy:
    required: true
    covered_by:
      - policy-allowed
      - policy-restricted
  ai_boundary:
    required: true
    covered_by:
      - ai-forbidden-action
  human_review:
    required: true
    covered_by:
      - human-review-required
  idempotency:
    required: true
    covered_by:
      - duplicate-safe-replay
  events:
    required: true
    covered_by:
      - no-direct-api-event-emission
  errors:
    required: true
    covered_by:
      - safe-error-shape
  versioning:
    required: true
    covered_by:
      - unsupported-version-fails-closed
```

Rules:

```text
- Every required area must map to at least one test.
- Uncovered required areas block acceptance.
- Coverage matrix must not be used to weaken source contracts.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite this Test Contract
cite the source contract being tested
cite related Common Contracts
cite related API Contracts
cite related Workflow Contracts
cite related Service Specs
generate positive and negative tests
generate permission and policy tests
generate AI forbidden-action tests where applicable
generate HumanReviewRequired tests where applicable
generate idempotency replay and conflict tests where applicable
generate event non-duplication tests where applicable
generate safe error tests
generate version unsupported tests
use deterministic fixtures
avoid production data
assert restricted_fields_omitted where redaction occurs
assert no database IDs are exposed
assert no direct event emission from API/workflow layer
```

Codex must not:

```text
treat happy-path coverage as sufficient
skip negative tests
mock away Permission or Policy without asserting invocation
allow AI tests to execute protected actions
allow workflow preview to create active Tasks
assert events as commands
use production data
ignore safe error requirements
ignore version trace requirements
```

---

# 21. Acceptance Criteria

This Test Contract is accepted only if:

```text
[ ] It defines metadata.
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines positive test rules.
[ ] It defines negative test rules.
[ ] It defines reference tests.
[ ] It defines permission tests.
[ ] It defines policy tests.
[ ] It defines AI boundary tests.
[ ] It defines human review tests.
[ ] It defines idempotency tests.
[ ] It defines event trace tests.
[ ] It defines error safety tests.
[ ] It defines versioning tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Test Contract Template. Defines mandatory test contract structure, fixture rules, positive/negative tests, reference/permission/policy/AI/human-review/idempotency/event/error/versioning test requirements, coverage matrix and Codex implementation expectations. |

---

**End of Test Contract Template**
