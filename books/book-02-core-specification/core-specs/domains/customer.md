# Domain Specification — Customer

**Spec ID:** B02-DOM-CUSTOMER  
**Spec Type:** Domain  
**Domain Name:** Customer  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/customer-contact.md; core-specs/objects/customer-organization-reference.md; core-specs/objects/customer-status.md; core-specs/objects/customer-service-context.md; core-specs/objects/customer-brand-relationship.md  
**Related Service Specs:** core-specs/services/customer-registration-service.md; core-specs/services/customer-contact-service.md; core-specs/services/customer-organization-reference-service.md; core-specs/services/customer-status-service.md; core-specs/services/customer-service-context-service.md; core-specs/services/customer-reference-validation-service.md  
**Related Event Specs:** core-specs/events/customer-created.md; core-specs/events/customer-updated.md; core-specs/events/customer-status-changed.md; core-specs/events/customer-contact-linked.md; core-specs/events/customer-organization-linked.md; core-specs/events/customer-brand-linked.md; core-specs/events/customer-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/customer/customer-contract.md; core-specs/contracts/customer/customer-contact-contract.md; core-specs/contracts/customer/customer-organization-reference-contract.md; core-specs/contracts/customer/customer-service-context-contract.md; core-specs/contracts/customer/customer-brand-relationship-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Customer Domain defines the Core meaning of the demand-side commercial party in MarkOrbit.

It exists so that Brands, Trademarks, Orders, Matters, Opportunities, Communications, Documents, Evidence, Workflows, AI Agents and product consumers can consistently refer to the party requesting, purchasing, owning, instructing or benefiting from professional trademark services.

Customer is required before:

```text
order creation
matter opening
client intake
customer contact management
brand-owner reference
trademark applicant reference
service requirement collection
commercial relationship tracking
communication routing
document request handling
evidence request handling
AI intake assistance
opportunity conversion
client-facing portal consumption
```

The Customer Domain is a Business Execution Domain because it represents the business-side demand relationship through which professional services are requested, delivered and managed.

---

# 2. Core Meaning

Customer means:

```text
a Core-recognized demand-side business or individual party that requests, purchases, instructs, owns, uses or benefits from MarkOrbit professional services.
```

Customer is not merely:

```text
a User
an Organization
a Brand owner
a trademark applicant
a contact person
a sales lead
an opportunity
an order
a matter
a billing account
a partner
a service provider
a local agent
```

Customer answers:

```text
Who is the demand-side party for this service relationship?
Which contacts can represent or communicate for this customer?
Which organization or individual reference is associated with the customer?
Which brands, trademarks, orders, matters and documents relate to this customer?
What service context and relationship status apply?
Can this customer be used consistently by sales, operations, AI Agents and product consumers?
```

---

# 3. Domain Category

Customer is a Business Execution Domain.

Business Execution Domains provide the Core basis for:

```text
commercial relationship handling
service intake
order creation
matter execution
communication routing
document and evidence requests
customer-facing product consumption
AI-assisted intake and summary
opportunity conversion
```

Customer connects Professional Core objects to business execution.

It does not define the professional meaning of Brand, Trademark, Document or Evidence.

---

# 4. Architectural Position

Customer sits at the start of the Business Execution Core.

```text
Professional Core defines Brand, Trademark, Jurisdiction, Classification, Document and Evidence
        ↓
Customer defines the demand-side commercial party
        ↓
Opportunity may identify potential service need
        ↓
Order commercializes the requested service
        ↓
Matter executes professional work
        ↓
Workflow, Task, Event and Notification coordinate execution
```

Customer provides commercial relationship context.

Order defines commercial transaction scope.

Matter defines professional execution scope.

Customer does not replace Order or Matter.

---

# 5. Scope

The Customer Domain includes:

```text
customer definition
customer type
customer status
customer contact boundary
customer organization reference
customer individual reference boundary
customer service context
customer brand relationship
customer trademark relationship boundary
customer document request boundary
customer evidence request boundary
customer communication reference boundary
customer intake source reference
customer reference validation
customer audit reference
customer event emission
customer use by AI Agents, Services, Workflows, APIs and Codex tasks
```

MVP implementation should focus on:

```text
Customer
Customer Contact
Customer Organization Reference
Customer Status
Customer Service Context
Customer Brand Relationship
Customer Registration Service
Customer Contact Service
Customer Organization Reference Service
Customer Status Service
Customer Service Context Service
Customer Reference Validation Service
CustomerCreated event
CustomerContactLinked event
CustomerOrganizationLinked event
CustomerBrandLinked event
CustomerReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Customer Domain owns:

```text
Core Customer definition
customer status
customer type
customer contact boundary
customer organization reference
customer individual reference boundary
customer service context
customer relationship to Brand
customer relationship to Trademark
customer reference validation
customer event emission
customer reference used by Orders, Matters, Communications and products
```

## 6.2 Out of Boundary

The Customer Domain does not own:

```text
Identity recognition
User account lifecycle
Organization core meaning
Brand commercial identity
Trademark lifecycle
Order commercial transaction lifecycle
Matter professional execution lifecycle
Opportunity scoring
Partner relationship
Service Provider relationship
local agent relationship
billing/invoice implementation
payment lifecycle
CRM marketing automation
public client portal UI
customer grade pricing policy
```

Those responsibilities belong to:

```text
Identity Domain
User Domain
Organization Domain
Brand Domain
Trademark Domain
Order Domain
Matter Domain
Opportunity Domain
Partner Domain
Service Provider Domain
Agent Domain
Finance/Product implementation
Product implementation
```

## 6.3 Boundary Notes

Customer is the demand-side commercial party.

User is an account.

Organization is an operating or tenant container.

Brand is the commercial identity being protected.

Order is the commercial service transaction.

Matter is the professional execution container.

A Customer may reference an Organization, but Customer does not redefine Organization.

---

# 7. Domain Rules

## 7.1 Customer Must Have Demand-Side Meaning

A Customer must represent a party with demand-side service relevance.

A contact, message sender or user is not automatically a Customer unless registered or linked through a governed service.

## 7.2 Customer Must Preserve Contact Boundary

Customer Contact is a communication or representation contact.

Customer Contact is not the same as User, Identity or Organization.

A Customer Contact may later be linked to a User, but the concepts must remain separate.

## 7.3 Customer Does Not Equal Brand Owner

A Customer may be a brand owner, applicant, authorized agent, buyer or service requester.

Brand Owner Reference and Trademark Owner Reference must not be silently replaced by Customer.

Ownership must be supported by Brand, Trademark, Document or Evidence context where relevant.

## 7.4 Customer Does Not Equal Order

A Customer may have many Orders.

Order defines the commercial service transaction.

Customer defines the party relationship.

## 7.5 Customer Must Be Auditable

Customer-sensitive actions must preserve audit trace.

Audit-sensitive customer actions include:

```text
customer creation
customer status change
contact linking
organization reference linking
brand relationship linking
trademark relationship linking
order creation from customer
matter creation from customer
AI intake summary
communication routing based on customer
customer data merge or archival
```

## 7.6 Customer Must Be Product-Neutral

Products may consume Customer.

Products must not redefine Customer as a product-only contact list, CRM pipeline or portal account.

---

# 8. Primary Objects

The Customer Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Customer | Customer | Must Implement | Core-recognized demand-side commercial party. |
| Customer Contact | Customer / Communication | Must Implement | Contact person, email, phone or communication reference associated with Customer. |
| Customer Organization Reference | Customer / Organization | Must Implement | Organization reference associated with Customer. |
| Customer Individual Reference | Customer / Identity / User | Partial Implement | Individual customer or representative reference. |
| Customer Status | Customer | Must Implement | Controlled status indicating customer relationship usability. |
| Customer Type | Customer | Must Implement | Controlled type of customer relationship. |
| Customer Service Context | Customer | Must Implement | Service-related context, needs or intake background. |
| Customer Brand Relationship | Customer / Brand | Must Implement | Relationship between Customer and Brand. |
| Customer Trademark Relationship | Customer / Trademark | Partial Implement | Relationship between Customer and Trademark. |
| Customer Audit Reference | Customer / Audit | Partial Implement | Audit reference for customer-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Identity Principal | Identity | Customer individual may reference identity where applicable. |
| User | User | Customer portal user may be linked to Customer. |
| Organization | Organization | Customer may reference an Organization. |
| Brand | Brand | Customer may own, use or request service for a Brand. |
| Trademark | Trademark | Customer may be applicant, owner, requester or service beneficiary. |
| Order | Order | Customer may create or be linked to Orders. |
| Matter | Matter | Customer may be linked to Matters. |
| Opportunity | Opportunity | Opportunity may convert into Customer or Order. |
| Communication | Communication | Customer may be communication participant or routing context. |
| Document | Document | Customer may provide or receive Documents. |
| Evidence | Evidence | Customer may provide Evidence. |
| Audit Record | Audit | Audit records customer-sensitive actions. |

---

# 9. Primary Services

The Customer Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Customer Registration Service | Customer | Must Implement | Create a Core Customer record. |
| Customer Update Service | Customer | Must Implement | Update controlled Customer fields. |
| Customer Contact Service | Customer / Communication | Must Implement | Link, update or validate customer contacts. |
| Customer Organization Reference Service | Customer / Organization | Must Implement | Link Customer to Organization reference. |
| Customer Status Service | Customer | Must Implement | Update Customer status through governed rules. |
| Customer Service Context Service | Customer | Must Implement | Create or update service needs and intake context. |
| Customer Brand Relationship Service | Customer / Brand | Must Implement | Link Customer to Brand relationship. |
| Customer Trademark Relationship Service | Customer / Trademark | Partial Implement | Link Customer to Trademark relationship. |
| Customer Reference Validation Service | Customer | Must Implement | Validate Customer references used by other domains. |
| Customer Audit Reference Service | Customer / Audit | Partial Implement | Produce customer audit reference for governed actions. |

Service rules:

```text
- Mutating Customer services must emit events.
- Customer services must not create Orders directly unless through Order service.
- Customer services must not create Matters directly unless through Matter service.
- Customer services must not verify Brand or Trademark ownership by themselves.
- Customer services must preserve contact, organization and service-context audit trace.
```

---

# 10. Primary Events

The Customer Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| CustomerCreated | Customer Registration Service | Must Implement | A Core Customer has been created. |
| CustomerUpdated | Customer Update Service | Must Implement | Controlled Customer fields have changed. |
| CustomerStatusChanged | Customer Status Service | Must Implement | Customer status has changed. |
| CustomerContactLinked | Customer Contact Service | Must Implement | Contact reference has been linked to Customer. |
| CustomerContactUpdated | Customer Contact Service | Partial Implement | Customer contact fields have changed. |
| CustomerOrganizationLinked | Customer Organization Reference Service | Must Implement | Organization reference has been linked to Customer. |
| CustomerServiceContextUpdated | Customer Service Context Service | Must Implement | Customer service context has changed. |
| CustomerBrandLinked | Customer Brand Relationship Service | Must Implement | Brand relationship has been linked to Customer. |
| CustomerTrademarkLinked | Customer Trademark Relationship Service | Partial Implement | Trademark relationship has been linked to Customer. |
| CustomerReferenceValidated | Customer Reference Validation Service | Must Implement | Customer reference has been validated for governed use. |
| CustomerMergeReviewRequired | Customer Update Service | Deferred | Potential customer merge requires review. |

Event rules:

```text
- Customer events must reference Customer.
- Contact events must not expose sensitive contact details unnecessarily.
- Brand and Trademark relationship events must not imply ownership unless supported.
- Customer status events must be auditable.
- Customer relationship events must preserve source and actor context.
```

---

# 11. Primary Contracts

Customer requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Customer Contract | Customer Contract | Must Implement | Defines Customer fields, type, status and reference behavior. |
| Customer Contact Contract | Customer / Communication Contract | Must Implement | Defines customer contact fields, source and allowed use. |
| Customer Organization Reference Contract | Customer / Organization Contract | Must Implement | Defines Customer-to-Organization relationship. |
| Customer Service Context Contract | Customer Contract | Must Implement | Defines service needs, intake context and relationship notes. |
| Customer Brand Relationship Contract | Customer / Brand Contract | Must Implement | Defines relationship between Customer and Brand. |
| Customer Trademark Relationship Contract | Customer / Trademark Contract | Partial Implement | Defines relationship between Customer and Trademark. |
| Customer Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for customer-sensitive actions. |

Contract rules:

```text
- Customer Contract must not define User, Organization or Brand meaning.
- Customer Contact Contract must distinguish contact from User.
- Customer Brand Relationship Contract must distinguish relationship from verified ownership.
- Customer Service Context Contract must not become a product-only CRM note.
```

---

# 12. Relationships to Other Domains

## 12.1 Identity and User

Customer may be represented by a User or Identity, but Customer is not User.

A Customer Contact may later be linked to a User.

## 12.2 Organization

Customer may reference an Organization.

Organization defines operating or tenant context.

Customer defines demand-side business relationship.

## 12.3 Brand

Customer may own, use, manage or request service for a Brand.

Brand owns commercial identity.

Customer does not verify Brand ownership by itself.

## 12.4 Trademark

Customer may be applicant, owner, requester, instructing party or beneficiary for Trademark work.

Trademark owns protection-record meaning.

## 12.5 Order

Order commercializes a service request from or for Customer.

Customer does not define order lifecycle or pricing.

## 12.6 Matter

Matter executes professional work for or related to Customer.

Customer does not define matter lifecycle.

## 12.7 Opportunity

Opportunity may identify a potential customer need and may convert into Customer, Order or Matter.

Customer does not own opportunity scoring.

## 12.8 Communication

Communication may use Customer as participant or routing context.

Customer does not own message lifecycle.

## 12.9 Document and Evidence

Customer may provide or receive Documents and Evidence.

Document and Evidence retain their own meanings.

## 12.10 AI Governance

AI may summarize customer intake or recommend missing information, but must not infer sensitive or unsupported customer facts.

## 12.11 Audit

Audit records should include Customer references for customer-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Customer only under governed Agent Contracts.

Allowed AI use:

```text
summarize customer intake context
identify missing customer contact or organization reference
suggest clarification questions
flag mismatch between Customer, Brand Owner and Trademark Applicant references
prepare draft customer service context
summarize customer-related orders or matters if authorized
support opportunity-to-customer conversion review
```

AI must not:

```text
create Customer without authorized service
infer verified ownership from customer relationship alone
infer sensitive personal attributes
merge customers automatically
assign pricing grade without approved policy
create Order or Matter without governed services
send external customer communication without review where required
expose customer contact details outside authorized scope
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Customer Object Access Rule
Customer Service Access Rule
Customer Event Access Rule
Permission Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for external or high-risk outputs
```

---

# 14. Workflow Usage

Customer participates in business execution workflows.

Customer-sensitive workflows may include:

```text
customer-intake-workflow.md
customer-registration-workflow.md
customer-contact-review-workflow.md
customer-brand-link-workflow.md
customer-to-order-workflow.md
customer-to-matter-workflow.md
opportunity-to-customer-conversion-workflow.md
customer-communication-routing-workflow.md
ai-customer-intake-summary-review-workflow.md
```

Workflow rules:

```text
- Customer workflows must reference Workflow Contracts.
- Customer creation from intake or opportunity should preserve source trace.
- Customer-to-Order creation must use Order services.
- Customer-to-Matter creation must use Matter services.
- AI customer summaries must require review before client-facing or operational use where high-risk.
```

---

# 15. API Usage

Customer APIs expose customer creation, contacts, organization references, service context and relationships through governed services.

Potential MVP APIs:

```text
POST /customers
GET /customers/{id}
PATCH /customers/{id}
POST /customers/{id}/contacts
POST /customers/{id}/organization-references
POST /customers/{id}/service-context
POST /customers/{id}/brand-relationships
POST /customers/reference/validate
```

Potential partial APIs:

```text
POST /customers/{id}/trademark-relationships
POST /customers/{id}/status
GET /customers/{id}/audit-reference
POST /customers/{id}/merge-review
```

API rules:

```text
- APIs must invoke Customer Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not create Order or Matter without corresponding services.
- APIs must not expose confidential customer data without Permission and Policy.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 MVP Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Client Portal
Partner Center
Service Platform
Opportunity Engine baseline
Reporting consumers
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
CRM integrations
Finance products
Customer success products
Advanced analytics
```

Product rule:

```text
Products consume Customer.
Products do not redefine Customer.
```

---

# 17. MVP Scope

Customer is a Phase 3 / Wave 3 Must Implement domain.

MVP includes:

```text
Customer
Customer Contact
Customer Organization Reference
Customer Status
Customer Type
Customer Service Context
Customer Brand Relationship
Customer Registration Service
Customer Update Service
Customer Contact Service
Customer Organization Reference Service
Customer Status Service
Customer Service Context Service
Customer Brand Relationship Service
Customer Reference Validation Service
CustomerCreated event
CustomerUpdated event
CustomerStatusChanged event
CustomerContactLinked event
CustomerOrganizationLinked event
CustomerServiceContextUpdated event
CustomerBrandLinked event
CustomerReferenceValidated event
basic customer metadata validation
source traceability to Brand, Trademark, Order, Matter, Opportunity and Communication systems
```

MVP should support:

```text
basic customer intake
basic contact reference
basic organization reference
basic service context
customer-brand relationship
customer reference for order and matter creation
AI-assisted customer intake summary with human review
```

MVP does not require full CRM automation, billing lifecycle, customer grading policy or customer success platform.

---

# 18. Deferred Scope

Deferred scope includes:

```text
full CRM pipeline
customer grading and pricing policy engine
billing account management
invoice account management
customer success automation
marketing automation
customer segmentation analytics
customer merge automation
external CRM synchronization
public client portal self-service profile management
advanced customer risk scoring
customer lifetime value analytics
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Customer should use stable immutable ID.
Customer Contact should not automatically become User.
Customer Organization Reference should use approved Organization references.
Customer Brand Relationship should distinguish owner, user, requester, agent and unknown roles.
Customer Service Context should preserve intake source and relationship notes.
Customer Status should use controlled values.
Customer data access should respect Permission and Policy.
AI-generated customer summaries should remain draft/recommendation output until reviewed where needed.
```

Suggested Customer Status values:

```text
Draft
Active
Prospective
ReviewRequired
Suspended
Archived
Merged
Superseded
DeletedReferenceOnly
```

MVP controlled Customer Status values:

```text
Draft
Active
Prospective
Archived
```

Suggested Customer Type values:

```text
Individual
Company
Agency
BrandOwner
AuthorizedRepresentative
InternalRelatedParty
Unknown
```

MVP controlled Customer Type values:

```text
Individual
Company
Agency
BrandOwner
AuthorizedRepresentative
Unknown
```

Suggested Customer-Brand Relationship values:

```text
Owner
DeclaredOwner
User
Applicant
AuthorizedRepresentative
Requester
Beneficiary
Unknown
```

MVP controlled relationship values:

```text
DeclaredOwner
User
Applicant
AuthorizedRepresentative
Requester
Unknown
```

Do not treat a Customer Contact as a verified legal owner.

---

# 20. Codex Implementation Notes

Codex may implement Customer only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Customer / User / Organization boundaries
preserve Customer / Brand / Trademark boundaries
preserve Customer / Order / Matter boundaries
implement only MVP scope unless task says otherwise
write tests for customer creation
write tests for contact linking
write tests for organization reference linking
write tests for service context update
write tests for customer-brand relationship
write tests preventing Customer from replacing Brand Owner or Trademark Owner without evidence/source
write tests preventing Customer service from creating Order or Matter directly
```

Codex must not:

```text
invent full CRM pipeline in MVP
invent customer pricing grade policy in Customer
invent billing or invoice lifecycle in Customer
treat Customer Contact as User automatically
treat Customer as verified Brand Owner automatically
create Order or Matter inside Customer services
expose customer contact data without Permission and Policy
allow product UI to redefine Customer meaning
```

---

# 21. Validation Rules

Customer Domain must pass the following checks.

```text
[ ] Customer is classified as Business Execution Domain.
[ ] Customer is counted within the 26 baseline Core Domains.
[ ] Customer does not change the baseline Core Domain Map.
[ ] Customer has MVP Phase 3 / Wave 3 classification.
[ ] Customer has MVP Depth = Must Implement.
[ ] Customer defines Core meaning.
[ ] Customer boundary excludes User and Organization meaning.
[ ] Customer boundary excludes Brand and Trademark meaning.
[ ] Customer boundary excludes Order and Matter lifecycle.
[ ] Customer boundary excludes full CRM, billing and pricing policy.
[ ] Customer owns Customer object.
[ ] Customer defines Customer Contact.
[ ] Customer defines Customer Organization Reference.
[ ] Customer defines Customer Service Context.
[ ] Customer defines Customer Brand Relationship.
[ ] Customer lists primary services.
[ ] Mutating Customer services emit events.
[ ] Customer lists primary events.
[ ] Customer defines contract requirements.
[ ] Customer defines AI Agent usage constraints.
[ ] Customer defines workflow usage constraints.
[ ] Customer defines API usage constraints.
[ ] Customer defines product consumers.
[ ] Customer defines MVP and deferred scope.
[ ] Customer defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Customer into User
turn Customer into Organization
turn Customer into Brand
turn Customer into Trademark Owner
turn Customer into Order
turn Customer into Matter
turn Customer into full CRM
turn Customer into billing account
turn Customer into customer grading policy
treat contact as verified legal representative without source
treat Customer as verified Brand Owner without evidence or official record
allow Customer service to create Order or Matter directly
expose confidential customer data without Permission and Policy
allow product UI to redefine Customer meaning
allow Codex to define new customer architecture
```

---

# 23. Acceptance Criteria

This Customer Domain Specification is accepted only if:

```text
[ ] It defines Customer purpose.
[ ] It defines Customer Core meaning.
[ ] It identifies Customer as Business Execution Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Identity, User, Organization, Brand, Trademark, Order, Matter, Opportunity, Communication, Document, Evidence, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Customer Domain specification. Establishes Customer as Phase 3 Business Execution Domain, defines Customer, Contact, Organization Reference, Service Context, Brand Relationship, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
