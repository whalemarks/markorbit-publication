# Event Specification — UserCreated

**Spec ID:** B02-EVT-USER-CREATED  
**Spec Type:** Event  
**Event Name:** UserCreated  
**Event File:** core-specs/events/user-created.md  
**Event Category:** DomainEvent  
**Owning Domain:** User  
**Producing Service:** core-specs/services/user-service.md  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/identity.md; core-specs/objects/organization.md; core-specs/objects/permission.md; core-specs/objects/policy.md  
**Related Service Specs:** core-specs/services/user-service.md; core-specs/services/identity-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md  
**Related API Specs:** core-specs/api/user-api.md; core-specs/api/event-api.md  
**Related Agent Specs:** core-specs/agents/user-agent.md; core-specs/agents/ai-agent-governance.md  
**Payload Contract:** core-specs/contracts/events/user-created-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

UserCreated records that a governed User account participant reference has been created by User Service.

It exists so that Identity, Organization, Permission, Policy, Event, Audit, AI Agents, APIs and product consumers can safely recognize that an account participant now exists without treating that User as authenticated, assigned to an Organization, granted Permission, approved by Policy, or authorized to perform business operations.

UserCreated is required before:

```text
user account participant trace
user-to-identity linkage trace
organization membership preparation
permission evaluation context
policy evaluation context
task assignment eligibility checks
actor audit trace
AI-assisted user administration review
API user reference validation
```

---

# 2. Event Meaning

UserCreated means:

```text
a stable User object reference has been created through governed User Service operation.
```

UserCreated does not mean:

```text
the User has authenticated
the User owns the referenced Identity
the User belongs to an Organization
the User has a role
the User has Permission
the User has passed Policy
the User is active in all products
the User may access business records
the User has accepted invitations or terms unless explicitly recorded elsewhere
```

UserCreated records account participant creation only.

It does not establish access, membership, professional authority or business responsibility.

---

# 3. Event Category

UserCreated is a:

```text
DomainEvent
```

It is a DomainEvent because it records a governed occurrence inside the User domain.

It is not an Identity event, even though User must reference Identity.

It is not a Permission event, even if User creation may later support permission evaluation.

---

# 4. Event Producer

Producing service:

```text
User Service
```

Producing operation:

```text
createUser
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
User Service createUser
        ↓
Event Service record UserCreated
```

Producer rules:

```text
- UserCreated must be emitted only after User Service successfully creates the User reference.
- UserCreated must not be emitted directly by product UI.
- UserCreated must not be emitted directly by AI Agent outside governed service operation.
- UserCreated must not be emitted for failed, duplicate-rejected or unauthorized user creation attempts.
```

---

# 5. Event Trigger

UserCreated is triggered when:

```text
User Service successfully creates a new User object and commits its stable user_reference_id.
```

Required trigger conditions:

```text
createUser operation completed
user_reference_id created
identity_reference_id validated
user_type validated
user_status validated
source_reference captured
actor_context captured
payload contract available
event recording requested through Event Service
```

Non-triggers:

```text
Identity creation
authentication success
organization membership creation
role assignment
permission grant
policy evaluation
invitation sent
AI suggestion to create User
failed validation
duplicate rejected User
```

Related but separate events may include:

```text
IdentityCreated
UserUpdated
UserStatusChanged
OrganizationMemberLinked
PermissionEvaluated
PolicyEvaluated
InvitationSent
```

---

# 6. Event Payload

Minimum payload:

```yaml
event_id: string
event_name: UserCreated
event_category: DomainEvent
event_version: 0.1.0
occurred_at: datetime
source_domain: User
source_service: User Service
source_operation: createUser
source_object_type: User
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: core-specs/contracts/events/user-created-payload.md
safe_summary:
  user_reference_id: string
  identity_reference_id: string
  user_type: string
  user_status: string
  source_type: string
restricted_fields_policy: UserCreatedRestrictedFieldsPolicy
metadata: object
```

Event-specific payload:

```yaml
user_reference_id: string
identity_reference_id: string
user_type: string
user_status: string
created_by_actor_reference_id: string
default_organization_reference_id: string | null
is_ai_user: boolean
is_system_user: boolean
source_type: string
```

Payload rules:

```text
- Payload must use references, not credentials.
- Payload must include identity_reference_id because User must reference Identity.
- Payload must not include password, token, secret, private key, biometric data or raw authentication material.
- Payload must not include personal profile details unless explicitly allowed by policy.
- Payload must not include role, permission or policy approval as implied facts.
- AI/system User creation must identify AI/system status safely where applicable.
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
invitation_reference_id
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
- actor_reference_id identifies who/what requested or performed creation.
- organization_reference_id must not be treated as membership unless Organization Service confirms it.
- permission_decision_reference_id is required only where User creation requires permission gate.
- policy_decision_reference_id is required only where policy gate applies.
```

---

# 8. Controlled Values

## 8.1 event_name

```text
UserCreated
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
UserCreated
AdminCreated
APIRequested
InvitationAccepted
MigrationCreated
SystemGenerated
AIGenerated
Unknown
```

---

# 9. Event Rules

## 9.1 UserCreated Records Account Participant Creation

UserCreated records that a User reference exists.

It must not be interpreted as authentication, organization membership, role assignment or permission grant.

## 9.2 UserCreated Requires Identity

A User must reference Identity.

UserCreated must not be valid without identity_reference_id.

## 9.3 UserCreated Does Not Create Identity Automatically

Identity Service owns Identity creation.

If Identity must be created, IdentityCreated must be produced separately by Identity Service.

## 9.4 UserCreated Does Not Grant Permission

Permission must be evaluated by Permission Service.

UserCreated must not imply allowed action.

## 9.5 UserCreated Does Not Pass Policy

Policy must be evaluated by Policy Service.

UserCreated must not imply policy compliance.

## 9.6 UserCreated Does Not Create Organization Membership

Organization Service owns membership and organization context.

UserCreated may later be linked to Organization, but not automatically.

## 9.7 UserCreated Must Be Immutable

UserCreated must not be rewritten except controlled event metadata/status handled by Event Service.

## 9.8 AI/System User Must Be Explicit

If user_type is AIAgentUser or SystemUser, payload must clearly mark it.

AI-generated or system-generated User creation must not be hidden as human User creation.

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
- Organization Service may consume UserCreated to prepare membership workflow only through governed operation.
- Permission Service may use user_reference_id for evaluation context.
- Policy Service may apply contextual constraints.
- Task Service may validate assignability only after Permission/Policy checks.
- Audit may preserve User creation trace.
- AI Agents may summarize User creation only under Authorized Knowledge and Policy.
```

Consumers must not:

```text
treat UserCreated as authentication
treat UserCreated as permission grant
treat UserCreated as organization membership
assign tasks without Permission/Policy
create Organization membership silently
expose restricted User data
```

---

# 11. Relationship to Services

Producing service:

```text
User Service produces UserCreated after createUser succeeds.
```

Event Service:

```text
Event Service records, validates and dispatches UserCreated.
```

Related services:

```text
Identity Service provides the required Identity reference.
Organization Service may link User to Organization through separate operation.
Permission Service may evaluate User actions.
Policy Service may apply contextual constraints.
Task Service may use User as assignee only under permission/policy.
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
- API must not create UserCreated directly.
- API must call User Service createUser, which emits the event.
- API must not expose credentials, tokens, secrets or raw authentication data.
- API must distinguish UserCreated from IdentityCreated, authentication events and Organization membership events.
- API must preserve actor_context, request_context and policy_context.
```

---

# 13. Relationship to AI Agents

Allowed AI use:

```text
summarize that a User reference was created
explain that User does not equal Identity, Organization membership or Permission
flag missing Organization membership for review
flag AI/system User classification inconsistencies
prepare audit-safe User creation summary
```

AI must not:

```text
fabricate UserCreated
rewrite UserCreated
delete UserCreated
treat UserCreated as authentication
treat UserCreated as permission
create Organization membership automatically
hide AI/system User type
expose restricted User fields
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

UserCreated is valid only if:

```text
[ ] event_name is UserCreated.
[ ] event_category is DomainEvent.
[ ] producing service is User Service.
[ ] producing operation is createUser.
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
[ ] user_status is controlled.
[ ] payload contains no credentials, tokens, secrets or raw authentication material.
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
- Failed User creation must not emit UserCreated.
- Duplicate rejected User creation must not emit UserCreated unless a separate duplicate event is defined.
- Missing or invalid Identity reference must reject UserCreated.
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
use exact event_name: UserCreated
use exact event_category: DomainEvent
validate user_reference_id
validate source_object_reference_id equals user_reference_id
validate identity_reference_id
validate actor_reference_id
validate payload contract
write tests that failed createUser does not emit UserCreated
write tests that UserCreated requires Identity
write tests that UserCreated does not create Organization membership automatically
write tests that UserCreated does not grant Permission
write tests that credentials/tokens/secrets are rejected from payload
write tests for AI/system User indicators where applicable
```

Codex must not:

```text
emit UserCreated directly from UI
treat authentication log as UserCreated
treat IdentityCreated as UserCreated
create Identity silently inside UserCreated event emission
include password/token/secret in payload
allow AI to fabricate UserCreated
use UserCreated as command to create Organization membership, Permission or Policy approval
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines UserCreated purpose.
[ ] It defines UserCreated meaning.
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
| 0.1.0 | Draft | Initial UserCreated Event specification. Defines User account participant creation event and separates UserCreated from Identity creation, authentication, Organization membership, Permission and Policy. |

---

**End of Event Specification**
