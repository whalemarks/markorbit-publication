# Event Specification — ClassificationCreated

**Spec ID:** B02-EVT-CLASSIFICATION-CREATED  
**Spec Type:** Event  
**Event Name:** ClassificationCreated  
**Event File:** core-specs/events/classification-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Classification  
**Producing Service:** core-specs/services/classification-service.md  
**Related Object Specs:** core-specs/objects/classification.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/jurisdiction.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/classification-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/classification-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/classification-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/classification-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Object Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

ClassificationCreated records that a governed Classification reference has been created by Classification Service.

It exists so that Trademark, Brand, Jurisdiction, Matter, Order, Document, Evidence, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a professional goods/services classification scope now exists without treating it as final filing scope, official acceptance, legal registrability, trademark filing instruction, jurisdiction rule compliance or AI-approved professional conclusion.

ClassificationCreated is required before:

```text
goods/services scope trace
trademark classification planning
jurisdiction-specific classification review
filing scope preparation
document requirement planning
evidence requirement planning
AI-assisted class recommendation review
matter/order classification context
API classification reference validation
audit trace for classification-sensitive actions
```

---

# 2. Event Meaning

ClassificationCreated means:

```text
a stable Classification object reference has been created through governed Classification Service operation.
```

ClassificationCreated does not mean:

```text
the classification is final filing scope
the selected class number is sufficient by itself
the goods/services are accepted by any trademark office
the Trademark is ready to file
the Classification is jurisdiction-compliant in all contexts
the Classification has been legally approved
documents or evidence are complete
AI recommendation has been accepted as professional truth
```

ClassificationCreated records professional classification scope creation only.

It does not establish final filing readiness, official acceptance, legal compliance or professional approval.

---

# 3. Event Category

ClassificationCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Classification domain.

It is not a Trademark event, Jurisdiction event, Document event or Evidence event.

---

# 4. Event Producer

Producing service:

```text
Classification Service
```

Producing operation:

```text
createClassification
```

Source domain:

```text
Classification
```

Source object type:

```text
Classification
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Classification Service createClassification
        ↓
Event Service record ClassificationCreated
```

Producer rules:

```text
- ClassificationCreated must be emitted only after Classification Service successfully creates the Classification reference.
- ClassificationCreated must not be emitted directly by product UI.
- ClassificationCreated must not be emitted directly by AI Agent outside governed service operation.
- ClassificationCreated must not be emitted for failed, duplicate-rejected or unauthorized classification creation attempts.
```

---

# 5. Event Trigger

ClassificationCreated is triggered when:

```text
Classification Service successfully creates a new Classification object and commits its stable classification_reference_id.
```

Required trigger conditions:

```text
createClassification operation completed
classification_reference_id created
classification_type validated
classification_status validated
class_system captured
class_number captured where applicable
goods_services_scope captured as governed reference
jurisdiction_reference_id captured where applicable
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Trademark creation
Brand creation
Jurisdiction link
class suggestion
AI classification recommendation
goods/services text draft only
official filing
office acceptance
document upload
evidence registration
failed validation
duplicate rejected Classification
```

Related but separate events may include:

```text
TrademarkCreated
BrandCreated
JurisdictionLinked
DocumentCreated
EvidenceCreated
MatterCreated
OrderCreated
AIAgentRecommendationCreated
ClassificationApproved
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: ClassificationCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Classification
source_service: Classification Service
source_operation: createClassification
source_object_type: Classification
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/classification-created-payload.md
safe_summary:
  classification_reference_id: string
  classification_type: string
  classification_status: string
  class_system: string
  class_number: string | null
  jurisdiction_reference_id: string | null
  source_type: string
restricted_fields_policy: ClassificationCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
classification_reference_id: string
classification_type: string
classification_status: string
class_system: string
class_number: string | null
goods_services_scope_reference_id: string | null
jurisdiction_reference_id: string | null
trademark_reference_id: string | null
brand_reference_id: string | null
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use goods_services_scope_reference_id or safe summary rather than embedding full confidential filing strategy by default.
- Payload may include class_number but must not treat class number alone as complete Classification.
- Payload must not imply official acceptance, final filing scope or jurisdiction-specific compliance.
- Payload must not expose restricted customer, matter, trademark strategy or unreleased product data.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
classification_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
trademark_reference_id
brand_reference_id
jurisdiction_reference_id
goods_services_scope_reference_id
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
- source_object_reference_id must equal classification_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- trademark_reference_id must not imply Trademark filing readiness.
- jurisdiction_reference_id must not imply office acceptance or rule compliance.
- class_number alone is not sufficient professional scope.
- document_reference_ids and evidence_reference_ids must not imply completeness or sufficiency.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
ClassificationCreated
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

## 8.4 classification_type

```text
NiceClassification
LocalClassification
CustomGoodsServicesScope
MadridClassification
USIDManualScope
CNSubclassScope
EUIPOClassificationScope
InternalDraftScope
Unknown
```

## 8.5 classification_status

```text
Draft
ReviewRequired
Approved
Active
Deprecated
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 class_system

```text
Nice
USIDManual
CNSubclass
EUIPOHarmonized
Madrid
LocalOffice
Custom
Unknown
```

## 8.7 source_type

```text
ProfessionalInput
CustomerInput
TrademarkContext
BrandContext
JurisdictionContext
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.8 reason_code

```text
ClassificationCreated
ProfessionalCreated
CustomerProvided
TrademarkContextCreated
JurisdictionContextCreated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 ClassificationCreated Records Professional Scope Creation

ClassificationCreated records that a Classification reference exists.

It must not be interpreted as final filing scope, official acceptance or legal/procedural compliance.

## 9.2 Class Number Alone Is Not Classification

A class number alone is insufficient.

Classification must include governed goods/services scope and context where required.

## 9.3 Classification Is Not Trademark

Trademark Service owns legal/procedural protection object.

Classification may link to Trademark but does not create or file Trademark.

## 9.4 Classification Is Not Jurisdiction Rule Evaluation

Jurisdiction Service provides where-context.

Policy/rule evaluation may apply separately.

ClassificationCreated does not prove jurisdiction-specific acceptability.

## 9.5 Classification Is Not Document or Evidence

Classification may guide Document or Evidence requirements.

Document Service and Evidence Service own their own lifecycle and sufficiency.

## 9.6 AI Classification Recommendation Is Not Approved Scope Automatically

AI may recommend classes or goods/services.

A Classification becomes governed only through Classification Service and applicable review rules.

## 9.7 ClassificationCreated Must Respect Permission and Policy

Classification creation and visibility must respect Permission, Policy, confidentiality and customer/matter access context.

## 9.8 ClassificationCreated Must Be Immutable

ClassificationCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Trademark Service
Brand Service
Jurisdiction Service
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
- Trademark Service may use Classification for planning but must not treat it as final filing scope unless approved.
- Jurisdiction Service may provide context but does not automatically approve Classification.
- Matter and Order services may reference Classification only under governed request context.
- Document and Evidence services may use Classification to plan requirements but must not infer sufficiency.
- AI Agents may analyze Classification only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Classification creation trace.
```

Consumers must not:

```text
treat ClassificationCreated as final filing approval
treat ClassificationCreated as official office acceptance
treat ClassificationCreated as Trademark filing
treat ClassificationCreated as Document or Evidence sufficiency
expose confidential goods/services strategy
let AI convert recommendation into final scope without governed review
```

---

# 11. Relationship to Services

Producing service:

```text
Classification Service produces ClassificationCreated after createClassification succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches ClassificationCreated.
```

Related services:

```text
Trademark Service may link Classification to Trademark context.
Brand Service may provide brand context.
Jurisdiction Service may provide jurisdiction context.
Matter Service may use Classification in execution preparation.
Order Service may use Classification in service request context.
Document Service may register related artifacts.
Evidence Service may register proof related to goods/services use.
Policy Service controls visibility and AI use.
Permission Service controls who may create, view or use Classification.
Audit Service records accountability trace.
AI Agent Governance controls AI classification recommendation behavior.
```

Boundary reminders:

```text
Classification Service owns professional goods/services scope.
Trademark Service owns legal/procedural protection object.
Jurisdiction Service owns where-context.
Document Service owns artifacts.
Evidence Service owns proof layer.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /classifications/{classification_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create ClassificationCreated directly.
- API must call Classification Service createClassification, which emits the event.
- API must not expose restricted goods/services strategy, customer data, matter data or unreleased product details.
- API must distinguish ClassificationCreated from TrademarkCreated, JurisdictionLinked, official filing and office acceptance events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Classification reference was created
explain that class number alone is not sufficient scope
flag missing Jurisdiction or Trademark context for review
flag AI-assisted recommendation requiring professional review
prepare audit-safe Classification creation summary
suggest next professional review step
```

AI must not:

```text
fabricate ClassificationCreated
rewrite ClassificationCreated
delete ClassificationCreated
treat ClassificationCreated as final filing scope
treat ClassificationCreated as office acceptance
treat ClassificationCreated as legal/procedural compliance
hide AI-assisted creation
expose restricted goods/services or customer strategy
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

ClassificationCreated is valid only if:

```text
[ ] event_name is ClassificationCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Classification Service.
[ ] producing operation is createClassification.
[ ] source_domain is Classification.
[ ] source_object_type is Classification.
[ ] source_object_reference_id is present.
[ ] classification_reference_id is present.
[ ] source_object_reference_id equals classification_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] classification_type is controlled.
[ ] classification_status is controlled.
[ ] class_system is controlled.
[ ] payload does not treat class_number alone as complete Classification.
[ ] payload does not expose restricted goods/services strategy or customer/matter data unless allowed.
[ ] final filing scope, office acceptance, jurisdiction compliance, Document completeness and Evidence sufficiency are not implied.
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
ClassificationReferenceMissing
ClassificationReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
ClassificationTypeInvalid
ClassificationStatusInvalid
ClassSystemInvalid
GoodsServicesScopeMissing
RestrictedFieldViolation
ConfidentialClassificationPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownClassificationEventError
```

Rejection rules:

```text
- Failed Classification creation must not emit ClassificationCreated.
- Duplicate rejected Classification creation must not emit ClassificationCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Classification Service Specification
cite Classification Object Specification
cite Event Service Specification
cite Trademark and Jurisdiction specs where references are used
use exact event_name: ClassificationCreated
use exact event_category: DomainEvent
validate classification_reference_id
validate source_object_reference_id equals classification_reference_id
validate actor_reference_id
validate controlled classification_type/status/class_system
validate payload contract
write tests that failed createClassification does not emit ClassificationCreated
write tests that ClassificationCreated does not imply final filing scope
write tests that class number alone is not treated as complete Classification
write tests that ClassificationCreated does not imply official office acceptance
write tests that ClassificationCreated does not approve Document or Evidence
write tests that AI-assisted creation is marked where applicable
write tests that restricted classification/customer/matter content is not exposed
```

Codex must not:

```text
emit ClassificationCreated directly from UI
treat AI class suggestion as ClassificationCreated
treat TrademarkCreated as ClassificationCreated
treat ClassificationCreated as official filing or office acceptance event
treat ClassificationCreated as legal/procedural compliance approval
create Trademark, Matter or Order silently from ClassificationCreated
store raw confidential goods/services strategy in event payload by default
allow AI to fabricate ClassificationCreated
use ClassificationCreated as command to file application or approve goods/services
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines ClassificationCreated purpose.
[ ] It defines ClassificationCreated meaning.
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
| 0.1.0 | Draft | Initial ClassificationCreated Event specification. Defines governed Classification scope creation event and separates ClassificationCreated from class number alone, final filing scope, office acceptance, Trademark filing, Document completeness, Evidence sufficiency and AI recommendation. |

---

**End of Event Specification**
