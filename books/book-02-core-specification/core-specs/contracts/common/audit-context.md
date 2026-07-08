# Common Contract — Audit Context

**Spec ID:** B02-CONTRACT-COMMON-AUDIT-CONTEXT  
**Spec Type:** Common Contract Specification  
**Contract Name:** Audit Context Contract  
**Contract File:** core-specs/contracts/common/audit-context.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** core-specs/objects/event.md; core-specs/objects/agent.md; core-specs/objects/user.md; core-specs/objects/organization.md; all Core object specifications where audit trace is required  
**Related Service Specs:** core-specs/services/event-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; all Core service specifications where auditable operations exist  
**Related API Specs:** core-specs/api/event-api.md; all Core API specifications where auditable operations exist  
**Related Event Specs:** All Core event specifications  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/audit-agent.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Audit Context Contract defines the canonical audit context shape used across MarkOrbit Core.

It standardizes how APIs, services, events, workflows, agents and validators preserve trace information for who acted, what object was affected, under what organization, through which agent or system context, with which permission/policy decision, and under which correlation chain.

This contract governs:

```text
actor trace
organization trace
agent trace
target object trace
subject object trace
operation trace
permission decision trace
policy decision trace
human review trace
correlation trace
idempotency trace
source trace
event trace linkage
safe audit exposure
Codex implementation rules
```

Audit Context Contract does not create events, certify compliance, approve legal conclusions, replace Event Service or expose restricted audit payloads.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for carrying auditable context across governed operations.
```

This contract does not mean:

```text
audit report
compliance certification
event payload by itself
debug log
database log
security incident record
professional conclusion
permission grant
policy approval
```

Core rule:

```text
Audit context preserves trace.
Event Service records events.
Owning services define operation truth.
Audit context is not compliance certification by itself.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
audit context field names
operation trace shape
actor and agent trace shape
target/subject object trace shape
permission/policy decision reference shape
human review reference shape
correlation and idempotency trace
safe source attribution
event linkage
audit context validation
```

This contract is not responsible for:

```text
event creation
event payload design
permission evaluation
policy evaluation
business state transition
legal conclusion
compliance certification
database logging implementation
security monitoring implementation
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related common contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/ai-context.md
```

Owning rule:

```text
Audit context must preserve Core responsibility boundaries and must not imply operation success, permission approval, policy approval, event emission or compliance certification.
```

---

# 5. Related Core Objects

Primary related objects:

```text
Event
Agent
User
Organization
Permission
Policy
Task
WorkflowContract
Communication
Routing
Matter
Order
Document
Evidence
Knowledge
```

Rules:

```text
- Event object owns recorded event trace.
- Audit context may reference event_reference_id but does not become Event.
- User and Agent must remain distinct.
- Target and subject object references must follow Reference Contract.
```

---

# 6. Required References

Audit context may include these references:

```yaml
audit_context:
  audit_context_reference_id: string | null
  actor_reference_id: string | null
  actor_type: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  agent_contract_reference_id: string | null
  operation_name: string
  operation_category: string
  target_object_type: string | null
  target_object_reference_id: string | null
  subject_object_type: string | null
  subject_object_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  human_review_reference_id: string | null
  event_reference_ids: list[string]
  source_type: string | null
  source_reference_id: string | null
  correlation_id: string | null
  causation_id: string | null
  idempotency_key: string | null
  requested_at: datetime | null
  completed_at: datetime | null
```

Rules:

```text
- operation_name is required for auditable operations.
- operation_category is required for auditable operations.
- actor_reference_id or approved system/agent context is required for protected operations.
- agent_reference_id is required for AI/agent-assisted operations.
- permission_decision_reference_id is required where permission was evaluated and exposed safely.
- policy_decision_reference_id is required where policy was evaluated and exposed safely.
```

---

# 7. Contract Shape

Canonical audit context shape:

```yaml
audit_context:
  audit_context_reference_id: string | null
  operation:
    operation_name: string
    operation_category: string
    operation_result: string | null
  actor:
    actor_type: string | null
    actor_reference_id: string | null
    organization_reference_id: string | null
  agent:
    ai_assisted: boolean | null
    agent_reference_id: string | null
    agent_registry_key: string | null
    agent_contract_reference_id: string | null
  target:
    target_object_type: string | null
    target_object_reference_id: string | null
  subject:
    subject_object_type: string | null
    subject_object_reference_id: string | null
  governance:
    permission_decision_reference_id: string | null
    policy_decision_reference_id: string | null
    human_review_reference_id: string | null
  trace:
    correlation_id: string | null
    causation_id: string | null
    idempotency_key: string | null
    event_reference_ids: list[string]
  source:
    source_type: string | null
    source_reference_id: string | null
  timestamps:
    requested_at: datetime | null
    completed_at: datetime | null
```

Safe audit summary shape:

```yaml
safe_audit_summary:
  operation_name: string
  operation_category: string
  operation_result: string | null
  actor_type: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  event_count: integer
  restricted_fields_omitted: boolean
  correlation_id: string | null
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| operation_name | string | Yes | No | Must identify operation safely. |
| operation_category | string | Yes | No | Must use controlled value. |
| operation_result | string | Contextual | Yes | Must use controlled value where provided. |
| actor_type | string | Contextual | Yes | Required unless system-only context is valid. |
| actor_reference_id | string | Contextual | Yes | Must not be confused with agent_reference_id. |
| organization_reference_id | string | Contextual | Yes | Required for organization-scoped audit. |
| agent_reference_id | string | Contextual | Yes | Required for agent-assisted operations. |
| target_object_type | string | Contextual | Yes | Must follow Reference Contract. |
| target_object_reference_id | string | Contextual | Yes | Must match target_object_type. |
| subject_object_type | string | Contextual | Yes | Must follow Reference Contract. |
| subject_object_reference_id | string | Contextual | Yes | Must match subject_object_type. |
| permission_decision_reference_id | string | Contextual | Yes | May be omitted where policy restricts exposure. |
| policy_decision_reference_id | string | Contextual | Yes | May be omitted where policy restricts exposure. |
| human_review_reference_id | string | Contextual | Yes | Required where action depends on human review. |
| correlation_id | string | Contextual | Yes | Must be preserved where provided. |
| causation_id | string | No | Yes | Used to link caused operations/events. |
| idempotency_key | string | Contextual | Yes | Must be preserved for idempotent operations. |
| event_reference_ids | list[string] | No | No | Empty list if none exposed. |

---

# 9. Controlled Values

## 9.1 operation_category

```text
Create
Read
Search
Update
Delete
Validate
Evaluate
Apply
Prepare
Draft
Review
Approve
Reject
Link
Unlink
Assign
TransitionState
EmitEvent
ObserveEvent
AgentAction
WorkflowAction
SystemAction
Unknown
```

## 9.2 operation_result

```text
Succeeded
Failed
Rejected
Prepared
Drafted
Validated
Invalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
DownstreamServiceRequired
PartiallyCompleted
Unknown
```

## 9.3 actor_type

```text
User
Agent
System
Integration
Service
Unknown
```

## 9.4 source_type

```text
APIRequest
ServiceOperation
Event
Workflow
Agent
SystemJob
Migration
ExternalIntegration
ProfessionalInput
Unknown
```

Rules:

```text
- Unknown is allowed only as temporary draft/diagnostic value.
- Production contracts should use specific controlled values.
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] operation_name is present.
[ ] operation_category is controlled.
[ ] operation_result is controlled where provided.
[ ] actor_type is controlled where provided.
[ ] actor_reference_id and agent_reference_id are not confused.
[ ] organization_reference_id is valid where provided.
[ ] target_object_type and target_object_reference_id match.
[ ] subject_object_type and subject_object_reference_id match.
[ ] references follow Reference Contract.
[ ] permission_decision_reference_id is safe to expose where included.
[ ] policy_decision_reference_id is safe to expose where included.
[ ] human_review_reference_id is present where required.
[ ] correlation_id is preserved where available.
[ ] idempotency_key is preserved where applicable.
[ ] event_reference_ids are valid where provided.
[ ] restricted audit fields are omitted unless policy allows them.
```

---

# 11. Permission Rules

Audit context use may require:

```text
audit:read
event:read
event:trace:read
permission:decision:read
policy:decision:read
<object-domain>:read
```

Rules:

```text
- Audit context does not grant permission.
- Permission Service evaluates access to audit context.
- Permission decisions may be referenced but not exposed in detail by default.
- PermissionDenied must stop protected audit context access.
```

---

# 12. Policy Rules

Audit context visibility is policy-controlled.

Common policies:

```text
AuditContextVisibilityPolicy
EventVisibilityPolicy
PermissionDecisionVisibilityPolicy
PolicyDecisionVisibilityPolicy
RestrictedAuditDataPolicy
CrossOrganizationAuditPolicy
AIAgentAuditAccessPolicy
```

Rules:

```text
- Policy may hide actor, agent, decision, event or source references.
- Policy may downgrade audit context to safe summary.
- Policy may require human review before external audit output.
- Policy may return NotFound where existence disclosure is restricted.
```

---

# 13. AI Agent Rules

AI Agent audit context must include:

```yaml
agent:
  ai_assisted: true
  agent_reference_id: string
  agent_registry_key: string
  agent_contract_reference_id: string | null
```

Rules:

```text
- AI-generated output must preserve audit context.
- AI must not fabricate audit_context_reference_id or event_reference_ids.
- AI must distinguish recorded trace from inference.
- AI must not expose restricted audit context beyond data access scope.
- Audit Agent must use this contract when preparing trace summaries.
```

---

# 14. Event Rules

Audit context may reference Events but must not create them.

Rules:

```text
- Event Service owns Event records.
- event_reference_ids are trace references, not commands.
- Audit context may be included in event payloads where event specs allow.
- Event payload visibility may be more restricted than audit context visibility.
- Event emission success/failure must be represented separately from business operation success where relevant.
```

---

# 15. Error Rules

Controlled audit context errors:

```text
AuditContextInvalid
AuditContextRestricted
AuditContextReferenceInvalid
AuditContextPermissionDenied
AuditContextPolicyRestricted
AuditActorInvalid
AuditTargetInvalid
AuditEventReferenceInvalid
AuditDecisionReferenceRestricted
```

Safe error shape:

```yaml
error:
  code: string
  category: Validation | Reference | Permission | Policy | Event
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose restricted actor, agent, permission or policy internals.
- Errors must not expose hidden event payload.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding operation_category values requires revision notes.
- Adding operation_result values requires revision notes.
- Renaming audit fields is breaking.
- Changing audit context meaning is breaking.
- Changing safe audit summary shape is breaking unless backward compatible.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this Audit Context Contract before implementing auditable operations
preserve correlation_id
preserve causation_id where supplied
preserve idempotency_key where applicable
differentiate actor_reference_id from agent_reference_id
use Reference Contract for target/subject references
use Error Contract for audit errors
route event validation through Event Service
apply Permission before exposing audit context
apply Policy before exposing audit context
produce safe audit summaries where full audit context is restricted
write tests for missing operation_name
write tests for invalid operation_category
write tests for actor/agent distinction
write tests for invalid target reference
write tests for hidden permission/policy decision references
write tests for restricted audit fields omitted
```

Codex must not:

```text
treat audit context as Event
create event records from audit context directly
expose raw audit payloads by default
expose permission or policy internals
merge user and agent identity
drop correlation_id
use database log records as public audit context without sanitization
allow AI to fabricate audit references
```

---

# 18. Acceptance Criteria

This Audit Context Contract is accepted only if:

```text
[ ] It defines audit context purpose.
[ ] It defines audit context meaning.
[ ] It defines audit context boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical audit context shape.
[ ] It defines safe audit summary shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Audit Context Contract. Defines canonical audit context shape, safe audit summary, operation/actor/agent/target/governance/trace/source fields, validation, permission/policy, AI, event, error and Codex rules. |

---

**End of Common Contract**
