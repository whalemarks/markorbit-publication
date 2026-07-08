# API Contract — Event API

**Spec ID:** B02-CONTRACT-API-EVENT  
**Spec Type:** API Contract Specification  
**Contract Name:** Event API Contract  
**Contract File:** core-specs/contracts/api/event-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/event-api.md  
**Related Domain:** Event  
**Related Object Specs:** core-specs/objects/event.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/communication.md; core-specs/objects/routing.md  
**Related Service Specs:** core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/communication-service.md; core-specs/services/routing-service.md  
**Related API Specs:** core-specs/api/event-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/communication-api.md; core-specs/api/routing-api.md  
**Related Event Specs:** all core-specs/events/*.md  
**Related Agent Specs:** core-specs/agents/audit-agent.md; core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Event API Contract defines the implementation-facing request and response contract for Event API operations in MarkOrbit Core.

It standardizes how clients read, search, validate, inspect and audit Event records through governed API boundaries without bypassing Event Service, Permission Service, Policy Service or audit governance.

This contract governs:

```text
Event API versioning
Event read response
Event search/list response
Event reference validation
Event stream query contract
Event audit trail contract
Event payload visibility rules
Event correlation query rules
Permission and Policy context
AI and Audit Agent context
Pagination behavior
Safe error behavior
Codex implementation rules
```

Event API Contract does not allow clients to create, mutate, delete, replay or fabricate Events. Event creation belongs to owning services as a result of governed domain behavior.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Event Service through governed read/audit boundaries.
```

This contract does not mean:

```text
event creation API
event mutation API
event replay API
command bus
message broker
business operation executor
compliance certification
legal conclusion
permission grant
policy approval
debug dump
```

Core rule:

```text
Event API exposes governed trace.
Event Service owns Event records.
Owning services emit Events.
Permission and Policy govern visibility.
Audit output distinguishes recorded trace from inference.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Event reference fields
event stream query fields
audit trail query fields
event payload visibility fields
correlation and causation fields
pagination shape for list/search
permission/policy context requirements
AI/audit-agent context requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
creating Events directly
mutating Events
deleting Events
replaying Events
executing business operations
certifying compliance
making legal conclusions
Permission evaluation logic
Policy evaluation logic
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/event-api.md
```

Owning service spec:

```text
core-specs/services/event-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Event API and Event Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Event
```

Related objects:

```text
Identity
Organization
User
Permission
Policy
Task
WorkflowContract
Communication
Routing
Agent
```

Reference rules:

```text
- event_reference_id identifies Event.
- aggregate_object_type and aggregate_object_reference_id identify the object whose lifecycle produced the Event.
- actor_reference_id identifies actor where visible.
- correlation_id groups related operations.
- causation_event_reference_id links Event causation where available.
- Event reference does not authorize access to the underlying object.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Event target context:

```yaml
target:
  event_reference_id: string | null
  target_object_type: Event
  target_object_reference_id: string | null
```

Rules:

```text
- event_reference_id is required for read/validate-by-reference operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- aggregate_object_type and aggregate_object_reference_id are required for aggregate event queries.
- correlation_id is required for correlation event queries.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
GET    /v1/events/{event_reference_id}
GET    /v1/events
POST   /v1/events/validate-reference
GET    /v1/events/aggregate/{aggregate_object_type}/{aggregate_object_reference_id}
GET    /v1/events/correlation/{correlation_id}
POST   /v1/events/audit-trail
```

Endpoint ownership:

```text
API layer validates request contract.
Event Service retrieves and filters Event records.
Permission Service evaluates Event API access.
Policy Service evaluates Event payload visibility.
Audit Agent may summarize visible trace only.
API layer must not create, mutate, delete or replay Events.
```

---

# 8. Read Event Contract

Endpoint:

```text
GET /v1/events/{event_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  event_reference_id: string
  event_type: string
  event_version: string
  event_status: string
  occurred_at: datetime
  recorded_at: datetime | null
  aggregate:
    aggregate_object_type: string
    aggregate_object_reference_id: string
  actor:
    actor_reference_id: string | null
    actor_type: string | null
  organization_reference_id: string | null
  causation_event_reference_id: string | null
  correlation_id: string | null
  payload_visible: object | null
  payload_visibility: string
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate event:read permission.
- Policy may redact payload, actor, organization, aggregate or causation details.
- Event payload visibility must be explicit.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 9. Search/List Events Contract

Endpoint:

```text
GET /v1/events
```

Query parameters:

```yaml
event_type: string | null
event_status: string | null
aggregate_object_type: string | null
aggregate_object_reference_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
correlation_id: string | null
occurred_after: datetime | null
occurred_before: datetime | null
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  items:
    - event_reference_id: string
      event_type: string
      event_version: string
      event_status: string
      occurred_at: datetime
      aggregate_object_type: string | null
      aggregate_object_reference_id: string | null
      actor_reference_id: string | null
      correlation_id: string | null
      payload_visibility: string
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
```

Rules:

```text
- Pagination must follow Pagination Contract.
- total_count must be omitted where policy or security requires it.
- Search must not reveal restricted Event existence.
- Query must not expose restricted actor or aggregate details.
```

---

# 10. Validate Event Reference Contract

Endpoint:

```text
POST /v1/events/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  event_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  event_reference_id: string
  valid: boolean
  validation_status: string
  event_type: string | null
  occurred_at: datetime | null
  payload_visibility: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read Event payload.
- Validation status must follow Reference Contract.
- Policy may hide event_type or occurred_at.
```

---

# 11. Aggregate Event Stream Contract

Endpoint:

```text
GET /v1/events/aggregate/{aggregate_object_type}/{aggregate_object_reference_id}
```

Path parameters:

```yaml
aggregate_object_type: string
aggregate_object_reference_id: string
```

Query parameters:

```yaml
event_type: string | null
occurred_after: datetime | null
occurred_before: datetime | null
include_payload: boolean | null
pagination:
  cursor: string | null
  limit: integer | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  aggregate_object_type: string
  aggregate_object_reference_id: string
  events:
    - event_reference_id: string
      event_type: string
      event_version: string
      occurred_at: datetime
      actor_reference_id: string | null
      correlation_id: string | null
      payload_visible: object | null
      payload_visibility: string
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
```

Rules:

```text
- Aggregate query must not bypass permission to view the aggregate object.
- include_payload is a request, not a guarantee.
- Policy may return metadata-only events.
```

---

# 12. Correlation Event Stream Contract

Endpoint:

```text
GET /v1/events/correlation/{correlation_id}
```

Path parameters:

```yaml
correlation_id: string
```

Query parameters:

```yaml
event_type: string | null
include_payload: boolean | null
pagination:
  cursor: string | null
  limit: integer | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string
result:
  events:
    - event_reference_id: string
      event_type: string
      event_version: string
      occurred_at: datetime
      aggregate_object_type: string | null
      aggregate_object_reference_id: string | null
      causation_event_reference_id: string | null
      payload_visibility: string
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
```

Rules:

```text
- Correlation query must not reveal events outside Permission/Policy visibility.
- Correlation stream is trace support, not proof of complete business state.
- Missing/restricted events must be safely disclosed where allowed.
```

---

# 13. Audit Trail Contract

Endpoint:

```text
POST /v1/events/audit-trail
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - event:audit-trail:read
policy_context:
  required_policy_scopes:
    - event:audit-trail:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  audit_subject:
    target_object_type: string
    target_object_reference_id: string
  audit_scope: string
  occurred_after: datetime | null
  occurred_before: datetime | null
  include_summary: boolean
  include_payload: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  audit_trail_status: string
  audit_subject:
    target_object_type: string
    target_object_reference_id: string
  events_visible:
    - event_reference_id: string
      event_type: string
      occurred_at: datetime
      payload_visibility: string
      restricted_fields_omitted: boolean
  audit_summary_safe: string | null
  missing_or_restricted_trace_disclosed: boolean
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Audit trail is trace support, not compliance certification by itself.
- Audit Agent may summarize only visible Event trace.
- Audit summary must distinguish recorded trace from inference.
- Payload access remains policy-controlled.
```

---

# 14. Controlled Values

## 14.1 event_status

```text
Recorded
Redacted
Archived
Invalidated
Unknown
```

## 14.2 payload_visibility

```text
Full
Redacted
MetadataOnly
Hidden
PolicyRestricted
PermissionDenied
Unknown
```

## 14.3 audit_scope

```text
Lifecycle
PermissionPolicy
Workflow
Task
Communication
Routing
CustomerFacing
ProfessionalAction
SystemTrace
Unknown
```

## 14.4 audit_trail_status

```text
Completed
Partial
NoVisibleEvents
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 14.5 actor_type

```text
User
Agent
System
Integration
Service
Unknown
```

## 14.6 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
Archived
ContextMismatch
Unknown
```

## 14.7 sort.field

```text
occurred_at
recorded_at
event_type
event_status
aggregate_object_type
actor_reference_id
```

---

# 15. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] event_reference_id is valid where required.
[ ] event_type is controlled by Event Index where provided.
[ ] event_version follows Versioning Contract.
[ ] aggregate_object_type and aggregate_object_reference_id are present for aggregate query.
[ ] correlation_id is present for correlation query.
[ ] occurred_after and occurred_before are valid datetimes where provided.
[ ] include_payload is treated as request only.
[ ] AI Context is present for AI-assisted audit summaries.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 16. Permission Rules

Required permission keys:

```text
event:read
event:search
event:validate
event:aggregate:read
event:correlation:read
event:audit-trail:read
event:payload:read
```

Rules:

```text
- Event API must not grant permission.
- Permission Service evaluates required permission keys.
- Payload visibility may require separate permission.
- PermissionDenied must stop protected operations.
```

---

# 17. Policy Rules

Required policy scopes may include:

```text
event:read:policy
event:search:policy
event:reference:policy
event:aggregate:read:policy
event:correlation:read:policy
event:audit-trail:policy
event:payload:visibility:policy
event:actor:visibility:policy
event:aggregate:visibility:policy
cross-organization:event
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact payload, actor, aggregate, causation, correlation, counts or summaries.
- Policy may downgrade response to metadata-only.
- Policy may return NotFound where existence disclosure is restricted.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 18. AI and Human Review Rules

AI rules:

```text
- Audit Agent may read and summarize only Event trace that Permission and Policy allow.
- AI must not create, mutate, delete, replay or fabricate Events.
- AI must distinguish recorded trace from inference.
- AI output must disclose missing/restricted trace, source scope and policy omissions.
```

Human review:

```text
- Human review may be required where audit trail output is used for external communication, compliance representation, customer-facing explanation or professional dispute handling.
- human_review_required must be explicit where policy requires review.
```

---

# 19. Idempotency and Event Rules

Idempotency:

```text
Event API read/search/audit operations do not normally require idempotency_key.
Event API must not expose event creation endpoints.
```

Event creation boundary:

```text
- Owning services emit Events as a result of governed domain behavior.
- Event API must not emit Events directly.
- Event API must not replay Events.
- Event API must not mutate Event payloads.
```

Rules:

```text
- Event references are audit trace, not commands.
- Reading Events must not produce additional business Events except system access logs if separately governed.
```

---

# 20. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
EventReferenceInvalid
EventPayloadRestricted
AggregateReferenceInvalid
CorrelationIdInvalid
AuditTrailUnavailable
VersionUnsupported
InternalError
```

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose restricted Event payload, actor details, aggregate details, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 21. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
event_payload_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Event payload versions must follow Versioning Contract.
- Breaking Event payload changes require event_payload_version change.
- Response payloads must preserve version fields.
```

---

# 22. Codex Implementation Notes

Codex must:

```text
cite Event API Spec
cite Event Service Spec
cite this Event API Contract
use Reference Contract for event_reference_id and aggregate references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before exposing payload, actor, aggregate, causation or correlation details
use AI Context Contract for AI-assisted audit summaries
use Human Review Contract where policy requires review
use Versioning Contract for event payload version validation
route all Event reads through Event Service
invoke Permission Service before protected behavior
invoke Policy Service before exposing Event details
return safe errors only
write tests for read/search/validate-reference/aggregate/correlation/audit-trail
write tests for payload visibility restriction
write tests for actor and aggregate redaction
write tests for aggregate query policy restriction
write tests for correlation query policy restriction
write tests that Audit Agent distinguishes trace from inference
write tests that Event API cannot create, mutate, delete or replay Events
write tests that API does not emit Events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Event directly in API layer
mutate, delete or replay Event records
query database directly from API contract implementation
use generic id where event_reference_id is required
expose database IDs, restricted payloads or hidden actor details
skip Permission or Policy checks
emit Events directly from controller/API handler
return unrestricted total_count by default
treat audit trail as compliance certification
allow AI to fabricate missing Event trace
allow AI context to exceed evaluated_data_access_scope
```

---

# 23. Acceptance Criteria

This Event API Contract is accepted only if:

```text
[ ] It defines Event API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Event API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines read event contract.
[ ] It defines search/list events contract.
[ ] It defines validate-reference contract.
[ ] It defines aggregate event stream contract.
[ ] It defines correlation event stream contract.
[ ] It defines audit trail contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event creation boundary rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Event API Contract. Defines governed read, search, validate-reference, aggregate stream, correlation stream and audit-trail payloads, Event immutability boundary, Permission/Policy context, AI audit rules, safe errors, versioning and Codex implementation rules. |

---

**End of API Contract**
