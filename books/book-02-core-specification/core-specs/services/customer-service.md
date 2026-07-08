# Service Specification — Customer Service

**Spec ID:** B02-SVC-CUSTOMER-SERVICE  
**Spec Type:** Service  
**Service Name:** Customer Service  
**Owning Domain:** Customer  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/customer.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/brand.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/opportunity.md; core-specs/objects/organization.md; core-specs/objects/user.md  
**Related Service Specs:** core-specs/services/brand-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/opportunity-service.md; core-specs/services/organization-service.md; core-specs/services/user-service.md  
**Related Event Specs:** core-specs/events/customer-created.md; core-specs/events/customer-updated.md; core-specs/events/customer-status-changed.md; core-specs/events/customer-brand-linked.md; core-specs/events/customer-contact-linked.md; core-specs/events/customer-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/customer/customer-contract.md; core-specs/contracts/customer/customer-reference-contract.md; core-specs/contracts/customer/customer-brand-link-contract.md; core-specs/contracts/customer/customer-contact-contract.md; core-specs/contracts/customer/customer-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Customer Service defines the Core service boundary for creating, updating, validating, linking and managing Customer objects.

It exists so that Brand, Opportunity, Order, Matter, Communication, Document, Evidence, AI Agents, APIs and product consumers can consistently reference the demand-side commercial party without confusing Customer with User, Organization, Brand, Partner, Agent, Service Provider, Contact or billing account.

Customer Service is required before:

```text
customer intake
customer profile management
customer-to-brand linkage
customer-to-opportunity linkage
customer-to-order linkage
customer-to-matter linkage
customer contact reference handling
business demand-side reference validation
customer communication context
AI-assisted customer intake summary
audit trace for customer-sensitive actions
```

---

# 2. Core Meaning

Customer Service means:

```text
the Core service that manages demand-side commercial party records and their governed relationships to brands, opportunities, orders, matters, contacts and execution context.
```

Customer Service does not mean:

```text
User Service
Organization Service
Brand Service
Partner Service
Agent Service
Service Provider Service
billing account service
CRM system by itself
marketing automation service
```

Customer Service answers:

```text
Does this Customer exist?
Who is the demand-side party?
Which Brands, Opportunities, Orders or Matters are related?
Which contact references are linked?
Is the Customer active, lead, inactive, archived or review-required?
Can another domain safely reference this Customer?
What audit trace is required?
```

---

# 3. Service Category

Customer Service is a Business Execution Core Service.

It manages the demand-side commercial party.

It does not own user login.

It does not define operating context.

It does not represent Partner, Agent or Service Provider.

---

# 4. Architectural Position

Customer Service sits between business demand and professional execution.

```text
Opportunity may identify potential demand
        ↓
Customer Service manages demand-side party
        ↓
Brand Service manages commercial identity
        ↓
Order Service records commercial service request
        ↓
Matter Service executes professional work
        ↓
Communication / Document / Evidence support delivery
```

Customer owns demand-side party context.

Order owns commercial request.

Matter owns execution container.

---

# 5. Scope

Customer Service includes:

```text
customer creation
customer update
customer status management
customer contact linkage
customer brand linkage
customer opportunity linkage
customer order linkage
customer matter linkage
customer organization/user reference linkage
customer reference validation
customer audit trace
customer event emission
```

MVP scope includes:

```text
create customer
get customer
update customer metadata
change customer status
link customer contact reference
link customer to brand
link customer to opportunity
link customer to order
link customer to matter
validate customer reference
emit customer events
```

Deferred scope includes:

```text
full CRM pipeline
customer scoring
billing account management
contract management
marketing automation
customer support ticketing
advanced customer segmentation
external company registry integration
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createCustomer | Create Customer object | Yes | CustomerCreated |
| getCustomer | Retrieve Customer by ID | Yes | No |
| updateCustomer | Update governed metadata | Yes | CustomerUpdated |
| changeCustomerStatus | Change Customer lifecycle status | Yes | CustomerStatusChanged |
| linkCustomerContact | Link contact reference | Yes | CustomerContactLinked |
| unlinkCustomerContact | Remove contact link | Partial | CustomerContactUnlinked |
| linkCustomerBrand | Link Customer to Brand | Yes | CustomerBrandLinked |
| unlinkCustomerBrand | Remove Brand link | Partial | CustomerBrandUnlinked |
| linkCustomerOpportunity | Link Customer to Opportunity | Yes | CustomerOpportunityLinked |
| linkCustomerOrder | Link Customer to Order | Yes | CustomerOrderLinked |
| linkCustomerMatter | Link Customer to Matter | Yes | CustomerMatterLinked |
| validateCustomerReference | Validate whether Customer can be referenced | Yes | CustomerReferenceValidated |
| archiveCustomer | Archive Customer reference | Partial | CustomerArchived |

---

# 7. Inputs

Customer Service accepts:

```text
customer_type
name_reference
status
organization_reference_id
user_reference_ids
contact_references
brand_reference_ids
opportunity_reference_ids
order_reference_ids
matter_reference_ids
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
customer_type
name_reference
status
source_reference
actor_context
```

Required for contact linkage:

```text
customer_reference_id
contact_reference
contact_link_type
actor_context
```

Required for brand linkage:

```text
customer_reference_id
brand_reference_id
link_type
actor_context
```

Required for validation:

```text
customer_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Customer Service returns:

```text
Customer object
Customer reference
Customer validation result
Customer contact link result
Customer brand link result
Customer opportunity/order/matter link result
Customer status result
Customer event reference
error result
```

Validation output must include:

```text
is_valid
customer_reference_id
customer_type
status
reason_code
organization_reference_hint where applicable
brand_reference_hint where applicable
policy_hint where applicable
```

Validation output must not expose unnecessary confidential customer, contact or business data.

---

# 9. Controlled Values

## 9.1 customer_type

```text
Individual
Company
Agency
BrandOwner
Applicant
Assignee
RepresentativeClient
InternalCustomer
Unknown
```

## 9.2 status

```text
Draft
Lead
Active
ReviewRequired
Inactive
Blocked
Archived
DeletedReferenceOnly
```

## 9.3 contact_link_type

```text
PrimaryContact
BillingContact
LegalContact
BrandContact
OrderContact
MatterContact
EmergencyContact
Unknown
```

## 9.4 business_link_type

```text
Owner
Applicant
Requester
Payor
Representative
Beneficiary
InterestedParty
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Inactive
Blocked
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Customer Represents Demand-Side Commercial Party

Customer Service manages the party requesting, owning, benefiting from or commercially associated with services.

## 10.2 Customer Is Not User

Customer contact may become or link to User only through User Service.

A Customer Contact is not automatically a User.

## 10.3 Customer Is Not Organization

Customer may reference Organization context.

Organization Service owns operating context.

## 10.4 Customer Is Not Brand

Customer may own, manage or request services for Brand.

Brand Service owns commercial identity.

## 10.5 Customer Is Not Partner, Agent or Service Provider

Customer belongs to demand side.

Partner, Agent and Service Provider belong to cooperation or supply-side contexts.

## 10.6 Customer Does Not Own Order or Matter Execution

Customer may link to Order and Matter.

Order owns commercial service request.

Matter owns professional execution container.

## 10.7 Customer Changes Must Be Auditable

Customer-sensitive operations must preserve actor, source, request context and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Brand Service | Customer may link to Brand | Brand owns commercial identity. |
| Opportunity Service | Opportunity may link to Customer | Opportunity owns potential demand. |
| Order Service | Order may link to Customer | Order owns commercial request. |
| Matter Service | Matter may link to Customer | Matter owns execution container. |
| Organization Service | Customer may reference Organization | Organization owns operating context. |
| User Service | Customer contact may link to User | User owns account participant. |
| Communication Service | Customer may participate in communication | Communication owns message lifecycle. |
| Document Service | Customer may provide documents | Document owns artifact lifecycle. |
| Evidence Service | Customer may provide evidence | Evidence owns proof layer. |
| AI Agent Governance | AI may summarize/intake | Agent Contract governs AI use. |
| Audit Service | Records Customer-sensitive action | Audit owns accountability trail. |
| Event Service | Records Customer events | Event records occurrence. |

---

# 12. Event Usage

Customer Service emits:

```text
CustomerCreated
CustomerUpdated
CustomerStatusChanged
CustomerContactLinked
CustomerContactUnlinked
CustomerBrandLinked
CustomerBrandUnlinked
CustomerOpportunityLinked
CustomerOrderLinked
CustomerMatterLinked
CustomerArchived
CustomerReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Contact link events must not expose unnecessary personal contact details.
- Brand/Order/Matter link events must reference related IDs.
- Blocked or archived status events should preserve reason code where allowed.
- AI-generated intake or summary events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /customers
GET /customers/{id}
PATCH /customers/{id}
POST /customers/{id}/status
POST /customers/{id}/contacts
DELETE /customers/{id}/contacts/{contactId}
POST /customers/{id}/brands
DELETE /customers/{id}/brands/{brandId}
POST /customers/{id}/opportunities
POST /customers/{id}/orders
POST /customers/{id}/matters
POST /customers/reference/validate
```

API rules:

```text
- APIs must invoke Customer Service operations.
- APIs must not create User automatically from Customer Contact.
- APIs must not create Organization automatically unless Organization Service is invoked.
- APIs must not create Brand/Order/Matter automatically unless respective services are invoked.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Customer Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize customer intake
identify missing customer information
suggest customer type for review
identify customer-brand/order/matter linkage gaps
draft customer onboarding notes
flag Customer/User/Organization boundary mismatch
prepare contact cleanup suggestions for review
```

AI must not:

```text
create Customer without authorized service
create User from Customer Contact automatically
create Organization automatically
treat Customer as Partner, Agent or Service Provider
change Customer status without authorized service
expose confidential customer or contact information
make final commercial/legal representation decision
```

AI Customer use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Customer Access Rule
Contact Data Rule
Brand/Order/Matter Rule where applicable
Audit Rule
Human Review Rule for sensitive customer changes
```

---

# 15. Validation Rules

Customer Service must enforce:

```text
[ ] customer_type is controlled.
[ ] status is controlled.
[ ] createCustomer requires name_reference.
[ ] createCustomer produces stable immutable Customer ID.
[ ] updateCustomer does not mutate immutable ID.
[ ] changeCustomerStatus follows allowed lifecycle.
[ ] linkCustomerBrand references valid Brand.
[ ] linkCustomerOrder references valid Order where implemented.
[ ] linkCustomerMatter references valid Matter where implemented.
[ ] validateCustomerReference rejects missing, blocked, inactive, archived or deleted-reference customers where not allowed.
[ ] Customer Service does not create User automatically.
[ ] Customer Service does not create Organization automatically.
[ ] Customer Service does not create Order/Matter automatically.
[ ] Customer Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Customer Service should return controlled errors:

```text
CustomerNotFound
InvalidCustomerType
InvalidCustomerStatus
InvalidCustomerTransition
InvalidCustomerReference
CustomerNameRequired
InvalidContactReference
BrandNotFound
OrderNotFound
MatterNotFound
OpportunityNotFound
OrganizationNotFound
UserNotFound
CustomerBlocked
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownCustomerError
```

Errors must be safe for product display and API consumption.

Sensitive customer, contact or business information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite customer domain spec
cite customer object spec
cite brand/order/matter specs where relevant
preserve Customer / User boundary
preserve Customer / Organization boundary
preserve Customer / Brand boundary
preserve Customer / Partner / Agent / Service Provider boundaries
preserve Customer / Order / Matter execution boundary
implement only Phase 3 MVP operations unless task says otherwise
write tests for createCustomer requiring name_reference
write tests for controlled customer_type
write tests for controlled status
write tests preventing Customer Contact from becoming User automatically
write tests preventing Customer Service from creating Organization automatically
write tests preventing Customer Service from creating Order/Matter automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full CRM system in Phase 3
treat Customer as User
treat Customer as Organization
treat Customer as Brand
treat Customer as Partner, Agent or Service Provider
create User from contact automatically
create Order or Matter directly from Customer Service
allow AI to expose customer confidential data
allow product UI to redefine Customer status
```

---

# 18. Acceptance Criteria

This Customer Service Specification is accepted only if:

```text
[ ] It defines Customer Service purpose.
[ ] It defines Customer Service Core meaning.
[ ] It identifies Customer Service as Business Execution Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Customer Service specification. Establishes Customer Service as demand-side commercial party service, separates Customer from User, Organization, Brand, Partner, Agent, Service Provider, Order and Matter, and defines Phase 3 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
