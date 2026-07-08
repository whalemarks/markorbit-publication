# Workflow Contract Validation

**Spec ID:** B02-VALIDATION-WORKFLOW-CONTRACT  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/workflow-contract-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Domain/Object/Service Validation:** core-specs/validation/domain-object-service-validation.md  
**Related API Validation:** core-specs/validation/api-contract-validation.md  
**Related Workflow Index:** core-specs/workflows/index.md  
**Related Workflow Contract Index:** core-specs/contracts/workflows/index.md  
**Related Test Contract:** core-specs/contracts/tests/workflow-contract-tests.md  
**Related Codex Task:** codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** MVP Workflows Level 2/3; Stub Workflows Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate MarkOrbit Core Workflow Contracts.

Workflow Contract Validation checks whether each workflow is correctly constrained, traceable, governed and implementation-ready.

It ensures that workflows:

```text
coordinate execution
do not own domain behavior
do not mutate state directly
do not create active Tasks directly
do not emit Events directly
do not send Communications directly
do not certify professional truth
use Workflow Contracts
use Common Contracts
use owning services
enforce Permission and Policy
require Idempotency for apply
preserve Human Review gates
preserve AI boundaries
return safe Errors
fail closed on unsupported versions
```

This validation is required before implementing workflow validators or the MVP execution spine.

---

# 2. Core Lock

```text
Workflows coordinate execution.
Workflow Contracts constrain execution.
Owning services own behavior.
Workflow layer does not own domain behavior.
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
Codex implements workflow validators from Workflow Contracts.
Codex does not build a full workflow engine in MVP.
```

---

# 3. Validation Scope

This validation covers the workflow specifications and workflow contracts for:

## 3.1 MVP Workflows

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

These require Level 2 validator coverage and selected Level 3 enforcement for protected gates.

## 3.2 Stub Workflows

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

These require safe Level 1/2 preview-only or validation-only scaffolds.

Validation covers:

```text
workflow file existence
workflow contract file existence
workflow-to-contract mapping
workflow-to-service mapping
preview behavior
apply behavior
task plan behavior
Permission/Policy coverage
Idempotency coverage
Event trace behavior
AI Context coverage
Human Review coverage
safe errors
versioning
test traceability
Codex task traceability
```

---

# 4. Required Source Files

Validation must inspect:

```text
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/workflows/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/common/index.md
core-specs/contracts/tests/workflow-contract-tests.md
codex-tasks/TASK-008-workflow-validator-scaffold.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/domain-object-service-validation.md
core-specs/validation/api-contract-validation.md
```

Validation must also inspect workflow specs:

```text
core-specs/workflows/customer-intake-workflow.md
core-specs/workflows/trademark-application-workflow.md
core-specs/workflows/communication-review-workflow.md
core-specs/workflows/office-action-response-workflow.md
core-specs/workflows/provider-routing-workflow.md
core-specs/workflows/renewal-workflow.md
core-specs/workflows/assignment-workflow.md
core-specs/workflows/evidence-review-workflow.md
```

Validation must also inspect workflow contract specs:

```text
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
core-specs/contracts/workflows/office-action-response-workflow-contract.md
core-specs/contracts/workflows/provider-routing-workflow-contract.md
core-specs/contracts/workflows/renewal-workflow-contract.md
core-specs/contracts/workflows/assignment-workflow-contract.md
core-specs/contracts/workflows/evidence-review-workflow-contract.md
```

---

# 5. Workflow File Existence Checks

Validate:

```text
[ ] Workflow index exists.
[ ] Workflow Contract index exists.
[ ] MVP workflow specs exist.
[ ] MVP workflow contracts exist.
[ ] Stub workflow specs exist or are explicitly deferred.
[ ] Stub workflow contracts exist or are explicitly deferred.
[ ] Workflow naming is consistent.
[ ] Each workflow spec maps to exactly one workflow contract.
[ ] No workflow contract exists without index entry.
[ ] No MVP workflow is missing contract mapping.
```

Blocked if:

```text
MVP workflow spec missing.
MVP workflow contract missing.
Workflow index omits MVP workflow.
Workflow contract index omits MVP workflow contract.
```

---

# 6. MVP Workflow Depth Classification

Validate depth according to the Implementation Depth Matrix.

## 6.1 MVP Workflows — Level 2/3

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Required:

```text
preview request validation
preview response validation
apply request validation
apply response validation
workflow contract version validation
reference validation
Permission/Policy validation
Human Review gates
AI Context where applicable
Idempotency for apply
Task plan validation
Event trace reference validation
safe Errors
Versioning
negative tests
```

## 6.2 Stub Workflows — Level 1/2

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

Required:

```text
schema validation
reference validation
preview-only or validation-only behavior
safe not-implemented where apply is out of scope
Permission/Policy hooks where protected
Human Review requirement where applicable
safe Errors
unsupported version failure
no production side effects
```

Architecture violation:

```text
Stub workflow performs production official filing.
Provider Routing Workflow selects provider finally in MVP.
Renewal Workflow executes official renewal filing in MVP.
Assignment Workflow executes official recordal filing in MVP.
Evidence Review Workflow certifies final sufficiency by AI.
Office Action Workflow submits official response in MVP.
```

---

# 7. Workflow-to-Contract Mapping Checks

Validate:

```text
[ ] Each workflow spec has a matching workflow contract.
[ ] Each workflow contract has a workflow_id.
[ ] Each workflow contract has workflow_contract_version.
[ ] Each workflow contract defines preview behavior.
[ ] Each workflow contract defines apply behavior or explicitly marks apply out of scope.
[ ] Each workflow contract defines inputs and outputs.
[ ] Each workflow contract defines required Common Contracts.
[ ] Each workflow contract defines failure conditions.
[ ] Each workflow contract maps to tests.
```

Blocked if:

```text
MVP workflow has no contract.
MVP workflow contract has no version.
MVP workflow contract has no preview/apply boundary.
```

---

# 8. Workflow-to-Service Mapping Checks

Validate that workflows coordinate owning services.

Required MVP mappings:

```text
Customer Intake Workflow → Customer Service; Brand Service; Matter Service; Order Service; Document Service; Task Service; Event Service; Permission Service; Policy Service
Trademark Application Workflow → Trademark Service; Brand Service; Jurisdiction Service; Classification Service; Document Service; Evidence Service; Matter Service; Order Service; Task Service; Event Service; Permission Service; Policy Service
Communication Review Workflow → Communication Service; Human Review Contract; Task Service; Event Service; Permission Service; Policy Service
```

Checks:

```text
[ ] Workflow maps each step to owning service.
[ ] Workflow does not own domain behavior.
[ ] Workflow does not mutate objects directly.
[ ] Workflow does not create active Tasks directly.
[ ] Workflow does not emit Events directly.
[ ] Workflow does not send Communications directly.
[ ] Workflow does not bypass Permission/Policy.
```

Architecture violation:

```text
workflow creates Customer directly without Customer Service
workflow creates active Task without Task Service
workflow emits Event without Event Service / owning service trace
workflow sends Communication without Communication Service
```

---

# 9. Preview Behavior Checks

Workflow preview must be side-effect free.

Validate:

```text
[ ] Preview validates inputs.
[ ] Preview validates references.
[ ] Preview validates Permission/Policy where protected.
[ ] Preview validates AI Context where AI-assisted.
[ ] Preview validates Human Review requirements where applicable.
[ ] Preview may return task plan.
[ ] Preview may return missing inputs.
[ ] Preview may return policy omissions.
[ ] Preview may return safe warnings.
[ ] Preview does not mutate state.
[ ] Preview does not create active Tasks.
[ ] Preview does not create Communications.
[ ] Preview does not emit Events.
[ ] Preview does not submit official filings.
```

Architecture violation:

```text
preview creates Matter
preview creates Order
preview creates active Task
preview sends Communication
preview emits Event
preview commits provider selection
```

---

# 10. Apply Behavior Checks

Workflow apply is protected and duplicate-sensitive.

Validate:

```text
[ ] Apply requires idempotency_key.
[ ] Apply validates same semantic request on replay.
[ ] Apply conflicts safely on same key + different semantic request.
[ ] Apply validates Permission/Policy.
[ ] Apply validates Human Review where required.
[ ] Apply coordinates owning services.
[ ] Apply may request Task Service to create active Tasks.
[ ] Apply may request Communication Service to create draft Communication.
[ ] Apply may result in Event trace through owning services/Event Service.
[ ] Apply returns safe response.
[ ] Apply preserves version context.
```

Apply must not:

```text
submit official filing
send external communication
certify registrability
certify deadline
certify evidence sufficiency
select provider finally by AI
emit Events directly
create active Tasks directly
```

Blocked if:

```text
MVP workflow apply has no Idempotency requirement.
MVP workflow apply bypasses Permission/Policy.
MVP workflow apply lacks owning service mapping.
```

---

# 11. Task Plan Checks

Workflows may prepare Task plans.

Validate:

```text
[ ] Task plan is clearly marked as plan.
[ ] Task plan is not active Task.
[ ] Task plan fields are defined.
[ ] Task plan references subject objects by public reference.
[ ] Task plan indicates required owner role or review requirement.
[ ] Task plan preserves policy restrictions.
[ ] Task plan is converted to active Task only by Task Service.
```

Architecture violation:

```text
workflow task plan is treated as active Task
workflow directly creates task_reference_id as active Task
agent-created task plan becomes active Task without Task Service
```

---

# 12. Communication Checks

Communication Review Workflow and any communication-related workflow must preserve Communication Service ownership.

Validate:

```text
[ ] Workflow may prepare or review Communication draft.
[ ] Communication draft is owned by Communication Service.
[ ] External send requires Human Review.
[ ] AI draft is marked draft/suggestion/non-final.
[ ] Policy omissions are disclosed.
[ ] Restricted content is redacted.
[ ] Workflow does not send Communication directly.
```

Architecture violation:

```text
workflow sends email
workflow marks communication as approved without review
AI draft becomes sent output
policy redaction bypassed
```

---

# 13. Permission / Policy Checks

Validate:

```text
[ ] Protected workflow steps require Permission.
[ ] Policy-controlled workflow output requires Policy.
[ ] UnknownPermission fails closed.
[ ] UnknownPolicy fails closed where policy-controlled.
[ ] PolicyRestrictedBlock blocks workflow step.
[ ] PolicyRestrictedRedact redacts output and sets restricted_fields_omitted.
[ ] PolicyRequiresHumanReview preserves HumanReviewRequired.
[ ] PolicyNonDisclosureNotFound hides object existence where required.
```

Required workflow-protected areas:

```text
customer intake
trademark application preparation
classification suggestion/finalization
document/evidence access
matter/order creation
task creation
communication draft/review
event trace access
AI-assisted source use
cross-organization/provider visibility
```

---

# 14. Idempotency Checks

Validate apply operations.

Required:

```text
[ ] workflow apply requires idempotency_key.
[ ] missing idempotency_key returns IdempotencyKeyRequired.
[ ] same key + same semantic apply request replays safely.
[ ] same key + different semantic apply request returns IdempotencyConflict.
[ ] replay does not duplicate Tasks.
[ ] replay does not duplicate Communications.
[ ] replay does not duplicate Events.
[ ] replay does not leak policy-hidden prior result.
```

Preview operations:

```text
Preview should not require idempotency if it has no side effects.
Preview must remain side-effect free.
```

---

# 15. Event Trace Checks

Validate:

```text
[ ] Workflow layer does not emit Events directly.
[ ] Workflow responses may include event_reference_ids only as trace.
[ ] event_reference_ids follow Reference Contract.
[ ] event_reference_ids are not commands.
[ ] Event visibility follows Permission/Policy.
[ ] Workflow-related Events are emitted by owning service or Event Service integration.
```

Required tests:

```text
workflow_layer_does_not_emit_events_directly
workflow_event_reference_not_command
```

Architecture violation:

```text
workflow emits workflow-applied Event directly without Event Service rule
event_reference_id triggers task completion
event_reference_id sends communication
```

---

# 16. AI Context Checks

Where workflow output is AI-assisted, validate:

```text
[ ] AI Context is required.
[ ] capability_scope is valid.
[ ] source_scope is valid.
[ ] policy_omissions_disclosed is true where restricted sources are omitted.
[ ] AI output is draft/suggestion/non-final.
[ ] AI output does not approve, send, select, submit, certify, complete or mutate protected state.
```

Applies to:

```text
intake summary
classification suggestion
communication draft
workflow preview explanation
task plan suggestion
evidence gap summary
routing candidate preview
```

Architecture violation:

```text
AI finalizes classification
AI certifies evidence sufficiency
AI certifies registrability
AI applies workflow
AI sends communication
AI submits official filing
```

---

# 17. Human Review Checks

Validate:

```text
[ ] HumanReviewRequired is returned where review is missing.
[ ] human_review_reference_id is validated where supplied.
[ ] Human Review does not execute downstream action by itself.
[ ] Human Review does not bypass Permission.
[ ] Human Review does not bypass Policy.
[ ] Owning service decides whether review satisfies transition requirement.
```

Required gates:

```text
external communication
classification finalization
evidence sufficiency conclusion
filing readiness confirmation
workflow apply where protected
provider final selection if routing preview is exposed
```

---

# 18. Error / Versioning Checks

Validate:

```text
[ ] Workflow failures use Error Contract.
[ ] Errors do not expose stack traces.
[ ] Errors do not expose database IDs.
[ ] Errors do not expose restricted data.
[ ] Errors do not expose policy/permission internals.
[ ] Errors preserve correlation_id.
[ ] workflow_contract_version is required.
[ ] schema_version is required where applicable.
[ ] unsupported workflow contract versions return VersionUnsupported.
[ ] historical workflow application versions are preserved where records are created.
```

---

# 19. Test Traceability Checks

Validate:

```text
[ ] Workflow Contract maps to workflow-contract-tests.md.
[ ] MVP workflow validators map to TASK-008.
[ ] MVP execution behavior maps to TASK-010.
[ ] Preview no-side-effect test exists.
[ ] Apply idempotency test exists.
[ ] PermissionDenied test exists.
[ ] PolicyRestricted test exists.
[ ] HumanReviewRequired test exists.
[ ] AI forbidden action test exists.
[ ] Task plan not active Task test exists.
[ ] Workflow no-direct-event-emission test exists.
[ ] Workflow no-direct-task-creation test exists.
[ ] VersionUnsupported test exists.
[ ] Safe error test exists.
```

Blocked if:

```text
MVP workflow lacks test mapping.
MVP workflow apply lacks idempotency tests.
MVP workflow has no negative governance tests.
```

---

# 20. Validation Procedure

Perform validation in this order:

```text
1. Confirm workflow index exists.
2. Confirm workflow contract index exists.
3. Confirm MVP workflow specs and contracts exist.
4. Confirm stub workflow specs/contracts exist or are safely deferred.
5. Validate workflow depth classification.
6. Validate workflow-to-contract mapping.
7. Validate workflow-to-service mapping.
8. Validate preview behavior.
9. Validate apply behavior.
10. Validate task plan behavior.
11. Validate Communication behavior.
12. Validate Permission/Policy coverage.
13. Validate Idempotency coverage.
14. Validate Event trace boundary.
15. Validate AI Context boundary.
16. Validate Human Review gates.
17. Validate Error/Versioning.
18. Validate test traceability.
19. Classify findings.
20. Produce validation report.
```

---

# 21. Finding Classification

Use:

```text
Pass
Warning
Blocked
Architecture Violation
Out of Scope
Deferred
```

Classification rules:

```text
Blocked = MVP workflow missing contract, required mapping or required governance.
Architecture Violation = workflow boundary breach or unsafe execution.
Warning = stub/future workflow incomplete but safe.
Out of Scope = valid but beyond MVP.
Deferred = later workflow intentionally postponed.
Pass = sufficient for current depth.
```

---

# 22. Required Evidence

Every finding must include:

```text
workflow
workflow contract
operation or step
source file
missing or inconsistent rule
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Trademark Application Workflow apply lacks idempotency_key requirement.
Status: Blocked
Workflow: trademark-application-workflow
Operation: apply
Required Fix: Add Idempotency requirement and test.
Codex Impact: Block TASK-008 and TASK-010.
```

---

# 23. Architecture Violation Triggers

The following always fail validation:

```text
Workflow preview has side effects.
Workflow apply lacks Idempotency.
Workflow owns domain behavior.
Workflow creates active Tasks directly.
Workflow emits Events directly.
Workflow sends Communication directly.
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

# 24. Acceptance Criteria

Workflow Contract Validation passes only if:

```text
[ ] Required source files exist.
[ ] MVP workflow specs exist.
[ ] MVP workflow contracts exist.
[ ] Stub workflows are safely scoped or deferred.
[ ] Each workflow maps to a workflow contract.
[ ] Each MVP workflow maps to owning services.
[ ] Preview behavior is side-effect free.
[ ] Apply behavior requires Idempotency.
[ ] Workflow task plans are not active Tasks.
[ ] Active Tasks are created only by Task Service.
[ ] Communications are owned by Communication Service.
[ ] Workflow layer does not emit Events directly.
[ ] Event references are trace only.
[ ] Permission/Policy governance is mapped.
[ ] AI Context boundaries are mapped.
[ ] Human Review gates are preserved.
[ ] Safe Error behavior is defined.
[ ] Unsupported workflow versions fail closed.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in MVP workflows.
```

---

# 25. Validation Report Template

```text
Validation: Workflow Contract
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Workflow Specs and Workflow Contracts

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Workflow:
- Workflow Contract:
- Operation / Step:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 26. Codex Usage

Codex must use this validation:

```text
before implementing TASK-008-workflow-validator-scaffold
before implementing workflow parts of TASK-010
after modifying workflow specs
after modifying workflow contracts
during PR review
```

Codex must not:

```text
build full workflow engine in MVP
treat workflow preview as apply
mutate domain state in workflow validators
create active Tasks from workflow layer
emit Events from workflow layer
send Communications from workflow layer
skip Permission/Policy hooks
skip Idempotency for apply
skip Human Review gates
skip AI forbidden-action checks
skip safe errors
skip unsupported version behavior
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contract Validation. Defines workflow file existence, MVP/stub depth, workflow-contract/service mapping, preview/apply behavior, Task plan, Communication, Permission/Policy, Idempotency, Event, AI, Human Review, Error/Versioning and test traceability validation. |

---

**End of Workflow Contract Validation**
