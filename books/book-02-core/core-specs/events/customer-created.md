# Event Specification — CustomerCreated

**Spec ID:** B02-EVT-CUSTOMER-CREATED  
**Spec Type:** Event  
**Event Name:** CustomerCreated  
**Event File:** core-specs/events/customer-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Customer  
**Producing Service:** core-specs/services/customer-service.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/organization.md; core-specs/objects/user.md; core-specs/objects/brand.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/organization-service.md; core-specs/services/user-service.md; core-specs/services/brand-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/customer-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/customer-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/customer-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

CustomerCreated records that a governed Customer demand-side commercial party reference has been created by Customer Service.

It exists so that Organization, User, Brand, Order, Matter, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a demand-side party now exists without treating that Customer as Organization, User, Partner, Agent, Service Provider, Order, Matter, payment account, ownership proof, authority proof or final business qualification.

CustomerCreated is required before:

```text
customer demand-side party trace
customer-to-organization context review
customer-to-user contact preparation
customer-to-brand linkage
order request preparation
matter context preparation
customer visibility policy enforcement
AI-assisted customer intake review
API customer reference validation
audit trace for customer-sensitive actions
```

---

# 2. Event Meaning

CustomerCreated means:

```text
a stable Customer object reference has been created through governed Customer Service operation.
```

CustomerCreated does not mean:

```text
an Organization was created
a User was created
a contact person was authorized
the Customer owns any Brand or Trademark
an Order has been created
a Matter has been created
payment or billing status has been established
the Customer passed KYC or compliance review
the Customer may access all related records
AI intake suggestion has been accepted as final business fact
```

CustomerCreated records demand-side commercial party creation only.

It does not establish ownership, authorization, billing, compliance approval, Order creation or Matter creation.

---

# 3. Event Category

CustomerCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Customer domain.

It is not an Organization event, User event, Order event, Matter event or Partner event.

---

# 4. Event Producer

Producing service:

```text
Customer Service
```

Producing operation:

```text
createCustomer
```

Source domain:

```text
Customer
```

Source object type:

```text
Customer
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Customer Service createCustomer
        ↓
Event Service record CustomerCreated
```

Producer rules:

```text
- CustomerCreated must be emitted only after Customer Service successfully creates the Customer reference.
- CustomerCreated must not be emitted directly by product UI.
- CustomerCreated must not be emitted directly by AI Agent outside governed service operation.
- CustomerCreated must not be emitted for failed, duplicate-rejected or unauthorized customer creation attempts.
```

---

# 5. Event Trigger

CustomerCreated is triggered when:

```text
Customer Service successfully creates a new Customer object and commits its stable customer_reference_id.
```

Required trigger conditions:

```text
createCustomer operation completed
customer_reference_id created
customer_type validated
customer_status validated
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Organization creation
User creation
contact creation
Brand creation
Order creation
Matter creation
payment setup
KYC/compliance approval
AI customer suggestion
lead/opportunity creation
failed validation
duplicate rejected Customer
```

Related but separate events may include:

```text
OrganizationCreated
UserCreated
BrandCreated
OrderCreated
MatterCreated
OpportunityCreated
CustomerUpdated
CustomerOrganizationLinked
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: CustomerCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Customer
source_service: Customer Service
source_operation: createCustomer
source_object_type: Customer
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/customer-created-payload.md
safe_summary:
  customer_reference_id: string
  customer_type: string
  customer_status: string
  source_type: string
restricted_fields_policy: CustomerCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
customer_reference_id: string
customer_type: string
customer_status: string
customer_source_type: string
linked_organization_reference_id: string | null
primary_contact_user_reference_id: string | null
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references rather than embedding confidential customer details by default.
- Payload must not include payment credentials, tax-sensitive data, identity documents or private contact details unless explicitly allowed.
- Payload must not imply Organization, User, Brand, Order or Matter creation.
- Payload must not imply customer authority, ownership proof, billing status or compliance approval.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
customer_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
linked_organization_reference_id
primary_contact_user_reference_id
brand_reference_id
order_reference_id
matter_reference_id
opportunity_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal customer_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- linked_organization_reference_id must not imply Organization creation unless Organization Service emits OrganizationCreated.
- primary_contact_user_reference_id must not imply contact authority unless separately governed.
- brand_reference_id must not imply ownership unless Brand/Customer linkage is governed separately.
- order_reference_id and matter_reference_id must not imply automatic Order or Matter creation.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
CustomerCreated
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

## 8.4 customer_type

```text
IndividualCustomer
CompanyCustomer
AgencyCustomer
BrandOwnerCustomer
InternalCustomer
ProspectiveCustomer
ExternalCustomer
Unknown
```

## 8.5 customer_status

```text
Draft
Active
ReviewRequired
PendingVerification
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 customer_source_type

```text
ProfessionalInput
CustomerInput
PartnerReferral
OpportunityConversion
OrderIntake
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
CustomerCreated
ProfessionalCreated
CustomerProvided
OpportunityConverted
OrderIntakeCreated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 CustomerCreated Records Demand-Side Party Creation

CustomerCreated records that a Customer reference exists.

It must not be interpreted as Organization creation, User creation, Order creation, Matter creation or payment setup.

## 9.2 Customer Is Not Organization

Organization Service owns operating context.

Customer may reference Organization, but CustomerCreated does not create Organization.

## 9.3 Customer Is Not User or Contact Authority

User Service owns account participants.

A referenced User/contact does not automatically have authority to act for Customer.

## 9.4 Customer Is Not Brand Ownership Proof

Brand ownership or relationship must be governed separately.

CustomerCreated alone does not prove ownership of Brand or Trademark.

## 9.5 CustomerCreated Does Not Create Order or Matter

Order Service owns commercial service request.

Matter Service owns professional execution container.

## 9.6 CustomerCreated Must Respect Permission and Policy

Customer creation and visibility must respect Permission, Policy, confidentiality and organization access context.

## 9.7 CustomerCreated Must Be Immutable

CustomerCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Organization Service
User Service
Brand Service
Order Service
Matter Service
Opportunity Service
Policy Service
Permission Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Organization Service may link Customer to Organization only through governed operation.
- User Service may provide user/contact context but must not infer authority.
- Brand Service may link Customer to Brand only through governed operation.
- Order Service may create Order using Customer context but must do so separately.
- Matter Service may use Customer context after Matter creation.
- AI Agents may assist customer intake only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Customer creation trace.
```

Consumers must not:

```text
treat CustomerCreated as OrganizationCreated
treat CustomerCreated as UserCreated
treat CustomerCreated as OrderCreated
treat CustomerCreated as MatterCreated
treat CustomerCreated as payment/compliance approval
treat CustomerCreated as Brand/Trademark ownership proof
expose restricted customer information
```

---

# 11. Relationship to Services

Producing service:

```text
Customer Service produces CustomerCreated after createCustomer succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches CustomerCreated.
```

Related services:

```text
Organization Service may link Customer to Organization context.
User Service may provide account/contact references.
Brand Service may link Customer and Brand under governed relationship.
Order Service may create commercial service request using Customer context.
Matter Service may later use Customer context in execution.
Opportunity Service may convert Opportunity into Customer.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or use Customer.
Audit Service records accountability trace.
AI Agent Governance controls AI customer intake behavior.
```

Boundary reminders:

```text
Customer Service owns demand-side commercial party.
Organization Service owns operating context.
User Service owns account participant.
Order Service owns commercial request.
Matter Service owns execution container.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /customers/{customer_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create CustomerCreated directly.
- API must call Customer Service createCustomer, which emits the event.
- API must not expose restricted customer details, payment data, tax data or private contact information.
- API must distinguish CustomerCreated from OrganizationCreated, UserCreated, OrderCreated, MatterCreated and Opportunity conversion events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Customer reference was created
explain that Customer is not Organization, User, Order or Matter
flag missing Organization/User/Brand linkage for review
flag customer record requiring verification
prepare audit-safe Customer creation summary
suggest next professional intake step
```

AI must not:

```text
fabricate CustomerCreated
rewrite CustomerCreated
delete CustomerCreated
treat CustomerCreated as payment/compliance approval
treat CustomerCreated as Brand/Trademark ownership proof
treat AI intake suggestion as verified customer fact
hide AI-assisted creation
expose restricted customer or contact information
```

AI-assisted creation requires:

```text
agent_identity_reference_id
agent_contract_reference_id
authorized_knowledge_reference where applicable
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

CustomerCreated is valid only if:

```text
[ ] event_name is CustomerCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Customer Service.
[ ] producing operation is createCustomer.
[ ] source_domain is Customer.
[ ] source_object_type is Customer.
[ ] source_object_reference_id is present.
[ ] customer_reference_id is present.
[ ] source_object_reference_id equals customer_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] customer_type is controlled.
[ ] customer_status is controlled.
[ ] customer_source_type is controlled.
[ ] payload does not include restricted customer, payment, tax or private contact data unless allowed.
[ ] Organization, User, Order, Matter, payment, compliance and ownership proof are not implied.
[ ] AI assistance is explicitly identified where applicable.
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
CustomerReferenceMissing
CustomerReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
CustomerTypeInvalid
CustomerStatusInvalid
CustomerSourceTypeInvalid
RestrictedFieldViolation
ConfidentialCustomerPayloadRejected
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownCustomerEventError
```

Rejection rules:

```text
- Failed Customer creation must not emit CustomerCreated.
- Duplicate rejected Customer creation must not emit CustomerCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Customer Service Specification
cite Customer Object Specification
cite Event Service Specification
cite Organization/User/Brand specs where references are used
use exact event_name: CustomerCreated
use exact event_category: DomainEvent
validate customer_reference_id
validate source_object_reference_id equals customer_reference_id
validate actor_reference_id
validate controlled customer_type/status/source_type
validate payload contract
write tests that failed createCustomer does not emit CustomerCreated
write tests that CustomerCreated does not create Organization or User automatically
write tests that CustomerCreated does not create Order or Matter automatically
write tests that CustomerCreated does not imply payment/compliance approval
write tests that CustomerCreated does not imply Brand/Trademark ownership proof
write tests that AI-assisted creation is marked where applicable
write tests that restricted customer/payment/contact data is not exposed
```

Codex must not:

```text
emit CustomerCreated directly from UI
treat OrganizationCreated as CustomerCreated
treat UserCreated as CustomerCreated
treat OpportunityCreated as CustomerCreated unless Customer Service creates Customer
create Order or Matter silently from CustomerCreated
store raw confidential customer/payment/contact data in event payload by default
allow AI to fabricate CustomerCreated
use CustomerCreated as command to create Organization, User, Brand ownership, Order, Matter or payment setup
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines CustomerCreated purpose.
[ ] It defines CustomerCreated meaning.
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
| 0.1.0 | Draft | Initial CustomerCreated Event specification. Defines governed Customer creation event and separates CustomerCreated from Organization, User, Brand ownership, Order, Matter, payment/compliance approval and AI intake suggestion. |

---

**End of Event Specification**
