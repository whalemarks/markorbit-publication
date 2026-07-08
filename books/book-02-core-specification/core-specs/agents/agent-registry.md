# Agent Specification — Agent Registry

**Spec ID:** B02-AGENT-REGISTRY  
**Spec Type:** Agent Registry Specification  
**Agent Spec Name:** Agent Registry  
**Agent Spec File:** core-specs/agents/agent-registry.md  
**Related Core Domains:** Agent; Permission; Policy; Knowledge; Task; Communication; Workflow Contract; Routing; Event  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/user.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/knowledge.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/workflow-contract.md; core-specs/objects/routing.md; core-specs/objects/event.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/knowledge-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/routing-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/knowledge-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/routing-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Cross-Phase Governance  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Agent Registry defines the canonical registry structure for all AI Agents, automation agents and system agents recognized by MarkOrbit Core.

It provides a governed index of agent identities, purposes, roles, capabilities, access scopes, review requirements and downstream service boundaries.

Agent Registry exists to ensure:

```text
every agent has explicit identity
every agent has bounded purpose
every agent has declared capability scope
every agent has governance profile
every agent has permission and policy boundary
every agent has safe data access rules
every agent has human-review rules
every agent can be audited
every Codex implementation can map agent behavior to a registered agent specification
```

Agent Registry is not a product feature list, prompt catalog or model provider list.

---

# 2. Registry Meaning

Agent Registry means:

```text
a Core-governed inventory of allowed agent categories and agent instances.
```

Agent Registry does not mean:

```text
unrestricted AI plugin marketplace
model selection table only
prompt library only
runtime credential store
permission grant table
policy bypass table
service execution engine
professional decision authority
```

Registry rule:

```text
No governed AI/automation behavior may exist outside Agent Registry.
```

---

# 3. Core Position

Agent Registry sits under AI Agent Governance and above individual specialized agent specs.

Canonical position:

```text
AI Agent Governance
↓
Agent Registry
↓
Specialized Agent Specs
↓
Agent API / Agent Service
↓
Domain Services
↓
Events
```

It is referenced by:

```text
core-specs/agents/ai-agent-governance.md
core-specs/api/agent-api.md
core-specs/services/agent-service.md
core-specs/objects/agent.md
Codex agent implementation tasks
```

---

# 4. Registry Boundary

Agent Registry is responsible for:

```text
agent category listing
agent purpose definition
agent capability declaration
agent data access scope declaration
agent downstream service boundary declaration
agent human-review requirement declaration
agent event/audit requirement declaration
agent status model
agent registry acceptance rules
```

Agent Registry is not responsible for:

```text
creating Agent objects directly
granting permissions
evaluating policies
running AI models
storing credentials
executing tasks
sending communications
selecting service providers
approving legal conclusions
```

---

# 5. Registry Governance Lock

All registered agents must obey:

```text
Agent Registry declares what an agent may be considered for.
Permission and Policy decide what an agent may do in context.
Owning services execute downstream actions.
Human review remains required where governance demands it.
Events preserve trace.
```

Registration is not authorization.

Capability is not permission.

Recommendation is not decision.

Preparation is not execution.

---

# 6. Registry Entry Contract

Each registry entry must include:

```yaml
agent_registry_key: string
agent_spec_reference: string | null
agent_type: string
agent_role: string
agent_purpose: string
allowed_capabilities: list[string]
restricted_capabilities: list[string]
default_data_access_scope: string
allowed_data_access_scopes: list[string]
default_execution_mode: string
human_review_required_for: list[string]
required_services:
  - service_spec_reference: string
required_api_specs:
  - api_spec_reference: string
required_event_specs:
  - event_spec_reference: string
required_policies:
  - policy_name: string
required_permissions:
  - permission_key: string
status: string
mvp_phase: string
mvp_depth: string
notes: string | null
```

Rules:

```text
- Registry keys must be stable.
- Registry keys must not expose model provider details.
- Registry entries must cite AI Agent Governance.
- Registry entries must declare default data access scope.
- Registry entries must declare human-review triggers.
- Registry entries must not grant permission by themselves.
```

---

# 7. Controlled Agent Types

Controlled `agent_type` values:

```text
AIAgent
AutomationAgent
IntegrationAgent
WorkflowAgent
KnowledgeAgent
CommunicationAgent
RoutingAgent
TaskAgent
AuditAgent
SystemAgent
Unknown
```

Rules:

```text
- Unknown agents may not perform protected operations.
- SystemAgent requires system-governed producer authority.
- IntegrationAgent requires integration contract governance.
- AIAgent requires AI Agent Governance.
```

---

# 8. Controlled Agent Roles

Controlled `agent_role` values:

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

Disallowed roles:

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

---

# 9. Capability Registry

Allowed capabilities:

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

Restricted capabilities:

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
- Allowed capability means eligible for permission/policy evaluation.
- Restricted capability requires explicit permission, policy and usually human review.
- Capability must map to owning service operation.
- Capability must not bypass service boundaries.
```

---

# 10. Data Access Registry

Controlled data access scopes:

```text
NoAccess
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
```

Default rule:

```text
SafeSummaryOnly is the default maximum data access scope unless the registry entry explicitly narrows it.
```

Disallowed default access:

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
- Registry may narrow access, not silently broaden it.
- Policy may further narrow access at runtime.
- Permission may deny access entirely.
- Prompt/context construction must use the evaluated access scope.
```

---

# 11. Execution Mode Registry

Controlled execution modes:

```text
ReadOnly
DraftOnly
SuggestOnly
PrepareOnly
HumanReviewRequired
SystemApproved
NotAllowed
Unknown
```

Rules:

```text
- DraftOnly means output cannot be treated as final.
- SuggestOnly means recommendation cannot become decision without governed acceptance.
- PrepareOnly means downstream service must execute actual action.
- HumanReviewRequired means a human review reference is required before downstream use.
- SystemApproved is allowed only for narrowly defined non-professional system operations.
```

---

# 12. Base Registry Entries

## 12.1 Knowledge Retrieval Agent

```yaml
agent_registry_key: knowledge-retrieval-agent
agent_spec_reference: core-specs/agents/knowledge-agent.md
agent_type: KnowledgeAgent
agent_role: KnowledgeRetrievalAssistant
agent_purpose: KnowledgeRetrieval
allowed_capabilities:
  - Read
  - Summarize
  - RequestKnowledge
  - ValidateReference
restricted_capabilities:
  - AccessRestrictedContent
  - AccessRawDocument
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: ReadOnly
human_review_required_for:
  - RestrictedContentWithHumanApproval
  - professional conclusion
required_services:
  - core-specs/services/knowledge-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/knowledge-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/permission-evaluated.md
  - core-specs/events/policy-evaluated.md
status: Draft
mvp_phase: Phase 1
mvp_depth: Must Implement
```

## 12.2 Task Agent

```yaml
agent_registry_key: task-agent
agent_spec_reference: core-specs/agents/task-agent.md
agent_type: TaskAgent
agent_role: TaskPlanningAssistant
agent_purpose: TaskPlanning
allowed_capabilities:
  - Read
  - Summarize
  - Suggest
  - PrepareTask
  - ValidateReference
restricted_capabilities:
  - CreateObject
  - UpdateObject
  - CompleteTask
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: PrepareOnly
human_review_required_for:
  - task completion
  - professional work output
  - external communication
required_services:
  - core-specs/services/task-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/task-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/task-created.md
  - core-specs/events/permission-evaluated.md
  - core-specs/events/policy-evaluated.md
status: Draft
mvp_phase: Phase 3
mvp_depth: Must Implement
```

## 12.3 Communication Agent

```yaml
agent_registry_key: communication-agent
agent_spec_reference: core-specs/agents/communication-agent.md
agent_type: CommunicationAgent
agent_role: CommunicationDraftingAssistant
agent_purpose: CommunicationDrafting
allowed_capabilities:
  - Read
  - Summarize
  - Draft
  - PrepareCommunication
  - ValidateReference
restricted_capabilities:
  - SendCommunication
  - AccessPrivateContact
  - AccessRestrictedContent
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: DraftOnly
human_review_required_for:
  - external communication
  - legal notice
  - customer instruction
  - service provider communication
required_services:
  - core-specs/services/communication-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/communication-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/communication-created.md
  - core-specs/events/permission-evaluated.md
  - core-specs/events/policy-evaluated.md
status: Draft
mvp_phase: Phase 4
mvp_depth: Must Implement
```

## 12.4 Workflow Agent

```yaml
agent_registry_key: workflow-agent
agent_spec_reference: core-specs/agents/workflow-agent.md
agent_type: WorkflowAgent
agent_role: WorkflowSupportAssistant
agent_purpose: WorkflowSupport
allowed_capabilities:
  - Read
  - Summarize
  - Suggest
  - PrepareWorkflow
  - PrepareTask
restricted_capabilities:
  - ApplyWorkflow
  - CreateObject
  - CompleteTask
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: PrepareOnly
human_review_required_for:
  - workflow application
  - active task creation
  - professional workflow output
required_services:
  - core-specs/services/workflow-contract-service.md
  - core-specs/services/task-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/workflow-contract-api.md
  - core-specs/api/task-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/workflow-contract-applied.md
  - core-specs/events/task-created.md
status: Draft
mvp_phase: Phase 3
mvp_depth: Must Implement
```

## 12.5 Routing Agent

```yaml
agent_registry_key: routing-agent
agent_spec_reference: core-specs/agents/routing-agent.md
agent_type: RoutingAgent
agent_role: RoutingSupportAssistant
agent_purpose: RoutingSupport
allowed_capabilities:
  - Read
  - Summarize
  - Suggest
  - PrepareRouting
  - ExplainTrace
restricted_capabilities:
  - SelectRouting
  - AccessPricing
  - AccessPrivateContact
  - AccessFinancialData
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: SuggestOnly
human_review_required_for:
  - provider selection
  - order assignment
  - payment or contract impact
required_services:
  - core-specs/services/routing-service.md
  - core-specs/services/service-provider-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/routing-api.md
  - core-specs/api/service-provider-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/routing-evaluated.md
  - core-specs/events/routing-selected.md
status: Draft
mvp_phase: Phase 4
mvp_depth: Must Implement
```

## 12.6 Audit Agent

```yaml
agent_registry_key: audit-agent
agent_spec_reference: core-specs/agents/audit-agent.md
agent_type: AuditAgent
agent_role: AuditSupportAssistant
agent_purpose: AuditSupport
allowed_capabilities:
  - Read
  - Summarize
  - ExplainTrace
  - ValidateReference
restricted_capabilities:
  - AccessRestrictedContent
  - AccessRawDocument
default_data_access_scope: SafeSummaryOnly
allowed_data_access_scopes:
  - MetadataOnly
  - SafeSummaryOnly
  - PolicyFilteredContent
default_execution_mode: ReadOnly
human_review_required_for:
  - compliance conclusion
  - professional conclusion
  - restricted event payload use
required_services:
  - core-specs/services/event-service.md
  - core-specs/services/permission-service.md
  - core-specs/services/policy-service.md
required_api_specs:
  - core-specs/api/event-api.md
  - core-specs/api/agent-api.md
required_event_specs:
  - core-specs/events/permission-evaluated.md
  - core-specs/events/policy-evaluated.md
status: Draft
mvp_phase: Phase 3
mvp_depth: Should Implement
```

---

# 13. Registry Status Model

Controlled registry status values:

```text
Draft
Active
ReviewRequired
Deprecated
Suspended
Revoked
Archived
Unknown
```

Rules:

```text
- Draft registry entries may be implemented only in controlled development scope.
- Active registry entries may be used in production if all required services, permissions and policies exist.
- ReviewRequired entries require architecture review before use.
- Deprecated entries must not be used for new implementations.
- Suspended or Revoked entries must not execute.
```

---

# 14. Registry Validation Rules

Registry entry validation checklist:

```text
[ ] agent_registry_key is stable.
[ ] agent_type is controlled.
[ ] agent_role is controlled.
[ ] agent_purpose is declared.
[ ] allowed_capabilities are controlled.
[ ] restricted_capabilities are controlled.
[ ] default_data_access_scope is controlled.
[ ] allowed_data_access_scopes are controlled.
[ ] default_execution_mode is controlled.
[ ] human_review_required_for is declared.
[ ] required services are declared.
[ ] required API specs are declared.
[ ] required event specs are declared where applicable.
[ ] required permissions are declared.
[ ] required policies are declared.
[ ] status is controlled.
[ ] MVP phase and depth are declared.
[ ] AI Agent Governance is cited.
```

---

# 15. Permission and Policy Integration

Agent Registry does not grant permissions or policy access.

Rules:

```text
- Registry only declares eligibility.
- Agent Service validates registry status.
- Permission Service evaluates action permission.
- Policy Service evaluates context restrictions.
- Domain services execute downstream behavior.
```

Required flow:

```text
Registry entry exists
↓
Agent status valid
↓
Capability eligible
↓
Permission evaluated
↓
Policy evaluated
↓
Human review checked where required
↓
Owning service executes or prepares
↓
Event trace recorded
```

---

# 16. Human Review Integration

Registry entries must define human-review triggers.

Default human-review triggers:

```text
external communication
professional conclusion
official filing
provider selection
payment or commission impact
task completion
document finalization
evidence sufficiency
workflow application with active task creation
restricted data use
cross-organization disclosure
```

Rules:

```text
- Human review triggers may not be omitted for restricted capabilities.
- Human review requirement may only be relaxed by explicit Policy.
- Human review must be traceable where required.
```

---

# 17. Event and Audit Integration

Agent Registry must support event trace.

Required trace fields:

```yaml
agent_registry_key: string
agent_reference_id: string | null
agent_contract_reference_id: string | null
operation: string
target_object_type: string | null
target_object_reference_id: string | null
capability_used: string
data_access_scope: string
execution_mode: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Agent actions must be traceable to registry entry.
- Agent output used downstream must preserve registry metadata.
- Events must be emitted by owning services, not by registry itself.
```

---

# 18. Codex Implementation Notes

Codex must:

```text
cite Agent Registry before implementing any specialized agent
cite AI Agent Governance before implementing any specialized agent
create typed registry entries rather than hard-coded scattered agent rules
validate agent_registry_key
validate agent status
validate capability eligibility before Permission and Policy checks
enforce SafeSummaryOnly default access unless registry narrows or policy allows more
enforce human-review triggers declared in registry
route downstream operations through owning services
preserve registry metadata in agent outputs
write tests for unknown registry key
write tests for suspended/revoked registry entry
write tests for capability not allowed
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for HumanReviewRequired
write tests for restricted data omission
```

Codex must not:

```text
hard-code agent behavior outside registry
treat registry entry as permission grant
allow unregistered agents to run governed operations
allow agent capability to bypass Policy
store credentials in registry entries
expose prompts or runtime secrets in registry responses
allow AI to self-register or self-escalate
allow registry to execute downstream services directly
```

---

# 19. Acceptance Criteria

This Agent Registry Specification is accepted only if:

```text
[ ] It defines Agent Registry purpose.
[ ] It defines Registry meaning.
[ ] It defines Core position.
[ ] It defines Registry boundary.
[ ] It defines Registry governance lock.
[ ] It defines registry entry contract.
[ ] It defines controlled agent types.
[ ] It defines controlled agent roles.
[ ] It defines capability registry.
[ ] It defines data access registry.
[ ] It defines execution mode registry.
[ ] It defines base registry entries.
[ ] It defines registry status model.
[ ] It defines registry validation rules.
[ ] It defines Permission and Policy integration.
[ ] It defines human review integration.
[ ] It defines event and audit integration.
[ ] It defines Codex implementation notes.
```

---

# 20. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent Registry specification. Defines canonical registry contract, controlled types/roles/capabilities/data scopes/execution modes, base agent entries, validation rules, human review integration, audit integration and Codex implementation boundaries. |

---

**End of Agent Specification**
