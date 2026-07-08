# Common Contract — Pagination

**Spec ID:** B02-CONTRACT-COMMON-PAGINATION  
**Spec Type:** Common Contract Specification  
**Contract Name:** Pagination Contract  
**Contract File:** core-specs/contracts/common/pagination.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** All Core object specifications where list/search results exist  
**Related Service Specs:** All Core service specifications where list/search operations exist  
**Related API Specs:** All Core API specifications where list/search operations exist  
**Related Event Specs:** Not Applicable unless event list/search is used  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Pagination Contract defines the canonical pagination, sorting and list-window rules used across MarkOrbit Core APIs and services.

It standardizes how list/search responses are returned safely and consistently without exposing unrestricted datasets, bypassing Permission/Policy, leaking hidden records, creating unstable result windows or allowing AI Agents to enumerate data beyond governed scope.

This contract governs:

```text
pagination request shape
pagination response shape
cursor rules
limit rules
sorting rules
filter interaction
permission/policy interaction
AI Agent list access
event list pagination
safe total count behavior
empty result behavior
error behavior
versioning
Codex implementation rules
```

Pagination Contract does not define database indexes, search engine technology, UI table layout or product-specific list screens.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for returning bounded, safe, deterministic list/search result windows.
```

This contract does not mean:

```text
unrestricted export
database paging implementation
UI infinite scroll design
analytics aggregation
data dump
permission bypass
policy bypass
AI data crawler
```

Core rule:

```text
Pagination limits exposure.
Permission controls access.
Policy controls visibility.
Owning service controls query behavior.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
page size limits
cursor shape
pagination request fields
pagination response fields
sort field rules
sort direction rules
safe count behavior
next/previous cursor rules
empty result behavior
pagination validation
pagination errors
AI pagination constraints
```

This contract is not responsible for:

```text
choosing database pagination strategy
choosing search engine
defining product UI
owning domain filters
evaluating permission
evaluating policy
creating export jobs
running analytics
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Owning rule:

```text
The Contracts layer defines enforceable shape. This Pagination Contract provides the common list/search shape used by API, Service, Agent and Event list contracts.
```

---

# 5. Related Core Objects

Pagination may apply to list/search operations for any Core object:

```text
Identity
Organization
User
Permission
Policy
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Matter
Order
Opportunity
WorkflowContract
Task
Event
Notification
Communication
Agent
ServiceProvider
Routing
Partner
ServiceNetwork
```

Rules:

```text
- Item shape is defined by the owning API or Service contract.
- Pagination shape is defined by this common contract.
- Restricted items must be omitted or safely redacted according to Policy.
```

---

# 6. Required References

Pagination context shape:

```yaml
pagination_context:
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  correlation_id: string | null
```

Rules:

```text
- Protected list/search operations require actor or governed agent context.
- Organization-scoped lists require organization_reference_id.
- Agent-assisted pagination requires agent_reference_id and evaluated data access scope.
- correlation_id must be preserved where provided.
```

---

# 7. Contract Shape

## 7.1 Pagination Request Shape

```yaml
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
  include_total_count: boolean | null
```

## 7.2 Pagination Response Shape

```yaml
pagination:
  next_cursor: string | null
  previous_cursor: string | null
  limit: integer
  returned_count: integer
  has_more: boolean
  total_count: integer | null
  total_count_omitted: boolean
```

## 7.3 List Response Envelope

```yaml
result:
  items: list[object]
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Rules:

```text
- items shape is owned by the specific API or Service contract.
- Pagination fields must be stable across list/search APIs.
- total_count may be omitted for policy, performance or security reasons.
- Cursor must not expose internal database keys.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| cursor | string | No | Yes | Opaque cursor from prior response. Must not expose internal IDs. |
| limit | integer | No | Yes | If null, default limit applies. |
| sort.field | string | No | Yes | Must be allowed by owning contract. |
| sort.direction | string | No | Yes | Must be Asc or Desc where provided. |
| include_total_count | boolean | No | Yes | May be ignored or denied by policy. |
| next_cursor | string | Yes | Yes | Null when no further page is available. |
| previous_cursor | string | No | Yes | Optional. Null where reverse pagination is not supported. |
| returned_count | integer | Yes | No | Number of visible items returned. |
| has_more | boolean | Yes | No | True if more visible items may exist. |
| total_count | integer | No | Yes | Null where omitted. |
| total_count_omitted | boolean | Yes | No | True when total_count is omitted. |

---

# 9. Controlled Values

## 9.1 sort.direction

```text
Asc
Desc
```

## 9.2 pagination_strategy

```text
Cursor
Offset
TimeWindow
SearchAfter
Unknown
```

## 9.3 total_count_behavior

```text
Returned
OmittedForPolicy
OmittedForPerformance
OmittedForSecurity
NotSupported
Unknown
```

## 9.4 empty_result_reason

```text
NoMatchingItems
NoVisibleItems
PolicyRestricted
PermissionDenied
InvalidFilter
Unknown
```

Rules:

```text
- Public API should prefer cursor pagination.
- Offset pagination may be allowed only for low-risk internal/admin lists.
- Unknown is not valid for production behavior.
```

---

# 10. Limit Rules

Default limits:

```yaml
default_limit: 20
max_limit_public: 100
max_limit_internal: 500
max_limit_agent: 50
```

Rules:

```text
- limit must be positive.
- limit must not exceed the maximum allowed for the context.
- AI Agent list access should use stricter limits by default.
- Large export must use a separate export/job contract, not pagination.
- Services may lower limits for policy or performance reasons.
```

---

# 11. Cursor Rules

Cursor requirements:

```text
opaque
tamper-resistant
bounded to query/filter context
bounded to permission/policy context where necessary
expires where policy requires
does not expose database primary key
does not expose restricted filter values
```

Rules:

```text
- Cursor must not be constructed by clients.
- Cursor must be returned by service/API.
- Cursor must be invalidated when query context is incompatible.
- Cursor reuse under different filters must fail validation.
```

---

# 12. Sorting Rules

Sort field rules:

```text
- Sort fields must be explicitly allowed by owning contract.
- Sort fields must not expose restricted fields.
- Sort must be deterministic.
- Tie-breaker must be stable internally.
- Internal tie-breaker must not be exposed if restricted.
```

Common safe sort fields:

```text
created_at
updated_at
safe_label
status
priority
due_at
occurred_at
```

Restricted sort fields by default:

```text
internal_score
risk_score
pricing
financial_amount
private_contact
policy_internal_value
permission_internal_value
```

---

# 13. Filter Interaction Rules

Pagination must preserve filter context.

Rules:

```text
- Cursor must be bound to filter context.
- Changing filters requires a new first-page request.
- Filters are owned by the specific API/Service contract.
- Filtered-out restricted items must not reveal their existence.
- Empty page may occur after policy filtering and must be handled safely.
```

---

# 14. Permission Rules

Pagination does not grant access.

Rules:

```text
- Permission must be evaluated before list/search execution.
- returned_count counts visible items only.
- total_count must not reveal restricted item count unless policy allows.
- PermissionDenied stops list/search operation.
```

Required pattern:

```text
request
↓
permission evaluation
↓
policy evaluation
↓
query visible scope
↓
return paginated safe result
```

---

# 15. Policy Rules

Policy may affect pagination.

Policy may:

```text
restrict visible items
redact fields
omit total_count
lower limit
disable sort fields
restrict cursor lifetime
return NotFound/empty instead of PolicyRestricted
```

Rules:

```text
- total_count must be omitted when it may reveal restricted data.
- Policy filtering must occur before response count is finalized.
- Cursor must not allow policy bypass across pages.
- PolicyRestricted must be safe and must not reveal hidden item counts.
```

---

# 16. AI Agent Rules

AI Agent pagination must be constrained.

AI Agent list request context:

```yaml
ai_pagination_context:
  ai_assisted: boolean
  agent_reference_id: string
  agent_registry_key: string
  agent_contract_reference_id: string | null
  data_access_scope: string
  max_pages_allowed: integer | null
```

Rules:

```text
- AI Agents must not enumerate unrestricted datasets.
- AI Agents should use max_limit_agent unless policy allows lower/higher.
- AI Agents must preserve source references from returned items.
- AI Agents must not infer hidden total counts from pagination behavior.
- AI Agents must stop when policy or permission restricts continuation.
```

---

# 17. Event Rules

Event list pagination must preserve event safety.

Rules:

```text
- Event payload visibility may be restricted.
- Event list pagination must not expose hidden event counts where policy forbids.
- Event references are audit trace, not commands.
- Event Service owns event list behavior.
```

---

# 18. Error Rules

Controlled pagination errors:

```text
PaginationInvalid
CursorInvalid
CursorExpired
CursorContextMismatch
LimitInvalid
LimitExceeded
SortFieldInvalid
SortDirectionInvalid
TotalCountRestricted
PaginationPolicyRestricted
PaginationPermissionDenied
```

Safe error shape:

```yaml
error:
  code: string
  category: Validation | Policy | Permission | Request
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Cursor errors must not expose cursor internals.
- Limit errors may state allowed maximum.
- Policy errors must not reveal hidden counts.
- Error shape must follow Error Contract.
```

---

# 19. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Changing default limit requires revision notes.
- Changing max limits requires revision notes.
- Changing cursor meaning is breaking.
- Changing response pagination shape is breaking unless backward compatible.
- Adding sort direction values requires revision notes.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite this Pagination Contract before implementing list/search APIs
use opaque cursors
preserve filter context in cursors
validate limit
apply permission before returning results
apply policy before count/visibility
omit total_count where policy/performance/security requires
preserve correlation_id
return Error Contract shape for pagination errors
write tests for default limit
write tests for max limit
write tests for invalid cursor
write tests for cursor/filter mismatch
write tests for invalid sort field
write tests for total_count omitted
write tests for AI max limit
write tests that restricted counts are not leaked
```

Codex must not:

```text
expose database primary keys in cursors
allow client-constructed cursors
allow cursor reuse across incompatible filters
return unrestricted total_count by default
allow AI agents to enumerate all data
apply pagination before permission/policy in a way that leaks hidden data
use uncontrolled sort fields
return raw database pagination errors
```

---

# 21. Acceptance Criteria

This Pagination Contract is accepted only if:

```text
[ ] It defines pagination purpose.
[ ] It defines pagination meaning.
[ ] It defines pagination boundary.
[ ] It defines related owning spec.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines request, response and list envelope shapes.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines limit rules.
[ ] It defines cursor rules.
[ ] It defines sorting rules.
[ ] It defines filter interaction rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Pagination Contract. Defines request/response envelope, limits, cursors, sorting, filter interaction, permission/policy, AI, event, error, versioning and Codex implementation rules. |

---

**End of Common Contract**
