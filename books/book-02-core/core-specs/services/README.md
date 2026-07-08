# core-specs/services/

**Repository:** `book-02-core`  
**Directory:** `core-specs/services/`  
**Document:** `core-specs/services/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/services/` directory contains detailed Service Specification files for MarkOrbit Core.

A Core Service is a governed capability that operates Core meaning.

This directory exists to define Core Services in a way that can later be used by:

```text
objects
events
contracts
APIs
agents
workflows
Codex tasks
tests
implementation artifacts
```

The purpose of this directory is not to define UI buttons, controller methods or helper functions.

The purpose is to define the canonical responsibility, inputs, outputs, object access, event side effects, contracts, permission rules, policy rules, review rules, audit requirements and implementation boundaries of Core Services.

---

# 2. Canonical Service Rule

Book 02 uses the following canonical rule:

```text
A Core Service is a governed capability that operates Core meaning.
```

Therefore:

```text
No owning domain or system, no Core Service.
No Core Object relationship, no implementation-ready service.
No input and output contract, no safe service.
No permission or policy boundary, no governed service.
No event or explicit no-event reason, no execution trace.
No acceptance criteria, no Codex implementation.
```

---

# 3. Service Is Not UI Action

A Core Service is not automatically:

```text
a UI button
a menu item
a controller method
a helper function
a database operation
a third-party API wrapper
a background job
a prompt
a workflow screen step
```

A Core Service may later be exposed through those artifacts, but those artifacts do not define the Core Service.

Core responsibility comes first.

Implementation representation comes later.

---

# 4. Directory Boundary

## 4.1 services/ Owns

This directory owns:

```text
Core Service Specification files
service purpose
service ownership
service category
input contract references
output contract references
objects read
objects created
objects updated
objects linked
events emitted
contracts required
permission requirements
policy requirements
review requirements
audit requirements
AI-assisted behavior rules
workflow usage
API exposure notes
failure behavior
idempotency requirements
MVP depth
deferred scope
acceptance criteria
```

## 4.2 services/ Does Not Own

This directory does not own:

```text
domain architecture
object meaning
event payload schemas
API endpoint routing
AI Agent Contracts
workflow transition definitions
product UI
physical database schema
controller code
background worker implementation
third-party integration implementation
Codex implementation code
```

Those belong to other specification layers.

---

# 5. Source Chain

Every Service Specification file must cite its source chain.

Required source chain:

```text
B02-CH-24 — Service Specification
B02-APP-D — Core Service Index
indexes/service-index.md
core-specs/services/{service-name}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
indexes/domain-index.md
indexes/object-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
B02-CH-15 — Core Service Architecture
B02-CH-17 — Core Contract Architecture
B02-CH-23 — Object Specification
B02-CH-25 — Event Specification
B02-CH-26 — AI Capability and Agent Governance Specification
B02-CH-27 — Core Consumption Specification
B02-CH-30 — MVP Execution Matrix
```

---

# 6. Required Service Spec Groups

Service Specification files should be grouped by responsibility.

Expected directory structure:

```text
core-specs/services/README.md
core-specs/services/_template.md

core-specs/services/foundation/
core-specs/services/professional/
core-specs/services/business-execution/
core-specs/services/collaboration-network/
core-specs/services/cross-cutting/
core-specs/services/ai-governance/
core-specs/services/codex/
core-specs/services/validation/
```

Each subdirectory should contain service specs for the corresponding category.

---

# 7. Service Categories

This directory uses the following service categories.

```text
Foundation Service
Professional Service
Business Execution Service
Execution Primitive Service
Collaboration Network Service
Cross-Cutting Service
AI Governance Service
Codex Service
Validation Service
```

A spec must use one canonical category.

---

# 8. Service Spec Metadata

Each Service Specification file must begin with metadata.

```text
# Service Specification — {Service Name}

**Spec ID:** B02-SVC-{SERVICE-ID}
**Spec Type:** Service
**Service Name:** {Service Name}
**Service Category:** Foundation | Professional | Business Execution | Execution Primitive | Collaboration Network | Cross-Cutting | AI Governance | Codex | Validation
**Owning Domain/System:** {Domain or Cross-Cutting System}
**Source Chapter:** B02-CH-24 — Service Specification
**Source Appendix:** B02-APP-D — Core Service Index
**Source Index:** indexes/service-index.md
**Related Domain Spec:** core-specs/domains/{domain}.md
**Related Object Specs:** core-specs/objects/{object}.md
**Related Event Specs:** core-specs/events/{event}.md
**Related Contract Specs:** core-specs/contracts/{contract}.md
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**API Exposure:** No API | Internal API | Product API | Agent API | Integration API | Admin API
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Service Spec Required Sections

Every Service Specification must include the following sections.

```text
1. Purpose
2. Core Responsibility
3. Owning Domain or System
4. Service Category
5. Scope
6. Service Boundary
7. Inputs
8. Outputs
9. Objects Read
10. Objects Created or Updated
11. Objects Linked or Unlinked
12. Events Emitted
13. Contracts Required
14. Permission Rules
15. Policy Rules
16. Review Rules
17. Audit Rules
18. AI Usage
19. Workflow Usage
20. API Exposure
21. Failure Behavior
22. Idempotency and Safety
23. Product Consumers
24. MVP Scope
25. Deferred Scope
26. Data and Implementation Notes
27. Codex Implementation Notes
28. Validation Rules
29. Prohibited Overreach
30. Acceptance Criteria
31. Revision Notes
```

---

# 10. Service Ownership Rules

## 10.1 Every Service Must Have an Owner

Each service must have one primary owner.

The owner must be either:

```text
one of the 26 baseline Core Domains
or an explicitly declared cross-cutting Core specification system
or AI Governance
or Codex Task System
or Specification Governance
```

## 10.2 Cross-Domain Services Must Declare Primary Ownership

A service may operate across domains, but it must still declare one primary owner.

Example:

```text
Order-to-Matter Conversion Service
    Primary Owner: Order
    Related Domain: Matter
```

## 10.3 Product Ownership Is Not Core Ownership

Products may consume Core Services, but products do not own Core Service meaning.

The following are not Core Service owners:

```text
MarkReg
MarkOrbit Lite
Workplace
MGSN
Partner Center
Client Portal
Service Platform
```

## 10.4 Cross-Cutting Ownership Must Be Explicit

Services owned by cross-cutting systems must be explicitly marked.

Examples:

```text
Capability Matching Service
Responsibility Assignment Service
Agent Contract Validation Service
Prohibited Overreach Check Service
```

---

# 11. Input and Output Rules

Every Service Specification must define inputs and outputs.

Inputs should be meaning-level, not physical payload-level.

Allowed input descriptions:

```text
actor identity
permission context
policy context
source object reference
request object
related object reference
review context
AI Agent context
workflow context
```

Outputs should state:

```text
object created
object updated
object linked
state changed
event emitted
review required
validation result
error result
audit record
```

Detailed payload contracts belong to:

```text
core-specs/contracts/
core-specs/api/
```

---

# 12. Service-to-Object Rules

Every implementation-ready service must specify object access.

Allowed access types:

```text
read
create
update
link
unlink
validate
approve
reject
archive
emit-reference
```

Use this structure in service specs:

```text
Objects Read:
- ...

Objects Created:
- ...

Objects Updated:
- ...

Objects Linked:
- ...

Objects Archived:
- ...
```

A service that changes Core state must emit at least one event or provide an explicit no-event reason.

---

# 13. Service-to-Event Rules

Every mutating service must define event side effects.

Examples:

```text
Order Confirmation Service
    emits: OrderConfirmed

Order-to-Matter Conversion Service
    emits: OrderConvertedToMatter
    emits: MatterCreated

Classification Recommendation Service
    emits: ClassificationRecommendationGenerated
    emits: ClassificationReviewRequired

Agent Contract Validation Service
    emits: AgentContractValidated
    or: AgentContractValidationFailed
```

Event detail belongs to:

```text
core-specs/events/
```

Service specs reference event meaning and emission conditions.

---

# 14. Service-to-Contract Rules

Every Core Service must reference required contracts.

Contract types may include:

```text
Input Contract
Output Contract
Data Contract
Service Contract
Event Contract
API Contract
Workflow Contract
Permission Contract
Policy Contract
Review Contract
Agent Contract
Codex Task Contract
```

A service without contract references is not implementation-ready.

---

# 15. Permission Rules

Every Core Service that reads, creates, updates, exports or invokes Core Objects must check permission.

Permission rules should define:

```text
who may invoke this service
which objects may be accessed
which actions are allowed
which roles or scopes are required
what happens when permission fails
whether failure emits an event
whether failure is audited
```

Permission-related services include:

```text
Permission Check Service
Access Scope Resolution Service
Permission Assignment Service
```

---

# 16. Policy Rules

Services affected by jurisdiction, AI risk, data exposure, review or business responsibility must check policy.

Policy rules should define:

```text
applicable policies
policy source
policy evaluation point
failure behavior
event emitted on violation
audit requirement
review requirement
```

Policy-sensitive services include:

```text
Jurisdiction Rule Validation Service
Classification Recommendation Service
Document Draft Service
Evidence Review Service
AI Risk Policy Check Service
Routing Recommendation Service
Prohibited Overreach Check Service
```

---

# 17. Review Rules

Services that produce high-risk professional output must require review.

Review-required service examples:

```text
Classification Recommendation Service
Classification Review Service
Document Draft Service
Evidence Review Service
Routing Recommendation Service
AI Output Registration Service
Office Action Analysis Service
Approval Service
```

Review rules should define:

```text
review trigger
review owner
review object
approval object
review events
blocking behavior
failure behavior
```

Review and approval objects belong primarily to:

```text
Business Responsibility
AI Governance
Workflow Contract
Task
```

---

# 18. Audit Rules

Audit is required when a service:

```text
uses professional knowledge
changes legal or business state
produces AI output
generates recommendation
requires review
approves or rejects output
changes responsibility
changes permission
detects policy violation
executes Codex task
detects prohibited overreach
```

Audit-related objects include:

```text
AI Audit Record
Event Audit Reference
Review Record
Approval Record
Validation Report
```

---

# 19. AI-Assisted Service Rules

AI-assisted services must follow AI governance.

AI-assisted services require:

```text
AI Agent
Agent Contract
Authorized Knowledge
Permission Check
Policy Check
AI Output
AI Audit Record
Review Rule
Event Emission
```

AI-assisted service examples:

```text
Classification Recommendation Service
Document Draft Service
Evidence Review Service
Trademark Lifecycle Summary Service
Communication Summary Service
Opportunity Detection Baseline Service
Routing Recommendation Service
Workflow Assistance Service
Spec Consistency Check Service
```

AI-assisted services must not:

```text
make final professional decisions without review
submit official filings
alter evidence
invent legal authority
change Core state directly outside governed services
bypass audit
```

---

# 20. Workflow Usage Rules

Services used in workflow execution must specify:

```text
workflow contract
allowed state transition
task creation or update
review requirement
events emitted
failure behavior
```

Workflow-critical services include:

```text
Order-to-Matter Conversion Service
Workflow Transition Validation Service
Task Creation Service
Task Assignment Service
Task Completion Service
Task Review Service
Matter Status Service
Approval Service
Event Publication Service
Notification Dispatch Service
```

---

# 21. API Exposure Rules

A service may be exposed through API only when it has:

```text
input contract
output contract
permission rule
policy rule
event side-effect definition
consumer classification
error contract
audit rule if required
```

API exposure levels:

```text
No API
Internal API
Product API
Agent API
Integration API
Admin API
```

MVP API exposure should be conservative.

High-risk services should use internal or product-mediated APIs first.

---

# 22. Failure Behavior Rules

Every Service Specification must define failure behavior.

Failure behavior should include:

```text
validation failure
permission failure
policy failure
missing object
invalid state transition
review required
AI governance failure
external dependency failure
idempotency conflict
unexpected error
```

For each failure type, define:

```text
result
event emitted if any
audit requirement
retry rule
review or escalation requirement
```

---

# 23. Idempotency and Safety Rules

Services that create or mutate Core state must define idempotency and safety behavior.

Relevant services include:

```text
Identity Registration Service
Order Creation Service
Order Confirmation Service
Order-to-Matter Conversion Service
Matter Creation Service
Task Creation Service
Event Publication Service
AI Output Registration Service
Codex Task Execution Service
```

Each spec should state:

```text
idempotency key or equivalent rule
duplicate handling
safe retry behavior
state conflict behavior
event duplication prevention
```

---

# 24. High-Priority Service Specs

Initial service specs should prioritize:

```text
identity-registration-service.md
identity-resolution-service.md
actor-identity-lookup-service.md
organization-registration-service.md
organization-membership-service.md
user-registration-service.md
user-profile-service.md
user-role-assignment-service.md
permission-check-service.md
access-scope-resolution-service.md
knowledge-retrieval-service.md
knowledge-source-registration-service.md
knowledge-asset-validation-service.md
brand-registration-service.md
trademark-registration-service.md
trademark-status-normalization-service.md
trademark-lookup-service.md
jurisdiction-requirement-lookup-service.md
jurisdiction-rule-validation-service.md
classification-recommendation-service.md
classification-validation-service.md
goods-services-term-lookup-service.md
classification-review-service.md
document-upload-service.md
document-requirement-service.md
document-validation-service.md
customer-registration-service.md
order-creation-service.md
order-validation-service.md
order-confirmation-service.md
order-to-matter-conversion-service.md
matter-creation-service.md
matter-status-service.md
workflow-contract-registration-service.md
workflow-transition-validation-service.md
task-creation-service.md
task-assignment-service.md
task-completion-service.md
task-review-service.md
event-publication-service.md
event-validation-service.md
responsibility-assignment-service.md
review-assignment-service.md
approval-service.md
agent-contract-validation-service.md
ai-output-registration-service.md
ai-audit-recording-service.md
prohibited-overreach-check-service.md
```

---

# 25. MVP Depth Rules

Service specs must preserve MVP depth from:

```text
indexes/service-index.md
```

Allowed values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A `Reserved Boundary` service may be specified at boundary level but should not be production-enabled in MVP.

A `Deferred` service should not be implemented without a later approved scope change.

---

# 26. Product Consumer Rules

Service specs must classify product consumers.

Consumer categories:

```text
MVP Consumer
Partial Consumer
Future Consumer
```

MVP consumers:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

Products may consume Core Services.

Products must not redefine service responsibility.

---

# 27. Data and Implementation Notes

Service specs may include implementation-facing notes.

Allowed notes:

```text
idempotency required
transaction boundary required
event publication required
audit record required
permission check required
policy check required
review queue required
source object lock required
retry strategy required
```

Prohibited notes:

```text
controller code
ORM implementation
physical database schema
UI component behavior
vendor-specific infrastructure
unreviewed background worker design
```

---

# 28. Codex Implementation Rules

Codex tasks generated from service specs must:

```text
cite the service spec
cite indexes/service-index.md
cite related object and event specs
preserve service ownership
preserve MVP depth
preserve deferred scope
write tests
follow prohibited-overreach rules
```

Codex must not:

```text
create services without owning domain or system
create services without related objects
create mutating services without events
create AI services without Agent Contract
create services that bypass permission or policy
implement deferred services as MVP
treat UI actions as Core Services
```

---

# 29. Validation Rules

The `core-specs/services/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] Every service spec has metadata.
[ ] Every service spec references indexes/service-index.md.
[ ] Every service has an owning domain or cross-cutting system.
[ ] Every service has a category.
[ ] Every service has MVP phase or wave.
[ ] Every service has MVP depth.
[ ] Every service defines purpose and Core responsibility.
[ ] Every service defines inputs.
[ ] Every service defines outputs.
[ ] Every service defines objects read or explicit no-read reason.
[ ] Every service defines objects created/updated or explicit no-mutation reason.
[ ] Every mutating service defines events emitted or explicit no-event reason.
[ ] Every service defines required contracts.
[ ] Every service defines permission rules.
[ ] Every policy-sensitive service defines policy rules.
[ ] Every high-risk service defines review rules.
[ ] Every AI-assisted service defines Agent Contract and audit requirements.
[ ] Every service defines failure behavior.
[ ] Every mutating service defines idempotency or safety rules.
[ ] No service is only a UI action.
[ ] No service is only a database operation.
```

---

# 30. Prohibited Behavior

This directory must not:

```text
add UI buttons as Core Services
add product-specific workflow steps as Core Services without Core meaning
add database CRUD operations as Core Services without governance
create services without owning domain or system
create AI services without Agent Contract
create AI services without audit
create mutating services without events
create services that bypass permission or policy
create official filing automation in MVP
create full marketplace services in MVP
create full opportunity scoring in MVP
rename canonical services without architecture review
define product UI
define physical database schema
```

---

# 31. Acceptance Criteria

The `core-specs/services/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/services/.
[ ] It defines Core Service as a governed capability that operates Core meaning.
[ ] It distinguishes service from UI action, helper, database operation and API wrapper.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required service spec groups.
[ ] It defines service categories.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines service ownership rules.
[ ] It defines input and output rules.
[ ] It defines service-to-object rules.
[ ] It defines service-to-event rules.
[ ] It defines service-to-contract rules.
[ ] It defines permission rules.
[ ] It defines policy rules.
[ ] It defines review rules.
[ ] It defines audit rules.
[ ] It defines AI-assisted service rules.
[ ] It defines workflow usage rules.
[ ] It defines API exposure rules.
[ ] It defines failure behavior rules.
[ ] It defines idempotency and safety rules.
[ ] It lists high-priority service specs.
[ ] It defines MVP depth rules.
[ ] It defines product consumer rules.
[ ] It defines data and implementation notes.
[ ] It defines Codex implementation rules.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 32. Next Action

After this README is accepted, generate:

```text
core-specs/services/_template.md
```

Do not generate detailed service specs before the template exists.

---

# 33. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/services/. Defines directory purpose, service responsibility, ownership, contracts, permission/policy/review/audit rules, AI-assisted service rules, validation rules and template handoff. |

---

**End of README**
