# Service Specification — Communication Service

**Spec ID:** B02-SVC-COMMUNICATION-SERVICE  
**Spec Type:** Service  
**Service Name:** Communication Service  
**Owning Domain:** Communication  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/communication.md  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/notification.md; core-specs/objects/event.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/customer.md; core-specs/objects/agent.md; core-specs/objects/document.md; core-specs/objects/evidence.md  
**Related Service Specs:** core-specs/services/notification-service.md; core-specs/services/event-service.md; core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/customer-service.md; core-specs/services/agent-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/communication-created.md; core-specs/events/communication-updated.md; core-specs/events/communication-status-changed.md; core-specs/events/communication-sent.md; core-specs/events/communication-received.md; core-specs/events/communication-participant-linked.md; core-specs/events/communication-document-linked.md; core-specs/events/communication-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/communication/communication-contract.md; core-specs/contracts/communication/communication-reference-contract.md; core-specs/contracts/communication/communication-participant-contract.md; core-specs/contracts/communication/communication-message-contract.md; core-specs/contracts/communication/communication-attachment-contract.md; core-specs/contracts/communication/communication-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Network and Growth Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication Service defines the Core service boundary for creating, updating, validating, linking and managing Communication objects and message/conversation lifecycle references.

It exists so that Notification, Event, Task, Matter, Customer, Agent, Service Provider, Document, Evidence, AI Agents, APIs and product consumers can consistently reference message content and conversation context without confusing Communication with Notification, Event, Document, Evidence, marketing automation, external gateway implementation or informal chat logs.

Communication Service is required before:

```text
customer communication tracking
agent communication tracking
service provider communication tracking
matter conversation context
task-related message handling
notification delivery handoff
document attachment registration
communication-to-document linkage
communication-to-evidence suggestion
AI-assisted email/message drafting and summary
audit trace for communication-sensitive actions
```

---

# 2. Core Meaning

Communication Service means:

```text
the Core service that manages governed message and conversation records, including participants, content references, channel context, status, attachments, related objects, delivery state and audit trace.
```

Communication Service does not mean:

```text
Notification Service
Event Service
Document Service
Evidence Service
email gateway by itself
chat gateway by itself
marketing automation system
CRM activity feed by itself
ungoverned chat log
```

Communication Service answers:

```text
Does this Communication exist?
Who participated?
Which channel or message context applies?
Which Matter, Task, Customer, Agent or Provider does it relate to?
Which attachments, Documents or Evidence references are linked?
What status applies?
Was it drafted, sent, received, failed, archived or review-required?
Can another domain safely reference this Communication?
What audit trace is required?
```

---

# 3. Service Category

Communication Service is a Collaboration Network Core Service.

It manages message and conversation lifecycle.

It does not create awareness intent.

It does not record source occurrence.

It does not convert attachments into Documents or Evidence automatically.

It does not implement external gateway details by itself.

---

# 4. Architectural Position

Communication Service sits after Notification and alongside Matter/Task collaboration.

```text
Event records occurrence
        ↓
Notification creates awareness intent
        ↓
Communication Service manages message/conversation lifecycle
        ↓
Participants exchange content
        ↓
Document Service may register attachments as Documents
        ↓
Evidence Service may register proof purpose where applicable
```

Notification asks for awareness.

Communication carries message content.

Document registers artifacts.

Evidence registers proof purpose.

---

# 5. Scope

Communication Service includes:

```text
communication creation
communication update
communication status management
communication participant linkage
communication channel reference
communication message content reference
communication attachment linkage
communication document linkage
communication evidence linkage
communication matter/task/customer/agent/provider linkage
communication send/receive status tracking
communication reference validation
communication audit trace
communication event emission
```

MVP/Phase 4 scope includes:

```text
create communication
get communication
update communication metadata
change communication status
link participants
link communication to matter/task/customer/agent
link attachments
link document references
record sent/received status
validate communication reference
emit communication events
```

Deferred scope includes:

```text
full email client
chat system
external gateway implementation
marketing campaign automation
mass mailing
automatic evidence conversion
automatic document approval
advanced communication analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createCommunication | Create Communication object | Yes | CommunicationCreated |
| getCommunication | Retrieve Communication by ID | Yes | No |
| updateCommunication | Update governed metadata | Yes | CommunicationUpdated |
| changeCommunicationStatus | Change lifecycle status | Yes | CommunicationStatusChanged |
| linkCommunicationParticipant | Link participant reference | Yes | CommunicationParticipantLinked |
| unlinkCommunicationParticipant | Remove participant link | Partial | CommunicationParticipantUnlinked |
| linkCommunicationMatter | Link Communication to Matter | Yes | CommunicationMatterLinked |
| linkCommunicationTask | Link Communication to Task | Partial | CommunicationTaskLinked |
| linkCommunicationCustomer | Link Communication to Customer | Yes | CommunicationCustomerLinked |
| linkCommunicationAgent | Link Communication to Agent | Yes | CommunicationAgentLinked |
| linkCommunicationAttachment | Link attachment reference | Yes | CommunicationAttachmentLinked |
| linkCommunicationDocument | Link registered Document | Yes | CommunicationDocumentLinked |
| linkCommunicationEvidence | Link registered Evidence | Partial | CommunicationEvidenceLinked |
| recordCommunicationSent | Record sent status | Yes | CommunicationSent |
| recordCommunicationReceived | Record received status | Yes | CommunicationReceived |
| validateCommunicationReference | Validate whether Communication can be referenced | Yes | CommunicationReferenceValidated |
| archiveCommunication | Archive Communication reference | Partial | CommunicationArchived |

---

# 7. Inputs

Communication Service accepts:

```text
communication_type
conversation_reference
message_reference
subject_reference
status
direction
channel_reference
participant_references
sender_reference
recipient_references
matter_reference_id
task_reference_id
customer_reference_id
agent_reference_id
service_provider_reference_id
notification_reference_id
event_reference_id
attachment_references
document_reference_ids
evidence_reference_ids
confidentiality_level
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
communication_type
status
direction
channel_reference
participant_references
source_reference
actor_context
```

Required for participant linkage:

```text
communication_reference_id
participant_reference
participant_role
actor_context
```

Required for send/receive recording:

```text
communication_reference_id
channel_reference
delivery_context
actor_context
```

Required for validation:

```text
communication_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Communication Service returns:

```text
Communication object
Communication reference
Communication validation result
Communication participant link result
Communication attachment link result
Communication document/evidence link result
Communication status result
Communication delivery status result
Communication event reference
error result
```

Validation output must include:

```text
is_valid
communication_reference_id
communication_type
status
direction
channel_reference
participant_hint where applicable
reason_code
confidentiality_hint where applicable
policy_hint where applicable
```

Validation output must not expose restricted message content, attachments or confidential customer/matter information unnecessarily.

---

# 9. Controlled Values

## 9.1 communication_type

```text
Email
Chat
CallNote
MeetingNote
SystemMessage
PortalMessage
AgentMessage
CustomerMessage
OfficialCommunication
InternalNote
Other
Unknown
```

## 9.2 status

```text
Draft
ReviewRequired
ReadyToSend
Sent
Received
Failed
Bounced
Replied
Closed
Archived
DeletedReferenceOnly
```

## 9.3 direction

```text
Inbound
Outbound
Internal
SystemGenerated
Unknown
```

## 9.4 participant_role

```text
Sender
Recipient
Cc
Bcc
Participant
Observer
Owner
Reviewer
Unknown
```

## 9.5 channel_reference

Suggested controlled values:

```text
Email
Phone
WhatsApp
WeChat
Portal
Slack
Feishu
OfficialPortal
ManualRecord
System
Unknown
```

## 9.6 validation_result

```text
Valid
Invalid
NotFound
ReviewRequired
Failed
Archived
ConfidentialityRestricted
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Communication Carries Message and Conversation Lifecycle

Communication Service manages governed message/conversation records.

It must not be reduced to Notification, Event or raw chat log.

## 10.2 Communication Is Not Notification

Notification represents awareness intent.

Communication represents message content and delivery/conversation lifecycle.

## 10.3 Communication Is Not Event

Event records occurrence.

Communication may emit or reference Events but must not replace Event Service.

## 10.4 Attachment Is Not Document Automatically

Attachments may be linked.

They become Documents only through Document Service.

## 10.5 Attachment or Message Is Not Evidence Automatically

Communication content or attachment may support Evidence.

Evidence Service owns proof purpose and review.

## 10.6 External Send Must Respect Policy

Outbound communication must respect Permission, Policy, confidentiality, target access and review requirements.

## 10.7 AI Draft Is Not Sent Communication

AI may draft or summarize.

Sending, external delivery or official submission requires authorized Communication Service operation and policy review.

## 10.8 Communication Changes Must Be Auditable

Communication-sensitive operations must preserve actor, source, request context, participants, channel, status and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Notification Service | May request communication delivery | Notification owns awareness intent. |
| Event Service | May record communication events | Event records occurrence. |
| Matter Service | Communication may link to Matter | Matter owns execution container. |
| Task Service | Communication may support Task | Task owns work unit. |
| Customer Service | Communication may include Customer | Customer owns demand-side party. |
| Agent Service | Communication may include Agent | Agent owns collaborator profile. |
| Service Provider Service | Communication may include Provider | Provider owns provider profile. |
| Document Service | Attachments may become Documents | Document owns artifact lifecycle. |
| Evidence Service | Communication may support Evidence | Evidence owns proof layer. |
| Policy Service | Controls send/visibility | Policy owns contextual constraints. |
| AI Agent Governance | AI may draft/summarize | Agent Contract governs AI use. |
| Audit Service | Records Communication-sensitive action | Audit owns accountability trail. |

---

# 12. Event Usage

Communication Service emits:

```text
CommunicationCreated
CommunicationUpdated
CommunicationStatusChanged
CommunicationParticipantLinked
CommunicationParticipantUnlinked
CommunicationMatterLinked
CommunicationTaskLinked
CommunicationCustomerLinked
CommunicationAgentLinked
CommunicationAttachmentLinked
CommunicationDocumentLinked
CommunicationEvidenceLinked
CommunicationSent
CommunicationReceived
CommunicationFailed
CommunicationArchived
CommunicationReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Participant events must not expose unnecessary contact details.
- Sent/received events must preserve channel reference and status.
- Attachment events must not expose restricted file content.
- AI-drafted communication events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /communications
GET /communications/{id}
PATCH /communications/{id}
POST /communications/{id}/status
POST /communications/{id}/participants
DELETE /communications/{id}/participants/{participantId}
POST /communications/{id}/matters
POST /communications/{id}/tasks
POST /communications/{id}/customers
POST /communications/{id}/agents
POST /communications/{id}/attachments
POST /communications/{id}/documents
POST /communications/{id}/evidence
POST /communications/{id}/sent
POST /communications/{id}/received
POST /communications/reference/validate
```

API rules:

```text
- APIs must invoke Communication Service operations.
- APIs must not implement external email/chat gateways directly unless an integration service is explicitly approved.
- APIs must not convert attachments into Documents/Evidence automatically.
- APIs must not bypass outbound review or policy.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Communication Service only under governed Agent Contracts.

Allowed AI use:

```text
draft outbound message for review
summarize inbound communication
extract action items for Task Service review
identify missing response
suggest participant linkage
suggest document registration from attachment
suggest evidence registration from communication content
flag confidentiality or policy risks
prepare communication timeline summary
```

AI must not:

```text
send external communication without authorization
create official submission directly
convert attachment into Document automatically
convert message into Evidence automatically
hide AI-generated draft source
invent message content or sender identity
expose restricted communication content
bypass outbound review or policy
```

AI Communication use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Communication Access Rule
Participant Access Rule
Document/Evidence Rule where applicable
Confidentiality Rule
Audit Rule
Human Review Rule for external-facing or official communication
```

---

# 15. Validation Rules

Communication Service must enforce:

```text
[ ] communication_type is controlled.
[ ] status is controlled.
[ ] direction is controlled.
[ ] createCommunication requires channel_reference.
[ ] createCommunication requires participant_references.
[ ] createCommunication produces stable immutable Communication ID.
[ ] updateCommunication does not mutate immutable ID.
[ ] changeCommunicationStatus follows allowed lifecycle.
[ ] recordCommunicationSent requires outbound authorization and policy pass.
[ ] validateCommunicationReference rejects missing, failed, archived or deleted-reference communications where not allowed.
[ ] Communication Service does not replace Notification or Event.
[ ] Communication Service does not convert attachments into Documents/Evidence automatically.
[ ] AI draft does not equal sent Communication.
[ ] Communication Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Communication Service should return controlled errors:

```text
CommunicationNotFound
InvalidCommunicationType
InvalidCommunicationStatus
InvalidCommunicationDirection
InvalidCommunicationTransition
ChannelReferenceRequired
ParticipantReferenceRequired
InvalidParticipantReference
MatterNotFound
TaskNotFound
CustomerNotFound
AgentNotFound
ServiceProviderNotFound
AttachmentReferenceInvalid
DocumentNotFound
EvidenceNotFound
OutboundReviewRequired
DeliveryFailed
ConfidentialityRestricted
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownCommunicationError
```

Errors must be safe for product display and API consumption.

Restricted message content, attachments, customer data and professional strategy must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite communication domain spec
cite communication object spec
cite notification, event, document and evidence specs where relevant
preserve Communication / Notification boundary
preserve Communication / Event boundary
preserve Communication / Document boundary
preserve Communication / Evidence boundary
preserve Communication / Gateway boundary
implement only Phase 4 MVP operations unless task says otherwise
write tests for createCommunication requiring channel_reference
write tests for createCommunication requiring participant_references
write tests for controlled communication_type, status and direction
write tests preventing attachment from becoming Document automatically
write tests preventing message/attachment from becoming Evidence automatically
write tests preventing AI draft from being marked Sent automatically
write tests preventing outbound send without Permission/Policy
write tests for event emission on mutation
```

Codex must not:

```text
invent full email/chat client in Phase 4
treat Communication as Notification
treat Communication as Event
implement external gateway details inside Communication Service
convert attachments into Documents or Evidence automatically
send official or external messages without authorization
allow AI to impersonate sender or fabricate communication
allow product UI to redefine Communication status
```

---

# 18. Acceptance Criteria

This Communication Service Specification is accepted only if:

```text
[ ] It defines Communication Service purpose.
[ ] It defines Communication Service Core meaning.
[ ] It identifies Communication Service as Collaboration Network Core Service.
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
| 0.1.0 | Draft | Initial Communication Service specification. Establishes Communication Service as governed message/conversation lifecycle service, separates Communication from Notification, Event, Document, Evidence and gateways, and defines Phase 4 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
