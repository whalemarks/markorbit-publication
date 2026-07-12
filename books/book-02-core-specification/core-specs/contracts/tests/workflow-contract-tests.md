# Workflow Contract Tests

**Spec ID:** B02-CONTRACT-TESTS-WORKFLOW  
**Spec Type:** Test Contract Specification  
**Contract Name:** Workflow Contract Tests  
**Contract File:** core-specs/contracts/tests/workflow-contract-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Workflow Contracts; API Contracts; Common Contracts; Agent Contracts  
**Related Workflow Contracts:** core-specs/contracts/workflows/*.md  
**Related API Contracts:** core-specs/contracts/api/workflow-contract-api-contract.md; core-specs/contracts/api/task-api-contract.md; core-specs/contracts/api/event-api-contract.md; core-specs/contracts/api/communication-api-contract.md; core-specs/contracts/api/routing-api-contract.md; core-specs/contracts/api/matter-api-contract.md; core-specs/contracts/api/order-api-contract.md; core-specs/contracts/api/document-api-contract.md; core-specs/contracts/api/evidence-api-contract.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md  
**Related Service Specs:** core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/agent-service.md  
**Related Agent Specs:** core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/knowledge-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 3–5 — Workflow Boundary Verification  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Workflow Contract Tests define acceptance-level testing requirements for all MarkOrbit Workflow Contracts.

They verify:

```text
workflow preview behavior
workflow apply behavior
workflow applicability behavior
trigger context validation
target object validation
workflow step contract validation
task plan generation
active task creation boundary
domain service ownership boundary
permission enforcement
policy enforcement
AI boundary enforcement
human review gating
idempotency behavior
event trace behavior
safe error behavior
version compatibility
restricted-field omission
Codex implementation acceptance
```

Workflow Contract Tests ensure that Workflow Contracts coordinate governed execution without owning domain state, creating active Tasks directly, emitting Events directly, bypassing Permission/Policy, or letting AI execute protected actions.

---

# 2. Core Lock

```text
Workflow Contract Tests verify governed execution coordination.
Workflow Contract Service owns preview and apply behavior.
Task Service owns active Task creation.
Owning domain services own domain state.
Permission and Policy must fail closed.
AI may prepare, summarize and suggest, but must not execute protected actions.
Human review gates protected workflow actions where required.
Idempotency prevents duplicate workflow effects.
Workflow layer must not emit Events directly.
Errors must remain safe.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing workflow preview contract
testing workflow apply contract
testing workflow applicability contract
testing trigger context validation
testing target context validation
testing workflow step contract validation
testing task plan behavior
testing active task creation boundary
testing owning service delegation
testing Permission Context behavior
testing Policy Context behavior
testing AI Context behavior
testing Human Review behavior
testing Idempotency behavior
testing Event Trace behavior
testing Error Contract behavior
testing Versioning behavior
testing restricted-field omission behavior
```

This Test Contract is not responsible for:

```text
domain service business logic by itself
API endpoint tests outside workflow APIs
UI behavior
production data validation
load/performance testing unless separately specified
agent behavior outside workflow-assisted operations
```

---

# 4. Related Contracts

This test contract validates Workflow Contract files under:

```text
core-specs/contracts/workflows/
```

It depends on:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
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
- Every Workflow Contract must have tests traceable to its contract file.
- Every protected workflow step must test Permission and Policy behavior.
- Every workflow apply operation must test idempotency.
- Every workflow preview must test no active side effects.
- Every AI-assisted step must test AI boundary.
- Every human-review checkpoint must test gating behavior.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: WorkflowContract
  subject_name: Workflow Contract Layer
  owning_service: Workflow Contract Service
  contract_file: core-specs/contracts/workflows/*.md
  behavior_scope:
    - preview behavior
    - apply behavior
    - applicability
    - trigger context
    - target context
    - workflow steps
    - task plan
    - task creation boundary
    - domain service delegation
    - permission enforcement
    - policy enforcement
    - AI boundary
    - human review
    - idempotency
    - event trace
    - errors
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: workflow-contract-fixture
    fixture_type: Workflow Fixture
    purpose: workflow contract reference, supported/unsupported workflow version, valid/invalid workflow definition
    contains_production_data: false
    required: true

  - fixture_key: workflow-preview-fixture
    fixture_type: Workflow Fixture
    purpose: valid and invalid preview request/response
    contains_production_data: false
    required: true

  - fixture_key: workflow-apply-fixture
    fixture_type: Workflow Fixture
    purpose: valid and invalid apply request/response
    contains_production_data: false
    required: true

  - fixture_key: target-context-fixture
    fixture_type: Reference Fixture
    purpose: valid, invalid, missing and wrong-type target object references
    contains_production_data: false
    required: true

  - fixture_key: trigger-context-fixture
    fixture_type: Domain Object Fixture
    purpose: manual, event-driven, scheduled, imported and agent-prepared trigger testing
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
    purpose: AI-assisted step testing and forbidden-action testing
    contains_production_data: false
    required: true

  - fixture_key: human-review-fixture
    fixture_type: Human Review Fixture
    purpose: review-required checkpoint testing
    contains_production_data: false
    required: true

  - fixture_key: idempotency-fixture
    fixture_type: Idempotency Fixture
    purpose: workflow apply replay and conflict testing
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
    purpose: supported, missing and unsupported workflow contract version testing
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain real customer data.
- Fixtures must include preview and apply cases.
- Fixtures must include active side-effect detection cases.
- Fixtures must include Permission and Policy combinations.
- Fixtures must include AI-assisted and non-AI-assisted cases.
- Fixtures must include human-review-present and human-review-missing cases.
- Fixtures must include idempotent replay and conflict cases.
```

---

# 7. Workflow Contract Coverage Scope

Every Workflow Contract must test:

```text
metadata validation
core lock preservation
trigger context validation
target object validation
workflow applicability
workflow step list shape
preview request and response
apply request and response
task plan generation
active task creation via Task Service only
domain service delegation
permission checks per protected step
policy checks per policy-controlled step
AI-assisted step boundaries
human review checkpoints
idempotent apply behavior
event trace behavior
safe errors
version validation
```

Workflow files covered:

```text
customer-intake-workflow-contract.md
trademark-application-workflow-contract.md
office-action-response-workflow-contract.md
provider-routing-workflow-contract.md
communication-review-workflow-contract.md
renewal-workflow-contract.md
assignment-workflow-contract.md
evidence-review-workflow-contract.md
```

---

# 8. Metadata and Core Lock Tests

## 8.1 Positive Tests

```yaml
positive_tests:
  - test_key: workflow-metadata-valid
    test_title: Workflow Contract Metadata Is Valid
    given:
      - workflow contract file
    when:
      - metadata is parsed
    then:
      - spec_id exists
      - contract_file matches file path
      - workflow_contract_version exists
      - status exists
      - mvp_depth exists
    required_contract_refs:
      - core-specs/contracts/workflows/template.md

  - test_key: workflow-core-lock-present
    test_title: Workflow Core Lock Is Present
    given:
      - workflow contract file
    when:
      - core lock section is parsed
    then:
      - Workflow Contract Service ownership is preserved
      - Task Service ownership is preserved
      - Permission and Policy governance is preserved
      - AI forbidden execution boundary is preserved
      - Event trace boundary is preserved
```

## 8.2 Negative Tests

```yaml
negative_tests:
  - test_key: workflow-metadata-missing-version
    test_title: Missing Workflow Contract Version Is Rejected
    given:
      - workflow contract missing workflow_contract_version
    when:
      - contract validation is performed
    then:
      - VersionUnsupported or ValidationFailed is returned
    expected_error_code: VersionUnsupported
```

---

# 9. Trigger Context Tests

Trigger tests must include:

```text
valid manual trigger accepted
valid APIRequest trigger accepted
valid EventDriven trigger validates source event
valid AgentPrepared trigger requires AI Context
invalid trigger_type rejected
missing trigger_source rejected or downgraded according to contract
scheduled trigger still evaluates current Policy
```

Test skeleton:

```yaml
trigger_tests:
  - test_key: workflow-event-driven-trigger-validates-event
    test_title: Event-driven Trigger Validates Source Event
    given:
      - EventDriven trigger
      - triggered_by_event_reference_id
    when:
      - workflow applicability is evaluated
    then:
      - source event reference is validated
      - source event visibility follows Policy
      - workflow is not applied by event reference alone
```

---

# 10. Target Context Tests

Target tests must include:

```text
valid target reference accepted
invalid target reference rejected
wrong target object type rejected
target owning service validation required
target status checked before apply
target status revalidated before protected transition
valid target reference does not imply read permission
```

Test skeleton:

```yaml
target_tests:
  - test_key: workflow-target-owning-service-validation
    test_title: Target Object Is Validated by Owning Service
    given:
      - workflow target_context
      - target_object_reference_id
    when:
      - workflow applicability is evaluated
    then:
      - owning service validation is invoked
      - workflow proceeds only if target is valid
      - no direct database validation occurs in workflow layer
```

---

# 11. Applicability Tests

Applicability tests must include:

```text
applicable workflow returns applicable true
insufficient context returns InsufficientContext
PermissionDenied returns not applicable or blocked
PolicyRestricted returns safe partial or blocked
StateInvalid blocks apply
VersionUnsupported blocks apply
human_review_required surfaced where required
```

Test skeleton:

```yaml
applicability_tests:
  - test_key: workflow-applicability-insufficient-context
    test_title: Insufficient Context Blocks Workflow Apply
    given:
      - valid target
      - missing required workflow context
    when:
      - applicability is evaluated
    then:
      - applicable is false
      - applicability_status is InsufficientContext
      - missing_context_safe is returned
      - no active side effect occurs
```

---

# 12. Preview Tests

Preview tests must prove:

```text
preview accepts valid request
preview returns safe proposed steps
preview returns safe proposed task plan where requested
preview may return AI summary only with AI Context
preview applies Policy redaction
preview does not create active Tasks
preview does not create Communications
preview does not create Documents
preview does not mutate target object
preview does not emit domain Events directly
preview does not submit filings, send communications, select providers or approve actions
```

Positive test:

```yaml
preview_tests:
  - test_key: workflow-preview-valid
    test_title: Valid Workflow Preview Returns Safe Preview
    given:
      - valid preview request
      - PermissionAllowed
      - PolicyAllowed
    when:
      - preview is executed
    then:
      - preview_status is Completed or Partial
      - proposed_steps_visible is returned
      - no active Task is created
      - no domain mutation occurs
```

Negative test:

```yaml
negative_tests:
  - test_key: workflow-preview-no-active-side-effects
    test_title: Preview Must Not Create Active Side Effects
    given:
      - preview request with include_task_plan true
    when:
      - preview is executed
    then:
      - no active Task is created
      - no Communication is created
      - no Event is emitted directly by workflow layer
      - no target object state changes
```

---

# 13. Apply Tests

Apply tests must prove:

```text
apply requires idempotency_key
apply validates applicability before execution
apply routes through Workflow Contract Service
apply routes active Task creation through Task Service
apply routes domain mutation through owning services
apply returns workflow_application_reference_id
apply preserves event trace references where allowed
apply surfaces skipped steps safely
apply applies Policy redaction
```

Positive test:

```yaml
apply_tests:
  - test_key: workflow-apply-valid
    test_title: Valid Workflow Apply Executes Through Owning Services
    given:
      - valid apply request
      - idempotency_key
      - PermissionAllowed
      - PolicyAllowed
    when:
      - apply is executed
    then:
      - Workflow Contract Service is invoked
      - required owning services are invoked
      - active Tasks are created only by Task Service
      - response returns workflow_application_reference_id
```

Negative test:

```yaml
negative_tests:
  - test_key: workflow-apply-missing-idempotency
    test_title: Apply Without Idempotency Key Is Rejected
    given:
      - valid apply request
      - missing idempotency_key
    when:
      - apply is evaluated
    then:
      - IdempotencyKeyRequired is returned
      - no active side effect occurs
    expected_error_code: IdempotencyKeyRequired
```

---

# 14. Workflow Step Contract Tests

Step tests must include:

```text
step_key is stable and unique
step_title_safe exists
step_type is controlled
owning_service is explicit
permission_keys exist for protected step
policy_scopes exist for policy-controlled step
human_review_required is explicit
ai_assistance_allowed is explicit
events_expected contains event names only, not commands
failure_behavior is explicit
```

Test skeleton:

```yaml
step_tests:
  - test_key: workflow-step-owning-service-explicit
    test_title: Every Workflow Step Declares Owning Service
    given:
      - workflow step list
    when:
      - step contract validation is performed
    then:
      - each step has owning_service
      - no step mutates object outside owning service
```

Negative test:

```yaml
negative_tests:
  - test_key: workflow-step-direct-domain-mutation-blocked
    test_title: Workflow Step Cannot Mutate Domain Outside Owning Service
    given:
      - workflow step attempts direct domain mutation
    when:
      - boundary validation is performed
    then:
      - test fails
      - step must call owning service
```

---

# 15. Task Creation Tests

Task tests must include:

```text
preview task plan is proposal only
preview creates no active Tasks
apply creates active Tasks only through Task Service
duplicate apply does not duplicate Tasks
TaskCreated event emitted only by Task Service
task references are returned safely
```

Test skeleton:

```yaml
task_tests:
  - test_key: workflow-task-service-only
    test_title: Active Tasks Are Created Only by Task Service
    given:
      - workflow apply with create_tasks true
    when:
      - apply is executed
    then:
      - Task Service is invoked
      - workflow layer does not create Task directly
      - TaskCreated is emitted only by Task Service where applicable
```

---

# 16. Domain Service Boundary Tests

Domain service boundary tests must verify:

```text
Customer mutations route through Customer Service.
Trademark mutations route through Trademark Service.
Document mutations route through Document Service.
Evidence mutations route through Evidence Service.
Communication mutations route through Communication Service.
Routing evaluation/selection routes through Routing Service.
Matter/Order mutations route through Matter/Order Service.
Notification creation routes through Notification Service.
```

Test skeleton:

```yaml
service_boundary_tests:
  - test_key: workflow-domain-service-delegation
    test_title: Workflow Delegates Domain Behavior to Owning Service
    given:
      - workflow apply with domain mutation enabled
    when:
      - apply is executed
    then:
      - owning domain service is invoked
      - workflow layer does not mutate domain state directly
```

---

# 17. Permission Tests

Permission tests must include:

```text
workflow-contract:preview required for preview
workflow-contract:apply required for apply
step-specific permission keys required
Permission Service invoked before protected step
PermissionDenied blocks protected behavior
PermissionAllowed does not bypass Policy
missing Permission Context fails closed
```

Test skeleton:

```yaml
permission_tests:
  - test_key: workflow-permission-denied
    test_title: PermissionDenied Blocks Workflow Step
    given:
      - workflow apply request
      - PermissionDenied for protected step
    when:
      - apply is evaluated
    then:
      - PermissionDenied is returned or step is safely skipped according to contract
      - no protected action occurs
```

---

# 18. Policy Tests

Policy tests must include:

```text
workflow-contract:preview:policy required for preview
workflow-contract:apply:policy required for apply
step-specific policy scopes required
Policy Service invoked before policy-controlled step
PolicyRestricted blocks, redacts or downgrades safely
restricted_fields_omitted is true where redaction occurs
policy omissions disclosed where required
NotFound may replace PolicyRestricted where non-disclosure is required
```

Test skeleton:

```yaml
policy_tests:
  - test_key: workflow-policy-restricted-safe-partial
    test_title: PolicyRestricted Produces Safe Partial Workflow Output
    given:
      - workflow preview or apply request
      - PermissionAllowed
      - PolicyRestricted
    when:
      - workflow operation is evaluated
    then:
      - restricted fields are omitted
      - restricted_fields_omitted is true
      - protected action is blocked or downgraded safely
```

---

# 19. AI Boundary Tests

AI tests must include:

```text
AI Context required for AI-assisted step
agent reference validated
agent capability scope enforced
source_scope_disclosed is true where required
policy_omissions_disclosed is preserved
human_review_required is preserved
AI cannot apply workflow
AI cannot create active Tasks
AI cannot complete Tasks
AI cannot approve communication
AI cannot send communication
AI cannot select provider
AI cannot submit filing or response
AI cannot certify deadline
AI cannot certify authority
AI cannot decide registrability
AI cannot decide evidence sufficiency
```

Test skeleton:

```yaml
ai_boundary_tests:
  - test_key: workflow-ai-cannot-apply
    test_title: AI Cannot Apply Workflow by Itself
    given:
      - AgentPrepared trigger
      - AI-assisted context
      - apply request without governed actor or review where required
    when:
      - workflow apply is evaluated
    then:
      - action is blocked or human_review_required is returned
      - no active side effect occurs
```

---

# 20. Human Review Tests

Human Review tests must include:

```text
review checkpoint exists for protected professional/external action
missing human_review_reference_id blocks gated action
valid review reference accepted as trace
review record does not execute downstream action by itself
owning service decides whether review satisfies requirements
review trace preserved where policy allows
```

Test skeleton:

```yaml
human_review_tests:
  - test_key: workflow-human-review-gates-protected-action
    test_title: Human Review Gates Protected Workflow Action
    given:
      - workflow apply request
      - protected step requires review
      - missing human_review_reference_id
    when:
      - apply is evaluated
    then:
      - HumanReviewRequired is returned
      - protected action does not occur
```

---

# 21. Idempotency Tests

Idempotency tests must include:

```text
apply requires idempotency_key
same key + same semantic apply = safe replay
same key + different semantic apply = IdempotencyConflict
duplicate apply does not duplicate Tasks
duplicate apply does not duplicate Communications
duplicate apply does not duplicate Documents
duplicate apply does not duplicate Matter/Order records
duplicate apply does not duplicate RoutingSelected event
duplicate apply does not duplicate Events
```

Test skeleton:

```yaml
idempotency_tests:
  - test_key: workflow-apply-idempotent-replay
    test_title: Duplicate Workflow Apply Replays Safely
    given:
      - idempotency_key
      - first successful workflow apply
    when:
      - same apply request is replayed
    then:
      - replay response is safe
      - no duplicate Task is created
      - no duplicate Communication is created
      - no duplicate Event is emitted
```

---

# 22. Event Trace Tests

Event tests must include:

```text
WorkflowContractApplied emitted only by Workflow Contract Service
TaskCreated emitted only by Task Service
CommunicationCreated emitted only by Communication Service
RoutingEvaluated/RoutingSelected emitted only by Routing Service
workflow layer does not emit Events directly
event references returned only where policy allows
event reference is audit trace, not command
idempotent replay does not duplicate Events
```

Test skeleton:

```yaml
event_trace_tests:
  - test_key: workflow-no-direct-event-emission
    test_title: Workflow Layer Does Not Emit Events Directly
    given:
      - workflow apply request
    when:
      - apply completes
    then:
      - owning services emit events where required
      - workflow layer does not emit domain events directly
      - event_reference_ids are trace only
```

---

# 23. Error Safety Tests

Error tests must include:

```text
controlled workflow error code
safe error shape
correlation_id preserved
retryable flag present
database IDs not exposed
restricted target data not exposed
private notes not exposed
policy internals not exposed
permission internals not exposed
NotFound substitution where required
```

Test skeleton:

```yaml
error_safety_tests:
  - test_key: workflow-safe-error-no-leakage
    test_title: Workflow Error Does Not Leak Restricted Information
    given:
      - restricted workflow target
      - policy forbids disclosure
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - restricted target details are not exposed
      - database IDs are not exposed
```

---

# 24. Versioning Tests

Versioning tests must include:

```text
supported workflow_contract_version accepted
supported contract_version accepted
schema_version preserved where required
missing workflow_contract_version rejected
unsupported workflow_contract_version rejected
historical workflow application records version used
deprecated version not silently rewritten
VersionUnsupported fails closed
```

Test skeleton:

```yaml
versioning_tests:
  - test_key: workflow-version-unsupported
    test_title: Unsupported Workflow Contract Version Fails Closed
    given:
      - unsupported workflow_contract_version
    when:
      - workflow apply is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 25. Workflow-Specific Boundary Tests

## 25.1 Customer Intake

Must verify:

```text
AI cannot approve engagement.
Preview creates no Customer, Opportunity, Communication or Tasks.
Apply does not duplicate Customer/Opportunity/Tasks/Communication.
Matter/Order are not created unless explicitly routed through owning services.
```

## 25.2 Trademark Application

Must verify:

```text
AI cannot decide registrability or filing strategy.
Official filing is not submitted by workflow.
Human review gates classification, documents, communication and filing readiness.
```

## 25.3 Office Action Response

Must verify:

```text
AI cannot decide legal strategy or certify deadline accuracy.
Official response is not submitted by workflow.
Human review gates deadline, strategy, response documents and response readiness.
```

## 25.4 Provider Routing

Must verify:

```text
Routing Agent cannot select provider.
Recommendation preparation does not select provider.
Provider selection requires explicit select_provider and human/service review.
Duplicate selection does not duplicate RoutingSelected event.
```

## 25.5 Communication Review

Must verify:

```text
AI draft does not approve or send.
Approval requires governed human/service review.
Send-preparation does not silently deliver externally.
Sent communication is immutable or revision-controlled.
```

## 25.6 Renewal

Must verify:

```text
AI cannot certify deadlines or submit renewal.
Official renewal filing/payment is not performed by workflow.
Human review gates deadline, customer instruction, documents, communication and renewal readiness.
```

## 25.7 Assignment

Must verify:

```text
AI cannot certify authority or approve assignment.
Official assignment recordal is not performed by workflow.
Human review gates ownership context, party authority, documents, communication and assignment readiness.
```

## 25.8 Evidence Review

Must verify:

```text
AI cannot decide evidence sufficiency or authenticate documents.
Official evidence submission is not performed by workflow.
Human review gates source documents, evidence classification, gap analysis, communication and evidence readiness.
```

---

# 26. Contract Coverage Matrix

```yaml
coverage_matrix:
  metadata_core_lock:
    required: true
    covered_by:
      - workflow-metadata-valid
      - workflow-core-lock-present
  trigger_context:
    required: true
    covered_by:
      - workflow-event-driven-trigger-validates-event
  target_context:
    required: true
    covered_by:
      - workflow-target-owning-service-validation
  applicability:
    required: true
    covered_by:
      - workflow-applicability-insufficient-context
  preview:
    required: true
    covered_by:
      - workflow-preview-valid
      - workflow-preview-no-active-side-effects
  apply:
    required: true
    covered_by:
      - workflow-apply-valid
      - workflow-apply-missing-idempotency
  workflow_steps:
    required: true
    covered_by:
      - workflow-step-owning-service-explicit
      - workflow-step-direct-domain-mutation-blocked
  task_creation:
    required: true
    covered_by:
      - workflow-task-service-only
  service_boundary:
    required: true
    covered_by:
      - workflow-domain-service-delegation
  permission:
    required: true
    covered_by:
      - workflow-permission-denied
  policy:
    required: true
    covered_by:
      - workflow-policy-restricted-safe-partial
  ai_boundary:
    required: true
    covered_by:
      - workflow-ai-cannot-apply
  human_review:
    required: true
    covered_by:
      - workflow-human-review-gates-protected-action
  idempotency:
    required: true
    covered_by:
      - workflow-apply-idempotent-replay
  event_trace:
    required: true
    covered_by:
      - workflow-no-direct-event-emission
  errors:
    required: true
    covered_by:
      - workflow-safe-error-no-leakage
  versioning:
    required: true
    covered_by:
      - workflow-version-unsupported
```

---

# 27. Codex Implementation Notes

Codex must:

```text
cite this Workflow Contract Tests file
cite the specific Workflow Contract being tested
cite Workflow Contracts README and Template
cite related API Contracts
cite related Common Contracts
cite related Service Specs
cite related Agent Specs where AI-assisted steps are tested
generate tests from contract files, not assumptions
write metadata and Core Lock tests
write trigger and target context tests
write applicability tests
write preview tests
write apply tests
write workflow step contract tests
write task creation boundary tests
write service boundary tests
write PermissionDenied tests
write PolicyRestricted and redaction tests
write AI forbidden-action tests
write HumanReviewRequired tests
write idempotency replay/conflict tests
write event non-duplication and no-direct-emission tests
write safe error tests
write VersionUnsupported tests
use deterministic non-production fixtures
```

Codex must not:

```text
treat happy-path workflow tests as sufficient
skip preview no-side-effect tests
skip apply idempotency tests
mock away Permission or Policy without asserting invocation
mutate domain state from workflow layer
create active Tasks outside Task Service
emit Events from workflow layer
allow AI output to execute protected actions
allow human review record to execute downstream action by itself
ignore restricted_fields_omitted
ignore workflow_contract_version trace
```

---

# 28. Acceptance Criteria

This Workflow Contract Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Workflow, API and Common Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines workflow coverage scope.
[ ] It defines metadata and Core Lock tests.
[ ] It defines trigger context tests.
[ ] It defines target context tests.
[ ] It defines applicability tests.
[ ] It defines preview tests.
[ ] It defines apply tests.
[ ] It defines workflow step contract tests.
[ ] It defines task creation tests.
[ ] It defines domain service boundary tests.
[ ] It defines Permission tests.
[ ] It defines Policy tests.
[ ] It defines AI Boundary tests.
[ ] It defines Human Review tests.
[ ] It defines Idempotency tests.
[ ] It defines Event Trace tests.
[ ] It defines Error Safety tests.
[ ] It defines Versioning tests.
[ ] It defines workflow-specific boundary tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contract Tests. Defines governed workflow metadata, trigger, target, applicability, preview/apply, step, task, service boundary, Permission/Policy, AI, human-review, idempotency, event, error, versioning and workflow-specific boundary test requirements with coverage matrix and Codex expectations. |

---

**End of Workflow Contract Tests**


# PUB-TASK-B02-003 Canonical Fixture Pack

Use `../fixtures/status-workflow/` as the canonical publication fixture pack. Status tests use matrix fixtures; API tests distinguish transition decision from performed owner-Service result; Workflow tests assert `mutation_performed=false`; unsupported versions, invalid transitions, missing permission/policy/review, protected external action, and invalid idempotent replay fail closed.
