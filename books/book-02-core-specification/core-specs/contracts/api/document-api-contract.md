# API Contract — Document API

**Spec ID:** B02-CONTRACT-API-DOCUMENT  
**Spec Type:** API Contract Specification  
**Contract Name:** Document API Contract  
**Contract File:** core-specs/contracts/api/document-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/document-api.md  
**Related Domain:** Document  
**Related Object Specs:** core-specs/objects/document.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/evidence.md; core-specs/objects/matter.md; core-specs/objects/customer.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/document-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/evidence-service.md; core-specs/services/matter-service.md; core-specs/services/customer-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/document-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/evidence-api.md; core-specs/api/matter-api.md; core-specs/api/customer-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/document-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Document API Contract defines the implementation-facing request and response contract for Document API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and reference Document records through governed API boundaries without bypassing Document Service, related owning services, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Document API versioning
Document metadata create request
Document update request
Document read response
Document search/list response
Document reference validation
Document relationship linkage
Document content access context
Document extraction/summary preparation context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Document API Contract does not define binary storage implementation, OCR implementation, legal sufficiency, evidence sufficiency, filing readiness, professional review, or official submission by itself.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Document Service through governed API boundaries.
```

This contract does not mean:

```text
file storage engine
binary upload protocol by itself
OCR engine
legal document approval
evidence sufficiency conclusion
filing-ready document approval
external communication approval
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Document API receives governed document requests.
Document Service owns Document behavior.
Linked domain references are validated by owning services.
Permission and Policy govern access.
Document content access is policy-controlled.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Document reference fields
Document metadata fields
content access metadata
relationship link fields
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
physical file storage
virus scanning implementation
OCR/extraction implementation
professional document sufficiency
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
core-specs/api/document-api.md
```

Owning service spec:

```text
core-specs/services/document-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Document API and Document Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Document
```

Related objects:

```text
Brand
Trademark
Evidence
Matter
Customer
Knowledge
Communication
Permission
Policy
Event
Agent
```

Reference rules:

```text
- document_reference_id identifies Document.
- linked target references must be validated by their owning services.
- storage_reference_id or file_reference_id is storage-level reference and must not replace document_reference_id.
- extracted_text_reference_id is not professional truth.
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

Document target context:

```yaml
target:
  document_reference_id: string | null
  target_object_type: Document
  target_object_reference_id: string | null
```

Rules:

```text
- document_reference_id is required for read/update/validate-by-reference/content-access operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked target references must be validated where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/documents
GET    /v1/documents/{document_reference_id}
PATCH  /v1/documents/{document_reference_id}
GET    /v1/documents
POST   /v1/documents/validate-reference
POST   /v1/documents/{document_reference_id}/content-access
POST   /v1/documents/{document_reference_id}/link-targets
POST   /v1/documents/{document_reference_id}/prepare-summary
```

Endpoint ownership:

```text
API layer validates request contract.
Document Service executes behavior.
Related owning services validate target references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs agent context where AI-assisted summary is used.
Event Service records events emitted by owning services.
```

---

# 8. Create Document Request Contract

Endpoint:

```text
POST /v1/documents
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
    - document:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - document:create:policy
  policy_decision_reference_id: string | null

payload:
  document_type: string
  document_status: string | null
  document_title_safe: string
  file_reference_id: string | null
  storage_reference_id: string | null
  mime_type: string | null
  file_size_bytes: integer | null
  checksum_safe: string | null
  source_type: string | null
  linked_targets:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- document_type and document_title_safe are required.
- file_reference_id/storage_reference_id are optional only for metadata-only documents.
- linked targets must be validated by owning services where provided.
- checksum_safe must not expose restricted content.
- Document Service assigns document_reference_id.
```

---

# 9. Create Document Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  document_reference_id: string
  document_type: string
  document_status: string
  document_title_safe: string
  mime_type: string | null
  file_size_bytes: integer | null
  source_type: string | null
  linked_targets_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
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
- DocumentCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate DocumentCreated event.
```

---

# 10. Read Document Contract

Endpoint:

```text
GET /v1/documents/{document_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  document_reference_id: string
  document_type: string
  document_status: string
  document_title_safe: string
  mime_type: string | null
  file_size_bytes: integer | null
  checksum_visible: string | null
  source_type: string | null
  linked_targets_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  extracted_text_available: boolean
  content_access_available: boolean
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
- Read must evaluate document:read permission.
- Policy may downgrade response to metadata-only.
- Raw content, checksum and linked targets may be omitted by policy.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Document Contract

Endpoint:

```text
PATCH /v1/documents/{document_reference_id}
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
  document_status: string | null
  document_title_safe: string | null
  source_type: string | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - document:update
policy_context:
  required_policy_scopes:
    - document:update:policy
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
  document_reference_id: string
  document_status: string
  document_title_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Document Service.
- Document status transitions must follow Document Service rules.
- Restricted metadata must not be patched through metadata_safe_patch unless policy allows it.
- Human review may be required for finalization or filing-use transitions.
```

---

# 12. Search/List Document Contract

Endpoint:

```text
GET /v1/documents
```

Query parameters:

```yaml
document_type: string | null
document_status: string | null
target_object_type: string | null
target_object_reference_id: string | null
source_type: string | null
mime_type: string | null
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
    - document_reference_id: string
      document_type: string
      document_status: string
      document_title_safe: string
      mime_type: string | null
      file_size_bytes: integer | null
      source_type: string | null
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
- Search must not reveal restricted Document existence.
- safe_query must not be treated as unrestricted search over raw content.
```

---

# 13. Validate Document Reference Contract

Endpoint:

```text
POST /v1/documents/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  document_reference_id: string
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
  document_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  document_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read raw content.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or document type.
```

---

# 14. Content Access Contract

Endpoint:

```text
POST /v1/documents/{document_reference_id}/content-access
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
    - document:content:read
policy_context:
  required_policy_scopes:
    - document:content:read:policy
payload:
  access_purpose: string
  requested_content_scope: string
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
  document_reference_id: string
  content_access_status: string
  evaluated_content_scope: string
  content_reference_id: string | null
  content_preview_safe: string | null
  expires_at: datetime | null
  restricted_fields_omitted: boolean
policy_context:
  policy_decision_reference_id: string | null
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Raw content access is policy-controlled.
- content_reference_id must not expose storage internals.
- Preview must be safe and policy-filtered.
- Human review may be required for restricted document content use.
```

---

# 15. Link Targets Contract

Endpoint:

```text
POST /v1/documents/{document_reference_id}/link-targets
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  linked_targets:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - document:link
policy_context:
  required_policy_scopes:
    - document:link:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  document_reference_id: string
  linked_targets_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Document Service.
- Linked target references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate target object lifecycle directly.
```

---

# 16. Prepare Summary Contract

Endpoint:

```text
POST /v1/documents/{document_reference_id}/prepare-summary
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
    - document:summary:prepare
policy_context:
  required_policy_scopes:
    - document:summary:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  summary_purpose: string
  requested_summary_scope: string
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
  summary_status: string
  summary_safe: string | null
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
- Summary is assistance, not professional truth.
- AI-assisted summary must follow AI governance.
- Policy may downgrade to metadata-only or safe-summary-only.
- Human review may be required before external or professional use.
```

---

# 17. Controlled Values

## 17.1 document_type

```text
ApplicationForm
PowerOfAttorney
Certificate
OfficeAction
ResponseDraft
EvidenceDocument
IdentityDocument
BusinessLicense
Invoice
EmailRecord
Screenshot
Template
InternalNote
Other
Unknown
```

## 17.2 document_status

```text
Draft
Uploaded
Processing
Active
UnderReview
Approved
Rejected
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 source_type

```text
UserUpload
SystemGenerated
EmailAttachment
ExternalSource
OfficialSource
AgentPrepared
AIGeneratedDraft
ManualRecord
Unknown
```

## 17.4 relationship_type

```text
PrimaryDocument
SupportingDocument
EvidenceSource
OfficialRecord
CustomerProvided
AgentProvided
InternalReference
CommunicationAttachment
Unknown
```

## 17.5 content_access_status

```text
Allowed
Denied
Restricted
PreviewOnly
MetadataOnly
RequiresHumanReview
Expired
Unknown
```

## 17.6 content_scope

```text
MetadataOnly
Preview
ExtractedText
FullContent
DownloadReference
Unknown
```

## 17.7 summary_status

```text
Completed
Partial
NoContent
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.8 validation_status

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

## 17.9 sort.field

```text
created_at
updated_at
document_title_safe
document_status
document_type
mime_type
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] document_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] document_type is controlled.
[ ] document_status is controlled where provided.
[ ] file_reference_id/storage_reference_id is present where non-metadata document requires it.
[ ] linked target references are validated where provided.
[ ] relationship_type is controlled.
[ ] content access scope is controlled.
[ ] AI Context is present for AI-assisted summary.
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
document:create
document:read
document:search
document:update
document:validate
document:link
document:content:read
document:summary:prepare
```

Rules:

```text
- Document API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
document:create:policy
document:read:policy
document:search:policy
document:update:policy
document:reference:policy
document:visibility:policy
document:content:read:policy
document:summary:prepare:policy
document:link:policy
document:relationship:visibility:policy
cross-organization:document
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact raw content, previews, checksums, linked targets, summaries or total_count.
- Policy may downgrade response to metadata-only or preview-only.
- Policy may require human review before professional or external use.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may summarize or extract document meaning only within Permission and Policy limits.
- AI must not decide legal sufficiency, evidence sufficiency, filing readiness or official document validity.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Document API output is used for filing, professional decision, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/documents requires idempotency_key.
PATCH /v1/documents/{document_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link endpoints may require idempotency_key for Add/Remove/Replace operations.
Summary preparation does not normally require idempotency unless result is persisted.
```

Events:

```text
DocumentCreated may be emitted by Document Service after successful creation.
Document update/link/content events may be reserved for later if event specs exist.
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
DocumentReferenceInvalid
LinkedTargetInvalid
ContentAccessDenied
ContentAccessRestricted
ContentUnavailable
SummaryUnavailable
RelationshipTypeInvalid
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
- Errors must not expose database IDs, storage internals, restricted document content, policy internals or permission internals.
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
cite Document API Spec
cite Document Service Spec
cite this Document API Contract
use Reference Contract for document_reference_id and linked target references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted summaries
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Document Service
invoke related owning services for target reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing metadata, content, previews, summaries or links
return safe errors only
write tests for create/read/update/search/validate-reference/content-access/link-targets/prepare-summary
write tests for linked target validation
write tests for content access policy restriction
write tests for AI summary source disclosure
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
create Document directly in API layer
query database or storage directly from API contract implementation
use generic id where document_reference_id is required
expose database IDs or storage internals
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate linked target lifecycle through Document link endpoints
treat document summary as legal conclusion or evidence sufficiency
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Document API Contract is accepted only if:

```text
[ ] It defines Document API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Document API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines content access contract.
[ ] It defines link targets contract.
[ ] It defines prepare summary contract.
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
| 0.1.0 | Draft | Initial Document API Contract. Defines governed create, read, update, search, validate-reference, content-access, target-link and summary-preparation payloads, linked target references, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
