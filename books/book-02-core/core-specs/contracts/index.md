# Contracts — Index

**Spec ID:** B02-CONTRACT-INDEX  
**Spec Type:** Contract Layer Index  
**Contract File:** core-specs/contracts/index.md  
**Contract Category:** Core Contracts  
**Related Files:** core-specs/contracts/README.md; core-specs/contracts/template.md  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Test Contracts  
**Related Index Files:** core-specs/contracts/common/index.md; core-specs/contracts/api/index.md; core-specs/contracts/workflows/index.md; core-specs/contracts/tests/index.md  
**Related Core Specs:** core-specs/services/*.md; core-specs/objects/*.md; core-specs/events/*.md; core-specs/agents/*.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Core Contract Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This index provides the canonical inventory and governance map for the MarkOrbit Core Contract layer under:

```text
core-specs/contracts/
```

It defines:

```text
contract layer inventory
contract layer responsibility
contract-to-core mapping
common contract inventory
API contract inventory
workflow contract inventory
test contract inventory
governance rules
implementation order
Codex implementation checklist
acceptance criteria
```

This file is the top-level contract navigation artifact. It does not replace any individual Common, API, Workflow or Test Contract file.

---

# 2. Core Lock

```text
Contracts define governed interaction boundaries.
Common Contracts provide shared primitives.
API Contracts define request and response boundaries.
Workflow Contracts define governed execution patterns.
Test Contracts verify Core behavior.
Owning services own behavior.
Permission and Policy govern protected actions.
AI remains bounded by Agent Governance.
Events preserve trace.
```

---

# 3. Contract Layer Map

```text
core-specs/contracts/
  README.md
  template.md
  index.md

  common/
    README.md
    template.md
    index.md
    references.md
    errors.md
    pagination.md
    audit-context.md
    ai-context.md
    human-review.md
    permission-context.md
    policy-context.md
    idempotency.md
    versioning.md

  api/
    README.md
    template.md
    index.md
    identity-api-contract.md
    organization-api-contract.md
    user-api-contract.md
    permission-api-contract.md
    policy-api-contract.md
    knowledge-api-contract.md
    brand-api-contract.md
    trademark-api-contract.md
    jurisdiction-api-contract.md
    classification-api-contract.md
    document-api-contract.md
    evidence-api-contract.md
    customer-api-contract.md
    matter-api-contract.md
    order-api-contract.md
    opportunity-api-contract.md
    workflow-contract-api-contract.md
    task-api-contract.md
    event-api-contract.md
    notification-api-contract.md
    communication-api-contract.md
    agent-api-contract.md
    service-provider-api-contract.md
    routing-api-contract.md
    partner-api-contract.md
    service-network-api-contract.md

  workflows/
    README.md
    template.md
    index.md
    customer-intake-workflow-contract.md
    trademark-application-workflow-contract.md
    office-action-response-workflow-contract.md
    provider-routing-workflow-contract.md
    communication-review-workflow-contract.md
    renewal-workflow-contract.md
    assignment-workflow-contract.md
    evidence-review-workflow-contract.md

  tests/
    README.md
    template.md
    index.md
    common-contract-tests.md
    api-contract-tests.md
    workflow-contract-tests.md
    agent-boundary-tests.md
    permission-policy-tests.md
    idempotency-event-tests.md
    error-versioning-tests.md
```

---

# 4. Contract Layer Responsibilities

| Layer | Responsibility | Must Not Own |
|---|---|---|
| Common Contracts | shared references, errors, pagination, audit, permission, policy, AI, human review, idempotency, versioning | domain behavior |
| API Contracts | request/response shape, endpoint boundary, API governance | service implementation |
| Workflow Contracts | governed execution coordination and workflow step contracts | domain mutation or task creation directly |
| Test Contracts | acceptance-level verification of Core behavior | production implementation logic |

Core rule:

```text
Contracts define boundaries.
Services implement behavior.
Tests verify compliance.
```

---

# 5. Common Contract Inventory

| No. | Common Contract | File | MVP Depth |
|---:|---|---|---|
| 1 | Common Contracts README | core-specs/contracts/common/README.md | Must Maintain |
| 2 | Common Contract Template | core-specs/contracts/common/template.md | Must Maintain |
| 3 | References Contract | core-specs/contracts/common/references.md | Must Implement |
| 4 | Errors Contract | core-specs/contracts/common/errors.md | Must Implement |
| 5 | Pagination Contract | core-specs/contracts/common/pagination.md | Must Implement |
| 6 | Audit Context Contract | core-specs/contracts/common/audit-context.md | Must Implement |
| 7 | AI Context Contract | core-specs/contracts/common/ai-context.md | Must Implement |
| 8 | Human Review Contract | core-specs/contracts/common/human-review.md | Must Implement |
| 9 | Permission Context Contract | core-specs/contracts/common/permission-context.md | Must Implement |
| 10 | Policy Context Contract | core-specs/contracts/common/policy-context.md | Must Implement |
| 11 | Idempotency Contract | core-specs/contracts/common/idempotency.md | Must Implement |
| 12 | Versioning Contract | core-specs/contracts/common/versioning.md | Must Implement |
| 13 | Common Contracts Index | core-specs/contracts/common/index.md | Must Maintain |

---

# 6. API Contract Inventory

## 6.1 Foundation API Contracts

```text
identity-api-contract.md
organization-api-contract.md
user-api-contract.md
permission-api-contract.md
policy-api-contract.md
knowledge-api-contract.md
```

## 6.2 Professional API Contracts

```text
brand-api-contract.md
trademark-api-contract.md
jurisdiction-api-contract.md
classification-api-contract.md
document-api-contract.md
evidence-api-contract.md
```

## 6.3 Business Execution API Contracts

```text
customer-api-contract.md
matter-api-contract.md
order-api-contract.md
opportunity-api-contract.md
workflow-contract-api-contract.md
task-api-contract.md
event-api-contract.md
notification-api-contract.md
communication-api-contract.md
```

## 6.4 Collaboration Network API Contracts

```text
agent-api-contract.md
service-provider-api-contract.md
routing-api-contract.md
partner-api-contract.md
service-network-api-contract.md
```

API rule:

```text
API Contracts expose governed access to Core services.
API Contracts must not redefine service behavior.
```

---

# 7. Workflow Contract Inventory

| No. | Workflow Contract | File | MVP Depth |
|---:|---|---|---|
| 1 | Customer Intake Workflow Contract | core-specs/contracts/workflows/customer-intake-workflow-contract.md | Must Implement |
| 2 | Trademark Application Workflow Contract | core-specs/contracts/workflows/trademark-application-workflow-contract.md | Must Implement |
| 3 | Office Action Response Workflow Contract | core-specs/contracts/workflows/office-action-response-workflow-contract.md | Must Implement |
| 4 | Provider Routing Workflow Contract | core-specs/contracts/workflows/provider-routing-workflow-contract.md | Must Implement |
| 5 | Communication Review Workflow Contract | core-specs/contracts/workflows/communication-review-workflow-contract.md | Must Implement |
| 6 | Renewal Workflow Contract | core-specs/contracts/workflows/renewal-workflow-contract.md | Should Implement |
| 7 | Assignment Workflow Contract | core-specs/contracts/workflows/assignment-workflow-contract.md | Should Implement |
| 8 | Evidence Review Workflow Contract | core-specs/contracts/workflows/evidence-review-workflow-contract.md | Should Implement |

Workflow rule:

```text
Workflow Contracts coordinate governed execution.
Workflow Contracts must route mutations and active task creation to owning services.
```

---

# 8. Test Contract Inventory

| No. | Test Contract | File | MVP Depth |
|---:|---|---|---|
| 1 | Test Contracts README | core-specs/contracts/tests/README.md | Must Implement |
| 2 | Test Contract Template | core-specs/contracts/tests/template.md | Must Maintain |
| 3 | Common Contract Tests | core-specs/contracts/tests/common-contract-tests.md | Must Implement |
| 4 | API Contract Tests | core-specs/contracts/tests/api-contract-tests.md | Must Implement |
| 5 | Workflow Contract Tests | core-specs/contracts/tests/workflow-contract-tests.md | Must Implement |
| 6 | Agent Boundary Tests | core-specs/contracts/tests/agent-boundary-tests.md | Should Implement |
| 7 | Permission Policy Tests | core-specs/contracts/tests/permission-policy-tests.md | Must Implement |
| 8 | Idempotency Event Tests | core-specs/contracts/tests/idempotency-event-tests.md | Must Implement |
| 9 | Error Versioning Tests | core-specs/contracts/tests/error-versioning-tests.md | Must Implement |
| 10 | Test Contracts Index | core-specs/contracts/tests/index.md | Must Maintain |

Test rule:

```text
Test Contracts verify that implementation preserves Core boundaries.
Happy-path tests are not sufficient.
```

---

# 9. Contract-to-Core Mapping

```text
Common Contracts
  Foundation for all Core interactions.

API Contracts
  Consume Object Specs and Service Specs.
  Expose governed request/response boundaries.

Workflow Contracts
  Consume API Contracts, Service Specs, Event Specs and Agent Specs.
  Coordinate execution across services.

Test Contracts
  Consume Common, API, Workflow, Event, Agent and Service specs.
  Verify implementation compliance.
```

Canonical flow:

```text
Principles define
↓
Core provides
↓
Contracts constrain
↓
Services implement
↓
Workflows coordinate
↓
Tests verify
↓
Products consume
```

---

# 10. Governance Rules

Every Contract file must:

```text
define metadata
define purpose
define Core Lock or equivalent boundary lock
define ownership boundary
define required references
define Permission and Policy behavior where applicable
define AI boundary where applicable
define Human Review behavior where applicable
define Idempotency behavior where applicable
define Event trace behavior where applicable
define Error behavior
define Versioning behavior
define Codex implementation notes
define Acceptance Criteria
```

Every Contract file must not:

```text
grant Permission
approve Policy
mutate domain state directly
create active Tasks outside Task Service
emit Events outside owning services
allow AI to execute protected actions
expose database IDs
expose restricted data
silently accept unsupported versions
silently rewrite historical versions
```

---

# 11. Permission / Policy Governance

Required rules:

```text
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Permission approval is not Policy approval.
Policy allowance is not Permission approval.
Unknown Permission fails closed.
Unknown Policy fails closed for policy-controlled behavior.
Policy may block, redact, downgrade or require human review.
```

Required testing:

```text
PermissionDenied
PolicyRestricted
redaction
non-disclosure
cross-organization restrictions
event visibility
AI output omissions
```

---

# 12. AI Governance

Contracts must preserve:

```text
AI may prepare.
AI may summarize.
AI may classify.
AI may draft.
AI may suggest.
AI may compare.
AI may identify gaps.
```

AI must not:

```text
approve
send
select provider
submit filing
certify deadline
certify authority
decide registrability
decide evidence sufficiency
approve payment
complete task
mutate protected state
emit events
```

AI-related contracts:

```text
core-specs/contracts/common/ai-context.md
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
core-specs/contracts/tests/agent-boundary-tests.md
```

---

# 13. Human Review Governance

Human Review must gate:

```text
professional conclusions
customer-facing communication
external communication
provider selection
deadline confirmation
classification or goods/services wording
evidence sufficiency
ownership or authority context
filing or submission readiness
payment-impacting or commercial decisions
```

Core rule:

```text
Human Review records accountable review.
Human Review does not execute downstream action by itself.
Owning services decide whether review satisfies action requirements.
```

---

# 14. Idempotency / Event Governance

Idempotency rules:

```text
Duplicate-sensitive operations require idempotency_key.
Same key and same semantic request replays safely.
Same key and different semantic request fails safely.
Duplicate replay must not duplicate objects, tasks, communications, routing selections or events.
```

Event rules:

```text
Events are emitted only by owning services.
API layer must not emit Events directly.
Workflow layer must not emit Events directly.
Agent layer must not emit Events directly.
Event references are audit trace, not commands.
Event visibility follows Policy.
```

---

# 15. Error / Versioning Governance

Error rules:

```text
Errors must follow Error Contract.
Errors must be safe.
Errors must preserve correlation_id where provided.
Errors must not expose database IDs.
Errors must not expose restricted data.
Errors must not expose policy internals.
Errors must not expose permission internals.
Errors must not expose prompt internals or hidden reasoning.
```

Versioning rules:

```text
Unsupported versions fail closed.
Breaking changes require version bumps.
Historical workflow applications preserve workflow_contract_version used.
Historical events preserve event/schema version where required.
Agent outputs preserve agent/capability version where required.
Deprecated versions must not be silently rewritten.
```

---

# 16. MVP Implementation Order

Recommended Codex implementation order for contract layer:

```text
1. Contracts README
2. Contracts Template
3. Common Contracts
4. Common Contracts Index
5. API Contracts
6. API Contracts Index
7. Workflow Contracts
8. Workflow Contracts Index
9. Test Contracts README
10. Test Contract Template
11. Test Contracts
12. Test Contracts Index
13. Contracts Index
```

Reasoning:

```text
- README/template establish the contract system.
- Common Contracts establish shared primitives.
- API Contracts expose service boundaries.
- Workflow Contracts coordinate execution.
- Test Contracts verify all boundaries.
- This index closes the contract layer.
```

---

# 17. Contract Layer Acceptance Matrix

```yaml
acceptance_matrix:
  common_contracts:
    required: true
    index: core-specs/contracts/common/index.md
    tests: core-specs/contracts/tests/common-contract-tests.md

  api_contracts:
    required: true
    index: core-specs/contracts/api/index.md
    tests: core-specs/contracts/tests/api-contract-tests.md

  workflow_contracts:
    required: true
    index: core-specs/contracts/workflows/index.md
    tests: core-specs/contracts/tests/workflow-contract-tests.md

  agent_boundaries:
    required: true
    tests: core-specs/contracts/tests/agent-boundary-tests.md

  permission_policy:
    required: true
    contracts:
      - core-specs/contracts/common/permission-context.md
      - core-specs/contracts/common/policy-context.md
    tests: core-specs/contracts/tests/permission-policy-tests.md

  idempotency_events:
    required: true
    contracts:
      - core-specs/contracts/common/idempotency.md
      - core-specs/contracts/common/audit-context.md
      - core-specs/contracts/api/event-api-contract.md
    tests: core-specs/contracts/tests/idempotency-event-tests.md

  errors_versioning:
    required: true
    contracts:
      - core-specs/contracts/common/errors.md
      - core-specs/contracts/common/versioning.md
    tests: core-specs/contracts/tests/error-versioning-tests.md
```

---

# 18. Codex Implementation Notes

Codex must:

```text
read this Contracts Index before contract-layer implementation
read Contracts README and Template before writing new contracts
use Common Contracts in every API and Workflow Contract
cite specific contracts before implementation
route behavior to owning services
use Permission Context Contract for protected behavior
use Policy Context Contract for policy-controlled behavior
use AI Context Contract for AI-assisted behavior
use Human Review Contract for gated behavior
use Idempotency Contract for duplicate-sensitive behavior
use Audit Context Contract and Event API/Event Specs for trace
use Error Contract for every failure path
use Versioning Contract for compatibility
implement Test Contracts before accepting production behavior
write positive and negative tests
write PermissionDenied and PolicyRestricted tests
write AI forbidden-action tests
write HumanReviewRequired tests
write idempotency replay/conflict tests
write event ownership/non-duplication tests
write safe error tests
write VersionUnsupported tests
```

Codex must not:

```text
treat contracts as optional documentation
implement from assumptions instead of contract files
mutate domain state outside owning services
create active Tasks outside Task Service
emit Events from API/Workflow/Agent layers
grant Permission from contract code
approve Policy from contract code
allow AI to execute protected actions
skip negative tests
use production data fixtures
expose database IDs
expose restricted data
silently accept unsupported versions
silently rewrite historical version traces
```

---

# 19. Acceptance Criteria

This Contracts Index is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines Contract Layer Map.
[ ] It defines Contract Layer Responsibilities.
[ ] It lists Common Contract inventory.
[ ] It lists API Contract inventory.
[ ] It lists Workflow Contract inventory.
[ ] It lists Test Contract inventory.
[ ] It defines Contract-to-Core mapping.
[ ] It defines governance rules.
[ ] It defines Permission / Policy governance.
[ ] It defines AI governance.
[ ] It defines Human Review governance.
[ ] It defines Idempotency / Event governance.
[ ] It defines Error / Versioning governance.
[ ] It defines MVP implementation order.
[ ] It defines Contract Layer Acceptance Matrix.
[ ] It defines Codex implementation notes.
```

---

# 20. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Contracts Index. Defines top-level contract inventory, layer responsibilities, common/API/workflow/test inventories, governance rules, implementation order, acceptance matrix and Codex expectations. |

---

**End of Contracts Index**
