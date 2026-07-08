# TASK-010 — MVP Execution Spine

**Task ID:** TASK-010  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-010-mvp-execution-spine.md  
**Task Title:** MVP Execution Spine  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md; codex-tasks/TASK-005-idempotency-event-trace.md; codex-tasks/TASK-006-error-versioning-validation.md; codex-tasks/TASK-007-api-validator-scaffold.md; codex-tasks/TASK-008-workflow-validator-scaffold.md; codex-tasks/TASK-009-agent-boundary-tests.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Workflow Specs:** core-specs/workflows/customer-intake-workflow.md; core-specs/workflows/trademark-application-workflow.md; core-specs/workflows/communication-review-workflow.md  
**Related Contracts:** core-specs/contracts/  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** MVP Spine Level 2/3  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements the first executable MarkOrbit Core MVP spine.

It should only begin after the contract, fixture, governance, API, workflow and agent boundary foundations are in place.

The MVP execution spine proves that MarkOrbit Core can support a governed professional trademark-service flow without building the full platform.

The target spine is:

```text
Customer
↓
Brand / Trademark
↓
Matter / Order
↓
Document / Evidence
↓
Workflow Contract
↓
Task
↓
Communication
↓
Event
↓
Permission / Policy
↓
Tests
```

This task is not a product UI task. It is a Core execution proof.

---

# 2. Core Lock

```text
MVP Execution Spine proves Core behavior.
Core provides primitives and contracts.
Owning services own behavior.
API layer routes and validates.
Workflow layer coordinates.
Task Service creates active Tasks.
Event Service preserves trace.
Communication Service owns Communication behavior.
Permission and Policy govern protected actions.
AI assists but does not decide or execute.
Human Review gates protected professional or external-facing actions.
Idempotency prevents duplicate execution.
Errors remain safe.
Unsupported versions fail closed.
Codex implements the scoped MVP spine.
Codex does not build the full platform.
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
codex-tasks/TASK-008-workflow-validator-scaffold.md
codex-tasks/TASK-009-agent-boundary-tests.md
```

Codex must also read MVP workflow specs and contracts:

```text
core-specs/workflows/customer-intake-workflow.md
core-specs/workflows/trademark-application-workflow.md
core-specs/workflows/communication-review-workflow.md
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
```

Codex must also read MVP API contracts:

```text
core-specs/contracts/api/customer-api-contract.md
core-specs/contracts/api/brand-api-contract.md
core-specs/contracts/api/trademark-api-contract.md
core-specs/contracts/api/jurisdiction-api-contract.md
core-specs/contracts/api/classification-api-contract.md
core-specs/contracts/api/document-api-contract.md
core-specs/contracts/api/evidence-api-contract.md
core-specs/contracts/api/matter-api-contract.md
core-specs/contracts/api/order-api-contract.md
core-specs/contracts/api/workflow-contract-api-contract.md
core-specs/contracts/api/task-api-contract.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/api/communication-api-contract.md
```

Codex must also read MVP service and object specs for the domains in scope.

---

# 4. Preconditions

This task must not start until:

```text
[ ] TASK-001 Common Contract Foundation is implemented or safely stubbed.
[ ] TASK-002 Contract Fixture System exists.
[ ] TASK-003 Common Contract Tests exist.
[ ] TASK-004 Permission Policy Hooks exist.
[ ] TASK-005 Idempotency Event Trace exists.
[ ] TASK-006 Error Versioning Validation exists.
[ ] TASK-007 API Validator Scaffold exists.
[ ] TASK-008 Workflow Validator Scaffold exists.
[ ] TASK-009 Agent Boundary Tests exist.
```

If any precondition is missing:

```text
Do not fake the missing foundation.
Mark the blocked dependency clearly.
Implement only safe adapters around existing foundations.
```

---

# 5. Scope

This task covers the first executable MVP spine across three workflows:

```text
Customer Intake Workflow
Trademark Application Workflow
Communication Review Workflow
```

It covers MVP service behavior for:

```text
Customer
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Matter
Order
Workflow Contract
Task
Event
Communication
Permission
Policy
```

It covers API/workflow wiring only to the extent needed to prove the spine.

---

# 6. Out of Scope

This task must not implement:

```text
full product UI
full workflow engine
full policy engine
full agent runtime
official filing submission
external email send
payment execution
provider marketplace settlement
provider final selection
renewal production workflow
assignment production workflow
office action response production workflow
evidence sufficiency certification
deadline certification
registrability certification
bulk data import/export
public open API portal
```

This task should be narrow and demonstrable.

---

# 7. MVP Spine Scenario

The first executable scenario should demonstrate:

```text
1. Create or link Customer.
2. Create or link Brand.
3. Create or link Trademark.
4. Link Jurisdiction.
5. Prepare Classification suggestion.
6. Attach Document.
7. Attach or prepare Evidence where applicable.
8. Create Matter / Order execution context.
9. Preview Workflow Contract.
10. Apply Workflow Contract with idempotency.
11. Create active Tasks only through Task Service.
12. Create Communication draft through Communication Service.
13. Require Human Review before protected communication send.
14. Record Event trace through Event Service.
15. Enforce Permission and Policy.
16. Return safe errors for invalid or restricted behavior.
17. Preserve version context.
```

The scenario may be implemented as a service-level integration test, CLI command, fixture-driven smoke test or internal test harness.

It does not require user-facing UI.

---

# 8. Required Implementation Behavior

## 8.1 Customer Intake

Must support:

```text
customer candidate or reference
brand candidate or reference
matter/order candidate
document attachment
AI-assisted intake summary where allowed
task plan preview
workflow preview
workflow apply
event trace reference
idempotency for apply
safe error behavior
```

Must enforce:

```text
Permission
Policy
Reference Contract
Error Contract
Idempotency Contract
Versioning Contract
Human Review where protected
```

## 8.2 Trademark Application Preparation

Must support:

```text
trademark candidate or reference
brand reference
jurisdiction reference
classification suggestion
goods/services draft
document attachment
evidence reference or draft
matter/order context
task plan preview
workflow preview
workflow apply
event trace reference
idempotency for apply
AI-assisted classification suggestion where allowed
```

Must enforce:

```text
classification suggestion is not final professional conclusion
goods/services finalization requires Human Review where applicable
no official filing submission
no registrability certification
```

## 8.3 Communication Review

Must support:

```text
communication draft
source context
AI-assisted draft where allowed
policy omission disclosure
human review gate
workflow preview
workflow apply
event trace reference
idempotency for apply
```

Must enforce:

```text
draft is not sent
AI draft is not approved output
Human Review required before external send
Communication Service owns Communication behavior
no external delivery integration
```

---

# 9. Service Ownership Requirements

Codex must preserve service ownership.

Required ownership:

```text
Customer Service owns Customer behavior.
Brand Service owns Brand behavior.
Trademark Service owns Trademark behavior.
Jurisdiction Service owns Jurisdiction behavior.
Classification Service owns Classification behavior.
Document Service owns Document behavior.
Evidence Service owns Evidence behavior.
Matter Service owns Matter behavior.
Order Service owns Order behavior.
Workflow Contract Service owns preview/apply behavior.
Task Service owns active Task creation.
Communication Service owns Communication behavior.
Event Service owns Event record behavior.
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
```

Forbidden:

```text
API layer mutates domain state directly.
Workflow layer creates active Tasks directly.
Workflow layer emits Events directly.
Agent layer mutates state.
Agent layer emits Events.
```

---

# 10. API Boundary Requirements

The MVP spine may expose API-level test calls or handlers, but must enforce:

```text
API validator runs before behavior.
API routes to owning service.
API does not mutate state directly.
API does not emit Events directly.
API returns safe errors.
API requires supported version.
API requires idempotency for duplicate-sensitive create/apply.
```

Required test:

```text
api_spine_routes_to_services
api_spine_does_not_emit_events_directly
api_spine_safe_errors
```

---

# 11. Workflow Boundary Requirements

Workflow behavior must enforce:

```text
workflow validator runs before workflow behavior.
workflow preview has no side effects.
workflow apply requires idempotency.
workflow coordinates owning services.
workflow creates Task plan before active Tasks.
active Tasks are created only by Task Service.
workflow does not emit Events directly.
workflow does not send Communication directly.
workflow does not certify professional conclusions.
```

Required test:

```text
workflow_apply_idempotent
workflow_preview_has_no_side_effects
workflow_does_not_create_tasks_directly
workflow_does_not_emit_events_directly
```

---

# 12. Task Requirements

Active Tasks may be created only through Task Service.

Required Task examples:

```text
review_customer_intake
review_classification_suggestion
prepare_filing_materials
review_communication_draft
confirm_human_review
```

Task records must include:

```text
task_reference_id
task_type
subject_reference_id
status
owner_role or assignee_reference_id where applicable
created_by_service
correlation_id
source_workflow_reference_id where applicable
schema_version
```

Task Service must preserve:

```text
idempotency
permission/policy
safe errors
event trace through Event Service
```

---

# 13. Communication Requirements

Communication behavior must be owned by Communication Service.

Required behavior:

```text
create communication draft
link source context
link matter/order/customer/trademark where applicable
mark as draft
require Human Review before external send
support AI-assisted draft metadata
support policy omission disclosure
record event trace through Event Service
```

Forbidden:

```text
external send
silent approval
AI-approved communication
workflow-sent communication
agent-sent communication
```

---

# 14. Event Trace Requirements

Events must be recorded by Event Service or owning service integration only.

Required event types for MVP spine:

```text
customer-created
brand-created
trademark-created
matter-created
order-created
document-created
document-attached
evidence-created
workflow-contract-previewed
workflow-contract-applied
task-created
task-updated
communication-created
communication-reviewed
permission-evaluated
policy-evaluated
```

Event behavior:

```text
event_reference_id uses Reference Contract.
source_service is owning service.
payload is safe.
visibility follows Permission and Policy.
event_reference_ids are trace only.
event_reference_ids are not commands.
```

---

# 15. Permission / Policy Requirements

The MVP spine must test:

```text
PermissionAllowed + PolicyAllowed success path
PermissionDenied blocked path
UnknownPermission fail-closed path
PolicyRestrictedBlock blocked path
PolicyRestrictedRedact redacted output path
PolicyRequiresHumanReview review-required path
PolicyNonDisclosureNotFound hidden object path where applicable
```

Permission and Policy must be checked for:

```text
workflow preview where protected
workflow apply
create/update Customer
create/update Trademark
create Matter / Order
create Task
create Communication
read restricted Event trace
AI-assisted source use
```

---

# 16. AI Requirements

AI in the MVP spine is allowed only for:

```text
intake summary
classification suggestion
communication draft
workflow preview explanation
task plan suggestion
audit trace summary
```

AI must not:

```text
approve
send
select
submit
certify
complete
mutate protected state
emit Events
finalize classification
certify registrability
certify evidence sufficiency
certify deadline
```

AI-assisted output must include:

```text
AI Context
source_scope
capability_scope
policy_omissions_disclosed where applicable
human_review_required where applicable
draft/suggestion/non_final status
```

---

# 17. Human Review Requirements

Human Review must gate:

```text
external communication
classification finalization
evidence sufficiency conclusion
filing readiness confirmation
workflow apply where protected
provider selection if routing preview appears
```

MVP may implement Human Review as a validated reference or test fixture.

Rules:

```text
Human Review does not execute downstream action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Owning service decides whether review satisfies the gate.
```

---

# 18. Idempotency Requirements

Duplicate-sensitive operations must require idempotency.

Required tests:

```text
workflow apply same key + same semantic request = safe replay
workflow apply same key + different request = IdempotencyConflict
create Customer replay does not duplicate Customer
create Task replay does not duplicate Task
create Communication replay does not duplicate Communication
create Event replay does not duplicate Event
```

---

# 19. Error / Versioning Requirements

Required error behavior:

```text
safe error shape
controlled error codes
no database ID leakage
no restricted data leakage
no stack trace leakage
no policy internals leakage
no permission internals leakage
no AI prompt or hidden reasoning leakage
correlation_id preserved
retryable flag present
```

Required version behavior:

```text
contract_version required
schema_version required where applicable
unsupported version returns VersionUnsupported
historical versions preserved in records where created
```

---

# 20. Required Fixtures

Use fixtures from TASK-002:

```text
customer_intake_preview_request
customer_intake_apply_request
trademark_application_preview_request
trademark_application_apply_request
communication_review_preview_request
communication_review_apply_request
PermissionAllowed
PermissionDenied
UnknownPermission
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
ValidAIContext
AIPolicyOmissions
AIForbiddenActionSubmit
ValidHumanReview
MissingHumanReview
ValidFirstRequest
ReplaySameRequest
ConflictDifferentRequest
VisibleEvent
RestrictedEvent
SupportedContractVersion
UnsupportedContractVersion
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline production-like fixtures.
```

---

# 21. Required Tests

This task must implement integration-level tests for:

```text
customer intake preview success
customer intake apply success
customer intake apply idempotent replay
customer intake apply idempotency conflict
trademark application preview success
trademark application apply success
communication review preview success
communication review apply success
PermissionDenied blocks protected action
UnknownPermission fails closed
PolicyRestrictedBlock blocks action
PolicyRestrictedRedact redacts output
PolicyRequiresHumanReview returns HumanReviewRequired
AI forbidden action blocked
Human Review gate preserved
workflow preview has no side effects
workflow apply creates active Tasks only through Task Service
Communication remains draft until reviewed
no external communication send
Event trace recorded through Event Service
event references are trace only
API layer does not emit Events directly
Workflow layer does not emit Events directly
Agent layer does not emit Events directly
safe errors
unsupported versions fail closed
```

---

# 22. Suggested Test Harness

Codex may implement the spine as:

```text
service-level integration tests
fixture-driven smoke tests
internal CLI demo command
in-memory execution harness
```

Preferred MVP approach:

```text
in-memory or fixture-backed execution harness
deterministic tests
no production persistence requirement
no external network calls
no real customer/trademark data
```

---

# 23. Forbidden Shortcuts

Codex must not:

```text
skip previous task foundations
create product UI instead of Core spine
build full workflow engine
build full policy engine
build full agent runtime
submit official filing
send external communication
execute payment
certify registrability
certify deadline
certify evidence sufficiency
allow AI to approve/send/select/submit/certify/complete
allow workflow layer to create active Tasks directly
allow workflow layer to emit Events directly
allow API layer to mutate domain state directly
allow API layer to emit Events directly
allow agent layer to emit Events directly
treat Event references as commands
treat Human Review as downstream execution
ignore idempotency
ignore unsupported versions
default Permission or Policy to allowed
use production data fixtures
```

---

# 24. Acceptance Criteria

This task is complete only if:

```text
[ ] MVP execution spine exists.
[ ] Customer Intake Workflow preview/apply works.
[ ] Trademark Application Workflow preview/apply works.
[ ] Communication Review Workflow preview/apply works.
[ ] API validators are used where API boundary exists.
[ ] Workflow validators are used.
[ ] Owning services own behavior.
[ ] Task Service creates active Tasks.
[ ] Communication Service creates Communication drafts.
[ ] Event Service records trace.
[ ] Permission and Policy are enforced.
[ ] AI output remains draft/suggestion/non-final.
[ ] Human Review gates protected actions.
[ ] Idempotency replay/conflict works.
[ ] Workflow preview has no side effects.
[ ] API layer does not emit Events directly.
[ ] Workflow layer does not emit Events directly.
[ ] Agent layer does not emit Events directly.
[ ] Event references are trace only.
[ ] Safe errors are used.
[ ] Unsupported versions fail closed.
[ ] Tests pass.
```

---

# 25. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- MVP execution spine implemented.
- Files added or changed.
- Which source specs were used.
- Which workflows are executable.
- Which services are real enforcement.
- Which behavior remains stubbed.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- API layer routes only.
- Workflow layer coordinates only.
- Task Service creates active Tasks.
- Event Service records trace.
- Communication remains draft until reviewed.
- Permission/Policy fail closed.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Idempotency replay/conflict verified.
- Events are trace, not commands.
- Errors are safe.
- Unsupported versions fail closed.

Deferred
- Full product UI remains out of scope.
- Full workflow engine remains out of scope.
- External filing/send/payment integrations remain out of scope.
- Recommended next task.
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-010. Defines MVP execution spine implementation scope, required source files, preconditions, three MVP workflow scenarios, service/API/workflow/task/communication/event/permission/policy/AI/human review/idempotency/error/versioning requirements, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-010 — MVP Execution Spine**
