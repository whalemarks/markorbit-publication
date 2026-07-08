# API Contract — Opportunity API

**Spec ID:** B02-CONTRACT-API-OPPORTUNITY  
**Spec Type:** API Contract Specification  
**Contract Name:** Opportunity API Contract  
**Contract File:** core-specs/contracts/api/opportunity-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/opportunity-api.md  
**Related Domain:** Opportunity  
**Related Object Specs:** core-specs/objects/opportunity.md; core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/communication.md; core-specs/objects/task.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/opportunity-service.md; core-specs/services/customer-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/communication-service.md; core-specs/services/task-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/opportunity-api.md; core-specs/api/customer-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/document-api.md; core-specs/api/communication-api.md; core-specs/api/task-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 4 — Collaboration Network / Business Expansion  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Opportunity API Contract defines the implementation-facing request and response contract for Opportunity API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and prepare Opportunity records through governed API boundaries without bypassing Opportunity Service, Customer Service, Order Service, Matter Service, Communication Service, Task Service, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Opportunity API versioning
Opportunity create request
Opportunity update request
Opportunity read response
Opportunity search/list response
Opportunity reference validation
Customer and business object linkage
Opportunity qualification assistance
Opportunity follow-up preparation
Opportunity conversion preparation
Communication and Task preparation context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Opportunity API Contract does not approve sales qualification by itself, create Orders, create Matters, send communications, create active Tasks, approve pricing, approve engagement, replace Opportunity Service, evaluate Permission/Policy, or authorize AI output as final business decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Opportunity Service through governed API boundaries.
```

This contract does not mean:

```text
CRM product UI
sales qualification finality
order creation
matter creation
pricing approval
engagement approval
customer consent
communication delivery
task execution
permission grant
policy approval
event emitter
```

Core rule:

```text
Opportunity API receives governed opportunity requests.
Opportunity Service owns Opportunity behavior.
Customer, Order, Matter, Brand, Trademark, Communication and Task references are validated by owning services.
Permission and Policy govern access.
Opportunity conversion requires governed service process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Opportunity reference fields
Customer/business object linkage fields
qualification preparation fields
follow-up preparation fields
conversion preparation fields
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
Opportunity lifecycle ownership outside Opportunity Service
sales approval
pricing approval
order creation
matter creation
communication sending
task creation
payment handling
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
core-specs/api/opportunity-api.md
```

Owning service spec:

```text
core-specs/services/opportunity-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Opportunity API and Opportunity Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Opportunity
```

Related objects:

```text
Customer
Order
Matter
Brand
Trademark
Document
Communication
Task
Permission
Policy
Event
Agent
```

Reference rules:

```text
- opportunity_reference_id identifies Opportunity.
- customer_reference_id links Opportunity to Customer where Opportunity Service allows.
- brand/trademark/document references must be validated by owning services.
- communication_reference_ids and task_reference_ids must be validated by Communication Service and Task Service.
- order_reference_id and matter_reference_id may be conversion outputs but must not be created by this API contract alone.
- Opportunity linkage does not create customer consent, order obligation or legal engagement by itself.
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

Opportunity target context:

```yaml
target:
  opportunity_reference_id: string | null
  target_object_type: Opportunity
  target_object_reference_id: string | null
```

Rules:

```text
- opportunity_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/opportunities
GET    /v1/opportunities/{opportunity_reference_id}
PATCH  /v1/opportunities/{opportunity_reference_id}
GET    /v1/opportunities
POST   /v1/opportunities/validate-reference
POST   /v1/opportunities/{opportunity_reference_id}/link-business-objects
POST   /v1/opportunities/{opportunity_reference_id}/prepare-qualification
POST   /v1/opportunities/{opportunity_reference_id}/prepare-follow-up
POST   /v1/opportunities/{opportunity_reference_id}/prepare-conversion
POST   /v1/opportunities/{opportunity_reference_id}/transition-status
```

Endpoint ownership:

```text
API layer validates request contract.
Opportunity Service executes Opportunity behavior.
Customer/Order/Matter/Brand/Trademark/Document/Communication/Task services validate references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted preparation where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Opportunity Request Contract

Endpoint:

```text
POST /v1/opportunities
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
    - opportunity:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - opportunity:create:policy
  policy_decision_reference_id: string | null

payload:
  opportunity_type: string
  opportunity_status: string | null
  opportunity_title_safe: string
  customer_reference_id: string | null
  source_type: string | null
  source_reference_id: string | null
  brand_reference_ids:
    - string
  trademark_reference_ids:
    - string
  document_reference_ids:
    - string
  estimated_service_scope_safe: string | null
  estimated_value_band: string | null
  priority_level: string | null
  expected_close_date: date | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- opportunity_type and opportunity_title_safe are required.
- customer_reference_id must be validated by Customer Service where provided.
- brand/trademark/document references must be validated by owning services where provided.
- estimated_value_band is a safe band, not exact pricing approval.
- Opportunity Service assigns opportunity_reference_id.
```

---

# 9. Create Opportunity Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  opportunity_reference_id: string
  opportunity_type: string
  opportunity_status: string
  opportunity_title_safe: string
  customer_reference_id: string | null
  source_type: string | null
  estimated_value_band: string | null
  priority_level: string | null
  expected_close_date: date | null
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
- Opportunity events may be returned only if event specs exist and service emits them.
- Replayed idempotent response must not duplicate events.
```

---

# 10. Read Opportunity Contract

Endpoint:

```text
GET /v1/opportunities/{opportunity_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  opportunity_reference_id: string
  opportunity_type: string
  opportunity_status: string
  opportunity_title_safe: string
  customer_reference_id: string | null
  source_type: string | null
  source_reference_id_visible: string | null
  brand_reference_ids_visible:
    - string
  trademark_reference_ids_visible:
    - string
  document_reference_ids_visible:
    - string
  communication_reference_ids_visible:
    - string
  task_reference_ids_visible:
    - string
  converted_order_reference_id: string | null
  converted_matter_reference_id: string | null
  estimated_service_scope_safe: string | null
  estimated_value_band: string | null
  priority_level: string | null
  expected_close_date: date | null
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
- Read must evaluate opportunity:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Private notes, commercial terms, source details and linked references may be omitted by policy.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Opportunity Contract

Endpoint:

```text
PATCH /v1/opportunities/{opportunity_reference_id}
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
  opportunity_status: string | null
  opportunity_title_safe: string | null
  estimated_service_scope_safe: string | null
  estimated_value_band: string | null
  priority_level: string | null
  expected_close_date: date | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - opportunity:update
policy_context:
  required_policy_scopes:
    - opportunity:update:policy
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
  opportunity_reference_id: string
  opportunity_status: string
  opportunity_title_safe: string
  estimated_value_band: string | null
  priority_level: string | null
  expected_close_date: date | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Opportunity Service.
- Opportunity status transitions must follow Opportunity Service rules.
- Restricted commercial or private metadata must not be patched unless policy allows it.
- Human review may be required for conversion, loss, handoff or payment-impacting updates.
```

---

# 12. Search/List Opportunity Contract

Endpoint:

```text
GET /v1/opportunities
```

Query parameters:

```yaml
opportunity_type: string | null
opportunity_status: string | null
customer_reference_id: string | null
brand_reference_id: string | null
trademark_reference_id: string | null
source_type: string | null
priority_level: string | null
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
    - opportunity_reference_id: string
      opportunity_type: string
      opportunity_status: string
      opportunity_title_safe: string
      customer_reference_id: string | null
      estimated_value_band: string | null
      priority_level: string | null
      expected_close_date: date | null
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
- Search must not reveal restricted Opportunity existence.
- safe_query must not be treated as unrestricted search over private notes or commercial terms.
```

---

# 13. Validate Opportunity Reference Contract

Endpoint:

```text
POST /v1/opportunities/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  opportunity_reference_id: string
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
  opportunity_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  opportunity_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Opportunity.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or opportunity type.
```

---

# 14. Link Business Objects Contract

Endpoint:

```text
POST /v1/opportunities/{opportunity_reference_id}/link-business-objects
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  business_object_links:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - opportunity:business-object:link
policy_context:
  required_policy_scopes:
    - opportunity:business-object:link:policy
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
  opportunity_reference_id: string
  linked_business_objects_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Opportunity Service.
- Linked target references must be validated by owning services.
- Link operation does not create or mutate linked objects.
- Human review may be required where linkage affects sales scope or customer-facing responsibility.
```

---

# 15. Prepare Qualification Contract

Endpoint:

```text
POST /v1/opportunities/{opportunity_reference_id}/prepare-qualification
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
    - opportunity:qualification:prepare
policy_context:
  required_policy_scopes:
    - opportunity:qualification:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  qualification_purpose: string
  requested_scope: string | null
  include_customer_context: boolean
  include_brand_trademark_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  qualification_status: string
  qualification_summary_safe: string | null
  suggested_next_actions_safe:
    - string
  missing_context_safe:
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
- Qualification preparation is assistance, not sales approval.
- AI must not make final commercial, legal or engagement decisions.
- Human review may be required before customer-facing or conversion use.
```

---

# 16. Prepare Follow-Up Contract

Endpoint:

```text
POST /v1/opportunities/{opportunity_reference_id}/prepare-follow-up
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
    - opportunity:follow-up:prepare
policy_context:
  required_policy_scopes:
    - opportunity:follow-up:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  follow_up_purpose: string
  channel_preference: string | null
  include_draft_communication: boolean
  include_task_suggestion: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  follow_up_status: string
  draft_communication_safe: string | null
  suggested_tasks_safe:
    - task_title_safe: string
      task_type: string
      suggested_due_date: date | null
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Follow-up preparation is assistance, not communication sending.
- Sending communication must route through Communication Service.
- Creating active Tasks must route through Task Service.
- Human review may be required before external communication.
```

---

# 17. Prepare Conversion Contract

Endpoint:

```text
POST /v1/opportunities/{opportunity_reference_id}/prepare-conversion
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
    - opportunity:conversion:prepare
policy_context:
  required_policy_scopes:
    - opportunity:conversion:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  conversion_target: string
  include_order_draft: boolean
  include_matter_draft: boolean
  include_task_plan: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  conversion_preparation_status: string
  proposed_order_payload_safe: object | null
  proposed_matter_payload_safe: object | null
  proposed_task_plan_safe: object | null
  missing_context_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Conversion preparation is assistance, not Order or Matter creation.
- Creating Order must route through Order Service.
- Creating Matter must route through Matter Service.
- Creating active Tasks must route through Task Service.
- Human review may be required before conversion.
```

---

# 18. Transition Status Contract

Endpoint:

```text
POST /v1/opportunities/{opportunity_reference_id}/transition-status
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
  requested_status: string
  transition_reason_safe: string | null
  converted_order_reference_id: string | null
  converted_matter_reference_id: string | null
permission_context:
  required_permission_keys:
    - opportunity:status:transition
policy_context:
  required_policy_scopes:
    - opportunity:status:transition:policy
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
  opportunity_reference_id: string
  previous_status: string
  current_status: string
  converted_order_reference_id: string | null
  converted_matter_reference_id: string | null
  transitioned_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Status transition must route through Opportunity Service.
- Converted order/matter references must be validated by owning services.
- Transitioning to Converted does not create Order or Matter by itself.
- Protected transitions may require human_review_reference_id.
```

---

# 19. Controlled Values

## 19.1 opportunity_type

```text
NewApplicationOpportunity
RenewalOpportunity
OfficeActionOpportunity
PortfolioOpportunity
EvidenceOpportunity
ConsultationOpportunity
CrossSellOpportunity
PartnerReferralOpportunity
InboundLeadOpportunity
InternalOpportunity
Other
Unknown
```

## 19.2 opportunity_status

```text
Draft
New
Qualified
Contacted
ProposalPrepared
ProposalSent
Negotiating
Won
Lost
Converted
Archived
DeletedReferenceOnly
Unknown
```

## 19.3 source_type

```text
Manual
WebsiteLead
PartnerReferral
CustomerRequest
ExistingCustomer
ExistingTrademark
Campaign
ImportedRecord
Communication
SystemGenerated
Unknown
```

## 19.4 estimated_value_band

```text
Unknown
Low
Medium
High
Strategic
```

## 19.5 priority_level

```text
Low
Normal
High
Urgent
Unknown
```

## 19.6 conversion_target

```text
Order
Matter
OrderAndMatter
TaskOnly
NoConversion
Unknown
```

## 19.7 channel_preference

```text
Email
Phone
Wechat
WhatsApp
PortalMessage
InternalTask
Unknown
```

## 19.8 target_object_type

```text
Customer
Order
Matter
Brand
Trademark
Document
Communication
Task
Unknown
```

## 19.9 relationship_type

```text
PrimarySubject
SupportingSubject
SourceObject
FollowUpObject
ConvertedObject
HistoricalReference
Unknown
```

## 19.10 qualification_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 19.11 follow_up_status

```text
Completed
Partial
NoFollowUpSuggested
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 19.12 conversion_preparation_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 19.13 validation_status

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

## 19.14 sort.field

```text
created_at
updated_at
expected_close_date
opportunity_title_safe
opportunity_status
opportunity_type
priority_level
estimated_value_band
```

---

# 20. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] opportunity_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] opportunity_type is controlled.
[ ] opportunity_status is controlled where provided.
[ ] customer/business object references are validated where provided.
[ ] converted_order_reference_id and converted_matter_reference_id are validated where provided.
[ ] relationship_type is controlled.
[ ] link_operation is controlled.
[ ] AI Context is present for AI-assisted preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 21. Permission Rules

Required permission keys:

```text
opportunity:create
opportunity:read
opportunity:search
opportunity:update
opportunity:validate
opportunity:business-object:link
opportunity:qualification:prepare
opportunity:follow-up:prepare
opportunity:conversion:prepare
opportunity:status:transition
```

Rules:

```text
- Opportunity API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 22. Policy Rules

Required policy scopes may include:

```text
opportunity:create:policy
opportunity:read:policy
opportunity:search:policy
opportunity:update:policy
opportunity:reference:policy
opportunity:visibility:policy
opportunity:business-object:link:policy
opportunity:qualification:prepare:policy
opportunity:follow-up:prepare:policy
opportunity:conversion:prepare:policy
opportunity:status:transition:policy
opportunity:commercial-terms:visibility:policy
cross-organization:opportunity
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact linked objects, commercial context, private notes, follow-up drafts, conversion payloads or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before conversion, status transition or customer-facing output.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 23. AI and Human Review Rules

AI rules:

```text
- AI may summarize Opportunity context and prepare qualification, follow-up and conversion drafts only within Permission and Policy limits.
- AI must not create Orders, create Matters, send communications, create active tasks, approve pricing or decide final sales qualification.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Opportunity output is used for conversion, status transition, external communication, task creation, pricing-impacting action or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 24. Idempotency and Event Rules

Idempotency:

```text
POST /v1/opportunities requires idempotency_key.
PATCH /v1/opportunities/{opportunity_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link and transition endpoints may require idempotency_key for duplicate-sensitive operations.
Preparation endpoints do not normally require idempotency unless result is persisted.
```

Events:

```text
Opportunity events may be reserved for later if event specs exist.
OrderCreated, MatterCreated, TaskCreated and CommunicationCreated may only be emitted by their owning services, not this API.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 25. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
OpportunityReferenceInvalid
CustomerReferenceInvalid
BusinessObjectReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
CommunicationReferenceInvalid
TaskReferenceInvalid
RelationshipTypeInvalid
QualificationUnavailable
FollowUpPreparationUnavailable
ConversionPreparationUnavailable
StatusTransitionInvalid
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
- Errors must not expose database IDs, restricted opportunity data, commercial terms, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 26. Versioning Rules

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

# 27. Codex Implementation Notes

Codex must:

```text
cite Opportunity API Spec
cite Opportunity Service Spec
cite this Opportunity API Contract
use Reference Contract for opportunity_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted qualification/follow-up/conversion preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link/transition operations
use Versioning Contract for version validation
route all Opportunity mutation through Opportunity Service
invoke Customer/Order/Matter/Brand/Trademark/Document/Communication/Task services for reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing linked objects, commercial context, private notes or drafts
return safe errors only
write tests for create/read/update/search/validate-reference/link-business-objects/prepare-qualification/prepare-follow-up/prepare-conversion/transition-status
write tests for linked reference validation
write tests that follow-up preparation does not send communication
write tests that conversion preparation does not create Order or Matter
write tests that task suggestions do not create active Tasks
write tests for protected status transition requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Opportunity directly in API layer
query database directly from API contract implementation
use generic id where opportunity_reference_id is required
expose database IDs, commercial terms or private opportunity notes without policy allowance
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
create Order, Matter, Task or Communication from preparation endpoints
send external communication from this API contract
treat AI qualification, follow-up or conversion preparation as approval
allow AI context to exceed evaluated_data_access_scope
```

---

# 28. Acceptance Criteria

This Opportunity API Contract is accepted only if:

```text
[ ] It defines Opportunity API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Opportunity API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link business objects contract.
[ ] It defines prepare qualification contract.
[ ] It defines prepare follow-up contract.
[ ] It defines prepare conversion contract.
[ ] It defines transition status contract.
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

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Opportunity API Contract. Defines governed create, read, update, search, validate-reference, business-object-link, qualification preparation, follow-up preparation, conversion preparation and status transition payloads, linked reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
