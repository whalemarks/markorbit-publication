# Agent Specification — Audit Agent

**Spec ID:** B02-AGENT-AUDIT  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Audit Agent  
**Agent Spec File:** core-specs/agents/audit-agent.md  
**Registry Key:** audit-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Event; Agent; Permission; Policy; Task; Workflow Contract; Communication; Knowledge; Matter; Order; Document; Evidence; Routing  
**Related Object Specs:** core-specs/objects/event.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/communication.md; core-specs/objects/knowledge.md; core-specs/objects/matter.md; core-specs/objects/order.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/routing.md  
**Related Service Specs:** core-specs/services/event-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/communication-service.md; core-specs/services/knowledge-service.md; core-specs/services/matter-service.md; core-specs/services/order-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/routing-service.md  
**Related API Specs:** core-specs/api/event-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/communication-api.md; core-specs/api/knowledge-api.md; core-specs/api/matter-api.md; core-specs/api/order-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/routing-api.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/communication-created.md; core-specs/events/routing-evaluated.md; core-specs/events/routing-selected.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 3 — Business Execution Core  
**MVP Depth:** Should Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Audit Agent defines the governed AI Agent pattern for assisting audit review, event trace explanation, permission/policy trace summarization, workflow trace review, task trace review and compliance-gap detection in MarkOrbit Core.

It exists to help professionals and administrators understand what happened in the system without allowing AI to become compliance authority, legal conclusion maker, event fabricator, hidden data reader, permission evaluator, policy evaluator or source of operational truth.

Audit Agent supports:

```text
event trace summarization
permission/policy decision trace review
workflow trace explanation
task trace explanation
communication trace explanation
routing trace explanation
missing event detection
audit checklist preparation
safe compliance-gap identification
source-scope explanation
```

Audit Agent does not certify compliance, approve legal outcomes, validate evidence sufficiency, fabricate audit records, mutate historical events or override Event Service.

---

# 2. Agent Meaning

Audit Agent means:

```text
a governed AI Agent that assists with safe audit and trace explanation through Event Service boundaries.
```

Audit Agent does not mean:

```text
compliance certification engine
legal conclusion engine
event writer
event mutation tool
permission evaluator
policy evaluator
unrestricted audit log reader
forensic authority
evidence sufficiency judge
professional truth source
```

Audit Agent may help answer:

```text
What events are visible for this object?
What sequence appears from the event trace?
Which permission or policy decisions are referenced?
What gaps or missing references should be reviewed?
What human review may be required?
What downstream service owns the next step?
```

Audit Agent must not claim:

```text
The audit is legally complete.
The compliance issue is resolved.
The evidence is sufficient.
The event definitely occurred if no Event record exists.
The user had permission unless Permission Service records it.
The policy allowed it unless Policy Service records it.
```

---

# 3. Registry Position

Registry entry:

```text
audit-agent
```

Required registry constraints:

```text
agent_type: AuditAgent
agent_role: AuditSupportAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: ReadOnly
```

Allowed capabilities:

```text
Read
Summarize
ExplainTrace
ValidateReference
Suggest
```

Restricted capabilities:

```text
AccessRestrictedContent
AccessRawDocument
AccessEvidence
CreateObject
UpdateObject
CompleteTask
SendCommunication
SelectRouting
```

Registry rule:

```text
Audit Agent may be considered for audit support and trace explanation.
Permission and Policy decide whether it may access specific Event, object, task, workflow, communication, document or evidence context.
```

---

# 4. Agent Boundary

Audit Agent is responsible for:

```text
event reference validation request
safe event trace retrieval request
safe trace summarization
permission/policy trace explanation
workflow trace explanation
task trace explanation
communication trace explanation
routing trace explanation
audit gap checklist preparation
source-scope and omission disclosure
```

Audit Agent is not responsible for:

```text
Event lifecycle ownership
event creation or mutation
permission evaluation
policy evaluation
compliance certification
legal conclusion
evidence sufficiency approval
document verification
task completion
workflow application
communication sending
routing selection
```

---

# 5. Governance Lock

Audit Agent must obey:

```text
Audit Agent may read and explain only Event and related context that Permission and Policy allow.
Audit Agent output is audit-support assistance, not compliance certification or legal conclusion.
Audit Agent must not create, mutate, delete, replay or fabricate Events.
Audit Agent must distinguish recorded trace from inference.
Audit Agent must disclose source scope, missing events, policy omissions and human-review requirements.
```

This lock applies to all Audit Agent implementations.

---

# 6. Agent Identity Requirements

Every Audit Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: audit-agent
agent_contract_reference_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Agent identity must be validated through Agent Service.
- Agent status must be Active or explicitly allowed.
- Agent Contract is required for protected audit access.
- Suspended, revoked, archived or unknown agents must not perform Audit operations.
- Agent must not borrow human User identity.
```

---

# 7. Capability Rules

Allowed operations:

```text
summarizeEventTrace
validateEventReference
explainPermissionTrace
explainPolicyTrace
explainWorkflowTrace
explainTaskTrace
explainCommunicationTrace
explainRoutingTrace
identifyAuditGaps
prepareAuditChecklist
prepareAuditReviewQuestions
```

Disallowed operations:

```text
createEvent
updateEvent
deleteEvent
replayEventAsCommand
fabricateEvent
evaluatePermissionDirectly
evaluatePolicyDirectly
certifyCompliance
approveLegalConclusion
approveEvidenceSufficiency
completeTask
sendCommunication
selectRouting
```

Capability rule:

```text
Audit Agent may explain visible trace; Event Service owns Event records and owning services own domain truth.
```

---

# 8. Data Access Rules

Default data access:

```text
SafeSummaryOnly
```

Allowed data access scopes:

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
```

Restricted data access scopes:

```text
RestrictedContentWithHumanApproval
AccessRawDocument
AccessEvidence
AccessPricing
AccessPrivateContact
AccessFinancialData
```

Rules:

```text
- SafeSummaryOnly is the default.
- Policy may downgrade access to MetadataOnly or NoAccess.
- Event payload details may be restricted by policy.
- Document/Evidence payload access requires owning service policy.
- Permission/Policy internals must not be exposed by default.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
raw event payload where restricted
permission internals
policy internals
privileged legal notes
customer private instructions
unredacted document content
raw evidence packages
payment data
private contacts
provider pricing
API credentials
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:audit:read
event:read
event:search
event:validate
event:trace:explain
permission:decision:read
policy:decision:read
task:read
workflow-contract:read
communication:read
routing:read
matter:read
order:read
document:read
evidence:read
knowledge:read
```

Rules:

```text
- Agent-level permission is required.
- Event-domain permission is required.
- Related domain permission is required where related object context is referenced.
- Restricted Event payload access requires explicit permission.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentEventVisibilityPolicy
EventVisibilityPolicy
EventPayloadVisibilityPolicy
AuditTracePolicy
PermissionDecisionVisibilityPolicy
PolicyDecisionVisibilityPolicy
RestrictedAuditDataPolicy
DocumentVisibilityPolicy
EvidenceVisibilityPolicy
CrossOrganizationAuditPolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether Audit Agent may access Event metadata, safe summary or restricted payload.
- Policy may restrict Permission/Policy decision detail.
- Policy may require human review before audit outputs are used externally.
- Policy may restrict cross-organization or cross-matter audit trace access.
- Policy may require redaction.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Event Trace Summary Request

```yaml
operation: summarizeEventTrace
agent_reference_id: string
agent_registry_key: audit-agent
actor_reference_id: string | null
organization_reference_id: string | null
target_context:
  target_object_type: string
  target_object_reference_id: string
event_scope:
  event_reference_ids: list[string]
  event_types: list[string]
  time_from: datetime | null
  time_to: datetime | null
summary_purpose: string
summary_depth: string
data_access_requested: string
correlation_id: string | null
```

## 11.2 Event Reference Validation Request

```yaml
operation: validateEventReference
agent_reference_id: string
event_reference_id: string
intended_use: string
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

## 11.3 Permission / Policy Trace Request

```yaml
operation: explainPermissionPolicyTrace
agent_reference_id: string
target_context:
  target_object_type: string
  target_object_reference_id: string
permission_decision_reference_ids: list[string]
policy_decision_reference_ids: list[string]
explanation_purpose: string
correlation_id: string | null
```

## 11.4 Audit Gap Review Request

```yaml
operation: identifyAuditGaps
agent_reference_id: string
target_context:
  target_object_type: string
  target_object_reference_id: string
expected_trace_types: list[string]
known_event_reference_ids: list[string]
gap_purpose: string
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Event Trace Summary Response

```yaml
agent_reference_id: string
trace_summary_reference_id: string | null
target_object_type: string
target_object_reference_id: string
safe_trace_summary:
  event_count: integer
  visible_event_types: list[string]
  sequence_summary: string
  important_transitions: list[string]
  missing_or_incomplete_items: list[string]
source_event_reference_ids: list[string]
source_scope: string
policy_omissions: list[string]
confidence_level: string
human_review_required: boolean
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.2 Event Validation Response

```yaml
agent_reference_id: string
event_reference_id: string
valid: boolean
validation_status: string
safe_reason: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Permission / Policy Trace Response

```yaml
agent_reference_id: string
trace_explanation_reference_id: string | null
safe_explanation:
  permission_trace_summary: string | null
  policy_trace_summary: string | null
  missing_decisions: list[string]
  review_notes: list[string]
source_permission_decision_reference_ids: list[string]
source_policy_decision_reference_ids: list[string]
restricted_fields_omitted: boolean
human_review_required: boolean
correlation_id: string | null
```

## 12.4 Audit Gap Response

```yaml
agent_reference_id: string
audit_gap_reference_id: string | null
safe_gap_summary:
  missing_event_types: list[string]
  incomplete_trace_items: list[string]
  suggested_review_questions: list[string]
  downstream_service_required: string | null
source_event_reference_ids: list[string]
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must distinguish recorded trace from inference.
- Responses must not imply compliance certification.
- Responses must disclose missing events and policy omissions.
- Responses must not expose restricted payloads, Permission internals or Policy internals by default.
```

---

# 13. Controlled Values

## 13.1 summary_purpose

```text
InternalReview
AuditReview
WorkflowReview
TaskReview
CommunicationReview
RoutingReview
CompliancePreparation
AIAssistedExplanation
Unknown
```

## 13.2 summary_depth

```text
Brief
Standard
DetailedSafe
RestrictedInternal
Unknown
```

## 13.3 explanation_purpose

```text
InternalReview
AuditReview
Debugging
GovernanceReview
CompliancePreparation
AIAssistedExplanation
Unknown
```

## 13.4 gap_purpose

```text
TraceCompleteness
WorkflowCompleteness
TaskCompleteness
PermissionPolicyCoverage
CommunicationTraceReview
RoutingTraceReview
CompliancePreparation
Unknown
```

## 13.5 source_scope

```text
EventMetadataOnly
EventSafeSummary
PolicyFilteredEventPayload
TaskTrace
WorkflowTrace
CommunicationTrace
RoutingTrace
CrossObjectTrace
Unknown
```

## 13.6 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
ContextMismatch
Unknown
```

## 13.7 confidence_level

```text
Low
Medium
High
Unknown
```

## 13.8 data_access_requested

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
RestrictedContentWithHumanApproval
Unknown
```

---

# 14. Human Review Rules

Human review is required when Audit Agent output may be used for:

```text
external audit report
legal or compliance conclusion
customer-facing explanation
regulator-facing explanation
dispute handling
evidence sufficiency conclusion
professional accountability determination
restricted payload use
cross-organization disclosure
```

Human review is not required for:

```text
safe internal event summary
safe metadata lookup
non-state-changing trace checklist
reference validation where no restricted payload is exposed
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit before external or compliance use.
- Human review reference must be preserved where audit output is used downstream.
```

---

# 15. Event and Audit Rules

Audit Agent operations must themselves be traceable.

Trace must include:

```yaml
agent_registry_key: audit-agent
agent_reference_id: string
operation: string
target_object_type: string | null
target_object_reference_id: string | null
event_reference_ids: list[string]
permission_decision_reference_ids: list[string]
policy_decision_reference_ids: list[string]
data_access_scope: string
execution_mode: string
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Audit Agent must not emit domain events directly.
- Event Service owns event recording.
- Audit trace must distinguish source events from AI summary.
- Audit Agent must not mutate or replay historical events.
```

---

# 16. Relationship to Event Service

Audit Agent must use Event Service for:

```text
getEvent
searchEvents
validateEventReference
listObjectEvents
explainEventTrace
```

Rules:

```text
- Audit Agent must not query or mutate event store directly.
- Event Service applies Event domain rules.
- Permission and Policy are evaluated before protected Event access.
- Audit Agent may transform safe event results into summaries, gap checklists or explanations.
```

---

# 17. Relationship to Permission and Policy Services

Audit Agent may reference Permission and Policy decisions only through governed service access.

Rules:

```text
- Permission Service owns Permission evaluation records.
- Policy Service owns Policy evaluation records.
- Audit Agent must not re-evaluate permission or policy.
- Audit Agent must not expose permission/policy internals by default.
- Audit Agent may explain safe decision trace where allowed.
```

---

# 18. Relationship to Domain Services

Audit Agent may reference domain context only through governed service access.

Related domain services may include:

```text
Task Service
Workflow Contract Service
Communication Service
Routing Service
Matter Service
Order Service
Document Service
Evidence Service
Knowledge Service
```

Rules:

```text
- Domain services own domain truth.
- Audit Agent may summarize visible traces.
- Audit Agent must not mutate domain state.
- Audit Agent must not certify domain correctness.
- Document/Evidence detail access requires owning service Permission and Policy.
```

---

# 19. Error and Rejection Rules

Controlled rejection reasons:

```text
PermissionDenied
PolicyRestricted
AgentSuspended
AgentRevoked
AgentContractRequired
CapabilityNotAllowed
HumanReviewRequired
RestrictedDataRequested
EventReferenceInvalid
PermissionDecisionReferenceInvalid
PolicyDecisionReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden Event payload.
- Rejections must not expose Permission or Policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Audit Agent spec
cite Event Service Specification
cite Event Object Specification
cite Event API Specification
cite Permission and Policy specs
validate agent_registry_key = audit-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected Event access
invoke Policy Service before Event payload access
use SafeSummaryOnly by default
mark AI-generated audit summaries and explanations
preserve source event references in output
distinguish recorded trace from inference
disclose missing events and policy omissions
route Event access through Event Service
route domain context access through owning services
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for HumanReviewRequired
write tests for restricted payload omission
write tests for invalid Event reference
write tests that Audit Agent cannot create, mutate or delete Events
write tests that Audit Agent cannot certify compliance or legal conclusion
write tests that Audit Agent cannot re-evaluate Permission or Policy directly
```

Codex must not:

```text
query Event database directly
bypass Event Service
bypass Permission or Policy
pass unrestricted event payloads into prompts
treat AI audit summary as compliance certification
fabricate missing events
mutate or replay events
expose Permission/Policy internals for convenience
approve evidence sufficiency
emit domain events directly
```

---

# 21. Acceptance Criteria

This Audit Agent Specification is accepted only if:

```text
[ ] It defines Audit Agent purpose.
[ ] It defines Agent meaning.
[ ] It defines registry position.
[ ] It defines Agent boundary.
[ ] It defines governance lock.
[ ] It defines identity requirements.
[ ] It defines capability rules.
[ ] It defines data access rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines request patterns.
[ ] It defines response patterns.
[ ] It defines controlled values.
[ ] It defines human review rules.
[ ] It defines event and audit rules.
[ ] It defines relationship to Event Service.
[ ] It defines relationship to Permission and Policy Services.
[ ] It defines relationship to Domain Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Audit Agent specification. Defines governed event trace summarization, permission/policy trace explanation, audit gap detection and compliance-support boundaries under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
