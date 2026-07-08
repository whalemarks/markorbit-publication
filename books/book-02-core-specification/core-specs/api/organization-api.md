# API Specification — Organization API

**Spec ID:** B02-API-ORGANIZATION  
**Spec Type:** API Specification  
**API Name:** Organization API  
**API File:** core-specs/api/organization-api.md  
**Related Domain:** core-specs/domains/organization.md  
**Related Object Specs:** core-specs/objects/organization.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/customer.md; core-specs/objects/partner.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/organization-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/organization-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/organization-api-contract.md; core-specs/contracts/events/organization-created-payload.md  
**Related Agent Specs:** core-specs/agents/organization-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Organization API exposes governed Organization operating-context operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search and validate Organization references without treating Organization as Customer, Partner, Agent, Service Provider, User, Identity, Permission grant, Policy approval, billing entity or legal ownership proof.

Organization API exists to support:

```text
operating context creation
tenant/workspace context lookup
user/identity operating context preparation
permission evaluation context
policy evaluation context
customer/partner/provider boundary separation
event trace access
AI-safe organization reference handling
```

Organization API does not authenticate users, grant permissions, define customer ownership or create business relationship objects automatically.

---

# 2. API Meaning

Organization API means:

```text
a governed interface for operating Organization references through Organization Service.
```

Organization API does not mean:

```text
Customer API
Partner API
Agent API
Service Provider API
User membership API
Permission API
Policy API
billing API
legal ownership API
AI authority API
```

Organization provides operating context.

It is not demand-side party, cooperation-side relationship or provider profile by itself.

---

# 3. API Boundary

Organization API is responsible for:

```text
Organization create request intake
Organization read/search/list access
Organization update request intake
Organization reference validation
safe Organization response shaping
Permission/Policy enforcement for Organization operations
Organization-related Event reference exposure where allowed
AI Agent access boundary for Organization operations
controlled API errors
```

Organization API is not responsible for:

```text
authentication
User account lifecycle
User membership lifecycle unless a separate membership API is defined
Customer creation
Partner creation
Agent creation
Service Provider creation
Permission grant
Policy evaluation ownership
billing or finance ownership
legal ownership proof
AI Agent authorization by itself
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/organization.md
```

Domain rule:

```text
Organization provides operating context.
Organization is not Customer, Partner, Agent or Service Provider.
Organization does not grant Permission or evaluate Policy.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/organization.md
core-specs/objects/identity.md
core-specs/objects/user.md
core-specs/objects/customer.md
core-specs/objects/partner.md
core-specs/objects/agent.md
core-specs/objects/service-provider.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Organization API returns organization_reference_id.
- Organization API may reference Identity/User context but must not create membership silently.
- Organization API must not create Customer, Partner, Agent or Service Provider silently.
- Organization API must not treat Organization existence as Permission.
- Organization API must not treat Organization status as Policy approval.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/organization-service.md
core-specs/services/identity-service.md
core-specs/services/user-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Organization API must invoke Organization Service for Organization behavior.
- Organization API may validate Identity/User references through their owning services where required.
- Organization API must invoke Permission Service where operation requires authorization.
- Organization API must invoke Policy Service where contextual constraints apply.
- Organization API must not emit Organization events directly; Organization Service and Event Service govern events.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/organization-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createOrganization may result in OrganizationCreated.
- protected operations may produce PermissionEvaluated and PolicyEvaluated.
- API consumers must not fabricate OrganizationCreated.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Organization

**Operation Category:** Create  
**Method:** POST  
**Path:** `/organizations`  
**Owning Service Operation:** `createOrganization`  
**Permission Required:** `organization:create`  
**Policy Required:** `OrganizationCreationPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service Must Emit OrganizationCreated

Meaning:

```text
Create a governed Organization operating-context reference.
```

Non-meaning:

```text
does not create Customer
does not create Partner
does not create Agent
does not create Service Provider
does not create User membership
does not grant Permission
does not approve Policy
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Organization Service createOrganization
  ↓
Event Service record OrganizationCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Organization

**Operation Category:** Read  
**Method:** GET  
**Path:** `/organizations/{organization_reference_id}`  
**Owning Service Operation:** `getOrganization`  
**Permission Required:** `organization:read`  
**Policy Required:** `OrganizationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Organization operating-context view.
```

Non-meaning:

```text
does not expose restricted tenant data automatically
does not expose members, customers, partners or providers automatically
does not imply business authority or ownership
```

## 8.3 Operation: Search Organizations

**Operation Category:** Search  
**Method:** GET  
**Path:** `/organizations`  
**Owning Service Operation:** `searchOrganizations`  
**Permission Required:** `organization:search`  
**Policy Required:** `OrganizationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Organization references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted tenant directory access
does not expose restricted operating-context data by default
```

## 8.4 Operation: Update Organization

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/organizations/{organization_reference_id}`  
**Owning Service Operation:** `updateOrganization`  
**Permission Required:** `organization:update`  
**Policy Required:** `OrganizationUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit OrganizationUpdated where event is defined

Meaning:

```text
Update governed Organization metadata or status under Organization Service rules.
```

Non-meaning:

```text
does not update User membership automatically
does not update Customer/Partner/Agent/Service Provider objects
does not grant Permission
does not change billing or legal ownership automatically
```

## 8.5 Operation: Validate Organization Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/organizations/reference/validate`  
**Owning Service Operation:** `validateOrganizationReference`  
**Permission Required:** `organization:validate`  
**Policy Required:** `OrganizationReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that an Organization reference exists and may be used in the requested operating context.
```

Non-meaning:

```text
does not authorize action
does not prove membership
does not prove customer/provider/partner relationship
does not grant access to target object
```

## 8.6 Operation: List Organization Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/organizations/{organization_reference_id}/events`  
**Owning Service Operation:** `listOrganizationEvents`  
**Permission Required:** `organization:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Organization-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Organization Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  parent_organization_reference_id: string | null
  organization_type: string
  organization_status: string | optional
  display_reference: string | null
  source_type: string
  request_context: object
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Organization Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  organization_reference_id: string
body:
  actor_reference_id: string
  organization_status: string | optional
  display_reference: string | optional
  parent_organization_reference_id: string | optional
  source_type: string | optional
  request_context: object
```

## 9.3 Validate Organization Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Request rules:

```text
- Requests must not include payment credentials, secrets or restricted business data by default.
- Requests must use controlled organization_type and organization_status values.
- Requests must include actor_reference_id for protected operations.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Organization Response

```yaml
status: 200
body:
  organization_reference_id: string
  parent_organization_reference_id: string | null
  organization_type: string
  organization_status: string
  safe_summary:
    display_reference: string | null
    source_type: string
    created_at: datetime
    updated_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Organization Response

```yaml
status: 201
body:
  organization_reference_id: string
  organization_status: string
  related_event_reference_ids:
    - organization_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Validation Response

```yaml
status: 200
body:
  organization_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply Permission grant.
- Responses must not imply Customer/Partner/Agent/Service Provider relationship.
- Responses must not expose restricted tenant, member, billing or legal ownership data unless separately authorized.
```

---

# 11. Controlled Values

## 11.1 organization_type

```text
InternalOrganization
ClientOrganization
PartnerOrganization
ServiceProviderOrganization
Department
Workspace
Tenant
ExternalOrganization
Unknown
```

## 11.2 organization_status

```text
Draft
Active
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 source_type

```text
ProfessionalInput
SystemProcess
TenantProvisioning
ExternalIntegration
Migration
APIRequest
AIAssisted
Unknown
```

## 11.4 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ContextMismatch
Unknown
```

## 11.5 intended_use

```text
OperatingContext
UserMembershipPreparation
PermissionEvaluation
PolicyEvaluation
CustomerContext
PartnerContext
ServiceProviderContext
AuditReference
AIAgentAction
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
organization:create
organization:read
organization:search
organization:update
organization:validate
organization:event:read
```

Rules:

```text
- Organization read/search must be permission-controlled.
- Organization creation must not imply Permission grant.
- Organization validation must not be used as authorization decision.
- Organization existence must not be treated as User membership.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
OrganizationCreationPolicy
OrganizationUpdatePolicy
OrganizationVisibilityPolicy
OrganizationReferencePolicy
EventVisibilityPolicy
AIAgentOrganizationAccessPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Organization fields.
- Policy may require human review for AI-created or AI-updated Organization references.
- Policy may restrict cross-organization lookup.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Organization: Restricted
Get Organization: Restricted
Search Organizations: Restricted
Update Organization: Restricted / HumanReviewRequired where sensitive
Validate Organization Reference: Allowed under contract
List Organization Events: Restricted
```

AI Agents may:

```text
validate organization references for authorized actions
summarize safe Organization metadata
prepare draft Organization creation/update requests where allowed
flag missing or invalid Organization references
flag cross-organization access requiring review
```

AI Agents must not:

```text
fabricate Organization
fabricate OrganizationCreated events
create Organization without Agent Contract where required
treat Organization as Customer, Partner, Agent or Service Provider
treat Organization as Permission grant
treat Organization as membership proof
expose restricted Organization data
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Organization API may expose:

```text
OrganizationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Organization events directly.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] organization_reference_id is present where required.
[ ] parent_organization_reference_id is valid where provided.
[ ] actor_reference_id is present.
[ ] organization_type is controlled.
[ ] organization_status is controlled.
[ ] source_type is controlled.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted fields are omitted or allowed.
[ ] No payment credentials, secrets or restricted business data are included by default.
[ ] AI Agent Contract is present where required.
[ ] OrganizationCreated is emitted after createOrganization succeeds.
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
OrganizationReferenceInvalid
ParentOrganizationReferenceInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
AgentContractRequired
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
- Errors must not expose restricted Organization fields.
- Errors must not expose member, customer, partner, provider, billing or ownership internals.
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
- organization_type and organization_status changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Organization API spec
cite Organization Service Specification
cite Organization Object Specification
cite OrganizationCreated Event Specification
cite Permission and Policy specs before protected operations
implement request validation before service invocation
validate parent_organization_reference_id where provided
enforce Permission and Policy before protected operations
return safe responses by default
write tests for invalid organization_reference_id
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for OrganizationCreated event after successful create
write tests that Organization API does not create Customer/Partner/Agent/Service Provider silently
write tests that Organization API does not imply User membership
write tests for AI Agent Contract requirement
```

Codex must not:

```text
write directly to database bypassing Organization Service
allow UI to emit OrganizationCreated directly
treat Organization as Customer
treat Organization as Partner
treat Organization as Agent
treat Organization as Service Provider
treat Organization validation as Permission
create membership silently from Organization operations
expose secrets, billing data or restricted business data
allow AI to fabricate Organization references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Organization API purpose.
[ ] It defines Organization API meaning.
[ ] It defines Organization API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate and event-list operations.
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
| 0.1.0 | Draft | Initial Organization API specification. Defines governed Organization operating-context interface and separates Organization API from Customer, Partner, Agent, Service Provider, User membership, Permission, Policy and AI authority. |

---

**End of API Specification**
