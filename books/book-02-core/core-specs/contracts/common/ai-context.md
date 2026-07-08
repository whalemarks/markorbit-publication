# Common Contract — AI Context

**Spec ID:** B02-CONTRACT-COMMON-AI-CONTEXT  
**Spec Type:** Common Contract Specification  
**Contract Name:** AI Context Contract  
**Contract File:** core-specs/contracts/common/ai-context.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/knowledge.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/workflow-contract.md; core-specs/objects/routing.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/knowledge-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/routing-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/agent-api.md; core-specs/api/knowledge-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/routing-api.md; core-specs/api/event-api.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/task-created.md; core-specs/events/communication-created.md; core-specs/events/routing-evaluated.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/knowledge-agent.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

AI Context Contract defines the canonical AI and Agent context shape used across MarkOrbit Core.

It standardizes how API requests, service inputs, agent outputs, workflow previews, communication drafts, task drafts, routing recommendations and audit summaries identify AI involvement, Agent identity, registry key, data access scope, output mode, human review requirement and governance trace.

This contract governs:

```text
AI-assisted operation markers
Agent identity context
Agent registry key context
Agent contract reference
data access scope
output mode
confidence and uncertainty
source references
permission and policy decision references
human review requirements
restricted data omission
downstream service requirement
AI output trace
Codex implementation rules
```

AI Context Contract does not define prompts, model selection, product UX, AI provider integration, professional truth, permission grants or policy approvals.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for carrying AI/Agent participation context safely and explicitly.
```

This contract does not mean:

```text
prompt template
model configuration
AI feature list
AI permission grant
policy bypass
professional conclusion
human replacement
agent runtime engine
unrestricted tool access
```

Core rule:

```text
AI context marks assistance.
Agent Service validates agent identity.
Permission and Policy govern access.
Human review governs downstream use where required.
AI output is not professional truth by default.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
AI context field names
agent identity fields
agent registry key fields
data access scope fields
AI output mode fields
AI source/reference trace fields
human review requirement fields
restricted data omission fields
downstream service requirement fields
AI context validation
safe AI output metadata
```

This contract is not responsible for:

```text
running AI models
choosing prompts
granting permissions
evaluating policies
creating Agent objects
executing downstream services
creating events directly
approving legal conclusions
sending communications
selecting providers
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related governance specs:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
```

Owning rule:

```text
AI Context must preserve AI Agent Governance and must never imply professional truth, permission approval, policy approval or downstream execution by itself.
```

---

# 5. Related Core Objects

Primary related objects:

```text
Agent
Permission
Policy
Knowledge
Task
Communication
WorkflowContract
Routing
Event
```

Rules:

```text
- Agent object owns agent identity.
- Permission object/decision governs action access.
- Policy object/decision governs contextual restriction.
- Event object preserves trace.
- Domain objects remain owned by their domains.
```

---

# 6. Required References

AI context references:

```yaml
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
  agent_contract_reference_id: string | null
  capability_used: string | null
  data_access_scope: string | null
  output_mode: string | null
  confidence_level: string | null
  human_review_required: boolean | null
  human_review_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  source_reference_ids: list[string]
  downstream_service_required: string | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- ai_assisted is required where AI/Agent participated.
- agent_reference_id is required for governed agent operations.
- agent_registry_key is required for registered Agent behavior.
- agent_contract_reference_id is required where Agent Contract applies.
- data_access_scope is required where AI reads context.
- output_mode is required where AI produces output.
- human_review_required must be explicit where AI output may be used downstream.
```

---

# 7. Contract Shape

Canonical AI context shape:

```yaml
ai_context:
  ai_assisted: boolean
  agent:
    agent_reference_id: string | null
    agent_registry_key: string | null
    agent_contract_reference_id: string | null
    agent_role: string | null
  capability:
    capability_used: string | null
    capability_category: string | null
    restricted_capability_used: boolean
  access:
    data_access_scope: string | null
    requested_data_access_scope: string | null
    restricted_fields_omitted: boolean
  output:
    output_mode: string | null
    ai_generated: boolean
    confidence_level: string | null
    uncertainty_notes: list[string]
    missing_context: list[string]
    policy_omissions: list[string]
  governance:
    permission_decision_reference_id: string | null
    policy_decision_reference_id: string | null
    human_review_required: boolean | null
    human_review_reference_id: string | null
  trace:
    source_reference_ids: list[string]
    source_scope: string | null
    downstream_service_required: string | null
    correlation_id: string | null
```

Minimal AI context shape:

```yaml
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
  data_access_scope: string | null
  output_mode: string | null
  human_review_required: boolean | null
  restricted_fields_omitted: boolean
```

Rules:

```text
- Minimal shape may be used only where owning contract allows it.
- Full shape is required for protected AI operations.
- AI-generated output must be marked.
- Data access and human review fields must not be hidden in free text.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| ai_assisted | boolean | Yes where AI participates | No | Must be true when AI/Agent assisted the operation. |
| agent_reference_id | string | Contextual | Yes | Required for governed Agent operations. |
| agent_registry_key | string | Contextual | Yes | Required where behavior maps to Agent Registry. |
| agent_contract_reference_id | string | Contextual | Yes | Required where Agent Contract applies. |
| agent_role | string | Contextual | Yes | Must match Agent Registry where provided. |
| capability_used | string | Contextual | Yes | Must use controlled capability. |
| restricted_capability_used | boolean | Contextual | No | Must be true when restricted capability was used/requested. |
| data_access_scope | string | Contextual | Yes | Must use controlled data access scope. |
| requested_data_access_scope | string | No | Yes | Must not exceed allowed policy scope. |
| output_mode | string | Contextual | Yes | Must use controlled output mode. |
| ai_generated | boolean | Contextual | No | Must be true for AI-generated content. |
| confidence_level | string | No | Yes | Must not imply professional truth. |
| human_review_required | boolean | Contextual | Yes | Required for downstream-use outputs. |
| human_review_reference_id | string | Contextual | Yes | Required where review is completed/needed for use. |
| source_reference_ids | list[string] | Contextual | No | Must preserve source trace where AI uses sources. |
| downstream_service_required | string | Contextual | Yes | Required where AI prepares but does not execute. |
| restricted_fields_omitted | boolean | Yes where safe response returned | No | Must be true where policy omitted fields. |

---

# 9. Controlled Values

## 9.1 agent_role

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
SystemSupportAssistant
Unknown
```

## 9.2 capability_used

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
Unknown
```

## 9.3 restricted_capability

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
Unknown
```

## 9.4 data_access_scope

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

## 9.5 output_mode

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
Unknown
```

## 9.6 confidence_level

```text
Low
Medium
High
Unknown
```

## 9.7 source_scope

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContext
KnowledgeContext
TaskContext
CommunicationContext
WorkflowContext
RoutingContext
EventTrace
CrossObjectContext
Unknown
```

## 9.8 downstream_service_required

```text
AgentService
KnowledgeService
TaskService
CommunicationService
WorkflowContractService
RoutingService
EventService
PermissionService
PolicyService
NotificationService
DocumentService
EvidenceService
None
Unknown
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] ai_assisted is present when AI participates.
[ ] ai_assisted is true for AI-generated output.
[ ] agent_reference_id is present for governed Agent operation.
[ ] agent_registry_key is present where behavior maps to registry.
[ ] agent_registry_key is valid.
[ ] agent_contract_reference_id is present where required.
[ ] agent_role is controlled where provided.
[ ] capability_used is controlled where provided.
[ ] restricted_capability_used is true where restricted capability is requested or used.
[ ] data_access_scope is controlled where provided.
[ ] requested_data_access_scope does not exceed allowed scope.
[ ] output_mode is controlled where provided.
[ ] ai_generated is true for AI output.
[ ] human_review_required is explicit where output may be used downstream.
[ ] human_review_reference_id is present where required.
[ ] permission_decision_reference_id is present where required.
[ ] policy_decision_reference_id is present where required.
[ ] source_reference_ids are preserved where AI uses sources.
[ ] restricted_fields_omitted is true where fields are omitted.
[ ] downstream_service_required is present where AI prepares but does not execute.
```

---

# 11. Permission Rules

AI Context does not grant permission.

Rules:

```text
- Agent Service validates agent identity.
- Permission Service evaluates allowed action.
- AI Context may include permission_decision_reference_id.
- Missing permission must stop protected AI behavior.
- Agent capability does not equal permission.
```

Required permission patterns:

```text
agent:<operation>
target-domain:<operation>
data-scope:<access>
```

---

# 12. Policy Rules

AI Context does not evaluate policy.

Rules:

```text
- Policy Service evaluates data access and output use.
- Policy may downgrade data_access_scope.
- Policy may require human_review_required = true.
- Policy may require restricted_fields_omitted = true.
- Policy may block downstream use.
- PolicyRestricted must stop or downgrade AI behavior.
```

Common policies:

```text
AIAgentAccessPolicy
AIAgentRestrictedDataPolicy
AIAgentHumanReviewPolicy
AIAgentKnowledgeAccessPolicy
AIAgentCommunicationDraftPolicy
AIAgentTaskActionPolicy
AIAgentWorkflowPolicy
AIAgentRoutingPolicy
```

---

# 13. AI Agent Rules

AI Agent operations must follow:

```text
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
```

Rules:

```text
- AI must not fabricate agent_reference_id.
- AI must not fabricate source_reference_ids.
- AI must not hide AI origin where governance requires marking.
- AI must not represent Draft, Suggestion or Recommendation as final professional truth.
- AI must not execute downstream service actions through context alone.
- AI must preserve missing_context and policy_omissions.
```

---

# 14. Event Rules

AI Context may be included in event payloads where allowed.

Rules:

```text
- AI Context is not Event.
- Event Service owns Event recording.
- Event payload contracts must define whether AI Context is included.
- AI Context in event payload must not expose prompts, hidden instructions or restricted context.
- Agent actions must be traceable through event/audit context where required.
```

---

# 15. Error Rules

Controlled AI context errors:

```text
AIContextInvalid
AgentReferenceInvalid
AgentRegistryKeyInvalid
AgentContractRequired
AgentSuspended
AgentRevoked
CapabilityNotAllowed
RestrictedCapabilityRequested
DataAccessScopeInvalid
DataAccessScopeExceeded
HumanReviewRequired
SourceReferenceInvalid
AIOutputModeInvalid
AIContextPolicyRestricted
AIContextPermissionDenied
```

Safe error shape:

```yaml
error:
  code: string
  category: Agent | Validation | Permission | Policy | HumanReview
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose prompts, hidden instructions, tools, model internals or restricted data.
- Errors must not echo restricted user input.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding data_access_scope values requires revision notes.
- Adding output_mode values requires revision notes.
- Renaming AI context fields is breaking.
- Changing meaning of human_review_required is breaking.
- Changing minimal AI context shape is breaking unless backward compatible.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this AI Context Contract before implementing AI-assisted operations
cite AI Agent Governance
cite Agent Registry
validate agent_reference_id through Agent Service
validate agent_registry_key
validate capability eligibility
invoke Permission Service before protected AI operation
invoke Policy Service before AI data access
use SafeSummaryOnly by default
mark AI-generated output
preserve source_reference_ids
preserve missing_context and policy_omissions
set restricted_fields_omitted correctly
require human_review_reference_id where required
return Error Contract shape for AI context errors
write tests for missing ai_assisted
write tests for invalid agent_registry_key
write tests for AgentContractRequired
write tests for CapabilityNotAllowed
write tests for DataAccessScopeExceeded
write tests for HumanReviewRequired
write tests that AI output is marked
write tests that restricted data is omitted
```

Codex must not:

```text
hide AI involvement
fabricate agent references
fabricate source references
pass unrestricted context into AI prompts
treat AI draft as final output
execute downstream services from AI context alone
expose prompts, hidden instructions or tool internals
skip permission or policy checks for AI convenience
```

---

# 18. Acceptance Criteria

This AI Context Contract is accepted only if:

```text
[ ] It defines AI context purpose.
[ ] It defines AI context meaning.
[ ] It defines AI context boundary.
[ ] It cites related owning spec and governance specs.
[ ] It defines related Core objects.
[ ] It defines required AI references.
[ ] It defines canonical AI context shape.
[ ] It defines minimal AI context shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common AI Context Contract. Defines canonical/minimal AI context shapes, agent identity, registry key, capability, data access, output mode, governance trace, validation, permission/policy, event, error and Codex rules. |

---

**End of Common Contract**
