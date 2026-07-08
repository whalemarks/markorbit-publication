# core-specs/events — README

**Spec Area:** Core Event Specifications  
**Book:** Book 02 — MarkOrbit Core Specification  
**Layer:** Core Specification System  
**Primary Chapters:** B02-CH-16 — Core Execution Primitives; B02-CH-25 — Event Specification  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The `core-specs/events` directory defines the governed Event specifications used by MarkOrbit Core.

An Event Specification describes:

```text
what meaningful occurrence happened
which domain or service produced it
which object reference is involved
which payload contract applies
which consumers may react
which audit, policy and AI constraints apply
```

Events are part of MarkOrbit Core execution primitives.

They connect Core services without allowing product UI, AI agents or implementation logs to redefine business truth.

---

# 2. Core Event Principle

```text
Event records that something meaningful happened.
Event does not execute work.
Event does not replace Task, Workflow, Notification, Communication or Audit.
```

Events are not:

```text
database logs
debug logs
UI activity feed items
notification messages
email/chat messages
task records
workflow definitions
AI thoughts
```

Events are governed professional occurrences.

---

# 3. Architectural Position

Events sit after governed service operations.

```text
Core Service performs governed operation
        ↓
Event Service records meaningful occurrence
        ↓
Notification / Communication / Task / Workflow / AI consumers may react
        ↓
Audit preserves accountability where required
```

Events allow Core to remain decoupled:

```text
Services own business operation.
Events record occurrence.
Consumers react under contract.
AI explains or assists only under governance.
```

---

# 4. Directory Scope

This directory contains:

```text
event README
event template
domain event specs
service event specs
cross-domain event specs
event payload contracts
event reference rules
event consumption rules
event validation rules
```

This directory does not contain:

```text
service implementation
message queue code
database schema code
product UI notification logic
email/SMS gateway logic
workflow runtime code
AI prompt implementation
```

---

# 5. Event Specification Standard Structure

Each Event Specification should follow this structure:

```text
1. Purpose
2. Event Meaning
3. Event Category
4. Event Producer
5. Event Trigger
6. Event Payload
7. Required References
8. Controlled Values
9. Event Rules
10. Consumer Rules
11. Relationship to Services
12. Relationship to APIs
13. Relationship to AI Agents
14. Validation Rules
15. Error / Rejection Handling
16. Codex Implementation Notes
17. Acceptance Criteria
18. Revision Notes
```

Small internal events may use an abbreviated structure only if explicitly marked as supporting events.

---

# 6. Event Categories

Baseline event categories:

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

Event category is not decorative.

It determines:

```text
payload expectations
consumer eligibility
audit sensitivity
AI access boundary
API exposure boundary
retention and visibility rules
```

---

# 7. Event Naming Rules

Event names must use past-tense occurrence language.

Preferred pattern:

```text
<Object><ActionPastTense>
```

Examples:

```text
MatterCreated
MatterStatusChanged
TaskAssigned
TaskCompleted
WorkflowTransitionValidated
NotificationTriggered
CommunicationSent
AgentReferenceValidated
RoutingSelectionApproved
```

Avoid names that imply commands:

```text
CreateMatter
AssignTask
SendNotification
ApproveRouting
```

Commands request action.

Events record that action occurred.

---

# 8. Event Producer Rules

Every event must define its producer.

Producer may be:

```text
Core Service
Domain Service
API Layer through service operation
AI Agent through governed service operation
System Process through governed service operation
External Integration through integration contract
```

Producer must not be ambiguous.

AI-originated events must identify AI source and Agent Contract reference where applicable.

---

# 9. Event Payload Rules

Event payload must be governed.

A payload must define:

```text
payload contract reference
event type
source domain
source service
source object type
source object reference
actor reference
occurred_at
correlation_id where applicable
causation_id where applicable
safe summary fields
restricted fields policy
```

Payload must not include:

```text
raw confidential document contents
raw evidence contents
passwords or secrets
unfiltered AI reasoning
unstructured debug logs
unbounded external payloads
unreviewed legal conclusions
```

---

# 10. Event Reference Rules

Events should reference Core objects by stable IDs.

Events should not embed full object snapshots unless a specific event contract requires a safe snapshot.

Preferred reference pattern:

```text
source_object_type
source_object_reference_id
related_object_references
actor_reference_id
organization_reference_id
service_reference
payload_contract_reference_id
```

---

# 11. Event Consumer Rules

Event consumers may include:

```text
Notification Service
Communication Service
Task Service
Workflow Contract Service
Audit Service
AI Agent under Agent Contract
API consumers under policy
Product UI read models
Integration services
```

Consumers must not reinterpret event truth.

Consumer reaction must be governed by:

```text
Permission
Policy
API contract
Agent Contract where AI is involved
Workflow Contract where execution is involved
Audit requirement where sensitive
```

---

# 12. Relationship to Event Service

The Event Service is the Core service that records and validates Events.

Event specs define event contracts.

Event Service enforces:

```text
event creation
event status
payload validation
reference validation
dispatch trace
consumer trace
policy-safe access
```

Event specs must not implement Event Service.

---

# 13. Relationship to Audit

Event is not Audit.

Event records occurrence.

Audit records accountability and governance trace.

Some events may be audit inputs.

Audit-sensitive events must preserve:

```text
actor_context
source_context
request_context
before/after references where safe
policy decision reference where applicable
permission decision reference where applicable
AI Agent Contract reference where applicable
```

---

# 14. Relationship to AI Agents

AI Agents may use events to:

```text
summarize authorized activity history
explain workflow progress
detect missing event traces
flag inconsistent sequences
draft next-step recommendations for review
record governed AI action events
```

AI Agents must not:

```text
fabricate events
rewrite event history
delete event traces silently
treat event record as permission
treat event record as task completion where service did not complete task
expose restricted payload fields
use hidden chain-of-thought as event payload
```

---

# 15. MVP Event Coverage

Phase 1 baseline:

```text
IdentityCreated
IdentityUpdated
UserCreated
UserUpdated
OrganizationCreated
PermissionEvaluated
PolicyEvaluated
KnowledgeRecordCreated
KnowledgeRecordUpdated
```

Phase 2 baseline:

```text
BrandCreated
TrademarkCreated
JurisdictionLinked
ClassificationCreated
DocumentCreated
EvidenceCreated
```

Phase 3 baseline:

```text
CustomerCreated
OrderCreated
MatterCreated
WorkflowContractCreated
WorkflowTransitionValidated
TaskCreated
TaskAssigned
TaskCompleted
EventRecorded
NotificationCreated
```

Phase 4 baseline:

```text
CommunicationCreated
CommunicationSent
CommunicationReceived
AgentCreated
ServiceProviderCreated
RoutingRequestCreated
RoutingEvaluated
RoutingSelectionApproved
```

Phase 5 reserved:

```text
PartnerCreated
ServiceNetworkCreated
ServiceNetworkNodeAdded
ServiceNetworkLinkAdded
```

---

# 16. Codex Usage Rules

Codex must:

```text
read the relevant Event Specification before implementing event emission
read the Event Service Specification before implementing recording/validation
use controlled event names
use governed payload contracts
preserve Event / Task / Workflow / Notification / Communication / Audit boundaries
write tests for required references
write tests for controlled values
write tests for restricted payload fields
write tests for AI-originated event source where applicable
```

Codex must not:

```text
invent event names silently
use debug logs as Core Events
store raw confidential content in event payloads
let product UI redefine event meanings
let AI fabricate or rewrite events
implement event bus infrastructure unless explicitly tasked
```

---

# 17. File Naming Convention

Event spec files should use kebab-case:

```text
<object-action-past-tense>.md
```

Examples:

```text
identity-created.md
matter-created.md
task-assigned.md
workflow-transition-validated.md
communication-sent.md
routing-selection-approved.md
service-network-node-added.md
```

Index and template files:

```text
README.md
_template.md
```

---

# 18. Acceptance Criteria

The `core-specs/events` directory is valid only if:

```text
[ ] It defines Event purpose and boundary.
[ ] It separates Event from Task, Workflow, Notification, Communication and Audit.
[ ] It defines event naming rules.
[ ] It defines event payload rules.
[ ] It defines event producer and consumer rules.
[ ] It defines AI Agent constraints.
[ ] It defines MVP event coverage.
[ ] It gives Codex implementation rules.
[ ] It supports Event Service enforcement.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/events. Defines event boundary, naming rules, payload rules, producer/consumer rules, AI constraints, MVP coverage and Codex usage rules. |

---

**End of README**
