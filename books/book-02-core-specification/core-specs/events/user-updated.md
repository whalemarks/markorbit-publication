# Event Specification — UserUpdated

**Spec ID:** B02-EVT-USER-UPDATED  
**Spec Type:** Event  
**Event Name:** UserUpdated  
**Event File:** core-specs/events/user-updated.md  
**Event Category:** DomainEvent  
**Owning Domain:** User  
**Producing Service:** core-specs/services/user-service.md  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/user-service.md; core-specs/services/identity-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/user-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/user-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/user-updated-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

UserUpdated records that a governed User account participant reference has been updated by User Service.

It exists so that Identity, Organization, Permission, Policy, Event, Audit, AI Agents, APIs and product consumers can safely recognize that user metadata or lifecycle-relevant account participant information changed without treating the update as authentication, organization membership, role assignment, permission grant, policy approval or business responsibility assignment.

UserUpdated is required before:

```text
user metadata change trace
user status change trace
user-to-identity consistency checks
organization membership consistency checks
permission evaluation context refresh
policy evaluation context refresh
task assignment eligibility refresh
actor audit trace
AI-assisted user administration review
API user reference validation
```

---

# 2. Event Meaning

UserUpdated means:

```text
an existing stable User object reference has been updated through governed User Service operation.
```

UserUpdated does not mean:

```text
the User has authenticated
the User belongs to an Organization
the User has a role
the User has Permission
the User has passed Policy
the User owns business responsibility
the User has accepted an invitation
the linked Identity has changed unless explicitly included and allowed
Organization membership has been updated
```

UserUpdated records governed User account participant update only.

It does not establish access, membership, authority, approval or business responsibility.

---

# 3. Event Category

UserUpdated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the User domain.

If the update is specifically a status transition, downstream systems may observe status-related fields, but the Event category remains DomainEvent unless a separate UserStatusChanged event is introduced.

---

# 4. Event Producer

Producing service:

```text
User Service
```

Producing operation:

```text
updateUser
```

Source domain:

```text
User
```

Source object type:

```text
User
```

Allowed producer path:

```text
API / Admin / System / AI-governed operation
        ↓
User Service updateUser
        ↓
Event Service record UserUpdated
```

Producer rules:

```text
- UserUpdated must be emitted only after User Service successfully updates the User reference.
- UserUpdated must not be emitted directly by product UI.
- UserUpdated must not be emitted directly by AI Agent outside governed service operation.
- UserUpdated must not be emitted for failed, unauthorized or rejected update attempts.
```

---

# 5. Event Trigger

UserUpdated is triggered when:

```text
User Service successfully updates an existing User object and commits the governed change.
```

Required trigger conditions:

```text
updateUser operation completed
user_reference_id validated
identity_reference_id preserved or updated under allowed rules
updated fields validated
actor_context captured
source_reference captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Identity update
authentication success
organization membership update
role assignment
permission grant
policy evaluation
task assignment
AI suggestion to update User
failed validation
unauthorized update attempt
duplicate rejected update
```

Related but separate events may include:

```text
IdentityUpdated
UserStatusChanged
OrganizationMemberUpdated
PermissionEvaluated
PolicyEvaluated
TaskAssigned
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: UserUpdated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: User
source_service: User Service
source_operation: updateUser
source_object_type: User
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/user-updated-payload.md
safe_summary:
  user_reference_id: string
  identity_reference_id: string
  user_type: string
  user_status_before: string | null
  user_status_after: string | null
  changed_field_keys: list[string]
  source_type: string
restricted_fields_policy: UserUpdatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
user_reference_id: string
identity_reference_id: string
user_type: string
user_status_before: string | null
user_status_after: string | null
changed_field_keys: list[string]
changed_reference_keys: list[string]
updated_by_actor_reference_id: string
default_organization_reference_id: string | null
is_ai_user: boolean
is_system_user: boolean
source_type: string
```

Payload rules:

```text
- Payload must use references, not credentials.
- Payload must include user_reference_id and identity_reference_id.
- Payload may include changed field keys but must not include restricted raw values unless explicitly allowed.
- Payload must not include password, token, secret, private key, biometric data or raw authentication material.
- Payload must not include personal profile details unless explicitly allowed by policy.
- Payload must not include role, permission, membership or policy approval as implied facts.
- AI/system User update must identify AI/system status safely where applicable.
```

---

# 7. Required References

Required references:

```text
event_id
user_reference_id
identity_reference_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
default_organization_reference_id
permission_decision_reference_id
policy_decision_reference_id
agent_contract_reference_id
correlation_id
causation_id
```

Reference rules:

```text
- source_object_reference_id must equal user_reference_id.
- identity_reference_id must reference an existing Identity.
- actor_reference_id identifies who/what requested or performed update.
- organization_reference_id must not be treated as membership unless Organization Service confirms it.
- permission_decision_reference_id is required only where User update requires permission gate.
- policy_decision_reference_id is required only where policy gate applies.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
UserUpdated
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

## 8.4 user_type

```text
HumanUser
AdminUser
StaffUser
CustomerUser
PartnerUser
AgentUser
ServiceProviderUser
AIAgentUser
SystemUser
ExternalUser
Unknown
```

## 8.5 user_status

```text
Created
Active
Invited
PendingActivation
Suspended
Inactive
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
InvitationFlow
Unknown
```

## 8.7 reason_code

```text
UserUpdated
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

## 9.1 UserUpdated Records Governed User Change Only

UserUpdated records that a User account participant reference changed.

It must not be interpreted as authentication, organization membership, role assignment, permission grant or policy approval.

## 9.2 UserUpdated Requires Identity

A User must reference Identity.

UserUpdated must not be valid without identity_reference_id.

## 9.3 UserUpdated Does Not Update Identity Automatically

Identity Service owns Identity update.

If Identity changes are required, IdentityUpdated must be produced separately by Identity Service.

## 9.4 UserUpdated Does Not Grant Permission

Permission must be evaluated by Permission Service.

UserUpdated must not imply allowed action.

## 9.5 UserUpdated Does Not Pass Policy

Policy must be evaluated by Policy Service.

UserUpdated must not imply policy compliance.

## 9.6 UserUpdated Does Not Update Organization Membership

Organization Service owns membership and organization context.

UserUpdated may trigger consistency checks but must not silently update membership.

## 9.7 UserUpdated Must Preserve Safe Diff

UserUpdated should preserve safe changed field keys and safe before/after status where allowed.

It must not expose restricted raw values.

## 9.8 UserUpdated Must Be Immutable

UserUpdated must not be rewritten except controlled event metadata/status handled by Event Service.

## 9.9 AI/System User Must Be Explicit

If user_type is AIAgentUser or SystemUser, payload must clearly mark it.

AI-generated or system-generated User updates must not be hidden as human User updates.

---

# 10. Consumer Rules

Allowed consumers:

```text
Identity Service
Organization Service
Permission Service
Policy Service
Task Service
Audit Service
AI Agent Governance
Product UI read model
API consumers under policy
Integration services under contract
```

Consumer rules:

```text
- Organization Service may consume UserUpdated for consistency review only through governed operation.
- Permission Service may refresh User context for evaluation.
- Policy Service may apply updated contextual constraints.
- Task Service may validate assignability only after Permission/Policy checks.
- Audit may preserve User update trace.
- AI Agents may summarize User update only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat UserUpdated as authentication
treat UserUpdated as permission grant
treat UserUpdated as organization membership
assign tasks without Permission/Policy
update Organization membership silently
expose restricted User changed values
```

---

# 11. Relationship to Services

Producing service:

```text
User Service produces UserUpdated after updateUser succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches UserUpdated.
```

Related services:

```text
Identity Service provides the required Identity reference and handles Identity changes separately.
Organization Service may review or link membership through separate operation.
Permission Service may evaluate User actions.
Policy Service may apply contextual constraints.
Task Service may use User as assignee only under Permission/Policy.
Audit Service may record accountability trace.
AI Agent Governance may require this Event for AI/system user trace.
```

Boundary reminders:

```text
Identity Service owns Identity.
User Service owns User.
Organization Service owns membership/context.
Permission Service owns allowed action.
Policy Service owns contextual constraints.
Event Service records occurrence.
```

---

# 12. Relationship to APIs

Possible API exposure:

```text
GET /events/{event_id}
GET /users/{user_id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create UserUpdated directly.
- API must call User Service updateUser, which emits the event.
- API must not expose credentials, tokens, secrets, raw authentication data or restricted changed values.
- API must distinguish UserUpdated from IdentityUpdated, authentication events and Organization membership events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a User reference was updated
explain that User update does not equal Identity update, Organization membership or Permission
flag missing Organization consistency review for review
flag AI/system User classification inconsistencies
prepare audit-safe User update summary
```

AI must not:

```text
fabricate UserUpdated
rewrite UserUpdated
delete UserUpdated
treat UserUpdated as authentication
treat UserUpdated as permission
update Organization membership automatically
hide AI/system User type
expose restricted User fields or changed values
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

UserUpdated is valid only if:

```text
[ ] event_name is UserUpdated.
[ ] event_category is DomainEvent.
[ ] producing service is User Service.
[ ] producing operation is updateUser.
[ ] source_domain is User.
[ ] source_object_type is User.
[ ] source_object_reference_id is present.
[ ] user_reference_id is present.
[ ] source_object_reference_id equals user_reference_id.
[ ] identity_reference_id is present.
[ ] identity_reference_id references an existing Identity.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] user_type is controlled.
[ ] user_status_before/after are controlled where provided.
[ ] changed_field_keys are provided where applicable.
[ ] payload contains no credentials, tokens, secrets or raw authentication material.
[ ] restricted raw changed values are not exposed.
[ ] role, permission and organization membership are not implied.
[ ] AI/system User is explicitly identified where applicable.
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
UserReferenceMissing
UserReferenceMismatch
IdentityReferenceMissing
IdentityReferenceInvalid
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
UserTypeInvalid
UserStatusInvalid
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
- Failed User update must not emit UserUpdated.
- Unauthorized update attempt must not emit UserUpdated.
- Missing or invalid Identity reference must reject UserUpdated.
- Restricted payload content must not be returned in error response.
- Rejection reason must be safe for API/product display.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite User Service Specification
cite User Object Specification
cite Identity Service/Object Specifications
cite Event Service Specification
use exact event_name: UserUpdated
use exact event_category: DomainEvent
validate user_reference_id
validate source_object_reference_id equals user_reference_id
validate identity_reference_id
validate actor_reference_id
validate payload contract
write tests that failed updateUser does not emit UserUpdated
write tests that unauthorized update does not emit UserUpdated
write tests that UserUpdated requires Identity
write tests that UserUpdated does not update Organization membership automatically
write tests that UserUpdated does not grant Permission
write tests that credentials/tokens/secrets are rejected from payload
write tests that restricted changed values are not exposed
write tests for AI/system User indicators where applicable
```

Codex must not:

```text
emit UserUpdated directly from UI
treat authentication log as UserUpdated
treat IdentityUpdated as UserUpdated
update Identity silently inside UserUpdated event emission
include password/token/secret in payload
include restricted raw changed values by default
allow AI to fabricate UserUpdated
use UserUpdated as command to update Organization membership, Permission or Policy approval
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines UserUpdated purpose.
[ ] It defines UserUpdated meaning.
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
| 0.1.0 | Draft | Initial UserUpdated Event specification. Defines governed User account participant update event and separates UserUpdated from Identity update, authentication, Organization membership, Permission and Policy. |

---

**End of Event Specification**
