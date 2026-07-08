# Event Specification — PartnerCreated

**Spec ID:** B02-EVT-PARTNER-CREATED  
**Spec Type:** Event  
**Event Name:** PartnerCreated  
**Event File:** core-specs/events/partner-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Partner  
**Producing Service:** core-specs/services/partner-service.md  
**Related Object Specs:** core-specs/objects/partner.md; core-specs/objects/customer.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/service-network.md; core-specs/objects/routing.md; core-specs/objects/communication.md; core-specs/objects/policy.md; core-specs/objects/permission.md  
**Related Service Specs:** core-specs/services/partner-service.md; core-specs/services/customer-service.md; core-specs/services/agent-service.md; core-specs/services/service-provider-service.md; core-specs/services/service-network-service.md; core-specs/services/routing-service.md; core-specs/services/communication-service.md; core-specs/services/policy-service.md; core-specs/services/permission-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/partner-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/partner-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/partner-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 5 — Reserved Collaboration Network  
**MVP Depth:** Reserved  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

PartnerCreated records that a governed Partner cooperation-side business relationship reference has been created by Partner Service.

It exists so that Customer, Agent, Service Provider, Service Network, Routing, Communication, Policy, Permission, AI Agents, APIs and product consumers can safely recognize that a cooperation-side relationship record now exists without treating that Partner as Customer, Agent, Service Provider, selected routing candidate, contracted supplier, payable vendor, settlement account, channel authorization, procurement approval or final cooperation decision.

PartnerCreated is required before:

```text
partner relationship trace
cooperation-side business context
partner-to-customer relationship review
partner-to-agent/service-provider mapping
service network relationship preparation
routing cooperation context
communication context preparation
AI-assisted partner profile enrichment review
policy-controlled partner visibility
API partner reference validation
audit trace for partner-sensitive actions
```

---

# 2. Event Meaning

PartnerCreated means:

```text
a stable Partner object reference has been created through governed Partner Service operation.
```

PartnerCreated does not mean:

```text
a Customer has been created
an Agent has been created
a Service Provider has been created
a Routing selection has been made
a Service Network membership has been approved
a contract has been formed
settlement or payment terms have been approved
channel authorization has been granted
AI-enriched partner data is verified business truth
```

PartnerCreated records cooperation-side relationship creation only.

It does not establish customer status, supplier status, routing selection, service network membership, settlement, payment, authorization or contractual commitment.

---

# 3. Event Category

PartnerCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Partner domain.

It is not a Customer event, Agent event, Service Provider event, Routing event or Service Network event.

---

# 4. Event Producer

Producing service:

```text
Partner Service
```

Producing operation:

```text
createPartner
```

Source domain:

```text
Partner
```

Source object type:

```text
Partner
```

Allowed producer path:

```text
API / Professional user / System / Migration / AI-assisted governed operation
        ↓
Partner Service createPartner
        ↓
Event Service record PartnerCreated
```

Producer rules:

```text
- PartnerCreated must be emitted only after Partner Service successfully creates the Partner reference.
- PartnerCreated must not be emitted directly by product UI.
- PartnerCreated must not be emitted directly by AI Agent outside governed service operation.
- PartnerCreated must not be emitted for failed, duplicate-rejected or unauthorized partner creation attempts.
```

---

# 5. Event Trigger

PartnerCreated is triggered when:

```text
Partner Service successfully creates a new Partner object and commits its stable partner_reference_id.
```

Required trigger conditions:

```text
createPartner operation completed
partner_reference_id created
partner_type validated
partner_status validated
cooperation context captured as references or safe summary
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Customer creation
Agent creation
Service Provider creation
Routing evaluation
Routing selection
Service Network mapping
communication received from external party
contract signing
settlement setup
payment setup
AI partner profile enrichment draft
failed validation
duplicate rejected Partner
```

Related but separate events may include:

```text
CustomerCreated
AgentCreated
ServiceProviderCreated
RoutingEvaluated
RoutingSelected
ServiceNetworkLinked
CommunicationCreated
PolicyEvaluated
PermissionEvaluated
PartnerVerified
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: PartnerCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Partner
source_service: Partner Service
source_operation: createPartner
source_object_type: Partner
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/partner-created-payload.md
safe_summary:
  partner_reference_id: string
  partner_type: string
  partner_status: string
  partner_source_type: string
  primary_relationship_type: string | null
restricted_fields_policy: PartnerCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
partner_reference_id: string
partner_type: string
partner_status: string
partner_source_type: string
primary_relationship_type: string | null
customer_reference_id: string | null
agent_reference_id: string | null
service_provider_reference_id: string | null
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
- Payload must use references and safe summaries rather than embedding confidential cooperation, settlement, pricing or contract terms by default.
- Payload must not include private personal data, bank/payment data, passwords, secrets or privileged cooperation records.
- Payload must not imply Customer, Agent, Service Provider or Service Network creation.
- Payload must not imply Routing selection, contract, settlement, payment approval or channel authorization.
- Payload must distinguish AI enrichment from verified Partner profile data.
- Payload must identify AI assistance where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
partner_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
customer_reference_id
agent_reference_id
service_provider_reference_id
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
- source_object_reference_id must equal partner_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- customer_reference_id must not imply Customer creation unless Customer Service emits CustomerCreated.
- agent_reference_id must not imply Agent creation unless Agent Service emits AgentCreated.
- service_provider_reference_id must not imply Service Provider creation unless Service Provider Service emits ServiceProviderCreated.
- service_network_reference_id must not imply network membership unless Service Network Service emits its own event.
- routing_reference_id must not imply selection unless Routing Service emits RoutingSelected.
- agent_contract_reference_id is required where AI assistance requires governance trace.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
PartnerCreated
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

## 8.4 partner_type

```text
AgencyPartner
ChannelPartner
ReferralPartner
BusinessPartner
PlatformPartner
ServicePartner
InternalPartner
Other
Unknown
```

## 8.5 partner_status

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

## 8.6 partner_source_type

```text
ProfessionalInput
CustomerContext
AgentContext
ServiceProviderContext
Referral
CommunicationDerived
SystemProcess
APIRequest
AIAssisted
Migration
ExternalIntegration
Unknown
```

## 8.7 primary_relationship_type

```text
Referral
Channel
Cooperation
Supplier
CustomerAgency
Platform
Internal
Other
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
PartnerCreated
ProfessionalCreated
ReferralCreated
CommunicationDerived
SystemGenerated
MigrationCreated
AIAssistedCreated
ReviewRequired
Unknown
```

---

# 9. Event Rules

## 9.1 PartnerCreated Records Cooperation Relationship Creation

PartnerCreated records that a Partner reference exists.

It must not be interpreted as customer creation, supplier approval, routing selection, contract formation, settlement setup or payment eligibility.

## 9.2 Partner Is Not Customer

Customer Service owns demand-side commercial party.

Partner may refer to a customer-side agency relationship, but PartnerCreated does not create Customer.

## 9.3 Partner Is Not Agent or Service Provider

Agent Service owns collaborator profile.

Service Provider Service owns provider entity/capability profile.

PartnerCreated does not create either automatically.

## 9.4 Partner Is Not Routing Selection

Routing Service owns evaluation and selection.

PartnerCreated may provide cooperation context, but it is not a selected routing candidate.

## 9.5 Partner Is Not Service Network Membership

Service Network Service owns network mapping.

PartnerCreated does not automatically join Partner into a Service Network.

## 9.6 Partner Is Not Settlement or Payment Approval

Settlement, payment, commission and finance rules are separate.

PartnerCreated must not be treated as payable setup.

## 9.7 AI Partner Enrichment Is Not Verified Fact

AI may enrich, normalize or summarize Partner data.

AI-enriched data must not become verified cooperation truth automatically.

## 9.8 PartnerCreated Must Respect Permission and Policy

Partner creation and visibility must respect Permission, Policy, privacy, confidentiality, settlement visibility and cooperation access context.

## 9.9 PartnerCreated Must Be Immutable

PartnerCreated must not be rewritten except controlled event metadata/status handled by Event Service.

---

# 10. Consumer Rules

Allowed consumers:

```text
Customer Service
Agent Service
Service Provider Service
Routing Service
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
- Customer Service may link Partner to Customer only through governed operation.
- Agent and Service Provider services may link Partner context only through governed operation.
- Routing Service may use Partner context but must not infer selection.
- Service Network Service may map Partner only through governed network operation.
- Communication Service may use Partner for participant/context under policy.
- Permission Service controls who may create, view or use Partner.
- Policy Service controls privacy, settlement visibility and AI use.
- AI Agents may enrich/summarize Partner data only under Agent Contract, Authorized Knowledge, Permission and Policy.
- Audit may preserve Partner creation trace.
```

Consumers must not:

```text
treat PartnerCreated as CustomerCreated
treat PartnerCreated as AgentCreated
treat PartnerCreated as ServiceProviderCreated
treat PartnerCreated as RoutingSelected
treat PartnerCreated as Service Network membership
treat PartnerCreated as contract, settlement or payment approval
treat AI-enriched partner profile as verified fact
expose restricted cooperation, pricing or settlement data
```

---

# 11. Relationship to Services

Producing service:

```text
Partner Service produces PartnerCreated after createPartner succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches PartnerCreated.
```

Related services:

```text
Customer Service may link Partner to demand-side customer context.
Agent Service may link Partner to collaborator profile.
Service Provider Service may link Partner to provider context.
Routing Service may use Partner context in selection reasoning.
Service Network Service may map Partner in network context.
Communication Service may link Partner to communication participants.
Policy Service controls visibility, privacy, settlement and AI use.
Permission Service controls who may create, view or use Partner.
Audit Service records accountability trace.
AI Agent Governance controls AI partner enrichment behavior.
```

Boundary reminders:

```text
Partner Service owns cooperation-side business relationship.
Customer Service owns demand-side commercial party.
Agent Service owns collaborator profile.
Service Provider Service owns provider entity/capability profile.
Routing Service owns candidate evaluation and selection.
Service Network Service owns network mapping.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /partners/{partner_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create PartnerCreated directly.
- API must call Partner Service createPartner, which emits the event.
- API must not expose restricted cooperation details, settlement terms, pricing, private personal data, cooperation history or bank/payment data by default.
- API must distinguish PartnerCreated from CustomerCreated, AgentCreated, ServiceProviderCreated, RoutingSelected and ServiceNetworkLinked.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a Partner reference was created
explain that Partner is not Customer, Agent, Service Provider or Routing selection
normalize safe partner profile fields where authorized
flag missing relationship type, verification or cooperation context for review
flag duplicate or conflicting partner candidates for human review
prepare audit-safe Partner creation summary
```

AI must not:

```text
fabricate PartnerCreated
rewrite PartnerCreated
delete PartnerCreated
treat PartnerCreated as contract, settlement, payment approval or channel authorization
treat PartnerCreated as Service Network membership
treat AI enrichment as verified partner fact
hide AI-assisted creation
expose restricted pricing, settlement, private or cooperation data
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

PartnerCreated is valid only if:

```text
[ ] event_name is PartnerCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Partner Service.
[ ] producing operation is createPartner.
[ ] source_domain is Partner.
[ ] source_object_type is Partner.
[ ] source_object_reference_id is present.
[ ] partner_reference_id is present.
[ ] source_object_reference_id equals partner_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] partner_type is controlled.
[ ] partner_status is controlled.
[ ] partner_source_type is controlled.
[ ] verification_status is controlled.
[ ] payload does not include restricted cooperation, settlement, pricing, payment, private personal or contract data unless allowed.
[ ] Customer, Agent, Service Provider, Routing selection, Service Network membership, contract, settlement and payment approval are not implied.
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
PartnerReferenceMissing
PartnerReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
PartnerTypeInvalid
PartnerStatusInvalid
PartnerSourceTypeInvalid
VerificationStatusInvalid
RestrictedFieldViolation
ConfidentialPartnerPayloadRejected
SettlementPayloadRestricted
PaymentDataPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownPartnerEventError
```

Rejection rules:

```text
- Failed Partner creation must not emit PartnerCreated.
- Duplicate rejected Partner creation must not emit PartnerCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Partner Service Specification
cite Partner Object Specification
cite Event Service Specification
cite Customer/Agent/Service Provider/Routing/Service Network specs where references are used
use exact event_name: PartnerCreated
use exact event_category: DomainEvent
validate partner_reference_id
validate source_object_reference_id equals partner_reference_id
validate actor_reference_id
validate controlled partner_type/status/source_type/verification_status
validate payload contract
write tests that failed createPartner does not emit PartnerCreated
write tests that PartnerCreated does not create Customer automatically
write tests that PartnerCreated does not create Agent automatically
write tests that PartnerCreated does not create Service Provider automatically
write tests that PartnerCreated does not imply Routing selection
write tests that PartnerCreated does not imply Service Network membership
write tests that PartnerCreated does not imply contract, settlement or payment approval
write tests that AI-assisted creation is marked where applicable
write tests that restricted cooperation/pricing/settlement/payment data is not exposed
```

Codex must not:

```text
emit PartnerCreated directly from UI
treat CustomerCreated as PartnerCreated
treat AgentCreated as PartnerCreated
treat ServiceProviderCreated as PartnerCreated
treat RoutingSelected as PartnerCreated
create Customer, Agent, Service Provider, Routing selection or Service Network membership silently from PartnerCreated
store private contact, settlement, payment, pricing or cooperation data in event payload by default
allow AI to fabricate PartnerCreated
use PartnerCreated as command to contract, settle, pay, route, verify or authorize channel status
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines PartnerCreated purpose.
[ ] It defines PartnerCreated meaning.
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
| 0.1.0 | Draft | Initial PartnerCreated Event specification. Defines governed Partner cooperation relationship creation event and separates PartnerCreated from Customer, Agent, Service Provider, Routing selection, Service Network membership, contract, settlement, payment approval and AI-enriched partner truth. |

---

**End of Event Specification**
