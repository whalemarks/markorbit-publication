# core-specs/objects/

**Repository:** `book-02-core`  
**Directory:** `core-specs/objects/`  
**Document:** `core-specs/objects/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/objects/` directory contains detailed Object Specification files for MarkOrbit Core.

A Core Object is professional meaning before data structure.

This directory exists to define Core Objects in a way that can later be used by:

```text
services
events
contracts
APIs
agents
workflows
Codex tasks
tests
implementation artifacts
```

The purpose of this directory is not to design database tables.

The purpose is to define the canonical meaning, ownership, lifecycle, relationships, validation rules and implementation boundaries of Core Objects.

---

# 2. Canonical Object Rule

Book 02 uses the following canonical rule:

```text
A Core Object is professional meaning before data structure.
Every Core Object must have an owning Core Domain or an explicitly declared cross-cutting specification system.
```

Therefore:

```text
No owner, no Core Object.
No professional meaning, no Core Object.
No lifecycle, no Core Object.
No service relationship, no implementation-ready object.
No event or contract relationship, no executable object.
```

---

# 3. Object Is Not Data Structure

A Core Object is not automatically:

```text
a database table
a DTO
a JSON object
an API response
a UI form
a spreadsheet row
a third-party payload
a file format
```

A Core Object may later be represented by those artifacts, but those artifacts do not define the Core Object.

Core meaning comes first.

Implementation representation comes later.

---

# 4. Directory Boundary

## 4.1 objects/ Owns

This directory owns:

```text
Core Object Specification files
object meaning
object ownership
object category
object lifecycle
object state model
object relationships
object validation rules
object service usage
object event usage
object contract mapping
object AI usage
object workflow usage
object API exposure notes
object MVP depth
object deferred scope
object acceptance criteria
```

## 4.2 objects/ Does Not Own

This directory does not own:

```text
domain architecture
service implementation logic
event payload schemas
API endpoint definitions
AI Agent Contracts
workflow transition definitions
product UI
physical database schema
ORM models
migration scripts
third-party integration payloads
Codex implementation code
```

Those belong to other specification layers.

---

# 5. Source Chain

Every Object Specification file must cite its source chain.

Required source chain:

```text
B02-CH-23 — Object Specification
B02-APP-C — Core Object Index
indexes/object-index.md
core-specs/objects/{object-name}.md
codex-tasks/{task}.md
```

Related sources may include:

```text
indexes/domain-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
B02-CH-14 — Core Object Architecture
B02-CH-22 — Domain Specification
B02-CH-24 — Service Specification
B02-CH-25 — Event Specification
B02-CH-26 — AI Capability and Agent Governance Specification
B02-CH-27 — Core Consumption Specification
B02-CH-30 — MVP Execution Matrix
```

---

# 6. Required Object Spec Groups

Object Specification files should be grouped by responsibility.

Expected directory structure:

```text
core-specs/objects/README.md
core-specs/objects/_template.md

core-specs/objects/foundation/
core-specs/objects/professional/
core-specs/objects/business-execution/
core-specs/objects/collaboration-network/
core-specs/objects/cross-cutting/
core-specs/objects/ai-governance/
core-specs/objects/codex/
```

Each subdirectory should contain object specs for the corresponding category.

---

# 7. Object Categories

This directory uses the following object categories.

```text
Foundation Object
Professional Object
Business Execution Object
Execution Primitive Object
Collaboration Network Object
Contract Object
Governance Object
AI Governance Object
Cross-Cutting Object
Codex Object
```

A spec must use one canonical category.

---

# 8. Object Spec Metadata

Each Object Specification file must begin with metadata.

```text
# Object Specification — {Object Name}

**Spec ID:** B02-OBJ-{OBJECT-ID}
**Spec Type:** Object
**Object Name:** {Object Name}
**Object Category:** Foundation | Professional | Business Execution | Execution Primitive | Collaboration Network | Contract | Governance | AI Governance | Cross-Cutting | Codex
**Owning Domain/System:** {Domain or Cross-Cutting System}
**Source Chapter:** B02-CH-23 — Object Specification
**Source Appendix:** B02-APP-C — Core Object Index
**Source Index:** indexes/object-index.md
**Related Domain Spec:** core-specs/domains/{domain}.md
**Status:** Draft
**Version:** 0.1.0
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Object Spec Required Sections

Every Object Specification must include the following sections.

```text
1. Purpose
2. Core Meaning
3. Owning Domain or System
4. Object Category
5. Scope
6. Object Boundary
7. Lifecycle
8. State Model
9. Fields and Meaning
10. Relationships
11. Primary Services
12. Primary Events
13. Primary Contracts
14. Validation Rules
15. Permission and Policy Rules
16. AI Usage
17. Workflow Usage
18. API Exposure
19. Product Consumers
20. MVP Scope
21. Deferred Scope
22. Data and Implementation Notes
23. Codex Implementation Notes
24. Prohibited Overreach
25. Acceptance Criteria
26. Revision Notes
```

---

# 10. Object Ownership Rules

## 10.1 Every Object Must Have an Owner

Each object must have one primary owner.

The owner must be either:

```text
one of the 26 baseline Core Domains
or an explicitly declared cross-cutting Core specification system
```

## 10.2 Product Ownership Is Not Core Ownership

A product may consume a Core Object, but a product does not own Core Object meaning.

The following are not Core Object owners:

```text
MarkReg
MarkOrbit Lite
Workplace
MGSN
Partner Center
Client Portal
Service Platform
```

## 10.3 Cross-Cutting Ownership Must Be Explicit

Objects owned by cross-cutting systems must be explicitly marked.

Examples:

```text
Capability
Business Responsibility
AI Governance
Codex Task System
Specification Governance
```

## 10.4 No Unowned Object

An object without ownership is not implementation-ready.

---

# 11. Object Lifecycle Rules

Each Object Specification must define lifecycle.

Lifecycle may include:

```text
created
registered
validated
linked
updated
review required
approved
rejected
active
inactive
archived
superseded
deleted
```

Not every object needs every lifecycle state.

The lifecycle must match the object's professional meaning.

---

# 12. Object State Model Rules

Objects with operational state must define a state model.

Examples:

```text
Trademark Status
Order Status
Matter Status
Task Status
Review Status
AI Output Status
Codex Task Status
```

State labels must be controlled.

AI output states must use:

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

Codex task states must use:

```text
Draft
Ready
In Progress
Blocked
Implemented
Tested
Accepted
Rejected
Deferred
Superseded
```

---

# 13. Field Meaning Rules

Object specs may define fields, but fields must be meaning-first.

Allowed field definitions:

```text
canonical identifier
display name
source reference
status
owner reference
relationship reference
review status
audit reference
created timestamp
updated timestamp
```

Avoid physical implementation definitions such as:

```text
VARCHAR(255)
SQL index
ORM relation
database partition
UI component binding
```

Those belong to implementation design, not object meaning.

---

# 14. Object-to-Service Rule

Every implementation-ready object must identify services that operate it.

Examples:

```text
Identity
    Identity Registration Service
    Identity Resolution Service

Classification Recommendation
    Classification Recommendation Service
    Classification Review Service

AI Output
    AI Output Registration Service
    AI Review Routing Service
    AI Audit Recording Service
```

An object must not mutate itself.

State changes must occur through governed Core Services.

---

# 15. Object-to-Event Rule

Objects produce or participate in Core Events when meaningful state changes occur.

Examples:

```text
Order
    OrderCreated
    OrderConfirmed
    OrderConvertedToMatter

Task
    TaskCreated
    TaskAssigned
    TaskCompleted
    TaskReviewRequired

AI Output
    AIOutputGenerated
    AIReviewRequired
    AIAuditRecordCreated
```

Events are specified in:

```text
core-specs/events/
```

Object specs should reference events but not define full payload contracts.

---

# 16. Object-to-Contract Rule

Each object should identify related contracts.

Contract types may include:

```text
Data Contract
API Contract
Event Contract
Workflow Contract
Agent Contract
Review Contract
Permission Contract
Policy Contract
Codex Task Contract
```

Examples:

```text
Trademark
    Trademark Data Contract
    Trademark API Contract
    Trademark Event Contract

Agent Contract
    Agent Contract
    Agent API Contract
    AI Audit Contract

Review Record
    Review Contract
    Approval Contract
```

Detailed contracts belong to:

```text
core-specs/contracts/
```

---

# 17. AI Governance Object Rules

AI-related objects must preserve governance.

AI governance objects include:

```text
AI Agent
AI Agent Identity
Agent Contract
AI Output
AI Recommendation
AI Draft
AI Audit Record
Review Record
Authorized Knowledge Source
```

AI governance object specs must define:

```text
risk level
review requirement
authorized knowledge reference
permission requirement
policy requirement
audit requirement
events emitted
prohibited use
```

AI output must not be treated as final professional truth unless review requirements are satisfied.

---

# 18. Codex Object Rules

Codex-related objects exist to keep implementation controlled.

Codex objects include:

```text
Codex Task
Spec File
Test Fixture
Implementation Artifact
Acceptance Criteria
Validation Report
```

Codex object specs must define:

```text
source specification requirement
task status
test requirement
prohibited-overreach rule
acceptance rule
release relationship
```

Codex must not create new Core Objects unless the object index is updated and approved.

---

# 19. High-Priority Object Specs

Initial object specs should prioritize:

```text
identity.md
actor.md
ai-agent-identity.md
organization.md
organization-membership.md
user.md
user-profile.md
user-role-assignment.md
permission-rule.md
access-scope.md
knowledge-source.md
knowledge-asset.md
knowledge-citation.md
brand.md
brand-owner.md
trademark.md
trademark-owner.md
trademark-status.md
trademark-goods-services.md
trademark-lifecycle-record.md
jurisdiction.md
trademark-office.md
jurisdiction-requirement.md
classification.md
class.md
goods-services-term.md
classification-recommendation.md
classification-review-record.md
document.md
document-requirement.md
document-metadata.md
customer.md
order.md
order-item.md
order-status.md
order-to-matter-link.md
matter.md
matter-status.md
matter-context.md
workflow-contract.md
workflow-state.md
workflow-transition.md
task.md
task-assignment.md
task-status.md
event.md
event-payload.md
responsibility-assignment.md
review-record.md
approval-record.md
ai-agent.md
agent-contract.md
ai-output.md
ai-recommendation.md
ai-audit-record.md
codex-task.md
spec-file.md
test-fixture.md
```

---

# 20. MVP Depth Rules

Object specs must preserve MVP depth from:

```text
indexes/object-index.md
```

Allowed values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A `Reserved Boundary` object may be specified at boundary level but should not be production-enabled in MVP.

A `Deferred` object should not be implemented without a later approved scope change.

---

# 21. Product Consumer Rules

Object specs must classify product consumers.

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

Products may consume Core Objects.

Products must not redefine object meaning.

---

# 22. Data and Implementation Notes

Object specs may include implementation-facing notes.

Allowed notes:

```text
canonical ID required
source reference required
state must be controlled
object must be versioned
object requires audit reference
object requires review status
object may be imported from external source
object must be linked to owning domain
```

Prohibited notes:

```text
physical table schema
SQL column type
ORM implementation
UI component mapping
vendor-specific payload design
unreviewed migration strategy
```

---

# 23. Codex Implementation Rules

Codex tasks generated from object specs must:

```text
cite the object spec
cite indexes/object-index.md
cite related domain, service and event specs
preserve object ownership
preserve MVP depth
preserve deferred scope
write tests
follow prohibited-overreach rules
```

Codex must not:

```text
create unowned objects
treat database tables as Core Objects
treat UI forms as Core Objects
mutate objects outside services
create AI objects without audit
implement deferred objects as MVP
```

---

# 24. Validation Rules

The `core-specs/objects/` directory must pass the following checks.

```text
[ ] It contains README.md.
[ ] It contains _template.md before detailed specs.
[ ] Every object spec has metadata.
[ ] Every object spec references indexes/object-index.md.
[ ] Every object has an owning domain or cross-cutting system.
[ ] Every object has a category.
[ ] Every object has MVP phase or wave.
[ ] Every object has MVP depth.
[ ] Every object defines Core meaning.
[ ] Every object defines lifecycle.
[ ] Every operational object defines state model or explicit no-state reason.
[ ] Every object lists related services.
[ ] Every object lists related events or explicit no-event reason.
[ ] Every object lists related contracts.
[ ] Every AI object defines review and audit requirements.
[ ] Every Codex object defines source specification requirements.
[ ] No object is only a database table.
[ ] No object is only a UI component.
```

---

# 25. Prohibited Behavior

This directory must not:

```text
turn database tables into Core Objects without meaning definition
add product screens as Core Objects
add DTOs as Core Objects without canonical ownership
create unowned objects
create AI outputs without audit
create AI agents without Agent Contract
treat Capability as an ordinary baseline domain
treat Business Responsibility as an ordinary baseline domain
merge objects across domains without architecture review
rename canonical objects without architecture review
implement deferred objects as MVP without approval
define product UI
define physical database schema
```

---

# 26. Acceptance Criteria

The `core-specs/objects/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/objects/.
[ ] It defines Core Object as professional meaning before data structure.
[ ] It distinguishes object from database table, DTO, API response and UI form.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required object spec groups.
[ ] It defines object categories.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines ownership rules.
[ ] It defines lifecycle rules.
[ ] It defines state model rules.
[ ] It defines field meaning rules.
[ ] It defines object-to-service rules.
[ ] It defines object-to-event rules.
[ ] It defines object-to-contract rules.
[ ] It defines AI governance object rules.
[ ] It defines Codex object rules.
[ ] It lists high-priority object specs.
[ ] It defines MVP depth rules.
[ ] It defines product consumer rules.
[ ] It defines data and implementation notes.
[ ] It defines Codex implementation rules.
[ ] It defines validation rules.
[ ] It defines prohibited behavior.
```

---

# 27. Next Action

After this README is accepted, generate:

```text
core-specs/objects/_template.md
```

Do not generate detailed object specs before the template exists.

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/objects/. Defines directory purpose, object meaning, ownership, lifecycle, relationships, AI governance objects, Codex objects, validation rules and template handoff. |

---

**End of README**
