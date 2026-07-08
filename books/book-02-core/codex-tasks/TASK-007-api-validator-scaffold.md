# TASK-007 — API Validator Scaffold

**Task ID:** TASK-007  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-007-api-validator-scaffold.md  
**Task Title:** API Validator Scaffold  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md; codex-tasks/TASK-005-idempotency-event-trace.md; codex-tasks/TASK-006-error-versioning-validation.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related API Index:** core-specs/contracts/api/index.md  
**Related Test Contract:** core-specs/contracts/tests/api-contract-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** MVP APIs Level 2/3; Stub APIs Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task creates API validator scaffolds for all 26 MarkOrbit Core API Contracts.

It ensures every API boundary validates:

```text
request shape
response shape
reference usage
permission context
policy context
idempotency where required
pagination where applicable
AI context where applicable
human review where applicable
event trace references
safe errors
versioning
owning service delegation
```

This task does not implement full API business behavior. It creates governed API boundary validation so later MVP execution work can proceed without architecture drift.

---

# 2. Core Lock

```text
API Contracts define governed request and response boundaries.
API layer receives requests and returns safe responses.
Owning services own behavior.
API layer must not mutate domain state directly.
API layer must not emit Events directly.
References are validated by owning services.
Permission and Policy govern protected API actions.
AI-assisted API output must remain bounded by AI Context and Agent Governance.
Human Review gates protected actions where required.
Idempotency prevents duplicate execution.
Errors must remain safe.
Unsupported versions fail closed.
Codex implements API validators.
Codex does not redefine service behavior through API code.
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
core-specs/contracts/api/index.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/common/index.md
```

Codex must also read all API Contracts:

```text
core-specs/contracts/api/identity-api-contract.md
core-specs/contracts/api/organization-api-contract.md
core-specs/contracts/api/user-api-contract.md
core-specs/contracts/api/permission-api-contract.md
core-specs/contracts/api/policy-api-contract.md
core-specs/contracts/api/knowledge-api-contract.md
core-specs/contracts/api/brand-api-contract.md
core-specs/contracts/api/trademark-api-contract.md
core-specs/contracts/api/jurisdiction-api-contract.md
core-specs/contracts/api/classification-api-contract.md
core-specs/contracts/api/document-api-contract.md
core-specs/contracts/api/evidence-api-contract.md
core-specs/contracts/api/customer-api-contract.md
core-specs/contracts/api/matter-api-contract.md
core-specs/contracts/api/order-api-contract.md
core-specs/contracts/api/opportunity-api-contract.md
core-specs/contracts/api/workflow-contract-api-contract.md
core-specs/contracts/api/task-api-contract.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/api/notification-api-contract.md
core-specs/contracts/api/communication-api-contract.md
core-specs/contracts/api/agent-api-contract.md
core-specs/contracts/api/service-provider-api-contract.md
core-specs/contracts/api/routing-api-contract.md
core-specs/contracts/api/partner-api-contract.md
core-specs/contracts/api/service-network-api-contract.md
```

---

# 4. Scope

This task covers API validator scaffolds for all 26 API Contracts.

MVP APIs require stronger validation:

```text
identity
organization
user
permission
policy
customer
brand
trademark
jurisdiction
classification
document
evidence
matter
order
workflow-contract
task
event
communication
```

Stub APIs require safe validator scaffolds:

```text
knowledge
notification
opportunity
partner
agent
service-provider
service-network
routing
```

---

# 5. Out of Scope

This task must not implement:

```text
full domain business logic
database persistence
product UI
external filing integration
payment execution
email/message delivery
full workflow engine
full agent runtime
full policy engine
provider routing optimization
service network marketplace logic
```

API validators may call or reference service hooks, but API layer must not become the service layer.

---

# 6. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/contracts/api/validators/
  identity.py
  organization.py
  user.py
  permission.py
  policy.py
  knowledge.py
  brand.py
  trademark.py
  jurisdiction.py
  classification.py
  document.py
  evidence.py
  customer.py
  matter.py
  order.py
  opportunity.py
  workflow_contract.py
  task.py
  event.py
  notification.py
  communication.py
  agent.py
  service_provider.py
  routing.py
  partner.py
  service_network.py
```

Preferred TypeScript-like shape:

```text
src/core/contracts/api/validators/
  identity.ts
  organization.ts
  user.ts
  permission.ts
  policy.ts
  knowledge.ts
  brand.ts
  trademark.ts
  jurisdiction.ts
  classification.ts
  document.ts
  evidence.ts
  customer.ts
  matter.ts
  order.ts
  opportunity.ts
  workflow-contract.ts
  task.ts
  event.ts
  notification.ts
  communication.ts
  agent.ts
  service-provider.ts
  routing.ts
  partner.ts
  service-network.ts
```

Suggested tests:

```text
tests/contracts/test_api_contract_validators.py
tests/contracts/test_api_service_boundaries.py
tests/contracts/test_api_permission_policy.py
tests/contracts/test_api_idempotency_event.py
tests/contracts/test_api_error_versioning.py
```

---

# 7. Required Validator Behavior

Every API validator must support:

```text
validate_request(...)
validate_response(...)
validate_reference_fields(...)
validate_permission_context(...)
validate_policy_context(...)
validate_version(...)
validate_error_shape(...)
```

Where applicable, API validators must also support:

```text
validate_pagination(...)
validate_idempotency(...)
validate_ai_context(...)
validate_human_review(...)
validate_event_trace(...)
```

Every validator must return controlled success/failure results.

---

# 8. Required API Boundary Rules

API validators must enforce:

```text
request schema is valid
response schema is valid
public references use Reference Contract
raw database IDs are rejected
Permission Context exists for protected behavior
Policy Context exists for policy-controlled behavior
idempotency_key exists for duplicate-sensitive operations
pagination follows Pagination Contract for list/search
AI Context exists for AI-assisted output
Human Review exists or HumanReviewRequired is returned where required
event_reference_ids are trace only
Error Contract is used for failures
Versioning Contract is used for compatibility
```

API validators must not:

```text
mutate domain state
emit Events
create active Tasks directly
send Communications
select providers
approve workflows
submit filings
certify professional truth
```

---

# 9. API-to-Service Boundary Assertions

Codex must implement or test boundary assertions:

```text
Identity API routes to Identity Service.
Organization API routes to Organization Service.
User API routes to User Service.
Permission API routes to Permission Service.
Policy API routes to Policy Service.
Customer API routes to Customer Service.
Brand API routes to Brand Service.
Trademark API routes to Trademark Service.
Jurisdiction API routes to Jurisdiction Service.
Classification API routes to Classification Service.
Document API routes to Document Service.
Evidence API routes to Evidence Service.
Matter API routes to Matter Service.
Order API routes to Order Service.
Workflow Contract API routes to Workflow Contract Service.
Task API routes to Task Service.
Event API routes to Event Service.
Communication API routes to Communication Service.
```

Stub APIs should route to safe stubs or return controlled not-implemented behavior:

```text
Knowledge API
Notification API
Opportunity API
Partner API
Agent API
Service Provider API
Service Network API
Routing API
```

---

# 10. MVP API Validators

## 10.1 Must Implement Strong Validators

These APIs must have Level 2/3 validator coverage:

```text
identity-api-contract
organization-api-contract
user-api-contract
permission-api-contract
policy-api-contract
customer-api-contract
brand-api-contract
trademark-api-contract
jurisdiction-api-contract
classification-api-contract
document-api-contract
evidence-api-contract
matter-api-contract
order-api-contract
workflow-contract-api-contract
task-api-contract
event-api-contract
communication-api-contract
```

Required coverage:

```text
request shape
response shape
reference validation
permission context
policy context
safe errors
versioning
idempotency where create/apply exists
pagination where list/search exists
event trace where events are returned
```

## 10.2 Stub Validators

These APIs require Level 1/2 stubs:

```text
knowledge-api-contract
notification-api-contract
opportunity-api-contract
partner-api-contract
agent-api-contract
service-provider-api-contract
service-network-api-contract
routing-api-contract
```

Stub coverage:

```text
request/response schema validation
reference validation
permission/policy context validation
VersionUnsupported behavior
safe NotImplemented where behavior is out of MVP scope
no production side effects
```

---

# 11. Required Operation Categories

API validators should cover operation categories defined by each API Contract.

Canonical operation categories:

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

MVP emphasis:

```text
Create
Read
Search
ValidateReference
Prepare
Preview
Apply
Review
```

Not required in MVP unless already specified:

```text
hard delete
bulk import
bulk export
external sync
payment execution
official submission
provider settlement
public open API
```

---

# 12. Idempotency Requirements

Duplicate-sensitive API operations must require:

```text
idempotency_key
```

Required duplicate-sensitive operations:

```text
create Customer
create Brand
create Trademark
create Matter
create Order
create Document
create Evidence
create Task
create Communication
workflow apply
routing selection stub if exposed
```

Tests must assert:

```text
missing idempotency_key returns IdempotencyKeyRequired
same key + same request replays safely where supported
same key + different request returns IdempotencyConflict
```

---

# 13. Event Requirements

API validators must ensure:

```text
API layer does not emit Events directly.
API response may include event_reference_ids only as trace.
event_reference_ids must follow Reference Contract.
event_reference_ids must not trigger commands.
Event visibility follows Permission and Policy.
```

Required test:

```text
api_layer_does_not_emit_events_directly
```

---

# 14. AI and Human Review Requirements

Where API output is AI-assisted:

```text
AI Context must exist.
capability_scope must be valid.
source_scope must be valid.
policy_omissions_disclosed must be true where restricted sources are omitted.
AI must not claim approval, submission, certification, completion or external send.
```

Where protected action requires review:

```text
human_review_reference_id must be valid.
missing review returns HumanReviewRequired.
Human Review must not execute downstream action by itself.
```

---

# 15. Required Fixtures

Use fixtures from TASK-002:

```text
MVP API request fixtures
MVP API response fixtures
invalid reference request
permission denied request
policy restricted request
idempotency missing key request
idempotency conflict request
unsupported version request
AI forbidden action request
human review required request
event visibility restricted request
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline ad hoc production-like fixtures.
```

---

# 16. Required Tests

This task must implement tests for:

```text
all 26 API validator files exist or are intentionally scaffolded
MVP API validators enforce request shape
MVP API validators enforce response shape
reference validation rejects database IDs
PermissionDenied blocks protected actions
PolicyRestricted blocks or redacts policy-controlled output
idempotency_key required for duplicate-sensitive operations
VersionUnsupported returned for unsupported versions
safe error shape used
pagination behavior for list/search APIs
AI Context required for AI-assisted output
HumanReviewRequired returned where review missing
event_reference_ids are trace only
API layer does not emit Events directly
API layer does not mutate domain state directly
API routes behavior to owning service or stub
```

Required test source:

```text
core-specs/contracts/tests/api-contract-tests.md
```

---

# 17. Integration Points for Later Tasks

This task must expose validator scaffolds usable by:

```text
TASK-008-workflow-validator-scaffold
TASK-010-mvp-execution-spine
```

Expected interfaces should support:

```text
validate_api_request(...)
validate_api_response(...)
validate_api_operation_boundary(...)
assert_api_routes_to_owning_service(...)
assert_api_does_not_emit_events(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 18. Forbidden Shortcuts

Codex must not:

```text
skip any of the 26 API validator scaffolds
only implement MVP APIs while leaving non-MVP APIs unacknowledged
mutate domain state in API validators
emit Events from API validators
create Tasks directly from API layer
send Communications directly from API layer
select providers directly from API layer
treat valid references as permission
default Permission to allowed
default Policy to allowed
skip idempotency validation for create/apply
skip unsupported version tests
expose raw database IDs
use production data fixtures
```

---

# 19. Acceptance Criteria

This task is complete only if:

```text
[ ] API validator scaffold exists.
[ ] All 26 API Contracts have validator files or explicit scaffold entries.
[ ] MVP API validators validate request shape.
[ ] MVP API validators validate response shape.
[ ] Reference validation is enforced.
[ ] Permission Context is enforced for protected actions.
[ ] Policy Context is enforced for policy-controlled behavior.
[ ] Idempotency is enforced for duplicate-sensitive operations.
[ ] Pagination is validated where list/search exists.
[ ] AI Context is validated where AI-assisted output exists.
[ ] Human Review is validated where review gates exist.
[ ] Event references are trace only.
[ ] API layer no-direct-event-emission is tested.
[ ] API layer no-direct-domain-mutation is tested.
[ ] Safe errors are used.
[ ] Unsupported versions fail closed.
[ ] Tests pass.
```

---

# 20. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- API validator scaffold implemented.
- Files added or changed.
- Which API validators are Level 2/3.
- Which API validators are Level 1/2 stubs.
- Which source specs were used.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- API layer does not mutate domain state directly.
- API layer does not emit Events directly.
- References use Reference Contract.
- Permission/Policy fail closed.
- Idempotency enforced where required.
- AI Context enforced where applicable.
- Human Review gates preserved.
- Errors are safe.
- Unsupported versions fail closed.

Deferred
- Full API behavior remains for MVP execution spine or later tasks.
- External integrations remain out of scope.
- Next task recommended.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-007. Defines API validator scaffold implementation scope, required source files, MVP/stub API depth, boundary rules, service routing assertions, idempotency, event, AI/human review requirements, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-007 — API Validator Scaffold**
