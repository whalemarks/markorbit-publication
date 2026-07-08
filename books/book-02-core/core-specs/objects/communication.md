# Object Specification — Communication

**Spec ID:** B02-OBJ-COMMUNICATION  
**Spec Type:** Object  
**Object Name:** Communication  
**Owning Domain:** Communication  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/communication.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/notification.md; core-specs/objects/document.md; core-specs/objects/communication-thread.md; core-specs/objects/communication-message.md; core-specs/objects/communication-participant.md; core-specs/objects/communication-attachment-reference.md  
**Related Service Specs:** core-specs/services/communication-registration-service.md; core-specs/services/communication-thread-service.md; core-specs/services/communication-message-service.md; core-specs/services/communication-participant-service.md; core-specs/services/communication-attachment-reference-service.md; core-specs/services/communication-status-service.md; core-specs/services/communication-reference-validation-service.md  
**Related Event Specs:** core-specs/events/communication-created.md; core-specs/events/communication-updated.md; core-specs/events/communication-message-added.md; core-specs/events/communication-sent.md; core-specs/events/communication-received.md; core-specs/events/communication-failed.md; core-specs/events/communication-attachment-linked.md; core-specs/events/communication-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/communication/communication-contract.md; core-specs/contracts/communication/communication-thread-contract.md; core-specs/contracts/communication/communication-message-contract.md; core-specs/contracts/communication/communication-participant-contract.md; core-specs/contracts/communication/communication-attachment-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Communication object defines the Core-recognized message and conversation lifecycle used to manage professional, customer, agent, provider, partner and system communications in MarkOrbit.

It exists so that Customers, Orders, Matters, Tasks, Notifications, Documents, Evidence, Agents, Service Providers, AI Agents, Services, APIs and product consumers can consistently reference conversations and messages without confusing Communication with Notification, Event, Document, Evidence, Task or marketing automation.

Communication is required before:

```text
customer email/message tracking
agent correspondence
service provider correspondence
matter conversation history
order-related communication
task-related communication
document request communication
evidence request communication
notification-to-message handoff
AI communication drafting and summarization
audit trace for outbound and inbound communication
```

---

# 2. Core Meaning

Communication means:

```text
a Core-recognized conversation or message lifecycle object with participants, channel, content reference, thread context, related business/professional objects, delivery status and audit trace.
```

Communication is not:

```text
Notification
Event
Task
Document
Evidence
Knowledge
Marketing campaign
Messaging gateway
AI Output
raw email only
chat transcript only
```

Communication answers:

```text
Who communicated with whom?
What channel or thread was used?
Which message or content reference applies?
Which Customer, Matter, Order, Task, Document, Evidence or Agent context is related?
Was the message drafted, sent, received, failed, archived or linked?
Which attachments exist?
Do attachments become Documents or Evidence?
What audit trace is required?
```

---

# 3. Object Category

Communication is a Business Execution Object owned by the Communication Domain.

It is the message and conversation lifecycle layer.

Notification is awareness intent.

Event records meaningful occurrence.

Document is professional artifact.

Evidence is proof layer.

Communication must preserve these boundaries.

---

# 4. Architectural Position

Communication sits between awareness, execution and external/internal correspondence.

```text
Event / Task / Matter may require awareness or action
        ↓
Notification records awareness intent
        ↓
Communication carries message content and conversation lifecycle
        ↓
Document may be linked from attachment or generated artifact
        ↓
Evidence may be registered from material where proof purpose exists
        ↓
Event and Audit preserve trace
```

Communication carries message content.

It does not prove facts by itself.

It does not become Document or Evidence automatically.

---

# 5. Scope

The Communication object includes:

```text
communication id
communication type
communication status
thread reference
message reference
channel reference
direction
participant references
sender reference
recipient references
subject/title reference
content reference
attachment references
customer reference
order reference
matter reference
task reference
notification reference
document references
evidence references
agent/service-provider references
delivery reference
source reference
created time
updated time
audit metadata
```

MVP / Phase 4 scope includes:

```text
communication id
communication type
communication status
thread reference
message reference
channel reference
direction
participant references
sender reference
recipient references
subject/title reference
content reference
attachment references
customer reference
matter reference
order reference
task reference
notification reference
document references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Communication ID. |
| communication_type | enum | Yes | Yes | Controlled communication type. |
| status | enum | Yes | Yes | Controlled Communication status. |
| channel | enum | Yes | Yes | Email, Chat, Phone, Meeting, Portal, System, Other, Unknown. |
| direction | enum | Yes | Yes | Inbound, Outbound, Internal, System, Unknown. |
| thread_reference_id | string | No | Yes | Thread/conversation reference. |
| message_reference_id | string | No | Yes | Specific message reference where applicable. |
| subject_reference | string | No | Yes | Subject/title reference. |
| content_reference | string | No | Yes | Content or body reference; use restricted references where needed. |
| participant_references | array | No | Yes | All participant references. |
| sender_reference_id | string | No | Yes | Sender reference. |
| recipient_references | array | No | Yes | Recipient references. |
| cc_references | array | No | Partial | CC recipient references where applicable. |
| attachment_references | array | No | Yes | Attachment references; not automatically Document/Evidence. |
| customer_reference_id | string | No | Yes | Related Customer reference. |
| order_reference_id | string | No | Partial | Related Order reference. |
| matter_reference_id | string | No | Yes | Related Matter reference. |
| task_reference_id | string | No | Partial | Related Task reference. |
| notification_reference_id | string | No | Partial | Related Notification reference. |
| document_reference_ids | array | No | Partial | Linked Document references where registered. |
| evidence_reference_ids | array | No | Deferred | Linked Evidence references where registered. |
| agent_reference_id | string | No | Partial | Related Agent reference. |
| service_provider_reference_id | string | No | Partial | Related Service Provider reference. |
| delivery_reference_id | string | No | Deferred | External delivery/system reference. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 communication_type

MVP controlled values:

```text
CustomerCommunication
AgentCommunication
ServiceProviderCommunication
PartnerCommunication
InternalCommunication
SystemCommunication
TaskCommunication
MatterCommunication
OrderCommunication
DocumentRequestCommunication
EvidenceRequestCommunication
Other
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Queued
Sent
Received
Failed
Read
Replied
Archived
DeletedReferenceOnly
```

## 7.3 channel

MVP controlled values:

```text
Email
Chat
Phone
Meeting
Portal
System
Webhook
Other
Unknown
```

## 7.4 direction

MVP controlled values:

```text
Inbound
Outbound
Internal
System
Unknown
```

## 7.5 participant_type

Suggested controlled values:

```text
User
CustomerContact
AgentContact
ServiceProviderContact
PartnerContact
SystemActor
AIAgent
Unknown
```

---

# 8. Object Rules

## 8.1 Communication Requires Channel, Direction and Status

Every Communication must define:

```text
communication_type
channel
direction
status
```

A raw message without channel and lifecycle state is not a Core-valid Communication.

## 8.2 Communication Is Not Notification

Notification records awareness intent.

Communication carries message content and conversation lifecycle.

A Notification may create or reference Communication, but they remain separate objects.

## 8.3 Communication Is Not Event

Event records that something meaningful happened.

Communication may emit Events when created, sent, received or failed.

## 8.4 Communication Is Not Document

Communication attachments or generated text do not automatically become Documents.

Document registration must be explicit through Document services.

## 8.5 Communication Is Not Evidence

Communication may contain evidence material.

It becomes Evidence only through Evidence Registration Service with source, purpose and review.

## 8.6 Communication Must Respect Confidentiality and Participants

Communication content, recipients, attachments and related business objects must respect permission, policy, confidentiality and visibility rules.

## 8.7 AI Draft Is Not Approved Communication

AI may draft or summarize communication.

Outbound communication requires governed service and review where policy requires it.

## 8.8 Communication Must Be Auditable

Communication-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
communication creation
message drafting
message sending
message receiving
participant update
attachment linkage
document linkage
evidence linkage
status change
delivery failure
AI draft or summary
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Communication may involve Customer | Customer remains demand-side party. |
| Order | Communication may relate to Order | Order remains commercial request. |
| Matter | Communication may belong to Matter | Matter remains execution container. |
| Task | Communication may support Task | Task remains work unit. |
| Notification | Notification may trigger Communication | Notification remains awareness intent. |
| Event | Communication changes may emit Events | Event remains occurrence record. |
| Document | Communication may link Documents | Document remains artifact. |
| Evidence | Communication may support Evidence registration | Evidence remains proof layer. |
| Agent | Communication may involve Agent | Agent remains collaborator. |
| Service Provider | Communication may involve Provider | Provider remains capability profile. |
| Partner | Communication may involve Partner | Partner remains cooperation relationship. |
| AI Output | AI may draft/summarize | AI Output is not approved Communication. |
| Audit Record | Audit may reference Communication | Audit remains accountability system. |

---

# 10. Lifecycle

Communication lifecycle states:

```text
Draft
Queued
Sent
Received
Failed
Read
Replied
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Queued
Draft → Sent
Queued → Sent
Queued → Failed
Sent → Read
Sent → Replied
Received → Read
Received → Replied
Failed → Queued
Failed → Archived
Sent → Archived
Received → Archived
Read → Archived
Replied → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
DeletedReferenceOnly → Active state
Archived → Sent without restoration/replay control
Failed → Read without successful delivery/receipt trace
Draft AI communication → Sent without governed send service where policy requires review
```

---

# 11. Service Usage

Communication object is created and managed through:

```text
Communication Registration Service
Communication Thread Service
Communication Message Service
Communication Participant Service
Communication Attachment Reference Service
Communication Status Service
Communication Document Link Service
Communication Evidence Link Service
Communication Reference Validation Service
Communication Audit Reference Service
```

Service rules:

```text
- Services must validate communication_type.
- Services must validate channel and direction.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not convert attachments into Documents automatically.
- Services must not convert content into Evidence automatically.
- Services must not bypass Permission, Policy or confidentiality rules.
```

---

# 12. Event Usage

Communication object emits or participates in:

```text
CommunicationCreated
CommunicationUpdated
CommunicationMessageAdded
CommunicationQueued
CommunicationSent
CommunicationReceived
CommunicationRead
CommunicationReplied
CommunicationFailed
CommunicationAttachmentLinked
CommunicationDocumentLinked
CommunicationEvidenceLinked
CommunicationArchived
CommunicationReferenceValidated
```

Event rules:

```text
- Communication events must reference Communication ID.
- Message events must not expose restricted message content unnecessarily.
- Attachment events must preserve attachment reference.
- Document/Evidence link events must reference registered objects.
- AI-drafted communication events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /communications
GET /communications/{id}
PATCH /communications/{id}
POST /communications/{id}/messages
POST /communications/{id}/status
POST /communications/{id}/participants
POST /communications/{id}/attachments
POST /communications/{id}/documents
POST /communications/{id}/evidence
POST /communications/reference/validate
```

API rules:

```text
- APIs must invoke Communication Services.
- APIs must not convert attachments into Documents automatically.
- APIs must not convert content into Evidence automatically.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Communication only under governed Agent Contracts.

Allowed AI use:

```text
draft communication for review
summarize communication thread if authorized
extract action items for review
identify missing reply or follow-up
suggest related Matter, Task, Document or Evidence links
translate communication draft for review
flag confidential or risky content
```

AI must not:

```text
send outbound communication without authorized service
bypass human review where policy requires it
expose confidential content beyond authorized scope
convert attachment into Document automatically
convert message content into Evidence automatically
invent sender, recipient or message facts
treat AI draft as approved Communication
```

AI Communication use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Communication Access Rule
Participant Visibility Rule
Confidentiality Rule
Document Rule where applicable
Evidence Rule where applicable
Audit Rule
Human Review Rule for external communication
```

---

# 15. Validation Rules

Communication object must pass:

```text
[ ] id is present and immutable.
[ ] communication_type is controlled.
[ ] channel is controlled.
[ ] direction is controlled.
[ ] status is controlled.
[ ] Communication does not equal Notification.
[ ] Communication does not equal Event.
[ ] Communication does not equal Document.
[ ] Communication does not equal Evidence.
[ ] Attachments do not become Documents automatically.
[ ] Message content does not become Evidence automatically.
[ ] AI draft does not become approved outbound communication automatically.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite communication domain spec
preserve Communication / Notification boundary
preserve Communication / Event boundary
preserve Communication / Document boundary
preserve Communication / Evidence boundary
implement only Phase 4 MVP fields unless task says otherwise
write tests for required communication_type
write tests for controlled channel
write tests for controlled direction
write tests for controlled status
write tests preventing Communication from becoming Notification or Event
write tests preventing attachment from becoming Document automatically
write tests preventing message content from becoming Evidence automatically
write tests preventing AI draft from being sent without governed service
write tests for event emission on mutation
```

Codex must not:

```text
invent full email/chat gateway in Phase 4 MVP
treat Communication as Notification
treat Communication as Event
treat Communication as Document
treat Communication as Evidence
send external communication directly from AI output
store sensitive message content inline by default
allow product UI to redefine Communication status
```

---

# 17. Acceptance Criteria

This Communication Object Specification is accepted only if:

```text
[ ] It defines Communication purpose.
[ ] It defines Communication Core meaning.
[ ] It identifies Communication as Business Execution Object.
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
| 0.1.0 | Draft | Initial Communication object specification. Establishes Communication as message and conversation lifecycle object, separates Communication from Notification, Event, Document and Evidence, and defines Phase 4 MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
