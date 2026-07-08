# API Contract — Jurisdiction API

**Spec ID:** B02-CONTRACT-API-JURISDICTION  
**Spec Type:** API Contract Specification  
**Contract Name:** Jurisdiction API Contract  
**Contract File:** core-specs/contracts/api/jurisdiction-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/jurisdiction-api.md  
**Related Domain:** Jurisdiction  
**Related Object Specs:** core-specs/objects/jurisdiction.md; core-specs/objects/trademark.md; core-specs/objects/classification.md; core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/jurisdiction-service.md; core-specs/services/trademark-service.md; core-specs/services/classification-service.md; core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/jurisdiction-api.md; core-specs/api/trademark-api.md; core-specs/api/classification-api.md; core-specs/api/knowledge-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/jurisdiction-linked.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
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

Jurisdiction API Contract defines the implementation-facing request and response contract for Jurisdiction API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate and reference Jurisdiction records and jurisdictional rule context through governed API boundaries without bypassing Jurisdiction Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Jurisdiction API versioning
Jurisdiction create request
Jurisdiction update request
Jurisdiction read response
Jurisdiction search/list response
Jurisdiction reference validation
Jurisdiction rule context retrieval
Trademark and Classification relationship references
Knowledge and Document linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Jurisdiction API Contract does not define legal advice, official law, filing eligibility finality, country coverage strategy, professional judgment or AI-generated jurisdiction recommendations as final truth.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Jurisdiction Service through governed API boundaries.
```

This contract does not mean:

```text
legal advice
official government source
country filing recommendation by itself
filing eligibility finality
classification rule finality
fee rule finality
trademark lifecycle action
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Jurisdiction API receives governed jurisdiction requests.
Jurisdiction Service owns Jurisdiction behavior.
Knowledge, Classification, Trademark and Document references are validated by owning services.
Permission and Policy govern access.
Professional truth requires governed source and human/service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Jurisdiction reference fields
Jurisdiction rule context fields
Trademark/Classification/Knowledge/Document reference fields
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
Jurisdiction lifecycle ownership outside Jurisdiction Service
legal interpretation finality
official government source verification by itself
filing strategy approval
fee calculation finality
classification professional approval
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
core-specs/api/jurisdiction-api.md
```

Owning service spec:

```text
core-specs/services/jurisdiction-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Jurisdiction API and Jurisdiction Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Jurisdiction
```

Related objects:

```text
Trademark
Classification
Knowledge
Document
Permission
Policy
Event
Agent
```

Reference rules:

```text
- jurisdiction_reference_id identifies Jurisdiction.
- country_code or region_code may be external identifiers but must not replace jurisdiction_reference_id.
- trademark_reference_id may be used as target context but does not transfer Trademark ownership.
- classification_reference_ids must be validated by Classification Service.
- knowledge_record_reference_ids and document_reference_ids must be validated by owning services.
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

Jurisdiction target context:

```yaml
target:
  jurisdiction_reference_id: string | null
  target_object_type: Jurisdiction
  target_object_reference_id: string | null
```

Rules:

```text
- jurisdiction_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- country_code/region_code must be normalized by Jurisdiction Service where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/jurisdictions
GET    /v1/jurisdictions/{jurisdiction_reference_id}
PATCH  /v1/jurisdictions/{jurisdiction_reference_id}
GET    /v1/jurisdictions
POST   /v1/jurisdictions/validate-reference
POST   /v1/jurisdictions/rule-context
POST   /v1/jurisdictions/{jurisdiction_reference_id}/link-knowledge
POST   /v1/jurisdictions/{jurisdiction_reference_id}/link-documents
```

Endpoint ownership:

```text
API layer validates request contract.
Jurisdiction Service executes behavior.
Knowledge Service validates knowledge references.
Document Service validates document references.
Classification Service validates classification context where needed.
Trademark Service validates trademark context where needed.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
```

---

# 8. Create Jurisdiction Request Contract

Endpoint:

```text
POST /v1/jurisdictions
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
    - jurisdiction:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - jurisdiction:create:policy
  policy_decision_reference_id: string | null

payload:
  jurisdiction_type: string
  jurisdiction_status: string | null
  jurisdiction_name_safe: string
  country_code: string | null
  region_code: string | null
  parent_jurisdiction_reference_id: string | null
  official_source_urls_safe:
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
- jurisdiction_type and jurisdiction_name_safe are required.
- country_code/region_code must be normalized where provided.
- parent_jurisdiction_reference_id must be validated by Jurisdiction Service where provided.
- knowledge/document references must be validated by owning services where provided.
- Jurisdiction Service assigns jurisdiction_reference_id.
```

---

# 9. Create Jurisdiction Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  jurisdiction_reference_id: string
  jurisdiction_type: string
  jurisdiction_status: string
  jurisdiction_name_safe: string
  country_code: string | null
  region_code: string | null
  parent_jurisdiction_reference_id: string | null
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
- Jurisdiction creation event may be returned only if event spec exists and service emits it.
- Replayed idempotent response must not duplicate events.
```

---

# 10. Read Jurisdiction Contract

Endpoint:

```text
GET /v1/jurisdictions/{jurisdiction_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  jurisdiction_reference_id: string
  jurisdiction_type: string
  jurisdiction_status: string
  jurisdiction_name_safe: string
  country_code: string | null
  region_code: string | null
  parent_jurisdiction_reference_id: string | null
  official_source_urls_visible:
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
- Read must evaluate jurisdiction:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Restricted source links and linked references must be omitted by default where policy requires.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Jurisdiction Contract

Endpoint:

```text
PATCH /v1/jurisdictions/{jurisdiction_reference_id}
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
  jurisdiction_status: string | null
  jurisdiction_name_safe: string | null
  parent_jurisdiction_reference_id: string | null
  official_source_urls_safe_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - jurisdiction:update
policy_context:
  required_policy_scopes:
    - jurisdiction:update:policy
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
  jurisdiction_reference_id: string
  jurisdiction_status: string
  jurisdiction_name_safe: string
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Jurisdiction Service.
- Status transitions must follow Jurisdiction Service rules.
- Parent jurisdiction changes must be validated and must not create cycles.
- Human review may be required where jurisdiction metadata affects professional rules.
```

---

# 12. Search/List Jurisdiction Contract

Endpoint:

```text
GET /v1/jurisdictions
```

Query parameters:

```yaml
jurisdiction_type: string | null
jurisdiction_status: string | null
country_code: string | null
region_code: string | null
parent_jurisdiction_reference_id: string | null
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
    - jurisdiction_reference_id: string
      jurisdiction_type: string
      jurisdiction_status: string
      jurisdiction_name_safe: string
      country_code: string | null
      region_code: string | null
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
- Search must not reveal restricted Jurisdiction existence.
- safe_query must not be treated as unrestricted search.
```

---

# 13. Validate Jurisdiction Reference Contract

Endpoint:

```text
POST /v1/jurisdictions/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  jurisdiction_reference_id: string
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
  jurisdiction_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  country_code: string | null
  region_code: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Jurisdiction.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or source context.
```

---

# 14. Rule Context Retrieval Contract

Endpoint:

```text
POST /v1/jurisdictions/rule-context
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
    - jurisdiction:rule-context:read
policy_context:
  required_policy_scopes:
    - jurisdiction:rule-context:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  jurisdiction_reference_id: string
  intended_use: string
  target_context:
    trademark_reference_id: string | null
    classification_reference_ids:
      - string
  requested_rule_groups:
    - string
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  jurisdiction_reference_id: string
  rule_context_status: string
  rule_groups:
    - rule_group: string
      summary_safe: string | null
      source_reference_ids_visible:
        - string
      restricted_fields_omitted: boolean
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Rule context retrieval is source-grounded assistance, not legal advice by itself.
- requested_rule_groups must be controlled.
- Trademark and Classification references must be validated where provided.
- AI-assisted rule context must follow Knowledge Agent governance.
- Human review may be required before downstream professional use.
```

---

# 15. Link Knowledge and Document Contracts

Endpoints:

```text
POST /v1/jurisdictions/{jurisdiction_reference_id}/link-knowledge
POST /v1/jurisdictions/{jurisdiction_reference_id}/link-documents
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
    - jurisdiction:link
policy_context:
  required_policy_scopes:
    - jurisdiction:link:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  jurisdiction_reference_id: string
  linked_reference_type: string
  linked_reference_ids_visible:
    - string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operations must route through Jurisdiction Service.
- Linked references must be validated by owning services.
- Link operation does not transfer ownership of linked records.
- Link operation must not mutate Knowledge or Document lifecycle directly.
```

---

# 16. Controlled Values

## 16.1 jurisdiction_type

```text
Country
Region
IntergovernmentalOffice
TreatySystem
CustomsTerritory
AdministrativeRegion
Unknown
```

## 16.2 jurisdiction_status

```text
Draft
Active
Suspended
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 16.3 rule_group

```text
FilingRequirement
ClassificationRule
GoodsServicesRule
OfficialFeeRule
ExaminationRule
OppositionRule
RenewalRule
UseRequirement
PowerOfAttorneyRule
DocumentRequirement
EvidenceRule
DeadlineRule
MadridRule
LocalAgentRule
Unknown
```

## 16.4 rule_context_status

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

## 16.5 validation_status

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

## 16.6 linked_reference_type

```text
Knowledge
Document
Unknown
```

## 16.7 sort.field

```text
created_at
updated_at
jurisdiction_name_safe
jurisdiction_status
jurisdiction_type
country_code
region_code
```

---

# 17. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] jurisdiction_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] jurisdiction_type is controlled.
[ ] jurisdiction_status is controlled where provided.
[ ] country_code and region_code are normalized where provided.
[ ] parent_jurisdiction_reference_id is validated where provided.
[ ] requested_rule_groups are controlled.
[ ] knowledge_record_reference_ids are validated where provided.
[ ] document_reference_ids are validated where provided.
[ ] trademark/classification context references are validated where provided.
[ ] link_operation is controlled.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] AI Context is present for agent-assisted rule-context retrieval.
[ ] Human Review Context is present where policy requires review.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 18. Permission Rules

Required permission keys:

```text
jurisdiction:create
jurisdiction:read
jurisdiction:search
jurisdiction:update
jurisdiction:validate
jurisdiction:link
jurisdiction:rule-context:read
```

Rules:

```text
- Jurisdiction API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 19. Policy Rules

Required policy scopes may include:

```text
jurisdiction:create:policy
jurisdiction:read:policy
jurisdiction:search:policy
jurisdiction:update:policy
jurisdiction:reference:policy
jurisdiction:visibility:policy
jurisdiction:link:policy
jurisdiction:rule-context:policy
jurisdiction:source:visibility:policy
cross-organization:jurisdiction
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact source URLs, linked references, rule groups, total_count or professional context.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review for downstream professional use.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 20. AI and Human Review Rules

AI rules:

```text
- AI may summarize Jurisdiction and rule context only within Permission and Policy limits.
- AI must not decide filing eligibility, legal interpretation, official fee finality or jurisdiction strategy by itself.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Jurisdiction API output is used for filing strategy, professional decision, external communication or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 21. Idempotency and Event Rules

Idempotency:

```text
POST /v1/jurisdictions requires idempotency_key.
PATCH /v1/jurisdictions/{jurisdiction_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link endpoints may require idempotency_key for Add/Remove/Replace operations.
Rule-context retrieval does not normally require idempotency unless result is persisted.
```

Events:

```text
JurisdictionLinked may be emitted where a jurisdiction is linked to downstream context and event spec applies.
Jurisdiction creation/update events may be reserved for later if event specs exist.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 22. Error Rules

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
ParentJurisdictionInvalid
JurisdictionCycleRejected
KnowledgeReferenceInvalid
DocumentReferenceInvalid
TrademarkReferenceInvalid
ClassificationReferenceInvalid
RuleGroupInvalid
RuleContextUnavailable
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
- Errors must not expose database IDs, restricted jurisdiction data, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 23. Versioning Rules

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

# 24. Codex Implementation Notes

Codex must:

```text
cite Jurisdiction API Spec
cite Jurisdiction Service Spec
cite this Jurisdiction API Contract
use Reference Contract for jurisdiction_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted rule-context retrieval
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Jurisdiction Service
invoke Knowledge/Document services for reference validation where applicable
invoke Trademark/Classification services for rule-context target validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing fields, sources or rule context
return safe errors only
write tests for create/read/update/search/validate-reference/rule-context/link relationships
write tests for parent jurisdiction validation
write tests for jurisdiction cycle rejection
write tests for rule_group validation
write tests for source/reference visibility restriction
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
create Jurisdiction directly in API layer
query database directly from API contract implementation
use generic id where jurisdiction_reference_id is required
expose database IDs
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Knowledge/Document lifecycle through Jurisdiction link endpoints
treat country_code as Core jurisdiction_reference_id
treat Jurisdiction rule context as legal advice or professional truth
allow AI context to exceed evaluated_data_access_scope
```

---

# 25. Acceptance Criteria

This Jurisdiction API Contract is accepted only if:

```text
[ ] It defines Jurisdiction API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Jurisdiction API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines rule context retrieval contract.
[ ] It defines link knowledge/document contracts.
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

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Jurisdiction API Contract. Defines governed create, read, update, search, validate-reference, rule-context retrieval and relationship-link payloads, Knowledge/Document/Trademark/Classification references, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
