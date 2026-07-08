# Domain Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/domains/`  
**Template ID:** B02-TPL-DOMAIN  
**Template Type:** Domain Specification Template  
**Source Chapter:** B02-CH-22 — Domain Specification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to:

```text
core-specs/domains/{domain-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
identity.md
trademark.md
workflow-contract.md
service-provider.md
```

This template is only for the 26 baseline Core Domains.

Do not use this template for:

```text
Capability
Business Responsibility
AI Governance
Codex Task System
Specification Governance
Product-specific modules
UI screens
database tables
```

Capability and Business Responsibility are cross-cutting Core specification systems and should be handled through `core-specs/cross-cutting/` or explicitly marked cross-cutting specs.

---

# Domain Specification — {Domain Name}

**Spec ID:** B02-DOM-{DOMAIN-ID}  
**Spec Type:** Domain  
**Domain Name:** {Domain Name}  
**Domain Category:** Foundation | Professional | Business Execution | Collaboration Network  
**Source Chapter:** B02-CH-22 — Domain Specification  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Source Index:** indexes/domain-index.md  
**Related Indexes:** indexes/object-index.md; indexes/service-index.md; indexes/event-index.md; indexes/api-index.md; indexes/agent-index.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Primary Consumers:** MarkReg | MarkOrbit Lite | Workplace | AI Agents | Codex Implementation | MGSN | Future Consumers  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this Core Domain exists.

The purpose should answer:

```text
What professional or architectural problem does this domain solve?
Why must this meaning be owned by Core rather than by a product?
Which later specs depend on this domain?
```

Example format:

```text
The {Domain Name} domain defines ...
It exists so that ...
It is required by ...
```

---

# 2. Core Meaning

Define the professional meaning owned by this domain.

This section should be short, precise and stable.

```text
{Domain Name} means ...
```

The definition must not be database-first, UI-first or implementation-first.

Avoid definitions such as:

```text
This domain stores ...
This domain manages screens for ...
This domain is a table for ...
```

Preferred definition pattern:

```text
This domain defines the shared Core meaning of ...
```

---

# 3. Domain Category

Select one canonical category.

```text
Foundation
Professional
Business Execution
Collaboration Network
```

Explain why the category is correct.

```text
This domain belongs to {Category} because ...
```

---

# 4. Scope

Define what is inside this domain.

Use concise bullets.

```text
This domain includes:
- ...
- ...
- ...
```

The scope should include only Core-level meaning.

It should not include product UI, data storage, pricing policy, full automation or future marketplace behavior unless explicitly approved.

---

# 5. Domain Boundary

Define the boundary of this domain.

## 5.1 In Boundary

```text
- ...
- ...
```

## 5.2 Out of Boundary

```text
- ...
- ...
```

## 5.3 Boundary Notes

Explain boundary-sensitive distinctions.

Examples:

```text
This domain owns ...
This domain references ...
This domain does not own ...
```

---

# 6. Owns

List what this domain owns.

```text
The {Domain Name} domain owns:
- Core meaning of ...
- Primary objects:
    - ...
- Primary services:
    - ...
- Primary events:
    - ...
- Primary contracts:
    - ...
```

Ownership means architectural responsibility, not implementation convenience.

---

# 7. Does Not Own

List what this domain explicitly does not own.

```text
The {Domain Name} domain does not own:
- product UI
- product-specific workflow experience
- database physical design
- unrelated business policy
- cross-cutting governance outside its scope
- ...
```

This section prevents overbuilding.

---

# 8. Primary Objects

List primary Core Objects owned by this domain.

Source:

```text
indexes/object-index.md
```

Use this format:

| Object | Object Category | MVP Depth | Notes |
|--------|-----------------|-----------|-------|
| {Object Name} | {Category} | {MVP Depth} | {Notes} |

Every object listed here should have a corresponding or planned Object Specification in:

```text
core-specs/objects/
```

Do not invent objects not present in `indexes/object-index.md` unless the index is updated through review.

---

# 9. Primary Services

List Core Services owned by or strongly associated with this domain.

Source:

```text
indexes/service-index.md
```

Use this format:

| Service | Service Category | MVP Depth | Objects Operated | Events Emitted |
|---------|------------------|-----------|------------------|----------------|
| {Service Name} | {Category} | {MVP Depth} | {Objects} | {Events} |

Every service listed here should have a corresponding or planned Service Specification in:

```text
core-specs/services/
```

A service that changes Core state must emit events or state an explicit no-event reason.

---

# 10. Primary Events

List Core Events emitted or consumed by this domain.

Source:

```text
indexes/event-index.md
```

Use this format:

| Event | Source Service | MVP Depth | Meaning |
|-------|----------------|-----------|---------|
| {Event Name} | {Service Name} | {MVP Depth} | {Meaning} |

Events must use canonical event naming rules.

```text
<Noun><PastTenseVerb>
<Noun><StateChanged>
<Noun><ReviewRequired>
<Noun><Approved>
<Noun><Rejected>
```

Do not treat logs, UI clicks or analytics pings as Core Events.

---

# 11. Primary Contracts

List contracts required by this domain.

Contract types may include:

```text
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

Detailed contract specs belong to:

```text
core-specs/contracts/
```

---

# 12. Relationships to Other Domains

Describe domain relationships.

Use this format:

| Related Domain | Relationship Type | Direction | Notes |
|----------------|-------------------|-----------|-------|
| {Domain} | owns / references / consumes / emits / validates / routes / reviews | inbound / outbound / bidirectional | {Notes} |

Relationship types may include:

```text
depends on
references
creates
updates
validates
routes to
emits events to
consumes events from
requires review from
uses knowledge from
```

This section should preserve domain boundaries.

---

# 13. AI Usage

Define allowed and prohibited AI usage for this domain.

## 13.1 Allowed AI Assistance

```text
AI may:
- ...
- ...
```

## 13.2 Prohibited AI Behavior

```text
AI must not:
- ...
- ...
```

## 13.3 Required AI Governance

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

If AI is not relevant to this domain, state:

```text
This domain does not require MVP AI usage.
```

AI must not replace professional responsibility.

---

# 14. Workflow Usage

Define how this domain participates in workflow execution.

Use this structure:

```text
Workflow role:
    none / source / participant / state owner / task owner / review owner / event source

Relevant Workflow Contracts:
    - ...

Relevant Tasks:
    - ...

Relevant State Transitions:
    - ...

Relevant Review Rules:
    - ...
```

If workflow is not relevant, state:

```text
This domain does not own workflow execution in MVP.
```

---

# 15. API Usage

Define how this domain may be consumed through APIs.

Use this structure:

```text
API exposure:
    No API / Internal API / Product API / Agent API / Integration API / Admin API

Related APIs:
    - ...

API rules:
    - API must reference service specs.
    - API must not define Core meaning.
    - Mutating APIs must map to events.
```

Detailed API specs belong to:

```text
core-specs/api/
```

---

# 16. Product Consumers

Classify product consumers.

## 16.1 MVP Consumers

```text
- MarkReg
- MarkOrbit Lite
- Workplace
- AI Agents
- Codex Implementation
```

## 16.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 16.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

Only list consumers that actually consume this domain.

Products may consume this domain but must not redefine domain meaning.

---

# 17. MVP Scope

Define MVP scope for this domain.

```text
MVP includes:
- ...
- ...
```

MVP scope must match `indexes/domain-index.md`.

## 17.1 MVP Phase

```text
Phase: {Phase}
```

## 17.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 17.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 18. Deferred Scope

Define what is explicitly deferred.

```text
Deferred:
- ...
- ...
```

Deferred scope must not be implemented by Codex unless a later approved task changes scope.

---

# 19. Data and Implementation Notes

Provide implementation-facing notes without defining physical schema.

Allowed notes:

```text
- canonical identifiers needed
- object ownership requirements
- required state labels
- source reference requirements
- validation expectations
- migration sensitivity
```

Prohibited notes:

```text
- physical database table design
- vendor-specific infrastructure design
- UI component design
- undocumented implementation shortcuts
```

---

# 20. Codex Implementation Notes

Define how Codex may implement this domain.

Codex must:

```text
- cite this domain spec
- cite indexes/domain-index.md
- cite related object, service and event indexes
- preserve MVP depth
- preserve deferred scope
- write tests
- follow prohibited-overreach rules
```

Codex must not:

```text
- invent new domains
- rename this domain
- merge this domain with another domain
- split this domain
- implement product UI
- implement deferred scope
- define database schema before object specs
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 21. Validation Rules

This Domain Specification must pass the following checks.

```text
[ ] Domain name matches indexes/domain-index.md.
[ ] Domain category matches indexes/domain-index.md.
[ ] MVP phase matches indexes/domain-index.md.
[ ] MVP depth matches indexes/domain-index.md.
[ ] Primary objects are listed.
[ ] Primary services are listed.
[ ] Primary events are listed.
[ ] Primary contracts are listed.
[ ] Product consumers are classified.
[ ] AI usage is defined or explicitly not required.
[ ] Workflow usage is defined or explicitly not required.
[ ] Deferred scope is defined.
[ ] Prohibited overreach is defined.
[ ] Codex implementation notes are included.
```

---

# 22. Prohibited Overreach

This domain spec must not be used to:

```text
change the 26-domain baseline
add a product as a domain
add a database table as a domain
add an AI Agent as a domain
promote Capability into an ordinary baseline domain
promote Business Responsibility into an ordinary baseline domain
invent unindexed objects
invent unindexed services
invent unindexed events
create APIs without contracts
create AI usage without Agent Contract
bypass human review for high-risk output
implement deferred scope
define product UI
define physical database schema
```

Add domain-specific prohibited overreach:

```text
- ...
- ...
```

---

# 23. Acceptance Criteria

This Domain Specification is accepted only if:

```text
[ ] It defines the domain purpose.
[ ] It defines Core meaning.
[ ] It identifies the correct domain category.
[ ] It defines scope and boundary.
[ ] It states what the domain owns.
[ ] It states what the domain does not own.
[ ] It lists primary objects.
[ ] It lists primary services.
[ ] It lists primary events.
[ ] It lists primary contracts.
[ ] It defines relationships to other domains.
[ ] It defines AI usage.
[ ] It defines workflow usage.
[ ] It defines API usage.
[ ] It classifies product consumers.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It includes Codex implementation notes.
[ ] It defines validation rules.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial domain specification created from B02-TPL-DOMAIN. |

---

**End of Domain Specification**
