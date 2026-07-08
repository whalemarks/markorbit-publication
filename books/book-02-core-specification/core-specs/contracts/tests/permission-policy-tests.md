# Permission Policy Tests

**Spec ID:** B02-CONTRACT-TESTS-PERMISSION-POLICY  
**Spec Type:** Test Contract Specification  
**Contract Name:** Permission Policy Tests  
**Contract File:** core-specs/contracts/tests/permission-policy-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Agent Contracts  
**Related Common Contracts:** core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related API Contracts:** core-specs/contracts/api/permission-api-contract.md; core-specs/contracts/api/policy-api-contract.md; core-specs/contracts/api/*.md  
**Related Workflow Contracts:** core-specs/contracts/workflows/*.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/*.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md; core-specs/contracts/tests/workflow-contract-tests.md; core-specs/contracts/tests/agent-boundary-tests.md  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/agent-service.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Permission / Policy Governance Verification  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Permission Policy Tests define acceptance-level testing requirements for MarkOrbit permission and policy governance across API, workflow, service and agent-assisted behavior.

They verify:

```text
Permission Context enforcement
Policy Context enforcement
Permission Service boundary
Policy Service boundary
Permission and Policy combination matrix
fail-closed behavior
policy redaction behavior
restricted-field omission behavior
non-disclosure substitution
cross-organization restrictions
agent-assisted permission/policy enforcement
human review interaction
event trace visibility
safe error behavior
version compatibility
Codex implementation acceptance
```

These tests ensure that Permission and Policy are independent but jointly required governance systems:

```text
Permission decides whether an actor may act.
Policy decides whether context allows or restricts the action or output.
Permission approval does not bypass Policy.
Policy allowance does not bypass Permission.
```

---

# 2. Core Lock

```text
Permission Policy Tests verify governed access and contextual restriction behavior.
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Permission approval is not Policy approval.
Policy allowance is not Permission approval.
Unknown Permission or unknown Policy must fail closed for protected behavior.
Policy may block, redact, downgrade or require human review.
Restricted data must not leak through responses, errors, events or AI output.
Events preserve trace only where visibility is allowed.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing Permission Context shape and behavior
testing Policy Context shape and behavior
testing Permission Service invocation
testing Policy Service invocation
testing Permission/Policy matrix behavior
testing redaction and restricted_fields_omitted
testing NotFound substitution where required
testing cross-organization policy behavior
testing API Permission/Policy enforcement
testing Workflow Permission/Policy enforcement
testing Agent Permission/Policy enforcement
testing Human Review interaction
testing safe errors
testing event visibility
testing versioning behavior
```

This Test Contract is not responsible for:

```text
defining business roles
defining policy rule authoring UI
granting permissions
approving policies
implementing identity provider logic
replacing Permission Service
replacing Policy Service
production access audits by itself
```

---

# 4. Related Contracts

This test contract validates:

```text
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/api/permission-api-contract.md
core-specs/contracts/api/policy-api-contract.md
all API Contracts with protected behavior
all Workflow Contracts with protected steps
all Agent Specs with governed capability use
```

Rules:

```text
- Every protected action must evaluate Permission.
- Every policy-controlled action or output must evaluate Policy.
- Permission and Policy must be tested independently and together.
- If behavior is ambiguous, test must expect fail-closed.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: PermissionPolicyBoundary
  subject_name: Permission and Policy Governance Boundary
  owning_service:
    - Permission Service
    - Policy Service
  contract_file:
    - core-specs/contracts/common/permission-context.md
    - core-specs/contracts/common/policy-context.md
  behavior_scope:
    - permission evaluation
    - policy evaluation
    - access gating
    - contextual restriction
    - redaction
    - non-disclosure
    - cross-organization restriction
    - human review escalation
    - AI output restriction
    - event visibility
    - safe errors
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: permission-allowed-fixture
    fixture_type: Permission Fixture
    purpose: actor has required permission keys
    contains_production_data: false
    required: true

  - fixture_key: permission-denied-fixture
    fixture_type: Permission Fixture
    purpose: actor lacks required permission keys
    contains_production_data: false
    required: true

  - fixture_key: permission-unknown-fixture
    fixture_type: Permission Fixture
    purpose: permission state unknown or service unavailable
    contains_production_data: false
    required: true

  - fixture_key: policy-allowed-fixture
    fixture_type: Policy Fixture
    purpose: context permits action and output
    contains_production_data: false
    required: true

  - fixture_key: policy-restricted-block-fixture
    fixture_type: Policy Fixture
    purpose: policy blocks action
    contains_production_data: false
    required: true

  - fixture_key: policy-restricted-redact-fixture
    fixture_type: Policy Fixture
    purpose: policy redacts fields but allows safe partial output
    contains_production_data: false
    required: true

  - fixture_key: policy-nondisclosure-fixture
    fixture_type: Policy Fixture
    purpose: policy requires NotFound or equivalent non-disclosure
    contains_production_data: false
    required: true

  - fixture_key: cross-organization-fixture
    fixture_type: Policy Fixture
    purpose: same-org, cross-org allowed, cross-org restricted cases
    contains_production_data: false
    required: true

  - fixture_key: ai-policy-fixture
    fixture_type: AI Context Fixture
    purpose: agent-assisted output with policy omissions
    contains_production_data: false
    required: true

  - fixture_key: human-review-policy-fixture
    fixture_type: Human Review Fixture
    purpose: policy requires human review before action
    contains_production_data: false
    required: true

  - fixture_key: event-visibility-fixture
    fixture_type: Event Trace Fixture
    purpose: visible, redacted and hidden event trace cases
    contains_production_data: false
    required: true

  - fixture_key: error-fixture
    fixture_type: Error Fixture
    purpose: safe errors for permission/policy failures
    contains_production_data: false
    required: true

  - fixture_key: version-fixture
    fixture_type: Version Fixture
    purpose: supported and unsupported Permission/Policy context versions
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain production data.
- Fixtures must cover all matrix combinations.
- Fixtures must include redaction and non-disclosure cases.
- Fixtures must include AI output and event visibility cases.
- Fixtures must include human-review-required policy cases.
```

---

# 7. Permission / Policy Matrix Tests

Core matrix:

```text
PermissionAllowed + PolicyAllowed = action may proceed
PermissionDenied + PolicyAllowed = blocked
PermissionAllowed + PolicyRestrictedBlock = blocked
PermissionAllowed + PolicyRestrictedRedact = safe partial output or downgraded action
PermissionAllowed + PolicyRequiresHumanReview = HumanReviewRequired unless valid review exists
PermissionDenied + PolicyRestricted = blocked
UnknownPermission + AnyPolicy = blocked
AnyPermission + UnknownPolicy for policy-controlled action = blocked
```

Positive test:

```yaml
matrix_tests:
  - test_key: permission-policy-allowed
    test_title: PermissionAllowed and PolicyAllowed Permit Action
    given:
      - PermissionAllowed decision
      - PolicyAllowed decision
      - valid protected request
    when:
      - operation is evaluated
    then:
      - operation may proceed
      - output follows contract
      - audit trace may include decisions where policy allows
```

Negative tests:

```yaml
negative_tests:
  - test_key: permission-denied-policy-allowed-blocked
    test_title: PermissionDenied Blocks Even When Policy Allows
    given:
      - PermissionDenied decision
      - PolicyAllowed decision
    when:
      - protected operation is evaluated
    then:
      - PermissionDenied is returned
      - no protected action occurs
    expected_error_code: PermissionDenied

  - test_key: permission-allowed-policy-blocked
    test_title: PolicyRestricted Blocks Even When Permission Allows
    given:
      - PermissionAllowed decision
      - PolicyRestricted block decision
    when:
      - policy-controlled operation is evaluated
    then:
      - PolicyRestricted is returned
      - no restricted action occurs
    expected_error_code: PolicyRestricted
```

---

# 8. Permission Context Tests

Permission tests must verify:

```text
required_permission_keys present
actor_reference_id present where required
organization_reference_id present where required
Permission Service invoked
permission_decision_reference_id recorded where policy allows
PermissionDenied blocks action
PermissionUnknown fails closed
permission result does not expose internal rule details
```

Test skeleton:

```yaml
permission_context_tests:
  - test_key: permission-service-invoked
    test_title: Permission Service Is Invoked for Protected Action
    given:
      - protected action request
      - required_permission_keys
    when:
      - operation is evaluated
    then:
      - Permission Service is invoked
      - decision is applied before protected behavior
```

Negative test:

```yaml
negative_tests:
  - test_key: permission-unknown-fails-closed
    test_title: Unknown Permission Fails Closed
    given:
      - protected action request
      - Permission evaluation unavailable or unknown
    when:
      - operation is evaluated
    then:
      - PermissionDenied or safe failure is returned
      - no protected action occurs
    expected_error_code: PermissionDenied
```

---

# 9. Policy Context Tests

Policy tests must verify:

```text
required_policy_scopes present
context fields present where required
Policy Service invoked
policy_decision_reference_id recorded where allowed
PolicyRestricted blocks or redacts
PolicyUnknown fails closed
policy result does not expose internal rule details
```

Test skeleton:

```yaml
policy_context_tests:
  - test_key: policy-service-invoked
    test_title: Policy Service Is Invoked for Policy-Controlled Action
    given:
      - policy-controlled action request
      - required_policy_scopes
    when:
      - operation is evaluated
    then:
      - Policy Service is invoked
      - decision is applied before restricted output/action
```

Negative test:

```yaml
negative_tests:
  - test_key: policy-unknown-fails-closed
    test_title: Unknown Policy Fails Closed
    given:
      - policy-controlled request
      - Policy evaluation unavailable or unknown
    when:
      - operation is evaluated
    then:
      - PolicyRestricted or safe failure is returned
      - no restricted output/action occurs
    expected_error_code: PolicyRestricted
```

---

# 10. Redaction Tests

Redaction tests must verify:

```text
restricted fields omitted
restricted_fields_omitted is true
policy_omissions_disclosed is true for AI-assisted output
total_count_omitted is true where list total is restricted
redacted fields do not appear in nested objects
redacted fields do not appear in errors
redacted fields do not appear in event trace
```

Test skeleton:

```yaml
redaction_tests:
  - test_key: policy-redaction-restricted-fields-omitted
    test_title: Policy Redaction Omits Restricted Fields
    given:
      - PermissionAllowed
      - PolicyRestricted redaction decision
      - response contains restricted candidate fields
    when:
      - response is generated
    then:
      - restricted fields are omitted
      - restricted_fields_omitted is true
      - no restricted nested fields appear
```

---

# 11. Non-Disclosure Tests

Non-disclosure tests must verify:

```text
NotFound may replace PolicyRestricted where policy requires non-disclosure
existence not disclosed
error safe_detail does not reveal hidden object
event trace does not reveal hidden object
pagination counts do not reveal hidden object where restricted
```

Test skeleton:

```yaml
nondisclosure_tests:
  - test_key: policy-nondisclosure-notfound
    test_title: Policy Non-disclosure May Return NotFound
    given:
      - object exists
      - actor has no policy visibility
      - policy requires non-disclosure
    when:
      - read request is evaluated
    then:
      - NotFound is returned
      - object existence is not revealed
      - restricted data is not exposed
```

---

# 12. Cross-Organization Policy Tests

Cross-organization tests must verify:

```text
same-organization access follows permission/policy
cross-organization access requires explicit policy allowance
partner/service-provider access uses relationship policy
customer data visibility restricted by policy
provider commercial terms restricted by policy
agent output respects cross-organization restrictions
```

Test skeleton:

```yaml
cross_org_tests:
  - test_key: cross-organization-requires-policy
    test_title: Cross-Organization Access Requires Explicit Policy
    given:
      - actor from organization A
      - target belongs to organization B
      - PermissionAllowed
      - no cross-organization policy allowance
    when:
      - operation is evaluated
    then:
      - PolicyRestricted is returned
      - target data is not exposed
```

---

# 13. API Permission / Policy Tests

Every protected API operation must verify:

```text
Permission Service invoked
Policy Service invoked where policy-controlled
PermissionDenied blocks before mutation
PolicyRestricted blocks or redacts before output
API layer does not bypass services
safe errors are returned
```

Test skeleton:

```yaml
api_permission_policy_tests:
  - test_key: api-permission-policy-enforced
    test_title: API Enforces Permission and Policy
    given:
      - protected API request
      - PermissionAllowed
      - PolicyRestricted
    when:
      - API operation is evaluated
    then:
      - Permission Service is invoked
      - Policy Service is invoked
      - restricted action/output is blocked or redacted
```

---

# 14. Workflow Permission / Policy Tests

Every protected workflow step must verify:

```text
workflow-contract:preview permission/policy for preview
workflow-contract:apply permission/policy for apply
step-specific permission keys
step-specific policy scopes
PermissionDenied blocks or skips protected step safely
PolicyRestricted blocks, redacts or downgrades safely
restricted_fields_omitted set where output is redacted
```

Test skeleton:

```yaml
workflow_permission_policy_tests:
  - test_key: workflow-step-permission-policy-enforced
    test_title: Workflow Step Enforces Permission and Policy
    given:
      - workflow apply request
      - protected step
      - PermissionAllowed
      - PolicyRestricted
    when:
      - workflow apply is evaluated
    then:
      - step is blocked, skipped or downgraded according to contract
      - no restricted domain mutation occurs
```

---

# 15. Agent Permission / Policy Tests

Every agent-assisted operation must verify:

```text
agent identity does not imply permission
agent capability does not imply permission
Permission Service invoked for agent-assisted protected behavior
Policy Service invoked for agent-visible context
PolicyRestricted redacts agent input/output
policy_omissions_disclosed is true for AI output with omissions
agent cannot infer or expose restricted facts
```

Test skeleton:

```yaml
agent_permission_policy_tests:
  - test_key: agent-policy-redacts-output
    test_title: Agent Output Respects Policy Redaction
    given:
      - valid agent
      - PermissionAllowed
      - PolicyRestricted redaction decision
    when:
      - agent-assisted output is generated
    then:
      - restricted facts are omitted
      - policy_omissions_disclosed is true
      - agent does not infer hidden data as fact
```

---

# 16. Human Review Interaction Tests

Human Review interaction tests must verify:

```text
Policy may require human review
HumanReviewRequired blocks protected action until review exists
valid review does not bypass Permission
valid review does not bypass Policy
review visibility follows Policy
review record does not execute downstream action by itself
```

Test skeleton:

```yaml
human_review_policy_tests:
  - test_key: policy-requires-human-review
    test_title: Policy Can Require Human Review
    given:
      - PermissionAllowed
      - PolicyRequiresHumanReview
      - missing human_review_reference_id
    when:
      - protected action is evaluated
    then:
      - HumanReviewRequired is returned
      - no protected action occurs
```

---

# 17. Event Visibility Tests

Event visibility tests must verify:

```text
event_reference_ids returned only where policy allows
event payload visibility follows Policy
restricted event details omitted
restricted_fields_omitted set where event data is redacted
NotFound/non-disclosure may apply to hidden events
event reference is audit trace, not command
```

Test skeleton:

```yaml
event_visibility_tests:
  - test_key: event-visibility-policy-restricted
    test_title: Policy Restricts Event Visibility
    given:
      - event exists
      - PermissionAllowed
      - PolicyRestricted for event visibility
    when:
      - event trace is requested
    then:
      - event details are redacted or hidden
      - restricted_fields_omitted is true where redacted
      - event is not treated as command
```

---

# 18. Error Safety Tests

Permission/Policy error tests must verify:

```text
PermissionDenied uses safe error shape
PolicyRestricted uses safe error shape
NotFound substitution does not reveal existence
permission internals not exposed
policy internals not exposed
restricted object data not exposed
database IDs not exposed
correlation_id preserved
retryable flag present
```

Test skeleton:

```yaml
error_safety_tests:
  - test_key: permission-policy-safe-error
    test_title: Permission and Policy Errors Are Safe
    given:
      - restricted request
      - PermissionDenied or PolicyRestricted
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - internals are not exposed
      - restricted object data is not exposed
```

---

# 19. Versioning Tests

Versioning tests must verify:

```text
supported Permission Context version accepted
supported Policy Context version accepted
missing required version rejected
unsupported permission context version rejected
unsupported policy context version rejected
version mismatch fails closed
historical decision references remain traceable where allowed
```

Test skeleton:

```yaml
versioning_tests:
  - test_key: permission-policy-version-unsupported
    test_title: Unsupported Permission or Policy Version Fails Closed
    given:
      - unsupported permission_context_version or policy_context_version
    when:
      - protected operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 20. Contract Coverage Matrix

```yaml
coverage_matrix:
  permission_policy_matrix:
    required: true
    covered_by:
      - permission-policy-allowed
      - permission-denied-policy-allowed-blocked
      - permission-allowed-policy-blocked
  permission_context:
    required: true
    covered_by:
      - permission-service-invoked
      - permission-unknown-fails-closed
  policy_context:
    required: true
    covered_by:
      - policy-service-invoked
      - policy-unknown-fails-closed
  redaction:
    required: true
    covered_by:
      - policy-redaction-restricted-fields-omitted
  nondisclosure:
    required: true
    covered_by:
      - policy-nondisclosure-notfound
  cross_organization:
    required: true
    covered_by:
      - cross-organization-requires-policy
  api:
    required: true
    covered_by:
      - api-permission-policy-enforced
  workflow:
    required: true
    covered_by:
      - workflow-step-permission-policy-enforced
  agent:
    required: true
    covered_by:
      - agent-policy-redacts-output
  human_review:
    required: true
    covered_by:
      - policy-requires-human-review
  event_visibility:
    required: true
    covered_by:
      - event-visibility-policy-restricted
  errors:
    required: true
    covered_by:
      - permission-policy-safe-error
  versioning:
    required: true
    covered_by:
      - permission-policy-version-unsupported
```

---

# 21. Codex Implementation Notes

Codex must:

```text
cite this Permission Policy Tests file
cite Permission Context Contract
cite Policy Context Contract
cite Permission API Contract
cite Policy API Contract
cite Permission Service Spec
cite Policy Service Spec
cite relevant API/Workflow/Agent specs being tested
generate deterministic non-production fixtures
write full Permission/Policy matrix tests
write Permission Service invocation tests
write Policy Service invocation tests
write fail-closed tests for unknown Permission/Policy
write redaction tests
write non-disclosure tests
write cross-organization tests
write API Permission/Policy tests
write Workflow Permission/Policy tests
write Agent Permission/Policy tests
write HumanReviewRequired policy tests
write event visibility tests
write safe error tests
write VersionUnsupported tests
assert restricted_fields_omitted where redaction occurs
assert policy_omissions_disclosed for AI output omissions
```

Codex must not:

```text
treat PermissionAllowed as PolicyAllowed
treat PolicyAllowed as PermissionAllowed
skip fail-closed tests
mock away Permission/Policy without asserting invocation
expose permission or policy internals
expose restricted data through errors, events, AI output or pagination
allow agent identity to imply permission
allow human review to bypass Permission or Policy
ignore cross-organization restrictions
ignore version validation
```

---

# 22. Acceptance Criteria

This Permission Policy Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Common, API, Workflow and Agent Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines Permission / Policy matrix tests.
[ ] It defines Permission Context tests.
[ ] It defines Policy Context tests.
[ ] It defines Redaction tests.
[ ] It defines Non-Disclosure tests.
[ ] It defines Cross-Organization Policy tests.
[ ] It defines API Permission / Policy tests.
[ ] It defines Workflow Permission / Policy tests.
[ ] It defines Agent Permission / Policy tests.
[ ] It defines Human Review interaction tests.
[ ] It defines Event visibility tests.
[ ] It defines Error Safety tests.
[ ] It defines Versioning tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Permission Policy Tests. Defines Permission/Policy matrix, context tests, fail-closed behavior, redaction, non-disclosure, cross-organization restrictions, API/workflow/agent enforcement, human review interaction, event visibility, safe errors, versioning and Codex implementation expectations. |

---

**End of Permission Policy Tests**
