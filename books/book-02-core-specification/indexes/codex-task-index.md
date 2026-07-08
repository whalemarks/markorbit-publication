# Codex Task Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-CODEX-TASK  
**Source Appendix:** B02-APP-H — Codex Task Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index; B02-APP-E — Event Index; B02-APP-F — API Index; B02-APP-G — Agent Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-H — Codex Task Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready Codex task index used by:

```text
codex-tasks/
core-specs/
validation scripts
release checks
implementation planning
Codex execution prompts
```

This index does not implement MarkOrbit Core.

It defines which Codex tasks may be generated, in what order, from which source specifications, with what dependencies, what prohibited overreach rules, and what acceptance criteria.

---

# 2. Canonical Codex Rule

Book 02 uses the following canonical rule:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

Therefore:

```text
No source specification, no Codex task.
No acceptance criteria, no implementation.
No prohibited-overreach rules, no safe Codex execution.
No tests, no acceptance.
No approved index or core-spec, no production implementation.
```

---

# 3. Codex Task Definition

A Codex Task is a controlled implementation instruction that tells Codex what to create, modify, validate or test based on approved Core specifications.

A Codex Task is not:

```text
a product idea
a vague prompt
a feature wish
a UI request
an architecture decision
a shortcut around core-specs/
a permission to expand MVP scope
```

A Codex Task must be:

```text
source-bound
scope-bound
testable
reviewable
traceable
implementation-safe
```

---

# 4. Codex Task ID Format

Codex task IDs use the following format:

```text
B02-CX-W{wave}-{sequence}
```

Examples:

```text
B02-CX-W0-001
B02-CX-W1-004
B02-CX-W3-012
B02-CX-W7-003
```

Where:

```text
B02
    Book 02

CX
    Codex Task

W{wave}
    Codex implementation wave

{sequence}
    three-digit sequence number inside the wave
```

---

# 5. Codex Task Status Vocabulary

Codex tasks use the following status values.

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

Only `Ready` tasks may be implemented.

Only `Tested` tasks may be reviewed for acceptance.

Only `Accepted` tasks may be treated as complete.

---

# 6. Codex Task Index Fields

Each task entry should include the following fields.

```text
Task ID
Task Title
Wave
Task Package
Status
Source Specifications
Related Appendix Entries
Related Index Entries
Related core-specs Files
Dependencies
Objective
In Scope
Out of Scope
Expected Outputs
Objects Affected
Services Affected
Events Affected
Contracts Affected
API Surfaces Affected
AI Agents Affected
Workflow Usage
Product Consumers
MVP Depth
Implementation Instructions
Test Requirements
Fixture Requirements
Validation Requirements
Prohibited Overreach
Acceptance Criteria
Review Notes
Revision Notes
```

---

# 7. Codex Wave Structure

Book 02 defines eight Codex waves.

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

The waves follow the dependency structure defined by:

```text
domain-index.md
object-index.md
service-index.md
event-index.md
api-index.md
agent-index.md
```

---

# 8. Wave 0 — Repository and Spec Scaffold

## Purpose

Create the repository, index, specification and task scaffold required before detailed implementation begins.

Wave 0 does not implement business functionality.

## Wave 0 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W0-001 | Create Repository Scaffold | Repository Scaffold | Draft | README.md, publication.yaml, B02-APP-H |
| B02-CX-W0-002 | Create indexes/ Scaffold | Index Scaffold | Draft | Appendices A–H, indexes/README.md |
| B02-CX-W0-003 | Create core-specs/ Scaffold | Spec Scaffold | Draft | Chapters 22–27, indexes/* |
| B02-CX-W0-004 | Create codex-tasks/ Scaffold | Task Scaffold | Draft | B02-APP-H, codex-task-index.md |
| B02-CX-W0-005 | Create Spec Templates | Template Scaffold | Draft | Chapters 22–27 |
| B02-CX-W0-006 | Create Codex Task Template | Task Template | Draft | Appendix H Section 6 |
| B02-CX-W0-007 | Create Publication Metadata Validation | Validation | Draft | publication.yaml |
| B02-CX-W0-008 | Create Appendix-to-Index Sync Check | Validation | Draft | Appendices A–H, indexes/* |

## Required Outputs

```text
indexes/README.md
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md

core-specs/README.md
core-specs/domains/README.md
core-specs/objects/README.md
core-specs/services/README.md
core-specs/events/README.md
core-specs/contracts/README.md
core-specs/api/README.md
core-specs/agents/README.md
core-specs/workflows/README.md

codex-tasks/README.md
codex-tasks/_template.md
codex-tasks/wave-0/README.md
codex-tasks/wave-1/README.md
codex-tasks/wave-2/README.md
codex-tasks/wave-3/README.md
codex-tasks/wave-4/README.md
codex-tasks/wave-5/README.md
codex-tasks/wave-6/README.md
codex-tasks/wave-7/README.md
```

## Prohibited Overreach

```text
no domain implementation
no business service implementation
no database schema design
no product UI
no AI behavior
no external integration
```

---

# 9. Wave 1 — Foundation Core

## Purpose

Implement the Foundation Core baseline.

## Wave 1 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W1-001 | Implement Identity Domain Spec | Foundation Core | Draft | domain-index.md, object-index.md |
| B02-CX-W1-002 | Implement Organization Domain Spec | Foundation Core | Draft | domain-index.md, object-index.md |
| B02-CX-W1-003 | Implement User Domain Spec | Foundation Core | Draft | domain-index.md, object-index.md |
| B02-CX-W1-004 | Implement Permission Domain Spec | Foundation Core | Draft | domain-index.md, service-index.md |
| B02-CX-W1-005 | Implement Knowledge Domain Spec | Foundation Core | Draft | domain-index.md, object-index.md |
| B02-CX-W1-006 | Create Foundation Object Specs | Foundation Objects | Draft | object-index.md |
| B02-CX-W1-007 | Create Foundation Service Specs | Foundation Services | Draft | service-index.md |
| B02-CX-W1-008 | Create Foundation Event Specs | Foundation Events | Draft | event-index.md |
| B02-CX-W1-009 | Create Foundation API Specs | Foundation APIs | Draft | api-index.md |
| B02-CX-W1-010 | Create Foundation Fixtures and Tests | Fixtures and Tests | Draft | core-specs/foundation |

## MVP Depth

```text
Identity: Must Implement
Organization: Must Implement
User: Must Implement
Permission: Must Implement
Knowledge: Must Implement
Policy: Partial Implement
Capability: Partial Implement as cross-cutting system
```

## Prohibited Overreach

```text
no full enterprise IAM
no full policy engine
no full knowledge automation
no unreviewed AI knowledge use
no external identity marketplace
```

---

# 10. Wave 2 — Professional Core

## Purpose

Implement the professional trademark and brand Core baseline.

## Wave 2 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W2-001 | Implement Brand Domain Spec | Professional Core | Draft | domain-index.md, object-index.md |
| B02-CX-W2-002 | Implement Trademark Domain Spec | Professional Core | Draft | domain-index.md, object-index.md |
| B02-CX-W2-003 | Implement Jurisdiction Domain Spec | Professional Core | Draft | domain-index.md, service-index.md |
| B02-CX-W2-004 | Implement Classification Domain Spec | Professional Core | Draft | domain-index.md, agent-index.md |
| B02-CX-W2-005 | Implement Document Domain Spec | Professional Core | Draft | domain-index.md, object-index.md |
| B02-CX-W2-006 | Implement Evidence Baseline Spec | Professional Core | Draft | domain-index.md, object-index.md |
| B02-CX-W2-007 | Create Professional Object Specs | Professional Objects | Draft | object-index.md |
| B02-CX-W2-008 | Create Professional Service Specs | Professional Services | Draft | service-index.md |
| B02-CX-W2-009 | Create Professional Event Specs | Professional Events | Draft | event-index.md |
| B02-CX-W2-010 | Create Professional API Specs | Professional APIs | Draft | api-index.md |
| B02-CX-W2-011 | Create Professional Fixtures and Tests | Fixtures and Tests | Draft | core-specs/professional |

## MVP Depth

```text
Brand: Must Implement
Trademark: Must Implement
Jurisdiction: Must Implement
Classification: Must Implement
Document: Must Implement
Evidence: Partial Implement
```

## Prohibited Overreach

```text
no complete global office automation
no full evidence scoring engine
no automatic legal strategy
no unreviewed classification finalization
no automatic official filing
```

---

# 11. Wave 3 — Business Execution Core

## Purpose

Implement the execution kernel that converts professional objects and service requests into orders, matters, tasks, events and workflow contracts.

## Wave 3 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W3-001 | Implement Customer Domain Spec | Business Execution | Draft | domain-index.md, object-index.md |
| B02-CX-W3-002 | Implement Order Domain Spec | Business Execution | Draft | domain-index.md, service-index.md |
| B02-CX-W3-003 | Implement Matter Domain Spec | Business Execution | Draft | domain-index.md, object-index.md |
| B02-CX-W3-004 | Implement Workflow Contract Domain Spec | Business Execution | Draft | domain-index.md, service-index.md |
| B02-CX-W3-005 | Implement Task Domain Spec | Business Execution | Draft | domain-index.md, object-index.md |
| B02-CX-W3-006 | Implement Event Domain Spec | Business Execution | Draft | domain-index.md, event-index.md |
| B02-CX-W3-007 | Implement Notification Baseline Spec | Business Execution | Draft | domain-index.md, service-index.md |
| B02-CX-W3-008 | Implement Business Responsibility Baseline | Cross-Cutting Responsibility | Draft | domain-index.md, object-index.md |
| B02-CX-W3-009 | Create Order-to-Matter Conversion Spec | Workflow Execution | Draft | service-index.md, event-index.md |
| B02-CX-W3-010 | Create Business Execution Fixtures and Tests | Fixtures and Tests | Draft | core-specs/business-execution |

## MVP Depth

```text
Customer: Must Implement
Order: Must Implement
Matter: Must Implement
Workflow Contract: Must Implement
Task: Must Implement
Event: Must Implement
Notification: Partial Implement
Business Responsibility: Partial Implement as cross-cutting system
```

## Prohibited Overreach

```text
no full CRM
no full billing system
no full sales commission system
no full workflow UI
no unbounded notification engine
no unreviewed AI task completion
```

---

# 12. Wave 4 — AI Governance and Review

## Purpose

Implement the AI governance baseline and review system required before AI becomes operational in Core-consuming products.

## Wave 4 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W4-001 | Implement AI Agent Object Spec | AI Governance | Draft | object-index.md, agent-index.md |
| B02-CX-W4-002 | Implement Agent Contract Spec | AI Governance | Draft | agent-index.md, api-index.md |
| B02-CX-W4-003 | Implement AI Output Object Spec | AI Governance | Draft | object-index.md, event-index.md |
| B02-CX-W4-004 | Implement AI Recommendation Object Spec | AI Governance | Draft | object-index.md, agent-index.md |
| B02-CX-W4-005 | Implement AI Audit Record Spec | AI Governance | Draft | object-index.md, event-index.md |
| B02-CX-W4-006 | Implement Review Record Spec | AI Governance | Draft | object-index.md, business responsibility |
| B02-CX-W4-007 | Create Agent Contract Validation Service | AI Governance | Draft | service-index.md, agent-index.md |
| B02-CX-W4-008 | Create Classification Assistant Baseline Spec | AI Agent | Draft | agent-index.md |
| B02-CX-W4-009 | Create Trademark Status Summary Agent Baseline Spec | AI Agent | Draft | agent-index.md |
| B02-CX-W4-010 | Create Codex Implementation Agent Constraints | Codex Governance | Draft | agent-index.md, codex-task-index.md |
| B02-CX-W4-011 | Create AI Governance Fixtures and Tests | Fixtures and Tests | Draft | core-specs/agents |

## MVP Depth

```text
AI Governance: Must Implement
AI Agent Identity: Must Implement
Agent Contract: Must Implement
AI Output: Must Implement
AI Audit Record: Must Implement
Classification Assistant: Must Implement / Partial
Trademark Status Summary: Must Implement / Partial
Document Draft Assistant: Partial
Routing Assistant: Partial
Office Action Assistant: Reserved Boundary
Opportunity Discovery Agent: Reserved Boundary
```

## Prohibited Overreach

```text
no prompt-only agents
no AI without Agent Contract
no AI without audit
no full AI legal strategy
no unreviewed official filing output
no autonomous professional decisions
no AI state mutation without services
```

---

# 13. Wave 5 — Product Consumption Baseline

## Purpose

Create consumption contracts for MVP consumers.

## Wave 5 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W5-001 | Create MarkReg Core Consumption Contract | Consumption Baseline | Draft | api-index.md, service-index.md |
| B02-CX-W5-002 | Create MarkOrbit Lite Core Consumption Contract | Consumption Baseline | Draft | api-index.md, service-index.md |
| B02-CX-W5-003 | Create Workplace Core Consumption Contract | Consumption Baseline | Draft | api-index.md, workflow contracts |
| B02-CX-W5-004 | Create AI Agent Consumption Contract | Consumption Baseline | Draft | agent-index.md, api-index.md |
| B02-CX-W5-005 | Create Codex Consumption Contract | Consumption Baseline | Draft | codex-task-index.md, agent-index.md |
| B02-CX-W5-006 | Create Core Consumption API Baseline | API Baseline | Draft | api-index.md |
| B02-CX-W5-007 | Create Consumption Contract Tests | Tests | Draft | core-specs/contracts |

## MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## Prohibited Overreach

```text
no full product UI
no full client portal
no full partner center
no full service platform
no full external integration layer
no full reporting suite
```

---

# 14. Wave 6 — Growth Core Baseline

## Purpose

Implement limited baseline support for collaboration and growth domains without overbuilding future marketplace or opportunity systems.

## Wave 6 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W6-001 | Implement Communication Baseline Spec | Growth Core | Draft | domain-index.md, object-index.md |
| B02-CX-W6-002 | Implement Agent Baseline Spec | Growth Core | Draft | domain-index.md, agent-index.md |
| B02-CX-W6-003 | Implement Service Provider Baseline Spec | Growth Core | Draft | domain-index.md, service-index.md |
| B02-CX-W6-004 | Implement Routing Baseline Spec | Growth Core | Draft | domain-index.md, agent-index.md |
| B02-CX-W6-005 | Implement Opportunity Baseline Spec | Growth Core | Draft | domain-index.md, object-index.md |
| B02-CX-W6-006 | Reserve Partner Boundary Spec | Reserved Boundary | Draft | domain-index.md |
| B02-CX-W6-007 | Reserve Service Network Boundary Spec | Reserved Boundary | Draft | domain-index.md |
| B02-CX-W6-008 | Create Growth Core Fixtures and Tests | Fixtures and Tests | Draft | core-specs/collaboration-network |

## MVP Depth

```text
Communication: Partial Implement
Agent: Partial Implement
Service Provider: Partial Implement
Routing: Partial Implement
Opportunity: Partial Implement
Partner: Reserved Boundary
Service Network: Reserved Boundary
```

## Prohibited Overreach

```text
no full MGSN marketplace
no full provider ranking
no full opportunity scoring engine
no full partner portal
no full network trust economy
no automatic provider selection without review
```

---

# 15. Wave 7 — Validation, Hardening and Release

## Purpose

Validate the Core specification system, implementation scaffold, fixtures, tests and release readiness.

Wave 7 is the acceptance wave.

## Wave 7 Task Index

| Task ID | Title | Package | Status | Primary Sources |
|--------|-------|---------|--------|-----------------|
| B02-CX-W7-001 | Validate Metadata and Paths | Validation | Draft | publication.yaml, repository scaffold |
| B02-CX-W7-002 | Validate Domain/Object/Service/Event Consistency | Validation | Draft | domain-index.md, object-index.md, service-index.md, event-index.md |
| B02-CX-W7-003 | Validate API and Contract Consistency | Validation | Draft | api-index.md, core-specs/contracts |
| B02-CX-W7-004 | Validate Agent Contract Completeness | Validation | Draft | agent-index.md, core-specs/agents |
| B02-CX-W7-005 | Validate Codex Task Source References | Validation | Draft | codex-task-index.md, codex-tasks/ |
| B02-CX-W7-006 | Run Fixture Test Suite | Testing | Draft | test fixtures |
| B02-CX-W7-007 | Run Prohibited Overreach Check | Governance | Draft | all indexes and core-specs |
| B02-CX-W7-008 | Produce Release Candidate Report | Release | Draft | validation results |
| B02-CX-W7-009 | Produce Second Draft Acceptance Report | Release | Draft | full repository |

## Prohibited Overreach

```text
no new architecture
no new domains
no new object meanings
no new service responsibilities
no new event semantics
no MVP expansion
```

Wave 7 validates and hardens approved specs only.

---

# 16. Task Package Map

Codex tasks are grouped into packages.

```text
Repository Scaffold
Index Scaffold
Spec Scaffold
Template Scaffold
Foundation Core
Professional Core
Business Execution Core
AI Governance
Product Consumption Baseline
Growth Core Baseline
Fixtures and Tests
Validation
Release
```

Package-to-wave mapping:

| Package | Waves |
|--------|-------|
| Repository Scaffold | Wave 0 |
| Index Scaffold | Wave 0 |
| Spec Scaffold | Wave 0 |
| Template Scaffold | Wave 0 |
| Foundation Core | Wave 1 |
| Professional Core | Wave 2 |
| Business Execution Core | Wave 3 |
| AI Governance | Wave 4 |
| Product Consumption Baseline | Wave 5 |
| Growth Core Baseline | Wave 6 |
| Fixtures and Tests | Waves 0–7 |
| Validation | Waves 0 and 7 |
| Release | Wave 7 |

---

# 17. Matrix-to-Codex Rule

Every implementation task must trace back to the MVP Execution Matrix.

The trace is:

```text
MVP Execution Matrix Row
        ↓
Appendix Entry
        ↓
Index Entry
        ↓
core-specs File
        ↓
Codex Task
        ↓
Implementation Artifact
        ↓
Test
        ↓
Acceptance
```

A Codex task without a matrix row is not implementation-ready unless it is a repository scaffold, template scaffold or validation task.

---

# 18. Source Specification Requirements

Every Codex task must cite source specifications.

Acceptable source specifications include:

```text
Book 02 manuscript chapter
Appendix A–H
index file
core-specs file
approved template
accepted previous Codex task output
```

Unacceptable sources include:

```text
memory only
conversation-only instruction
product assumption
AI guess
unreviewed prompt
unapproved implementation shortcut
```

---

# 19. Test Requirements

Every Codex task must define test requirements.

Allowed test types include:

```text
path existence test
metadata validation test
schema validation test
object ownership test
service-event mapping test
event naming test
contract completeness test
API permission test
agent contract completeness test
fixture test
snapshot test
prohibited-overreach test
acceptance checklist test
```

A task cannot be accepted without tests unless it is explicitly marked documentation-only and reviewed.

---

# 20. Fixture Requirements

Core fixtures validate implementation behavior without production data.

Fixture categories include:

```text
identity fixtures
organization fixtures
user fixtures
permission fixtures
knowledge fixtures
brand fixtures
trademark fixtures
jurisdiction fixtures
classification fixtures
document fixtures
customer fixtures
order fixtures
matter fixtures
task fixtures
event fixtures
AI output fixtures
agent contract fixtures
routing fixtures
communication fixtures
Codex task fixtures
```

Fixtures must not contain sensitive production data.

---

# 21. Prohibited Overreach Rules

Codex must not:

```text
invent Core domains
change the 26-domain baseline
treat Capability or Business Responsibility as ordinary domains without classification
invent Core Object meanings
invent service responsibilities
invent event semantics
treat logs as Core Events
create AI agents without Agent Contract
treat prompt as agent
bypass review for high-risk AI output
implement full MGSN marketplace
implement full opportunity scoring
implement full Brand Asset Vault
implement full external integration platform
implement product UI in Core tasks
create business pricing policy
skip tests
ignore source specs
```

---

# 22. Acceptance Gate Sequence

Codex work must pass these gates.

```text
Gate 0 — Source Spec Gate
Gate 1 — Scope Gate
Gate 2 — Dependency Gate
Gate 3 — Template Gate
Gate 4 — Implementation Gate
Gate 5 — Test Gate
Gate 6 — Governance Gate
Gate 7 — Acceptance Gate
```

## Gate 0 — Source Spec Gate

The task references approved sources.

## Gate 1 — Scope Gate

The task has clear in-scope and out-of-scope boundaries.

## Gate 2 — Dependency Gate

Dependencies are implemented or explicitly mocked.

## Gate 3 — Template Gate

Output follows approved templates.

## Gate 4 — Implementation Gate

Implementation exists.

## Gate 5 — Test Gate

Tests pass.

## Gate 6 — Governance Gate

No prohibited overreach is detected.

## Gate 7 — Acceptance Gate

Human review accepts the task.

---

# 23. Initial Detailed Task Seeds

The following task seeds should be generated first after this index is accepted.

## 23.1 B02-CX-W0-001 — Create Repository Scaffold

```text
Wave: 0
Package: Repository Scaffold
Status: Draft
Source Specs:
    README.md
    publication.yaml
    indexes/README.md
    codex-task-index.md
Expected Outputs:
    required repository folders
    README files
    placeholder files
Tests:
    path existence tests
Prohibited Overreach:
    no business functionality
```

## 23.2 B02-CX-W0-002 — Create indexes/ Scaffold

```text
Wave: 0
Package: Index Scaffold
Status: Draft
Source Specs:
    Appendices A–H
    indexes/README.md
Expected Outputs:
    indexes/*.md
Tests:
    appendix-to-index consistency test
```

## 23.3 B02-CX-W0-003 — Create core-specs/ Scaffold

```text
Wave: 0
Package: Spec Scaffold
Status: Draft
Source Specs:
    Chapters 22–27
    indexes/domain-index.md
    indexes/object-index.md
    indexes/service-index.md
    indexes/event-index.md
    indexes/api-index.md
    indexes/agent-index.md
Expected Outputs:
    core-specs folders and templates
Tests:
    template completeness tests
```

## 23.4 B02-CX-W0-004 — Create codex-tasks/ Scaffold

```text
Wave: 0
Package: Task Scaffold
Status: Draft
Source Specs:
    indexes/codex-task-index.md
Expected Outputs:
    codex-tasks wave folders
Tests:
    task naming and wave structure tests
```

## 23.5 B02-CX-W0-006 — Create Codex Task Template

```text
Wave: 0
Package: Task Template
Status: Draft
Source Specs:
    codex-task-index.md Section 6
Expected Outputs:
    codex-tasks/_template.md
Tests:
    template field completeness test
```

---

# 24. Required codex-tasks/ Scaffold

After this index is accepted, generate:

```text
codex-tasks/README.md
codex-tasks/_template.md
codex-tasks/wave-0/README.md
codex-tasks/wave-1/README.md
codex-tasks/wave-2/README.md
codex-tasks/wave-3/README.md
codex-tasks/wave-4/README.md
codex-tasks/wave-5/README.md
codex-tasks/wave-6/README.md
codex-tasks/wave-7/README.md
```

Each wave directory should later include task files generated from this index.

---

# 25. Codex Task File Naming

Task files should use:

```text
{task_id}_{short-kebab-title}.md
```

Examples:

```text
B02-CX-W0-001_create-repository-scaffold.md
B02-CX-W1-001_implement-identity-domain-spec.md
B02-CX-W4-002_implement-agent-contract-spec.md
B02-CX-W7-007_run-prohibited-overreach-check.md
```

---

# 26. Validation Rules

The Codex task index must pass the following validation checks.

```text
[ ] Every task has a Task ID.
[ ] Every task ID follows B02-CX-W{wave}-{sequence}.
[ ] Every task has a wave.
[ ] Every task has a package.
[ ] Every task has a status.
[ ] Every task has source specifications.
[ ] Every implementation task has related index entries.
[ ] Every implementation task has related core-specs files or planned core-specs outputs.
[ ] Every task has dependencies or explicit no-dependency reason.
[ ] Every task has expected outputs.
[ ] Every task has test requirements.
[ ] Every task has prohibited overreach.
[ ] Every task has acceptance criteria.
[ ] No task changes the 26-domain baseline.
[ ] No task promotes cross-cutting systems into ordinary domains.
[ ] No task implements deferred scope without approval.
[ ] No task allows Codex to define Core architecture.
```

---

# 27. Prohibited Task Changes

This index must not be changed to:

```text
allow Codex to define architecture
allow Codex to invent Core domains
allow Codex to invent object meanings
allow Codex to invent service responsibilities
allow Codex to invent event semantics
allow tasks without source specifications
allow tasks without tests
allow tasks without prohibited-overreach rules
allow MVP implementation of reserved future systems
allow AI agents without Agent Contract
allow product UI implementation in Core tasks
allow external integration implementation before API contracts
```

---

# 28. Release Readiness Criteria

The Core implementation roadmap is release-ready only when:

```text
[ ] Appendices A–H are complete.
[ ] indexes/ exists.
[ ] core-specs/ scaffold exists.
[ ] codex-tasks/ scaffold exists.
[ ] Wave 0 tasks are generated.
[ ] Source spec references are valid.
[ ] Prohibited overreach checks are defined.
[ ] Fixture strategy is defined.
[ ] Test strategy is defined.
[ ] Acceptance gates are defined.
```

---

# 29. Handoff to codex-tasks/

This index will generate future files under:

```text
codex-tasks/
```

Expected scaffold:

```text
codex-tasks/README.md
codex-tasks/_template.md
codex-tasks/wave-0/
codex-tasks/wave-1/
codex-tasks/wave-2/
codex-tasks/wave-3/
codex-tasks/wave-4/
codex-tasks/wave-5/
codex-tasks/wave-6/
codex-tasks/wave-7/
```

Initial task files should prioritize:

```text
B02-CX-W0-001_create-repository-scaffold.md
B02-CX-W0-002_create-indexes-scaffold.md
B02-CX-W0-003_create-core-specs-scaffold.md
B02-CX-W0-004_create-codex-tasks-scaffold.md
B02-CX-W0-005_create-spec-templates.md
B02-CX-W0-006_create-codex-task-template.md
B02-CX-W0-007_create-publication-metadata-validation.md
B02-CX-W0-008_create-appendix-to-index-sync-check.md
```

---

# 30. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines Codex Task operationally.
[ ] It states Codex does not define Core architecture.
[ ] It defines task ID format.
[ ] It defines task status vocabulary.
[ ] It defines task index fields.
[ ] It defines Wave 0–7.
[ ] It lists all Wave 0 tasks.
[ ] It lists all Wave 1 tasks.
[ ] It lists all Wave 2 tasks.
[ ] It lists all Wave 3 tasks.
[ ] It lists all Wave 4 tasks.
[ ] It lists all Wave 5 tasks.
[ ] It lists all Wave 6 tasks.
[ ] It lists all Wave 7 tasks.
[ ] It defines task package map.
[ ] It defines matrix-to-Codex rule.
[ ] It defines source specification requirements.
[ ] It defines test requirements.
[ ] It defines fixture requirements.
[ ] It defines prohibited overreach rules.
[ ] It defines acceptance gate sequence.
[ ] It defines initial detailed task seeds.
[ ] It defines codex-tasks/ scaffold.
[ ] It defines task file naming.
[ ] It defines validation rules.
[ ] It defines prohibited task changes.
[ ] It defines release readiness criteria.
[ ] It hands off to codex-tasks/.
```

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Codex Task Index derived from B02-APP-H. Defines task identity, wave structure, task packages, source requirements, tests, fixtures, prohibited overreach, acceptance gates and handoff to codex-tasks/. |

---

**End of Index**
