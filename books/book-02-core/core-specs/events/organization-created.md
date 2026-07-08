# Event Specification — OrganizationCreated

**Spec ID:** B02-EVT-ORGANIZATION-CREATED  
**Spec Type:** Event  
**Event Name:** OrganizationCreated  
**Event File:** core-specs/events/organization-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Organization  
**Producing Service:** core-specs/services/organization-service.md  
**Related Object Specs:** core-specs/objects/organization.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/organization-service.md; core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/organization-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/organization-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/organization-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

OrganizationCreated records that a governed Organization operating-context reference has been created by Organization Service.

It exists so that Identity, User, Permission, Policy, Event, Audit, AI Agents, APIs and product consumers can safely recognize that an organization context now exists without treating that Organization as a Customer, Partner, Agent, Service Provider, billing entity, permission grant, policy approval or automatic membership container.

OrganizationCreated is required before:

```text
organization operating context trace
user organization membership preparation
permission evaluation context
policy evaluation context
multi-tenant context validation
business object ownership context
actor audit trace
AI-assisted organization administration review
API organization reference validation
```

---

# 2. Event Meaning

OrganizationCreated means:

```text
a stable Organization object reference has been created through governed Organization Service operation.
```

OrganizationCreated does not mean:

```text
the Organization is a Customer
the Organization is a Partner
the Organization is an Agent
the Organization is a Service Provider
any User belongs to the Organization
any Identity has Permission in the Organization
the Organization has passed Policy
the Organization has billing/payment status
the Organization owns any Matter, Order, Brand or Trademark
```

OrganizationCreated records operating-context creation only.

It does not establish membership, authorization, commercial relationship, billing relationship or business object ownership.

---

# 3. Event Category

OrganizationCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Organization domain.

It is not a Customer event, Partner event, Agent event or Service Provider event.

---

# 4. Event Producer

Producing service:

```text
Organization Service
```

Producing operation:

```text
createOrganization
```

Source domain:

```text
Organization
```

Source object type:

```text
Organization
```

Allowed producer path:

```text
API / Admin / System / AI-governed operation
        ↓
Organization Service createOrganization
        ↓
Event Service record OrganizationCreated
```

Producer rules:

```text
- OrganizationCreated must be emitted only after Organization Service successfully creates the Organization reference.
- OrganizationCreated must not be emitted directly by product UI.
- OrganizationCreated must not be emitted directly by AI Agent outside governed service operation.
- OrganizationCreated must not be emitted for failed, duplicate-rejected or unauthorized organization creation attempts.
```

---

# 5. Event Trigger

OrganizationCreated is triggered when:

```text
Organization Service successfully creates a new Organization object and commits its stable organization_reference_id.
```

Required trigger conditions:

```text
createOrganization operation completed
organization_reference_id created
organization_type validated
organization_status validated
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
User creation
Identity creation
Organization membership creation
Customer creation
Partner creation
Agent creation
Service Provider creation
billing setup
permission grant
policy evaluation
AI suggestion to create Organization
failed validation
duplicate rejected Organization
```

Related but separate events may include:

```text
UserCreated
IdentityCreated
OrganizationUpdated
OrganizationMemberLinked
CustomerCreated
PartnerCreated
AgentCreated
ServiceProviderCreated
PermissionEvaluated
PolicyEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: OrganizationCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Organization
source_service: Organization Service
source_operation: createOrganization
source_object_type: Organization
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/organization-created-payload.md
safe_summary:
  organization_reference_id: string
  organization_type: string
  organization_status: string
  source_type: string
restricted_fields_policy: OrganizationCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
organization_reference_id: string
organization_type: string
organization_status: string
created_by_actor_reference_id: string
parent_organization_reference_id: string | null
source_type: string
is_internal_organization: boolean
is_external_organization: boolean
```

Payload rules:

```text
- Payload must use organization_reference_id, not full business registration or billing data.
- Payload must not include bank account, payment credential, tax-sensitive details or restricted commercial data.
- Payload must not include member list unless explicitly allowed by policy.
- Payload must not imply Customer, Partner, Agent or Service Provider role.
- Payload must not imply Permission, Policy approval or membership.
```

---

# 7. Required References

Required references:

```text
event_id
organization_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
parent_organization_reference_id
created_by_user_reference_id
created_by_identity_reference_id
permission_decision_reference_id
policy_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal organization_reference_id.
- organization_reference_id identifies the created operating context.
- actor_reference_id identifies who/what requested or performed creation.
- created_by_user_reference_id must not be treated as membership unless Organization Service confirms membership.
- permission_decision_reference_id is required only where Organization creation requires permission gate.
- policy_decision_reference_id is required only where policy gate applies.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
OrganizationCreated
```

## 8.2 event_category

```text
DomainEvent
```

## 8.3 event_status

```text
Recorded
Validated
DispatchPending
Dispatched
DispatchFailed
Consumed
Ignored
Archived
DeletedReferenceOnly
```

## 8.4 organization_type

```text
InternalOrganization
ClientOrganization
PartnerOrganization
AgentOrganization
ServiceProviderOrganization
SystemOrganization
ExternalOrganization
Unknown
```

## 8.5 organization_status

```text
Created
Active
PendingVerification
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 source_type

```text
AdminAction
SystemProcess
APIRequest
AIAgentRequest
Migration
ExternalIntegration
OnboardingFlow
Unknown
```

## 8.7 reason_code

```text
OrganizationCreated
AdminCreated
APIRequested
OnboardingCreated
MigrationCreated
SystemGenerated
AIGenerated
Unknown
```

---

# 9. Event Rules

## 9.1 OrganizationCreated Records Operating Context Creation

OrganizationCreated records that an Organization reference exists.

It must not be interpreted as customer creation, partner creation, provider creation, membership creation or permission grant.

## 9.2 OrganizationCreated Does Not Create User Membership

Organization membership is governed by Organization Service membership/link operations.

OrganizationCreated must not imply any User or Identity belongs to it.

## 9.3 OrganizationCreated Does Not Create Customer

Customer Service owns Customer creation.

An Organization may later be referenced by Customer, but CustomerCreated is separate.

## 9.4 OrganizationCreated Does Not Create Partner, Agent or Service Provider

Partner, Agent and Service Provider services own their own objects.

OrganizationCreated must not be used as a substitute for those records.

## 9.5 OrganizationCreated Does Not Grant Permission

Permission must be evaluated by Permission Service.

OrganizationCreated must not imply allowed action.

## 9.6 OrganizationCreated Does Not Pass Policy

Policy must be evaluated by Policy Service.

OrganizationCreated must not imply policy compliance.

## 9.7 OrganizationCreated Must Be Immutable

OrganizationCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
User Service
Identity Service
Permission Service
Policy Service
Customer Service
Partner Service
Agent Service
Service Provider Service
Audit Service
AI Agent Governance
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- User Service may use OrganizationCreated for membership workflow preparation only through governed operation.
- Permission Service may use organization_reference_id for evaluation context.
- Policy Service may use organization_reference_id for contextual constraints.
- Customer, Partner, Agent and Service Provider services may reference Organization only through their own governed operations.
- Audit may preserve Organization creation trace.
- AI Agents may summarize Organization creation only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat OrganizationCreated as User membership
treat OrganizationCreated as Customer/Partner/Agent/Provider creation
treat OrganizationCreated as Permission grant
treat OrganizationCreated as billing setup
expose restricted organization details
```

---

# 11. Relationship to Services

Producing service:

```text
Organization Service produces OrganizationCreated after createOrganization succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches OrganizationCreated.
```

Related services:

```text
User Service may later link User to Organization through separate operation.
Permission Service may evaluate actions within Organization context.
Policy Service may apply contextual constraints.
Customer Service may reference Organization when creating Customer.
Partner Service may reference Organization when creating Partner relationship.
Agent / Service Provider services may reference Organization where applicable.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for organization context trace.
```

Boundary reminders:

```text
Organization Service owns Organization operating context.
Customer Service owns Customer.
Partner Service owns Partner relationship.
Agent Service owns Agent collaborator profile.
Service Provider Service owns provider profile.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /organizations/{organization_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create OrganizationCreated directly.
- API must call Organization Service createOrganization, which emits the event.
- API must not expose restricted business registration, billing, tax or member details.
- API must distinguish OrganizationCreated from CustomerCreated, PartnerCreated, AgentCreated, ServiceProviderCreated and membership events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Organization reference was created
explain that Organization does not equal Customer, Partner, Agent or Service Provider
flag missing membership setup for review
flag missing Customer/Provider/Partner link for review where applicable
prepare audit-safe Organization creation summary
```

AI must not:

```text
fabricate OrganizationCreated
rewrite OrganizationCreated
delete OrganizationCreated
treat OrganizationCreated as permission
create Customer/Partner/Agent/ServiceProvider automatically
create membership automatically
expose restricted organization details
```

AI-originated creation requires:

```text
agent_identity_reference_id
agent_contract_reference_id
authorized_knowledge_reference
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

OrganizationCreated is valid only if:

```text
[ ] event_name is OrganizationCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Organization Service.
[ ] producing operation is createOrganization.
[ ] source_domain is Organization.
[ ] source_object_type is Organization.
[ ] source_object_reference_id is present.
[ ] organization_reference_id is present.
[ ] source_object_reference_id equals organization_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] organization_type is controlled.
[ ] organization_status is controlled.
[ ] payload contains no payment credentials, bank details, tax-sensitive restricted data or member list unless allowed by policy.
[ ] Customer, Partner, Agent, Service Provider, membership and Permission are not implied.
[ ] event is not used as command.
```

---

# 15. Error / Rejection Handling

Controlled rejection reasons:

```text
EventNameInvalid
EventCategoryInvalid
ProducingServiceMissing
ProducingOperationMissing
SourceObjectMissing
OrganizationReferenceMissing
OrganizationReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
OrganizationTypeInvalid
OrganizationStatusInvalid
RestrictedFieldViolation
CommercialDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownEventError
```

Rejection rules:

```text
- Failed Organization creation must not emit OrganizationCreated.
- Duplicate rejected Organization creation must not emit OrganizationCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Organization Service Specification
cite Organization Object Specification
cite Event Service Specification
use exact event_name: OrganizationCreated
use exact event_category: DomainEvent
validate organization_reference_id
validate source_object_reference_id equals organization_reference_id
validate actor_reference_id
validate payload contract
write tests that failed createOrganization does not emit OrganizationCreated
write tests that OrganizationCreated does not create User membership
write tests that OrganizationCreated does not create Customer/Partner/Agent/ServiceProvider automatically
write tests that OrganizationCreated does not grant Permission
write tests that restricted organization/billing/tax/member data is rejected from payload unless allowed
```

Codex must not:

```text
emit OrganizationCreated directly from UI
treat CustomerCreated as OrganizationCreated
treat OrganizationCreated as membership event
create Customer/Partner/Agent/ServiceProvider silently from OrganizationCreated
include restricted billing, tax or member data in payload by default
allow AI to fabricate OrganizationCreated
use OrganizationCreated as command to create membership, Permission or Policy approval
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines OrganizationCreated purpose.
[ ] It defines OrganizationCreated meaning.
[ ] It defines Event category.
[ ] It defines producer and trigger.
[ ] It defines payload contract.
[ ] It defines required references.
[ ] It defines controlled values.
[ ] It defines event rules.
[ ] It defines consumer rules.
[ ] It defines service relationships.
[ ] It defines API relationships.
[ ] It defines AI Agent constraints.
[ ] It defines validation rules.
[ ] It defines error/rejection handling.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial OrganizationCreated Event specification. Defines Organization operating-context creation event and separates OrganizationCreated from Customer, Partner, Agent, Service Provider, membership, Permission and Policy. |

---

**End of Event Specification**
