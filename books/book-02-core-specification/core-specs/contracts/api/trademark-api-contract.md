# API Contract — Trademark API

**Spec ID:** B02-CONTRACT-API-TRADEMARK  
**Spec Type:** API Contract Specification  
**Contract Name:** Trademark API Contract  
**Contract File:** core-specs/contracts/api/trademark-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/trademark-api.md  
**Related Domain:** Trademark  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/matter.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/matter-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/brand-api.md; core-specs/api/customer-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/classification-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/matter-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/trademark-created.md; core-specs/events/jurisdiction-linked.md; core-specs/events/classification-created.md; core-specs/events/document-created.md; core-specs/events/evidence-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Trademark API Contract defines the implementation-facing request and response contract for Trademark API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and reference Trademark records through governed API boundaries without bypassing Trademark Service, Brand Service, Jurisdiction Service, Classification Service, Document Service, Evidence Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Trademark API versioning
Trademark create request
Trademark update request
Trademark read response
Trademark search/list response
Trademark reference validation
Brand and Customer linkage
Jurisdiction linkage
Classification linkage
Document and Evidence linkage
Matter linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Trademark API Contract does not determine registrability, provide legal opinion, submit official filings, replace professional review, replace Trademark Service, evaluate Permission/Policy, or authorize AI output as final professional advice.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Trademark Service through governed API boundaries.
```

This contract does not mean:

```text
official trademark filing
registrability opinion
legal conclusion
classification finality
evidence sufficiency
brand ownership proof
filing submission authorization
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Trademark API receives governed trademark requests.
Trademark Service owns Trademark behavior.
Brand, Jurisdiction, Classification, Document, Evidence and Matter references are validated by owning services.
Permission and Policy govern access.
Professional truth requires governed human/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Trademark reference fields
Brand/Customer/Jurisdiction/Classification/Document/Evidence/Matter reference fields
pagination shape for list/search
permission/policy context requirements
AI and human-review context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Trademark lifecycle ownership outside Trademark Service
official filing submission
registrability analysis finality
classification professional approval
evidence sufficiency conclusion
document binary storage
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
core-specs/api/trademark-api.md
```

Owning service spec:

```text
core-specs/services/trademark-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Trademark API and Trademark Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Trademark
```

Related objects:

```text
Brand
Customer
Jurisdiction
Classification
Document
Evidence
Matter
Permission
Policy
Event
Agent
```

Reference rules:

```text
- trademark_reference_id identifies Trademark.
- brand_reference_id links Trademark to Brand where Trademark Service allows.
- customer_reference_id may link Trademark to Customer context where owning services allow.
- jurisdiction_reference_id must be validated by Jurisdiction Service.
- classification_reference_ids must be validated by Classification Service.
- document_reference_ids and evidence_reference_ids must be validated by owning services.
- matter_reference_id must be validated by Matter Service where provided.
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

Trademark target context:

```yaml
target:
  trademark_reference_id: string | null
  target_object_type: Trademark
  target_object_reference_id: string | null
```

Rules:

```text
- trademark_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- jurisdiction_reference_id must be validated where provided.
- brand/customer/classification/document/evidence/matter references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/trademarks
GET    /v1/trademarks/{trademark_reference_id}
PATCH  /v1/trademarks/{trademark_reference_id}
GET    /v1/trademarks
POST   /v1/trademarks/validate-reference
POST   /v1/trademarks/{trademark_reference_id}/link-classifications
POST   /v1/trademarks/{trademark_reference_id}/link-documents
POST   /v1/trademarks/{trademark_reference_id}/link-evidence
POST   /v1/trademarks/{trademark_reference_id}/link-matter
```

Endpoint ownership:

```text
API layer validates request contract.
Trademark Service executes behavior.
Brand Service validates brand references.
Customer Service validates customer references.
Jurisdiction Service validates jurisdiction references.
Classification Service validates classification references.
Document Service validates document references.
Evidence Service validates evidence references.
Matter Service validates matter references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
```

---

# 8. Create Trademark Request Contract

Endpoint:

```text
POST /v1/trademarks
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
    - trademark:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - trademark:create:policy
  policy_decision_reference_id: string | null

payload:
  trademark_type: string
  trademark_status: string | null
  mark_text_safe: string | null
  mark_image_document_reference_id: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  owner_name_safe: string | null
  jurisdiction_reference_id: string | null
  application_number_safe: string | null
  registration_number_safe: string | null
  filing_date: date | null
  registration_date: date | null
  classification_reference_ids:
    - string
  document_reference_ids:
    - string
  evidence_reference_ids:
    - string
  matter_reference_id: string | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- trademark_type is required.
- mark_text_safe or mark_image_document_reference_id should be present unless status/type allows placeholder.
- brand_reference_id must be validated through Brand Service where provided.
- jurisdiction_reference_id must be validated through Jurisdiction Service where provided.
- classification/document/evidence/matter references must be validated by owning services where provided.
- application_number_safe and registration_number_safe are official identifiers but not Core reference IDs.
- Trademark Service assigns trademark_reference_id.
```

---

# 9. Create Trademark Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  trademark_reference_id: string
  trademark_type: string
  trademark_status: string
  mark_text_safe: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  jurisdiction_reference_id: string | null
  application_number_safe: string | null
  registration_number_safe: string | null
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
- TrademarkCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate TrademarkCreated event.
```

---

# 10. Read Trademark Contract

Endpoint:

```text
GET /v1/trademarks/{trademark_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  trademark_reference_id: string
  trademark_type: string
  trademark_status: string
  mark_text_safe: string | null
  mark_image_document_reference_id: string | null
  brand_reference_id: string | null
  customer_reference_id: string | null
  owner_name_safe: string | null
  jurisdiction_reference_id: string | null
  application_number_safe: string | null
  registration_number_safe: string | null
  filing_date: date | null
  registration_date: date | null
  classification_reference_ids_visible:
    - string
  document_reference_ids_visible:
    - string
  evidence_reference_ids_visible:
    - string
  matter_reference_id: string | null
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
- Read must evaluate trademark:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted fields and linked references must be omitted by default where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Trademark Contract

Endpoint:

```text
PATCH /v1/trademarks/{trademark_reference_id}
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
  trademark_status: string | null
  mark_text_safe: string | null
  owner_name_safe: string | null
  application_number_safe: string | null
  registration_number_safe: string | null
  filing_date: date | null
  registration_date: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - trademark:update
policy_context:
  required_policy_scopes:
    - trademark:update:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  trademark_reference_id: string
  trademark_status: string
  mark_text_safe: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Trademark Service.
- Trademark status transitions must follow Trademark Service rules.
- Restricted metadata must not be patched through metadata_safe_patch unless policy allows it.
- Human review may be required for professional-state transitions.
- Trademark update event may be returned only if the event spec exists and service emits it.
```

---

# 12. Search/List Trademark Contract

Endpoint:

```text
GET /v1/trademarks
```

Query parameters:

```yaml
trademark_type: string | null
trademark_status: string | null
brand_reference_id: string | null
customer_reference_id: string | null
jurisdiction_reference_id: string | null
application_number_safe: string | null
registration_number_safe: string | null
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
    - trademark_reference_id: string
      trademark_type: string
      trademark_status: string
      mark_text_safe: string | null
      brand_reference_id: string | null
      customer_reference_id: string | null
      jurisdiction_reference_id: string | null
      application_number_safe: string | null
      registration_number_safe: string | null
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
- Search must not reveal restricted Trademark existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Trademark Reference Contract

Endpoint:

```text
POST /v1/trademarks/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  trademark_reference_id: string
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
  trademark_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Trademark.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Link Relationship Contracts

Endpoints:

```text
POST /v1/trademarks/{trademark_reference_id}/link-classifications
POST /v1/trademarks/{trademark_reference_id}/link-documents
POST /v1/trademarks/{trademark_reference_id}/link-evidence
POST /v1/trademarks/{trademark_reference_id}/link-matter
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
    - trademark:link
policy_context:
  required_policy_scopes:
    - trademark:link:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  trademark_reference_id: string
  linked_reference_type: string
  linked_reference_ids_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Trademark Service.
- Linked references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate Classification, Document, Evidence or Matter lifecycle directly.
- Human review may be required where classification/evidence relationship affects professional decision.
```

---

# 15. Controlled Values

## 15.1 trademark_type

```text
WordMark
LogoMark
CombinedMark
ThreeDimensionalMark
ColorMark
SoundMark
PositionMark
PatternMark
MotionMark
Other
Unknown
```

## 15.2 trademark_status

```text
Draft
Proposed
Filed
Pending
Published
Registered
Refused
Opposed
Cancelled
Expired
Abandoned
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
Classification
Document
Evidence
Matter
Unknown
```

## 15.5 sort.field

```text
created_at
updated_at
filing_date
registration_date
mark_text_safe
trademark_status
trademark_type
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] trademark_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] trademark_type is controlled.
[ ] trademark_status is controlled where provided.
[ ] mark text or mark image reference is present where required.
[ ] brand_reference_id is validated where provided.
[ ] customer_reference_id is validated where provided.
[ ] jurisdiction_reference_id is validated where provided.
[ ] classification_reference_ids are validated where provided.
[ ] document_reference_ids are validated where provided.
[ ] evidence_reference_ids are validated where provided.
[ ] matter_reference_id is validated where provided.
[ ] link_operation is controlled.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] Human Review Context is present where policy requires review.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 17. Permission Rules

Required permission keys:

```text
trademark:create
trademark:read
trademark:search
trademark:update
trademark:validate
trademark:link
```

Rules:

```text
- Trademark API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 18. Policy Rules

Required policy scopes may include:

```text
trademark:create:policy
trademark:read:policy
trademark:search:policy
trademark:update:policy
trademark:reference:policy
trademark:visibility:policy
trademark:link:policy
trademark:relationship:visibility:policy
cross-organization:trademark
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact owner, customer, application, registration, linked references or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review for professional-state transitions.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 19. AI and Human Review Rules

AI rules:

```text
- AI may summarize Trademark context only within Permission and Policy limits.
- AI must not decide registrability, confusion risk, legal status finality, classification sufficiency or evidence sufficiency.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Trademark API output is used for filing strategy, professional decision, external communication, customer-facing recommendation or status transition.
- human_review_required must be explicit where policy requires review.
```

---

# 20. Idempotency and Event Rules

Idempotency:

```text
POST /v1/trademarks requires idempotency_key.
PATCH /v1/trademarks/{trademark_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link relationship endpoints may require idempotency_key for Add/Remove/Replace operations.
```

Events:

```text
TrademarkCreated may be emitted by Trademark Service after successful creation.
JurisdictionLinked may be emitted where jurisdiction link behavior is owned and event spec applies.
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
BrandReferenceInvalid
CustomerReferenceInvalid
JurisdictionReferenceInvalid
ClassificationReferenceInvalid
DocumentReferenceInvalid
EvidenceReferenceInvalid
MatterReferenceInvalid
LinkOperationInvalid
StateInvalid
HumanReviewRequired
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
- Errors must not expose database IDs, restricted Trademark data, policy internals or permission internals.
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
cite Trademark API Spec
cite Trademark Service Spec
cite this Trademark API Contract
use Reference Contract for trademark_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted trademark summaries where applicable
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Trademark Service
invoke Brand/Customer/Jurisdiction/Classification/Document/Evidence/Matter services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields or relationship references
return safe errors only
write tests for create/read/update/search/validate-reference/link relationships
write tests for jurisdiction/classification/document/evidence reference validation
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for HumanReviewRequired
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Trademark directly in API layer
query database directly from API contract implementation
use generic id where trademark_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Classification/Document/Evidence/Matter lifecycle through Trademark link endpoints
treat Trademark as Brand
treat Trademark API output as registrability opinion or legal conclusion
submit official filings from this API contract
```

---

# 24. Acceptance Criteria

This Trademark API Contract is accepted only if:

```text
[ ] It defines Trademark API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Trademark API and Service specs.
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
| 0.1.0 | Draft | Initial Trademark API Contract. Defines governed create, read, update, search, validate-reference and relationship-link payloads, Brand/Customer/Jurisdiction/Classification/Document/Evidence/Matter references, Permission/Policy context, human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---


## Canonical Status Contract Consumption

Trademark API Contract consumes `core-specs/controlled-state-values/trademark-status-values.md`. Requests cannot define new Trademark statuses, cannot bypass Trademark Service, cannot use PATCH or generic update to bypass invalid transitions, and responses/errors must preserve source, reason and requirement context without adding endpoints or changing endpoint paths.

## Status Transition Contract Consumption

Related Contracts: [Trademark Status Contract](../status/trademark-status-contract.md) and [Status Transition Contract](../status/status-transition-contract.md).

Status Transition request validation consumes the shared `status_transition_request` shape. API validation responses consume `status_transition_decision`. Owner Service execution is required before a performed `status_transition_result` can exist. Generic PATCH or update semantics must not bypass the status contract, endpoint paths do not change, no endpoint is added, API does not directly mutate status, and responses must not return legacy statuses that conflict with the canonical status list.

**End of API Contract**
