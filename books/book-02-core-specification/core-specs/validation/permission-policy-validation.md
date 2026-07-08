# Permission Policy Validation

**Spec ID:** B02-VALIDATION-PERMISSION-POLICY  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/permission-policy-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Domain/Object/Service Validation:** core-specs/validation/domain-object-service-validation.md  
**Related API Validation:** core-specs/validation/api-contract-validation.md  
**Related Workflow Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Agent Validation:** core-specs/validation/agent-boundary-validation.md  
**Related Common Contracts:** core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md  
**Related Test Contract:** core-specs/contracts/tests/permission-policy-tests.md  
**Related Codex Task:** codex-tasks/TASK-004-permission-policy-hooks.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Permission Level 2/3; Policy Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate Permission and Policy governance in MarkOrbit Core.

Permission Policy Validation checks whether protected actions and policy-controlled data are correctly governed across:

```text
Services
API Contracts
Workflow Contracts
Agents
Events
Tasks
Communications
Tests
Codex implementation tasks
```

This validation ensures that MarkOrbit Core never treats access as a simple boolean and never allows implementation shortcuts that expose restricted data or execute protected actions without governance.

---

# 2. Core Lock

```text
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Permission and Policy are separate governance systems.
Permission approval is not Policy approval.
Policy allowance is not Permission approval.
Unknown Permission must fail closed.
Unknown Policy must fail closed for policy-controlled behavior.
Policy may allow, block, redact, require review or hide existence.
Human Review does not bypass Permission.
Human Review does not bypass Policy.
AI Context does not bypass Permission or Policy.
Restricted data must not leak through responses, errors, events, tasks, communications or AI output.
Codex must preserve Permission and Policy boundaries.
```

---

# 3. Validation Scope

This validation covers:

```text
Permission Context
Policy Context
Permission Service
Policy Service
protected service actions
policy-controlled data and output
API Permission/Policy hooks
Workflow Permission/Policy hooks
Agent Permission/Policy hooks
Event visibility
Task visibility and creation
Communication draft/review/send governance
cross-organization access
redaction behavior
non-disclosure behavior
Human Review interaction
AI Context interaction
Error safety
test traceability
Codex task traceability
```

This validation does not cover:

```text
full enterprise role administration UI
final policy authoring engine
complex ABAC/RBAC editor
production compliance dashboard
external identity provider integration
commercial account permission design
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
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/references.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/tests/permission-policy-tests.md
codex-tasks/TASK-004-permission-policy-hooks.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/domain-object-service-validation.md
core-specs/validation/api-contract-validation.md
core-specs/validation/workflow-contract-validation.md
core-specs/validation/agent-boundary-validation.md
```

Validation should also inspect:

```text
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/contracts/api/
core-specs/contracts/workflows/
core-specs/workflows/
core-specs/agents/
codex-tasks/
```

---

# 5. Permission / Policy Separation Checks

Validate:

```text
[ ] Permission and Policy are documented as separate systems.
[ ] Permission Service owns Permission evaluation.
[ ] Policy Service owns Policy evaluation.
[ ] Permission Context and Policy Context are separate contracts.
[ ] PermissionAllowed does not imply PolicyAllowed.
[ ] PolicyAllowed does not imply PermissionAllowed.
[ ] Protected actions require Permission.
[ ] Policy-controlled data/output requires Policy.
[ ] Both layers are evaluated where both are required.
```

Architecture violation:

```text
Permission and Policy collapsed into one access boolean.
PermissionAllowed used as enough for policy-controlled output.
PolicyAllowed used as enough for protected action.
Policy bypass added for convenience.
Permission bypass added for convenience.
```

---

# 6. Permission Decision Validation

Allowed Permission decision states:

```text
PermissionAllowed
PermissionDenied
UnknownPermission
MissingPermissionContext
```

Validate:

```text
[ ] PermissionAllowed permits only when Policy also allows or does not restrict.
[ ] PermissionDenied blocks protected actions.
[ ] UnknownPermission fails closed.
[ ] MissingPermissionContext fails closed for protected actions.
[ ] Permission decision internals are not exposed in public errors.
[ ] Permission decision references are returned only where allowed.
```

Blocked if:

```text
UnknownPermission defaults to allowed.
MissingPermissionContext defaults to allowed.
PermissionDenied still allows protected action.
```

---

# 7. Policy Decision Validation

Allowed Policy decision states:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
```

Validate:

```text
[ ] PolicyAllowed allows only if Permission also allows where protected.
[ ] PolicyRestrictedBlock blocks the action/output.
[ ] PolicyRestrictedRedact removes restricted fields.
[ ] PolicyRequiresHumanReview preserves HumanReviewRequired.
[ ] PolicyNonDisclosureNotFound hides object/source/event existence.
[ ] UnknownPolicy fails closed for policy-controlled behavior.
[ ] MissingPolicyContext fails closed for policy-controlled behavior.
[ ] Policy internals are not exposed in public errors.
```

Blocked if:

```text
UnknownPolicy defaults to allowed.
MissingPolicyContext defaults to allowed.
PolicyRestrictedRedact returns restricted fields.
PolicyNonDisclosureNotFound reveals existence.
```

---

# 8. Permission / Policy Matrix Validation

Validate the matrix:

```text
PermissionAllowed + PolicyAllowed = may proceed
PermissionDenied + PolicyAllowed = blocked
PermissionAllowed + PolicyRestrictedBlock = blocked
PermissionAllowed + PolicyRestrictedRedact = redacted or downgraded safe output
PermissionAllowed + PolicyRequiresHumanReview = HumanReviewRequired unless valid review exists
PermissionAllowed + PolicyNonDisclosureNotFound = NotFound or equivalent non-disclosure response
PermissionDenied + PolicyRestricted = blocked
UnknownPermission + AnyPolicy = blocked
AnyPermission + UnknownPolicy for policy-controlled behavior = blocked
MissingPermission + AnyPolicy for protected behavior = blocked
AnyPermission + MissingPolicy for policy-controlled behavior = blocked
```

Architecture violation:

```text
single-layer approval permits action requiring both layers
redaction treated as full allowance without disclosure
review-required treated as approval
```

---

# 9. Protected Action Coverage

Validate Permission coverage for protected MVP actions:

```text
create or update Customer
create or update Brand
create or update Trademark
create or update Matter
create or update Order
create or attach Document
create or update Evidence
create active Task
create or review Communication
workflow preview where protected
workflow apply
read restricted Event trace
use restricted sources in AI-assisted behavior
cross-organization access
```

Checks:

```text
[ ] Each protected action maps to required_permission_keys.
[ ] Each protected action checks actor_reference_id.
[ ] Each protected action checks organization_reference_id where applicable.
[ ] Each protected action fails closed when context is missing.
[ ] Each protected action has PermissionDenied negative test.
```

Blocked if:

```text
Must Build Now protected action has no Permission trace.
```

---

# 10. Policy-Controlled Data Coverage

Validate Policy coverage for:

```text
customer data
trademark data
documents
evidence
matter/order execution data
task data
communication content
event payloads
provider commercial terms
cross-organization data
AI source contents
AI output
pagination counts
search result visibility
```

Checks:

```text
[ ] Each policy-controlled field/output maps to required_policy_scopes.
[ ] Restricted fields can be redacted.
[ ] Hidden objects can be non-disclosed.
[ ] AI omissions can be disclosed.
[ ] Pagination count leakage is prevented.
```

Blocked if:

```text
policy-controlled data has no Policy trace.
```

---

# 11. Redaction Validation

When PolicyRestrictedRedact applies:

```text
restricted fields must be omitted
restricted_fields_omitted must be true
safe fields may remain
nested restricted fields must be omitted
errors must not expose redacted fields
event payloads must not expose redacted fields
AI output must disclose policy omissions
pagination/search must not leak restricted fields
```

Required tests:

```text
policy_restricted_redact_omits_fields
restricted_fields_omitted_true
nested_restricted_fields_omitted
redacted_fields_not_in_errors
redacted_fields_not_in_events
ai_policy_omissions_disclosed
```

Architecture violation:

```text
restricted field remains in response
redaction occurs silently without restricted_fields_omitted
AI output uses redacted source without disclosure
```

---

# 12. Non-Disclosure Validation

When PolicyNonDisclosureNotFound applies:

```text
object existence must not be revealed
source existence must not be revealed
event existence must not be revealed
safe NotFound or equivalent response must be returned
safe_detail must not reveal existence
pagination totals must not reveal hidden objects
idempotency replay must not leak hidden prior result
```

Required tests:

```text
policy_nondisclosure_returns_notfound
notfound_does_not_reveal_existence
pagination_does_not_reveal_hidden_count
idempotency_replay_does_not_leak_hidden_result
event_read_hides_restricted_event
```

Architecture violation:

```text
PolicyNonDisclosureNotFound returns PolicyRestricted with hidden object details.
Error message reveals hidden object exists.
Pagination count reveals hidden records.
```

---

# 13. Human Review Interaction Validation

Validate:

```text
[ ] PolicyRequiresHumanReview returns HumanReviewRequired when review is missing.
[ ] human_review_reference_id is validated where supplied.
[ ] Human Review does not bypass Permission.
[ ] Human Review does not bypass Policy.
[ ] Human Review does not execute downstream action by itself.
[ ] Owning service decides whether review satisfies action requirement.
```

Required scenarios:

```text
PermissionAllowed + PolicyRequiresHumanReview + missing review = HumanReviewRequired
PermissionDenied + valid review = PermissionDenied
PolicyRestrictedBlock + valid review = PolicyRestricted unless policy specifically allows review override
Valid review without owning service apply = no downstream execution
```

Architecture violation:

```text
Human Review record directly sends communication.
Human Review bypasses PermissionDenied.
Human Review bypasses PolicyRestrictedBlock.
```

---

# 14. AI Interaction Validation

Validate:

```text
[ ] AI Context does not imply Permission.
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] AI source use obeys Policy.
[ ] AI output obeys Policy.
[ ] policy_omissions_disclosed is true where AI omits restricted sources.
[ ] AI cannot infer hidden restricted facts as truth.
[ ] AI cannot expose hidden source existence.
[ ] AI cannot execute protected actions.
```

Required tests:

```text
agent_permission_denied_blocks
agent_policy_restricted_blocks
agent_policy_redacts_output
agent_policy_nondisclosure_hides_source
ai_policy_omissions_disclosed
ai_forbidden_action_blocked
```

Architecture violation:

```text
AI uses restricted source without Policy.
AI reveals hidden source existence.
AI output counts as approval.
AI executes protected action.
```

---

# 15. API Permission / Policy Validation

Validate API Contracts:

```text
[ ] Protected API operations require Permission Context.
[ ] Policy-controlled API responses require Policy Context.
[ ] API validators call or require Permission/Policy hooks.
[ ] API layer does not bypass Permission/Policy.
[ ] API errors do not expose permission/policy internals.
[ ] API redaction/non-disclosure behavior is documented or tested.
```

Blocked if:

```text
MVP protected API lacks Permission/Policy.
API validator defaults to allowed.
```

---

# 16. Workflow Permission / Policy Validation

Validate Workflow Contracts:

```text
[ ] Protected workflow steps require Permission.
[ ] Policy-controlled workflow outputs require Policy.
[ ] Workflow preview checks Permission/Policy where protected.
[ ] Workflow apply checks Permission/Policy.
[ ] Workflow task plans preserve policy restrictions.
[ ] Workflow cannot bypass Permission/Policy by delegating to AI.
[ ] Workflow cannot bypass Permission/Policy by using Human Review.
```

Blocked if:

```text
MVP workflow apply lacks Permission/Policy.
Workflow task plan drops policy restrictions.
```

---

# 17. Event Permission / Policy Validation

Validate Event visibility:

```text
[ ] Event read/search checks Permission/Policy.
[ ] Restricted event payload is redacted.
[ ] Hidden event returns NotFound or equivalent where required.
[ ] Event payload does not expose policy internals.
[ ] Event payload does not expose permission internals.
[ ] Event visibility applies to idempotent replay results.
```

Architecture violation:

```text
restricted Event payload leaks
hidden Event existence revealed
Event read bypasses Policy
```

---

# 18. Task Permission / Policy Validation

Validate Task behavior:

```text
[ ] Active Task creation requires Permission where protected.
[ ] Task visibility follows Policy.
[ ] Task subject references do not reveal hidden objects.
[ ] Task plan preserves policy restrictions.
[ ] Agent cannot create or complete active Task.
[ ] Workflow cannot create active Task directly.
```

Blocked if:

```text
Task visibility bypasses Policy.
Task creation bypasses Permission.
```

---

# 19. Communication Permission / Policy Validation

Validate Communication behavior:

```text
[ ] Communication draft creation requires Permission where protected.
[ ] Communication content follows Policy.
[ ] Restricted content is redacted.
[ ] External send requires Human Review.
[ ] AI draft preserves policy omissions.
[ ] Communication Agent cannot send.
[ ] Workflow cannot send Communication directly.
```

Architecture violation:

```text
restricted content appears in communication draft
external send bypasses Human Review
AI sends communication
workflow sends communication directly
```

---

# 20. Cross-Organization Validation

Validate:

```text
[ ] Cross-organization access requires explicit Policy.
[ ] Partner / Provider / Service Network access requires relationship Policy.
[ ] Customer data visibility is restricted by Policy.
[ ] Provider commercial terms are restricted by Policy.
[ ] PolicyNonDisclosureNotFound hides cross-organization object existence where required.
```

Blocked if:

```text
PermissionAllowed without cross-organization Policy grants access.
```

---

# 21. Error Safety Validation

Validate:

```text
[ ] PermissionDenied error is safe.
[ ] PolicyRestricted error is safe.
[ ] HumanReviewRequired error is safe.
[ ] NotFound substitution is safe.
[ ] Errors do not expose permission internals.
[ ] Errors do not expose policy internals.
[ ] Errors do not expose restricted fields.
[ ] Errors preserve correlation_id.
```

Architecture violation:

```text
error reveals policy rule internals
error reveals permission graph
error reveals restricted data
error reveals hidden object existence
```

---

# 22. Test Traceability Validation

Validate:

```text
[ ] permission-policy-tests.md exists.
[ ] TASK-004 exists.
[ ] PermissionAllowed tests exist.
[ ] PermissionDenied tests exist.
[ ] UnknownPermission fail-closed tests exist.
[ ] MissingPermissionContext tests exist.
[ ] PolicyAllowed tests exist.
[ ] PolicyRestrictedBlock tests exist.
[ ] PolicyRestrictedRedact tests exist.
[ ] PolicyRequiresHumanReview tests exist.
[ ] PolicyNonDisclosureNotFound tests exist.
[ ] UnknownPolicy fail-closed tests exist.
[ ] MissingPolicyContext tests exist.
[ ] AI policy omission tests exist.
[ ] Human Review interaction tests exist.
[ ] Cross-organization restriction tests exist.
[ ] Event visibility tests exist.
```

Blocked if:

```text
Permission/Policy tests missing.
No negative tests for PermissionDenied or PolicyRestricted.
No fail-closed tests for UnknownPermission/UnknownPolicy.
```

---

# 23. Validation Procedure

Perform validation in this order:

```text
1. Confirm Permission/Policy source files exist.
2. Confirm Permission/Policy separation.
3. Validate Permission decision states.
4. Validate Policy decision states.
5. Validate Permission/Policy matrix.
6. Validate protected action coverage.
7. Validate policy-controlled data coverage.
8. Validate redaction behavior.
9. Validate non-disclosure behavior.
10. Validate Human Review interaction.
11. Validate AI interaction.
12. Validate API Permission/Policy.
13. Validate Workflow Permission/Policy.
14. Validate Event Permission/Policy.
15. Validate Task Permission/Policy.
16. Validate Communication Permission/Policy.
17. Validate cross-organization behavior.
18. Validate error safety.
19. Validate test traceability.
20. Classify findings.
21. Produce validation report.
```

---

# 24. Finding Classification

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
Blocked = Must Build Now protected behavior lacks Permission/Policy mapping or tests.
Architecture Violation = Permission/Policy bypass or restricted data leak.
Warning = future/stub governance incomplete but safe.
Out of Scope = valid but beyond MVP.
Deferred = later policy engine feature.
Pass = sufficient for current depth.
```

---

# 25. Required Evidence

Every finding must include:

```text
governance area
action or output
source file
decision state
affected domain/service/API/workflow/agent
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Communication draft returns restricted customer note after PolicyRestrictedRedact.
Status: Architecture Violation
Area: Communication / Policy
Required Fix: Redact restricted field and set restricted_fields_omitted.
Codex Impact: Block TASK-004, TASK-007, TASK-008 and TASK-010.
```

---

# 26. Architecture Violation Triggers

The following always fail validation:

```text
Permission defaults to allowed.
Policy defaults to allowed.
Permission and Policy are collapsed into one boolean.
PermissionAllowed bypasses PolicyRestricted.
PolicyAllowed bypasses PermissionDenied.
UnknownPermission allows protected action.
UnknownPolicy allows policy-controlled output.
Restricted fields leak after PolicyRestrictedRedact.
PolicyNonDisclosureNotFound reveals object existence.
Human Review bypasses Permission.
Human Review bypasses Policy.
AI Context bypasses Permission or Policy.
Agent capability implies Permission.
Event read bypasses Policy.
Task visibility bypasses Policy.
Communication content bypasses Policy.
Cross-organization access bypasses Policy.
Permission/Policy internals leak in errors.
```

---

# 27. Acceptance Criteria

Permission Policy Validation passes only if:

```text
[ ] Required source files exist.
[ ] Permission and Policy remain separate.
[ ] Permission Service ownership is clear.
[ ] Policy Service ownership is clear.
[ ] Permission decision states are validated.
[ ] Policy decision states are validated.
[ ] Permission/Policy matrix is enforced.
[ ] Protected MVP actions map to Permission.
[ ] Policy-controlled data/output maps to Policy.
[ ] Redaction behavior is safe and disclosed.
[ ] Non-disclosure behavior hides existence.
[ ] Human Review interaction is safe.
[ ] AI interaction is safe.
[ ] API Permission/Policy boundaries are mapped.
[ ] Workflow Permission/Policy boundaries are mapped.
[ ] Event visibility is governed.
[ ] Task visibility/creation is governed.
[ ] Communication content/send is governed.
[ ] Cross-organization access is governed.
[ ] Error safety is preserved.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now protected behavior.
```

---

# 28. Validation Report Template

```text
Validation: Permission Policy
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Permission / Policy Governance

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Area:
- Action / Output:
- Decision State:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 29. Codex Usage

Codex must use this validation:

```text
before implementing TASK-004-permission-policy-hooks
before implementing API validators
before implementing workflow validators
before implementing agent boundary tests
before implementing MVP execution spine
after modifying Permission/Policy contracts
during PR review
```

Codex must not:

```text
default Permission to allowed
default Policy to allowed
merge Permission and Policy
skip redaction tests
skip non-disclosure tests
skip Human Review interaction tests
skip AI policy omission tests
skip cross-organization restriction tests
expose Permission/Policy internals
```

---

# 30. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Permission Policy Validation. Defines Permission/Policy separation, decision states, matrix, protected action coverage, policy-controlled data coverage, redaction, non-disclosure, Human Review, AI, API, Workflow, Event, Task, Communication, cross-organization and error safety validation. |

---

**End of Permission Policy Validation**
