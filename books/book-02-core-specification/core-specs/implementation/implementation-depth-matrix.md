# Implementation Depth Matrix

**Spec ID:** B02-IMPLEMENTATION-DEPTH-MATRIX  
**Spec Type:** Implementation Depth Matrix  
**Spec File:** core-specs/implementation/implementation-depth-matrix.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Layers:** Common Contracts; API Contracts; Workflow Contracts; Services; Events; Agents; Tests; Codex Tasks  
**Status:** Draft  
**Version:** 0.1.0  
**Matrix Version:** v0.1.0  
**MVP Phase:** Phase 0–1 — Implementation Depth Governance  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This matrix defines the implementation depth required for each major MarkOrbit Core capability during MVP.

Book 02 defines a full Core architecture. MVP implementation must not attempt to build the entire architecture at full production depth.

This file answers:

```text
Which capability must be fully enforced now?
Which capability only needs schema validation now?
Which capability needs a service hook?
Which capability should remain document-only?
Which capability must be blocked from MVP implementation?
```

Its purpose is to prevent:

```text
overbuilding before MVP
underbuilding critical governance
Codex implementing unscoped infrastructure
fake implementation of protected behavior
AI overreach
workflow engine overreach
policy engine overreach
event infrastructure overreach
```

---

# 2. Core Lock

```text
Implementation depth is governed by MVP scope.
Architecture may be complete while implementation is phased.
Must Build Now does not always mean full production depth.
Stub Now must remain safe and explicit.
Document Only must not be silently implemented.
Deferred capabilities must not block MVP.
Never in MVP items are architecture violations if implemented.
Codex must implement only the assigned depth.
Codex must not deepen implementation without an explicit task.
```

---

# 3. Depth Levels

Implementation depth uses five levels.

| Level | Name | Meaning | MVP Use |
|---:|---|---|---|
| 0 | Documented Only | Spec exists, no implementation required | Future architecture |
| 1 | Schema Validation | Validate shape, required fields, controlled values and safe failure | MVP baseline for many governance capabilities |
| 2 | Service Hook | Route to owning service or hook; may use simple placeholder logic | MVP operational boundary |
| 3 | Real Enforcement | Enforce behavior in MVP runtime with tests | Critical MVP governance |
| 4 | Audited Production Enforcement | Production-grade enforcement, observability, audit and compliance | Later phase |

Core rule:

```text
MVP should implement critical safety at Level 3.
MVP should implement extensibility hooks at Level 1 or Level 2.
MVP should not implement future platform infrastructure at Level 4.
```

---

# 4. Depth Category Rules

## 4.1 Level 0 — Documented Only

Allowed behavior:

```text
spec file exists
architecture reference exists
future implementation notes exist
```

Not allowed:

```text
runtime code pretending to implement the capability
production path depending on the capability
fake success responses
silent bypass
```

## 4.2 Level 1 — Schema Validation

Required behavior:

```text
validate request/response shape
validate required fields
validate controlled values
validate version fields
return safe errors
include fixtures and tests
```

Not required:

```text
full business logic
full policy evaluation
full external integration
full workflow orchestration
```

## 4.3 Level 2 — Service Hook

Required behavior:

```text
call or route to owning service
preserve ownership boundary
return controlled allowed/restricted placeholder where appropriate
record trace where required
provide negative tests for bypass attempts
```

Not required:

```text
complete production rule engine
complete ranking engine
complete workflow engine
```

## 4.4 Level 3 — Real Enforcement

Required behavior:

```text
enforce behavior at runtime
block invalid or unauthorized action
prevent duplicate effects
return safe errors
preserve trace
pass positive and negative tests
```

## 4.5 Level 4 — Audited Production Enforcement

Required behavior:

```text
production-grade observability
audit records
operational monitoring
administrative controls
policy lifecycle management
migration and compatibility support
security review
```

MVP note:

```text
Level 4 is generally out of MVP scope unless a security-critical primitive requires it later.
```

---

# 5. MVP Capability Depth Matrix

| Capability | MVP Category | MVP Depth | Target Later | Notes |
|---|---|---:|---:|---|
| Reference Contract | Must Build Now | 3 | 4 | Public references must hide database IDs. |
| Error Contract | Must Build Now | 3 | 4 | Safe errors are required for every failure path. |
| Versioning Contract | Must Build Now | 1 | 3 | Unsupported versions must fail closed; full compatibility lifecycle later. |
| Permission Context | Must Build Now | 2 / 3 | 4 | Protected actions require real enforcement for MVP spine. |
| Policy Context | Must Build Now | 1 / 2 | 4 | MVP needs schema and hook; full policy engine later. |
| Audit Context | Must Build Now | 2 | 4 | Correlation and trace hook required. |
| Idempotency Contract | Must Build Now | 3 | 4 | Required for create/apply duplicate-sensitive operations. |
| Pagination Contract | Must Build Now | 2 | 3 | Basic list/search behavior required. |
| AI Context | Must Build Now | 1 | 3 | Metadata and boundary validation required. |
| Human Review Contract | Must Build Now | 2 | 4 | Gate validation required for protected outputs. |
| Event Trace | Must Build Now | 2 | 4 | Persisted or fixture-backed trace acceptable in MVP. |
| API Validators | Must Build Now | 2 / 3 | 4 | MVP APIs need validators and ownership boundary tests. |
| Workflow Validators | Must Build Now | 2 | 4 | Preview/apply validators; no full engine required. |
| Agent Boundary | Must Build Now | 1 / 2 | 3 / 4 | Boundary and forbidden-action tests required. |
| Contract Tests | Must Build Now | 3 | 4 | Negative tests required. |
| Fixtures | Must Build Now | 3 | 4 | Deterministic non-production fixtures required. |
| Knowledge Retrieval | Stub Now | 1 / 2 | 4 | Basic reference/search stub only. |
| Notification Delivery | Stub Now | 1 / 2 | 4 | No production push/email integration in MVP. |
| Opportunity Lifecycle | Stub Now | 1 / 2 | 3 | Basic placeholder; customer intake may create candidate. |
| Partner Management | Stub Now | 1 / 2 | 3 | Safe reference interface only. |
| Service Provider Management | Stub Now | 1 / 2 | 3 | Basic provider reference and profile stub. |
| Service Network | Stub Now | 1 | 4 | No full network optimization. |
| Routing | Stub Now | 1 / 2 | 4 | Suggestions allowed; final selection human-gated. |
| Full Workflow Engine | Document Only | 0 / 1 | 4 | MVP uses workflow validators, not full engine. |
| Full Policy Engine | Document Only | 0 / 1 | 4 | MVP uses hooks and simple restrictions. |
| Full Agent Runtime | Document Only | 0 / 1 | 4 | MVP uses boundary scaffolds and tests. |
| External Filing Integration | Defer | 0 | 4 | Must not block MVP. |
| Payment Execution | Defer | 0 | 4 | Must not be implemented in MVP. |
| Provider Marketplace Settlement | Defer | 0 | 4 | Later platform phase. |
| AI Official Submission | Never in MVP | Forbidden | Forbidden | Architecture violation. |
| AI Deadline Certification | Never in MVP | Forbidden | Forbidden | Professional risk. |
| AI Final Provider Selection | Never in MVP | Forbidden | Forbidden | Business/professional risk. |

---

# 6. Common Contracts Depth

| Common Contract | MVP Depth | Required MVP Behavior |
|---|---:|---|
| references.md | 3 | Generate/validate public reference IDs; reject DB IDs; validate type. |
| errors.md | 3 | Controlled errors; no stack traces; no restricted leakage. |
| pagination.md | 2 | Basic limit/cursor/search result shape; policy-aware count omission. |
| audit-context.md | 2 | correlation_id, causation_event_reference_id, event_reference_ids validation. |
| ai-context.md | 1 | source scope, AI output metadata, policy omissions and capability scope validation. |
| human-review.md | 2 | review reference validation and HumanReviewRequired gate. |
| permission-context.md | 2 / 3 | Permission check hook; Level 3 enforcement for protected MVP actions. |
| policy-context.md | 1 / 2 | Policy context schema and restriction hook; redaction placeholders where needed. |
| idempotency.md | 3 | missing key failure, replay, conflict and duplicate prevention. |
| versioning.md | 1 | contract_version/schema_version validation; unsupported version failure. |

---

# 7. API Depth

## 7.1 MVP API Depth

MVP APIs require Level 2 or Level 3 depending on operation.

Level 3 required for:

```text
create Customer
create Brand
create Trademark
create Matter
create Order
create Document
create Evidence
create Task through Task Service
create Communication draft
workflow preview
workflow apply
read Event trace
Permission evaluation for protected actions
Policy restriction hook for protected output
```

Level 2 acceptable for:

```text
search/list
reference validation
basic read
status summary
AI-assisted prepare endpoints
human review reference validation
```

Level 1 acceptable for:

```text
future fields
optional advanced filters
non-MVP API stubs
```

## 7.2 API Depth Rules

API layer must always enforce:

```text
no direct domain mutation
no direct event emission
safe error shape
reference validation
version validation
permission and policy context validation
```

---

# 8. Workflow Depth

## 8.1 MVP Workflow Depth

MVP workflows require Level 2.

Required behavior:

```text
preview request validation
apply request validation
step contract validation
Task plan validation
Human Review gate validation
AI boundary validation
Permission and Policy validation
Idempotency validation
Event trace reference validation
safe errors
```

Level 3 required only for:

```text
idempotent apply behavior
Task Service delegation
protected action gate blocking
safe state transition where implemented
```

## 8.2 Workflow Engine Depth

Full workflow engine is not required in MVP.

MVP should not implement:

```text
complex workflow runtime
distributed workflow orchestration
dynamic workflow designer
production workflow scheduling engine
automatic external execution
```

MVP may implement:

```text
workflow preview function
workflow apply function
workflow step validator
workflow result object
workflow task plan
```

---

# 9. Event Depth

MVP Event depth is Level 2.

Required:

```text
event_reference_id
event_type
source_service
subject_reference_id
correlation_id
created_at
safe payload shape
schema_version
visibility policy hook
```

Level 3 required for:

```text
idempotency preventing duplicate events
API/Workflow/Agent no-direct-emission tests
Event reference not command tests
safe event visibility behavior
```

Not required in MVP:

```text
streaming event bus
Kafka or equivalent
event replay engine
event sourcing as system-of-record
production audit dashboard
```

---

# 10. Agent Depth

MVP Agent depth is Level 1 / 2.

Required:

```text
agent identity and capability metadata
allowed capability validation
forbidden action validation
AI Context output metadata
policy omissions disclosure
human review preservation
agent boundary tests
```

Allowed:

```text
summarize
draft
classify
compare
suggest
identify gaps
prepare task plan
prepare communication draft
summarize audit trace
```

Forbidden:

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

MVP agents may produce draft output but must not trigger downstream execution.

---

# 11. Permission / Policy Depth

## 11.1 Permission

MVP Permission depth:

```text
Level 2 for general hooks.
Level 3 for protected MVP actions.
```

Protected MVP actions include:

```text
create or update Customer
create or update Trademark
create or update Matter
create or update Order
create Task
create Communication
workflow apply
communication review
event read where restricted
```

Required tests:

```text
PermissionAllowed permits only when Policy also allows.
PermissionDenied blocks.
UnknownPermission fails closed.
```

## 11.2 Policy

MVP Policy depth:

```text
Level 1 for schema validation.
Level 2 for contextual restriction hooks.
```

Required MVP behavior:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact placeholder
PolicyRequiresHumanReview
NotFound substitution where specified
restricted_fields_omitted flag
```

Full policy rule authoring is not required.

---

# 12. Human Review Depth

MVP Human Review depth is Level 2.

Required:

```text
human_review_reference_id validation
review_required flag
HumanReviewRequired error
review status check
review does not execute downstream action
owning service decides whether review satisfies gate
```

Required gates:

```text
customer-facing communication
external communication
classification recommendation finalization
evidence sufficiency conclusion
provider selection
workflow apply where protected
```

---

# 13. Idempotency Depth

MVP Idempotency depth is Level 3 for duplicate-sensitive operations.

Required operations:

```text
create Customer
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

Required behavior:

```text
missing idempotency_key rejected where required
same key + same semantic request replays safely
same key + different semantic request returns IdempotencyConflict
replay does not duplicate objects
replay does not duplicate Tasks
replay does not duplicate Communications
replay does not duplicate Events
```

---

# 14. Error / Versioning Depth

## 14.1 Errors

MVP Error depth is Level 3.

Required:

```text
ReferenceInvalid
ValidationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
StateInvalid
InternalError with safe message only
```

Errors must not expose:

```text
database IDs
stack traces
restricted data
policy internals
permission internals
prompt internals
hidden reasoning
secrets or tokens
```

## 14.2 Versioning

MVP Versioning depth is Level 1.

Required:

```text
contract_version required
schema_version where applicable
unsupported version returns VersionUnsupported
historical version field preserved where record is created
```

Not required:

```text
full migration engine
backward compatibility service
deprecation lifecycle tooling
```

---

# 15. Validation Depth

Validation specs should operate at Level 2 in MVP.

Required validation files:

```text
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/mvp-readiness-validation.md
```

Level 2 behavior:

```text
validate required files exist
validate traceability mappings
validate MVP cut coverage
validate contract/test coverage
validate no forbidden MVP items are in scope
```

---

# 16. Codex Depth Rules

Codex must:

```text
implement only the assigned depth
not deepen Stub Now items into full production systems
not implement Document Only items unless explicitly moved into scope
not implement Defer items before MVP acceptance
not implement Never in MVP items
cite this matrix in every implementation task
```

Codex summary must state:

```text
which depth level was implemented
which items remain stubs
which items remain document-only
which tests enforce boundaries
```

---

# 17. Depth Change Governance

Any change to implementation depth requires:

```text
updated mvp-cut-v0.1.md or successor
updated implementation-depth-matrix.md
updated TRACEABILITY.md where mapping changes
updated Codex Task Index
updated Test Contract coverage
explicit review note
```

Depth increases are not allowed by convenience.

Depth increase examples:

```text
Policy Level 2 → Level 3
Agent Runtime Level 1 → Level 2
Workflow Engine Level 1 → Level 3
Routing Level 2 → Level 3
Event Trace Level 2 → Level 4
```

Each requires explicit architecture approval.

---

# 18. Acceptance Criteria

This Implementation Depth Matrix is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines Level 0–4.
[ ] It defines category rules.
[ ] It defines MVP Capability Depth Matrix.
[ ] It defines Common Contracts depth.
[ ] It defines API depth.
[ ] It defines Workflow depth.
[ ] It defines Event depth.
[ ] It defines Agent depth.
[ ] It defines Permission / Policy depth.
[ ] It defines Human Review depth.
[ ] It defines Idempotency depth.
[ ] It defines Error / Versioning depth.
[ ] It defines Validation depth.
[ ] It defines Codex depth rules.
[ ] It defines depth change governance.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Implementation Depth Matrix. Defines depth levels, MVP capability depth, Common/API/Workflow/Event/Agent/Permission/Policy/Human Review/Idempotency/Error/Versioning/Validation depth and Codex depth governance. |

---

**End of Implementation Depth Matrix**
