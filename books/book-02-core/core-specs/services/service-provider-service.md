# Service Specification — Service Provider Service

**Spec ID:** B02-SVC-SERVICE-PROVIDER-SERVICE  
**Spec Type:** Service  
**Service Name:** Service Provider Service  
**Owning Domain:** Service Provider  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/service-provider.md  
**Related Object Specs:** core-specs/objects/service-provider.md; core-specs/objects/agent.md; core-specs/objects/partner.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/communication.md; core-specs/objects/matter.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/partner-service.md; core-specs/services/routing-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/communication-service.md; core-specs/services/matter-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/service-provider-created.md; core-specs/events/service-provider-updated.md; core-specs/events/service-provider-status-changed.md; core-specs/events/service-provider-capability-linked.md; core-specs/events/service-provider-jurisdiction-linked.md; core-specs/events/service-provider-agent-linked.md; core-specs/events/service-provider-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/service-provider/service-provider-contract.md; core-specs/contracts/service-provider/service-provider-reference-contract.md; core-specs/contracts/service-provider/service-provider-capability-contract.md; core-specs/contracts/service-provider/service-provider-coverage-contract.md; core-specs/contracts/service-provider/service-provider-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Network and Growth Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Service Provider Service defines the Core service boundary for creating, updating, validating, linking and managing Service Provider objects.

It exists so that Agent, Partner, Routing, Communication, Matter, Jurisdiction, Task, AI Agents, APIs and product consumers can consistently reference provider entities and capability profiles without confusing Service Provider with Agent, Partner, Customer, Organization, Routing decision, procurement contract, payment account or general contact record.

Service Provider Service is required before:

```text
provider profile management
provider capability reference
provider jurisdiction/service coverage reference
provider-to-agent linkage
provider-to-partner linkage
provider candidate validation for routing
provider communication context
provider matter collaboration context
AI-assisted provider summary
audit trace for provider-sensitive actions
```

---

# 2. Core Meaning

Service Provider Service means:

```text
the Core service that manages external or internal provider entity profiles, capability references, coverage references and governed relationships to agents, partners, routing context, communication and matters.
```

Service Provider Service does not mean:

```text
Agent Service
Partner Service
Customer Service
Organization Service
Routing Service
Communication Service
procurement marketplace
vendor payment system
provider selection decision engine
```

Service Provider Service answers:

```text
Does this Service Provider exist?
Which capabilities and service scopes are associated?
Which jurisdictions or regions are covered?
Which Agent or Partner records relate to it?
Is this Service Provider active, preferred, limited, suspended or archived?
Can this Service Provider be considered as a routing candidate?
Can another domain safely reference this Service Provider?
What audit trace is required?
```

---

# 3. Service Category

Service Provider Service is a Collaboration Network Core Service.

It manages provider entity and capability profiles.

It does not make routing decisions.

It does not replace Agent.

It does not execute matters.

---

# 4. Architectural Position

Service Provider Service sits beside Agent and before Routing.

```text
Service Provider Service manages provider entity/capability profile
        ↓
Agent Service manages trademark-specific collaborator profile
        ↓
Jurisdiction and capability references define coverage context
        ↓
Routing Service evaluates candidate selection
        ↓
Matter / Task / Communication execute collaboration
```

Service Provider provides entity/capability profile.

Agent provides trademark collaborator profile.

Routing decides selection.

Matter executes work.

---

# 5. Scope

Service Provider Service includes:

```text
service provider creation
service provider update
service provider status management
service provider capability linkage
service provider jurisdiction linkage
service provider agent linkage
service provider partner linkage
service provider communication linkage
service provider matter linkage
service provider routing candidate validation
service provider reference validation
service provider audit trace
service provider event emission
```

MVP/Phase 4 scope includes:

```text
create service provider
get service provider
update service provider metadata
change service provider status
link service provider to capability/service scope
link service provider to jurisdiction
link service provider to agent
link service provider to communication
link service provider to matter
validate service provider reference
validate routing eligibility
emit service provider events
```

Deferred scope includes:

```text
procurement marketplace
provider contract lifecycle
payment settlement
automatic provider ranking
performance scoring automation
supplier risk engine
advanced service network analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createServiceProvider | Create Service Provider object | Yes | ServiceProviderCreated |
| getServiceProvider | Retrieve Service Provider by ID | Yes | No |
| updateServiceProvider | Update governed metadata | Yes | ServiceProviderUpdated |
| changeServiceProviderStatus | Change lifecycle status | Yes | ServiceProviderStatusChanged |
| linkServiceProviderCapability | Link capability/service scope | Yes | ServiceProviderCapabilityLinked |
| unlinkServiceProviderCapability | Remove capability/service scope | Partial | ServiceProviderCapabilityUnlinked |
| linkServiceProviderJurisdiction | Link jurisdiction coverage | Yes | ServiceProviderJurisdictionLinked |
| unlinkServiceProviderJurisdiction | Remove jurisdiction coverage | Partial | ServiceProviderJurisdictionUnlinked |
| linkServiceProviderAgent | Link Service Provider to Agent | Yes | ServiceProviderAgentLinked |
| linkServiceProviderPartner | Link Service Provider to Partner | Partial | ServiceProviderPartnerLinked |
| linkServiceProviderCommunication | Link Service Provider to Communication | Partial | ServiceProviderCommunicationLinked |
| linkServiceProviderMatter | Link Service Provider to Matter | Partial | ServiceProviderMatterLinked |
| validateServiceProviderReference | Validate whether Service Provider can be referenced | Yes | ServiceProviderReferenceValidated |
| validateServiceProviderRoutingEligibility | Validate candidate eligibility for Routing | Yes | ServiceProviderRoutingEligibilityValidated |
| archiveServiceProvider | Archive Service Provider reference | Partial | ServiceProviderArchived |

---

# 7. Inputs

Service Provider Service accepts:

```text
service_provider_type
provider_name_reference
status
jurisdiction_reference_ids
capability_reference_ids
service_scope_references
agent_reference_ids
partner_reference_ids
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
service_provider_type
provider_name_reference
status
source_reference
actor_context
```

Required for capability linkage:

```text
service_provider_reference_id
capability_reference_id or service_scope_reference
actor_context
```

Required for jurisdiction linkage:

```text
service_provider_reference_id
jurisdiction_reference_id
coverage_type
actor_context
```

Required for routing eligibility validation:

```text
service_provider_reference_id
jurisdiction_reference_id
service_scope_reference
routing_context
actor_context
```

Required for validation:

```text
service_provider_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Service Provider Service returns:

```text
Service Provider object
Service Provider reference
Service Provider validation result
Service Provider capability link result
Service Provider jurisdiction link result
Service Provider agent link result
Service Provider routing eligibility result
Service Provider status result
Service Provider event reference
error result
```

Validation output must include:

```text
is_valid
service_provider_reference_id
service_provider_type
status
jurisdiction_reference_hint where applicable
capability_reference_hint where applicable
agent_reference_hint where applicable
reason_code
policy_hint where applicable
```

Routing eligibility output must include:

```text
eligible
service_provider_reference_id
jurisdiction_reference_id
service_scope_reference
eligibility_status
reason_code
review_required
routing_hint
```

Validation output must not expose confidential pricing, contract, performance, customer, agent or matter data unnecessarily.

---

# 9. Controlled Values

## 9.1 service_provider_type

```text
TrademarkFirm
LawFirm
FilingProvider
SearchProvider
RenewalProvider
TranslationProvider
DocumentProvider
EvidenceProvider
TechnologyProvider
InternalProvider
GeneralProvider
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

## 10.1 Service Provider Represents Provider Entity and Capability Profile

Service Provider Service manages provider entity profile, capability references and coverage references.

It must not be reduced to Agent or contact record.

## 10.2 Service Provider Is Not Agent

Service Provider may link to Agent.

Agent Service owns trademark-specific collaborator profile.

## 10.3 Service Provider Is Not Partner

Partner represents cooperation-side business relationship.

Service Provider represents provider entity/capability profile.

## 10.4 Service Provider Is Not Customer

Service Provider belongs to supply-side or collaboration context, not demand-side party context.

## 10.5 Service Provider Does Not Make Routing Decision

Service Provider provides candidate data and eligibility context.

Routing Service makes recommendation or selection decision.

## 10.6 Service Provider Does Not Own Procurement or Payment

Procurement contracts, settlement, payable, invoice and payment workflows are outside this service unless future finance/procurement specs define them.

## 10.7 Service Provider Changes Must Be Auditable

Service Provider-sensitive operations must preserve actor, source, request context, capability changes, coverage changes and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Agent Service | Service Provider may link to Agent | Agent owns collaborator profile. |
| Partner Service | Provider may have Partner relationship | Partner owns cooperation relationship. |
| Jurisdiction Service | Provider may cover Jurisdiction | Jurisdiction owns where context. |
| Routing Service | Provider may be routing candidate | Routing makes decision. |
| Matter Service | Provider may support Matter | Matter owns execution container. |
| Task Service | Provider may relate to tasks | Task owns work unit. |
| Communication Service | Provider may participate in communication | Communication owns message lifecycle. |
| Document Service | Provider may provide documents | Document owns artifact lifecycle. |
| Policy Service | Controls eligibility/access | Policy owns contextual constraints. |
| AI Agent Governance | AI may summarize Provider profile | Agent Contract governs AI use. |
| Audit Service | Records Provider-sensitive action | Audit owns accountability trail. |
| Event Service | Records Provider events | Event records occurrence. |

---

# 12. Event Usage

Service Provider Service emits:

```text
ServiceProviderCreated
ServiceProviderUpdated
ServiceProviderStatusChanged
ServiceProviderCapabilityLinked
ServiceProviderCapabilityUnlinked
ServiceProviderJurisdictionLinked
ServiceProviderJurisdictionUnlinked
ServiceProviderAgentLinked
ServiceProviderPartnerLinked
ServiceProviderCommunicationLinked
ServiceProviderMatterLinked
ServiceProviderRoutingEligibilityValidated
ServiceProviderArchived
ServiceProviderReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Jurisdiction link events must reference Jurisdiction ID.
- Capability link events must reference capability or service scope.
- Agent link events must reference Agent ID.
- Routing eligibility events must not imply final Routing decision.
- Events must not expose confidential pricing, contract or matter data unnecessarily.
- AI-generated provider summaries must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /service-providers
GET /service-providers/{id}
PATCH /service-providers/{id}
POST /service-providers/{id}/status
POST /service-providers/{id}/capabilities
DELETE /service-providers/{id}/capabilities/{capabilityId}
POST /service-providers/{id}/jurisdictions
DELETE /service-providers/{id}/jurisdictions/{jurisdictionId}
POST /service-providers/{id}/agents
POST /service-providers/{id}/partners
POST /service-providers/{id}/communications
POST /service-providers/{id}/matters
POST /service-providers/{id}/routing-eligibility/validate
POST /service-providers/reference/validate
```

API rules:

```text
- APIs must invoke Service Provider Service operations.
- APIs must not create Agent unless Agent Service is invoked.
- APIs must not create Partner unless Partner Service is invoked.
- APIs must not make Routing selection.
- APIs must not create Matter, Task, Document or Evidence automatically.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Service Provider Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Service Provider profile
identify missing capability/service scope
identify missing jurisdiction coverage
suggest provider-agent relationship for review
suggest routing eligibility questions for review
compare provider capability context for review
flag inactive, suspended or review-required provider
prepare provider onboarding note
```

AI must not:

```text
select provider as final routing decision
create Service Provider without authorized service
change Service Provider status without authorized service
invent jurisdiction coverage or capability
expose confidential pricing, contracts or matter data
create Agent or Partner automatically
create procurement/payment obligations
```

AI Service Provider use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Service Provider Access Rule
Jurisdiction Access Rule
Routing Rule where applicable
Agent/Partner Access Rule where applicable
Audit Rule
Human Review Rule for status, coverage and routing-sensitive changes
```

---

# 15. Validation Rules

Service Provider Service must enforce:

```text
[ ] service_provider_type is controlled.
[ ] status is controlled.
[ ] coverage_type is controlled.
[ ] createServiceProvider requires provider_name_reference.
[ ] createServiceProvider produces stable immutable Service Provider ID.
[ ] updateServiceProvider does not mutate immutable ID.
[ ] changeServiceProviderStatus follows allowed lifecycle.
[ ] linkServiceProviderJurisdiction references valid Jurisdiction.
[ ] linkServiceProviderAgent references valid Agent.
[ ] validateServiceProviderRoutingEligibility does not make final Routing decision.
[ ] validateServiceProviderReference rejects missing, inactive, suspended, archived or deleted-reference providers where not allowed.
[ ] Service Provider Service does not create Agent or Partner automatically.
[ ] Service Provider Service does not create Matter/Task/Document/Evidence automatically.
[ ] Service Provider Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Service Provider Service should return controlled errors:

```text
ServiceProviderNotFound
InvalidServiceProviderType
InvalidServiceProviderStatus
InvalidServiceProviderTransition
InvalidServiceProviderReference
ProviderNameRequired
JurisdictionNotFound
InvalidJurisdictionReference
CapabilityNotFound
InvalidCapabilityReference
AgentNotFound
InvalidAgentReference
PartnerNotFound
InvalidPartnerReference
ServiceProviderSuspended
ServiceProviderInactive
JurisdictionMismatch
CapabilityMismatch
RoutingEligibilityFailed
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownServiceProviderError
```

Errors must be safe for product display and API consumption.

Confidential provider pricing, contract, agent, matter and relationship data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite service-provider domain spec
cite service-provider object spec
cite agent and routing specs where relevant
preserve Service Provider / Agent boundary
preserve Service Provider / Partner boundary
preserve Service Provider / Customer boundary
preserve Service Provider / Routing boundary
preserve Service Provider / Procurement / Payment boundaries
implement only Phase 4 MVP operations unless task says otherwise
write tests for createServiceProvider requiring provider_name_reference
write tests for controlled service_provider_type
write tests for controlled status
write tests for jurisdiction coverage validation
write tests preventing Service Provider Service from making Routing decisions
write tests preventing Service Provider Service from creating Agent/Partner automatically
write tests preventing procurement/payment obligations inside Service Provider Service
write tests for event emission on mutation
```

Codex must not:

```text
invent full procurement marketplace in Phase 4
treat Service Provider as Agent
treat Service Provider as Partner
treat Service Provider as Customer
make routing selection inside Service Provider Service
create Agent or Partner directly from Service Provider Service
create Matter or Task directly from Service Provider Service
create payment or procurement obligations
expose confidential provider terms by default
allow product UI to redefine Service Provider status
```

---

# 18. Acceptance Criteria

This Service Provider Service Specification is accepted only if:

```text
[ ] It defines Service Provider Service purpose.
[ ] It defines Service Provider Service Core meaning.
[ ] It identifies Service Provider Service as Collaboration Network Core Service.
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
| 0.1.0 | Draft | Initial Service Provider Service specification. Establishes Service Provider Service as provider entity/capability profile service, separates Service Provider from Agent, Partner, Customer, Routing, procurement and payment, and defines Phase 4 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
