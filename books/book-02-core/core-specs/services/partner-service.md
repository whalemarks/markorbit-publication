# Service Specification — Partner Service

**Spec ID:** B02-SVC-PARTNER-SERVICE  
**Spec Type:** Service  
**Service Name:** Partner Service  
**Owning Domain:** Partner  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/partner.md  
**Related Object Specs:** core-specs/objects/partner.md; core-specs/objects/service-provider.md; core-specs/objects/agent.md; core-specs/objects/routing.md; core-specs/objects/service-network.md; core-specs/objects/customer.md; core-specs/objects/communication.md; core-specs/objects/matter.md  
**Related Service Specs:** core-specs/services/service-provider-service.md; core-specs/services/agent-service.md; core-specs/services/routing-service.md; core-specs/services/service-network-service.md; core-specs/services/communication-service.md; core-specs/services/matter-service.md; core-specs/services/policy-service.md  
**Related Event Specs:** core-specs/events/partner-created.md; core-specs/events/partner-updated.md; core-specs/events/partner-status-changed.md; core-specs/events/partner-service-scope-linked.md; core-specs/events/partner-provider-linked.md; core-specs/events/partner-agent-linked.md; core-specs/events/partner-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/partner/partner-contract.md; core-specs/contracts/partner/partner-reference-contract.md; core-specs/contracts/partner/partner-relationship-contract.md; core-specs/contracts/partner/partner-scope-contract.md; core-specs/contracts/partner/partner-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 5 — Network Expansion Core  
**MVP Wave:** Wave 5  
**MVP Depth:** Reserved  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Partner Service defines the Core service boundary for creating, updating, validating, linking and managing Partner objects.

It exists so that Service Provider, Agent, Routing, Service Network, Communication, Matter, AI Agents, APIs and product consumers can consistently reference cooperation-side business relationships without confusing Partner with Customer, Agent, Service Provider, Organization, Routing decision, procurement contract, referral source or generic contact record.

Partner Service is required before:

```text
partner relationship management
partner cooperation scope reference
partner-to-agent linkage
partner-to-service-provider linkage
partner communication context
partner matter collaboration context
partner service network mapping
partner routing context
AI-assisted partner summary
audit trace for partner-sensitive actions
```

---

# 2. Core Meaning

Partner Service means:

```text
the Core service that manages cooperation-side business relationship records and their governed relationships to agents, service providers, routing context, service network context, communication and matters.
```

Partner Service does not mean:

```text
Customer Service
Agent Service
Service Provider Service
Organization Service
Routing Service
Service Network Service
procurement contract system
payment settlement system
generic CRM contact system
```

Partner Service answers:

```text
Does this Partner relationship exist?
What cooperation type and scope apply?
Which Agent or Service Provider records relate to it?
Which Service Network context may include it?
Is this Partner active, limited, suspended, archived or review-required?
Can this Partner be considered as routing or collaboration context?
Can another domain safely reference this Partner?
What audit trace is required?
```

---

# 3. Service Category

Partner Service is a Collaboration Network Core Service.

It manages cooperation-side relationship context.

It does not own provider capability profiles.

It does not own trademark-specific agent profiles.

It does not make routing decisions.

Partner is Phase 5 Reserved in current MVP planning.

---

# 4. Architectural Position

Partner Service sits above individual provider/agent records as a cooperation relationship layer.

```text
Agent Service manages trademark collaborator profile
        ↓
Service Provider Service manages provider entity/capability profile
        ↓
Partner Service manages cooperation-side relationship context
        ↓
Service Network maps broader ecosystem
        ↓
Routing Service may consume partner context
        ↓
Matter / Task / Communication execute collaboration
```

Partner represents cooperation relationship.

Agent and Service Provider represent operational candidate profiles.

Routing decides.

Service Network maps ecosystem.

---

# 5. Scope

Partner Service includes:

```text
partner creation
partner update
partner status management
partner relationship scope management
partner service scope linkage
partner jurisdiction linkage
partner agent linkage
partner service-provider linkage
partner communication linkage
partner matter linkage
partner service-network linkage
partner reference validation
partner audit trace
partner event emission
```

Phase 5 reserved scope includes:

```text
create partner
get partner
update partner metadata
change partner status
link partner to service scope
link partner to agent
link partner to service provider
link partner to communication
link partner to service network
validate partner reference
emit partner events
```

Deferred scope includes:

```text
partner revenue sharing
partner settlement
partner contract lifecycle
partner commission engine
partner marketplace
partner performance scoring automation
automatic partner routing selection
advanced partner network analytics
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createPartner | Create Partner object | Reserved | PartnerCreated |
| getPartner | Retrieve Partner by ID | Reserved | No |
| updatePartner | Update governed metadata | Reserved | PartnerUpdated |
| changePartnerStatus | Change lifecycle status | Reserved | PartnerStatusChanged |
| linkPartnerServiceScope | Link service/cooperation scope | Reserved | PartnerServiceScopeLinked |
| unlinkPartnerServiceScope | Remove service/cooperation scope | Reserved | PartnerServiceScopeUnlinked |
| linkPartnerJurisdiction | Link jurisdiction context | Reserved | PartnerJurisdictionLinked |
| linkPartnerAgent | Link Partner to Agent | Reserved | PartnerAgentLinked |
| linkPartnerServiceProvider | Link Partner to Service Provider | Reserved | PartnerServiceProviderLinked |
| linkPartnerCommunication | Link Partner to Communication | Reserved | PartnerCommunicationLinked |
| linkPartnerMatter | Link Partner to Matter | Reserved | PartnerMatterLinked |
| linkPartnerServiceNetwork | Link Partner to Service Network | Reserved | PartnerServiceNetworkLinked |
| validatePartnerReference | Validate whether Partner can be referenced | Reserved | PartnerReferenceValidated |
| validatePartnerRoutingContext | Validate partner context for Routing | Reserved | PartnerRoutingContextValidated |
| archivePartner | Archive Partner reference | Reserved | PartnerArchived |

---

# 7. Inputs

Partner Service accepts:

```text
partner_type
partner_name_reference
status
relationship_type
cooperation_scope_references
service_scope_references
jurisdiction_reference_ids
agent_reference_ids
service_provider_reference_ids
service_network_reference_ids
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
partner_type
partner_name_reference
relationship_type
status
source_reference
actor_context
```

Required for service scope linkage:

```text
partner_reference_id
service_scope_reference
scope_type
actor_context
```

Required for agent/provider linkage:

```text
partner_reference_id
agent_reference_id or service_provider_reference_id
link_type
actor_context
```

Required for validation:

```text
partner_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Partner Service returns:

```text
Partner object
Partner reference
Partner validation result
Partner relationship result
Partner service scope link result
Partner agent/provider link result
Partner routing context result
Partner status result
Partner event reference
error result
```

Validation output must include:

```text
is_valid
partner_reference_id
partner_type
relationship_type
status
service_scope_hint where applicable
agent_reference_hint where applicable
service_provider_reference_hint where applicable
reason_code
policy_hint where applicable
```

Routing context output must include:

```text
eligible_context
partner_reference_id
service_scope_reference
jurisdiction_reference_id where applicable
routing_context_status
reason_code
review_required
```

Validation output must not expose confidential partner terms, commercial arrangements, pricing, contracts, customer, agent, provider or matter data unnecessarily.

---

# 9. Controlled Values

## 9.1 partner_type

```text
AgencyPartner
ReferralPartner
ChannelPartner
StrategicPartner
TechnologyPartner
ServicePartner
RegionalPartner
InternalPartner
GeneralPartner
Unknown
```

## 9.2 relationship_type

```text
Referral
Channel
ServiceCooperation
StrategicCooperation
TechnologyIntegration
RegionalCooperation
NetworkCooperation
InternalCooperation
Other
Unknown
```

## 9.3 status

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

## 9.4 scope_type

```text
ServiceScope
JurisdictionScope
CustomerScope
MatterScope
TechnologyScope
NetworkScope
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

## 10.1 Partner Represents Cooperation-Side Relationship

Partner Service manages cooperation relationship context.

It must not be reduced to a customer, provider, agent or contact record.

## 10.2 Partner Is Not Customer

Customer is the demand-side commercial party.

Partner is cooperation-side business relationship.

## 10.3 Partner Is Not Agent

Agent represents trademark-specific collaborator profile.

Partner may link to Agent but must not replace it.

## 10.4 Partner Is Not Service Provider

Service Provider represents provider entity/capability profile.

Partner may link to Service Provider but must not replace it.

## 10.5 Partner Is Not Routing

Partner may provide routing context.

Routing Service makes candidate evaluation, recommendation or selection records.

## 10.6 Partner Is Phase 5 Reserved

Partner Service must remain reserved unless a Phase 5 task explicitly activates implementation.

Phase 1–4 products must not depend on Partner as mandatory execution primitive.

## 10.7 Partner Does Not Own Settlement or Contract Lifecycle

Commission, revenue sharing, procurement contracts, settlement and payment are outside this service unless future finance/procurement specs define them.

## 10.8 Partner Changes Must Be Auditable

Partner-sensitive operations must preserve actor, source, request context, relationship scope, linked object trace and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Agent Service | Partner may link to Agent | Agent owns collaborator profile. |
| Service Provider Service | Partner may link to Provider | Provider owns capability profile. |
| Service Network Service | Partner may be network node/context | Service Network maps ecosystem. |
| Routing Service | Routing may consume Partner context | Routing makes decision. |
| Matter Service | Partner may support Matter | Matter owns execution container. |
| Task Service | Partner may relate to tasks | Task owns work unit. |
| Communication Service | Partner may participate in communication | Communication owns message lifecycle. |
| Customer Service | Partner is not Customer | Customer owns demand-side party. |
| Policy Service | Controls relationship visibility/use | Policy owns contextual constraints. |
| AI Agent Governance | AI may summarize Partner profile | Agent Contract governs AI use. |
| Audit Service | Records Partner-sensitive action | Audit owns accountability trail. |
| Event Service | Records Partner events | Event records occurrence. |

---

# 12. Event Usage

Partner Service emits:

```text
PartnerCreated
PartnerUpdated
PartnerStatusChanged
PartnerServiceScopeLinked
PartnerServiceScopeUnlinked
PartnerJurisdictionLinked
PartnerAgentLinked
PartnerServiceProviderLinked
PartnerCommunicationLinked
PartnerMatterLinked
PartnerServiceNetworkLinked
PartnerRoutingContextValidated
PartnerArchived
PartnerReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Scope events must preserve service/jurisdiction/network scope reference.
- Agent/provider link events must reference Agent or Service Provider ID.
- Routing context events must not imply final Routing decision.
- Events must not expose confidential partner terms, pricing or contracts unnecessarily.
- AI-generated partner summaries must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 5 APIs:

```text
POST /partners
GET /partners/{id}
PATCH /partners/{id}
POST /partners/{id}/status
POST /partners/{id}/service-scopes
DELETE /partners/{id}/service-scopes/{scopeId}
POST /partners/{id}/jurisdictions
POST /partners/{id}/agents
POST /partners/{id}/service-providers
POST /partners/{id}/communications
POST /partners/{id}/matters
POST /partners/{id}/service-networks
POST /partners/{id}/routing-context/validate
POST /partners/reference/validate
```

API rules:

```text
- APIs must invoke Partner Service operations.
- APIs must not create Customer, Agent or Service Provider automatically.
- APIs must not make Routing selection.
- APIs must not create settlement, commission, procurement or payment obligations.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Partner Service only under governed Agent Contracts.

Allowed AI use:

```text
summarize Partner profile
identify missing cooperation scope
identify missing Agent or Service Provider link
suggest partner relationship classification for review
suggest routing-context questions for review
compare partner cooperation context for review
flag inactive, suspended or review-required Partner
prepare partner onboarding note
```

AI must not:

```text
create Partner without authorized service
change Partner status without authorized service
invent cooperation scope or commercial terms
treat Partner as Customer, Agent or Service Provider
select Partner as final Routing decision
create settlement, commission, procurement or payment obligations
expose confidential partner agreements
activate Phase 5 behavior without approved task
```

AI Partner use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Partner Access Rule
Agent/Provider Access Rule where applicable
Routing Rule where applicable
Service Network Rule where applicable
Audit Rule
Human Review Rule for status, scope and routing-sensitive changes
```

---

# 15. Validation Rules

Partner Service must enforce:

```text
[ ] partner_type is controlled.
[ ] relationship_type is controlled.
[ ] status is controlled.
[ ] createPartner requires partner_name_reference.
[ ] createPartner requires relationship_type.
[ ] createPartner produces stable immutable Partner ID.
[ ] updatePartner does not mutate immutable ID.
[ ] changePartnerStatus follows allowed lifecycle.
[ ] linkPartnerAgent references valid Agent.
[ ] linkPartnerServiceProvider references valid Service Provider.
[ ] validatePartnerRoutingContext does not make final Routing decision.
[ ] validatePartnerReference rejects missing, inactive, suspended, archived or deleted-reference partners where not allowed.
[ ] Partner Service does not create Customer/Agent/Service Provider automatically.
[ ] Partner Service does not create settlement/payment obligations.
[ ] Partner Service preserves Phase 5 Reserved boundary.
[ ] Partner Service emits events for mutation where implemented.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Partner Service should return controlled errors:

```text
PartnerNotFound
InvalidPartnerType
InvalidRelationshipType
InvalidPartnerStatus
InvalidPartnerTransition
InvalidPartnerReference
PartnerNameRequired
RelationshipTypeRequired
AgentNotFound
InvalidAgentReference
ServiceProviderNotFound
InvalidServiceProviderReference
ServiceScopeInvalid
PartnerSuspended
PartnerInactive
RoutingContextInvalid
Phase5Reserved
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownPartnerError
```

Errors must be safe for product display and API consumption.

Confidential partner terms, contracts, pricing, customer, agent, provider and matter relationship data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite partner domain spec
cite partner object spec
cite agent, service-provider, routing and service-network specs where relevant
preserve Partner / Customer boundary
preserve Partner / Agent boundary
preserve Partner / Service Provider boundary
preserve Partner / Routing boundary
preserve Partner / Settlement / Payment boundaries
preserve Phase 5 Reserved status
implement only scaffold/reference behavior unless Phase 5 task says otherwise
write tests for createPartner requiring partner_name_reference where implemented
write tests for createPartner requiring relationship_type where implemented
write tests for controlled partner_type, relationship_type and status
write tests preventing Partner Service from creating Customer/Agent/Provider automatically
write tests preventing Partner Service from making Routing decisions
write tests preventing settlement/payment obligations
write tests preserving Phase 5 reserved gate
```

Codex must not:

```text
invent full partner marketplace in Phase 1–4
treat Partner as Customer
treat Partner as Agent
treat Partner as Service Provider
make routing selection inside Partner Service
create Agent or Service Provider directly from Partner Service
create settlement, commission or payment obligations
activate Partner as mandatory MVP dependency before Phase 5 approval
expose confidential partner terms by default
allow product UI to redefine Partner status
```

---

# 18. Acceptance Criteria

This Partner Service Specification is accepted only if:

```text
[ ] It defines Partner Service purpose.
[ ] It defines Partner Service Core meaning.
[ ] It identifies Partner Service as Collaboration Network Core Service.
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
| 0.1.0 | Draft | Initial Partner Service specification. Establishes Partner Service as cooperation-side relationship service, separates Partner from Customer, Agent, Service Provider, Routing, settlement and payment, and preserves Phase 5 Reserved implementation boundary. |

---

**End of Service Specification**
