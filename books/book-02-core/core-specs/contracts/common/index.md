# Common Contracts — Index

**Spec ID:** B02-CONTRACT-COMMON-INDEX  
**Spec Type:** Common Contract Index  
**Contract File:** core-specs/contracts/common/index.md  
**Contract Category:** Common Contracts  
**Related Files:** core-specs/contracts/common/README.md; core-specs/contracts/common/template.md  
**Related Parent Index:** core-specs/contracts/index.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 0 — Contract Foundation  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This index provides the canonical inventory and governance map for all Common Contracts under:

```text
core-specs/contracts/common/
```

Common Contracts define the shared primitives used by API Contracts, Workflow Contracts, Agent governance, Event trace and Test Contracts.

This file defines:

```text
common contract inventory
common contract responsibility
common primitive ownership
cross-contract dependency rules
governance rules
implementation order
Codex implementation checklist
acceptance criteria
```

---

# 2. Core Lock

```text
Common Contracts provide shared Core primitives.
References must hide database IDs.
Errors must be safe.
Pagination must respect Policy.
Audit Context preserves trace.
Permission and Policy contexts govern protected behavior.
AI Context bounds AI-assisted output.
Human Review records accountable review.
Idempotency prevents duplicate execution.
Versioning protects compatibility.
Common Contracts do not own domain behavior.
```

---

# 3. Common Contract Inventory

| No. | Common Contract | File | MVP Depth | Status |
|---:|---|---|---|---|
| 1 | Common Contracts README | core-specs/contracts/common/README.md | Must Maintain | Draft |
| 2 | Common Contract Template | core-specs/contracts/common/template.md | Must Maintain | Draft |
| 3 | References Contract | core-specs/contracts/common/references.md | Must Implement | Draft |
| 4 | Errors Contract | core-specs/contracts/common/errors.md | Must Implement | Draft |
| 5 | Pagination Contract | core-specs/contracts/common/pagination.md | Must Implement | Draft |
| 6 | Audit Context Contract | core-specs/contracts/common/audit-context.md | Must Implement | Draft |
| 7 | AI Context Contract | core-specs/contracts/common/ai-context.md | Must Implement | Draft |
| 8 | Human Review Contract | core-specs/contracts/common/human-review.md | Must Implement | Draft |
| 9 | Permission Context Contract | core-specs/contracts/common/permission-context.md | Must Implement | Draft |
| 10 | Policy Context Contract | core-specs/contracts/common/policy-context.md | Must Implement | Draft |
| 11 | Idempotency Contract | core-specs/contracts/common/idempotency.md | Must Implement | Draft |
| 12 | Versioning Contract | core-specs/contracts/common/versioning.md | Must Implement | Draft |
| 13 | Common Contracts Index | core-specs/contracts/common/index.md | Must Maintain | Draft |

---

# 4. Common Contract Responsibilities

| Contract | Responsibility | Must Not Own |
|---|---|---|
| references.md | public-safe reference shape and linked-object reference rules | database identity or permission grant |
| errors.md | safe error shape and controlled failure behavior | exception framework or internal diagnostics exposure |
| pagination.md | list/search pagination and count visibility rules | domain search semantics |
| audit-context.md | correlation, causation and event trace context | event execution or command behavior |
| ai-context.md | AI-assisted output metadata and boundary disclosure | professional truth or execution authority |
| human-review.md | human review trace and gated review context | downstream execution by itself |
| permission-context.md | permission evaluation context and fail-closed behavior | permission grant logic |
| policy-context.md | policy evaluation context, redaction and non-disclosure behavior | policy authoring or approval logic |
| idempotency.md | duplicate-safe request semantics | business deduplication policy beyond contract |
| versioning.md | version compatibility and historical trace rules | release management process by itself |

---

# 5. Cross-Contract Dependency Rules

## 5.1 References

```text
Every contract that refers to an object must use Reference Contract.
Every public object reference must use *_reference_id.
Database IDs must not be exposed.
Valid reference does not imply read permission.
```

## 5.2 Errors

```text
Every failure path must use Error Contract.
Errors must be safe.
Errors must not expose restricted data, database IDs, policy internals, permission internals, prompt internals or hidden reasoning.
```

## 5.3 Permission and Policy

```text
Permission Context and Policy Context are independent.
Permission approval does not imply Policy approval.
Policy allowance does not imply Permission approval.
Unknown Permission fails closed.
Unknown Policy fails closed for policy-controlled behavior.
```

## 5.4 AI and Human Review

```text
AI Context must be present for AI-assisted output.
AI output must not become professional truth by itself.
Human Review must gate protected professional or external-facing actions where required.
Human Review does not execute downstream action by itself.
```

## 5.5 Idempotency and Audit

```text
Duplicate-sensitive operations must use Idempotency Contract.
Audit Context preserves trace.
Event references are trace, not commands.
Idempotent replay must not duplicate Events.
```

## 5.6 Versioning

```text
Every contract must declare contract_version.
Unsupported versions fail closed.
Breaking changes require version bump.
Historical records must preserve the version used.
```

---

# 6. Common Contract Use by Layer

## 6.1 API Contracts

API Contracts must use:

```text
references.md
errors.md
versioning.md
permission-context.md
policy-context.md
pagination.md where list/search exists
idempotency.md where duplicate-sensitive behavior exists
audit-context.md where event trace appears
ai-context.md where AI-assisted behavior exists
human-review.md where review gates exist
```

## 6.2 Workflow Contracts

Workflow Contracts must use:

```text
references.md
errors.md
audit-context.md
permission-context.md
policy-context.md
ai-context.md where AI-assisted steps exist
human-review.md where review checkpoints exist
idempotency.md for apply operations
versioning.md for workflow contract compatibility
```

## 6.3 Test Contracts

Test Contracts must verify:

```text
reference safety
safe errors
pagination policy behavior
audit trace behavior
Permission / Policy fail-closed behavior
AI boundary behavior
Human Review gate behavior
Idempotency replay/conflict behavior
VersionUnsupported behavior
```

---

# 7. Required Global Controlled Fields

Common fields reused across contracts:

```text
*_reference_id
correlation_id
causation_event_reference_id
event_reference_ids
permission_decision_reference_id
policy_decision_reference_id
human_review_reference_id
idempotency_key
api_version
contract_version
schema_version
workflow_contract_version
agent_contract_version
restricted_fields_omitted
policy_omissions_disclosed
human_review_required
```

Rules:

```text
- Field names must remain stable.
- Breaking field changes require version bump.
- Public fields must not expose database IDs.
- Restricted fields must be omitted or redacted according to Policy.
```

---

# 8. Required Implementation Order

Recommended Codex implementation order:

```text
1. references.md
2. errors.md
3. versioning.md
4. permission-context.md
5. policy-context.md
6. audit-context.md
7. idempotency.md
8. pagination.md
9. ai-context.md
10. human-review.md
11. common-contract-tests.md
12. common/index.md
```

Reasoning:

```text
References and Errors are the base safety layer.
Versioning protects compatibility.
Permission and Policy govern protected behavior.
Audit and Idempotency protect trace and duplicate safety.
Pagination, AI Context and Human Review extend reusable interaction behavior.
Tests verify the shared primitives.
Index closes the common layer.
```

---

# 9. Governance Rules

Every Common Contract must:

```text
define purpose
define Core Lock
define contract meaning
define canonical shape
define required fields
define optional fields
define controlled values where applicable
define Permission and Policy interaction where applicable
define AI and Human Review interaction where applicable
define Idempotency behavior where applicable
define Error behavior
define Versioning behavior
define Codex implementation notes
define Acceptance Criteria
```

Every Common Contract must not:

```text
own domain behavior
grant permission
approve policy
execute AI output
execute human review downstream action
emit events by itself
expose database IDs
expose restricted data
silently accept unsupported versions
```

---

# 10. Test Coverage Requirements

Common Contracts must be verified by:

```text
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
core-specs/contracts/tests/agent-boundary-tests.md where AI Context is involved
```

Required test categories:

```text
positive shape tests
negative shape tests
invalid reference tests
safe error tests
permission denied tests
policy restricted tests
redaction tests
AI forbidden-action tests
human review required tests
idempotency replay tests
idempotency conflict tests
event reference not command tests
version unsupported tests
```

---

# 11. Codex Implementation Notes

Codex must:

```text
read this Common Contracts Index before implementing common contracts
read Common Contracts README and Template before writing new common contracts
cite the specific Common Contract being implemented
preserve stable field names
use Reference Contract for all references
use Error Contract for all failures
use Versioning Contract for compatibility
use Permission and Policy Context for protected behavior
use AI Context for AI-assisted output
use Human Review Contract for review-gated behavior
use Idempotency Contract for duplicate-sensitive behavior
use Audit Context Contract for trace
write deterministic non-production tests
```

Codex must not:

```text
treat Common Contracts as optional helpers
create domain behavior in Common Contracts
expose database IDs
expose restricted data
skip Permission or Policy interaction
allow AI to execute protected actions
allow Human Review to execute downstream action by itself
treat event references as commands
silently accept unsupported versions
silently rewrite historical version traces
```

---

# 12. Acceptance Criteria

This Common Contracts Index is accepted only if:

```text
[ ] It lists all Common Contract files.
[ ] It defines Core Lock.
[ ] It defines Common Contract responsibilities.
[ ] It defines cross-contract dependency rules.
[ ] It defines Common Contract use by layer.
[ ] It defines required global controlled fields.
[ ] It defines implementation order.
[ ] It defines governance rules.
[ ] It defines test coverage requirements.
[ ] It defines Codex implementation notes.
```

---

# 13. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Common Contracts Index. Defines common inventory, responsibilities, dependency rules, layer usage, controlled fields, implementation order, governance rules, test coverage and Codex expectations. |

---

**End of Common Contracts Index**
