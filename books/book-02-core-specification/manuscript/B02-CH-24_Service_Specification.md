# Book 02

# 24 — Service Specification

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-24  
**Chapter Title:** Service Specification  
**Part:** Part III — Core Specification System  
**Chapter Type:** Specification  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-CH-13 — Core Domain Architecture
- B02-CH-15 — Core Service Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-25 — Event Specification
- B02-CH-27 — Core Consumption Specification
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the Service Specification standard for the MarkOrbit Core.

Chapter 22 defined how Core Domains should be specified.

Chapter 23 defined how Core Objects should be specified.

This chapter defines how Core Services should be specified.

A Core Service is not a UI button.

A Core Service is not a helper function.

A Core Service is not a controller method.

A Core Service is not a vendor wrapper.

A Core Service is not an AI prompt.

A Core Service is a governed capability that operates Core meaning through defined inputs, outputs, permissions, side effects, events and contracts.

The purpose of Service Specification is to prevent implementation from turning Core architecture into scattered functions.

Service Specification ensures that every service has:

```text
clear purpose
owning domain or cross-cutting system
objects read
objects created or updated
inputs and outputs
permission and policy rules
knowledge dependencies
event side effects
contracts
AI usage boundary
human review requirement
failure behavior
consumers
MVP depth
acceptance criteria
```

This chapter prepares the foundation for:

```text
Appendix D — Core Service Index
core-specs/services/
core-specs/contracts/
core-specs/api/
Codex implementation tasks
service tests
workflow execution
AI governance
product consumption
```

---

# 2. Core Question

This chapter answers one question:

> How should a Core Service be specified so that it can operate Core meaning safely without becoming product-specific logic, hidden automation, uncontrolled AI behavior or implementation-only code?

The answer is:

> A Core Service must be specified as a governed operation owned by a Core Domain or explicitly declared cross-cutting system, acting on defined Core Objects, producing defined outputs and events, protected by permissions, policies and contracts, and consumable only through approved boundaries.

---

# 3. Core Definition

A Core Service is:

> a governed capability that reads, validates, creates, updates, transforms, recommends, routes, reviews or publishes Core meaning under explicit domain ownership and contract rules.

This definition contains eight commitments.

```text
1. A service must have an owner.
2. A service must operate defined Core Objects.
3. A service must have explicit inputs and outputs.
4. A service must declare side effects.
5. A service must emit required events.
6. A service must respect permission, policy and responsibility.
7. A service must define AI usage and review boundaries.
8. A service must be consumable through approved contracts.
```

---

# 4. What a Service Is Not

A Core Service must not be confused with implementation details.

## 4.1 Not a UI Button

A product button may call a service.

The button is not the service.

Example:

```text
Button: Submit Application
Possible Core Service: CreateTrademarkApplicationMatter
```

## 4.2 Not a Helper Function

A helper function may support implementation.

It does not necessarily carry Core responsibility.

Example:

```text
Helper: formatDate()
Core Service: NormalizeTrademarkStatus
```

## 4.3 Not a Controller Method

An HTTP controller may expose a service.

It does not define service meaning.

Example:

```text
Route: POST /matters
Core Service: CreateMatter
```

## 4.4 Not a Vendor Wrapper

A vendor adapter may call an external system.

It does not own Core meaning.

Example:

```text
Vendor Adapter: USPTO API client
Core Service: ImportTrademarkStatus
```

## 4.5 Not an AI Prompt

An AI prompt may assist a service.

It is not a Core Service by itself.

Example:

```text
Prompt: summarize office action
Core Service: GenerateOfficeActionSummary
Agent Contract: Office Action Assistant
```

---

# 5. Service Specification Statement

A Service Specification is:

> the canonical document that defines one Core Service’s purpose, ownership, inputs, outputs, object operations, events, contracts, governance rules, consumers and acceptance criteria.

A Service Specification must be detailed enough for Codex to implement.

It must also be strict enough to prevent Codex from inventing architecture.

---

# 6. Standard Service Specification Template

Every service spec should follow this structure.

```text
# Service Name

1. Service Metadata
2. Service Purpose
3. Core Definition
4. Owning Domain or Cross-Cutting System
5. Service Category
6. In Scope
7. Out of Scope
8. Inputs
9. Outputs
10. Objects Read
11. Objects Created or Updated
12. State Changes
13. Events Emitted
14. Events Consumed
15. Contracts Required
16. Permission Rules
17. Policy Rules
18. Knowledge Dependencies
19. AI Usage
20. Human Review Requirement
21. Responsibility and Audit
22. Failure Behavior
23. Idempotency and Retry Rules
24. API Exposure
25. Workflow Usage
26. Product Consumers
27. MVP Phase and Depth
28. Tests Required
29. Acceptance Criteria
30. Revision Notes
```

This template is the expected baseline for future files under:

```text
core-specs/services/
```

---

# 7. Service Metadata

Every Service Specification must include metadata.

Required metadata:

```yaml
service_id: SERVICE-XXX
service_name: CreateMatter
service_type: command | query | recommendation | validation | transformation | routing | review | notification | integration | AI-assisted
owning_domain: Matter
owning_system: null
status: Draft
mvp_phase: Phase 3
mvp_depth: Must Implement
source_chapter: B02-CH-24
source_index: B02-APP-D
authority: Book 02 / core-specs/services
version: 0.1.0
```

If a service belongs to a cross-cutting system instead of a baseline domain, it must state that explicitly.

Example:

```yaml
owning_domain: null
owning_system: Business Responsibility
```

---

# 8. Service Ownership Rule

Every Core Service must have one primary owner.

The owner may be:

```text
a baseline Core Domain
an explicitly declared cross-cutting specification system
```

Allowed examples:

```text
CreateMatter
    owner: Matter Domain

RecommendClassification
    owner: Classification Domain

GenerateDocumentDraft
    owner: Document Domain

AssignReviewResponsibility
    owner: Business Responsibility cross-cutting system

MatchCapabilityProvider
    owner: Capability cross-cutting system
```

A service may involve multiple domains.

But it must still declare a primary owner.

This prevents service ownership drift.

---

# 9. Service Categories

Core Services should be classified by category.

## 9.1 Command Service

A command service changes Core state.

Examples:

```text
CreateCustomer
CreateOrder
ConvertOrderToMatter
AssignTask
UploadDocument
ApproveReview
```

Command services usually emit events.

## 9.2 Query Service

A query service retrieves Core meaning without changing state.

Examples:

```text
GetTrademarkProfile
ListMatterTasks
RetrieveJurisdictionRequirement
GetCustomerMatters
```

Query services should still respect permissions and contracts.

## 9.3 Validation Service

A validation service checks whether data, objects or actions satisfy rules.

Examples:

```text
ValidateClassificationTerms
ValidateDocumentRequirement
ValidateOrderReadiness
ValidateAgentContract
```

## 9.4 Transformation Service

A transformation service converts one representation into another governed form.

Examples:

```text
NormalizeTrademarkStatus
TransformOfficeDocumentToStructuredRecord
ConvertIntakeToOrderDraft
```

## 9.5 Recommendation Service

A recommendation service produces a suggested output.

Examples:

```text
RecommendJurisdiction
RecommendClassification
RecommendAgentRouting
RecommendEvidenceGap
```

Recommendation services may require AI governance and human review.

## 9.6 Routing Service

A routing service decides or recommends where work should go.

Examples:

```text
RouteMatterToAgent
RecommendServiceProvider
AssignTaskByCapability
```

Routing services must connect to Capability and Business Responsibility.

## 9.7 Review Service

A review service handles review state, approval, rejection or escalation.

Examples:

```text
CreateReviewRequest
ApproveAIRecommendation
RejectDocumentDraft
EscalateMatterReview
```

Review services must be auditable.

## 9.8 Notification Service

A notification service sends or schedules alerts.

Examples:

```text
NotifyTaskAssigned
NotifyReviewRequired
NotifyDeadlineApproaching
```

Notification service does not own the event meaning that triggers it.

## 9.9 Integration Service

An integration service interacts with an external system through a contract.

Examples:

```text
ImportTrademarkStatus
SendAgentCommunication
SyncDocumentToStorage
```

Integration services must not let vendor API shape define Core meaning.

## 9.10 AI-Assisted Service

An AI-assisted service uses an AI Agent under Agent Contract.

Examples:

```text
GenerateClassificationRecommendation
SummarizeTrademarkStatus
DraftOfficeActionResponseOutline
SummarizeAgentCommunication
```

AI-assisted services must define risk, review and audit.

---

# 10. Inputs

A Service Specification must define service inputs.

Inputs should include:

```text
input name
input type
required or optional
source
validation rule
permission requirement
sensitivity
example
```

Inputs may come from:

```text
user action
product flow
workflow context
AI agent context
external integration
existing Core Object
event payload
fixture
Codex task
```

Inputs must not silently include private internal data.

---

# 11. Outputs

A Service Specification must define service outputs.

Outputs may include:

```text
created object
updated object
recommendation
validation result
routing decision
review request
notification request
structured summary
external sync result
event publication result
```

Outputs must declare whether they are:

```text
final
recommendation
draft
review-required
rejected
accepted
partial
error
```

AI outputs must never be treated as final professional truth unless the service explicitly permits it and review rules allow it.

---

# 12. Objects Read

Every service must declare which Core Objects it reads.

Example:

```text
Service: ConvertOrderToMatter
Objects Read:
    Order
    Customer
    Trademark
    Jurisdiction
    Classification
    Document Requirement
    Responsibility Assignment
```

Read access must comply with:

```text
permission
policy
contract
consumer boundary
AI access rule
```

---

# 13. Objects Created or Updated

Every command service must declare which objects it creates or updates.

Example:

```text
Service: ConvertOrderToMatter
Objects Created:
    Matter
    Task
    Workflow State

Objects Updated:
    Order
    Responsibility Assignment
```

A service may not mutate objects that are not declared in its spec.

---

# 14. State Changes

A service that changes state must define state transitions.

Required fields:

```text
object
previous state
new state
allowed transition
trigger
actor
review requirement
event emitted
```

Example:

```text
Order.status: confirmed → converted_to_matter
Matter.status: null → active
Task.status: null → open
```

Hidden state changes are prohibited.

---

# 15. Events Emitted

Every meaningful service side effect should emit a Core Event.

A Service Specification must declare:

```text
event name
source domain
trigger condition
payload contract
related objects
consumer domains
human review impact
audit requirement
```

Examples:

```text
CustomerCreated
OrderCreated
OrderConvertedToMatter
MatterCreated
TaskAssigned
DocumentUploaded
ReviewRequired
AIRecommendationGenerated
RoutingDecisionMade
```

Event names should be semantic and past-tense.

Event files should use lowercase kebab-case.

Example:

```text
Event Name: MatterCreated
File Name: matter-created.md
```

---

# 16. Events Consumed

Some services may be triggered by events.

Example:

```text
Service: NotifyReviewRequired
Consumes Event:
    ReviewRequired

Service: CreateInitialMatterTasks
Consumes Event:
    MatterCreated

Service: GenerateDeadlineReminder
Consumes Event:
    DeadlineScheduled
```

Event consumption must not create uncontrolled loops.

The service spec must define:

```text
trigger event
conditions
debounce or idempotency rule
output events
failure behavior
```

---

# 17. Contracts Required

A Core Service may require one or more contracts.

Contract types include:

```text
Data Contract
API Contract
Event Contract
Agent Contract
Workflow Contract
Consumption Contract
```

Examples:

```text
RecommendClassification
    requires Agent Contract if AI-assisted
    requires Classification Recommendation Output Contract
    requires Review Contract for high-risk output

CreateMatter
    requires Data Contract
    requires Workflow Contract
    emits MatterCreated Event Contract

ImportTrademarkStatus
    requires External Integration Contract
    requires Trademark Data Contract
    emits TrademarkStatusChanged Event Contract
```

Contracts protect Core from uncontrolled consumption.

---

# 18. Permission Rules

Every service must define permission rules.

Permission rules answer:

```text
who may invoke the service?
who may read the input objects?
who may see the output?
who may approve the output?
who may export the result?
can AI invoke or assist this service?
can external integrations invoke this service?
```

Example:

```text
Only users with MatterOperator permission may create Matter tasks.
Only reviewers with ReviewApprover permission may approve AI-generated classification recommendation.
AI agents may assist but may not approve high-risk professional outputs.
```

---

# 19. Policy Rules

Service behavior may depend on policy.

Policy rules may include:

```text
jurisdiction-specific rule
risk threshold
review rule
document requirement
classification constraint
AI usage rule
data sharing rule
external communication rule
```

Example:

```text
If classification confidence is below threshold, ReviewRequired must be emitted.
If jurisdiction requires POA, DocumentRequirement must be created.
If AI output affects filing scope, human review is mandatory.
```

Policy must be explicit.

---

# 20. Knowledge Dependencies

Some services depend on Knowledge.

Knowledge dependencies must be declared.

Examples:

```text
Jurisdiction Requirement Knowledge
Classification Knowledge
Trademark Office Status Knowledge
Document Requirement Knowledge
Agent Capability Knowledge
Evidence Practice Knowledge
```

For AI-assisted services, authorized knowledge must be stated in the Agent Contract.

A service must not use unapproved knowledge sources when producing professional recommendations.

---

# 21. AI Usage

A Service Specification must declare whether AI is used.

Allowed AI usage categories:

```text
none
retrieval assistance
classification assistance
draft generation
summary generation
risk flagging
routing recommendation
opportunity discovery
Codex implementation assistance
```

If AI is used, the spec must declare:

```text
agent identity
agent contract
allowed capabilities
prohibited capabilities
authorized knowledge
objects accessible
output type
risk level
human review requirement
events emitted
audit record
failure behavior
```

AI usage without Agent Contract is prohibited.

---

# 22. Human Review Requirement

A service must declare whether human review is required.

Review levels may include:

```text
No Review Required
Optional Review
Review Required
Approval Required
Professional Sign-off Required
Escalation Required
```

Review is required when service output affects:

```text
filing scope
legal position
official submission
client commitment
external agent instruction
AI-generated recommendation
high-risk classification
jurisdiction strategy
evidence sufficiency
```

Review status must be represented through Core Objects, Events and Audit.

---

# 23. Responsibility and Audit

Every service must define responsibility and audit requirements.

Responsibility fields:

```text
service actor
object owner
reviewer
approver
responsible team
external responsible party
AI agent identity if applicable
```

Audit fields:

```text
who invoked the service
when it was invoked
input summary
output summary
objects changed
events emitted
AI used or not
review status
failure or exception
```

High-risk services must always be auditable.

---

# 24. Failure Behavior

A service must define failure behavior.

Failure behavior may include:

```text
reject request
return validation error
create review task
emit failure event
retry later
fallback to manual handling
mark output as partial
block state transition
escalate to responsible user
```

AI failure must not silently produce trusted output.

External integration failure must not corrupt Core state.

---

# 25. Idempotency and Retry Rules

Services that create objects, emit events or call integrations must define idempotency rules.

Required questions:

```text
Can the service be safely retried?
What key prevents duplicate objects?
What key prevents duplicate events?
What happens if external integration succeeds but local update fails?
What happens if local update succeeds but event publishing fails?
```

Examples:

```text
CreateMatter should not create duplicate matters for the same converted order.
DocumentUpload should not duplicate files when retried.
Notification dispatch should not send duplicate urgent messages unless allowed.
```

---

# 26. API Exposure

A service may or may not be exposed through API.

The Service Specification must declare:

```text
API exposed: yes / no / internal only / future
API name
API contract
input contract
output contract
permission requirement
consumer type
event side effects
```

API exposure must follow Appendix F — API Index.

A service must not become public API by accident.

---

# 27. Workflow Usage

A service may be part of a Workflow Contract.

The spec must declare:

```text
workflow name
state before
state after
allowed transition
required actor
review point
events emitted
failure transition
```

Examples:

```text
Order Intake Workflow
Order-to-Matter Workflow
Matter Execution Workflow
AI Recommendation Review Workflow
Document Draft Review Workflow
Routing Review Workflow
```

Workflow rules must not be hidden inside UI or service code.

---

# 28. Product Consumers

A service must declare product consumers.

Consumer categories:

```text
MVP Consumer
Partial Consumer
Future Consumer
```

MVP Consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Partial Consumers:

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

Future Consumers:

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

A future consumer must not force premature MVP implementation.

---

# 29. MVP Phase and Depth

Each service must declare MVP phase and depth.

MVP depth values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Examples:

```text
CreateCustomer
    MVP Depth: Must Implement

RecommendClassification
    MVP Depth: Partial Implement or Must Implement depending on product scope

AdvancedOpportunityScoring
    MVP Depth: Deferred

ProviderMarketplaceRanking
    MVP Depth: Deferred

RouteMatterToAgent
    MVP Depth: Partial Implement
```

Depth controls Codex implementation priority.

---

# 30. Service Naming Rules

Service names should be explicit and action-oriented.

Preferred patterns:

```text
CreateObject
UpdateObject
ValidateObject
NormalizeObject
GenerateOutput
RecommendAction
AssignResponsibility
ApproveReview
RejectReview
PublishEvent
ImportExternalData
SyncExternalData
RouteMatter
```

Examples:

```text
CreateCustomer
CreateOrder
ConvertOrderToMatter
CreateMatter
AssignTask
ValidateClassificationTerms
RecommendClassification
GenerateDocumentDraft
CreateReviewRequest
ApproveAIRecommendation
ImportTrademarkStatus
NotifyReviewRequired
```

Avoid vague names:

```text
HandleData
DoTask
ProcessInfo
RunAI
SubmitForm
UpdateThings
ManageCase
```

---

# 31. Service Anti-Patterns

## 31.1 UI Action as Service

A UI button is treated as a Core Service.

Correction:

```text
Define the underlying Core Service separately from product UI.
```

## 31.2 Direct Database Mutation

Service code mutates data without object, permission, event or audit rules.

Correction:

```text
Service Specification must define object operations and side effects.
```

## 31.3 Eventless Command

A state-changing service emits no event.

Correction:

```text
Meaningful state changes must emit Core Events.
```

## 31.4 Contractless Consumption

A product or integration calls internal service logic without contract.

Correction:

```text
Use API, Data, Event or Consumption Contract.
```

## 31.5 Prompt as Service

An AI prompt is treated as a service.

Correction:

```text
AI behavior must be governed by Agent Contract and attached to a Core Service.
```

## 31.6 Multi-Domain Service Without Owner

A service touches many domains without primary ownership.

Correction:

```text
Declare a primary owning domain or cross-cutting system.
```

## 31.7 Hidden Workflow Logic

Workflow state changes are embedded in service implementation without Workflow Contract.

Correction:

```text
Workflow transitions must be declared.
```

## 31.8 Premature Future Service

A future marketplace, scoring or analytics service enters MVP without approval.

Correction:

```text
Use Deferred or Reserved Boundary classification.
```

---

# 32. Appendix D Readiness

This chapter prepares Appendix D — Core Service Index.

Appendix D must list services with:

```text
service name
service category
owning domain or cross-cutting system
objects read
objects created or updated
events emitted
contracts required
AI usage
review requirement
MVP phase
MVP depth
product consumers
status
```

Appendix D should be generated before detailed service specs.

---

# 33. Relationship to Other Specification Chapters

## 33.1 Relationship to Domain Specification

Domain Specification defines the owner.

Service Specification defines the operation.

## 33.2 Relationship to Object Specification

Object Specification defines meaning and lifecycle.

Service Specification defines how objects are operated.

## 33.3 Relationship to Event Specification

Service Specification defines events emitted and consumed.

Event Specification defines event semantics and payloads.

## 33.4 Relationship to AI Governance Specification

Service Specification declares AI usage.

Agent Specification governs the AI actor.

## 33.5 Relationship to Core Consumption Specification

Service Specification defines what may be consumed.

Consumption Specification defines how products, AI agents, integrations and Codex consume it.

---

# 34. Relationship to core-specs/

This chapter governs future files under:

```text
core-specs/services/
```

A future service spec file should use a filename pattern such as:

```text
create-customer.md
create-order.md
convert-order-to-matter.md
create-matter.md
assign-task.md
recommend-classification.md
generate-document-draft.md
approve-ai-recommendation.md
route-matter-to-agent.md
import-trademark-status.md
notify-review-required.md
```

Each file must follow the Service Specification Template.

---

# 35. Codex Implementation Requirements

Codex may implement a service only when the task provides:

```text
service spec reference
owning domain reference
related object specs
related event specs
contract references
MVP depth
input/output expectations
permission requirements
AI usage rule
review rule
tests required
acceptance criteria
out-of-scope items
```

Codex must not invent service responsibilities.

If a service spec is missing, Codex should create a specification gap issue, not implement the service from assumption.

---

# 36. Specification Output

This chapter produces the following specification outputs:

```text
Core Service Definition
Service Specification Statement
Standard Service Specification Template
Service Metadata Rules
Service Ownership Rule
Service Category Model
Input/Output Rules
Object Operation Rules
State Change Rules
Event Side Effect Rules
Contract Rules
Permission and Policy Rules
Knowledge Dependency Rules
AI Usage Rules
Human Review Rules
Responsibility and Audit Rules
Failure Behavior Rules
Idempotency and Retry Rules
API Exposure Rules
Workflow Usage Rules
Product Consumer Classification
MVP Phase and Depth Rules
Service Naming Rules
Service Anti-Patterns
Appendix D Readiness Requirements
core-specs/services/ Readiness Requirements
Codex Implementation Requirements
```

---

# 37. Execution Mapping

| Service Specification Decision | Execution Impact |
|-------------------------------|------------------|
| Service owner required | Codex must map service to domain/system |
| Objects read/updated required | Object specs must exist before implementation |
| Events emitted required | Event specs must be generated for side effects |
| Contracts required | Consumption and API boundaries are protected |
| Permission rules required | Services cannot bypass access control |
| AI usage required | Agent Contract and audit are mandatory when AI is used |
| Review requirement required | High-risk outputs cannot skip human review |
| MVP depth required | Deferred services do not enter early implementation |
| Failure behavior required | Services become testable and safe |

---

# 38. Exclusions

This chapter does not define:

```text
complete service implementations
programming language code
HTTP route definitions
full API endpoint list
complete database transaction design
vendor adapter implementation
production AI prompts
final event payload schemas
complete test files
```

Those belong to `core-specs/`, Appendix F, implementation tasks and code repositories.

---

# 39. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Service clearly.
[ ] It distinguishes service from UI button, helper, controller, vendor wrapper and prompt.
[ ] It provides a standard Service Specification Template.
[ ] It requires service ownership by domain or cross-cutting system.
[ ] It defines service categories.
[ ] It requires inputs and outputs.
[ ] It requires objects read and objects created/updated.
[ ] It requires state changes and events.
[ ] It requires contracts.
[ ] It requires permission and policy rules.
[ ] It requires knowledge dependencies.
[ ] It requires AI usage boundaries.
[ ] It requires human review rules.
[ ] It requires responsibility and audit.
[ ] It requires failure behavior and idempotency rules.
[ ] It defines API exposure rules.
[ ] It defines workflow usage rules.
[ ] It defines product consumer classification.
[ ] It defines MVP phase and depth.
[ ] It prepares Appendix D — Core Service Index.
[ ] It prepares core-specs/services/.
[ ] It protects Codex from inventing service responsibilities.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 40. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 24, defining Service Specification. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened Service Specification as a governed operation standard, added template, ownership rules, event side effects, contracts, AI/review/audit rules, MVP depth and Codex implementation requirements. |

---

**End of Chapter**
