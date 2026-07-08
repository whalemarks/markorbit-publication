# Workflow Specifications Index

**Spec ID:** B02-WORKFLOWS-INDEX  
**Spec Type:** Workflow Specification Index  
**Spec File:** core-specs/workflows/index.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Workflow Contracts:** core-specs/contracts/workflows/index.md  
**Related Workflow Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md; codex-tasks/TASK-010-mvp-execution-spine.md  
**Status:** Draft  
**Version:** 0.1.0  
**Workflow Index Version:** v0.1.0  
**MVP Phase:** Phase 0–1 — Workflow Specification Baseline  
**MVP Depth:** MVP Workflows Level 2/3; Stub Workflows Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file is the canonical index for MarkOrbit Core workflow specifications.

It defines which workflows exist in Book 02, which workflows are included in the MVP execution spine, which workflows are stubs, and which implementation boundaries must be preserved.

Workflow specifications describe professional execution coordination.

Workflow specifications do not create a full workflow engine.

---

# 2. Core Lock

```text
Workflows coordinate execution.
Workflow Contracts constrain execution.
Owning services own behavior.
Workflow preview has no side effects.
Workflow apply requires Idempotency.
Workflow layer may prepare Task plans.
Workflow layer must not create active Tasks directly.
Task Service creates active Tasks.
Workflow layer must not emit Events directly.
Event Service preserves trace.
Workflow layer must not send Communications directly.
Communication Service owns Communication behavior.
AI may assist workflow preparation but must not execute protected actions.
Human Review gates protected workflow transitions.
Codex implements workflow validators from specs and contracts.
Codex does not build a full workflow engine in MVP.
```

---

# 3. Workflow Specification Set

The workflow specification set contains eight workflows.

## 3.1 MVP Workflows

```text
core-specs/workflows/customer-intake-workflow.md
core-specs/workflows/trademark-application-workflow.md
core-specs/workflows/communication-review-workflow.md
```

## 3.2 Stub / Preview Workflows

```text
core-specs/workflows/office-action-response-workflow.md
core-specs/workflows/provider-routing-workflow.md
core-specs/workflows/renewal-workflow.md
core-specs/workflows/assignment-workflow.md
core-specs/workflows/evidence-review-workflow.md
```

---

# 4. Workflow File Map

| Workflow ID | Spec File | Contract File | MVP Category | Depth |
|---|---|---|---|---|
| customer-intake-workflow | core-specs/workflows/customer-intake-workflow.md | core-specs/contracts/workflows/customer-intake-workflow-contract.md | Must Build Now | Level 2/3 |
| trademark-application-workflow | core-specs/workflows/trademark-application-workflow.md | core-specs/contracts/workflows/trademark-application-workflow-contract.md | Must Build Now | Level 2/3 |
| communication-review-workflow | core-specs/workflows/communication-review-workflow.md | core-specs/contracts/workflows/communication-review-workflow-contract.md | Must Build Now | Level 2/3 |
| office-action-response-workflow | core-specs/workflows/office-action-response-workflow.md | core-specs/contracts/workflows/office-action-response-workflow-contract.md | Stub Now | Level 1/2 |
| provider-routing-workflow | core-specs/workflows/provider-routing-workflow.md | core-specs/contracts/workflows/provider-routing-workflow-contract.md | Stub Now | Level 1/2 |
| renewal-workflow | core-specs/workflows/renewal-workflow.md | core-specs/contracts/workflows/renewal-workflow-contract.md | Stub Now | Level 1/2 |
| assignment-workflow | core-specs/workflows/assignment-workflow.md | core-specs/contracts/workflows/assignment-workflow-contract.md | Stub Now | Level 1/2 |
| evidence-review-workflow | core-specs/workflows/evidence-review-workflow.md | core-specs/contracts/workflows/evidence-review-workflow-contract.md | Stub Now | Level 1/2 |

---

# 5. MVP Workflow Role

The MVP workflow set proves the first executable Core spine:

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

MVP workflows are:

```text
Customer Intake Workflow
Trademark Application Workflow
Communication Review Workflow
```

These workflows must be enough to test:

```text
customer intake
trademark application preparation
communication review
task plan generation
active Task creation through Task Service
Communication draft creation through Communication Service
Event trace through Event Service or owning service integration
Permission and Policy governance
Idempotency replay/conflict
AI Context
Human Review gates
safe Errors
Versioning
```

---

# 6. Stub Workflow Role

Stub workflows exist to preserve future architecture without forcing premature implementation.

Stub workflows are:

```text
Office Action Response Workflow
Provider Routing Workflow
Renewal Workflow
Assignment Workflow
Evidence Review Workflow
```

Stub workflow rules:

```text
schema validation is allowed
reference validation is allowed
preview-only behavior is allowed
task plan preview is allowed
AI-assisted draft or gap summary is allowed within boundaries
Human Review requirement may be declared
safe NotImplemented is allowed
production execution is not allowed
official filing/submission is not allowed
external send is not allowed
provider final selection is not allowed
AI professional certification is not allowed
```

---

# 7. Universal Workflow Rules

Every workflow spec must preserve:

```text
Workflow coordinates.
Workflow does not own domain behavior.
Workflow uses Workflow Contract.
Workflow maps to owning services.
Workflow preview has no side effects.
Workflow apply requires Idempotency.
Workflow task plan is not active Task.
Workflow does not emit Events directly.
Workflow does not send Communications directly.
Workflow does not submit official filings.
Workflow does not certify professional truth.
Workflow uses Permission and Policy.
Workflow uses safe Errors.
Workflow rejects unsupported versions.
```

---

# 8. Universal Workflow Sections

Every workflow spec should include:

```text
Purpose
Core Lock
MVP Category
Implementation Depth
Related Contracts
Related Services
Inputs
Outputs
Preview Behavior
Apply Behavior
Task Plan
Event Trace
Permission / Policy
AI Context
Human Review
Idempotency
Error / Versioning
Out of Scope
Forbidden Shortcuts
Acceptance Criteria
Revision Notes
```

---

# 9. Workflow-to-Service Ownership

## 9.1 Customer Intake Workflow

Coordinates:

```text
Customer Service
Brand Service
Matter Service
Order Service
Document Service
Task Service
Communication Service where applicable
Event Service
Permission Service
Policy Service
```

Does not own:

```text
Customer state
Brand state
Matter state
Order state
Document state
active Task state
Communication state
Event records
```

## 9.2 Trademark Application Workflow

Coordinates:

```text
Trademark Service
Brand Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
Matter Service
Order Service
Task Service
Event Service
Permission Service
Policy Service
```

Does not own:

```text
Trademark state
Classification finalization
Document storage
Evidence sufficiency conclusion
active Task state
Event records
official filing submission
```

## 9.3 Communication Review Workflow

Coordinates:

```text
Communication Service
Task Service
Event Service
Permission Service
Policy Service
Human Review Contract
```

Does not own:

```text
Communication send execution
Human Review execution
active Task state
Event records
```

---

# 10. Workflow Preview Standard

Preview must be safe.

Preview may:

```text
validate inputs
validate references
check Permission/Policy where protected
identify missing inputs
prepare workflow explanation
prepare task plan
prepare AI-assisted draft or summary
show policy omissions
show Human Review requirements
return safe warnings
```

Preview must not:

```text
mutate state
create active Tasks
create Communications
emit Events
send Communications
submit official filings
select final provider
certify professional conclusions
execute payments
```

---

# 11. Workflow Apply Standard

Apply is protected and duplicate-sensitive.

Apply must:

```text
validate request
require idempotency_key
check Permission/Policy
validate Human Review where required
coordinate owning services
create active Tasks only through Task Service
create Communication drafts only through Communication Service
record Event trace through Event Service or owning service integration
preserve version context
return safe errors
```

Apply must not:

```text
bypass owning services
bypass Permission/Policy
bypass Human Review gates
emit Events directly
create active Tasks directly
send Communications directly
submit official filings
certify professional truth
```

---

# 12. Task Plan Standard

Workflow task plans may include:

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
Task plan must preserve policy restrictions.
Task plan must use public references.
```

---

# 13. Event Trace Standard

Workflow specs must preserve Event trace.

Rules:

```text
Workflow does not emit Events directly.
Workflow response may include event_reference_ids only as trace.
event_reference_ids follow Reference Contract.
event_reference_ids are not commands.
Event visibility follows Permission and Policy.
State-changing effects are traced by owning services or Event Service.
```

---

# 14. Permission / Policy Standard

Workflow specs must state:

```text
required Permission checks
required Policy scopes
redaction behavior
non-disclosure behavior
HumanReviewRequired behavior
cross-organization restrictions where applicable
```

Rules:

```text
PermissionAllowed does not bypass Policy.
PolicyAllowed does not bypass Permission.
UnknownPermission fails closed.
UnknownPolicy fails closed where policy-controlled.
```

---

# 15. AI Standard

Workflow AI assistance is limited.

Allowed:

```text
intake summary
classification suggestion
communication draft
workflow preview explanation
task plan suggestion
evidence gap summary
routing candidate preview
audit trace summary
```

Forbidden:

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
certify official deadline
```

---

# 16. Human Review Standard

Human Review gates protected professional or external-facing workflow outcomes.

Required review gates include:

```text
external communication
classification finalization
evidence sufficiency conclusion
filing readiness confirmation
workflow apply where protected
provider final selection if routing preview appears
```

Rules:

```text
Human Review does not execute downstream action by itself.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
Owning service decides whether review satisfies the gate.
```

---

# 17. Idempotency Standard

Workflow apply must be idempotent.

Required behavior:

```text
missing idempotency_key returns IdempotencyKeyRequired
same key + same semantic apply request replays safely
same key + different semantic apply request returns IdempotencyConflict
replay creates no duplicate active Tasks
replay creates no duplicate Communications
replay creates no duplicate Events
replay does not leak policy-hidden previous result
```

---

# 18. Error / Versioning Standard

Workflow specs must require:

```text
safe Error Contract behavior
controlled error codes
no database ID leakage
no stack trace leakage
no restricted data leakage
no policy/permission internals leakage
workflow_contract_version
schema_version where applicable
VersionUnsupported for unsupported versions
historical version preservation where records are created
```

---

# 19. Workflow Test Requirements

Workflow tests must cover:

```text
preview request validation
preview response validation
apply request validation
apply response validation
preview no-side-effects
apply idempotency required
idempotency replay
idempotency conflict
PermissionDenied
PolicyRestricted
HumanReviewRequired
AI forbidden action
Task plan not active Task
Workflow no-direct-task-creation
Workflow no-direct-event-emission
Workflow no-direct-communication-send
event_reference_id trace only
safe errors
VersionUnsupported
```

---

# 20. Workflow Validation Requirements

Workflow specs must pass:

```text
core-specs/validation/workflow-contract-validation.md
core-specs/validation/permission-policy-validation.md
core-specs/validation/idempotency-event-validation.md
core-specs/validation/error-versioning-validation.md
core-specs/validation/agent-boundary-validation.md
core-specs/validation/mvp-readiness-validation.md
```

---

# 21. Codex Implementation Mapping

Workflow implementation is governed by:

```text
codex-tasks/TASK-008-workflow-validator-scaffold.md
codex-tasks/TASK-010-mvp-execution-spine.md
```

Codex must not implement workflow behavior before:

```text
TASK-001 Common Contract Foundation
TASK-002 Contract Fixture System
TASK-003 Common Contract Tests
TASK-004 Permission Policy Hooks
TASK-005 Idempotency Event Trace
TASK-006 Error Versioning Validation
TASK-007 API Validator Scaffold
TASK-009 Agent Boundary Tests
```

---

# 22. Architecture Violation Triggers

The following always violate workflow architecture:

```text
Workflow preview has side effects.
Workflow apply lacks Idempotency.
Workflow owns domain behavior.
Workflow creates active Tasks directly.
Workflow emits Events directly.
Workflow sends Communications directly.
Workflow submits official filing.
Workflow certifies deadline.
Workflow certifies registrability.
Workflow certifies evidence sufficiency.
Workflow allows AI final decision for protected action.
Workflow bypasses Permission/Policy.
Workflow accepts unsupported version silently.
Workflow returns unsafe errors.
Workflow treats event_reference_id as command.
```

---

# 23. Acceptance Criteria

This Workflow Specifications Index is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It lists all workflow specs.
[ ] It identifies MVP workflows.
[ ] It identifies Stub workflows.
[ ] It maps workflow specs to workflow contracts.
[ ] It defines universal workflow rules.
[ ] It defines universal workflow sections.
[ ] It defines workflow-to-service ownership.
[ ] It defines preview standard.
[ ] It defines apply standard.
[ ] It defines task plan standard.
[ ] It defines Event trace standard.
[ ] It defines Permission/Policy standard.
[ ] It defines AI standard.
[ ] It defines Human Review standard.
[ ] It defines Idempotency standard.
[ ] It defines Error/Versioning standard.
[ ] It defines test requirements.
[ ] It defines validation requirements.
[ ] It defines Codex implementation mapping.
[ ] It defines architecture violation triggers.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Specifications Index. Defines MVP and stub workflows, workflow file map, workflow standards, service ownership, validation requirements, Codex mapping and architecture violation triggers. |

---

**End of Workflow Specifications Index**
