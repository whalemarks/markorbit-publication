# Event Specification — NotificationCreated

**Spec ID:** B02-EVT-NOTIFICATION-CREATED  
**Spec Type:** Event  
**Event Name:** NotificationCreated  
**Event File:** core-specs/events/notification-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Notification  
**Producing Service:** core-specs/services/notification-service.md  
**Related Object Specs:** core-specs/objects/notification.md; core-specs/objects/event.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/notification-service.md; core-specs/services/event-service.md; core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/user-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/communication-service.md  
**Related API Specs:** core-specs/api/notification-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/notification-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/notification-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

NotificationCreated records that a governed Notification awareness-intent reference has been created by Notification Service.

It exists so that Event, Task, Matter, Order, User, Communication, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that an awareness intent now exists without treating that Notification as Event occurrence, Communication message, delivery success, read receipt, task assignment, workflow execution, approval or marketing automation.

NotificationCreated is required before:

```text
awareness intent trace
task-related notification planning
matter/order notification context
event-to-notification awareness flow
user-targeted notification visibility
communication delivery preparation
policy-controlled notification targeting
AI-assisted notification summary review
API notification reference validation
audit trace for notification-sensitive actions
```

---

# 2. Event Meaning

NotificationCreated means:

```text
a stable Notification object reference has been created through governed Notification Service operation.
```

NotificationCreated does not mean:

```text
the notification was delivered
the notification was read
a Communication message was sent
an Event occurred
a Task was assigned
a Workflow transition occurred
the recipient has permission to see restricted content
the recipient approved anything
AI-generated notification content is verified professional truth
```

NotificationCreated records awareness-intent creation only.

It does not establish delivery, reading, communication, workflow execution, approval or professional completion.

---

# 3. Event Category

NotificationCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Notification domain.

It is not a Communication event, delivery event, read event, Task event or Workflow event.

---

# 4. Event Producer

Producing service:

```text
Notification Service
```

Producing operation:

```text
createNotification
```

Source domain:

```text
Notification
```

Source object type:

```text
Notification
```

Allowed producer path:

```text
Event / Task / Matter / Order / API / System / AI-assisted governed operation
        ↓
Notification Service createNotification
        ↓
Event Service record NotificationCreated
```

Producer rules:

```text
- NotificationCreated must be emitted only after Notification Service successfully creates the Notification reference.
- NotificationCreated must not be emitted directly by product UI.
- NotificationCreated must not be emitted directly by AI Agent outside governed service operation.
- NotificationCreated must not be emitted for failed, duplicate-rejected or unauthorized notification creation attempts.
```

---

# 5. Event Trigger

NotificationCreated is triggered when:

```text
Notification Service successfully creates a new Notification object and commits its stable notification_reference_id.
```

Required trigger conditions:

```text
createNotification operation completed
notification_reference_id created
notification_type validated
notification_status validated
target_reference captured
recipient context captured where applicable
source_event_reference_id captured where applicable
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Event recording alone
Task creation
Task assignment
Communication sent
email/SMS/push delivery
read receipt
workflow transition
approval
AI notification suggestion
failed validation
duplicate rejected Notification
```

Related but separate events may include:

```text
EventRecorded
TaskCreated
TaskAssigned
CommunicationSent
NotificationDispatched
NotificationRead
WorkflowTransitionCompleted
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: NotificationCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Notification
source_service: Notification Service
source_operation: createNotification
source_object_type: Notification
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/notification-created-payload.md
safe_summary:
  notification_reference_id: string
  notification_type: string
  notification_status: string
  target_object_type: string | null
  target_object_reference_id: string | null
  source_type: string
restricted_fields_policy: NotificationCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
notification_reference_id: string
notification_type: string
notification_status: string
notification_priority: string
notification_source_type: string
source_event_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
recipient_user_reference_ids: list[string]
recipient_role_reference_ids: list[string]
matter_reference_id: string | null
order_reference_id: string | null
task_reference_id: string | null
created_by_actor_reference_id: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding restricted notification content by default.
- Payload must not include confidential matter data, legal strategy, raw document/evidence content, credentials or secrets.
- Payload must not imply delivery, read receipt, Communication sending, Task assignment or approval.
- Payload must not bypass Permission or Policy for recipient visibility.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
notification_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
source_event_reference_id
target_object_type
target_object_reference_id
recipient_user_reference_ids
recipient_role_reference_ids
matter_reference_id
order_reference_id
task_reference_id
communication_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal notification_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- source_event_reference_id must not imply that Notification is the source Event.
- recipient_user_reference_ids must not imply delivery or read state.
- communication_reference_id must not imply CommunicationSent unless Communication Service emits its own event.
- permission_decision_reference_id must be context-specific and must not be generalized.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
NotificationCreated
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

## 8.4 notification_type

```text
TaskNotification
MatterNotification
OrderNotification
WorkflowNotification
EventNotification
DeadlineNotification
ReviewNotification
ApprovalNotification
SystemNotification
InternalNotification
Other
Unknown
```

## 8.5 notification_status

```text
Draft
Created
DispatchPending
Dispatched
DispatchFailed
Read
Dismissed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 notification_priority

```text
Low
Normal
High
Urgent
Critical
Unknown
```

## 8.7 notification_source_type

```text
EventTriggered
TaskTriggered
MatterTriggered
OrderTriggered
WorkflowTriggered
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.8 reason_code

```text
NotificationCreated
EventTriggered
TaskTriggered
MatterTriggered
OrderTriggered
WorkflowTriggered
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 NotificationCreated Records Awareness Intent

NotificationCreated records that a Notification reference exists.

It must not be interpreted as delivery, read receipt, Communication message or professional completion.

## 9.2 Notification Is Not Event

Event Service records meaningful domain occurrences.

Notification may be created because of an Event, but it is not the Event itself.

## 9.3 Notification Is Not Communication

Communication Service owns message and conversation lifecycle.

NotificationCreated may later lead to Communication, but it does not send a message.

## 9.4 Notification Is Not Task Assignment

Task Service owns assignment and work unit lifecycle.

NotificationCreated does not assign Task or grant work authority.

## 9.5 Notification Delivery Requires Separate State

Dispatch, delivery, read, failure and dismissal states must be represented by Notification Service state or separate events.

## 9.6 AI Notification Content Is Not Professional Truth

AI may draft or summarize notification content.

AI-generated content must obey authorized knowledge, policy, permission and review requirements.

## 9.7 NotificationCreated Must Respect Permission and Policy

Notification creation, targeting, visibility and content rendering must respect Permission, Policy, confidentiality and organization access context.

## 9.8 NotificationCreated Must Be Immutable

NotificationCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Task Service
Matter Service
Order Service
Workflow Contract Service
Event Service
Communication Service
User Service
Permission Service
Policy Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Communication Service may deliver a message only through governed communication operation.
- Task Service may display task-related notification context but must not infer assignment.
- User Service may provide recipient context but must not infer authorization.
- Permission Service must evaluate visibility where required.
- Policy Service must enforce confidentiality and content/target constraints.
- AI Agents may summarize notification only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Notification creation trace.
```

Consumers must not:

```text
treat NotificationCreated as CommunicationSent
treat NotificationCreated as delivered or read
treat NotificationCreated as TaskAssigned
treat NotificationCreated as Event occurrence
treat NotificationCreated as Permission grant
expose restricted notification content or target context
```

---

# 11. Relationship to Services

Producing service:

```text
Notification Service produces NotificationCreated after createNotification succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches NotificationCreated.
```

Related services:

```text
Task, Matter, Order and Workflow Contract services may provide target context.
Communication Service may later send messages based on Notification under governed operation.
User Service provides recipient references.
Permission Service controls who may create, view or act on Notification.
Policy Service controls targeting, visibility and content.
Audit Service records accountability trace.
AI Agent Governance controls AI notification content behavior.
```

Boundary reminders:

```text
Notification Service owns awareness intent.
Event Service records occurrence.
Communication Service owns message lifecycle.
Task Service owns actionable work units.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /notifications/{notification_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create NotificationCreated directly.
- API must call Notification Service createNotification, which emits the event.
- API must not expose restricted notification content, recipient confidentiality, matter strategy or raw document/evidence content.
- API must distinguish NotificationCreated from CommunicationSent, NotificationDispatched, NotificationRead, TaskAssigned and EventRecorded.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Notification reference was created
explain that Notification is awareness intent, not delivery or Communication
flag missing recipient or target context for review
flag notification requiring policy/content review
suggest next governed delivery step
prepare audit-safe Notification creation summary
```

AI must not:

```text
fabricate NotificationCreated
rewrite NotificationCreated
delete NotificationCreated
treat NotificationCreated as delivery, read receipt or CommunicationSent
treat NotificationCreated as Task assignment or Permission grant
treat AI notification draft as verified professional content
hide AI-assisted creation
expose restricted notification, matter or customer data
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

NotificationCreated is valid only if:

```text
[ ] event_name is NotificationCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Notification Service.
[ ] producing operation is createNotification.
[ ] source_domain is Notification.
[ ] source_object_type is Notification.
[ ] source_object_reference_id is present.
[ ] notification_reference_id is present.
[ ] source_object_reference_id equals notification_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] notification_type is controlled.
[ ] notification_status is controlled.
[ ] notification_priority is controlled.
[ ] notification_source_type is controlled.
[ ] payload does not include restricted notification content, matter strategy, customer data or raw document/evidence content unless allowed.
[ ] delivery, read receipt, Communication, Task assignment, Event occurrence and Permission grant are not implied.
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
NotificationReferenceMissing
NotificationReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
NotificationTypeInvalid
NotificationStatusInvalid
NotificationPriorityInvalid
NotificationSourceTypeInvalid
RecipientReferenceInvalid
TargetReferenceInvalid
RestrictedFieldViolation
ConfidentialNotificationPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownNotificationEventError
```

Rejection rules:

```text
- Failed Notification creation must not emit NotificationCreated.
- Duplicate rejected Notification creation must not emit NotificationCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Notification Service Specification
cite Notification Object Specification
cite Event Service Specification
cite Communication/Task/User specs where references are used
use exact event_name: NotificationCreated
use exact event_category: DomainEvent
validate notification_reference_id
validate source_object_reference_id equals notification_reference_id
validate actor_reference_id
validate controlled notification_type/status/priority/source_type
validate payload contract
write tests that failed createNotification does not emit NotificationCreated
write tests that NotificationCreated does not imply delivery or read receipt
write tests that NotificationCreated does not send Communication automatically
write tests that NotificationCreated does not assign Task
write tests that NotificationCreated does not grant Permission
write tests that AI-assisted creation is marked where applicable
write tests that restricted notification/matter/customer content is not exposed
```

Codex must not:

```text
emit NotificationCreated directly from UI
treat EventRecorded as NotificationCreated
treat CommunicationSent as NotificationCreated
treat NotificationCreated as delivered or read
treat NotificationCreated as TaskAssigned
store raw confidential notification content in event payload by default
allow AI to fabricate NotificationCreated
use NotificationCreated as command to send Communication, assign Task, complete workflow, grant permission or approve content
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines NotificationCreated purpose.
[ ] It defines NotificationCreated meaning.
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
| 0.1.0 | Draft | Initial NotificationCreated Event specification. Defines governed Notification awareness-intent creation event and separates NotificationCreated from Event, Communication, delivery, read receipt, Task assignment, Permission grant and AI-generated professional content. |

---

**End of Event Specification**
