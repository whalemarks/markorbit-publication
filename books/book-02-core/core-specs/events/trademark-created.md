# Event Specification — TrademarkCreated

**Spec ID:** B02-EVT-TRADEMARK-CREATED  
**Spec Type:** Event  
**Event Name:** TrademarkCreated  
**Event File:** core-specs/events/trademark-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Trademark  
**Producing Service:** core-specs/services/trademark-service.md  
**Related Object Specs:** core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/jurisdiction.md; core-specs/objects/classification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/classification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/trademark-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/trademark-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/trademark-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Object Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

TrademarkCreated records that a governed Trademark legal/procedural protection object reference has been created by Trademark Service.

It exists so that Brand, Customer, Jurisdiction, Classification, Document, Evidence, Matter, Order, Workflow, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a trademark protection object now exists without treating it as an official filing, registered right, clearance result, legal conclusion, document, evidence, order, matter or AI-approved filing strategy.

TrademarkCreated is required before:

```text
trademark object trace
brand-to-trademark linkage
jurisdiction and classification planning context
trademark matter/order preparation
document and evidence preparation
AI-assisted trademark analysis
trademark lifecycle initialization
API trademark reference validation
audit trace for trademark-sensitive actions
```

---

# 2. Event Meaning

TrademarkCreated means:

```text
a stable Trademark object reference has been created through governed Trademark Service operation.
```

TrademarkCreated does not mean:

```text
a trademark application has been filed
a trademark right has been registered
the mark is legally available or registrable
the Trademark has official serial/application number
the Trademark has approved goods/services
the Trademark has complete documents
the Trademark has sufficient evidence
a Matter or Order has been created
AI analysis has become final legal conclusion
```

TrademarkCreated records legal/procedural protection object creation only.

It does not establish official filing, legal right, filing readiness, clearance, registrability or professional approval.

---

# 3. Event Category

TrademarkCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Trademark domain.

It is not a Brand event, Matter event, Order event, Document event or Evidence event.

---

# 4. Event Producer

Producing service:

```text
Trademark Service
```

Producing operation:

```text
createTrademark
```

Source domain:

```text
Trademark
```

Source object type:

```text
Trademark
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Trademark Service createTrademark
        ↓
Event Service record TrademarkCreated
```

Producer rules:

```text
- TrademarkCreated must be emitted only after Trademark Service successfully creates the Trademark reference.
- TrademarkCreated must not be emitted directly by product UI.
- TrademarkCreated must not be emitted directly by AI Agent outside governed service operation.
- TrademarkCreated must not be emitted for failed, duplicate-rejected or unauthorized trademark creation attempts.
```

---

# 5. Event Trigger

TrademarkCreated is triggered when:

```text
Trademark Service successfully creates a new Trademark object and commits its stable trademark_reference_id.
```

Required trigger conditions:

```text
createTrademark operation completed
trademark_reference_id created
trademark_type validated
trademark_status validated
brand_reference_id captured where applicable
jurisdiction_reference_id captured where applicable
classification_reference_ids captured where applicable
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Brand creation
Customer creation
Trademark filing submission
official application number receipt
registration issuance
classification suggestion
document upload
evidence registration
AI trademark analysis
clearance search
filing instruction
failed validation
duplicate rejected Trademark
```

Related but separate events may include:

```text
BrandCreated
CustomerCreated
JurisdictionLinked
ClassificationCreated
DocumentCreated
EvidenceCreated
MatterCreated
OrderCreated
TrademarkFiled
TrademarkRegistered
AIAgentRecommendationCreated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: TrademarkCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Trademark
source_service: Trademark Service
source_operation: createTrademark
source_object_type: Trademark
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/trademark-created-payload.md
safe_summary:
  trademark_reference_id: string
  trademark_type: string
  trademark_status: string
  brand_reference_id: string | null
  jurisdiction_reference_id: string | null
  source_type: string
restricted_fields_policy: TrademarkCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
trademark_reference_id: string
trademark_type: string
trademark_status: string
brand_reference_id: string | null
customer_reference_id: string | null
jurisdiction_reference_id: string | null
classification_reference_ids: list[string]
document_reference_ids: list[string]
evidence_reference_ids: list[string]
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
official_application_reference: string | null
```

Payload rules:

```text
- Payload must use references rather than embedding full confidential filing strategy by default.
- Payload may include official_application_reference only if already known and governed.
- Payload must not imply that official filing occurred.
- Payload must not imply registrability, clearance or legal right.
- Payload must not embed raw documents, evidence or trademark images unless explicitly allowed by payload policy.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
trademark_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
brand_reference_id
customer_reference_id
jurisdiction_reference_id
classification_reference_ids
document_reference_ids
evidence_reference_ids
matter_reference_id
order_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal trademark_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- brand_reference_id must not imply Brand ownership or filing approval.
- jurisdiction_reference_id must not imply official filing in that jurisdiction.
- classification_reference_ids must not imply final approved goods/services.
- document_reference_ids and evidence_reference_ids must not imply completeness or sufficiency.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
TrademarkCreated
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

## 8.4 trademark_type

```text
WordMark
DeviceMark
CombinedMark
SeriesMark
CertificationMark
CollectiveMark
SoundMark
ColorMark
ThreeDimensionalMark
Other
Unknown
```

## 8.5 trademark_status

```text
Draft
Planning
ReviewRequired
ReadyForMatter
MatterLinked
Filed
Published
Registered
Refused
Opposed
Cancelled
Expired
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 source_type

```text
ProfessionalInput
CustomerInput
BrandConversion
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
TrademarkCreated
ProfessionalCreated
CustomerProvided
BrandConverted
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 TrademarkCreated Records Trademark Object Creation

TrademarkCreated records that a Trademark reference exists.

It must not be interpreted as official filing, registration, legal right, clearance or filing readiness.

## 9.2 Trademark Is Not Brand

Brand Service owns commercial identity.

Trademark Service owns legal/procedural protection object.

## 9.3 Trademark Is Not Matter or Order

Matter Service owns professional execution container.

Order Service owns commercial service request.

TrademarkCreated does not create Matter or Order automatically.

## 9.4 Trademark Is Not Document or Evidence

Trademark may reference Documents and Evidence.

Document Service and Evidence Service own their own lifecycle and proof purpose.

## 9.5 Classification Reference Is Not Final Filing Scope

Classification Service owns professional goods/services scope.

Classification references must not imply approved filing scope unless separately governed.

## 9.6 AI Trademark Analysis Is Not Final Legal Conclusion

AI may assist in drafting, classification, risk notes or summaries.

AI assistance must not convert analysis into final registrability or filing strategy approval.

## 9.7 TrademarkCreated Must Respect Permission and Policy

Trademark creation and visibility must respect Permission, Policy, confidentiality and customer/matter access context.

## 9.8 TrademarkCreated Must Be Immutable

TrademarkCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Brand Service
Customer Service
Jurisdiction Service
Classification Service
Matter Service
Order Service
Document Service
Evidence Service
Workflow Contract Service
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
- Brand Service may link Brand to Trademark only through governed operation.
- Matter and Order services may use Trademark as context but must create their objects separately.
- Classification Service may refine classification under governed operation.
- Document and Evidence services may link artifacts/proof but must not infer completeness.
- AI Agents may analyze Trademark only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Trademark creation trace.
```

Consumers must not:

```text
treat TrademarkCreated as filing or registration
treat TrademarkCreated as legal availability or registrability conclusion
treat TrademarkCreated as Matter or Order creation
treat TrademarkCreated as final classification approval
treat TrademarkCreated as Document or Evidence sufficiency
expose confidential filing strategy
let AI convert analysis into final filing decision without governed review
```

---

# 11. Relationship to Services

Producing service:

```text
Trademark Service produces TrademarkCreated after createTrademark succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches TrademarkCreated.
```

Related services:

```text
Brand Service may link Trademark to Brand.
Customer Service may link customer context.
Jurisdiction Service provides jurisdiction context.
Classification Service provides goods/services scope context.
Matter Service may create execution container using Trademark context.
Order Service may create commercial request using Trademark context.
Document Service may register related artifacts.
Evidence Service may register proof related to Trademark.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or use Trademark.
Audit Service records accountability trace.
AI Agent Governance controls AI trademark analysis behavior.
```

Boundary reminders:

```text
Trademark Service owns legal/procedural protection object.
Brand Service owns commercial identity.
Matter Service owns execution container.
Order Service owns commercial request.
Document Service owns artifacts.
Evidence Service owns proof layer.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /trademarks/{trademark_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create TrademarkCreated directly.
- API must call Trademark Service createTrademark, which emits the event.
- API must not expose restricted filing strategy, customer data, raw document/evidence content or confidential analysis.
- API must distinguish TrademarkCreated from BrandCreated, MatterCreated, OrderCreated, TrademarkFiled and TrademarkRegistered.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Trademark reference was created
explain that TrademarkCreated is not filing, registration or legal right
flag missing Brand, Jurisdiction or Classification context for review
flag missing Document/Evidence preparation for review
prepare audit-safe Trademark creation summary
suggest next professional review step
```

AI must not:

```text
fabricate TrademarkCreated
rewrite TrademarkCreated
delete TrademarkCreated
treat TrademarkCreated as official filing or registration
treat TrademarkCreated as registrability or clearance conclusion
treat TrademarkCreated as final filing instruction
hide AI-assisted creation
expose restricted filing strategy or customer data
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

TrademarkCreated is valid only if:

```text
[ ] event_name is TrademarkCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Trademark Service.
[ ] producing operation is createTrademark.
[ ] source_domain is Trademark.
[ ] source_object_type is Trademark.
[ ] source_object_reference_id is present.
[ ] trademark_reference_id is present.
[ ] source_object_reference_id equals trademark_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] trademark_type is controlled.
[ ] trademark_status is controlled.
[ ] payload does not include restricted filing strategy, raw document/evidence content or confidential customer data unless allowed.
[ ] official filing, registration, registrability, Matter, Order, Document completeness and Evidence sufficiency are not implied.
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
TrademarkReferenceMissing
TrademarkReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
TrademarkTypeInvalid
TrademarkStatusInvalid
RestrictedFieldViolation
ConfidentialTrademarkPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownTrademarkEventError
```

Rejection rules:

```text
- Failed Trademark creation must not emit TrademarkCreated.
- Duplicate rejected Trademark creation must not emit TrademarkCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Trademark Service Specification
cite Trademark Object Specification
cite Event Service Specification
cite Brand, Jurisdiction and Classification specs where references are used
use exact event_name: TrademarkCreated
use exact event_category: DomainEvent
validate trademark_reference_id
validate source_object_reference_id equals trademark_reference_id
validate actor_reference_id
validate controlled trademark_type/status
validate payload contract
write tests that failed createTrademark does not emit TrademarkCreated
write tests that TrademarkCreated does not create Brand, Matter or Order automatically
write tests that TrademarkCreated does not imply official filing or registration
write tests that TrademarkCreated does not imply registrability or clearance
write tests that TrademarkCreated does not approve Classification, Document or Evidence
write tests that AI-assisted creation is marked where applicable
write tests that restricted filing/customer/document/evidence content is not exposed
```

Codex must not:

```text
emit TrademarkCreated directly from UI
treat BrandCreated as TrademarkCreated
treat TrademarkCreated as filing or registration event
treat TrademarkCreated as legal clearance or registrability approval
create Matter or Order silently from TrademarkCreated
store raw confidential filing strategy or source content in event payload by default
allow AI to fabricate TrademarkCreated
use TrademarkCreated as command to file application, create Document, Evidence, Matter or Order
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines TrademarkCreated purpose.
[ ] It defines TrademarkCreated meaning.
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
| 0.1.0 | Draft | Initial TrademarkCreated Event specification. Defines governed Trademark object creation event and separates TrademarkCreated from Brand, Matter, Order, official filing, registration, classification approval, Evidence sufficiency and legal registrability conclusion. |

---

**End of Event Specification**
