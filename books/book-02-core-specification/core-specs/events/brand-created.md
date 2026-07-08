# Event Specification — BrandCreated

**Spec ID:** B02-EVT-BRAND-CREATED  
**Spec Type:** Event  
**Event Name:** BrandCreated  
**Event File:** core-specs/events/brand-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Brand  
**Producing Service:** core-specs/services/brand-service.md  
**Related Object Specs:** core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/trademark.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/trademark-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/brand-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/brand-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/brand-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Object Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

BrandCreated records that a governed Brand reference has been created by Brand Service.

It exists so that Customer, Trademark, Document, Evidence, Matter, Order, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a commercial identity reference now exists without treating that Brand as a Trademark, Customer, legal right, filing instruction, evidence, document, approved naming decision or final professional conclusion.

BrandCreated is required before:

```text
brand identity trace
customer-to-brand linkage
trademark planning context
brand asset/document linkage
brand evidence preparation
AI-assisted brand analysis
brand portfolio creation
matter/order brand context
API brand reference validation
audit trace for brand-sensitive actions
```

---

# 2. Event Meaning

BrandCreated means:

```text
a stable Brand object reference has been created through governed Brand Service operation.
```

BrandCreated does not mean:

```text
a Trademark has been created
a trademark application should be filed
the Brand is legally registrable
the Brand is available for use or registration
the Brand belongs to a Customer unless linked separately
the Brand has approved logo/name assets
the Brand has Evidence
the Brand has Document
AI recommendation has been accepted as professional truth
```

BrandCreated records commercial identity creation only.

It does not establish legal protection, ownership proof, filing readiness or trademark clearance.

---

# 3. Event Category

BrandCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Brand domain.

It is not a Trademark event, Customer event, Document event or Evidence event.

---

# 4. Event Producer

Producing service:

```text
Brand Service
```

Producing operation:

```text
createBrand
```

Source domain:

```text
Brand
```

Source object type:

```text
Brand
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Brand Service createBrand
        ↓
Event Service record BrandCreated
```

Producer rules:

```text
- BrandCreated must be emitted only after Brand Service successfully creates the Brand reference.
- BrandCreated must not be emitted directly by product UI.
- BrandCreated must not be emitted directly by AI Agent outside governed service operation.
- BrandCreated must not be emitted for failed, duplicate-rejected or unauthorized brand creation attempts.
```

---

# 5. Event Trigger

BrandCreated is triggered when:

```text
Brand Service successfully creates a new Brand object and commits its stable brand_reference_id.
```

Required trigger conditions:

```text
createBrand operation completed
brand_reference_id created
brand_type validated
brand_status validated
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Trademark creation
Customer creation
Document upload
Evidence registration
brand name suggestion
AI brand analysis
trademark search
availability assessment
filing instruction
failed validation
duplicate rejected Brand
```

Related but separate events may include:

```text
CustomerCreated
TrademarkCreated
DocumentCreated
EvidenceCreated
BrandUpdated
BrandCustomerLinked
TrademarkBrandLinked
AIAgentRecommendationCreated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: BrandCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Brand
source_service: Brand Service
source_operation: createBrand
source_object_type: Brand
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/brand-created-payload.md
safe_summary:
  brand_reference_id: string
  brand_type: string
  brand_status: string
  brand_name_reference: string | null
  source_type: string
restricted_fields_policy: BrandCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
brand_reference_id: string
brand_type: string
brand_status: string
brand_name_reference: string | null
customer_reference_id: string | null
document_reference_ids: list[string]
evidence_reference_ids: list[string]
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references rather than embedding full confidential brand strategy by default.
- Payload may include safe brand name reference but must not expose restricted strategy, customer confidential data or raw asset content.
- Payload must not imply Trademark creation or legal registrability.
- Payload must not imply Customer ownership unless Customer linkage is governed separately.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
brand_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
customer_reference_id
trademark_reference_id
document_reference_ids
evidence_reference_ids
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal brand_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- customer_reference_id must not imply ownership unless Customer/Brand linkage is separately governed.
- trademark_reference_id must not be present unless a separate governed linkage exists.
- document_reference_ids and evidence_reference_ids must not imply automatic conversion or approval.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
BrandCreated
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

## 8.4 brand_type

```text
WordBrand
LogoBrand
CombinedBrand
ProductBrand
CompanyBrand
PersonalBrand
SeriesBrand
SubBrand
CampaignBrand
Unknown
```

## 8.5 brand_status

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 source_type

```text
ProfessionalInput
CustomerInput
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
BrandCreated
ProfessionalCreated
CustomerProvided
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 BrandCreated Records Commercial Identity Creation

BrandCreated records that a Brand reference exists.

It must not be interpreted as Trademark creation, legal protection or filing readiness.

## 9.2 Brand Is Not Trademark

Trademark Service owns trademark legal/procedural protection objects.

BrandCreated may be followed by TrademarkCreated, but they are separate events.

## 9.3 Brand Is Not Customer

Customer Service owns the demand-side commercial party.

Brand may link to Customer, but BrandCreated does not create Customer.

## 9.4 Brand Is Not Document or Evidence

Brand may reference Documents or Evidence.

Document Service and Evidence Service own their own lifecycle and proof purpose.

## 9.5 AI Brand Suggestion Is Not Approved Brand Automatically

AI may suggest names, categories or risk notes.

A Brand becomes a governed Brand only through Brand Service creation and applicable review rules.

## 9.6 BrandCreated Must Respect Permission and Policy

Brand creation and visibility must respect Permission, Policy, confidentiality and customer/matter access context.

## 9.7 BrandCreated Must Be Immutable

BrandCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Customer Service
Trademark Service
Matter Service
Order Service
Document Service
Evidence Service
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
- Customer Service may link Customer to Brand only through governed operation.
- Trademark Service may use Brand as planning context but must create Trademark separately.
- Matter and Order services may reference Brand only under governed request context.
- AI Agents may analyze Brand only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Brand creation trace.
```

Consumers must not:

```text
treat BrandCreated as TrademarkCreated
treat BrandCreated as legal registrability conclusion
treat BrandCreated as Customer ownership proof
treat BrandCreated as Document or Evidence approval
expose confidential brand strategy
let AI convert suggestion into final Brand without governed operation
```

---

# 11. Relationship to Services

Producing service:

```text
Brand Service produces BrandCreated after createBrand succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches BrandCreated.
```

Related services:

```text
Customer Service may link Brand to Customer.
Trademark Service may create Trademark based on Brand context.
Document Service may register brand assets as Documents.
Evidence Service may register proof related to Brand.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or use Brand.
Audit Service records accountability trace.
AI Agent Governance controls AI brand analysis behavior.
```

Boundary reminders:

```text
Brand Service owns commercial identity.
Trademark Service owns legal/procedural protection object.
Customer Service owns demand-side party.
Document Service owns artifacts.
Evidence Service owns proof layer.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /brands/{brand_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create BrandCreated directly.
- API must call Brand Service createBrand, which emits the event.
- API must not expose restricted brand strategy, customer data or raw asset content.
- API must distinguish BrandCreated from TrademarkCreated, CustomerCreated, DocumentCreated and EvidenceCreated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Brand reference was created
explain that Brand is not Trademark or legal protection
flag missing Customer linkage for review
flag missing Trademark planning context for review
prepare audit-safe Brand creation summary
suggest next professional review step
```

AI must not:

```text
fabricate BrandCreated
rewrite BrandCreated
delete BrandCreated
treat BrandCreated as legal registrability conclusion
treat BrandCreated as Trademark creation
treat BrandCreated as Customer ownership proof
hide AI-assisted creation
expose restricted brand strategy or customer data
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

BrandCreated is valid only if:

```text
[ ] event_name is BrandCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Brand Service.
[ ] producing operation is createBrand.
[ ] source_domain is Brand.
[ ] source_object_type is Brand.
[ ] source_object_reference_id is present.
[ ] brand_reference_id is present.
[ ] source_object_reference_id equals brand_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] brand_type is controlled.
[ ] brand_status is controlled.
[ ] payload does not include restricted brand strategy, raw asset content or confidential customer data unless allowed.
[ ] Trademark, Customer ownership, Document approval and Evidence sufficiency are not implied.
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
BrandReferenceMissing
BrandReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
BrandTypeInvalid
BrandStatusInvalid
RestrictedFieldViolation
ConfidentialBrandPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownBrandEventError
```

Rejection rules:

```text
- Failed Brand creation must not emit BrandCreated.
- Duplicate rejected Brand creation must not emit BrandCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Brand Service Specification
cite Brand Object Specification
cite Event Service Specification
cite Customer and Trademark specs where references are used
use exact event_name: BrandCreated
use exact event_category: DomainEvent
validate brand_reference_id
validate source_object_reference_id equals brand_reference_id
validate actor_reference_id
validate controlled brand_type/status
validate payload contract
write tests that failed createBrand does not emit BrandCreated
write tests that BrandCreated does not create Trademark automatically
write tests that BrandCreated does not create Customer ownership automatically
write tests that BrandCreated does not approve Document or Evidence
write tests that AI-assisted creation is marked where applicable
write tests that restricted brand/customer/asset content is not exposed
```

Codex must not:

```text
emit BrandCreated directly from UI
treat TrademarkCreated as BrandCreated
treat BrandCreated as legal clearance or registrability approval
create Trademark silently from BrandCreated
create Customer ownership silently from BrandCreated
store raw confidential brand strategy or asset content in event payload by default
allow AI to fabricate BrandCreated
use BrandCreated as command to create Trademark, Document, Evidence or filing instruction
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines BrandCreated purpose.
[ ] It defines BrandCreated meaning.
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
| 0.1.0 | Draft | Initial BrandCreated Event specification. Defines governed Brand creation event and separates BrandCreated from Trademark, Customer ownership, Document, Evidence, AI suggestion and legal registrability conclusion. |

---

**End of Event Specification**
