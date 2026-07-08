# Event Specification — CommunicationCreated

**Spec ID:** B02-EVT-COMMUNICATION-CREATED  
**Spec Type:** Event  
**Event Name:** CommunicationCreated  
**Event File:** core-specs/events/communication-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Communication  
**Producing Service:** core-specs/services/communication-service.md  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/notification.md; core-specs/objects/document.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/communication-service.md; core-specs/services/notification-service.md; core-specs/services/document-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/communication-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/communication-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration and Network Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

CommunicationCreated records that a governed Communication reference has been created by Communication Service.

It exists so that Notification, Document, Customer, Matter, Order, Agent, Service Provider, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a message or conversation record now exists without treating that Communication as Notification, Event, delivery success, recipient read receipt, legal notice, Document approval, Evidence creation, agreement, instruction acceptance or final professional decision.

CommunicationCreated is required before:

```text
communication lifecycle trace
matter/order conversation context
customer/agent/service-provider communication context
notification-to-communication delivery preparation
communication attachment registration
document/evidence review from communication source
AI-assisted communication drafting or summarization review
policy-controlled communication visibility
API communication reference validation
audit trace for communication-sensitive actions
```

---

# 2. Event Meaning

CommunicationCreated means:

```text
a stable Communication object reference has been created through governed Communication Service operation.
```

CommunicationCreated does not mean:

```text
the message was delivered
the message was read
a Notification was created
an Event occurrence is replaced
an attachment became Document automatically
an attachment became Evidence automatically
the recipient accepted instructions
the communication has legal notice effect
AI-generated message content is verified professional truth
```

CommunicationCreated records governed message/conversation record creation only.

It does not establish delivery, read state, legal notice, agreement, document approval or evidence sufficiency.

---

# 3. Event Category

CommunicationCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Communication domain.

It is not a Notification event, delivery event, read event, Document event or Evidence event.

---

# 4. Event Producer

Producing service:

```text
Communication Service
```

Producing operation:

```text
createCommunication
```

Source domain:

```text
Communication
```

Source object type:

```text
Communication
```

Allowed producer path:

```text
API / Professional user / System / Gateway / AI-assisted governed operation
        ↓
Communication Service createCommunication
        ↓
Event Service record CommunicationCreated
```

Producer rules:

```text
- CommunicationCreated must be emitted only after Communication Service successfully creates the Communication reference.
- CommunicationCreated must not be emitted directly by product UI.
- CommunicationCreated must not be emitted directly by AI Agent outside governed service operation.
- CommunicationCreated must not be emitted for failed, duplicate-rejected or unauthorized communication creation attempts.
```

---

# 5. Event Trigger

CommunicationCreated is triggered when:

```text
Communication Service successfully creates a new Communication object and commits its stable communication_reference_id.
```

Required trigger conditions:

```text
createCommunication operation completed
communication_reference_id created
communication_type validated
communication_status validated
participant context captured
linked business/professional context captured where applicable
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Notification creation
Event recording
raw email/message received but not registered
document upload
evidence registration
attachment upload
message delivery success
recipient read receipt
agreement acceptance
AI draft generation only
failed validation
duplicate rejected Communication
```

Related but separate events may include:

```text
NotificationCreated
DocumentCreated
EvidenceCreated
CommunicationSent
CommunicationReceived
CommunicationRead
AttachmentLinked
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: CommunicationCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Communication
source_service: Communication Service
source_operation: createCommunication
source_object_type: Communication
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/communication-created-payload.md
safe_summary:
  communication_reference_id: string
  communication_type: string
  communication_status: string
  communication_channel: string
  linked_object_type: string | null
  linked_object_reference_id: string | null
  source_type: string
restricted_fields_policy: CommunicationCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
communication_reference_id: string
communication_type: string
communication_status: string
communication_channel: string
communication_direction: string
communication_source_type: string
linked_object_type: string | null
linked_object_reference_id: string | null
customer_reference_id: string | null
matter_reference_id: string | null
order_reference_id: string | null
agent_reference_id: string | null
service_provider_reference_id: string | null
notification_reference_id: string | null
document_reference_ids: list[string]
created_by_actor_reference_id: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding raw message body by default.
- Payload must not include confidential legal strategy, privileged content, credentials, secrets or raw attachments.
- Payload must not imply delivery, read receipt, Notification creation, Document approval or Evidence creation.
- Payload must not bypass Permission or Policy for participant visibility.
- Payload must identify AI drafting/summarization assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
communication_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
customer_reference_id
matter_reference_id
order_reference_id
agent_reference_id
service_provider_reference_id
notification_reference_id
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
- source_object_reference_id must equal communication_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- notification_reference_id must not imply Notification delivery or read state.
- document_reference_ids must not imply Document approval or Evidence creation.
- evidence_reference_ids must not imply Evidence sufficiency.
- participant references must respect visibility and confidentiality policy.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
CommunicationCreated
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

## 8.4 communication_type

```text
Email
Message
InternalNote
CallRecord
MeetingRecord
ChatThread
PortalMessage
SystemMessage
ExternalGatewayMessage
Other
Unknown
```

## 8.5 communication_status

```text
Draft
Created
Queued
Sent
Received
DeliveryFailed
Read
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 communication_channel

```text
Email
Portal
Chat
Phone
Meeting
WeChat
WhatsApp
Slack
System
ExternalGateway
Unknown
```

## 8.7 communication_direction

```text
Inbound
Outbound
Internal
System
Unknown
```

## 8.8 communication_source_type

```text
ProfessionalInput
CustomerInput
AgentInput
ServiceProviderInput
NotificationGenerated
SystemProcess
GatewayIngested
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.9 reason_code

```text
CommunicationCreated
ProfessionalCreated
CustomerProvided
AgentProvided
ServiceProviderProvided
GatewayIngested
NotificationGenerated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 CommunicationCreated Records Message/Conversation Record Creation

CommunicationCreated records that a Communication reference exists.

It must not be interpreted as delivery, read state, legal notice, agreement acceptance or professional completion.

## 9.2 Communication Is Not Notification

Notification Service owns awareness intent.

Communication may be created from a Notification, but it is not the Notification itself.

## 9.3 Communication Is Not Event

Event Service records meaningful domain occurrences.

CommunicationCreated is one Event about Communication creation; the Communication object does not replace Event.

## 9.4 Attachment Is Not Document or Evidence Automatically

Attachments may later become Documents or Evidence through governed Document/Evidence Service operations.

CommunicationCreated does not approve or convert attachments.

## 9.5 Communication Does Not Establish Instruction Acceptance

A message or conversation record does not prove that recipient accepted instructions, fees, settlement or filing strategy unless governed acceptance workflow exists.

## 9.6 AI Draft or Summary Is Not Professional Truth

AI may draft, translate or summarize.

AI-generated communication content must obey authorized knowledge, policy, permission and review requirements.

## 9.7 CommunicationCreated Must Respect Permission and Policy

Communication creation, participant visibility, content rendering, attachment access and AI summarization must respect Permission, Policy and confidentiality.

## 9.8 CommunicationCreated Must Be Immutable

CommunicationCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Notification Service
Document Service
Evidence Service
Customer Service
Matter Service
Order Service
Agent Service
Service Provider Service
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
- Notification Service may reference Communication but must not infer delivery/read state unless status event exists.
- Document Service may register attachments as Documents only through governed operation.
- Evidence Service may register communication content as Evidence only through governed operation.
- Matter and Order services may display communication context but must not infer professional completion.
- Permission Service must evaluate communication visibility and actions where required.
- Policy Service must enforce confidentiality, retention and AI content rules.
- AI Agents may summarize or draft only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Communication creation trace.
```

Consumers must not:

```text
treat CommunicationCreated as NotificationCreated
treat CommunicationCreated as delivered or read
treat CommunicationCreated as DocumentCreated
treat CommunicationCreated as EvidenceCreated
treat CommunicationCreated as agreement or instruction acceptance
treat CommunicationCreated as legal notice effect by default
expose restricted communication content or attachments
```

---

# 11. Relationship to Services

Producing service:

```text
Communication Service produces CommunicationCreated after createCommunication succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches CommunicationCreated.
```

Related services:

```text
Notification Service may trigger or reference Communication.
Document Service may create Document records from attachments.
Evidence Service may create Evidence records from communication proof materials.
Customer, Matter and Order services provide business context.
Agent and Service Provider services provide external collaborator context.
Permission Service controls who may create, view, send or summarize Communication.
Policy Service controls confidentiality, retention, channel rules and AI use.
Audit Service records accountability trace.
AI Agent Governance controls AI drafting, translation and summarization behavior.
```

Boundary reminders:

```text
Communication Service owns message and conversation lifecycle.
Notification Service owns awareness intent.
Document Service owns artifacts.
Evidence Service owns proof layer.
Event Service records occurrence.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /communications/{communication_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create CommunicationCreated directly.
- API must call Communication Service createCommunication, which emits the event.
- API must not expose raw message body, raw attachments, privileged content, customer confidential data or legal strategy by default.
- API must distinguish CommunicationCreated from NotificationCreated, CommunicationSent, CommunicationRead, DocumentCreated and EvidenceCreated.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Communication reference was created
explain that Communication is not Notification, delivery, read receipt or Evidence
flag missing participant or linked object context for review
flag communication requiring policy/content review
draft safe communication summaries where authorized
prepare audit-safe Communication creation summary
```

AI must not:

```text
fabricate CommunicationCreated
rewrite CommunicationCreated
delete CommunicationCreated
treat CommunicationCreated as delivery, read receipt or legal notice
treat CommunicationCreated as Document or Evidence creation
treat AI draft/summary as verified professional content
hide AI-assisted creation
expose restricted communication, attachment, customer or matter data
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

CommunicationCreated is valid only if:

```text
[ ] event_name is CommunicationCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Communication Service.
[ ] producing operation is createCommunication.
[ ] source_domain is Communication.
[ ] source_object_type is Communication.
[ ] source_object_reference_id is present.
[ ] communication_reference_id is present.
[ ] source_object_reference_id equals communication_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] communication_type is controlled.
[ ] communication_status is controlled.
[ ] communication_channel is controlled.
[ ] communication_direction is controlled.
[ ] communication_source_type is controlled.
[ ] payload does not include raw message body, raw attachments, privileged content, matter strategy or customer data unless allowed.
[ ] delivery, read receipt, Notification, Document, Evidence, agreement and legal notice are not implied.
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
CommunicationReferenceMissing
CommunicationReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
CommunicationTypeInvalid
CommunicationStatusInvalid
CommunicationChannelInvalid
CommunicationDirectionInvalid
CommunicationSourceTypeInvalid
ParticipantReferenceInvalid
LinkedObjectReferenceInvalid
RestrictedFieldViolation
ConfidentialCommunicationPayloadRejected
PrivilegedContentPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownCommunicationEventError
```

Rejection rules:

```text
- Failed Communication creation must not emit CommunicationCreated.
- Duplicate rejected Communication creation must not emit CommunicationCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Communication Service Specification
cite Communication Object Specification
cite Event Service Specification
cite Notification/Document/Evidence specs where references are used
use exact event_name: CommunicationCreated
use exact event_category: DomainEvent
validate communication_reference_id
validate source_object_reference_id equals communication_reference_id
validate actor_reference_id
validate controlled communication_type/status/channel/direction/source_type
validate payload contract
write tests that failed createCommunication does not emit CommunicationCreated
write tests that CommunicationCreated does not imply delivery or read receipt
write tests that CommunicationCreated does not create Notification automatically
write tests that CommunicationCreated does not create Document or Evidence automatically
write tests that CommunicationCreated does not imply agreement or legal notice effect
write tests that AI-assisted creation is marked where applicable
write tests that restricted communication/customer/matter/attachment content is not exposed
```

Codex must not:

```text
emit CommunicationCreated directly from UI
treat NotificationCreated as CommunicationCreated
treat CommunicationSent as CommunicationCreated
treat CommunicationCreated as delivered or read
treat attachments as DocumentCreated or EvidenceCreated automatically
store raw confidential/privileged communication content in event payload by default
allow AI to fabricate CommunicationCreated
use CommunicationCreated as command to send message, create Evidence, approve Document, confirm agreement or grant permission
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines CommunicationCreated purpose.
[ ] It defines CommunicationCreated meaning.
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
| 0.1.0 | Draft | Initial CommunicationCreated Event specification. Defines governed Communication creation event and separates CommunicationCreated from Notification, delivery, read receipt, Document, Evidence, agreement, legal notice and AI-generated professional content. |

---

**End of Event Specification**
