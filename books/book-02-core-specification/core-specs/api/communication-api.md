# API Specification — Communication API

**Spec ID:** B02-API-COMMUNICATION  
**Spec Type:** API Specification  
**API Name:** Communication API  
**API File:** core-specs/api/communication-api.md  
**Related Domain:** core-specs/domains/communication.md  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/customer.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/task.md; core-specs/objects/notification.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/communication-service.md; core-specs/services/customer-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/task-service.md; core-specs/services/notification-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related Event Specs:** core-specs/events/communication-created.md; core-specs/events/notification-created.md; core-specs/events/document-created.md; core-specs/events/evidence-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/communication-api-contract.md; core-specs/contracts/events/communication-created-payload.md  
**Related Agent Specs:** core-specs/agents/communication-agent.md; core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**API Version:** v0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication API exposes governed Communication operations for MarkOrbit Core.

It allows authorized consumers to create, read, update, search, validate, draft, link and prepare Communication references without treating Communication as Notification, legal notice effectiveness, delivery guarantee, customer instruction approval, task completion, evidence proof, document truth, filing submission or AI autonomous external outreach.

Communication API exists to support:

```text
governed internal and external message context
customer / agent / service-provider communication records
matter/order/task communication context
communication draft preparation
document attachment reference
communication-to-evidence preparation
policy-controlled visibility and content access
AI-assisted drafting under governance
event trace access
API-safe communication reference validation
```

Communication API does not guarantee message delivery by itself, create legal effect, prove facts, approve instructions, file applications or replace professional review.

---

# 2. API Meaning

Communication API means:

```text
a governed interface for operating Communication references through Communication Service.
```

Communication API does not mean:

```text
Notification API
email provider API
SMS provider API
legal notice API
filing API
Evidence API
Document truth API
Task completion API
AI outreach API
```

Communication is a governed exchange or message context.

Notification is an alert/reminder.

Document stores artifacts.

Evidence organizes proof context.

Delivery channels and legal-effect communications require separate policy and execution governance.

---

# 3. API Boundary

Communication API is responsible for:

```text
Communication create request intake
Communication read/search/list access
Communication update request intake
Communication reference validation
Communication draft preparation request intake
Communication link request intake where explicitly governed
Attachment/document reference registration
Communication-to-evidence preparation
safe Communication response shaping
Permission/Policy enforcement for Communication operations
Communication-related Event reference exposure where allowed
AI Agent access boundary for Communication operations
controlled API errors
```

Communication API is not responsible for:

```text
guaranteed external delivery
legal notice effectiveness
official filing execution
Task completion
Matter or Order lifecycle ownership
Document storage truth
Evidence sufficiency
payment or invoice ownership
AI autonomous external outreach
```

---

# 4. Related Core Domain

Related domain:

```text
core-specs/domains/communication.md
```

Domain rule:

```text
Communication records governed exchanges and message context.
Communication is not Notification, delivery proof, legal notice, Evidence, Document truth, filing or professional approval by itself.
```

The API must preserve this distinction in every endpoint.

---

# 5. Related Core Objects

Related objects:

```text
core-specs/objects/communication.md
core-specs/objects/customer.md
core-specs/objects/matter.md
core-specs/objects/order.md
core-specs/objects/task.md
core-specs/objects/notification.md
core-specs/objects/document.md
core-specs/objects/evidence.md
core-specs/objects/agent.md
core-specs/objects/service-provider.md
core-specs/objects/permission.md
core-specs/objects/policy.md
```

Object rules:

```text
- Communication API returns communication_reference_id.
- Communication API may reference Customer, Matter, Order, Task, Notification, Document, Evidence, Agent or Service Provider context but must not create or execute them silently.
- Communication creation is not delivery proof.
- Communication content is restricted by default.
- Communication may produce Document or Evidence preparation context only through owning services.
```

---

# 6. Related Core Services

Related services:

```text
core-specs/services/communication-service.md
core-specs/services/customer-service.md
core-specs/services/matter-service.md
core-specs/services/order-service.md
core-specs/services/task-service.md
core-specs/services/notification-service.md
core-specs/services/document-service.md
core-specs/services/evidence-service.md
core-specs/services/agent-service.md
core-specs/services/service-provider-service.md
core-specs/services/permission-service.md
core-specs/services/policy-service.md
core-specs/services/event-service.md
```

Service rules:

```text
- Communication API must invoke Communication Service for Communication behavior.
- Communication API must validate related references through their owning services where required.
- Communication API must invoke Permission Service where operation requires authorization.
- Communication API must invoke Policy Service where contextual constraints apply.
- Communication API must not emit Communication events directly; Communication Service and Event Service govern events.
- Document and Evidence creation must route through Document Service and Evidence Service respectively.
```

---

# 7. Related Core Events

Related events:

```text
core-specs/events/communication-created.md
core-specs/events/notification-created.md
core-specs/events/document-created.md
core-specs/events/evidence-created.md
core-specs/events/permission-evaluated.md
core-specs/events/policy-evaluated.md
```

Event rules:

```text
- createCommunication may result in CommunicationCreated.
- Communication attachments may reference DocumentCreated only when Document Service creates the Document.
- Communication-to-Evidence preparation may result in EvidenceCreated only when Evidence Service creates Evidence.
- API consumers must not fabricate CommunicationCreated.
- CommunicationCreated is message-context trace, not delivery proof, legal notice, instruction approval or Task completion.
- Event payload visibility must respect Permission and Policy.
```

---

# 8. API Operations

## 8.1 Operation: Create Communication

**Operation Category:** Create  
**Method:** POST  
**Path:** `/communications`  
**Owning Service Operation:** `createCommunication`  
**Permission Required:** `communication:create`  
**Policy Required:** `CommunicationCreationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Service Must Emit CommunicationCreated

Meaning:

```text
Create a governed Communication reference and message-context record.
```

Non-meaning:

```text
does not guarantee delivery
does not create legal notice
does not approve customer instruction
does not complete Task
does not create Evidence automatically
does not file application
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
Communication Service createCommunication
  ↓
Event Service record CommunicationCreated
  ↓
Safe API response
```

## 8.2 Operation: Get Communication

**Operation Category:** Read  
**Method:** GET  
**Path:** `/communications/{communication_reference_id}`  
**Owning Service Operation:** `getCommunication`  
**Permission Required:** `communication:read`  
**Policy Required:** `CommunicationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
Retrieve a safe Communication view.
```

Non-meaning:

```text
does not expose full message content automatically
does not expose contact details automatically
does not prove delivery or legal effect automatically
```

## 8.3 Operation: Search Communications

**Operation Category:** Search  
**Method:** GET  
**Path:** `/communications`  
**Owning Service Operation:** `searchCommunications`  
**Permission Required:** `communication:search`  
**Policy Required:** `CommunicationVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** No Event

Meaning:

```text
Search Communication references using controlled filters.
```

Non-meaning:

```text
does not provide unrestricted mailbox access
does not expose restricted content, recipient, customer, matter or strategy data by default
```

## 8.4 Operation: Update Communication

**Operation Category:** Update  
**Method:** PATCH  
**Path:** `/communications/{communication_reference_id}`  
**Owning Service Operation:** `updateCommunication`  
**Permission Required:** `communication:update`  
**Policy Required:** `CommunicationUpdatePolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where sensitive  
**Event Behavior:** Service May Emit CommunicationUpdated where event is defined

Meaning:

```text
Update governed Communication metadata, status, linkage or safe summary under Communication Service rules.
```

Non-meaning:

```text
does not rewrite communication history
does not prove delivery
does not approve instruction
does not mutate Matter, Order or Task state automatically
```

## 8.5 Operation: Validate Communication Reference

**Operation Category:** Validate  
**Method:** POST  
**Path:** `/communications/reference/validate`  
**Owning Service Operation:** `validateCommunicationReference`  
**Permission Required:** `communication:validate`  
**Policy Required:** `CommunicationReferencePolicy`  
**AI Agent Access:** Allowed under contract  
**Event Behavior:** No Event unless service requires audit event

Meaning:

```text
Validate that a Communication reference exists and may be used in the requested context.
```

Non-meaning:

```text
does not prove delivery
does not prove legal notice
does not authorize instruction
does not authorize raw content access
```

## 8.6 Operation: Link Communication to Object

**Operation Category:** Link  
**Method:** POST  
**Path:** `/communications/{communication_reference_id}/links`  
**Owning Service Operation:** `linkCommunicationToObject`  
**Permission Required:** `communication:link`  
**Policy Required:** `CommunicationLinkPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-suggested  
**Event Behavior:** Service May Emit CommunicationUpdated or future LinkEvent where defined

Meaning:

```text
Create a governed relationship between Communication and a target Core object.
```

Non-meaning:

```text
does not create target object
does not approve instruction
does not complete Task
does not file or submit anything
```

## 8.7 Operation: Prepare Communication Draft

**Operation Category:** Action  
**Method:** POST  
**Path:** `/communications/drafts/prepare`  
**Owning Service Operation:** `prepareCommunicationDraft`  
**Permission Required:** `communication:draft:prepare`  
**Policy Required:** `CommunicationDraftPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-drafted  
**Event Behavior:** Service May Emit PolicyEvaluated; must not emit CommunicationCreated unless createCommunication succeeds

Meaning:

```text
Prepare a governed Communication draft for human review or downstream creation.
```

Non-meaning:

```text
does not create Communication automatically
does not send message
does not approve external wording
does not create legal notice
```

## 8.8 Operation: Register Communication Attachment

**Operation Category:** Action  
**Method:** POST  
**Path:** `/communications/{communication_reference_id}/attachments`  
**Owning Service Operation:** `registerCommunicationAttachment`  
**Permission Required:** `communication:attachment:register`  
**Policy Required:** `CommunicationAttachmentPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Must route through Document Service if Document is created

Meaning:

```text
Register a governed Document reference as Communication attachment context.
```

Non-meaning:

```text
does not create Document unless Document Service creates it
does not prove attachment content
does not create Evidence automatically
does not approve filing use
```

## 8.9 Operation: Prepare Evidence from Communication

**Operation Category:** Action  
**Method:** POST  
**Path:** `/communications/{communication_reference_id}/evidence/prepare`  
**Owning Service Operation:** `prepareEvidenceFromCommunication`  
**Permission Required:** `communication:evidence:prepare`  
**Policy Required:** `CommunicationEvidencePreparationPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI-assisted  
**Event Behavior:** Must route through Evidence Service if Evidence is created

Meaning:

```text
Prepare a governed Evidence creation request from Communication context.
```

Non-meaning:

```text
does not create Evidence unless Evidence Service accepts it
does not prove legal fact
does not approve evidence sufficiency
does not expose restricted message content by default
```

## 8.10 Operation: Mark Communication Reviewed

**Operation Category:** StateTransition  
**Method:** POST  
**Path:** `/communications/{communication_reference_id}/reviewed`  
**Owning Service Operation:** `markCommunicationReviewed`  
**Permission Required:** `communication:review:mark`  
**Policy Required:** `CommunicationReviewPolicy`  
**AI Agent Access:** Restricted / HumanReviewRequired where AI review used  
**Event Behavior:** Service May Emit audit event where defined

Meaning:

```text
Mark a governed Communication as reviewed for an authorized review context.
```

Non-meaning:

```text
does not approve legal conclusion automatically
does not approve customer instruction automatically
does not complete Task automatically
does not prove delivery
```

## 8.11 Operation: List Communication Events

**Operation Category:** ObserveEvent  
**Method:** GET  
**Path:** `/communications/{communication_reference_id}/events`  
**Owning Service Operation:** `listCommunicationEvents`  
**Permission Required:** `communication:event:read`  
**Policy Required:** `EventVisibilityPolicy`  
**AI Agent Access:** Restricted  
**Event Behavior:** Read Events Only

Meaning:

```text
List safe Communication-related Event references.
```

Non-meaning:

```text
does not expose restricted event payload
does not allow event fabrication
does not allow event replay as command
```

---

# 9. Request Contracts

## 9.1 Create Communication Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | required
body:
  actor_reference_id: string
  organization_reference_id: string | null
  communication_type: string
  communication_status: string | optional
  communication_direction: string
  channel_type: string
  sender_type: string
  sender_reference_id: string | null
  recipient_type: string
  recipient_reference_id: string | null
  subject_object_type: string | null
  subject_object_reference_id: string | null
  source_task_reference_id: string | null
  source_notification_reference_id: string | null
  title: string | null
  safe_summary: string | null
  content_reference_id: string | null
  source_type: string
  request_context: object
  ai_context:
    ai_drafted: boolean
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
```

## 9.2 Update Communication Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  communication_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  communication_status: string | optional
  title: string | optional
  safe_summary: string | optional
  request_context: object
```

## 9.3 Validate Communication Reference Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  communication_reference_id: string
  intended_use: string
  target_context:
    target_object_type: string | null
    target_object_reference_id: string | null
```

## 9.4 Link Communication to Object Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  communication_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_reason: string | null
  request_context: object
```

## 9.5 Prepare Communication Draft Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  draft_purpose: string
  communication_type: string
  channel_type: string
  subject_object_type: string | null
  subject_object_reference_id: string | null
  recipient_context:
    recipient_type: string | null
    recipient_reference_id: string | null
  source_context:
    task_reference_id: string | null
    notification_reference_id: string | null
    matter_reference_id: string | null
    order_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

## 9.6 Register Attachment Request

```yaml
headers:
  X-Correlation-ID: string | optional
  X-Idempotency-Key: string | optional
path_parameters:
  communication_reference_id: string
body:
  actor_reference_id: string
  organization_reference_id: string | null
  document_reference_id: string | null
  file_reference_id: string | null
  attachment_type: string
  request_context: object
```

## 9.7 Prepare Evidence from Communication Request

```yaml
body:
  actor_reference_id: string
  organization_reference_id: string | null
  evidence_type: string
  evidence_purpose: string
  target_object_type: string | null
  target_object_reference_id: string | null
  ai_context:
    agent_identity_reference_id: string | null
    agent_contract_reference_id: string | null
  request_context: object
```

Request rules:

```text
- Requests must not include unrestricted raw message body, contact data, secrets, privileged notes or raw attachments by default.
- Requests must use controlled communication_type, communication_status, communication_direction, channel_type, sender_type, recipient_type, source_type and link_type values.
- AI-drafted communication content must be explicitly marked.
- AI-originated requests must include Agent context where required.
```

---

# 10. Response Contracts

## 10.1 Communication Response

```yaml
status: 200
body:
  communication_reference_id: string
  communication_type: string
  communication_status: string
  communication_direction: string
  channel_type: string
  sender_type: string
  sender_reference_id: string | null
  recipient_type: string
  recipient_reference_id: string | null
  subject_object_type: string | null
  subject_object_reference_id: string | null
  source_task_reference_id: string | null
  source_notification_reference_id: string | null
  title: string | null
  safe_summary:
    source_type: string
    created_at: datetime
    updated_at: datetime | null
    content_summary: string | null
  attachment_document_reference_ids: list[string]
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.2 Create Communication Response

```yaml
status: 201
body:
  communication_reference_id: string
  communication_status: string
  review_required: boolean
  related_event_reference_ids:
    - communication_created_event_id
  restricted_fields_omitted: true
  correlation_id: string | null
```

## 10.3 Communication Reference Validation Response

```yaml
status: 200
body:
  communication_reference_id: string
  valid: boolean
  validation_status: string
  reason_code: string
  safe_detail: string | null
  correlation_id: string | null
```

## 10.4 Communication Draft Response

```yaml
status: 200
body:
  communication_draft_reference_id: string | null
  usable_for_communication_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.5 Attachment Registration Response

```yaml
status: 200
body:
  communication_reference_id: string
  document_reference_id: string | null
  attachment_status: string
  related_event_reference_ids: list[string]
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

## 10.6 Evidence Preparation Response

```yaml
status: 200
body:
  communication_reference_id: string
  evidence_draft_reference_id: string | null
  usable_for_evidence_creation: boolean
  missing_items: list[string]
  review_required: boolean
  policy_decision_reference_id: string | null
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

Response rules:

```text
- Responses must not imply delivery proof, legal notice, customer instruction approval, Task completion, Evidence sufficiency or filing.
- Responses must not expose restricted raw message content, contact data, privileged notes or attachment content by default.
- Responses must distinguish Communication references from Notification, Document, Evidence, Task, Matter and Order references.
- Responses must identify review requirements for AI-drafted content.
```

---

# 11. Controlled Values

## 11.1 communication_type

```text
Email
PhoneCall
Meeting
Chat
PortalMessage
AgentInstruction
CustomerInstruction
InternalNote
SystemMessage
DocumentExchange
Other
Unknown
```

## 11.2 communication_status

```text
Draft
Prepared
ReviewRequired
Created
SentReferenceOnly
Received
Reviewed
Archived
DeletedReferenceOnly
Unknown
```

## 11.3 communication_direction

```text
Inbound
Outbound
Internal
System
Unknown
```

## 11.4 channel_type

```text
Email
Phone
WeChat
WhatsApp
Portal
System
Meeting
Offline
ExternalIntegration
Unknown
```

## 11.5 sender_type

```text
User
Customer
Agent
ServiceProvider
Partner
Organization
System
Unknown
```

## 11.6 recipient_type

```text
User
Customer
Agent
ServiceProvider
Partner
Organization
Role
Queue
System
Unknown
```

## 11.7 source_type

```text
ProfessionalInput
CustomerInput
AgentInput
ServiceProviderInput
TaskDerived
NotificationDerived
SystemGenerated
AIAssisted
Migration
ExternalIntegration
APIRequest
Unknown
```

## 11.8 link_type

```text
PrimaryCommunication
SupportingCommunication
SourceCommunication
DerivedCommunication
InstructionReference
EvidenceSource
DocumentExchange
ReferenceOnly
Unknown
```

## 11.9 draft_purpose

```text
ClientUpdate
AgentInstruction
CustomerQuestion
InternalReview
DocumentRequest
EvidenceRequest
TaskFollowUp
MatterUpdate
OrderUpdate
AIAssistedDraft
Unknown
```

## 11.10 attachment_type

```text
SourceAttachment
SupportingAttachment
DocumentExchange
EvidenceCandidate
ReferenceOnly
Unknown
```

## 11.11 attachment_status

```text
Registered
Rejected
PolicyRestricted
PermissionDenied
ReviewRequired
Unknown
```

## 11.12 validation_status

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

## 11.13 intended_use

```text
TaskContext
MatterContext
OrderContext
CustomerContext
DocumentContext
EvidencePreparation
AIAgentAnalysis
AuditReference
Unknown
```

---

# 12. Permission Rules

Permission keys:

```text
communication:create
communication:read
communication:search
communication:update
communication:validate
communication:link
communication:draft:prepare
communication:attachment:register
communication:evidence:prepare
communication:review:mark
communication:event:read
```

Rules:

```text
- Communication read/search must be permission-controlled.
- Communication creation must not imply delivery, legal notice or instruction approval.
- Communication validation must not authorize raw content access or downstream object mutation.
- Draft preparation requires separate permission.
- Attachment registration and Evidence preparation require separate permissions and downstream service rules.
- Permission evaluation must be context-specific.
- API must return PermissionDenied when actor lacks required action permission.
```

---

# 13. Policy Rules

Policy scopes:

```text
CommunicationCreationPolicy
CommunicationUpdatePolicy
CommunicationVisibilityPolicy
CommunicationReferencePolicy
CommunicationLinkPolicy
CommunicationDraftPolicy
CommunicationAttachmentPolicy
CommunicationEvidencePreparationPolicy
CommunicationReviewPolicy
EventVisibilityPolicy
AIAgentCommunicationAccessPolicy
RestrictedCommunicationContentPolicy
CrossOrganizationCommunicationPolicy
```

Rules:

```text
- Policy must restrict visibility of sensitive Communication fields and raw content.
- Policy may require human review for AI-drafted communications.
- Policy may restrict cross-organization Communication lookup.
- Policy may restrict recipient details, message bodies, attachments, customer strategy, privileged notes and legal instructions.
- Policy may restrict Evidence preparation from Communication.
- Policy failure must return safe PolicyRestricted error.
```

---

# 14. AI Agent Access Rules

AI Agent access:

```text
Create Communication: Restricted / HumanReviewRequired where AI-drafted
Get Communication: Restricted
Search Communications: Restricted
Update Communication: Restricted / HumanReviewRequired where sensitive
Validate Communication Reference: Allowed under contract
Link Communication to Object: Restricted / HumanReviewRequired where AI-suggested
Prepare Communication Draft: Restricted / HumanReviewRequired
Register Communication Attachment: Restricted
Prepare Evidence from Communication: Restricted / HumanReviewRequired
Mark Communication Reviewed: Restricted / HumanReviewRequired where AI review used
List Communication Events: Restricted
```

AI Agents may:

```text
summarize safe Communication metadata
prepare Communication drafts for human review
flag missing recipient, subject or attachment context
validate Communication references for authorized actions
suggest Communication-to-object links for human review
prepare Evidence request draft from Communication context for human review
summarize communication trace where allowed
```

AI Agents must not:

```text
fabricate Communication
fabricate CommunicationCreated events
treat AI-drafted Communication as approved external message
send message without governed communication channel and review
treat Communication as legal notice or delivery proof
approve customer instruction or professional conclusion
complete Task or workflow through Communication API
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

Communication API may expose:

```text
CommunicationCreated
NotificationCreated
DocumentCreated
EvidenceCreated
PermissionEvaluated
PolicyEvaluated
```

Rules:

```text
- Event detail visibility must be Permission and Policy controlled.
- Restricted event payload fields must be omitted.
- Events must not be replayed as commands.
- API clients must not create Communication events directly.
- CommunicationCreated must not be treated as delivery proof, legal notice, customer instruction approval, Evidence creation, Task completion or filing.
```

---

# 16. Validation Rules

Validation checklist:

```text
[ ] Request schema is valid.
[ ] communication_reference_id is present where required.
[ ] actor_reference_id is present.
[ ] organization_reference_id is valid where provided.
[ ] sender_reference_id is valid where provided.
[ ] recipient_reference_id is valid where provided.
[ ] subject_object_type and subject_object_reference_id are valid where provided.
[ ] source_task_reference_id is valid where provided.
[ ] source_notification_reference_id is valid where provided.
[ ] document_reference_id is valid for attachment registration where provided.
[ ] communication_type is controlled.
[ ] communication_status is controlled.
[ ] communication_direction is controlled.
[ ] channel_type is controlled.
[ ] sender_type is controlled.
[ ] recipient_type is controlled.
[ ] source_type is controlled.
[ ] link_type is controlled where applicable.
[ ] draft_purpose is controlled where applicable.
[ ] attachment_type is controlled where applicable.
[ ] Permission is evaluated where required.
[ ] Policy is evaluated where required.
[ ] Restricted communication/content/recipient/customer/strategy fields are omitted or allowed.
[ ] AI-drafted communication data is marked where applicable.
[ ] AI Agent Contract is present where required.
[ ] CommunicationCreated is emitted after createCommunication succeeds.
[ ] Draft preparation does not create Communication automatically.
[ ] Attachment registration routes through Document Service where Document creation is required.
[ ] Evidence preparation routes through Evidence Service where Evidence creation is required.
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
CommunicationReferenceInvalid
SenderReferenceInvalid
RecipientReferenceInvalid
SubjectReferenceInvalid
SourceTaskReferenceInvalid
SourceNotificationReferenceInvalid
DocumentReferenceInvalid
EvidencePreparationInvalid
ValidationFailed
DuplicateRejected
StateInvalid
RestrictedFieldViolation
RestrictedCommunicationContent
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
- Errors must not expose restricted Communication content.
- Errors must not expose recipient details, message bodies, attachments, customer strategy or privileged notes.
- Errors must not expose unrelated Customer, Matter, Order, Task, Document or Evidence details.
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
- communication_type, communication_status, communication_direction, channel_type, sender_type, recipient_type and link_type changes must be documented.
- Event behavior changes must be documented.
- Permission and Policy requirement changes must be documented.
- AI communication behavior changes must be documented.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Communication API spec
cite Communication Service Specification
cite Communication Object Specification
cite CommunicationCreated Event Specification
cite Customer/Matter/Order/Task/Notification/Document/Evidence specs where references are used
cite Permission and Policy specs before protected operations
implement request validation before service invocation
enforce Permission and Policy before protected operations
return safe metadata by default
write tests for invalid communication_reference_id
write tests for invalid sender/recipient/source/subject references
write tests for PermissionDenied
write tests for PolicyRestricted
write tests that Communication creation does not prove delivery or legal notice
write tests that Communication creation does not approve customer instruction
write tests that draft preparation does not create Communication automatically
write tests that attachment registration does not create Evidence automatically
write tests that Evidence preparation routes through Evidence Service
write tests for AI Agent Contract and human review requirement
write tests for CommunicationCreated event after successful create
```

Codex must not:

```text
write directly to database bypassing Communication Service
allow UI to emit CommunicationCreated directly
treat Communication as Notification
treat Communication as delivery proof or legal notice
treat Communication as customer instruction approval
treat Communication as Evidence or Document truth
send external messages without governed channel and review
expose restricted message bodies, attachments or recipient data for convenience
allow AI to fabricate Communication references or events
```

---

# 20. Acceptance Criteria

This API Specification is accepted only if:

```text
[ ] It defines Communication API purpose.
[ ] It defines Communication API meaning.
[ ] It defines Communication API boundary.
[ ] It cites related Domain, Object, Service and Event specs.
[ ] It defines create, read, search, update, validate, link, draft preparation, attachment registration, evidence preparation, review marking and event-list operations.
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
| 0.1.0 | Draft | Initial Communication API specification. Defines governed Communication exchange/message interface and separates Communication API from Notification, delivery proof, legal notice, customer instruction approval, Evidence, Document truth, filing and AI autonomous outreach. |

---

**End of API Specification**
