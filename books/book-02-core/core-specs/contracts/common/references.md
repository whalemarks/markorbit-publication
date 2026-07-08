# Common Contract — References

**Spec ID:** B02-CONTRACT-COMMON-REFERENCES  
**Spec Type:** Common Contract Specification  
**Contract Name:** Reference Contract  
**Contract File:** core-specs/contracts/common/references.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** All Core object specifications  
**Related Service Specs:** All Core service specifications  
**Related API Specs:** All Core API specifications  
**Related Event Specs:** All Core event specifications  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Reference Contract defines the canonical reference field rules used across MarkOrbit Core.

It standardizes how domain objects, services, APIs, events, agents, workflows and validation contracts identify and link to one another without merging domain ownership or relying on ambiguous generic IDs.

This contract governs:

```text
reference field naming
domain-specific reference IDs
cross-domain reference shape
target object references
subject references
actor references
organization references
agent references
event references
reference validation responsibility
deleted/archived reference behavior
safe reference exposure
```

Reference Contract does not define database primary keys, storage technology, UI labels or business lifecycle ownership.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for naming, passing, validating and interpreting references between Core domains.
```

This contract does not mean:

```text
database schema
foreign-key implementation only
object ownership transfer
permission grant
policy approval
event creation
domain merge
generic ID convention
```

Core rule:

```text
A reference identifies.
The owning domain validates.
The owning service controls lifecycle.
The consuming service must not assume ownership.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
canonical reference field names
explicit domain reference naming
target reference shape
subject reference shape
actor reference shape
agent reference shape
correlation reference shape
reference validation rules
cross-domain reference rules
reference error rules
safe exposure rules
```

This contract is not responsible for:

```text
creating referenced objects
owning referenced object state
evaluating permission
evaluating policy
executing cross-domain behavior
choosing database keys
creating event payloads directly
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Owning rule:

```text
The Contracts layer defines enforceable shape. This Reference Contract provides the common reference shape used by API, Service, Event, Agent, Workflow and Validation contracts.
```

---

# 5. Related Core Objects

This contract applies to references for all baseline Core objects:

```text
identity
organization
user
permission
policy
knowledge
brand
trademark
jurisdiction
classification
document
evidence
customer
matter
order
opportunity
workflow-contract
task
event
notification
communication
agent
service-provider
routing
partner
service-network
```

It also supports cross-cutting references:

```text
capability
business-responsibility
human-review
permission-decision
policy-decision
agent-contract
workflow-application
routing-selection
```

---

# 6. Required References

Common reference context shape:

```yaml
reference_context:
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_contract_reference_id: string | null
  target_object_type: string | null
  target_object_reference_id: string | null
  subject_object_type: string | null
  subject_object_reference_id: string | null
  permission_decision_reference_id: string | null
  policy_decision_reference_id: string | null
  human_review_reference_id: string | null
  correlation_id: string | null
```

Rules:

```text
- Required references depend on operation type.
- Protected operations require actor_reference_id or approved system/agent context.
- Organization-scoped operations require organization_reference_id.
- Agent-assisted operations require agent_reference_id and agent_registry_key where applicable.
- Cross-object operations require target_object_type and target_object_reference_id.
```

---

# 7. Contract Shape

Canonical reference field shape:

```yaml
reference:
  reference_id: string
  reference_type: string
  reference_domain: string
  reference_status: string | null
  safe_label: string | null
  restricted_fields_omitted: boolean
```

Canonical typed reference shape:

```yaml
typed_reference:
  object_type: string
  object_reference_id: string
  object_status: string | null
  safe_label: string | null
  owner_service: string | null
  restricted_fields_omitted: boolean
```

Canonical cross-domain reference shape:

```yaml
cross_domain_reference:
  source_object_type: string
  source_object_reference_id: string
  target_object_type: string
  target_object_reference_id: string
  relationship_type: string
  relationship_status: string | null
  validation_status: string | null
```

Rules:

```text
- reference_id alone is not sufficient when domain meaning is known.
- object_type must be controlled.
- object_reference_id must use the matching domain reference.
- safe_label must not expose restricted data.
- owner_service identifies validation authority, not ownership transfer.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| reference_id | string | Contextual | No | Generic only when domain is not yet known. Prefer typed domain references. |
| reference_type | string | Contextual | No | Must use controlled reference type. |
| reference_domain | string | Contextual | No | Must map to a Core domain or cross-cutting system. |
| object_type | string | Yes for typed reference | No | Must use controlled object type. |
| object_reference_id | string | Yes for typed reference | No | Must match object_type. |
| source_object_type | string | Yes for cross-domain link | No | Must use controlled object type. |
| source_object_reference_id | string | Yes for cross-domain link | No | Must match source_object_type. |
| target_object_type | string | Yes for target operations | No | Must use controlled object type. |
| target_object_reference_id | string | Yes for target operations | No | Must match target_object_type. |
| relationship_type | string | Contextual | No | Must use owning contract controlled values. |
| validation_status | string | Contextual | Yes | Must use controlled validation status. |
| safe_label | string | No | Yes | Must not expose restricted data. |
| restricted_fields_omitted | boolean | Yes where safe response is returned | No | Must be true when fields are omitted by policy. |

---

# 9. Controlled Values

## 9.1 object_type

```text
Identity
Organization
User
Permission
Policy
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Matter
Order
Opportunity
WorkflowContract
Task
Event
Notification
Communication
Agent
ServiceProvider
Routing
Partner
ServiceNetwork
Capability
BusinessResponsibility
HumanReview
PermissionDecision
PolicyDecision
AgentContract
WorkflowApplication
RoutingSelection
Unknown
```

## 9.2 reference_domain

```text
identity
organization
user
permission
policy
knowledge
brand
trademark
jurisdiction
classification
document
evidence
customer
matter
order
opportunity
workflow-contract
task
event
notification
communication
agent
service-provider
routing
partner
service-network
capability
business-responsibility
human-review
permission-decision
policy-decision
agent-contract
workflow-application
routing-selection
unknown
```

## 9.3 reference_status

```text
Active
Draft
ReviewRequired
Suspended
Archived
DeletedReferenceOnly
Deprecated
Revoked
Invalid
Unknown
```

## 9.4 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
DeletedReferenceOnly
ContextMismatch
Unknown
```

## 9.5 relationship_status

```text
Draft
Active
ReviewRequired
Suspended
Archived
DeletedReferenceOnly
Invalid
Unknown
```

---

# 10. Canonical Domain Reference Fields

Domain reference fields must use these names:

```yaml
identity_reference_id: string
organization_reference_id: string
user_reference_id: string
permission_reference_id: string
policy_reference_id: string
knowledge_record_reference_id: string
brand_reference_id: string
trademark_reference_id: string
jurisdiction_reference_id: string
classification_reference_id: string
document_reference_id: string
evidence_reference_id: string
customer_reference_id: string
matter_reference_id: string
order_reference_id: string
opportunity_reference_id: string
workflow_contract_reference_id: string
task_reference_id: string
event_reference_id: string
notification_reference_id: string
communication_reference_id: string
agent_reference_id: string
service_provider_reference_id: string
routing_reference_id: string
partner_reference_id: string
service_network_reference_id: string
```

Cross-cutting reference fields:

```yaml
capability_reference_id: string
business_responsibility_reference_id: string
human_review_reference_id: string
permission_decision_reference_id: string
policy_decision_reference_id: string
agent_contract_reference_id: string
workflow_application_reference_id: string
routing_selection_reference_id: string
```

Rules:

```text
- Do not use generic id where a domain-specific reference is known.
- Do not use database primary key names in public Core contracts.
- Do not use foreign system IDs as Core reference IDs.
- External IDs must be placed in external_reference fields.
```

---

# 11. Reference Validation Rules

Validation checklist:

```text
[ ] Reference field name matches domain.
[ ] object_type matches object_reference_id field.
[ ] reference_domain matches object_type.
[ ] reference_id format is valid.
[ ] referenced object exists or is allowed as DeletedReferenceOnly.
[ ] referenced object status is allowed for intended use.
[ ] actor has permission to use the reference.
[ ] policy allows reference visibility/use.
[ ] cross-domain relationship is allowed by owning services.
[ ] archived/deleted references are handled according to owning domain policy.
[ ] safe_label does not expose restricted data.
```

Validation authority:

```text
The owning service validates its own references.
```

Examples:

```text
Task Service validates task_reference_id.
Order Service validates order_reference_id.
Communication Service validates communication_reference_id.
Agent Service validates agent_reference_id.
Routing Service validates routing_reference_id.
```

---

# 12. Cross-Domain Reference Rules

Cross-domain references must not imply ownership transfer.

Rules:

```text
- A Matter may reference Customer, but Matter does not own Customer.
- An Order may reference Matter, but Order does not own Matter professional truth.
- A Task may reference Order or Matter, but Task does not own Order or Matter lifecycle.
- Communication may reference Task, Matter or Order, but Communication is not task completion.
- Routing may reference Service Provider, but Routing does not own Service Provider lifecycle.
- Agent may reference Task or Knowledge context, but Agent does not own those objects.
```

Cross-domain validation flow:

```text
consuming service receives reference
↓
consuming service checks local contract
↓
owning service validates referenced object
↓
Permission Service evaluates use
↓
Policy Service evaluates visibility/context
↓
consuming service continues or rejects
```

---

# 13. Permission Rules

Reference use may require permissions such as:

```text
<object-domain>:read
<object-domain>:validate
<object-domain>:link
<object-domain>:reference:use
```

Rules:

```text
- This contract does not grant permission.
- Permission Service evaluates reference use.
- A valid reference does not imply actor may access it.
- A readable reference does not imply actor may mutate it.
- PermissionDenied must stop protected reference use.
```

---

# 14. Policy Rules

Reference visibility and use may be policy-restricted.

Rules:

```text
- Policy may allow reference existence but hide safe_label.
- Policy may allow metadata reference but block payload access.
- Policy may block cross-organization reference use.
- Policy may require human review for reference linking.
- PolicyRestricted must stop or downgrade reference use.
```

Common policies:

```text
ReferenceVisibilityPolicy
CrossOrganizationReferencePolicy
RestrictedReferenceDataPolicy
ReferenceLinkPolicy
AIAgentReferenceAccessPolicy
```

---

# 15. AI Agent Rules

AI Agent reference use must include explicit agent context where applicable:

```yaml
ai_reference_context:
  ai_assisted: boolean
  agent_reference_id: string
  agent_registry_key: string
  agent_contract_reference_id: string | null
  intended_use: string
  data_access_scope: string
```

Rules:

```text
- AI must not fabricate references.
- AI must not infer one reference from another unless owning service confirms it.
- AI must not access referenced objects beyond evaluated data access scope.
- AI output must preserve source references used.
- AI must disclose missing or invalid references.
```

---

# 16. Event Rules

Event references must follow event-specific rules:

```yaml
event_reference:
  event_reference_id: string
  event_type: string
  event_subject_type: string
  event_subject_reference_id: string
  event_producer_service: string
```

Rules:

```text
- Event references are audit trace, not commands.
- Events must not be replayed as commands unless a command contract explicitly allows it.
- Event payload visibility may be restricted.
- Event Service validates event_reference_id.
```

---

# 17. Error Rules

Controlled reference errors:

```text
ReferenceInvalid
ReferenceNotFound
ReferenceTypeMismatch
ReferenceDomainMismatch
ReferenceStatusInvalid
ReferenceContextMismatch
ReferencePermissionDenied
ReferencePolicyRestricted
ReferenceArchived
ReferenceDeletedReferenceOnly
CrossDomainReferenceNotAllowed
ExternalReferenceInvalid
```

Safe error shape:

```yaml
error:
  code: string
  category: Reference
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must not disclose restricted object existence where policy forbids it.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
- Errors must not expose internal database IDs.
```

---

# 18. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding a new reference_domain requires revision notes.
- Adding a new object_type requires revision notes.
- Renaming a reference field is breaking.
- Changing reference validation meaning is breaking.
- Removing Unknown requires migration plan.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Reference Contract before implementing cross-domain references
use canonical reference field names
generate typed reference validators
reject object_type/reference_id mismatches
validate cross-domain references through owning services
preserve correlation_id
preserve reference trace in AI outputs
write tests for invalid reference field names
write tests for object_type mismatch
write tests for NotFound
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for archived/deleted references
write tests that generic id is not used where domain reference is known
```

Codex must not:

```text
use generic id in public contract where domain meaning is known
reuse one domain reference as another domain reference
infer foreign keys without owning service validation
expose database IDs in API responses
treat valid reference as permission grant
treat Event reference as command
allow AI to fabricate references
```

---

# 20. Acceptance Criteria

This Reference Contract is accepted only if:

```text
[ ] It defines reference purpose.
[ ] It defines reference meaning.
[ ] It defines reference boundary.
[ ] It defines related owning spec.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines contract shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines canonical domain reference fields.
[ ] It defines reference validation rules.
[ ] It defines cross-domain reference rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Reference Contract. Defines canonical reference names, typed reference shapes, cross-domain reference behavior, validation, permission/policy, AI, event, error and Codex implementation rules. |

---

**End of Common Contract**
