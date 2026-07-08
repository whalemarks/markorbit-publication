# TASK-008 — Workflow Validator Scaffold

**Task ID:** TASK-008  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Task Title:** Workflow Validator Scaffold  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md; codex-tasks/TASK-005-idempotency-event-trace.md; codex-tasks/TASK-006-error-versioning-validation.md; codex-tasks/TASK-007-api-validator-scaffold.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Workflow Specs:** core-specs/workflows/  
**Related Workflow Contracts:** core-specs/contracts/workflows/  
**Related Test Contract:** core-specs/contracts/tests/workflow-contract-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** MVP Workflows Level 2/3; Stub Workflows Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task creates workflow validator scaffolds for MarkOrbit Core workflows.

It ensures every workflow boundary validates:

```text
workflow request shape
workflow response shape
workflow contract version
workflow step contract
reference usage
permission context
policy context
idempotency for apply
AI context where applicable
human review gates
task plan generation boundaries
event trace references
safe errors
owning service delegation
```

This task does not implement a full workflow engine.

It creates governed workflow preview/apply validators so the MVP execution spine can proceed without architecture drift.

---

# 2. Core Lock

```text
Workflows coordinate execution.
Workflow Contracts constrain execution.
Owning services own behavior.
Workflow layer must not own domain behavior.
Workflow layer must not create active Tasks directly.
Workflow layer must not emit Events directly.
Workflow layer may prepare Task plans.
Task Service creates active Tasks.
Event Service preserves Event trace.
Permission and Policy govern workflow behavior.
AI may assist workflow preparation but must not execute protected actions.
Human Review gates protected workflow transitions.
Idempotency protects workflow apply.
Codex implements workflow validators.
Codex does not build a full workflow engine in MVP.
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
codex-tasks/TASK-004-permission-policy-hooks.md
codex-tasks/TASK-005-idempotency-event-trace.md
codex-tasks/TASK-006-error-versioning-validation.md
codex-tasks/TASK-007-api-validator-scaffold.md
core-specs/workflows/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/common/index.md
```

Codex must also read MVP workflow specs:

```text
core-specs/workflows/customer-intake-workflow.md
core-specs/workflows/trademark-application-workflow.md
core-specs/workflows/communication-review-workflow.md
```

Codex must also read MVP workflow contracts:

```text
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
```

Codex should also read stub workflow specs and contracts:

```text
core-specs/workflows/office-action-response-workflow.md
core-specs/workflows/provider-routing-workflow.md
core-specs/workflows/renewal-workflow.md
core-specs/workflows/assignment-workflow.md
core-specs/workflows/evidence-review-workflow.md
core-specs/contracts/workflows/office-action-response-workflow-contract.md
core-specs/contracts/workflows/provider-routing-workflow-contract.md
core-specs/contracts/workflows/renewal-workflow-contract.md
core-specs/contracts/workflows/assignment-workflow-contract.md
core-specs/contracts/workflows/evidence-review-workflow-contract.md
```

---

# 4. Scope

This task covers workflow validator scaffolds for:

## 4.1 MVP Workflows

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

These require Level 2 validator implementation and selected Level 3 enforcement for protected gates.

## 4.2 Stub Workflows

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

These require Level 1/2 validation-only or preview-only scaffolds.

---

# 5. Out of Scope

This task must not implement:

```text
full workflow engine
dynamic workflow designer
distributed workflow orchestration
production scheduling engine
official filing execution
external communication sending
provider final selection
automatic evidence sufficiency decision
automatic deadline certification
full agent runtime
product UI
payment execution
external integrations
```

Workflow validators coordinate and constrain. They do not execute protected professional actions by themselves.

---

# 6. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/contracts/workflows/validators/
  base.py
  customer_intake.py
  trademark_application.py
  communication_review.py
  office_action_response.py
  provider_routing.py
  renewal.py
  assignment.py
  evidence_review.py
```

Preferred TypeScript-like shape:

```text
src/core/contracts/workflows/validators/
  base.ts
  customer-intake.ts
  trademark-application.ts
  communication-review.ts
  office-action-response.ts
  provider-routing.ts
  renewal.ts
  assignment.ts
  evidence-review.ts
```

Suggested tests:

```text
tests/contracts/test_workflow_validators.py
tests/contracts/test_workflow_preview_apply.py
tests/contracts/test_workflow_permission_policy.py
tests/contracts/test_workflow_idempotency_event.py
tests/contracts/test_workflow_ai_human_review.py
tests/contracts/test_workflow_service_boundaries.py
```

---

# 7. Required Workflow Validator Behavior

Every workflow validator must support:

```text
validate_preview_request(...)
validate_preview_response(...)
validate_apply_request(...)
validate_apply_response(...)
validate_workflow_contract_version(...)
validate_workflow_steps(...)
validate_references(...)
validate_permission_context(...)
validate_policy_context(...)
validate_error_shape(...)
```

Where applicable, validators must also support:

```text
validate_idempotency_for_apply(...)
validate_ai_context(...)
validate_human_review(...)
validate_task_plan(...)
validate_event_trace(...)
validate_service_delegation(...)
```

Every validator must return controlled success/failure results.

---

# 8. Workflow Boundary Rules

Workflow validators must enforce:

```text
workflow request schema is valid
workflow response schema is valid
workflow_contract_version is supported
public references use Reference Contract
raw database IDs are rejected
Permission Context exists for protected behavior
Policy Context exists for policy-controlled behavior
idempotency_key exists for apply
AI Context exists for AI-assisted workflow output
Human Review exists where protected transition requires review
Task plan is only a plan until Task Service creates active Tasks
event_reference_ids are trace only
Error Contract is used for failures
Versioning Contract is used for compatibility
```

Workflow validators must not:

```text
mutate domain state directly
create active Tasks directly
emit Events directly
send Communications
select providers as final decision
submit official filings
certify deadlines
certify registrability
certify evidence sufficiency
```

---

# 9. Workflow-to-Service Boundary Assertions

Codex must implement or test boundary assertions:

```text
Customer Intake Workflow coordinates Customer, Brand, Matter, Order, Document, Task and Event trace through owning services.
Trademark Application Workflow coordinates Trademark, Brand, Jurisdiction, Classification, Document, Evidence, Matter, Order, Task and Event trace through owning services.
Communication Review Workflow coordinates Communication, Human Review, Task and Event trace through owning services.
Office Action Response Workflow remains validation-only or preview-only in MVP.
Provider Routing Workflow remains validation-only or preview-only in MVP.
Renewal Workflow remains validation-only or preview-only in MVP.
Assignment Workflow remains validation-only or preview-only in MVP.
Evidence Review Workflow remains validation-only or preview-only in MVP.
```

Core rule:

```text
Workflow coordinates.
Owning Service mutates.
Task Service creates active Tasks.
Event Service records trace.
```

---

# 10. MVP Workflow Validators

## 10.1 Customer Intake Workflow

Must validate:

```text
customer reference or customer candidate
brand reference or brand candidate
matter/order candidate
document attachments
permission context
policy context
AI-assisted intake summary where applicable
human review where protected
task plan
idempotency_key for apply
event trace references
safe errors
supported workflow_contract_version
```

Must not:

```text
approve legal strategy
submit official filing
send external communication automatically
create active Tasks outside Task Service
emit Events directly
```

## 10.2 Trademark Application Workflow

Must validate:

```text
trademark reference or trademark candidate
brand reference
jurisdiction reference
classification suggestions
goods/services draft
document attachments
evidence references where applicable
matter/order context
permission context
policy context
AI-assisted classification draft
human review before professional conclusion
task plan
idempotency_key for apply
event trace references
safe errors
supported workflow_contract_version
```

Must not:

```text
certify registrability
finalize goods/services without human review
submit official application
certify official deadline
emit Events directly
create active Tasks outside Task Service
```

## 10.3 Communication Review Workflow

Must validate:

```text
communication draft
communication type
source context
AI-assisted draft where applicable
policy omissions
human review gate
permission context
policy context
task plan where applicable
idempotency_key for apply
event trace references
safe errors
supported workflow_contract_version
```

Must not:

```text
send external communication without human review
represent AI draft as approved professional output
bypass Policy redaction
emit Events directly
create active Tasks outside Task Service
```

---

# 11. Stub Workflow Validators

Stub workflows must support safe validation only.

## 11.1 Office Action Response Workflow

Allowed:

```text
preview-only validation
document/reference validation
task plan preview
human review requirement
AI draft support within bounds
```

Forbidden:

```text
filing response submission
professional legal conclusion certification
deadline certification
```

## 11.2 Provider Routing Workflow

Allowed:

```text
routing candidate preview
provider reference validation
policy visibility validation
human review requirement for selection
```

Forbidden:

```text
final provider selection by AI
automatic routing commitment
provider engagement without review
```

## 11.3 Renewal Workflow

Allowed:

```text
renewal readiness preview
document/reference validation
task plan preview
human review requirement
```

Forbidden:

```text
official renewal filing
deadline certification
payment execution
```

## 11.4 Assignment Workflow

Allowed:

```text
assignment readiness preview
document/reference validation
task plan preview
human review requirement
```

Forbidden:

```text
official recordal filing
legal ownership certification
payment execution
```

## 11.5 Evidence Review Workflow

Allowed:

```text
evidence gap preview
evidence reference validation
AI-assisted summary
human review requirement
```

Forbidden:

```text
AI final evidence sufficiency decision
professional truth certification
official filing submission
```

---

# 12. Idempotency Requirements

Workflow apply operations must require:

```text
idempotency_key
```

Required behavior:

```text
missing key returns IdempotencyKeyRequired
same key + same semantic workflow apply request replays safely
same key + different workflow apply request returns IdempotencyConflict
replay creates no duplicate active Tasks
replay creates no duplicate Communications
replay creates no duplicate Events
```

Preview operations may be idempotent by nature but must not create side effects.

---

# 13. Event Requirements

Workflow validators must ensure:

```text
Workflow layer does not emit Events directly.
Workflow response may include event_reference_ids only as trace.
event_reference_ids must follow Reference Contract.
event_reference_ids must not trigger commands.
Event visibility follows Permission and Policy.
```

Required test:

```text
workflow_layer_does_not_emit_events_directly
```

---

# 14. Task Plan Requirements

Workflow validators may validate Task plans.

Task plan fields may include:

```text
planned_task_type
subject_reference_id
required_owner_role
priority
due_date_basis
human_review_required
policy_restrictions
source_step
```

Rules:

```text
Task plan is not an active Task.
Task plan does not create work by itself.
Only Task Service creates active Tasks.
Workflow apply may request Task Service to create active Tasks if allowed by contract.
```

Required test:

```text
workflow_task_plan_not_active_task
```

---

# 15. AI and Human Review Requirements

Where workflow output is AI-assisted:

```text
AI Context must exist.
capability_scope must be valid.
source_scope must be valid.
policy_omissions_disclosed must be true where restricted sources are omitted.
AI must not approve, send, select, submit, certify, complete or mutate protected state.
```

Where protected transition requires review:

```text
human_review_reference_id must be valid.
missing review returns HumanReviewRequired.
Human Review must not execute downstream action by itself.
```

---

# 16. Required Fixtures

Use fixtures from TASK-002:

```text
customer_intake_preview_request
customer_intake_apply_request
trademark_application_preview_request
trademark_application_apply_request
communication_review_preview_request
communication_review_apply_request
missing_permission_request
policy_restricted_request
human_review_required_request
idempotency_replay_request
idempotency_conflict_request
unsupported_version_request
AI forbidden action fixture
event_reference_not_command fixture
task_plan_preview fixture
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline ad hoc production-like fixtures.
```

---

# 17. Required Tests

This task must implement tests for:

```text
all workflow validator files exist or are intentionally scaffolded
MVP workflow preview request validation
MVP workflow preview response validation
MVP workflow apply request validation
MVP workflow apply response validation
stub workflow preview-only or validation-only behavior
reference validation rejects database IDs
PermissionDenied blocks protected workflow action
PolicyRestricted blocks or redacts workflow output
HumanReviewRequired returned where review missing
AI forbidden workflow action blocked
idempotency_key required for apply
idempotency replay/conflict behavior for apply
task plan is not active Task
Workflow layer does not create active Tasks directly
Workflow layer does not emit Events directly
event_reference_ids are trace only
safe error shape used
unsupported workflow version fails closed
```

Required test source:

```text
core-specs/contracts/tests/workflow-contract-tests.md
```

---

# 18. Integration Points for Later Tasks

This task must expose validator scaffolds usable by:

```text
TASK-009-agent-boundary-tests
TASK-010-mvp-execution-spine
```

Expected interfaces should support:

```text
validate_workflow_preview_request(...)
validate_workflow_preview_response(...)
validate_workflow_apply_request(...)
validate_workflow_apply_response(...)
validate_workflow_task_plan(...)
assert_workflow_does_not_emit_events(...)
assert_workflow_does_not_create_active_tasks(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 19. Forbidden Shortcuts

Codex must not:

```text
build full workflow engine in MVP
skip stub workflow validators
mutate domain state in workflow validators
create active Tasks directly from workflow layer
emit Events from workflow layer
send Communications directly from workflow layer
select providers directly from workflow layer or AI
submit official filings
certify deadlines
certify registrability
certify evidence sufficiency
treat preview as apply
skip idempotency validation for apply
default Permission to allowed
default Policy to allowed
ignore HumanReviewRequired
ignore AI forbidden actions
expose raw database IDs
use production data fixtures
```

---

# 20. Acceptance Criteria

This task is complete only if:

```text
[ ] Workflow validator scaffold exists.
[ ] All MVP workflow validators exist.
[ ] Stub workflow validators exist or are explicitly marked preview-only/validation-only.
[ ] Preview request validation exists.
[ ] Preview response validation exists.
[ ] Apply request validation exists.
[ ] Apply response validation exists.
[ ] Reference validation is enforced.
[ ] Permission Context is enforced for protected workflow actions.
[ ] Policy Context is enforced for policy-controlled workflow behavior.
[ ] Idempotency is enforced for apply.
[ ] AI Context is validated where AI-assisted output exists.
[ ] Human Review is validated where review gates exist.
[ ] Task plan is validated but not treated as active Task.
[ ] Workflow layer no-direct-task-creation is tested.
[ ] Workflow layer no-direct-event-emission is tested.
[ ] Event references are trace only.
[ ] Safe errors are used.
[ ] Unsupported workflow versions fail closed.
[ ] Tests pass.
```

---

# 21. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Workflow validator scaffold implemented.
- Files added or changed.
- Which MVP workflow validators are Level 2/3.
- Which stub workflow validators are Level 1/2.
- Which source specs were used.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- Workflow layer does not mutate domain state directly.
- Workflow layer does not create active Tasks directly.
- Workflow layer does not emit Events directly.
- References use Reference Contract.
- Permission/Policy fail closed.
- Idempotency enforced for apply.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Event references are trace, not commands.
- Errors are safe.
- Unsupported versions fail closed.

Deferred
- Full workflow engine remains out of scope.
- Production workflow execution remains out of scope.
- Next task recommended.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-008. Defines Workflow validator scaffold implementation scope, required source files, MVP/stub workflow depth, workflow boundary rules, task plan rules, idempotency, event, AI/human review requirements, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-008 — Workflow Validator Scaffold**
