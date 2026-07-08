# Domain Specification — Routing

**Spec ID:** B02-DOM-ROUTING  
**Spec Type:** Domain  
**Domain Name:** Routing  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-08 — Ontology and Domain Classification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Object Specs:** core-specs/objects/routing.md; core-specs/objects/routing-request.md; core-specs/objects/routing-candidate.md; core-specs/objects/routing-rule.md; core-specs/objects/routing-decision.md; core-specs/objects/routing-result.md; core-specs/objects/routing-status.md  
**Related Service Specs:** core-specs/services/routing-request-service.md; core-specs/services/routing-candidate-service.md; core-specs/services/routing-rule-service.md; core-specs/services/routing-decision-service.md; core-specs/services/routing-result-service.md; core-specs/services/routing-reference-validation-service.md  
**Related Event Specs:** core-specs/events/routing-request-created.md; core-specs/events/routing-candidates-generated.md; core-specs/events/routing-decision-created.md; core-specs/events/routing-decision-approved.md; core-specs/events/routing-decision-rejected.md; core-specs/events/routing-result-applied.md; core-specs/events/routing-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/routing/routing-contract.md; core-specs/contracts/routing/routing-request-contract.md; core-specs/contracts/routing/routing-candidate-contract.md; core-specs/contracts/routing/routing-rule-contract.md; core-specs/contracts/routing/routing-decision-contract.md; core-specs/contracts/routing/routing-result-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Routing Domain defines the Core meaning of selecting or recommending the appropriate party, channel, service provider, agent, workflow path or execution destination for a governed business or professional action in MarkOrbit.

It exists so that Orders, Matters, Tasks, Communications, Jurisdictions, Agents, Service Providers, Partners, AI Agents and product consumers can consistently request, evaluate, recommend, approve and apply routing decisions.

Routing is required before:

```text
agent selection
service provider selection
jurisdiction-specific assignment
matter handoff
task assignment recommendation
communication routing
customer-to-team routing
partner/service network routing
fallback provider selection
AI routing recommendation
reviewed routing decision
Codex implementation of collaboration routing workflows
```

The Routing Domain is a Collaboration Network Domain because MarkOrbit must coordinate work across internal teams, customers, agents, service providers and partners.

---

# 2. Core Meaning

Routing means:

```text
a governed Core decision or recommendation process that evaluates context, candidates, rules, eligibility and constraints to determine where work, communication, instruction or service execution should go.
```

Routing is not merely:

```text
an Agent
a Service Provider
a Partner
a Customer
a task assignment
a communication send action
a product dropdown
a hard-coded country mapping
a price comparison
an AI guess
a marketplace ranking
```

Routing answers:

```text
What needs to be routed?
Which object, matter, order, task or communication context applies?
Which candidates are eligible?
Which jurisdiction, service, status, capability, policy or business rule matters?
What recommendation or decision was produced?
Was the decision reviewed or approved?
Which downstream service should apply the result?
What audit trace is required?
```

---

# 3. Domain Category

Routing is a Collaboration Network Domain.

Collaboration Network Domains provide the Core basis for:

```text
cross-party coordination
agent selection support
service provider selection support
workflow handoff
communication destination selection
jurisdiction-sensitive execution routing
fallback decision support
AI-assisted routing recommendation
service network orchestration
```

Routing uses data from Agent, Service Provider, Jurisdiction, Communication, Matter, Order and Partner domains, but does not own those domains.

---

# 4. Architectural Position

Routing sits between collaboration capability data and execution handoff.

```text
Jurisdiction defines where the service applies
        ↓
Agent and Service Provider provide capability and eligibility
        ↓
Routing evaluates candidates and produces decision/recommendation
        ↓
Matter, Task, Communication or Workflow applies the result
        ↓
Event records routing outcome
        ↓
Audit preserves trace
```

Routing makes selection decisions or recommendations.

Agent and Service Provider provide candidate information.

Communication sends messages.

Matter and Task execute work.

Routing does not replace any of them.

---

# 5. Scope

The Routing Domain includes:

```text
routing definition
routing request
routing context
routing candidate
routing eligibility
routing rule
routing decision
routing recommendation
routing result
routing status
routing fallback boundary
routing approval boundary
routing relationship to Agent
routing relationship to Service Provider
routing relationship to Partner
routing relationship to Matter, Order and Task
routing relationship to Communication
routing reference validation
routing audit reference
routing event emission
routing use by AI Agents, Services, Workflows, APIs and Codex tasks
```

Phase 4 implementation should focus on:

```text
Routing Request
Routing Candidate
Routing Rule
Routing Decision
Routing Result
Routing Status
Routing Request Service
Routing Candidate Service
Routing Decision Service
Routing Result Service
Routing Reference Validation Service
RoutingRequestCreated event
RoutingCandidatesGenerated event
RoutingDecisionCreated event
RoutingDecisionApproved event
RoutingResultApplied event
RoutingReferenceValidated event
```

---

# 6. Boundary

## 6.1 In Boundary

The Routing Domain owns:

```text
Core Routing definition
routing request
routing context
routing candidate reference
routing eligibility boundary
routing rule boundary
routing decision
routing recommendation
routing result
routing fallback boundary
routing approval boundary
routing reference validation
routing event emission
routing reference used by collaboration workflows and products
```

## 6.2 Out of Boundary

The Routing Domain does not own:

```text
Agent profile lifecycle
Service Provider profile lifecycle
Partner relationship lifecycle
Customer lifecycle
Matter lifecycle
Order lifecycle
Task lifecycle
Communication message lifecycle
Notification lifecycle
payment or settlement lifecycle
pricing engine
provider marketplace
agent performance analytics engine
AI model scoring as final truth
official filing automation
```

Those responsibilities belong to:

```text
Agent Domain
Service Provider Domain
Partner Domain
Customer Domain
Matter Domain
Order Domain
Task Domain
Communication Domain
Notification Domain
Finance/Product implementation
AI Governance
Product implementation
External integration implementation
```

## 6.3 Boundary Notes

Routing selects or recommends destinations.

Agent and Service Provider supply candidate data.

Partner supplies cooperation/channel relationship context.

Matter, Task and Communication apply routing outcomes through their own services.

Routing must not perform external communication or professional execution directly.

---

# 7. Domain Rules

## 7.1 Routing Requires Request Context

Every Routing Decision must originate from a Routing Request or explicit system-triggered routing context.

Routing context should include:

```text
requested service
jurisdiction
matter or order reference
customer context where applicable
brand or trademark context where applicable
required capability
candidate pool
policy constraints
review requirement
```

## 7.2 Routing Requires Candidate Eligibility

Routing must evaluate candidates through controlled eligibility references.

Candidate eligibility may consider:

```text
jurisdiction scope
service capability
status
do-not-use status
communication availability
commercial reference
prior assignment
manual preference
policy restriction
```

## 7.3 Routing Recommendation Does Not Equal Approved Decision

AI or system recommendation must be distinguished from approved Routing Decision.

Routing decisions affecting external execution, provider selection or client-facing commitment should be reviewable.

## 7.4 Routing Does Not Execute Work

Routing may produce result references.

Matter, Task, Communication or Workflow services apply routing results.

Routing must not send communications, create external instructions or mutate matter execution directly.

## 7.5 Routing Must Support Fallback

Routing should support fallback or no-route outcomes.

No eligible candidate is a valid Routing Result and should trigger review or escalation where needed.

## 7.6 Routing Must Be Auditable

Routing-sensitive actions must preserve audit trace.

Audit-sensitive routing actions include:

```text
routing request creation
candidate generation
eligibility filtering
routing recommendation
routing decision approval
routing decision rejection
routing result application
fallback route selection
AI routing recommendation
manual override
no-route outcome
```

---

# 8. Primary Objects

The Routing Domain owns or directly governs the following Core Objects.

| Object | Ownership | MVP Depth | Meaning |
|--------|-----------|-----------|---------|
| Routing | Routing | Partial Implement | Core decision/recommendation process for selecting execution destination. |
| Routing Request | Routing | Partial Implement | Request to determine where work, communication or service should go. |
| Routing Context | Routing | Partial Implement | Context used to evaluate routing. |
| Routing Candidate | Routing / Agent / Service Provider / Partner | Partial Implement | Candidate destination or participant. |
| Routing Eligibility | Routing | Partial Implement | Eligibility result for candidate. |
| Routing Rule | Routing / Policy | Partial Implement | Rule or constraint used for routing. |
| Routing Decision | Routing | Partial Implement | Selected or approved routing outcome. |
| Routing Recommendation | Routing / AI Governance | Partial Implement | Suggested routing outcome requiring review where applicable. |
| Routing Result | Routing | Partial Implement | Result applied or ready to apply to downstream service. |
| Routing Status | Routing | Partial Implement | Controlled status of routing request or decision. |
| Routing Audit Reference | Routing / Audit | Partial Implement | Audit reference for routing-sensitive actions. |

Related objects owned by other domains or systems:

| Object | Owning Domain/System | Relationship |
|--------|----------------------|--------------|
| Agent | Agent | Agent may be routing candidate. |
| Service Provider | Service Provider | Service Provider may be routing candidate. |
| Partner | Partner | Partner may influence routing or be candidate. |
| Jurisdiction | Jurisdiction | Routing is often jurisdiction-sensitive. |
| Matter | Matter | Routing may assign or hand off matter execution. |
| Order | Order | Routing may be based on order scope. |
| Task | Task | Routing may recommend task assignee or destination. |
| Communication | Communication | Routing may determine communication recipient/channel. |
| Notification | Notification | Routing may inform notification recipients. |
| Policy | Policy | Routing rules and restrictions may be policy-sensitive. |
| AI Output | AI Governance | AI may produce routing recommendations. |
| Audit Record | Audit | Audit records routing-sensitive actions. |

---

# 9. Primary Services

The Routing Domain requires the following Core Services.

| Service | Ownership | MVP Depth | Purpose |
|---------|-----------|-----------|---------|
| Routing Request Service | Routing | Partial Implement | Create or update Routing Requests. |
| Routing Candidate Service | Routing / Agent / Service Provider | Partial Implement | Generate and validate routing candidates. |
| Routing Eligibility Service | Routing | Partial Implement | Evaluate candidate eligibility. |
| Routing Rule Service | Routing / Policy | Partial Implement | Resolve routing rules or constraints. |
| Routing Recommendation Service | Routing / AI Governance | Partial Implement | Produce routing recommendation. |
| Routing Decision Service | Routing | Partial Implement | Create or approve Routing Decision. |
| Routing Result Service | Routing | Partial Implement | Produce routing result for downstream application. |
| Routing Reference Validation Service | Routing | Partial Implement | Validate Routing references used by other domains. |
| Routing Audit Reference Service | Routing / Audit | Partial Implement | Produce routing audit reference for governed actions. |

Service rules:

```text
- Mutating Routing services must emit events.
- Routing services must not mutate Agent or Service Provider profiles.
- Routing services must not send Communication messages directly.
- Routing services must not create or close Matter directly.
- Routing Recommendation must be distinguishable from Routing Decision.
- AI-generated routing recommendations must be review-required where high-risk.
```

---

# 10. Primary Events

The Routing Domain emits or consumes the following Core Events.

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| RoutingRequestCreated | Routing Request Service | Partial Implement | Routing Request has been created. |
| RoutingRequestUpdated | Routing Request Service | Partial Implement | Routing Request fields have changed. |
| RoutingCandidatesGenerated | Routing Candidate Service | Partial Implement | Routing candidates have been generated. |
| RoutingCandidateEvaluated | Routing Eligibility Service | Partial Implement | Routing candidate eligibility has been evaluated. |
| RoutingRecommendationCreated | Routing Recommendation Service | Partial Implement | Routing recommendation has been created. |
| RoutingDecisionCreated | Routing Decision Service | Partial Implement | Routing Decision has been created. |
| RoutingDecisionApproved | Routing Decision Service / Review Service | Partial Implement | Routing Decision has been approved. |
| RoutingDecisionRejected | Routing Decision Service / Review Service | Partial Implement | Routing Decision has been rejected. |
| RoutingResultApplied | Routing Result Service / Downstream Service | Partial Implement | Routing Result has been applied downstream. |
| RoutingNoCandidateFound | Routing Candidate Service | Partial Implement | No eligible candidate was found. |
| RoutingReferenceValidated | Routing Reference Validation Service | Partial Implement | Routing reference has been validated for governed use. |
| RoutingReviewRequired | Routing Recommendation / Decision Service | Partial Implement | Routing output requires review. |

Event rules:

```text
- Routing events must reference Routing Request or Routing Decision.
- Candidate events must reference candidate type without exposing confidential provider details unnecessarily.
- Recommendation events must distinguish AI, system and human source.
- Result events must reference downstream object where applied.
- No-candidate events should trigger review or escalation where required.
```

---

# 11. Primary Contracts

Routing requires the following contracts.

| Contract | Contract Type | MVP Depth | Purpose |
|----------|---------------|-----------|---------|
| Routing Contract | Routing Contract | Partial Implement | Defines Routing fields, request, decision and result behavior. |
| Routing Request Contract | Routing Contract | Partial Implement | Defines routing context, required capability and candidate pool. |
| Routing Candidate Contract | Routing / Agent / Service Provider Contract | Partial Implement | Defines candidate reference and eligibility input. |
| Routing Eligibility Contract | Routing Contract | Partial Implement | Defines eligibility result and reason. |
| Routing Rule Contract | Routing / Policy Contract | Partial Implement | Defines routing rule, restriction and source reference. |
| Routing Recommendation Contract | Routing / AI Contract | Partial Implement | Defines recommendation source, confidence boundary and review requirement. |
| Routing Decision Contract | Routing Contract | Partial Implement | Defines selected candidate, decision source, approval and status. |
| Routing Result Contract | Routing / Workflow Contract | Partial Implement | Defines result applied to downstream service. |
| Routing Audit Contract | Audit Contract | Partial Implement | Defines audit fields required for routing-sensitive actions. |

Contract rules:

```text
- Routing Decision Contract must distinguish recommendation from approved decision.
- Routing Candidate Contract must not redefine Agent or Service Provider.
- Routing Result Contract must not execute downstream service by itself.
- Routing Rule Contract must preserve Policy boundary.
```

---

# 12. Relationships to Other Domains

## 12.1 Agent

Agent may be a routing candidate.

Agent owns foreign trademark collaborator profile and capability.

Routing owns candidate evaluation and decision.

## 12.2 Service Provider

Service Provider may be a routing candidate.

Service Provider owns provider profile and capability.

Routing owns selection logic.

## 12.3 Partner

Partner may influence routing or be a candidate in partner workflows.

Partner owns cooperation relationship lifecycle.

## 12.4 Jurisdiction

Routing is often jurisdiction-sensitive.

Jurisdiction provides where service applies.

## 12.5 Matter

Routing may assign or recommend matter participant or execution handoff.

Matter applies routing result through Matter services.

## 12.6 Order

Routing may use Order scope to determine needed provider or agent.

Order owns commercial service request.

## 12.7 Task

Routing may recommend Task assignee or execution destination.

Task applies assignment through Task services.

## 12.8 Communication

Routing may recommend communication participant or channel.

Communication sends messages through Communication services.

## 12.9 Notification

Routing may inform notification recipient routing, but Notification owns awareness intent.

## 12.10 Policy and Permission

Routing decisions may require Permission and Policy checks.

Policy may block certain candidates or require review.

## 12.11 AI Governance

AI may recommend routes but must not finalize high-risk routing decisions without governed service and review.

## 12.12 Audit

Audit records should include Routing references for routing-sensitive actions.

Audit storage and reporting rules belong to Audit cross-cutting system.

---

# 13. AI Agent Usage

AI Agents may use Routing only under governed Agent Contracts.

Allowed AI use:

```text
suggest routing candidates
summarize routing context
identify missing routing inputs
compare candidate eligibility
flag candidate mismatch with jurisdiction or capability
prepare routing recommendation notes
explain why no candidate is eligible
recommend review or escalation
```

AI must not:

```text
make final high-risk routing decision without governed service and review
apply routing result directly to Matter, Task or Communication
invent candidate eligibility
override do-not-use or policy restrictions
send external communication to routed party
change Agent or Service Provider status
expose confidential routing context outside authorized scope
```

AI Agent access requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Routing Object Access Rule
Routing Service Access Rule
Routing Event Access Rule
Agent / Service Provider / Partner Access Rules
Jurisdiction Rule
Permission Rule
Policy Rule
Review Rule
Audit Rule
Human Review Rule for high-risk routing decisions
```

---

# 14. Workflow Usage

Routing participates in collaboration and execution workflows.

Routing-sensitive workflows may include:

```text
routing-request-workflow.md
agent-routing-workflow.md
service-provider-routing-workflow.md
task-assignment-routing-workflow.md
communication-recipient-routing-workflow.md
matter-handoff-routing-workflow.md
routing-review-workflow.md
routing-fallback-workflow.md
ai-routing-recommendation-review-workflow.md
```

Workflow rules:

```text
- Routing workflows must reference Workflow Contracts.
- Routing candidates must be generated through governed services.
- Routing recommendations must be reviewable where high-risk.
- Routing results must be applied through downstream domain services.
- Routing must not send messages or mutate Matters directly.
- No-candidate outcomes must create review/escalation where required.
```

---

# 15. API Usage

Routing APIs expose request, candidate generation, eligibility, recommendation, decision and result through governed services.

Potential Phase 4 APIs:

```text
POST /routing/requests
GET /routing/requests/{id}
POST /routing/requests/{id}/candidates
POST /routing/requests/{id}/eligibility/evaluate
POST /routing/requests/{id}/recommendations
POST /routing/requests/{id}/decisions
POST /routing/decisions/{id}/approve
POST /routing/decisions/{id}/reject
POST /routing/results/{id}/apply
POST /routing/reference/validate
```

Potential partial/deferred APIs:

```text
POST /routing/requests/{id}/fallback
GET /routing/requests/{id}/audit-reference
POST /routing/requests/{id}/ai-recommendation
```

API rules:

```text
- APIs must invoke Routing Services.
- APIs must preserve Identity, User, Organization and Policy context.
- APIs must not mutate Agent, Service Provider, Matter, Task or Communication directly outside governed services.
- APIs must not expose confidential candidate data without Permission and Policy.
- Mutating APIs must emit or cause service-level events.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

API details belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

## 16.1 Phase 4 Consumers

```text
Workplace
MarkReg
MarkOrbit Lite
AI Agents
Codex Implementation
Validation tools
```

## 16.2 Partial Consumers

```text
Partner Center
Service Platform
Communication tools
Reporting consumers
Admin routing tools
```

## 16.3 Future Consumers

```text
External Integrations
Service Network
Marketplace
Advanced routing products
Provider procurement products
Agent performance analytics
Partner settlement products
```

Product rule:

```text
Products consume Routing.
Products do not redefine Routing.
```

---

# 17. MVP Scope

Routing is a Phase 4 / Wave 4 Partial Implement domain.

Phase 4 includes:

```text
Routing Request
Routing Context
Routing Candidate
Routing Eligibility
Routing Rule
Routing Decision
Routing Recommendation
Routing Result
Routing Status
Routing Request Service
Routing Candidate Service
Routing Eligibility Service
Routing Recommendation Service
Routing Decision Service
Routing Result Service
Routing Reference Validation Service
RoutingRequestCreated event
RoutingRequestUpdated event
RoutingCandidatesGenerated event
RoutingCandidateEvaluated event
RoutingRecommendationCreated event
RoutingDecisionCreated event
RoutingDecisionApproved event
RoutingDecisionRejected event
RoutingResultApplied event
RoutingNoCandidateFound event
RoutingReferenceValidated event
basic routing metadata validation
source traceability to Agent, Service Provider, Partner, Jurisdiction, Matter, Order, Task, Communication and AI systems
```

Phase 4 should support:

```text
basic routing request
basic candidate generation
basic eligibility evaluation
basic routing recommendation
basic routing decision
basic routing result reference
no-candidate outcome
AI-assisted routing recommendation with human review
```

Phase 4 does not require automated ranking engine, marketplace routing, performance analytics or autonomous routing.

---

# 18. Deferred Scope

Deferred scope includes:

```text
advanced automated ranking engine
performance-based routing optimization
provider marketplace routing
agent bidding workflow
multi-provider procurement routing
real-time capacity-based routing
risk-based routing engine
automatic fallback chains
cross-tenant routing federation
AI-autonomous routing decision
routing simulation environment
advanced routing analytics
```

Deferred scope must not be implemented by Codex as MVP unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Implementation-facing notes:

```text
Routing Request should use stable immutable ID.
Routing Context should include service, jurisdiction, object and required capability references.
Routing Candidate should reference Agent, Service Provider, Partner, User, Team or other approved candidate type.
Routing Eligibility should record decision reason.
Routing Recommendation should distinguish AI, system and human source.
Routing Decision should distinguish selected candidate from recommended candidate.
Routing Result should not directly mutate downstream objects without downstream services.
AI-generated routing recommendations should remain draft/recommendation output until reviewed where needed.
```

Suggested Routing Status values:

```text
Draft
Requested
CandidatesGenerated
RecommendationCreated
ReviewRequired
DecisionCreated
Approved
Rejected
Applied
NoCandidateFound
Cancelled
Archived
```

Phase 4 controlled Routing Status values:

```text
Draft
Requested
CandidatesGenerated
RecommendationCreated
ReviewRequired
DecisionCreated
Approved
Rejected
Applied
NoCandidateFound
Archived
```

Suggested Candidate Type values:

```text
Agent
ServiceProvider
Partner
InternalUser
InternalTeam
OrganizationUnit
SystemActor
AIAgent
Unknown
```

Phase 4 controlled Candidate Type values:

```text
Agent
ServiceProvider
Partner
InternalUser
InternalTeam
OrganizationUnit
Unknown
```

Suggested Eligibility Result values:

```text
Eligible
Ineligible
ReviewRequired
BlockedByPolicy
MissingCapability
MissingJurisdictionScope
Inactive
DoNotUse
Unknown
```

Do not treat Routing recommendation as final decision.

---

# 20. Codex Implementation Notes

Codex may implement Routing only from approved specs.

Codex must:

```text
cite this domain spec
cite related object specs
cite related service specs
cite related event specs
cite related contract specs
preserve Routing / Agent boundary
preserve Routing / Service Provider boundary
preserve Routing / Communication boundary
preserve Routing / Matter / Task boundaries
preserve Routing / AI Governance boundary
implement only Phase 4 Partial scope unless task says otherwise
write tests for routing request creation
write tests for candidate generation
write tests for eligibility evaluation
write tests for recommendation vs decision separation
write tests for decision approval/rejection
write tests for no-candidate outcome
write tests preventing Routing from mutating downstream domains directly
write tests preventing AI recommendation from becoming final decision automatically
```

Codex must not:

```text
invent automated ranking engine in Phase 4 Partial scope
invent marketplace routing in MVP
invent provider performance analytics inside Routing
mutate Agent or Service Provider profiles from Routing
send Communication messages from Routing
create or close Matter from Routing
assign Task directly without Task service
treat AI recommendation as approved routing decision
allow product UI to redefine Routing status
```

---

# 21. Validation Rules

Routing Domain must pass the following checks.

```text
[ ] Routing is classified as Collaboration Network Domain.
[ ] Routing is counted within the 26 baseline Core Domains.
[ ] Routing does not change the baseline Core Domain Map.
[ ] Routing has MVP Phase 4 / Wave 4 classification.
[ ] Routing has MVP Depth = Partial Implement.
[ ] Routing defines Core meaning.
[ ] Routing boundary excludes Agent and Service Provider lifecycle.
[ ] Routing boundary excludes Partner lifecycle.
[ ] Routing boundary excludes Matter, Order and Task lifecycle.
[ ] Routing boundary excludes Communication message lifecycle.
[ ] Routing boundary excludes marketplace, ranking and performance analytics engines.
[ ] Routing owns Routing Request.
[ ] Routing defines Routing Candidate.
[ ] Routing defines Routing Eligibility.
[ ] Routing defines Routing Recommendation.
[ ] Routing defines Routing Decision.
[ ] Routing defines Routing Result.
[ ] Routing lists primary services.
[ ] Mutating Routing services emit events.
[ ] Routing lists primary events.
[ ] Routing defines contract requirements.
[ ] Routing defines AI Agent usage constraints.
[ ] Routing defines workflow usage constraints.
[ ] Routing defines API usage constraints.
[ ] Routing defines product consumers.
[ ] Routing defines MVP and deferred scope.
[ ] Routing defines prohibited overreach.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
turn Routing into Agent
turn Routing into Service Provider
turn Routing into Partner
turn Routing into Matter
turn Routing into Task
turn Routing into Communication
turn Routing into provider marketplace
turn Routing into performance analytics engine
turn Routing into automated ranking engine in Phase 4
mutate downstream objects directly from Routing
send external communication from Routing
treat AI recommendation as approved decision
ignore do-not-use or policy restrictions
allow product UI to redefine Routing meaning
allow Codex to define new routing architecture
```

---

# 23. Acceptance Criteria

This Routing Domain Specification is accepted only if:

```text
[ ] It defines Routing purpose.
[ ] It defines Routing Core meaning.
[ ] It identifies Routing as Collaboration Network Domain.
[ ] It defines architectural position.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines domain rules.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to Agent, Service Provider, Partner, Jurisdiction, Matter, Order, Task, Communication, Notification, Permission, Policy, AI Governance and Audit.
[ ] It defines AI Agent usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Routing Domain specification. Establishes Routing as Phase 4 Collaboration Network Domain with Partial Implement depth, defines Routing Request, Candidate, Eligibility, Recommendation, Decision, Result, services, events, contracts, AI/workflow/API constraints, MVP scope and prohibited overreach. |

---

**End of Domain Specification**
