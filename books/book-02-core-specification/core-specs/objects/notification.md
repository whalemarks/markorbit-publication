# Object Specification — Notification

**Spec ID:** B02-OBJ-NOTIFICATION  
**Spec Type:** Object  
**Object Name:** Notification  
**Owning Domain:** Notification  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-16 — Core Execution Primitives; B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/notification.md  
**Related Object Specs:** core-specs/objects/event.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/communication.md; core-specs/objects/notification-recipient.md; core-specs/objects/notification-template.md; core-specs/objects/notification-status.md; core-specs/objects/notification-preference.md  
**Related Service Specs:** core-specs/services/notification-registration-service.md; core-specs/services/notification-recipient-service.md; core-specs/services/notification-status-service.md; core-specs/services/notification-delivery-reference-service.md; core-specs/services/notification-reference-validation-service.md  
**Related Event Specs:** core-specs/events/notification-created.md; core-specs/events/notification-queued.md; core-specs/events/notification-delivered.md; core-specs/events/notification-failed.md; core-specs/events/notification-dismissed.md; core-specs/events/notification-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/notification/notification-contract.md; core-specs/contracts/notification/notification-recipient-contract.md; core-specs/contracts/notification/notification-template-contract.md; core-specs/contracts/notification/notification-delivery-contract.md; core-specs/contracts/notification/notification-preference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Notification object defines the Core-recognized awareness intent used to inform a recipient that something requires attention, awareness, review, action or acknowledgement.

It exists so that Events, Tasks, Matters, Workflow Contracts, Communications, Users, Customers, Agents, Service Providers, AI Agents, Services, APIs and product consumers can consistently create, queue, route, deliver, dismiss and audit awareness signals without confusing Notification with Event, Communication, Task, marketing message or messaging gateway.

Notification is required before:

```text
task assignment awareness
matter status awareness
workflow transition awareness
document/evidence review reminder
customer input reminder
agent follow-up reminder
deadline awareness
AI-generated attention suggestion
in-app alert
email/push/SMS delivery reference
audit trace for awareness delivery
```

---

# 2. Core Meaning

Notification means:

```text
a Core-recognized awareness intent directed to one or more recipients, triggered by an event, workflow, task, matter, policy or service context, with status, recipient, delivery reference and audit trace.
```

Notification is not:

```text
Event
Communication
Task
Workflow
Marketing campaign
Messaging gateway
Email message itself
Chat message itself
AI Output
Audit Record
```

Notification answers:

```text
Who should be made aware?
What should they be aware of?
Which event, task, matter, workflow or service caused the awareness intent?
Which channel or delivery reference may apply?
Has it been queued, delivered, failed, read, dismissed or archived?
What preference or policy applies?
What audit trace is required?
```

---

# 3. Object Category

Notification is a Business Execution Object owned by the Notification Domain.

It is the awareness intent layer.

Event records what happened.

Communication carries message content and conversation lifecycle.

Task represents actionable work.

Notification must preserve these boundaries.

---

# 4. Architectural Position

Notification sits after meaningful occurrence and before awareness delivery.

```text
Event / Workflow / Task / Matter indicates attention need
        ↓
Notification records awareness intent
        ↓
Recipient and preference rules are evaluated
        ↓
Delivery reference may be created
        ↓
Communication may carry content where conversation is needed
        ↓
Event and Audit preserve trace
```

Notification informs.

It does not execute work.

It does not replace Communication.

---

# 5. Scope

The Notification object includes:

```text
notification id
notification type
notification status
notification title/reference
notification body/reference
trigger source reference
event reference
task reference
matter reference
workflow reference
recipient references
recipient type
priority
delivery channel reference
delivery status reference
delivery attempt reference
preference reference
policy reference
communication reference
created time
updated time
audit metadata
```

MVP / Phase 3 partial scope includes:

```text
notification id
notification type
notification status
title/reference
body/reference
trigger source reference
event reference
task reference
matter reference
recipient references
priority
delivery channel reference
communication reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Notification ID. |
| notification_type | enum | Yes | Yes | Controlled notification type. |
| title_reference | string | Yes | Yes | Human-readable title/reference. |
| body_reference | string | No | Yes | Body/content reference; avoid storing sensitive content where possible. |
| status | enum | Yes | Yes | Controlled Notification status. |
| trigger_source_type | enum | Yes | Yes | Event, Task, Matter, Workflow, Policy, System, AI, Manual, Unknown. |
| trigger_source_reference_id | string | No | Yes | Source object reference. |
| event_reference_id | string | No | Yes | Related Event reference where applicable. |
| task_reference_id | string | No | Partial | Related Task reference. |
| matter_reference_id | string | No | Partial | Related Matter reference. |
| workflow_contract_reference_id | string | No | Partial | Related Workflow Contract reference. |
| recipient_references | array | Yes | Yes | Recipient references. |
| recipient_type | enum | Yes | Yes | User, CustomerContact, AgentContact, ServiceProviderContact, Team, SystemActor, Unknown. |
| priority | enum | No | Yes | Notification priority. |
| delivery_channel | enum | No | Partial | InApp, Email, SMS, Push, Chat, Webhook, None, Unknown. |
| delivery_status | enum | No | Partial | Queued, Delivered, Failed, Read, Dismissed, Unknown. |
| delivery_reference_id | string | No | Deferred | Gateway or delivery reference. |
| preference_reference_id | string | No | Deferred | Notification preference reference. |
| policy_reference_id | string | No | Partial | Policy governing delivery/visibility. |
| communication_reference_id | string | No | Partial | Communication reference where message/conversation is created. |
| source_reference | string | No | Yes | Intake/system/source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 notification_type

MVP controlled values:

```text
TaskAssigned
TaskDue
TaskBlocked
MatterStatusChanged
WorkflowTransition
ReviewRequired
ApprovalRequired
DocumentRequired
EvidenceRequired
CustomerInputRequired
AgentFollowUpRequired
DeadlineAwareness
SystemAlert
AIAttentionSuggestion
Other
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Created
Queued
Delivered
Read
Dismissed
Failed
Cancelled
Archived
DeletedReferenceOnly
```

## 7.3 trigger_source_type

MVP controlled values:

```text
Event
Task
Matter
Workflow
Policy
System
AI
Manual
Unknown
```

## 7.4 recipient_type

MVP controlled values:

```text
User
Team
CustomerContact
AgentContact
ServiceProviderContact
PartnerContact
SystemActor
Unknown
```

## 7.5 priority

MVP controlled values:

```text
Low
Normal
High
Urgent
Unknown
```

## 7.6 delivery_channel

Suggested controlled values:

```text
InApp
Email
SMS
Push
Chat
Webhook
None
Unknown
```

---

# 8. Object Rules

## 8.1 Notification Requires Recipient and Type

Every Notification must define:

```text
notification_type
recipient_references
recipient_type
status
```

A message without recipient intent is not a Core-valid Notification.

## 8.2 Notification Is Not Event

Event records that something happened.

Notification records awareness intent that may be triggered by Event.

## 8.3 Notification Is Not Communication

Communication carries message content and conversation lifecycle.

Notification may create or reference Communication when message content or reply lifecycle is required.

## 8.4 Notification Is Not Task

Task is actionable work.

Notification may inform an assignee or reviewer about a Task, but it does not execute or complete the Task.

## 8.5 Notification Does Not Own Messaging Gateway

Notification may reference delivery channel or delivery result.

Gateway, email, SMS, push and chat delivery implementations are outside Notification object ownership.

## 8.6 Notification Must Respect Preferences and Policy

Notification delivery must respect recipient preference, policy, permission, confidentiality and visibility rules where applicable.

## 8.7 Notification Must Be Auditable

Notification-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
notification creation
recipient resolution
status change
delivery channel assignment
delivery attempt
delivery failure
read/dismiss action
communication linkage
AI attention suggestion
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Event | Notification may be triggered by Event | Event remains occurrence record. |
| Task | Notification may inform about Task | Task remains work unit. |
| Matter | Notification may inform about Matter | Matter remains execution container. |
| Workflow Contract | Notification may relate to transition | Workflow owns transition rules. |
| Communication | Notification may create/reference Communication | Communication remains message lifecycle. |
| User | Notification may target User | User remains account participant. |
| Customer Contact | Notification may target customer contact | Customer remains demand-side party. |
| Agent | Notification may target agent contact | Agent remains collaborator. |
| Service Provider | Notification may target provider contact | Provider remains capability profile. |
| Policy | Policy may constrain delivery | Policy remains contextual rule. |
| AI Output | AI may suggest attention | AI Output is not Notification by itself. |
| Audit Record | Audit may reference Notification | Audit remains accountability system. |

---

# 10. Lifecycle

Notification lifecycle states:

```text
Draft
Created
Queued
Delivered
Read
Dismissed
Failed
Cancelled
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Created
Created → Queued
Created → Cancelled
Queued → Delivered
Queued → Failed
Delivered → Read
Delivered → Dismissed
Read → Archived
Dismissed → Archived
Failed → Queued
Failed → Cancelled
Cancelled → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
DeletedReferenceOnly → Active state
Archived → Delivered without restoration/replay control
Cancelled → Delivered without recreation or restoration
Read → Queued without new notification instance
```

---

# 11. Service Usage

Notification object is created and managed through:

```text
Notification Registration Service
Notification Recipient Service
Notification Status Service
Notification Preference Service
Notification Delivery Reference Service
Notification Communication Link Service
Notification Reference Validation Service
Notification Audit Reference Service
```

Service rules:

```text
- Services must validate notification_type.
- Services must validate recipient references.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not execute Task or Matter work.
- Services must not send Communication unless Communication service is invoked.
- Services must not implement external gateway delivery directly unless explicitly scoped.
```

---

# 12. Event Usage

Notification object emits or participates in:

```text
NotificationCreated
NotificationQueued
NotificationDelivered
NotificationFailed
NotificationRead
NotificationDismissed
NotificationCancelled
NotificationArchived
NotificationCommunicationLinked
NotificationReferenceValidated
```

Event rules:

```text
- Notification events must reference Notification ID.
- Delivery events must preserve channel/reference where allowed.
- Failure events must preserve failure reason where allowed.
- Recipient details must not be exposed unnecessarily.
- AI-generated attention events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 3 partial APIs:

```text
POST /notifications
GET /notifications/{id}
PATCH /notifications/{id}
POST /notifications/{id}/status
POST /notifications/{id}/recipients
POST /notifications/{id}/delivery-reference
POST /notifications/{id}/communication
POST /notifications/reference/validate
```

API rules:

```text
- APIs must invoke Notification Services.
- APIs must not execute Task or Matter work.
- APIs must not send Communication directly unless Communication service is invoked.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Notification only under governed Agent Contracts.

Allowed AI use:

```text
suggest attention-worthy notification
summarize notification backlog
identify overdue/unread notifications
suggest recipient for review
draft notification text for review
flag duplicate or noisy notifications
explain notification source based on event/task/matter context
```

AI must not:

```text
send notification without authorized service
bypass recipient preference or policy
expose confidential matter/document/evidence details
convert notification into communication without Communication service
execute Task or Matter action from notification
invent event source
create external delivery without governed channel
```

AI Notification use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Notification Access Rule
Recipient Visibility Rule
Communication Rule where applicable
Audit Rule
Human Review Rule for external or high-risk notifications
```

---

# 15. Validation Rules

Notification object must pass:

```text
[ ] id is present and immutable.
[ ] notification_type is controlled.
[ ] title_reference is present.
[ ] status is controlled.
[ ] recipient_references are present.
[ ] recipient_type is controlled.
[ ] trigger_source_type is controlled.
[ ] Notification does not equal Event.
[ ] Notification does not equal Communication.
[ ] Notification does not equal Task.
[ ] Notification does not own messaging gateway.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite notification domain spec
preserve Notification / Event boundary
preserve Notification / Communication boundary
preserve Notification / Task boundary
preserve Notification / Gateway boundary
implement only Phase 3 Partial fields unless task says otherwise
write tests for required notification_type
write tests for required recipient_references
write tests for controlled recipient_type
write tests for controlled status
write tests preventing Notification from becoming Communication
write tests preventing Notification from executing Task/Matter work
write tests preventing gateway delivery implementation unless explicitly scoped
write tests for event emission on mutation
```

Codex must not:

```text
invent full notification platform in Phase 3 Partial scope
treat Notification as Event
treat Notification as Communication
treat Notification as Task
send external messages directly from Notification object
bypass recipient preferences or policy
allow AI to send external notifications without governed service
allow product UI to redefine Notification status
```

---

# 17. Acceptance Criteria

This Notification Object Specification is accepted only if:

```text
[ ] It defines Notification purpose.
[ ] It defines Notification Core meaning.
[ ] It identifies Notification as Business Execution Object.
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
| 0.1.0 | Draft | Initial Notification object specification. Establishes Notification as awareness intent, separates Notification from Event, Communication, Task and messaging gateways, and defines Phase 3 Partial fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
