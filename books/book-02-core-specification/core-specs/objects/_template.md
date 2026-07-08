# Object Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/objects/`  
**Template ID:** B02-TPL-OBJECT  
**Template Type:** Object Specification Template  
**Source Chapter:** B02-CH-23 — Object Specification  
**Source Appendix:** B02-APP-C — Core Object Index  
**Source Index:** indexes/object-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the appropriate object category directory.

Recommended locations:

```text
core-specs/objects/foundation/{object-name}.md
core-specs/objects/professional/{object-name}.md
core-specs/objects/business-execution/{object-name}.md
core-specs/objects/collaboration-network/{object-name}.md
core-specs/objects/cross-cutting/{object-name}.md
core-specs/objects/ai-governance/{object-name}.md
core-specs/objects/codex/{object-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
identity.md
trademark.md
classification-recommendation.md
order-to-matter-link.md
ai-audit-record.md
codex-task.md
```

This template is for Core Objects only.

Do not use this template for:

```text
database tables
DTOs
UI forms
API responses
third-party payloads
spreadsheet columns
product widgets
temporary implementation helpers
```

A Core Object may later be represented by those artifacts, but those artifacts do not define the Core Object.

---

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
**Related Service Specs:** core-specs/services/{service}.md  
**Related Event Specs:** core-specs/events/{event}.md  
**Related Contract Specs:** core-specs/contracts/{contract}.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Primary Consumers:** MarkReg | MarkOrbit Lite | Workplace | AI Agents | Codex Implementation | MGSN | Future Consumers  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Core Object exists.

The purpose should answer:

```text
What professional meaning does this object represent?
Why must this object be part of Core?
Which services, events, contracts, APIs, agents or workflows depend on it?
```

Example format:

```text
The {Object Name} object represents ...
It exists so that ...
It is required by ...
```

---

# 2. Core Meaning

Define the canonical meaning of this object.

```text
{Object Name} means ...
```

This definition must be meaning-first.

Do not define the object as:

```text
a table
a JSON payload
a form
a DTO
an API response
a database row
```

Preferred definition pattern:

```text
This object defines the shared Core meaning of ...
```

---

# 3. Owning Domain or System

State the primary owner.

```text
Primary Owner: {Domain or Cross-Cutting System}
Owner Type: Baseline Core Domain | Cross-Cutting Core Specification System | AI Governance | Codex Task System | Specification Governance
```

Ownership rules:

```text
- Every Core Object must have one primary owner.
- Product ownership is not Core ownership.
- Cross-cutting ownership must be explicit.
- Secondary relationships do not change primary ownership.
```

If the object has secondary relationships, list them.

```text
Related Domains/Systems:
- ...
- ...
```

---

# 4. Object Category

Select one canonical category.

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

Explain why the category is correct.

```text
This object belongs to {Object Category} because ...
```

---

# 5. Scope

Define what is inside this object.

```text
This object includes:
- ...
- ...
- ...
```

The scope should include professional meaning, ownership and executable relevance.

It should not include database implementation, UI layout or third-party-specific payload structure.

---

# 6. Object Boundary

Define the object boundary.

## 6.1 In Boundary

```text
- ...
- ...
```

## 6.2 Out of Boundary

```text
- ...
- ...
```

## 6.3 Boundary Notes

Explain boundary-sensitive distinctions.

Examples:

```text
This object owns ...
This object references ...
This object does not own ...
```

---

# 7. Lifecycle

Define the lifecycle of this object.

Use only states that match the object's meaning.

Example lifecycle:

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

Object-specific lifecycle:

```text
1. ...
2. ...
3. ...
```

If the object has no meaningful lifecycle beyond creation and reference, state that clearly.

```text
This object has a limited lifecycle: created, updated and archived.
```

---

# 8. State Model

Define the state model if the object has operational state.

Use controlled labels.

## 8.1 State Values

```text
- ...
- ...
```

## 8.2 State Transition Rules

```text
{From State} → {To State}
    allowed by: {Service}
    event emitted: {Event}
    review required: Yes / No
```

## 8.3 No-State Reason

If the object has no operational state, state:

```text
This object does not require a separate state model because ...
```

## 8.4 Required Controlled Status Sets

If this is an AI output object, use:

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

If this is a Codex task object, use:

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

# 9. Fields and Meaning

Define meaning-level fields.

Do not define physical database types.

Use this format:

| Field | Meaning | Required | Notes |
|-------|---------|----------|-------|
| id | Canonical identifier for this object | Yes | Must be stable |
| ... | ... | ... | ... |

Allowed field types at this level:

```text
canonical identifier
display name
source reference
owner reference
status
relationship reference
review status
audit reference
created timestamp
updated timestamp
version reference
```

Avoid:

```text
VARCHAR(255)
SQL index
foreign key constraint
ORM decorator
UI component binding
vendor-specific payload field
```

---

# 10. Relationships

List relationships to other Core Objects.

Use this format:

| Related Object | Relationship Type | Direction | Required | Notes |
|----------------|-------------------|-----------|----------|-------|
| {Object} | owns / references / links / validates / reviews / emits / consumes | inbound / outbound / bidirectional | Yes / No | {Notes} |

Relationship types may include:

```text
owns
references
links to
created from
converted to
validated by
reviewed by
approved by
emits event
consumed by service
```

---

# 11. Primary Services

List Core Services that operate this object.

Source:

```text
indexes/service-index.md
```

Use this format:

| Service | Access Type | Purpose | Events Emitted |
|---------|-------------|---------|----------------|
| {Service Name} | read / create / update / link / validate / approve / reject / archive | {Purpose} | {Events} |

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

An object must not mutate itself.

State changes must occur through governed Core Services.

---

# 12. Primary Events

List Core Events involving this object.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Role | Source Service | Meaning |
|-------|------|----------------|---------|
| {Event Name} | subject / related object / payload reference / audit reference | {Service Name} | {Meaning} |

If the object has no related event, state the explicit reason.

```text
No MVP event is required because ...
```

---

# 13. Primary Contracts

List contracts involving this object.

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

Use this format:

| Contract | Contract Type | Required For | Notes |
|----------|---------------|--------------|-------|
| {Contract Name} | {Type} | {Usage} | {Notes} |

Detailed contract specs belong to:

```text
core-specs/contracts/
```

---

# 14. Validation Rules

Define validation rules for this object.

Validation rules should be meaning-level and contract-level.

```text
[ ] Object has canonical identifier.
[ ] Object has owning domain/system.
[ ] Object has required source reference.
[ ] Object has valid status.
[ ] Object relationships are valid.
[ ] Required services are available.
[ ] Required events are mapped.
[ ] Required contracts are defined.
```

Add object-specific validation rules:

```text
[ ] ...
[ ] ...
```

---

# 15. Permission and Policy Rules

Define permission and policy requirements.

## 15.1 Permission Rules

```text
read:
    required permission: ...

create:
    required permission: ...

update:
    required permission: ...

approve/reject:
    required permission: ...

archive/delete:
    required permission: ...
```

## 15.2 Policy Rules

```text
Applicable policies:
- ...
- ...
```

If no special policy is required, state:

```text
No additional object-specific policy is required beyond standard Core permission rules.
```

---

# 16. AI Usage

Define AI usage involving this object.

## 16.1 Allowed AI Usage

```text
AI may:
- ...
- ...
```

## 16.2 Prohibited AI Usage

```text
AI must not:
- ...
- ...
```

## 16.3 AI Governance Requirements

If AI uses or produces this object, define:

```text
AI Agent required: Yes / No
Agent Contract required: Yes / No
Authorized Knowledge required: Yes / No
Human Review required: Yes / No
AI Audit Record required: Yes / No
Related AI Events:
    - ...
```

If AI is not relevant, state:

```text
This object does not require MVP AI usage.
```

AI output must not be treated as final professional truth unless review requirements are satisfied.

---

# 17. Workflow Usage

Define how this object participates in workflow.

```text
Workflow role:
    none / input / output / state object / task object / review object / approval object / event reference

Relevant Workflow Contracts:
    - ...

Relevant Tasks:
    - ...

Relevant State Transitions:
    - ...
```

If workflow is not relevant, state:

```text
This object does not participate in MVP workflow execution.
```

---

# 18. API Exposure

Define API exposure for this object.

```text
API exposure:
    No API / Internal API / Product API / Agent API / Integration API / Admin API

Related APIs:
    - ...

API rules:
    - API must reference service specs.
    - API must not define object meaning.
    - Mutating APIs must map to services and events.
```

Detailed API specs belong to:

```text
core-specs/api/
```

---

# 19. Product Consumers

Classify product consumers.

## 19.1 MVP Consumers

```text
- MarkReg
- MarkOrbit Lite
- Workplace
- AI Agents
- Codex Implementation
```

## 19.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 19.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

Only list consumers that actually consume this object.

Products may consume this object but must not redefine object meaning.

---

# 20. MVP Scope

Define MVP scope for this object.

```text
MVP includes:
- ...
- ...
```

## 20.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 20.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 20.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 21. Deferred Scope

Define what is explicitly deferred.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

---

# 22. Data and Implementation Notes

Provide implementation-facing notes without defining physical schema.

Allowed notes:

```text
- canonical ID required
- source reference required
- state must be controlled
- object must be versioned
- object requires audit reference
- object requires review status
- object may be imported from external source
- object must be linked to owning domain
```

Prohibited notes:

```text
- physical database table schema
- SQL column types
- ORM decorator details
- UI component mapping
- vendor-specific payload design
- undocumented migration shortcuts
```

---

# 23. Codex Implementation Notes

Define how Codex may implement this object.

Codex must:

```text
- cite this object spec
- cite indexes/object-index.md
- cite related domain, service and event specs
- preserve object ownership
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- create unowned objects
- treat database tables as Core Objects
- treat UI forms as Core Objects
- mutate objects outside services
- create AI objects without audit
- implement deferred objects as MVP
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 24. Prohibited Overreach

This object spec must not be used to:

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

Add object-specific prohibited overreach:

```text
- ...
- ...
```

---

# 25. Acceptance Criteria

This Object Specification is accepted only if:

```text
[ ] It defines the object purpose.
[ ] It defines Core meaning.
[ ] It identifies owning domain or cross-cutting system.
[ ] It identifies object category.
[ ] It defines scope.
[ ] It defines object boundary.
[ ] It defines lifecycle.
[ ] It defines state model or explicit no-state reason.
[ ] It defines fields by meaning, not physical schema.
[ ] It defines relationships.
[ ] It lists primary services.
[ ] It lists primary events or explicit no-event reason.
[ ] It lists primary contracts.
[ ] It defines validation rules.
[ ] It defines permission and policy rules.
[ ] It defines AI usage.
[ ] It defines workflow usage.
[ ] It defines API exposure.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines prohibited overreach.
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial object specification created from B02-TPL-OBJECT. |

---

**End of Object Specification**
