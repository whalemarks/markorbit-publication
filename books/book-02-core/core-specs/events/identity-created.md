# Event Specification — IdentityCreated

**Spec ID:** B02-EVT-IDENTITY-CREATED  
**Spec Type:** Event  
**Event Name:** IdentityCreated  
**Event File:** core-specs/events/identity-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** Identity  
**Producing Service:** core-specs/services/identity-service.md  
**Related Object Specs:** core-specs/objects/identity.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/identity-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/identity-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/identity-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

IdentityCreated records that a governed Identity reference has been created by Identity Service.

It exists so that User, Organization, Permission, Policy, Event, Audit, AI Agents, APIs and product consumers can safely recognize that an actor identity reference now exists without treating that identity as authenticated, authorized, assigned to an organization, or granted any permission.

IdentityCreated is required before:

```text
identity reference trace
user-to-identity linkage
organization membership linkage
permission evaluation context
policy evaluation context
actor audit trace
AI actor governance trace
API identity reference validation
```

---

# 2. Event Meaning

IdentityCreated means:

```text
a stable Identity object reference has been created through governed Identity Service operation.
```

IdentityCreated does not mean:

```text
the actor has authenticated
the actor has a User account
the actor belongs to an Organization
the actor has Permission
the actor has passed Policy
the actor has accepted terms
the actor is human rather than AI/system
the actor may perform business operations
```

IdentityCreated records recognition reference creation only.

It does not establish trust, access, membership or authority.

---

# 3. Event Category

IdentityCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Identity domain.

It is not a StatusEvent because it does not primarily record a lifecycle transition.

It is not an AIAgentEvent unless the created Identity itself is an AI Agent identity; even then, the event category remains DomainEvent, while payload must include AI/system identity indicators where applicable.

---

# 4. Event Producer

Producing service:

```text
Identity Service
```

Producing operation:

```text
createIdentity
```

Source domain:

```text
Identity
```

Source object type:

```text
Identity
```

Allowed producer path:

```text
API / System / Admin / AI-governed operation
        ↓
Identity Service createIdentity
        ↓
Event Service record IdentityCreated
```

Producer rules:

```text
- IdentityCreated must be emitted only after Identity Service successfully creates the Identity reference.
- IdentityCreated must not be emitted directly by product UI.
- IdentityCreated must not be emitted directly by AI Agent outside governed service operation.
- IdentityCreated must not be emitted for failed, duplicate-rejected or unauthorized identity creation attempts.
```

---

# 5. Event Trigger

IdentityCreated is triggered when:

```text
Identity Service successfully creates a new Identity object and commits its stable identity_reference_id.
```

Required trigger conditions:

```text
createIdentity operation completed
identity_type validated
identity_reference_id created
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
login attempt
authentication success
user account creation
organization membership creation
permission assignment
policy evaluation
AI suggestion to create identity
failed validation
duplicate identity rejected
```

Related but separate events may include:

```text
UserCreated
OrganizationMemberLinked
PermissionEvaluated
PolicyEvaluated
AIAgentIdentityLinked
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: IdentityCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Identity
source_service: Identity Service
source_operation: createIdentity
source_object_type: Identity
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/identity-created-payload.md
safe_summary:
  identity_reference_id: string
  identity_type: string
  identity_status: string
  source_type: string
restricted_fields_policy: IdentityCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
identity_reference_id: string
identity_type: string
identity_status: string
source_type: string
created_by_actor_reference_id: string
created_for_actor_reference_id: string | null
is_ai_identity: boolean
is_system_identity: boolean
```

Payload rules:

```text
- Payload must use identity_reference_id, not personal credentials.
- Payload must not include password, token, secret, private key, biometric data or raw authentication material.
- Payload must not include sensitive personal profile details unless explicitly allowed by policy.
- Payload must not treat identity_type as permission.
- AI identity creation must identify AI/system status safely.
```

---

# 7. Required References

Required references:

```text
event_id
identity_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
user_reference_id
system_reference_id
agent_contract_reference_id
permission_decision_reference_id
policy_decision_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal identity_reference_id.
- actor_reference_id identifies who/what requested or performed creation.
- user_reference_id must not be assumed.
- organization_reference_id must not be assumed.
- permission_decision_reference_id is required only where identity creation requires permission gate.
- policy_decision_reference_id is required only where policy gate applies.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
IdentityCreated
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

## 8.4 identity_type

```text
Human
System
AIAgent
ServiceAccount
ExternalActor
Unknown
```

## 8.5 identity_status

```text
Created
Active
PendingVerification
Suspended
Archived
DeletedReferenceOnly
Unknown
```

## 8.6 source_type

```text
AdminAction
SystemProcess
APIRequest
AIAgentRequest
Migration
ExternalIntegration
Unknown
```

## 8.7 reason_code

```text
IdentityCreated
SystemGenerated
AdminCreated
APIRequested
MigrationCreated
AIGenerated
Unknown
```

---

# 9. Event Rules

## 9.1 IdentityCreated Records Reference Creation Only

IdentityCreated records that an Identity reference exists.

It must not be interpreted as login, authentication, authorization or user membership.

## 9.2 IdentityCreated Does Not Grant Permission

Permission must be evaluated by Permission Service.

IdentityCreated must not imply allowed actions.

## 9.3 IdentityCreated Does Not Pass Policy

Policy must be evaluated by Policy Service.

IdentityCreated must not imply policy compliance.

## 9.4 IdentityCreated Does Not Create User

User Service owns User creation.

IdentityCreated may be followed by UserCreated, but they are separate events.

## 9.5 IdentityCreated Must Be Immutable

IdentityCreated must not be rewritten except controlled event metadata/status handled by Event Service.

## 9.6 AI or System Identity Must Be Explicit

If identity_type is AIAgent or System, payload must clearly mark it.

AI-generated or system-generated identity creation must not be hidden as human identity.

---

# 10. Consumer Rules

Allowed consumers:

```text
User Service
Organization Service
Permission Service
Policy Service
Audit Service
AI Agent Governance
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- User Service may consume IdentityCreated to create or link User only through User Service operation.
- Organization Service may link Identity to Organization only through Organization Service operation.
- Permission Service may use identity_reference_id for evaluation context.
- Policy Service may use identity_reference_id for policy context.
- Audit may preserve identity creation trace.
- AI Agents may summarize identity creation only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat IdentityCreated as authentication
treat IdentityCreated as permission grant
treat IdentityCreated as organization membership
create User silently without User Service
expose restricted identity details
```

---

# 11. Relationship to Services

Producing service:

```text
Identity Service produces IdentityCreated after createIdentity succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches IdentityCreated.
```

Related services:

```text
User Service may link a User to the created Identity.
Organization Service may link Organization membership or context.
Permission Service may evaluate actions for this Identity.
Policy Service may apply contextual constraints.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for AI actor trace.
```

Boundary reminders:

```text
Identity Service owns Identity.
User Service owns User.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /identities/{identity_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create IdentityCreated directly.
- API must call Identity Service createIdentity, which emits the event.
- API must not expose credentials, tokens, secrets or raw authentication data.
- API must distinguish IdentityCreated from UserCreated and authentication events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Identity reference was created
explain that Identity does not equal User or Permission
flag missing User linkage for review
flag AI/system identity classification inconsistencies
prepare audit-safe identity creation summary
```

AI must not:

```text
fabricate IdentityCreated
rewrite IdentityCreated
delete IdentityCreated
treat IdentityCreated as authentication
treat IdentityCreated as permission
hide AI/system identity type
expose restricted identity fields
```

AI-originated creation requires:

```text
agent_identity_reference_id
agent_contract_reference_id
authorized_knowledge_reference
permission_decision_reference_id where applicable
policy_decision_reference_id where applicable
human_review_reference where required
```

---

# 14. Validation Rules

IdentityCreated is valid only if:

```text
[ ] event_name is IdentityCreated.
[ ] event_category is DomainEvent.
[ ] producing service is Identity Service.
[ ] producing operation is createIdentity.
[ ] source_domain is Identity.
[ ] source_object_type is Identity.
[ ] source_object_reference_id is present.
[ ] identity_reference_id is present.
[ ] source_object_reference_id equals identity_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] identity_type is controlled.
[ ] identity_status is controlled.
[ ] payload contains no credentials, tokens, secrets or raw authentication material.
[ ] AI/system identity is explicitly identified where applicable.
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
IdentityReferenceMissing
IdentityReferenceMismatch
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
IdentityTypeInvalid
IdentityStatusInvalid
RestrictedFieldViolation
CredentialsPayloadRejected
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownEventError
```

Rejection rules:

```text
- Failed identity creation must not emit IdentityCreated.
- Duplicate rejected identity creation must not emit IdentityCreated unless a separate duplicate event is defined.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite Identity Service Specification
cite Identity Object Specification
cite Event Service Specification
use exact event_name: IdentityCreated
use exact event_category: DomainEvent
validate identity_reference_id
validate source_object_reference_id equals identity_reference_id
validate actor_reference_id
validate payload contract
write tests that failed createIdentity does not emit IdentityCreated
write tests that IdentityCreated does not create User automatically
write tests that IdentityCreated does not grant Permission
write tests that credentials/tokens/secrets are rejected from payload
write tests for AI/system identity indicators where applicable
```

Codex must not:

```text
emit IdentityCreated directly from UI
treat authentication log as IdentityCreated
treat UserCreated as IdentityCreated
include password/token/secret in payload
allow AI to fabricate IdentityCreated
use IdentityCreated as command to create User, Permission or Organization membership
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines IdentityCreated purpose.
[ ] It defines IdentityCreated meaning.
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
| 0.1.0 | Draft | Initial IdentityCreated Event specification. Defines identity reference creation event and separates IdentityCreated from authentication, User creation, Organization membership, Permission and Policy. |

---

**End of Event Specification**
