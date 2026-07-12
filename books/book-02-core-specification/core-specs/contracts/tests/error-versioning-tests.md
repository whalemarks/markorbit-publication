# Error Versioning Tests

**Spec ID:** B02-CONTRACT-TESTS-ERROR-VERSIONING  
**Spec Type:** Test Contract Specification  
**Contract Name:** Error Versioning Tests  
**Contract File:** core-specs/contracts/tests/error-versioning-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Event Contracts; Agent Contracts  
**Related Common Contracts:** core-specs/contracts/common/errors.md; core-specs/contracts/common/versioning.md; core-specs/contracts/common/references.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md  
**Related API Contracts:** core-specs/contracts/api/*.md  
**Related Workflow Contracts:** core-specs/contracts/workflows/*.md  
**Related Event Specs:** core-specs/events/*.md  
**Related Agent Specs:** core-specs/agents/*.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md; core-specs/contracts/tests/workflow-contract-tests.md; core-specs/contracts/tests/agent-boundary-tests.md; core-specs/contracts/tests/permission-policy-tests.md; core-specs/contracts/tests/idempotency-event-tests.md  
**Related Service Specs:** core-specs/services/*.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Error Safety / Version Compatibility Verification  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Error Versioning Tests define acceptance-level testing requirements for safe error behavior and contract version compatibility across MarkOrbit Core.

They verify:

```text
safe error shape
controlled error codes
error category consistency
correlation_id preservation
retryability indicators
restricted data leakage prevention
database ID leakage prevention
permission/policy internal leakage prevention
AI/prompt/internal reasoning leakage prevention
NotFound substitution behavior
VersionUnsupported fail-closed behavior
contract version compatibility
schema version compatibility
workflow contract version trace
event version trace
agent capability version trace
historical version preservation
Codex implementation acceptance
```

These tests ensure that failures are safe, traceable and compatible with Core version governance.

---

# 2. Core Lock

```text
Error Versioning Tests verify safe failure and compatibility behavior.
Errors must be controlled, safe and traceable.
Errors must not expose restricted data, database IDs, policy internals, permission internals, prompt internals or hidden reasoning.
Unsupported versions must fail closed.
Breaking changes require version bumps.
Historical objects, workflow applications, events and agent outputs must preserve the version used.
Deprecated versions must not be silently rewritten.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing Error Contract shape
testing controlled error codes
testing safe error content
testing restricted data leakage prevention
testing non-disclosure substitution
testing correlation and retryability
testing Versioning Contract shape
testing supported version behavior
testing missing/unsupported version behavior
testing version mismatch behavior
testing historical version trace
testing deprecation behavior
testing API, workflow, event and agent version enforcement
```

This Test Contract is not responsible for:

```text
choosing exception framework
choosing logging vendor
defining production incident playbooks
changing source contract semantics
replacing Permission or Policy checks
replacing domain service validation
```

---

# 4. Related Contracts

This test contract validates:

```text
core-specs/contracts/common/errors.md
core-specs/contracts/common/versioning.md
all API Contracts
all Workflow Contracts
all Event Specs
all Agent Specs
```

Rules:

```text
- Every failure path must return a safe error.
- Every protected action with unsupported version must fail closed.
- Every breaking change must require a version bump.
- Every historical execution trace must preserve version context.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: ErrorVersioningBoundary
  subject_name: Error and Versioning Boundary
  owning_service: varies_by_contract
  contract_file:
    - core-specs/contracts/common/errors.md
    - core-specs/contracts/common/versioning.md
  behavior_scope:
    - safe errors
    - controlled error codes
    - leakage prevention
    - correlation
    - retryability
    - version acceptance
    - version rejection
    - compatibility
    - historical trace
    - deprecation
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: safe-error-fixture
    fixture_type: Error Fixture
    purpose: controlled error shape and safe details
    contains_production_data: false
    required: true

  - fixture_key: restricted-error-fixture
    fixture_type: Error Fixture
    purpose: restricted data leakage testing
    contains_production_data: false
    required: true

  - fixture_key: policy-nondisclosure-error-fixture
    fixture_type: Policy Fixture
    purpose: NotFound substitution and existence hiding
    contains_production_data: false
    required: true

  - fixture_key: permission-error-fixture
    fixture_type: Permission Fixture
    purpose: PermissionDenied safe error testing
    contains_production_data: false
    required: true

  - fixture_key: policy-error-fixture
    fixture_type: Policy Fixture
    purpose: PolicyRestricted safe error testing
    contains_production_data: false
    required: true

  - fixture_key: ai-error-fixture
    fixture_type: AI Context Fixture
    purpose: prompt/internal reasoning/source leakage testing
    contains_production_data: false
    required: true

  - fixture_key: supported-version-fixture
    fixture_type: Version Fixture
    purpose: supported api/contract/schema/workflow/event/agent versions
    contains_production_data: false
    required: true

  - fixture_key: unsupported-version-fixture
    fixture_type: Version Fixture
    purpose: unsupported and malformed versions
    contains_production_data: false
    required: true

  - fixture_key: missing-version-fixture
    fixture_type: Version Fixture
    purpose: missing required version fields
    contains_production_data: false
    required: true

  - fixture_key: historical-version-fixture
    fixture_type: Version Fixture
    purpose: historical workflow application, event and agent output version trace
    contains_production_data: false
    required: true

  - fixture_key: deprecation-fixture
    fixture_type: Version Fixture
    purpose: deprecated version warning/blocking behavior
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain production data.
- Fixtures must include positive and negative cases.
- Fixtures must include restricted data designed to test leakage prevention.
- Fixtures must include supported, unsupported, missing and deprecated version cases.
```

---

# 7. Safe Error Shape Tests

Safe error shape tests must verify:

```text
error.code exists
error.category exists
error.message exists
error.safe_detail is safe or null
error.correlation_id preserved where provided
error.retryable is boolean
error does not expose stack traces
error does not expose database IDs
error does not expose private notes
```

Test skeleton:

```yaml
safe_error_tests:
  - test_key: error-safe-shape
    test_title: Error Uses Safe Contract Shape
    given:
      - controlled failure
      - correlation_id
    when:
      - error response is generated
    then:
      - error.code exists
      - error.category exists
      - error.message exists
      - error.correlation_id is preserved
      - error.retryable is present
      - no restricted internals are exposed
```

---

# 8. Controlled Error Code Tests

Controlled error code tests must verify:

```text
ReferenceInvalid used for invalid references
ValidationFailed used for invalid schema where appropriate
PermissionDenied used for permission failures
PolicyRestricted used for policy failures
HumanReviewRequired used for missing review gates
IdempotencyKeyRequired used for missing idempotency key
IdempotencyConflict used for semantic idempotency conflict
VersionUnsupported used for unsupported version
StateInvalid used for invalid state
InternalError used only for safe unexpected failures
```

Test skeleton:

```yaml
controlled_error_code_tests:
  - test_key: controlled-error-code-version-unsupported
    test_title: Unsupported Version Uses VersionUnsupported
    given:
      - unsupported contract_version
    when:
      - operation is evaluated
    then:
      - error.code is VersionUnsupported
      - no protected action occurs
```

---

# 9. Leakage Prevention Tests

Leakage prevention tests must verify errors do not expose:

```text
database IDs
raw customer data
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

Test skeleton:

```yaml
leakage_tests:
  - test_key: error-no-restricted-data-leakage
    test_title: Error Does Not Leak Restricted Data
    given:
      - failure involving restricted object
      - policy restricts object visibility
    when:
      - error response is generated
    then:
      - restricted fields are not present
      - database IDs are not present
      - policy internals are not present
      - permission internals are not present
```

---

# 10. Non-Disclosure Error Tests

Non-disclosure tests must verify:

```text
NotFound may replace PolicyRestricted where policy requires non-disclosure
object existence is not revealed
safe_detail does not reveal existence
pagination counts do not reveal hidden objects where restricted
event trace does not reveal hidden objects
idempotency replay does not leak hidden prior result
```

Test skeleton:

```yaml
nondisclosure_error_tests:
  - test_key: error-nondisclosure-notfound
    test_title: Non-disclosure Policy Returns NotFound
    given:
      - object exists
      - policy requires non-disclosure
    when:
      - read operation fails due to visibility
    then:
      - NotFound is returned
      - object existence is not disclosed
      - restricted data is not exposed
```

---

# 11. Permission / Policy Error Tests

Permission and Policy error tests must verify:

```text
PermissionDenied is safe
PolicyRestricted is safe
PermissionDenied does not reveal hidden policy details
PolicyRestricted does not reveal policy internals
PermissionDenied and PolicyRestricted do not expose restricted object data
Permission and Policy decision references are returned only where policy allows
```

Test skeleton:

```yaml
permission_policy_error_tests:
  - test_key: permission-policy-error-safe
    test_title: Permission and Policy Errors Are Safe
    given:
      - protected request
      - PermissionDenied or PolicyRestricted decision
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - restricted fields are not exposed
      - permission/policy internals are not exposed
```

---

# 12. AI Error Safety Tests

AI error tests must verify:

```text
agent prompt internals not exposed
hidden reasoning not exposed
restricted source data not exposed
policy-omitted source details not exposed
model/provider raw errors sanitized
tool raw errors sanitized
AI output failure preserves correlation_id
AI output failure does not become professional truth
```

Test skeleton:

```yaml
ai_error_tests:
  - test_key: ai-error-no-prompt-or-reasoning-leakage
    test_title: AI Error Does Not Leak Prompt Internals or Hidden Reasoning
    given:
      - agent-assisted operation fails
    when:
      - error response is generated
    then:
      - prompt internals are not exposed
      - hidden reasoning is not exposed
      - restricted source data is not exposed
      - safe error shape is preserved
```

---

# 13. Correlation and Retryability Tests

Correlation and retryability tests must verify:

```text
correlation_id preserved in success and error
causation_event_reference_id preserved where allowed
retryable true only for safe retry cases
retryable false for validation, permission, policy and version errors unless contract says otherwise
idempotency conflict retryability is false unless semantic request changes
InternalError may be retryable only if safe
```

Test skeleton:

```yaml
correlation_retry_tests:
  - test_key: error-correlation-preserved
    test_title: Error Preserves Correlation ID
    given:
      - request with correlation_id
      - operation fails
    when:
      - error response is generated
    then:
      - error.correlation_id equals request correlation_id
      - error.retryable is present
```

---

# 14. Supported Version Tests

Supported version tests must verify:

```text
supported api_version accepted
supported contract_version accepted
supported schema_version accepted
supported workflow_contract_version accepted
supported event_version accepted
supported agent_contract_version accepted
response preserves version where required
historical trace records version used
```

Test skeleton:

```yaml
supported_version_tests:
  - test_key: supported-version-accepted
    test_title: Supported Contract Version Is Accepted
    given:
      - supported version fields
    when:
      - operation is evaluated
    then:
      - operation may proceed
      - response preserves relevant version fields
```

---

# 15. Missing Version Tests

Missing version tests must verify:

```text
missing required api_version rejected
missing required contract_version rejected
missing required schema_version rejected
missing required workflow_contract_version rejected for workflow application
missing event_version rejected where event version is required
missing agent_contract_version rejected where agent version is required
no protected action occurs
```

Test skeleton:

```yaml
missing_version_tests:
  - test_key: missing-version-rejected
    test_title: Missing Required Version Is Rejected
    given:
      - request missing required contract_version
    when:
      - operation is evaluated
    then:
      - VersionUnsupported or ValidationFailed is returned
      - no protected action occurs
```

---

# 16. Unsupported Version Tests

Unsupported version tests must verify:

```text
unsupported api_version fails closed
unsupported contract_version fails closed
unsupported schema_version fails closed
unsupported workflow_contract_version fails closed
unsupported event_version fails closed
unsupported agent_contract_version fails closed
no protected action occurs
safe VersionUnsupported error returned
```

Test skeleton:

```yaml
unsupported_version_tests:
  - test_key: unsupported-version-fails-closed
    test_title: Unsupported Version Fails Closed
    given:
      - unsupported contract_version
    when:
      - protected operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 17. Version Mismatch Tests

Version mismatch tests must verify:

```text
api_version and contract_version mismatch rejected where incompatible
contract_version and schema_version mismatch rejected where incompatible
workflow_contract_version mismatch rejected for workflow apply
event spec version mismatch rejected where incompatible
agent capability version mismatch rejected
safe error returned
no protected action occurs
```

Test skeleton:

```yaml
version_mismatch_tests:
  - test_key: version-mismatch-rejected
    test_title: Incompatible Version Mismatch Is Rejected
    given:
      - api_version compatible with old schema
      - contract_version requiring new schema
    when:
      - operation is evaluated
    then:
      - VersionUnsupported or ValidationFailed is returned
      - no protected action occurs
```

---

# 18. Breaking Change Tests

Breaking change tests must verify:

```text
required field removal requires version bump
required field type change requires version bump
controlled value removal requires version bump
permission key semantic change requires version bump
policy scope semantic change requires version bump
workflow step key removal requires workflow version bump
event payload breaking change requires event version bump
agent capability expansion requires agent version bump
```

Test skeleton:

```yaml
breaking_change_tests:
  - test_key: breaking-change-requires-version-bump
    test_title: Breaking Contract Change Requires Version Bump
    given:
      - contract change removes required field
      - version unchanged
    when:
      - contract compatibility validation runs
    then:
      - compatibility test fails
      - version bump is required
```

---

# 19. Historical Version Trace Tests

Historical trace tests must verify:

```text
workflow application records workflow_contract_version used
event records preserve event_version/schema_version
agent output records agent/capability version where required
API response preserves contract_version
deprecated version output remains traceable
historical records are not rewritten silently
```

Test skeleton:

```yaml
historical_version_tests:
  - test_key: workflow-application-records-version
    test_title: Workflow Application Records Contract Version Used
    given:
      - workflow apply request
      - workflow_contract_version v0.1.0
    when:
      - workflow application is created
    then:
      - workflow_application records v0.1.0
      - later contract version changes do not rewrite historical record
```

---

# 20. Deprecation Tests

Deprecation tests must verify:

```text
deprecated version behavior explicit
deprecated version warning returned where allowed
deprecated version may be blocked if policy requires
deprecated version not silently upgraded
deprecated version not silently rewritten in historical trace
migration path documented where required
```

Test skeleton:

```yaml
deprecation_tests:
  - test_key: deprecated-version-not-silently-upgraded
    test_title: Deprecated Version Is Not Silently Upgraded
    given:
      - request uses deprecated but supported version
    when:
      - operation is evaluated
    then:
      - response preserves requested/effective version context
      - warning may be returned where contract defines it
      - version is not silently rewritten
```

---

# 21. API Error / Versioning Tests

API-specific tests must verify:

```text
API request errors use Error Contract
API response errors do not expose database IDs
API unsupported version fails closed
API version fields preserved in success and error where required
API layer does not convert service errors into unsafe errors
API pagination errors are safe
API idempotency errors are safe
```

Test skeleton:

```yaml
api_error_versioning_tests:
  - test_key: api-version-error-safe
    test_title: API Version Error Is Safe
    given:
      - unsupported api_version
    when:
      - API operation is evaluated
    then:
      - VersionUnsupported is returned
      - error follows Error Contract
      - no protected action occurs
```

---

# 22. Workflow Error / Versioning Tests

Workflow-specific tests must verify:

```text
workflow preview errors are safe
workflow apply errors are safe
workflow unsupported version fails closed
workflow application records workflow_contract_version
workflow skipped steps are safe
workflow apply conflict errors are safe
workflow does not expose restricted target data in errors
```

Test skeleton:

```yaml
workflow_error_versioning_tests:
  - test_key: workflow-version-error-safe
    test_title: Workflow Version Error Is Safe
    given:
      - unsupported workflow_contract_version
    when:
      - workflow apply is evaluated
    then:
      - VersionUnsupported is returned
      - no workflow side effect occurs
      - error does not expose restricted target data
```

---

# 23. Event Error / Versioning Tests

Event-specific tests must verify:

```text
event read errors are safe
event visibility errors are safe
event unsupported version fails closed
event schema version preserved
event references do not expose database IDs
event hidden payload does not leak in errors
historical events remain readable with version context where allowed
```

Test skeleton:

```yaml
event_error_versioning_tests:
  - test_key: event-hidden-error-safe
    test_title: Hidden Event Error Is Safe
    given:
      - event exists
      - policy requires non-disclosure
    when:
      - event read is requested
    then:
      - NotFound or PolicyRestricted is returned according to policy
      - event existence/payload is not leaked
```

---

# 24. Agent Error / Versioning Tests

Agent-specific tests must verify:

```text
agent unsupported version fails closed
agent capability version mismatch rejected
agent prompt/tool errors sanitized
hidden reasoning not exposed
policy-omitted source data not exposed
agent output version trace preserved
agent capability expansion requires version bump
```

Test skeleton:

```yaml
agent_error_versioning_tests:
  - test_key: agent-capability-version-error-safe
    test_title: Agent Capability Version Error Is Safe
    given:
      - agent capability version mismatch
    when:
      - agent-assisted operation is evaluated
    then:
      - VersionUnsupported or CapabilityUnsupported is returned
      - no protected action occurs
      - prompt internals and hidden reasoning are not exposed
```

---

# 25. Contract Coverage Matrix

```yaml
coverage_matrix:
  safe_error_shape:
    required: true
    covered_by:
      - error-safe-shape
  controlled_error_codes:
    required: true
    covered_by:
      - controlled-error-code-version-unsupported
  leakage_prevention:
    required: true
    covered_by:
      - error-no-restricted-data-leakage
  nondisclosure:
    required: true
    covered_by:
      - error-nondisclosure-notfound
  permission_policy_errors:
    required: true
    covered_by:
      - permission-policy-error-safe
  ai_errors:
    required: true
    covered_by:
      - ai-error-no-prompt-or-reasoning-leakage
  correlation_retry:
    required: true
    covered_by:
      - error-correlation-preserved
  supported_versions:
    required: true
    covered_by:
      - supported-version-accepted
  missing_versions:
    required: true
    covered_by:
      - missing-version-rejected
  unsupported_versions:
    required: true
    covered_by:
      - unsupported-version-fails-closed
  version_mismatch:
    required: true
    covered_by:
      - version-mismatch-rejected
  breaking_changes:
    required: true
    covered_by:
      - breaking-change-requires-version-bump
  historical_version_trace:
    required: true
    covered_by:
      - workflow-application-records-version
  deprecation:
    required: true
    covered_by:
      - deprecated-version-not-silently-upgraded
  api:
    required: true
    covered_by:
      - api-version-error-safe
  workflow:
    required: true
    covered_by:
      - workflow-version-error-safe
  event:
    required: true
    covered_by:
      - event-hidden-error-safe
  agent:
    required: true
    covered_by:
      - agent-capability-version-error-safe
```

---

# 26. Codex Implementation Notes

Codex must:

```text
cite this Error Versioning Tests file
cite Error Contract
cite Versioning Contract
cite related API Contracts
cite related Workflow Contracts
cite related Event Specs
cite related Agent Specs
cite Permission Context Contract and Policy Context Contract for restricted error cases
generate deterministic non-production fixtures
write safe error shape tests
write controlled error code tests
write leakage prevention tests
write non-disclosure error tests
write Permission/Policy error tests
write AI error safety tests
write correlation and retryability tests
write supported version tests
write missing version tests
write unsupported version tests
write version mismatch tests
write breaking change tests
write historical version trace tests
write deprecation tests
write API/workflow/event/agent error-versioning tests
assert no database IDs are exposed
assert no restricted data is exposed
assert no policy/permission internals are exposed
assert no prompt internals or hidden reasoning are exposed
assert unsupported versions fail closed
```

Codex must not:

```text
treat InternalError as acceptable without safe shape
expose stack traces
expose database IDs
expose restricted data through errors
expose policy or permission internals
expose prompt internals or hidden reasoning
silently accept unsupported versions
silently rewrite deprecated versions
skip historical version trace tests
ignore breaking change version bumps
mock away error/version behavior without assertions
```

---

# 27. Acceptance Criteria

This Error Versioning Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Common, API, Workflow, Event and Agent Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines Safe Error Shape tests.
[ ] It defines Controlled Error Code tests.
[ ] It defines Leakage Prevention tests.
[ ] It defines Non-Disclosure Error tests.
[ ] It defines Permission / Policy Error tests.
[ ] It defines AI Error Safety tests.
[ ] It defines Correlation and Retryability tests.
[ ] It defines Supported Version tests.
[ ] It defines Missing Version tests.
[ ] It defines Unsupported Version tests.
[ ] It defines Version Mismatch tests.
[ ] It defines Breaking Change tests.
[ ] It defines Historical Version Trace tests.
[ ] It defines Deprecation tests.
[ ] It defines API Error / Versioning tests.
[ ] It defines Workflow Error / Versioning tests.
[ ] It defines Event Error / Versioning tests.
[ ] It defines Agent Error / Versioning tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Error Versioning Tests. Defines safe error shape, controlled error codes, leakage prevention, non-disclosure, Permission/Policy errors, AI errors, correlation/retryability, supported/missing/unsupported/mismatched versions, breaking change checks, historical trace, deprecation, API/workflow/event/agent error-versioning coverage and Codex expectations. |

---

**End of Error Versioning Tests**
