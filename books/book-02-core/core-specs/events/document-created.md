# Event Specification — DocumentCreated

**Spec ID:** B02-EVT-DOCUMENT-CREATED  
**Spec Type:** Event  
**Event Name:** DocumentCreated  
**Event File:** core-specs/events/document-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Document  
**Producing Service:** core-specs/services/document-service.md  
**Related Object Specs:** core-specs/objects/document.md; core-specs/objects/trademark.md; core-specs/objects/brand.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/evidence.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/trademark-service.md; core-specs/services/brand-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/document-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/document-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/document-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Object Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

DocumentCreated records that a governed Document reference has been created by Document Service.

It exists so that Trademark, Brand, Customer, Matter, Order, Evidence, Communication, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a professional artifact record now exists without treating the Document as Evidence, Knowledge, official filing, approved proof, accepted submission, final legal conclusion or unrestricted AI source.

DocumentCreated is required before:

```text
document artifact trace
trademark document preparation
matter/order document context
customer document context
document-to-evidence review
document-to-knowledge review
communication attachment registration
AI-assisted document extraction
policy-controlled document visibility
API document reference validation
audit trace for document-sensitive actions
```

---

# 2. Event Meaning

DocumentCreated means:

```text
a stable Document object reference has been created through governed Document Service operation.
```

DocumentCreated does not mean:

```text
the file content is legally sufficient
the Document is Evidence
the Document is Knowledge
the Document has been reviewed
the Document has been approved
the Document has been filed with an authority
the Document has been accepted by an office
the Document may be used without Permission and Policy checks
AI extraction from the Document is approved truth
```

DocumentCreated records professional artifact creation only.

It does not establish proof sufficiency, legal effect, filing status, official acceptance or professional conclusion.

---

# 3. Event Category

DocumentCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Document domain.

It is not an Evidence event, Knowledge event, Communication event or official filing event.

---

# 4. Event Producer

Producing service:

```text
Document Service
```

Producing operation:

```text
createDocument
```

Source domain:

```text
Document
```

Source object type:

```text
Document
```

Allowed producer path:

```text
API / Professional user / Customer upload / System / AI-assisted governed operation
        ↓
Document Service createDocument
        ↓
Event Service record DocumentCreated
```

Producer rules:

```text
- DocumentCreated must be emitted only after Document Service successfully creates the Document reference.
- DocumentCreated must not be emitted directly by product UI.
- DocumentCreated must not be emitted directly by AI Agent outside governed service operation.
- DocumentCreated must not be emitted for failed upload, duplicate-rejected or unauthorized document creation attempts.
```

---

# 5. Event Trigger

DocumentCreated is triggered when:

```text
Document Service successfully creates a new Document object and commits its stable document_reference_id.
```

Required trigger conditions:

```text
createDocument operation completed
document_reference_id created
document_type validated
document_status validated
storage/reference context captured
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
raw file selected in UI
communication received with attachment but not registered
Evidence registration
Knowledge record creation
AI extraction result
official filing submission
office acceptance
document review approval
failed upload
failed validation
duplicate rejected Document
```

Related but separate events may include:

```text
EvidenceCreated
KnowledgeRecordCreated
CommunicationAttachmentLinked
DocumentReviewed
DocumentApproved
DocumentFiled
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: DocumentCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Document
source_service: Document Service
source_operation: createDocument
source_object_type: Document
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/document-created-payload.md
safe_summary:
  document_reference_id: string
  document_type: string
  document_status: string
  document_source_type: string
  linked_object_type: string | null
  linked_object_reference_id: string | null
restricted_fields_policy: DocumentCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
document_reference_id: string
document_type: string
document_status: string
document_source_type: string
file_reference_id: string | null
linked_object_type: string | null
linked_object_reference_id: string | null
customer_reference_id: string | null
trademark_reference_id: string | null
brand_reference_id: string | null
matter_reference_id: string | null
order_reference_id: string | null
communication_reference_id: string | null
created_by_actor_reference_id: string
ai_extracted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use file/document references rather than embedding raw file content.
- Payload must not include raw document contents, secrets, payment credentials or confidential legal strategy.
- Payload must not imply Evidence, Knowledge, filing, approval or official acceptance.
- Payload must not expose customer confidential information unless policy allows.
- AI extraction status must be marked separately and must not imply approved content.
```

---

# 7. Required References

Required references:

```text
event_id
document_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
file_reference_id
customer_reference_id
trademark_reference_id
brand_reference_id
matter_reference_id
order_reference_id
communication_reference_id
evidence_reference_id
knowledge_record_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal document_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- file_reference_id must not expose raw file content.
- evidence_reference_id must not imply Evidence creation unless Evidence Service emits EvidenceCreated.
- knowledge_record_reference_id must not imply Knowledge creation unless Knowledge Service emits KnowledgeRecordCreated.
- agent_contract_reference_id is required where AI extraction/assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
DocumentCreated
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

## 8.4 document_type

```text
PowerOfAttorney
Certificate
ApplicationForm
OfficeAction
ResponseDraft
EvidenceFile
BrandAsset
TrademarkImage
Translation
Invoice
Receipt
CommunicationAttachment
InternalNote
Other
Unknown
```

## 8.5 document_status

```text
Draft
Uploaded
Registered
ReviewRequired
Approved
Rejected
Filed
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 document_source_type

```text
ProfessionalUpload
CustomerUpload
AgentProvided
OfficialSource
CommunicationAttachment
SystemGenerated
AIGeneratedDraft
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
DocumentCreated
Uploaded
Registered
SystemGenerated
CommunicationAttachmentRegistered
MigrationCreated
AIGeneratedDraft
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 DocumentCreated Records Artifact Creation

DocumentCreated records that a Document reference exists.

It must not be interpreted as Evidence, Knowledge, filing, approval or legal sufficiency.

## 9.2 Document Is Not Evidence

Evidence Service owns proof purpose and sufficiency.

A Document may become a source for Evidence only through Evidence Service.

## 9.3 Document Is Not Knowledge

Knowledge Service owns professional reference knowledge.

Document content may support Knowledge only through Knowledge Service.

## 9.4 Document Is Not Official Filing

Filing or submission requires separate governed service/workflow events.

DocumentCreated does not mean the document was submitted or accepted.

## 9.5 AI Extraction Is Not Approved Document Meaning

AI may extract, classify or summarize.

AI extraction must be reviewed where required and must not become approved professional truth automatically.

## 9.6 DocumentCreated Must Respect Permission and Policy

Document creation, visibility, download, extraction and use must respect Permission, Policy, confidentiality and linked object access context.

## 9.7 DocumentCreated Must Be Immutable

DocumentCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Trademark Service
Brand Service
Customer Service
Matter Service
Order Service
Evidence Service
Knowledge Service
Communication Service
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
- Evidence Service may use Document as source only through governed evidence operation.
- Knowledge Service may reference Document only through governed knowledge operation.
- Matter and Order services may use Document context but must not infer completion.
- Communication Service may link attachments but must not auto-approve Document.
- AI Agents may extract/summarize only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Document creation trace.
```

Consumers must not:

```text
treat DocumentCreated as EvidenceCreated
treat DocumentCreated as KnowledgeRecordCreated
treat DocumentCreated as official filing
treat DocumentCreated as document approval
treat DocumentCreated as proof sufficiency
expose restricted document content
let AI extraction become final professional conclusion automatically
```

---

# 11. Relationship to Services

Producing service:

```text
Document Service produces DocumentCreated after createDocument succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches DocumentCreated.
```

Related services:

```text
Evidence Service may create Evidence using Document as source.
Knowledge Service may create Knowledge using Document as source.
Trademark, Brand, Customer, Matter and Order services may link Document to business/professional context.
Communication Service may link attachments to Document records.
Policy Service controls visibility, extraction and AI use.
Permission Service controls who may create, view or use Document.
Audit Service records accountability trace.
AI Agent Governance controls AI document extraction behavior.
```

Boundary reminders:

```text
Document Service owns artifacts.
Evidence Service owns proof layer.
Knowledge Service owns professional reference knowledge.
Communication Service owns message lifecycle.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /documents/{document_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create DocumentCreated directly.
- API must call Document Service createDocument, which emits the event.
- API must not expose raw document content, restricted file content, customer confidential data or legal strategy.
- API must distinguish DocumentCreated from EvidenceCreated, KnowledgeRecordCreated, CommunicationReceived and filing events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Document reference was created
classify document type for review
extract safe metadata where authorized
flag missing linked object context for review
flag document requiring review
prepare audit-safe Document creation summary
```

AI must not:

```text
fabricate DocumentCreated
rewrite DocumentCreated
delete DocumentCreated
treat DocumentCreated as Evidence or Knowledge
treat DocumentCreated as official filing or acceptance
treat AI extraction as approved document meaning
expose restricted document contents
hide AI-generated or AI-extracted status
```

AI-assisted document use requires:

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

DocumentCreated is valid only if:

```text
[ ] event_name is DocumentCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Document Service.
[ ] producing operation is createDocument.
[ ] source_domain is Document.
[ ] source_object_type is Document.
[ ] source_object_reference_id is present.
[ ] document_reference_id is present.
[ ] source_object_reference_id equals document_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] document_type is controlled.
[ ] document_status is controlled.
[ ] document_source_type is controlled.
[ ] payload does not include raw document content or restricted file content.
[ ] Evidence, Knowledge, official filing, approval and proof sufficiency are not implied.
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
DocumentReferenceMissing
DocumentReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
DocumentTypeInvalid
DocumentStatusInvalid
DocumentSourceTypeInvalid
FileReferenceInvalid
RestrictedFieldViolation
RawDocumentPayloadRejected
ConfidentialDocumentPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownDocumentEventError
```

Rejection rules:

```text
- Failed Document creation or failed upload must not emit DocumentCreated.
- Duplicate rejected Document creation must not emit DocumentCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Document Service Specification
cite Document Object Specification
cite Event Service Specification
cite Evidence and Knowledge specs where references are used
use exact event_name: DocumentCreated
use exact event_category: DomainEvent
validate document_reference_id
validate source_object_reference_id equals document_reference_id
validate actor_reference_id
validate controlled document_type/status/source_type
validate payload contract
write tests that failed createDocument does not emit DocumentCreated
write tests that DocumentCreated does not create Evidence automatically
write tests that DocumentCreated does not create Knowledge automatically
write tests that DocumentCreated does not imply official filing or approval
write tests that raw/restricted document content is not stored in payload
write tests that AI extraction/assistance is marked where applicable
```

Codex must not:

```text
emit DocumentCreated directly from UI file selection
treat raw upload attempt as DocumentCreated before Document Service succeeds
treat EvidenceCreated as DocumentCreated
treat KnowledgeRecordCreated as DocumentCreated
store raw file content in event payload by default
allow AI to fabricate DocumentCreated
use DocumentCreated as command to create Evidence, Knowledge, filing or approval
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines DocumentCreated purpose.
[ ] It defines DocumentCreated meaning.
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
| 0.1.0 | Draft | Initial DocumentCreated Event specification. Defines governed Document artifact creation event and separates DocumentCreated from Evidence, Knowledge, official filing, approval, proof sufficiency and AI extraction truth. |

---

**End of Event Specification**
