# Event Specification — EvidenceCreated

**Spec ID:** B02-EVT-EVIDENCE-CREATED  
**Spec Type:** Event  
**Event Name:** EvidenceCreated  
**Event File:** core-specs/events/evidence-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Evidence  
**Producing Service:** core-specs/services/evidence-service.md  
**Related Object Specs:** core-specs/objects/evidence.md; core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/evidence-service.md; core-specs/services/document-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/evidence-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/evidence-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/evidence-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Object Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

EvidenceCreated records that a governed Evidence reference has been created by Evidence Service.

It exists so that Document, Trademark, Brand, Customer, Matter, Order, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a proof-purpose record now exists without treating the Evidence as raw Document, Knowledge, official acceptance, legal sufficiency, use proof approval, filing submission or final professional conclusion.

EvidenceCreated is required before:

```text
evidence proof-purpose trace
document-to-evidence conversion trace
trademark use evidence preparation
brand evidence preparation
matter/order evidence context
customer proof material context
AI-assisted evidence extraction review
policy-controlled evidence visibility
API evidence reference validation
audit trace for evidence-sensitive actions
```

---

# 2. Event Meaning

EvidenceCreated means:

```text
a stable Evidence object reference has been created through governed Evidence Service operation.
```

EvidenceCreated does not mean:

```text
the Evidence is legally sufficient
the Evidence has been accepted by an authority
the Evidence proves use in all jurisdictions
the Evidence is a Document
the Evidence is Knowledge
the source Document was approved
the Evidence has been filed
the Evidence may be used without Permission and Policy checks
AI extraction from the source is approved professional truth
```

EvidenceCreated records proof-purpose object creation only.

It does not establish legal sufficiency, official acceptance, filing status, use proof approval or final professional conclusion.

---

# 3. Event Category

EvidenceCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Evidence domain.

It is not a Document event, Knowledge event, official filing event or legal sufficiency event.

---

# 4. Event Producer

Producing service:

```text
Evidence Service
```

Producing operation:

```text
createEvidence
```

Source domain:

```text
Evidence
```

Source object type:

```text
Evidence
```

Allowed producer path:

```text
API / Professional user / System / AI-assisted governed operation
        ↓
Evidence Service createEvidence
        ↓
Event Service record EvidenceCreated
```

Producer rules:

```text
- EvidenceCreated must be emitted only after Evidence Service successfully creates the Evidence reference.
- EvidenceCreated must not be emitted directly by product UI.
- EvidenceCreated must not be emitted directly by AI Agent outside governed service operation.
- EvidenceCreated must not be emitted for failed, duplicate-rejected or unauthorized evidence creation attempts.
```

---

# 5. Event Trigger

EvidenceCreated is triggered when:

```text
Evidence Service successfully creates a new Evidence object and commits its stable evidence_reference_id.
```

Required trigger conditions:

```text
createEvidence operation completed
evidence_reference_id created
evidence_type validated
evidence_status validated
evidence_purpose captured
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Document upload
raw file selected in UI
AI extraction result
Knowledge record creation
official filing submission
office acceptance
evidence review approval
use sufficiency conclusion
failed validation
duplicate rejected Evidence
```

Related but separate events may include:

```text
DocumentCreated
KnowledgeRecordCreated
EvidenceReviewed
EvidenceApproved
DocumentFiled
PolicyEvaluated
PermissionEvaluated
AIAgentExtractionCreated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: EvidenceCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Evidence
source_service: Evidence Service
source_operation: createEvidence
source_object_type: Evidence
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/evidence-created-payload.md
safe_summary:
  evidence_reference_id: string
  evidence_type: string
  evidence_status: string
  evidence_purpose: string
  source_type: string
  linked_object_type: string | null
  linked_object_reference_id: string | null
restricted_fields_policy: EvidenceCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
evidence_reference_id: string
evidence_type: string
evidence_status: string
evidence_purpose: string
source_type: string
source_document_reference_ids: list[string]
linked_object_type: string | null
linked_object_reference_id: string | null
customer_reference_id: string | null
trademark_reference_id: string | null
brand_reference_id: string | null
matter_reference_id: string | null
order_reference_id: string | null
created_by_actor_reference_id: string
ai_extracted: boolean
agent_contract_reference_id: string | null
review_required: boolean
sufficiency_status: string
```

Payload rules:

```text
- Payload must use evidence and source references rather than embedding raw proof content.
- Payload must not include raw document contents, screenshots, confidential customer data or legal strategy by default.
- Payload must distinguish Evidence from Document and Knowledge.
- Payload must not imply legal sufficiency, filing, approval or official acceptance.
- Payload must identify AI extraction/assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
evidence_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
source_document_reference_ids
customer_reference_id
trademark_reference_id
brand_reference_id
matter_reference_id
order_reference_id
document_reference_id
knowledge_record_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal evidence_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- source_document_reference_ids must not imply Document approval.
- knowledge_record_reference_id must not imply Knowledge creation unless Knowledge Service emits its own event.
- trademark_reference_id must not imply that Evidence is sufficient for that Trademark.
- agent_contract_reference_id is required where AI extraction/assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
EvidenceCreated
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

## 8.4 evidence_type

```text
UseEvidence
SalesEvidence
WebsiteEvidence
MarketplaceEvidence
PackagingEvidence
AdvertisingEvidence
BusinessEvidence
OwnershipEvidence
CommunicationEvidence
OfficialRecordEvidence
Other
Unknown
```

## 8.5 evidence_status

```text
Draft
Registered
ReviewRequired
Approved
Rejected
Filed
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 evidence_purpose

```text
TrademarkUse
OfficeActionResponse
Opposition
Cancellation
Renewal
DeclarationOfUse
OwnershipProof
PriorityClaim
CustomerRecord
InternalReview
Other
Unknown
```

## 8.7 source_type

```text
DocumentReference
CustomerProvided
ProfessionalInput
AgentProvided
OfficialSource
WebsiteCapture
MarketplaceCapture
CommunicationReference
SystemGenerated
AIExtracted
Migration
ExternalIntegration
Unknown
```

## 8.8 sufficiency_status

```text
NotEvaluated
ReviewRequired
PotentiallySufficient
Insufficient
Sufficient
Rejected
Unknown
```

## 8.9 reason_code

```text
EvidenceCreated
DocumentConverted
ProfessionalCreated
CustomerProvided
AgentProvided
OfficialSourceCreated
AIExtractedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 EvidenceCreated Records Proof-Purpose Creation

EvidenceCreated records that an Evidence reference exists.

It must not be interpreted as legal sufficiency, office acceptance, filing or approval.

## 9.2 Evidence Is Not Document

Document Service owns artifacts.

Evidence may reference Document, but Evidence has its own proof purpose, review state and sufficiency context.

## 9.3 Evidence Is Not Knowledge

Knowledge Service owns professional reference knowledge.

Evidence may inform knowledge but must not become Knowledge automatically.

## 9.4 EvidenceCreated Does Not Prove Use Automatically

Trademark use evidence requires jurisdiction, goods/services, date, source and professional review context.

EvidenceCreated alone does not prove use.

## 9.5 AI Extraction Is Not Evidence Sufficiency

AI may extract or summarize source material.

AI extraction must not be treated as professional sufficiency review automatically.

## 9.6 EvidenceCreated Must Respect Permission and Policy

Evidence creation, visibility, download, extraction and use must respect Permission, Policy, confidentiality and linked object access context.

## 9.7 EvidenceCreated Must Be Immutable

EvidenceCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Document Service
Trademark Service
Brand Service
Customer Service
Matter Service
Order Service
Knowledge Service
Policy Service
Permission Service
Workflow Contract Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Trademark Service may use Evidence for professional review but must not infer sufficiency automatically.
- Document Service may provide source artifacts but does not own Evidence purpose.
- Knowledge Service may reference Evidence only through governed knowledge operation.
- Matter and Order services may use Evidence context but must not infer completion.
- AI Agents may extract/summarize only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Evidence creation trace.
```

Consumers must not:

```text
treat EvidenceCreated as DocumentCreated
treat EvidenceCreated as KnowledgeRecordCreated
treat EvidenceCreated as legal sufficiency
treat EvidenceCreated as official filing or acceptance
treat EvidenceCreated as proof of use without review
expose restricted evidence content
let AI extraction become final professional conclusion automatically
```

---

# 11. Relationship to Services

Producing service:

```text
Evidence Service produces EvidenceCreated after createEvidence succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches EvidenceCreated.
```

Related services:

```text
Document Service may provide source artifact references.
Trademark Service may use Evidence for trademark use/prosecution review.
Brand, Customer, Matter and Order services may link Evidence to business/professional context.
Knowledge Service may reference Evidence through governed knowledge operation.
Policy Service controls visibility, extraction and AI use.
Permission Service controls who may create, view or use Evidence.
Audit Service records accountability trace.
AI Agent Governance controls AI evidence extraction behavior.
```

Boundary reminders:

```text
Evidence Service owns proof purpose and sufficiency context.
Document Service owns artifacts.
Knowledge Service owns professional reference knowledge.
Trademark Service owns legal/procedural protection object.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /evidence/{evidence_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create EvidenceCreated directly.
- API must call Evidence Service createEvidence, which emits the event.
- API must not expose raw evidence content, raw source documents, customer confidential data or legal strategy.
- API must distinguish EvidenceCreated from DocumentCreated, KnowledgeRecordCreated, review/approval and filing events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Evidence reference was created
classify evidence type for review
extract safe metadata where authorized
flag missing source, date, jurisdiction or goods/services context for review
flag evidence requiring professional sufficiency review
prepare audit-safe Evidence creation summary
```

AI must not:

```text
fabricate EvidenceCreated
rewrite EvidenceCreated
delete EvidenceCreated
treat EvidenceCreated as Document or Knowledge
treat EvidenceCreated as legal sufficiency
treat EvidenceCreated as proof of use without review
treat AI extraction as approved evidence meaning
expose restricted evidence contents
hide AI-extracted status
```

AI-assisted evidence use requires:

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

EvidenceCreated is valid only if:

```text
[ ] event_name is EvidenceCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Evidence Service.
[ ] producing operation is createEvidence.
[ ] source_domain is Evidence.
[ ] source_object_type is Evidence.
[ ] source_object_reference_id is present.
[ ] evidence_reference_id is present.
[ ] source_object_reference_id equals evidence_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] evidence_type is controlled.
[ ] evidence_status is controlled.
[ ] evidence_purpose is controlled.
[ ] sufficiency_status is controlled.
[ ] payload does not include raw evidence/source content or restricted file content.
[ ] Document, Knowledge, official filing, approval and proof sufficiency are not implied.
[ ] AI extraction/assistance is explicitly identified where applicable.
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
EvidenceReferenceMissing
EvidenceReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
EvidenceTypeInvalid
EvidenceStatusInvalid
EvidencePurposeInvalid
SufficiencyStatusInvalid
SourceReferenceInvalid
RestrictedFieldViolation
RawEvidencePayloadRejected
ConfidentialEvidencePayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownEvidenceEventError
```

Rejection rules:

```text
- Failed Evidence creation must not emit EvidenceCreated.
- Duplicate rejected Evidence creation must not emit EvidenceCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Evidence Service Specification
cite Evidence Object Specification
cite Event Service Specification
cite Document specs where source documents are used
use exact event_name: EvidenceCreated
use exact event_category: DomainEvent
validate evidence_reference_id
validate source_object_reference_id equals evidence_reference_id
validate actor_reference_id
validate controlled evidence_type/status/purpose/sufficiency_status
validate payload contract
write tests that failed createEvidence does not emit EvidenceCreated
write tests that EvidenceCreated does not create Document automatically
write tests that EvidenceCreated does not create Knowledge automatically
write tests that EvidenceCreated does not imply proof sufficiency
write tests that EvidenceCreated does not imply official filing or acceptance
write tests that raw/restricted evidence content is not stored in payload
write tests that AI extraction/assistance is marked where applicable
```

Codex must not:

```text
emit EvidenceCreated directly from UI file selection
treat DocumentCreated as EvidenceCreated
treat KnowledgeRecordCreated as EvidenceCreated
store raw evidence or source document content in event payload by default
treat AI extraction as sufficiency review
allow AI to fabricate EvidenceCreated
use EvidenceCreated as command to create Document, Knowledge, filing, approval or sufficiency conclusion
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines EvidenceCreated purpose.
[ ] It defines EvidenceCreated meaning.
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
| 0.1.0 | Draft | Initial EvidenceCreated Event specification. Defines governed Evidence proof-purpose creation event and separates EvidenceCreated from Document, Knowledge, official filing, approval, proof sufficiency and AI extraction truth. |

---

**End of Event Specification**
