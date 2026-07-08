# API Contract — Knowledge API

**Spec ID:** B02-CONTRACT-API-KNOWLEDGE  
**Spec Type:** API Contract Specification  
**Contract Name:** Knowledge API Contract  
**Contract File:** core-specs/contracts/api/knowledge-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/knowledge-api.md  
**Related Domain:** Knowledge  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/agent-service.md  
**Related API Specs:** core-specs/api/knowledge-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/agent-api.md  
**Related Event Specs:** core-specs/events/knowledge-record-created.md; core-specs/events/knowledge-record-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Knowledge API Contract defines the implementation-facing request and response contract for Knowledge API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and retrieve Knowledge records through governed API boundaries without bypassing Knowledge Service, Permission Service, Policy Service, Agent governance or Event Service.

This contract governs:

```text
Knowledge API versioning
Knowledge record create request
Knowledge record update request
Knowledge record read response
Knowledge record search/list response
Knowledge source/reference validation
Knowledge retrieval request
source-grounded result shape
AI-safe retrieval context
Permission and Policy context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Knowledge API Contract does not define professional truth by itself, create legal authority, replace Knowledge Service, replace Knowledge Agent, evaluate Permission/Policy, or authorize AI output as final professional advice.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Knowledge Service through governed API boundaries.
```

This contract does not mean:

```text
professional conclusion
legal opinion
source authority by itself
AI answer contract
document storage contract
evidence sufficiency contract
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Knowledge API receives governed knowledge requests.
Knowledge Service owns Knowledge behavior.
Permission and Policy govern access.
AI retrieval is source-grounded assistance, not professional truth.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Knowledge reference fields
Knowledge source fields
retrieval result shape
source citation/reference shape
pagination shape for list/search
permission/policy context requirements
AI context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
Knowledge lifecycle ownership outside Knowledge Service
professional truth approval
legal interpretation finality
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
core-specs/api/knowledge-api.md
```

Owning service spec:

```text
core-specs/services/knowledge-service.md
```

Owning agent spec:

```text
core-specs/agents/knowledge-agent.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Knowledge API, Knowledge Service or Knowledge Agent responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Knowledge
```

Related objects:

```text
Document
Evidence
Permission
Policy
Event
Agent
```

Reference rules:

```text
- knowledge_record_reference_id identifies Knowledge.
- source_reference_ids identify source records, documents, evidence or approved knowledge sources.
- document_reference_id and evidence_reference_id must be validated by their owning services.
- agent_reference_id identifies Knowledge Agent context where AI-assisted retrieval is used.
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

Knowledge target context:

```yaml
target:
  knowledge_record_reference_id: string | null
  target_object_type: Knowledge
  target_object_reference_id: string | null
```

Rules:

```text
- knowledge_record_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- agent_reference_id and agent_registry_key are required for AI-assisted retrieval.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/knowledge/records
GET    /v1/knowledge/records/{knowledge_record_reference_id}
PATCH  /v1/knowledge/records/{knowledge_record_reference_id}
GET    /v1/knowledge/records
POST   /v1/knowledge/records/validate-reference
POST   /v1/knowledge/retrieve
```

Endpoint ownership:

```text
API layer validates request contract.
Knowledge Service executes behavior.
Document Service validates document references where needed.
Evidence Service validates evidence references where needed.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs agent identity where AI-assisted retrieval is used.
Event Service records events emitted by owning services.
```

---

# 8. Create Knowledge Record Request Contract

Endpoint:

```text
POST /v1/knowledge/records
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
    - knowledge:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - knowledge:create:policy
  policy_decision_reference_id: string | null

payload:
  knowledge_record_type: string
  knowledge_record_status: string | null
  title_safe: string
  summary_safe: string | null
  content_safe: string | null
  source_references:
    - source_type: string
      source_reference_id: string
      source_label_safe: string | null
  jurisdiction_reference_id: string | null
  domain_tags:
    - string
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- knowledge_record_type and title_safe are required.
- source_references must be validated where they reference Core objects.
- content_safe must not contain restricted data unless policy allows it.
- Knowledge Service assigns knowledge_record_reference_id.
```

---

# 9. Create Knowledge Record Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  knowledge_record_reference_id: string
  knowledge_record_type: string
  knowledge_record_status: string
  title_safe: string
  summary_safe: string | null
  source_references_visible: list[object]
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
- KnowledgeRecordCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate KnowledgeRecordCreated event.
```

---

# 10. Read Knowledge Record Contract

Endpoint:

```text
GET /v1/knowledge/records/{knowledge_record_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  knowledge_record_reference_id: string
  knowledge_record_type: string
  knowledge_record_status: string
  title_safe: string
  summary_safe: string | null
  content_visible: string | null
  source_references_visible:
    - source_type: string
      source_reference_id: string
      source_label_safe: string | null
  jurisdiction_reference_id: string | null
  domain_tags:
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
- Read must evaluate knowledge:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted content must be omitted by default.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Knowledge Record Contract

Endpoint:

```text
PATCH /v1/knowledge/records/{knowledge_record_reference_id}
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
  knowledge_record_status: string | null
  title_safe: string | null
  summary_safe: string | null
  content_safe_patch: string | null
  source_references_patch:
    - source_type: string
      source_reference_id: string
      operation: Add | Remove | Replace
  domain_tags_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - knowledge:update
policy_context:
  required_policy_scopes:
    - knowledge:update:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  knowledge_record_reference_id: string
  knowledge_record_status: string
  title_safe: string
  summary_safe: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Knowledge Service.
- Knowledge status transitions must follow Knowledge Service rules.
- Source reference changes must be validated.
- Restricted content must not be patched through content_safe_patch unless policy allows it.
- KnowledgeRecordUpdated event reference may be returned where policy allows it.
```

---

# 12. Search/List Knowledge Records Contract

Endpoint:

```text
GET /v1/knowledge/records
```

Query parameters:

```yaml
knowledge_record_type: string | null
knowledge_record_status: string | null
jurisdiction_reference_id: string | null
domain_tag: string | null
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
    - knowledge_record_reference_id: string
      knowledge_record_type: string
      knowledge_record_status: string
      title_safe: string
      summary_safe: string | null
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
- Search must not reveal restricted Knowledge existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Knowledge Reference Contract

Endpoint:

```text
POST /v1/knowledge/records/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  knowledge_record_reference_id: string
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
  knowledge_record_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Knowledge.
- Validation status must follow Reference Contract.
- Policy may hide safe_label.
```

---

# 14. Retrieve Knowledge Contract

Endpoint:

```text
POST /v1/knowledge/retrieve
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
    - knowledge:retrieve
policy_context:
  required_policy_scopes:
    - knowledge:retrieve:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: KnowledgeAgent | null
payload:
  retrieval_query_safe: string
  retrieval_scope:
    knowledge_record_types:
      - string
    jurisdiction_reference_ids:
      - string
    domain_tags:
      - string
  max_results: integer | null
  require_source_references: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  retrieval_status: string
  items:
    - knowledge_record_reference_id: string
      title_safe: string
      summary_safe: string | null
      source_references_visible:
        - source_type: string
          source_reference_id: string
          source_label_safe: string | null
      relevance_reason_safe: string | null
      restricted_fields_omitted: boolean
  ai_context:
    ai_assisted: boolean
    agent_reference_id: string | null
    agent_registry_key: string | null
    source_scope_disclosed: boolean
    policy_omissions_disclosed: boolean
  human_review:
    human_review_required: boolean | null
```

Rules:

```text
- Retrieval must be source-grounded.
- Knowledge retrieval result is assistance, not professional truth.
- Agent-assisted retrieval must follow Knowledge Agent governance.
- Policy may downgrade retrieval to safe summary only.
- Missing sources or restricted omissions must be disclosed safely.
```

---

# 15. Controlled Values

## 15.1 knowledge_record_type

```text
LegalRule
JurisdictionGuide
Procedure
Checklist
Template
CaseNote
PracticeNote
FAQ
GlossaryTerm
SourceIndex
Unknown
```

## 15.2 knowledge_record_status

```text
Draft
Active
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 15.3 source_type

```text
KnowledgeRecord
Document
Evidence
OfficialSource
InternalPracticeNote
ExternalReference
ManualInput
Unknown
```

## 15.4 retrieval_status

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

## 15.5 validation_status

```text
Valid
Invalid
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

## 15.6 sort.field

```text
created_at
updated_at
title_safe
knowledge_record_status
knowledge_record_type
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] knowledge_record_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] knowledge_record_type is controlled.
[ ] knowledge_record_status is controlled where provided.
[ ] source references are valid where provided.
[ ] retrieval_query_safe is present for retrieve.
[ ] retrieval results include source references where required.
[ ] AI Context is present for agent-assisted retrieval.
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
knowledge:create
knowledge:read
knowledge:search
knowledge:update
knowledge:validate
knowledge:retrieve
```

Rules:

```text
- Knowledge API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 18. Policy Rules

Required policy scopes may include:

```text
knowledge:create:policy
knowledge:read:policy
knowledge:search:policy
knowledge:update:policy
knowledge:reference:policy
knowledge:retrieve:policy
knowledge:visibility:policy
knowledge:source:visibility:policy
cross-organization:knowledge
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact content, sources, total_count, relevance reasons or retrieval scope.
- Policy may downgrade to metadata-only or safe-summary-only.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 19. AI and Human Review Rules

AI rules:

```text
- Knowledge Agent may retrieve and summarize only Knowledge that Permission and Policy allow.
- AI output must disclose source scope, missing context and policy omissions.
- AI output must not fabricate source references, legal authority or evidence sufficiency.
```

Human review:

```text
- Human review may be required where retrieval is used for professional decision, external communication, filing or customer-facing output.
- human_review_required must be explicit where policy requires review.
```

Rules:

```text
- Knowledge retrieval is assistance until accepted through governed human or service process.
- Agent must not create or mutate Knowledge records unless routed through Knowledge Service.
```

---

# 20. Idempotency and Event Rules

Idempotency:

```text
POST /v1/knowledge/records requires idempotency_key.
PATCH /v1/knowledge/records/{knowledge_record_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
POST /v1/knowledge/retrieve does not normally require idempotency unless retrieval result is persisted.
```

Events:

```text
KnowledgeRecordCreated may be emitted by Knowledge Service after successful creation.
KnowledgeRecordUpdated may be emitted by Knowledge Service after successful update.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
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
SourceReferenceInvalid
RetrievalScopeInvalid
KnowledgeRecordDeprecated
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
- Errors must not expose restricted Knowledge, source content, policy internals or permission internals.
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
cite Knowledge API Spec
cite Knowledge Service Spec
cite Knowledge Agent Spec where retrieval is AI-assisted
cite this Knowledge API Contract
use Reference Contract for knowledge_record_reference_id and source references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for agent-assisted retrieval
use Human Review Contract where policy requires review
use Idempotency Contract for create
use Versioning Contract for version validation
route all mutation through Knowledge Service
invoke Document/Evidence services for source validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields or retrieval results
return safe errors only
write tests for create/read/update/search/validate-reference/retrieve
write tests for source reference validation
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for AI retrieval source disclosure
write tests for human_review_required
write tests for VersionUnsupported
```

Codex must not:

```text
create Knowledge directly in API layer
query database directly from API contract implementation
use generic id where knowledge_record_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
fabricate source references
treat Knowledge retrieval as professional truth
allow AI context to exceed evaluated_data_access_scope
```

---

# 24. Acceptance Criteria

This Knowledge API Contract is accepted only if:

```text
[ ] It defines Knowledge API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Knowledge API, Service and Agent specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines retrieve contract.
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
| 0.1.0 | Draft | Initial Knowledge API Contract. Defines governed create, read, update, search, validate-reference and retrieval payloads, source references, AI context, Permission/Policy context, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
