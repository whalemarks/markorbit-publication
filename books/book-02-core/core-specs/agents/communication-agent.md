# Agent Specification — Communication Agent

**Spec ID:** B02-AGENT-COMMUNICATION  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Communication Agent  
**Agent Spec File:** core-specs/agents/communication-agent.md  
**Registry Key:** communication-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Communication; Agent; Permission; Policy; Event; Task; Matter; Order; Customer; Partner; Service Provider; Notification; Knowledge  
**Related Object Specs:** core-specs/objects/communication.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/task.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/customer.md; core-specs/objects/partner.md; core-specs/objects/service-provider.md; core-specs/objects/notification.md; core-specs/objects/knowledge.md  
**Related Service Specs:** core-specs/services/communication-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/task-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/customer-service.md; core-specs/services/partner-service.md; core-specs/services/service-provider-service.md; core-specs/services/notification-service.md; core-specs/services/knowledge-service.md  
**Related API Specs:** core-specs/api/communication-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/task-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/customer-api.md; core-specs/api/partner-api.md; core-specs/api/service-provider-api.md; core-specs/api/notification-api.md; core-specs/api/knowledge-api.md  
**Related Event Specs:** core-specs/events/communication-created.md; core-specs/events/notification-created.md; core-specs/events/task-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Communication Agent defines the governed AI Agent pattern for assisting Communication review, drafting, summarization, translation preparation, recipient-context checking and communication-to-task preparation in MarkOrbit Core.

It exists to help professionals prepare clear and traceable communications without allowing AI to become sender, legal notice issuer, customer-instruction approver, contract acceptor, external representative, service-provider negotiator, payment approver or silent communication delivery engine.

Communication Agent supports:

```text
communication thread summarization
communication draft preparation
reply suggestion
translation draft preparation
recipient/context check
communication gap detection
communication-to-task preparation
provider/customer/partner communication preparation
safe tone and consistency assistance
communication trace explanation
```

Communication Agent does not send external communications, approve legal wording, bind the company, accept instructions, create legal notices or bypass Communication Service.

---

# 2. Agent Meaning

Communication Agent means:

```text
a governed AI Agent that assists with Communication drafting and communication-context preparation through Communication Service boundaries.
```

Communication Agent does not mean:

```text
message sender
legal notice engine
customer instruction authority
contract acceptance authority
provider negotiation authority
payment commitment authority
unrestricted mailbox reader
private contact extractor
communication delivery engine
policy bypasser
```

Communication Agent may help answer:

```text
What did this thread say?
What reply draft can be prepared?
What action items should be extracted?
Which context is missing before replying?
What recipient or object should this communication reference?
What follow-up task should be prepared?
```

Communication Agent must not claim:

```text
The message has been sent.
The customer instruction has been accepted.
The legal notice has been issued.
The company has agreed to terms.
The provider has been selected.
The payment has been approved.
```

---

# 3. Registry Position

Registry entry:

```text
communication-agent
```

Required registry constraints:

```text
agent_type: CommunicationAgent
agent_role: CommunicationDraftingAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: DraftOnly
```

Allowed capabilities:

```text
Read
Summarize
Draft
PrepareCommunication
ValidateReference
ExplainTrace
```

Restricted capabilities:

```text
SendCommunication
AccessPrivateContact
AccessRestrictedContent
AccessRawDocument
AccessFinancialData
CreateObject
UpdateObject
```

Registry rule:

```text
Communication Agent may be considered for communication drafting and communication-context preparation.
Permission and Policy decide whether it may access specific Communication context and prepare specific drafts.
```

---

# 4. Agent Boundary

Communication Agent is responsible for:

```text
communication query preparation
communication reference validation request
safe communication summary generation
reply draft preparation
translation draft preparation
recipient and context check
missing-information detection
communication-to-task preparation
communication-to-notification preparation
communication trace explanation
```

Communication Agent is not responsible for:

```text
Communication lifecycle ownership
Communication delivery
external message sending
legal notice issuance
customer instruction approval
contract acceptance
payment commitment
Task creation without Task Service
Notification delivery
provider selection
professional approval
permission grant
policy evaluation
```

---

# 5. Governance Lock

Communication Agent must obey:

```text
Communication Agent may read, summarize and draft only within Permission and Policy limits.
Communication Agent output is a draft or summary, not sent communication.
Communication Agent must not send, approve, issue or bind any external communication.
Communication Agent must mark AI-generated drafts and disclose missing context, source scope, policy omissions and human-review requirements.
Communication Agent must route Communication creation and delivery through Communication Service and governed channel delivery.
```

This lock applies to all Communication Agent implementations.

---

# 6. Agent Identity Requirements

Every Communication Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: communication-agent
agent_contract_reference_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Agent identity must be validated through Agent Service.
- Agent status must be Active or explicitly allowed.
- Agent Contract is required for protected communication access.
- Suspended, revoked, archived or unknown agents must not perform Communication operations.
- Agent must not borrow human User identity.
```

---

# 7. Capability Rules

Allowed operations:

```text
summarizeCommunication
searchCommunicationsSafely
validateCommunicationReference
prepareCommunicationDraft
prepareReplyDraft
prepareTranslationDraft
prepareRecipientContextCheck
identifyCommunicationGaps
extractCommunicationActionItems
prepareTaskFromCommunication
explainCommunicationTrace
```

Disallowed operations:

```text
sendCommunication
approveExternalWording
issueLegalNotice
acceptCustomerInstruction
bindCompanyToTerms
commitPayment
selectProvider
createCommunicationWithoutService
deliverNotification
completeTask
```

Capability rule:

```text
Communication Agent may prepare communication context and drafts; Communication Service owns Communication creation and delivery governance.
```

---

# 8. Data Access Rules

Default data access:

```text
SafeSummaryOnly
```

Allowed data access scopes:

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
```

Restricted data access scopes:

```text
RestrictedContentWithHumanApproval
AccessRawDocument
AccessEvidence
AccessPricing
AccessPrivateContact
AccessFinancialData
```

Rules:

```text
- SafeSummaryOnly is the default.
- Policy may downgrade access to MetadataOnly or NoAccess.
- Raw thread bodies, attachments, private contacts and legal strategy require explicit policy.
- Customer instructions and service-provider negotiation details require contextual policy.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
private contact details
unredacted customer instructions
privileged legal strategy
payment data
bank details
provider pricing
contract terms
raw attachments
filing credentials
internal escalation notes
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:communication:prepare-draft
communication:read
communication:search
communication:validate
communication:draft:prepare
communication:create
communication:send
communication:recipient:validate
task:create
notification:create
customer:read
matter:read
order:read
partner:read
service-provider:read
knowledge:read
```

Rules:

```text
- Agent-level permission is required.
- Communication-domain permission is required.
- Related Customer/Matter/Order/Partner/Service Provider permission is required where those records are referenced.
- Sending permission is not implied by drafting permission.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentCommunicationDraftPolicy
CommunicationVisibilityPolicy
CommunicationReferencePolicy
CommunicationDraftPolicy
CommunicationRecipientPolicy
CommunicationSendPolicy
RestrictedCommunicationDataPolicy
CustomerInstructionPolicy
LegalNoticePolicy
ProviderCommunicationPolicy
CrossOrganizationCommunicationPolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether Communication Agent may read, summarize or draft.
- Policy may require human review before external communication.
- Policy may restrict raw thread bodies, attachments, private contacts and legal strategy.
- Policy may block legal notice, customer instruction or contract-related drafts.
- Policy may restrict cross-organization or cross-matter communication context.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Communication Summary Request

```yaml
operation: summarizeCommunication
agent_reference_id: string
agent_registry_key: communication-agent
actor_reference_id: string | null
organization_reference_id: string | null
communication_reference_id: string
summary_purpose: string
summary_depth: string
data_access_requested: string
correlation_id: string | null
```

## 11.2 Communication Draft Request

```yaml
operation: prepareCommunicationDraft
agent_reference_id: string
agent_registry_key: communication-agent
actor_reference_id: string | null
organization_reference_id: string | null
draft_purpose: string
communication_type: string
subject_object_type: string | null
subject_object_reference_id: string | null
recipient_context:
  recipient_type: string | null
  recipient_reference_id: string | null
source_context:
  communication_reference_ids: list[string]
  task_reference_id: string | null
  matter_reference_id: string | null
  order_reference_id: string | null
  knowledge_record_reference_ids: list[string]
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.3 Recipient Context Check Request

```yaml
operation: prepareRecipientContextCheck
agent_reference_id: string
communication_type: string
recipient_context:
  recipient_type: string | null
  recipient_reference_id: string | null
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
  partner_reference_id: string | null
  service_provider_reference_id: string | null
correlation_id: string | null
```

## 11.4 Communication-to-Task Request

```yaml
operation: prepareTaskFromCommunication
agent_reference_id: string
communication_reference_id: string
task_preparation_purpose: string
target_context:
  matter_reference_id: string | null
  order_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Communication Summary Response

```yaml
agent_reference_id: string
summary_reference_id: string | null
communication_reference_id: string
summary_type: string
safe_summary: string
action_items: list[string]
missing_context: list[string]
policy_omissions: list[string]
source_scope: string
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.2 Communication Draft Response

```yaml
agent_reference_id: string
draft_reference_id: string | null
preparation_status: string
safe_draft:
  communication_type: string
  draft_purpose: string
  subject: string | null
  body_draft: string | null
  recipient_type: string | null
  recipient_reference_id: string | null
  disclaimers: list[string]
  review_notes: list[string]
source_communication_reference_ids: list[string]
source_knowledge_record_reference_ids: list[string]
missing_context: list[string]
policy_omissions: list[string]
human_review_required: boolean
downstream_service_required: string | null
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Recipient Context Check Response

```yaml
agent_reference_id: string
recipient_check_reference_id: string | null
recipient_context_valid: boolean
validation_status: string
safe_reason: string | null
missing_items: list[string]
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.4 Communication-to-Task Response

```yaml
agent_reference_id: string
task_draft_reference_id: string | null
communication_reference_id: string
safe_task_draft:
  task_type: string | null
  title: string | null
  safe_summary: string | null
  suggested_priority: string | null
  required_inputs: list[string]
preparation_status: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must not imply Communication creation or delivery.
- Responses must disclose missing context and policy omissions.
- Responses must not expose restricted fields by default.
- Responses must identify required human review and downstream service.
```

---

# 13. Controlled Values

## 13.1 draft_purpose

```text
ClientReply
ProviderReply
PartnerReply
InternalUpdate
TaskFollowUp
StatusUpdate
DocumentRequest
EvidenceRequest
InstructionClarification
TranslationDraft
AIAssistedDraft
Unknown
```

## 13.2 communication_type

```text
Email
PortalMessage
InternalNote
PhoneCallNote
ChatMessage
WhatsApp
WeChat
SMS
Letter
LegalNotice
Unknown
```

## 13.3 summary_purpose

```text
InternalReview
ClientSupport
TaskPreparation
MatterReview
OrderReview
ProviderCoordination
PartnerCoordination
AuditReview
AIAssistedExplanation
Unknown
```

## 13.4 summary_depth

```text
Brief
Standard
DetailedSafe
RestrictedInternal
Unknown
```

## 13.5 task_preparation_purpose

```text
FollowUpTask
DocumentRequestTask
EvidenceReviewTask
ClientInstructionTask
ProviderCoordinationTask
DeadlineTask
InternalReviewTask
Unknown
```

## 13.6 preparation_status

```text
Prepared
Rejected
PolicyRestricted
PermissionDenied
HumanReviewRequired
DownstreamServiceRequired
Unknown
```

## 13.7 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
ContextMismatch
Unknown
```

## 13.8 source_scope

```text
CommunicationOnly
CommunicationThread
MatterContext
OrderContext
TaskContext
KnowledgeContext
PolicyFilteredContext
Unknown
```

## 13.9 confidence_level

```text
Low
Medium
High
Unknown
```

---

# 14. Human Review Rules

Human review is required when Communication Agent output may be used for:

```text
external communication
legal notice
customer instruction acceptance
provider negotiation
partner agreement context
payment or fee discussion
deadline commitment
filing instruction
contract-related statement
professional legal explanation
cross-organization disclosure
restricted content use
```

Human review is not required for:

```text
safe internal communication summary
safe metadata lookup
non-state-changing action item extraction
recipient-context checklist where no restricted content is exposed
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit before external sending.
- Human review reference must be passed to Communication Service where required.
```

---

# 15. Event and Audit Rules

Communication Agent operations must be traceable.

Trace must include:

```yaml
agent_registry_key: communication-agent
agent_reference_id: string
operation: string
communication_reference_id: string | null
draft_reference_id: string | null
communication_type: string | null
draft_purpose: string | null
target_object_type: string | null
target_object_reference_id: string | null
data_access_scope: string
execution_mode: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Communication Agent must not emit domain events directly.
- Event Service owns event recording.
- CommunicationCreated must only be emitted after Communication Service creates Communication.
- NotificationCreated must only be emitted after Notification Service creates Notification.
- Delivery events, where later defined, must be channel-governed and not AI-agent fabricated.
```

---

# 16. Relationship to Communication Service

Communication Agent must use Communication Service for:

```text
getCommunication
searchCommunications
validateCommunicationReference
prepareCommunicationDraft
createCommunication
prepareCommunicationAttachment
markCommunicationReviewed
```

Rules:

```text
- Communication Agent must not query or mutate communication store directly.
- Communication Service applies Communication domain rules.
- Permission and Policy are evaluated before protected Communication operations.
- Communication Agent may transform safe context into drafts or summaries.
```

---

# 17. Relationship to Task and Notification Services

Communication Agent may prepare downstream drafts.

Allowed:

```text
prepare follow-up task draft
prepare reminder context
prepare notification draft
prepare action item checklist
```

Rules:

```text
- Task creation must route through Task Service.
- Notification creation must route through Notification Service.
- Communication Agent output must not be treated as created Task or delivered Notification.
```

---

# 18. Relationship to Customer, Partner and Service Provider Services

Communication Agent may reference relationship context only through governed service access.

Rules:

```text
- Customer Service owns Customer reference and customer context.
- Partner Service owns Partner relationship context.
- Service Provider Service owns provider context.
- Communication Agent must not expose private contact data by default.
- Communication Agent must not approve partner/provider terms.
- Communication Agent must not accept customer instruction.
```

---

# 19. Error and Rejection Rules

Controlled rejection reasons:

```text
PermissionDenied
PolicyRestricted
AgentSuspended
AgentRevoked
AgentContractRequired
CapabilityNotAllowed
HumanReviewRequired
RestrictedDataRequested
CommunicationReferenceInvalid
RecipientContextInvalid
CustomerReferenceInvalid
PartnerReferenceInvalid
ServiceProviderReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden Communication content.
- Rejections must not expose private contacts or policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Communication Agent spec
cite Communication Service Specification
cite Communication Object Specification
cite Communication API Specification
cite Permission and Policy specs
validate agent_registry_key = communication-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected communication access
invoke Policy Service before communication content access
use SafeSummaryOnly by default
mark AI-generated drafts and summaries
preserve source communication/task/matter/order/knowledge references in output
disclose missing context and policy omissions
route Communication creation and review through Communication Service
route Notification preparation through Notification Service
route Task preparation through Task Service
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted data omission
write tests for invalid Communication reference
write tests that Communication Agent cannot send messages directly
write tests that Communication Agent cannot accept customer instructions
write tests that Communication Agent cannot expose private contacts by default
```

Codex must not:

```text
query Communication database directly
bypass Communication Service
bypass Permission or Policy
pass unrestricted message bodies into prompts
treat AI draft as sent Communication
approve external wording
issue legal notice
accept customer instruction
commit payment or contract terms
create tasks or notifications directly
emit domain events directly
```

---

# 21. Acceptance Criteria

This Communication Agent Specification is accepted only if:

```text
[ ] It defines Communication Agent purpose.
[ ] It defines Agent meaning.
[ ] It defines registry position.
[ ] It defines Agent boundary.
[ ] It defines governance lock.
[ ] It defines identity requirements.
[ ] It defines capability rules.
[ ] It defines data access rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines request patterns.
[ ] It defines response patterns.
[ ] It defines controlled values.
[ ] It defines human review rules.
[ ] It defines event and audit rules.
[ ] It defines relationship to Communication Service.
[ ] It defines relationship to Task and Notification Services.
[ ] It defines relationship to Customer, Partner and Service Provider Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Communication Agent specification. Defines governed communication summarization, drafting, recipient-context checking, communication-to-task preparation and trace rules under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
