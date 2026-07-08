# Event Specification Template

**Spec ID:** B02-EVT-[EVENT-NAME]  
**Spec Type:** Event  
**Event Name:** [ObjectActionPastTense]  
**Event File:** core-specs/events/[object-action-past-tense].md  
**Event Category:** [DomainEvent / WorkflowEvent / TaskEvent / StatusEvent / LinkEvent / ReviewEvent / ApprovalEvent / NotificationTriggerEvent / CommunicationTriggerEvent / AIAgentEvent / SystemEvent / IntegrationEvent]  
**Owning Domain:** [Domain Name]  
**Producing Service:** core-specs/services/[service-name].md  
**Related Object Specs:** core-specs/objects/[object].md  
**Related Service Specs:** core-specs/services/[service].md  
**Related API Specs:** core-specs/api/[api].md  
**Related Agent Specs:** core-specs/agents/[agent].md  
**Payload Contract:** core-specs/contracts/events/[object-action-past-tense]-payload.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** [Phase 1 / Phase 2 / Phase 3 / Phase 4 / Phase 5 Reserved]  
**MVP Depth:** [Must Implement / Partial Implement / Reference Only / Reserved]  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Event exists.

This section must answer:

```text
what meaningful occurrence this Event records
which Core service operation produces it
which Core object reference is involved
why downstream consumers need this Event
why this Event is not merely an implementation log
```

Template rule:

```text
[Event Name] records that [specific governed occurrence] happened.
It is produced by [Producing Service] after [operation] succeeds.
It allows [consumers] to react under governed contracts.
```

---

# 2. Event Meaning

Define the Core meaning of the Event.

```text
[Event Name] means that [precise business occurrence] has occurred under governed Core operation.
```

Also define what it does not mean:

```text
[Event Name] does not mean:
- the next task has been executed
- the workflow has advanced unless explicitly stated
- notification has been delivered
- communication has been sent
- audit has been completed
- AI has made a final professional decision
```

---

# 3. Event Category

Select one controlled event category:

```text
DomainEvent
WorkflowEvent
TaskEvent
StatusEvent
LinkEvent
ReviewEvent
ApprovalEvent
NotificationTriggerEvent
CommunicationTriggerEvent
AIAgentEvent
SystemEvent
IntegrationEvent
Unknown
```

Explain why this category applies.

Example:

```text
This is a StatusEvent because it records a governed lifecycle status change of [object].
```

---

# 4. Event Producer

Define the producer.

```text
Producing Service: [Service Name]
Producing Operation: [operationName]
Source Domain: [Domain Name]
Source Object Type: [Object Type]
```

Allowed producers:

```text
Core Service
Domain Service
API Layer through service operation
AI Agent through governed service operation
System Process through governed service operation
External Integration through integration contract
```

Producer rules:

```text
- Event must be emitted only after the producing operation succeeds.
- Event must not be emitted directly by product UI.
- Event must not be emitted directly by AI unless through governed service operation.
- Event must include actor_context and source_context.
```

---

# 5. Event Trigger

Define the precise trigger condition.

Trigger must include:

```text
operation completed
validation passed
object reference created/updated/linked/status changed
required permission/policy checks completed where applicable
transaction boundary where applicable
```

Example:

```text
This Event is triggered when [Service].[operation] successfully creates [Object] and commits the governed object reference.
```

Non-triggers:

```text
- UI button clicked
- draft form opened
- AI suggestion generated but not accepted
- debug log written
- failed validation
- unauthorized operation attempt
```

Failed attempts should use separate rejection/failure events where required.

---

# 6. Event Payload

Define payload fields.

Minimum payload:

```yaml
event_id: string
event_name: string
event_category: string
event_version: string
occurred_at: datetime
source_domain: string
source_service: string
source_operation: string
source_object_type: string
source_object_reference_id: string
actor_reference_id: string
organization_reference_id: string | null
correlation_id: string | null
causation_id: string | null
payload_contract_reference_id: string
safe_summary: object
restricted_fields_policy: string
metadata: object
```

Event-specific payload:

```yaml
# Add event-specific safe fields here.
[object_reference_id]: string
[status_before]: string | null
[status_after]: string | null
[relationship_reference_id]: string | null
[reason_code]: string | null
```

Payload rules:

```text
- Payload must follow the payload contract.
- Payload must use references rather than full object snapshots by default.
- Payload must not expose restricted content unnecessarily.
- Payload must not include raw document/evidence content.
- Payload must not include hidden AI reasoning.
```

---

# 7. Required References

List required references.

Required Core references:

```text
event_id
source_object_reference_id
actor_reference_id
payload_contract_reference_id
```

Optional references:

```text
organization_reference_id
matter_reference_id
order_reference_id
task_reference_id
workflow_contract_reference_id
customer_reference_id
agent_reference_id
service_provider_reference_id
communication_reference_id
notification_reference_id
policy_decision_reference_id
permission_decision_reference_id
agent_contract_reference_id
```

Reference rules:

```text
- Required references must be stable IDs.
- Missing required references must reject event creation.
- Related references must not embed confidential data.
- DeletedReferenceOnly objects may be referenced only when policy allows.
```

---

# 8. Controlled Values

Define controlled values used by this Event.

## 8.1 event_name

```text
[ObjectActionPastTense]
```

## 8.2 event_category

```text
[SelectedCategory]
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

## 8.4 reason_code

```text
Success
ValidationPassed
StatusChanged
ReferenceLinked
ReferenceValidated
ReviewRequired
PolicyRestricted
PermissionRequired
SystemGenerated
AIGenerated
Unknown
```

Add event-specific controlled values where required.

---

# 9. Event Rules

Define event-specific rules.

Baseline rules:

```text
- Event records occurrence only.
- Event does not execute work.
- Event does not grant Permission.
- Event does not bypass Policy.
- Event does not replace Audit.
- Event does not create Notification or Communication by itself.
- Event does not advance Workflow unless the producing service operation has done so.
- Event must be immutable except controlled metadata/status fields.
```

Event-specific rules:

```text
- [Add rule]
- [Add rule]
- [Add rule]
```

---

# 10. Consumer Rules

Define who may consume this Event and how.

Allowed consumers:

```text
Notification Service
Communication Service
Task Service
Workflow Contract Service
Audit Service
AI Agent under Agent Contract
Product UI read model
Integration service under API contract
```

Consumer rules:

```text
- Consumers must respect Permission and Policy.
- Consumers must not reinterpret Event meaning.
- Consumers must not treat Event as command.
- Consumers must not expose restricted payload fields.
- AI consumers must use Agent Contract and Authorized Knowledge.
```

Consumer reactions must be explicit:

```text
Notification Service may create awareness intent.
Communication Service may prepare message lifecycle.
Task Service may create/recommend task only under workflow/policy.
Audit Service may record accountability trace.
AI Agent may summarize or flag next step for review.
```

---

# 11. Relationship to Services

Describe relationship to services.

```text
Producing Service:
- [Service] produces this Event after [operation].

Event Service:
- records, validates and dispatches this Event.

Related Services:
- [Service] may consume this Event for [purpose].
- [Service] must not consume this Event for [forbidden purpose].
```

Boundary reminders:

```text
Event Service records Event.
Producing Service owns business operation.
Consumer Service owns reaction.
Audit Service owns accountability.
```

---

# 12. Relationship to APIs

Define API usage.

Possible API exposure:

```text
GET /events/{event_id}
GET /[objects]/{id}/events
POST /events/reference/validate
```

API rules:

```text
- API must not create this Event directly unless routed through producing service.
- API must not expose restricted payload fields.
- API must preserve actor_context, request_context and policy_context.
- API must distinguish event record from command execution.
```

---

# 13. Relationship to AI Agents

Define AI usage.

Allowed AI use:

```text
summarize this Event
explain this Event in workflow context
identify missing follow-up actions for review
detect inconsistent event sequence
draft professional note based on authorized fields
```

AI must not:

```text
fabricate this Event
rewrite this Event
delete this Event
use hidden reasoning as payload
expose restricted payload fields
treat this Event as final professional judgment unless producing service says so
```

AI-originated event requirements:

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

This Event is valid only if:

```text
[ ] event_name is controlled.
[ ] event_category is controlled.
[ ] producing service is defined.
[ ] producing operation is defined.
[ ] source_domain is defined.
[ ] source_object_type is defined.
[ ] source_object_reference_id is present.
[ ] actor_reference_id is present.
[ ] occurred_at is present.
[ ] payload_contract_reference_id is present.
[ ] payload validates against contract.
[ ] restricted fields are not exposed.
[ ] AI source is identified where applicable.
[ ] event is not used as command.
```

Event-specific validation:

```text
[ ] [Add validation rule]
[ ] [Add validation rule]
[ ] [Add validation rule]
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
ActorReferenceMissing
OccurredAtMissing
PayloadContractMissing
PayloadInvalid
RestrictedFieldViolation
PolicyRestricted
PermissionRequired
AgentContractRequired
DuplicateEventRejected
UnknownEventError
```

Rejection rules:

```text
- Failed event creation must not be silently ignored.
- Rejection reason must be safe for product/API display.
- Restricted payload content must not be returned in error response.
- Failed command/operation must not emit success Event.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this Event Specification
cite the producing Service Specification
cite the Event Service Specification
cite the related Object Specification
use exact event_name
use exact event_category
validate required references
validate payload contract
write tests for required references
write tests for restricted payload fields
write tests that failed operations do not emit success Events
write tests for AI-originated event requirements where applicable
```

Codex must not:

```text
invent event fields silently
rename event without spec update
emit Event directly from UI
treat debug logs as Events
store raw confidential content
allow AI to fabricate or rewrite Event
use Event as command
```

---

# 17. Acceptance Criteria

This Event Specification is accepted only if:

```text
[ ] It defines Event purpose.
[ ] It defines Event meaning.
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
| 0.1.0 | Draft | Initial Event Specification template. Defines standard structure, payload rules, references, consumers, AI constraints, validation, rejection handling and Codex rules. |

---

**End of Event Specification Template**
