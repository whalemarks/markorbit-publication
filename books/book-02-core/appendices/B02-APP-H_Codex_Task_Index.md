# Book 02

# Appendix H — Codex Task Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-H  
**Appendix Title:** Codex Task Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Chapters:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-CH-31 — Codex Implementation Roadmap

**Related Appendices:**

- B02-APP-A — Glossary
- B02-APP-B — Core Domain Index
- B02-APP-C — Core Object Index
- B02-APP-D — Core Service Index
- B02-APP-E — Event Index
- B02-APP-F — API Index
- B02-APP-G — Agent Index

---

# 1. Appendix Purpose

This appendix defines the canonical Codex Task Index for Book 02.

The Codex Task Index converts the second canonical draft into a controlled implementation roadmap.

It does not implement the Core.

It defines what Codex may implement later, in what order, from which source specifications, under what constraints, and with what acceptance criteria.

The purpose of this appendix is to prevent Codex from becoming an uncontrolled architecture author.

The rule is:

```text
Codex implements approved Core specifications.
Codex does not define Core architecture.
```

This appendix defines:

```text
Codex task identity rules
Codex task template
Codex wave structure
Codex task package mapping
task dependency rules
source specification requirements
prohibited overreach
test requirements
acceptance criteria
MVP / Partial / Future consumer constraints
core-specs/ handoff requirements
indexes/ handoff requirements
release gate requirements
```

---

# 2. Canonical Codex Rule

Book 02 uses the following canonical Codex rule:

```text
Specifications before Codex.
Appendices before core-specs.
Indexes before implementation tasks.
Tests before acceptance.
Deferred scope remains deferred.
```

Codex may implement only after:

```text
1. Book 02 manuscript has defined the architecture.
2. Appendices A–H have stabilized canonical indexes.
3. indexes/ has been generated from appendices.
4. core-specs/ templates and baseline specs exist.
5. A Codex task references approved source specs.
6. The task defines acceptance criteria and prohibited overreach.
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

# 4. Codex Task Identity Format

Codex tasks use the following ID format:

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

# 5. Codex Task Status

Codex tasks use the following status vocabulary.

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

## 5.1 Draft

The task is proposed but not ready for implementation.

## 5.2 Ready

The task has source specs, dependencies, scope, tests and acceptance criteria.

## 5.3 In Progress

Codex or engineering is implementing the task.

## 5.4 Blocked

The task cannot proceed because a source spec, dependency, decision or test fixture is missing.

## 5.5 Implemented

Implementation exists but has not yet passed required tests and review.

## 5.6 Tested

Implementation has passed required tests but still requires acceptance.

## 5.7 Accepted

The implementation has passed review and may be treated as complete.

## 5.8 Rejected

The implementation does not meet acceptance criteria.

## 5.9 Deferred

The task is intentionally postponed.

## 5.10 Superseded

The task has been replaced by a later task.

---

# 6. Codex Task Template

Every Codex task must follow this template.

```text
# Codex Task

1. Task ID
2. Task Title
3. Wave
4. Task Package
5. Status
6. Source Specifications
7. Related Appendix Entries
8. Related core-specs Files
9. Dependencies
10. Objective
11. In Scope
12. Out of Scope
13. Expected Outputs
14. Objects Affected
15. Services Affected
16. Events Affected
17. Contracts Affected
18. API Surfaces Affected
19. AI Agents Affected
20. Workflow Usage
21. Product Consumers
22. MVP Depth
23. Implementation Instructions
24. Test Requirements
25. Fixture Requirements
26. Validation Requirements
27. Prohibited Overreach
28. Acceptance Criteria
29. Review Notes
30. Revision Notes
```

A Codex task that lacks source specifications is not ready.

A Codex task that lacks prohibited overreach is unsafe.

A Codex task that lacks tests cannot be accepted.

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

The waves follow the dependency structure defined in Chapters 29–31 and Appendices A–G.

---

# 8. Wave 0 — Repository and Spec Scaffold

## Purpose

Wave 0 creates the repository and specification scaffold required before any detailed implementation begins.

Wave 0 does not implement business functionality.

It establishes controlled folders, templates, indexes and validation scripts.

## Source Specifications

```text
README.md
publication.yaml
CHANGELOG.md
B02-APP-A — Glossary
B02-APP-B — Core Domain Index
B02-APP-C — Core Object Index
B02-APP-D — Core Service Index
B02-APP-E — Event Index
B02-APP-F — API Index
B02-APP-G — Agent Index
B02-APP-H — Codex Task Index
B02-CH-31 — Codex Implementation Roadmap
```

## Wave 0 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W0-001 | Create Repository Scaffold | Repository Scaffold | Draft |
| B02-CX-W0-002 | Create indexes/ Scaffold | Index Scaffold | Draft |
| B02-CX-W0-003 | Create core-specs/ Scaffold | Spec Scaffold | Draft |
| B02-CX-W0-004 | Create codex-tasks/ Scaffold | Task Scaffold | Draft |
| B02-CX-W0-005 | Create Spec Templates | Template Scaffold | Draft |
| B02-CX-W0-006 | Create Codex Task Template | Task Template | Draft |
| B02-CX-W0-007 | Create Publication Metadata Validation | Validation | Draft |
| B02-CX-W0-008 | Create Appendix-to-Index Sync Check | Validation | Draft |

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

core-specs/domains/_template.md
core-specs/objects/_template.md
core-specs/services/_template.md
core-specs/events/_template.md
core-specs/contracts/_template.md
core-specs/api/_template.md
core-specs/agents/_template.md
core-specs/workflows/_template.md

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

Wave 0 must not implement:

```text
domain models
business services
AI behavior
product UI
API routes
event bus logic
database schemas
external integrations
```

---

# 9. Wave 1 — Foundation Core

## Purpose

Wave 1 implements the Foundation Core baseline.

It creates the initial executable foundation for identity, organization, users, permissions and knowledge.

## Source Specifications

```text
B02-APP-B — Foundation Domains
B02-APP-C — Foundation Objects
B02-APP-D — Foundation Services
B02-APP-E — Foundation Events
B02-APP-F — Foundation APIs
B02-CH-18 — Identity Specification
B02-CH-20 — Knowledge Specification
```

## Wave 1 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W1-001 | Implement Identity Domain Spec | Foundation Core | Draft |
| B02-CX-W1-002 | Implement Organization Domain Spec | Foundation Core | Draft |
| B02-CX-W1-003 | Implement User Domain Spec | Foundation Core | Draft |
| B02-CX-W1-004 | Implement Permission Domain Spec | Foundation Core | Draft |
| B02-CX-W1-005 | Implement Knowledge Domain Spec | Foundation Core | Draft |
| B02-CX-W1-006 | Create Foundation Object Specs | Foundation Objects | Draft |
| B02-CX-W1-007 | Create Foundation Service Specs | Foundation Services | Draft |
| B02-CX-W1-008 | Create Foundation Event Specs | Foundation Events | Draft |
| B02-CX-W1-009 | Create Foundation API Specs | Foundation APIs | Draft |
| B02-CX-W1-010 | Create Foundation Fixtures and Tests | Fixtures and Tests | Draft |

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

Wave 1 must not implement:

```text
full enterprise IAM platform
full policy engine
full knowledge automation
unreviewed AI knowledge use
external partner identity marketplace
```

---

# 10. Wave 2 — Professional Core

## Purpose

Wave 2 implements the professional trademark and brand Core baseline.

It provides the minimum professional domain foundation required by MarkReg and MarkOrbit Lite.

## Source Specifications

```text
B02-APP-B — Professional Domains
B02-APP-C — Professional Objects
B02-APP-D — Professional Services
B02-APP-E — Professional Events
B02-APP-F — Professional APIs
B02-CH-22 — Domain Specification
B02-CH-23 — Object Specification
B02-CH-24 — Service Specification
B02-CH-25 — Event Specification
```

## Wave 2 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W2-001 | Implement Brand Domain Spec | Professional Core | Draft |
| B02-CX-W2-002 | Implement Trademark Domain Spec | Professional Core | Draft |
| B02-CX-W2-003 | Implement Jurisdiction Domain Spec | Professional Core | Draft |
| B02-CX-W2-004 | Implement Classification Domain Spec | Professional Core | Draft |
| B02-CX-W2-005 | Implement Document Domain Spec | Professional Core | Draft |
| B02-CX-W2-006 | Implement Evidence Baseline Spec | Professional Core | Draft |
| B02-CX-W2-007 | Create Professional Object Specs | Professional Objects | Draft |
| B02-CX-W2-008 | Create Professional Service Specs | Professional Services | Draft |
| B02-CX-W2-009 | Create Professional Event Specs | Professional Events | Draft |
| B02-CX-W2-010 | Create Professional API Specs | Professional APIs | Draft |
| B02-CX-W2-011 | Create Professional Fixtures and Tests | Fixtures and Tests | Draft |

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

Wave 2 must not implement:

```text
complete global office data automation
full evidence scoring engine
full legal strategy engine
unreviewed classification finalization
automatic official filing
```

---

# 11. Wave 3 — Business Execution Core

## Purpose

Wave 3 implements the execution kernel that converts professional objects and service requests into orders, matters, tasks, events and workflow contracts.

## Source Specifications

```text
B02-APP-B — Business Execution Domains
B02-APP-C — Business Execution Objects
B02-APP-D — Business Execution Services
B02-APP-E — Business Execution Events
B02-APP-F — Business Execution APIs
B02-CH-27 — Core Consumption Specification
B02-CH-28 — Core MVP Boundary
B02-CH-29 — MVP Domain Priority
B02-CH-30 — MVP Execution Matrix
```

## Wave 3 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W3-001 | Implement Customer Domain Spec | Business Execution | Draft |
| B02-CX-W3-002 | Implement Order Domain Spec | Business Execution | Draft |
| B02-CX-W3-003 | Implement Matter Domain Spec | Business Execution | Draft |
| B02-CX-W3-004 | Implement Workflow Contract Domain Spec | Business Execution | Draft |
| B02-CX-W3-005 | Implement Task Domain Spec | Business Execution | Draft |
| B02-CX-W3-006 | Implement Event Domain Spec | Business Execution | Draft |
| B02-CX-W3-007 | Implement Notification Baseline Spec | Business Execution | Draft |
| B02-CX-W3-008 | Implement Business Responsibility Baseline | Cross-Cutting Responsibility | Draft |
| B02-CX-W3-009 | Create Order-to-Matter Conversion Spec | Workflow Execution | Draft |
| B02-CX-W3-010 | Create Business Execution Fixtures and Tests | Fixtures and Tests | Draft |

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

Wave 3 must not implement:

```text
full CRM
full billing system
full sales commission system
full workflow UI
unbounded notification engine
unreviewed AI task completion
```

---

# 12. Wave 4 — AI Governance and Review

## Purpose

Wave 4 implements the AI governance baseline and review system required before AI becomes operational in Core-consuming products.

## Source Specifications

```text
B02-CH-26 — AI Capability and Agent Governance Specification
B02-APP-C — AI Governance Objects
B02-APP-D — AI-assisted Services
B02-APP-E — AI Governance Events
B02-APP-F — AI Invocation API
B02-APP-G — Agent Index
```

## Wave 4 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W4-001 | Implement AI Agent Object Spec | AI Governance | Draft |
| B02-CX-W4-002 | Implement Agent Contract Spec | AI Governance | Draft |
| B02-CX-W4-003 | Implement AI Output Object Spec | AI Governance | Draft |
| B02-CX-W4-004 | Implement AI Recommendation Object Spec | AI Governance | Draft |
| B02-CX-W4-005 | Implement AI Audit Record Spec | AI Governance | Draft |
| B02-CX-W4-006 | Implement Review Record Spec | AI Governance | Draft |
| B02-CX-W4-007 | Create Agent Contract Validation Service | AI Governance | Draft |
| B02-CX-W4-008 | Create Classification Assistant Baseline Spec | AI Agent | Draft |
| B02-CX-W4-009 | Create Trademark Status Summary Agent Baseline Spec | AI Agent | Draft |
| B02-CX-W4-010 | Create Codex Implementation Agent Constraints | Codex Governance | Draft |
| B02-CX-W4-011 | Create AI Governance Fixtures and Tests | Fixtures and Tests | Draft |

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

Wave 4 must not implement:

```text
prompt-only agents
full AI legal strategy
unreviewed official filing output
autonomous professional decisions
AI state mutation without services
AI without audit
```

---

# 13. Wave 5 — Product Consumption Baseline

## Purpose

Wave 5 creates consumption contracts for MVP consumers.

It ensures that MarkReg, MarkOrbit Lite, Workplace, AI Agents and Codex consume the Core without redefining it.

## Source Specifications

```text
B02-CH-27 — Core Consumption Specification
B02-APP-F — API Index
B02-APP-G — Agent Index
B02-APP-H — Codex Task Index
```

## Wave 5 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W5-001 | Create MarkReg Core Consumption Contract | Consumption Baseline | Draft |
| B02-CX-W5-002 | Create MarkOrbit Lite Core Consumption Contract | Consumption Baseline | Draft |
| B02-CX-W5-003 | Create Workplace Core Consumption Contract | Consumption Baseline | Draft |
| B02-CX-W5-004 | Create AI Agent Consumption Contract | Consumption Baseline | Draft |
| B02-CX-W5-005 | Create Codex Consumption Contract | Consumption Baseline | Draft |
| B02-CX-W5-006 | Create Core Consumption API Baseline | API Baseline | Draft |
| B02-CX-W5-007 | Create Consumption Contract Tests | Tests | Draft |

## MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## Prohibited Overreach

Wave 5 must not implement:

```text
full product UI
full client portal
full partner center
full service platform
full external integration layer
full reporting suite
```

---

# 14. Wave 6 — Growth Core Baseline

## Purpose

Wave 6 implements limited baseline support for collaboration and growth domains without overbuilding future marketplace or opportunity systems.

## Source Specifications

```text
B02-APP-B — Collaboration Network Domains
B02-APP-C — Collaboration Network Objects
B02-APP-D — Collaboration Network Services
B02-APP-E — Collaboration Network Events
B02-APP-F — Collaboration Network APIs
B02-APP-G — Routing and Opportunity Agents
```

## Wave 6 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W6-001 | Implement Communication Baseline Spec | Growth Core | Draft |
| B02-CX-W6-002 | Implement Agent Baseline Spec | Growth Core | Draft |
| B02-CX-W6-003 | Implement Service Provider Baseline Spec | Growth Core | Draft |
| B02-CX-W6-004 | Implement Routing Baseline Spec | Growth Core | Draft |
| B02-CX-W6-005 | Implement Opportunity Baseline Spec | Growth Core | Draft |
| B02-CX-W6-006 | Reserve Partner Boundary Spec | Reserved Boundary | Draft |
| B02-CX-W6-007 | Reserve Service Network Boundary Spec | Reserved Boundary | Draft |
| B02-CX-W6-008 | Create Growth Core Fixtures and Tests | Fixtures and Tests | Draft |

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

Wave 6 must not implement:

```text
full MGSN marketplace
full provider ranking
full opportunity scoring engine
full partner portal
full network trust economy
automatic provider selection without review
```

---

# 15. Wave 7 — Validation, Hardening and Release

## Purpose

Wave 7 validates the Core specification system, implementation scaffold, fixtures, tests and release readiness.

It is the acceptance wave.

## Source Specifications

```text
All rewritten manuscript chapters
Appendices A–H
indexes/
core-specs/
codex-tasks/
test fixtures
validation scripts
release checklist
```

## Wave 7 Task Index

| Task ID | Title | Package | Status |
|--------|-------|---------|--------|
| B02-CX-W7-001 | Validate Metadata and Paths | Validation | Draft |
| B02-CX-W7-002 | Validate Domain/Object/Service/Event Consistency | Validation | Draft |
| B02-CX-W7-003 | Validate API and Contract Consistency | Validation | Draft |
| B02-CX-W7-004 | Validate Agent Contract Completeness | Validation | Draft |
| B02-CX-W7-005 | Validate Codex Task Source References | Validation | Draft |
| B02-CX-W7-006 | Run Fixture Test Suite | Testing | Draft |
| B02-CX-W7-007 | Run Prohibited Overreach Check | Governance | Draft |
| B02-CX-W7-008 | Produce Release Candidate Report | Release | Draft |
| B02-CX-W7-009 | Produce Second Draft Acceptance Report | Release | Draft |

## Prohibited Overreach

Wave 7 must not introduce new architecture.

It validates and hardens existing approved specs.

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

Each package must reference one or more waves.

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

A Codex task without a matrix row is not implementation-ready unless it is a repository scaffold or validation task.

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

Tests may include:

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

Core fixtures should be used to validate implementation behavior without requiring production data.

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

Task references approved sources.

## Gate 1 — Scope Gate

Task has clear in-scope and out-of-scope boundaries.

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

# 23. Required Index Outputs After Appendix H

After Appendix H is accepted, generate:

```text
indexes/README.md
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
```

The Codex Task Index should be converted into:

```text
indexes/codex-task-index.md
```

before detailed Codex task files are generated.

---

# 24. Required core-specs Scaffold After Indexes

After indexes exist, generate:

```text
core-specs/README.md
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
```

Only templates and baseline specs should be generated first.

Detailed implementation should wait for task readiness.

---

# 25. Required codex-tasks Scaffold

After `indexes/codex-task-index.md` exists, generate:

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

Each wave directory should include a README and task files generated from this appendix.

---

# 26. Codex Task File Naming

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

# 27. Initial Detailed Task Seeds

The following task seeds should be generated first after this appendix is accepted.

## 27.1 B02-CX-W0-001 — Create Repository Scaffold

```text
Wave: 0
Package: Repository Scaffold
Source Specs:
    README.md
    publication.yaml
    B02-APP-H
Expected Outputs:
    required repository folders
    README files
    placeholder files
Tests:
    path existence tests
Prohibited Overreach:
    no business functionality
```

## 27.2 B02-CX-W0-002 — Create indexes/ Scaffold

```text
Wave: 0
Package: Index Scaffold
Source Specs:
    Appendices A–H
Expected Outputs:
    indexes/*.md
Tests:
    appendix-to-index consistency test
```

## 27.3 B02-CX-W0-003 — Create core-specs/ Scaffold

```text
Wave: 0
Package: Spec Scaffold
Source Specs:
    Chapters 22–27
    Appendices B–G
Expected Outputs:
    core-specs folders and templates
Tests:
    template completeness tests
```

## 27.4 B02-CX-W0-004 — Create codex-tasks/ Scaffold

```text
Wave: 0
Package: Task Scaffold
Source Specs:
    Appendix H
Expected Outputs:
    codex-tasks wave folders
Tests:
    task naming and wave structure tests
```

## 27.5 B02-CX-W0-006 — Create Codex Task Template

```text
Wave: 0
Package: Task Template
Source Specs:
    Appendix H Section 6
Expected Outputs:
    codex-tasks/_template.md
Tests:
    template field completeness test
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

# 29. Acceptance Criteria

This appendix is accepted only if it satisfies the following criteria.

```text
[ ] It defines Codex Task clearly.
[ ] It defines Codex task ID rules.
[ ] It defines Codex task status vocabulary.
[ ] It defines the Codex task template.
[ ] It defines Wave 0–7.
[ ] It lists task seeds for each wave.
[ ] It maps tasks to source specifications.
[ ] It defines prohibited overreach.
[ ] It defines test requirements.
[ ] It defines fixture requirements.
[ ] It defines acceptance gate sequence.
[ ] It states that Codex does not define Core architecture.
[ ] It protects the 26-domain baseline.
[ ] It protects cross-cutting system classification.
[ ] It protects AI governance requirements.
[ ] It protects MVP scope.
[ ] It defines indexes/ handoff.
[ ] It defines core-specs/ handoff.
[ ] It defines codex-tasks/ handoff.
```

---

# 30. Appendix Completion Status

After Appendix H is accepted, the appendix sequence is complete.

```text
Appendix A — Glossary: Complete
Appendix B — Core Domain Index: Complete
Appendix C — Core Object Index: Complete
Appendix D — Core Service Index: Complete
Appendix E — Event Index: Complete
Appendix F — API Index: Complete
Appendix G — Agent Index: Complete
Appendix H — Codex Task Index: Complete
```

The next workstream should be:

```text
indexes/
```

not detailed implementation.

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex Task Index for second canonical draft. Defines Codex task identity, wave structure, task seeds, source requirements, prohibited overreach, testing, fixture strategy, acceptance gates and handoff to indexes/core-specs/codex-tasks. |

---

**End of Appendix**
