# API Contract Validation

**Spec ID:** B02-VALIDATION-API-CONTRACT  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/api-contract-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Domain/Object/Service Validation:** core-specs/validation/domain-object-service-validation.md  
**Related API Index:** core-specs/contracts/api/index.md  
**Related Test Contract:** core-specs/contracts/tests/api-contract-tests.md  
**Related Codex Task:** codex-tasks/TASK-007-api-validator-scaffold.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** MVP APIs Level 2/3; Stub APIs Level 1/2  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate MarkOrbit Core API Contracts.

API Contract Validation checks whether API boundaries are correctly specified, governed, traceable and ready for Codex implementation.

It ensures that API Contracts:

```text
expose governed access
do not own business behavior
route to owning services
validate request and response shape
use Common Contracts
enforce Permission and Policy
enforce Idempotency where required
preserve Event trace as trace only
return safe Errors
fail closed on unsupported versions
```

This validation is required before implementing API validators or the MVP execution spine.

---

# 2. Core Lock

```text
API Contracts expose governed access.
API layer validates and routes.
API layer does not own domain behavior.
API layer does not mutate domain state directly.
API layer does not emit Events directly.
API layer does not create active Tasks directly.
Owning services own behavior.
Permission and Policy govern protected API actions.
Idempotency protects duplicate-sensitive API operations.
Event references are trace only.
Errors must remain safe.
Unsupported versions must fail closed.
Codex implements API validators from API Contracts.
Codex does not redefine service behavior through API code.
```

---

# 3. Validation Scope

This validation covers all 26 API Contracts:

```text
identity-api-contract
organization-api-contract
user-api-contract
permission-api-contract
policy-api-contract
knowledge-api-contract
brand-api-contract
trademark-api-contract
jurisdiction-api-contract
classification-api-contract
document-api-contract
evidence-api-contract
customer-api-contract
matter-api-contract
order-api-contract
opportunity-api-contract
workflow-contract-api-contract
task-api-contract
event-api-contract
notification-api-contract
communication-api-contract
agent-api-contract
service-provider-api-contract
routing-api-contract
partner-api-contract
service-network-api-contract
```

It validates:

```text
file existence
domain mapping
owning service mapping
request/response shape
reference usage
permission/policy coverage
idempotency coverage
pagination coverage
AI Context coverage
Human Review coverage
Event trace usage
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
core-specs/contracts/api/index.md
core-specs/contracts/common/index.md
core-specs/contracts/tests/api-contract-tests.md
codex-tasks/TASK-007-api-validator-scaffold.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/domain-object-service-validation.md
```

Validation must also inspect all API Contract files under:

```text
core-specs/contracts/api/
```

---

# 5. API Contract File Existence Checks

Validate:

```text
[ ] All 26 API Contract files exist.
[ ] API index lists all 26 API Contracts.
[ ] API Contract naming is consistent.
[ ] No duplicate API Contract represents the same domain.
[ ] No MVP domain is missing an API Contract.
[ ] Stub Now domains have API Contracts or explicit stub contracts.
```

Blocked if:

```text
Must Build Now domain API Contract missing.
API index omits an API Contract.
API Contract file exists but is not indexed.
```

---

# 6. MVP API Depth Classification

Validate depth according to the Implementation Depth Matrix.

## 6.1 MVP APIs — Level 2/3

These API Contracts require stronger validation:

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

Required:

```text
request validation
response validation
service boundary mapping
Permission/Policy where protected
Idempotency where create/apply exists
safe Errors
Versioning
negative tests
```

## 6.2 Stub APIs — Level 1/2

These API Contracts require safe stubs:

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

Required:

```text
schema validation
reference validation
safe not-implemented or preview-only behavior
Permission/Policy hooks where protected
safe errors
unsupported version failure
no production side effects
```

Architecture violation:

```text
Stub API silently performs production behavior.
Routing API selects final provider in MVP.
Notification API sends real external notification in MVP.
Agent API enables protected autonomous execution in MVP.
```

---

# 7. API-to-Domain Mapping Checks

Validate:

```text
[ ] Each API Contract maps to exactly one primary domain.
[ ] Cross-domain references are explicit.
[ ] API Contract does not create ambiguous ownership.
[ ] API Contract does not merge unrelated domains.
[ ] API Contract does not introduce new domain concepts.
```

Examples:

```text
customer-api-contract → Customer Domain
trademark-api-contract → Trademark Domain
workflow-contract-api-contract → Workflow Contract Domain
event-api-contract → Event Domain
communication-api-contract → Communication Domain
```

Failure condition:

```text
API Contract introduces unapproved domain.
API Contract mixes Matter and Order ownership without service boundary.
API Contract treats Capability as new domain API without architecture review.
```

---

# 8. API-to-Service Mapping Checks

Validate:

```text
[ ] API Contract maps to owning service.
[ ] API Contract describes service delegation.
[ ] API Contract does not own behavior.
[ ] API Contract does not mutate objects directly.
[ ] API Contract does not emit Events directly.
[ ] API Contract does not create active Tasks directly.
```

Required MVP mapping:

```text
Identity API → Identity Service
Organization API → Organization Service
User API → User Service
Permission API → Permission Service
Policy API → Policy Service
Customer API → Customer Service
Brand API → Brand Service
Trademark API → Trademark Service
Jurisdiction API → Jurisdiction Service
Classification API → Classification Service
Document API → Document Service
Evidence API → Evidence Service
Matter API → Matter Service
Order API → Order Service
Workflow Contract API → Workflow Contract Service
Task API → Task Service
Event API → Event Service
Communication API → Communication Service
```

Blocked if:

```text
MVP API has no owning service mapping.
API Contract states direct mutation without service owner.
```

---

# 9. Common Contract Usage Checks

Each API Contract must use relevant Common Contracts.

Validate:

```text
[ ] Reference Contract for all public object references.
[ ] Error Contract for all failures.
[ ] Versioning Contract for request/response compatibility.
[ ] Permission Context for protected actions.
[ ] Policy Context for policy-controlled data/output.
[ ] Idempotency Contract for duplicate-sensitive create/apply operations.
[ ] Pagination Contract for list/search operations.
[ ] Audit Context for trace/correlation.
[ ] AI Context for AI-assisted output.
[ ] Human Review Contract for protected professional/external-facing actions.
```

Architecture violations:

```text
raw database IDs used as public references
errors are raw exception strings
protected action without Permission/Policy
create/apply without Idempotency
unsupported version silently accepted
```

---

# 10. Request Validation Checks

Every API Contract must define or imply request validation.

Checks:

```text
[ ] Required fields are listed.
[ ] Optional fields are listed.
[ ] Reference fields specify expected reference type.
[ ] Version fields are required.
[ ] Permission/Policy context requirements are specified.
[ ] Idempotency key is required where duplicate-sensitive.
[ ] AI Context is required where AI-assisted.
[ ] Human Review is required where protected.
[ ] Payload size or attachment limits are acknowledged where relevant.
[ ] Invalid requests return safe Error Contract shape.
```

Blocked if:

```text
MVP create/apply request lacks idempotency requirement.
MVP protected request lacks Permission/Policy context.
MVP request uses raw database ID.
```

---

# 11. Response Validation Checks

Every API Contract must define or imply response validation.

Checks:

```text
[ ] Response uses public references.
[ ] Response does not expose database IDs.
[ ] Response includes version context where required.
[ ] Response includes event_reference_ids only as trace.
[ ] Response marks AI-assisted output where applicable.
[ ] Response marks human_review_required where applicable.
[ ] Response sets restricted_fields_omitted where redaction occurs.
[ ] Response omits total_count where Policy restricts counts.
[ ] Response uses safe Error Contract for failures.
```

Architecture violation:

```text
response leaks database ID
response leaks restricted field after PolicyRestrictedRedact
response exposes hidden object existence where NonDisclosure applies
response event_reference_id triggers command semantics
```

---

# 12. Operation Category Checks

Validate operations in each API Contract.

Common operation categories:

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
Review
Archive
Disable
```

Checks:

```text
[ ] Each operation has clear action boundary.
[ ] Each operation maps to owning service.
[ ] Each protected operation maps to Permission/Policy.
[ ] Each state-changing operation maps to Event trace.
[ ] Each duplicate-sensitive operation maps to Idempotency.
[ ] Each operation has failure conditions.
[ ] Each operation has version behavior.
```

Forbidden in MVP unless explicitly scoped:

```text
official submission
external send
payment execution
provider final selection
professional certification by AI
bulk production import
hard delete
```

---

# 13. Idempotency Checks

Validate that duplicate-sensitive API operations require Idempotency.

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

Checks:

```text
[ ] idempotency_key required.
[ ] Missing key returns IdempotencyKeyRequired.
[ ] Same key + same semantic request safely replays.
[ ] Same key + different semantic request returns IdempotencyConflict.
[ ] Replay does not duplicate objects, Tasks, Communications or Events.
```

Blocked if:

```text
MVP duplicate-sensitive operation has no Idempotency requirement.
```

---

# 14. Permission / Policy Checks

Validate:

```text
[ ] Protected API actions require Permission.
[ ] Policy-controlled output requires Policy.
[ ] UnknownPermission fails closed.
[ ] UnknownPolicy fails closed where policy-controlled.
[ ] PermissionAllowed alone is not enough if Policy restricts.
[ ] PolicyAllowed alone is not enough if Permission denies.
[ ] Redaction sets restricted_fields_omitted.
[ ] Non-disclosure can return safe NotFound.
```

Required protected areas:

```text
customer data
trademark data
documents
evidence
matter/order execution data
task data
communication drafts
event trace
AI-assisted source use
cross-organization access
service provider data where exposed
```

---

# 15. Pagination Checks

List/search APIs must use Pagination Contract.

Checks:

```text
[ ] limit is validated.
[ ] cursor is validated.
[ ] next_cursor is safe.
[ ] items use public references.
[ ] total_count is omitted where Policy restricts count visibility.
[ ] pagination does not leak hidden object count.
```

Applies to:

```text
Customer search
Trademark search
Document search
Evidence search
Matter search
Order search
Task search
Event search
Communication search
Partner/Provider/Network search stubs where exposed
```

---

# 16. Event Trace Checks

Validate:

```text
[ ] API layer does not emit Events directly.
[ ] API Contract may return event_reference_ids only as trace.
[ ] event_reference_ids follow Reference Contract.
[ ] Event visibility follows Permission/Policy.
[ ] Event references are not commands.
[ ] API failures do not expose hidden event data.
```

Architecture violation:

```text
API Contract says event_reference_id triggers workflow apply.
API Contract emits Event directly.
API Contract lets client create Event record except through Event Service contract.
```

---

# 17. AI Context Checks

Where API Contract allows AI-assisted output, validate:

```text
[ ] AI Context is required.
[ ] agent_reference_id or capability scope is present where applicable.
[ ] source_scope is present.
[ ] policy_omissions_disclosed is true where restricted sources are omitted.
[ ] AI output is marked draft/suggestion/non-final where applicable.
[ ] AI cannot approve, send, select, submit, certify, complete or mutate protected state.
```

Applies to APIs exposing:

```text
classification suggestions
communication drafts
workflow preview explanations
task plan suggestions
knowledge summaries
routing candidate previews
audit summaries
```

---

# 18. Human Review Checks

Validate that protected professional or external-facing API operations require Human Review where applicable.

Required gates:

```text
external communication send or approval
classification finalization
evidence sufficiency conclusion
filing readiness confirmation
workflow apply where protected
provider final selection if exposed
```

Checks:

```text
[ ] Missing review returns HumanReviewRequired.
[ ] human_review_reference_id is validated.
[ ] Human Review does not execute downstream action by itself.
[ ] Human Review does not bypass Permission.
[ ] Human Review does not bypass Policy.
```

---

# 19. Error / Versioning Checks

Validate:

```text
[ ] API Contract uses controlled error codes.
[ ] Errors do not expose stack traces.
[ ] Errors do not expose database IDs.
[ ] Errors do not expose restricted data.
[ ] Errors do not expose policy/permission internals.
[ ] Errors preserve correlation_id.
[ ] retryable flag is explicit.
[ ] contract_version is required.
[ ] schema_version is required where applicable.
[ ] unsupported versions return VersionUnsupported.
[ ] deprecated versions are not silently rewritten.
```

---

# 20. Test Traceability Checks

Validate:

```text
[ ] API Contract maps to api-contract-tests.md.
[ ] MVP API maps to TASK-007.
[ ] MVP API has positive and negative tests.
[ ] PermissionDenied is tested where protected.
[ ] PolicyRestricted is tested where policy-controlled.
[ ] IdempotencyKeyRequired and IdempotencyConflict are tested where duplicate-sensitive.
[ ] VersionUnsupported is tested.
[ ] Safe error behavior is tested.
[ ] API no-direct-event-emission is tested.
[ ] API no-direct-domain-mutation is tested.
```

Blocked if:

```text
MVP API Contract lacks test mapping.
MVP API protected operation lacks negative tests.
```

---

# 21. Validation Procedure

Perform validation in this order:

```text
1. Confirm API index exists.
2. Confirm all 26 API Contract files exist.
3. Confirm MVP/stub depth classification.
4. Validate API-to-domain mapping.
5. Validate API-to-service mapping.
6. Validate Common Contract usage.
7. Validate request shape rules.
8. Validate response shape rules.
9. Validate operation categories.
10. Validate Idempotency coverage.
11. Validate Permission/Policy coverage.
12. Validate Pagination coverage.
13. Validate Event trace boundary.
14. Validate AI Context boundary.
15. Validate Human Review gates.
16. Validate Error/Versioning.
17. Validate test traceability.
18. Classify findings.
19. Produce validation report.
```

---

# 22. Finding Classification

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
Blocked = Must Build Now API missing required mapping or contract behavior.
Architecture Violation = API boundary breach or unsafe governance.
Warning = Stub/future API incomplete but safe.
Out of Scope = valid but outside MVP.
Deferred = future API behavior intentionally postponed.
Pass = sufficient for current depth.
```

---

# 23. Required Evidence

Every finding must include:

```text
API Contract
domain
owning service
operation
source file
missing or inconsistent rule
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: customer-api-contract create operation lacks idempotency_key.
Status: Blocked
API Contract: customer-api-contract
Operation: Create Customer
Required Fix: Add Idempotency requirement and tests.
Codex Impact: Block TASK-007 and TASK-010.
```

---

# 24. Architecture Violation Triggers

The following always fail validation:

```text
API layer mutates domain state directly.
API layer emits Events directly.
API layer creates active Tasks directly.
API layer sends Communication directly.
API layer selects final provider directly.
API layer submits official filing.
API layer certifies registrability, deadlines or evidence sufficiency.
API Contract uses raw database IDs publicly.
API Contract lacks Permission/Policy for protected action.
API Contract accepts unsupported version silently.
API Contract exposes unsafe errors.
API Contract treats Event reference as command.
AI-assisted API operation executes protected action.
```

---

# 25. Acceptance Criteria

API Contract Validation passes only if:

```text
[ ] Required source files exist.
[ ] All 26 API Contracts exist or are explicitly documented.
[ ] API index lists all API Contracts.
[ ] MVP APIs have Level 2/3 validation requirements.
[ ] Stub APIs have safe Level 1/2 validation requirements.
[ ] Each API maps to a domain.
[ ] Each MVP API maps to owning service.
[ ] Common Contracts are referenced where applicable.
[ ] Request validation rules are defined.
[ ] Response validation rules are defined.
[ ] Protected operations map to Permission/Policy.
[ ] Duplicate-sensitive operations map to Idempotency.
[ ] List/search operations map to Pagination.
[ ] Event references are trace only.
[ ] AI-assisted operations map to AI Context.
[ ] Human Review gates are preserved.
[ ] Safe Error behavior is defined.
[ ] Unsupported versions fail closed.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now APIs.
```

---

# 26. Validation Report Template

```text
Validation: API Contract
Status: Pass | Warning | Blocked | Architecture Violation
Scope: API Contracts

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- API Contract:
- Operation:
- Domain:
- Owning Service:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 27. Codex Usage

Codex must use this validation:

```text
before implementing TASK-007-api-validator-scaffold
before implementing API-facing parts of TASK-010
after modifying API Contracts
during PR review
```

Codex must not:

```text
implement API behavior without contract trace
mutate domain state in API validators
emit Events from API validators
skip Permission/Policy hooks
skip Idempotency for create/apply
skip safe errors
skip unsupported version behavior
```

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial API Contract Validation. Defines API file existence, MVP/stub depth, API-domain-service mapping, Common Contract usage, request/response rules, operation categories, Idempotency, Permission/Policy, Pagination, Event, AI, Human Review, Error/Versioning and test traceability validation. |

---

**End of API Contract Validation**
