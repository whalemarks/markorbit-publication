# Object Specification — Order

**Spec ID:** B02-OBJ-ORDER  
**Spec Type:** Object  
**Object Name:** Order  
**Owning Domain:** Order  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/order.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/opportunity.md; core-specs/objects/order-line.md; core-specs/objects/order-status.md; core-specs/objects/order-scope.md; core-specs/objects/order-commercial-reference.md  
**Related Service Specs:** core-specs/services/order-registration-service.md; core-specs/services/order-status-service.md; core-specs/services/order-scope-service.md; core-specs/services/order-line-service.md; core-specs/services/order-matter-link-service.md; core-specs/services/order-reference-validation-service.md  
**Related Event Specs:** core-specs/events/order-created.md; core-specs/events/order-updated.md; core-specs/events/order-status-changed.md; core-specs/events/order-line-added.md; core-specs/events/order-matter-linked.md; core-specs/events/order-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/order/order-contract.md; core-specs/contracts/order/order-line-contract.md; core-specs/contracts/order/order-scope-contract.md; core-specs/contracts/order/order-status-contract.md; core-specs/contracts/order/order-matter-link-contract.md; core-specs/contracts/order/order-commercial-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Order object defines the Core-recognized commercial service request in MarkOrbit.

It exists so that Customers, Opportunities, Brands, Trademarks, Jurisdictions, Classifications, Matters, Tasks, Documents, Evidence, Notifications, Communications, AI Agents, Services, APIs and product consumers can consistently reference a customer-approved or internally accepted service request without confusing it with professional execution, task work, payment, invoice, matter lifecycle or product checkout.

Order is required before:

```text
commercial service request tracking
customer service confirmation
service scope recording
trademark filing request
renewal/change/assignment request
office action response request
matter creation
order-to-matter conversion
commercial status tracking
client-facing progress visibility
AI order summary
audit trace for commercial commitment
```

---

# 2. Core Meaning

Order means:

```text
a Core-recognized commercial service request that records the customer, requested service scope, order lines, commercial references, status and relationship to professional execution containers.
```

Order is not:

```text
Matter
Task
Workflow Contract
Invoice
Payment
Receipt
Quote
Opportunity
Customer
Trademark
Product checkout only
AI Output
```

Order answers:

```text
What service has been requested or accepted?
Who is the customer?
Which brand, trademark, jurisdiction, classification or service scope applies?
Which order lines are included?
Which commercial reference applies?
Which Matter or Matters execute the work?
What order status applies?
What audit trace is required?
```

---

# 3. Object Category

Order is a Business Execution Object owned by the Order Domain.

It is the commercial service request object.

Matter is the professional execution container.

Task is the actionable work unit.

Opportunity is potential demand before order.

Order must preserve these boundaries.

---

# 4. Architectural Position

Order sits between demand qualification and professional execution.

```text
Opportunity identifies potential need
        ↓
Customer confirms demand
        ↓
Order records commercial service request
        ↓
Matter executes professional work
        ↓
Task coordinates work units
        ↓
Document / Evidence / Communication support execution
```

Order records commercial commitment or request.

It does not execute professional work.

It does not own payment or invoice lifecycle.

---

# 5. Scope

The Order object includes:

```text
order id
order type
order status
order title/reference
customer reference
opportunity reference
brand reference
trademark reference
jurisdiction reference
classification reference
order line references
commercial reference
pricing reference boundary
payment reference boundary
matter references
document references
communication references
notification references
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
order id
order type
order status
title/reference
customer reference
opportunity reference
brand reference
trademark reference
jurisdiction reference
classification reference
order line references
commercial reference
matter references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Order ID. |
| order_type | enum | Yes | Yes | Controlled order type. |
| title_reference | string | Yes | Yes | Human-readable order title/reference. |
| status | enum | Yes | Yes | Controlled Order status. |
| customer_reference_id | string | Yes | Yes | Related Customer reference. |
| opportunity_reference_id | string | No | Partial | Related Opportunity reference. |
| brand_reference_id | string | No | Yes | Related Brand reference. |
| trademark_reference_id | string | No | Yes | Related Trademark reference. |
| jurisdiction_reference_id | string | No | Yes | Related Jurisdiction reference. |
| classification_reference_ids | array | No | Yes | Related Classification references. |
| order_line_references | array | No | Yes | Order Line references. |
| commercial_reference_id | string | No | Yes | Quote/fee/term reference boundary. |
| pricing_reference_id | string | No | Partial | Pricing reference; not pricing engine. |
| payment_reference_id | string | No | Deferred | Payment reference; not payment lifecycle. |
| invoice_reference_id | string | No | Deferred | Invoice reference; not invoice lifecycle. |
| matter_reference_ids | array | No | Yes | Related Matter references. |
| document_reference_ids | array | No | Partial | Related Document references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| notification_reference_ids | array | No | Partial | Related Notification references. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 order_type

MVP controlled values:

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
EvidenceReview
DocumentReview
GeneralConsultation
Bundle
Other
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
PendingConfirmation
Confirmed
ReadyForMatter
MatterCreated
InProgress
WaitingForCustomer
Completed
Cancelled
Archived
DeletedReferenceOnly
```

## 7.3 commercial_reference_type

Suggested controlled values:

```text
Quote
FeeSchedule
ManualPrice
DiscountReference
PackageReference
PaymentTermReference
ServiceTermReference
Unknown
```

Commercial reference does not own finance lifecycle.

---

# 8. Object Rules

## 8.1 Order Requires Customer

Every Order must reference a Customer.

A service request without Customer context is not a Core-valid Order.

## 8.2 Order Requires Type, Title and Status

Every Order must define:

```text
order_type
title_reference
status
```

## 8.3 Order Is Not Matter

Order records commercial service request.

Matter executes professional work.

One Order may create one or many Matters.

One Matter may reference an Order.

## 8.4 Order Does Not Own Payment or Invoice Lifecycle

Order may reference pricing, payment or invoice objects.

But Order must not implement payment, receipt, invoice, settlement or accounting lifecycle.

## 8.5 Order Is Not Opportunity

Opportunity is potential demand.

Order is accepted or confirmed service request.

Conversion from Opportunity to Order must be explicit and auditable.

## 8.6 Order Does Not Execute Tasks

Tasks are created and executed through Task and Matter services.

Order may request work, but does not own task execution.

## 8.7 Order Must Be Auditable

Order-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
order creation
customer linkage
scope update
order line update
commercial reference update
status change
opportunity conversion
matter linkage
order cancellation
order completion
AI order summary or recommendation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Order must reference Customer | Customer remains demand-side party. |
| Opportunity | Opportunity may convert to Order | Opportunity remains potential demand. |
| Brand | Order may request service for Brand | Brand remains commercial identity. |
| Trademark | Order may request service for Trademark | Trademark remains protection object. |
| Jurisdiction | Order may be jurisdiction-scoped | Jurisdiction remains procedural context. |
| Classification | Order may include class/goods scope | Classification remains goods/services scope. |
| Matter | Order may create/link Matters | Matter remains execution container. |
| Task | Tasks may support Order through Matter | Task remains actionable work unit. |
| Document | Order may require Documents | Document remains artifact. |
| Evidence | Order may require Evidence | Evidence remains proof layer. |
| Communication | Order may have Communications | Communication remains message lifecycle. |
| Notification | Order may trigger Notifications | Notification remains awareness intent. |
| Business Responsibility | Order may assign commercial owner | Responsibility remains accountability system. |
| Audit Record | Audit may reference Order | Audit remains accountability system. |

---

# 10. Lifecycle

Order lifecycle states:

```text
Draft
PendingConfirmation
Confirmed
ReadyForMatter
MatterCreated
InProgress
WaitingForCustomer
Completed
Cancelled
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → PendingConfirmation
Draft → Confirmed
PendingConfirmation → Confirmed
Confirmed → ReadyForMatter
ReadyForMatter → MatterCreated
MatterCreated → InProgress
InProgress → WaitingForCustomer
WaitingForCustomer → InProgress
InProgress → Completed
Draft → Cancelled
PendingConfirmation → Cancelled
Confirmed → Cancelled
Completed → Archived
Cancelled → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Draft → Completed without confirmation and execution trace
Cancelled → InProgress without restoration/reopen service
Archived → InProgress without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Order object is created and managed through:

```text
Order Registration Service
Order Update Service
Order Status Service
Order Scope Service
Order Line Service
Order Commercial Reference Service
Order Matter Link Service
Order Opportunity Conversion Service
Order Reference Validation Service
Order Audit Reference Service
```

Service rules:

```text
- Services must validate order_type.
- Services must validate customer reference.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not mutate payment, invoice or settlement lifecycle.
- Services must not create Matter unless Matter service is invoked.
- Services must not execute Task directly.
```

---

# 12. Event Usage

Order object emits or participates in:

```text
OrderCreated
OrderUpdated
OrderStatusChanged
OrderScopeUpdated
OrderLineAdded
OrderLineUpdated
OrderLineRemoved
OrderCommercialReferenceUpdated
OrderOpportunityConverted
OrderMatterLinked
OrderCancelled
OrderCompleted
OrderArchived
OrderReferenceValidated
```

Event rules:

```text
- Order events must reference Order ID.
- Status events must preserve previous and new status.
- Commercial reference events must not imply payment completion.
- Matter link events must reference Matter ID.
- Opportunity conversion events must preserve source Opportunity reference.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /orders
GET /orders/{id}
PATCH /orders/{id}
POST /orders/{id}/status
POST /orders/{id}/lines
PATCH /orders/{id}/lines/{lineId}
DELETE /orders/{id}/lines/{lineId}
POST /orders/{id}/matters
POST /orders/reference/validate
```

API rules:

```text
- APIs must invoke Order Services.
- APIs must not mutate payment or invoice lifecycle.
- APIs must not create Matter unless Matter service is invoked.
- APIs must not execute Task directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Order only under governed Agent Contracts.

Allowed AI use:

```text
summarize order scope
identify missing customer, brand, trademark or jurisdiction reference
suggest order line draft for review
detect order/matter mismatch
prepare client-facing order explanation draft
flag missing commercial reference
suggest matter creation readiness for review
```

AI must not:

```text
confirm Order without authorized service
change commercial commitment without review
create payment or invoice lifecycle
create Matter directly without governed service
execute Task directly
make final pricing commitment without review
send external order communication without Communication service
```

AI Order use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Order Access Rule
Customer Access Rule
Matter Rule where applicable
Communication Rule where applicable
Audit Rule
Human Review Rule for commercial commitment
```

---

# 15. Validation Rules

Order object must pass:

```text
[ ] id is present and immutable.
[ ] customer_reference_id is present.
[ ] order_type is controlled.
[ ] title_reference is present.
[ ] status is controlled.
[ ] Order does not equal Matter.
[ ] Order does not equal Opportunity.
[ ] Order does not own payment or invoice lifecycle.
[ ] Order does not execute Tasks.
[ ] Matter links reference valid Matter objects.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite order domain spec
preserve Order / Matter boundary
preserve Order / Task boundary
preserve Order / Opportunity boundary
preserve Order / Finance boundary
implement only MVP fields unless task says otherwise
write tests for required customer_reference_id
write tests for required title_reference
write tests for controlled order_type
write tests for controlled status
write tests preventing Order from mutating payment/invoice lifecycle
write tests preventing Order from executing Task directly
write tests preventing Order from creating Matter without Matter service
write tests for event emission on mutation
```

Codex must not:

```text
invent full ecommerce checkout system inside Order object
invent payment, invoice or settlement lifecycle inside Order
treat Order as Matter
treat Order as Task
confirm commercial commitment by AI without review
create Matter directly from Order object without Matter service
allow product UI to redefine Order status
```

---

# 17. Acceptance Criteria

This Order Object Specification is accepted only if:

```text
[ ] It defines Order purpose.
[ ] It defines Order Core meaning.
[ ] It identifies Order as Business Execution Object.
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
| 0.1.0 | Draft | Initial Order object specification. Establishes Order as commercial service request, separates Order from Matter, Task, Opportunity and Finance lifecycle, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
