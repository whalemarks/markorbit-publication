# Object Specification — Partner

**Spec ID:** B02-OBJ-PARTNER  
**Spec Type:** Object  
**Object Name:** Partner  
**Owning Domain:** Partner  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/partner.md  
**Related Object Specs:** core-specs/objects/customer.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/routing.md; core-specs/objects/partner-profile.md; core-specs/objects/partner-contact.md; core-specs/objects/partner-relationship.md; core-specs/objects/partner-status.md  
**Related Service Specs:** core-specs/services/partner-registration-service.md; core-specs/services/partner-profile-service.md; core-specs/services/partner-contact-service.md; core-specs/services/partner-relationship-service.md; core-specs/services/partner-status-service.md; core-specs/services/partner-reference-validation-service.md  
**Related Event Specs:** core-specs/events/partner-created.md; core-specs/events/partner-updated.md; core-specs/events/partner-status-changed.md; core-specs/events/partner-contact-linked.md; core-specs/events/partner-relationship-updated.md; core-specs/events/partner-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/partner/partner-contract.md; core-specs/contracts/partner/partner-profile-contract.md; core-specs/contracts/partner/partner-contact-contract.md; core-specs/contracts/partner/partner-relationship-contract.md; core-specs/contracts/partner/partner-network-link-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 5 — Network Expansion Core  
**MVP Wave:** Wave 5  
**MVP Depth:** Reserved  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Partner object defines the Core-recognized cooperation-side business relationship used to represent organizations, agencies, channels, alliances or collaborators that participate in MarkOrbit’s broader service ecosystem.

It exists so that Service Network, Customers, Agents, Service Providers, Routing, Opportunities, Orders, Communications, AI Agents, Services, APIs and product consumers can consistently reference cooperation relationships without confusing Partner with Customer, Agent, Service Provider, Routing decision or Service Network.

Partner is required before:

```text
partner ecosystem mapping
agency/channel cooperation
referral relationship tracking
business alliance management
partner contact management
partner opportunity source tracking
service network mapping
partner-to-customer or partner-to-provider relationship modeling
AI-assisted partner summary
audit trace for cooperation-side relationships
```

---

# 2. Core Meaning

Partner means:

```text
a Core-recognized cooperation-side business relationship or ecosystem participant that may refer, collaborate, co-sell, coordinate, integrate or otherwise participate in service network activity.
```

Partner is not:

```text
Customer
Agent
Service Provider
Service Network
Routing decision
Matter
Order
Communication
User
Organization tenant
AI Output
```

Partner answers:

```text
Who is the cooperation-side relationship?
What type of partnership or cooperation exists?
Which contacts and relationship references apply?
Which Customers, Opportunities, Orders, Agents, Service Providers or Service Network nodes relate to it?
Is the partnership active, inactive, review-required or archived?
What audit trace is required?
```

---

# 3. Object Category

Partner is a Collaboration Network Object owned by the Partner Domain.

It is the cooperation-side relationship object.

Customer is demand-side commercial party.

Agent is trademark-specific collaborator.

Service Provider is provider entity and capability profile.

Service Network maps ecosystem structure.

Partner must preserve these boundaries.

---

# 4. Architectural Position

Partner sits in the broader collaboration network layer.

```text
Business cooperation relationship appears
        ↓
Partner records cooperation-side relationship
        ↓
Service Network maps ecosystem structure
        ↓
Opportunity / Order / Routing may reference Partner context
        ↓
Communication coordinates relationship
        ↓
Event and Audit preserve trace
```

Partner represents relationship.

Service Network maps ecosystem.

Routing makes selection decisions.

---

# 5. Scope

The Partner object includes:

```text
partner id
partner type
partner status
partner name/reference
partner profile reference
partner relationship reference
organization reference
contact references
service network reference
customer references
opportunity references
order references
agent references
service provider references
communication references
source reference
created time
updated time
audit metadata
```

Phase 5 reserved scope includes:

```text
partner id
partner type
partner status
partner name/reference
profile reference
relationship reference
contact references
service network reference
opportunity references
communication references
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Reserved | Stable immutable Partner ID. |
| partner_type | enum | Yes | Reserved | Controlled partner type. |
| name_reference | string | Yes | Reserved | Human-readable partner name/reference. |
| status | enum | Yes | Reserved | Controlled Partner status. |
| profile_reference_id | string | No | Reserved | Partner Profile reference. |
| relationship_reference_id | string | No | Reserved | Partner Relationship reference. |
| organization_reference_id | string | No | Reserved | Related Organization reference where applicable. |
| primary_contact_reference_id | string | No | Reserved | Primary Partner Contact reference. |
| contact_references | array | No | Reserved | Partner Contact references. |
| service_network_reference_id | string | No | Reserved | Related Service Network reference. |
| customer_reference_ids | array | No | Reserved | Related Customer references. |
| opportunity_reference_ids | array | No | Reserved | Related Opportunity references. |
| order_reference_ids | array | No | Reserved | Related Order references. |
| agent_reference_ids | array | No | Reserved | Related Agent references. |
| service_provider_reference_ids | array | No | Reserved | Related Service Provider references. |
| communication_reference_ids | array | No | Reserved | Related Communication references. |
| source_reference | string | No | Reserved | Intake/import/system source reference. |
| metadata | object | No | Reserved | Non-sensitive metadata only. |
| created_at | datetime | Yes | Reserved | Creation timestamp. |
| updated_at | datetime | Yes | Reserved | Last update timestamp. |
| created_by | string | No | Reserved | Identity or system actor reference. |
| updated_by | string | No | Reserved | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 partner_type

Phase 5 controlled values:

```text
ReferralPartner
ChannelPartner
AgencyPartner
TechnologyPartner
StrategicPartner
NetworkPartner
InternalPartner
Other
Unknown
```

## 7.2 status

Phase 5 controlled values:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
Archived
DeletedReferenceOnly
```

## 7.3 relationship_type

Suggested controlled values:

```text
Referral
Channel
Cooperation
StrategicAlliance
TechnologyIntegration
ServiceNetworkMember
InternalCooperation
Other
Unknown
```

---

# 8. Object Rules

## 8.1 Partner Requires Name, Type and Status

Every Partner must define:

```text
partner_type
name_reference
status
```

A cooperation note without type and status is not a Core-valid Partner.

## 8.2 Partner Is Not Customer

Customer is the demand-side commercial party.

Partner is cooperation-side relationship.

A Partner may refer, serve, represent or cooperate around Customers, but it is not Customer by default.

## 8.3 Partner Is Not Agent

Agent is trademark-specific external collaborator.

Partner is broader cooperation relationship.

## 8.4 Partner Is Not Service Provider

Service Provider is provider entity/capability profile.

Partner is relationship context.

## 8.5 Partner Is Not Service Network

Service Network maps ecosystem structure.

Partner may be a node or participant in Service Network.

## 8.6 Partner Is Phase 5 Reserved

Partner must not be implemented as MVP execution dependency unless explicitly approved.

Current use should remain reference/scaffold unless a Phase 5 task activates it.

## 8.7 Partner Must Be Auditable

Partner-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
partner creation
partner profile update
partner status change
contact update
relationship update
service network linkage
customer/opportunity/order linkage
agent/provider linkage
AI partner summary
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Customer | Partner may refer or cooperate around Customer | Customer remains demand-side party. |
| Opportunity | Partner may source Opportunity | Opportunity remains potential service need. |
| Order | Partner may be linked to Order context | Order remains commercial request. |
| Agent | Partner may cooperate with Agent | Agent remains trademark collaborator. |
| Service Provider | Partner may cooperate with Provider | Provider remains capability profile. |
| Service Network | Partner may belong to Service Network | Network remains ecosystem map. |
| Routing | Routing may consider Partner context | Routing makes decision. |
| Communication | Partner may participate in Communication | Communication remains message lifecycle. |
| Organization | Partner may reference Organization | Organization remains operating context. |
| AI Output | AI may summarize Partner | AI Output is not relationship truth. |
| Audit Record | Audit may reference Partner | Audit remains accountability system. |

---

# 10. Lifecycle

Partner lifecycle states:

```text
Draft
Active
ReviewRequired
Suspended
Inactive
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
Active → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration/review
DeletedReferenceOnly → Active state
Suspended → Active without policy clearance where required
```

---

# 11. Service Usage

Partner object is created and managed through:

```text
Partner Registration Service
Partner Profile Service
Partner Contact Service
Partner Relationship Service
Partner Status Service
Partner Service Network Link Service
Partner Reference Validation Service
Partner Audit Reference Service
```

Service rules:

```text
- Services must validate partner_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not create Customer, Agent or Service Provider automatically.
- Services must not make Routing decision.
- Services must not activate Phase 5 behavior in Phase 1–4 MVP without explicit task approval.
```

---

# 12. Event Usage

Partner object emits or participates in:

```text
PartnerCreated
PartnerUpdated
PartnerStatusChanged
PartnerContactLinked
PartnerRelationshipUpdated
PartnerServiceNetworkLinked
PartnerCustomerLinked
PartnerOpportunityLinked
PartnerAgentLinked
PartnerServiceProviderLinked
PartnerArchived
PartnerReferenceValidated
```

Event rules:

```text
- Partner events must reference Partner ID.
- Relationship events must preserve relationship type/source where allowed.
- Link events must reference related object IDs.
- Events must not imply Customer, Agent or Provider identity equivalence.
- AI-generated partner events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 5 APIs:

```text
POST /partners
GET /partners/{id}
PATCH /partners/{id}
POST /partners/{id}/status
POST /partners/{id}/contacts
POST /partners/{id}/relationships
POST /partners/{id}/service-network
POST /partners/reference/validate
```

API rules:

```text
- APIs must invoke Partner Services.
- APIs must not create Customer, Agent or Service Provider automatically.
- APIs must not make Routing selection directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Partner objects only under governed Agent Contracts.

Allowed AI use:

```text
summarize partner profile
identify missing relationship or contact data
suggest relationship classification for review
identify linked opportunity or service network context
prepare partner communication draft
flag inactive, suspended or review-required partner
suggest partner-related opportunity note for review
```

AI must not:

```text
create Customer, Agent or Service Provider automatically
make final partnership decision
change partner status without authorized service
make Routing decision based on Partner alone
expose confidential relationship data outside authorized scope
send partner communication without Communication service
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
Communication Rule where applicable
Service Network Rule where applicable
Audit Rule
Human Review Rule for relationship change or external commitment
```

---

# 15. Validation Rules

Partner object must pass:

```text
[ ] id is present and immutable.
[ ] partner_type is controlled.
[ ] name_reference is present.
[ ] status is controlled.
[ ] Partner does not equal Customer.
[ ] Partner does not equal Agent.
[ ] Partner does not equal Service Provider.
[ ] Partner does not equal Service Network.
[ ] Phase 5 Reserved boundary is preserved.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite partner domain spec
preserve Partner / Customer boundary
preserve Partner / Agent boundary
preserve Partner / Service Provider boundary
preserve Partner / Service Network boundary
preserve Phase 5 Reserved status
implement only scaffold/reference behavior unless Phase 5 task says otherwise
write tests for required name_reference
write tests for controlled partner_type
write tests for controlled status
write tests preventing Partner from creating Customer/Agent/Service Provider automatically
write tests preventing Partner from making Routing decision
write tests preserving Phase 5 reserved gate
write tests for event emission on mutation where implemented
```

Codex must not:

```text
invent full partner management system before Phase 5 approval
treat Partner as Customer
treat Partner as Agent
treat Partner as Service Provider
treat Partner as Service Network
activate partner workflow in Phase 1–4 MVP without explicit task
create downstream entities automatically from Partner
allow product UI to redefine Partner status
```

---

# 17. Acceptance Criteria

This Partner Object Specification is accepted only if:

```text
[ ] It defines Partner purpose.
[ ] It defines Partner Core meaning.
[ ] It identifies Partner as Collaboration Network Object.
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
| 0.1.0 | Draft | Initial Partner object specification. Establishes Partner as cooperation-side relationship object, separates Partner from Customer, Agent, Service Provider, Service Network and Routing, and preserves Phase 5 Reserved implementation boundary. |

---

**End of Object Specification**
