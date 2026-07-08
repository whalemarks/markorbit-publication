# Service Specification — Order Service

**Spec ID:** B02-SVC-ORDER-SERVICE  
**Spec Type:** Service  
**Service Name:** Order Service  
**Owning Domain:** Order  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/order.md  
**Related Object Specs:** core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/opportunity.md; core-specs/objects/brand.md; core-specs/objects/trademark.md; core-specs/objects/task.md  
**Related Service Specs:** core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/opportunity-service.md; core-specs/services/brand-service.md; core-specs/services/trademark-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/task-service.md  
**Related Event Specs:** core-specs/events/order-created.md; core-specs/events/order-updated.md; core-specs/events/order-status-changed.md; core-specs/events/order-customer-linked.md; core-specs/events/order-matter-linked.md; core-specs/events/order-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/order/order-contract.md; core-specs/contracts/order/order-reference-contract.md; core-specs/contracts/order/order-customer-link-contract.md; core-specs/contracts/order/order-matter-link-contract.md; core-specs/contracts/order/order-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Order Service defines the Core service boundary for creating, updating, validating, linking and managing Order objects.

It exists so that Customer, Opportunity, Brand, Trademark, Matter, Workflow Contract, Task, Document, Communication, AI Agents, APIs and product consumers can consistently reference commercial service requests without confusing Order with Matter, Task, payment, invoice, pricing engine, workflow execution or professional work itself.

Order Service is required before:

```text
commercial service request creation
opportunity-to-order conversion
customer order intake
brand/trademark service request handling
order-to-matter linkage
order status tracking
service scope reference management
order readiness validation
AI-assisted order intake summary
audit trace for order-sensitive actions
```

---

# 2. Core Meaning

Order Service means:

```text
the Core service that manages commercial service request records and their governed relationships to customers, opportunities, brands, trademarks, matters and execution context.
```

Order Service does not mean:

```text
Matter Service
Task Service
Workflow engine
payment service
invoice service
pricing engine
contract management system
professional execution service
product checkout UI by itself
```

Order Service answers:

```text
Does this Order exist?
Which Customer requested it?
Which Opportunity, Brand or Trademark does it relate to?
What service scope is requested?
What lifecycle status applies?
Has the Order been accepted, cancelled, converted or linked to Matter?
Can another domain safely reference this Order?
What audit trace is required?
```

---

# 3. Service Category

Order Service is a Business Execution Core Service.

It manages commercial service requests.

It does not execute professional work.

It does not own payment, invoice or pricing engines.

It does not replace Matter.

---

# 4. Architectural Position

Order Service sits between business demand and professional execution.

```text
Opportunity identifies potential demand
        ↓
Customer provides demand-side party context
        ↓
Order Service records commercial service request
        ↓
Matter Service creates professional execution container
        ↓
Workflow Contract governs execution structure
        ↓
Task Service manages actionable work units
```

Order is commercial request.

Matter is execution container.

Task is work unit.

Payment and invoice are separate finance systems.

---

# 5. Scope

Order Service includes:

```text
order creation
order update
order status management
order customer linkage
order opportunity linkage
order brand/trademark linkage
order service scope linkage
order matter linkage
order readiness validation
order reference validation
order audit trace
order event emission
```

MVP scope includes:

```text
create order
get order
update order metadata
change order status
link order to customer
link order to opportunity
link order to brand/trademark
link order to matter
validate order reference
validate order readiness
emit order events
```

Deferred scope includes:

```text
payment processing
invoice lifecycle
pricing calculation
discount engine
contract lifecycle management
refund handling
revenue recognition
advanced order analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createOrder | Create Order object | Yes | OrderCreated |
| getOrder | Retrieve Order by ID | Yes | No |
| updateOrder | Update governed metadata | Yes | OrderUpdated |
| changeOrderStatus | Change Order lifecycle status | Yes | OrderStatusChanged |
| linkOrderCustomer | Link Order to Customer | Yes | OrderCustomerLinked |
| linkOrderOpportunity | Link Order to Opportunity | Yes | OrderOpportunityLinked |
| linkOrderBrand | Link Order to Brand | Yes | OrderBrandLinked |
| linkOrderTrademark | Link Order to Trademark | Yes | OrderTrademarkLinked |
| linkOrderMatter | Link Order to Matter | Yes | OrderMatterLinked |
| validateOrderReference | Validate whether Order can be referenced | Yes | OrderReferenceValidated |
| validateOrderReadiness | Validate readiness for Matter creation/execution | Yes | OrderReadinessValidated |
| acceptOrder | Mark Order accepted | Yes | OrderAccepted |
| cancelOrder | Cancel Order | Yes | OrderCancelled |
| archiveOrder | Archive Order reference | Partial | OrderArchived |

---

# 7. Inputs

Order Service accepts:

```text
order_type
order_title_reference
status
customer_reference_id
opportunity_reference_id
brand_reference_id
trademark_reference_id
jurisdiction_reference_id
classification_reference_ids
service_scope_reference
matter_reference_ids
document_reference_ids
communication_reference_ids
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
order_type
order_title_reference
status
customer_reference_id
service_scope_reference
source_reference
actor_context
```

Required for customer linkage:

```text
order_reference_id
customer_reference_id
link_type
actor_context
```

Required for matter linkage:

```text
order_reference_id
matter_reference_id
link_type
actor_context
```

Required for validation:

```text
order_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Order Service returns:

```text
Order object
Order reference
Order validation result
Order readiness result
Order customer link result
Order matter link result
Order status result
Order event reference
error result
```

Validation output must include:

```text
is_valid
order_reference_id
order_type
status
customer_reference_hint where applicable
service_scope_hint where applicable
matter_reference_hint where applicable
reason_code
policy_hint where applicable
```

Readiness output must include:

```text
is_ready
missing_required_references
review_required
recommended_next_action
reason_code
```

Validation output must not expose unnecessary confidential customer, commercial or professional strategy data.

---

# 9. Controlled Values

## 9.1 order_type

```text
TrademarkFilingOrder
TrademarkSearchOrder
OfficeActionResponseOrder
RenewalOrder
ChangeOrder
AssignmentOrder
OppositionOrder
CancellationOrder
MonitoringOrder
ConsultationOrder
DocumentReviewOrder
EvidenceReviewOrder
GeneralServiceOrder
Unknown
```

## 9.2 status

```text
Draft
Submitted
ReviewRequired
Quoted
Accepted
Rejected
Cancelled
ReadyForMatter
MatterCreated
InProgress
Completed
Archived
DeletedReferenceOnly
```

## 9.3 customer_link_type

```text
Requester
Applicant
Owner
Payor
Representative
Beneficiary
InterestedParty
Unknown
```

## 9.4 matter_link_type

```text
PrimaryMatter
SupplementalMatter
RelatedMatter
HistoricalMatter
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Draft
Cancelled
Rejected
Completed
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Order Is Commercial Service Request

Order Service manages commercial service request context.

It must not execute professional work directly.

## 10.2 Order Is Not Matter

Order may be linked to Matter.

Matter Service owns professional execution container.

## 10.3 Order Is Not Task

Order may produce or relate to Tasks through Matter or Workflow.

Task Service owns actionable work units.

## 10.4 Order Does Not Own Payment or Invoice

Order may reference payment or invoice contexts where future finance services exist.

Payment, invoice, refund and pricing engines are out of Order Service scope.

## 10.5 Order Readiness Is Not Matter Creation

Order readiness validation may indicate whether an Order can proceed.

Matter creation must be performed by Matter Service or approved orchestration.

## 10.6 Order Status Must Not Replace Workflow Contract

Order status tracks commercial request lifecycle.

Workflow Contract governs execution transitions.

## 10.7 Order Changes Must Be Auditable

Order-sensitive operations must preserve actor, source, request context, linked object trace and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Customer Service | Order must reference Customer | Customer owns demand-side party. |
| Opportunity Service | Order may originate from Opportunity | Opportunity owns potential demand. |
| Brand Service | Order may reference Brand | Brand owns commercial identity. |
| Trademark Service | Order may reference Trademark | Trademark owns protection object. |
| Jurisdiction Service | Order may reference Jurisdiction | Jurisdiction owns where context. |
| Classification Service | Order may reference Classification | Classification owns goods/services scope. |
| Matter Service | Order may link to Matter | Matter owns execution container. |
| Workflow Contract Service | May guide conversion/execution | Workflow owns allowed structure. |
| Task Service | Task may be created downstream | Task owns work unit. |
| Document Service | Order may link Documents | Document owns artifact lifecycle. |
| Communication Service | Order may link Communications | Communication owns message lifecycle. |
| Event Service | Records Order events | Event records occurrence. |
| Audit Service | Records Order-sensitive action | Audit owns accountability trail. |

---

# 12. Event Usage

Order Service emits:

```text
OrderCreated
OrderUpdated
OrderStatusChanged
OrderCustomerLinked
OrderOpportunityLinked
OrderBrandLinked
OrderTrademarkLinked
OrderMatterLinked
OrderReadinessValidated
OrderAccepted
OrderCancelled
OrderRejected
OrderCompleted
OrderArchived
OrderReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Status events must preserve previous and next status.
- Customer link events must reference Customer ID.
- Matter link events must reference Matter ID.
- Readiness validation events may be emitted where audit requires.
- Events must not expose payment, invoice or confidential commercial details unnecessarily.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /orders
GET /orders/{id}
PATCH /orders/{id}
POST /orders/{id}/status
POST /orders/{id}/customers
POST /orders/{id}/opportunities
POST /orders/{id}/brands
POST /orders/{id}/trademarks
POST /orders/{id}/matters
POST /orders/{id}/readiness/validate
POST /orders/{id}/accept
POST /orders/{id}/cancel
POST /orders/reference/validate
```

API rules:

```text
- APIs must invoke Order Service operations.
- APIs must not process payment or invoice directly.
- APIs must not create Matter automatically unless Matter Service or approved orchestration is invoked.
- APIs must not create Task directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Order Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Order intake
identify missing Order information
suggest Order type for review
validate Order readiness for Matter creation
identify Customer/Brand/Trademark linkage gaps
draft Order review notes
suggest next action for human review
flag Order / Matter boundary mismatch
```

AI must not:

```text
create Order without authorized service
accept, cancel, reject or complete Order without authorized service
process payment or invoice
create Matter automatically
create Task automatically
make final commercial commitment
expose confidential commercial or customer data
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
Brand/Trademark Access Rule where applicable
Audit Rule
Human Review Rule for commercial commitment and status changes
```

---

# 15. Validation Rules

Order Service must enforce:

```text
[ ] order_type is controlled.
[ ] status is controlled.
[ ] createOrder requires order_title_reference.
[ ] createOrder requires customer_reference_id.
[ ] createOrder requires service_scope_reference.
[ ] createOrder produces stable immutable Order ID.
[ ] updateOrder does not mutate immutable ID.
[ ] changeOrderStatus follows allowed lifecycle.
[ ] linkOrderCustomer references valid Customer.
[ ] linkOrderMatter references valid Matter where implemented.
[ ] validateOrderReference rejects missing, cancelled, rejected, archived or deleted-reference orders where not allowed.
[ ] validateOrderReadiness does not create Matter automatically.
[ ] Order Service does not process payment or invoice.
[ ] Order Service does not create Task automatically.
[ ] Order Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Order Service should return controlled errors:

```text
OrderNotFound
InvalidOrderType
InvalidOrderStatus
InvalidOrderTransition
InvalidOrderReference
OrderTitleRequired
CustomerRequired
ServiceScopeRequired
CustomerNotFound
OpportunityNotFound
BrandNotFound
TrademarkNotFound
MatterNotFound
OrderNotReady
OrderCancelled
OrderRejected
OrderCompleted
PaymentOutOfScope
InvoiceOutOfScope
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownOrderError
```

Errors must be safe for product display and API consumption.

Sensitive customer, commercial, payment or professional strategy information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite order domain spec
cite order object spec
cite customer and matter specs where relevant
preserve Order / Matter boundary
preserve Order / Task boundary
preserve Order / Workflow Contract boundary
preserve Order / Payment / Invoice boundaries
implement only Phase 3 MVP operations unless task says otherwise
write tests for createOrder requiring order_title_reference
write tests for createOrder requiring customer_reference_id
write tests for createOrder requiring service_scope_reference
write tests for controlled order_type
write tests for controlled status
write tests preventing Order Service from creating Matter automatically
write tests preventing Order Service from creating Task automatically
write tests preventing payment/invoice logic inside Order Service
write tests for event emission on mutation
```

Codex must not:

```text
invent payment, invoice or pricing engine inside Order Service
treat Order as Matter
treat Order as Task
execute professional work from Order Service
create Matter directly without approved Matter Service/orchestration call
create Task directly from Order Service
allow AI to accept/cancel/complete Order without authorization
allow product UI to redefine Order status
```

---

# 18. Acceptance Criteria

This Order Service Specification is accepted only if:

```text
[ ] It defines Order Service purpose.
[ ] It defines Order Service Core meaning.
[ ] It identifies Order Service as Business Execution Core Service.
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
| 0.1.0 | Draft | Initial Order Service specification. Establishes Order Service as commercial service request service, separates Order from Matter, Task, Workflow Contract, payment, invoice and pricing, and defines Phase 3 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
