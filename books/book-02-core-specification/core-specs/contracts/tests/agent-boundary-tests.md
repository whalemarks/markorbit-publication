# Agent Boundary Tests

**Spec ID:** B02-CONTRACT-TESTS-AGENT-BOUNDARY  
**Spec Type:** Test Contract Specification  
**Contract Name:** Agent Boundary Tests  
**Contract File:** core-specs/contracts/tests/agent-boundary-tests.md  
**Contract Category:** Test Contracts  
**Related Contract Layers:** Agent Contracts; Common Contracts; API Contracts; Workflow Contracts  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/workflow-agent.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md  
**Related API Contracts:** core-specs/contracts/api/agent-api-contract.md; core-specs/contracts/api/workflow-contract-api-contract.md; core-specs/contracts/api/task-api-contract.md; core-specs/contracts/api/communication-api-contract.md; core-specs/contracts/api/routing-api-contract.md; core-specs/contracts/api/knowledge-api-contract.md; core-specs/contracts/api/event-api-contract.md  
**Related Workflow Contracts:** core-specs/contracts/workflows/customer-intake-workflow-contract.md; core-specs/contracts/workflows/trademark-application-workflow-contract.md; core-specs/contracts/workflows/office-action-response-workflow-contract.md; core-specs/contracts/workflows/provider-routing-workflow-contract.md; core-specs/contracts/workflows/communication-review-workflow-contract.md; core-specs/contracts/workflows/renewal-workflow-contract.md; core-specs/contracts/workflows/assignment-workflow-contract.md; core-specs/contracts/workflows/evidence-review-workflow-contract.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contracts:** core-specs/contracts/tests/README.md; core-specs/contracts/tests/template.md; core-specs/contracts/tests/common-contract-tests.md; core-specs/contracts/tests/api-contract-tests.md; core-specs/contracts/tests/workflow-contract-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**Test Contract Version:** v0.1.0  
**MVP Phase:** Phase 3–5 — AI / Agent Governance Verification  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Agent Boundary Tests define acceptance-level testing requirements for all MarkOrbit AI and agent-assisted behavior.

They verify:

```text
agent registry validation
agent capability scope enforcement
agent identity and reference validation
AI Context enforcement
Permission and Policy enforcement
source-grounded output requirements
policy omission disclosure
human review preservation
forbidden action blocking
downstream service boundary
event trace behavior
idempotency behavior
safe error behavior
version compatibility
Codex implementation acceptance
```

Agent Boundary Tests ensure that agents can prepare, summarize, draft, suggest, compare and validate within governed scope, but cannot approve, submit, send, select, certify, mutate protected state, create professional truth, bypass Permission/Policy, or complete downstream execution.

---

# 2. Core Lock

```text
Agent Boundary Tests verify governed AI capability boundaries.
Agent Service owns agent identity and capability registry behavior.
Agents may prepare, summarize, draft, suggest, compare and validate within scope.
Agents must not approve, send, select, submit, certify, complete or mutate protected state.
Permission and Policy must govern every agent-assisted action.
AI Context must disclose source scope and policy omissions.
Human review requirements must be preserved.
Downstream actions must route through owning services.
Events preserve trace.
```

---

# 3. Test Boundary

This Test Contract is responsible for:

```text
testing agent registry validation
testing agent capability scope
testing AI Context shape
testing source scope disclosure
testing policy omission disclosure
testing Permission and Policy enforcement
testing forbidden actions
testing human review preservation
testing downstream service routing
testing safe output boundaries
testing safe errors
testing event trace behavior
testing idempotency behavior
testing versioning behavior
```

This Test Contract is not responsible for:

```text
model quality scoring by itself
prompt optimization
generic LLM evaluation
UI chat tests
production data evaluation
unbounded autonomous agents
permission grant logic implementation
policy rule implementation
domain service business logic by itself
```

---

# 4. Related Contracts

This test contract validates:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
core-specs/agents/workflow-agent.md
core-specs/agents/knowledge-agent.md
core-specs/agents/task-agent.md
core-specs/agents/communication-agent.md
core-specs/agents/routing-agent.md
core-specs/agents/audit-agent.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/human-review.md
```

Rules:

```text
- Every agent-assisted behavior must trace to an Agent Spec or AI Agent Governance Spec.
- Every agent-assisted API or workflow behavior must preserve the related API/Workflow Contract boundaries.
- Agent tests must not invent autonomous authority not granted by Core.
```

---

# 5. Test Subject

```yaml
test_subject:
  subject_type: AgentBoundary
  subject_name: Agent Boundary Layer
  owning_service: Agent Service
  contract_file: core-specs/agents/*.md
  behavior_scope:
    - agent registry validation
    - capability scope enforcement
    - AI Context enforcement
    - Permission and Policy enforcement
    - source-grounding disclosure
    - policy omission disclosure
    - human review preservation
    - forbidden action blocking
    - downstream service routing
    - safe output
    - errors
    - versioning
```

---

# 6. Required Fixtures

Required fixture set:

```yaml
fixtures:
  - fixture_key: agent-registry-fixture
    fixture_type: AI Context Fixture
    purpose: valid, invalid, inactive and wrong-capability agent references
    contains_production_data: false
    required: true

  - fixture_key: agent-capability-fixture
    fixture_type: AI Context Fixture
    purpose: allowed and forbidden capability testing
    contains_production_data: false
    required: true

  - fixture_key: source-scope-fixture
    fixture_type: Domain Object Fixture
    purpose: source-grounded, partial-source and no-source output testing
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

  - fixture_key: human-review-fixture
    fixture_type: Human Review Fixture
    purpose: human-review-required and missing-review testing
    contains_production_data: false
    required: true

  - fixture_key: forbidden-action-fixture
    fixture_type: AI Context Fixture
    purpose: approve, send, select, submit, certify, complete and mutate attempts
    contains_production_data: false
    required: true

  - fixture_key: idempotency-fixture
    fixture_type: Idempotency Fixture
    purpose: duplicate agent-prepared downstream requests
    contains_production_data: false
    required: true

  - fixture_key: event-trace-fixture
    fixture_type: Event Trace Fixture
    purpose: agent output trace and no-direct-event-emission testing
    contains_production_data: false
    required: true

  - fixture_key: error-fixture
    fixture_type: Error Fixture
    purpose: safe error and restricted leakage testing
    contains_production_data: false
    required: true

  - fixture_key: version-fixture
    fixture_type: Version Fixture
    purpose: supported and unsupported agent contract version testing
    contains_production_data: false
    required: true
```

Fixture rules:

```text
- Fixtures must be deterministic.
- Fixtures must not contain production data.
- Fixtures must include allowed and forbidden capabilities.
- Fixtures must include policy-allowed, redacted and blocked cases.
- Fixtures must include source-grounded and insufficient-source cases.
- Fixtures must include human-review-present and human-review-missing cases.
- Fixtures must include downstream action attempts.
```

---

# 7. Agent Registry Tests

Agent registry tests must verify:

```text
valid agent reference accepted
invalid agent reference rejected
inactive agent rejected
wrong agent type rejected
agent registry key matches capability scope
agent version supported
agent identity does not imply permission
agent identity does not bypass policy
```

Test skeleton:

```yaml
agent_registry_tests:
  - test_key: agent-registry-valid
    test_title: Valid Agent Registry Entry Is Accepted
    given:
      - valid agent_reference_id
      - active agent registry entry
      - requested capability within scope
    when:
      - agent-assisted operation is evaluated
    then:
      - agent is accepted
      - capability scope validation passes
      - Permission and Policy evaluation still occur
```

Negative test:

```yaml
negative_tests:
  - test_key: agent-registry-invalid
    test_title: Invalid Agent Registry Entry Is Rejected
    given:
      - invalid or inactive agent_reference_id
    when:
      - agent-assisted operation is evaluated
    then:
      - AgentReferenceInvalid or PermissionDenied is returned
      - no agent-assisted output is trusted as governed output
```

---

# 8. Capability Scope Tests

Capability tests must verify:

```text
allowed capability accepted
forbidden capability rejected
capability scope must match agent type
capability scope must match target operation
capability scope must not expand at runtime
capability scope must be versioned
```

Test skeleton:

```yaml
capability_scope_tests:
  - test_key: agent-capability-allowed
    test_title: Allowed Agent Capability Is Accepted
    given:
      - agent with CommunicationDraft capability
      - communication draft request
    when:
      - capability is evaluated
    then:
      - draft assistance may proceed
      - approve/send capability is not granted
```

Negative test:

```yaml
negative_tests:
  - test_key: agent-capability-forbidden
    test_title: Forbidden Agent Capability Is Blocked
    given:
      - agent without RoutingSelect capability
      - provider selection request
    when:
      - capability is evaluated
    then:
      - action is blocked
      - no provider selection occurs
```

---

# 9. AI Context Tests

AI Context tests must verify:

```text
ai_assisted is true for AI output
agent_reference_id or agent_registry_key is present
source_scope_disclosed is true where source-grounded output is required
policy_omissions_disclosed is true where policy redaction occurred
human_review_required is preserved
AI output is marked as assistance
AI output does not become professional truth by itself
```

Test skeleton:

```yaml
ai_context_tests:
  - test_key: ai-context-required
    test_title: AI-Assisted Output Requires AI Context
    given:
      - AI-generated draft or recommendation
      - missing AI Context
    when:
      - output is returned
    then:
      - ValidationFailed is returned
      - output is not accepted as governed output
```

---

# 10. Source Scope Tests

Source scope tests must verify:

```text
visible sources are disclosed
missing source scope downgrades output
policy-redacted sources are disclosed as omissions
source-grounded output distinguishes source facts from inference
Knowledge Agent output cites source references where required
Audit Agent output distinguishes trace from inference
```

Test skeleton:

```yaml
source_scope_tests:
  - test_key: source-scope-disclosed
    test_title: Agent Output Discloses Source Scope
    given:
      - agent-assisted summary
      - visible source references
    when:
      - output is returned
    then:
      - source_scope_disclosed is true
      - source references are included where policy allows
      - policy omissions are disclosed where applicable
```

Negative test:

```yaml
negative_tests:
  - test_key: source-scope-missing
    test_title: Missing Source Scope Downgrades Agent Output
    given:
      - source-grounded operation
      - no source scope disclosed
    when:
      - output is evaluated
    then:
      - output is rejected or downgraded
      - human_review_required is true where applicable
```

---

# 11. Permission Tests

Permission tests must verify:

```text
agent-assisted action requires permission keys
Permission Service invoked
PermissionDenied blocks agent-assisted output or downstream action
agent identity does not imply permission
permission approval does not bypass Policy
unknown permission fails closed
```

Test skeleton:

```yaml
permission_tests:
  - test_key: agent-permission-denied
    test_title: PermissionDenied Blocks Agent-Assisted Action
    given:
      - valid agent
      - requested protected capability
      - PermissionDenied decision
    when:
      - agent-assisted operation is evaluated
    then:
      - PermissionDenied is returned
      - no protected output or downstream action occurs
```

---

# 12. Policy Tests

Policy tests must verify:

```text
agent-assisted action requires policy scopes
Policy Service invoked
PolicyRestricted blocks or redacts output
restricted_fields_omitted is true where redaction occurs
policy_omissions_disclosed is true where AI output is partial
policy internals not exposed
NotFound may replace PolicyRestricted where non-disclosure is required
```

Test skeleton:

```yaml
policy_tests:
  - test_key: agent-policy-restricted-redaction
    test_title: PolicyRestricted Redacts Agent Output
    given:
      - valid agent
      - PermissionAllowed
      - PolicyRestricted redaction decision
    when:
      - agent-assisted output is generated
    then:
      - restricted fields are omitted
      - policy_omissions_disclosed is true
      - restricted_fields_omitted is true where applicable
```

---

# 13. Human Review Preservation Tests

Human Review tests must verify:

```text
agent output preserves human_review_required
missing human review blocks protected downstream action
valid human review reference is trace only
agent cannot satisfy review requirement by itself
human reviewer identity is governed by Permission/Policy
owning service decides whether review satisfies action requirement
```

Test skeleton:

```yaml
human_review_tests:
  - test_key: agent-does-not-satisfy-human-review
    test_title: Agent Output Does Not Satisfy Human Review by Itself
    given:
      - AI-assisted recommendation
      - protected downstream action requires human review
    when:
      - downstream action is requested
    then:
      - HumanReviewRequired is returned
      - agent output is treated as assistance only
```

---

# 14. Forbidden Action Tests

Agent forbidden actions must include:

```text
approve communication
send communication
select provider
submit filing
submit office action response
submit renewal
record assignment
certify deadline
certify authority
decide registrability
decide evidence sufficiency
approve payment
complete task
mutate protected domain state directly
emit events directly
```

Test skeleton:

```yaml
forbidden_action_tests:
  - test_key: agent-cannot-send-communication
    test_title: Agent Cannot Send Communication
    given:
      - Communication Agent
      - send communication request
    when:
      - agent-assisted operation is evaluated
    then:
      - action is blocked
      - Communication Service governed send process is required
      - no external delivery occurs

  - test_key: agent-cannot-select-provider
    test_title: Routing Agent Cannot Select Provider
    given:
      - Routing Agent
      - provider selection request
    when:
      - agent-assisted operation is evaluated
    then:
      - action is blocked
      - Routing Service selection with human/service review is required
      - no RoutingSelected event is emitted by agent

  - test_key: agent-cannot-certify-deadline
    test_title: Agent Cannot Certify Deadline
    given:
      - Knowledge Agent or Workflow Agent
      - deadline certification request
    when:
      - output is generated
    then:
      - output is marked as candidate or summary
      - human_review_required is true
      - no certified deadline state is created
```

---

# 15. Downstream Service Boundary Tests

Downstream boundary tests must verify:

```text
agent cannot create active Task directly
agent cannot create Communication directly outside Communication Service
agent cannot evaluate/select Routing outside Routing Service
agent cannot mutate Trademark/Customer/Matter/Order/Document/Evidence directly
agent cannot emit Events directly
agent-prepared output must route through owning service for execution
```

Test skeleton:

```yaml
service_boundary_tests:
  - test_key: agent-output-routes-through-owning-service
    test_title: Agent Output Routes Through Owning Service
    given:
      - agent-prepared task plan
      - create_tasks requested
    when:
      - execution is requested
    then:
      - Task Service is invoked
      - agent does not create active Tasks directly
      - TaskCreated event is emitted only by Task Service where applicable
```

---

# 16. Agent-Specific Boundary Tests

## 16.1 Workflow Agent

Must verify:

```text
may summarize workflow context
may prepare preview suggestions
may identify missing context
must not apply workflow by itself
must not create active Tasks
must not mutate domain state
```

## 16.2 Knowledge Agent

Must verify:

```text
may retrieve and summarize governed sources
must disclose source scope
must disclose policy omissions
must not create professional truth
must not certify legal rules or deadlines
```

## 16.3 Task Agent

Must verify:

```text
may prepare task plans
may summarize task state
must not create active Tasks directly
must not complete Tasks
must not bypass Task Service
```

## 16.4 Communication Agent

Must verify:

```text
may draft communication
may summarize context
may propose revisions
must not approve communication
must not send communication
must not bind the organization
```

## 16.5 Routing Agent

Must verify:

```text
may compare candidates
may prepare recommendation summary
must not select provider
must not approve provider engagement
must not expose restricted commercial terms
```

## 16.6 Audit Agent

Must verify:

```text
may summarize visible event trace
must distinguish trace from inference
must not treat event references as commands
must not expose restricted events
```

---

# 17. Idempotency Tests

Idempotency tests must verify:

```text
agent-prepared duplicate-sensitive execution requires idempotency_key
same agent-prepared request + same key replays safely
same key + different semantic request returns IdempotencyConflict
duplicate agent-prepared task creation request does not duplicate Tasks
duplicate agent-prepared communication request does not duplicate Communication
duplicate agent-prepared routing request does not duplicate RoutingSelected event
```

Test skeleton:

```yaml
idempotency_tests:
  - test_key: agent-prepared-request-idempotent
    test_title: Agent-Prepared Downstream Request Is Idempotent
    given:
      - agent-prepared request
      - idempotency_key
      - first successful downstream service request
    when:
      - same request is replayed
    then:
      - response is safe
      - no duplicate downstream object is created
      - no duplicate event is emitted
```

---

# 18. Event Trace Tests

Event tests must verify:

```text
agent output may reference event trace where policy allows
agent does not emit Events directly
event references are trace only
Audit Agent does not treat events as commands
restricted event visibility follows Policy
idempotent replay does not duplicate events
```

Test skeleton:

```yaml
event_trace_tests:
  - test_key: agent-no-direct-event-emission
    test_title: Agent Does Not Emit Events Directly
    given:
      - agent-assisted operation
    when:
      - operation completes
    then:
      - Event Service or owning domain service owns events
      - agent output may include event_reference_ids as trace where allowed
      - no direct agent event emission occurs
```

---

# 19. Error Safety Tests

Error tests must verify:

```text
controlled error code
safe error shape
agent errors do not expose prompt internals
agent errors do not expose hidden chain-of-thought
agent errors do not expose restricted source data
agent errors do not expose policy internals
agent errors do not expose permission internals
database IDs not exposed
correlation_id preserved
retryable flag present
```

Test skeleton:

```yaml
error_safety_tests:
  - test_key: agent-safe-error-no-leakage
    test_title: Agent Error Does Not Leak Restricted Information
    given:
      - agent-assisted request
      - restricted source data
      - failure occurs
    when:
      - error response is generated
    then:
      - error follows Error Contract
      - prompt internals are not exposed
      - restricted source data is not exposed
      - policy and permission internals are not exposed
```

---

# 20. Versioning Tests

Versioning tests must verify:

```text
supported agent_contract_version accepted
supported ai_context_version accepted
supported capability version accepted
missing required version rejected
unsupported version rejected
capability expansion requires version bump
historical agent output records version where required
deprecated version not silently rewritten
```

Test skeleton:

```yaml
versioning_tests:
  - test_key: agent-version-unsupported
    test_title: Unsupported Agent Version Fails Closed
    given:
      - unsupported agent_contract_version
    when:
      - agent-assisted operation is evaluated
    then:
      - VersionUnsupported is returned
      - no protected action occurs
```

---

# 21. Contract Coverage Matrix

```yaml
coverage_matrix:
  agent_registry:
    required: true
    covered_by:
      - agent-registry-valid
      - agent-registry-invalid
  capability_scope:
    required: true
    covered_by:
      - agent-capability-allowed
      - agent-capability-forbidden
  ai_context:
    required: true
    covered_by:
      - ai-context-required
  source_scope:
    required: true
    covered_by:
      - source-scope-disclosed
      - source-scope-missing
  permission:
    required: true
    covered_by:
      - agent-permission-denied
  policy:
    required: true
    covered_by:
      - agent-policy-restricted-redaction
  human_review:
    required: true
    covered_by:
      - agent-does-not-satisfy-human-review
  forbidden_actions:
    required: true
    covered_by:
      - agent-cannot-send-communication
      - agent-cannot-select-provider
      - agent-cannot-certify-deadline
  service_boundary:
    required: true
    covered_by:
      - agent-output-routes-through-owning-service
  idempotency:
    required: true
    covered_by:
      - agent-prepared-request-idempotent
  event_trace:
    required: true
    covered_by:
      - agent-no-direct-event-emission
  errors:
    required: true
    covered_by:
      - agent-safe-error-no-leakage
  versioning:
    required: true
    covered_by:
      - agent-version-unsupported
```

---

# 22. Codex Implementation Notes

Codex must:

```text
cite this Agent Boundary Tests file
cite AI Agent Governance Spec
cite Agent Registry Spec
cite the specific Agent Spec being tested
cite AI Context Contract
cite Permission Context Contract
cite Policy Context Contract
cite Human Review Contract
cite related API and Workflow Contracts
generate deterministic non-production fixtures
write registry validation tests
write capability scope tests
write AI Context tests
write source scope disclosure tests
write PermissionDenied tests
write PolicyRestricted and redaction tests
write human-review preservation tests
write forbidden-action tests
write downstream service boundary tests
write agent-specific boundary tests
write idempotency replay/conflict tests
write event trace tests
write safe error tests
write VersionUnsupported tests
```

Codex must not:

```text
treat model output quality tests as boundary tests
skip forbidden-action tests
allow agents to execute protected actions
mock away Permission or Policy without asserting invocation
allow agent identity to imply permission
allow AI output to become professional truth by itself
allow agent-created event emission
allow agent-created active Tasks outside Task Service
expose prompt internals or hidden reasoning
ignore source scope or policy omissions
ignore human-review requirements
ignore version validation
```

---

# 23. Acceptance Criteria

This Agent Boundary Tests file is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines test boundary.
[ ] It lists related Agent, API, Workflow and Common Contracts.
[ ] It defines test subject.
[ ] It defines required fixtures.
[ ] It defines agent registry tests.
[ ] It defines capability scope tests.
[ ] It defines AI Context tests.
[ ] It defines source scope tests.
[ ] It defines Permission tests.
[ ] It defines Policy tests.
[ ] It defines Human Review preservation tests.
[ ] It defines forbidden action tests.
[ ] It defines downstream service boundary tests.
[ ] It defines agent-specific boundary tests.
[ ] It defines Idempotency tests.
[ ] It defines Event Trace tests.
[ ] It defines Error Safety tests.
[ ] It defines Versioning tests.
[ ] It defines coverage matrix.
[ ] It defines Codex implementation notes.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent Boundary Tests. Defines agent registry, capability scope, AI Context, source scope, Permission/Policy, human review, forbidden actions, downstream service boundary, agent-specific boundaries, idempotency, event trace, safe errors, versioning and Codex implementation expectations. |

---

**End of Agent Boundary Tests**
