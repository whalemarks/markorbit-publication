# Event Specification — AgentCreated

**Spec ID:** B02-EVT-AGENT-CREATED  
**Spec Type:** Event  
**Event Name:** AgentCreated  
**Event File:** core-specs/events/agent-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Agent  
**Producing Service:** core-specs/services/agent-service.md  
**Related Object Specs:** core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/routing.md; core-specs/objects/partner.md; core-specs/objects/service-network.md; core-specs/objects/communication.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/routing-service.md; core-specs/services/partner-service.md; core-specs/services/service-network-service.md; core-specs/services/communication-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/agent-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/agent-profile-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/agent-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 4 — Collaboration and Network Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

AgentCreated records that a governed Agent collaborator profile reference has been created by Agent Service.

It exists so that Service Provider, Routing, Partner, Service Network, Communication, Matter, Order, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that an external trademark collaborator profile now exists without treating that Agent as Service Provider, Partner, selected routing candidate, contracted supplier, payable vendor, authorized representative, professional qualification approval or final cooperation decision.

AgentCreated is required before:

```text
external collaborator profile trace
agent contact and capability preparation
service provider relationship review
routing candidate preparation
service network mapping
communication context preparation
AI-assisted agent profile enrichment review
policy-controlled agent visibility
API agent reference validation
audit trace for agent-sensitive actions
```

---

# 2. Event Meaning

AgentCreated means:

```text
a stable Agent object reference has been created through governed Agent Service operation.
```

AgentCreated does not mean:

```text
a Service Provider has been created
a Partner has been created
the Agent has been selected by Routing
the Agent is contracted or payable
the Agent is legally authorized as representative
the Agent capability has been verified
the Agent quality has been approved
the Agent belongs to a Service Network automatically
AI-enriched profile data is verified professional truth
```

AgentCreated records external collaborator profile creation only.

It does not establish service provider status, routing selection, contractual relationship, authority, verification or payment eligibility.

---

# 3. Event Category

AgentCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Agent domain.

It is not a Service Provider event, Partner event, Routing event or Service Network event.

---

# 4. Event Producer

Producing service:

```text
Agent Service
```

Producing operation:

```text
createAgent
```

Source domain:

```text
Agent
```

Source object type:

```text
Agent
```

Allowed producer path:

```text
API / Professional user / System / Migration / AI-assisted governed operation
        ↓
Agent Service createAgent
        ↓
Event Service record AgentCreated
```

Producer rules:

```text
- AgentCreated must be emitted only after Agent Service successfully creates the Agent reference.
- AgentCreated must not be emitted directly by product UI.
- AgentCreated must not be emitted directly by AI Agent outside governed service operation.
- AgentCreated must not be emitted for failed, duplicate-rejected or unauthorized agent creation attempts.
```

---

# 5. Event Trigger

AgentCreated is triggered when:

```text
Agent Service successfully creates a new Agent object and commits its stable agent_reference_id.
```

Required trigger conditions:

```text
createAgent operation completed
agent_reference_id created
agent_type validated
agent_status validated
contact/profile context captured as references or safe summary
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Service Provider creation
Partner creation
Routing evaluation
Routing selection
communication received from external contact
agent capability verification
contract signing
payment setup
AI profile enrichment draft
failed validation
duplicate rejected Agent
```

Related but separate events may include:

```text
ServiceProviderCreated
PartnerCreated
RoutingEvaluated
RoutingSelected
CommunicationCreated
ServiceNetworkLinked
PolicyEvaluated
PermissionEvaluated
AgentVerified
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: AgentCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Agent
source_service: Agent Service
source_operation: createAgent
source_object_type: Agent
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/agent-created-payload.md
safe_summary:
  agent_reference_id: string
  agent_type: string
  agent_status: string
  primary_jurisdiction_reference_id: string | null
  source_type: string
restricted_fields_policy: AgentCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
agent_reference_id: string
agent_type: string
agent_status: string
agent_source_type: string
primary_jurisdiction_reference_id: string | null
service_provider_reference_id: string | null
partner_reference_id: string | null
service_network_reference_id: string | null
communication_reference_ids: list[string]
created_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
verification_status: string
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding confidential contact, pricing or cooperation details by default.
- Payload must not include private personal data, bank/payment data, passwords, secrets or privileged cooperation records.
- Payload must not imply Service Provider creation, Partner creation, Routing selection, contract status, payment eligibility or authorization.
- Payload must distinguish AI enrichment from verified Agent profile data.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
agent_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
primary_jurisdiction_reference_id
service_provider_reference_id
partner_reference_id
service_network_reference_id
communication_reference_ids
routing_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal agent_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- service_provider_reference_id must not imply Service Provider creation unless Service Provider Service emits ServiceProviderCreated.
- partner_reference_id must not imply Partner creation unless Partner Service emits PartnerCreated.
- routing_reference_id must not imply selection unless Routing Service emits routing selection event.
- communication_reference_ids must not imply contract or authority.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
AgentCreated
```

## 8.2 event_category

```text
DomainEvent
```

## 8.3 event_status

```text
Recorded
Validated
DispatchPending
Dispatched
DispatchFailed
Consumed
Ignored
Archived
DeletedReferenceOnly
```

## 8.4 agent_type

```text
ForeignTrademarkAgent
DomesticTrademarkAgent
LawFirmContact
IndividualAttorney
ParalegalContact
GovernmentLiaison
TranslationAgent
SearchAgent
FilingAgent
Other
Unknown
```

## 8.5 agent_status

```text
Draft
Active
ReviewRequired
PendingVerification
Verified
Suspended
Inactive
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 agent_source_type

```text
ProfessionalInput
CommunicationDerived
Referral
PublicSource
ServiceProviderContext
PartnerContext
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 verification_status

```text
NotVerified
ReviewRequired
PartiallyVerified
Verified
Rejected
Expired
Unknown
```

## 8.8 reason_code

```text
AgentCreated
ProfessionalCreated
CommunicationDerived
ReferralCreated
PublicSourceCreated
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 AgentCreated Records Collaborator Profile Creation

AgentCreated records that an Agent reference exists.

It must not be interpreted as service provider approval, routing selection, contract formation, authority or payment eligibility.

## 9.2 Agent Is Not Service Provider

Service Provider Service owns provider entity and capability profile.

Agent may be a contact or collaborator profile, but AgentCreated does not create Service Provider.

## 9.3 Agent Is Not Partner

Partner Service owns cooperation-side business relationship.

AgentCreated does not create Partner relationship or commercial cooperation agreement.

## 9.4 Agent Is Not Routing Selection

Routing Service owns evaluation, recommendation and selection.

AgentCreated may feed candidate data, but selection must be governed separately.

## 9.5 Agent Profile Is Not Verification

AgentCreated may create a profile in PendingVerification or ReviewRequired state.

Verified status requires governed verification rules.

## 9.6 AI Profile Enrichment Is Not Verified Fact

AI may enrich, normalize or summarize Agent data.

AI-enriched data must not become verified professional fact automatically.

## 9.7 AgentCreated Must Respect Permission and Policy

Agent creation and visibility must respect Permission, Policy, privacy, confidentiality and cooperation access context.

## 9.8 AgentCreated Must Be Immutable

AgentCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Service Provider Service
Routing Service
Partner Service
Service Network Service
Communication Service
Matter Service
Order Service
Policy Service
Permission Service
AI Agent Governance
Audit Service
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Service Provider Service may link Agent to provider context only through governed operation.
- Routing Service may use Agent as candidate data but must not infer selection.
- Partner Service may use Agent context but must not infer Partner relationship.
- Service Network Service may map Agent but must not infer service coverage approval.
- Communication Service may use Agent for participant context under policy.
- AI Agents may enrich/summarize Agent data only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Agent creation trace.
```

Consumers must not:

```text
treat AgentCreated as ServiceProviderCreated
treat AgentCreated as PartnerCreated
treat AgentCreated as RoutingSelected
treat AgentCreated as contract, authority or payment approval
treat AI-enriched profile as verified fact
expose restricted contact, pricing or cooperation data
```

---

# 11. Relationship to Services

Producing service:

```text
Agent Service produces AgentCreated after createAgent succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches AgentCreated.
```

Related services:

```text
Service Provider Service may link Agent to provider profile.
Routing Service may evaluate Agent as candidate input.
Partner Service may reference Agent in cooperation context.
Service Network Service may map Agent in network context.
Communication Service may link Agent to communication participants.
Policy Service controls visibility, privacy and AI use.
Permission Service controls who may create, view or use Agent.
Audit Service records accountability trace.
AI Agent Governance controls AI profile enrichment behavior.
```

Boundary reminders:

```text
Agent Service owns collaborator profile.
Service Provider Service owns provider entity/capability profile.
Partner Service owns cooperation relationship.
Routing Service owns candidate evaluation and selection.
Service Network Service owns network mapping.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /agents/{agent_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create AgentCreated directly.
- API must call Agent Service createAgent, which emits the event.
- API must not expose restricted contact details, pricing, private personal data, cooperation history or bank/payment data by default.
- API must distinguish AgentCreated from ServiceProviderCreated, PartnerCreated, RoutingSelected and verification events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Agent reference was created
explain that Agent is not Service Provider, Partner or Routing selection
normalize safe profile fields where authorized
flag missing jurisdiction, service scope or verification data for review
flag duplicate or conflicting profile candidates for human review
prepare audit-safe Agent creation summary
```

AI must not:

```text
fabricate AgentCreated
rewrite AgentCreated
delete AgentCreated
treat AgentCreated as verified capability
treat AgentCreated as contract, authority or routing selection
treat AI enrichment as verified profile fact
hide AI-assisted creation
expose restricted contact, pricing, private or cooperation data
```

AI-assisted creation requires:

```text
agent_identity_reference_id
agent_contract_reference_id
authorized_knowledge_reference where applicable
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

AgentCreated is valid only if:

```text
[ ] event_name is AgentCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Agent Service.
[ ] producing operation is createAgent.
[ ] source_domain is Agent.
[ ] source_object_type is Agent.
[ ] source_object_reference_id is present.
[ ] agent_reference_id is present.
[ ] source_object_reference_id equals agent_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] agent_type is controlled.
[ ] agent_status is controlled.
[ ] agent_source_type is controlled.
[ ] verification_status is controlled.
[ ] payload does not include restricted contact, pricing, payment, private personal or cooperation data unless allowed.
[ ] Service Provider, Partner, Routing selection, contract, authority and payment eligibility are not implied.
[ ] AI assistance is explicitly identified where applicable.
[ ] event is not used as command.
```

---

# 15. Error / Rejection Handling

Controlled rejection reasons:

```text
EventNameInvalid
EventCategoryInvalid
ProducingServiceMissing
ProducingOperationMissing
SourceObjectMissing
AgentReferenceMissing
AgentReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
AgentTypeInvalid
AgentStatusInvalid
AgentSourceTypeInvalid
VerificationStatusInvalid
RestrictedFieldViolation
ConfidentialAgentPayloadRejected
PrivateContactPayloadRejected
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownAgentEventError
```

Rejection rules:

```text
- Failed Agent creation must not emit AgentCreated.
- Duplicate rejected Agent creation must not emit AgentCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Agent Service Specification
cite Agent Object Specification
cite Event Service Specification
cite Service Provider/Routing/Partner specs where references are used
use exact event_name: AgentCreated
use exact event_category: DomainEvent
validate agent_reference_id
validate source_object_reference_id equals agent_reference_id
validate actor_reference_id
validate controlled agent_type/status/source_type/verification_status
validate payload contract
write tests that failed createAgent does not emit AgentCreated
write tests that AgentCreated does not create Service Provider automatically
write tests that AgentCreated does not create Partner automatically
write tests that AgentCreated does not imply Routing selection
write tests that AgentCreated does not imply verification, contract, authority or payment eligibility
write tests that AI-assisted creation is marked where applicable
write tests that restricted contact/pricing/payment/cooperation data is not exposed
```

Codex must not:

```text
emit AgentCreated directly from UI
treat ServiceProviderCreated as AgentCreated
treat PartnerCreated as AgentCreated
treat RoutingSelected as AgentCreated
create Service Provider, Partner or Routing selection silently from AgentCreated
store private contact, payment, pricing or cooperation data in event payload by default
allow AI to fabricate AgentCreated
use AgentCreated as command to contract, route, pay, verify or authorize representative status
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines AgentCreated purpose.
[ ] It defines AgentCreated meaning.
[ ] It defines Event category.
[ ] It defines producer and trigger.
[ ] It defines payload contract.
[ ] It defines required references.
[ ] It defines controlled values.
[ ] It defines event rules.
[ ] It defines consumer rules.
[ ] It defines service relationships.
[ ] It defines API relationships.
[ ] It defines AI Agent constraints.
[ ] It defines validation rules.
[ ] It defines error/rejection handling.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial AgentCreated Event specification. Defines governed Agent collaborator profile creation event and separates AgentCreated from Service Provider, Partner, Routing selection, verification, contract, authority, payment eligibility and AI-enriched profile truth. |

---

**End of Event Specification**
