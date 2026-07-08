# Object Specification — Agent

**Spec ID:** B02-OBJ-AGENT  
**Spec Type:** Object  
**Object Name:** Agent  
**Owning Domain:** Agent  
**Domain Category:** Collaboration Network Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/agent.md  
**Related Object Specs:** core-specs/objects/service-provider.md; core-specs/objects/routing.md; core-specs/objects/communication.md; core-specs/objects/agent-profile.md; core-specs/objects/agent-contact.md; core-specs/objects/agent-capability.md; core-specs/objects/agent-jurisdiction-coverage.md; core-specs/objects/agent-status.md  
**Related Service Specs:** core-specs/services/agent-registration-service.md; core-specs/services/agent-profile-service.md; core-specs/services/agent-contact-service.md; core-specs/services/agent-capability-service.md; core-specs/services/agent-status-service.md; core-specs/services/agent-reference-validation-service.md  
**Related Event Specs:** core-specs/events/agent-created.md; core-specs/events/agent-updated.md; core-specs/events/agent-status-changed.md; core-specs/events/agent-capability-linked.md; core-specs/events/agent-jurisdiction-coverage-updated.md; core-specs/events/agent-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/agent/agent-contract.md; core-specs/contracts/agent/agent-profile-contract.md; core-specs/contracts/agent/agent-contact-contract.md; core-specs/contracts/agent/agent-capability-contract.md; core-specs/contracts/agent/agent-routing-eligibility-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Execution Extension Core  
**MVP Wave:** Wave 4  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Agent object defines the Core-recognized external trademark collaborator that may support trademark filing, prosecution, renewal, change, assignment, opposition, cancellation, evidence review, document handling, local advice or other professional services in one or more jurisdictions.

It exists so that Service Providers, Routing, Matters, Orders, Communications, Documents, Evidence, Jurisdictions, Tasks, AI Agents, Services, APIs and product consumers can consistently reference trademark collaborators without confusing Agent with Service Provider entity, Partner relationship, Customer, Routing decision or Communication record.

Agent is required before:

```text
foreign associate management
jurisdiction-based collaborator records
agent contact management
agent capability tracking
agent fee/service capability reference
agent communication
matter assignment to external collaborator
routing eligibility
agent performance review
AI-assisted agent selection explanation
audit trace for external collaboration
```

---

# 2. Core Meaning

Agent means:

```text
a Core-recognized external trademark collaborator profile that describes trademark-related service capability, jurisdiction coverage, contact references, status and routing eligibility inputs.
```

Agent is not:

```text
Service Provider
Partner
Customer
User
Routing decision
Matter
Order
Communication
Fee engine
Quality score engine
AI agent
```

Agent answers:

```text
Who is the external trademark collaborator?
Which jurisdictions and services can they support?
Which contacts and communication channels are available?
Which Service Provider entity may they belong to or represent?
Which Matters, Orders or Communications have involved them?
Are they active, inactive, review-required or archived?
Can Routing consider them as candidate input?
What audit trace is required?
```

---

# 3. Object Category

Agent is a Collaboration Network Object owned by the Agent Domain.

It is the trademark-specific collaborator role/profile.

Service Provider is the provider entity and capability profile.

Routing makes selection or recommendation decisions.

Agent must preserve these boundaries.

---

# 4. Architectural Position

Agent sits in the collaboration network layer.

```text
Matter requires external/local support
        ↓
Jurisdiction and service scope define need
        ↓
Agent provides trademark collaborator profile
        ↓
Service Provider may provide broader provider entity context
        ↓
Routing evaluates candidates and recommends/selects
        ↓
Communication coordinates execution
```

Agent supplies candidate data.

Routing makes decisions.

Matter executes professional work.

---

# 5. Scope

The Agent object includes:

```text
agent id
agent type
agent status
agent name/reference
service provider reference
organization reference
contact references
jurisdiction coverage references
service capability references
language references
communication references
matter references
order references
routing eligibility reference
performance/reference metadata
source reference
created time
updated time
audit metadata
```

MVP / Phase 4 scope includes:

```text
agent id
agent type
agent status
agent name/reference
service provider reference
contact references
jurisdiction coverage references
service capability references
communication references
matter references
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
| id | string | Yes | Yes | Stable immutable Agent ID. |
| agent_type | enum | Yes | Yes | IndividualAgent, LawFirmAgent, AgencyAgent, InternalAgent, Unknown. |
| name_reference | string | Yes | Yes | Human-readable agent name/reference. |
| status | enum | Yes | Yes | Controlled Agent status. |
| service_provider_reference_id | string | No | Yes | Related Service Provider reference where applicable. |
| organization_reference_id | string | No | Partial | Related Organization reference where applicable. |
| primary_contact_reference_id | string | No | Yes | Primary Agent Contact reference. |
| contact_references | array | No | Yes | Agent contact references. |
| jurisdiction_coverage_references | array | No | Yes | Jurisdiction coverage references. |
| service_capability_references | array | No | Yes | Service capability references. |
| language_references | array | No | Partial | Supported language references. |
| communication_reference_ids | array | No | Partial | Related Communication references. |
| matter_reference_ids | array | No | Partial | Related Matter references. |
| order_reference_ids | array | No | Partial | Related Order references. |
| routing_eligibility_reference_id | string | No | Partial | Routing eligibility input reference. |
| performance_reference_id | string | No | Deferred | Performance reference; not scoring engine. |
| source_reference | string | No | Yes | Intake/import/system source reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 agent_type

MVP controlled values:

```text
IndividualAgent
LawFirmAgent
AgencyAgent
InternalAgent
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

## 7.3 service_capability_type

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
EvidenceReview
DocumentReview
LocalAdvice
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

## 8.1 Agent Requires Name, Type and Status

Every Agent must define:

```text
agent_type
name_reference
status
```

An external collaborator note without type and status is not a Core-valid Agent.

## 8.2 Agent Is Not Service Provider

Agent is trademark-specific collaborator role/profile.

Service Provider is broader provider entity and capability profile.

An Agent may reference a Service Provider, but they are not the same object.

## 8.3 Agent Is Not Partner

Partner is cooperation-side business relationship.

Agent is external trademark collaborator.

## 8.4 Agent Does Not Make Routing Decision

Agent provides routing inputs such as jurisdiction coverage, service capability and contact data.

Routing makes selection or recommendation decisions.

## 8.5 Agent Contact Is Not Automatically User

Agent Contact may be linked to communication or external identity references.

It does not automatically become User.

## 8.6 Agent Capability Must Be Explicit

Jurisdiction coverage and service capability should be represented as explicit references.

Free text notes should not be the only capability source where routing eligibility is involved.

## 8.7 Agent Must Be Auditable

Agent-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
agent creation
agent profile update
agent status change
contact update
service capability update
jurisdiction coverage update
routing eligibility update
service provider linkage
communication linkage
AI agent summary or recommendation
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Service Provider | Agent may reference provider entity | Service Provider remains entity/profile. |
| Jurisdiction | Agent may support jurisdictions | Jurisdiction remains procedural context. |
| Routing | Routing may evaluate Agent | Routing makes decision. |
| Matter | Agent may participate in Matter | Matter remains execution container. |
| Order | Agent may support Order execution indirectly | Order remains commercial request. |
| Communication | Agent may participate in Communication | Communication remains message lifecycle. |
| Document | Agent may provide/request Documents | Document remains artifact. |
| Evidence | Agent may provide/review Evidence | Evidence remains proof layer. |
| Task | Agent may be task assignee/collaborator | Task remains work unit. |
| Partner | Partner may refer or cooperate with Agent | Partner remains cooperation relationship. |
| AI Output | AI may summarize/recommend Agent | AI Output is not Routing decision. |
| Audit Record | Audit may reference Agent | Audit remains accountability system. |

---

# 10. Lifecycle

Agent lifecycle states:

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

Agent object is created and managed through:

```text
Agent Registration Service
Agent Profile Service
Agent Contact Service
Agent Status Service
Agent Capability Service
Agent Jurisdiction Coverage Service
Agent Service Provider Link Service
Agent Routing Eligibility Service
Agent Reference Validation Service
Agent Audit Reference Service
```

Service rules:

```text
- Services must validate agent_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not select Agent for Matter by themselves.
- Services must not create Service Provider unless Service Provider service is invoked.
- Services must not create User automatically from Agent Contact.
- Services must preserve confidentiality and commercial policy.
```

---

# 12. Event Usage

Agent object emits or participates in:

```text
AgentCreated
AgentUpdated
AgentStatusChanged
AgentContactLinked
AgentCapabilityLinked
AgentCapabilityUpdated
AgentJurisdictionCoverageUpdated
AgentServiceProviderLinked
AgentRoutingEligibilityUpdated
AgentCommunicationLinked
AgentArchived
AgentReferenceValidated
```

Event rules:

```text
- Agent events must reference Agent ID.
- Contact events must not expose sensitive contact details unnecessarily.
- Capability events must preserve service/jurisdiction reference.
- Routing eligibility events must not imply final Routing decision.
- AI-generated agent events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 4 APIs:

```text
POST /agents
GET /agents/{id}
PATCH /agents/{id}
POST /agents/{id}/status
POST /agents/{id}/contacts
POST /agents/{id}/capabilities
POST /agents/{id}/jurisdictions
POST /agents/{id}/service-provider
POST /agents/reference/validate
```

API rules:

```text
- APIs must invoke Agent Services.
- APIs must not make Routing selection directly.
- APIs must not create Service Provider unless Service Provider service is invoked.
- APIs must not create User automatically from contact data.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Agent objects only under governed Agent Contracts.

Allowed AI use:

```text
summarize agent profile
identify missing contact or capability data
identify jurisdiction coverage gaps
compare candidate agents for review
prepare agent communication draft
flag inactive, suspended or review-required agent
suggest routing inputs for review
```

AI must not:

```text
make final Routing decision without Routing service
assign Agent to Matter without governed service
create Service Provider automatically
create User from Agent Contact
expose confidential agent pricing or performance data outside authorized scope
blacklist or activate Agent without authorized service
send agent communication without Communication service
```

AI Agent-object use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Agent Object Access Rule
Routing Rule where applicable
Communication Rule where applicable
Audit Rule
Human Review Rule for selection, blacklisting or external commitment
```

---

# 15. Validation Rules

Agent object must pass:

```text
[ ] id is present and immutable.
[ ] agent_type is controlled.
[ ] name_reference is present.
[ ] status is controlled.
[ ] Agent does not equal Service Provider.
[ ] Agent does not equal Partner.
[ ] Agent does not make Routing decision.
[ ] Agent Contact does not become User automatically.
[ ] Jurisdiction coverage and service capability are explicit where routing eligibility is used.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite agent domain spec
preserve Agent / Service Provider boundary
preserve Agent / Partner boundary
preserve Agent / Routing boundary
preserve Agent / User boundary
implement only Phase 4 MVP fields unless task says otherwise
write tests for required name_reference
write tests for controlled agent_type
write tests for controlled status
write tests preventing Agent from making Routing decision
write tests preventing Agent Contact from becoming User automatically
write tests preventing Agent service from creating Service Provider automatically
write tests for explicit capability/jurisdiction coverage references
write tests for event emission on mutation
```

Codex must not:

```text
invent full vendor management system in Phase 4 MVP
treat Agent as Service Provider
treat Agent as Partner
treat Agent as Routing decision
create User automatically from Agent Contact
select Agent directly from Agent object/service
store sensitive commercial terms by default
allow product UI to redefine Agent status
```

---

# 17. Acceptance Criteria

This Agent Object Specification is accepted only if:

```text
[ ] It defines Agent purpose.
[ ] It defines Agent Core meaning.
[ ] It identifies Agent as Collaboration Network Object.
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
| 0.1.0 | Draft | Initial Agent object specification. Establishes Agent as external trademark collaborator, separates Agent from Service Provider, Partner, Routing, Customer and User, and defines Phase 4 MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
