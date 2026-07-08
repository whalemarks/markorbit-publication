# API Contract Tests

**Spec ID:** B02-CONTRACT-TESTS-API  
**Spec Type:** Test Contract Specification  
**Contract Name:** API Contract Tests  
**Contract File:** core-specs/contracts/tests/api-contract-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** API Contracts; Common Contracts; Agent Contracts  
**Related API Contracts:** core-specs/contracts/api/*.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md  
**Related Service Specs:** core-specs/services/*.md  
**Related Agent Specs:** core-specs/agents/*.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 1–5 — API Boundary Verification  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

API Contract Tests define acceptance-level testing requirements for all MarkOrbit Core API Contracts.

They verify:

```text
API request schema validation
API response schema validation
API version validation
reference validation
owning service boundary
permission enforcement
policy enforcement
AI Context enforcement
human review gating
idempotency behavior
event trace behavior
pagination behavior
safe error behavior
restricted-field omission
no direct event emission from API layer
Codex implementation acceptance
```

API Contract Tests ensure that API endpoints receive governed requests and delegate behavior to owning services without expanding domain ownership, bypassing Permission/Policy, leaking restricted data, or letting AI execute protected actions.

---

# 2. Core Lock

```text
API Contract Tests verify governed API boundaries.
API layer receives requests and returns safe responses.
Owning services own behavior.
References are validated by owning services.
Permission and Policy must fail closed.
AI assistance must remain within governed scope.
Human review gates protected API actions where required.
Idempotency prevents duplicate execution.
API layer must not emit events directly.
Errors must remain safe.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing API request contract shape
testing API response contract shape
testing reference validation behavior
testing service delegation boundary
testing Permission Context behavior
testing Policy Context behavior
testing AI Context behavior
testing Human Review behavior
testing Idempotency behavior
testing Event Trace behavior
testing Pagination behavior
testing Error Contract behavior
testing Versioning behavior
testing restricted-field omission behavior
```

This Test Contract is not responsible for:

```text
service business logic implementation by itself
database schema tests by itself
UI behavior
workflow preview/apply behavior by itself
agent behavior outside API-assisted operations
production data validation
load/performance testing unless separately specified
```

---

# 4. Related Contracts

This test contract validates API Contract files under:

```text
core-specs/contracts/api/
```

It depends on:

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
- Every API Contract must have tests traceable to its contract file.
- Every protected API operation must test Permission and Policy behavior.
- Every API mutation must test owning service delegation.
- Every duplicate-sensitive API operation must test idempotency.
- Every API error path must test safe errors.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: APIContract
  subject_name: API Contract Layer
  owning_service: varies_by_api_contract
  contract_file: core-specs/contracts/api/*.md
  behavior_scope:
    - request validation
    - response validation
    - reference validation
    - permission enforcement
    - policy enforcement
    - AI boundary
    - human review
    - idempotency
    - event trace
    - pagination
    - errors
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: api-request-fixture
    fixture_type: Domain Object Fixture
    purpose: valid and invalid request body/path/query fixtures
    contains_production_data: false
    required: true

  - fixture_key: api-response-fixture
    fixture_type: Domain Object Fixture
    purpose: expected safe response fixtures
    contains_production_data: false
    required: true

  - fixture_key: reference-fixture
    fixture_type: Reference Fixture
    purpose: valid, invalid, missing and wrong-type reference testing
    contains_production_data: false
    required: true

  - fixture_key: permission-fixture
    fixture_type: Permission Fixture
    purpose: PermissionAllowed, PermissionDenied and unknown permission testing
    contains_production_data: false
    required: true

  - fixture_key: policy-fixture
    fixture_type: Policy Fixture
    purpose: PolicyAllowed, PolicyRestricted, redaction and non-disclosure testing
    contains_production_data: false
    required: true

  - fixture_key: ai-context-fixture
    fixture_type: AI Context Fixture
    purpose: AI-assisted API operation testing
    contains_production_data: false
    required: true

  - fixture_key: human-review-fixture
    fixture_type: Human Review Fixture
    purpose: review-required API operation testing
    contains_production_data: false
    required: true

  - fixture_key: idempotency-fixture
    fixture_type: Idempotency Fixture
    purpose: create/update/select/apply duplicate prevention
    contains_production_data: false
    required: true

  - fixture_key: event-trace-fixture
    fixture_type: Event Trace Fixture
    purpose: event_reference_ids and no-direct-event-emission testing
    contains_production_data: false
    required: true

  - fixture_key: error-fixture
    fixture_type: Error Fixture
    purpose: safe error and leakage testing
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
- Fixtures must cover positive and negative cases.
- Fixtures must include Permission and Policy combinations.
- Fixtures must include restricted-field and non-disclosure cases.
- Fixtures must include AI-assisted and non-AI-assisted cases where applicable.
- Fixtures must include idempotent replay and idempotency conflict cases where applicable.
```

---

# 7. API Contract Coverage Scope

Every API Contract must test:

```text
create endpoint where defined
read endpoint where defined
update endpoint where defined
search/list endpoint where defined
validate-reference endpoint where defined
prepare endpoint where defined
evaluate endpoint where defined
select/approve endpoint where defined
AI-assisted endpoint where defined
human-review-gated endpoint where defined
```

Endpoint patterns:

```text
POST /v1/{resources}
GET /v1/{resources}/{reference_id}
PATCH /v1/{resources}/{reference_id}
GET /v1/{resources}
POST /v1/{resources}/validate-reference
POST /v1/{resources}/{reference_id}/prepare-*
POST /v1/{resources}/{reference_id}/evaluate
POST /v1/{resources}/{reference_id}/select
POST /v1/{resources}/{reference_id}/approve
```

---

# 8. Request Schema Tests

## 8.1 Positive Tests

```yaml
positive_tests:
  - test_key: api-request-valid-schema
    test_title: Valid API Request Schema Is Accepted
    given:
      - valid request fixture
      - supported api_version
      - supported contract_version
    when:
      - API request validation is performed
    then:
      - request is accepted
      - required fields are present
      - unknown unsafe fields are rejected or ignored according to contract
    required_contract_refs:
      - core-specs/contracts/api/{api-name}-api-contract.md
      - core-specs/contracts/common/versioning.md
```

## 8.2 Negative Tests

```yaml
negative_tests:
  - test_key: api-request-missing-required-field
    test_title: Missing Required API Field Is Rejected
    given:
      - request missing required field
    when:
      - API request validation is performed
    then:
      - ValidationFailed is returned
      - no owning service mutation occurs
    expected_error_code: ValidationFailed

  - test_key: api-request-unsupported-version
    test_title: Unsupported API Version Fails Closed
    given:
      - unsupported api_version or contract_version
    when:
      - API request validation is performed
    then:
      - VersionUnsupported is returned
      - no protected action occurs
    expected_error_code: VersionUnsupported
```

---

# 9. Response Schema Tests

## 9.1 Positive Tests

```yaml
positive_tests:
  - test_key: api-response-valid-schema
    test_title: API Response Uses Contract Shape
    given:
      - successful API operation
    when:
      - API response is generated
    then:
      - api_version is present
      - contract_version is present
      - correlation_id is preserved where provided
      - result shape follows contract
      - restricted_fields_omitted is present where contract requires it
    required_contract_refs:
      - core-specs/contracts/api/{api-name}-api-contract.md
```

## 9.2 Negative Tests

```yaml
negative_tests:
  - test_key: api-response-no-database-id
    test_title: API Response Does Not Expose Database IDs
    given:
      - internal object has database id
    when:
      - API response is generated
    then:
      - database id is not exposed
      - *_reference_id is used
    expected_error_code: null
```

---

# 10. Reference Validation Tests

Reference tests must include:

```text
valid reference accepted
invalid reference rejected
missing required reference rejected
wrong-type reference rejected
linked domain reference validated by owning service
valid reference does not imply read permission
database ID not exposed
```

Test skeleton:

```yaml
reference_tests:
  - test_key: api-reference-owning-service-validation
    test_title: API Reference Is Validated by Owning Service
    given:
      - request with linked reference
    when:
      - API operation is evaluated
    then:
      - owning service validation is invoked
      - operation proceeds only if validation succeeds
      - no direct database lookup is required in API layer
```

Rules:

```text
- API layer must not treat a reference string as valid without owning service validation where the contract requires validation.
- API layer must not expose existence where policy forbids disclosure.
```

---

# 11. Owning Service Boundary Tests

Every API Contract must prove:

```text
API layer validates request contract.
Owning service owns behavior.
API layer does not mutate domain state directly.
API layer does not emit events directly.
API layer does not bypass Permission or Policy.
```

Test skeleton:

```yaml
service_boundary_tests:
  - test_key: api-delegates-to-owning-service
    test_title: API Delegates Behavior to Owning Service
    given:
      - valid protected mutation request
    when:
      - API operation is performed
    then:
      - owning service is invoked
      - API controller/handler does not mutate state directly
      - service result is returned through safe response contract
```

Negative test:

```yaml
negative_tests:
  - test_key: api-direct-mutation-blocked
    test_title: API Direct Domain Mutation Is Forbidden
    given:
      - implementation attempts mutation in API layer
    when:
      - contract test inspects execution boundary
    then:
      - test fails
      - mutation must route through owning service
```

---

# 12. Permission Tests

Permission tests must include:

```text
required permission key exists for protected endpoint
Permission Service invoked before protected behavior
PermissionAllowed proceeds to Policy evaluation
PermissionDenied blocks protected behavior
missing Permission Context fails closed
permission approval does not bypass Policy
```

Permission matrix:

```text
PermissionAllowed + PolicyAllowed = action may proceed
PermissionDenied + PolicyAllowed = blocked
PermissionAllowed + PolicyRestricted = blocked or downgraded
PermissionDenied + PolicyRestricted = blocked
UnknownPermission + AnyPolicy = blocked
```

Test skeleton:

```yaml
permission_tests:
  - test_key: api-permission-denied
    test_title: PermissionDenied Blocks API Operation
    given:
      - valid request
      - PermissionDenied decision
    when:
      - protected API operation is evaluated
    then:
      - PermissionDenied is returned
      - owning service mutation is not performed
      - restricted content is not returned
```

---

# 13. Policy Tests

Policy tests must include:

```text
required policy scope exists for policy-controlled endpoint
Policy Service invoked before restricted output/action
PolicyAllowed returns allowed fields
PolicyRestricted blocks or downgrades safely
redaction sets restricted_fields_omitted = true
NotFound may replace PolicyRestricted where policy requires non-disclosure
policy internals are not exposed
```

Test skeleton:

```yaml
policy_tests:
  - test_key: api-policy-restricted-redaction
    test_title: PolicyRestricted Redacts API Response
    given:
      - valid request
      - PermissionAllowed decision
      - PolicyRestricted redaction decision
    when:
      - API response is generated
    then:
      - restricted fields are omitted
      - restricted_fields_omitted is true
      - policy internals are not exposed
```

---

# 14. Pagination Tests

For search/list endpoints, tests must include:

```text
valid cursor accepted
invalid cursor rejected
limit boundary enforced
sort field controlled
restricted total_count omitted where required
policy redaction applied per item
returned_count counts visible items only
```

Test skeleton:

```yaml
pagination_tests:
  - test_key: api-search-pagination-policy-total-count
    test_title: Search Total Count Omitted by Policy
    given:
      - list endpoint request
      - policy restricts total_count disclosure
    when:
      - response is generated
    then:
      - total_count is null
      - total_count_omitted is true
      - returned_count reflects visible items
```

---

# 15. AI Boundary Tests

For AI-assisted endpoints, tests must include:

```text
AI Context required
agent reference validated
agent capability scope enforced
source scope disclosed
policy omissions disclosed
human_review_required preserved
AI output not treated as professional truth
AI cannot execute protected action
```

Forbidden actions must be tested where relevant:

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

Test skeleton:

```yaml
ai_boundary_tests:
  - test_key: api-ai-cannot-protected-action
    test_title: AI-Assisted API Cannot Execute Protected Action
    given:
      - AI-assisted request
      - protected action requested
    when:
      - API operation is evaluated
    then:
      - action is blocked or requires human review
      - no protected state change occurs
      - AI output remains assistance
```

---

# 16. Human Review Tests

Human Review tests must include:

```text
human_review_required returned where required
missing human_review_reference_id blocks protected action
valid human_review_reference_id accepted only as review trace
review record does not execute downstream action by itself
owning service decides whether review satisfies action requirements
```

Test skeleton:

```yaml
human_review_tests:
  - test_key: api-human-review-required
    test_title: Missing Human Review Blocks Protected API Action
    given:
      - protected API action
      - human review required by contract or policy
      - missing human_review_reference_id
    when:
      - operation is evaluated
    then:
      - HumanReviewRequired is returned
      - no protected downstream action occurs
```

---

# 17. Idempotency Tests

For duplicate-sensitive endpoints, tests must include:

```text
idempotency_key required
same key + same semantic request = safe replay
same key + different semantic request = IdempotencyConflict
duplicate create does not duplicate object
duplicate update does not duplicate side effects
duplicate select does not duplicate selection
duplicate communication creation does not duplicate communication
duplicate event trace not created
```

Test skeleton:

```yaml
idempotency_tests:
  - test_key: api-idempotent-create-replay
    test_title: Duplicate Create Replays Safely
    given:
      - POST create endpoint
      - idempotency_key
      - first successful request
    when:
      - same request is replayed
    then:
      - replayed response is safe
      - object is not duplicated
      - event is not duplicated
```

---

# 18. Event Trace Tests

Event tests must include:

```text
event_reference_ids returned only where policy allows
events emitted only by owning services
API layer does not emit events directly
event reference is audit trace, not command
idempotent replay does not duplicate events
event visibility follows Policy
```

Test skeleton:

```yaml
event_trace_tests:
  - test_key: api-no-direct-event-emission
    test_title: API Layer Does Not Emit Events Directly
    given:
      - API operation that may result in event
    when:
      - operation completes
    then:
      - owning service emits event if required
      - API layer only returns event_reference_ids where allowed
      - no API-layer event emission occurs
```

---

# 19. Error Safety Tests

Error tests must include:

```text
controlled error code
safe error shape
correlation_id preserved
retryable flag present
database IDs not exposed
restricted content not exposed
private notes not exposed
policy internals not exposed
permission internals not exposed
NotFound substitution where required
```

Test skeleton:

```yaml
error_safety_tests:
  - test_key: api-safe-error-no-leakage
    test_title: API Error Does Not Leak Restricted Information
    given:
      - request for restricted object
      - policy forbids disclosure
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - restricted object details are not exposed
      - database IDs are not exposed
```

---

# 20. Versioning Tests

Versioning tests must include:

```text
supported api_version accepted
supported contract_version accepted
schema_version preserved where required
missing version rejected
unsupported version rejected
VersionUnsupported fails closed
breaking change requires version bump
```

Test skeleton:

```yaml
versioning_tests:
  - test_key: api-version-unsupported
    test_title: Unsupported API Contract Version Fails Closed
    given:
      - unsupported api_version or contract_version
    when:
      - API operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 21. API Contract Family Coverage

The following API Contract families must be covered:

```text
Foundation API Contracts:
  identity-api-contract.md
  organization-api-contract.md
  user-api-contract.md
  permission-api-contract.md
  policy-api-contract.md
  knowledge-api-contract.md

Professional API Contracts:
  brand-api-contract.md
  trademark-api-contract.md
  jurisdiction-api-contract.md
  classification-api-contract.md
  document-api-contract.md
  evidence-api-contract.md

Business Execution API Contracts:
  customer-api-contract.md
  matter-api-contract.md
  order-api-contract.md
  opportunity-api-contract.md
  workflow-contract-api-contract.md
  task-api-contract.md
  event-api-contract.md
  notification-api-contract.md
  communication-api-contract.md

Collaboration Network API Contracts:
  agent-api-contract.md
  service-provider-api-contract.md
  routing-api-contract.md
  partner-api-contract.md
  service-network-api-contract.md
```

Coverage rule:

```text
- Each API Contract family must include at least one create/read/search or equivalent endpoint test.
- Each mutation endpoint must include Permission, Policy, Idempotency and Event boundary tests where applicable.
- Each read/search endpoint must include Policy redaction tests.
- Each AI-assisted endpoint must include AI boundary tests.
```

---

# 22. Contract Coverage Matrix

```yaml
coverage_matrix:
  request_schema:
    required: true
    covered_by:
      - api-request-valid-schema
      - api-request-missing-required-field
  response_schema:
    required: true
    covered_by:
      - api-response-valid-schema
      - api-response-no-database-id
  references:
    required: true
    covered_by:
      - api-reference-owning-service-validation
  service_boundary:
    required: true
    covered_by:
      - api-delegates-to-owning-service
      - api-direct-mutation-blocked
  permission:
    required: true
    covered_by:
      - api-permission-denied
  policy:
    required: true
    covered_by:
      - api-policy-restricted-redaction
  pagination:
    required: true
    covered_by:
      - api-search-pagination-policy-total-count
  ai_boundary:
    required: true
    covered_by:
      - api-ai-cannot-protected-action
  human_review:
    required: true
    covered_by:
      - api-human-review-required
  idempotency:
    required: true
    covered_by:
      - api-idempotent-create-replay
  event_trace:
    required: true
    covered_by:
      - api-no-direct-event-emission
  errors:
    required: true
    covered_by:
      - api-safe-error-no-leakage
  versioning:
    required: true
    covered_by:
      - api-version-unsupported
```

---

# 23. Codex Implementation Notes

Codex must:

```text
cite this API Contract Tests file
cite the specific API Contract being tested
cite related Common Contracts
cite related Service Specs
cite related Agent Specs where AI-assisted endpoints are tested
generate tests from contract files, not assumptions
write request schema tests
write response schema tests
write reference validation tests
write owning service boundary tests
write PermissionDenied tests
write PolicyRestricted and redaction tests
write pagination tests for list/search endpoints
write AI forbidden-action tests for AI-assisted endpoints
write HumanReviewRequired tests for gated endpoints
write idempotency replay/conflict tests for duplicate-sensitive endpoints
write event non-duplication and no-direct-emission tests
write safe error tests
write VersionUnsupported tests
use deterministic non-production fixtures
```

Codex must not:

```text
treat happy-path API tests as sufficient
skip negative tests
mock away Permission or Policy without asserting invocation
mutate domain state from API layer
emit events from API layer
allow AI output to execute protected actions
allow valid reference to imply read permission
expose database IDs in expected outputs
ignore restricted_fields_omitted
ignore idempotency conflict behavior
ignore version validation
```

---

# 24. Acceptance Criteria

This API Contract Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related API and Common Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines API Contract coverage scope.
[ ] It defines request schema tests.
[ ] It defines response schema tests.
[ ] It defines reference validation tests.
[ ] It defines owning service boundary tests.
[ ] It defines Permission tests.
[ ] It defines Policy tests.
[ ] It defines Pagination tests.
[ ] It defines AI Boundary tests.
[ ] It defines Human Review tests.
[ ] It defines Idempotency tests.
[ ] It defines Event Trace tests.
[ ] It defines Error Safety tests.
[ ] It defines Versioning tests.
[ ] It defines API Contract family coverage.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 25. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial API Contract Tests. Defines governed API request/response validation, reference validation, service boundary tests, Permission/Policy tests, pagination, AI and human-review boundaries, idempotency, event trace, safe errors, versioning, API family coverage matrix and Codex implementation expectations. |

---

**End of API Contract Tests**
