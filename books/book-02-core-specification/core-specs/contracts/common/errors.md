# Common Contract — Errors

**Spec ID:** B02-CONTRACT-COMMON-ERRORS  
**Spec Type:** Common Contract Specification  
**Contract Name:** Error Contract  
**Contract File:** core-specs/contracts/common/errors.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** All Core object specifications  
**Related Service Specs:** All Core service specifications  
**Related API Specs:** All Core API specifications  
**Related Event Specs:** All Core event specifications where error or rejection trace is referenced  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Error Contract defines the canonical safe error shape used across MarkOrbit Core.

It standardizes how APIs, services, agents, workflows, events and validators return rejection, failure and warning information without leaking restricted data, permission internals, policy internals, database identifiers, credentials, professional strategy or unsafe implementation details.

This contract governs:

```text
safe error shape
error code naming
error category naming
validation errors
permission errors
policy errors
reference errors
state errors
agent errors
human-review errors
idempotency errors
version errors
restricted-data errors
retry behavior
correlation trace
safe display rules
Codex error implementation rules
```

Error Contract does not define business truth, perform Permission/Policy evaluation, decide professional result or replace owning service behavior.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for representing safe, controlled and traceable errors.
```

This contract does not mean:

```text
exception class hierarchy only
HTTP status table only
debug log format
database error passthrough
permission evaluation engine
policy evaluation engine
product copywriting system
customer-facing explanation standard
```

Core rule:

```text
Errors explain safe failure.
Errors do not expose hidden state.
Errors do not grant permission.
Errors do not replace service validation.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
canonical error response shape
controlled error codes
controlled error categories
safe_detail rules
retryable rules
correlation_id preservation
field error shape
validation error aggregation
permission/policy error safety
agent rejection safety
version and idempotency error safety
```

This contract is not responsible for:

```text
executing operation
evaluating permission
evaluating policy
resolving business dispute
issuing legal conclusion
choosing UI error wording
exposing debug stack traces
creating audit events directly
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Owning rule:

```text
The Contracts layer defines enforceable shape. This Error Contract provides the common error shape used by API, Service, Agent, Workflow, Event and Validation contracts.
```

---

# 5. Related Core Objects

This contract may reference any Core object through the Reference Contract:

```text
core-specs/contracts/common/references.md
```

Rules:

```text
- Errors may include safe object type.
- Errors may include reference field name.
- Errors must not expose restricted object existence where policy forbids disclosure.
- Errors must not expose database IDs.
```

---

# 6. Required References

Error context shape:

```yaml
error_context:
  correlation_id: string | null
  request_reference_id: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  human_review_reference_id: string | null
```

Rules:

```text
- correlation_id must be preserved where provided.
- request_reference_id may be used for async or idempotent operations.
- permission_decision_reference_id may be included only if policy allows safe exposure.
- policy_decision_reference_id may be included only if policy allows safe exposure.
- target references must follow Reference Contract.
```

---

# 7. Contract Shape

Canonical safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Extended error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
  field_errors:
    - field: string
      code: string
      message: string
      safe_detail: string | null
  reference_errors:
    - reference_field: string
      object_type: string | null
      code: string
      message: string
      safe_detail: string | null
  required_next_step:
    next_step_type: string | null
    owning_service: string | null
    safe_instruction: string | null
```

Rules:

```text
- API contracts may use canonical or extended error shape.
- Service contracts may include internal-safe diagnostic fields only in non-public internal context.
- Public responses must not expose stack traces, SQL errors, raw provider errors or model prompts.
- safe_detail must be safe to display.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| code | string | Yes | No | Must use controlled error code. |
| category | string | Yes | No | Must use controlled error category. |
| message | string | Yes | No | Safe human-readable message. Must not expose restricted data. |
| safe_detail | string | No | Yes | Optional safe details. Must not expose internals. |
| correlation_id | string | No | Yes | Must preserve request correlation_id where available. |
| retryable | boolean | Yes | No | Indicates whether retry may succeed without changing request. |
| field_errors | list | No | Yes | Used for validation errors. |
| reference_errors | list | No | Yes | Used for reference validation errors. |
| required_next_step | object | No | Yes | Safe next governed step where applicable. |

---

# 9. Controlled Values

## 9.1 error category

```text
Request
Authentication
Authorization
Permission
Policy
Validation
Reference
State
Conflict
Idempotency
Version
RestrictedData
HumanReview
Agent
Workflow
Event
Service
ExternalDependency
RateLimit
Timeout
Internal
Unknown
```

## 9.2 common error codes

```text
BadRequest
Unauthorized
Forbidden
PermissionDenied
PolicyRestricted
ValidationFailed
ReferenceInvalid
ReferenceNotFound
ReferenceTypeMismatch
ReferenceDomainMismatch
StateInvalid
StateTransitionNotAllowed
Conflict
DuplicateRejected
IdempotencyConflict
VersionUnsupported
RestrictedFieldViolation
RestrictedDataRequested
HumanReviewRequired
AgentContractRequired
AgentSuspended
AgentRevoked
CapabilityNotAllowed
WorkflowReferenceInvalid
TaskReferenceInvalid
EventReferenceInvalid
DownstreamServiceRequired
ExternalDependencyFailed
RateLimited
Timeout
InternalError
UnknownError
```

## 9.3 next_step_type

```text
FixRequest
ValidateReference
RequestPermission
RequestPolicyReview
RequestHumanReview
UseOwningService
RetryLater
ContactSupport
CheckDownstreamService
NoActionAvailable
Unknown
```

## 9.4 retryable meaning

```text
true:
  request may succeed later without semantic change

false:
  request must be changed, reviewed, authorized or escalated before retry
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] error.code is present.
[ ] error.category is present.
[ ] error.message is present.
[ ] error.retryable is present.
[ ] error.code is controlled.
[ ] error.category is controlled.
[ ] message is safe to display.
[ ] safe_detail is safe to display.
[ ] correlation_id is preserved where available.
[ ] field_errors use safe field names.
[ ] reference_errors follow Reference Contract.
[ ] permission/policy internals are not exposed.
[ ] restricted data is not exposed.
[ ] database IDs are not exposed.
[ ] stack traces are not exposed.
[ ] raw external provider errors are not exposed.
[ ] model prompts or hidden instructions are not exposed.
```

Validation failure of error shape itself must be treated as implementation defect.

---

# 11. Permission Rules

Permission-related errors:

```yaml
error:
  code: PermissionDenied
  category: Permission
  message: You do not have permission to perform this action.
  safe_detail: null
  correlation_id: string | null
  retryable: false
```

Rules:

```text
- PermissionDenied must not expose permission evaluation internals by default.
- Permission decision references may be exposed only where policy allows.
- Missing permission must not reveal restricted object existence where policy forbids disclosure.
- Permission errors must stop protected behavior.
```

---

# 12. Policy Rules

Policy-related errors:

```yaml
error:
  code: PolicyRestricted
  category: Policy
  message: This action is restricted by policy.
  safe_detail: string | null
  correlation_id: string | null
  retryable: false
```

Rules:

```text
- PolicyRestricted must not expose policy internals by default.
- Policy may require returning NotFound instead of PolicyRestricted.
- Policy errors may include safe next step such as RequestPolicyReview.
- Policy errors must stop or downgrade protected behavior.
```

---

# 13. AI Agent Rules

Agent-related errors:

```text
AgentContractRequired
AgentSuspended
AgentRevoked
CapabilityNotAllowed
RestrictedDataRequested
HumanReviewRequired
DownstreamServiceRequired
```

Rules:

```text
- Agent errors must not expose hidden prompt, model, system instruction or tool internals.
- RestrictedDataRequested must not echo the restricted data requested.
- CapabilityNotAllowed must not reveal unavailable restricted tools.
- HumanReviewRequired must identify safe review need, not disclose hidden policy details.
- Agent errors must preserve agent_reference_id only where safe.
```

Example:

```yaml
error:
  code: HumanReviewRequired
  category: HumanReview
  message: Human review is required before this output can be used.
  safe_detail: The prepared draft cannot be used for external action until reviewed.
  correlation_id: string | null
  retryable: false
```

---

# 14. Event Rules

Event-related errors:

```text
EventReferenceInvalid
EventEmissionFailed
EventPayloadInvalid
EventVisibilityRestricted
```

Rules:

```text
- Event errors must not expose restricted event payloads.
- EventEmissionFailed must not imply business operation success unless owning service explicitly defines compensation behavior.
- Event references must not be replayed as commands.
- Event Service owns event validation.
```

---

# 15. Reference Error Rules

Reference errors must follow Reference Contract.

Common examples:

```yaml
error:
  code: ReferenceInvalid
  category: Reference
  message: The provided reference is invalid.
  safe_detail: null
  correlation_id: string | null
  retryable: false
```

```yaml
error:
  code: ReferenceNotFound
  category: Reference
  message: The requested reference was not found.
  safe_detail: null
  correlation_id: string | null
  retryable: false
```

Rules:

```text
- Do not expose internal database IDs.
- Do not disclose object existence where policy forbids it.
- Use ReferenceNotFound instead of PolicyRestricted where non-disclosure policy requires it.
- Include reference_errors only with safe field names.
```

---

# 16. State and Conflict Error Rules

State errors:

```text
StateInvalid
StateTransitionNotAllowed
Conflict
DuplicateRejected
IdempotencyConflict
```

Rules:

```text
- State errors must identify safe state problem.
- State errors must not expose restricted lifecycle details.
- IdempotencyConflict must be safe and deterministic.
- DuplicateRejected must not expose restricted existing object details.
```

Example:

```yaml
error:
  code: StateTransitionNotAllowed
  category: State
  message: The requested state transition is not allowed.
  safe_detail: The object is not in a state that supports this operation.
  correlation_id: string | null
  retryable: false
```

---

# 17. External Dependency Error Rules

External dependency errors:

```text
ExternalDependencyFailed
RateLimited
Timeout
```

Rules:

```text
- Raw third-party error payloads must not be passed through directly.
- Credentials, URLs with tokens, API keys and private headers must be removed.
- retryable may be true for timeout/rate limit where appropriate.
- safe_detail may identify the dependency category but not secret internals.
```

---

# 18. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding a new error code requires revision notes.
- Adding a new error category requires revision notes.
- Renaming an error code is breaking.
- Changing retryable meaning is breaking.
- Changing canonical error shape is breaking unless backward compatible.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Error Contract before implementing error responses
use controlled error codes
use controlled error categories
preserve correlation_id
return safe error shape
sanitize raw exceptions
sanitize external dependency errors
sanitize permission/policy errors
sanitize AI/agent errors
sanitize stack traces
sanitize database errors
write tests for BadRequest
write tests for ValidationFailed
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for ReferenceInvalid
write tests for HumanReviewRequired
write tests that restricted data is not present in errors
write tests that stack traces are not present in public errors
```

Codex must not:

```text
return raw exceptions to API users
return SQL/database errors to API users
return raw external provider errors without sanitization
expose permission or policy internals
expose prompt, system instruction or tool internals
echo restricted user input in safe_detail
use uncontrolled error codes for Core contracts
drop correlation_id where provided
```

---

# 20. Acceptance Criteria

This Error Contract is accepted only if:

```text
[ ] It defines error purpose.
[ ] It defines error meaning.
[ ] It defines error boundary.
[ ] It defines related owning spec.
[ ] It defines related Core objects.
[ ] It defines required error references.
[ ] It defines canonical and extended error shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission error rules.
[ ] It defines Policy error rules.
[ ] It defines AI Agent error rules.
[ ] It defines Event error rules.
[ ] It defines Reference error rules.
[ ] It defines State and Conflict error rules.
[ ] It defines External Dependency error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Error Contract. Defines safe error shape, controlled categories/codes, validation, permission/policy, AI, event, reference, state, dependency, versioning and Codex implementation rules. |

---

**End of Common Contract**
