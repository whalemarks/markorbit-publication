# API Contracts — Index

**Spec ID:** B02-CONTRACT-API-INDEX  
**Spec Type:** API Contract Index  
**Contract File:** core-specs/contracts/api/index.md  
**Contract Category:** API Contracts  
**Related Files:** core-specs/contracts/api/README.md; core-specs/contracts/api/template.md  
**Related Parent Index:** core-specs/contracts/index.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Related Test Contract:** core-specs/contracts/tests/api-contract-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 1–5 — API Boundary Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This index provides the canonical inventory and governance map for all API Contracts under:

```text
core-specs/contracts/api/
```

API Contracts define governed request and response boundaries for MarkOrbit Core services.

This file defines:

```text
API contract inventory
API family grouping
API contract responsibility
API-to-domain mapping
API-to-service mapping
required common contract usage
governance rules
implementation order
Codex implementation checklist
acceptance criteria
```

This index is a navigation and governance artifact. It does not replace any individual API Contract file.

---

# 2. Core Lock

```text
API Contracts define governed request and response boundaries.
API layer receives requests and returns safe responses.
Owning services own behavior.
References are validated by owning services.
Permission and Policy govern protected API actions.
AI-assisted API output must remain bounded by AI Context and Agent Governance.
Human Review gates protected actions where required.
Idempotency prevents duplicate execution.
Events preserve trace and are not emitted directly by API layer.
Errors must remain safe.
Unsupported versions fail closed.
```

---

# 3. API Contract Inventory

## 3.1 Foundation API Contracts

| No. | API Contract | File | Related Domain | MVP Depth | Status |
|---:|---|---|---|---|---|
| 1 | Identity API Contract | core-specs/contracts/api/identity-api-contract.md | Identity | Must Implement | Draft |
| 2 | Organization API Contract | core-specs/contracts/api/organization-api-contract.md | Organization | Must Implement | Draft |
| 3 | User API Contract | core-specs/contracts/api/user-api-contract.md | User | Must Implement | Draft |
| 4 | Permission API Contract | core-specs/contracts/api/permission-api-contract.md | Permission | Must Implement | Draft |
| 5 | Policy API Contract | core-specs/contracts/api/policy-api-contract.md | Policy | Must Implement | Draft |
| 6 | Knowledge API Contract | core-specs/contracts/api/knowledge-api-contract.md | Knowledge | Must Implement | Draft |

## 3.2 Professional API Contracts

| No. | API Contract | File | Related Domain | MVP Depth | Status |
|---:|---|---|---|---|---|
| 7 | Brand API Contract | core-specs/contracts/api/brand-api-contract.md | Brand | Must Implement | Draft |
| 8 | Trademark API Contract | core-specs/contracts/api/trademark-api-contract.md | Trademark | Must Implement | Draft |
| 9 | Jurisdiction API Contract | core-specs/contracts/api/jurisdiction-api-contract.md | Jurisdiction | Must Implement | Draft |
| 10 | Classification API Contract | core-specs/contracts/api/classification-api-contract.md | Classification | Must Implement | Draft |
| 11 | Document API Contract | core-specs/contracts/api/document-api-contract.md | Document | Must Implement | Draft |
| 12 | Evidence API Contract | core-specs/contracts/api/evidence-api-contract.md | Evidence | Must Implement | Draft |

## 3.3 Business Execution API Contracts

| No. | API Contract | File | Related Domain | MVP Depth | Status |
|---:|---|---|---|---|---|
| 13 | Customer API Contract | core-specs/contracts/api/customer-api-contract.md | Customer | Must Implement | Draft |
| 14 | Matter API Contract | core-specs/contracts/api/matter-api-contract.md | Matter | Must Implement | Draft |
| 15 | Order API Contract | core-specs/contracts/api/order-api-contract.md | Order | Must Implement | Draft |
| 16 | Opportunity API Contract | core-specs/contracts/api/opportunity-api-contract.md | Opportunity | Must Implement | Draft |
| 17 | Workflow Contract API Contract | core-specs/contracts/api/workflow-contract-api-contract.md | Workflow Contract | Must Implement | Draft |
| 18 | Task API Contract | core-specs/contracts/api/task-api-contract.md | Task | Must Implement | Draft |
| 19 | Event API Contract | core-specs/contracts/api/event-api-contract.md | Event | Must Implement | Draft |
| 20 | Notification API Contract | core-specs/contracts/api/notification-api-contract.md | Notification | Must Implement | Draft |
| 21 | Communication API Contract | core-specs/contracts/api/communication-api-contract.md | Communication | Must Implement | Draft |

## 3.4 Collaboration Network API Contracts

| No. | API Contract | File | Related Domain | MVP Depth | Status |
|---:|---|---|---|---|---|
| 22 | Agent API Contract | core-specs/contracts/api/agent-api-contract.md | Agent | Must Implement | Draft |
| 23 | Service Provider API Contract | core-specs/contracts/api/service-provider-api-contract.md | Service Provider | Must Implement | Draft |
| 24 | Routing API Contract | core-specs/contracts/api/routing-api-contract.md | Routing | Must Implement | Draft |
| 25 | Partner API Contract | core-specs/contracts/api/partner-api-contract.md | Partner | Must Implement | Draft |
| 26 | Service Network API Contract | core-specs/contracts/api/service-network-api-contract.md | Service Network | Must Implement | Draft |

---

# 4. API Contract Responsibilities

API Contracts are responsible for:

```text
endpoint boundary definition
request shape
response shape
reference usage
pagination shape where applicable
permission context requirements
policy context requirements
AI context requirements where applicable
human review requirements where applicable
idempotency requirements where applicable
event trace references where applicable
safe error shape
versioning behavior
Codex implementation expectations
```

API Contracts are not responsible for:

```text
service implementation
domain state ownership
database schema
UI behavior
permission grant logic
policy approval logic
official filing execution
external communication delivery by themselves
event emission by API layer
```

Core rule:

```text
API Contracts expose governed access.
Owning services implement behavior.
```

---

# 5. API-to-Service Mapping

| API Contract | Owning Service |
|---|---|
| identity-api-contract.md | Identity Service |
| organization-api-contract.md | Organization Service |
| user-api-contract.md | User Service |
| permission-api-contract.md | Permission Service |
| policy-api-contract.md | Policy Service |
| knowledge-api-contract.md | Knowledge Service |
| brand-api-contract.md | Brand Service |
| trademark-api-contract.md | Trademark Service |
| jurisdiction-api-contract.md | Jurisdiction Service |
| classification-api-contract.md | Classification Service |
| document-api-contract.md | Document Service |
| evidence-api-contract.md | Evidence Service |
| customer-api-contract.md | Customer Service |
| matter-api-contract.md | Matter Service |
| order-api-contract.md | Order Service |
| opportunity-api-contract.md | Opportunity Service |
| workflow-contract-api-contract.md | Workflow Contract Service |
| task-api-contract.md | Task Service |
| event-api-contract.md | Event Service |
| notification-api-contract.md | Notification Service |
| communication-api-contract.md | Communication Service |
| agent-api-contract.md | Agent Service |
| service-provider-api-contract.md | Service Provider Service |
| routing-api-contract.md | Routing Service |
| partner-api-contract.md | Partner Service |
| service-network-api-contract.md | Service Network Service |

Rules:

```text
- API layer must not mutate domain state directly.
- API layer must route behavior to owning service.
- Owning service validates domain state and emits events where applicable.
```

---

# 6. Required Common Contract Usage

Every API Contract must use:

```text
Reference Contract
Error Contract
Versioning Contract
Permission Context Contract
Policy Context Contract
```

API Contracts must additionally use:

```text
Pagination Contract:
  when list/search endpoint exists

Idempotency Contract:
  when create/update/select/apply/send or other duplicate-sensitive operation exists

Audit Context Contract:
  when event_reference_ids or correlation/causation trace is returned

AI Context Contract:
  when AI-assisted output is provided

Human Review Contract:
  when protected action requires accountable review
```

---

# 7. API Operation Categories

Canonical API operation categories:

```text
Create
Read
Update
Search
ValidateReference
Evaluate
Prepare
Preview
Apply
Approve
Select
Send
Archive
DeleteOrDisable
```

Rules:

```text
- Create operations are duplicate-sensitive unless explicitly read-only.
- Protected operations require Permission Context.
- Policy-controlled operations require Policy Context.
- Prepare operations may use AI Context where AI-assisted.
- Approve, Select and Send operations must define Human Review / Permission / Policy gates.
- DeleteOrDisable operations must be explicit and policy controlled.
```

---

# 8. Required Endpoint Boundary Rules

Every API Contract must state:

```text
endpoint path
method
request shape
response shape
required permissions
required policy scopes
idempotency behavior
event trace behavior
error behavior
version behavior
```

API implementation must ensure:

```text
request validation before service mutation
Permission evaluation before protected behavior
Policy evaluation before restricted output/action
owning service delegation for behavior
safe response construction
safe error construction
no direct event emission by API layer
```

---

# 9. API Governance Rules

Every API Contract must preserve:

```text
No database ID exposure.
No restricted data leakage.
No Permission bypass.
No Policy bypass.
No direct domain mutation by API layer.
No direct Event emission by API layer.
No AI protected action execution.
No hidden Human Review requirement.
No duplicate side effects on idempotent replay.
No unsafe error.
No unsupported version accepted silently.
```

---

# 10. API Family Implementation Order

Recommended Codex implementation order:

```text
1. API README
2. API Template
3. Foundation API Contracts
4. Professional API Contracts
5. Business Execution API Contracts
6. Collaboration Network API Contracts
7. API Contract Tests
8. API Index
```

Detailed sequence:

```text
1. identity-api-contract.md
2. organization-api-contract.md
3. user-api-contract.md
4. permission-api-contract.md
5. policy-api-contract.md
6. knowledge-api-contract.md
7. brand-api-contract.md
8. trademark-api-contract.md
9. jurisdiction-api-contract.md
10. classification-api-contract.md
11. document-api-contract.md
12. evidence-api-contract.md
13. customer-api-contract.md
14. matter-api-contract.md
15. order-api-contract.md
16. opportunity-api-contract.md
17. workflow-contract-api-contract.md
18. task-api-contract.md
19. event-api-contract.md
20. notification-api-contract.md
21. communication-api-contract.md
22. agent-api-contract.md
23. service-provider-api-contract.md
24. routing-api-contract.md
25. partner-api-contract.md
26. service-network-api-contract.md
```

---

# 11. Test Coverage Requirements

API Contracts must be verified by:

```text
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
core-specs/contracts/tests/agent-boundary-tests.md where AI-assisted behavior exists
```

Required tests:

```text
request schema tests
response schema tests
reference validation tests
owning service boundary tests
PermissionDenied tests
PolicyRestricted tests
redaction tests
pagination tests where applicable
AI forbidden-action tests where applicable
HumanReviewRequired tests where applicable
idempotency replay and conflict tests where applicable
event ownership and no-direct-emission tests
safe error tests
VersionUnsupported tests
```

---

# 12. API Contract Acceptance Matrix

```yaml
api_contract_acceptance:
  total_domain_api_contracts:
    expected: 26
    required: true

  foundation:
    expected: 6
    required: true

  professional:
    expected: 6
    required: true

  business_execution:
    expected: 9
    required: true

  collaboration_network:
    expected: 5
    required: true

  required_common_contracts:
    references: true
    errors: true
    permission_context: true
    policy_context: true
    versioning: true

  conditional_common_contracts:
    pagination: when_list_or_search_exists
    idempotency: when_duplicate_sensitive
    audit_context: when_event_trace_exists
    ai_context: when_ai_assisted
    human_review: when_review_gated

  required_test_contract:
    api_contract_tests: core-specs/contracts/tests/api-contract-tests.md
```

---

# 13. Codex Implementation Notes

Codex must:

```text
read this API Contracts Index before implementing API contracts
read API Contracts README and Template before writing new API contracts
cite the specific API Contract being implemented
cite related Common Contracts
cite related Service Specs
cite related Object Specs
cite related Event Specs where event trace exists
cite related Agent Specs where AI-assisted behavior exists
route behavior to owning service
use Permission Context before protected behavior
use Policy Context before restricted output/action
use Idempotency Contract for duplicate-sensitive operations
use Pagination Contract for list/search
use Error Contract for every failure path
use Versioning Contract for compatibility
write API Contract Tests before accepting implementation
```

Codex must not:

```text
treat API Contracts as service implementation
mutate domain state in API layer
emit Events from API layer
grant Permission from API layer
approve Policy from API layer
allow AI to execute protected actions
skip Permission/Policy checks
expose database IDs
expose restricted data
ignore idempotency for duplicate-sensitive operations
silently accept unsupported versions
```

---

# 14. Acceptance Criteria

This API Contracts Index is accepted only if:

```text
[ ] It lists all 26 API Contract files.
[ ] It defines Core Lock.
[ ] It groups APIs into Foundation, Professional, Business Execution and Collaboration Network.
[ ] It defines API Contract responsibilities.
[ ] It defines API-to-Service mapping.
[ ] It defines required Common Contract usage.
[ ] It defines API operation categories.
[ ] It defines endpoint boundary rules.
[ ] It defines API governance rules.
[ ] It defines implementation order.
[ ] It defines test coverage requirements.
[ ] It defines API Contract Acceptance Matrix.
[ ] It defines Codex implementation notes.
```

---

# 15. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial API Contracts Index. Defines 26 API Contract inventory, API family grouping, responsibilities, API-to-Service mapping, common contract usage, operation categories, endpoint boundary rules, governance, implementation order, test coverage and Codex expectations. |

---

**End of API Contracts Index**
