# Agent Specification — AI Agent Governance

**Spec ID:** B02-AGENT-AI-GOVERNANCE  
**Spec Type:** Agent Governance Specification  
**Agent Spec Name:** AI Agent Governance  
**Agent Spec File:** core-specs/agents/ai-agent-governance.md  
**Related Core Domains:** Agent; Permission; Policy; Knowledge; Task; Event; Communication; Workflow Contract; Routing  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/knowledge.md; core-specs/objects/task.md; core-specs/objects/event.md; core-specs/objects/communication.md; core-specs/objects/workflow-contract.md; core-specs/objects/routing.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/knowledge-service.md; core-specs/services/task-service.md; core-specs/services/event-service.md; core-specs/services/communication-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/routing-service.md  
**Related API Specs:** core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/knowledge-api.md; core-specs/api/task-api.md; core-specs/api/event-api.md; core-specs/api/communication-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/routing-api.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/routing-evaluated.md  
**Related Contract Specs:** core-specs/contracts/api/agent-api-contract.md; core-specs/contracts/agents/agent-runtime-contract.md  
**Related Agent Specs:** core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Cross-Phase Governance  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

AI Agent Governance defines the mandatory governance rules for all AI Agents, automation agents and agent-assisted operations in MarkOrbit Core.

It exists to ensure that AI can support professional work without becoming the source of professional truth, uncontrolled system authority, hidden decision-maker, unrestricted data reader, autonomous legal actor or silent executor.

AI Agent Governance provides the common rules for:

```text
agent identity
agent capability boundary
agent permission evaluation
agent policy evaluation
knowledge access
document and evidence access
task preparation
communication drafting
workflow support
routing recommendation
event trace
human review
auditability
failure handling
Codex implementation boundaries
```

AI enhances professionals.

AI does not define professional truth.

---

# 2. Governance Meaning

AI Agent Governance means:

```text
a Core-level governance layer that controls how AI Agents may read, draft, suggest, prepare, summarize, validate, classify and request actions.
```

AI Agent Governance does not mean:

```text
AI product feature design
prompt library only
model selection only
unrestricted automation
human replacement
legal conclusion engine
filing engine
payment authority
customer instruction authority
service-provider selection authority
```

The governance rule is:

```text
AI may assist.
Core must govern.
Human responsibility must remain explicit.
Services must own execution.
Events must record trace.
```

---

# 3. Core Position

AI Agent Governance sits above individual Agent specs and below Core principles.

It constrains:

```text
core-specs/agents/*
core-specs/api/* where AI Agent Access Rules exist
core-specs/services/* where agent access or agent-prepared operations exist
core-specs/events/* where AI-driven actions are referenced
workflow-contract applications involving agents
task creation or completion involving agents
communication drafting involving agents
routing recommendations involving agents
knowledge retrieval involving agents
```

It must be cited by every Agent spec and every Codex task that implements agent behavior.

---

# 4. Governance Boundary

AI Agent Governance is responsible for:

```text
AI role boundary
AI capability boundary
AI permission and policy preconditions
AI knowledge access constraints
AI action-preparation constraints
AI human-review requirements
AI event trace requirements
AI restricted-data handling
AI error and rejection rules
AI Codex implementation constraints
```

AI Agent Governance is not responsible for:

```text
choosing a specific AI model
writing prompt text for product UX
defining professional legal standards
owning domain object lifecycle
executing business services directly
approving final legal or business decisions
replacing Permission Service
replacing Policy Service
replacing Event Service
replacing human responsibility
```

---

# 5. Core Governance Lock

All AI Agent operations must obey this lock:

```text
AI Agent may read only what Permission and Policy allow.
AI Agent may draft, summarize, suggest, classify, validate and prepare.
AI Agent may not silently create professional truth, approve legal conclusions, submit filings, settle payments, select providers, send external communications, complete tasks or mutate domain state outside governed services.
AI Agent output is advisory until accepted through governed human or service process.
```

This lock is non-negotiable.

---

# 6. Agent Identity Rules

Every AI Agent must have an explicit Agent identity.

Required identity fields:

```yaml
agent_reference_id: string
agent_type: string
agent_status: string
agent_name: string
agent_purpose: string
owner_user_reference_id: string | null
owner_organization_reference_id: string | null
capability_profile_reference_id: string | null
governance_profile_reference_id: string | null
agent_contract_reference_id: string | null
```

Rules:

```text
- No anonymous AI Agent may perform governed operations.
- No AI Agent may use a human User identity as its own identity.
- No AI Agent may be treated as Service Provider.
- No AI Agent may self-create, self-authorize or self-escalate authority.
- Agent status must be checked before use.
- Suspended, revoked, archived or unknown agents must not perform protected operations.
```

---

# 7. Agent Role Rules

Allowed AI Agent roles include:

```text
ReadOnlyAssistant
DraftingAssistant
ClassificationAssistant
KnowledgeRetrievalAssistant
TaskPlanningAssistant
CommunicationDraftingAssistant
WorkflowSupportAssistant
RoutingSupportAssistant
AuditSupportAssistant
IntegrationAssistant
```

Disallowed implicit roles:

```text
FinalLegalDecisionMaker
PaymentApprover
FilingSubmitter
ProviderSelectorWithoutReview
TaskCompleterWithoutReview
CustomerInstructionApprover
PermissionGrantor
PolicyBypasser
HiddenHumanUser
UnrestrictedDataReader
```

Rule:

```text
AI Agent role must be explicit, bounded and testable.
```

---

# 8. Capability Boundary

AI capabilities must be declared before use.

Capability categories:

```text
Read
Summarize
Classify
Extract
ValidateReference
Draft
Suggest
PrepareAction
PrepareTask
PrepareCommunication
PrepareWorkflow
PrepareRouting
RequestKnowledge
ExplainTrace
```

Restricted capability categories:

```text
CreateObject
UpdateObject
CompleteTask
SendCommunication
SelectRouting
ApplyWorkflow
AccessRestrictedContent
AccessRawDocument
AccessEvidence
AccessPricing
AccessPrivateContact
AccessFinancialData
```

Rules:

```text
- Restricted capabilities require explicit Permission and Policy evaluation.
- Some restricted capabilities may require human review even when permitted.
- Capability declaration is not authorization.
- Authorization must be evaluated per operation and per context.
```

---

# 9. Permission Rules

AI Agent operations must pass Permission evaluation where protected.

Required permission pattern:

```text
agent:<operation>
target-domain:<operation>
data-scope:<access>
```

Examples:

```text
agent:knowledge:request-access
knowledge:read
task:communication:prepare
communication:draft:prepare
routing:evaluate
routing:select
```

Rules:

```text
- Agent permission is necessary but not sufficient.
- Target domain permission is also required.
- Permission must be evaluated against actor, agent, organization, target object and intended use.
- Permission decisions must be recorded or referenceable where required.
- PermissionDenied must stop the operation.
```

---

# 10. Policy Rules

AI Agent operations must pass Policy evaluation where contextual restrictions apply.

Common policies:

```text
AIAgentAccessPolicy
AIAgentKnowledgeAccessPolicy
AIAgentTaskActionPolicy
AIAgentCommunicationDraftPolicy
AIAgentWorkflowPolicy
AIAgentRoutingPolicy
AIAgentRestrictedDataPolicy
AIAgentHumanReviewPolicy
AIAgentEventVisibilityPolicy
CrossOrganizationAgentPolicy
```

Rules:

```text
- Policy may restrict data even when Permission allows access.
- Policy may require human review.
- Policy may restrict output use.
- Policy may downgrade access from raw content to safe summary.
- Policy may require redaction.
- Policy may block cross-organization or cross-matter context.
- PolicyRestricted must stop or downgrade the operation.
```

---

# 11. Knowledge Access Rules

AI Agent knowledge access must be policy-filtered.

Allowed access levels:

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
```

Rules:

```text
- AI Agent must not access all Knowledge by default.
- Knowledge access must be tied to purpose.
- Knowledge access must be tied to target context.
- Retrieved Knowledge is reference material, not professional truth by itself.
- AI must cite or reference the knowledge records used where the product surface requires traceability.
- RestrictedContentWithHumanApproval must not be used silently.
```

Knowledge output must disclose:

```text
source scope
confidence level where available
missing context
policy omissions
need for professional review
```

---

# 12. Document and Evidence Access Rules

AI Agent access to Document and Evidence is restricted.

Rules:

```text
- Raw document content access requires explicit permission and policy.
- Evidence sufficiency must not be concluded by AI alone.
- AI may extract, summarize or flag issues under governance.
- AI may prepare Evidence draft context for human review.
- AI must not alter source documents.
- AI must not fabricate evidence.
- AI must not treat OCR/extraction as verified truth without review.
```

Disallowed by default:

```text
unrestricted raw document access
privileged document access
customer identity document access
financial document access
filing credential access
private attorney-client strategy notes
```

---

# 13. Task Action Rules

AI Agents may assist Task operations only through governed Task Service boundaries.

Allowed:

```text
summarize task
flag missing task inputs
suggest next step
prepare task draft
prepare assignment suggestion
prepare completion draft
prepare review checklist
```

Restricted:

```text
create active task without permission
assign task without policy
start task automatically
complete task automatically
approve task output
mark professional conclusion complete
```

Rules:

```text
- AI-generated Task action must be marked.
- Human review is required where task affects professional output, external communication, filing, payment or customer instruction.
- Task completion by AI requires explicit service operation and human-review policy unless the task is defined as system-only and non-professional.
```

---

# 14. Communication Rules

AI Agents may draft communications but must not send external communications directly through Agent API.

Allowed:

```text
prepare draft
summarize thread
extract action items
suggest reply
prepare translation draft
prepare recipient/context check
```

Restricted:

```text
send email
send portal message
send WhatsApp/WeChat/SMS
approve external wording
issue legal notice
accept customer instruction
bind company to terms
```

Rules:

```text
- AI-drafted communication must be marked.
- Human review is required for external communication unless policy explicitly defines a safe system notification or internal message.
- Communication Service owns Communication creation.
- Channel delivery must be governed separately.
```

---

# 15. Workflow Rules

AI Agents may support Workflow Contract operations but must not become workflow runtime authority.

Allowed:

```text
suggest workflow contract
preview workflow application
prepare task plan
flag missing workflow inputs
summarize workflow trace
```

Restricted:

```text
apply workflow without permission
create active tasks silently
complete workflow
bypass workflow policy
approve professional workflow result
```

Rules:

```text
- AI workflow suggestions are drafts until accepted.
- Workflow Contract Service owns workflow application.
- Task Service owns task creation.
- Event Service records workflow trace.
```

---

# 16. Routing Rules

AI Agents may support Routing evaluation but must not autonomously select service providers where human review is required.

Allowed:

```text
prepare routing evaluation
compare safe provider summaries
flag missing candidate context
recommend candidate for review
explain routing evaluation
prepare provider communication draft
```

Restricted:

```text
select provider without governed permission
assign order
approve contract
approve payment
treat provider as legal representative
expose restricted pricing or bank data
```

Rules:

```text
- AI routing recommendation must disclose basis and omitted fields.
- RoutingSelected must only be emitted by Routing Service.
- AI recommendation is not RoutingSelected.
- Human review is required where provider selection has business, financial or legal consequence.
```

---

# 17. Data Handling Rules

AI Agent data access must follow least privilege.

Default data mode:

```text
SafeSummaryOnly
```

Allowed data modes:

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithApproval
```

Disallowed default data:

```text
raw credentials
API keys
bank details
payment credentials
private contacts
customer identity documents
privileged attorney strategy
unredacted evidence
unrestricted message bodies
internal scoring formulas
provider contracts
commission terms
```

Rules:

```text
- Restricted data must be omitted unless explicitly allowed.
- Output must not leak restricted input.
- Logs must not store restricted data unless audit policy allows.
- Prompt/context construction must be policy-filtered.
```

---

# 18. Human Review Rules

Human review is required when AI output may affect:

```text
legal conclusion
official filing
external communication
customer instruction
provider selection
payment or commission
task completion
evidence sufficiency
document finalization
workflow application with active task creation
cross-organization disclosure
```

Human review record should include:

```yaml
human_review_reference_id: string
reviewer_user_reference_id: string
review_scope: string
review_decision: Approved | Rejected | Revised | Escalated
reviewed_at: datetime
```

Rules:

```text
- Human review must be explicit.
- Human review must not be implied by user login alone.
- Human review must be traceable where output is used downstream.
```

---

# 19. Event and Audit Rules

AI Agent operations must be traceable.

Required event or audit references may include:

```text
AgentCreated
PermissionEvaluated
PolicyEvaluated
TaskCreated
CommunicationCreated
RoutingEvaluated
RoutingSelected
WorkflowContractApplied
```

Trace fields:

```yaml
agent_reference_id: string
agent_contract_reference_id: string | null
actor_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
operation: string
input_scope: string
output_scope: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- AI Agent actions must be auditable.
- AI Agent output used downstream must preserve origin metadata.
- Events must not be fabricated by AI.
- Event Service owns Event recording.
```

---

# 20. Output Rules

AI Agent output must be classified.

Output categories:

```text
SafeSummary
Draft
Suggestion
ValidationResult
ExtractionResult
ClassificationResult
Recommendation
PreparationResult
TraceExplanation
```

Output must indicate:

```text
whether it is AI-generated
source scope
confidence or uncertainty where applicable
missing information
policy omissions
review requirement
downstream service required
```

Output must not:

```text
pretend to be final professional truth
hide AI origin where governance requires disclosure
include restricted fields without policy approval
claim action completion when only preparation occurred
```

---

# 21. Error and Rejection Rules

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
KnowledgeAccessRestricted
TargetContextInvalid
CrossOrganizationRestricted
OperationNotAllowedForAgent
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not expose restricted policy internals.
- Rejections must not leak hidden data.
- Rejections may suggest required next governed step.
```

---

# 22. Codex Implementation Notes

Codex must:

```text
cite this AI Agent Governance spec before implementing any AI Agent behavior
implement agent identity checks
implement agent status checks
implement agent capability checks
invoke Permission Service for protected operations
invoke Policy Service for contextual restrictions
enforce SafeSummaryOnly default data mode
mark AI-generated outputs
carry agent_reference_id through downstream requests
carry agent_contract_reference_id where required
preserve permission_decision_reference_id and policy_decision_reference_id where required
require human_review_reference_id where policy requires review
route Task behavior through Task Service
route Communication behavior through Communication Service
route Workflow behavior through Workflow Contract Service
route Routing behavior through Routing Service
route Event recording through Event Service
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted data omission
write tests that AI cannot fabricate events
write tests that AI cannot complete tasks or send communications directly
write tests that AI output is marked and traceable
```

Codex must not:

```text
implement AI shortcuts around services
grant permissions inside Agent API
allow agent self-escalation
pass raw unrestricted data to prompts
hide AI origin
treat AI output as final professional truth
allow AI to emit domain events directly
allow AI to mutate domain objects outside owning services
allow AI to send external communications without governed service flow
allow AI to select providers or approve payments without governed review
```

---

# 23. Acceptance Criteria

This Agent Governance Specification is accepted only if:

```text
[ ] It defines AI Agent governance purpose.
[ ] It defines AI Agent governance meaning.
[ ] It defines Core position and boundary.
[ ] It defines Agent identity rules.
[ ] It defines Agent role rules.
[ ] It defines capability boundary.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines Knowledge access rules.
[ ] It defines Document/Evidence access rules.
[ ] It defines Task action rules.
[ ] It defines Communication rules.
[ ] It defines Workflow rules.
[ ] It defines Routing rules.
[ ] It defines data handling rules.
[ ] It defines human review rules.
[ ] It defines event and audit rules.
[ ] It defines output rules.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial AI Agent Governance specification. Establishes common governance lock for agent identity, permission, policy, knowledge access, task action, communication drafting, workflow support, routing recommendation, event trace, human review and Codex implementation boundaries. |

---

**End of Agent Specification**
