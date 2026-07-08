# Book 02

# 31 — Codex Implementation Roadmap

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-31  
**Chapter Title:** Codex Implementation Roadmap  
**Part:** Part IV — Core Execution Boundary  
**Chapter Type:** Execution  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the Codex Implementation Roadmap for the MarkOrbit Core.

The previous chapters define what the Core is, where it sits, what it owns, what it excludes, how it is specified, how MVP scope is controlled and how the execution matrix should be read.

This chapter turns those architecture decisions into an implementation roadmap for Codex.

Codex is not the Core.

Codex is not the architecture owner.

Codex is an implementation actor that consumes approved specifications and produces repository structures, templates, tests, fixtures, validation logic and implementation code.

The purpose of this chapter is to ensure that Codex implements the Core in the right order, with the right scope, from the right sources, under the right acceptance criteria.

---

# 2. Core Question

This chapter answers one question:

> How should Codex implement the MarkOrbit Core without inventing architecture, expanding MVP scope or bypassing governance?

The answer is:

> Codex shall implement only approved specification artifacts, sequenced by the MVP Execution Matrix, controlled by appendices and indexes, organized into implementation waves, and accepted only through tests, fixtures, documentation and architecture review.

---

# 3. Roadmap Statement

The Codex Implementation Roadmap is governed by the following statement:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

This statement creates five roadmap constraints:

```text
1. Appendices before detailed core-specs.
2. Indexes before Codex tasks.
3. Specs before code.
4. Tests before acceptance.
5. Deferred scope remains deferred.
```

Codex may accelerate implementation.

Codex must not accelerate architectural drift.

---

# 4. Codex Position

Codex sits below specification and above implementation.

```text
Book 02 manuscript
        ↓
Appendices A–H
        ↓
indexes/
        ↓
core-specs/
        ↓
Codex task files
        ↓
Codex implementation
        ↓
tests / fixtures / validation
        ↓
accepted Core implementation
```

Codex may read earlier layers.

Codex may not redefine them.

If Codex identifies a missing concept, it must produce an implementation issue or architecture gap note, not silently create the architecture.

---

# 5. Codex Implementation Principles

Codex implementation must follow these principles.

```text
CIP1 — Source Specifications Required
CIP2 — Matrix Row Required
CIP3 — Scope Boundary Required
CIP4 — Tests Required
CIP5 — Fixtures Required Where Possible
CIP6 — AI Governance Required Before AI Implementation
CIP7 — Event Contracts Required Before Event Infrastructure
CIP8 — API Contracts Required Before API Exposure
CIP9 — Deferred Scope Must Stay Deferred
CIP10 — Acceptance Must Be Explicit
```

These principles apply to every Codex task.

---

# 6. Pre-Codex Gates

Codex implementation shall not start until the following gates are satisfied.

## 6.1 Appendix Gate

Appendices A–H must exist or the relevant appendix must be explicitly approved for the task.

```text
Appendix A — Glossary
Appendix B — Core Domain Index
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
```

## 6.2 Index Gate

The relevant index must exist before a task is generated.

Examples:

```text
Domain task requires Domain Index.
Object task requires Object Index.
Service task requires Service Index.
Event task requires Event Index.
API task requires API Index.
Agent task requires Agent Index.
Codex task sequencing requires Codex Task Index.
```

## 6.3 core-specs Gate

A task that implements code must reference a detailed `core-specs/` file or a formally approved scaffold template.

## 6.4 Test Gate

Each task must define tests before it is accepted.

## 6.5 Scope Gate

Each task must state:

```text
in scope
out of scope
deferred scope
prohibited overreach
```

---

# 7. Codex Waves

Book 02 defines eight Codex implementation waves.

```text
Wave 0 — Repository and Spec Scaffold
Wave 1 — Foundation Core
Wave 2 — Professional Core
Wave 3 — Business Execution Core
Wave 4 — AI Governance and Review
Wave 5 — Product Consumption Baseline
Wave 6 — Growth Core Baseline
Wave 7 — Validation, Hardening and Release
```

The waves are ordered by execution dependency, not by product attractiveness.

Codex must not skip ahead to later waves unless earlier gates are explicitly satisfied.

---

# 8. Wave 0 — Repository and Spec Scaffold

## 8.1 Purpose

Wave 0 creates the repository skeleton, templates, indexes and validation baseline required before implementation.

## 8.2 Required Outputs

```text
README.md update
publication.yaml update
CHANGELOG.md update
appendices/ folder
indexes/ folder
core-specs/ folder
codex-tasks/ folder
core-specs templates
Codex task template
validation script baseline
fixture directory baseline
release directory baseline
```

## 8.3 Required Folders

```text
book-02-core/
├── appendices/
├── indexes/
├── core-specs/
│   ├── domains/
│   ├── objects/
│   ├── services/
│   ├── events/
│   ├── contracts/
│   ├── api/
│   ├── agents/
│   └── workflows/
├── codex-tasks/
│   ├── wave-0/
│   ├── wave-1/
│   ├── wave-2/
│   ├── wave-3/
│   ├── wave-4/
│   ├── wave-5/
│   ├── wave-6/
│   └── wave-7/
├── assets/
└── releases/
```

## 8.4 Wave 0 Acceptance Criteria

```text
[ ] Repository structure exists.
[ ] README reflects repository structure.
[ ] publication.yaml references all canonical directories.
[ ] Planning file names are normalized.
[ ] Appendices are present or scheduled.
[ ] Index scaffold exists.
[ ] core-specs templates exist.
[ ] Codex task template exists.
[ ] No detailed implementation code is generated prematurely.
```

---

# 9. Wave 1 — Foundation Core

## 9.1 Purpose

Wave 1 implements the minimum foundation required for all other Core execution.

## 9.2 Domains and Systems

```text
Identity
Organization
User
Permission
Knowledge
Policy baseline
Capability baseline
```

Capability is a cross-cutting system, not an additional baseline Core Domain.

## 9.3 Required Specs

```text
core-specs/domains/identity.md
core-specs/domains/organization.md
core-specs/domains/user.md
core-specs/domains/permission.md
core-specs/domains/knowledge.md
core-specs/domains/policy.md
core-specs/objects/* foundation objects
core-specs/services/* foundation services
core-specs/events/* foundation events
core-specs/contracts/* foundation contracts
```

## 9.4 Implementation Focus

```text
actor identity
organization ownership
user model
permission baseline
knowledge source model
knowledge asset model
knowledge retrieval baseline
policy placeholder
capability baseline
```

## 9.5 Wave 1 Acceptance Criteria

```text
[ ] Identity and User objects are defined.
[ ] Organization relationships are defined.
[ ] Permission baseline exists.
[ ] Knowledge Source and Knowledge Asset specs exist.
[ ] Capability baseline is classified as cross-cutting.
[ ] No product-specific user model overrides Core Identity.
[ ] Tests cover identity, permission and knowledge access boundaries.
```

---

# 10. Wave 2 — Professional Core

## 10.1 Purpose

Wave 2 implements the professional trademark and brand foundation.

## 10.2 Domains

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence baseline
```

## 10.3 Implementation Focus

```text
Brand Object
Trademark Object
Jurisdiction Object
Classification Term / Class Recommendation baseline
Document Object
Document Requirement baseline
Evidence placeholder / baseline
jurisdiction requirement retrieval
classification recommendation contract
trademark status normalization baseline
```

## 10.4 Required AI Constraints

AI may assist classification, jurisdiction requirement retrieval and document drafting only if Agent Contracts exist.

If Agent Contracts are not yet complete, AI implementation remains stubbed or disabled.

## 10.5 Wave 2 Acceptance Criteria

```text
[ ] Brand, Trademark, Jurisdiction, Classification and Document specs exist.
[ ] Evidence is explicitly Partial Implement or Reserved where needed.
[ ] Classification recommendation is contract-bound.
[ ] Document requirements are linked to Jurisdiction and Knowledge.
[ ] No trademark office connector becomes Core meaning.
[ ] Tests cover jurisdiction/classification/document boundaries.
```

---

# 11. Wave 3 — Business Execution Core

## 11.1 Purpose

Wave 3 turns professional objects into executable work.

## 11.2 Domains and Systems

```text
Customer
Order
Matter
Workflow Contract
Task
Event
Notification baseline
Business Responsibility baseline
```

Business Responsibility is a cross-cutting system, not an additional baseline Core Domain.

## 11.3 Implementation Focus

```text
Customer Object
Order Object
Matter Object
Task Object
Workflow Contract baseline
Event baseline
Notification baseline
Responsibility Assignment baseline
Order-to-Matter conversion
Task assignment
Review requirement
Matter lifecycle
```

## 11.4 Critical Rule

Order, Matter, Task, Event and Workflow Contract must not be hidden inside product UI.

They must be Core-specified.

## 11.5 Wave 3 Acceptance Criteria

```text
[ ] Customer, Order, Matter, Task and Event specs exist.
[ ] Workflow Contract baseline exists.
[ ] Responsibility Assignment baseline exists.
[ ] Order-to-Matter conversion emits events.
[ ] Task assignment emits events.
[ ] Notification baseline is partial and controlled.
[ ] Tests cover order/matter/task/event execution flow.
```

---

# 12. Wave 4 — AI Governance and Review

## 12.1 Purpose

Wave 4 implements governed AI capability infrastructure.

AI must not be implemented as prompt-only behavior.

## 12.2 Required Specs

```text
AI Agent Identity
Agent Contract
AI Capability
AI Output
AI Recommendation
AI Audit Record
Review Record
Risk Level
Human Review Rule
AI Events
```

## 12.3 MVP Agents

MVP AI agents may include:

```text
Classification Assistant Agent
Document Draft Assistant Agent
Trademark Status Summary Agent
Evidence Review Assistant Agent
Communication Summary Agent
Routing Assistant Agent
Workflow Assistant Agent
Codex Implementation Agent
Spec Consistency Review Agent
```

Each agent must have an Agent Contract.

## 12.4 Wave 4 Acceptance Criteria

```text
[ ] Agent Contract template exists.
[ ] AI Agent objects are indexed.
[ ] AI Output and AI Audit Record are indexed.
[ ] Risk levels and review requirements are defined.
[ ] AI events are defined.
[ ] No AI agent can mutate Core state without service and audit rules.
[ ] Tests cover Agent Contract enforcement.
```

---

# 13. Wave 5 — Product Consumption Baseline

## 13.1 Purpose

Wave 5 defines how first products and Workplaces consume Core.

## 13.2 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## 13.3 Required Contracts

```text
MarkReg Core Consumption Contract
Lite Core Consumption Contract
Workplace Core Consumption Contract
AI Agent Consumption Contract
Codex Task Contract
API Contract baseline
Event Subscription Contract baseline
```

## 13.4 Implementation Focus

```text
read/write boundaries
API exposure baseline
event subscription baseline
product-specific prohibited redefinitions
consumer permission boundaries
workflow consumption boundary
AI consumption boundary
```

## 13.5 Wave 5 Acceptance Criteria

```text
[ ] Core Consumption Contracts exist for MVP consumers.
[ ] API baseline is contract-bound.
[ ] Product consumers cannot redefine Core objects.
[ ] Workplace cannot redefine Task, Event or Workflow Contract.
[ ] Codex task contract is enforced.
[ ] Tests cover product consumption boundaries.
```

---

# 14. Wave 6 — Growth Core Baseline

## 14.1 Purpose

Wave 6 prepares future growth without overbuilding the MVP.

## 14.2 Partial and Reserved Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
Partner Center future
Client Portal future
Service Platform future
External Integrations future
Reporting Consumers future
```

## 14.3 Domains

```text
Opportunity
Communication
Agent
Service Provider
Routing
Partner reserved
Service Network reserved
```

## 14.4 Implementation Focus

```text
Opportunity baseline
Communication baseline
Agent baseline
Service Provider baseline
Routing baseline
Partner reserved boundary
Service Network reserved boundary
External integration contract placeholder
Reporting contract placeholder
```

## 14.5 Wave 6 Acceptance Criteria

```text
[ ] Opportunity baseline does not become full scoring engine.
[ ] Routing baseline is governed by Capability and Responsibility.
[ ] Agent and Service Provider baseline are defined.
[ ] Partner and Service Network remain reserved unless approved.
[ ] External integrations remain contract placeholders unless approved.
[ ] Tests protect deferred scope.
```

---

# 15. Wave 7 — Validation, Hardening and Release

## 15.1 Purpose

Wave 7 validates that the Core MVP is consistent, testable and release-ready.

## 15.2 Validation Areas

```text
repository structure
publication metadata
appendix completeness
index completeness
core-specs completeness
Codex task traceability
domain/object/service/event consistency
contract coverage
AI governance coverage
MVP/deferred-scope enforcement
test coverage
fixture coverage
release notes
```

## 15.3 Required Outputs

```text
validation report
acceptance report
release notes
known limitations
open architecture issues
deferred scope register
Codex task completion report
```

## 15.4 Wave 7 Acceptance Criteria

```text
[ ] Every implemented item traces to a source spec.
[ ] Every Codex task has tests.
[ ] Every MVP object has an owner.
[ ] Every MVP service declares events and contracts.
[ ] Every AI agent has an Agent Contract.
[ ] Every event has source ownership.
[ ] Deferred scope remains unimplemented.
[ ] Release notes are complete.
```

---

# 16. Codex Task Template

Every Codex task must use a standard template.

```text
# Codex Task

1. Task ID
2. Wave
3. Task Package
4. Source Documents
5. Source Specs
6. Execution Matrix Row
7. Purpose
8. In Scope
9. Out of Scope
10. Deferred Scope
11. Required Inputs
12. Expected Outputs
13. Files to Create or Update
14. Objects Involved
15. Services Involved
16. Events Involved
17. Contracts Required
18. AI Usage
19. Permission / Policy Requirements
20. Tests Required
21. Fixtures Required
22. Validation Command
23. Acceptance Criteria
24. Prohibited Overreach
25. Revision Notes
```

Tasks without source specs, scope and acceptance criteria are invalid.

---

# 17. Codex Task Packages

Codex tasks should be grouped into packages.

```text
Package A — Repository Scaffold
Package B — Foundation Core
Package C — Professional Core
Package D — Business Execution Core
Package E — AI Governance and Review
Package F — Product Consumption Baseline
Package G — Growth Core Baseline
Package H — Validation and Release
```

Each package may contain tasks across one or more waves, but the wave order remains authoritative.

---

# 18. Matrix-to-Codex Rule

The MVP Execution Matrix is the primary task source.

A Codex task must map to at least one matrix row.

```text
Matrix Row
    ↓
Required Specs
    ↓
Codex Task
    ↓
Expected Files
    ↓
Tests
    ↓
Acceptance Criteria
```

If a task does not map to a matrix row, it must be treated as an architecture issue or future-scope request.

---

# 19. Codex Prohibited Overreach

Codex must not:

```text
create new baseline Core Domains
change the 26-domain baseline
convert Capability or Business Responsibility into ordinary domains without approval
create product UI scope inside Core specs
implement full MGSN marketplace early
implement full Opportunity Engine scoring early
implement full Brand Asset Vault early
create prompt-only AI agents
allow AI to mutate Core state without services and audit
create events as logs or analytics pings
expose APIs without API Contracts
write database schemas as Core meaning
skip appendices or indexes
skip tests
```

Any of these actions should fail review.

---

# 20. Testing Strategy

Codex implementation requires tests at multiple levels.

```text
structure tests
metadata tests
schema/spec tests
object lifecycle tests
service behavior tests
event emission tests
contract validation tests
permission tests
AI governance tests
workflow transition tests
consumer boundary tests
deferred-scope tests
```

Tests must not be treated as optional.

A task without tests cannot be accepted.

---

# 21. Fixture Strategy

Fixtures should be used to validate Core behavior without connecting production systems too early.

Fixture categories:

```text
identity fixtures
knowledge fixtures
jurisdiction fixtures
classification fixtures
trademark fixtures
document fixtures
customer/order/matter fixtures
task/event fixtures
AI output fixtures
agent/routing fixtures
consumer contract fixtures
```

Fixture-only workflows may exist before production connectors.

Production connectors should remain disabled until contracts, permissions, events and tests are complete.

---

# 22. Validation Strategy

Validation should confirm:

```text
files exist in expected paths
metadata is valid
chapter and spec IDs are consistent
appendix references resolve
index entries match specs
spec ownership is declared
objects have domains or cross-cutting systems
services declare inputs, outputs, events and contracts
events declare source domains and payload contracts
agents have Agent Contracts
Codex tasks reference matrix rows
MVP/deferred boundaries are enforced
```

Validation should run before release.

---

# 23. Release Strategy

Codex implementation should produce release stages.

```text
Stage 1 — Scaffold Release
Stage 2 — Foundation Core Release
Stage 3 — Professional Core Release
Stage 4 — Execution Core Release
Stage 5 — AI Governance Release
Stage 6 — Product Consumption Baseline Release
Stage 7 — MVP Core Release Candidate
```

Each release stage must include:

```text
release notes
implemented scope
deferred scope
known limitations
test summary
validation summary
open issues
```

---

# 24. Codex Review Process

Every Codex output must be reviewed.

Review questions:

```text
Does the output trace to approved specs?
Does it preserve Core boundaries?
Does it preserve the 26-domain baseline?
Does it respect cross-cutting system classification?
Does it include tests?
Does it avoid deferred scope?
Does it enforce AI governance where needed?
Does it avoid product-first architecture?
Does it avoid database-first architecture?
Does it avoid prompt-first AI?
```

Outputs that fail these questions should be revised before acceptance.

---

# 25. Relationship to Appendix H

Appendix H — Codex Task Index is the direct bridge from this chapter to implementation.

Appendix H must include:

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

This chapter defines the roadmap.

Appendix H defines the task index.

Codex task files define implementation units.

---

# 26. Relationship to core-specs/

`core-specs/` is the direct source for implementation tasks.

Codex tasks must reference `core-specs/` files where available.

Expected `core-specs/` areas:

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

If a required spec does not exist, Codex should generate a spec-scaffold task before generating implementation code.

---

# 27. Execution Mapping

| Roadmap Layer | Codex Output |
|--------------|--------------|
| Appendices | Canonical indexes and glossary references |
| Indexes | Machine-readable or reviewable source lists |
| core-specs/ | Detailed executable specs |
| Execution Matrix | Task sequencing and MVP depth |
| Codex Task Index | Task registry |
| Codex Task Files | Unit implementation instructions |
| Tests | Acceptance evidence |
| Fixtures | Safe validation data |
| Release Notes | Release documentation |

---

# 28. Exclusions

This chapter does not define:

```text
actual implementation code
final database schema
production API routes
product UI tasks
commercial pricing tasks
full deployment pipeline
full external connector implementation
production AI prompts
full marketplace implementation
```

Those belong to later implementation repositories, product books or operational documents.

---

# 29. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It positions Codex as implementation actor, not architecture owner.
[ ] It defines pre-Codex gates.
[ ] It defines Wave 0 through Wave 7.
[ ] It links Codex tasks to the MVP Execution Matrix.
[ ] It requires appendices before core-specs.
[ ] It requires indexes before Codex tasks.
[ ] It defines a Codex task template.
[ ] It defines prohibited overreach.
[ ] It protects the 26-domain baseline.
[ ] It protects Capability and Business Responsibility cross-cutting status.
[ ] It protects AI governance.
[ ] It protects MVP/deferred scope.
[ ] It defines testing and fixture strategy.
[ ] It defines validation and release strategy.
[ ] It prepares Appendix H.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 30. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 31, defining Codex implementation waves. |
| 0.2.0 | Draft | Second canonical draft rewrite. Strengthened Codex position, pre-Codex gates, Wave 0–7 roadmap, task template, matrix-to-Codex rule, testing/fixture strategy, validation/release strategy and prohibited-overreach controls. |

---

**End of Chapter**
