# Service Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/services/`  
**Template ID:** B02-TPL-SERVICE  
**Template Type:** Service Specification Template  
**Source Chapter:** B02-CH-24 — Service Specification  
**Source Appendix:** B02-APP-D — Core Service Index  
**Source Index:** indexes/service-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the appropriate service category directory.

Recommended locations:

```text
core-specs/services/foundation/{service-name}.md
core-specs/services/professional/{service-name}.md
core-specs/services/business-execution/{service-name}.md
core-specs/services/collaboration-network/{service-name}.md
core-specs/services/cross-cutting/{service-name}.md
core-specs/services/ai-governance/{service-name}.md
core-specs/services/codex/{service-name}.md
core-specs/services/validation/{service-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
identity-registration-service.md
classification-recommendation-service.md
order-to-matter-conversion-service.md
agent-contract-validation-service.md
prohibited-overreach-check-service.md
```

This template is for Core Services only.

Do not use this template for:

```text
UI buttons
menu items
controller methods
helper functions
database CRUD helpers
third-party API wrappers
background jobs without Core meaning
prompts
product-specific workflow steps
```

A Core Service may later be represented by controllers, workers, APIs or UI actions, but those artifacts do not define the Core Service.

---

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
**Related API Specs:** core-specs/api/{api}.md  
**Related Agent Specs:** core-specs/agents/{agent}.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Wave 0–7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**API Exposure:** No API | Internal API | Product API | Agent API | Integration API | Admin API  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Core Service exists.

The purpose should answer:

```text
What Core meaning does this service operate?
Why must this capability be governed by Core?
Which objects, events, contracts, APIs, agents or workflows depend on it?
```

Example format:

```text
The {Service Name} operates ...
It exists so that ...
It is required by ...
```

---

# 2. Core Responsibility

Define the canonical responsibility of this service.

```text
{Service Name} is responsible for ...
```

The responsibility must be Core-level, not UI-level.

Avoid definitions such as:

```text
This service handles the button click for ...
This service runs a database update for ...
This service calls vendor API ...
```

Preferred definition pattern:

```text
This service governs the Core operation of ...
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
- Every Core Service must have one primary owner.
- Cross-domain services must declare primary ownership.
- Product ownership is not Core ownership.
- Cross-cutting ownership must be explicit.
```

If the service has secondary relationships, list them.

```text
Related Domains/Systems:
- ...
- ...
```

---

# 4. Service Category

Select one canonical category.

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

Explain why the category is correct.

```text
This service belongs to {Service Category} because ...
```

---

# 5. Scope

Define what is inside this service.

```text
This service includes:
- ...
- ...
- ...
```

The scope should include governed service behavior, object operations, event side effects and contract obligations.

It should not include product UI, physical database implementation or vendor-specific integration details.

---

# 6. Service Boundary

Define the service boundary.

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
This service owns ...
This service invokes ...
This service emits ...
This service does not own ...
```

---

# 7. Inputs

Define the meaning-level inputs required by this service.

Do not define physical request payloads here.

Use this format:

| Input | Meaning | Required | Source | Notes |
|-------|---------|----------|--------|-------|
| actor_identity | Actor invoking the service | Yes | Identity | Required for permission check |
| ... | ... | ... | ... | ... |

Common input types:

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
idempotency key
correlation ID
```

Detailed input payload contracts belong to:

```text
core-specs/contracts/
core-specs/api/
```

---

# 8. Outputs

Define service outputs.

Use this format:

| Output | Meaning | Required | Notes |
|--------|---------|----------|-------|
| {Output Name} | {Meaning} | Yes / No | {Notes} |

Common output types:

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

If the service does not mutate state, state that explicitly.

```text
This service is read-only and does not mutate Core state.
```

---

# 9. Objects Read

List Core Objects read by this service.

Source:

```text
indexes/object-index.md
```

Use this format:

| Object | Purpose of Read | Required | Notes |
|--------|-----------------|----------|-------|
| {Object Name} | {Purpose} | Yes / No | {Notes} |

If no objects are read, state the explicit reason.

```text
This service does not read existing Core Objects because ...
```

---

# 10. Objects Created or Updated

List Core Objects created or updated by this service.

Use this format:

| Object | Operation | Conditions | Notes |
|--------|-----------|------------|-------|
| {Object Name} | create / update / validate / approve / reject / archive | {Conditions} | {Notes} |

Allowed operations:

```text
create
update
validate
approve
reject
archive
deactivate
supersede
```

If no objects are created or updated, state:

```text
This service does not create or update Core Objects.
```

---

# 11. Objects Linked or Unlinked

List relationship changes made by this service.

Use this format:

| Source Object | Target Object | Operation | Meaning |
|---------------|---------------|-----------|---------|
| {Object} | {Object} | link / unlink | {Meaning} |

If the service does not create relationships, state:

```text
This service does not link or unlink Core Objects.
```

---

# 12. Events Emitted

List Core Events emitted by this service.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Trigger | Payload Contract | Required |
|-------|---------|------------------|----------|
| {Event Name} | {Trigger} | {Contract} | Yes / No |

Rules:

```text
- Mutating services must emit events.
- Review-triggering services must emit review events.
- AI-assisted services must emit AI governance events where required.
- Permission or policy failure may require audit or failure events.
```

If the service emits no event, state the explicit no-event reason.

```text
No event is emitted because this service is read-only and produces no meaningful Core state change.
```

---

# 13. Contracts Required

List required contracts.

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

Use this format:

| Contract | Contract Type | Required For | Notes |
|----------|---------------|--------------|-------|
| {Contract Name} | {Type} | {Usage} | {Notes} |

A service without contract references is not implementation-ready.

---

# 14. Permission Rules

Define permission requirements.

Use this structure:

```text
Invoker Requirements:
- ...

Object Access Requirements:
- read:
    - ...
- create:
    - ...
- update:
    - ...
- approve/reject:
    - ...
- archive/delete:
    - ...

Permission Failure Behavior:
- result:
- event emitted:
- audit required:
```

Every Core Service that reads, creates, updates, exports or invokes Core Objects must check permission.

---

# 15. Policy Rules

Define policy requirements.

Use this structure:

```text
Applicable Policies:
- ...

Policy Evaluation Point:
- before object read
- before mutation
- before event emission
- before external exposure
- before AI use
- before approval
```

Policy failure behavior:

```text
result:
event emitted:
audit required:
review required:
```

If no special policy is required, state:

```text
No additional service-specific policy is required beyond standard Core permission rules.
```

---

# 16. Review Rules

Define review requirements.

Use this structure:

```text
Review Required: Yes / No

Review Trigger:
- ...

Review Owner:
- ...

Review Object:
- Review Record
- Approval Record
- Responsibility Assignment

Review Events:
- ReviewRequired
- ReviewApproved
- ReviewRejected

Blocking Behavior:
- blocks external use
- blocks state transition
- blocks final output
- advisory only
```

High-risk professional services must require review.

---

# 17. Audit Rules

Define audit requirements.

Use this structure:

```text
Audit Required: Yes / No

Audit Trigger:
- ...

Audit Object:
- AI Audit Record
- Event Audit Reference
- Review Record
- Approval Record
- Validation Report

Audit Content:
- actor identity
- service name
- objects accessed
- output reference
- policy context
- review status
- event IDs
- timestamp
```

Audit is required when the service:

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

---

# 18. AI Usage

Define AI usage.

## 18.1 AI Assistance

```text
AI usage:
    none / optional / required / prohibited
```

## 18.2 Allowed AI Assistance

```text
AI may:
- ...
- ...
```

## 18.3 Prohibited AI Behavior

```text
AI must not:
- ...
- ...
```

## 18.4 Required AI Governance

If AI is used, define:

```text
AI Agent required: Yes / No
Agent Contract required: Yes / No
Authorized Knowledge required: Yes / No
Human Review required: Yes / No
AI Audit Record required: Yes / No
Related AI Events:
    - ...
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

# 19. Workflow Usage

Define workflow usage.

Use this structure:

```text
Workflow role:
    none / workflow source / state transition validator / task creator / task updater / review trigger / approval gate / event source

Relevant Workflow Contracts:
- ...

Relevant State Transitions:
- ...

Relevant Tasks:
- ...

Workflow Events:
- ...

Failure Behavior:
- ...
```

If workflow is not relevant, state:

```text
This service does not participate in MVP workflow execution.
```

---

# 20. API Exposure

Define API exposure.

```text
API exposure:
    No API / Internal API / Product API / Agent API / Integration API / Admin API
```

Related APIs:

```text
- ...
```

API exposure requires:

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

Mutating APIs must map to this service and its events.

---

# 21. Failure Behavior

Define failure behavior.

Use this format:

| Failure Type | Result | Event Emitted | Audit Required | Retry Rule | Review/Escalation |
|--------------|--------|---------------|----------------|------------|-------------------|
| validation failure | ... | ... | ... | ... | ... |
| permission failure | ... | ... | ... | ... | ... |
| policy failure | ... | ... | ... | ... | ... |
| missing object | ... | ... | ... | ... | ... |
| invalid state transition | ... | ... | ... | ... | ... |
| AI governance failure | ... | ... | ... | ... | ... |
| external dependency failure | ... | ... | ... | ... | ... |
| idempotency conflict | ... | ... | ... | ... | ... |

Add service-specific failure types as needed.

---

# 22. Idempotency and Safety

Define idempotency and safety behavior.

This is required for services that create or mutate Core state.

Use this structure:

```text
Idempotency required: Yes / No

Idempotency Key:
- ...

Duplicate Handling:
- ...

Safe Retry Behavior:
- ...

State Conflict Behavior:
- ...

Event Duplication Prevention:
- ...
```

If idempotency is not relevant, state:

```text
This service is read-only and does not require idempotency beyond standard request tracing.
```

---

# 23. Product Consumers

Classify product consumers.

## 23.1 MVP Consumers

```text
- MarkReg
- MarkOrbit Lite
- Workplace
- AI Agents
- Codex Implementation
```

## 23.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 23.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

Only list consumers that actually consume this service.

Products may consume this service but must not redefine service responsibility.

---

# 24. MVP Scope

Define MVP scope for this service.

```text
MVP includes:
- ...
- ...
```

## 24.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 24.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 24.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 25. Deferred Scope

Define what is explicitly deferred.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

---

# 26. Data and Implementation Notes

Provide implementation-facing notes without defining physical schema or code.

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

# 27. Codex Implementation Notes

Define how Codex may implement this service.

Codex must:

```text
- cite this service spec
- cite indexes/service-index.md
- cite related object and event specs
- preserve service ownership
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- create services without owning domain or system
- create services without related objects
- create mutating services without events
- create AI services without Agent Contract
- create services that bypass permission or policy
- implement deferred services as MVP
- treat UI actions as Core Services
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 28. Validation Rules

This Service Specification must pass the following checks.

```text
[ ] Service name matches indexes/service-index.md.
[ ] Service owner matches indexes/service-index.md.
[ ] Service category is defined.
[ ] MVP phase or wave is defined.
[ ] MVP depth is defined.
[ ] Purpose and Core responsibility are defined.
[ ] Inputs are defined.
[ ] Outputs are defined.
[ ] Objects read are listed or explicit no-read reason is provided.
[ ] Objects created or updated are listed or explicit no-mutation reason is provided.
[ ] Object links or unlinking are defined or explicitly not required.
[ ] Events emitted are listed or explicit no-event reason is provided.
[ ] Required contracts are listed.
[ ] Permission rules are defined.
[ ] Policy rules are defined or explicitly not required.
[ ] Review rules are defined or explicitly not required.
[ ] Audit rules are defined.
[ ] AI usage is defined or explicitly not required.
[ ] Workflow usage is defined or explicitly not required.
[ ] API exposure is defined.
[ ] Failure behavior is defined.
[ ] Idempotency and safety rules are defined.
[ ] Product consumers are classified.
[ ] MVP scope is defined.
[ ] Deferred scope is defined.
[ ] Codex implementation notes are included.
[ ] Prohibited overreach is defined.
```

---

# 29. Prohibited Overreach

This service spec must not be used to:

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

Add service-specific prohibited overreach:

```text
- ...
- ...
```

---

# 30. Acceptance Criteria

This Service Specification is accepted only if:

```text
[ ] It defines the service purpose.
[ ] It defines Core responsibility.
[ ] It identifies owning domain or system.
[ ] It identifies service category.
[ ] It defines scope.
[ ] It defines service boundary.
[ ] It defines inputs.
[ ] It defines outputs.
[ ] It defines objects read.
[ ] It defines objects created or updated.
[ ] It defines objects linked or unlinked.
[ ] It defines events emitted or explicit no-event reason.
[ ] It defines contracts required.
[ ] It defines permission rules.
[ ] It defines policy rules.
[ ] It defines review rules.
[ ] It defines audit rules.
[ ] It defines AI usage.
[ ] It defines workflow usage.
[ ] It defines API exposure.
[ ] It defines failure behavior.
[ ] It defines idempotency and safety.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial service specification created from B02-TPL-SERVICE. |

---

**End of Service Specification**
