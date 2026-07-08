# Service Specification — Opportunity Service

**Spec ID:** B02-SVC-OPPORTUNITY-SERVICE  
**Spec Type:** Service  
**Service Name:** Opportunity Service  
**Owning Domain:** Opportunity  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/opportunity.md  
**Related Object Specs:** core-specs/objects/opportunity.md; core-specs/objects/customer.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/knowledge.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/knowledge-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/opportunity-created.md; core-specs/events/opportunity-updated.md; core-specs/events/opportunity-status-changed.md; core-specs/events/opportunity-qualified.md; core-specs/events/opportunity-customer-linked.md; core-specs/events/opportunity-order-converted.md; core-specs/events/opportunity-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/opportunity/opportunity-contract.md; core-specs/contracts/opportunity/opportunity-reference-contract.md; core-specs/contracts/opportunity/opportunity-qualification-contract.md; core-specs/contracts/opportunity/opportunity-customer-link-contract.md; core-specs/contracts/opportunity/opportunity-order-conversion-contract.md; core-specs/contracts/opportunity/opportunity-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Network and Growth Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Opportunity Service defines the Core service boundary for creating, updating, validating, qualifying, linking and converting Opportunity objects.

It exists so that Customer, Brand, Trademark, Order, Communication, Knowledge, AI Agents, APIs and product consumers can consistently reference potential service needs without confusing Opportunity with Customer, Order, Matter, marketing lead, AI suggestion, sales campaign or confirmed commercial commitment.

Opportunity Service is required before:

```text
potential demand intake
lead-to-opportunity normalization
opportunity qualification
customer opportunity linkage
brand/trademark service need discovery
AI-assisted opportunity discovery
communication-to-opportunity linkage
opportunity-to-order conversion
sales pipeline boundary governance
audit trace for opportunity-sensitive actions
```

---

# 2. Core Meaning

Opportunity Service means:

```text
the Core service that manages potential service needs and their governed relationships to customers, brands, trademarks, communications, qualification state and order conversion.
```

Opportunity Service does not mean:

```text
Customer Service
Order Service
Matter Service
marketing automation system
advertising campaign system
AI lead generator by itself
confirmed commercial commitment
professional execution container
```

Opportunity Service answers:

```text
Does this Opportunity exist?
What potential service need is represented?
Which Customer, Brand or Trademark may be related?
What qualification status applies?
Is the Opportunity ready to convert to Order?
Which Communication, Knowledge or source context supports it?
Can another domain safely reference this Opportunity?
What audit trace is required?
```

---

# 3. Service Category

Opportunity Service is a Business Execution Core Service.

It manages potential demand.

It does not own confirmed commercial request.

It does not execute professional work.

It does not treat AI suggestions as qualified opportunities automatically.

---

# 4. Architectural Position

Opportunity Service sits before Customer/Order execution.

```text
Communication / Intake / AI / Sales signal appears
        ↓
Opportunity Service records potential service need
        ↓
Qualification determines whether demand is actionable
        ↓
Customer Service links demand-side party
        ↓
Order Service records confirmed commercial service request
        ↓
Matter Service executes professional work
```

Opportunity is potential need.

Order is commercial request.

Matter is execution container.

---

# 5. Scope

Opportunity Service includes:

```text
opportunity creation
opportunity update
opportunity status management
opportunity qualification
opportunity customer linkage
opportunity brand/trademark linkage
opportunity communication/source linkage
opportunity order conversion reference
opportunity reference validation
opportunity audit trace
opportunity event emission
```

MVP/Phase 4 scope includes:

```text
create opportunity
get opportunity
update opportunity metadata
change opportunity status
qualify opportunity
link opportunity to customer
link opportunity to brand/trademark
link opportunity to communication/source
convert opportunity to order by approved service call
validate opportunity reference
emit opportunity events
```

Deferred scope includes:

```text
full CRM pipeline
marketing automation
campaign attribution engine
lead scoring model
sales forecasting
automatic order creation without review
advanced revenue analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createOpportunity | Create Opportunity object | Yes | OpportunityCreated |
| getOpportunity | Retrieve Opportunity by ID | Yes | No |
| updateOpportunity | Update governed metadata | Yes | OpportunityUpdated |
| changeOpportunityStatus | Change Opportunity lifecycle status | Yes | OpportunityStatusChanged |
| qualifyOpportunity | Record qualification result | Yes | OpportunityQualified |
| disqualifyOpportunity | Record disqualification result | Partial | OpportunityDisqualified |
| linkOpportunityCustomer | Link Opportunity to Customer | Yes | OpportunityCustomerLinked |
| linkOpportunityBrand | Link Opportunity to Brand | Yes | OpportunityBrandLinked |
| linkOpportunityTrademark | Link Opportunity to Trademark | Partial | OpportunityTrademarkLinked |
| linkOpportunityCommunication | Link Opportunity to Communication | Partial | OpportunityCommunicationLinked |
| convertOpportunityToOrder | Convert to Order through approved Order Service call | Partial | OpportunityOrderConverted |
| validateOpportunityReference | Validate whether Opportunity can be referenced | Yes | OpportunityReferenceValidated |
| archiveOpportunity | Archive Opportunity reference | Partial | OpportunityArchived |

---

# 7. Inputs

Opportunity Service accepts:

```text
opportunity_type
opportunity_title_reference
status
qualification_status
customer_reference_id
brand_reference_id
trademark_reference_id
communication_reference_id
source_reference
service_need_reference
recommended_service_scope
order_reference_id
confidence_reference
metadata
actor_context
request_context
```

Required for creation:

```text
opportunity_type
opportunity_title_reference
status
source_reference
actor_context
```

Required for qualification:

```text
opportunity_reference_id
qualification_status
qualification_reason_reference
actor_context
```

Required for customer linkage:

```text
opportunity_reference_id
customer_reference_id
link_type
actor_context
```

Required for conversion:

```text
opportunity_reference_id
customer_reference_id
service_scope_reference
conversion_context
actor_context
```

Required for validation:

```text
opportunity_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Opportunity Service returns:

```text
Opportunity object
Opportunity reference
Opportunity validation result
Opportunity qualification result
Opportunity customer link result
Opportunity order conversion result
Opportunity status result
Opportunity event reference
error result
```

Validation output must include:

```text
is_valid
opportunity_reference_id
opportunity_type
status
qualification_status
customer_reference_hint where applicable
order_reference_hint where applicable
reason_code
policy_hint where applicable
```

Conversion output must include:

```text
converted
opportunity_reference_id
order_reference_id where created
review_required
reason_code
```

Validation output must not expose confidential customer, sales or communication content unnecessarily.

---

# 9. Controlled Values

## 9.1 opportunity_type

```text
TrademarkFilingNeed
TrademarkSearchNeed
RenewalNeed
OfficeActionNeed
ChangeNeed
AssignmentNeed
OppositionNeed
CancellationNeed
MonitoringNeed
ConsultationNeed
CrossSellNeed
GeneralServiceNeed
Unknown
```

## 9.2 status

```text
Draft
New
ReviewRequired
Qualified
Disqualified
Converted
OnHold
Expired
Archived
DeletedReferenceOnly
```

## 9.3 qualification_status

```text
Unqualified
AIProposed
HumanReviewRequired
Qualified
Disqualified
NeedsMoreInformation
ConvertedToOrder
Unknown
```

## 9.4 source_type

```text
ManualIntake
Communication
CustomerRequest
AIRecommendation
Campaign
PartnerReferral
AgentReferral
SystemSignal
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Unqualified
Disqualified
Converted
Expired
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Opportunity Represents Potential Service Need

Opportunity Service manages potential demand.

It must not be treated as confirmed Order or professional Matter.

## 10.2 Opportunity Is Not Customer

Opportunity may link to Customer.

Customer Service owns demand-side commercial party.

## 10.3 Opportunity Is Not Order

Opportunity may convert to Order only through approved Order Service operation or orchestration.

Order Service owns confirmed commercial service request.

## 10.4 Opportunity Is Not Matter

Opportunity must not create or manage professional execution containers.

Matter Service owns execution.

## 10.5 AI Suggestion Is Not Qualified Opportunity

AI may propose potential opportunities.

Qualification must be recorded explicitly and may require human review.

## 10.6 Opportunity Conversion Requires Readiness

Opportunity-to-Order conversion must validate customer reference, service scope, qualification status and policy constraints.

## 10.7 Opportunity Changes Must Be Auditable

Opportunity-sensitive operations must preserve actor, source, request context, qualification reason and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Customer Service | Opportunity may link to Customer | Customer owns demand-side party. |
| Brand Service | Opportunity may reference Brand | Brand owns commercial identity. |
| Trademark Service | Opportunity may reference Trademark | Trademark owns protection object. |
| Order Service | Opportunity may convert to Order | Order owns commercial request. |
| Matter Service | Matter may be created downstream | Matter owns execution container. |
| Communication Service | Opportunity may originate from Communication | Communication owns message lifecycle. |
| Knowledge Service | May support opportunity identification | Knowledge owns governed reference. |
| Policy Service | Controls conversion/visibility | Policy owns contextual constraint. |
| AI Agent Governance | AI may propose Opportunity | Agent Contract governs AI use. |
| Audit Service | Records Opportunity-sensitive action | Audit owns accountability trail. |
| Event Service | Records Opportunity events | Event records occurrence. |

---

# 12. Event Usage

Opportunity Service emits:

```text
OpportunityCreated
OpportunityUpdated
OpportunityStatusChanged
OpportunityQualified
OpportunityDisqualified
OpportunityCustomerLinked
OpportunityBrandLinked
OpportunityTrademarkLinked
OpportunityCommunicationLinked
OpportunityOrderConverted
OpportunityOnHold
OpportunityExpired
OpportunityArchived
OpportunityReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Qualification events must preserve qualification reason where allowed.
- AI-proposed opportunity events must identify AI source.
- Conversion events must reference Order ID where created.
- Events must not expose confidential communication or customer content unnecessarily.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /opportunities
GET /opportunities/{id}
PATCH /opportunities/{id}
POST /opportunities/{id}/status
POST /opportunities/{id}/qualify
POST /opportunities/{id}/disqualify
POST /opportunities/{id}/customers
POST /opportunities/{id}/brands
POST /opportunities/{id}/trademarks
POST /opportunities/{id}/communications
POST /opportunities/{id}/convert-to-order
POST /opportunities/reference/validate
```

API rules:

```text
- APIs must invoke Opportunity Service operations.
- APIs must not create Customer automatically unless Customer Service is invoked.
- APIs must not create Order automatically without approved conversion operation.
- APIs must not create Matter or Task directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Opportunity Service only under governed Agent Contracts.

Allowed AI use:

```text
detect potential service need from authorized communication
summarize opportunity context
suggest opportunity type for review
suggest qualification questions
identify missing customer/brand/trademark link
prepare opportunity qualification note
recommend conversion readiness for human review
```

AI must not:

```text
mark Opportunity as Qualified without governed review where required
convert Opportunity to Order without authorized service
create Customer automatically
create Matter or Task automatically
make final commercial commitment
use confidential communication outside authorized context
inflate opportunity confidence without source
```

AI Opportunity use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Opportunity Access Rule
Communication Access Rule where applicable
Customer Access Rule where applicable
Order Conversion Rule
Audit Rule
Human Review Rule for qualification and commercial commitment
```

---

# 15. Validation Rules

Opportunity Service must enforce:

```text
[ ] opportunity_type is controlled.
[ ] status is controlled.
[ ] qualification_status is controlled.
[ ] createOpportunity requires opportunity_title_reference.
[ ] createOpportunity requires source_reference.
[ ] createOpportunity produces stable immutable Opportunity ID.
[ ] updateOpportunity does not mutate immutable ID.
[ ] changeOpportunityStatus follows allowed lifecycle.
[ ] qualifyOpportunity records qualification status and reason.
[ ] AIProposed does not equal Qualified.
[ ] convertOpportunityToOrder validates customer, service scope, qualification and policy constraints.
[ ] Opportunity Service does not create Matter or Task.
[ ] Opportunity Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Opportunity Service should return controlled errors:

```text
OpportunityNotFound
InvalidOpportunityType
InvalidOpportunityStatus
InvalidQualificationStatus
InvalidOpportunityTransition
OpportunityTitleRequired
SourceReferenceRequired
CustomerNotFound
BrandNotFound
TrademarkNotFound
CommunicationNotFound
OpportunityNotQualified
OpportunityDisqualified
OpportunityAlreadyConverted
ConversionNotAllowed
ServiceScopeRequired
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownOpportunityError
```

Errors must be safe for product display and API consumption.

Sensitive customer, sales or communication content must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite opportunity domain spec
cite opportunity object spec
cite customer and order specs where relevant
preserve Opportunity / Customer boundary
preserve Opportunity / Order boundary
preserve Opportunity / Matter boundary
preserve Opportunity / AI Suggestion boundary
implement only Phase 4 Partial operations unless task says otherwise
write tests for createOpportunity requiring opportunity_title_reference
write tests for createOpportunity requiring source_reference
write tests for controlled opportunity_type
write tests for controlled status and qualification_status
write tests preventing AIProposed from becoming Qualified automatically
write tests preventing Opportunity Service from creating Matter or Task
write tests for conversion requiring approved Order Service path
write tests for event emission on mutation
```

Codex must not:

```text
invent full CRM or marketing automation system in Phase 4
treat Opportunity as Customer
treat Opportunity as Order
treat Opportunity as Matter
convert AI suggestion directly into qualified Opportunity
create Matter or Task directly from Opportunity Service
make final commercial commitment without authorized process
allow product UI to redefine Opportunity status
```

---

# 18. Acceptance Criteria

This Opportunity Service Specification is accepted only if:

```text
[ ] It defines Opportunity Service purpose.
[ ] It defines Opportunity Service Core meaning.
[ ] It identifies Opportunity Service as Business Execution Core Service.
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
| 0.1.0 | Draft | Initial Opportunity Service specification. Establishes Opportunity Service as potential demand service, separates Opportunity from Customer, Order, Matter and AI suggestions, and defines Phase 4 Partial operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
