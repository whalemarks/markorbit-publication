# Object Specification — Opportunity

**Spec ID:** B02-OBJ-OPPORTUNITY  
**Spec Type:** Object  
**Object Name:** Opportunity  
**Owning Domain:** Opportunity  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/opportunity.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/order.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/opportunity-status.md; core-specs/objects/opportunity-source.md; core-specs/objects/opportunity-scope.md; core-specs/objects/opportunity-qualification.md  
**Related Service Specs:** core-specs/services/opportunity-registration-service.md; core-specs/services/opportunity-qualification-service.md; core-specs/services/opportunity-status-service.md; core-specs/services/opportunity-conversion-service.md; core-specs/services/opportunity-reference-validation-service.md  
**Related Event Specs:** core-specs/events/opportunity-created.md; core-specs/events/opportunity-updated.md; core-specs/events/opportunity-qualified.md; core-specs/events/opportunity-status-changed.md; core-specs/events/opportunity-converted-to-order.md; core-specs/events/opportunity-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/opportunity/opportunity-contract.md; core-specs/contracts/opportunity/opportunity-source-contract.md; core-specs/contracts/opportunity/opportunity-qualification-contract.md; core-specs/contracts/opportunity/opportunity-conversion-contract.md; core-specs/contracts/opportunity/opportunity-order-link-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Opportunity object defines the Core-recognized potential service need before it becomes an Order.

It exists so that Customers, Brands, Trademarks, Jurisdictions, Classifications, Communications, AI Agents, Services, APIs and product consumers can consistently record, qualify, evaluate and convert potential demand without confusing it with Customer, Order, Matter, Task, marketing lead or AI suggestion.

Opportunity is required before:

```text
business lead capture
potential trademark service need tracking
brand protection suggestion
trademark renewal or maintenance opportunity
office action / deadline opportunity
cross-jurisdiction expansion opportunity
customer upsell/cross-sell context
AI opportunity recommendation
opportunity qualification
opportunity-to-order conversion
audit trace for business development actions
```

---

# 2. Core Meaning

Opportunity means:

```text
a Core-recognized potential service need or business possibility that may be qualified, reviewed and converted into an Order.
```

Opportunity is not:

```text
Customer
Order
Matter
Task
Brand
Trademark
Communication
Marketing campaign
AI suggestion by itself
Quote
Invoice
Payment
```

Opportunity answers:

```text
What potential service need exists?
Who or what is the potential customer context?
Which brand, trademark, jurisdiction or service scope may be involved?
Where did the opportunity come from?
Has it been qualified, rejected, deferred or converted?
Which Order did it convert to?
What audit trace is required?
```

---

# 3. Object Category

Opportunity is a Business Execution Object owned by the Opportunity Domain.

It is the potential demand object before Order.

It is Phase 4 Partial Implement, not Phase 3 Must Implement.

Order is the commercial service request.

Matter is the professional execution container.

Opportunity must preserve these boundaries.

---

# 4. Architectural Position

Opportunity sits before Order in the commercial value flow.

```text
Signal or potential need appears
        ↓
Opportunity records potential service need
        ↓
Qualification determines whether it is actionable
        ↓
Customer / scope context is confirmed
        ↓
Order records commercial service request
        ↓
Matter executes professional work
```

Opportunity captures possibility.

Order records accepted service request.

Matter executes work.

---

# 5. Scope

The Opportunity object includes:

```text
opportunity id
opportunity type
opportunity status
opportunity title/reference
opportunity source
customer reference
prospect reference
brand reference
trademark reference
jurisdiction reference
classification reference
service scope reference
qualification reference
score/reference
priority/reference
communication reference
AI recommendation reference
converted order reference
source reference
created time
updated time
audit metadata
```

MVP / Phase 4 partial scope includes:

```text
opportunity id
opportunity type
opportunity status
title/reference
opportunity source
customer/prospect reference
brand reference
trademark reference
jurisdiction reference
service scope reference
qualification status
converted order reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Opportunity ID. |
| opportunity_type | enum | Yes | Yes | Controlled opportunity type. |
| title_reference | string | Yes | Yes | Human-readable opportunity title/reference. |
| status | enum | Yes | Yes | Controlled Opportunity status. |
| source_type | enum | Yes | Yes | Source category. |
| source_reference | string | No | Yes | Intake/import/system/AI/manual source reference. |
| customer_reference_id | string | No | Yes | Existing Customer reference where applicable. |
| prospect_reference | string | No | Partial | Prospect reference before Customer exists. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| jurisdiction_reference_id | string | No | Yes | Related Jurisdiction reference. |
| classification_reference_id | string | No | Partial | Related Classification reference. |
| service_scope_reference | string | No | Yes | Potential service scope reference. |
| qualification_status | enum | Yes | Yes | Controlled qualification state. |
| qualification_reference_id | string | No | Partial | Qualification record reference. |
| priority | enum | No | Partial | Business priority. |
| score_reference | string | No | Deferred | Scoring reference; not scoring engine. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| ai_recommendation_reference_id | string | No | Partial | AI recommendation reference. |
| converted_order_reference_id | string | No | Yes | Order reference after conversion. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 opportunity_type

Phase 4 controlled values:

```text
NewFilingOpportunity
RenewalOpportunity
MaintenanceOpportunity
OfficeActionOpportunity
ExpansionOpportunity
ChangeOpportunity
AssignmentOpportunity
OppositionOpportunity
CancellationOpportunity
EvidenceOpportunity
ConsultationOpportunity
Other
Unknown
```

## 7.2 status

Phase 4 controlled values:

```text
Draft
Identified
ReviewRequired
Qualified
Rejected
Deferred
Converted
Archived
DeletedReferenceOnly
```

## 7.3 source_type

Phase 4 controlled values:

```text
Manual
CustomerInquiry
Communication
TrademarkStatus
DeadlineSignal
BrandAnalysis
AIRecommendation
PartnerReferral
SystemSignal
Import
Unknown
```

## 7.4 qualification_status

Phase 4 controlled values:

```text
Unqualified
ReviewRequired
Qualified
NotQualified
NeedsMoreInformation
Deferred
Converted
```

## 7.5 priority

Suggested controlled values:

```text
Low
Normal
High
Urgent
Unknown
```

---

# 8. Object Rules

## 8.1 Opportunity Requires Type, Title, Source and Status

Every Opportunity must define:

```text
opportunity_type
title_reference
source_type
status
qualification_status
```

A vague note without source and status is not a Core-valid Opportunity.

## 8.2 Opportunity Is Not Customer

Opportunity may reference an existing Customer or prospect context.

It does not create Customer automatically.

Customer creation must use Customer services.

## 8.3 Opportunity Is Not Order

Opportunity is potential demand.

Order is accepted or confirmed service request.

Conversion from Opportunity to Order must be explicit, service-driven and auditable.

## 8.4 Opportunity Is Not Matter

Matter executes professional work.

Opportunity must not open execution workflows directly.

## 8.5 AI Suggestion Is Not Qualified Opportunity

AI may suggest a potential opportunity.

It becomes an Opportunity only through Opportunity Registration Service.

It becomes Qualified only through qualification rules or review.

## 8.6 Opportunity Scoring Is Deferred

Opportunity may contain score references.

Full scoring, forecasting and CRM analytics are deferred.

## 8.7 Opportunity Must Be Auditable

Opportunity-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
opportunity creation
source update
qualification update
status change
customer linkage
brand/trademark linkage
AI recommendation linkage
conversion to order
rejection
deferral
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Opportunity may reference Customer | Customer remains demand-side party. |
| Brand | Opportunity may involve Brand | Brand remains commercial identity. |
| Trademark | Opportunity may involve Trademark | Trademark remains protection object. |
| Jurisdiction | Opportunity may be jurisdiction-scoped | Jurisdiction remains procedural context. |
| Classification | Opportunity may reference Classification | Classification remains goods/services scope. |
| Order | Opportunity may convert to Order | Order remains commercial service request. |
| Matter | Matter may later execute converted Order | Matter remains execution container. |
| Communication | Communication may create/support Opportunity | Communication remains message lifecycle. |
| Notification | Opportunity review may trigger Notification | Notification remains awareness intent. |
| Partner | Partner may refer Opportunity | Partner remains cooperation relationship. |
| AI Output | AI may suggest Opportunity | AI Output is not qualified opportunity. |
| Audit Record | Audit may reference Opportunity | Audit remains accountability system. |

---

# 10. Lifecycle

Opportunity lifecycle states:

```text
Draft
Identified
ReviewRequired
Qualified
Rejected
Deferred
Converted
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Identified
Identified → ReviewRequired
Identified → Qualified
ReviewRequired → Qualified
ReviewRequired → Rejected
ReviewRequired → Deferred
Qualified → Converted
Qualified → Deferred
Qualified → Rejected
Rejected → Archived
Deferred → ReviewRequired
Deferred → Archived
Converted → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Draft → Converted without qualification or explicit conversion service
Rejected → Converted without restoration/review
Archived → Qualified without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Opportunity object is created and managed through:

```text
Opportunity Registration Service
Opportunity Update Service
Opportunity Status Service
Opportunity Qualification Service
Opportunity Source Service
Opportunity Customer Link Service
Opportunity Order Conversion Service
Opportunity Reference Validation Service
Opportunity Audit Reference Service
```

Service rules:

```text
- Services must validate opportunity_type.
- Services must validate source_type.
- Services must validate status and qualification_status.
- Services must emit events for mutating actions.
- Services must not create Customer automatically.
- Services must not create Order except through Opportunity Conversion Service using Order service.
- Services must not create Matter directly.
- AI recommendations must remain source/reference until registered and reviewed.
```

---

# 12. Event Usage

Opportunity object emits or participates in:

```text
OpportunityCreated
OpportunityUpdated
OpportunityStatusChanged
OpportunitySourceUpdated
OpportunityQualified
OpportunityRejected
OpportunityDeferred
OpportunityCustomerLinked
OpportunityBrandLinked
OpportunityTrademarkLinked
OpportunityAIRecommendationLinked
OpportunityConvertedToOrder
OpportunityArchived
OpportunityReferenceValidated
```

Event rules:

```text
- Opportunity events must reference Opportunity ID.
- Conversion events must reference created or linked Order ID.
- AI recommendation events must identify AI source.
- Status events must preserve previous and new status.
- Events must not expose confidential customer or communication details unnecessarily.
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
POST /opportunities/{id}/customer
POST /opportunities/{id}/convert-to-order
POST /opportunities/reference/validate
```

API rules:

```text
- APIs must invoke Opportunity Services.
- APIs must not create Customer automatically.
- APIs must not create Matter directly.
- Conversion to Order must use Opportunity Conversion Service and Order services.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Opportunity only under governed Agent Contracts.

Allowed AI use:

```text
suggest potential opportunities
summarize opportunity context
identify missing customer, brand, trademark or jurisdiction reference
suggest qualification questions
flag likely renewal or maintenance opportunity
draft opportunity note for review
suggest order conversion readiness for review
```

AI must not:

```text
mark Opportunity as Qualified without governed service/review
convert Opportunity to Order without authorized service
create Customer automatically
create Matter directly
make final commercial commitment
invent demand or source facts
send customer communication without Communication service
```

AI Opportunity use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Opportunity Access Rule
Customer Access Rule where applicable
Order Rule where applicable
Communication Rule where applicable
Audit Rule
Human Review Rule for qualification and conversion
```

---

# 15. Validation Rules

Opportunity object must pass:

```text
[ ] id is present and immutable.
[ ] opportunity_type is controlled.
[ ] title_reference is present.
[ ] source_type is controlled.
[ ] status is controlled.
[ ] qualification_status is controlled.
[ ] Opportunity does not equal Customer.
[ ] Opportunity does not equal Order.
[ ] Opportunity does not equal Matter.
[ ] AI suggestion is not Qualified Opportunity automatically.
[ ] Conversion to Order is explicit and auditable.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite opportunity domain spec
preserve Opportunity / Customer boundary
preserve Opportunity / Order boundary
preserve Opportunity / Matter boundary
preserve Opportunity / AI Output boundary
implement only Phase 4 Partial fields unless task says otherwise
write tests for required title_reference
write tests for controlled opportunity_type
write tests for controlled source_type
write tests for controlled status
write tests for controlled qualification_status
write tests preventing Opportunity from creating Customer automatically
write tests preventing Opportunity from creating Matter directly
write tests preventing AI suggestion from becoming Qualified automatically
write tests for explicit conversion to Order
write tests for event emission on mutation
```

Codex must not:

```text
invent full CRM or sales pipeline engine in Phase 4 Partial scope
treat Opportunity as Customer
treat Opportunity as Order
treat Opportunity as Matter
create Customer automatically from Opportunity
create Matter directly from Opportunity
convert AI recommendation into Qualified Opportunity without review
implement scoring/forecasting engine in MVP
allow product UI to redefine Opportunity status
```

---

# 17. Acceptance Criteria

This Opportunity Object Specification is accepted only if:

```text
[ ] It defines Opportunity purpose.
[ ] It defines Opportunity Core meaning.
[ ] It identifies Opportunity as Business Execution Object.
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
| 0.1.0 | Draft | Initial Opportunity object specification. Establishes Opportunity as potential service need before Order, separates Opportunity from Customer, Order, Matter and AI suggestion, and defines Phase 4 Partial fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
