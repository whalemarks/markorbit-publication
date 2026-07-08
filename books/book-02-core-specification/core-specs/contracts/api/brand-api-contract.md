# API Contract — Brand API

**Spec ID:** B02-CONTRACT-API-BRAND  
**Spec Type:** API Contract Specification  
**Contract Name:** Brand API Contract  
**Contract File:** core-specs/contracts/api/brand-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/brand-api.md  
**Related Domain:** Brand  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/brand-api.md; core-specs/api/customer-api.md; core-specs/api/trademark-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/brand-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Brand API Contract defines the implementation-facing request and response contract for Brand API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and reference Brand records through governed API boundaries without bypassing Brand Service, Customer Service, Trademark Service, Document Service, Evidence Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Brand API versioning
Brand create request
Brand update request
Brand read response
Brand search/list response
Brand reference validation
Brand owner/customer linkage
Trademark relationship references
Document and Evidence linkage
Permission and Policy context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Brand API Contract does not define trademark rights by itself, determine registrability, prove ownership, replace Brand Service, replace Trademark Service, evaluate Permission/Policy, or authorize AI output as final professional advice.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Brand Service through governed API boundaries.
```

This contract does not mean:

```text
trademark record
legal ownership proof
registrability opinion
brand strategy conclusion
customer record
document storage contract
evidence sufficiency contract
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Brand API receives governed brand requests.
Brand Service owns Brand behavior.
Customer, Trademark, Document and Evidence references are validated by owning services.
Permission and Policy govern access.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Brand reference fields
Brand relationship fields
Customer/Trademark/Document/Evidence reference fields
pagination shape for list/search
permission/policy context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Brand lifecycle ownership outside Brand Service
trademark lifecycle management
registrability analysis
brand valuation
document binary storage
evidence sufficiency conclusion
Permission evaluation logic
Policy evaluation logic
Event emission implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/brand-api.md
```

Owning service spec:

```text
core-specs/services/brand-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Brand API and Brand Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Brand
```

Related objects:

```text
Customer
Trademark
Document
Evidence
Permission
Policy
Event
Agent
```

Reference rules:

```text
- brand_reference_id identifies Brand.
- customer_reference_id links Brand to Customer where Brand Service allows.
- trademark_reference_ids link Brand to Trademark records but must not replace Trademark lifecycle.
- document_reference_ids and evidence_reference_ids must be validated by their owning services.
- Permission/Policy decision references must not be treated as approval unless validated by owning services.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  idempotency_key: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Brand target context:

```yaml
target:
  brand_reference_id: string | null
  target_object_type: Brand
  target_object_reference_id: string | null
```

Rules:

```text
- brand_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- customer_reference_id must be validated where provided.
- trademark/document/evidence references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/brands
GET    /v1/brands/{brand_reference_id}
PATCH  /v1/brands/{brand_reference_id}
GET    /v1/brands
POST   /v1/brands/validate-reference
POST   /v1/brands/{brand_reference_id}/link-trademarks
POST   /v1/brands/{brand_reference_id}/link-documents
POST   /v1/brands/{brand_reference_id}/link-evidence
```

Endpoint ownership:

```text
API layer validates request contract.
Brand Service executes behavior.
Customer Service validates customer references.
Trademark Service validates trademark references.
Document Service validates document references.
Evidence Service validates evidence references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
```

---

# 8. Create Brand Request Contract

Endpoint:

```text
POST /v1/brands
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null

permission_context:
  required_permission_keys:
    - brand:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - brand:create:policy
  policy_decision_reference_id: string | null

payload:
  brand_type: string
  brand_status: string | null
  brand_name_safe: string
  brand_display_name_safe: string | null
  customer_reference_id: string | null
  owner_name_safe: string | null
  jurisdiction_reference_ids:
    - string
  trademark_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- brand_type and brand_name_safe are required.
- customer_reference_id must be validated through Customer Service where provided.
- trademark_reference_ids must be validated through Trademark Service where provided.
- document/evidence references must be validated by owning services where provided.
- Brand Service assigns brand_reference_id.
```

---

# 9. Create Brand Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  brand_reference_id: string
  brand_type: string
  brand_status: string
  brand_name_safe: string
  brand_display_name_safe: string | null
  customer_reference_id: string | null
  owner_name_safe: string | null
  created_at: datetime
  updated_at: datetime | null
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- Response must not expose database IDs.
- BrandCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate BrandCreated event.
```

---

# 10. Read Brand Contract

Endpoint:

```text
GET /v1/brands/{brand_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  brand_reference_id: string
  brand_type: string
  brand_status: string
  brand_name_safe: string
  brand_display_name_safe: string | null
  customer_reference_id: string | null
  owner_name_safe: string | null
  jurisdiction_reference_ids:
    - string
  trademark_reference_ids_visible:
    - string
  document_reference_ids_visible:
    - string
  evidence_reference_ids_visible:
    - string
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate brand:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted fields and linked references must be omitted by default where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Brand Contract

Endpoint:

```text
PATCH /v1/brands/{brand_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  brand_status: string | null
  brand_name_safe: string | null
  brand_display_name_safe: string | null
  owner_name_safe: string | null
  jurisdiction_reference_ids_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - brand:update
policy_context:
  required_policy_scopes:
    - brand:update:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  brand_reference_id: string
  brand_status: string
  brand_name_safe: string
  brand_display_name_safe: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Brand Service.
- Brand status transitions must follow Brand Service rules.
- Restricted metadata must not be patched through metadata_safe_patch unless policy allows it.
- Brand update event may be returned only if the event spec exists and service emits it.
```

---

# 12. Search/List Brand Contract

Endpoint:

```text
GET /v1/brands
```

Query parameters:

```yaml
brand_type: string | null
brand_status: string | null
customer_reference_id: string | null
jurisdiction_reference_id: string | null
safe_query: string | null
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
    - brand_reference_id: string
      brand_type: string
      brand_status: string
      brand_name_safe: string
      brand_display_name_safe: string | null
      customer_reference_id: string | null
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
- Search must not reveal restricted Brand existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Brand Reference Contract

Endpoint:

```text
POST /v1/brands/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  brand_reference_id: string
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
  brand_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Brand.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Link Relationship Contracts

Endpoints:

```text
POST /v1/brands/{brand_reference_id}/link-trademarks
POST /v1/brands/{brand_reference_id}/link-documents
POST /v1/brands/{brand_reference_id}/link-evidence
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  reference_ids:
    - string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - brand:link
policy_context:
  required_policy_scopes:
    - brand:link:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  brand_reference_id: string
  linked_reference_type: string
  linked_reference_ids_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Brand Service.
- Linked references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate Trademark, Document or Evidence lifecycle directly.
```

---

# 15. Controlled Values

## 15.1 brand_type

```text
WordBrand
LogoBrand
CombinedBrand
SeriesBrand
ProductBrand
CompanyBrand
PersonalBrand
Unknown
```

## 15.2 brand_status

```text
Draft
Active
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 15.3 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 15.4 linked_reference_type

```text
Trademark
Document
Evidence
Unknown
```

## 15.5 sort.field

```text
created_at
updated_at
brand_name_safe
brand_status
brand_type
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] brand_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] brand_type is controlled.
[ ] brand_status is controlled where provided.
[ ] customer_reference_id is validated where provided.
[ ] trademark_reference_ids are validated where provided.
[ ] document_reference_ids are validated where provided.
[ ] evidence_reference_ids are validated where provided.
[ ] link_operation is controlled.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 17. Permission Rules

Required permission keys:

```text
brand:create
brand:read
brand:search
brand:update
brand:validate
brand:link
```

Rules:

```text
- Brand API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 18. Policy Rules

Required policy scopes may include:

```text
brand:create:policy
brand:read:policy
brand:search:policy
brand:update:policy
brand:reference:policy
brand:visibility:policy
brand:link:policy
brand:relationship:visibility:policy
cross-organization:brand
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact owner, customer, linked trademark/document/evidence references or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 19. AI and Human Review Rules

AI rules:

```text
- AI may summarize Brand context only within Permission and Policy limits.
- AI must not decide legal ownership, registrability, conflict risk or evidence sufficiency.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Brand API output is used for professional decision, filing strategy, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 20. Idempotency and Event Rules

Idempotency:

```text
POST /v1/brands requires idempotency_key.
PATCH /v1/brands/{brand_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link relationship endpoints may require idempotency_key for Add/Remove/Replace operations.
```

Events:

```text
BrandCreated may be emitted by Brand Service after successful creation.
BrandUpdated may be reserved for later if event spec exists.
Brand relationship link events may be reserved for later if event specs exist.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 21. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
CustomerReferenceInvalid
TrademarkReferenceInvalid
DocumentReferenceInvalid
EvidenceReferenceInvalid
LinkOperationInvalid
StateInvalid
IdempotencyKeyRequired
IdempotencyConflict
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
- Errors must not expose database IDs, restricted Brand data, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 22. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 23. Codex Implementation Notes

Codex must:

```text
cite Brand API Spec
cite Brand Service Spec
cite this Brand API Contract
use Reference Contract for brand_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted brand summaries where applicable
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Brand Service
invoke Customer/Trademark/Document/Evidence services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields or relationship references
return safe errors only
write tests for create/read/update/search/validate-reference/link relationships
write tests for linked reference validation
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Brand directly in API layer
query database directly from API contract implementation
use generic id where brand_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Trademark/Document/Evidence lifecycle through Brand link endpoints
treat Brand as Trademark
treat Brand ownership as legal proof by itself
```

---

# 24. Acceptance Criteria

This Brand API Contract is accepted only if:

```text
[ ] It defines Brand API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Brand API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link relationship contracts.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 25. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Brand API Contract. Defines governed create, read, update, search, validate-reference and relationship-link payloads, Customer/Trademark/Document/Evidence references, Permission/Policy context, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
