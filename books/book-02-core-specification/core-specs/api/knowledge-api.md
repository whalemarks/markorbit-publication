# API Specification — Knowledge API

**Spec ID:** B02-API-KNOWLEDGE  
**Spec Type:** API Specification  
**API Name:** Knowledge API  
**API File:** core-specs/api/knowledge-api.md  
**Related Domain:** core-specs/domains/knowledge.md  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/knowledge-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/knowledge-record-created.md; core-specs/events/knowledge-record-updated.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/knowledge-api-contract.md; core-specs/contracts/events/knowledge-record-created-payload.md; core-specs/contracts/events/knowledge-record-updated-payload.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Knowledge API exposes governed Knowledge Record operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate and reference Knowledge Records without treating Knowledge as Policy, Permission, legal conclusion, official source truth, professional advice, AI memory, workflow decision or product content management.

Knowledge API exists to support:

```text
governed knowledge record creation
professional reference material lookup
AI-authorized knowledge retrieval
source and version trace
policy-controlled knowledge visibility
knowledge record validation
event trace access
safe knowledge summary for products and integrations
```

Knowledge API does not make AI output true, replace professional review, override official sources or grant permission to use restricted knowledge.

---

# 2. API Meaning

Knowledge API means:

```text
a governed interface for operating Knowledge Records through Knowledge Service.
```

Knowledge API does not mean:

```text
Policy API
Permission API
AI memory API
legal opinion API
official registry API
document storage API
evidence API
workflow approval API
content marketing CMS
```

Knowledge supports professional and AI-assisted work.

It is not professional truth automatically.

---

# 3. API Boundary

Knowledge API is responsible for:

```text
Knowledge Record create request intake
Knowledge Record read/search/list access
Knowledge Record update request intake
Knowledge reference validation
source/version metadata exposure
safe Knowledge response shaping
Permission/Policy enforcement for Knowledge operations
Knowledge-related Event reference exposure where allowed
AI Agent access boundary for Knowledge operations
controlled API errors
```

Knowledge API is not responsible for:

```text
official government registry truth
professional legal conclusion
document/evidence lifecycle
policy ownership
permission ownership
workflow execution
AI reasoning truth
source crawling implementation
content publishing decisions
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/knowledge.md
```

Domain rule:

```text
Knowledge provides governed reference material.
Knowledge does not replace professional judgment, official source verification, Permission or Policy.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/knowledge.md
core-specs/objects/policy.md
core-specs/objects/permission.md
core-specs/objects/event.md
```

Object rules:

```text
- Knowledge API returns knowledge_record_reference_id.
- Knowledge API must expose source and version metadata where allowed.
- Knowledge API must not expose restricted Knowledge content by default.
- Knowledge API must not treat Knowledge as Evidence or Document.
- Knowledge API must not treat AI-generated knowledge drafts as verified Knowledge automatically.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/knowledge-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Knowledge API must invoke Knowledge Service for Knowledge behavior.
- Knowledge API must invoke Permission Service where operation requires authorization.
- Knowledge API must invoke Policy Service where contextual constraints apply.
- Knowledge API must not emit Knowledge events directly; Knowledge Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/knowledge-record-created.md
core-specs/events/knowledge-record-updated.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createKnowledgeRecord may result in KnowledgeRecordCreated.
- updateKnowledgeRecord may result in KnowledgeRecordUpdated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate KnowledgeRecordCreated or KnowledgeRecordUpdated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Knowledge Record

**Operation Category:** Create  
**Method:** POST  
**Path:** `/knowledge-records`  
**Owning Service Operation:** `createKnowledgeRecord`  
**Permission Required:** `knowledge:create`  
**Policy Required:** `KnowledgeCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-generated  
**Event Behavior:** Service Must Emit KnowledgeRecordCreated

Meaning:

```text
Create a governed Knowledge Record reference.
```

Non-meaning:

```text
does not prove official truth
does not create Evidence
does not create Document
does not approve legal advice
does not grant Permission
does not bypass Policy
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Knowledge Service createKnowledgeRecord
  ↓
Event Service record KnowledgeRecordCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Knowledge Record

**Operation Category:** Read  
**Method:** GET  
**Path:** `/knowledge-records/{knowledge_record_reference_id}`  
**Owning Service Operation:** `getKnowledgeRecord`  
**Permission Required:** `knowledge:read`  
**Policy Required:** `KnowledgeVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Knowledge Record view.
```

Non-meaning:

```text
does not expose restricted content automatically
does not guarantee current official truth
does not authorize use in every context
```

## 8.3 Operation: Search Knowledge Records

**Operation Category:** Search  
**Method:** GET  
**Path:** `/knowledge-records`  
**Owning Service Operation:** `searchKnowledgeRecords`  
**Permission Required:** `knowledge:search`  
**Policy Required:** `KnowledgeVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Knowledge Records using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted knowledge corpus access
does not expose restricted source material by default
```

## 8.4 Operation: Update Knowledge Record

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/knowledge-records/{knowledge_record_reference_id}`  
**Owning Service Operation:** `updateKnowledgeRecord`  
**Permission Required:** `knowledge:update`  
**Policy Required:** `KnowledgeUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service Must Emit KnowledgeRecordUpdated

Meaning:

```text
Update governed Knowledge Record metadata, status or safe content under Knowledge Service rules.
```

Non-meaning:

```text
does not rewrite source history
does not silently approve AI-generated content
does not create legal conclusion
does not alter Evidence or Document records
```

## 8.5 Operation: Validate Knowledge Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/knowledge-records/reference/validate`  
**Owning Service Operation:** `validateKnowledgeReference`  
**Permission Required:** `knowledge:validate`  
**Policy Required:** `KnowledgeReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Knowledge Record reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not verify official truth
does not authorize restricted use
does not approve professional conclusion
```

## 8.6 Operation: Retrieve Authorized Knowledge for AI

**Operation Category:** Action  
**Method:** POST  
**Path:** `/knowledge-records/authorized-retrieval`  
**Owning Service Operation:** `retrieveAuthorizedKnowledge`  
**Permission Required:** `knowledge:ai:retrieve`  
**Policy Required:** `AIAgentKnowledgeAccessPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit PolicyEvaluated

Meaning:

```text
Retrieve policy-filtered Knowledge Records for an AI Agent or AI-assisted operation.
```

Non-meaning:

```text
does not give AI unrestricted corpus access
does not make AI response professional truth
does not remove human review where required
```

## 8.7 Operation: List Knowledge Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/knowledge-records/{knowledge_record_reference_id}/events`  
**Owning Service Operation:** `listKnowledgeRecordEvents`  
**Permission Required:** `knowledge:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Knowledge-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Knowledge Record Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  knowledge_type: string
  knowledge_status: string | optional
  source_type: string
  source_reference: string | null
  jurisdiction_reference_id: string | null
  language_code: string | null
  title: string
  safe_summary: string | null
  content_reference_id: string | null
  request_context: object
  ai_context:
    ai_generated: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Knowledge Record Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  knowledge_record_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  knowledge_status: string | optional
  title: string | optional
  safe_summary: string | optional
  source_reference: string | optional
  content_reference_id: string | optional
  request_context: object
```

## 9.3 Validate Knowledge Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  knowledge_record_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Authorized AI Retrieval Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  agent_identity_reference_id: string
  agent_contract_reference_id: string
  retrieval_purpose: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
  filters:
    knowledge_type: list[string]
    jurisdiction_reference_ids: list[string]
    language_codes: list[string]
    max_results: integer
```

Request rules:

```text
- Requests must not include credentials, secrets or raw restricted source material by default.
- Requests must use controlled knowledge_type, knowledge_status and source_type values.
- AI-generated or AI-assisted creation/update must be explicitly marked.
- AI retrieval must include Agent Contract where required.
```

---

# 10. Response Contracts

## 10.1 Knowledge Record Response

```yaml
status: 200
body:
  knowledge_record_reference_id: string
  knowledge_type: string
  knowledge_status: string
  source_type: string
  source_reference: string | null
  jurisdiction_reference_id: string | null
  language_code: string | null
  safe_summary:
    title: string
    summary: string | null
    version: string | null
    last_reviewed_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Knowledge Record Response

```yaml
status: 201
body:
  knowledge_record_reference_id: string
  knowledge_status: string
  review_required: boolean
  related_event_reference_ids:
    - knowledge_record_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Authorized AI Retrieval Response

```yaml
status: 200
body:
  authorized_knowledge_reference_id: string
  retrieved_records:
    - knowledge_record_reference_id: string
      safe_summary: object
      allowed_content_scope: string
  policy_decision_reference_id: string | null
  human_review_required: boolean
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not expose restricted Knowledge content unless policy allows.
- Responses must not imply official truth or legal conclusion.
- Responses must distinguish safe summaries from full content.
- Responses must identify human review requirements for AI use.
```

---

# 11. Controlled Values

## 11.1 knowledge_type

```text
TrademarkLaw
JurisdictionRule
ClassificationGuidance
ProcedureGuidance
FeeGuidance
OfficePractice
CaseNote
TemplateGuidance
InternalPractice
AIAssistedDraft
Other
Unknown
```

## 11.2 knowledge_status

```text
Draft
Active
ReviewRequired
Verified
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
OfficialSource
ProfessionalInput
InternalPractice
ExternalArticle
CaseRecord
Template
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 11.4 retrieval_purpose

```text
Read
Summarize
Draft
Recommend
Validate
Classify
Explain
AIAssistedWorkflow
Unknown
```

## 11.5 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
Deprecated
ReviewRequired
ContextMismatch
Unknown
```

## 11.6 intended_use

```text
ProfessionalReference
AIAgentRetrieval
WorkflowSupport
DraftingSupport
ClassificationSupport
JurisdictionSupport
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
knowledge:create
knowledge:read
knowledge:search
knowledge:update
knowledge:validate
knowledge:ai:retrieve
knowledge:event:read
```

Rules:

```text
- Knowledge read/search must be permission-controlled.
- Knowledge creation must not imply verification.
- Knowledge validation must not authorize restricted use.
- AI retrieval requires explicit permission.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
KnowledgeCreationPolicy
KnowledgeUpdatePolicy
KnowledgeVisibilityPolicy
KnowledgeReferencePolicy
AIAgentKnowledgeAccessPolicy
EventVisibilityPolicy
RestrictedKnowledgeContentPolicy
CrossOrganizationKnowledgePolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Knowledge fields.
- Policy may require human review for AI-generated Knowledge.
- Policy may restrict cross-organization Knowledge lookup.
- Policy may restrict full content access and return safe summaries only.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Knowledge Record: Restricted / HumanReviewRequired where AI-generated
Get Knowledge Record: Restricted
Search Knowledge Records: Restricted
Update Knowledge Record: Restricted / HumanReviewRequired where sensitive
Validate Knowledge Reference: Allowed under contract
Retrieve Authorized Knowledge for AI: Restricted
List Knowledge Events: Restricted
```

AI Agents may:

```text
retrieve authorized Knowledge summaries
summarize allowed Knowledge content
draft Knowledge updates where allowed
flag stale, deprecated or conflicting Knowledge records
validate Knowledge references for authorized actions
```

AI Agents must not:

```text
fabricate verified Knowledge
fabricate Knowledge events
treat AI-generated content as verified Knowledge
treat Knowledge as legal conclusion
bypass source/version review
bypass Permission or Policy
expose restricted Knowledge content
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
authorized_knowledge_reference_id where applicable
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Knowledge API may expose:

```text
KnowledgeRecordCreated
KnowledgeRecordUpdated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Knowledge events directly.
- Knowledge events must not be treated as official source verification by themselves.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] knowledge_record_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] knowledge_type is controlled.
[ ] knowledge_status is controlled.
[ ] source_type is controlled.
[ ] source_reference is captured where required.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted content is omitted or allowed.
[ ] AI-generated content is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] KnowledgeRecordCreated is emitted after createKnowledgeRecord succeeds.
[ ] KnowledgeRecordUpdated is emitted after updateKnowledgeRecord succeeds.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
KnowledgeReferenceInvalid
SourceReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedKnowledgeContent
AgentContractRequired
HumanReviewRequired
EventEmissionFailed
InternalError
```

Error response:

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
- Errors must not expose restricted Knowledge content.
- Errors must not expose source access secrets.
- Errors must not expose permission or policy internals.
- Errors must be safe for product/API consumers.
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
- knowledge_type, knowledge_status and source_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI retrieval behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Knowledge API spec
cite Knowledge Service Specification
cite Knowledge Object Specification
cite KnowledgeRecordCreated and KnowledgeRecordUpdated Event Specifications
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe summaries by default
write tests for restricted Knowledge content hiding
write tests for invalid knowledge_record_reference_id
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AI Agent Contract requirement
write tests that AI-generated Knowledge is not verified automatically
write tests for KnowledgeRecordCreated event after successful create
write tests for KnowledgeRecordUpdated event after successful update
```

Codex must not:

```text
write directly to database bypassing Knowledge Service
allow UI to emit KnowledgeRecordCreated or KnowledgeRecordUpdated directly
treat Knowledge as official truth automatically
treat Knowledge as Evidence or Document
treat AI output as verified Knowledge
expose restricted Knowledge content for convenience
allow AI to fabricate Knowledge references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Knowledge API purpose.
[ ] It defines Knowledge API meaning.
[ ] It defines Knowledge API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, authorized AI retrieval and event-list operations.
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
| 0.1.0 | Draft | Initial Knowledge API specification. Defines governed Knowledge Record interface and separates Knowledge API from Policy, Permission, legal conclusion, official source truth, Evidence, Document, AI memory and AI-generated truth. |

---

**End of API Specification**
