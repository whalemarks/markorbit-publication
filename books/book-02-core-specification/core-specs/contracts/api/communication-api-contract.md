# API Contract — Communication API

**Spec ID:** B02-CONTRACT-API-COMMUNICATION  
**Spec Type:** API Contract Specification  
**Contract Name:** Communication API Contract  
**Contract File:** core-specs/contracts/api/communication-api-contract.md  
**Contract Category:** API  
**Related Owning Spec:** core-specs/api/communication-api.md  
**Related Domain:** Communication  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/document.md; core-specs/objects/notification.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/communication-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/document-service.md; core-specs/services/notification-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/communication-api.md; core-specs/api/customer-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/task-api.md; core-specs/api/document-api.md; core-specs/api/notification-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/communication-created.md; core-specs/events/notification-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/task-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/audit-agent.md; core-specs/agents/ai-agent-governance.md  
**Related Common Contracts:** core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/pagination.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**API Version:** v1  
**MVP Phase:** Phase 4 — Collaboration Network / Communication Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication API Contract defines the implementation-facing request and response contract for Communication API operations in MarkOrbit Core.

It standardizes how clients create, read, update, search, validate, draft, review, approve, send-prep and link Communication records through governed API boundaries without bypassing Communication Service, Permission Service, Policy Service, Agent governance, Human Review rules or Event Service.

This contract governs:

```text
Communication API versioning
Communication create request
Communication update request
Communication read response
Communication search/list response
Communication reference validation
Communication draft preparation
Communication review and approval context
Communication send-preparation boundary
Recipient and channel context
Attachment and document linkage
Matter, Order, Task and Customer linkage
Permission and Policy context
AI and Human Review context
Idempotency behavior
Audit context
Event trace references
Safe error behavior
Codex implementation rules
```

Communication API Contract does not silently send external communications, bind the organization, approve legal/professional positions, complete tasks, replace Communication Service, evaluate Permission/Policy, or authorize AI output as final communication.

---

# 2. Contract Meaning

This contract means:

```text
a stable API payload and behavior contract for consuming Communication Service through governed API boundaries.
```

This contract does not mean:

```text
email provider integration
message delivery by itself
legal notice approval
professional advice approval
customer consent
task completion
matter completion
order completion
permission grant
policy approval
event emitter
UI inbox
```

Core rule:

```text
Communication API receives governed communication requests.
Communication Service owns Communication behavior.
AI may draft but must not send.
Permission and Policy govern visibility and action.
External delivery requires explicit governed send process and human review where required.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
API request shape
API response shape
path/query/body parameter rules
Communication reference fields
recipient fields
channel fields
draft content fields
review and approval fields
attachment and linked object fields
send-preparation fields
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
external delivery provider internals
email/SMS/chat transport implementation
legal notice validity
professional conclusion approval
customer consent proof
task/matter/order lifecycle completion
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
core-specs/api/communication-api.md
```

Owning service spec:

```text
core-specs/services/communication-service.md
```

Owning agent spec:

```text
core-specs/agents/communication-agent.md
```

Owning rule:

```text
This API contract must not expand, override or weaken Communication API, Communication Service or Communication Agent responsibility boundaries.
```

---

# 5. Related Core Objects

Primary object:

```text
Communication
```

Related objects:

```text
Customer
Matter
Order
Task
Document
Notification
Agent
Permission
Policy
Event
```

Reference rules:

```text
- communication_reference_id identifies Communication.
- customer/matter/order/task references must be validated by owning services where provided.
- document_reference_ids identify attachments or source documents and must be validated by Document Service.
- notification_reference_id may link internal attention signal to Communication but does not send it.
- Communication draft does not equal sent communication.
- AI-generated content remains draft until accepted through governed process.
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

Communication target context:

```yaml
target:
  communication_reference_id: string | null
  target_object_type: Communication
  target_object_reference_id: string | null
```

Rules:

```text
- communication_reference_id is required for read/update/validate/review/approve/send-preparation operations.
- idempotency_key is required for create and duplicate-sensitive operations.
- actor_reference_id or governed system/agent context is required for protected operations.
- recipient and linked object references must be validated where required by owning services.
```

---

# 7. API Endpoint Contract Set

Canonical endpoints:

```text
POST   /v1/communications
GET    /v1/communications/{communication_reference_id}
PATCH  /v1/communications/{communication_reference_id}
GET    /v1/communications
POST   /v1/communications/validate-reference
POST   /v1/communications/{communication_reference_id}/prepare-draft
POST   /v1/communications/{communication_reference_id}/review
POST   /v1/communications/{communication_reference_id}/approve
POST   /v1/communications/{communication_reference_id}/prepare-send
POST   /v1/communications/{communication_reference_id}/link-objects
```

Endpoint ownership:

```text
API layer validates request contract.
Communication Service executes Communication behavior.
Customer/Matter/Order/Task/Document/Notification services validate references where applicable.
Agent Service governs Communication Agent context.
Permission Service evaluates access.
Policy Service evaluates contextual restrictions.
Event Service records events emitted by owning services.
API layer must not send external communications directly.
```

---

# 8. Create Communication Request Contract

Endpoint:

```text
POST /v1/communications
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
    - communication:create
  permission_decision_reference_id: string | null

policy_context:
  required_policy_scopes:
    - communication:create:policy
  policy_decision_reference_id: string | null

payload:
  communication_type: string
  communication_status: string | null
  communication_channel: string | null
  subject_safe: string | null
  body_safe: string | null
  recipient_refs:
    - recipient_type: string
      recipient_reference_id: string | null
      recipient_address_safe: string | null
      recipient_role: string | null
  linked_object_refs:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  attachment_document_reference_ids:
    - string
  source_type: string | null
  source_reference_id: string | null
  ai_generated: boolean
  metadata_safe: object | null
```

Rules:

```text
- idempotency_key is required.
- communication_type is required.
- body_safe may be null for placeholder/draft records.
- recipient addresses must be policy-filtered and safe.
- attachment documents must be validated by Document Service where provided.
- Communication Service assigns communication_reference_id.
```

---

# 9. Create Communication Response Contract

Success response:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  communication_reference_id: string
  communication_type: string
  communication_status: string
  communication_channel: string | null
  subject_safe: string | null
  body_preview_safe: string | null
  recipient_refs_visible:
    - recipient_type: string
      recipient_reference_id: string | null
      recipient_role: string | null
  attachment_document_reference_ids_visible:
    - string
  ai_generated: boolean
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
- CommunicationCreated event reference may be included where policy allows it.
- Replayed idempotent response must not duplicate CommunicationCreated event.
```

---

# 10. Read Communication Contract

Endpoint:

```text
GET /v1/communications/{communication_reference_id}
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  communication_reference_id: string
  communication_type: string
  communication_status: string
  communication_channel: string | null
  subject_safe: string | null
  body_visible: string | null
  recipient_refs_visible:
    - recipient_type: string
      recipient_reference_id: string | null
      recipient_address_visible: string | null
      recipient_role: string | null
  linked_object_refs_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  attachment_document_reference_ids_visible:
    - string
  source_type: string | null
  source_reference_id_visible: string | null
  ai_generated: boolean
  review_status: string | null
  approved_at: datetime | null
  sent_at: datetime | null
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
- Read must evaluate communication:read permission.
- Policy may redact body, recipients, addresses, attachments, linked objects or source references.
- NotFound may be returned where policy forbids existence disclosure.
- Reading communication does not approve or send it.
```

---

# 11. Update Communication Contract

Endpoint:

```text
PATCH /v1/communications/{communication_reference_id}
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
  communication_status: string | null
  communication_channel: string | null
  subject_safe: string | null
  body_safe: string | null
  recipient_refs_patch:
    - recipient_type: string
      recipient_reference_id: string | null
      recipient_address_safe: string | null
      recipient_role: string | null
      operation: Add | Update | Remove | Replace
  attachment_document_reference_ids_patch:
    - string
  metadata_safe_patch: object | null
permission_context:
  required_permission_keys:
    - communication:update
policy_context:
  required_policy_scopes:
    - communication:update:policy
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
  communication_reference_id: string
  communication_status: string
  subject_safe: string | null
  body_preview_safe: string | null
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Update must route through Communication Service.
- Sent communications must not be edited as if unsent unless service supports immutable revision records.
- Restricted body/recipient fields must not be patched unless policy allows them.
- Human review may be required for customer-facing or external-facing content.
```

---

# 12. Search/List Communication Contract

Endpoint:

```text
GET /v1/communications
```

Query parameters:

```yaml
communication_type: string | null
communication_status: string | null
communication_channel: string | null
recipient_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
ai_generated: boolean | null
sent_after: datetime | null
sent_before: datetime | null
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
    - communication_reference_id: string
      communication_type: string
      communication_status: string
      communication_channel: string | null
      subject_safe: string | null
      body_preview_safe: string | null
      ai_generated: boolean
      sent_at: datetime | null
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
- Search must not reveal restricted Communication existence.
- safe_query must not be treated as unrestricted search over private content.
```

---

# 13. Validate Communication Reference Contract

Endpoint:

```text
POST /v1/communications/validate-reference
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
payload:
  communication_reference_id: string
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
  communication_reference_id: string
  valid: boolean
  validation_status: string
  safe_label: string | null
  communication_type: string | null
  communication_status: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Valid reference does not imply permission to read body or send communication.
- Validation status must follow Reference Contract.
- Policy may hide safe_label, type or status.
```

---

# 14. Prepare Draft Contract

Endpoint:

```text
POST /v1/communications/{communication_reference_id}/prepare-draft
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
    - communication:draft:prepare
policy_context:
  required_policy_scopes:
    - communication:draft:prepare:policy
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: CommunicationAgent | null
payload:
  draft_purpose: string
  requested_tone: string | null
  include_linked_context: boolean
  requested_output_language: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  draft_status: string
  proposed_subject_safe: string | null
  proposed_body_safe: string | null
  missing_context_safe:
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
- Draft preparation is assistance, not approval or sending.
- AI-assisted draft must follow Communication Agent governance.
- Policy may omit linked context or restrict output content.
- Human review may be required before approval or sending.
```

---

# 15. Review Communication Contract

Endpoint:

```text
POST /v1/communications/{communication_reference_id}/review
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
  review_decision: string
  review_notes_safe: string | null
  requested_revision_safe: string | null
permission_context:
  required_permission_keys:
    - communication:review
policy_context:
  required_policy_scopes:
    - communication:review:policy
human_review_context:
  human_review_required: boolean
  human_review_reference_id: string | null
```

Response shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
result:
  communication_reference_id: string
  review_status: string
  review_decision: string
  reviewed_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Review must route through Communication Service.
- Review does not send communication.
- Review notes must be safe and policy-filtered.
- Human review reference may be required for professional/customer-facing content.
```

---

# 16. Approve Communication Contract

Endpoint:

```text
POST /v1/communications/{communication_reference_id}/approve
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
  approval_decision: string
  approval_note_safe: string | null
permission_context:
  required_permission_keys:
    - communication:approve
policy_context:
  required_policy_scopes:
    - communication:approve:policy
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
  communication_reference_id: string
  communication_status: string
  approval_status: string
  approved_at: datetime | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Approval must route through Communication Service.
- Approval does not guarantee delivery.
- Approval may be required before prepare-send or external delivery.
- Human review may be required for external/customer-facing communication.
```

---

# 17. Prepare Send Contract

Endpoint:

```text
POST /v1/communications/{communication_reference_id}/prepare-send
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
  send_purpose: string
  intended_channel: string
  recipient_confirmation_required: boolean
permission_context:
  required_permission_keys:
    - communication:send:prepare
policy_context:
  required_policy_scopes:
    - communication:send:prepare:policy
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
  communication_reference_id: string
  send_preparation_status: string
  send_ready: boolean
  missing_requirements_safe:
    - string
  delivery_request_reference_id: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Prepare-send is not delivery unless Communication Service explicitly owns a governed delivery handoff.
- Missing approval, recipient confirmation or policy checks must block send readiness.
- External delivery must not occur silently.
```

---

# 18. Link Objects Contract

Endpoint:

```text
POST /v1/communications/{communication_reference_id}/link-objects
```

Request shape:

```yaml
api_version: v1
contract_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null
payload:
  linked_object_refs:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: Add | Remove | Replace
permission_context:
  required_permission_keys:
    - communication:object:link
policy_context:
  required_policy_scopes:
    - communication:object:link:policy
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
  communication_reference_id: string
  linked_object_refs_visible:
    - target_object_type: string
      target_object_reference_id: string
      relationship_type: string
  link_operation: string
  updated_at: datetime
  restricted_fields_omitted: boolean
```

Rules:

```text
- Link operation must route through Communication Service.
- Linked object references must be validated by owning services.
- Link operation does not mutate linked object lifecycle directly.
```

---

# 19. Controlled Values

## 19.1 communication_type

```text
InternalNote
CustomerMessage
AgentMessage
ProviderMessage
OfficialDraft
OfficeActionResponseDraft
EmailRecord
CallNote
MeetingNote
PortalMessage
SystemGeneratedMessage
AIGeneratedDraft
Other
Unknown
```

## 19.2 communication_status

```text
Draft
Prepared
UnderReview
RevisionRequested
Approved
SendPrepared
Sent
Failed
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 19.3 communication_channel

```text
Internal
Email
Phone
Wechat
WhatsApp
Portal
System
ExternalPlatform
Unknown
```

## 19.4 recipient_type

```text
Customer
User
Agent
ServiceProvider
Partner
OfficialOffice
InternalTeam
ExternalContact
Unknown
```

## 19.5 recipient_role

```text
To
Cc
Bcc
From
ReplyTo
InternalReviewer
Unknown
```

## 19.6 relationship_type

```text
PrimaryCommunication
SupportingCommunication
DraftFor
ResponseTo
AttachmentFor
SourceFor
FollowUpFor
HistoricalReference
Unknown
```

## 19.7 review_decision

```text
Approve
RequestRevision
Reject
Escalate
NoDecision
Unknown
```

## 19.8 approval_decision

```text
Approve
Reject
RevokeApproval
Escalate
NoDecision
Unknown
```

## 19.9 review_status

```text
NotReviewed
UnderReview
Approved
RevisionRequested
Rejected
Escalated
Unknown
```

## 19.10 approval_status

```text
NotApproved
Approved
Rejected
Revoked
Escalated
Unknown
```

## 19.11 send_preparation_status

```text
Ready
NotReady
MissingApproval
MissingRecipient
PolicyRestricted
PermissionDenied
RequiresHumanReview
ChannelUnavailable
Error
Unknown
```

## 19.12 draft_status

```text
Completed
Partial
InsufficientContext
PolicyRestricted
PermissionDenied
RequiresHumanReview
Error
Unknown
```

## 19.13 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
SentImmutable
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 19.14 sort.field

```text
created_at
updated_at
sent_at
subject_safe
communication_status
communication_type
communication_channel
```

---

# 20. Validation Rules

Validation checklist:

```text
[ ] api_version is supported.
[ ] contract_version is supported.
[ ] communication_reference_id is valid where required.
[ ] idempotency_key is present for create.
[ ] communication_type is controlled.
[ ] communication_status is controlled where provided.
[ ] communication_channel is controlled where provided.
[ ] recipient refs are valid where required.
[ ] recipient addresses are safe and policy-filtered.
[ ] attachment document references are validated where provided.
[ ] linked object references are validated where provided.
[ ] review_decision and approval_decision are controlled where provided.
[ ] AI Context is present for AI-assisted draft preparation.
[ ] Human Review Context is present where policy requires review.
[ ] pagination follows Pagination Contract.
[ ] Permission Context is present for protected operations.
[ ] Policy Context is present for policy-controlled operations.
[ ] restricted fields are omitted unless policy allows them.
[ ] errors follow Error Contract.
```

---

# 21. Permission Rules

Required permission keys:

```text
communication:create
communication:read
communication:search
communication:update
communication:validate
communication:draft:prepare
communication:review
communication:approve
communication:send:prepare
communication:object:link
```

Rules:

```text
- Communication API must not grant permission.
- Permission Service evaluates required permission keys.
- PermissionDenied must stop protected operations.
- Permission decisions may be included only where policy allows safe exposure.
```

---

# 22. Policy Rules

Required policy scopes may include:

```text
communication:create:policy
communication:read:policy
communication:search:policy
communication:update:policy
communication:reference:policy
communication:visibility:policy
communication:recipient:visibility:policy
communication:draft:prepare:policy
communication:review:policy
communication:approve:policy
communication:send:prepare:policy
communication:object:link:policy
cross-organization:communication
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may redact body, recipients, addresses, attachments, linked objects, source references or total_count.
- Policy may downgrade response to metadata-only or safe-summary-only.
- Policy may require human review before approval or send-preparation.
- PolicyRestricted must stop or downgrade behavior.
```

---

# 23. AI and Human Review Rules

AI rules:

```text
- Communication Agent may read, summarize and draft only within Permission and Policy limits.
- AI output is a draft or summary, not sent communication.
- AI must not send, approve, issue, bind, or represent professional truth.
- AI output must mark AI-generated drafts and disclose missing context, source scope and policy omissions.
```

Human review:

```text
- Human review may be required before review, approval, send-preparation, external communication, customer-facing output or professional-risk communication.
- human_review_required must be explicit where policy requires review.
```

---

# 24. Idempotency and Event Rules

Idempotency:

```text
POST /v1/communications requires idempotency_key.
PATCH /v1/communications/{communication_reference_id} may require idempotency_key where owning service marks the operation duplicate-sensitive.
Review, approve, prepare-send and link endpoints may require idempotency_key for duplicate-sensitive operations.
Prepare-draft does not normally require idempotency unless result is persisted.
```

Events:

```text
CommunicationCreated may be emitted by Communication Service after successful creation.
Communication review/approval/send-preparation events may be reserved for later if event specs exist.
API layer must not emit events directly.
```

Rules:

```text
- Idempotent replay must not duplicate events.
- Event references are audit trace, not commands.
- API response must not claim an event unless the event spec exists and service emits it.
```

---

# 25. Error Rules

Controlled API errors:

```text
BadRequest
ValidationFailed
Unauthorized
PermissionDenied
PolicyRestricted
ReferenceInvalid
ReferenceNotFound
CommunicationReferenceInvalid
RecipientReferenceInvalid
AttachmentReferenceInvalid
LinkedObjectReferenceInvalid
RecipientAddressRestricted
SentCommunicationImmutable
DraftPreparationUnavailable
ReviewInvalid
ApprovalInvalid
SendPreparationBlocked
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
- Errors must not expose database IDs, restricted communication body, hidden recipients, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 26. Versioning Rules

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

# 27. Codex Implementation Notes

Codex must:

```text
cite Communication API Spec
cite Communication Service Spec
cite Communication Agent Spec for AI-assisted drafts
cite this Communication API Contract
use Reference Contract for communication_reference_id, recipients, attachments and linked references
use Error Contract for errors
use Pagination Contract for list/search
use Permission Context Contract before protected operations
use Policy Context Contract before policy-controlled response
use AI Context Contract for AI-assisted draft preparation
use Human Review Contract where policy requires review
use Idempotency Contract for create and duplicate-sensitive review/approval/send-preparation/link operations
use Versioning Contract for version validation
route all Communication mutation through Communication Service
invoke Document Service for attachment validation
invoke linked owning services for object reference validation where applicable
invoke Permission Service before protected behavior
invoke Policy Service before exposing body, recipients, addresses, attachments or linked objects
return safe errors only
write tests for create/read/update/search/validate-reference/prepare-draft/review/approve/prepare-send/link-objects
write tests for recipient and attachment validation
write tests that AI draft preparation does not approve or send
write tests that approval does not guarantee delivery
write tests that prepare-send does not silently deliver externally
write tests for sent communication immutability
write tests for human_review_required
write tests for idempotent create replay
write tests that API does not emit events directly
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for restricted_fields_omitted
write tests for VersionUnsupported
```

Codex must not:

```text
create Communication directly in API layer
query database directly from API contract implementation
use generic id where communication_reference_id is required
expose database IDs, restricted communication body or hidden recipient addresses
skip Permission or Policy checks
emit events directly from controller/API handler
return unrestricted total_count by default
send external communication from prepare-draft or prepare-send without governed Communication Service delivery process
approve AI-generated content without human/service review where required
complete Task, Matter or Order from Communication API
treat AI draft as professional truth or external communication
allow AI context to exceed evaluated_data_access_scope
```

---

# 28. Acceptance Criteria

This Communication API Contract is accepted only if:

```text
[ ] It defines Communication API purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites Communication API, Service and Agent specs.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines endpoint contract set.
[ ] It defines create request/response.
[ ] It defines read contract.
[ ] It defines update contract.
[ ] It defines search/list contract.
[ ] It defines validate-reference contract.
[ ] It defines prepare draft contract.
[ ] It defines review contract.
[ ] It defines approve contract.
[ ] It defines prepare send contract.
[ ] It defines link objects contract.
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

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Communication API Contract. Defines governed create, read, update, search, validate-reference, draft preparation, review, approval, send-preparation and object-link payloads, recipient/attachment/reference validation, Permission/Policy context, AI and human review, idempotency, event trace, errors, versioning and Codex implementation rules. |

---

**End of API Contract**
