# Book 02

# 25 — Event Specification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-25  
**Chapter Title:** Event Specification  
**Part:** Part III — Core Specification System  
**Chapter Type:** Specification  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-05 — Core Principles
- B02-CH-13 — Core Domain Architecture
- B02-CH-16 — Core Execution Primitives
- B02-CH-17 — Core Contract Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-30 — MVP Execution Matrix
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines how Core Events are specified in MarkOrbit.

A Core Event is not a log line.

A Core Event is not a UI click.

A Core Event is not an activity feed item.

A Core Event is not merely a queue message.

A Core Event is a meaningful change in Core state, professional execution, review requirement, AI output, routing decision, communication linkage or workflow progress.

Events make change observable.

Events allow domains, Workplaces, products, AI agents, integrations and Codex-generated implementation to coordinate without redefining Core meaning.

The purpose of this chapter is to define:

```text
what a Core Event is
what a Core Event is not
how events are named
how events are owned
how events are triggered
how event payloads are governed
how events relate to objects and services
how events support workflow, AI, audit and integrations
how events are indexed before implementation
```

This chapter prepares:

```text
Appendix E — Event Index
core-specs/events/
core-specs/contracts/event-contracts/
workflow contracts
AI agent event rules
Codex event implementation tasks
```

---

# 2. Core Question

This chapter answers one question:

> How should MarkOrbit specify events so that meaningful changes are observable, contract-bound, auditable and safe for downstream coordination?

The answer is:

> MarkOrbit shall specify Core Events as semantic, source-owned, contract-bound change declarations emitted by governed services, workflows or agents and consumed only through approved event contracts.

---

# 3. Event Definition

A Core Event is:

> a named, source-owned and contract-bound declaration that a meaningful Core or execution change has occurred.

A Core Event must have:

```text
event name
source domain or source system
trigger
related objects
actor or source
payload contract
consumer boundary
audit rule
retention or replay rule
MVP status
```

A Core Event communicates that something meaningful has happened.

It does not perform the change by itself.

It records and communicates the change after the governed service, workflow or agent action has occurred.

---

# 4. Event Principle

Book 02 uses the following event principle:

```text
Event Before Coordination.
```

This means:

```text
Meaningful change must become a Core Event before it coordinates downstream behavior.
```

If a state change matters to another domain, product, workflow, AI agent, audit process, integration or user notification, it should be expressed as a Core Event.

If a change remains hidden inside a service, UI screen or database update, downstream systems cannot safely coordinate.

---

# 5. What Events Are Not

Core Events must not be confused with other technical or product artifacts.

## 5.1 Event Is Not a Log

A log records technical activity.

An Event records semantic change.

```text
Log:
    user clicked save

Event:
    MatterStatusChanged
```

## 5.2 Event Is Not a UI Action

A UI action may trigger a service.

A service may emit an Event.

The UI action itself is not the Core Event.

```text
UI action:
    click Submit

Service:
    CreateOrderService

Event:
    OrderCreated
```

## 5.3 Event Is Not an Activity Feed Row

An activity feed may display events.

The feed is not the event source of truth.

## 5.4 Event Is Not a Queue Message

A queue message transports information.

A Core Event defines semantic meaning and payload contract.

A queue may carry an event.

It does not define the event.

## 5.5 Event Is Not an Analytics Ping

Analytics may consume event data.

Analytics must not define Core event meaning.

---

# 6. Event Specification Statement

An Event Specification is:

> the canonical specification document that defines one Core Event, including its source, trigger, payload contract, consumers, audit requirements and execution implications.

Every event specification must answer:

```text
What happened?
Where did it happen?
Who or what caused it?
Which objects are affected?
Which service or workflow emitted it?
What payload is allowed?
Who may consume it?
What downstream behavior may it trigger?
What audit or review is required?
What is out of scope?
```

---

# 7. Standard Event Specification Template

Every event spec in `core-specs/events/` should follow this template.

```text
# Event: <EventName>

1. Event Purpose
2. Event Definition
3. Source Domain or Source System
4. Trigger
5. Emitting Service / Workflow / Agent
6. Related Objects
7. Actor / Source Identity
8. Payload Contract
9. Required Fields
10. Optional Fields
11. Event Timing
12. Event Ordering
13. Idempotency Rule
14. Consumers
15. Consumer Permissions
16. Workflow Effects
17. Notification Effects
18. AI Usage
19. Audit and Retention
20. Failure and Retry Behavior
21. Privacy and Data Exposure
22. MVP Phase and Depth
23. Out of Scope
24. Acceptance Criteria
25. Revision Notes
```

This template prevents events from becoming informal messages.

---

# 8. Event Naming Rules

Event names must be semantic, past-tense and domain meaningful.

## 8.1 Name Format

Canonical event name:

```text
PascalCase
```

File name:

```text
lowercase-kebab-case.md
```

Example:

```text
Event Name: MatterCreated
File Name: matter-created.md
```

## 8.2 Verb Tense

Events describe what has already happened.

Use past tense:

```text
Created
Updated
Assigned
Completed
Submitted
Approved
Rejected
Generated
Linked
Converted
Required
Made
```

## 8.3 Good Event Names

```text
CustomerCreated
OrderCreated
OrderConfirmed
OrderConvertedToMatter
MatterCreated
MatterStatusChanged
TaskCreated
TaskAssigned
TaskCompleted
DocumentUploaded
DocumentGenerated
ReviewRequired
ReviewApproved
ReviewRejected
AIRecommendationGenerated
AIRecommendationReviewRequired
RoutingDecisionMade
CommunicationLinked
OpportunityCreated
```

## 8.4 Bad Event Names

```text
SaveButtonClicked
UserDidSomething
SendMessage
ProcessData
LogChanged
UpdateThing
AIResult
NotifyUser
```

Bad names are usually too technical, too vague or too UI-dependent.

---

# 9. Event Source Ownership

Every Core Event must have a source owner.

Source ownership may belong to:

```text
one Core Domain
one cross-cutting specification system
one governed workflow contract
one governed AI agent under Agent Contract
```

Examples:

```text
TrademarkCreated
    source domain: Trademark

OrderCreated
    source domain: Order

MatterCreated
    source domain: Matter

TaskAssigned
    source domain: Task

ReviewRequired
    source system: Business Responsibility / Workflow Contract

AIRecommendationGenerated
    source system: AI Governance

RoutingDecisionMade
    source domain: Routing
```

Source ownership matters because it controls:

```text
payload meaning
emitting service
consumer boundary
audit responsibility
index placement
Codex implementation task ownership
```

---

# 10. Event Trigger Rules

Every event must define its trigger.

A trigger may be:

```text
service completion
workflow transition
human review action
AI agent output
external status synchronization
document upload
document generation
routing decision
communication linkage
scheduled deadline condition
```

A trigger must not be merely:

```text
page loaded
button clicked
field focused
frontend state changed
background job started
```

Those are technical events, not Core Events.

---

# 11. Emitting Services, Workflows and Agents

Events should normally be emitted by governed services.

Examples:

```text
CreateOrderService
    emits OrderCreated

ConvertOrderToMatterService
    emits OrderConvertedToMatter and MatterCreated

AssignTaskService
    emits TaskAssigned

GenerateDocumentService
    emits DocumentGenerated

CreateRoutingDecisionService
    emits RoutingDecisionMade
```

Events may also be emitted by workflow transitions.

Examples:

```text
ReviewRequired
ReviewApproved
ReviewRejected
MatterStatusChanged
```

Events may be emitted by AI agents only if the Agent Contract allows it.

Examples:

```text
AIRecommendationGenerated
AIRecommendationReviewRequired
AIOutputRejected
```

AI must not emit Core Events without:

```text
Agent Contract
allowed capability
structured output
risk level
review rule
audit rule
```

---

# 12. Related Objects

Every event must identify related objects.

Related objects may include:

```text
primary object
secondary objects
actor identity
organization
matter
order
task
document
AI output
review record
communication record
routing decision
```

Example:

```text
Event: TaskAssigned
Primary Object: Task
Related Objects:
    Matter
    User
    Responsibility Assignment
    Workflow Contract
```

The event references objects.

It does not own their meaning.

---

# 13. Payload Contract

Every event must have a payload contract.

The payload contract defines:

```text
required fields
optional fields
field meanings
object references
actor reference
timestamp
source service
correlation ID
causation ID
version
privacy constraints
consumer-visible fields
internal-only fields
```

A payload must be stable enough for downstream consumers.

It must not expose internal implementation details unless explicitly allowed.

---

# 14. Required Payload Fields

Most Core Events should include the following baseline fields.

```text
event_id
event_name
event_version
occurred_at
source_domain
source_service_or_agent
actor_id
actor_type
primary_object_type
primary_object_id
related_object_refs
correlation_id
causation_id
payload
visibility
metadata
```

Not every event needs every field in the same way.

But deviations must be justified in the Event Specification.

---

# 15. Event Timing

Every event must define when it is emitted.

Timing options include:

```text
after successful state change
after validation but before workflow transition
after workflow transition
after human approval
after AI output generation
after external synchronization confirmation
after document persistence
```

Default rule:

```text
Emit Core Events only after the meaningful change has succeeded.
```

If an event is emitted before final completion, the event name must make that clear.

Example:

```text
ReviewRequired
SubmissionRequested
```

---

# 16. Event Ordering

Some events depend on order.

Examples:

```text
OrderCreated
↓
OrderConfirmed
↓
OrderConvertedToMatter
↓
MatterCreated
```

Ordering rules must be specified when downstream behavior depends on sequence.

Event ordering may use:

```text
occurred_at
correlation_id
causation_id
aggregate version
workflow state version
event sequence number
```

Codex implementation must not assume ordering without a spec rule.

---

# 17. Idempotency

Events may be delivered or processed more than once.

Every event spec should define idempotency behavior.

Idempotency rules may include:

```text
event_id uniqueness
consumer processed-event tracking
aggregate version check
source service idempotency key
correlation-based deduplication
```

Event consumers must not produce duplicate side effects when the same event is processed more than once.

---

# 18. Event Consumers

Event consumers may include:

```text
Core Services
Workflow Contracts
Workplace
Products
AI Agents
Notification Services
Audit Services
Reporting Consumers
External Integrations
Codex-generated tests
```

Consumers must be declared in the Event Specification.

A consumer may read an event only if allowed by:

```text
Event Contract
Permission
Policy
Data exposure rule
Consumer classification
```

---

# 19. Workflow Effects

Events often coordinate workflow.

Examples:

```text
OrderConfirmed
    may trigger order-to-matter conversion eligibility

MatterCreated
    may trigger default task creation

TaskAssigned
    may trigger notification

ReviewRequired
    may transition work into review queue

ReviewApproved
    may allow next workflow transition

ReviewRejected
    may return work to draft or correction state
```

Workflow effects must be specified.

Events must not secretly change workflow state unless a Workflow Contract allows it.

---

# 20. Notification Effects

Some events may trigger notifications.

Examples:

```text
TaskAssigned
ReviewRequired
DeadlineApproaching
MatterStatusChanged
RoutingDecisionMade
CommunicationLinked
```

Notification effects must define:

```text
who may be notified
what information may be included
whether notification is required or optional
whether notification is internal or external
what permission rule applies
```

Notification is a consumer effect.

It is not the event itself.

---

# 21. AI Usage

Events can be used by AI agents only under governance.

AI may consume events for:

```text
workflow summary
matter status summary
classification recommendation context
communication summary
opportunity discovery
routing recommendation
document drafting context
Codex implementation review
```

AI may emit events only if governed.

AI-related events include:

```text
AIRecommendationGenerated
AIRecommendationReviewRequired
AIRecommendationApproved
AIRecommendationRejected
AIOutputLinked
AIOutputArchived
```

AI event rules must define:

```text
Agent Contract
risk level
allowed event consumption
allowed event emission
human review requirement
audit requirement
prohibited autonomous side effects
```

---

# 22. Audit and Retention

Events are important audit artifacts.

Event specs must define:

```text
audit requirement
retention period category
visibility
redaction rules
replay eligibility
export eligibility
legal or professional sensitivity
```

High-risk events require stronger audit.

Examples:

```text
ReviewApproved
ReviewRejected
AIRecommendationApproved
RoutingDecisionMade
DocumentSubmitted
TrademarkStatusChanged
OrderConvertedToMatter
```

---

# 23. Privacy and Data Exposure

Events must not expose unnecessary data.

Payloads should distinguish:

```text
public consumer fields
internal consumer fields
restricted fields
sensitive professional fields
AI-accessible fields
external integration fields
```

External consumers should receive minimal contracted data.

AI consumers should receive only authorized context.

Reporting consumers should not receive private content unless permitted.

---

# 24. Failure and Retry Behavior

Event specs should define failure behavior.

Failure categories include:

```text
emission failure
consumer processing failure
retryable delivery failure
non-retryable validation failure
permission failure
schema version mismatch
external integration failure
AI consumer failure
```

Retry behavior should avoid duplicate side effects.

Failure behavior should be observable through logs or operational records, but failure logs are not Core Events unless they represent meaningful Core state.

---

# 25. Event Categories

Book 02 uses the following event categories.

## 25.1 Lifecycle Events

Events that indicate object lifecycle changes.

```text
CustomerCreated
OrderCreated
MatterCreated
TaskCreated
DocumentUploaded
OpportunityCreated
```

## 25.2 Status Events

Events that indicate meaningful status changes.

```text
TrademarkStatusChanged
MatterStatusChanged
TaskStatusChanged
OrderStatusChanged
```

## 25.3 Workflow Events

Events that support workflow coordination.

```text
ReviewRequired
ReviewApproved
ReviewRejected
OrderConvertedToMatter
TaskAssigned
TaskCompleted
```

## 25.4 AI Events

Events generated by governed AI activity.

```text
AIRecommendationGenerated
AIRecommendationReviewRequired
AIRecommendationApproved
AIRecommendationRejected
```

## 25.5 Routing Events

Events related to routing or provider selection.

```text
RoutingDecisionMade
AgentSuggested
ServiceProviderSelected
```

## 25.6 Communication Events

Events related to professional communication.

```text
CommunicationLinked
CommunicationSummaryGenerated
AgentMessageReceived
ClientMessageReceived
```

## 25.7 Notification Events

Events that may trigger alerts.

```text
NotificationRequested
NotificationSent
NotificationFailed
```

## 25.8 Integration Events

Events related to external systems.

```text
ExternalStatusSynced
OfficeDataImported
DocumentSignatureCompleted
PaymentStatusSynced
```

Integration events should be contract-bound and should not expose vendor-specific implementation as Core meaning.

---

# 26. MVP Event Baseline

The Core MVP should include a controlled event baseline.

Initial MVP event candidates include:

```text
CustomerCreated
BrandCreated
TrademarkCreated
OrderCreated
OrderConfirmed
OrderConvertedToMatter
MatterCreated
MatterStatusChanged
TaskCreated
TaskAssigned
TaskCompleted
DocumentUploaded
DocumentGenerated
ReviewRequired
ReviewApproved
ReviewRejected
AIRecommendationGenerated
AIRecommendationReviewRequired
RoutingDecisionMade
CommunicationLinked
NotificationRequested
```

This list should be finalized in Appendix E.

Detailed payloads should be defined later in `core-specs/events/`.

---

# 27. Deferred Event Scope

The following event areas should be deferred or reserved until later releases.

```text
full marketplace event set
advanced provider ranking events
full opportunity scoring events
full brand asset vault events
advanced analytics events
public webhook event library
multi-tenant external partner event feed
full AI autonomous execution events
```

Deferred events must not be implemented by Codex unless explicitly approved.

---

# 28. Event Anti-Patterns

## 28.1 UI Event as Core Event

A click is treated as a Core Event.

Correction:

```text
The service result should emit the Core Event, not the click.
```

## 28.2 Log as Core Event

A technical log is used as event source of truth.

Correction:

```text
Core Events require semantic names and payload contracts.
```

## 28.3 Event Without Source Domain

An event has no source owner.

Correction:

```text
Every event must declare source domain or source system.
```

## 28.4 Event Without Payload Contract

Consumers rely on informal payload shape.

Correction:

```text
Every event must have an Event Contract.
```

## 28.5 Eventless State Change

A meaningful state change occurs silently.

Correction:

```text
Governed services must declare event side effects.
```

## 28.6 Analytics Defines Event Meaning

Reporting creates its own event definitions.

Correction:

```text
Reporting consumes Core Events and requests extensions through governance.
```

## 28.7 AI Emits Events Without Governance

AI emits workflow or state events without Agent Contract.

Correction:

```text
AI event emission requires Agent Contract, risk rule, review rule and audit.
```

## 28.8 Event Storm in MVP

Too many events are implemented before consumers need them.

Correction:

```text
Use MVP depth and Appendix E to control event scope.
```

---

# 29. Appendix E Readiness

This chapter prepares Appendix E — Event Index.

Appendix E must include:

```text
event name
file name
source domain or source system
event category
trigger
emitting service / workflow / agent
related objects
payload contract
consumer domains
workflow effects
AI usage
audit requirement
MVP phase
MVP depth
deferred scope
```

Appendix E must also include:

```text
event naming rules
event anti-patterns
MVP event baseline
deferred event scope
AI event governance notes
```

---

# 30. Relationship to Other Specifications

## 30.1 Relationship to Domain Specification

Every event must declare a source domain or cross-cutting source system.

## 30.2 Relationship to Object Specification

Every event must reference affected Core Objects.

## 30.3 Relationship to Service Specification

Core Services must declare which events they emit.

## 30.4 Relationship to Contract Architecture

Every event requires an Event Contract.

## 30.5 Relationship to Workflow Contract

Workflow-related events must respect allowed states and transitions.

## 30.6 Relationship to AI Governance

AI-related events must be governed by Agent Contracts.

## 30.7 Relationship to API Specification

APIs may trigger services that emit events, but API calls are not events by themselves.

## 30.8 Relationship to Core Consumption

Products and integrations may consume events only through approved contracts.

---

# 31. Specification Output

This chapter produces the following specification outputs:

```text
Core Event definition
Event Specification definition
Event naming rules
Event source ownership rules
Event trigger rules
Event payload contract requirements
Event timing rules
Event ordering rules
Event idempotency rules
Event consumer rules
Workflow effect rules
Notification effect rules
AI event governance rules
Audit and retention rules
Privacy and data exposure rules
Failure and retry behavior rules
Event categories
MVP event baseline
Deferred event scope
Event anti-patterns
Appendix E readiness requirements
```

---

# 32. Execution Mapping

| Event Specification Decision | Execution Impact |
|------------------------------|------------------|
| Events are semantic changes | Do not implement UI clicks as Core Events |
| Events have source owners | Event files must declare source domain/system |
| Events require payload contracts | `core-specs/events/` and event contracts are required |
| Services emit events | Service specs must declare event side effects |
| Events coordinate workflow | Workflow contracts must define event effects |
| AI event usage is governed | Agent Contracts must define event access/emission |
| Events require audit | Audit records and retention rules are needed |
| MVP event baseline is controlled | Codex must not overbuild event library |

---

# 33. Relationship to core-specs/

This chapter governs the future `core-specs/events/` scaffold.

Each event spec should include:

```text
Event Purpose
Event Definition
Source Domain or Source System
Trigger
Emitting Service / Workflow / Agent
Related Objects
Actor / Source Identity
Payload Contract
Required Fields
Optional Fields
Event Timing
Event Ordering
Idempotency Rule
Consumers
Consumer Permissions
Workflow Effects
Notification Effects
AI Usage
Audit and Retention
Failure and Retry Behavior
Privacy and Data Exposure
MVP Phase and Depth
Out of Scope
Acceptance Criteria
Revision Notes
```

`core-specs/events/` must not become a log catalog or message bus dump.

It must remain a semantic event specification system.

---

# 34. Exclusions

This chapter does not define:

```text
final event payload schemas
final event broker implementation
database event tables
message queue technology
vendor-specific webhook behavior
full external public event library
complete reporting event warehouse
all future marketplace events
all future AI autonomy events
```

Those belong to later `core-specs/`, implementation, integration or product documents.

---

# 35. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Event as semantic change.
[ ] It distinguishes event from log, UI action, activity feed, queue message and analytics ping.
[ ] It defines Event Specification clearly.
[ ] It provides a standard event spec template.
[ ] It defines event naming rules.
[ ] It requires source domain or source system ownership.
[ ] It requires event triggers.
[ ] It requires payload contracts.
[ ] It defines timing, ordering and idempotency rules.
[ ] It defines event consumers and permissions.
[ ] It defines workflow and notification effects.
[ ] It defines AI event governance.
[ ] It defines audit, retention, privacy and data exposure rules.
[ ] It defines event categories.
[ ] It proposes an MVP event baseline.
[ ] It protects deferred event scope.
[ ] It prepares Appendix E — Event Index.
[ ] It supports future core-specs/events/.
[ ] It supports Codex-safe event implementation.
```

---

# 36. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 25, defining Event Specification. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened event semantics, naming, source ownership, payload contracts, timing, ordering, idempotency, AI governance, audit, MVP baseline and Appendix E readiness. |

---

**End of Chapter**
