# Event Specification — KnowledgeRecordCreated

**Spec ID:** B02-EVT-KNOWLEDGE-RECORD-CREATED  
**Spec Type:** Event  
**Event Name:** KnowledgeRecordCreated  
**Event File:** core-specs/events/knowledge-record-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Knowledge  
**Producing Service:** core-specs/services/knowledge-service.md  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/knowledge-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/knowledge-record-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

KnowledgeRecordCreated records that a governed Knowledge Record has been created by Knowledge Service.

It exists so that Document, Evidence, Policy, Permission, AI Agents, APIs, product consumers and professional workflows can safely recognize that a professional reference knowledge record now exists without treating that record as approved legal conclusion, Evidence, Document, source-of-law, final professional judgment or AI-generated truth.

KnowledgeRecordCreated is required before:

```text
knowledge base trace
professional reference creation trace
AI authorized knowledge retrieval
document-to-knowledge reference review
evidence-to-knowledge boundary enforcement
knowledge governance audit
policy-controlled knowledge visibility
knowledge citation and source context
API knowledge reference validation
```

---

# 2. Event Meaning

KnowledgeRecordCreated means:

```text
a stable Knowledge Record reference has been created through governed Knowledge Service operation.
```

KnowledgeRecordCreated does not mean:

```text
the Knowledge Record is legally correct in all contexts
the Knowledge Record is final professional advice
the Knowledge Record is Evidence
the Knowledge Record is Document
the Knowledge Record is official law
the Knowledge Record has been approved for all AI Agents
the Knowledge Record may be used without Policy and Permission checks
the Knowledge Record replaces human professional judgment
```

KnowledgeRecordCreated records governed professional reference creation only.

It does not establish final truth, evidence sufficiency or legal conclusion.

---

# 3. Event Category

KnowledgeRecordCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Knowledge domain.

It is not an AIAgentEvent even if AI assisted the draft, unless a separate AI drafting event is defined.

---

# 4. Event Producer

Producing service:

```text
Knowledge Service
```

Producing operation:

```text
createKnowledgeRecord
```

Source domain:

```text
Knowledge
```

Source object type:

```text
KnowledgeRecord
```

Allowed producer path:

```text
API / Admin / System / AI-assisted governed operation
        ↓
Knowledge Service createKnowledgeRecord
        ↓
Event Service record KnowledgeRecordCreated
```

Producer rules:

```text
- KnowledgeRecordCreated must be emitted only after Knowledge Service successfully creates the Knowledge Record reference.
- KnowledgeRecordCreated must not be emitted directly by product UI.
- KnowledgeRecordCreated must not be emitted directly by AI Agent outside governed service operation.
- KnowledgeRecordCreated must not be emitted for failed, duplicate-rejected or unauthorized creation attempts.
```

---

# 5. Event Trigger

KnowledgeRecordCreated is triggered when:

```text
Knowledge Service successfully creates a new Knowledge Record and commits its stable knowledge_record_reference_id.
```

Required trigger conditions:

```text
createKnowledgeRecord operation completed
knowledge_record_reference_id created
knowledge_record_type validated
knowledge_status validated
source_reference captured
governance_context captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Document upload
Evidence registration
AI draft generation
web source discovery
unreviewed note creation
policy evaluation
permission evaluation
failed validation
duplicate rejected Knowledge Record
```

Related but separate events may include:

```text
DocumentCreated
EvidenceCreated
KnowledgeRecordUpdated
PolicyEvaluated
PermissionEvaluated
AIAgentDraftCreated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: KnowledgeRecordCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Knowledge
source_service: Knowledge Service
source_operation: createKnowledgeRecord
source_object_type: KnowledgeRecord
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/knowledge-record-created-payload.md
safe_summary:
  knowledge_record_reference_id: string
  knowledge_record_type: string
  knowledge_status: string
  knowledge_scope: string
  source_type: string
restricted_fields_policy: KnowledgeRecordCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
knowledge_record_reference_id: string
knowledge_record_type: string
knowledge_status: string
knowledge_scope: string
source_type: string
source_reference_ids: list[string]
document_reference_ids: list[string]
evidence_reference_ids: list[string]
created_by_actor_reference_id: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references rather than embedding full knowledge content by default.
- Payload must not include restricted legal strategy, confidential client data or raw document/evidence content.
- Payload must distinguish Knowledge from Document and Evidence.
- Payload must identify AI assistance where applicable.
- Payload must not state that the Knowledge Record is final legal advice unless a separate approval/review process says so.
```

---

# 7. Required References

Required references:

```text
event_id
knowledge_record_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
source_reference_ids
document_reference_ids
evidence_reference_ids
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
review_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal knowledge_record_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- document_reference_ids must not convert Documents into Knowledge automatically unless Knowledge Service created a governed record.
- evidence_reference_ids must not convert Evidence into Knowledge automatically unless Knowledge Service created a governed record.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
KnowledgeRecordCreated
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

## 8.4 knowledge_record_type

```text
LegalRule
ProcedureRule
JurisdictionGuide
ClassificationGuide
FilingRequirement
OfficePractice
TemplateInstruction
ProfessionalNote
CaseReference
FAQ
AIAssistedDraft
Unknown
```

## 8.5 knowledge_status

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

## 8.6 knowledge_scope

```text
Global
JurisdictionSpecific
ServiceSpecific
ProcedureSpecific
ProductSpecific
InternalOnly
AIAuthorized
Restricted
Unknown
```

## 8.7 source_type

```text
ProfessionalInput
OfficialSource
DocumentReference
EvidenceReference
Migration
ExternalIntegration
AIAssisted
SystemGenerated
Unknown
```

## 8.8 reason_code

```text
KnowledgeRecordCreated
ProfessionalCreated
OfficialSourceCreated
DocumentReferenced
EvidenceReferenced
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 KnowledgeRecordCreated Records Governed Knowledge Creation

KnowledgeRecordCreated records that a Knowledge Record exists.

It must not be interpreted as final professional advice or official legal truth.

## 9.2 Knowledge Is Not Document

Document Service owns professional artifacts.

Knowledge may reference Document, but DocumentCreated is separate.

## 9.3 Knowledge Is Not Evidence

Evidence Service owns proof purpose and sufficiency.

Knowledge may reference Evidence, but EvidenceCreated is separate.

## 9.4 Knowledge Is Not AI Truth

AI may assist in drafting or summarizing.

AI assistance must not convert a draft into approved Knowledge automatically.

## 9.5 Knowledge Use Requires Permission and Policy

A Knowledge Record may be restricted, internal, deprecated or AI-authorized only under defined rules.

Consumers must respect Permission and Policy.

## 9.6 KnowledgeRecordCreated Must Preserve Source Context

Knowledge creation must preserve source_reference_ids or source_type where available.

Unsupported source claims must not be hidden.

## 9.7 KnowledgeRecordCreated Must Be Immutable

KnowledgeRecordCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
AI Agent Governance
Document Service
Evidence Service
Policy Service
Permission Service
Workflow Contract Service
Task Service
API Layer
Product UI read model
Audit Service
Integration services under contract
```

Consumer rules:

```text
- AI Agents may retrieve Knowledge only if authorized by Agent Contract, Permission and Policy.
- Document Service may link Knowledge to Document but must not convert Knowledge into Document automatically.
- Evidence Service may link Knowledge to Evidence but must not treat Knowledge as proof.
- Policy Service may restrict visibility or AI use.
- Permission Service may evaluate whether actor may create, view or use Knowledge.
- Audit may preserve Knowledge creation trace.
```

Consumers must not:

```text
treat KnowledgeRecordCreated as legal approval
treat KnowledgeRecordCreated as Evidence sufficiency
treat KnowledgeRecordCreated as Document approval
use deprecated/restricted Knowledge without policy check
expose restricted knowledge content
let AI cite unapproved or restricted Knowledge as final truth
```

---

# 11. Relationship to Services

Producing service:

```text
Knowledge Service produces KnowledgeRecordCreated after createKnowledgeRecord succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches KnowledgeRecordCreated.
```

Related services:

```text
Document Service may provide referenced artifacts.
Evidence Service may provide referenced proof objects.
Policy Service controls visibility, use and AI authorization.
Permission Service controls who may create/view/use Knowledge.
AI Agent Governance controls AI retrieval and generation behavior.
Audit Service records accountability trace.
```

Boundary reminders:

```text
Knowledge Service owns professional reference knowledge.
Document Service owns artifacts.
Evidence Service owns proof layer.
Policy Service owns contextual constraints.
Permission Service owns allowed action.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /knowledge-records/{knowledge_record_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create KnowledgeRecordCreated directly.
- API must call Knowledge Service createKnowledgeRecord, which emits the event.
- API must not expose restricted knowledge content, confidential client information or raw source material.
- API must distinguish KnowledgeRecordCreated from DocumentCreated and EvidenceCreated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Knowledge Record was created
explain source and scope where authorized
flag missing source references for review
flag AI-assisted draft requiring review
recommend deprecation/review checks
prepare audit-safe Knowledge creation summary
```

AI must not:

```text
fabricate KnowledgeRecordCreated
rewrite KnowledgeRecordCreated
delete KnowledgeRecordCreated
treat KnowledgeRecordCreated as final legal advice
treat Knowledge as Evidence or Document
cite restricted Knowledge without authorization
hide AI-assisted creation
expose restricted Knowledge content
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

KnowledgeRecordCreated is valid only if:

```text
[ ] event_name is KnowledgeRecordCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Knowledge Service.
[ ] producing operation is createKnowledgeRecord.
[ ] source_domain is Knowledge.
[ ] source_object_type is KnowledgeRecord.
[ ] source_object_reference_id is present.
[ ] knowledge_record_reference_id is present.
[ ] source_object_reference_id equals knowledge_record_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] knowledge_record_type is controlled.
[ ] knowledge_status is controlled.
[ ] knowledge_scope is controlled.
[ ] payload does not include restricted raw knowledge/source content unless allowed.
[ ] Document and Evidence references do not imply automatic conversion.
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
KnowledgeRecordReferenceMissing
KnowledgeRecordReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
KnowledgeRecordTypeInvalid
KnowledgeStatusInvalid
KnowledgeScopeInvalid
SourceReferenceInvalid
RestrictedFieldViolation
ConfidentialKnowledgePayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownKnowledgeEventError
```

Rejection rules:

```text
- Failed Knowledge Record creation must not emit KnowledgeRecordCreated.
- Duplicate rejected Knowledge creation must not emit KnowledgeRecordCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Knowledge Service Specification
cite Knowledge Object Specification
cite Event Service Specification
cite Document/Evidence specs where references are used
use exact event_name: KnowledgeRecordCreated
use exact event_category: DomainEvent
validate knowledge_record_reference_id
validate source_object_reference_id equals knowledge_record_reference_id
validate actor_reference_id
validate controlled knowledge_record_type/status/scope
validate payload contract
write tests that failed createKnowledgeRecord does not emit KnowledgeRecordCreated
write tests that KnowledgeRecordCreated does not create Document or Evidence automatically
write tests that AI-assisted creation is marked where applicable
write tests that restricted knowledge/source content is not exposed
write tests that KnowledgeRecordCreated is not treated as final professional advice
```

Codex must not:

```text
emit KnowledgeRecordCreated directly from UI
treat DocumentCreated as KnowledgeRecordCreated
treat EvidenceCreated as KnowledgeRecordCreated
store raw confidential source content in event payload by default
allow AI to fabricate KnowledgeRecordCreated
allow AI-assisted draft to become approved Knowledge automatically
use KnowledgeRecordCreated as command to create Document, Evidence or final legal conclusion
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines KnowledgeRecordCreated purpose.
[ ] It defines KnowledgeRecordCreated meaning.
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
| 0.1.0 | Draft | Initial KnowledgeRecordCreated Event specification. Defines governed Knowledge Record creation event and separates Knowledge from Document, Evidence, AI output, final legal advice and unrestricted professional truth. |

---

**End of Event Specification**
