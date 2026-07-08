# API Specification Template

**Spec ID:** B02-API-[DOMAIN-OR-CAPABILITY]  
**Spec Type:** API Specification  
**API Name:** [Name] API  
**API File:** core-specs/api/[name]-api.md  
**Related Domain:** core-specs/domains/[domain].md  
**Related Object Specs:** core-specs/objects/[object].md  
**Related Service Specs:** core-specs/services/[service].md  
**Related Event Specs:** core-specs/events/[event].md  
**Related Contract Specs:** core-specs/contracts/[contract].md  
**Related Agent Specs:** core-specs/agents/[agent].md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** [Phase]  
**MVP Depth:** [Must Implement / Should Implement / Reserved]  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this API exists and what Core capability it exposes.

This section must answer:

```text
what Core capability is exposed
which consumers may use it
which Core Service owns the behavior
which object references are returned
which operations are protected
which events may be observed or emitted by service-side behavior
```

The API must expose Core capabilities without redefining Core meaning.

---

# 2. API Meaning

This API means:

```text
[Define the governed interface meaning.]
```

This API does not mean:

```text
product UI behavior
direct database access
domain ownership
workflow ownership
permission grant by API access alone
policy approval by API access alone
AI-approved truth
professional legal conclusion
```

API meaning must be aligned with the related Domain, Object and Service specifications.

---

# 3. API Boundary

This API is responsible for:

```text
request intake
request validation
reference validation
permission enforcement entry point
policy enforcement entry point
Core Service invocation
safe response shaping
controlled error response
event reference exposure where allowed
AI Agent access boundary where allowed
```

This API is not responsible for:

```text
domain meaning
object lifecycle ownership beyond service invocation
workflow execution beyond governed service operation
product UI state
pricing/payment/finance logic unless explicitly specified
AI reasoning truth
professional legal conclusion
raw storage implementation
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/[domain].md
```

Domain ownership rule:

```text
The API must not redefine the related Core Domain.
```

The API must follow the domain boundary and controlled vocabulary defined by the domain spec.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/[object].md
core-specs/objects/[related-object].md
```

Object rules:

```text
- API request fields must map to governed object references or controlled values.
- API responses must return governed reference IDs.
- API must not expose restricted object fields by default.
- API must not create related objects silently unless operation explicitly defines it and the relevant Service owns it.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/[service].md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- API must call the owning Core Service for behavior.
- API must not bypass Core Service logic.
- API must not write Core records directly.
- API must not emit domain events directly; events must be emitted through governed service/event behavior.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/[event].md
```

Event rules:

```text
- API may expose event references only under Permission and Policy.
- API must not allow product clients to fabricate Core events.
- API must distinguish command/request from event occurrence.
- API must not expose restricted event payload fields by default.
```

---

# 8. API Operations

Define operations in the following format.

## 8.1 Operation: [Operation Name]

**Operation Category:** [Create / Read / Update / Archive / Link / Unlink / Evaluate / Validate / Search / List / Action / Export / Import / ObserveEvent]  
**Method:** [GET / POST / PATCH / DELETE]  
**Path:** `/[resource]`  
**Owning Service Operation:** `[serviceOperation]`  
**Permission Required:** `[permission-key]`  
**Policy Required:** `[policy-scope]`  
**AI Agent Access:** [Allowed / Restricted / Not Allowed]  
**Event Behavior:** [No Event / Service May Emit / Service Must Emit / Read Events Only]

Meaning:

```text
[What this operation means.]
```

Non-meaning:

```text
[What this operation must not be interpreted as.]
```

Required references:

```text
[reference_id]
```

Expected service call:

```text
API
  ↓
Permission / Policy where required
  ↓
Owning Core Service
  ↓
Event Service where applicable
  ↓
Safe API response
```

---

# 9. Request Contracts

Request contract must define:

```text
headers
path parameters
query parameters
request body
required references
controlled values
idempotency key where applicable
correlation ID where applicable
actor context
organization context
AI Agent context where applicable
```

Example:

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  resource_id: string
query_parameters:
  include_events: boolean | optional
body:
  actor_reference_id: string
  organization_reference_id: string | null
  request_context: object
  payload: object
```

Request rules:

```text
- Requests must use governed references.
- Requests must use controlled values.
- Requests must not include restricted fields unless explicitly allowed.
- Requests must not include credentials, tokens, secrets or raw confidential content.
```

---

# 10. Response Contracts

Response contract must define:

```text
status code
response body
safe summary
reference IDs
controlled values
restricted field behavior
related event references where allowed
error response shape
```

Example:

```yaml
status: 200
body:
  result_reference_id: string
  status: string
  safe_summary: object
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must be safe by default.
- Responses must return governed references.
- Responses must not expose restricted object, service, policy, permission or event internals.
- Responses must not imply legal/professional conclusion unless the related service explicitly produces it.
```

---

# 11. Controlled Values

List API-specific controlled values:

```text
api_operation_status
operation_category
include_mode
sort_mode
filter_mode
error_code
visibility_mode
ai_access_mode
```

Example:

```text
api_operation_status:
- Accepted
- Completed
- Rejected
- PermissionDenied
- PolicyRestricted
- ValidationFailed
- Conflict
- InternalError
```

Controlled values must align with related Object, Service and Event specs.

---

# 12. Permission Rules

Define permission requirements by operation:

```text
Create: [permission-key]
Read: [permission-key]
Update: [permission-key]
Archive: [permission-key]
Link: [permission-key]
Evaluate: [permission-key]
ObserveEvent: [permission-key]
```

Permission rules:

```text
- API access is not permission.
- Permission must be evaluated where required.
- Task assignment, Organization membership or User existence must not be treated as Permission by itself.
- Permission decisions must be context-specific.
```

---

# 13. Policy Rules

Define policy requirements by operation:

```text
visibility policy
confidentiality policy
AI access policy
event access policy
data retention policy
export policy
integration policy
```

Policy rules:

```text
- Policy must be evaluated where contextual constraints apply.
- Policy is not Permission.
- Policy restrictions must hide or redact restricted fields.
- Policy failure must return controlled safe errors.
```

---

# 14. AI Agent Access Rules

AI Agent access mode:

```text
Allowed
Restricted
NotAllowed
HumanReviewRequired
```

AI Agents may:

```text
call read operations where authorized
call evaluate/validate operations where authorized
prepare drafts where allowed
summarize safe responses where allowed
```

AI Agents must not:

```text
fabricate Core records
fabricate Core events
turn recommendations into approved Core truth
bypass Permission
bypass Policy
expose restricted data
rewrite audit or event history
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
authorized_knowledge_reference where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Define how this API exposes or references events:

```text
related_event_reference_ids
event listing endpoint
event detail endpoint
event payload visibility
restricted event fields
```

Rules:

```text
- Events are occurrence records, not commands.
- API must not allow direct client event fabrication.
- API must not expose restricted event payload by default.
- Domain service behavior owns whether an event must be emitted.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] Required path parameters are present.
[ ] Required references exist.
[ ] Actor context is present where required.
[ ] Organization context is valid where required.
[ ] Controlled values are valid.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted fields are absent or allowed.
[ ] Idempotency key is present where required.
[ ] AI Agent contract is present where required.
[ ] Related event behavior is correct.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled error categories:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
ReferenceInvalid
ValidationFailed
Conflict
DuplicateRejected
StateInvalid
PayloadTooLarge
RestrictedFieldViolation
AgentContractRequired
EventEmissionFailed
InternalError
```

Error response shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Error rules:

```text
- Errors must be safe for product/API consumers.
- Errors must not expose secrets.
- Errors must not expose restricted policy internals.
- Errors must not expose restricted permission internals.
- Errors must not expose confidential customer, matter, document, evidence or legal strategy content.
```

---

# 18. Versioning Rules

API version:

```text
v0.1.0
```

Versioning rules:

```text
- Breaking changes require new version or explicit migration rule.
- Deprecated fields must remain readable until removal window ends.
- Controlled value changes must be documented.
- Event behavior changes must be documented.
- Permission/Policy changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this API spec
cite the related Service spec before implementing behavior
cite the related Object spec before implementing payloads
cite the related Event spec before emitting or exposing events
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe responses by default
write tests for restricted field hiding
write tests for invalid references
write tests for denied Permission
write tests for Policy restriction
write tests for AI Agent access restrictions
write tests for event behavior
```

Codex must not:

```text
invent endpoint semantics from UI needs
write directly to database bypassing Core Service behavior
allow UI to emit Core events directly
treat API access as Permission
treat Policy pass as Permission grant
treat AI output as approved Core data
expose restricted fields for convenience
merge Product workflow with Core API meaning
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines API purpose.
[ ] It defines API meaning.
[ ] It defines API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines API operations.
[ ] It defines request contracts.
[ ] It defines response contracts.
[ ] It defines controlled values.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent access rules.
[ ] It defines Event access rules.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial API specification template. Defines standard API structure, boundary, request/response contracts, Permission/Policy, AI access, Event access, validation, errors and Codex implementation rules. |

---

**End of API Specification Template**
