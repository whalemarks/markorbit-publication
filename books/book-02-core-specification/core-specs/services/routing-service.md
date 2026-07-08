# Service Specification — Routing Service

**Spec ID:** B02-SVC-ROUTING-SERVICE  
**Spec Type:** Service  
**Service Name:** Routing Service  
**Owning Domain:** Routing  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/routing.md  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/jurisdiction.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/partner-service.md; core-specs/services/service-network-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md  
**Related Event Specs:** core-specs/events/routing-request-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-recommendation-created.md; core-specs/events/routing-selection-approved.md; core-specs/events/routing-selection-rejected.md; core-specs/events/routing-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/routing/routing-contract.md; core-specs/contracts/routing/routing-request-contract.md; core-specs/contracts/routing/routing-candidate-contract.md; core-specs/contracts/routing/routing-evaluation-contract.md; core-specs/contracts/routing/routing-selection-contract.md; core-specs/contracts/routing/routing-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Network and Growth Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Routing Service defines the Core service boundary for creating, validating, evaluating, recommending, approving and managing Routing objects and routing decisions.

It exists so that Agent, Service Provider, Partner, Service Network, Jurisdiction, Order, Matter, Task, Communication, AI Agents, APIs and product consumers can consistently evaluate and record candidate selection without confusing Routing with Agent profile, Service Provider profile, Partner relationship, Service Network map, procurement execution, task assignment or AI suggestion.

Routing Service is required before:

```text
agent candidate evaluation
service provider candidate evaluation
jurisdiction-based routing
service scope-based routing
matter routing recommendation
order-to-agent/provider routing context
human-approved routing selection
AI-assisted routing recommendation
routing decision audit trace
routing candidate validation
```

---

# 2. Core Meaning

Routing Service means:

```text
the Core service that evaluates candidate options and produces governed routing recommendations or selection records based on context, rules, eligibility, policy and review requirements.
```

Routing Service does not mean:

```text
Agent Service
Service Provider Service
Partner Service
Service Network Service
procurement system
payment system
task assignment service
automatic final selection by AI
relationship management system
```

Routing Service answers:

```text
What needs to be routed?
Which jurisdiction, service scope, matter or order context applies?
Which Agents, Service Providers or Partners are eligible candidates?
Which candidates are blocked, limited or review-required?
What recommendation is produced?
Has a human or authorized service approved the selection?
Can another domain safely reference this Routing result?
What audit trace is required?
```

---

# 3. Service Category

Routing Service is a Collaboration Network Core Service.

It manages candidate evaluation and selection records.

It does not own Agent, Service Provider, Partner or Service Network data.

It does not execute procurement, payment, task work or external communication.

---

# 4. Architectural Position

Routing Service sits after candidate data and before execution.

```text
Agent / Service Provider / Partner / Service Network provide candidate context
        ↓
Jurisdiction and service scope define routing requirements
        ↓
Routing Service evaluates eligibility and recommendation
        ↓
Human or authorized process approves selection where required
        ↓
Matter / Task / Communication use approved routing reference
```

Agent and Service Provider provide candidate data.

Service Network maps ecosystem context.

Routing evaluates and records recommendation/selection.

Matter executes work.

---

# 5. Scope

Routing Service includes:

```text
routing request creation
routing request update
routing status management
candidate collection reference
candidate eligibility evaluation
candidate comparison
routing recommendation creation
routing selection approval/rejection
routing reference validation
routing audit trace
routing event emission
```

MVP/Phase 4 scope includes:

```text
create routing request
get routing request
update routing metadata
change routing status
link routing to order/matter/jurisdiction/service scope
add routing candidates
evaluate routing candidates
create routing recommendation
approve routing selection
reject routing selection
validate routing reference
emit routing events
```

Deferred scope includes:

```text
fully automated routing engine
provider marketplace ranking
real-time price optimization
automatic procurement execution
payment settlement
advanced machine-learning ranking
multi-factor performance scoring automation
service network graph optimization
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createRoutingRequest | Create Routing object/request | Yes | RoutingRequestCreated |
| getRoutingRequest | Retrieve Routing object by ID | Yes | No |
| updateRoutingRequest | Update governed routing metadata | Yes | RoutingRequestUpdated |
| changeRoutingStatus | Change routing lifecycle status | Yes | RoutingStatusChanged |
| linkRoutingOrder | Link Routing to Order | Partial | RoutingOrderLinked |
| linkRoutingMatter | Link Routing to Matter | Yes | RoutingMatterLinked |
| linkRoutingJurisdiction | Link Routing to Jurisdiction | Yes | RoutingJurisdictionLinked |
| addRoutingCandidate | Add Agent/Provider/Partner candidate | Yes | RoutingCandidateAdded |
| removeRoutingCandidate | Remove candidate | Partial | RoutingCandidateRemoved |
| evaluateRoutingCandidates | Evaluate candidate eligibility | Yes | RoutingEvaluated |
| createRoutingRecommendation | Create recommendation result | Yes | RoutingRecommendationCreated |
| approveRoutingSelection | Approve selected candidate | Yes | RoutingSelectionApproved |
| rejectRoutingSelection | Reject recommendation/selection | Yes | RoutingSelectionRejected |
| validateRoutingReference | Validate whether Routing can be referenced | Yes | RoutingReferenceValidated |
| archiveRouting | Archive Routing reference | Partial | RoutingArchived |

---

# 7. Inputs

Routing Service accepts:

```text
routing_type
routing_title_reference
status
order_reference_id
matter_reference_id
customer_reference_id
jurisdiction_reference_id
service_scope_reference
candidate_references
candidate_type
agent_reference_ids
service_provider_reference_ids
partner_reference_ids
service_network_reference_id
evaluation_criteria_reference
recommendation_reference
selected_candidate_reference
selection_reason_reference
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
routing_type
routing_title_reference
status
jurisdiction_reference_id
service_scope_reference
source_reference
actor_context
```

Required for candidate evaluation:

```text
routing_reference_id
candidate_references
jurisdiction_reference_id
service_scope_reference
evaluation_criteria_reference
actor_context
```

Required for selection approval:

```text
routing_reference_id
selected_candidate_reference
selection_reason_reference
approval_context
actor_context
```

Required for validation:

```text
routing_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Routing Service returns:

```text
Routing object
Routing reference
Routing validation result
Routing candidate result
Routing evaluation result
Routing recommendation result
Routing selection result
Routing status result
Routing event reference
error result
```

Evaluation output must include:

```text
evaluated
routing_reference_id
candidate_results
eligible_candidates
blocked_candidates
review_required_candidates
reason_code
policy_hint where applicable
```

Recommendation output must include:

```text
recommended
routing_reference_id
recommended_candidate_reference
recommendation_reason_reference
review_required
selection_required
reason_code
```

Selection output must include:

```text
selected
routing_reference_id
selected_candidate_reference
approval_status
reason_code
```

Outputs must not expose confidential pricing, contract, performance, customer, matter or partner relationship data unnecessarily.

---

# 9. Controlled Values

## 9.1 routing_type

```text
MatterRouting
OrderRouting
AgentRouting
ServiceProviderRouting
PartnerRouting
JurisdictionRouting
ServiceScopeRouting
ManualRouting
AIRoutingDraft
Unknown
```

## 9.2 status

```text
Draft
Requested
Evaluating
RecommendationCreated
ReviewRequired
SelectionApproved
SelectionRejected
Cancelled
Expired
Archived
DeletedReferenceOnly
```

## 9.3 candidate_type

```text
Agent
ServiceProvider
Partner
ServiceNetworkNode
InternalTeam
Unknown
```

## 9.4 eligibility_status

```text
Eligible
NotEligible
Limited
ReviewRequired
JurisdictionMismatch
CapabilityMismatch
PolicyRestricted
Suspended
Unavailable
Unknown
```

## 9.5 recommendation_status

```text
NotRecommended
Recommended
ReviewRequired
Rejected
Approved
Unknown
```

## 9.6 validation_result

```text
Valid
Invalid
NotFound
Draft
Cancelled
Expired
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Routing Makes Recommendation or Selection Record

Routing Service evaluates candidate context and records recommendations or approved selections.

It must not be reduced to Agent or Service Provider lookup.

## 10.2 Routing Is Not Agent

Agent Service owns external trademark collaborator profile.

Routing may evaluate Agent as candidate.

## 10.3 Routing Is Not Service Provider

Service Provider Service owns provider entity/capability profile.

Routing may evaluate Service Provider as candidate.

## 10.4 Routing Is Not Partner or Service Network

Partner owns cooperation-side business relationship.

Service Network maps ecosystem relationships.

Routing consumes context and makes evaluation/selection records.

## 10.5 AI Recommendation Is Not Final Selection

AI may draft candidate recommendations.

Final selection requires authorized service or human approval where policy requires.

## 10.6 Routing Does Not Execute Procurement, Payment or Communication

Routing selection may be used by Matter, Task or Communication.

Routing Service does not create procurement obligations, payments or outbound communications by itself.

## 10.7 Routing Must Respect Permission and Policy

Routing evaluation, recommendation and selection must respect Permission, Policy, confidentiality, conflicts, availability and candidate status.

## 10.8 Routing Changes Must Be Auditable

Routing-sensitive operations must preserve actor, source, request context, candidate list, criteria, recommendation and selection trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Agent Service | Routing evaluates Agent candidates | Agent owns collaborator profile. |
| Service Provider Service | Routing evaluates Provider candidates | Provider owns capability profile. |
| Partner Service | Routing may evaluate Partner context | Partner owns cooperation relationship. |
| Service Network Service | Routing may consume network context | Network maps ecosystem. |
| Jurisdiction Service | Routing uses jurisdiction context | Jurisdiction owns where context. |
| Matter Service | Matter may use approved routing | Matter owns execution container. |
| Order Service | Order may request routing | Order owns commercial request. |
| Task Service | Task may follow routing result | Task owns work unit. |
| Communication Service | Communication may use selected candidate | Communication owns message lifecycle. |
| Policy Service | Controls eligibility/selection | Policy owns contextual constraints. |
| AI Agent Governance | AI may suggest candidates | Agent Contract governs AI use. |
| Audit Service | Records Routing-sensitive action | Audit owns accountability trail. |
| Event Service | Records Routing events | Event records occurrence. |

---

# 12. Event Usage

Routing Service emits:

```text
RoutingRequestCreated
RoutingRequestUpdated
RoutingStatusChanged
RoutingOrderLinked
RoutingMatterLinked
RoutingJurisdictionLinked
RoutingCandidateAdded
RoutingCandidateRemoved
RoutingEvaluated
RoutingRecommendationCreated
RoutingSelectionApproved
RoutingSelectionRejected
RoutingCancelled
RoutingExpired
RoutingArchived
RoutingReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Candidate events must reference candidate type and candidate ID.
- Evaluation events must preserve criteria reference and result summary.
- Recommendation events must identify AI/system/human source where applicable.
- Selection approval/rejection events must preserve approver/source where allowed.
- Events must not expose confidential pricing, contracts or matter strategy unnecessarily.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /routing
GET /routing/{id}
PATCH /routing/{id}
POST /routing/{id}/status
POST /routing/{id}/orders
POST /routing/{id}/matters
POST /routing/{id}/jurisdictions
POST /routing/{id}/candidates
DELETE /routing/{id}/candidates/{candidateId}
POST /routing/{id}/evaluate
POST /routing/{id}/recommend
POST /routing/{id}/selection/approve
POST /routing/{id}/selection/reject
POST /routing/reference/validate
```

API rules:

```text
- APIs must invoke Routing Service operations.
- APIs must not create Agent, Service Provider, Partner or Service Network automatically.
- APIs must not create Matter, Task or Communication directly.
- APIs must not execute procurement, payment or outbound communication.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Routing Service only under governed Agent Contracts.

Allowed AI use:

```text
suggest candidate list for review
summarize candidate eligibility
identify missing routing inputs
compare candidates based on authorized criteria
draft recommendation reason for review
flag policy or coverage mismatch
prepare routing decision memo
```

AI must not:

```text
make final selection where review is required
invent candidate capability, coverage or performance facts
expose confidential pricing or relationship data
create Agent/Provider/Partner records automatically
create Matter, Task or Communication automatically
execute procurement or payment
bypass conflicts, confidentiality or policy checks
```

AI Routing use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Routing Access Rule
Agent/Provider/Partner Access Rule
Jurisdiction Rule
Candidate Visibility Rule
Audit Rule
Human Review Rule for final selection where required
```

---

# 15. Validation Rules

Routing Service must enforce:

```text
[ ] routing_type is controlled.
[ ] status is controlled.
[ ] candidate_type is controlled.
[ ] createRoutingRequest requires routing_title_reference.
[ ] createRoutingRequest requires jurisdiction_reference_id.
[ ] createRoutingRequest requires service_scope_reference.
[ ] createRoutingRequest produces stable immutable Routing ID.
[ ] updateRoutingRequest does not mutate immutable ID.
[ ] changeRoutingStatus follows allowed lifecycle.
[ ] evaluateRoutingCandidates validates candidate references.
[ ] createRoutingRecommendation distinguishes AI draft from approved selection.
[ ] approveRoutingSelection requires selected_candidate_reference and approval context.
[ ] Routing Service does not create Agent/Provider/Partner automatically.
[ ] Routing Service does not create Matter/Task/Communication automatically.
[ ] Routing Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Routing Service should return controlled errors:

```text
RoutingNotFound
InvalidRoutingType
InvalidRoutingStatus
InvalidRoutingTransition
InvalidRoutingReference
RoutingTitleRequired
JurisdictionRequired
ServiceScopeRequired
CandidateRequired
InvalidCandidateType
InvalidCandidateReference
AgentNotFound
ServiceProviderNotFound
PartnerNotFound
JurisdictionNotFound
CandidateNotEligible
PolicyRestricted
SelectionApprovalRequired
SelectionRejected
RoutingExpired
ReviewRequired
PermissionRequired
AuditContextMissing
UnknownRoutingError
```

Errors must be safe for product display and API consumption.

Confidential pricing, contract, performance, relationship and matter strategy data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite routing domain spec
cite routing object spec
cite agent, service-provider, partner and service-network specs where relevant
preserve Routing / Agent boundary
preserve Routing / Service Provider boundary
preserve Routing / Partner boundary
preserve Routing / Service Network boundary
preserve Routing / Matter / Task / Communication boundaries
implement only Phase 4 MVP operations unless task says otherwise
write tests for createRoutingRequest requiring jurisdiction_reference_id
write tests for createRoutingRequest requiring service_scope_reference
write tests for controlled routing_type
write tests for controlled status and candidate_type
write tests preventing Routing Service from creating Agent/Provider/Partner automatically
write tests preventing Routing Service from creating Matter/Task/Communication automatically
write tests distinguishing AI recommendation from approved selection
write tests for event emission on mutation
```

Codex must not:

```text
invent full automatic routing marketplace in Phase 4
treat Routing as Agent or Service Provider lookup
treat Routing as Partner or Service Network
create candidate records directly
create execution objects directly
execute procurement, payment or communication
allow AI to finalize selection where review is required
expose confidential candidate terms by default
allow product UI to redefine Routing status
```

---

# 18. Acceptance Criteria

This Routing Service Specification is accepted only if:

```text
[ ] It defines Routing Service purpose.
[ ] It defines Routing Service Core meaning.
[ ] It identifies Routing Service as Collaboration Network Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing Service specification. Establishes Routing Service as candidate evaluation and selection-record service, separates Routing from Agent, Service Provider, Partner, Service Network, procurement and execution objects, and defines Phase 4 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
