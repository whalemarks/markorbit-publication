# Object Specification — Event

**Spec ID:** B02-OBJ-EVENT  
**Spec Type:** Object  
**Object Name:** Event  
**Owning Domain:** Event  
**Domain Category:** Business Execution Domain  
**Source Chapter:** B02-CH-16 — Core Execution Primitives; B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/event.md  
**Related Object Specs:** core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/workflow-contract.md; core-specs/objects/notification.md; core-specs/objects/communication.md; core-specs/objects/event-type.md; core-specs/objects/event-payload.md; core-specs/objects/event-source.md  
**Related Service Specs:** core-specs/services/event-registration-service.md; core-specs/services/event-publication-service.md; core-specs/services/event-subscription-service.md; core-specs/services/event-reference-validation-service.md; core-specs/services/event-audit-reference-service.md  
**Related Event Specs:** core-specs/events/event-created.md; core-specs/events/event-published.md; core-specs/events/event-consumed.md; core-specs/events/event-failed.md; core-specs/events/event-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/event/event-contract.md; core-specs/contracts/event/event-payload-contract.md; core-specs/contracts/event/event-publication-contract.md; core-specs/contracts/event/event-subscription-contract.md; core-specs/contracts/event/event-audit-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Wave:** Wave 3  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Event object defines the Core-recognized record that something meaningful happened inside MarkOrbit.

It exists so that Domains, Objects, Services, Workflow Contracts, Tasks, Matters, Notifications, Communications, AI Agents, APIs and product consumers can consistently record, publish, consume and audit meaningful state changes or business/professional signals without confusing Event with workflow logic, task execution, notification delivery, communication message or implementation log.

Event is required before:

```text
state change recording
workflow transition trace
task status change trace
matter status change trace
order conversion trace
document/evidence review trace
notification triggering
integration signaling
AI action trace
audit-friendly execution history
event-driven product consumption
Codex implementation of safe service mutations
```

---

# 2. Core Meaning

Event means:

```text
a Core-recognized immutable or append-only signal that records that a meaningful domain, object, service, workflow, task, communication, notification or AI-related occurrence happened.
```

Event is not:

```text
Workflow
Task
Notification
Communication
Audit Record
Implementation log
Debug log
Queue message only
AI Output
Service command
```

Event answers:

```text
What happened?
When did it happen?
Which object or domain did it affect?
Who or what caused it?
Which service or workflow emitted it?
What payload is allowed?
Which consumers may react to it?
Which Notification, Communication, Audit or downstream workflow may reference it?
```

---

# 3. Object Category

Event is a Business Execution Object owned by the Event Domain.

It is an execution primitive.

It records meaningful occurrences.

It does not execute work, notify users, send messages or define workflow structure by itself.

---

# 4. Architectural Position

Event sits after service action and before downstream reaction.

```text
Service performs governed action
        ↓
Object state may change
        ↓
Event records meaningful occurrence
        ↓
Workflow / Notification / Integration / Audit may consume Event
        ↓
Product UI may display event history
```

Event records.

Notification informs.

Communication carries content.

Audit governs accountability.

---

# 5. Scope

The Event object includes:

```text
event id
event type
event category
event status
source domain
source object type
source object reference
actor reference
service reference
workflow contract reference
task/matter/order reference
event payload reference
correlation reference
causation reference
occurred time
published time
consumed time reference
failure reference
visibility/audience reference
created time
audit metadata
```

MVP scope includes:

```text
event id
event type
event category
event status
source domain
source object type
source object reference
actor reference
service reference
payload reference
correlation reference
causation reference
occurred time
created time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Event ID. |
| event_type | string/enum | Yes | Yes | Controlled or registered event type. |
| event_category | enum | Yes | Yes | Domain, Workflow, Task, Notification, Communication, AI, System, Integration, Unknown. |
| status | enum | Yes | Yes | Controlled Event status. |
| source_domain | string | Yes | Yes | Domain emitting or owning event. |
| source_object_type | string | Yes | Yes | Object type affected or referenced. |
| source_object_reference_id | string | Yes | Yes | Primary object reference. |
| actor_reference_id | string | No | Yes | Identity/User/System/Agent actor reference. |
| service_reference | string | No | Yes | Service that emitted event. |
| workflow_contract_reference_id | string | No | Partial | Workflow Contract reference where applicable. |
| matter_reference_id | string | No | Partial | Related Matter reference. |
| task_reference_id | string | No | Partial | Related Task reference. |
| order_reference_id | string | No | Partial | Related Order reference. |
| payload_reference | object/string | No | Yes | Payload or payload reference, governed by contract. |
| correlation_id | string | No | Yes | Correlation trace across related actions. |
| causation_id | string | No | Yes | Prior event/command causing this event. |
| occurred_at | datetime | Yes | Yes | Time the occurrence happened. |
| published_at | datetime | No | Partial | Time event was published. |
| consumed_reference_ids | array | No | Deferred | Consumer references, if tracked. |
| failure_reference | string | No | Deferred | Failure reference, if publication/consumption failed. |
| visibility | enum | No | Partial | Internal, CustomerVisible, ProviderVisible, SystemOnly, Restricted. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Event creation timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 event_category

MVP controlled values:

```text
Domain
Workflow
Task
Matter
Order
Document
Evidence
Notification
Communication
AI
System
Integration
Unknown
```

## 7.2 status

MVP controlled values:

```text
Recorded
PendingPublication
Published
Consumed
Failed
Ignored
Archived
```

## 7.3 visibility

Suggested controlled values:

```text
Internal
CustomerVisible
ProviderVisible
PartnerVisible
SystemOnly
Restricted
Unknown
```

## 7.4 payload_policy

Suggested controlled values:

```text
InlineSafePayload
ReferenceOnlyPayload
RestrictedPayload
NoPayload
Unknown
```

---

# 8. Object Rules

## 8.1 Event Requires Type and Source

Every Event must define:

```text
event_type
source_domain
source_object_type
source_object_reference_id
occurred_at
```

An occurrence without source and type is not a Core-valid Event.

## 8.2 Event Is Not Workflow

Workflow Contract defines allowed execution structure.

Event records that a workflow-related occurrence happened.

## 8.3 Event Is Not Task

Task is an actionable work unit.

Event may record task creation, assignment, status change or completion.

## 8.4 Event Is Not Notification

Notification is awareness intent.

Event may trigger Notification.

Event itself does not deliver awareness to users.

## 8.5 Event Is Not Communication

Communication carries message content and conversation lifecycle.

Event may record that Communication was created, sent, received or failed.

## 8.6 Event Is Not Implementation Log

Only meaningful business, professional, workflow, integration or AI occurrences should become Core Events.

Debug logs, low-level server logs and trace logs are not Core Events by default.

## 8.7 Event Must Be Append-Oriented

Event should be immutable or append-only.

Corrections should produce correction events rather than silently editing historical events, unless policy explicitly allows metadata repair.

## 8.8 Event Must Be Payload-Governed

Payload must follow event payload contracts.

Sensitive content should use reference-only payloads.

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Matter | Matter changes may emit Events | Matter remains execution container. |
| Task | Task changes may emit Events | Task remains work unit. |
| Workflow Contract | Workflow transitions may emit Events | Workflow owns rules. |
| Order | Order changes may emit Events | Order remains commercial request. |
| Document | Document changes may emit Events | Document remains artifact. |
| Evidence | Evidence changes may emit Events | Evidence remains proof layer. |
| Notification | Event may trigger Notification | Notification remains awareness intent. |
| Communication | Event may record Communication occurrence | Communication remains message lifecycle. |
| AI Agent | AI actions may emit Events | AI Output is not Event. |
| Service | Services emit Events | Services perform action. |
| Audit Record | Audit may reference Events | Audit remains accountability system. |

---

# 10. Lifecycle

Event lifecycle states:

```text
Recorded
PendingPublication
Published
Consumed
Failed
Ignored
Archived
```

Lifecycle rules:

```text
Recorded → PendingPublication
Recorded → Published
PendingPublication → Published
Published → Consumed
PendingPublication → Failed
Published → Failed
Failed → Published
Published → Ignored
Consumed → Archived
Ignored → Archived
Failed → Archived
```

Prohibited lifecycle behavior:

```text
Consumed → Recorded
Archived → Published without replay/restoration control
Failed → Consumed without successful publication/consumption trace
```

Event lifecycle is not the same as the lifecycle of the source object.

---

# 11. Service Usage

Event object is created and managed through:

```text
Event Registration Service
Event Publication Service
Event Subscription Service
Event Consumption Tracking Service
Event Payload Validation Service
Event Reference Validation Service
Event Audit Reference Service
```

Service rules:

```text
- Services must validate event_type.
- Services must validate source object reference.
- Services must validate payload contract.
- Services must preserve correlation_id and causation_id where available.
- Services must not execute workflow transitions directly.
- Services must not send notifications directly unless Notification service is invoked.
- Services must not send communications directly unless Communication service is invoked.
```

---

# 12. Event Usage

Event object emits or participates in meta-events only where useful:

```text
EventCreated
EventRecorded
EventPublished
EventConsumed
EventFailed
EventIgnored
EventArchived
EventReferenceValidated
```

Event rules:

```text
- Meta-events should be used sparingly.
- Event publication and failure may be recorded for audit and integration trace.
- Event payload must not expose restricted content unnecessarily.
- AI-generated or AI-caused events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 3 APIs:

```text
POST /events
GET /events/{id}
GET /events?sourceObjectReferenceId={id}
POST /events/{id}/publish
POST /events/{id}/consume
POST /events/{id}/fail
POST /events/reference/validate
```

API rules:

```text
- APIs must invoke Event Services.
- APIs must not mutate source object state directly.
- APIs must not execute workflow, task, notification or communication action directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Event only under governed Agent Contracts.

Allowed AI use:

```text
summarize event history
identify unusual event sequence
explain why a status changed based on events
detect missing expected event
suggest audit review where event chain is incomplete
generate timeline draft for human review
flag AI-caused events for review
```

AI must not:

```text
create false historical events
rewrite event history silently
treat debug logs as Core Events
execute workflow transition from event history alone
send notifications or communications directly from Event access
expose restricted event payload
treat event timeline as final legal conclusion
```

AI Event use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Event Access Rule
Payload Visibility Rule
Audit Rule
Human Review Rule for correction, replay or compliance-sensitive timelines
```

---

# 15. Validation Rules

Event object must pass:

```text
[ ] id is present and immutable.
[ ] event_type is present and registered/controlled.
[ ] event_category is controlled.
[ ] status is controlled.
[ ] source_domain is present.
[ ] source_object_type is present.
[ ] source_object_reference_id is present.
[ ] occurred_at is present.
[ ] Event does not equal Workflow, Task, Notification or Communication.
[ ] Event is not implementation log by default.
[ ] Payload follows payload contract.
[ ] Correlation and causation references are preserved where available.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite event domain spec
preserve Event / Workflow Contract boundary
preserve Event / Task boundary
preserve Event / Notification boundary
preserve Event / Communication boundary
implement only MVP fields unless task says otherwise
write tests for required event_type
write tests for required source_domain
write tests for required source_object_type
write tests for required source_object_reference_id
write tests for required occurred_at
write tests preventing debug logs from becoming Core Events by default
write tests preventing Event service from sending Notification directly
write tests preventing Event service from sending Communication directly
write tests for payload contract validation
```

Codex must not:

```text
invent full event bus infrastructure beyond approved MVP
treat Event as Workflow
treat Event as Task
treat Event as Notification
treat Event as Communication
store sensitive payload inline by default
allow AI to rewrite event history
allow product UI to redefine Event status
```

---

# 17. Acceptance Criteria

This Event Object Specification is accepted only if:

```text
[ ] It defines Event purpose.
[ ] It defines Event Core meaning.
[ ] It identifies Event as Business Execution Object.
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
| 0.1.0 | Draft | Initial Event object specification. Establishes Event as meaningful occurrence record, separates Event from Workflow, Task, Notification, Communication and implementation logs, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
