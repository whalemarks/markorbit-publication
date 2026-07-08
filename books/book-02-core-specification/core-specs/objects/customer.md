# Object Specification — Customer

**Spec ID:** B02-OBJ-CUSTOMER  
**Spec Type:** Object  
**Object Name:** Customer  
**Owning Domain:** Customer  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/customer.md  
**Related Object Specs:** core-specs/objects/customer-profile.md; core-specs/objects/customer-contact.md; core-specs/objects/customer-status.md; core-specs/objects/customer-organization-reference.md; core-specs/objects/customer-brand-reference.md; core-specs/objects/customer-order-reference.md; core-specs/objects/customer-matter-reference.md  
**Related Service Specs:** core-specs/services/customer-registration-service.md; core-specs/services/customer-profile-service.md; core-specs/services/customer-contact-service.md; core-specs/services/customer-status-service.md; core-specs/services/customer-reference-validation-service.md  
**Related Event Specs:** core-specs/events/customer-created.md; core-specs/events/customer-updated.md; core-specs/events/customer-contact-linked.md; core-specs/events/customer-status-changed.md; core-specs/events/customer-brand-linked.md; core-specs/events/customer-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/customer/customer-contract.md; core-specs/contracts/customer/customer-profile-contract.md; core-specs/contracts/customer/customer-contact-contract.md; core-specs/contracts/customer/customer-brand-reference-contract.md; core-specs/contracts/customer/customer-order-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Customer object defines the Core-recognized demand-side commercial party that requests, owns, receives, pays for or coordinates trademark-related services in MarkOrbit.

It exists so that Orders, Matters, Brands, Trademarks, Communications, Documents, Evidence, Opportunities, Tasks, Notifications, AI Agents, Services, APIs and product consumers can consistently reference the customer relationship without confusing Customer with User, Organization, Brand, Partner, Agent or Service Provider.

Customer is required before:

```text
customer intake
order creation
matter creation
brand ownership/reference
client communication
document request
evidence request
commercial service tracking
opportunity conversion
customer-facing portal access
AI customer context summary
audit trace for customer-sensitive actions
```

---

# 2. Core Meaning

Customer means:

```text
a Core-recognized demand-side commercial party or client relationship that may request, receive, own, coordinate or pay for trademark-related services.
```

Customer is not:

```text
User
Organization
Identity
Brand
Trademark
Order
Matter
Partner
Agent
Service Provider
Contact person only
Billing account only
```

Customer answers:

```text
Who is the demand-side party?
Which contacts represent or communicate for the customer?
Which organization or identity references may be linked?
Which brands, trademarks, orders, matters or opportunities relate to the customer?
What customer status applies?
What communication, document and evidence context belongs to the customer?
What audit trace is required?
```

---

# 3. Object Category

Customer is a Business Execution Object owned by the Customer Domain.

It is the demand-side commercial party object.

It may link to Organization, User, Brand, Order and Matter, but it must not absorb their meanings.

---

# 4. Architectural Position

Customer sits at the entrance of business execution.

```text
Customer expresses demand
        ↓
Brand captures commercial identity
        ↓
Order records commercial service request
        ↓
Matter executes professional work
        ↓
Task coordinates work units
        ↓
Communication, Document and Evidence support execution
```

Customer provides commercial party context.

Order commercializes a service request.

Matter executes work.

Customer does not replace either.

---

# 5. Scope

The Customer object includes:

```text
customer id
customer type
customer status
customer name/reference
customer profile reference
customer contact references
organization reference
identity/user reference boundary
brand references
trademark references
order references
matter references
opportunity references
communication references
document/evidence references
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
customer id
customer type
customer status
name/reference
profile reference
contact references
organization reference
brand references
order references
matter references
communication references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Customer ID. |
| customer_type | enum | Yes | Yes | Individual, Company, AgencyClient, InternalClient, Unknown. |
| name_reference | string | Yes | Yes | Customer display/name reference; not legal proof by itself. |
| status | enum | Yes | Yes | Controlled Customer status. |
| profile_reference_id | string | No | Partial | Customer Profile reference. |
| organization_reference_id | string | No | Yes | Related Organization reference where applicable. |
| primary_contact_reference_id | string | No | Yes | Primary Customer Contact reference. |
| contact_references | array | No | Yes | Customer Contact references. |
| user_reference_ids | array | No | Partial | Linked portal/user references; not automatic. |
| brand_reference_ids | array | No | Yes | Related Brand references. |
| trademark_reference_ids | array | No | Partial | Related Trademark references. |
| order_reference_ids | array | No | Yes | Related Order references. |
| matter_reference_ids | array | No | Yes | Related Matter references. |
| opportunity_reference_ids | array | No | Partial | Related Opportunity references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| source_reference | string | No | Yes | Intake/import/source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 customer_type

MVP controlled values:

```text
Individual
Company
AgencyClient
InternalClient
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
Archived
DeletedReferenceOnly
```

## 7.3 contact_role

Suggested controlled values:

```text
PrimaryContact
LegalContact
BusinessContact
FinanceContact
DocumentContact
EvidenceContact
PortalUser
Other
Unknown
```

---

# 8. Object Rules

## 8.1 Customer Requires Name and Type

Every Customer must define:

```text
name_reference
customer_type
status
```

A Customer without name or type is not Core-valid.

## 8.2 Customer Is Not User

A Customer Contact or portal user may link to User.

But Customer is demand-side commercial relationship, not account participant.

## 8.3 Customer Is Not Organization

A Customer may reference Organization.

But Organization provides operating context; Customer represents demand-side commercial party.

## 8.4 Customer Is Not Brand

Customer may own, request, manage or coordinate Brands.

Brand remains commercial identity.

## 8.5 Customer Contact Is Not Automatically User

A contact person, email or phone number does not automatically become User.

User linkage must be governed by User/Identity services.

## 8.6 Customer Must Be Auditable

Customer-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
customer creation
customer profile update
customer contact linking
customer status change
organization linkage
brand linkage
order linkage
matter linkage
portal user linkage
AI customer summary
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Organization | Customer may reference Organization | Organization remains operating context. |
| User | Customer Contact may link to User | User remains account participant. |
| Identity | Customer actions may reference Identity | Identity remains actor reference. |
| Brand | Customer may own or manage Brand | Brand remains commercial identity. |
| Trademark | Customer may request services for Trademark | Trademark remains protection object. |
| Order | Customer may create or own Orders | Order remains commercial service request. |
| Matter | Customer may have Matters | Matter remains execution container. |
| Opportunity | Opportunity may convert to Customer/Order | Opportunity remains potential service need. |
| Communication | Customer participates in Communication | Communication remains message lifecycle. |
| Document | Customer may provide/request Documents | Document remains artifact. |
| Evidence | Customer may provide/request Evidence | Evidence remains proof layer. |
| Task | Tasks may request Customer input | Task remains work unit. |
| Audit Record | Audit may reference Customer | Audit remains accountability system. |

---

# 10. Lifecycle

Customer lifecycle states:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Active
Draft → ReviewRequired
ReviewRequired → Active
Active → Suspended
Suspended → Active
Active → Inactive
Inactive → Active
Inactive → Archived
Active → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
DeletedReferenceOnly → Active
Archived → Active without restoration service and review
Suspended → Archived without reason/source reference where policy requires it
```

---

# 11. Service Usage

Customer object is created and managed through:

```text
Customer Registration Service
Customer Profile Service
Customer Contact Service
Customer Status Service
Customer Organization Reference Service
Customer Brand Reference Service
Customer Order Reference Service
Customer Matter Reference Service
Customer Reference Validation Service
Customer Audit Reference Service
```

Service rules:

```text
- Services must validate customer_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not create User automatically from Customer Contact.
- Services must not create Brand, Order or Matter directly unless their services are invoked.
- Services must preserve data access and confidentiality policy.
```

---

# 12. Event Usage

Customer object emits or participates in:

```text
CustomerCreated
CustomerUpdated
CustomerStatusChanged
CustomerContactLinked
CustomerContactUpdated
CustomerOrganizationLinked
CustomerBrandLinked
CustomerOrderLinked
CustomerMatterLinked
CustomerArchived
CustomerReferenceValidated
```

Event rules:

```text
- Customer events must reference Customer ID.
- Contact events must not expose sensitive contact details unnecessarily.
- Link events must preserve related object reference.
- Status events must preserve previous and new status.
- AI-generated customer context events must identify AI source where applicable.
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
POST /customers/{id}/brands
POST /customers/{id}/orders
POST /customers/{id}/matters
POST /customers/reference/validate
```

API rules:

```text
- APIs must invoke Customer Services.
- APIs must not create User automatically from contact data.
- APIs must not create Brand, Order or Matter unless their services are invoked.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Customer only under governed Agent Contracts.

Allowed AI use:

```text
summarize customer profile if authorized
identify missing customer contact
identify customer-brand/order/matter linkage gaps
draft customer intake notes
suggest customer status review
summarize customer communication context if authorized
prepare client-facing explanation draft for review
```

AI must not:

```text
create Customer without authorized service
create User from Customer Contact automatically
expose customer confidential data outside authorized scope
treat Customer as Organization or Brand
make final commercial commitment without review
send customer communication without Communication service and review where required
alter customer status without authorized service
```

AI Customer use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Customer Access Rule
Communication Rule where applicable
Audit Rule
Human Review Rule for external communication or commercial commitment
```

---

# 15. Validation Rules

Customer object must pass:

```text
[ ] id is present and immutable.
[ ] customer_type is controlled.
[ ] name_reference is present.
[ ] status is controlled.
[ ] Customer does not equal User.
[ ] Customer does not equal Organization.
[ ] Customer does not equal Brand.
[ ] Customer Contact does not become User automatically.
[ ] Links to Brand, Order and Matter use valid references.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite customer domain spec
preserve Customer / User boundary
preserve Customer / Organization boundary
preserve Customer / Brand boundary
preserve Customer / Order / Matter boundaries
implement only MVP fields unless task says otherwise
write tests for required name_reference
write tests for controlled customer_type
write tests for controlled status
write tests preventing Customer Contact from becoming User automatically
write tests preventing Customer from becoming Organization
write tests preventing Customer from creating Brand/Order/Matter directly
write tests for event emission on mutation
```

Codex must not:

```text
invent full CRM in MVP
treat Customer as User account
treat Customer as Organization tenant
treat Customer Contact as User automatically
create Order, Matter or Brand directly from Customer service
store sensitive customer data by default
allow product UI to redefine Customer status
```

---

# 17. Acceptance Criteria

This Customer Object Specification is accepted only if:

```text
[ ] It defines Customer purpose.
[ ] It defines Customer Core meaning.
[ ] It identifies Customer as Business Execution Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Customer object specification. Establishes Customer as demand-side commercial party, separates Customer from User, Organization, Brand, Order and Matter, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
