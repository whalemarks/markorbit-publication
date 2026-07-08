# API Contract — Evidence API

**Spec ID:** B02-CONTRACT-API-EVIDENCE  
**Spec Type:** API Contract Specification  
**Contract Name:** Evidence API Contract  
**Contract File:** core-specs/contracts/api/evidence-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/evidence-api.md  
**Related Domain:** Evidence  
**Related Object Specs:** core-specs/objects/evidence.md; core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/jurisdiction.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/evidence-service.md; core-specs/services/document-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/evidence-api.md; core-specs/api/document-api.md; core-specs/api/trademark-api.md; core-specs/api/brand-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/jurisdiction-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/evidence-created.md; core-specs/events/document-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
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

Evidence API Contract defines the implementation-facing request and response contract for Evidence API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and prepare Evidence records through governed API boundaries without bypassing Evidence Service, Document Service, related owning services, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Evidence API versioning
Evidence create request
Evidence update request
Evidence read response
Evidence search/list response
Evidence reference validation
Evidence source document linkage
Evidence target linkage
Evidence use-context preparation
Evidence sufficiency assistance context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Evidence API Contract does not prove evidence sufficiency by itself, decide legal use, determine filing readiness, replace professional review, replace Evidence Service, evaluate Permission/Policy, or authorize AI output as final evidentiary conclusion.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Evidence Service through governed API boundaries.
```

This contract does not mean:

```text
legal evidence sufficiency
official acceptance of evidence
filing readiness approval
use proof conclusion
document authenticity proof
professional legal conclusion
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Evidence API receives governed evidence requests.
Evidence Service owns Evidence behavior.
Document and target domain references are validated by owning services.
Permission and Policy govern access.
Evidence sufficiency requires governed human/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Evidence reference fields
source document reference fields
target object reference fields
evidence use-context fields
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
Evidence lifecycle ownership outside Evidence Service
document binary storage
legal sufficiency conclusion
official filing acceptance
professional judgment
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
core-specs/api/evidence-api.md
```

Owning service spec:

```text
core-specs/services/evidence-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Evidence API and Evidence Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Evidence
```

Related objects:

```text
Document
Trademark
Brand
Customer
Matter
Jurisdiction
Permission
Policy
Event
Agent
```

Reference rules:

```text
- evidence_reference_id identifies Evidence.
- document_reference_ids identify evidence source documents and must be validated by Document Service.
- target_object_type and target_object_reference_id identify the Evidence target and must be validated by owning services.
- jurisdiction_reference_id must be validated by Jurisdiction Service where provided.
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

Evidence target context:

```yaml
target:
  evidence_reference_id: string | null
  target_object_type: Evidence
  target_object_reference_id: string | null
```

Rules:

```text
- evidence_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- source document references and target object references must be validated where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/evidence
GET    /v1/evidence/{evidence_reference_id}
PATCH  /v1/evidence/{evidence_reference_id}
GET    /v1/evidence
POST   /v1/evidence/validate-reference
POST   /v1/evidence/{evidence_reference_id}/link-documents
POST   /v1/evidence/{evidence_reference_id}/link-targets
POST   /v1/evidence/{evidence_reference_id}/prepare-use-summary
POST   /v1/evidence/evaluate-sufficiency-preview
```

Endpoint ownership:

```text
API layer validates request contract.
Evidence Service executes behavior.
Document Service validates source document references.
Target owning services validate target references.
Jurisdiction Service validates jurisdiction references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preview where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Evidence Request Contract

Endpoint:

```text
POST /v1/evidence
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
    - evidence:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - evidence:create:policy
  policy_decision_reference_id: string | null

payload:
  evidence_type: string
  evidence_status: string | null
  evidence_title_safe: string
  evidence_summary_safe: string | null
  source_document_reference_ids:
    - string
  target_links:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  jurisdiction_reference_id: string | null
  evidence_date: date | null
  evidence_period_start: date | null
  evidence_period_end: date | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- evidence_type and evidence_title_safe are required.
- source_document_reference_ids must be validated by Document Service where provided.
- target_links must be validated by owning services where provided.
- jurisdiction_reference_id must be validated where provided.
- Evidence Service assigns evidence_reference_id.
```

---

# 9. Create Evidence Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  evidence_reference_id: string
  evidence_type: string
  evidence_status: string
  evidence_title_safe: string
  evidence_summary_safe: string | null
  source_document_reference_ids_visible:
    - string
  target_links_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  jurisdiction_reference_id: string | null
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
- EvidenceCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate EvidenceCreated event.
```

---

# 10. Read Evidence Contract

Endpoint:

```text
GET /v1/evidence/{evidence_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  evidence_reference_id: string
  evidence_type: string
  evidence_status: string
  evidence_title_safe: string
  evidence_summary_safe: string | null
  source_document_reference_ids_visible:
    - string
  target_links_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  jurisdiction_reference_id: string | null
  evidence_date: date | null
  evidence_period_start: date | null
  evidence_period_end: date | null
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
- Read must evaluate evidence:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted document links, target links and metadata must be omitted where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Evidence Contract

Endpoint:

```text
PATCH /v1/evidence/{evidence_reference_id}
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
  evidence_status: string | null
  evidence_title_safe: string | null
  evidence_summary_safe: string | null
  evidence_date: date | null
  evidence_period_start: date | null
  evidence_period_end: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - evidence:update
policy_context:
  required_policy_scopes:
    - evidence:update:policy
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
  evidence_reference_id: string
  evidence_status: string
  evidence_title_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Evidence Service.
- Evidence status transitions must follow Evidence Service rules.
- Restricted metadata must not be patched unless policy allows it.
- Human review may be required for finalization or filing-use transitions.
```

---

# 12. Search/List Evidence Contract

Endpoint:

```text
GET /v1/evidence
```

Query parameters:

```yaml
evidence_type: string | null
evidence_status: string | null
target_object_type: string | null
target_object_reference_id: string | null
jurisdiction_reference_id: string | null
source_document_reference_id: string | null
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
    - evidence_reference_id: string
      evidence_type: string
      evidence_status: string
      evidence_title_safe: string
      evidence_summary_safe: string | null
      jurisdiction_reference_id: string | null
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
- Search must not reveal restricted Evidence existence.
- safe_query must not be treated as unrestricted search over raw document content.
```

---

# 13. Validate Evidence Reference Contract

Endpoint:

```text
POST /v1/evidence/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  evidence_reference_id: string
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
  evidence_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  evidence_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Evidence.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or evidence type.
```

---

# 14. Link Document and Target Contracts

Endpoints:

```text
POST /v1/evidence/{evidence_reference_id}/link-documents
POST /v1/evidence/{evidence_reference_id}/link-targets
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  references:
    - reference_type: string
      reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - evidence:link
policy_context:
  required_policy_scopes:
    - evidence:link:policy
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
  evidence_reference_id: string
  linked_reference_type: string
  linked_references_visible:
    - reference_type: string
      reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Evidence Service.
- Linked document and target references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate Document or target object lifecycle directly.
```

---

# 15. Prepare Use Summary Contract

Endpoint:

```text
POST /v1/evidence/{evidence_reference_id}/prepare-use-summary
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
    - evidence:summary:prepare
policy_context:
  required_policy_scopes:
    - evidence:summary:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  summary_purpose: string
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
  summary_status: string
  evidence_use_summary_safe: string | null
  source_document_reference_ids_visible:
    - string
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
- Use summary is assistance, not evidence sufficiency conclusion.
- AI-assisted summary must follow AI governance.
- Policy may downgrade to metadata-only or safe-summary-only.
- Human review may be required before filing or external use.
```

---

# 16. Sufficiency Preview Contract

Endpoint:

```text
POST /v1/evidence/evaluate-sufficiency-preview
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
    - evidence:sufficiency:preview
policy_context:
  required_policy_scopes:
    - evidence:sufficiency:preview:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  evidence_reference_ids:
    - string
  intended_use: string
  jurisdiction_reference_id: string | null
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
  preview_status: string
  sufficiency_preview_safe: string | null
  evidence_gaps_safe:
    - string
  source_reference_ids_visible:
    - string
  restricted_fields_omitted: boolean
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
human_review:
  human_review_required: boolean
```

Rules:

```text
- Sufficiency preview is not final evidence sufficiency.
- Preview must disclose that professional review is required where applicable.
- AI must not certify sufficiency.
- Policy may restrict evidence references, gaps or summary.
```

---

# 17. Controlled Values

## 17.1 evidence_type

```text
UseEvidence
OwnershipEvidence
PriorityEvidence
Specimen
SalesEvidence
AdvertisingEvidence
WebsiteEvidence
MarketplaceEvidence
CertificateEvidence
CorrespondenceEvidence
OfficialRecordEvidence
Other
Unknown
```

## 17.2 evidence_status

```text
Draft
Collected
UnderReview
AcceptedForInternalUse
Rejected
Submitted
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 relationship_type

```text
PrimaryEvidenceSource
SupportingEvidenceSource
UseProof
OwnershipProof
PriorityProof
SpecimenSource
OfficialRecord
CustomerProvided
AgentProvided
InternalReference
Unknown
```

## 17.4 reference_type

```text
Document
Trademark
Brand
Customer
Matter
Jurisdiction
Unknown
```

## 17.5 summary_status

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

## 17.6 preview_status

```text
Completed
Partial
InsufficientContext
NoResult
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.7 validation_status

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

## 17.8 sort.field

```text
created_at
updated_at
evidence_title_safe
evidence_status
evidence_type
evidence_date
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] evidence_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] evidence_type is controlled.
[ ] evidence_status is controlled where provided.
[ ] source_document_reference_ids are validated where provided.
[ ] target references are validated where provided.
[ ] jurisdiction_reference_id is validated where provided.
[ ] relationship_type is controlled.
[ ] link_operation is controlled.
[ ] AI Context is present for AI-assisted summary or preview.
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
evidence:create
evidence:read
evidence:search
evidence:update
evidence:validate
evidence:link
evidence:summary:prepare
evidence:sufficiency:preview
```

Rules:

```text
- Evidence API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
evidence:create:policy
evidence:read:policy
evidence:search:policy
evidence:update:policy
evidence:reference:policy
evidence:visibility:policy
evidence:link:policy
evidence:summary:prepare:policy
evidence:sufficiency:preview:policy
evidence:relationship:visibility:policy
cross-organization:evidence
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact source documents, target links, gaps, previews, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before professional or external use.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may summarize Evidence and prepare sufficiency preview only within Permission and Policy limits.
- AI must not certify evidence sufficiency, authenticity, legal use or filing readiness.
- AI output must disclose source scope, missing context, gaps and policy omissions where applicable.
```

Human review:

```text
- Human review is required where Evidence output is used for filing, professional decision, official submission, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/evidence requires idempotency_key.
PATCH /v1/evidence/{evidence_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link endpoints may require idempotency_key for Add/Remove/Replace operations.
Summary and sufficiency preview endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
EvidenceCreated may be emitted by Evidence Service after successful creation.
Evidence update/link events may be reserved for later if event specs exist.
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
EvidenceReferenceInvalid
DocumentReferenceInvalid
TargetReferenceInvalid
JurisdictionReferenceInvalid
RelationshipTypeInvalid
ContentAccessRestricted
SummaryUnavailable
SufficiencyPreviewUnavailable
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
- Errors must not expose database IDs, restricted evidence data, restricted document content, policy internals or permission internals.
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
cite Evidence API Spec
cite Evidence Service Spec
cite this Evidence API Contract
use Reference Contract for evidence_reference_id, document references and target references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted summaries and sufficiency previews
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Evidence Service
invoke Document Service for source document validation
invoke related target services for target reference validation where applicable
invoke Jurisdiction Service where jurisdiction context is provided
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields, source documents, target links, previews or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/link-documents/link-targets/prepare-use-summary/evaluate-sufficiency-preview
write tests for document and target reference validation
write tests for sufficiency preview disclaimer and human_review_required
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Evidence directly in API layer
query database directly from API contract implementation
use generic id where evidence_reference_id is required
expose database IDs or restricted document content
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Document or target object lifecycle through Evidence link endpoints
treat sufficiency preview as professional conclusion
treat AI output as evidence certification
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Evidence API Contract is accepted only if:

```text
[ ] It defines Evidence API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Evidence API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link document and target contracts.
[ ] It defines prepare use summary contract.
[ ] It defines sufficiency preview contract.
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
| 0.1.0 | Draft | Initial Evidence API Contract. Defines governed create, read, update, search, validate-reference, document/target linking, use-summary and sufficiency-preview payloads, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
