# Event Specification — IdentityUpdated

**Spec ID:** B02-EVT-IDENTITY-UPDATED  
**Spec Type:** Event  
**Event Name:** IdentityUpdated  
**Event File:** core-specs/events/identity-updated.md  
**Event Category:** DomainEvent  
**Owning Domain:** Identity  
**Producing Service:** core-specs/services/identity-service.md  
**Related Object Specs:** core-specs/objects/identity.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/identity-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/identity-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/identity-updated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

IdentityUpdated records that a governed Identity reference has been updated by Identity Service.

It exists so that User, Organization, Permission, Policy, Event, Audit, AI Agents, APIs and product consumers can safely recognize that identity metadata or lifecycle-relevant reference information changed without treating the update as authentication, permission grant, organization membership, user account update, or policy approval.

IdentityUpdated is required before:

```text
identity metadata change trace
identity status change trace
actor reference audit
user-to-identity consistency checks
organization membership consistency checks
permission evaluation context refresh
policy evaluation context refresh
AI/system identity governance trace
API identity reference validation
```

---

# 2. Event Meaning

IdentityUpdated means:

```text
an existing stable Identity object reference has been updated through governed Identity Service operation.
```

IdentityUpdated does not mean:

```text
the actor has authenticated
the actor has a User account
the actor belongs to an Organization
the actor has Permission
the actor has passed Policy
the actor profile has been fully verified
the actor may perform business operations
a User record has been updated
```

IdentityUpdated records governed Identity reference update only.

It does not establish trust, access, membership or authority.

---

# 3. Event Category

IdentityUpdated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the Identity domain.

If the update is specifically a status transition, downstream systems may also observe status-related fields, but the Event category remains DomainEvent unless a separate IdentityStatusChanged event is introduced.

---

# 4. Event Producer

Producing service:

```text
Identity Service
```

Producing operation:

```text
updateIdentity
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
Identity Service updateIdentity
        ↓
Event Service record IdentityUpdated
```

Producer rules:

```text
- IdentityUpdated must be emitted only after Identity Service successfully updates the Identity reference.
- IdentityUpdated must not be emitted directly by product UI.
- IdentityUpdated must not be emitted directly by AI Agent outside governed service operation.
- IdentityUpdated must not be emitted for failed, unauthorized or rejected update attempts.
```

---

# 5. Event Trigger

IdentityUpdated is triggered when:

```text
Identity Service successfully updates an existing Identity object and commits the governed change.
```

Required trigger conditions:

```text
updateIdentity operation completed
identity_reference_id validated
updated fields validated
actor_context captured
source_reference captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
login attempt
authentication success
user profile update
organization membership update
permission evaluation
policy evaluation
AI suggestion to update identity
failed validation
unauthorized update attempt
duplicate rejected update
```

Related but separate events may include:

```text
UserUpdated
OrganizationMemberUpdated
PermissionEvaluated
PolicyEvaluated
IdentityStatusChanged
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: IdentityUpdated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: Identity
source_service: Identity Service
source_operation: updateIdentity
source_object_type: Identity
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/identity-updated-payload.md
safe_summary:
  identity_reference_id: string
  identity_type: string
  identity_status_before: string | null
  identity_status_after: string | null
  changed_field_keys: list[string]
  source_type: string
restricted_fields_policy: IdentityUpdatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
identity_reference_id: string
identity_type: string
identity_status_before: string | null
identity_status_after: string | null
changed_field_keys: list[string]
changed_reference_keys: list[string]
source_type: string
updated_by_actor_reference_id: string
is_ai_identity: boolean
is_system_identity: boolean
```

Payload rules:

```text
- Payload must use identity_reference_id, not personal credentials.
- Payload may include changed field keys but must not include restricted raw values unless explicitly allowed.
- Payload must not include password, token, secret, private key, biometric data or raw authentication material.
- Payload must not include sensitive personal profile details unless explicitly allowed by policy.
- Payload must not treat identity_status_after as permission.
- AI/system identity update must identify AI/system status safely.
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
- actor_reference_id identifies who/what requested or performed update.
- user_reference_id must not be assumed.
- organization_reference_id must not be assumed.
- permission_decision_reference_id is required only where identity update requires permission gate.
- policy_decision_reference_id is required only where policy gate applies.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
IdentityUpdated
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
IdentityUpdated
StatusUpdated
MetadataUpdated
ReferenceUpdated
SystemUpdated
AdminUpdated
APIRequested
MigrationUpdated
AIGenerated
Unknown
```

---

# 9. Event Rules

## 9.1 IdentityUpdated Records Governed Identity Change Only

IdentityUpdated records that an Identity reference changed.

It must not be interpreted as login, authentication, authorization, user profile update or organization membership update.

## 9.2 IdentityUpdated Does Not Grant Permission

Permission must be evaluated by Permission Service.

IdentityUpdated must not imply allowed actions.

## 9.3 IdentityUpdated Does Not Pass Policy

Policy must be evaluated by Policy Service.

IdentityUpdated must not imply policy compliance.

## 9.4 IdentityUpdated Does Not Update User Automatically

User Service owns User update.

IdentityUpdated may trigger consistency checks but must not silently update User.

## 9.5 IdentityUpdated Must Preserve Safe Diff

IdentityUpdated should preserve safe changed field keys and safe before/after status where allowed.

It must not expose restricted raw values.

## 9.6 IdentityUpdated Must Be Immutable

IdentityUpdated must not be rewritten except controlled event metadata/status handled by Event Service.

## 9.7 AI or System Identity Must Be Explicit

If identity_type is AIAgent or System, payload must clearly mark it.

AI-generated or system-generated identity updates must not be hidden as human updates.

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
- User Service may consume IdentityUpdated for consistency review only through governed User Service operation.
- Organization Service may review membership context only through Organization Service operation.
- Permission Service may refresh identity context for evaluation.
- Policy Service may refresh contextual constraints.
- Audit may preserve identity update trace.
- AI Agents may summarize identity update only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat IdentityUpdated as authentication
treat IdentityUpdated as permission grant
treat IdentityUpdated as organization membership
update User silently without User Service
expose restricted identity change values
```

---

# 11. Relationship to Services

Producing service:

```text
Identity Service produces IdentityUpdated after updateIdentity succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches IdentityUpdated.
```

Related services:

```text
User Service may review linked User consistency.
Organization Service may review organization membership context.
Permission Service may evaluate actions using updated Identity context.
Policy Service may apply contextual constraints.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for AI/system actor trace.
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
- API must not create IdentityUpdated directly.
- API must call Identity Service updateIdentity, which emits the event.
- API must not expose credentials, tokens, secrets, raw authentication data or restricted changed values.
- API must distinguish IdentityUpdated from UserUpdated and authentication events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that an Identity reference was updated
explain that Identity update does not equal User update or Permission grant
flag missing User consistency review for review
flag AI/system identity classification inconsistencies
prepare audit-safe identity update summary
```

AI must not:

```text
fabricate IdentityUpdated
rewrite IdentityUpdated
delete IdentityUpdated
treat IdentityUpdated as authentication
treat IdentityUpdated as permission
hide AI/system identity type
expose restricted identity fields or changed values
```

AI-originated update requires:

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

IdentityUpdated is valid only if:

```text
[ ] event_name is IdentityUpdated.
[ ] event_category is DomainEvent.
[ ] producing service is Identity Service.
[ ] producing operation is updateIdentity.
[ ] source_domain is Identity.
[ ] source_object_type is Identity.
[ ] source_object_reference_id is present.
[ ] identity_reference_id is present.
[ ] source_object_reference_id equals identity_reference_id.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] identity_type is controlled.
[ ] identity_status_before/after are controlled where provided.
[ ] changed_field_keys are provided where applicable.
[ ] payload contains no credentials, tokens, secrets or raw authentication material.
[ ] restricted raw changed values are not exposed.
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
ChangedFieldKeysMissing
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
- Failed identity update must not emit IdentityUpdated.
- Unauthorized update attempt must not emit IdentityUpdated.
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
use exact event_name: IdentityUpdated
use exact event_category: DomainEvent
validate identity_reference_id
validate source_object_reference_id equals identity_reference_id
validate actor_reference_id
validate payload contract
write tests that failed updateIdentity does not emit IdentityUpdated
write tests that unauthorized update does not emit IdentityUpdated
write tests that IdentityUpdated does not update User automatically
write tests that IdentityUpdated does not grant Permission
write tests that credentials/tokens/secrets are rejected from payload
write tests that restricted changed values are not exposed
write tests for AI/system identity indicators where applicable
```

Codex must not:

```text
emit IdentityUpdated directly from UI
treat authentication log as IdentityUpdated
treat UserUpdated as IdentityUpdated
include password/token/secret in payload
include restricted raw changed values by default
allow AI to fabricate IdentityUpdated
use IdentityUpdated as command to update User, Permission or Organization membership
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines IdentityUpdated purpose.
[ ] It defines IdentityUpdated meaning.
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
| 0.1.0 | Draft | Initial IdentityUpdated Event specification. Defines governed Identity reference update event and separates IdentityUpdated from authentication, User update, Organization membership, Permission and Policy. |

---

**End of Event Specification**
