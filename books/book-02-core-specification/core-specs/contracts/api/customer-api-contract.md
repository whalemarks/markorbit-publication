# API Contract — Customer API

**Spec ID:** B02-CONTRACT-API-CUSTOMER  
**Spec Type:** API Contract Specification  
**Contract Name:** Customer API Contract  
**Contract File:** core-specs/contracts/api/customer-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/customer-api.md  
**Related Domain:** Customer  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/organization.md; core-specs/objects/user.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/document.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/organization-service.md; core-specs/services/user-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/document-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/customer-api.md; core-specs/api/organization-api.md; core-specs/api/user-api.md; core-specs/api/brand-api.md; core-specs/api/trademark-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/document-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/customer-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/task-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Customer API Contract defines the implementation-facing request and response contract for Customer API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, link and reference Customer records through governed API boundaries without bypassing Customer Service, Organization Service, User Service, related professional/business services, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Customer API versioning
Customer create request
Customer update request
Customer read response
Customer search/list response
Customer reference validation
Customer organization/user linkage
Brand/Trademark/Matter/Order relationship references
Customer contact-safe fields
Customer relationship context
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Customer API Contract does not define sales qualification by itself, create legal representation, approve engagement, replace Customer Service, replace Matter or Order governance, evaluate Permission/Policy, or authorize AI output as final business decision.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Customer Service through governed API boundaries.
```

This contract does not mean:

```text
CRM product UI
sales qualification finality
legal representation approval
engagement letter approval
billing account by itself
brand owner proof
permission grant
policy approval
event emitter
UI form
```

Core rule:

```text
Customer API receives governed customer requests.
Customer Service owns Customer behavior.
Organization, User, Brand, Trademark, Matter and Order references are validated by owning services.
Permission and Policy govern access.
Customer relationship use requires governed business process.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Customer reference fields
Organization/User linkage fields
Brand/Trademark/Matter/Order relationship fields
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
Customer lifecycle ownership outside Customer Service
sales pipeline ownership
legal engagement approval
matter creation
order creation
billing execution
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
core-specs/api/customer-api.md
```

Owning service spec:

```text
core-specs/services/customer-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Customer API and Customer Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Customer
```

Related objects:

```text
Organization
User
Brand
Trademark
Matter
Order
Document
Permission
Policy
Event
Agent
```

Reference rules:

```text
- customer_reference_id identifies Customer.
- organization_reference_id may link Customer to Organization where Customer Service allows.
- user_reference_ids may identify customer-side contacts where User Service allows.
- brand/trademark/matter/order/document references must be validated by owning services.
- Customer linkage does not create legal representation or order obligation by itself.
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

Customer target context:

```yaml
target:
  customer_reference_id: string | null
  target_object_type: Customer
  target_object_reference_id: string | null
```

Rules:

```text
- customer_reference_id is required for read/update/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- linked references must be validated by owning services where provided.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/customers
GET    /v1/customers/{customer_reference_id}
PATCH  /v1/customers/{customer_reference_id}
GET    /v1/customers
POST   /v1/customers/validate-reference
POST   /v1/customers/{customer_reference_id}/link-contacts
POST   /v1/customers/{customer_reference_id}/link-business-objects
POST   /v1/customers/{customer_reference_id}/prepare-profile-summary
```

Endpoint ownership:

```text
API layer validates request contract.
Customer Service executes behavior.
Organization Service validates organization references.
User Service validates contact/user references.
Brand/Trademark/Matter/Order/Document services validate relationship references.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted customer summaries where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Customer Request Contract

Endpoint:

```text
POST /v1/customers
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
    - customer:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - customer:create:policy
  policy_decision_reference_id: string | null

payload:
  customer_type: string
  customer_status: string | null
  customer_name_safe: string
  customer_display_name_safe: string | null
  customer_organization_reference_id: string | null
  contact_user_reference_ids:
    - string
  primary_contact_name_safe: string | null
  primary_contact_email_safe: string | null
  primary_contact_phone_safe: string | null
  source_type: string | null
  source_reference_id: string | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- customer_type and customer_name_safe are required.
- customer_organization_reference_id must be validated by Organization Service where provided.
- contact_user_reference_ids must be validated by User Service where provided.
- contact fields are safe contact fields and do not prove legal authority.
- Customer Service assigns customer_reference_id.
```

---

# 9. Create Customer Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  customer_reference_id: string
  customer_type: string
  customer_status: string
  customer_name_safe: string
  customer_display_name_safe: string | null
  customer_organization_reference_id: string | null
  contact_user_reference_ids_visible:
    - string
  primary_contact_name_safe: string | null
  primary_contact_email_safe: string | null
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
- CustomerCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate CustomerCreated event.
```

---

# 10. Read Customer Contract

Endpoint:

```text
GET /v1/customers/{customer_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  customer_reference_id: string
  customer_type: string
  customer_status: string
  customer_name_safe: string
  customer_display_name_safe: string | null
  customer_organization_reference_id: string | null
  contact_user_reference_ids_visible:
    - string
  primary_contact_name_safe: string | null
  primary_contact_email_safe: string | null
  primary_contact_phone_visible: string | null
  linked_brand_reference_ids_visible:
    - string
  linked_trademark_reference_ids_visible:
    - string
  linked_matter_reference_ids_visible:
    - string
  linked_order_reference_ids_visible:
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
- Read must evaluate customer:read permission.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Contact fields, relationship references and metadata may be omitted by policy.
- NotFound may be returned where policy forbids existence disclosure.
```

---

# 11. Update Customer Contract

Endpoint:

```text
PATCH /v1/customers/{customer_reference_id}
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
  customer_status: string | null
  customer_name_safe: string | null
  customer_display_name_safe: string | null
  primary_contact_name_safe: string | null
  primary_contact_email_safe: string | null
  primary_contact_phone_safe: string | null
  source_type: string | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - customer:update
policy_context:
  required_policy_scopes:
    - customer:update:policy
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
  customer_reference_id: string
  customer_status: string
  customer_name_safe: string
  customer_display_name_safe: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
```

Rules:

```text
- Update must route through Customer Service.
- Customer status transitions must follow Customer Service rules.
- Restricted contact/metadata fields must not be patched unless policy allows them.
- Human review may be required for status changes affecting engagement or handoff.
```

---

# 12. Search/List Customer Contract

Endpoint:

```text
GET /v1/customers
```

Query parameters:

```yaml
customer_type: string | null
customer_status: string | null
customer_organization_reference_id: string | null
contact_user_reference_id: string | null
source_type: string | null
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
    - customer_reference_id: string
      customer_type: string
      customer_status: string
      customer_name_safe: string
      customer_display_name_safe: string | null
      primary_contact_name_safe: string | null
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
- Search must not reveal restricted Customer existence.
- safe_query must not be treated as unrestricted search over private contact data.
```

---

# 13. Validate Customer Reference Contract

Endpoint:

```text
POST /v1/customers/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  customer_reference_id: string
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
  customer_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  customer_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Customer.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or customer type.
```

---

# 14. Link Contacts Contract

Endpoint:

```text
POST /v1/customers/{customer_reference_id}/link-contacts
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  user_reference_ids:
    - string
  contact_relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - customer:contact:link
policy_context:
  required_policy_scopes:
    - customer:contact:link:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  customer_reference_id: string
  contact_user_reference_ids_visible:
    - string
  contact_relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Customer Service.
- User references must be validated by User Service.
- Contact linkage does not prove legal authority or signatory authority by itself.
```

---

# 15. Link Business Objects Contract

Endpoint:

```text
POST /v1/customers/{customer_reference_id}/link-business-objects
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
    - customer:business-object:link
policy_context:
  required_policy_scopes:
    - customer:business-object:link:policy
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
  customer_reference_id: string
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
- Linked target references must be validated by owning services.
- Link operation does not create Matter, Order, Brand or Trademark.
- Link operation does not transfer ownership of linked records.
- Human review may be required where linkage affects engagement or customer-facing responsibility.
```

---

# 16. Prepare Profile Summary Contract

Endpoint:

```text
POST /v1/customers/{customer_reference_id}/prepare-profile-summary
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
    - customer:summary:prepare
policy_context:
  required_policy_scopes:
    - customer:summary:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  summary_purpose: string
  requested_summary_scope: string
  include_relationship_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  summary_status: string
  customer_profile_summary_safe: string | null
  relationship_context_visible:
    brand_count: integer | null
    trademark_count: integer | null
    matter_count: integer | null
    order_count: integer | null
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
- Profile summary is assistance, not sales qualification or legal engagement approval.
- AI-assisted summary must follow AI governance.
- Policy may downgrade to metadata-only or omit relationship context.
- Human review may be required before customer-facing use.
```

---

# 17. Controlled Values

## 17.1 customer_type

```text
Individual
Company
AgencyPartner
BrandOwner
Applicant
Registrant
Prospect
InternalCustomer
Unknown
```

## 17.2 customer_status

```text
Draft
Prospect
Active
Inactive
Suspended
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 source_type

```text
Manual
WebsiteLead
PartnerReferral
ExistingOrder
ImportedRecord
EmailInquiry
WechatInquiry
SystemGenerated
Unknown
```

## 17.4 contact_relationship_type

```text
PrimaryContact
BillingContact
LegalContact
BusinessContact
TechnicalContact
ExternalAgentContact
Unknown
```

## 17.5 relationship_type

```text
Owner
Applicant
Registrant
Payer
Requester
Beneficiary
RelatedParty
HistoricalReference
Unknown
```

## 17.6 target_object_type

```text
Brand
Trademark
Matter
Order
Document
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
customer_name_safe
customer_status
customer_type
source_type
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] customer_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] customer_type is controlled.
[ ] customer_status is controlled where provided.
[ ] source_type is controlled where provided.
[ ] customer_organization_reference_id is validated where provided.
[ ] contact_user_reference_ids are validated where provided.
[ ] business object references are validated where provided.
[ ] contact_relationship_type is controlled.
[ ] relationship_type is controlled.
[ ] link_operation is controlled.
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
customer:create
customer:read
customer:search
customer:update
customer:validate
customer:contact:link
customer:business-object:link
customer:summary:prepare
```

Rules:

```text
- Customer API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
customer:create:policy
customer:read:policy
customer:search:policy
customer:update:policy
customer:reference:policy
customer:visibility:policy
customer:contact:visibility:policy
customer:contact:link:policy
customer:business-object:link:policy
customer:summary:prepare:policy
cross-organization:customer
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact contact fields, linked business objects, relationship context, summaries or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before customer-facing use.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may summarize Customer context only within Permission and Policy limits.
- AI must not decide legal engagement, signatory authority, payment responsibility or customer qualification finality.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Customer API output is used for engagement, billing, external communication, task creation or customer-facing recommendation.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/customers requires idempotency_key.
PATCH /v1/customers/{customer_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Link endpoints may require idempotency_key for Add/Remove/Replace operations.
Summary preparation does not normally require idempotency unless result is persisted.
```

Events:

```text
CustomerCreated may be emitted by Customer Service after successful creation.
Customer update/link events may be reserved for later if event specs exist.
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
CustomerReferenceInvalid
OrganizationReferenceInvalid
UserReferenceInvalid
BusinessObjectReferenceInvalid
ContactRelationshipInvalid
RelationshipTypeInvalid
SummaryUnavailable
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
- Errors must not expose database IDs, restricted customer data, private contact data, policy internals or permission internals.
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
cite Customer API Spec
cite Customer Service Spec
cite this Customer API Contract
use Reference Contract for customer_reference_id and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted profile summaries
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive link operations
use Versioning Contract for version validation
route all mutation through Customer Service
invoke Organization/User services for customer organization and contact reference validation
invoke Brand/Trademark/Matter/Order/Document services for business object reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing contact fields, relationship context or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/link-contacts/link-business-objects/prepare-profile-summary
write tests for organization/user reference validation
write tests for business object reference validation
write tests for contact visibility restriction
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
create Customer directly in API layer
query database directly from API contract implementation
use generic id where customer_reference_id is required
expose database IDs or private contact data
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
mutate Brand/Trademark/Matter/Order/Document lifecycle through Customer link endpoints
treat Customer linkage as legal representation or engagement approval
treat AI customer summary as sales qualification finality
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Customer API Contract is accepted only if:

```text
[ ] It defines Customer API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Customer API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines link contacts contract.
[ ] It defines link business objects contract.
[ ] It defines prepare profile summary contract.
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
| 0.1.0 | Draft | Initial Customer API Contract. Defines governed create, read, update, search, validate-reference, contact-link, business-object-link and profile-summary payloads, linked reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
