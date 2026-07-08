# MVP Cut v0.1

**Spec ID:** B02-IMPLEMENTATION-MVP-CUT-V0.1  
**Spec Type:** MVP Implementation Cut  
**Spec File:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Layers:** Domains; Objects; Services; Events; APIs; Agents; Contracts; Workflows; Tests; Codex Tasks  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Cut Version:** v0.1  
**MVP Phase:** Phase 0–1 — Implementation Scope Lock  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines the first executable MVP cut for MarkOrbit Core.

Its purpose is to prevent Book 02 from being implemented as a large set of shallow stubs or an overbuilt platform before the first working execution spine exists.

This file answers:

```text
What must be built now?
What should be stubbed now?
What should remain document-only?
What must be deferred?
What must never be implemented in MVP?
```

This MVP cut applies to:

```text
Core Domains
Core Objects
Core Services
API Contracts
Workflow Specs
Workflow Contracts
Event Specs
Agent Specs
Common Contracts
Test Contracts
Codex Tasks
```

---

# 2. Core Lock

```text
MVP Cut defines implementation scope.
Core architecture remains larger than MVP.
MVP must build a working execution spine, not the whole platform.
Must Build Now items require implementation and tests.
Stub Now items require safe interfaces and boundary tests.
Document Only items remain specification references.
Defer items must not block MVP.
Never items must not be implemented in MVP.
Codex implements only the scoped MVP cut.
Codex does not redefine architecture.
```

---

# 3. MVP Strategy

The MVP should prove that MarkOrbit Core can support a governed trademark service execution flow.

The first executable spine is:

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

This MVP is not intended to prove every future platform feature.

It is intended to prove:

```text
Core ownership boundaries work.
API access is governed.
Workflow coordination works.
Tasks are created by Task Service.
Events preserve trace.
AI assistance stays bounded.
Permission and Policy fail closed.
Idempotency prevents duplicate execution.
Errors are safe.
Codex can implement without architecture drift.
```

---

# 4. MVP Scope Categories

All items are classified into one of five categories:

```text
Must Build Now
Stub Now
Document Only
Defer
Never in MVP
```

## 4.1 Must Build Now

Meaning:

```text
Must have real implementation, fixtures and tests in MVP.
```

## 4.2 Stub Now

Meaning:

```text
Must expose safe interface, reference shape or validation hook.
May return controlled placeholder behavior.
Must not fake full business behavior.
```

## 4.3 Document Only

Meaning:

```text
Specification remains in Book 02.
No MVP implementation required.
May be cited as future architecture.
```

## 4.4 Defer

Meaning:

```text
Valid future feature.
Not needed for MVP.
Must not block MVP.
```

## 4.5 Never in MVP

Meaning:

```text
Must not be implemented in MVP because it creates unacceptable architecture, legal, security or operational risk.
```

---

# 5. Must Build Now

## 5.1 Domains

```text
Identity
Organization
User
Permission
Policy
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
```

These domains form the minimum working execution spine.

## 5.2 Objects

Must implement object skeletons and validation for:

```text
identity-object
organization-object
user-object
permission-object
policy-object
customer-object
brand-object
trademark-object
jurisdiction-object
classification-object
document-object
evidence-object
matter-object
order-object
workflow-contract-object
task-object
event-object
communication-object
```

Object implementation requirement:

```text
public reference ID
type
status where applicable
core metadata
audit metadata
permission/policy visibility fields where applicable
version field where applicable
```

## 5.3 Services

Must implement service skeletons with real boundary behavior for:

```text
Identity Service
Organization Service
User Service
Permission Service
Policy Service
Customer Service
Brand Service
Trademark Service
Jurisdiction Service
Classification Service
Document Service
Evidence Service
Matter Service
Order Service
Workflow Contract Service
Task Service
Event Service
Communication Service
```

Minimum service behavior:

```text
create where required
read where required
search/list where required
validate_reference
basic status transition where required
permission check hook
policy check hook
safe error return
event trace handoff where applicable
idempotency handling where duplicate-sensitive
```

## 5.4 Common Contracts

Must implement:

```text
Reference Contract
Error Contract
Permission Context Contract
Policy Context Contract
Idempotency Contract
Audit Context Contract
Versioning Contract
Pagination Contract
AI Context Contract
Human Review Contract
```

Minimum implementation depth:

```text
schema validation
safe helpers
fail-closed behavior
test fixtures
negative tests
```

## 5.5 API Contracts

Must implement or scaffold validators for these MVP APIs:

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

Minimum API behavior:

```text
request validation
response validation
reference validation
permission context validation
policy context validation
idempotency validation for duplicate-sensitive operations
safe error behavior
version validation
no direct domain mutation in API layer
no direct event emission in API layer
```

## 5.6 Workflows

Must implement workflow specifications and contract validation for:

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Minimum workflow behavior:

```text
preview
apply
step validation
task plan generation
human review checkpoint validation
AI assistance boundary validation
permission/policy validation
idempotency validation
event trace reference validation
safe error behavior
```

## 5.7 Events

Must implement event records or event fixtures for:

```text
customer-created
brand-created
trademark-created
matter-created
order-created
document-created
document-attached
evidence-created
task-created
task-updated
task-completed
communication-created
communication-reviewed
communication-sent
workflow-contract-previewed
workflow-contract-applied
permission-evaluated
policy-evaluated
```

Minimum event behavior:

```text
event_reference_id
event_type
source_service
subject_reference_id
correlation_id
causation_event_reference_id where applicable
created_at
visibility policy hook
safe payload
schema_version
```

## 5.8 Agents

Must implement only boundary-safe scaffolds for:

```text
Knowledge Agent
Task Agent
Communication Agent
Workflow Agent
Audit Agent
```

Allowed MVP behavior:

```text
summarize
draft
classify
compare
suggest
identify gaps
prepare task plan
prepare communication draft
prepare workflow preview explanation
summarize audit trace
```

Forbidden MVP behavior:

```text
approve
send
select
submit
certify
complete
mutate protected state
emit events
```

## 5.9 Tests

Must implement tests for:

```text
common-contract-tests
api-contract-tests for MVP APIs
workflow-contract-tests for MVP workflows
agent-boundary-tests for MVP agents
permission-policy-tests
idempotency-event-tests
error-versioning-tests
```

Minimum negative tests:

```text
invalid reference rejected
database ID not exposed
PermissionDenied blocks protected action
PolicyRestricted blocks or redacts
AI forbidden action rejected
HumanReviewRequired blocks gated action
missing idempotency_key rejected
idempotency conflict rejected
duplicate replay creates no duplicate effects
API layer does not emit Events directly
Workflow layer does not emit Events directly
Agent layer does not emit Events directly
event reference is not command
unsafe error leakage blocked
unsupported version fails closed
```

---

# 6. Stub Now

Stub Now items must exist as safe interfaces or placeholder implementations, but must not be overbuilt.

## 6.1 Domains

```text
Knowledge
Notification
Opportunity
Partner
Agent
Service Provider
Service Network
Routing
```

## 6.2 Services

Stub services:

```text
Knowledge Service
Notification Service
Opportunity Service
Partner Service
Agent Service
Service Provider Service
Service Network Service
Routing Service
```

Stub requirements:

```text
reference validation
basic read/search where needed
safe error behavior
permission/policy hooks
version validation
no complex optimization
no production external integration
```

## 6.3 APIs

Stub API validators:

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

Stub behavior:

```text
validate request shape
validate response shape
validate references
fail safely for unsupported operations
return NotImplemented or controlled placeholder only where allowed
```

## 6.4 Workflows

Stub workflow specs and validators:

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

Stub requirements:

```text
preview-only or validation-only
no production execution
no official filing action
no external communication send
no provider final selection
```

## 6.5 Agents

Stub only:

```text
Routing Agent
advanced Agent Registry runtime
full AI orchestration
```

Stub requirement:

```text
capability registry may exist
agent execution must remain non-production and boundary-tested
```

---

# 7. Document Only

The following remain documented in Book 02 but do not require MVP implementation.

```text
full policy engine
full agent runtime orchestration
full workflow engine
external official filing integrations
foreign associate live network integrations
payment execution
provider marketplace settlement
advanced analytics
advanced service network optimization
multi-product app marketplace
public developer API portal
AI autonomous workflow execution
official deadline certification automation
professional registrability decision automation
```

Document-only items may appear in specs, but Codex must not implement them unless a later task explicitly moves them into scope.

---

# 8. Defer

The following are valid future work but deferred from MVP:

```text
renewal production workflow
assignment production workflow
office action response production workflow
evidence review production workflow
provider routing production workflow
foreign agent onboarding automation
partner-facing mini program
client self-service filing portal
global jurisdiction rule automation
official fee calculation engine
trademark watch/monitoring
bulk opportunity generation
service provider scoring
communication delivery integrations
document e-signature integration
external storage integrations
billing and invoice automation
```

Deferred items must not block MVP.

---

# 9. Never in MVP

The following must not be implemented in MVP:

```text
AI submitting official filings
AI certifying legal deadlines
AI certifying trademark registrability
AI deciding evidence sufficiency as professional truth
AI selecting service provider as final decision
AI sending external communication without human review
API layer mutating domain state directly
Workflow layer creating active Tasks outside Task Service
Workflow layer emitting domain Events directly
Agent layer emitting Events directly
Event references triggering commands
Permission bypass for convenience
Policy bypass for convenience
production data fixtures
raw database IDs in public responses
unsafe stack traces in API responses
silent unsupported-version acceptance
silent historical-version rewriting
```

These items are not implementation shortcuts. They are architecture violations.

---

# 10. MVP Workflow Cut

## 10.1 Customer Intake Workflow

Must support:

```text
create or link Customer
create or link Brand
create Opportunity or Matter candidate
create Order candidate where applicable
attach intake Documents
prepare Task plan
preserve Event trace
require Permission and Policy
support AI-assisted summary only
```

Must not:

```text
approve legal strategy
submit official filing
send external communication automatically
create active Tasks outside Task Service
```

## 10.2 Trademark Application Workflow

Must support:

```text
create or link Trademark
link Brand
link Jurisdiction
prepare Classification suggestions
attach Documents
prepare Evidence if applicable
create Matter / Order execution context
prepare Task plan
preserve Event trace
support AI-assisted classification draft
require Human Review before professional conclusion
```

Must not:

```text
certify registrability
submit official application
finalize goods/services without human review
certify official deadline
```

## 10.3 Communication Review Workflow

Must support:

```text
create Communication draft
classify communication type
compare source context
require Human Review
prepare safe outbound draft
record review state
preserve Event trace
support AI-assisted drafting and comparison
```

Must not:

```text
send external communication without human review
represent AI draft as approved professional output
bypass Policy redaction
```

---

# 11. MVP API Cut

## 11.1 Required API Operations

Minimum required operation categories:

```text
create
read
search/list
validate_reference
preview
apply
prepare
review
```

## 11.2 Not Required in MVP

```text
delete
hard delete
bulk import
bulk export
external sync
payment execution
official submission
provider settlement
public open API
```

## 11.3 Required API Safety

All MVP API operations must enforce:

```text
Reference Contract
Error Contract
Permission Context
Policy Context
Versioning
Idempotency for duplicate-sensitive operations
Pagination for list/search
safe Event trace references
```

---

# 12. MVP Governance Depth

| Governance Capability | MVP Category | MVP Depth |
|---|---|---|
| References | Must Build Now | Level 3 — real enforcement |
| Errors | Must Build Now | Level 3 — real enforcement |
| Permission | Must Build Now | Level 2/3 — service hook plus core enforcement for protected actions |
| Policy | Must Build Now | Level 1/2 — schema validation plus service hook |
| Idempotency | Must Build Now | Level 3 for create/apply |
| Audit Context | Must Build Now | Level 2 — trace hook |
| Events | Must Build Now | Level 2 — persisted or fixture-backed event trace |
| Versioning | Must Build Now | Level 1 — schema validation and unsupported version failure |
| Pagination | Must Build Now | Level 2 — basic list/search support |
| AI Context | Must Build Now | Level 1 — schema validation and boundary metadata |
| Human Review | Must Build Now | Level 2 — review gate validation |
| Agent Runtime | Stub Now | Level 1 — capability registry and boundary tests |
| Workflow Engine | Stub Now | Level 1/2 — preview/apply validators, not full engine |
| Policy Engine | Document Only | Level 0/1 — no full rule engine |

Level definitions:

```text
Level 0 — documented only
Level 1 — schema validation
Level 2 — service hook
Level 3 — real enforcement
Level 4 — audited production enforcement
```

---

# 13. Codex Task Cut

MVP Codex tasks should be ordered as follows:

```text
TASK-001-common-contract-foundation
TASK-002-contract-fixture-system
TASK-003-common-contract-tests
TASK-004-permission-policy-hooks
TASK-005-idempotency-event-trace
TASK-006-error-versioning-validation
TASK-007-api-validator-scaffold
TASK-008-workflow-validator-scaffold
TASK-009-agent-boundary-tests
TASK-010-mvp-execution-spine
```

Codex must not start TASK-010 before TASK-001 through TASK-006 are complete or intentionally stubbed.

---

# 14. MVP Acceptance Criteria

The MVP cut is accepted only if:

```text
[ ] Must Build Now domains are implemented or scaffolded with tests.
[ ] Must Build Now objects have public reference IDs.
[ ] Must Build Now services own behavior.
[ ] Must Build Now API validators exist.
[ ] Customer Intake Workflow supports preview/apply.
[ ] Trademark Application Workflow supports preview/apply.
[ ] Communication Review Workflow supports preview/apply.
[ ] Permission and Policy fail closed.
[ ] AI forbidden actions are blocked.
[ ] Human Review gates protected actions.
[ ] Idempotency replay and conflict are tested.
[ ] Event trace exists and is not command.
[ ] API layer does not emit Events directly.
[ ] Workflow layer does not emit Events directly.
[ ] Agent layer does not emit Events directly.
[ ] Errors are safe.
[ ] Unsupported versions fail closed.
[ ] Deferred items do not block MVP.
[ ] Never in MVP items are not implemented.
```

---

# 15. Review Checklist Before Codex Implementation

Before implementation begins:

```text
[ ] core-specs/TRACEABILITY.md is read.
[ ] this MVP Cut is read.
[ ] implementation-depth-matrix.md is read or created.
[ ] DEVELOPER_START_HERE.md is read or created.
[ ] CODEX-TASK-INDEX.md is read or created.
[ ] Contract README, Index and MANIFEST are read.
[ ] Common Contracts are read.
[ ] Test Contracts are read.
[ ] First Codex task is scoped to TASK-001 only.
```

---

# 16. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial MVP Cut. Defines Must Build Now, Stub Now, Document Only, Defer and Never in MVP categories, MVP workflow/API/governance/task cuts and acceptance criteria. |

---

**End of MVP Cut v0.1**
