# Common Contract Tests

**Spec ID:** B02-CONTRACT-TESTS-COMMON  
**Spec Type:** Test Contract Specification  
**Contract Name:** Common Contract Tests  
**Contract File:** core-specs/contracts/tests/common-contract-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 0 — Cross-Cutting Contract Foundation  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Common Contract Tests define acceptance-level testing requirements for all shared contract primitives used across MarkOrbit Core.

They verify:

```text
Reference Contract behavior
Error Contract behavior
Pagination Contract behavior
Audit Context behavior
Permission Context behavior
Policy Context behavior
AI Context behavior
Human Review behavior
Idempotency behavior
Versioning behavior
cross-contract reuse consistency
restricted-field omission behavior
safe failure behavior
```

Common Contract Tests ensure that API Contracts, Workflow Contracts, Agent boundaries and service implementations use the same shared rules and fail closed when shared context is missing, malformed, unauthorized, policy-restricted or version-incompatible.

---

# 2. Core Lock

```text
Common Contract Tests verify shared Core primitives.
Shared contracts must be stable and reusable.
References must not expose database IDs.
Errors must be safe.
Permission and Policy contexts must fail closed.
AI context must preserve capability scope.
Human review must not execute downstream action by itself.
Idempotency must prevent duplicate execution.
Versioning must protect compatibility.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing common contract shape
testing shared field names
testing required/optional field behavior
testing fail-closed behavior
testing safe redaction
testing cross-contract consistency
testing restricted-field omission
testing version compatibility
testing deterministic fixture use
```

This Test Contract is not responsible for:

```text
domain-specific service behavior
API endpoint behavior by itself
workflow preview/apply behavior by itself
UI behavior
database schema validation by itself
production data validation
permission grant logic implementation
policy rule implementation
```

---

# 4. Related Contracts

This test contract validates:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/pagination.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/versioning.md
```

Rules:

```text
- Each Common Contract must be tested independently.
- Each Common Contract must be tested in at least one cross-contract usage case.
- Test behavior must trace to the relevant Common Contract.
- Common Contract tests must not invent domain behavior.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: CommonContract
  subject_name: Common Contract Layer
  owning_service: null
  contract_file: core-specs/contracts/common/*
  behavior_scope:
    - reference validation shape
    - safe errors
    - pagination
    - audit trace
    - permission context
    - policy context
    - AI context
    - human review
    - idempotency
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: reference-fixture
    fixture_type: Reference Fixture
    purpose: valid, invalid, missing and wrong-type reference testing
    contains_production_data: false
    required: true

  - fixture_key: error-fixture
    fixture_type: Error Fixture
    purpose: safe error shape and leakage testing
    contains_production_data: false
    required: true

  - fixture_key: pagination-fixture
    fixture_type: Pagination Fixture
    purpose: cursor, limit, total_count and policy omission testing
    contains_production_data: false
    required: true

  - fixture_key: audit-context-fixture
    fixture_type: Event Trace Fixture
    purpose: correlation, causation and event reference testing
    contains_production_data: false
    required: true

  - fixture_key: permission-context-fixture
    fixture_type: Permission Fixture
    purpose: PermissionAllowed, PermissionDenied and unknown permission testing
    contains_production_data: false
    required: true

  - fixture_key: policy-context-fixture
    fixture_type: Policy Fixture
    purpose: PolicyAllowed, PolicyRestricted and redaction testing
    contains_production_data: false
    required: true

  - fixture_key: ai-context-fixture
    fixture_type: AI Context Fixture
    purpose: agent scope, source scope and policy omission testing
    contains_production_data: false
    required: true

  - fixture_key: human-review-fixture
    fixture_type: Human Review Fixture
    purpose: required review, missing review and valid review reference testing
    contains_production_data: false
    required: true

  - fixture_key: idempotency-fixture
    fixture_type: Idempotency Fixture
    purpose: replay, conflict and duplicate-prevention testing
    contains_production_data: false
    required: true

  - fixture_key: version-fixture
    fixture_type: Version Fixture
    purpose: supported, missing and unsupported version testing
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain real customer data.
- Fixtures must include positive and negative cases.
- Fixtures must not require production connectors.
- Fixtures must be reusable by API and Workflow Contract tests.
```

---

# 7. Reference Contract Tests

## 7.1 Positive Tests

```yaml
positive_tests:
  - test_key: reference-valid-shape
    test_title: Valid Reference Shape Is Accepted
    given:
      - a valid *_reference_id
      - supported target_object_type
    when:
      - reference contract validation is performed
    then:
      - reference is accepted
      - database id is not exposed
      - validation result is safe
    required_contract_refs:
      - core-specs/contracts/common/references.md

  - test_key: reference-cross-domain-validation
    test_title: Cross-domain Reference Requires Owning Service Validation
    given:
      - a valid reference to another domain object
    when:
      - contract uses the reference
    then:
      - owning service validation is required
      - valid reference does not imply read permission
    required_contract_refs:
      - core-specs/contracts/common/references.md
```

## 7.2 Negative Tests

```yaml
negative_tests:
  - test_key: reference-invalid
    test_title: Invalid Reference Is Rejected
    given:
      - malformed reference id
    when:
      - reference validation is performed
    then:
      - ReferenceInvalid is returned
      - no protected action occurs
    expected_error_code: ReferenceInvalid
    required_contract_refs:
      - core-specs/contracts/common/references.md

  - test_key: database-id-leak-blocked
    test_title: Database ID Is Not Exposed
    given:
      - internal database id exists
    when:
      - response or error is generated
    then:
      - internal id is not exposed
      - *_reference_id is used instead
    expected_error_code: null
    required_contract_refs:
      - core-specs/contracts/common/references.md
```

---

# 8. Error Contract Tests

## 8.1 Positive Tests

```yaml
positive_tests:
  - test_key: safe-error-shape
    test_title: Error Uses Safe Shape
    given:
      - a controlled contract error
    when:
      - error response is generated
    then:
      - error.code exists
      - error.category exists
      - error.message exists
      - error.safe_detail is safe or null
      - error.correlation_id is preserved
      - error.retryable is present
    required_contract_refs:
      - core-specs/contracts/common/errors.md
```

## 8.2 Negative Tests

```yaml
negative_tests:
  - test_key: error-no-restricted-leakage
    test_title: Error Does Not Leak Restricted Data
    given:
      - restricted object exists
      - policy forbids disclosure
    when:
      - error response is generated
    then:
      - database id is not exposed
      - restricted fields are not exposed
      - policy internals are not exposed
      - permission internals are not exposed
    expected_error_code: null
    required_contract_refs:
      - core-specs/contracts/common/errors.md
```

---

# 9. Pagination Contract Tests

## 9.1 Positive Tests

```yaml
positive_tests:
  - test_key: pagination-valid-cursor
    test_title: Valid Cursor Pagination Is Accepted
    given:
      - cursor fixture
      - limit within allowed range
    when:
      - paginated response is generated
    then:
      - next_cursor is returned where more results exist
      - returned_count is accurate for visible records
      - has_more is accurate
    required_contract_refs:
      - core-specs/contracts/common/pagination.md

  - test_key: pagination-total-count-omitted-by-policy
    test_title: Total Count Can Be Omitted by Policy
    given:
      - policy restricts total count disclosure
    when:
      - paginated response is generated
    then:
      - total_count is null
      - total_count_omitted is true
      - restricted_fields_omitted is true where applicable
    required_contract_refs:
      - core-specs/contracts/common/pagination.md
      - core-specs/contracts/common/policy-context.md
```

## 9.2 Negative Tests

```yaml
negative_tests:
  - test_key: pagination-invalid-limit
    test_title: Invalid Pagination Limit Is Rejected
    given:
      - limit outside allowed range
    when:
      - pagination validation is performed
    then:
      - ValidationFailed is returned
      - no protected data is returned
    expected_error_code: ValidationFailed
    required_contract_refs:
      - core-specs/contracts/common/pagination.md
```

---

# 10. Audit Context Tests

## 10.1 Positive Tests

```yaml
positive_tests:
  - test_key: audit-context-preserves-correlation
    test_title: Audit Context Preserves Correlation
    given:
      - correlation_id
      - causation_event_reference_id
    when:
      - operation result includes audit_context
    then:
      - correlation_id is preserved
      - causation_event_reference_id is preserved where policy allows
      - event_reference_ids are references only
    required_contract_refs:
      - core-specs/contracts/common/audit-context.md
```

## 10.2 Negative Tests

```yaml
negative_tests:
  - test_key: audit-event-is-not-command
    test_title: Event Reference Is Not Treated as Command
    given:
      - event_reference_id in audit context
    when:
      - consuming code reads audit_context
    then:
      - no downstream action is triggered by event reference alone
    expected_error_code: null
    required_contract_refs:
      - core-specs/contracts/common/audit-context.md
```

---

# 11. Permission Context Tests

## 11.1 Positive Tests

```yaml
positive_tests:
  - test_key: permission-context-allowed
    test_title: Permission Allowed Context Is Accepted
    given:
      - required_permission_keys
      - PermissionAllowed decision
    when:
      - protected operation is evaluated
    then:
      - operation may proceed to Policy evaluation
      - permission_decision_reference_id may be recorded where policy allows
    required_contract_refs:
      - core-specs/contracts/common/permission-context.md
```

## 11.2 Negative Tests

```yaml
negative_tests:
  - test_key: permission-context-denied
    test_title: Permission Denied Blocks Protected Operation
    given:
      - required_permission_keys
      - PermissionDenied decision
    when:
      - protected operation is evaluated
    then:
      - PermissionDenied is returned
      - Policy approval does not override denial
      - no protected action occurs
    expected_error_code: PermissionDenied
    required_contract_refs:
      - core-specs/contracts/common/permission-context.md

  - test_key: permission-missing-fails-closed
    test_title: Missing Permission Context Fails Closed
    given:
      - protected operation
      - no Permission Context
    when:
      - operation is evaluated
    then:
      - PermissionDenied or ValidationFailed is returned
      - no protected action occurs
    expected_error_code: PermissionDenied
    required_contract_refs:
      - core-specs/contracts/common/permission-context.md
```

---

# 12. Policy Context Tests

## 12.1 Positive Tests

```yaml
positive_tests:
  - test_key: policy-context-allowed
    test_title: Policy Allowed Context Is Accepted
    given:
      - required_policy_scopes
      - PolicyAllowed decision
      - PermissionAllowed decision
    when:
      - policy-controlled operation is evaluated
    then:
      - operation may proceed
      - allowed fields may be returned
    required_contract_refs:
      - core-specs/contracts/common/policy-context.md
```

## 12.2 Negative Tests

```yaml
negative_tests:
  - test_key: policy-context-restricted
    test_title: Policy Restricted Blocks or Redacts Safely
    given:
      - PermissionAllowed decision
      - PolicyRestricted decision
    when:
      - policy-controlled operation is evaluated
    then:
      - action is blocked or downgraded
      - restricted_fields_omitted is true where redaction occurs
      - policy internals are not exposed
    expected_error_code: PolicyRestricted
    required_contract_refs:
      - core-specs/contracts/common/policy-context.md

  - test_key: policy-missing-fails-closed
    test_title: Missing Policy Context Fails Closed
    given:
      - policy-controlled operation
      - no Policy Context
    when:
      - operation is evaluated
    then:
      - PolicyRestricted or ValidationFailed is returned
      - no protected action occurs
    expected_error_code: PolicyRestricted
    required_contract_refs:
      - core-specs/contracts/common/policy-context.md
```

---

# 13. AI Context Tests

## 13.1 Positive Tests

```yaml
positive_tests:
  - test_key: ai-context-valid-assisted-output
    test_title: Valid AI Context Is Accepted for Assisted Output
    given:
      - ai_assisted is true
      - valid agent_reference_id
      - allowed capability scope
      - source_scope_disclosed is true
    when:
      - AI-assisted preparation is evaluated
    then:
      - AI-assisted output may be returned as assistance
      - policy_omissions_disclosed is preserved
      - human_review_required is preserved
    required_contract_refs:
      - core-specs/contracts/common/ai-context.md
```

## 13.2 Negative Tests

```yaml
negative_tests:
  - test_key: ai-context-missing-for-ai-output
    test_title: AI-Assisted Output Requires AI Context
    given:
      - AI-assisted operation
      - missing AI Context
    when:
      - operation is evaluated
    then:
      - ValidationFailed is returned
      - no AI-assisted output is trusted as governed output
    expected_error_code: ValidationFailed
    required_contract_refs:
      - core-specs/contracts/common/ai-context.md

  - test_key: ai-forbidden-protected-action
    test_title: AI Cannot Execute Protected Action
    given:
      - AI-assisted context
      - protected action request
    when:
      - operation is evaluated
    then:
      - action is blocked
      - human_review_required or safe error is returned
      - no protected state change occurs
    expected_error_code: HumanReviewRequired
    required_contract_refs:
      - core-specs/contracts/common/ai-context.md
      - core-specs/contracts/common/human-review.md
```

---

# 14. Human Review Contract Tests

## 14.1 Positive Tests

```yaml
positive_tests:
  - test_key: human-review-valid-reference
    test_title: Valid Human Review Reference Is Accepted
    given:
      - human_review_required is true
      - valid human_review_reference_id
      - reviewer role satisfies policy
    when:
      - protected action is evaluated
    then:
      - operation may proceed to owning service decision
      - review trace is preserved where policy allows
    required_contract_refs:
      - core-specs/contracts/common/human-review.md
```

## 14.2 Negative Tests

```yaml
negative_tests:
  - test_key: human-review-missing
    test_title: Missing Human Review Blocks Protected Action
    given:
      - human_review_required is true
      - missing human_review_reference_id
    when:
      - protected action is evaluated
    then:
      - HumanReviewRequired is returned
      - no protected downstream action occurs
    expected_error_code: HumanReviewRequired
    required_contract_refs:
      - core-specs/contracts/common/human-review.md

  - test_key: human-review-not-executor
    test_title: Human Review Does Not Execute Downstream Action
    given:
      - valid human review record
    when:
      - review record is created
    then:
      - downstream action is not executed by review record itself
      - owning service must still decide execution
    expected_error_code: null
    required_contract_refs:
      - core-specs/contracts/common/human-review.md
```

---

# 15. Idempotency Contract Tests

## 15.1 Positive Tests

```yaml
positive_tests:
  - test_key: idempotency-safe-replay
    test_title: Same Key and Same Semantic Request Replays Safely
    given:
      - idempotency_key
      - first successful duplicate-sensitive request
    when:
      - same request is replayed
    then:
      - replayed response is safe
      - duplicate object is not created
      - duplicate event is not emitted
    required_contract_refs:
      - core-specs/contracts/common/idempotency.md
```

## 15.2 Negative Tests

```yaml
negative_tests:
  - test_key: idempotency-key-required
    test_title: Missing Idempotency Key Is Rejected
    given:
      - duplicate-sensitive operation
      - missing idempotency_key
    when:
      - operation is evaluated
    then:
      - IdempotencyKeyRequired is returned
      - no duplicate-sensitive action occurs
    expected_error_code: IdempotencyKeyRequired
    required_contract_refs:
      - core-specs/contracts/common/idempotency.md

  - test_key: idempotency-conflict
    test_title: Same Key with Different Semantic Request Fails
    given:
      - idempotency_key already used for different semantic request
    when:
      - conflicting request is submitted
    then:
      - IdempotencyConflict is returned
      - no protected action occurs
    expected_error_code: IdempotencyConflict
    required_contract_refs:
      - core-specs/contracts/common/idempotency.md
```

---

# 16. Versioning Contract Tests

## 16.1 Positive Tests

```yaml
positive_tests:
  - test_key: version-supported
    test_title: Supported Version Is Accepted
    given:
      - supported api_version
      - supported contract_version
      - supported schema_version
    when:
      - contract validation is performed
    then:
      - version is accepted
      - response preserves version fields
    required_contract_refs:
      - core-specs/contracts/common/versioning.md
```

## 16.2 Negative Tests

```yaml
negative_tests:
  - test_key: version-unsupported
    test_title: Unsupported Version Fails Closed
    given:
      - unsupported contract_version
    when:
      - contract validation is performed
    then:
      - VersionUnsupported is returned
      - no protected action occurs
    expected_error_code: VersionUnsupported
    required_contract_refs:
      - core-specs/contracts/common/versioning.md

  - test_key: version-missing
    test_title: Missing Required Version Is Rejected
    given:
      - missing required version field
    when:
      - contract validation is performed
    then:
      - VersionUnsupported or ValidationFailed is returned
      - no protected action occurs
    expected_error_code: VersionUnsupported
    required_contract_refs:
      - core-specs/contracts/common/versioning.md
```

---

# 17. Cross-Contract Consistency Tests

Cross-contract tests must verify:

```text
Permission Context and Policy Context are both required for protected policy-controlled behavior.
AI Context does not bypass Human Review.
Human Review does not bypass Permission or Policy.
Idempotency prevents duplicate Events.
Audit Context event references do not trigger commands.
Pagination redaction follows Policy.
Error responses use Error Contract in all Common Contract failures.
Versioning applies before protected action.
```

Test matrix:

```yaml
cross_contract_tests:
  - test_key: permission-policy-both-required
    required_contract_refs:
      - core-specs/contracts/common/permission-context.md
      - core-specs/contracts/common/policy-context.md

  - test_key: ai-does-not-bypass-human-review
    required_contract_refs:
      - core-specs/contracts/common/ai-context.md
      - core-specs/contracts/common/human-review.md

  - test_key: idempotency-prevents-duplicate-events
    required_contract_refs:
      - core-specs/contracts/common/idempotency.md
      - core-specs/contracts/common/audit-context.md

  - test_key: error-shape-used-on-version-failure
    required_contract_refs:
      - core-specs/contracts/common/errors.md
      - core-specs/contracts/common/versioning.md
```

---

# 18. Contract Coverage Matrix

```yaml
coverage_matrix:
  references:
    required: true
    covered_by:
      - reference-valid-shape
      - reference-invalid
      - database-id-leak-blocked
  errors:
    required: true
    covered_by:
      - safe-error-shape
      - error-no-restricted-leakage
  pagination:
    required: true
    covered_by:
      - pagination-valid-cursor
      - pagination-total-count-omitted-by-policy
      - pagination-invalid-limit
  audit_context:
    required: true
    covered_by:
      - audit-context-preserves-correlation
      - audit-event-is-not-command
  permission:
    required: true
    covered_by:
      - permission-context-allowed
      - permission-context-denied
      - permission-missing-fails-closed
  policy:
    required: true
    covered_by:
      - policy-context-allowed
      - policy-context-restricted
      - policy-missing-fails-closed
  ai_context:
    required: true
    covered_by:
      - ai-context-valid-assisted-output
      - ai-context-missing-for-ai-output
      - ai-forbidden-protected-action
  human_review:
    required: true
    covered_by:
      - human-review-valid-reference
      - human-review-missing
      - human-review-not-executor
  idempotency:
    required: true
    covered_by:
      - idempotency-safe-replay
      - idempotency-key-required
      - idempotency-conflict
  versioning:
    required: true
    covered_by:
      - version-supported
      - version-unsupported
      - version-missing
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Common Contract Tests file
cite every Common Contract being tested
generate fixture-only deterministic tests
write positive and negative tests for each Common Contract
assert Permission and Policy fail closed
assert AI cannot execute protected action
assert Human Review does not execute downstream action by itself
assert Idempotency prevents duplicate effects
assert Audit Context events are trace only
assert Error Contract is used for all failure paths
assert VersionUnsupported fails closed
assert restricted_fields_omitted where redaction occurs
assert no database IDs are exposed
```

Codex must not:

```text
treat happy-path tests as sufficient
skip negative tests for shared contracts
use production data
expose internal IDs in expected output
mock away Permission/Policy without asserting behavior
allow AI tests to pass protected actions
allow event references to trigger commands
ignore version validation
```

---

# 20. Acceptance Criteria

This Common Contract Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Common Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines Reference Contract tests.
[ ] It defines Error Contract tests.
[ ] It defines Pagination Contract tests.
[ ] It defines Audit Context tests.
[ ] It defines Permission Context tests.
[ ] It defines Policy Context tests.
[ ] It defines AI Context tests.
[ ] It defines Human Review tests.
[ ] It defines Idempotency tests.
[ ] It defines Versioning tests.
[ ] It defines Cross-Contract Consistency tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Common Contract Tests. Defines positive/negative tests for references, errors, pagination, audit context, permission context, policy context, AI context, human review, idempotency, versioning and cross-contract consistency, with fixture requirements, coverage matrix and Codex expectations. |

---

**End of Common Contract Tests**
