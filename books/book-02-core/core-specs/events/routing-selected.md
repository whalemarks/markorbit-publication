# Event Specification — RoutingSelected

**Spec ID:** B02-EVT-ROUTING-SELECTED  
**Spec Type:** Event  
**Event Name:** RoutingSelected  
**Event File:** core-specs/events/routing-selected.md  
**Event Category:** DomainEvent  
**Owning Domain:** Routing  
**Producing Service:** core-specs/services/routing-service.md  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/jurisdiction.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/partner-service.md; core-specs/services/service-network-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/routing-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/routing-selected-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration and Network Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

RoutingSelected records that Routing Service selected a governed Agent or Service Provider candidate for a specific routing context.

It exists so that Matter, Order, Agent, Service Provider, Jurisdiction, Partner, Service Network, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a routing selection decision has been recorded without treating that selection as contract formation, procurement approval, payment authorization, task assignment, professional execution, official representative authority or final service quality verification.

RoutingSelected is required before:

```text
routing selection trace
matter/order provider selection context
jurisdiction-specific collaborator selection
agent/service-provider engagement preparation
communication and instruction preparation
AI-assisted routing selection review
policy-controlled routing selection visibility
API routing selection reference validation
audit trace for routing-sensitive decisions
```

---

# 2. Event Meaning

RoutingSelected means:

```text
Routing Service has recorded a governed selection of one or more candidates for a specific routing context.
```

RoutingSelected does not mean:

```text
a contract has been formed
procurement has been approved
payment has been authorized
the selected candidate accepted the work
the selected candidate is legally appointed as representative
a Task has been assigned
a Matter step has been executed
the selected candidate's capability or quality has been verified
AI recommendation alone made the selection
```

RoutingSelected records selection decision only.

It does not establish contract, payment, appointment, acceptance, execution authority or professional completion.

---

# 3. Event Category

RoutingSelected is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Routing domain.

It is not an Agent event, Service Provider event, Partner event, procurement event, payment event, Task event or appointment event.

---

# 4. Event Producer

Producing service:

```text
Routing Service
```

Producing operation:

```text
selectRoutingCandidate
```

Source domain:

```text
Routing
```

Source object type:

```text
RoutingSelection
```

Allowed producer path:

```text
API / Professional user / Matter / Order / System / AI-assisted governed operation
        ↓
Routing Service selectRoutingCandidate
        ↓
Event Service record RoutingSelected
```

Producer rules:

```text
- RoutingSelected must be emitted only after Routing Service successfully records a governed selection.
- RoutingSelected must not be emitted directly by product UI.
- RoutingSelected must not be emitted directly by AI Agent outside governed service operation.
- RoutingSelected must not be emitted for failed, unauthorized, rejected or incomplete selection attempts.
```

---

# 5. Event Trigger

RoutingSelected is triggered when:

```text
Routing Service completes candidate selection and commits the routing_selection_reference_id.
```

Required trigger conditions:

```text
selectRoutingCandidate operation completed
routing_selection_reference_id created
routing_context_type validated
selected candidate reference captured
selection_status captured
target service context captured
permission/policy context captured where required
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Agent creation
Service Provider creation
Routing evaluation only
AI recommendation only
Partner creation
Service Network mapping
contract creation
payment setup
provider acceptance
task assignment
failed validation
unauthorized selection attempt
```

Related but separate events may include:

```text
RoutingEvaluated
AgentCreated
ServiceProviderCreated
PartnerCreated
ServiceNetworkLinked
TaskCreated
TaskAssigned
CommunicationCreated
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: RoutingSelected
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Routing
source_service: Routing Service
source_operation: selectRoutingCandidate
source_object_type: RoutingSelection
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/routing-selected-payload.md
safe_summary:
  routing_selection_reference_id: string
  routing_evaluation_reference_id: string | null
  routing_context_type: string
  selection_status: string
  selected_candidate_type: string
  source_type: string
restricted_fields_policy: RoutingSelectedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
routing_selection_reference_id: string
routing_evaluation_reference_id: string | null
routing_context_type: string
selection_status: string
selection_source_type: string
matter_reference_id: string | null
order_reference_id: string | null
jurisdiction_reference_ids: list[string]
selected_candidate_type: string
selected_agent_reference_id: string | null
selected_service_provider_reference_id: string | null
selected_partner_reference_id: string | null
selected_service_network_reference_id: string | null
selection_reason_code: string
selected_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use selected candidate references and safe summaries rather than embedding confidential pricing, scoring, cooperation terms or legal strategy by default.
- Payload may reference RoutingEvaluated but must not require it where selection is manual and governed.
- Payload must not include bank/payment data, procurement terms, privileged strategy, private contact details or restricted scoring internals.
- Payload must not imply contract, provider acceptance, task assignment, payment authorization or official appointment.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
routing_selection_reference_id
source_object_reference_id
actor_reference_id
selected_candidate_type
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
routing_evaluation_reference_id
matter_reference_id
order_reference_id
jurisdiction_reference_ids
selected_agent_reference_id
selected_service_provider_reference_id
selected_partner_reference_id
selected_service_network_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal routing_selection_reference_id.
- actor_reference_id identifies who/what requested or performed selection.
- selected candidate references must point to governed Agent, Service Provider, Partner or Service Network records.
- routing_evaluation_reference_id must not imply the evaluation itself selected the candidate unless selection operation is recorded.
- selected candidate reference must not imply contract, acceptance, payment or legal appointment.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
RoutingSelected
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

## 8.4 routing_context_type

```text
MatterRouting
OrderRouting
TrademarkRouting
JurisdictionRouting
ServiceProviderRouting
AgentRouting
InternalRouting
Other
Unknown
```

## 8.5 selected_candidate_type

```text
Agent
ServiceProvider
Partner
ServiceNetwork
InternalTeam
Unknown
```

## 8.6 selection_status

```text
Draft
Selected
ReviewRequired
Blocked
Rejected
Superseded
Cancelled
Archived
DeletedReferenceOnly
Unknown
```

## 8.7 selection_source_type

```text
ProfessionalInput
RoutingEvaluation
MatterContext
OrderContext
JurisdictionContext
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.8 selection_reason_code

```text
BestFit
CostPreference
JurisdictionCoverage
CapabilityMatch
ExistingRelationship
Urgency
ManualOverride
CustomerPreference
NoAlternative
AIAssistedRecommendation
Unknown
```

## 8.9 reason_code

```text
RoutingSelected
CandidateSelected
ManualSelection
EvaluationBasedSelection
AIAssistedSelected
ReviewRequired
Blocked
Unknown
```

---

# 9. Event Rules

## 9.1 RoutingSelected Records Selection Decision

RoutingSelected records that a candidate selection decision occurred.

It must not be interpreted as contract, acceptance, procurement approval, payment authorization or work execution.

## 9.2 RoutingSelected Is Different From RoutingEvaluated

RoutingEvaluated records candidate evaluation.

RoutingSelected records governed selection.

A recommendation is not selection unless RoutingSelected is emitted.

## 9.3 Selection Is Not Engagement

Selected candidate may still require communication, confirmation, contract, POA, instruction or acceptance.

RoutingSelected alone does not engage the selected candidate.

## 9.4 Selection Is Not Verification

Agent or Service Provider verification is owned by their respective services and governance rules.

RoutingSelected does not verify capability, quality or authority.

## 9.5 Selection Is Not Task Assignment

Task Service owns actionable work units and assignments.

RoutingSelected does not assign work to a User or external collaborator by itself.

## 9.6 AI Recommendation Is Not Selection Automatically

AI may recommend candidates.

Selection requires governed Routing Service operation and applicable review rules.

## 9.7 RoutingSelected Must Respect Permission and Policy

Routing selection and visibility must respect Permission, Policy, confidentiality, pricing access and cooperation access context.

## 9.8 RoutingSelected Must Be Immutable

RoutingSelected must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Matter Service
Order Service
Agent Service
Service Provider Service
Partner Service
Service Network Service
Communication Service
Task Service
Policy Service
Permission Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Matter and Order services may display selected routing candidate but must not infer engagement or execution.
- Communication Service may prepare contact/instruction communication under governed operation.
- Task Service may create follow-up tasks only through governed Task Service operation.
- Agent and Service Provider services may show selection context but must not infer verification.
- Permission Service must evaluate who may view or act on selected routing result.
- Policy Service must enforce restricted pricing, scoring and cooperation visibility.
- AI Agents may summarize selected candidate only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Routing selection trace.
```

Consumers must not:

```text
treat RoutingSelected as contract or acceptance
treat RoutingSelected as provider assignment or legal appointment
treat RoutingSelected as payment/procurement approval
treat RoutingSelected as Agent or Service Provider verification
treat RoutingSelected as Task assignment
treat AI recommendation as final routing selection
expose restricted pricing, scores or cooperation data
```

---

# 11. Relationship to Services

Producing service:

```text
Routing Service produces RoutingSelected after selectRoutingCandidate succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches RoutingSelected.
```

Related services:

```text
Matter and Order services provide routing context.
Agent Service provides selected agent references.
Service Provider Service provides selected provider references.
Partner and Service Network services may provide cooperation/network context.
Communication Service may prepare contact or instruction messages.
Task Service may create follow-up work units.
Policy Service controls visibility, pricing and AI use.
Permission Service controls who may select, view or act on selected candidate.
Audit Service records accountability trace.
AI Agent Governance controls AI routing recommendation and selection support behavior.
```

Boundary reminders:

```text
Routing Service owns candidate evaluation and selection.
Agent Service owns collaborator profile.
Service Provider Service owns provider entity/capability profile.
Partner Service owns cooperation relationship.
Service Network Service owns network mapping.
Task Service owns actionable work units.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /routing-selections/{routing_selection_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create RoutingSelected directly.
- API must call Routing Service selectRoutingCandidate, which emits the event.
- API must not expose restricted pricing, scoring internals, private contact details, cooperation history, contract terms or strategy by default.
- API must distinguish RoutingSelected from RoutingEvaluated, AgentCreated, ServiceProviderCreated, PartnerCreated, TaskAssigned and contract/procurement events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that Routing selection was recorded
explain that selection is not contract, acceptance, payment or appointment
compare selected candidate with evaluated alternatives where authorized
flag missing confirmation, contract or instruction step for review
flag selection requiring human approval where policy requires it
prepare audit-safe Routing selection summary
```

AI must not:

```text
fabricate RoutingSelected
rewrite RoutingSelected
delete RoutingSelected
treat RoutingSelected as provider engagement, contract or legal appointment
treat RoutingSelected as procurement or payment approval
treat RoutingSelected as verification or quality approval
hide AI-assisted selection
expose restricted pricing, scores, contacts or cooperation data
```

AI-assisted selection requires:

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

RoutingSelected is valid only if:

```text
[ ] event_name is RoutingSelected.
[ ] event_category is DomainEvent.
[ ] producing service is Routing Service.
[ ] producing operation is selectRoutingCandidate.
[ ] source_domain is Routing.
[ ] source_object_type is RoutingSelection.
[ ] source_object_reference_id is present.
[ ] routing_selection_reference_id is present.
[ ] source_object_reference_id equals routing_selection_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] routing_context_type is controlled.
[ ] selected_candidate_type is controlled.
[ ] selection_status is controlled.
[ ] selection_source_type is controlled.
[ ] at least one selected candidate reference is present unless selection_status is Blocked or Rejected.
[ ] selected candidate references are valid where provided.
[ ] payload does not include restricted pricing, scoring internals, private contact data, payment data, contract terms or cooperation strategy unless allowed.
[ ] contract, payment, procurement approval, verification, acceptance, appointment and assignment are not implied.
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
RoutingSelectionReferenceMissing
RoutingSelectionReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
RoutingContextTypeInvalid
SelectedCandidateTypeInvalid
SelectionStatusInvalid
SelectionSourceTypeInvalid
SelectedCandidateReferenceMissing
SelectedCandidateReferenceInvalid
RestrictedFieldViolation
ConfidentialRoutingPayloadRejected
PricingPayloadRestricted
ScoringPayloadRestricted
ContractPayloadRestricted
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownRoutingSelectionEventError
```

Rejection rules:

```text
- Failed Routing selection must not emit RoutingSelected.
- Unauthorized selection attempt must not emit RoutingSelected.
- Rejected/Blocked attempts may emit RoutingSelected only if selection_status explicitly records Blocked or Rejected under governed operation.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Routing Service Specification
cite Routing Object Specification
cite Event Service Specification
cite Agent and Service Provider specs where selected candidate references are used
use exact event_name: RoutingSelected
use exact event_category: DomainEvent
validate routing_selection_reference_id
validate source_object_reference_id equals routing_selection_reference_id
validate actor_reference_id
validate selected_candidate_type and selected candidate references
validate controlled routing_context_type/selection_status/source_type
validate payload contract
write tests that failed selectRoutingCandidate does not emit RoutingSelected
write tests that RoutingEvaluated does not imply RoutingSelected
write tests that RoutingSelected does not imply contract, provider acceptance or legal appointment
write tests that RoutingSelected does not imply procurement or payment approval
write tests that RoutingSelected does not verify Agent or Service Provider
write tests that RoutingSelected does not assign Task
write tests that AI-assisted selection is marked where applicable
write tests that restricted pricing/scoring/contact/contract/cooperation data is not exposed
```

Codex must not:

```text
emit RoutingSelected directly from UI
treat RoutingEvaluated as RoutingSelected
treat AgentCreated or ServiceProviderCreated as RoutingSelected
treat RoutingSelected as contract, payment or appointment event
create Task, Partner, Service Network mapping, provider engagement or payment silently from RoutingSelected
store private contact, pricing, scoring, contract or cooperation data in event payload by default
allow AI to fabricate RoutingSelected
use RoutingSelected as command to contract, pay, verify, assign, communicate or appoint provider
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines RoutingSelected purpose.
[ ] It defines RoutingSelected meaning.
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
| 0.1.0 | Draft | Initial RoutingSelected Event specification. Defines governed Routing selection event and separates RoutingSelected from evaluation, provider engagement, contract, procurement, payment approval, verification, assignment, appointment and AI recommendation. |

---

**End of Event Specification**
