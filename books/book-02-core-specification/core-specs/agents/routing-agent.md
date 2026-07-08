# Agent Specification — Routing Agent

**Spec ID:** B02-AGENT-ROUTING  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Routing Agent  
**Agent Spec File:** core-specs/agents/routing-agent.md  
**Registry Key:** routing-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Routing; Service Provider; Service Network; Partner; Agent; Permission; Policy; Event; Order; Matter; Task; Communication; Jurisdiction; Capability  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/partner.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/order.md; core-specs/objects/matter.md; core-specs/objects/task.md; core-specs/objects/communication.md; core-specs/objects/jurisdiction.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/partner-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/order-service.md; core-specs/services/matter-service.md; core-specs/services/task-service.md; core-specs/services/communication-service.md; core-specs/services/jurisdiction-service.md  
**Related API Specs:** core-specs/api/routing-api.md; core-specs/api/service-provider-api.md; core-specs/api/service-network-api.md; core-specs/api/partner-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/order-api.md; core-specs/api/matter-api.md; core-specs/api/task-api.md; core-specs/api/communication-api.md; core-specs/api/jurisdiction-api.md  
**Related Event Specs:** core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md; core-specs/events/service-provider-created.md; core-specs/events/service-network-linked.md; core-specs/events/communication-created.md; core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration / Network Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Routing Agent defines the governed AI Agent pattern for assisting Routing evaluation, service-provider comparison, candidate explanation, routing-scope preparation and provider communication draft preparation in MarkOrbit Core.

It exists to help professionals evaluate service route candidates without allowing AI to become provider selector, order assignee, payment approver, contract approver, legal representative verifier, service-provider truth source or silent network operator.

Routing Agent supports:

```text
routing evaluation preparation
service-provider candidate comparison
safe candidate explanation
routing gap detection
routing-scope preparation
service-network candidate pool preparation
provider communication draft preparation
routing trace explanation
human-review routing recommendation
order-assignment preparation context
```

Routing Agent does not select providers autonomously, assign orders, approve payments, approve contracts, prove legal authority or mutate Routing/Order/Service Provider state outside governed services.

---

# 2. Agent Meaning

Routing Agent means:

```text
a governed AI Agent that assists with Routing evaluation and routing-candidate preparation through Routing Service boundaries.
```

Routing Agent does not mean:

```text
provider selector
order assignment authority
payment approver
contract approver
legal representative verifier
vendor truth engine
service-provider lifecycle owner
service-network operator
pricing exposure engine
policy bypasser
```

Routing Agent may help answer:

```text
Which candidates should be reviewed?
What safe comparison can be prepared?
What jurisdiction/service capability gaps exist?
Why was this candidate recommended for review?
What provider communication draft should be prepared?
What downstream review is required before selection?
```

Routing Agent must not claim:

```text
The provider has been selected unless Routing Service records RoutingSelected.
The order has been assigned.
Payment has been approved.
Contract terms are accepted.
The provider is legally authorized unless separately verified by governed proof.
```

---

# 3. Registry Position

Registry entry:

```text
routing-agent
```

Required registry constraints:

```text
agent_type: RoutingAgent
agent_role: RoutingSupportAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: SuggestOnly
```

Allowed capabilities:

```text
Read
Summarize
Suggest
PrepareRouting
ValidateReference
ExplainTrace
```

Restricted capabilities:

```text
SelectRouting
AccessPricing
AccessPrivateContact
AccessFinancialData
AccessRestrictedContent
CreateObject
UpdateObject
```

Registry rule:

```text
Routing Agent may be considered for routing evaluation assistance and candidate recommendation.
Permission and Policy decide whether it may access specific Routing, Service Provider, Service Network or Partner context.
```

---

# 4. Agent Boundary

Routing Agent is responsible for:

```text
routing query preparation
routing reference validation request
safe routing evaluation preparation
safe service-provider comparison
candidate gap detection
candidate recommendation draft
routing explanation draft
routing-scope preparation
provider communication draft context
order-assignment preparation context
routing event trace explanation
```

Routing Agent is not responsible for:

```text
Routing lifecycle ownership
Routing selection without Routing Service
Service Provider lifecycle ownership
Service Network lifecycle ownership
Partner lifecycle ownership
Order assignment
Task execution
Communication delivery
payment approval
contract approval
legal authority verification by itself
permission grant
policy evaluation
```

---

# 5. Governance Lock

Routing Agent must obey:

```text
Routing Agent may read, summarize, compare, suggest and prepare only within Permission and Policy limits.
Routing Agent output is routing assistance, not RoutingSelected.
Routing Agent must not silently select providers, assign Orders, approve payments, approve contracts or verify legal authority.
Routing Agent must disclose candidate basis, source scope, missing context, restricted omissions and human-review requirements.
Routing Agent must route Routing evaluation and selection through Routing Service.
```

This lock applies to all Routing Agent implementations.

---

# 6. Agent Identity Requirements

Every Routing Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: routing-agent
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
- Agent Contract is required for protected routing access.
- Suspended, revoked, archived or unknown agents must not perform Routing operations.
- Agent must not borrow human User identity.
```

---

# 7. Capability Rules

Allowed operations:

```text
prepareRoutingEvaluation
summarizeRoutingEvaluation
validateRoutingReference
compareRoutingCandidates
identifyRoutingGaps
prepareRoutingRecommendationDraft
explainRoutingEvaluation
prepareRoutingScope
prepareOrderAssignmentContext
prepareProviderCommunicationDraft
explainRoutingTrace
```

Disallowed operations:

```text
selectRoutingSilently
assignOrder
approveProviderContract
approveProviderPayment
verifyLegalAuthorityAsFinal
createServiceProviderWithoutService
updateServiceProviderWithoutService
sendProviderCommunication
completeTask
```

Capability rule:

```text
Routing Agent may prepare routing assistance; Routing Service owns Routing evaluation and selection.
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
AccessPricing
AccessPrivateContact
AccessFinancialData
AccessRawDocument
AccessEvidence
```

Rules:

```text
- SafeSummaryOnly is the default.
- Policy may downgrade access to MetadataOnly or NoAccess.
- Provider pricing, private contacts, contracts, bank data, performance notes and internal scoring are restricted by default.
- Service Network member lists may be restricted by policy.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
provider bank details
provider private contacts
provider contract terms
provider pricing details
commission terms
internal candidate scoring formulas
privileged vendor strategy
customer private instructions
filing credentials
payment data
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:routing:prepare
routing:evaluate
routing:read
routing:search
routing:validate
routing:candidates:read
routing:explain
routing:select
routing:order-assignment:prepare
routing:communication:prepare
service-provider:read
service-provider:capability:read
service-network:member:read
partner:read
order:read
matter:read
communication:draft:prepare
event:read
```

Rules:

```text
- Agent-level permission is required.
- Routing-domain permission is required.
- Related Service Provider, Service Network, Partner, Order and Matter permission is required where those records are referenced.
- Routing selection requires explicit permission and policy.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentRoutingPolicy
RoutingEvaluationPolicy
RoutingVisibilityPolicy
RoutingCandidateVisibilityPolicy
RoutingExplanationPolicy
RoutingSelectionPolicy
RoutingOrderAssignmentPolicy
RoutingCommunicationPolicy
ServiceProviderVisibilityPolicy
ServiceNetworkMemberVisibilityPolicy
RestrictedRoutingDataPolicy
CrossOrganizationRoutingPolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether Routing Agent may evaluate, explain, recommend or prepare selection context.
- Policy may require human review before routing selection or order-assignment preparation.
- Policy may restrict provider pricing, private contacts, scoring formulas, contract terms and performance notes.
- Policy may restrict cross-organization or cross-matter routing access.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Routing Evaluation Preparation Request

```yaml
operation: prepareRoutingEvaluation
agent_reference_id: string
agent_registry_key: routing-agent
actor_reference_id: string | null
organization_reference_id: string | null
routing_purpose: string
target_context:
  order_reference_id: string | null
  matter_reference_id: string | null
  jurisdiction_reference_id: string | null
  service_type: string | null
candidate_scope:
  service_provider_reference_ids: list[string]
  service_network_reference_id: string | null
  include_preferred_only: boolean | null
data_access_requested: string
correlation_id: string | null
```

## 11.2 Candidate Comparison Request

```yaml
operation: compareRoutingCandidates
agent_reference_id: string
routing_reference_id: string | null
candidate_service_provider_reference_ids: list[string]
comparison_purpose: string
comparison_depth: string
target_context:
  order_reference_id: string | null
  matter_reference_id: string | null
  jurisdiction_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.3 Routing Recommendation Draft Request

```yaml
operation: prepareRoutingRecommendationDraft
agent_reference_id: string
routing_reference_id: string
recommendation_purpose: string
candidate_context:
  recommended_service_provider_reference_id: string | null
  alternative_service_provider_reference_ids: list[string]
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.4 Provider Communication Draft Request

```yaml
operation: prepareProviderCommunicationDraft
agent_reference_id: string
routing_reference_id: string | null
service_provider_reference_id: string
draft_purpose: string
communication_type: string
target_context:
  order_reference_id: string | null
  matter_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Routing Evaluation Preparation Response

```yaml
agent_reference_id: string
routing_preparation_reference_id: string | null
preparation_status: string
safe_routing_preview:
  candidate_count: integer
  usable_candidate_count: integer
  missing_items: list[string]
  warnings: list[string]
  suggested_evaluation_mode: string | null
source_scope: string
policy_omissions: list[string]
human_review_required: boolean
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.2 Candidate Comparison Response

```yaml
agent_reference_id: string
comparison_reference_id: string | null
safe_candidate_comparison:
  candidates:
    - service_provider_reference_id: string
      safe_score_band: string | null
      safe_reason: string | null
      missing_context: list[string]
      review_required: boolean
  recommended_for_review_reference_id: string | null
source_scope: string
policy_omissions: list[string]
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Routing Recommendation Draft Response

```yaml
agent_reference_id: string
recommendation_draft_reference_id: string | null
routing_reference_id: string
safe_recommendation:
  recommended_service_provider_reference_id: string | null
  safe_reason: string | null
  alternatives: list[string]
  risks_or_gaps: list[string]
  review_notes: list[string]
recommendation_status: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.4 Provider Communication Draft Response

```yaml
agent_reference_id: string
draft_reference_id: string | null
service_provider_reference_id: string
safe_draft:
  communication_type: string
  draft_purpose: string
  subject: string | null
  body_draft: string | null
  review_notes: list[string]
preparation_status: string
human_review_required: boolean
downstream_service_required: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must not imply RoutingSelected or Order assignment.
- Responses must disclose candidate basis, missing context and policy omissions.
- Responses must not expose restricted pricing, private contacts or contract terms by default.
- Responses must identify required human review and downstream service.
```

---

# 13. Controlled Values

## 13.1 routing_purpose

```text
OrderProviderSelection
MatterProviderSelection
JurisdictionProviderSelection
ServiceNetworkSelection
TaskAssigneeSupport
ProviderComparison
AIAssistedRouting
Unknown
```

## 13.2 comparison_purpose

```text
CandidateReview
ProviderComparison
JurisdictionCapabilityReview
ServiceCapabilityReview
RiskReview
FeeReviewSafe
AIAssistedComparison
Unknown
```

## 13.3 comparison_depth

```text
Brief
Standard
DetailedSafe
RestrictedInternal
Unknown
```

## 13.4 recommendation_purpose

```text
HumanReviewPreparation
OrderPreparation
MatterPreparation
ProviderSelectionSupport
RiskReview
AIAssistedRecommendation
Unknown
```

## 13.5 draft_purpose

```text
ProviderInquiry
FeeRequest
AvailabilityCheck
DocumentRequest
FilingInstructionDraft
StatusFollowUp
AIAssistedDraft
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

## 13.7 recommendation_status

```text
Drafted
Rejected
PolicyRestricted
PermissionDenied
HumanReviewRequired
InsufficientContext
Unknown
```

## 13.8 source_scope

```text
RoutingOnly
ServiceProviderContext
ServiceNetworkContext
OrderContext
MatterContext
JurisdictionContext
PolicyFilteredContext
Unknown
```

## 13.9 safe_score_band

```text
Low
Medium
High
NotDisclosed
Unknown
```

## 13.10 confidence_level

```text
Low
Medium
High
Unknown
```

## 13.11 data_access_requested

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

---

# 14. Human Review Rules

Human review is required when Routing Agent output may be used for:

```text
routing selection
provider selection
order assignment
provider engagement
provider communication
fee or payment discussion
contract or commercial term discussion
legal representative reliance
customer-facing recommendation
cross-organization disclosure
restricted provider data use
```

Human review is not required for:

```text
safe internal routing summary
safe metadata lookup
non-state-changing candidate gap checklist
reference validation where no restricted content is exposed
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit before RoutingSelected where required.
- Human review reference must be passed to Routing Service where required.
```

---

# 15. Event and Audit Rules

Routing Agent operations must be traceable.

Trace must include:

```yaml
agent_registry_key: routing-agent
agent_reference_id: string
operation: string
routing_reference_id: string | null
routing_selection_reference_id: string | null
service_provider_reference_ids: list[string]
service_network_reference_id: string | null
order_reference_id: string | null
matter_reference_id: string | null
jurisdiction_reference_id: string | null
data_access_scope: string
execution_mode: string
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Routing Agent must not emit domain events directly.
- Event Service owns event recording.
- RoutingEvaluated must only be emitted after Routing Service evaluates routing.
- RoutingSelected must only be emitted after Routing Service selects routing.
- Routing trace must distinguish AI recommendation from actual selection.
```

---

# 16. Relationship to Routing Service

Routing Agent must use Routing Service for:

```text
evaluateRouting
getRoutingEvaluation
searchRoutingEvaluations
validateRoutingReference
listRoutingCandidates
explainRoutingEvaluation
selectRoutingCandidate
prepareOrderAssignmentFromRouting
prepareProviderCommunicationFromRouting
```

Rules:

```text
- Routing Agent must not query or mutate routing store directly.
- Routing Service applies Routing domain rules.
- Permission and Policy are evaluated before protected Routing operations.
- Routing Agent may transform safe results into recommendations, summaries or drafts.
```

---

# 17. Relationship to Service Provider and Service Network Services

Routing Agent may use provider/network context only through governed service access.

Rules:

```text
- Service Provider Service owns provider reference, status and capability context.
- Service Network Service owns network membership and routing-scope context.
- Partner Service owns partner relationship context where relevant.
- Routing Agent must not expose restricted provider/network fields by default.
- Routing Agent must not create or update providers/networks directly.
```

---

# 18. Relationship to Order, Matter and Communication Services

Routing Agent may prepare downstream context.

Allowed:

```text
prepare order assignment context
prepare matter provider coordination context
prepare provider communication draft
prepare routing follow-up task context
```

Rules:

```text
- Order assignment must route through Order Service.
- Matter updates must route through Matter Service.
- Communication creation and delivery must route through Communication Service.
- Routing Agent output must not be treated as assigned Order or sent provider communication.
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
RoutingReferenceInvalid
ServiceProviderReferenceInvalid
ServiceNetworkReferenceInvalid
PartnerReferenceInvalid
OrderReferenceInvalid
MatterReferenceInvalid
JurisdictionReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden provider or routing data.
- Rejections must not expose private contacts, pricing, contracts or policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Routing Agent spec
cite Routing Service Specification
cite Routing Object Specification
cite Routing API Specification
cite Service Provider and Service Network specs where context is used
cite Permission and Policy specs
validate agent_registry_key = routing-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected routing access
invoke Policy Service before routing/provider context access
use SafeSummaryOnly by default
mark AI-generated recommendations and comparisons
preserve routing/provider/network/order/matter references in output
disclose candidate basis, missing context and policy omissions
route Routing evaluation/selection through Routing Service
route Order assignment through Order Service
route provider Communication preparation through Communication Service
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted data omission
write tests for invalid Routing reference
write tests that Routing Agent cannot emit RoutingSelected directly
write tests that Routing Agent recommendation is not RoutingSelected
write tests that Routing Agent cannot assign Order or approve payment
write tests that restricted pricing/contact/contract data is omitted by default
```

Codex must not:

```text
query Routing database directly
bypass Routing Service
bypass Service Provider Service
bypass Permission or Policy
pass unrestricted provider or pricing context into prompts
treat AI recommendation as selected route
treat AI comparison as provider truth
approve contract, payment or legal authority
assign Orders directly
send provider communications directly
emit domain events directly
```

---

# 21. Acceptance Criteria

This Routing Agent Specification is accepted only if:

```text
[ ] It defines Routing Agent purpose.
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
[ ] It defines relationship to Routing Service.
[ ] It defines relationship to Service Provider and Service Network Services.
[ ] It defines relationship to Order, Matter and Communication Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing Agent specification. Defines governed routing evaluation assistance, candidate comparison, routing recommendation drafting, provider communication preparation and trace rules under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
