# Object Specification — Service Network

**Spec ID:** B02-OBJ-SERVICE-NETWORK  
**Spec Type:** Object  
**Object Name:** Service Network  
**Owning Domain:** Service Network  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/service-network.md  
**Related Object Specs:** core-specs/objects/partner.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/service-network-node.md; core-specs/objects/service-network-link.md; core-specs/objects/service-network-status.md  
**Related Service Specs:** core-specs/services/service-network-registration-service.md; core-specs/services/service-network-node-service.md; core-specs/services/service-network-link-service.md; core-specs/services/service-network-status-service.md; core-specs/services/service-network-reference-validation-service.md  
**Related Event Specs:** core-specs/events/service-network-created.md; core-specs/events/service-network-updated.md; core-specs/events/service-network-node-linked.md; core-specs/events/service-network-link-updated.md; core-specs/events/service-network-status-changed.md; core-specs/events/service-network-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/service-network/service-network-contract.md; core-specs/contracts/service-network/service-network-node-contract.md; core-specs/contracts/service-network/service-network-link-contract.md; core-specs/contracts/service-network/service-network-status-contract.md; core-specs/contracts/service-network/network-routing-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 5 — Network Expansion Core  
**MVP Wave:** Wave 5  
**MVP Depth:** Reserved  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Service Network object defines the Core-recognized collaboration ecosystem map used to represent how Partners, Agents, Service Providers, jurisdictions, service scopes and cooperation relationships connect within MarkOrbit.

It exists so that Partner, Agent, Service Provider, Routing, Jurisdiction, Matter, Opportunity, Communication, AI Agents, Services, APIs and product consumers can consistently reference the broader service ecosystem without confusing Service Network with a Partner relationship, Agent profile, Service Provider entity, Routing decision or execution workflow.

Service Network is required before:

```text
global service ecosystem mapping
partner-agent-provider network modeling
jurisdiction service coverage mapping
cross-border collaboration graph
network-based routing context
service coverage analysis
network relationship trace
partner ecosystem expansion
AI-assisted network summary
audit trace for network relationship changes
```

---

# 2. Core Meaning

Service Network means:

```text
a Core-recognized ecosystem map that describes nodes, links, coverage, relationships and service connectivity among Partners, Agents, Service Providers, jurisdictions and service scopes.
```

Service Network is not:

```text
Partner
Agent
Service Provider
Routing decision
Matter
Order
Task
Communication
Organization hierarchy
CRM pipeline
AI-generated graph by itself
```

Service Network answers:

```text
Which participants exist in the broader service ecosystem?
How are Partners, Agents and Service Providers connected?
Which jurisdictions and service scopes are covered?
Which links are active, limited, review-required or archived?
Which network context may support Routing?
What audit trace is required?
```

---

# 3. Object Category

Service Network is a Collaboration Network Object owned by the Service Network Domain.

It is the ecosystem mapping object.

Partner is cooperation-side relationship.

Agent is trademark-specific collaborator.

Service Provider is provider entity/capability profile.

Routing makes selection decisions.

Service Network must preserve these boundaries.

---

# 4. Architectural Position

Service Network sits above individual collaboration objects.

```text
Partner records cooperation relationship
        ↓
Agent records trademark collaborator profile
        ↓
Service Provider records provider entity/capability profile
        ↓
Service Network maps ecosystem relationships and coverage
        ↓
Routing may consume network context
        ↓
Matter / Task / Communication execute operational collaboration
```

Service Network maps.

Routing decides.

Matter executes.

Communication coordinates.

---

# 5. Scope

The Service Network object includes:

```text
service network id
network type
network status
network name/reference
network node references
network link references
partner references
agent references
service provider references
jurisdiction references
service scope references
coverage references
routing context references
source reference
created time
updated time
audit metadata
```

Phase 5 reserved scope includes:

```text
service network id
network type
network status
network name/reference
node references
link references
partner references
agent references
service provider references
jurisdiction references
service scope references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Reserved | Stable immutable Service Network ID. |
| network_type | enum | Yes | Reserved | Controlled network type. |
| name_reference | string | Yes | Reserved | Human-readable network name/reference. |
| status | enum | Yes | Reserved | Controlled Service Network status. |
| node_references | array | No | Reserved | Network node references. |
| link_references | array | No | Reserved | Network link references. |
| partner_reference_ids | array | No | Reserved | Related Partner references. |
| agent_reference_ids | array | No | Reserved | Related Agent references. |
| service_provider_reference_ids | array | No | Reserved | Related Service Provider references. |
| jurisdiction_reference_ids | array | No | Reserved | Jurisdiction coverage references. |
| service_scope_references | array | No | Reserved | Service scope coverage references. |
| coverage_reference_ids | array | No | Reserved | Coverage references. |
| routing_context_reference_ids | array | No | Reserved | Routing context references; not decision. |
| source_reference | string | No | Reserved | Intake/import/system source reference. |
| metadata | object | No | Reserved | Non-sensitive metadata only. |
| created_at | datetime | Yes | Reserved | Creation timestamp. |
| updated_at | datetime | Yes | Reserved | Last update timestamp. |
| created_by | string | No | Reserved | Identity or system actor reference. |
| updated_by | string | No | Reserved | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 network_type

Phase 5 controlled values:

```text
GlobalServiceNetwork
JurisdictionServiceNetwork
PartnerNetwork
AgentNetwork
ProviderNetwork
RegionalNetwork
InternalNetwork
CustomNetwork
Unknown
```

## 7.2 status

Phase 5 controlled values:

```text
Draft
Active
ReviewRequired
Limited
Deprecated
Archived
DeletedReferenceOnly
```

## 7.3 node_type

Suggested controlled values:

```text
Partner
Agent
ServiceProvider
Jurisdiction
Organization
InternalTeam
ExternalResource
Unknown
```

## 7.4 link_type

Suggested controlled values:

```text
Cooperation
Referral
Coverage
Capability
Representation
PreferredProvider
BackupProvider
Integration
HistoricalRelationship
Unknown
```

---

# 8. Object Rules

## 8.1 Service Network Requires Name, Type and Status

Every Service Network must define:

```text
network_type
name_reference
status
```

A loose collection of providers is not a Core-valid Service Network.

## 8.2 Service Network Is Not Partner

Partner represents cooperation-side relationship.

Service Network maps ecosystem structure across participants.

## 8.3 Service Network Is Not Agent

Agent represents trademark collaborator profile.

Service Network may include Agent nodes or links.

## 8.4 Service Network Is Not Service Provider

Service Provider represents provider entity/capability profile.

Service Network may include Service Provider nodes or links.

## 8.5 Service Network Is Not Routing

Service Network may provide context for Routing.

Routing makes selection or recommendation decisions.

## 8.6 Service Network Is Phase 5 Reserved

Service Network must not become MVP execution dependency unless explicitly approved.

Current implementation should remain reference/scaffold unless a Phase 5 task activates it.

## 8.7 Service Network Must Be Auditable

Service Network-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
service network creation
network type update
network status change
node addition/removal
link addition/removal
coverage update
partner linkage
agent linkage
service provider linkage
routing context linkage
AI network summary or recommendation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Partner | Network may include Partner | Partner remains cooperation relationship. |
| Agent | Network may include Agent | Agent remains trademark collaborator. |
| Service Provider | Network may include Provider | Provider remains entity/capability profile. |
| Jurisdiction | Network may map jurisdiction coverage | Jurisdiction remains procedural context. |
| Routing | Routing may consume network context | Routing makes decision. |
| Matter | Matter may reference network context indirectly | Matter remains execution container. |
| Opportunity | Opportunity may arise from network | Opportunity remains potential demand. |
| Communication | Network participants may communicate | Communication remains message lifecycle. |
| Organization | Network may include internal org context | Organization remains operating context. |
| AI Output | AI may summarize network | AI Output is not network truth. |
| Audit Record | Audit may reference network | Audit remains accountability system. |

---

# 10. Lifecycle

Service Network lifecycle states:

```text
Draft
Active
ReviewRequired
Limited
Deprecated
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → ReviewRequired
Draft → Active
ReviewRequired → Active
ReviewRequired → Limited
Active → ReviewRequired
Active → Limited
Limited → Active
Active → Deprecated
Deprecated → Archived
Limited → Archived
Active → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration/review
Deprecated → Active without reissue/new version
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Service Network object is created and managed through:

```text
Service Network Registration Service
Service Network Node Service
Service Network Link Service
Service Network Coverage Service
Service Network Status Service
Service Network Routing Context Service
Service Network Reference Validation Service
Service Network Audit Reference Service
```

Service rules:

```text
- Services must validate network_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not create Partner, Agent or Service Provider automatically.
- Services must not make Routing decision.
- Services must not activate Phase 5 behavior in Phase 1–4 MVP without explicit task approval.
```

---

# 12. Event Usage

Service Network object emits or participates in:

```text
ServiceNetworkCreated
ServiceNetworkUpdated
ServiceNetworkStatusChanged
ServiceNetworkNodeLinked
ServiceNetworkNodeRemoved
ServiceNetworkLinkCreated
ServiceNetworkLinkUpdated
ServiceNetworkLinkRemoved
ServiceNetworkCoverageUpdated
ServiceNetworkRoutingContextLinked
ServiceNetworkArchived
ServiceNetworkReferenceValidated
```

Event rules:

```text
- Service Network events must reference Service Network ID.
- Node and link events must preserve node/link references.
- Coverage events must preserve jurisdiction/service scope references.
- Routing context events must not imply Routing decision.
- AI-generated network events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 5 APIs:

```text
POST /service-networks
GET /service-networks/{id}
PATCH /service-networks/{id}
POST /service-networks/{id}/status
POST /service-networks/{id}/nodes
DELETE /service-networks/{id}/nodes/{nodeId}
POST /service-networks/{id}/links
PATCH /service-networks/{id}/links/{linkId}
POST /service-networks/reference/validate
```

API rules:

```text
- APIs must invoke Service Network Services.
- APIs must not create Partner, Agent or Service Provider automatically.
- APIs must not make Routing selection directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Service Network objects only under governed Agent Contracts.

Allowed AI use:

```text
summarize service network structure
identify missing network links
identify jurisdiction or service coverage gaps
suggest network relationship classification for review
prepare network expansion note
compare service network coverage for review
flag inactive or deprecated network nodes
```

AI must not:

```text
create Partner, Agent or Service Provider automatically
make final Routing decision
change network status without authorized service
invent relationship links or coverage facts
expose confidential network relationship data outside authorized scope
activate Phase 5 behavior without approved task
```

AI Service Network use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Service Network Access Rule
Partner/Agent/Provider Access Rule where applicable
Routing Rule where applicable
Audit Rule
Human Review Rule for network relationship changes
```

---

# 15. Validation Rules

Service Network object must pass:

```text
[ ] id is present and immutable.
[ ] network_type is controlled.
[ ] name_reference is present.
[ ] status is controlled.
[ ] Service Network does not equal Partner.
[ ] Service Network does not equal Agent.
[ ] Service Network does not equal Service Provider.
[ ] Service Network does not equal Routing.
[ ] Phase 5 Reserved boundary is preserved.
[ ] Node/link references are valid where implemented.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite service-network domain spec
preserve Service Network / Partner boundary
preserve Service Network / Agent boundary
preserve Service Network / Service Provider boundary
preserve Service Network / Routing boundary
preserve Phase 5 Reserved status
implement only scaffold/reference behavior unless Phase 5 task says otherwise
write tests for required name_reference
write tests for controlled network_type
write tests for controlled status
write tests preventing Service Network from creating Partner/Agent/Service Provider automatically
write tests preventing Service Network from making Routing decision
write tests preserving Phase 5 reserved gate
write tests for event emission on mutation where implemented
```

Codex must not:

```text
invent full service graph engine before Phase 5 approval
treat Service Network as Partner
treat Service Network as Agent
treat Service Network as Service Provider
treat Service Network as Routing
activate network workflow in Phase 1–4 MVP without explicit task
create downstream entities automatically from Service Network
allow product UI to redefine Service Network status
```

---

# 17. Acceptance Criteria

This Service Network Object Specification is accepted only if:

```text
[ ] It defines Service Network purpose.
[ ] It defines Service Network Core meaning.
[ ] It identifies Service Network as Collaboration Network Object.
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
| 0.1.0 | Draft | Initial Service Network object specification. Establishes Service Network as collaboration ecosystem map, separates it from Partner, Agent, Service Provider and Routing, and preserves Phase 5 Reserved implementation boundary. |

---

**End of Object Specification**
