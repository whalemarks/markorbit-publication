# Service Specification — Agent Service

**Spec ID:** B02-SVC-AGENT-SERVICE  
**Spec Type:** Service  
**Service Name:** Agent Service  
**Owning Domain:** Agent  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/agent.md  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/partner.md; core-specs/objects/routing.md; core-specs/objects/communication.md; core-specs/objects/jurisdiction.md; core-specs/objects/matter.md  
**Related Service Specs:** core-specs/services/service-provider-service.md; core-specs/services/partner-service.md; core-specs/services/routing-service.md; core-specs/services/communication-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/matter-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/agent-updated.md; core-specs/events/agent-status-changed.md; core-specs/events/agent-jurisdiction-linked.md; core-specs/events/agent-capability-linked.md; core-specs/events/agent-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/agent/agent-contract.md; core-specs/contracts/agent/agent-reference-contract.md; core-specs/contracts/agent/agent-coverage-contract.md; core-specs/contracts/agent/agent-capability-contract.md; core-specs/contracts/agent/agent-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Network and Growth Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Agent Service defines the Core service boundary for creating, updating, validating, linking and managing Agent objects.

It exists so that Service Provider, Partner, Routing, Communication, Matter, Jurisdiction, Task, AI Agents, APIs and product consumers can consistently reference external trademark collaborators without confusing Agent with Service Provider, Partner, Customer, Organization, Routing decision, communication contact or general vendor profile.

Agent Service is required before:

```text
foreign agent profile management
agent jurisdiction coverage reference
agent capability reference
agent matter collaboration context
agent communication context
agent candidate validation for routing
agent performance/reference metadata
AI-assisted agent summary
audit trace for agent-sensitive actions
```

---

# 2. Core Meaning

Agent Service means:

```text
the Core service that manages external trademark collaborator profiles and their governed relationships to jurisdictions, capabilities, service providers, routing context, communication and matters.
```

Agent Service does not mean:

```text
Service Provider Service
Partner Service
Customer Service
Organization Service
Routing Service
Communication Service
vendor procurement system
agent selection decision engine
```

Agent Service answers:

```text
Does this Agent exist?
Which jurisdictions and service capabilities are associated?
Which Service Provider or Organization context may relate to it?
Is this Agent active, suspended, review-required or archived?
Can this Agent be considered as a routing candidate?
Which Communication or Matter references are linked?
Can another domain safely reference this Agent?
What audit trace is required?
```

---

# 3. Service Category

Agent Service is a Collaboration Network Core Service.

It manages trademark-specific collaborator profiles.

It does not own provider entity lifecycle.

It does not make routing decisions.

It does not execute matters.

---

# 4. Architectural Position

Agent Service sits between collaboration profile and routing/execution.

```text
Service Provider may define provider entity/capability profile
        ↓
Agent Service manages trademark collaborator profile
        ↓
Jurisdiction and capability references define coverage context
        ↓
Routing Service evaluates candidate selection
        ↓
Matter / Task / Communication execute collaboration
```

Agent provides candidate data.

Routing decides selection.

Matter executes professional work.

Communication coordinates messages.

---

# 5. Scope

Agent Service includes:

```text
agent creation
agent update
agent status management
agent jurisdiction linkage
agent capability linkage
agent service-provider linkage
agent communication linkage
agent matter linkage
agent routing candidate validation
agent reference validation
agent audit trace
agent event emission
```

MVP/Phase 4 scope includes:

```text
create agent
get agent
update agent metadata
change agent status
link agent to jurisdiction
link agent to capability/service scope
link agent to service provider
link agent to communication
link agent to matter
validate agent reference
validate agent routing eligibility
emit agent events
```

Deferred scope includes:

```text
agent ranking engine
agent procurement marketplace
agent performance scoring automation
contract negotiation system
payment settlement
automatic agent selection
advanced service network analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createAgent | Create Agent object | Yes | AgentCreated |
| getAgent | Retrieve Agent by ID | Yes | No |
| updateAgent | Update governed metadata | Yes | AgentUpdated |
| changeAgentStatus | Change Agent lifecycle status | Yes | AgentStatusChanged |
| linkAgentJurisdiction | Link jurisdiction coverage | Yes | AgentJurisdictionLinked |
| unlinkAgentJurisdiction | Remove jurisdiction coverage | Partial | AgentJurisdictionUnlinked |
| linkAgentCapability | Link capability/service scope | Yes | AgentCapabilityLinked |
| unlinkAgentCapability | Remove capability/service scope | Partial | AgentCapabilityUnlinked |
| linkAgentServiceProvider | Link Agent to Service Provider | Yes | AgentServiceProviderLinked |
| linkAgentCommunication | Link Agent to Communication | Partial | AgentCommunicationLinked |
| linkAgentMatter | Link Agent to Matter | Partial | AgentMatterLinked |
| validateAgentReference | Validate whether Agent can be referenced | Yes | AgentReferenceValidated |
| validateAgentRoutingEligibility | Validate candidate eligibility for Routing | Yes | AgentRoutingEligibilityValidated |
| archiveAgent | Archive Agent reference | Partial | AgentArchived |

---

# 7. Inputs

Agent Service accepts:

```text
agent_type
agent_name_reference
status
jurisdiction_reference_ids
capability_reference_ids
service_scope_references
service_provider_reference_id
organization_reference_id
contact_references
communication_reference_ids
matter_reference_ids
routing_context_reference
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
agent_type
agent_name_reference
status
source_reference
actor_context
```

Required for jurisdiction linkage:

```text
agent_reference_id
jurisdiction_reference_id
coverage_type
actor_context
```

Required for capability linkage:

```text
agent_reference_id
capability_reference_id or service_scope_reference
actor_context
```

Required for routing eligibility validation:

```text
agent_reference_id
jurisdiction_reference_id
service_scope_reference
routing_context
actor_context
```

Required for validation:

```text
agent_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Agent Service returns:

```text
Agent object
Agent reference
Agent validation result
Agent jurisdiction link result
Agent capability link result
Agent service-provider link result
Agent routing eligibility result
Agent status result
Agent event reference
error result
```

Validation output must include:

```text
is_valid
agent_reference_id
agent_type
status
jurisdiction_reference_hint where applicable
capability_reference_hint where applicable
reason_code
policy_hint where applicable
```

Routing eligibility output must include:

```text
eligible
agent_reference_id
jurisdiction_reference_id
service_scope_reference
eligibility_status
reason_code
review_required
routing_hint
```

Validation output must not expose confidential pricing, contract, performance, customer or matter data unnecessarily.

---

# 9. Controlled Values

## 9.1 agent_type

```text
ForeignTrademarkAgent
LocalCounsel
FilingAgent
SearchAgent
RenewalAgent
LitigationAgent
TranslationAgent
DocumentAgent
EvidenceAgent
GeneralAgent
Unknown
```

## 9.2 status

```text
Draft
Active
ReviewRequired
Preferred
Limited
Suspended
Inactive
Archived
DeletedReferenceOnly
```

## 9.3 coverage_type

```text
PrimaryCoverage
SecondaryCoverage
BackupCoverage
LimitedCoverage
HistoricalCoverage
Unknown
```

## 9.4 eligibility_status

```text
Eligible
NotEligible
ReviewRequired
Limited
Suspended
JurisdictionMismatch
CapabilityMismatch
PolicyRestricted
Unknown
```

## 9.5 validation_result

```text
Valid
Invalid
NotFound
Inactive
Suspended
Archived
ReviewRequired
PolicyRestricted
Unknown
```

---

# 10. Service Rules

## 10.1 Agent Is External Trademark Collaborator

Agent Service manages trademark-specific collaborator profiles.

It must not be generalized into every supplier or vendor type.

## 10.2 Agent Is Not Service Provider

Agent may link to Service Provider.

Service Provider Service owns provider entity and capability profile.

## 10.3 Agent Is Not Partner

Partner represents cooperation-side business relationship.

Agent represents trademark collaborator profile.

## 10.4 Agent Is Not Customer

Agent belongs to collaboration/supply-side context, not demand-side party context.

## 10.5 Agent Does Not Make Routing Decision

Agent provides candidate data and eligibility context.

Routing Service makes recommendation or selection decision.

## 10.6 Agent Communication Does Not Become Document or Evidence Automatically

Communication involving Agent remains Communication unless registered by Document or Evidence Service.

## 10.7 Agent Changes Must Be Auditable

Agent-sensitive operations must preserve actor, source, request context, coverage changes, capability changes and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Service Provider Service | Agent may link to Provider | Provider owns entity/capability profile. |
| Partner Service | Partner may cooperate with Agent | Partner owns cooperation relationship. |
| Jurisdiction Service | Agent may cover Jurisdiction | Jurisdiction owns where context. |
| Routing Service | Agent may be routing candidate | Routing makes decision. |
| Matter Service | Agent may support Matter | Matter owns execution container. |
| Task Service | Agent may relate to tasks | Task owns work unit. |
| Communication Service | Agent may participate in communication | Communication owns message lifecycle. |
| Document Service | Agent may provide documents | Document owns artifact lifecycle. |
| Policy Service | Controls eligibility/access | Policy owns contextual constraints. |
| AI Agent Governance | AI may summarize Agent profile | Agent Contract governs AI use. |
| Audit Service | Records Agent-sensitive action | Audit owns accountability trail. |
| Event Service | Records Agent events | Event records occurrence. |

---

# 12. Event Usage

Agent Service emits:

```text
AgentCreated
AgentUpdated
AgentStatusChanged
AgentJurisdictionLinked
AgentJurisdictionUnlinked
AgentCapabilityLinked
AgentCapabilityUnlinked
AgentServiceProviderLinked
AgentCommunicationLinked
AgentMatterLinked
AgentRoutingEligibilityValidated
AgentArchived
AgentReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Jurisdiction link events must reference Jurisdiction ID.
- Capability link events must reference capability or service scope.
- Routing eligibility events must not imply final Routing decision.
- Events must not expose confidential pricing, contract or matter data unnecessarily.
- AI-generated agent summaries must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /agents
GET /agents/{id}
PATCH /agents/{id}
POST /agents/{id}/status
POST /agents/{id}/jurisdictions
DELETE /agents/{id}/jurisdictions/{jurisdictionId}
POST /agents/{id}/capabilities
DELETE /agents/{id}/capabilities/{capabilityId}
POST /agents/{id}/service-provider
POST /agents/{id}/communications
POST /agents/{id}/matters
POST /agents/{id}/routing-eligibility/validate
POST /agents/reference/validate
```

API rules:

```text
- APIs must invoke Agent Service operations.
- APIs must not create Service Provider unless Service Provider Service is invoked.
- APIs must not make Routing selection.
- APIs must not create Matter, Task, Document or Evidence automatically.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Agent Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Agent profile
identify missing jurisdiction coverage
identify missing capability/service scope
suggest routing eligibility questions for review
compare Agent coverage context for review
flag inactive, suspended or review-required Agent
prepare Agent onboarding note
suggest Communication linkage for review
```

AI must not:

```text
select Agent as final routing decision
create Agent without authorized service
change Agent status without authorized service
invent jurisdiction coverage or capability
expose confidential pricing, contracts or matter data
create Service Provider automatically
convert Agent communication into Document/Evidence automatically
```

AI Agent Service use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Agent Access Rule
Jurisdiction Access Rule
Routing Rule where applicable
Communication Access Rule where applicable
Audit Rule
Human Review Rule for status, coverage and routing-sensitive changes
```

---

# 15. Validation Rules

Agent Service must enforce:

```text
[ ] agent_type is controlled.
[ ] status is controlled.
[ ] coverage_type is controlled.
[ ] createAgent requires agent_name_reference.
[ ] createAgent produces stable immutable Agent ID.
[ ] updateAgent does not mutate immutable ID.
[ ] changeAgentStatus follows allowed lifecycle.
[ ] linkAgentJurisdiction references valid Jurisdiction.
[ ] validateAgentRoutingEligibility does not make final Routing decision.
[ ] validateAgentReference rejects missing, inactive, suspended, archived or deleted-reference agents where not allowed.
[ ] Agent Service does not create Service Provider automatically.
[ ] Agent Service does not create Matter/Task/Document/Evidence automatically.
[ ] Agent Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Agent Service should return controlled errors:

```text
AgentNotFound
InvalidAgentType
InvalidAgentStatus
InvalidAgentTransition
InvalidAgentReference
AgentNameRequired
JurisdictionNotFound
InvalidJurisdictionReference
CapabilityNotFound
InvalidCapabilityReference
ServiceProviderNotFound
InvalidServiceProviderReference
AgentSuspended
AgentInactive
JurisdictionMismatch
CapabilityMismatch
RoutingEligibilityFailed
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownAgentError
```

Errors must be safe for product display and API consumption.

Confidential agent pricing, contract, matter and relationship data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite agent domain spec
cite agent object spec
cite service-provider and routing specs where relevant
preserve Agent / Service Provider boundary
preserve Agent / Partner boundary
preserve Agent / Customer boundary
preserve Agent / Routing boundary
implement only Phase 4 MVP operations unless task says otherwise
write tests for createAgent requiring agent_name_reference
write tests for controlled agent_type
write tests for controlled status
write tests for jurisdiction coverage validation
write tests preventing Agent Service from making Routing decisions
write tests preventing Agent Service from creating Service Provider automatically
write tests preventing Agent Service from creating Matter/Task/Document/Evidence automatically
write tests for event emission on mutation
```

Codex must not:

```text
invent full procurement marketplace in Phase 4
treat Agent as Service Provider
treat Agent as Partner
treat Agent as Customer
make routing selection inside Agent Service
create Service Provider directly from Agent Service
create Matter or Task directly from Agent Service
expose confidential agent terms by default
allow product UI to redefine Agent status
```

---

# 18. Acceptance Criteria

This Agent Service Specification is accepted only if:

```text
[ ] It defines Agent Service purpose.
[ ] It defines Agent Service Core meaning.
[ ] It identifies Agent Service as Collaboration Network Core Service.
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
| 0.1.0 | Draft | Initial Agent Service specification. Establishes Agent Service as external trademark collaborator profile service, separates Agent from Service Provider, Partner, Customer, Routing and Communication, and defines Phase 4 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
