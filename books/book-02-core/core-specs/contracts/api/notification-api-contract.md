# API Contract — Notification API

**Spec ID:** B02-CONTRACT-API-NOTIFICATION  
**Spec Type:** API Contract Specification  
**Contract Name:** Notification API Contract  
**Contract File:** core-specs/contracts/api/notification-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/notification-api.md  
**Related Domain:** Notification  
**Related Object Specs:** core-specs/objects/notification.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/communication.md; core-specs/objects/event.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/notification-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/communication-service.md; core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md  
**Related API Specs:** core-specs/api/notification-api.md; core-specs/api/user-api.md; core-specs/api/organization-api.md; core-specs/api/task-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/communication-api.md; core-specs/api/event-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md  
**Related Event Specs:** core-specs/events/notification-created.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Notification API Contract defines the implementation-facing request and response contract for Notification API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, acknowledge, dismiss and prepare Notification records through governed API boundaries without bypassing Notification Service, User Service, related owning services, Permission Service, Policy Service or Event Service.

This contract governs:

```text
Notification API versioning
Notification create request
Notification update request
Notification read response
Notification search/list response
Notification reference validation
Notification recipient context
Notification source object context
Notification delivery preparation context
Notification acknowledgement and dismissal
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Notification API Contract does not send external communications, replace Communication Service, guarantee user delivery, create legal notice, approve professional action, or authorize AI output as final instruction.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Notification Service through governed API boundaries.
```

This contract does not mean:

```text
external communication delivery
legal notice service
email sending
SMS sending
push provider integration
task execution
professional approval
permission grant
policy approval
event emitter
UI notification center
```

Core rule:

```text
Notification API receives governed notification requests.
Notification Service owns Notification behavior.
Recipient and source references are validated by owning services.
Permission and Policy govern visibility.
Notification is an internal attention signal, not professional execution.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Notification reference fields
recipient fields
source object fields
delivery preparation fields
acknowledgement and dismissal fields
pagination shape for list/search
permission/policy context requirements
AI and human-review context requirements
idempotency requirements
safe error shape
version fields
Codex API implementation expectations
```

This contract is not responsible for:

```text
external message delivery
communication sending
push provider implementation
email/SMS integration
task completion
matter/order completion
legal notice validation
Permission evaluation logic
Policy evaluation logic
Event emission implementation
database schema design
UI rendering
```

---

# 4. Related Owning Spec

Owning API spec:

```text
core-specs/api/notification-api.md
```

Owning service spec:

```text
core-specs/services/notification-service.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Notification API and Notification Service responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Notification
```

Related objects:

```text
User
Organization
Task
Matter
Order
Communication
Event
Permission
Policy
Agent
```

Reference rules:

```text
- notification_reference_id identifies Notification.
- recipient_user_reference_id must be validated by User Service.
- organization_reference_id scopes notification visibility where applicable.
- source_object_type and source_object_reference_id identify the source object and must be validated by owning services where required.
- communication_reference_id may link a notification to a Communication but does not send it.
- Notification acknowledgement does not complete the source object.
```

---

# 6. Required References

Common API context:

```yaml
api_context:
  api_version: v1
  contract_version: v0.1.0
  correlation_id: string | null
  idempotency_key: string | null
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
```

Notification target context:

```yaml
target:
  notification_reference_id: string | null
  target_object_type: Notification
  target_object_reference_id: string | null
```

Rules:

```text
- notification_reference_id is required for read/update/acknowledge/dismiss/validate-by-reference operations.
- idempotency_key is required for create operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- recipient_user_reference_id must be validated where provided.
- source references must be validated where owning contract requires it.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/notifications
GET    /v1/notifications/{notification_reference_id}
PATCH  /v1/notifications/{notification_reference_id}
GET    /v1/notifications
POST   /v1/notifications/validate-reference
POST   /v1/notifications/{notification_reference_id}/acknowledge
POST   /v1/notifications/{notification_reference_id}/dismiss
POST   /v1/notifications/prepare-recipient-summary
```

Endpoint ownership:

```text
API layer validates request contract.
Notification Service executes Notification behavior.
User Service validates recipient references.
Related owning services validate source references where needed.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Agent Service governs AI-assisted recipient summaries where used.
Event Service records events emitted by owning services.
```

---

# 8. Create Notification Request Contract

Endpoint:

```text
POST /v1/notifications
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string
actor_reference_id: string | null
organization_reference_id: string | null

permission_context:
  required_permission_keys:
    - notification:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - notification:create:policy
  policy_decision_reference_id: string | null

payload:
  notification_type: string
  notification_status: string | null
  notification_title_safe: string
  notification_body_safe: string | null
  recipient_user_reference_ids:
    - string
  source_object_type: string | null
  source_object_reference_id: string | null
  priority_level: string | null
  delivery_channel_preference: string | null
  action_required: boolean
  action_url_safe: string | null
  due_at: datetime | null
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- notification_type and notification_title_safe are required.
- recipient_user_reference_ids must be validated by User Service.
- source object reference must be validated where provided and supported.
- delivery_channel_preference is preference only, not external delivery guarantee.
- Notification Service assigns notification_reference_id.
```

---

# 9. Create Notification Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  notification_type: string
  notification_status: string
  notification_title_safe: string
  recipient_user_reference_ids_visible:
    - string
  source_object_type: string | null
  source_object_reference_id: string | null
  priority_level: string | null
  due_at: datetime | null
  created_at: datetime
  updated_at: datetime | null
  restricted_fields_omitted: boolean
audit_context:
  event_reference_ids:
    - string
idempotency_result:
  idempotency_key: string
  idempotency_status: string
  replayed: boolean
```

Rules:

```text
- Response must not expose database IDs.
- NotificationCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate NotificationCreated event.
```

---

# 10. Read Notification Contract

Endpoint:

```text
GET /v1/notifications/{notification_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  notification_type: string
  notification_status: string
  notification_title_safe: string
  notification_body_visible: string | null
  recipient_user_reference_ids_visible:
    - string
  source_object_type: string | null
  source_object_reference_id: string | null
  priority_level: string | null
  delivery_channel_preference: string | null
  action_required: boolean
  action_url_visible: string | null
  due_at: datetime | null
  acknowledged_at: datetime | null
  dismissed_at: datetime | null
  metadata_safe: object | null
  created_at: datetime | null
  updated_at: datetime | null
  restricted_fields_omitted: boolean
permission_context:
  permission_decision_reference_id: string | null
policy_context:
  policy_decision_reference_id: string | null
```

Rules:

```text
- Read must evaluate notification:read permission.
- Policy may redact body, action URL, recipients or source object references.
- NotFound may be returned where policy forbids existence disclosure.
- Notification read does not imply acknowledgement.
```

---

# 11. Update Notification Contract

Endpoint:

```text
PATCH /v1/notifications/{notification_reference_id}
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  notification_status: string | null
  notification_title_safe: string | null
  notification_body_safe: string | null
  priority_level: string | null
  delivery_channel_preference: string | null
  action_required: boolean | null
  action_url_safe: string | null
  due_at: datetime | null
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - notification:update
policy_context:
  required_policy_scopes:
    - notification:update:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  notification_status: string
  notification_title_safe: string
  priority_level: string | null
  due_at: datetime | null
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Notification Service.
- Restricted body/action fields must not be patched unless policy allows them.
- Human review may be required where notification wording has customer-facing or professional-risk impact.
```

---

# 12. Search/List Notification Contract

Endpoint:

```text
GET /v1/notifications
```

Query parameters:

```yaml
notification_type: string | null
notification_status: string | null
recipient_user_reference_id: string | null
source_object_type: string | null
source_object_reference_id: string | null
priority_level: string | null
action_required: boolean | null
due_before: datetime | null
safe_query: string | null
pagination:
  cursor: string | null
  limit: integer | null
  sort:
    field: string | null
    direction: Asc | Desc | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  items:
    - notification_reference_id: string
      notification_type: string
      notification_status: string
      notification_title_safe: string
      source_object_type: string | null
      source_object_reference_id: string | null
      priority_level: string | null
      action_required: boolean
      due_at: datetime | null
      restricted_fields_omitted: boolean
  pagination:
    next_cursor: string | null
    previous_cursor: string | null
    limit: integer
    returned_count: integer
    has_more: boolean
    total_count: integer | null
    total_count_omitted: boolean
```

Rules:

```text
- Pagination must follow Pagination Contract.
- total_count must be omitted where policy or security requires it.
- Search must not reveal restricted Notification existence.
- safe_query must not be treated as unrestricted search over notification body.
```

---

# 13. Validate Notification Reference Contract

Endpoint:

```text
POST /v1/notifications/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  notification_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  notification_type: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read full Notification.
- Validation status must follow Reference Contract.
- Policy may hide safe_label or notification type.
```

---

# 14. Acknowledge Notification Contract

Endpoint:

```text
POST /v1/notifications/{notification_reference_id}/acknowledge
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  acknowledgement_note_safe: string | null
permission_context:
  required_permission_keys:
    - notification:acknowledge
policy_context:
  required_policy_scopes:
    - notification:acknowledge:policy
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  previous_status: string
  current_status: string
  acknowledged_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Acknowledgement must route through Notification Service.
- Acknowledgement does not complete source Task, Matter, Order or Communication.
- Acknowledgement may be idempotent.
```

---

# 15. Dismiss Notification Contract

Endpoint:

```text
POST /v1/notifications/{notification_reference_id}/dismiss
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
actor_reference_id: string | null
organization_reference_id: string | null
payload:
  dismissal_reason_safe: string | null
permission_context:
  required_permission_keys:
    - notification:dismiss
policy_context:
  required_policy_scopes:
    - notification:dismiss:policy
human_review_context:
  human_review_required: boolean | null
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  notification_reference_id: string
  previous_status: string
  current_status: string
  dismissed_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Dismissal must route through Notification Service.
- Dismissal does not cancel source Task, Matter, Order or Communication.
- Human review may be required for dismissing critical notifications.
```

---

# 16. Prepare Recipient Summary Contract

Endpoint:

```text
POST /v1/notifications/prepare-recipient-summary
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
permission_context:
  required_permission_keys:
    - notification:summary:prepare
policy_context:
  required_policy_scopes:
    - notification:summary:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
payload:
  recipient_user_reference_id: string
  summary_purpose: string
  notification_scope:
    notification_status: string | null
    due_before: datetime | null
    action_required: boolean | null
  include_source_context: boolean
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  summary_status: string
  recipient_user_reference_id: string
  notification_summary_safe: string | null
  action_items_safe:
    - string
  source_scope_disclosed: boolean
  policy_omissions_disclosed: boolean
  restricted_fields_omitted: boolean
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
human_review:
  human_review_required: boolean | null
```

Rules:

```text
- Recipient summary is assistance, not task execution or professional instruction.
- AI-assisted summary must follow AI governance.
- Policy may omit source context or sensitive notifications.
- Human review may be required before customer-facing summary use.
```

---

# 17. Controlled Values

## 17.1 notification_type

```text
TaskReminder
DeadlineReminder
StatusChange
ActionRequired
ReviewRequired
PolicyRestriction
PermissionIssue
WorkflowUpdate
CommunicationUpdate
RoutingUpdate
SystemNotice
CustomerNoticeDraft
InternalAlert
Other
Unknown
```

## 17.2 notification_status

```text
Draft
Pending
Visible
Read
Acknowledged
Dismissed
Expired
Archived
DeletedReferenceOnly
Unknown
```

## 17.3 priority_level

```text
Low
Normal
High
Urgent
Critical
Unknown
```

## 17.4 delivery_channel_preference

```text
InApp
Email
Push
Portal
InternalOnly
NoExternalDelivery
Unknown
```

## 17.5 source_object_type

```text
Task
Matter
Order
WorkflowContract
Communication
Routing
Event
Customer
Trademark
Document
Evidence
System
Unknown
```

## 17.6 summary_status

```text
Completed
Partial
NoVisibleNotifications
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 17.7 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
Expired
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 17.8 sort.field

```text
created_at
updated_at
due_at
notification_title_safe
notification_status
notification_type
priority_level
```

---

# 18. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] notification_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] notification_type is controlled.
[ ] notification_status is controlled where provided.
[ ] priority_level is controlled where provided.
[ ] delivery_channel_preference is controlled where provided.
[ ] recipient_user_reference_ids are validated where provided.
[ ] source object references are validated where required.
[ ] AI Context is present for AI-assisted recipient summary.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 19. Permission Rules

Required permission keys:

```text
notification:create
notification:read
notification:search
notification:update
notification:validate
notification:acknowledge
notification:dismiss
notification:summary:prepare
```

Rules:

```text
- Notification API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 20. Policy Rules

Required policy scopes may include:

```text
notification:create:policy
notification:read:policy
notification:search:policy
notification:update:policy
notification:reference:policy
notification:visibility:policy
notification:recipient:visibility:policy
notification:acknowledge:policy
notification:dismiss:policy
notification:summary:prepare:policy
cross-organization:notification
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact body, action URLs, recipients, source context, summaries or total_count.
- Policy may downgrade response to metadata-only.
- Policy may require human review before dismissing critical notifications or preparing customer-facing summaries.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 21. AI and Human Review Rules

AI rules:

```text
- AI may summarize Notification context only within Permission and Policy limits.
- AI must not acknowledge, dismiss, complete tasks, send communications or decide professional action.
- AI output must disclose source scope, missing context and policy omissions where applicable.
```

Human review:

```text
- Human review may be required where Notification output is used for customer-facing summary, critical dismissal, workflow change explanation or external communication.
- human_review_required must be explicit where policy requires review.
```

---

# 22. Idempotency and Event Rules

Idempotency:

```text
POST /v1/notifications requires idempotency_key.
PATCH /v1/notifications/{notification_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Acknowledge and dismiss endpoints may require idempotency_key for duplicate-sensitive operations.
Prepare-recipient-summary does not normally require idempotency unless result is persisted.
```

Events:

```text
NotificationCreated may be emitted by Notification Service after successful creation.
Notification acknowledgement/dismissal events may be reserved for later if event specs exist.
CommunicationCreated may be emitted only by Communication Service, not this API.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 23. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
NotificationReferenceInvalid
RecipientReferenceInvalid
SourceReferenceInvalid
AcknowledgementInvalid
DismissalInvalid
CriticalNotificationReviewRequired
SummaryUnavailable
HumanReviewRequired
StateInvalid
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose database IDs, restricted notification body, hidden recipients, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 24. Versioning Rules

Version fields:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Unsupported API or contract versions must fail closed.
- Breaking changes require contract version bump.
- Response payloads must preserve version fields.
```

---

# 25. Codex Implementation Notes

Codex must:

```text
cite Notification API Spec
cite Notification Service Spec
cite this Notification API Contract
use Reference Contract for notification_reference_id, recipient references and source references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted recipient summaries
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive acknowledgement/dismissal operations
use Versioning Contract for version validation
route all Notification mutation through Notification Service
invoke User Service for recipient validation
invoke source owning services for source reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing body, action URL, recipients, source context or summaries
return safe errors only
write tests for create/read/update/search/validate-reference/acknowledge/dismiss/prepare-recipient-summary
write tests for recipient validation
write tests for source reference validation
write tests that acknowledgement does not complete source object
write tests that dismissal does not cancel source object
write tests for critical dismissal requiring human review
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Notification directly in API layer
query database directly from API contract implementation
use generic id where notification_reference_id is required
expose database IDs, restricted notification body or hidden recipients
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
send external communication from Notification API
complete Task, Matter, Order or Communication from acknowledgement/dismissal
treat AI notification summary as professional instruction
allow AI context to exceed evaluated_data_access_scope
```

---

# 26. Acceptance Criteria

This Notification API Contract is accepted only if:

```text
[ ] It defines Notification API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Notification API and Service specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines acknowledge contract.
[ ] It defines dismiss contract.
[ ] It defines prepare recipient summary contract.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI and Human Review rules.
[ ] It defines idempotency and event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Notification API Contract. Defines governed create, read, update, search, validate-reference, acknowledgement, dismissal and recipient-summary payloads, recipient/source validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
