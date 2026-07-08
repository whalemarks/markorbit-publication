# Object Specification — Routing

**Spec ID:** B02-OBJ-ROUTING  
**Spec Type:** Object  
**Object Name:** Routing  
**Owning Domain:** Routing  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/routing.md  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/jurisdiction.md; core-specs/objects/routing-request.md; core-specs/objects/routing-candidate.md; core-specs/objects/routing-decision.md; core-specs/objects/routing-rule-reference.md  
**Related Service Specs:** core-specs/services/routing-request-service.md; core-specs/services/routing-candidate-service.md; core-specs/services/routing-evaluation-service.md; core-specs/services/routing-decision-service.md; core-specs/services/routing-reference-validation-service.md  
**Related Event Specs:** core-specs/events/routing-request-created.md; core-specs/events/routing-candidates-generated.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-decision-made.md; core-specs/events/routing-decision-overridden.md; core-specs/events/routing-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/routing/routing-contract.md; core-specs/contracts/routing/routing-request-contract.md; core-specs/contracts/routing/routing-candidate-contract.md; core-specs/contracts/routing/routing-evaluation-contract.md; core-specs/contracts/routing/routing-decision-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Routing object defines the Core-recognized selection or recommendation context used to determine which Agent, Service Provider, Partner, internal team or other execution resource should support a matter, order, task or professional service need.

It exists so that Matters, Orders, Agents, Service Providers, Jurisdictions, Capabilities, Policies, Communications, AI Agents, Services, APIs and product consumers can consistently request, evaluate, explain, approve, override and audit routing decisions without confusing Routing with Agent data, Service Provider data, Partner relationship, workflow execution or AI recommendation alone.

Routing is required before:

```text
agent selection
service provider selection
jurisdiction-based routing
capability-based routing
matter assignment support
order fulfillment allocation
routing candidate comparison
routing decision explanation
human override of recommendation
AI-assisted routing recommendation
audit trace for provider selection
```

---

# 2. Core Meaning

Routing means:

```text
a Core-recognized decision or recommendation context that evaluates eligible candidates against governed criteria and records candidate set, evaluation basis, decision status, selected target and audit trace.
```

Routing is not:

```text
Agent
Service Provider
Partner
Matter
Order
Task
Workflow Contract
Communication
AI recommendation by itself
fee engine
quality score engine
procurement system
```

Routing answers:

```text
What execution need requires routing?
Which candidates are eligible?
Which criteria or rules were considered?
Which Agent, Service Provider or team was recommended or selected?
Was the decision automatic, AI-assisted, manual or overridden?
Which Matter, Order, Task, Jurisdiction or service scope is affected?
What audit trace is required?
```

---

# 3. Object Category

Routing is a Collaboration Network Object owned by the Routing Domain.

It is the selection/recommendation decision context.

Agent and Service Provider provide candidate data.

Routing makes or records selection decisions.

Routing must preserve these boundaries.

---

# 4. Architectural Position

Routing sits between execution need and collaborator assignment.

```text
Matter / Order / Task requires execution support
        ↓
Jurisdiction and service scope define requirements
        ↓
Agent / Service Provider provide candidate data
        ↓
Routing evaluates candidates
        ↓
Decision or recommendation is recorded
        ↓
Matter / Task / Communication consumes approved routing result
```

Routing decides or recommends.

Agent and Service Provider do not decide.

Matter and Task consume routing results.

---

# 5. Scope

The Routing object includes:

```text
routing id
routing type
routing status
routing request reference
source object reference
jurisdiction reference
service scope reference
candidate references
evaluation criteria references
policy reference
capability reference
recommendation reference
decision reference
selected candidate reference
override reference
review reference
matter/order/task reference
source reference
created time
updated time
audit metadata
```

MVP / Phase 4 scope includes:

```text
routing id
routing type
routing status
routing request reference
source object reference
jurisdiction reference
service scope reference
candidate references
evaluation criteria references
recommendation reference
decision reference
selected candidate reference
override reference
matter/order/task reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Routing ID. |
| routing_type | enum | Yes | Yes | Controlled routing type. |
| status | enum | Yes | Yes | Controlled Routing status. |
| title_reference | string | No | Yes | Human-readable routing title/reference. |
| routing_request_reference_id | string | No | Yes | Routing request reference. |
| source_object_type | enum/string | Yes | Yes | Matter, Order, Task, Communication, System, Unknown. |
| source_object_reference_id | string | Yes | Yes | Object that requires routing. |
| jurisdiction_reference_id | string | No | Yes | Jurisdiction context. |
| service_scope_reference | string | No | Yes | Service scope reference. |
| candidate_references | array | No | Yes | Candidate Agent/Service Provider/team references. |
| evaluation_criteria_references | array | No | Yes | Criteria/rule references. |
| policy_reference_ids | array | No | Partial | Related Policy references. |
| capability_reference_ids | array | No | Partial | Capability references considered. |
| recommendation_reference_id | string | No | Partial | AI/system/manual recommendation reference. |
| decision_status | enum | No | Yes | Decision status. |
| selected_candidate_reference_id | string | No | Yes | Selected/recommended candidate reference. |
| selected_candidate_type | enum | No | Yes | Agent, ServiceProvider, Team, User, Partner, Unknown. |
| override_reference_id | string | No | Partial | Override reason/actor reference. |
| review_reference_id | string | No | Partial | Review/approval reference. |
| matter_reference_id | string | No | Partial | Related Matter reference. |
| order_reference_id | string | No | Partial | Related Order reference. |
| task_reference_id | string | No | Partial | Related Task reference. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 routing_type

MVP controlled values:

```text
AgentRouting
ServiceProviderRouting
InternalTeamRouting
TaskAssigneeRouting
MatterSupportRouting
OrderFulfillmentRouting
CommunicationRouting
Other
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Requested
CandidatesGenerated
EvaluationRequired
Recommended
DecisionRequired
Selected
Rejected
Overridden
Cancelled
Archived
DeletedReferenceOnly
```

## 7.3 decision_status

Suggested controlled values:

```text
NoDecision
RecommendationOnly
PendingReview
Approved
Rejected
Overridden
AutoSelected
ManuallySelected
Unknown
```

## 7.4 selected_candidate_type

Suggested controlled values:

```text
Agent
ServiceProvider
Team
User
Partner
SystemActor
Unknown
```

## 7.5 source_object_type

Suggested controlled values:

```text
Matter
Order
Task
Communication
Notification
System
Unknown
```

---

# 8. Object Rules

## 8.1 Routing Requires Source Object

Every Routing object must define:

```text
source_object_type
source_object_reference_id
routing_type
status
```

A candidate comparison without source execution need is not Core-valid Routing.

## 8.2 Routing Is Not Agent

Agent provides collaborator profile and routing eligibility data.

Routing evaluates candidates and records recommendation/decision.

## 8.3 Routing Is Not Service Provider

Service Provider provides entity/capability profile.

Routing evaluates and decides.

## 8.4 Routing Is Not AI Recommendation Alone

AI may recommend routing options.

A Routing decision must be created and recorded through Routing services.

AI recommendation must not become selected candidate automatically unless policy allows automated selection.

## 8.5 Routing Does Not Mutate Downstream Objects Directly

Routing may produce selected candidate or decision reference.

Matter, Task, Communication or Order assignment must be performed by their respective services.

## 8.6 Routing Must Preserve Criteria and Candidate Trace

Routing-sensitive decisions should preserve:

```text
candidate set
criteria references
jurisdiction/service scope
recommendation source
decision actor/source
override reason where applicable
```

## 8.7 Routing Must Be Auditable

Routing-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
routing request creation
candidate generation
criteria update
AI recommendation
manual recommendation
selection decision
decision rejection
decision override
selected candidate update
downstream assignment linkage
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Agent | Routing may evaluate Agent | Agent remains candidate data. |
| Service Provider | Routing may evaluate Provider | Provider remains candidate data. |
| Partner | Routing may consider Partner | Partner remains cooperation relationship. |
| Jurisdiction | Routing may be jurisdiction-scoped | Jurisdiction remains procedural context. |
| Capability | Routing may use capability references | Capability remains ability descriptor. |
| Policy | Routing may be policy-constrained | Policy remains contextual constraint. |
| Matter | Routing may support Matter assignment | Matter service performs assignment. |
| Order | Routing may support Order fulfillment | Order remains commercial request. |
| Task | Routing may support Task assignment | Task service performs assignment. |
| Communication | Routing may support communication destination | Communication service sends/links message. |
| AI Output | AI may recommend candidates | AI Output is not final Routing decision. |
| Audit Record | Audit may reference Routing | Audit remains accountability system. |

---

# 10. Lifecycle

Routing lifecycle states:

```text
Draft
Requested
CandidatesGenerated
EvaluationRequired
Recommended
DecisionRequired
Selected
Rejected
Overridden
Cancelled
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → Requested
Requested → CandidatesGenerated
CandidatesGenerated → EvaluationRequired
EvaluationRequired → Recommended
Recommended → DecisionRequired
DecisionRequired → Selected
DecisionRequired → Rejected
Recommended → Selected
Selected → Overridden
Requested → Cancelled
Rejected → Archived
Cancelled → Archived
Selected → Archived
Overridden → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Draft → Selected without candidate/decision trace
AI Recommendation → Selected without policy/decision service
Rejected → Selected without restoration/review
Archived → Selected without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Routing object is created and managed through:

```text
Routing Request Service
Routing Candidate Service
Routing Evaluation Service
Routing Recommendation Service
Routing Decision Service
Routing Override Service
Routing Reference Validation Service
Routing Audit Reference Service
```

Service rules:

```text
- Services must validate routing_type.
- Services must validate source object reference.
- Services must validate candidate references.
- Services must validate status and decision transitions.
- Services must emit events for mutating actions.
- Services must not mutate Matter, Task, Order or Communication directly.
- Services must not create Agent or Service Provider directly.
- AI recommendations must remain recommendation references until decision rules are satisfied.
```

---

# 12. Event Usage

Routing object emits or participates in:

```text
RoutingRequestCreated
RoutingUpdated
RoutingStatusChanged
RoutingCandidatesGenerated
RoutingEvaluationRequired
RoutingEvaluated
RoutingRecommended
RoutingDecisionRequired
RoutingDecisionMade
RoutingDecisionRejected
RoutingDecisionOverridden
RoutingCancelled
RoutingArchived
RoutingReferenceValidated
```

Event rules:

```text
- Routing events must reference Routing ID.
- Candidate events must preserve candidate references.
- Decision events must preserve selected candidate and decision actor/source where allowed.
- Override events must preserve override reason/reference.
- AI recommendation events must identify AI source.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /routing
GET /routing/{id}
PATCH /routing/{id}
POST /routing/{id}/candidates
POST /routing/{id}/evaluate
POST /routing/{id}/recommend
POST /routing/{id}/decision
POST /routing/{id}/override
POST /routing/reference/validate
```

API rules:

```text
- APIs must invoke Routing Services.
- APIs must not mutate Matter, Task, Order or Communication directly.
- APIs must not create Agent or Service Provider directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Routing only under governed Agent Contracts.

Allowed AI use:

```text
suggest candidate agents or providers
summarize routing criteria
compare candidates for review
identify missing routing inputs
flag candidate mismatch with jurisdiction or capability
draft routing recommendation explanation
detect routing decision/assignment mismatch
```

AI must not:

```text
make final routing decision unless policy explicitly allows automated selection
assign Agent or Service Provider to Matter directly
mutate Task assignee directly
invent candidate capability or coverage
ignore blacklisted/suspended candidate status
override human decision without authorized service
send communication based on routing decision directly
```

AI Routing use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Routing Access Rule
Agent Access Rule
Service Provider Access Rule
Matter/Task/Order Rule where applicable
Audit Rule
Human Review Rule for final selection or override
```

---

# 15. Validation Rules

Routing object must pass:

```text
[ ] id is present and immutable.
[ ] routing_type is controlled.
[ ] status is controlled.
[ ] source_object_type is present.
[ ] source_object_reference_id is present.
[ ] Routing does not equal Agent.
[ ] Routing does not equal Service Provider.
[ ] Routing does not equal AI recommendation alone.
[ ] Candidate references are valid where present.
[ ] Selected candidate is traceable to candidate set or override.
[ ] Routing does not mutate downstream objects directly.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite routing domain spec
preserve Routing / Agent boundary
preserve Routing / Service Provider boundary
preserve Routing / Matter / Task / Order boundaries
preserve Routing / AI Recommendation boundary
implement only Phase 4 MVP fields unless task says otherwise
write tests for required source_object_type
write tests for required source_object_reference_id
write tests for controlled routing_type
write tests for controlled status
write tests preventing Routing from mutating Matter/Task/Order directly
write tests preventing AI recommendation from becoming selected decision automatically
write tests preventing Routing from creating Agent/Service Provider directly
write tests for selected candidate traceability
write tests for event emission on mutation
```

Codex must not:

```text
invent full routing optimization engine in Phase 4 MVP
treat Agent as Routing decision
treat Service Provider as Routing decision
make AI recommendation a final selection without policy
assign Matter/Task directly from Routing object
create Agent or Service Provider from Routing service
store sensitive commercial scoring by default
allow product UI to redefine Routing status
```

---

# 17. Acceptance Criteria

This Routing Object Specification is accepted only if:

```text
[ ] It defines Routing purpose.
[ ] It defines Routing Core meaning.
[ ] It identifies Routing as Collaboration Network Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing object specification. Establishes Routing as selection/recommendation decision context, separates Routing from Agent, Service Provider, Partner, Matter, Task and AI recommendation, and defines Phase 4 MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
