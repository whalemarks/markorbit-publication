# Service Specification — Policy Service

**Spec ID:** B02-SVC-POLICY-SERVICE  
**Spec Type:** Service  
**Service Name:** Policy Service  
**Owning Domain:** Policy  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-18 — Identity Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/policy.md  
**Related Object Specs:** core-specs/objects/policy.md; core-specs/objects/permission.md; core-specs/objects/identity.md; core-specs/objects/user.md; core-specs/objects/organization.md  
**Related Service Specs:** core-specs/services/identity-service.md; core-specs/services/user-service.md; core-specs/services/organization-service.md; core-specs/services/permission-service.md  
**Related Event Specs:** core-specs/events/policy-created.md; core-specs/events/policy-updated.md; core-specs/events/policy-status-changed.md; core-specs/events/policy-evaluated.md; core-specs/events/policy-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/policy/policy-contract.md; core-specs/contracts/policy/policy-evaluation-contract.md; core-specs/contracts/policy/policy-reference-contract.md; core-specs/contracts/policy/policy-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Policy Service defines the Core service boundary for creating, updating, validating and evaluating Policy objects and contextual constraints.

It exists so that Permission, Identity, User, Organization, Workflow Contract, Task, Document, Evidence, Communication, AI Agents, APIs and product consumers can consistently determine whether an otherwise permitted action is contextually allowed, restricted, review-required or prohibited without confusing Policy with Permission, approval, workflow, professional judgment or legal rule engines.

Policy Service is required before:

```text
contextual access constraints
organization-scoped restrictions
confidentiality checks
AI action boundaries
document/evidence visibility checks
workflow guard evaluation
high-risk action review requirements
external communication constraints
data handling rules
audit trace for policy-sensitive actions
```

---

# 2. Core Meaning

Policy Service means:

```text
the Core service that evaluates contextual constraints for an actor, action, resource and environment after or alongside permission evaluation.
```

Policy Service does not mean:

```text
Permission Service
Identity Service
User Service
Organization Service
approval workflow
legal rule engine
fee engine
deadline engine
professional judgment
compliance department by itself
```

Policy Service answers:

```text
Is this action contextually allowed?
Which policy rule applies?
Does this action require review or approval?
Is the resource restricted by confidentiality, organization, role, status, jurisdiction or AI boundary?
Should the action be allowed, denied, restricted, redacted or escalated?
What audit trace is required?
```

---

# 3. Service Category

Policy Service is a Foundation Core Service.

It is the contextual constraint service.

It does not grant permission.

It does not authenticate actors.

It does not replace professional review.

It does not implement jurisdiction-specific legal rule engines by itself.

---

# 4. Architectural Position

Policy Service sits after Identity/User/Organization recognition and beside Permission evaluation.

```text
Identity recognizes actor
        ↓
User represents account participant
        ↓
Organization provides operating context
        ↓
Permission Service determines allowed action
        ↓
Policy Service evaluates contextual constraints
        ↓
Workflow / Review / Approval may be required
        ↓
Domain Service executes or rejects action
        ↓
Event and Audit record outcome
```

Permission answers “may this actor do this action?”

Policy answers “is this action contextually allowed under current constraints?”

---

# 5. Scope

Policy Service includes:

```text
policy creation
policy update
policy status management
policy evaluation
policy reference validation
policy rule matching
policy review requirement output
policy redaction/visibility guidance
policy audit trace
policy event emission
```

MVP scope includes:

```text
create policy
get policy
update policy metadata
change policy status
evaluate policy
validate policy reference
return allowed/denied/review-required/restricted result
emit policy events
```

Deferred scope includes:

```text
full policy language engine
complex policy composition
external compliance engine integration
jurisdiction-specific legal rule engine
advanced data loss prevention
dynamic risk scoring
policy simulation UI
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createPolicy | Create Policy object/rule | Yes | PolicyCreated |
| getPolicy | Retrieve Policy by ID | Yes | No |
| updatePolicy | Update governed metadata/rule fields | Yes | PolicyUpdated |
| changePolicyStatus | Change Policy lifecycle status | Yes | PolicyStatusChanged |
| evaluatePolicy | Evaluate contextual constraints | Yes | PolicyEvaluated |
| validatePolicyReference | Validate whether Policy can be referenced | Yes | PolicyReferenceValidated |
| listApplicablePolicies | List policies for context | Partial | No |
| archivePolicy | Archive Policy reference | Partial | PolicyArchived |

---

# 7. Inputs

Policy Service accepts:

```text
policy_type
status
actor_reference_id
actor_type
action
resource_type
resource_reference_id
organization_reference_id
jurisdiction_reference_id
confidentiality_level
workflow_state_reference
context_attributes
condition_reference
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
policy_type
policy_scope
condition_reference
status
source_reference
actor_context
```

Required for evaluation:

```text
requesting_actor_reference_id
action
resource_type
resource_reference_id
organization_reference_id where applicable
context_attributes
request_context
```

Required for validation:

```text
policy_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Policy Service returns:

```text
Policy object
Policy reference
Policy evaluation result
Policy validation result
Policy status result
Policy event reference
error result
```

Evaluation output must include:

```text
decision
actor_reference_id
action
resource_type
resource_reference_id
matched_policy_reference_id
reason_code
review_required
approval_required
redaction_required
audit_required
policy_hint
```

Evaluation output must not expose unrelated policy rules or confidential resource details.

---

# 9. Controlled Values

## 9.1 policy_type

```text
AccessPolicy
DataPolicy
ConfidentialityPolicy
WorkflowPolicy
AIAgentPolicy
CommunicationPolicy
DocumentPolicy
EvidencePolicy
OrganizationPolicy
SystemPolicy
Unknown
```

## 9.2 status

```text
Draft
Active
Suspended
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

## 9.3 decision

```text
Allowed
Denied
Restricted
ReviewRequired
ApprovalRequired
RedactionRequired
NotApplicable
Unknown
```

## 9.4 policy_scope

Suggested controlled values:

```text
Global
Organization
Domain
Service
ObjectType
Resource
Jurisdiction
Workflow
AIAgent
Unknown
```

---

# 10. Service Rules

## 10.1 Policy Evaluates Contextual Constraints

Policy Service evaluates whether an action is contextually allowed under rules, conditions, resource state, actor context and environment.

## 10.2 Policy Does Not Grant Permission

Policy may restrict, require review or allow context.

It must not grant action permission by itself.

Permission Service owns authorization.

## 10.3 Policy Is Not Approval

Policy may require approval.

Approval must be executed through Workflow, Task, Review or relevant domain services.

## 10.4 Policy Is Not Legal Rule Engine

Policy may reference Knowledge, Jurisdiction or legal-rule sources.

It must not become the full legal rule engine for registrability, deadlines, fees or substantive legal advice.

## 10.5 Policy Must Be Explicit for AI Actions

AI actions must be policy-evaluated where they affect protected data, professional conclusions, external communication or automated execution.

## 10.6 Policy May Require Redaction or Restricted Output

Policy Service may return redaction guidance.

It must not expose protected data in policy output.

## 10.7 Policy Changes Must Be Auditable

Policy-sensitive operations must preserve actor, source, request context, evaluation result and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Permission Service | Policy evaluates after/with Permission | Permission grants allowed action. |
| Identity Service | Validates actor reference | Identity recognizes actor. |
| User Service | Provides user context | User manages participant. |
| Organization Service | Provides operating context | Organization provides context. |
| Workflow Contract | May use Policy as guard | Workflow owns transition structure. |
| Task Service | May require policy check | Task owns work unit. |
| Document Service | May require access/redaction policy | Document owns artifact. |
| Evidence Service | May require sensitivity policy | Evidence owns proof layer. |
| Communication Service | May require external-send policy | Communication owns message lifecycle. |
| AI Agent Governance | Requires policy for AI action | Agent Contract governs AI use. |
| Audit Service | Records policy-sensitive action | Audit owns accountability trail. |
| Event Service | Records policy events | Event records occurrence. |

---

# 12. Event Usage

Policy Service emits:

```text
PolicyCreated
PolicyUpdated
PolicyStatusChanged
PolicyEvaluated
PolicyDenied
PolicyRestricted
PolicyReviewRequired
PolicyApprovalRequired
PolicyArchived
PolicyReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Policy evaluation events may be emitted where audit requires.
- Denied, restricted, review-required and approval-required actions should be traceable where governance requires.
- Events must reference actor, action and resource type safely.
- Events must not expose unrelated policy rules or restricted resource content.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /policies
GET /policies/{id}
PATCH /policies/{id}
POST /policies/{id}/status
POST /policies/evaluate
POST /policies/reference/validate
GET /policies/applicable
```

API rules:

```text
- APIs must invoke Policy Service operations.
- APIs must not authenticate credentials.
- APIs must not grant Permission.
- APIs must not approve workflow or professional actions by themselves.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Policy Service only under governed Agent Contracts.

Allowed AI use:

```text
check whether AI action is contextually allowed
check whether output should be redacted
check whether external communication requires review
check whether document/evidence access is restricted
summarize non-sensitive policy result
prepare policy review note
```

AI must not:

```text
grant itself permission through policy
bypass policy evaluation
hide denied or restricted policy results
expose restricted policy details
alter policy status without authorized service
treat policy result as professional legal conclusion
send external communication when policy requires review
```

AI Policy use requires:

```text
Agent Identity
Agent Contract
Permission Rule
Policy Rule
Policy Access Rule
Data Visibility Rule
Audit Rule
Human Review Rule for policy creation, override or high-risk action
```

---

# 15. Validation Rules

Policy Service must enforce:

```text
[ ] policy_type is controlled.
[ ] status is controlled.
[ ] decision is controlled.
[ ] createPolicy produces stable immutable Policy ID.
[ ] updatePolicy does not mutate immutable ID.
[ ] changePolicyStatus follows allowed lifecycle.
[ ] evaluatePolicy requires actor, action, resource and context.
[ ] evaluatePolicy distinguishes Allowed from Denied, Restricted, ReviewRequired and ApprovalRequired.
[ ] Policy Service does not grant Permission.
[ ] Policy Service does not execute Approval.
[ ] Policy Service does not become legal rule engine.
[ ] Policy Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Policy Service should return controlled errors:

```text
PolicyNotFound
InvalidPolicyType
InvalidPolicyStatus
InvalidPolicyTransition
InvalidPolicyReference
ActorReferenceRequired
InvalidActorReference
ActionRequired
ResourceReferenceRequired
ContextRequired
InvalidContext
PolicyDenied
PolicyRestricted
ReviewRequired
ApprovalRequired
AuditContextMissing
UnknownPolicyError
```

Errors must be safe for product display and API consumption.

Sensitive policy logic or protected resource details must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite policy domain spec
cite policy object spec
cite permission service spec
preserve Policy / Permission boundary
preserve Policy / Approval boundary
preserve Policy / Workflow boundary
preserve Policy / Legal Rule Engine boundary
implement only Phase 1 Partial operations unless task says otherwise
write tests for evaluatePolicy requiring actor/action/resource/context
write tests for controlled policy_type
write tests for controlled status
write tests for controlled decision
write tests preventing Policy Service from granting Permission
write tests preventing Policy Service from executing Approval
write tests preventing Policy Service from becoming legal rule engine
write tests for review_required / approval_required / redaction_required outputs
write tests for event emission on mutation
```

Codex must not:

```text
invent full policy language engine beyond approved MVP
implement authentication or permission granting logic
approve workflow or professional review from Policy Service
implement jurisdiction legal rule engine inside Policy Service
expose restricted data in policy results
allow AI to override or bypass policy
allow product UI to redefine Policy status
```

---

# 18. Acceptance Criteria

This Policy Service Specification is accepted only if:

```text
[ ] It defines Policy Service purpose.
[ ] It defines Policy Service Core meaning.
[ ] It identifies Policy Service as Foundation Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Policy Service specification. Establishes Policy Service as contextual constraint service, separates it from Permission, Approval, Workflow and legal rule engines, and defines Phase 1 Partial operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
