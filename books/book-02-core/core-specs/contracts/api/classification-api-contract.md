# API Contract — Classification API

**Spec ID:** B02-CONTRACT-API-CLASSIFICATION  
**Spec Type:** API Contract Specification  
**Contract Name:** Classification API Contract  
**Contract File:** core-specs/contracts/api/classification-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/classification-api.md  
**Related Domain:** Classification  
**Related Object Specs:** core-specs/objects/classification.md; core-specs/objects/trademark.md; core-specs/objects/jurisdiction.md; core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/classification-service.md; core-specs/services/trademark-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/classification-api.md; core-specs/api/trademark-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/knowledge-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/classification-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Classification API Contract defines the implementation-facing request and response contract for Classification API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, suggest and reference Classification records through governed API boundaries without bypassing Classification Service, Jurisdiction Service, Trademark Service, Knowledge Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Classification API versioning
Classification create request
Classification update request
Classification read response
Classification search/list response
Classification reference validation
Goods/services item validation
Classification suggestion request/response
Jurisdiction rule context
Trademark linkage
Knowledge and Document source linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Classification API Contract does not provide legal opinion, guarantee goods/services acceptability, determine Nice class finality, replace professional review, replace Classification Service, evaluate Permission/Policy, or authorize AI output as final classification advice.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Classification Service through governed API boundaries.
```

This contract does not mean:

```text
final legal classification
official goods/services acceptance
filing submission
trademark registrability opinion
jurisdiction rule finality
AI classification finality
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Classification API receives governed classification requests.
Classification Service owns Classification behavior.
Jurisdiction, Trademark, Knowledge and Document references are validated by owning services.
Permission and Policy govern access.
Classification suggestions are assistance until accepted through governed human/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Classification reference fields
goods/services item fields
jurisdiction and trademark reference fields
classification suggestion payloads
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
Classification lifecycle ownership outside Classification Service
official acceptance by trademark offices
legal interpretation finality
filing strategy approval
goods/services professional approval
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
core-specs/api/classification-api.md
```

Owning service spec:

```text
core-specs/services/classification-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Classification API and Classification Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Classification
```

Related objects:

```text
Trademark
Jurisdiction
Knowledge
Document
Permission
Policy
Event
Agent
```

Reference rules:

```text
- classification_reference_id identifies Classification.
- trademark_reference_id may link Classification to Trademark context where Classification Service allows.
- jurisdiction_reference_id must be validated by Jurisdiction Service.
- knowledge_record_reference_ids and document_reference_ids must be validated by owning services.
- class_number is a classification value but must not replace classification_reference_id.
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

Classification target context:

```yaml
target:
  classification_reference_id: string | null
  target_object_type: Classification
  target_object_reference_id: string | null
```

Rules:

```text
- classification_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- jurisdiction_reference_id must be validated where provided.
- trademark/knowledge/document references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/classifications
GET    /v1/classifications/{classification_reference_id}
PATCH  /v1/classifications/{classification_reference_id}
GET    /v1/classifications
POST   /v1/classifications/validate-reference
POST   /v1/classifications/validate-items
POST   /v1/classifications/suggest
POST   /v1/classifications/{classification_reference_id}/link-trademark
POST   /v1/classifications/{classification_reference_id}/link-knowledge
POST   /v1/classifications/{classification_reference_id}/link-documents
```

Endpoint ownership:

```text
API layer validates request contract.
Classification Service executes behavior.
Jurisdiction Service validates jurisdiction references.
Trademark Service validates trademark references.
Knowledge Service validates knowledge references.
Document Service validates document references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
```

---

# 8. Create Classification Request Contract

Endpoint:

```text
POST /v1/classifications
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
    - classification:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - classification:create:policy
  policy_decision_reference_id: string | null

payload:
  classification_type: string
  classification_status: string | null
  jurisdiction_reference_id: string | null
  trademark_reference_id: string | null
  class_system: string
  class_number: string | null
  goods_services_items:
    - item_text_safe: string
      item_language: string | null
      item_status: string | null
      source_reference_ids:
        - string
  knowledge_record_reference_ids:
    - string
  document_reference_ids:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- classification_type and class_system are required.
- class_number is required where classification_type is class-specific.
- goods_services_items must be non-empty where classification is item-based.
- jurisdiction_reference_id must be validated by Jurisdiction Service where provided.
- trademark_reference_id must be validated by Trademark Service where provided.
- Classification Service assigns classification_reference_id.
```

---

# 9. Create Classification Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  classification_reference_id: string
  classification_type: string
  classification_status: string
  jurisdiction_reference_id: string | null
  trademark_reference_id: string | null
  class_system: string
  class_number: string | null
  goods_services_items_visible:
    - item_reference_id: string | null
      item_text_safe: string
      item_status: string | null
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
- ClassificationCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate ClassificationCreated event.
```

---

# 10. Read Classification Contract

Endpoint:

```text
GET /v1/classifications/{classification_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  classification_reference_id: string
  classification_type: string
  classification_status: string
  jurisdiction_reference_id: string | null
  trademark_reference_id: string | null
  class_system: string
  class_number: string | null
  goods_services_items_visible:
    - item_reference_id: string | null
      item_text_safe: string
      item_language: string | null
      item_status: string | null
      source_reference_ids_visible:
        - string
  knowledge_record_reference_ids_visible:
    - string
  document_reference_ids_visible:
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
- Read must evaluate classification:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted item text, source references and linked references must be omitted by default where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Classification Contract

Endpoint:

```text
PATCH /v1/classifications/{classification_reference_id}
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
  classification_status: string | null
  class_number: string | null
  goods_services_items_patch:
    - item_reference_id: string | null
      item_text_safe: string | null
      item_language: string | null
      item_status: string | null
      operation: Add | Update | Remove | Replace
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - classification:update
policy_context:
  required_policy_scopes:
    - classification:update:policy
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
  classification_reference_id: string
  classification_status: string
  class_system: string
  class_number: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Classification Service.
- Item changes must follow Classification Service rules.
- Human review may be required for professional classification changes.
- Classification update event may be returned only if the event spec exists and service emits it.
```

---

# 12. Search/List Classification Contract

Endpoint:

```text
GET /v1/classifications
```

Query parameters:

```yaml
classification_type: string | null
classification_status: string | null
jurisdiction_reference_id: string | null
trademark_reference_id: string | null
class_system: string | null
class_number: string | null
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
    - classification_reference_id: string
      classification_type: string
      classification_status: string
      jurisdiction_reference_id: string | null
      trademark_reference_id: string | null
      class_system: string
      class_number: string | null
      item_summary_safe: string | null
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
- Search must not reveal restricted Classification existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Classification Reference Contract

Endpoint:

```text
POST /v1/classifications/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  classification_reference_id: string
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
  classification_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Classification.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or item detail.
```

---

# 14. Validate Items Contract

Endpoint:

```text
POST /v1/classifications/validate-items
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
    - classification:item:validate
policy_context:
  required_policy_scopes:
    - classification:item:validate:policy
payload:
  jurisdiction_reference_id: string | null
  class_system: string
  class_number: string | null
  goods_services_items:
    - item_text_safe: string
      item_language: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  validation_status: string
  item_results:
    - item_text_safe: string
      item_valid: boolean
      item_status: string
      safe_reason: string | null
      suggested_item_text_safe: string | null
      restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Item validation is assistance unless owning service confirms it as accepted internal validation.
- Official acceptability is not guaranteed.
- Human review may be required before filing or customer-facing output.
```

---

# 15. Suggest Classification Contract

Endpoint:

```text
POST /v1/classifications/suggest
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
    - classification:suggest
policy_context:
  required_policy_scopes:
    - classification:suggest:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  brand_reference_id: string | null
  trademark_reference_id: string | null
  jurisdiction_reference_id: string | null
  goods_services_description_safe: string
  requested_class_system: string | null
  max_suggestions: integer | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  suggestion_status: string
  suggestions:
    - class_system: string
      class_number: string | null
      suggested_items:
        - item_text_safe: string
          item_language: string | null
      source_reference_ids_visible:
        - string
      confidence_level: string | null
      restricted_fields_omitted: boolean
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Suggestions are source-grounded assistance, not professional truth.
- AI-assisted suggestions must follow AI governance and Knowledge Agent rules.
- Human review may be required before creating final Classification or filing.
```

---

# 16. Link Relationship Contracts

Endpoints:

```text
POST /v1/classifications/{classification_reference_id}/link-trademark
POST /v1/classifications/{classification_reference_id}/link-knowledge
POST /v1/classifications/{classification_reference_id}/link-documents
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
    - classification:link
policy_context:
  required_policy_scopes:
    - classification:link:policy
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
  classification_reference_id: string
  linked_reference_type: string
  linked_reference_ids_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Classification Service.
- Linked references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate Trademark, Knowledge or Document lifecycle directly.
```

---

# 17. Controlled Values

## 17.1 classification_type

```text
NiceClass
GoodsServicesSet
JurisdictionSpecificItem
InternalRecommendation
FilingDraft
Unknown
```

## 17.2 classification_status

```text
Draft
Suggested
UnderReview
Approved
Rejected
Filed
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 class_system

```text
Nice
USPTO
CNIPA
EUIPO
Madrid
JurisdictionSpecific
Internal
Unknown
```

## 17.4 item_status

```text
Draft
Suggested
Validated
Rejected
Approved
Filed
DeletedReferenceOnly
Unknown
```

## 17.5 validation_status

```text
Valid
Invalid
Partial
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Deprecated
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 17.6 suggestion_status

```text
Completed
Partial
NoResult
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.7 confidence_level

```text
High
Medium
Low
Unknown
```

## 17.8 linked_reference_type

```text
Trademark
Knowledge
Document
Unknown
```

## 17.9 sort.field

```text
created_at
updated_at
classification_status
classification_type
class_system
class_number
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] classification_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] classification_type is controlled.
[ ] classification_status is controlled where provided.
[ ] class_system is controlled.
[ ] class_number is valid for class_system where required.
[ ] goods_services_items are present where required.
[ ] item_text_safe is non-empty where provided.
[ ] jurisdiction_reference_id is validated where provided.
[ ] trademark_reference_id is validated where provided.
[ ] knowledge/document references are validated where provided.
[ ] link_operation is controlled.
[ ] AI Context is present for AI-assisted suggestions.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 19. Permission Rules

Required permission keys:

```text
classification:create
classification:read
classification:search
classification:update
classification:validate
classification:item:validate
classification:suggest
classification:link
```

Rules:

```text
- Classification API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
classification:create:policy
classification:read:policy
classification:search:policy
classification:update:policy
classification:reference:policy
classification:item:validate:policy
classification:suggest:policy
classification:visibility:policy
classification:link:policy
classification:relationship:visibility:policy
cross-organization:classification
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact item text, sources, suggestions, linked references or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before professional use.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may suggest classes/items only within Permission and Policy limits.
- AI must not decide official acceptability, final Nice class, filing readiness or legal sufficiency.
- AI output must disclose source scope, confidence, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where classification output is used for filing, professional decision, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/classifications requires idempotency_key.
PATCH /v1/classifications/{classification_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link endpoints may require idempotency_key for Add/Remove/Replace operations.
Suggestion and item validation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
ClassificationCreated may be emitted by Classification Service after successful creation.
Classification update/link events may be reserved for later if event specs exist.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 23. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
JurisdictionReferenceInvalid
TrademarkReferenceInvalid
KnowledgeReferenceInvalid
DocumentReferenceInvalid
ClassSystemInvalid
ClassNumberInvalid
GoodsServicesItemInvalid
SuggestionUnavailable
LinkOperationInvalid
HumanReviewRequired
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
- Errors must not expose database IDs, restricted classification data, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 24. Versioning Rules

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

# 25. Codex Implementation Notes

Codex must:

```text
cite Classification API Spec
cite Classification Service Spec
cite this Classification API Contract
use Reference Contract for classification_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted suggestions
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Classification Service
invoke Jurisdiction/Trademark/Knowledge/Document services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields, items, sources or suggestions
return safe errors only
write tests for create/read/update/search/validate-reference/validate-items/suggest/link relationships
write tests for class_system and class_number validation
write tests for goods/services item validation
write tests for jurisdiction/trademark/knowledge/document reference validation
write tests for AI suggestion source disclosure
write tests for human_review_required
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Classification directly in API layer
query database directly from API contract implementation
use generic id where classification_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Trademark/Knowledge/Document lifecycle through Classification link endpoints
treat class_number as Core classification_reference_id
treat suggestions as legal conclusion or filing-ready approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Classification API Contract is accepted only if:

```text
[ ] It defines Classification API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Classification API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines validate-items contract.
[ ] It defines suggest contract.
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

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Classification API Contract. Defines governed create, read, update, search, validate-reference, validate-items, suggest and relationship-link payloads, Jurisdiction/Trademark/Knowledge/Document references, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
