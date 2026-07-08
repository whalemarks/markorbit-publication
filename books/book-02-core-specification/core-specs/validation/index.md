# Validation Index

**Spec ID:** B02-VALIDATION-INDEX  
**Spec Type:** Validation Index  
**Spec File:** core-specs/validation/index.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Codex Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Index Version:** v0.1.0  
**MVP Phase:** Phase 0–1 — Core Validation Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file is the canonical index for MarkOrbit Core validation specifications.

Validation files define how Book 02 is checked before and during Codex implementation.

The validation system answers:

```text
Is the architecture internally consistent?
Are domains, objects and services aligned?
Are API Contracts aligned with owning services?
Are Workflow Contracts aligned with workflow boundaries?
Are Permission and Policy enforced correctly?
Are Idempotency and Event trace rules enforced?
Are Agent boundaries preserved?
Are errors safe and versions controlled?
Is the MVP ready for implementation?
```

Validation does not replace implementation.

Validation constrains implementation.

---

# 2. Core Lock

```text
Validation protects architecture.
Validation prevents drift.
Validation checks traceability.
Validation checks implementation readiness.
Validation does not define new architecture.
Validation does not replace tests.
Validation does not execute business workflows.
Validation must fail closed where Core governance is missing.
Codex must pass validation before expanding implementation.
```

---

# 3. Validation Principles

All validation specs must follow these principles:

```text
Validate against Book 02 specifications.
Validate against TRACEABILITY.md.
Validate against MVP Cut.
Validate against Implementation Depth Matrix.
Validate ownership boundaries.
Validate Permission and Policy fail-closed behavior.
Validate AI boundaries.
Validate Event trace boundaries.
Validate safe errors.
Validate unsupported-version failure.
Validate negative cases, not only happy paths.
```

---

# 4. Validation Scope

The validation layer covers:

```text
architecture consistency
traceability
domain/object/service alignment
API contract alignment
workflow contract alignment
agent boundaries
permission/policy governance
idempotency/event trace
error/versioning behavior
MVP readiness
```

Validation does not cover:

```text
product UI design
commercial pricing
external filing execution
production infrastructure monitoring
external provider SLA performance
payment settlement
official office integrations
```

---

# 5. Required Validation Files

The validation folder must contain these files:

```text
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

---

# 6. Validation File Map

| Validation File | Primary Purpose | MVP Priority |
|---|---|---|
| architecture-consistency-validation.md | Validate Core architecture consistency and no boundary drift | P0 |
| traceability-validation.md | Validate layer-to-layer traceability | P0 |
| domain-object-service-validation.md | Validate Domains, Objects and Services alignment | P0 |
| api-contract-validation.md | Validate API Contract boundaries | P0 |
| workflow-contract-validation.md | Validate Workflow Contract boundaries | P0 |
| agent-boundary-validation.md | Validate AI/Agent boundaries | P0 |
| permission-policy-validation.md | Validate Permission and Policy governance | P0 |
| idempotency-event-validation.md | Validate duplicate safety and Event trace behavior | P0 |
| error-versioning-validation.md | Validate safe errors and version fail-closed behavior | P0 |
| mvp-readiness-validation.md | Validate whether MVP can enter implementation | P0 |

---

# 7. Validation Dependency Order

Validation should run in this order:

```text
1. architecture-consistency-validation.md
2. traceability-validation.md
3. domain-object-service-validation.md
4. api-contract-validation.md
5. workflow-contract-validation.md
6. permission-policy-validation.md
7. idempotency-event-validation.md
8. error-versioning-validation.md
9. agent-boundary-validation.md
10. mvp-readiness-validation.md
```

Rationale:

```text
architecture first
traceability second
domain/service ownership third
API/workflow boundaries fourth
governance primitives fifth
agent boundaries sixth
MVP readiness last
```

---

# 8. Validation Depth

Validation depth follows the Implementation Depth Matrix.

| Validation Area | MVP Validation Depth | Notes |
|---|---:|---|
| Architecture consistency | Level 2 | Structural and boundary validation |
| Traceability | Level 2 | Required mappings and gaps |
| Domain/Object/Service | Level 2 | Ownership consistency |
| API Contracts | Level 2/3 | MVP APIs stronger |
| Workflow Contracts | Level 2/3 | MVP workflows stronger |
| Permission/Policy | Level 3 | Fail-closed behavior must be tested |
| Idempotency/Event | Level 3 | Duplicate and event boundary tests required |
| Error/Versioning | Level 3 for errors, Level 1 for versioning | Safe failure required |
| Agent Boundaries | Level 3 for forbidden actions | Autonomous execution blocked |
| MVP Readiness | Level 2/3 | Gate before implementation expansion |

---

# 9. Validation Inputs

Validation specs must reference:

```text
Book 02 table of contents
core-specs/reviews/book-02-core-review.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/contracts/MANIFEST.md
core-specs/contracts/index.md
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
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

# 10. Validation Outputs

Each validation file should define:

```text
validation purpose
required source files
validation checks
failure conditions
required evidence
Codex implications
acceptance criteria
```

Validation output should classify findings as:

```text
Pass
Warning
Blocked
Architecture Violation
Out of Scope
Deferred
```

---

# 11. Failure Severity

## 11.1 Pass

Meaning:

```text
validation area is complete enough for the current phase
```

## 11.2 Warning

Meaning:

```text
issue exists but does not block current MVP implementation
```

Examples:

```text
future workflow incomplete
stub API missing future operation
document-only capability not implemented
```

## 11.3 Blocked

Meaning:

```text
required MVP file, contract, mapping or test is missing
```

Examples:

```text
TRACEABILITY.md missing
MVP cut missing
Permission/Policy tests missing
API validator scaffold missing
```

## 11.4 Architecture Violation

Meaning:

```text
implementation or spec breaks Core boundary
```

Examples:

```text
API layer mutates domain state directly
Workflow layer emits Events directly
Agent sends external communication
AI certifies professional truth
Permission defaults to allowed
Policy defaults to allowed
```

## 11.5 Out of Scope

Meaning:

```text
requested implementation belongs to later phase
```

Examples:

```text
full workflow engine
full policy engine
full agent runtime
external filing integration
payment execution
```

## 11.6 Deferred

Meaning:

```text
valid future capability, intentionally postponed
```

---

# 12. Universal Validation Checks

Every validation file should check:

```text
[ ] Required source files exist.
[ ] Required mappings are present.
[ ] MVP scope is respected.
[ ] Implementation depth is respected.
[ ] Ownership boundaries are preserved.
[ ] Permission and Policy fail closed where relevant.
[ ] AI does not execute protected actions.
[ ] Events are trace, not commands.
[ ] Errors are safe.
[ ] Unsupported versions fail closed.
[ ] Negative cases are covered.
[ ] Out-of-scope items are not implemented accidentally.
```

---

# 13. Architecture Violation Triggers

The following must always fail validation:

```text
API layer mutates domain state directly.
API layer emits Events directly.
Workflow layer owns domain behavior.
Workflow layer creates active Tasks directly.
Workflow layer emits Events directly.
Agent layer mutates protected state.
Agent layer emits Events.
Agent sends external communication.
Agent selects provider finally.
Agent submits official filing.
Agent certifies deadlines.
Agent certifies registrability.
Agent certifies evidence sufficiency.
Permission defaults to allowed.
Policy defaults to allowed.
Unsupported version is silently accepted.
Raw database IDs appear in public responses.
Unsafe stack traces appear in errors.
Production data is used as fixtures.
```

---

# 14. MVP Readiness Gate

MVP implementation should not expand unless these validations pass:

```text
architecture-consistency-validation
traceability-validation
domain-object-service-validation
api-contract-validation for MVP APIs
workflow-contract-validation for MVP workflows
permission-policy-validation
idempotency-event-validation
error-versioning-validation
agent-boundary-validation
mvp-readiness-validation
```

Minimum pass condition:

```text
No Architecture Violation.
No Blocked finding in Must Build Now areas.
Warnings are documented.
Deferred items are explicitly out of MVP scope.
```

---

# 15. Validation Report Format

Each validation file should be able to produce or support a report like:

```text
Validation: <name>
Status: Pass | Warning | Blocked | Architecture Violation
Scope: <area>
Sources Checked:
- <file>
Findings:
- <finding>
Evidence:
- <file / contract / test>
Required Fix:
- <fix>
Codex Impact:
- <task affected>
Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 16. Codex Usage

Codex must use validation specs as:

```text
pre-implementation checklist
post-implementation checklist
review checklist
source of failure conditions
source of acceptance criteria
```

Codex must not use validation specs to:

```text
invent new architecture
expand MVP scope
deepen implementation without approval
skip source specs
skip tests
```

---

# 17. Acceptance Criteria

This Validation Index is accepted only if:

```text
[ ] It defines validation purpose.
[ ] It defines Core Lock.
[ ] It defines validation principles.
[ ] It defines validation scope.
[ ] It lists required validation files.
[ ] It defines validation file map.
[ ] It defines validation dependency order.
[ ] It defines validation depth.
[ ] It defines validation inputs.
[ ] It defines validation outputs.
[ ] It defines failure severity.
[ ] It defines universal validation checks.
[ ] It defines architecture violation triggers.
[ ] It defines MVP readiness gate.
[ ] It defines validation report format.
[ ] It defines Codex usage.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Validation Index. Defines validation file map, dependency order, depth, inputs, outputs, severity, universal checks, architecture violation triggers, MVP readiness gate and Codex usage. |

---

**End of Validation Index**
