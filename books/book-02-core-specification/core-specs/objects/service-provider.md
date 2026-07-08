# Object Specification — Service Provider

**Spec ID:** B02-OBJ-SERVICE-PROVIDER  
**Spec Type:** Object  
**Object Name:** Service Provider  
**Owning Domain:** Service Provider  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/service-provider.md  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/routing.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/service-provider-profile.md; core-specs/objects/service-provider-capability.md; core-specs/objects/service-provider-contact.md; core-specs/objects/service-provider-status.md  
**Related Service Specs:** core-specs/services/service-provider-registration-service.md; core-specs/services/service-provider-profile-service.md; core-specs/services/service-provider-capability-service.md; core-specs/services/service-provider-contact-service.md; core-specs/services/service-provider-status-service.md; core-specs/services/service-provider-reference-validation-service.md  
**Related Event Specs:** core-specs/events/service-provider-created.md; core-specs/events/service-provider-updated.md; core-specs/events/service-provider-status-changed.md; core-specs/events/service-provider-capability-linked.md; core-specs/events/service-provider-agent-linked.md; core-specs/events/service-provider-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/service-provider/service-provider-contract.md; core-specs/contracts/service-provider/service-provider-profile-contract.md; core-specs/contracts/service-provider/service-provider-capability-contract.md; core-specs/contracts/service-provider/service-provider-agent-link-contract.md; core-specs/contracts/service-provider/service-provider-routing-eligibility-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Service Provider object defines the Core-recognized external or internal provider entity that can deliver, support or coordinate professional, operational, legal, technical, document, evidence, translation, filing or related trademark services in MarkOrbit.

It exists so that Agents, Routing, Matters, Orders, Tasks, Communications, Documents, Evidence, Jurisdictions, Service Network, AI Agents, Services, APIs and product consumers can consistently reference provider entities and capabilities without confusing Service Provider with Agent, Partner, Customer, Routing decision or Service Network.

Service Provider is required before:

```text
provider entity management
provider capability tracking
provider contact management
provider jurisdiction/service scope reference
agent-to-provider linkage
matter/provider collaboration
routing candidate input
service network mapping
provider communication
AI-assisted provider comparison
audit trace for provider-sensitive actions
```

---

# 2. Core Meaning

Service Provider means:

```text
a Core-recognized provider entity or profile that describes who can provide services, what capabilities they offer, which jurisdictions or scopes they support, and how they may participate in collaboration or routing.
```

Service Provider is not:

```text
Agent
Partner
Customer
Routing decision
Matter
Order
Communication
Service Network
Fee engine
Quality score engine
AI agent
```

Service Provider answers:

```text
Who is the service-providing entity?
Which capabilities and service scopes are available?
Which jurisdictions, languages or operational scopes are supported?
Which Agents, contacts or teams represent the provider?
Which Matters, Orders or Communications have involved the provider?
Can Routing consider this provider as candidate input?
What audit trace is required?
```

---

# 3. Object Category

Service Provider is a Collaboration Network Object owned by the Service Provider Domain.

It is the provider entity and capability profile.

Agent is the trademark-specific collaborator role.

Routing makes selection or recommendation decisions.

Partner is cooperation-side business relationship.

Service Provider must preserve these boundaries.

---

# 4. Architectural Position

Service Provider sits in the collaboration network layer.

```text
Matter requires external or internal service support
        ↓
Service Provider describes provider entity and capability
        ↓
Agent may represent trademark-specific collaborator role
        ↓
Routing evaluates candidates and recommends/selects
        ↓
Communication coordinates execution
        ↓
Matter and Task execute work
```

Service Provider supplies provider context and capability data.

Routing makes decisions.

Matter executes professional work.

---

# 5. Scope

The Service Provider object includes:

```text
service provider id
provider type
provider status
provider name/reference
profile reference
organization reference
contact references
agent references
capability references
jurisdiction coverage references
service scope references
language references
communication references
matter references
routing eligibility reference
service network reference
performance/reference metadata
source reference
created time
updated time
audit metadata
```

MVP / Phase 4 scope includes:

```text
service provider id
provider type
provider status
provider name/reference
profile reference
contact references
agent references
capability references
jurisdiction coverage references
service scope references
communication references
routing eligibility reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Service Provider ID. |
| provider_type | enum | Yes | Yes | LawFirm, Agency, TranslationProvider, DocumentProvider, EvidenceProvider, TechnologyProvider, InternalProvider, Other, Unknown. |
| name_reference | string | Yes | Yes | Human-readable provider name/reference. |
| status | enum | Yes | Yes | Controlled Service Provider status. |
| profile_reference_id | string | No | Partial | Provider profile reference. |
| organization_reference_id | string | No | Partial | Related Organization reference where applicable. |
| primary_contact_reference_id | string | No | Yes | Primary provider contact reference. |
| contact_references | array | No | Yes | Service Provider contact references. |
| agent_reference_ids | array | No | Yes | Related Agent references where applicable. |
| capability_references | array | No | Yes | Provider capability references. |
| jurisdiction_coverage_references | array | No | Yes | Jurisdiction coverage references. |
| service_scope_references | array | No | Yes | Supported service scope references. |
| language_references | array | No | Partial | Supported language references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| matter_reference_ids | array | No | Partial | Related Matter references. |
| order_reference_ids | array | No | Partial | Related Order references. |
| routing_eligibility_reference_id | string | No | Partial | Routing eligibility input reference. |
| service_network_reference_id | string | No | Deferred | Related Service Network reference. |
| performance_reference_id | string | No | Deferred | Performance reference; not scoring engine. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 provider_type

MVP controlled values:

```text
LawFirm
TrademarkAgency
TranslationProvider
DocumentProvider
EvidenceProvider
TechnologyProvider
ConsultingProvider
InternalProvider
Other
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
Blacklisted
Archived
DeletedReferenceOnly
```

## 7.3 capability_type

Suggested controlled values:

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
Recordal
Translation
DocumentPreparation
EvidenceReview
LocalAdvice
TechnicalIntegration
Other
Unknown
```

## 7.4 coverage_status

Suggested controlled values:

```text
Supported
Limited
ReviewRequired
Unsupported
Unknown
```

---

# 8. Object Rules

## 8.1 Service Provider Requires Name, Type and Status

Every Service Provider must define:

```text
provider_type
name_reference
status
```

A vendor note without type and status is not a Core-valid Service Provider.

## 8.2 Service Provider Is Not Agent

Service Provider is the provider entity and capability profile.

Agent is the trademark-specific collaborator role.

A Service Provider may have or reference Agents.

## 8.3 Service Provider Is Not Partner

Partner is cooperation-side business relationship.

Service Provider is provider entity/capability profile.

## 8.4 Service Provider Does Not Make Routing Decision

Service Provider provides candidate data and capability references.

Routing makes selection or recommendation decisions.

## 8.5 Service Provider Contact Is Not Automatically User

Provider contact data does not automatically create a User.

User linkage must be governed by User/Identity services.

## 8.6 Capability and Coverage Must Be Explicit

Provider capability, service scope and jurisdiction coverage should be explicit where routing eligibility or matter assignment depends on them.

## 8.7 Service Provider Must Be Auditable

Service Provider-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
service provider creation
profile update
status change
contact update
capability update
jurisdiction coverage update
agent linkage
routing eligibility update
service network linkage
communication linkage
AI provider summary or recommendation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Agent | Service Provider may include Agents | Agent remains trademark collaborator. |
| Jurisdiction | Provider may support jurisdictions | Jurisdiction remains procedural context. |
| Routing | Routing may evaluate Provider | Routing makes decision. |
| Matter | Provider may participate in Matter | Matter remains execution container. |
| Order | Provider may support Order execution indirectly | Order remains commercial request. |
| Communication | Provider may participate in Communication | Communication remains message lifecycle. |
| Document | Provider may prepare/provide Documents | Document remains artifact. |
| Evidence | Provider may review/provide Evidence | Evidence remains proof layer. |
| Task | Provider may be assignee/collaborator | Task remains work unit. |
| Partner | Partner may cooperate with Provider | Partner remains cooperation relationship. |
| Service Network | Provider may belong to network | Network remains ecosystem map. |
| AI Output | AI may summarize/recommend Provider | AI Output is not Routing decision. |
| Audit Record | Audit may reference Provider | Audit remains accountability system. |

---

# 10. Lifecycle

Service Provider lifecycle states:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
Blacklisted
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → ReviewRequired
Draft → Active
ReviewRequired → Active
ReviewRequired → Inactive
Active → ReviewRequired
Active → Suspended
Suspended → Active
Suspended → Inactive
Active → Inactive
Inactive → Active
Inactive → Archived
Blacklisted → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Blacklisted → Active without restoration/review and policy clearance
Archived → Active without restoration/review
DeletedReferenceOnly → Active state
```

---

# 11. Service Usage

Service Provider object is created and managed through:

```text
Service Provider Registration Service
Service Provider Profile Service
Service Provider Contact Service
Service Provider Status Service
Service Provider Capability Service
Service Provider Jurisdiction Coverage Service
Service Provider Agent Link Service
Service Provider Routing Eligibility Service
Service Provider Reference Validation Service
Service Provider Audit Reference Service
```

Service rules:

```text
- Services must validate provider_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not select provider for Matter by themselves.
- Services must not create Agent unless Agent service is invoked.
- Services must not create User automatically from provider contact.
- Services must preserve confidentiality and commercial policy.
```

---

# 12. Event Usage

Service Provider object emits or participates in:

```text
ServiceProviderCreated
ServiceProviderUpdated
ServiceProviderStatusChanged
ServiceProviderContactLinked
ServiceProviderCapabilityLinked
ServiceProviderCapabilityUpdated
ServiceProviderJurisdictionCoverageUpdated
ServiceProviderAgentLinked
ServiceProviderRoutingEligibilityUpdated
ServiceProviderCommunicationLinked
ServiceProviderArchived
ServiceProviderReferenceValidated
```

Event rules:

```text
- Service Provider events must reference Service Provider ID.
- Contact events must not expose sensitive contact details unnecessarily.
- Capability events must preserve service/jurisdiction reference.
- Agent link events must reference Agent ID.
- Routing eligibility events must not imply final Routing decision.
- AI-generated provider events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /service-providers
GET /service-providers/{id}
PATCH /service-providers/{id}
POST /service-providers/{id}/status
POST /service-providers/{id}/contacts
POST /service-providers/{id}/capabilities
POST /service-providers/{id}/jurisdictions
POST /service-providers/{id}/agents
POST /service-providers/reference/validate
```

API rules:

```text
- APIs must invoke Service Provider Services.
- APIs must not make Routing selection directly.
- APIs must not create Agent unless Agent service is invoked.
- APIs must not create User automatically from contact data.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Service Provider objects only under governed Agent Contracts.

Allowed AI use:

```text
summarize service provider profile
identify missing contact or capability data
identify jurisdiction or service scope gaps
compare candidate providers for review
prepare provider communication draft
flag inactive, suspended or review-required provider
suggest routing inputs for review
```

AI must not:

```text
make final Routing decision without Routing service
assign provider to Matter without governed service
create Agent automatically
create User from provider contact
expose confidential provider pricing or performance data outside authorized scope
blacklist or activate provider without authorized service
send provider communication without Communication service
```

AI Service Provider use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Service Provider Access Rule
Routing Rule where applicable
Communication Rule where applicable
Audit Rule
Human Review Rule for selection, blacklisting or external commitment
```

---

# 15. Validation Rules

Service Provider object must pass:

```text
[ ] id is present and immutable.
[ ] provider_type is controlled.
[ ] name_reference is present.
[ ] status is controlled.
[ ] Service Provider does not equal Agent.
[ ] Service Provider does not equal Partner.
[ ] Service Provider does not make Routing decision.
[ ] Service Provider Contact does not become User automatically.
[ ] Capability and jurisdiction coverage are explicit where routing eligibility is used.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite service-provider domain spec
preserve Service Provider / Agent boundary
preserve Service Provider / Partner boundary
preserve Service Provider / Routing boundary
preserve Service Provider / User boundary
implement only Phase 4 MVP fields unless task says otherwise
write tests for required name_reference
write tests for controlled provider_type
write tests for controlled status
write tests preventing Service Provider from making Routing decision
write tests preventing Service Provider Contact from becoming User automatically
write tests preventing Service Provider service from creating Agent automatically
write tests for explicit capability/jurisdiction coverage references
write tests for event emission on mutation
```

Codex must not:

```text
invent full vendor management or procurement system in Phase 4 MVP
treat Service Provider as Agent
treat Service Provider as Partner
treat Service Provider as Routing decision
create User automatically from Service Provider Contact
select Service Provider directly from provider object/service
store sensitive commercial terms by default
allow product UI to redefine Service Provider status
```

---

# 17. Acceptance Criteria

This Service Provider Object Specification is accepted only if:

```text
[ ] It defines Service Provider purpose.
[ ] It defines Service Provider Core meaning.
[ ] It identifies Service Provider as Collaboration Network Object.
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
| 0.1.0 | Draft | Initial Service Provider object specification. Establishes Service Provider as provider entity and capability profile, separates Service Provider from Agent, Partner, Routing, Customer and User, and defines Phase 4 MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
