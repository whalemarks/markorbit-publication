# API Specification — Notification API

**Spec ID:** B02-API-NOTIFICATION  
**Spec Type:** API Specification  
**API Name:** Notification API  
**API File:** core-specs/api/notification-api.md  
**Related Domain:** core-specs/domains/notification.md  
**Related Object Specs:** core-specs/objects/notification.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/notification-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/notification-created.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/notification-api-contract.md; core-specs/contracts/events/notification-created-payload.md  
**Related Agent Specs:** core-specs/agents/notification-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Notification API exposes governed Notification operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, prepare and mark Notification references without treating Notification as Communication, email/SMS delivery, legal notice, task completion, workflow execution, customer instruction, professional approval or AI autonomous outreach.

Notification API exists to support:

```text
internal and system notification context
task and event reminder preparation
safe user-facing alert metadata
matter/order/workflow notification context
notification preference and visibility governance
AI-assisted notification drafting under governance
event trace access
API-safe notification reference validation
```

Notification API does not send external communications by itself, prove message delivery, create legal notice, complete tasks, execute workflow or replace communication review.

---

# 2. API Meaning

Notification API means:

```text
a governed interface for operating Notification references through Notification Service.
```

Notification API does not mean:

```text
Communication API
email delivery API
SMS delivery API
legal notice API
Task API
workflow execution API
customer instruction API
AI outreach API
```

Notification is an alert/reminder/system-message object.

Communication is a governed exchange or message context.

Delivery channels and legal-effect communications are separate.

---

# 3. API Boundary

Notification API is responsible for:

```text
Notification create request intake
Notification read/search/list access
Notification update request intake
Notification reference validation
Notification preparation request intake
Notification state marking request intake
safe Notification response shaping
Permission/Policy enforcement for Notification operations
Notification-related Event reference exposure where allowed
AI Agent access boundary for Notification operations
controlled API errors
```

Notification API is not responsible for:

```text
external communication delivery
email/SMS/channel sending
legal notice effect
Task execution
Workflow execution
Matter or Order lifecycle ownership
Communication lifecycle ownership
professional approval
AI autonomous outreach
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/notification.md
```

Domain rule:

```text
Notification provides governed alert/reminder context.
Notification is not Communication, delivery proof, legal notice, Task execution or workflow completion by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/notification.md
core-specs/objects/task.md
core-specs/objects/event.md
core-specs/objects/user.md
core-specs/objects/organization.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/communication.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Notification API returns notification_reference_id.
- Notification API may reference Task, Event, User, Organization, Matter, Order or Communication context but must not create or execute them silently.
- Notification creation is not delivery proof.
- Notification read or acknowledgement is not Task completion.
- Notification must not expose restricted message content or recipient details by default.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/notification-service.md
core-specs/services/task-service.md
core-specs/services/event-service.md
core-specs/services/user-service.md
core-specs/services/organization-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/communication-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
```

Service rules:

```text
- Notification API must invoke Notification Service for Notification behavior.
- Notification API must validate related references through their owning services where required.
- Notification API must invoke Permission Service where operation requires authorization.
- Notification API must invoke Policy Service where contextual constraints apply.
- Notification API must not emit Notification events directly; Notification Service and Event Service govern events.
- Communication delivery must route through Communication Service, not Notification API.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/notification-created.md
core-specs/events/task-created.md
core-specs/events/communication-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createNotification may result in NotificationCreated.
- Communication delivery or creation must use Communication Service and may result in CommunicationCreated.
- API consumers must not fabricate NotificationCreated.
- NotificationCreated is alert/reminder trace, not delivery proof, legal notice or Task completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Notification

**Operation Category:** Create  
**Method:** POST  
**Path:** `/notifications`  
**Owning Service Operation:** `createNotification`  
**Permission Required:** `notification:create`  
**Policy Required:** `NotificationCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Service Must Emit NotificationCreated

Meaning:

```text
Create a governed Notification reference.
```

Non-meaning:

```text
does not send external communication
does not prove delivery
does not create legal notice
does not complete Task
does not execute workflow
does not grant Permission
```

Expected service call:

```text
API
  ↓
Permission Service evaluatePermission
  ↓
Policy Service evaluatePolicy where required
  ↓
Notification Service createNotification
  ↓
Event Service record NotificationCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Notification

**Operation Category:** Read  
**Method:** GET  
**Path:** `/notifications/{notification_reference_id}`  
**Owning Service Operation:** `getNotification`  
**Permission Required:** `notification:read`  
**Policy Required:** `NotificationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Notification view.
```

Non-meaning:

```text
does not expose restricted message body automatically
does not expose unrelated recipient details automatically
does not prove delivery or acknowledgement automatically
```

## 8.3 Operation: Search Notifications

**Operation Category:** Search  
**Method:** GET  
**Path:** `/notifications`  
**Owning Service Operation:** `searchNotifications`  
**Permission Required:** `notification:search`  
**Policy Required:** `NotificationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Notification references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted notification inbox access
does not expose restricted recipient, task, matter or order data by default
```

## 8.4 Operation: Update Notification

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/notifications/{notification_reference_id}`  
**Owning Service Operation:** `updateNotification`  
**Permission Required:** `notification:update`  
**Policy Required:** `NotificationUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit NotificationUpdated where event is defined

Meaning:

```text
Update governed Notification metadata, status or timing under Notification Service rules.
```

Non-meaning:

```text
does not update Task status automatically
does not update Communication status automatically
does not prove delivery
does not complete workflow
```

## 8.5 Operation: Validate Notification Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/notifications/reference/validate`  
**Owning Service Operation:** `validateNotificationReference`  
**Permission Required:** `notification:validate`  
**Policy Required:** `NotificationReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Notification reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not prove delivery
does not prove acknowledgement
does not authorize communication sending
does not authorize Task completion
```

## 8.6 Operation: Prepare Notification from Task

**Operation Category:** Action  
**Method:** POST  
**Path:** `/notifications/prepare-from-task`  
**Owning Service Operation:** `prepareNotificationFromTask`  
**Permission Required:** `notification:task:prepare`  
**Policy Required:** `NotificationTaskPreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit NotificationCreated unless createNotification succeeds separately

Meaning:

```text
Prepare a governed Notification draft or request from Task context.
```

Non-meaning:

```text
does not create Notification automatically unless explicitly requested
does not deliver notification
does not complete Task
does not create Communication
```

## 8.7 Operation: Mark Notification Read

**Operation Category:** StateTransition  
**Method:** POST  
**Path:** `/notifications/{notification_reference_id}/read`  
**Owning Service Operation:** `markNotificationRead`  
**Permission Required:** `notification:read:mark`  
**Policy Required:** `NotificationStatePolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit audit event where defined

Meaning:

```text
Mark a governed Notification as read for an authorized recipient context.
```

Non-meaning:

```text
does not complete Task
does not acknowledge legal notice
does not prove external message delivery
does not mutate Communication status
```

## 8.8 Operation: Mark Notification Dismissed

**Operation Category:** StateTransition  
**Method:** POST  
**Path:** `/notifications/{notification_reference_id}/dismiss`  
**Owning Service Operation:** `markNotificationDismissed`  
**Permission Required:** `notification:dismiss`  
**Policy Required:** `NotificationStatePolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Service May Emit audit event where defined

Meaning:

```text
Dismiss a governed Notification for an authorized recipient context.
```

Non-meaning:

```text
does not complete Task
does not cancel Matter or Order
does not stop required legal or workflow obligations
```

## 8.9 Operation: Prepare Communication from Notification

**Operation Category:** Action  
**Method:** POST  
**Path:** `/notifications/{notification_reference_id}/communications/prepare`  
**Owning Service Operation:** `prepareCommunicationFromNotification`  
**Permission Required:** `notification:communication:prepare`  
**Policy Required:** `NotificationCommunicationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Must route through Communication Service if Communication is created

Meaning:

```text
Prepare a governed Communication draft or request from Notification context.
```

Non-meaning:

```text
does not create Communication unless Communication Service accepts it
does not send message
does not create legal notice
does not bypass communication review
```

## 8.10 Operation: List Notification Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/notifications/{notification_reference_id}/events`  
**Owning Service Operation:** `listNotificationEvents`  
**Permission Required:** `notification:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Notification-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Notification Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  notification_type: string
  notification_status: string | optional
  notification_priority: string | optional
  recipient_type: string
  recipient_reference_id: string
  subject_object_type: string | null
  subject_object_reference_id: string | null
  source_event_reference_id: string | null
  source_task_reference_id: string | null
  title: string
  safe_summary: string | null
  scheduled_at: datetime | null
  source_type: string
  request_context: object
  ai_context:
    ai_drafted: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Notification Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  notification_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  notification_status: string | optional
  notification_priority: string | optional
  title: string | optional
  safe_summary: string | optional
  scheduled_at: datetime | optional
  request_context: object
```

## 9.3 Validate Notification Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  notification_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Prepare Notification from Task Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  task_reference_id: string
  preparation_purpose: string
  draft_mode: string
  recipient_context:
    recipient_type: string | null
    recipient_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.5 Mark Notification State Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  notification_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  recipient_reference_id: string | null
  state_reason: string | null
  request_context: object
```

## 9.6 Prepare Communication from Notification Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  preparation_purpose: string
  draft_mode: string
  recipient_context:
    recipient_type: string | null
    recipient_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted message body, contact data, privileged notes, secrets or raw document content by default.
- Requests must use controlled notification_type, notification_status, notification_priority, recipient_type, source_type and draft_mode values.
- AI-drafted notification content must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Notification Response

```yaml
status: 200
body:
  notification_reference_id: string
  notification_type: string
  notification_status: string
  notification_priority: string
  recipient_type: string
  recipient_reference_id: string
  subject_object_type: string | null
  subject_object_reference_id: string | null
  source_event_reference_id: string | null
  source_task_reference_id: string | null
  title: string
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    message_summary: string | null
  scheduled_at: datetime | null
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Notification Response

```yaml
status: 201
body:
  notification_reference_id: string
  notification_status: string
  review_required: boolean
  related_event_reference_ids:
    - notification_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Notification Reference Validation Response

```yaml
status: 200
body:
  notification_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Prepared Notification Response

```yaml
status: 200
body:
  notification_draft_reference_id: string | null
  usable_for_notification_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Notification State Response

```yaml
status: 200
body:
  notification_reference_id: string
  from_status: string
  to_status: string
  transition_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Prepared Communication Response

```yaml
status: 200
body:
  notification_reference_id: string
  communication_draft_reference_id: string | null
  preparation_status: string
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply external delivery, legal notice, Task completion, Communication creation or workflow completion.
- Responses must not expose restricted message body, recipient details, customer strategy or privileged notes by default.
- Responses must distinguish Notification references from Communication, Task, Matter and Order references.
- Responses must identify review requirements for AI-drafted content.
```

---

# 11. Controlled Values

## 11.1 notification_type

```text
TaskReminder
TaskAssignment
TaskDue
TaskOverdue
WorkflowAlert
MatterUpdate
OrderUpdate
SystemNotice
ClientPortalNotice
InternalNotice
ReviewRequired
CommunicationPrompt
Unknown
```

## 11.2 notification_status

```text
Draft
Scheduled
Active
Read
Dismissed
Expired
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 notification_priority

```text
Low
Normal
High
Urgent
Unknown
```

## 11.4 recipient_type

```text
User
Agent
Role
Queue
Organization
System
Unknown
```

## 11.5 source_type

```text
ProfessionalInput
TaskDerived
EventDerived
WorkflowDerived
MatterDerived
OrderDerived
SystemGenerated
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.6 draft_mode

```text
Preview
CreateDraft
CreateAndRequestReview
Unknown
```

## 11.7 preparation_purpose

```text
Reminder
AssignmentNotice
ReviewPrompt
Escalation
ClientUpdate
InternalNotice
CommunicationPreparation
AIAssistedDraft
Unknown
```

## 11.8 transition_status

```text
Accepted
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.9 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
ContextMismatch
Unknown
```

## 11.10 intended_use

```text
TaskContext
MatterContext
OrderContext
WorkflowContext
CommunicationPreparation
AIAgentAction
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
notification:create
notification:read
notification:search
notification:update
notification:validate
notification:task:prepare
notification:read:mark
notification:dismiss
notification:communication:prepare
notification:event:read
```

Rules:

```text
- Notification read/search must be permission-controlled.
- Notification creation must not imply delivery or legal notice.
- Notification validation must not authorize communication sending or Task completion.
- Read/dismiss state changes require recipient or delegated authority.
- Communication preparation requires separate permission and downstream Communication rules.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
NotificationCreationPolicy
NotificationUpdatePolicy
NotificationVisibilityPolicy
NotificationReferencePolicy
NotificationTaskPreparationPolicy
NotificationStatePolicy
NotificationCommunicationPolicy
EventVisibilityPolicy
AIAgentNotificationAccessPolicy
RestrictedNotificationDataPolicy
CrossOrganizationNotificationPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Notification fields.
- Policy may require human review for AI-drafted notifications.
- Policy may restrict cross-organization Notification lookup.
- Policy may restrict recipient details, message bodies, customer strategy and privileged notes.
- Policy may restrict state changes and Communication preparation.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Notification: Restricted / HumanReviewRequired where AI-drafted
Get Notification: Restricted
Search Notifications: Restricted
Update Notification: Restricted / HumanReviewRequired where sensitive
Validate Notification Reference: Allowed under contract
Prepare Notification from Task: Restricted / HumanReviewRequired where AI-drafted
Mark Notification Read: Restricted
Mark Notification Dismissed: Restricted
Prepare Communication from Notification: Restricted / HumanReviewRequired where AI-drafted
List Notification Events: Restricted
```

AI Agents may:

```text
summarize safe Notification metadata
prepare Notification draft for human review
flag missing recipient or source context
validate Notification references for authorized actions
prepare Communication draft from Notification for human review
summarize notification trace where allowed
```

AI Agents must not:

```text
fabricate Notification
fabricate NotificationCreated events
treat AI-drafted Notification as approved notice
send external communication through Notification API
treat Notification as legal notice or delivery proof
complete Task or workflow through Notification API
bypass Permission or Policy
expose restricted message body or recipient details
```

AI access requires:

```text
agent_identity_reference_id
agent_contract_reference_id where required
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 15. Event Access Rules

Notification API may expose:

```text
NotificationCreated
TaskCreated
CommunicationCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Notification events directly.
- NotificationCreated must not be treated as external delivery, legal notice, Task completion, workflow completion or Communication creation.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] notification_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] recipient_reference_id is valid where required.
[ ] subject_object_type and subject_object_reference_id are valid where provided.
[ ] source_event_reference_id is valid where provided.
[ ] source_task_reference_id is valid where provided.
[ ] notification_type is controlled.
[ ] notification_status is controlled.
[ ] notification_priority is controlled.
[ ] recipient_type is controlled.
[ ] source_type is controlled.
[ ] draft_mode is controlled where applicable.
[ ] state transition is allowed from current status.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted notification/message/recipient/customer/strategy fields are omitted or allowed.
[ ] AI-drafted notification data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] NotificationCreated is emitted after createNotification succeeds.
[ ] Notification preparation does not create Notification unless createNotification succeeds.
[ ] Communication preparation routes through Communication Service if Communication is created.
[ ] Response shape is safe.
```

---

# 17. Error Handling

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
NotificationReferenceInvalid
RecipientReferenceInvalid
SubjectReferenceInvalid
SourceEventReferenceInvalid
SourceTaskReferenceInvalid
StateTransitionInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedNotificationData
AgentContractRequired
HumanReviewRequired
EventEmissionFailed
InternalError
```

Error response:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Error rules:

```text
- Errors must not expose restricted Notification content.
- Errors must not expose recipient details, message bodies, customer strategy or privileged notes.
- Errors must not expose unrelated Task, Matter, Order or Communication details.
- Errors must not expose permission or policy internals.
- Errors must be safe for product/API consumers.
```

---

# 18. Versioning Rules

API version:

```text
v0.1.0
```

Versioning rules:

```text
- Breaking changes require new version or explicit migration rule.
- notification_type, notification_status, notification_priority, recipient_type and state transition changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI notification behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Notification API spec
cite Notification Service Specification
cite Notification Object Specification
cite NotificationCreated Event Specification
cite Task/Event/User/Communication specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid notification_reference_id
write tests for invalid recipient/source/subject references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Notification creation does not send external communication
write tests that Notification read/dismiss does not complete Task
write tests that Notification preparation does not create Notification automatically
write tests that Communication preparation routes through Communication Service
write tests for AI Agent Contract and human review requirement
write tests for NotificationCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Notification Service
allow UI to emit NotificationCreated directly
treat Notification as Communication
treat Notification as delivery proof or legal notice
treat Notification as Task completion or workflow completion
send communications directly through Notification API
expose restricted message bodies or recipient data for convenience
allow AI to fabricate Notification references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Notification API purpose.
[ ] It defines Notification API meaning.
[ ] It defines Notification API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, prepare, mark-read, dismiss, communication preparation and event-list operations.
[ ] It defines request contracts.
[ ] It defines response contracts.
[ ] It defines controlled values.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent access rules.
[ ] It defines Event access rules.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Notification API specification. Defines governed Notification alert/reminder interface and separates Notification API from Communication, external delivery, legal notice, Task completion, workflow execution and AI autonomous outreach. |

---

**End of API Specification**
