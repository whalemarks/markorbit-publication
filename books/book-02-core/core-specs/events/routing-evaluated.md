# Event Specification — RoutingEvaluated

**Spec ID:** B02-EVT-ROUTING-EVALUATED  
**Spec Type:** Event  
**Event Name:** RoutingEvaluated  
**Event File:** core-specs/events/routing-evaluated.md  
**Event Category:** DomainEvent  
**Owning Domain:** Routing  
**Producing Service:** core-specs/services/routing-service.md  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/jurisdiction.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/routing-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/routing-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/routing-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/routing-evaluated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration and Network Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

RoutingEvaluated records that Routing Service evaluated candidate collaborators or service providers for a target service context.

It exists so that Matter, Order, Agent, Service Provider, Jurisdiction, Partner, Service Network, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that candidate evaluation occurred without treating that evaluation as final selection, engagement, assignment, contract, procurement approval, payment approval, service quality approval or professional execution decision.

RoutingEvaluated is required before:

```text
routing candidate evaluation trace
matter/order provider matching context
jurisdiction-based provider evaluation
agent/service-provider comparison
routing recommendation review
AI-assisted routing evaluation review
policy-controlled routing visibility
API routing reference validation
audit trace for routing-sensitive actions
```

---

# 2. Event Meaning

RoutingEvaluated means:

```text
Routing Service has evaluated candidate options for a specific routing context and produced a governed routing evaluation result.
```

RoutingEvaluated does not mean:

```text
a candidate has been selected
a provider has been engaged
an Agent has been assigned
a Service Provider has been contracted
a Partner relationship was created
pricing or procurement has been approved
payment is authorized
quality or capability has been verified
AI recommendation has become final routing decision
```

RoutingEvaluated records candidate evaluation only.

It does not establish final selection, contractual commitment, payment eligibility, execution authority or professional acceptance.

---

# 3. Event Category

RoutingEvaluated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Routing domain.

It is not an Agent event, Service Provider event, Partner event, procurement event or payment event.

---

# 4. Event Producer

Producing service:

```text
Routing Service
```

Producing operation:

```text
evaluateRouting
```

Source domain:

```text
Routing
```

Source object type:

```text
RoutingEvaluation
```

Allowed producer path:

```text
API / Matter / Order / Professional user / System / AI-assisted governed operation
        ↓
Routing Service evaluateRouting
        ↓
Event Service record RoutingEvaluated
```

Producer rules:

```text
- RoutingEvaluated must be emitted only after Routing Service successfully completes a governed routing evaluation.
- RoutingEvaluated must not be emitted directly by product UI.
- RoutingEvaluated must not be emitted directly by AI Agent outside governed service operation.
- RoutingEvaluated must not be emitted for failed, unauthorized or incomplete routing evaluation attempts.
```

---

# 5. Event Trigger

RoutingEvaluated is triggered when:

```text
Routing Service completes routing candidate evaluation and commits the routing_evaluation_reference_id.
```

Required trigger conditions:

```text
evaluateRouting operation completed
routing_evaluation_reference_id created
routing_context_type validated
candidate scope captured
evaluation_result captured
target service context captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Agent creation
Service Provider creation
Partner creation
Jurisdiction link
candidate search draft
AI routing suggestion only
routing selection
contract creation
payment setup
provider assignment
failed validation
unauthorized evaluation attempt
```

Related but separate events may include:

```text
AgentCreated
ServiceProviderCreated
PartnerCreated
JurisdictionLinked
RoutingSelected
MatterCreated
OrderCreated
PolicyEvaluated
PermissionEvaluated
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: RoutingEvaluated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Routing
source_service: Routing Service
source_operation: evaluateRouting
source_object_type: RoutingEvaluation
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/routing-evaluated-payload.md
safe_summary:
  routing_evaluation_reference_id: string
  routing_context_type: string
  evaluation_status: string
  candidate_count: integer
  recommended_candidate_count: integer
  source_type: string
restricted_fields_policy: RoutingEvaluatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
routing_evaluation_reference_id: string
routing_context_type: string
evaluation_status: string
evaluation_source_type: string
matter_reference_id: string | null
order_reference_id: string | null
jurisdiction_reference_ids: list[string]
agent_candidate_reference_ids: list[string]
service_provider_candidate_reference_ids: list[string]
recommended_agent_reference_ids: list[string]
recommended_service_provider_reference_ids: list[string]
selected_agent_reference_id: string | null
selected_service_provider_reference_id: string | null
evaluated_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
```

Payload rules:

```text
- Payload must use candidate references and safe summaries rather than embedding confidential pricing, quality scores or cooperation strategy by default.
- Payload may include recommended candidates but must not imply final selection unless a separate RoutingSelected event exists.
- Payload must not include bank/payment data, procurement terms, privileged strategy, private contact details or restricted scoring internals.
- Payload must distinguish AI-assisted recommendation from approved routing selection.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
routing_evaluation_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
matter_reference_id
order_reference_id
jurisdiction_reference_ids
agent_candidate_reference_ids
service_provider_candidate_reference_ids
recommended_agent_reference_ids
recommended_service_provider_reference_ids
selected_agent_reference_id
selected_service_provider_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal routing_evaluation_reference_id.
- actor_reference_id identifies who/what requested or performed evaluation.
- candidate references must not imply selection.
- recommended references must not imply engagement or contract.
- selected references should normally be null for RoutingEvaluated unless evaluation and selection are intentionally combined under a governed operation and a separate selection event is also emitted.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
RoutingEvaluated
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

## 8.5 evaluation_status

```text
Draft
Evaluated
ReviewRequired
NoCandidate
Blocked
Rejected
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 evaluation_source_type

```text
ProfessionalInput
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

## 8.7 reason_code

```text
RoutingEvaluated
CandidateEvaluationCompleted
NoCandidateFound
RecommendationCreated
ReviewRequired
Blocked
SystemEvaluated
MigrationEvaluated
AIAssistedEvaluated
Unknown
```

---

# 9. Event Rules

## 9.1 RoutingEvaluated Records Candidate Evaluation

RoutingEvaluated records that candidate evaluation occurred.

It must not be interpreted as routing selection, provider engagement, assignment, procurement approval or payment authorization.

## 9.2 Routing Is Not Agent

Agent Service owns collaborator profile.

Routing may evaluate Agents, but RoutingEvaluated does not create or verify Agents.

## 9.3 Routing Is Not Service Provider

Service Provider Service owns provider entity/capability profile.

Routing may evaluate Service Providers, but RoutingEvaluated does not verify capability or quality.

## 9.4 Routing Evaluation Is Not Selection

Selection must be governed separately, normally by RoutingSelected or an equivalent selection event.

Recommendation is not final selection.

## 9.5 Routing Evaluation Is Not Contract or Procurement

Contracting, procurement, pricing approval and payment are separate business/finance processes.

RoutingEvaluated must not be used as payment or supplier commitment.

## 9.6 AI Routing Recommendation Is Not Final Decision

AI may assist evaluation, scoring or ranking.

AI-assisted recommendation must not become final selection automatically.

## 9.7 RoutingEvaluated Must Respect Permission and Policy

Routing evaluation and visibility must respect Permission, Policy, confidentiality, pricing access and cooperation access context.

## 9.8 RoutingEvaluated Must Be Immutable

RoutingEvaluated must not be rewritten except controlled event metadata/status handled by Event Service.

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
Jurisdiction Service
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
- Matter and Order services may display routing evaluation context but must not infer final selection.
- Agent and Service Provider services may use evaluation context but must not infer verification.
- Partner and Service Network services may use evaluation data for mapping only under governed rules.
- Permission Service must evaluate who may view evaluation results or make selection.
- Policy Service must enforce restricted pricing, scoring and cooperation data visibility.
- AI Agents may summarize routing evaluation only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Routing evaluation trace.
```

Consumers must not:

```text
treat RoutingEvaluated as RoutingSelected
treat RoutingEvaluated as Agent or Service Provider verification
treat RoutingEvaluated as contract, procurement or payment approval
treat RoutingEvaluated as assignment or authority
treat AI recommendation as final routing decision
expose restricted pricing, scores or cooperation data
```

---

# 11. Relationship to Services

Producing service:

```text
Routing Service produces RoutingEvaluated after evaluateRouting succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches RoutingEvaluated.
```

Related services:

```text
Matter and Order services provide routing context.
Agent Service provides agent candidate references.
Service Provider Service provides provider candidate references.
Jurisdiction Service provides where-context.
Partner and Service Network services may provide network context.
Policy Service controls visibility, pricing and AI use.
Permission Service controls who may evaluate, view or select candidates.
Audit Service records accountability trace.
AI Agent Governance controls AI routing evaluation behavior.
```

Boundary reminders:

```text
Routing Service owns candidate evaluation and recommendation.
Agent Service owns collaborator profile.
Service Provider Service owns provider entity/capability profile.
Partner Service owns cooperation relationship.
Service Network Service owns network mapping.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /routing-evaluations/{routing_evaluation_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create RoutingEvaluated directly.
- API must call Routing Service evaluateRouting, which emits the event.
- API must not expose restricted pricing, scoring internals, private contact details, cooperation history or strategy by default.
- API must distinguish RoutingEvaluated from RoutingSelected, AgentCreated, ServiceProviderCreated, PartnerCreated and verification events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that Routing evaluation was completed
explain that evaluation/recommendation is not final selection
rank or compare candidates only where authorized
flag missing jurisdiction, capability, price or verification data for review
flag routing result requiring human selection
prepare audit-safe Routing evaluation summary
```

AI must not:

```text
fabricate RoutingEvaluated
rewrite RoutingEvaluated
delete RoutingEvaluated
treat RoutingEvaluated as selected provider or assigned agent
treat AI ranking as final routing decision
treat RoutingEvaluated as contract, procurement or payment approval
hide AI-assisted evaluation
expose restricted pricing, scores, contacts or cooperation data
```

AI-assisted evaluation requires:

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

RoutingEvaluated is valid only if:

```text
[ ] event_name is RoutingEvaluated.
[ ] event_category is DomainEvent.
[ ] producing service is Routing Service.
[ ] producing operation is evaluateRouting.
[ ] source_domain is Routing.
[ ] source_object_type is RoutingEvaluation.
[ ] source_object_reference_id is present.
[ ] routing_evaluation_reference_id is present.
[ ] source_object_reference_id equals routing_evaluation_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] routing_context_type is controlled.
[ ] evaluation_status is controlled.
[ ] evaluation_source_type is controlled.
[ ] candidate references are valid where provided.
[ ] payload does not include restricted pricing, scoring internals, private contact data, payment data or cooperation strategy unless allowed.
[ ] final selection, contract, payment, procurement approval, verification and assignment are not implied.
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
RoutingEvaluationReferenceMissing
RoutingEvaluationReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
RoutingContextTypeInvalid
EvaluationStatusInvalid
EvaluationSourceTypeInvalid
CandidateReferenceInvalid
RestrictedFieldViolation
ConfidentialRoutingPayloadRejected
PricingPayloadRestricted
ScoringPayloadRestricted
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownRoutingEventError
```

Rejection rules:

```text
- Failed Routing evaluation must not emit RoutingEvaluated.
- Unauthorized evaluation attempt must not emit RoutingEvaluated.
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
cite Agent and Service Provider specs where candidate references are used
use exact event_name: RoutingEvaluated
use exact event_category: DomainEvent
validate routing_evaluation_reference_id
validate source_object_reference_id equals routing_evaluation_reference_id
validate actor_reference_id
validate controlled routing_context_type/evaluation_status/source_type
validate payload contract
write tests that failed evaluateRouting does not emit RoutingEvaluated
write tests that RoutingEvaluated does not imply Routing selection
write tests that RoutingEvaluated does not verify Agent or Service Provider
write tests that RoutingEvaluated does not imply contract, procurement or payment approval
write tests that AI-assisted evaluation is marked where applicable
write tests that restricted pricing/scoring/contact/cooperation data is not exposed
```

Codex must not:

```text
emit RoutingEvaluated directly from UI
treat AgentCreated or ServiceProviderCreated as RoutingEvaluated
treat RoutingEvaluated as RoutingSelected
treat RoutingEvaluated as contract or payment approval
create Partner, Service Network mapping or provider engagement silently from RoutingEvaluated
store private contact, pricing, scoring or cooperation data in event payload by default
allow AI to fabricate RoutingEvaluated
use RoutingEvaluated as command to select, contract, route, pay, verify or assign provider
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines RoutingEvaluated purpose.
[ ] It defines RoutingEvaluated meaning.
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
| 0.1.0 | Draft | Initial RoutingEvaluated Event specification. Defines governed Routing candidate evaluation event and separates RoutingEvaluated from final selection, provider engagement, contract, procurement, payment approval, verification, authority and AI routing decision. |

---

**End of Event Specification**
