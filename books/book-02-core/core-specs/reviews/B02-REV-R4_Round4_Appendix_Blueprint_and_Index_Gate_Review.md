# B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review

**Book:** Book 02 — MarkOrbit Core Specification  
**Repository:** `book-02-core`  
**Review ID:** B02-REV-R4  
**Review Round:** Round 4  
**Review Type:** Appendix Blueprint / Canonical Index Gate Review  
**Source Package Reviewed:** `book 2.zip` and Round 1–3 review results  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Review Purpose

Round 4 is the final review before generating appendices.

Round 1 confirmed manuscript architecture.

Round 2 confirmed packaged manuscript completeness and repository structure issues.

Round 3 approved the manuscript for appendices but held `core-specs/` and Codex tasks.

Round 4 now defines the exact appendix and index blueprint.

The review question is:

> What must be fixed, clarified and frozen before Appendix A–H are generated?

Round 4 is not another broad manuscript review.

It is a canonicalization review.

Its job is to prevent the appendices from copying unresolved ambiguity into the executable specification system.

---

# 2. Round 4 Decision

Round 4 decision:

```text
APPROVED TO GENERATE APPENDICES A–H
WITH CANONICAL CLARIFICATIONS REQUIRED
```

Do not generate `core-specs/` yet.

Do not generate Codex tasks yet.

Appendices must be generated first.

---

# 3. Current State

The organized Book 2 package has already passed the following gates:

```text
Manuscript completeness: PASS
Architecture coherence: PASS
Chapter path consistency: PASS
Chapter ID consistency: PASS
Publication metadata baseline: PASS WITH FIXES
Repository scaffold readiness: PARTIAL
Appendix readiness: READY
core-specs readiness: HOLD
Codex readiness: HOLD
```

Book 02 is now in this state:

```text
Draft complete
Architecture accepted
Appendix-ready
Not yet implementation-ready
```

---

# 4. Round 4 Review Scope

Round 4 reviews:

```text
Appendix generation order
canonical terminology
domain index rules
object index rules
service index rules
event naming/index rules
API index rules
agent index rules
Codex task index rules
repository structure fixes
cross-cutting specification placement
consumer classification
status vocabulary
```

Round 4 does not rewrite chapters 00–31.

Round 4 does not generate implementation code.

Round 4 does not scaffold full `core-specs/`.

---

# 5. Canonical Decisions Required Before Appendices

Round 4 identifies seven canonical decisions.

```text
D1 — Preserve 26 baseline Core Domains.
D2 — Treat Capability and Business Responsibility as cross-cutting specification systems.
D3 — Add appendices/ before any index or core-specs work.
D4 — Make API an explicit index/spec surface even without a standalone chapter.
D5 — Index AI Agent / AI Output / AI Audit as first-class execution concepts.
D6 — Classify consumers as MVP / Partial / Future.
D7 — Separate publication, chapter, spec, task and implementation statuses.
```

These decisions should be reflected in Appendix A and Appendix B first.

---

# 6. D1 — Preserve 26 Baseline Core Domains

## Decision

The baseline Core Domain Map remains 26 domains.

Canonical baseline:

```text
Foundation Domains
    Identity
    Organization
    User
    Permission
    Policy
    Knowledge

Professional Domains
    Brand
    Trademark
    Jurisdiction
    Classification
    Document
    Evidence

Business Execution Domains
    Customer
    Matter
    Order
    Opportunity
    Workflow Contract
    Task
    Event
    Notification

Collaboration Network Domains
    Partner
    Agent
    Service Provider
    Service Network
    Routing
    Communication
```

## Rationale

The 26-domain map is already stable across the book and planning documents.

Changing the baseline domain count now would create unnecessary architecture churn.

## Appendix Requirement

Appendix B must state:

```text
The canonical baseline Core Domain Map contains 26 domains.
```

---

# 7. D2 — Capability and Business Responsibility Are Cross-Cutting Systems

## Problem

Capability and Business Responsibility appear in multiple roles:

```text
Canonical Models
Specification chapters
MVP priority items
Execution matrix rows
Possible future implementation specs
```

They are important, but they should not silently change the 26-domain baseline.

## Decision

Capability and Business Responsibility shall be treated as:

```text
Cross-Cutting Core Specification Systems
```

They may produce objects, services, contracts, events and implementation specs.

But they do not change the 26 baseline domain count.

## Recommended wording

Appendix A and B should include this note:

```text
Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

## Repository implication

Do not place them casually as normal domain files without explanation.

Preferred future scaffold options:

```text
Option A:
    core-specs/cross-cutting/capability.md
    core-specs/cross-cutting/business-responsibility.md

Option B:
    core-specs/capabilities/
    core-specs/responsibilities/

Option C:
    keep related executable artifacts under objects/, services/, contracts/, events/
    and explain their cross-cutting status in indexes
```

## Round 4 recommendation

Use Option C for MVP to minimize structural change.

Appendix B should list them under:

```text
Cross-Cutting Specification Systems
    Capability
    Business Responsibility
```

not under the 26-domain baseline.

---

# 8. D3 — Add appendices/ Before Index or core-specs Work

## Decision

The repository must include:

```text
appendices/
```

before Appendix A is generated.

## Required files

```text
appendices/B02-APP-A_Glossary.md
appendices/B02-APP-B_Core_Domain_Index.md
appendices/B02-APP-C_Core_Object_Index.md
appendices/B02-APP-D_Core_Service_Index.md
appendices/B02-APP-E_Event_Index.md
appendices/B02-APP-F_API_Index.md
appendices/B02-APP-G_Agent_Index.md
appendices/B02-APP-H_Codex_Task_Index.md
```

## README update

README repository tree must include:

```text
book-02-core/
├── appendices/
```

## publication.yaml update

`publication.yaml` should include a directory mapping:

```yaml
appendices: book-02-core/appendices/
```

---

# 9. D4 — API Requires Explicit Index and Template

## Problem

Book 02 handles API mainly through contracts and `core-specs/api/`, but there is no standalone API chapter.

This is acceptable only if Appendix F and API templates make the API surface explicit.

## Decision

Appendix F — API Index is mandatory before `core-specs/api/` scaffold.

## Appendix F must define:

```text
API Index purpose
API naming rules
API contract relationship
MVP API surfaces
Deferred API surfaces
API template expectations
API consumer boundaries
```

## MVP API surfaces should include:

```text
Identity API
Knowledge Retrieval API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Customer API
Order API
Matter API
Task API
Event API
AI Invocation API
Core Consumption API baseline
```

## Future API surfaces should include:

```text
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
```

---

# 10. D5 — AI Agent / AI Output / AI Audit Must Be Indexed

## Decision

AI execution concepts must be indexed as first-class Core execution concepts.

They should not be left as prompt or implementation details.

Appendix C should include object entries such as:

```text
AI Agent
AI Capability
AI Output
AI Recommendation
AI Audit Record
Agent Contract
Review Record
```

Appendix G should include agent entries such as:

```text
AI Governance
Classification Assistant Agent
Document Draft Assistant Agent
Evidence Review Assistant Agent
Trademark Status Summary Agent
Office Action Assistant
Communication Summary Agent
Opportunity Discovery Agent
Routing Assistant Agent
Workflow Assistant Agent
Codex Implementation Agent
Spec Consistency Review Agent
```

AI index entries must include:

```text
Agent identity
Allowed capabilities
Prohibited capabilities
Knowledge access
Object access
Risk level
Review rules
Events
Audit
Product consumers
```

---

# 11. D6 — Consumer Classification Is Required

## Decision

All Core consumers must be classified.

Canonical classification:

```text
MVP Consumers
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
    Codex Implementation

Partial Consumers
    MGSN
    Opportunity Engine baseline
    Brand Asset Vault baseline

Future Consumers
    Partner Center
    Client Portal
    Service Platform
    External Integrations
    Reporting Consumers
```

## Rationale

Without this classification, future product names may pull MVP implementation too far forward.

## Appendix requirement

Appendix A should define consumer status vocabulary.

Appendix H should reference consumer classification when generating Codex tasks.

---

# 12. D7 — Status Vocabulary Must Be Separated

## Decision

Status values should be separated by layer.

## Publication Status

```text
draft
canonical_draft
reviewing
approved
released
deprecated
superseded
archived
```

## Chapter Status

```text
Draft
Reviewing
Approved
Revised
Deprecated
Superseded
Archived
```

## Spec Status

```text
Draft
Reviewing
Approved
Deprecated
Superseded
Archived
```

## Codex Task Status

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

## Implementation Status

```text
Not Started
Planned
In Progress
Implemented
Tested
Accepted
Deferred
Blocked
Deprecated
```

## Appendix requirement

Appendix A should include these status definitions.

---

# 13. Appendix Generation Blueprint

Round 4 approves the following appendix blueprint.

---

## Appendix A — Glossary

### Purpose

Define canonical terminology used across Book 02.

### Must include

```text
Core
Kernel
Canonical Model
Domain
Object
Service
Event
Contract
Consumption
Capability
Business Responsibility
Knowledge
Identity
Policy
Permission
Workflow Contract
Task
State
Context
AI Capability
AI Agent
Agent Contract
AI Output
AI Audit
Product Consumer
Workplace Consumer
Codex Implementation Consumer
MVP Depth
Reserved Boundary
Deferred
Codex Wave
Spec Status
Task Status
```

### Special notes required

```text
26 baseline Core Domains remain canonical.
Capability and Business Responsibility are cross-cutting systems.
AI is governed capability, not Core authority.
Codex is implementation actor, not architecture owner.
```

---

## Appendix B — Core Domain Index

### Purpose

List all baseline Core Domains and their MVP phase/depth.

### Must include

```text
26-domain baseline
domain categories
owning canonical model
MVP phase
MVP depth
primary objects
primary services
primary events
product consumers
AI usage
deferred scope
```

### Must not do

```text
Do not add Capability or Business Responsibility as ordinary baseline domains.
Do not change domain count without release decision.
```

---

## Appendix C — Core Object Index

### Purpose

List Core Objects and their owning domains or cross-cutting systems.

### Must include object categories

```text
Identity Objects
Professional Objects
Business Execution Objects
Execution Primitive Objects
Collaboration Network Objects
Contract / Governance Objects
AI Governance Objects
```

### Required AI / Governance objects

```text
AI Agent
AI Output
AI Recommendation
AI Audit Record
Agent Contract
Review Record
Responsibility Assignment
Capability
Capability Provider
Policy Rule
Permission Rule
```

---

## Appendix D — Core Service Index

### Purpose

List MVP and future Core Services by owning domain or cross-cutting system.

### Must include

```text
service name
owning domain
service category
objects read
objects created/updated
events emitted
contracts required
AI usage
MVP phase
MVP depth
product consumers
```

---

## Appendix E — Event Index

### Purpose

List Core Events and their source domain.

### Must include

```text
event name
event file name
source domain
event type
trigger
related objects
payload contract
downstream consumers
AI usage
audit requirement
MVP phase
```

### Naming rule

Use semantic event names and lowercase kebab-case filenames.

Example:

```text
Event Name: MatterCreated
File Name: matter-created.md
```

---

## Appendix F — API Index

### Purpose

Define API surfaces and their relation to contracts.

### Must include

```text
API name
owning domain/service
consumer
input contract
output contract
permission requirement
event side effects
MVP status
future status
```

---

## Appendix G — Agent Index

### Purpose

List AI agents and governance rules.

### Must include

```text
agent name
agent identity
agent contract
allowed capabilities
prohibited capabilities
authorized knowledge
allowed object access
risk level
human review
events
audit
product consumers
MVP status
```

---

## Appendix H — Codex Task Index

### Purpose

Map Codex tasks to roadmap waves and execution matrix rows.

### Must include

```text
task ID
wave
package
matrix row
source specs
dependencies
expected outputs
tests required
acceptance criteria
prohibited overreach
status
```

---

# 14. Repository Fix Blueprint

Before or during Appendix A generation, apply these repository fixes.

## Fix R4-F1 — Add appendices directory

```text
book-02-core/appendices/
```

## Fix R4-F2 — Update README tree

Add:

```text
├── appendices/
```

## Fix R4-F3 — Update publication.yaml directory mapping

Add:

```yaml
appendices: book-02-core/appendices/
```

## Fix R4-F4 — Normalize B02-PLN-0003 file name/reference

Preferred file:

```text
planning/B02-PLN-0003_Core_Domain_Map_v1.0.md
```

## Fix R4-F5 — Add status vocabulary to README or Appendix A

Do not overload one status field.

---

# 15. Pre-core-specs Hold

Round 4 explicitly holds `core-specs/` generation.

Reason:

```text
Appendices have not yet created canonical index lists.
```

Do not generate:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
```

until Appendix A–H are complete.

A structural empty scaffold may be created only after appendices begin, but detailed specs should wait.

---

# 16. Pre-Codex Hold

Round 4 explicitly holds Codex implementation tasks.

Reason:

```text
Codex tasks require Appendix H and indexes/codex-task-index.md.
```

Do not generate:

```text
codex-tasks/wave-0/
```

until:

```text
Appendix H is complete
indexes/ scaffold exists
Codex task template is approved
```

---

# 17. Round 4 Risk Assessment

## Risk R4-001 — Appendix A Too Shallow

If Glossary is too short, later indexes will inherit ambiguity.

Mitigation:

```text
Make Appendix A a real canonical glossary, not a short word list.
```

## Risk R4-002 — Domain Count Drift

If Capability and Business Responsibility are indexed as ordinary domains, the 26-domain baseline will become unstable.

Mitigation:

```text
Classify them as cross-cutting systems.
```

## Risk R4-003 — API Surface Omission

If API Index is weak, Codex may implement services without stable API contracts.

Mitigation:

```text
Make Appendix F mandatory and explicit.
```

## Risk R4-004 — AI Governance Omission

If AI objects are not indexed, AI may become prompt-only implementation.

Mitigation:

```text
Index AI Agent, AI Output, AI Audit and Agent Contract.
```

## Risk R4-005 — Product Overbuild

If consumers are not classified, future products may enter MVP too early.

Mitigation:

```text
Tag MVP / Partial / Future consumers.
```

---

# 18. Round 4 Acceptance Checklist

Round 4 can be closed when:

```text
[ ] Appendix A blueprint is accepted.
[ ] Appendix B blueprint is accepted.
[ ] Appendix C blueprint is accepted.
[ ] Appendix D blueprint is accepted.
[ ] Appendix E blueprint is accepted.
[ ] Appendix F blueprint is accepted.
[ ] Appendix G blueprint is accepted.
[ ] Appendix H blueprint is accepted.
[ ] 26-domain baseline is frozen.
[ ] Capability / Business Responsibility cross-cutting rule is accepted.
[ ] API Index requirement is accepted.
[ ] AI indexing requirement is accepted.
[ ] Consumer classification is accepted.
[ ] appendices/ directory is created or scheduled.
[ ] README tree update is created or scheduled.
[ ] publication.yaml mapping update is created or scheduled.
[ ] core-specs/ remains on hold.
[ ] Codex tasks remain on hold.
```

---

# 19. Round 4 Final Decision

Round 4 final decision:

```text
APPENDIX GENERATION MAY START.
APPENDIX A — GLOSSARY MUST BE FIRST.
CORE-SPECS GENERATION REMAINS ON HOLD.
CODEX TASK GENERATION REMAINS ON HOLD.
```

---

# 20. Immediate Next Action

Generate:

```text
book-02-core/appendices/B02-APP-A_Glossary.md
```

Appendix A should include all canonical terms and the cross-cutting clarification for Capability and Business Responsibility.

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Round 4 appendix blueprint and canonical index gate review. |

---

**End of Review**
