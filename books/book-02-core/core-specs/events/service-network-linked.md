# Event Specification — ServiceNetworkLinked

**Spec ID:** B02-EVT-SERVICE-NETWORK-LINKED  
**Spec Type:** Event  
**Event Name:** ServiceNetworkLinked  
**Event File:** core-specs/events/service-network-linked.md  
**Event Category:** LinkEvent  
**Owning Domain:** Service Network  
**Producing Service:** core-specs/services/service-network-service.md  
**Related Object Specs:** core-specs/objects/service-network.md; core-specs/objects/partner.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/routing.md; core-specs/objects/jurisdiction.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/service-network-service.md; core-specs/services/partner-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/routing-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/service-network-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/service-network-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/service-network-linked-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 5 — Reserved Collaboration Network  
**MVP Depth:** Reserved  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

ServiceNetworkLinked records that a governed Service Network relationship has been created between a Service Network and a target collaboration object.

It exists so that Partner, Agent, Service Provider, Routing, Jurisdiction, Communication, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a network relationship now exists without treating that link as Partner creation, Agent creation, Service Provider creation, Routing selection, verified service coverage, contract, settlement, payment approval or final cooperation decision.

ServiceNetworkLinked is required before:

```text
service network relationship trace
partner-to-network mapping
agent-to-network mapping
service-provider-to-network mapping
jurisdiction coverage mapping
routing network context
AI-assisted network enrichment review
policy-controlled network visibility
API service network reference validation
audit trace for network-sensitive actions
```

---

# 2. Event Meaning

ServiceNetworkLinked means:

```text
a stable Service Network relationship reference has been created through governed Service Network Service operation.
```

ServiceNetworkLinked does not mean:

```text
a Partner has been created
an Agent has been created
a Service Provider has been created
a Routing selection has been made
network membership is fully verified
jurisdiction coverage is verified
a contract has been formed
settlement or payment terms have been approved
AI-enriched network data is verified business truth
```

ServiceNetworkLinked records collaboration network mapping only.

It does not establish provider selection, contractual commitment, verified capability, payment, settlement or final cooperation approval.

---

# 3. Event Category

ServiceNetworkLinked is a:

```text
LinkEvent
```

It is a LinkEvent because it records a governed relationship between Service Network and another collaboration object.

It is not a Partner event, Agent event, Service Provider event or Routing event.

---

# 4. Event Producer

Producing service:

```text
Service Network Service
```

Producing operation:

```text
linkServiceNetwork
```

Source domain:

```text
Service Network
```

Source object type:

```text
ServiceNetworkLink
```

Allowed producer path:

```text
API / Professional user / System / Migration / AI-assisted governed operation
        ↓
Service Network Service linkServiceNetwork
        ↓
Event Service record ServiceNetworkLinked
```

Producer rules:

```text
- ServiceNetworkLinked must be emitted only after Service Network Service successfully creates the network link reference.
- ServiceNetworkLinked must not be emitted directly by product UI.
- ServiceNetworkLinked must not be emitted directly by AI Agent outside governed service operation.
- ServiceNetworkLinked must not be emitted for failed, duplicate-rejected or unauthorized network link attempts.
```

---

# 5. Event Trigger

ServiceNetworkLinked is triggered when:

```text
Service Network Service successfully links a Service Network reference to a target object and commits its stable service_network_link_reference_id.
```

Required trigger conditions:

```text
linkServiceNetwork operation completed
service_network_link_reference_id created
service_network_reference_id validated
target_object_type validated
target_object_reference_id validated
link_type validated
link_status validated
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Partner creation
Agent creation
Service Provider creation
Routing evaluation
Routing selection
Jurisdiction link
contract signing
settlement setup
payment setup
AI network enrichment draft
failed validation
duplicate rejected Service Network link
```

Related but separate events may include:

```text
PartnerCreated
AgentCreated
ServiceProviderCreated
RoutingEvaluated
RoutingSelected
JurisdictionLinked
PolicyEvaluated
PermissionEvaluated
ServiceNetworkVerified
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: ServiceNetworkLinked
event_category: LinkEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Service Network
source_service: Service Network Service
source_operation: linkServiceNetwork
source_object_type: ServiceNetworkLink
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/service-network-linked-payload.md
safe_summary:
  service_network_link_reference_id: string
  service_network_reference_id: string
  target_object_type: string
  target_object_reference_id: string
  link_type: string
  link_status: string
restricted_fields_policy: ServiceNetworkLinkedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
service_network_link_reference_id: string
service_network_reference_id: string
target_object_type: string
target_object_reference_id: string
link_type: string
link_status: string
jurisdiction_reference_ids: list[string]
partner_reference_id: string | null
agent_reference_id: string | null
service_provider_reference_id: string | null
routing_reference_id: string | null
linked_by_actor_reference_id: string
source_type: string
ai_assisted: boolean
agent_contract_reference_id: string | null
review_required: boolean
verification_status: string
```

Payload rules:

```text
- Payload must use references and safe summaries rather than embedding confidential network, pricing, settlement or cooperation details by default.
- Payload must not include private personal data, bank/payment data, passwords, secrets or privileged cooperation records.
- Payload must not imply Partner, Agent, Service Provider or Routing selection creation.
- Payload must not imply verified service coverage, contract, settlement or payment approval.
- Payload must distinguish AI enrichment from verified Service Network data.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
service_network_link_reference_id
service_network_reference_id
target_object_type
target_object_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
jurisdiction_reference_ids
partner_reference_id
agent_reference_id
service_provider_reference_id
routing_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal service_network_link_reference_id.
- service_network_reference_id must reference a valid governed Service Network.
- target_object_type and target_object_reference_id must be valid.
- partner_reference_id must not imply Partner creation unless Partner Service emits PartnerCreated.
- agent_reference_id must not imply Agent creation unless Agent Service emits AgentCreated.
- service_provider_reference_id must not imply Service Provider creation unless Service Provider Service emits ServiceProviderCreated.
- routing_reference_id must not imply Routing selection unless Routing Service emits RoutingSelected.
- jurisdiction_reference_ids must not imply verified coverage unless separately governed.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
ServiceNetworkLinked
```

## 8.2 event_category

```text
LinkEvent
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

## 8.4 target_object_type

```text
Partner
Agent
ServiceProvider
Routing
Jurisdiction
Communication
InternalTeam
Other
Unknown
```

## 8.5 link_type

```text
NetworkMembership
CoverageLink
CooperationLink
ReferralLink
CapabilityLink
JurisdictionCoverageLink
RoutingContextLink
InternalLink
ReferenceLink
Other
Unknown
```

## 8.6 link_status

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

## 8.7 source_type

```text
ProfessionalInput
PartnerContext
AgentContext
ServiceProviderContext
RoutingContext
JurisdictionContext
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.8 verification_status

```text
NotVerified
ReviewRequired
PartiallyVerified
Verified
Rejected
Expired
Unknown
```

## 8.9 reason_code

```text
ServiceNetworkLinked
ProfessionalLinked
PartnerLinked
AgentLinked
ServiceProviderLinked
RoutingContextLinked
JurisdictionCoverageLinked
SystemLinked
MigrationLinked
AIAssistedLinked
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 ServiceNetworkLinked Records Network Relationship

ServiceNetworkLinked records that a Service Network relationship exists.

It must not be interpreted as partner creation, agent creation, provider creation, routing selection, contract, settlement or payment setup.

## 9.2 Service Network Is Not Partner

Partner Service owns cooperation-side business relationship.

ServiceNetworkLinked may link Partner, but does not create or verify Partner.

## 9.3 Service Network Is Not Agent or Service Provider

Agent Service owns collaborator profile.

Service Provider Service owns provider entity/capability profile.

ServiceNetworkLinked does not create or verify either automatically.

## 9.4 Service Network Link Is Not Routing Selection

Routing Service owns evaluation and selection.

Network membership or coverage may inform routing but does not select a candidate.

## 9.5 Service Network Link Is Not Verified Coverage Automatically

Jurisdiction or capability coverage requires separate verification rules.

A network link alone is only mapping context.

## 9.6 Service Network Link Is Not Settlement or Payment Approval

Settlement, commission, payment and finance rules are separate.

ServiceNetworkLinked must not be treated as payable setup.

## 9.7 AI Network Enrichment Is Not Verified Fact

AI may enrich, normalize or summarize network mapping.

AI-enriched data must not become verified cooperation truth automatically.

## 9.8 ServiceNetworkLinked Must Respect Permission and Policy

Network linking and visibility must respect Permission, Policy, privacy, confidentiality, settlement visibility and cooperation access context.

## 9.9 ServiceNetworkLinked Must Be Immutable

ServiceNetworkLinked must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Partner Service
Agent Service
Service Provider Service
Routing Service
Jurisdiction Service
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
- Partner, Agent and Service Provider services may display network context but must not infer verification.
- Routing Service may use network link as context but must not infer selection.
- Jurisdiction Service may validate jurisdiction references but must not infer verified coverage.
- Communication Service may use network context under policy.
- Permission Service controls who may create, view or use Service Network links.
- Policy Service controls privacy, settlement visibility, network visibility and AI use.
- AI Agents may enrich/summarize Service Network data only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Service Network link trace.
```

Consumers must not:

```text
treat ServiceNetworkLinked as PartnerCreated
treat ServiceNetworkLinked as AgentCreated
treat ServiceNetworkLinked as ServiceProviderCreated
treat ServiceNetworkLinked as RoutingSelected
treat ServiceNetworkLinked as verified coverage
treat ServiceNetworkLinked as contract, settlement or payment approval
treat AI-enriched network data as verified fact
expose restricted network, pricing, settlement or cooperation data
```

---

# 11. Relationship to Services

Producing service:

```text
Service Network Service produces ServiceNetworkLinked after linkServiceNetwork succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches ServiceNetworkLinked.
```

Related services:

```text
Partner Service may use Service Network link for cooperation context.
Agent Service may use Service Network link for collaborator mapping.
Service Provider Service may use Service Network link for provider mapping.
Routing Service may use Service Network context in candidate evaluation.
Jurisdiction Service may validate jurisdiction coverage references.
Communication Service may link network context to conversations.
Policy Service controls visibility, privacy, settlement and AI use.
Permission Service controls who may create, view or use network links.
Audit Service records accountability trace.
AI Agent Governance controls AI network enrichment behavior.
```

Boundary reminders:

```text
Service Network Service owns collaboration ecosystem mapping.
Partner Service owns cooperation-side business relationship.
Agent Service owns collaborator profile.
Service Provider Service owns provider entity/capability profile.
Routing Service owns candidate evaluation and selection.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /service-network-links/{service_network_link_id}/events
GET /service-networks/{service_network_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create ServiceNetworkLinked directly.
- API must call Service Network Service linkServiceNetwork, which emits the event.
- API must not expose restricted cooperation details, settlement terms, pricing, private personal data, cooperation history or bank/payment data by default.
- API must distinguish ServiceNetworkLinked from PartnerCreated, AgentCreated, ServiceProviderCreated, RoutingSelected and verification events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Service Network relationship was linked
explain that Service Network link is not Partner/Agent/Provider creation or Routing selection
normalize safe network mapping fields where authorized
flag missing jurisdiction, capability, relationship type or verification data for review
flag duplicate or conflicting network links for human review
prepare audit-safe Service Network link summary
```

AI must not:

```text
fabricate ServiceNetworkLinked
rewrite ServiceNetworkLinked
delete ServiceNetworkLinked
treat ServiceNetworkLinked as contract, settlement, payment approval or routing selection
treat ServiceNetworkLinked as verified service coverage
treat AI enrichment as verified network fact
hide AI-assisted linking
expose restricted pricing, settlement, private or cooperation data
```

AI-assisted linking requires:

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

ServiceNetworkLinked is valid only if:

```text
[ ] event_name is ServiceNetworkLinked.
[ ] event_category is LinkEvent.
[ ] producing service is Service Network Service.
[ ] producing operation is linkServiceNetwork.
[ ] source_domain is Service Network.
[ ] source_object_type is ServiceNetworkLink.
[ ] source_object_reference_id is present.
[ ] service_network_link_reference_id is present.
[ ] source_object_reference_id equals service_network_link_reference_id.
[ ] service_network_reference_id is present and valid.
[ ] target_object_type is controlled.
[ ] target_object_reference_id is present and valid.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] link_type is controlled.
[ ] link_status is controlled.
[ ] verification_status is controlled.
[ ] payload does not include restricted cooperation, settlement, pricing, payment, private personal or contract data unless allowed.
[ ] Partner, Agent, Service Provider, Routing selection, verified coverage, contract, settlement and payment approval are not implied.
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
ServiceNetworkLinkReferenceMissing
ServiceNetworkLinkReferenceMismatch
ServiceNetworkReferenceMissing
ServiceNetworkReferenceInvalid
TargetObjectTypeInvalid
TargetObjectReferenceMissing
TargetObjectReferenceInvalid
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
LinkTypeInvalid
LinkStatusInvalid
VerificationStatusInvalid
RestrictedFieldViolation
ConfidentialServiceNetworkPayloadRejected
SettlementPayloadRestricted
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateLinkRejected
DuplicateEventRejected
UnknownServiceNetworkEventError
```

Rejection rules:

```text
- Failed Service Network link operation must not emit ServiceNetworkLinked.
- Unauthorized link attempt must not emit ServiceNetworkLinked.
- Duplicate rejected links must not emit ServiceNetworkLinked unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Service Network Service Specification
cite Service Network Object Specification
cite Event Service Specification
cite Partner/Agent/Service Provider/Routing specs where references are used
use exact event_name: ServiceNetworkLinked
use exact event_category: LinkEvent
validate service_network_link_reference_id
validate source_object_reference_id equals service_network_link_reference_id
validate service_network_reference_id
validate target_object_type and target_object_reference_id
validate actor_reference_id
validate controlled link_type/status/source_type/verification_status
validate payload contract
write tests that failed linkServiceNetwork does not emit ServiceNetworkLinked
write tests that ServiceNetworkLinked does not create Partner automatically
write tests that ServiceNetworkLinked does not create Agent automatically
write tests that ServiceNetworkLinked does not create Service Provider automatically
write tests that ServiceNetworkLinked does not imply Routing selection
write tests that ServiceNetworkLinked does not imply verified coverage
write tests that ServiceNetworkLinked does not imply contract, settlement or payment approval
write tests that AI-assisted linking is marked where applicable
write tests that restricted cooperation/pricing/settlement/payment data is not exposed
```

Codex must not:

```text
emit ServiceNetworkLinked directly from UI
treat PartnerCreated as ServiceNetworkLinked
treat AgentCreated as ServiceNetworkLinked
treat ServiceProviderCreated as ServiceNetworkLinked
treat RoutingSelected as ServiceNetworkLinked
create Partner, Agent, Service Provider or Routing selection silently from ServiceNetworkLinked
store private contact, settlement, payment, pricing or cooperation data in event payload by default
allow AI to fabricate ServiceNetworkLinked
use ServiceNetworkLinked as command to contract, settle, pay, route, verify or authorize network coverage
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines ServiceNetworkLinked purpose.
[ ] It defines ServiceNetworkLinked meaning.
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
| 0.1.0 | Draft | Initial ServiceNetworkLinked Event specification. Defines governed Service Network relationship link event and separates ServiceNetworkLinked from Partner, Agent, Service Provider, Routing selection, verified coverage, contract, settlement, payment approval and AI-enriched network truth. |

---

**End of Event Specification**
