# Event Specification — KnowledgeRecordUpdated

**Spec ID:** B02-EVT-KNOWLEDGE-RECORD-UPDATED  
**Spec Type:** Event  
**Event Name:** KnowledgeRecordUpdated  
**Event File:** core-specs/events/knowledge-record-updated.md  
**Event Category:** DomainEvent  
**Owning Domain:** Knowledge  
**Producing Service:** core-specs/services/knowledge-service.md  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/knowledge-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/knowledge-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/knowledge-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/knowledge-record-updated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

KnowledgeRecordUpdated records that a governed Knowledge Record has been updated by Knowledge Service.

It exists so that Document, Evidence, Policy, Permission, AI Agents, APIs, product consumers and professional workflows can safely recognize that professional reference knowledge has changed without treating the update as final legal approval, Evidence revision, Document revision, source-of-law update, AI truth update or unrestricted professional conclusion.

KnowledgeRecordUpdated is required before:

```text
knowledge change trace
knowledge version/revision trace
professional reference update trace
AI authorized knowledge refresh
document-to-knowledge reference review
evidence-to-knowledge boundary enforcement
knowledge governance audit
policy-controlled knowledge visibility update
knowledge deprecation or review tracking
API knowledge reference validation
```

---

# 2. Event Meaning

KnowledgeRecordUpdated means:

```text
an existing stable Knowledge Record reference has been updated through governed Knowledge Service operation.
```

KnowledgeRecordUpdated does not mean:

```text
the Knowledge Record is legally correct in all contexts
the Knowledge Record is final professional advice
the Knowledge Record is Evidence
the Knowledge Record is Document
the source document or evidence object was updated
the Knowledge Record is approved for all AI Agents
the Knowledge Record may be used without Policy and Permission checks
the Knowledge Record replaces human professional judgment
```

KnowledgeRecordUpdated records governed professional reference update only.

It does not establish final truth, evidence sufficiency or legal conclusion.

---

# 3. Event Category

KnowledgeRecordUpdated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Knowledge domain.

If the update is specifically a lifecycle status change, downstream consumers may observe status fields, but the category remains DomainEvent unless a separate KnowledgeRecordStatusChanged event is introduced.

---

# 4. Event Producer

Producing service:

```text
Knowledge Service
```

Producing operation:

```text
updateKnowledgeRecord
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
Knowledge Service updateKnowledgeRecord
        ↓
Event Service record KnowledgeRecordUpdated
```

Producer rules:

```text
- KnowledgeRecordUpdated must be emitted only after Knowledge Service successfully updates the Knowledge Record reference.
- KnowledgeRecordUpdated must not be emitted directly by product UI.
- KnowledgeRecordUpdated must not be emitted directly by AI Agent outside governed service operation.
- KnowledgeRecordUpdated must not be emitted for failed, unauthorized or rejected update attempts.
```

---

# 5. Event Trigger

KnowledgeRecordUpdated is triggered when:

```text
Knowledge Service successfully updates an existing Knowledge Record and commits the governed change.
```

Required trigger conditions:

```text
updateKnowledgeRecord operation completed
knowledge_record_reference_id validated
updated fields validated
knowledge_record_type validated where changed
knowledge_status validated where changed
source_reference captured
governance_context captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Document update
Evidence update
AI draft update
web source refresh not accepted into Knowledge
unreviewed note update
policy evaluation
permission evaluation
failed validation
unauthorized update attempt
```

Related but separate events may include:

```text
DocumentUpdated
EvidenceUpdated
KnowledgeRecordCreated
KnowledgeRecordStatusChanged
PolicyEvaluated
PermissionEvaluated
AIAgentDraftUpdated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: KnowledgeRecordUpdated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Knowledge
source_service: Knowledge Service
source_operation: updateKnowledgeRecord
source_object_type: KnowledgeRecord
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/knowledge-record-updated-payload.md
safe_summary:
  knowledge_record_reference_id: string
  knowledge_record_type: string
  knowledge_status_before: string | null
  knowledge_status_after: string | null
  knowledge_scope: string
  changed_field_keys: list[string]
  source_type: string
restricted_fields_policy: KnowledgeRecordUpdatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
knowledge_record_reference_id: string
knowledge_record_type: string
knowledge_status_before: string | null
knowledge_status_after: string | null
knowledge_scope_before: string | null
knowledge_scope_after: string | null
changed_field_keys: list[string]
changed_reference_keys: list[string]
source_type: string
source_reference_ids_added: list[string]
source_reference_ids_removed: list[string]
document_reference_ids_added: list[string]
document_reference_ids_removed: list[string]
evidence_reference_ids_added: list[string]
evidence_reference_ids_removed: list[string]
updated_by_actor_reference_id: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references and safe change summaries rather than embedding full knowledge content by default.
- Payload may include changed field keys but must not include restricted raw values unless explicitly allowed.
- Payload must not include restricted legal strategy, confidential client data or raw document/evidence content.
- Payload must distinguish Knowledge update from Document update and Evidence update.
- Payload must identify AI assistance where applicable.
- Payload must not state that the updated Knowledge Record is final legal advice unless a separate approval/review process says so.
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
- actor_reference_id identifies who/what requested or performed update.
- document_reference_ids must not imply Document update unless Document Service emits its own event.
- evidence_reference_ids must not imply Evidence update unless Evidence Service emits its own event.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
KnowledgeRecordUpdated
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
KnowledgeRecordUpdated
ProfessionalUpdated
OfficialSourceUpdated
DocumentReferenceUpdated
EvidenceReferenceUpdated
StatusUpdated
ScopeUpdated
Deprecated
MigrationUpdated
AIAssistedUpdated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 KnowledgeRecordUpdated Records Governed Knowledge Change

KnowledgeRecordUpdated records that a Knowledge Record changed.

It must not be interpreted as final professional advice or official legal truth.

## 9.2 Knowledge Update Is Not Document Update

Document Service owns Document lifecycle.

Updating a Knowledge reference to a Document does not update the Document itself.

## 9.3 Knowledge Update Is Not Evidence Update

Evidence Service owns Evidence lifecycle and proof purpose.

Updating a Knowledge reference to Evidence does not update the Evidence object itself.

## 9.4 Knowledge Update Is Not AI Truth Update

AI may assist in drafting or summarizing updates.

AI assistance must not convert a draft or change into approved Knowledge automatically.

## 9.5 Knowledge Use Requires Permission and Policy

Updated Knowledge may be restricted, internal, deprecated or AI-authorized only under defined rules.

Consumers must respect Permission and Policy.

## 9.6 KnowledgeRecordUpdated Must Preserve Safe Diff

Knowledge update must preserve safe changed field keys, safe reference diffs and status/scope changes where allowed.

Restricted raw values must not be exposed.

## 9.7 KnowledgeRecordUpdated Must Be Immutable

KnowledgeRecordUpdated must not be rewritten except controlled event metadata/status handled by Event Service.

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
- AI Agents may refresh or use updated Knowledge only if authorized by Agent Contract, Permission and Policy.
- Document Service may review Knowledge links to Documents but must not update Document automatically.
- Evidence Service may review Knowledge links to Evidence but must not treat Knowledge as proof.
- Policy Service may restrict visibility, use and AI access after update.
- Permission Service may evaluate whether actor may view or use updated Knowledge.
- Audit may preserve Knowledge update trace.
```

Consumers must not:

```text
treat KnowledgeRecordUpdated as legal approval
treat KnowledgeRecordUpdated as Evidence sufficiency
treat KnowledgeRecordUpdated as Document approval
use deprecated/restricted Knowledge without policy check
expose restricted knowledge changes
let AI cite unapproved or restricted Knowledge as final truth
```

---

# 11. Relationship to Services

Producing service:

```text
Knowledge Service produces KnowledgeRecordUpdated after updateKnowledgeRecord succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches KnowledgeRecordUpdated.
```

Related services:

```text
Document Service may provide referenced artifacts but owns Document changes separately.
Evidence Service may provide referenced proof objects but owns Evidence changes separately.
Policy Service controls visibility, use and AI authorization.
Permission Service controls who may update/view/use Knowledge.
AI Agent Governance controls AI retrieval, generation and update behavior.
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
- API must not create KnowledgeRecordUpdated directly.
- API must call Knowledge Service updateKnowledgeRecord, which emits the event.
- API must not expose restricted knowledge content, confidential client information, raw source material or restricted change values.
- API must distinguish KnowledgeRecordUpdated from DocumentUpdated and EvidenceUpdated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Knowledge Record was updated
explain source, scope, status and safe change summary where authorized
flag missing source references for review
flag AI-assisted update requiring review
recommend deprecation/review checks
prepare audit-safe Knowledge update summary
```

AI must not:

```text
fabricate KnowledgeRecordUpdated
rewrite KnowledgeRecordUpdated
delete KnowledgeRecordUpdated
treat KnowledgeRecordUpdated as final legal advice
treat Knowledge as Evidence or Document
cite restricted or deprecated Knowledge without authorization
hide AI-assisted update
expose restricted Knowledge content or raw changed values
```

AI-assisted update requires:

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

KnowledgeRecordUpdated is valid only if:

```text
[ ] event_name is KnowledgeRecordUpdated.
[ ] event_category is DomainEvent.
[ ] producing service is Knowledge Service.
[ ] producing operation is updateKnowledgeRecord.
[ ] source_domain is Knowledge.
[ ] source_object_type is KnowledgeRecord.
[ ] source_object_reference_id is present.
[ ] knowledge_record_reference_id is present.
[ ] source_object_reference_id equals knowledge_record_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] knowledge_record_type is controlled.
[ ] knowledge_status_before/after are controlled where provided.
[ ] knowledge_scope_before/after are controlled where provided.
[ ] changed_field_keys are provided where applicable.
[ ] payload does not include restricted raw knowledge/source/change content unless allowed.
[ ] Document and Evidence references do not imply automatic update.
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
ChangedFieldKeysMissing
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
- Failed Knowledge Record update must not emit KnowledgeRecordUpdated.
- Unauthorized update attempt must not emit KnowledgeRecordUpdated.
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
use exact event_name: KnowledgeRecordUpdated
use exact event_category: DomainEvent
validate knowledge_record_reference_id
validate source_object_reference_id equals knowledge_record_reference_id
validate actor_reference_id
validate controlled knowledge_record_type/status/scope
validate payload contract
write tests that failed updateKnowledgeRecord does not emit KnowledgeRecordUpdated
write tests that unauthorized update does not emit KnowledgeRecordUpdated
write tests that KnowledgeRecordUpdated does not update Document or Evidence automatically
write tests that AI-assisted update is marked where applicable
write tests that restricted knowledge/source/change content is not exposed
write tests that KnowledgeRecordUpdated is not treated as final professional advice
```

Codex must not:

```text
emit KnowledgeRecordUpdated directly from UI
treat DocumentUpdated as KnowledgeRecordUpdated
treat EvidenceUpdated as KnowledgeRecordUpdated
store raw confidential source or changed content in event payload by default
allow AI to fabricate KnowledgeRecordUpdated
allow AI-assisted update to become approved Knowledge automatically
use KnowledgeRecordUpdated as command to update Document, Evidence or final legal conclusion
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines KnowledgeRecordUpdated purpose.
[ ] It defines KnowledgeRecordUpdated meaning.
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
| 0.1.0 | Draft | Initial KnowledgeRecordUpdated Event specification. Defines governed Knowledge Record update event and separates Knowledge update from Document update, Evidence update, AI output, final legal advice and unrestricted professional truth. |

---

**End of Event Specification**
