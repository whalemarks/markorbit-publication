# MVP Readiness Validation

**Spec ID:** B02-VALIDATION-MVP-READINESS  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/mvp-readiness-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Codex Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Codex Tasks:** codex-tasks/TASK-001 through codex-tasks/TASK-010  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Level 2/3 — MVP Entry Gate  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines the MVP readiness gate for Book 02 — MarkOrbit Core Specification.

It determines whether the Core specification package is ready for Codex implementation of the first executable MVP spine.

This validation answers:

```text
Are the required architecture files present?
Is MVP scope clear?
Is implementation depth clear?
Are Core boundaries protected?
Are Codex tasks sequenced?
Are validation specs complete?
Are tests mapped?
Are Must Build Now areas traceable?
Are Stub Now areas safe?
Are Document Only / Defer / Never items blocked from accidental implementation?
```

MVP readiness is not the same as product readiness.

MVP readiness means:

```text
Core can safely enter scoped implementation without architecture drift.
```

---

# 2. Core Lock

```text
MVP readiness is an architecture gate.
MVP readiness does not expand MVP scope.
MVP readiness does not authorize full platform implementation.
MVP readiness requires traceability.
MVP readiness requires implementation depth control.
MVP readiness requires validation coverage.
MVP readiness requires Codex task discipline.
MVP readiness requires negative tests.
No Architecture Violation may remain.
No Blocked Must Build Now finding may remain.
Warnings may proceed only if documented and outside MVP blocking scope.
Codex must not begin MVP execution spine until this gate passes.
```

---

# 3. Validation Scope

This validation covers:

```text
architecture baseline
traceability baseline
MVP scope
implementation depth
contract readiness
API readiness
workflow readiness
agent boundary readiness
Permission/Policy readiness
Idempotency/Event readiness
Error/Versioning readiness
fixture readiness
test readiness
Codex task readiness
out-of-scope protection
MVP execution spine readiness
```

This validation does not cover:

```text
full product UI readiness
production infrastructure readiness
commercial launch readiness
external official filing readiness
payment readiness
provider marketplace readiness
full workflow engine readiness
full policy engine readiness
full agent runtime readiness
```

---

# 4. Required Source Files

MVP readiness validation must inspect:

```text
core-specs/reviews/book-02-core-review.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/contracts/README.md
core-specs/contracts/MANIFEST.md
core-specs/contracts/index.md
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/domain-object-service-validation.md
core-specs/validation/api-contract-validation.md
core-specs/validation/workflow-contract-validation.md
core-specs/validation/agent-boundary-validation.md
core-specs/validation/permission-policy-validation.md
core-specs/validation/idempotency-event-validation.md
core-specs/validation/error-versioning-validation.md
core-specs/validation/mvp-readiness-validation.md
```

It must also inspect:

```text
codex-tasks/TASK-001-common-contract-foundation.md
codex-tasks/TASK-002-contract-fixture-system.md
codex-tasks/TASK-003-common-contract-tests.md
codex-tasks/TASK-004-permission-policy-hooks.md
codex-tasks/TASK-005-idempotency-event-trace.md
codex-tasks/TASK-006-error-versioning-validation.md
codex-tasks/TASK-007-api-validator-scaffold.md
codex-tasks/TASK-008-workflow-validator-scaffold.md
codex-tasks/TASK-009-agent-boundary-tests.md
codex-tasks/TASK-010-mvp-execution-spine.md
```

---

# 5. MVP Readiness Gate Summary

MVP readiness requires all of the following:

```text
[ ] Architecture baseline exists.
[ ] Traceability baseline exists.
[ ] MVP Cut exists.
[ ] Implementation Depth Matrix exists.
[ ] Developer Start Here exists.
[ ] Codex Task Index exists.
[ ] TASK-001 through TASK-010 exist.
[ ] Validation Index exists.
[ ] P0 validation files exist.
[ ] Common Contracts are indexed.
[ ] API Contracts are indexed.
[ ] Workflow Contracts are indexed.
[ ] Test Contracts are indexed.
[ ] Must Build Now domains are traceable.
[ ] MVP workflows are traceable.
[ ] Stub Now items are safe.
[ ] Never in MVP items are explicitly blocked.
[ ] No Architecture Violation exists.
[ ] No Blocked Must Build Now finding exists.
```

---

# 6. Architecture Baseline Readiness

Validate:

```text
[ ] book-02-core-review.md exists.
[ ] Architecture review identifies strengths, risks and implementation readiness.
[ ] Architecture consistency validation exists.
[ ] Canonical architecture flow is preserved.
[ ] Core responsibility boundary is preserved.
[ ] 26-domain baseline is preserved.
[ ] Layer responsibility rules are preserved.
[ ] Codex is positioned as implementer, not architect.
```

Blocked if:

```text
architecture baseline missing
canonical flow missing
Core/Product/Workflow/Agent boundaries unclear
Codex allowed to define architecture
```

---

# 7. Traceability Readiness

Validate:

```text
[ ] TRACEABILITY.md exists.
[ ] traceability-validation.md exists.
[ ] 26 domains are mapped.
[ ] Must Build Now domains are mapped to object/service/API/test expectations.
[ ] MVP workflows are mapped.
[ ] Common/API/Workflow/Test contracts are mapped.
[ ] Agent specs are mapped.
[ ] Codex tasks are mapped.
[ ] Known traceability gaps are documented.
```

Blocked if:

```text
Must Build Now domain has no trace.
MVP workflow has no trace.
Protected behavior has no Permission/Policy trace.
Duplicate-sensitive behavior has no Idempotency trace.
State-changing behavior has no Event trace.
```

---

# 8. MVP Scope Readiness

Validate:

```text
[ ] mvp-cut-v0.1.md exists.
[ ] Must Build Now items are defined.
[ ] Stub Now items are defined.
[ ] Document Only items are defined.
[ ] Defer items are defined.
[ ] Never in MVP items are defined.
[ ] MVP execution spine is defined.
[ ] MVP workflows are defined.
[ ] MVP API cut is defined.
[ ] Codex task cut is defined.
```

Blocked if:

```text
MVP scope is unclear.
Must Build Now not defined.
Never in MVP not defined.
Full platform implementation not explicitly blocked.
```

---

# 9. Implementation Depth Readiness

Validate:

```text
[ ] implementation-depth-matrix.md exists.
[ ] Level 0–4 definitions exist.
[ ] MVP capability depth matrix exists.
[ ] Common Contract depth is defined.
[ ] API depth is defined.
[ ] Workflow depth is defined.
[ ] Agent depth is defined.
[ ] Permission/Policy depth is defined.
[ ] Idempotency/Event depth is defined.
[ ] Error/Versioning depth is defined.
[ ] Codex depth rules are defined.
```

Blocked if:

```text
implementation depth missing
Codex can overbuild stubs
Codex can underbuild safety primitives
MVP depth for Permission/Policy or Idempotency/Event is unclear
```

---

# 10. Contract Readiness

Validate:

```text
[ ] contracts/README.md exists.
[ ] contracts/MANIFEST.md exists.
[ ] contracts/index.md exists.
[ ] Common Contract index exists.
[ ] API Contract index exists.
[ ] Workflow Contract index exists.
[ ] Test Contract index exists.
[ ] Contract naming is consistent.
[ ] contracts/test vs contracts/tests naming is normalized or explicitly resolved.
```

Common Contracts required:

```text
references
errors
pagination
audit-context
ai-context
human-review
permission-context
policy-context
idempotency
versioning
```

Blocked if:

```text
Common Contract index missing.
API Contract index missing.
Workflow Contract index missing.
Test Contract index missing.
Required Common Contract missing.
contracts/test and contracts/tests conflict unresolved.
```

---

# 11. API Readiness

Validate:

```text
[ ] api-contract-validation.md exists.
[ ] API Contract index lists all 26 API Contracts.
[ ] MVP API Contracts exist.
[ ] Stub API Contracts exist or are safely documented.
[ ] MVP APIs map to owning services.
[ ] MVP APIs require Permission/Policy where protected.
[ ] MVP create/apply APIs require Idempotency.
[ ] MVP APIs use safe Errors.
[ ] MVP APIs use Versioning.
[ ] API validator Codex task exists.
```

Blocked if:

```text
MVP API Contract missing.
MVP API has no owning service mapping.
MVP protected API lacks Permission/Policy.
MVP duplicate-sensitive API lacks Idempotency.
```

---

# 12. Workflow Readiness

Validate:

```text
[ ] workflow-contract-validation.md exists.
[ ] Workflow index exists.
[ ] Workflow Contract index exists.
[ ] MVP workflow specs exist.
[ ] MVP workflow contracts exist.
[ ] Stub workflows are safe or deferred.
[ ] Workflow preview is side-effect free.
[ ] Workflow apply requires Idempotency.
[ ] Workflow task plans are not active Tasks.
[ ] Workflow layer does not emit Events directly.
[ ] Workflow layer does not send Communications directly.
[ ] Workflow validator Codex task exists.
```

MVP workflows:

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Blocked if:

```text
MVP workflow spec missing.
MVP workflow contract missing.
Workflow apply lacks Idempotency.
Workflow creates active Tasks directly.
Workflow emits Events directly.
```

---

# 13. Domain Object Service Readiness

Validate:

```text
[ ] domain-object-service-validation.md exists.
[ ] 26-domain baseline is preserved.
[ ] Must Build Now domains have owning service mapping.
[ ] Must Build Now domains have API/test trace.
[ ] Stub Now domains have safe owners.
[ ] Objects describe state only.
[ ] Services own behavior.
[ ] Lifecycle transitions are service-owned.
[ ] Cross-domain relationships use public references.
```

Blocked if:

```text
Must Build Now domain has no owning service.
Object owns behavior.
API or Workflow owns domain behavior.
Service ownership is ambiguous.
```

---

# 14. Permission / Policy Readiness

Validate:

```text
[ ] permission-policy-validation.md exists.
[ ] Permission Context exists.
[ ] Policy Context exists.
[ ] Permission Service ownership is defined.
[ ] Policy Service ownership is defined.
[ ] Permission and Policy remain separate.
[ ] UnknownPermission fails closed.
[ ] UnknownPolicy fails closed.
[ ] Redaction is defined.
[ ] Non-disclosure is defined.
[ ] Human Review interaction is defined.
[ ] AI interaction is defined.
[ ] TASK-004 exists.
```

Blocked if:

```text
Permission/Policy collapsed into one boolean.
Permission defaults to allowed.
Policy defaults to allowed.
Protected MVP behavior lacks Permission/Policy.
Restricted data may leak.
```

---

# 15. Idempotency / Event Readiness

Validate:

```text
[ ] idempotency-event-validation.md exists.
[ ] Idempotency Contract exists.
[ ] Audit Context exists.
[ ] Event API Contract exists.
[ ] Event Object / Event Service mapping exists or is explicitly traceable.
[ ] Duplicate-sensitive operations require idempotency_key.
[ ] Safe replay is defined.
[ ] Conflict behavior is defined.
[ ] Event record shape is defined.
[ ] Event ownership is defined.
[ ] Event references are trace only.
[ ] Event visibility follows Permission/Policy.
[ ] TASK-005 exists.
```

Blocked if:

```text
MVP duplicate-sensitive action lacks Idempotency.
Event reference can trigger command.
API/Workflow/Agent emits Events directly.
Event visibility lacks Policy.
```

---

# 16. Error / Versioning Readiness

Validate:

```text
[ ] error-versioning-validation.md exists.
[ ] Error Contract exists.
[ ] Versioning Contract exists.
[ ] Required controlled error codes exist.
[ ] Safe error shape is defined.
[ ] Leakage prevention is defined.
[ ] Unsupported version failure is defined.
[ ] Deprecated version behavior is safe.
[ ] Historical version preservation is defined.
[ ] TASK-006 exists.
```

Blocked if:

```text
raw errors allowed
stack traces can leak
database IDs can leak
restricted data can leak
unsupported versions silently accepted
historical versions silently rewritten
```

---

# 17. Agent Boundary Readiness

Validate:

```text
[ ] agent-boundary-validation.md exists.
[ ] AI Agent Governance exists.
[ ] Agent Registry exists.
[ ] MVP agent specs exist.
[ ] AI Context exists.
[ ] Agent forbidden actions are defined.
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] Agent output does not equal Human Review.
[ ] Agent cannot mutate state.
[ ] Agent cannot emit Events.
[ ] TASK-009 exists.
```

Blocked if:

```text
AI can approve/send/select/submit/certify/complete.
AI can mutate protected state.
AI can emit Events.
AI output can count as Human Review.
```

---

# 18. Fixture Readiness

Validate:

```text
[ ] TASK-002 exists.
[ ] Fixture system is specified.
[ ] Fixtures are deterministic.
[ ] Fixtures are non-production.
[ ] Positive fixtures are required.
[ ] Negative fixtures are required.
[ ] PermissionDenied fixtures are required.
[ ] PolicyRestricted fixtures are required.
[ ] AI forbidden-action fixtures are required.
[ ] Idempotency conflict fixtures are required.
[ ] Unsupported version fixtures are required.
[ ] Fixture integrity tests are required.
```

Blocked if:

```text
fixtures may use production data.
negative fixtures missing.
Permission/Policy negative fixtures missing.
AI forbidden-action fixtures missing.
idempotency conflict fixtures missing.
unsupported version fixtures missing.
```

---

# 19. Test Readiness

Validate:

```text
[ ] Common Contract Tests are specified.
[ ] API Contract Tests are specified.
[ ] Workflow Contract Tests are specified.
[ ] Agent Boundary Tests are specified.
[ ] Permission Policy Tests are specified.
[ ] Idempotency Event Tests are specified.
[ ] Error Versioning Tests are specified.
[ ] MVP execution spine tests are specified.
[ ] Negative tests are required.
[ ] Architecture boundary tests are required.
```

Required negative tests include:

```text
PermissionDenied
UnknownPermission
PolicyRestricted
UnknownPolicy
HumanReviewRequired
AI forbidden actions
IdempotencyConflict
VersionUnsupported
database ID leakage
stack trace leakage
restricted data leakage
event reference not command
API no-direct-event-emission
Workflow no-direct-event-emission
Agent no-direct-event-emission
Workflow no-direct-task-creation
```

Blocked if:

```text
happy-path-only testing is allowed.
negative tests are missing from Must Build Now areas.
boundary tests are missing.
```

---

# 20. Codex Task Readiness

Validate:

```text
[ ] CODEX-TASK-INDEX.md exists.
[ ] TASK-001 exists.
[ ] TASK-002 exists.
[ ] TASK-003 exists.
[ ] TASK-004 exists.
[ ] TASK-005 exists.
[ ] TASK-006 exists.
[ ] TASK-007 exists.
[ ] TASK-008 exists.
[ ] TASK-009 exists.
[ ] TASK-010 exists.
[ ] Each task has required source files.
[ ] Each task has scope.
[ ] Each task has out-of-scope.
[ ] Each task has forbidden shortcuts.
[ ] Each task has required tests.
[ ] Each task has acceptance criteria.
[ ] Task dependency sequence is clear.
```

Blocked if:

```text
any TASK-001 through TASK-010 missing.
task lacks source files or acceptance criteria.
task expands MVP scope.
task lacks forbidden shortcuts.
```

---

# 21. Out-of-Scope Protection

Validate that these are explicitly not implemented in MVP:

```text
full workflow engine
full policy engine
full agent runtime
external official filing integration
external communication send
payment execution
provider marketplace settlement
provider final selection by AI
official deadline certification by AI
registrability certification by AI
evidence sufficiency certification by AI
production notification delivery
production external integrations
public open API portal
```

Architecture violation if:

```text
Never in MVP item is included in MVP implementation.
Document Only item is implemented as production behavior.
Defer item blocks MVP acceptance.
```

---

# 22. MVP Execution Spine Readiness

Validate the first executable spine:

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

Readiness checks:

```text
[ ] Spine is defined in mvp-cut-v0.1.md.
[ ] TASK-010 exists.
[ ] Customer Intake Workflow is included.
[ ] Trademark Application Workflow is included.
[ ] Communication Review Workflow is included.
[ ] API validators are prerequisites.
[ ] Workflow validators are prerequisites.
[ ] Agent boundary tests are prerequisites.
[ ] Permission/Policy hooks are prerequisites.
[ ] Idempotency/Event trace is prerequisite.
[ ] Error/Versioning is prerequisite.
[ ] Active Tasks created only by Task Service.
[ ] Communications owned by Communication Service.
[ ] Events recorded through Event Service / owning service integration.
```

Blocked if:

```text
TASK-010 can start without TASK-001 through TASK-009.
MVP spine bypasses Task Service, Event Service or Communication Service.
```

---

# 23. Gate Decision Rules

Use the following decision rules.

## 23.1 Proceed

Allowed only if:

```text
No Architecture Violation.
No Blocked Must Build Now finding.
All P0 validation files exist.
TASK-001 through TASK-010 exist.
Must Build Now traceability is complete.
```

## 23.2 Proceed with Warning

Allowed if:

```text
Warnings are limited to Stub Now, Document Only, Defer or future-phase areas.
Warnings are documented.
Warnings do not affect MVP execution spine.
```

## 23.3 Block

Required if:

```text
Any Architecture Violation exists.
Any Must Build Now finding is Blocked.
Any P0 validation file missing.
Any TASK-001 through TASK-010 missing.
Permission/Policy fail-closed behavior missing.
Idempotency/Event boundary missing.
Error/Versioning safe failure missing.
Agent forbidden-action boundary missing.
```

## 23.4 Defer

Use when:

```text
finding is valid but outside MVP scope
finding belongs to later product/platform phase
finding is already listed as Document Only or Defer
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
Pass = ready for current MVP depth.
Warning = non-blocking issue documented.
Blocked = required MVP readiness item missing.
Architecture Violation = boundary breach or unsafe governance.
Out of Scope = requested item belongs outside MVP.
Deferred = valid later-phase item.
```

---

# 25. Required Evidence

Every finding must include:

```text
readiness area
source file
missing or inconsistent item
MVP category
implementation depth
affected Codex task
required fix
gate impact
```

Example:

```text
Finding: TASK-008 exists but Workflow Contract validation file is missing.
Status: Blocked
Readiness Area: Workflow
Required Fix: Generate core-specs/validation/workflow-contract-validation.md.
Codex Impact: Block TASK-008 and TASK-010.
Gate Impact: Block MVP readiness.
```

---

# 26. Architecture Violation Triggers

The following always block MVP readiness:

```text
API layer mutates domain state directly.
API layer emits Events directly.
Workflow layer owns domain behavior.
Workflow layer creates active Tasks directly.
Workflow layer emits Events directly.
Workflow preview has side effects.
Agent mutates protected state.
Agent emits Events.
Agent sends Communication.
Agent selects final provider.
Agent submits official filing.
Agent certifies deadline.
Agent certifies registrability.
Agent certifies evidence sufficiency.
Permission defaults to allowed.
Policy defaults to allowed.
UnknownPermission allows protected action.
UnknownPolicy allows restricted output.
Replay creates duplicate effects.
Event reference triggers command.
Raw database IDs appear in public responses.
Unsafe stack traces appear in errors.
Restricted data leaks.
Unsupported versions are silently accepted.
Production data is used as fixture.
Never in MVP item is implemented.
```

---

# 27. Validation Procedure

Perform validation in this order:

```text
1. Confirm all required source files exist.
2. Validate architecture baseline readiness.
3. Validate traceability readiness.
4. Validate MVP scope readiness.
5. Validate implementation depth readiness.
6. Validate contract readiness.
7. Validate API readiness.
8. Validate workflow readiness.
9. Validate domain/object/service readiness.
10. Validate Permission/Policy readiness.
11. Validate Idempotency/Event readiness.
12. Validate Error/Versioning readiness.
13. Validate Agent Boundary readiness.
14. Validate Fixture readiness.
15. Validate Test readiness.
16. Validate Codex Task readiness.
17. Validate out-of-scope protection.
18. Validate MVP execution spine readiness.
19. Classify findings.
20. Apply gate decision rules.
21. Produce MVP readiness report.
```

---

# 28. MVP Readiness Report Template

```text
Validation: MVP Readiness
Status: Pass | Proceed with Warning | Block | Defer
Scope: Book 02 Core MVP Implementation Readiness

Sources Checked:
- <file>
- <file>

Gate Summary:
- Architecture:
- Traceability:
- MVP Scope:
- Implementation Depth:
- Contracts:
- API:
- Workflow:
- Domain/Object/Service:
- Permission/Policy:
- Idempotency/Event:
- Error/Versioning:
- Agent Boundary:
- Fixtures:
- Tests:
- Codex Tasks:
- Out-of-Scope Protection:
- MVP Spine:

Findings:
- <finding>

Blocked Items:
- <blocked item>

Warnings:
- <warning>

Architecture Violations:
- <violation>

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
before starting TASK-010-mvp-execution-spine
after generating TASK-001 through TASK-010
after generating validation specs
before any implementation expansion beyond contracts
during PR review
before declaring MVP Core ready
```

Codex must not:

```text
start TASK-010 when TASK-001 through TASK-009 are missing
skip validation files
skip negative tests
implement Never in MVP items
deepen Stub Now items without approval
implement Document Only items as production systems
treat warnings as permission to expand scope
```

---

# 30. Acceptance Criteria

MVP Readiness Validation passes only if:

```text
[ ] Required source files exist.
[ ] Architecture baseline is ready.
[ ] Traceability baseline is ready.
[ ] MVP Cut is ready.
[ ] Implementation Depth Matrix is ready.
[ ] Developer Start Here is ready.
[ ] Codex Task Index is ready.
[ ] TASK-001 through TASK-010 exist.
[ ] Validation Index exists.
[ ] All P0 validation files exist.
[ ] Contract readiness passes.
[ ] API readiness passes for MVP APIs.
[ ] Workflow readiness passes for MVP workflows.
[ ] Domain/Object/Service readiness passes for Must Build Now.
[ ] Permission/Policy readiness passes.
[ ] Idempotency/Event readiness passes.
[ ] Error/Versioning readiness passes.
[ ] Agent Boundary readiness passes.
[ ] Fixture readiness is specified.
[ ] Test readiness is specified.
[ ] Out-of-scope protection is explicit.
[ ] MVP Execution Spine readiness is defined.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now areas.
```

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial MVP Readiness Validation. Defines MVP readiness gate, required sources, architecture/traceability/scope/depth/contract/API/workflow/domain/permission/idempotency/error/agent/fixture/test/Codex readiness, out-of-scope protection, decision rules and report template. |

---

**End of MVP Readiness Validation**
