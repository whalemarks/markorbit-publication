# Object Specification — Policy

**Spec ID:** B02-OBJ-POLICY  
**Spec Type:** Object  
**Object Name:** Policy  
**Owning Domain:** Policy  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-17 — Core Contract Architecture  
**Source Domain Spec:** core-specs/domains/policy.md  
**Related Object Specs:** core-specs/objects/permission.md; core-specs/objects/policy-rule.md; core-specs/objects/policy-condition.md; core-specs/objects/policy-scope.md; core-specs/objects/policy-decision.md; core-specs/objects/policy-status.md; core-specs/objects/policy-review-reference.md  
**Related Service Specs:** core-specs/services/policy-registration-service.md; core-specs/services/policy-evaluation-service.md; core-specs/services/policy-status-service.md; core-specs/services/policy-scope-validation-service.md; core-specs/services/policy-reference-validation-service.md  
**Related Event Specs:** core-specs/events/policy-created.md; core-specs/events/policy-updated.md; core-specs/events/policy-status-changed.md; core-specs/events/policy-evaluated.md; core-specs/events/policy-review-required.md; core-specs/events/policy-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/policy/policy-contract.md; core-specs/contracts/policy/policy-rule-contract.md; core-specs/contracts/policy/policy-condition-contract.md; core-specs/contracts/policy/policy-evaluation-contract.md; core-specs/contracts/policy/policy-review-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Partial Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Policy object defines the Core contextual rule used to evaluate whether an otherwise possible or permitted action should be allowed, denied, reviewed, constrained or escalated under specific business, professional, security, compliance or execution conditions.

It exists so that Permission, Capability, Workflow, Task, Matter, Document, Evidence, Communication, AI Agent and product consumers can consistently apply contextual constraints without confusing Policy with Permission, Identity, Capability, workflow state or professional truth.

Policy is required before:

```text
contextual access control
workflow guard evaluation
review requirement evaluation
data sensitivity constraint
AI action constraint
jurisdiction-sensitive rule
document/evidence handling constraint
communication sending constraint
task escalation rule
professional review requirement
audit trace for governed decisions
```

---

# 2. Core Meaning

Policy means:

```text
a Core-recognized contextual rule or rule set that evaluates conditions around an action, object, actor, workflow, data scope or professional context and produces a governed decision or review requirement.
```

Policy is not:

```text
Permission
Identity
User
Organization
Capability
Business Responsibility
Workflow
Task
Professional truth
Legal opinion
Product setting
AI prompt
Audit record
```

Policy answers:

```text
Which contextual rule applies?
Which scope or condition is being evaluated?
Which action, object, actor or workflow context is constrained?
Does the context allow, deny, require review, require approval or require audit?
Which reason or rule source supports the decision?
What event and audit trace is required?
```

---

# 3. Object Category

Policy is a Foundation Object owned by the Policy Domain.

It is a Core governance object.

It may be referenced by Permission, Capability, Workflow Contract, AI Governance, Professional Domains and Business Execution Domains.

Policy must not absorb Permission, Capability or professional legal judgment.

---

# 4. Architectural Position

Policy sits after Permission and before governed execution.

```text
Identity recognizes actor
        ↓
Capability describes possible action
        ↓
Permission determines allowed action
        ↓
Policy evaluates contextual constraints
        ↓
Review / Approval may be required
        ↓
Service executes if allowed
        ↓
Event and Audit preserve trace
```

Permission asks whether the actor may act.

Policy asks whether this context allows the action.

Policy does not execute the action.

---

# 5. Scope

The Policy object includes:

```text
policy id
policy type
policy name/reference
policy status
policy scope
policy rule reference
policy condition reference
policy effect
policy decision boundary
review requirement
approval requirement
audit requirement
priority
source reference
version reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
policy id
policy type
policy name/reference
policy status
policy scope
policy effect
review requirement
approval requirement
audit requirement
priority
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Policy ID. |
| policy_type | enum | Yes | Yes | AccessPolicy, WorkflowPolicy, ReviewPolicy, DataPolicy, AIPolicy, CompliancePolicy, SystemPolicy, Unknown. |
| name_reference | string | Yes | Yes | Human-readable policy reference. |
| status | enum | Yes | Yes | Controlled Policy status. |
| scope_type | enum | Yes | Yes | Global, Organization, Domain, Object, Service, Workflow, API, Product, DataAccess, Agent, Jurisdiction. |
| scope_reference | string | No | Yes | Scope reference where applicable. |
| rule_reference_id | string | No | Partial | Rule object/reference. |
| condition_reference_id | string | No | Partial | Condition object/reference. |
| effect | enum | Yes | Yes | Allow, Deny, ReviewRequired, ApprovalRequired, AuditRequired, Escalate. |
| priority | integer | No | Yes | Evaluation priority. |
| review_required | boolean | No | Yes | Explicit review requirement. |
| approval_required | boolean | No | Yes | Explicit approval requirement. |
| audit_required | boolean | No | Yes | Explicit audit requirement. |
| version_reference | string | No | Partial | Version reference where applicable. |
| source_reference | string | No | Yes | Source/system/professional reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 policy_type

MVP controlled values:

```text
AccessPolicy
WorkflowPolicy
ReviewPolicy
DataPolicy
AIPolicy
CompliancePolicy
SystemPolicy
Unknown
```

## 7.2 scope_type

MVP controlled values:

```text
Global
Organization
Domain
Object
Service
Workflow
API
Product
DataAccess
Agent
Jurisdiction
```

## 7.3 effect

MVP controlled values:

```text
Allow
Deny
ReviewRequired
ApprovalRequired
AuditRequired
Escalate
```

## 7.4 status

MVP controlled values:

```text
Draft
Active
Suspended
Deprecated
Archived
```

---

# 8. Object Rules

## 8.1 Policy Requires Scope

Every Policy must define scope.

A Policy without scope is not Core-valid.

## 8.2 Policy Requires Effect

Every Policy must define a controlled effect.

Policy may allow, deny, require review, require approval, require audit or escalate.

## 8.3 Policy Does Not Grant Permission by Itself

Policy may constrain or qualify action.

Permission still determines whether the actor has authorization.

## 8.4 Policy Does Not Replace Professional Judgment

Policy may require review or approval.

It must not be treated as legal conclusion, trademark strategy or professional truth by itself.

## 8.5 Policy Must Be Version-Aware Where Risk Is High

High-risk policy changes should preserve version or source references.

This includes AI policy, data access policy, client-facing communication policy, document/evidence handling policy and external filing policy.

## 8.6 Policy Must Be Auditable

Policy-sensitive changes and evaluations must preserve audit trace.

Audit-sensitive actions include:

```text
policy creation
policy update
policy status change
policy evaluation
policy denial
policy review requirement
policy override
AI policy evaluation
policy deprecation
policy version change
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Permission | Policy constrains Permission context | Policy does not grant Permission. |
| Capability | Policy constrains Capability use | Capability remains descriptive. |
| Identity | Policy may evaluate actor context | Identity remains actor reference. |
| User | Policy may evaluate user context | User remains account participant. |
| Organization | Policy may be scoped by Organization | Organization remains operating context. |
| Workflow Contract | Policy may guard transitions | Workflow owns transition structure. |
| Task | Policy may constrain task action | Task remains work unit. |
| Matter | Policy may constrain execution context | Matter remains execution container. |
| Document | Policy may constrain document handling | Document remains artifact. |
| Evidence | Policy may constrain evidence handling | Evidence remains proof layer. |
| Communication | Policy may constrain message sending/access | Communication remains message lifecycle. |
| AI Agent | AI actions must be Policy-governed | AI Governance remains separate. |
| Event | Policy evaluation may emit Event | Event remains signal. |
| Audit Record | Audit may reference Policy | Audit remains accountability system. |

---

# 10. Lifecycle

Policy lifecycle states:

```text
Draft
Active
Suspended
Deprecated
Archived
```

Lifecycle rules:

```text
Draft → Active
Active → Suspended
Suspended → Active
Active → Deprecated
Deprecated → Archived
Draft → Archived
Suspended → Archived
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration service and review
Deprecated → Active without reissue or review
Suspended → Deprecated without reason/source reference
```

---

# 11. Service Usage

Policy object is created, evaluated and managed through:

```text
Policy Registration Service
Policy Update Service
Policy Status Service
Policy Evaluation Service
Policy Scope Validation Service
Policy Reference Validation Service
Policy Audit Reference Service
```

Service rules:

```text
- Services must validate policy_type.
- Services must validate scope_type.
- Services must validate effect.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Evaluation service must return controlled decision.
- Evaluation service must not execute the requested business action.
- Permission evaluation must remain separate.
```

---

# 12. Event Usage

Policy object emits or participates in:

```text
PolicyCreated
PolicyUpdated
PolicyStatusChanged
PolicyDeprecated
PolicyEvaluated
PolicyDenied
PolicyReviewRequired
PolicyApprovalRequired
PolicyAuditRequired
PolicyReferenceValidated
```

Event rules:

```text
- Policy events must reference Policy ID where applicable.
- Evaluation events must preserve scope, context and decision references.
- PolicyDenied events must not expose protected resource details unnecessarily.
- AI policy events must identify AI agent source where applicable.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /policies
GET /policies/{id}
PATCH /policies/{id}
POST /policies/{id}/status
POST /policies/evaluate
POST /policies/reference/validate
```

API rules:

```text
- APIs must invoke Policy Services.
- APIs must not grant Permission.
- APIs must not execute business actions directly.
- APIs must preserve audit context.
- AI-facing APIs must respect Agent Contract.
```

---

# 14. AI Agent Usage

AI Agents may use Policy only under governed Agent Contracts.

Allowed AI use:

```text
request policy evaluation
summarize policy decision if authorized
identify missing policy scope
flag conflicting policies
flag overbroad policy
suggest policy review
```

AI must not:

```text
create policy without authorized service
override Deny or ReviewRequired effect
treat policy as legal opinion
bypass Permission because policy allows context
execute action after policy check without governed service
hide policy review requirement
```

AI policy use requires:

```text
Agent Identity
Agent Contract
Capability Binding where applicable
Permission Rule
Policy Rule
Audit Rule
Human Review Rule for high-risk policy creation, override or interpretation
```

---

# 15. Validation Rules

Policy object must pass:

```text
[ ] id is present and immutable.
[ ] policy_type is controlled.
[ ] scope_type is controlled.
[ ] effect is controlled.
[ ] status is controlled.
[ ] Policy has scope.
[ ] Policy does not grant Permission.
[ ] Policy does not replace Capability.
[ ] Policy does not replace professional judgment.
[ ] Policy evaluation does not execute action.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite policy domain spec
preserve Policy / Permission boundary
preserve Policy / Capability boundary
preserve Policy / Workflow boundary
preserve Policy / Professional Judgment boundary
implement only MVP fields unless task says otherwise
write tests for required scope
write tests for controlled policy_type
write tests for controlled scope_type
write tests for controlled effect
write tests for controlled status
write tests preventing Policy from granting Permission
write tests preventing Policy from executing action
write tests preventing AI from overriding Policy
write tests for event emission on mutation
```

Codex must not:

```text
invent full policy engine beyond approved scope
grant permission through Policy
treat Policy as product setting only
treat Policy as legal opinion or professional truth
bypass Permission evaluation
allow AI policy override without governed review
execute business action from Policy Evaluation Service
allow product UI to redefine Policy status
```

---

# 17. Acceptance Criteria

This Policy Object Specification is accepted only if:

```text
[ ] It defines Policy purpose.
[ ] It defines Policy Core meaning.
[ ] It identifies Policy as Foundation Object.
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
| 0.1.0 | Draft | Initial Policy object specification. Establishes Policy as Core contextual governance object, separates Policy from Permission, Capability, Workflow and professional judgment, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
