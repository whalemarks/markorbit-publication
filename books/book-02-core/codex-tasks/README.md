# codex-tasks/

**Repository:** `book-02-core`  
**Directory:** `codex-tasks/`  
**Document:** `codex-tasks/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `codex-tasks/` directory contains controlled implementation instructions for Codex.

A Codex Task tells Codex what may be generated, modified, validated or tested based on approved MarkOrbit Core specifications.

This directory exists to convert approved Core specifications into safe, traceable, testable implementation work.

Codex tasks are not architecture decisions.

Codex tasks are not product ideas.

Codex tasks are not broad prompts.

Codex tasks are implementation controls.

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

# 3. Codex Task Is Not Architecture

A Codex Task is not:

```text
a new domain proposal
a new object meaning
a new service responsibility
a new event semantics definition
a product PRD
a UI design request
a database-first design
a prompt-only instruction
an integration shortcut
```

A Codex Task may implement artifacts derived from architecture.

It must not create architecture.

---

# 4. Directory Boundary

## 4.1 codex-tasks/ Owns

This directory owns:

```text
Codex task files
Codex task template
Codex task wave directories
task IDs
task packages
task scope
task dependencies
task source specifications
task expected outputs
task test requirements
task fixture requirements
task validation requirements
task prohibited-overreach rules
task acceptance criteria
task review notes
```

## 4.2 codex-tasks/ Does Not Own

This directory does not own:

```text
Book 02 architecture
appendix canonical definitions
index reference lists
core-spec meaning
domain baseline
object meaning
service responsibility
event semantics
API exposure rules
Agent governance rules
workflow state meaning
product UI
physical database schema
implementation code outside approved tasks
```

Those belong to manuscript, appendices, indexes, `core-specs/` or later implementation repositories.

---

# 5. Required Source Chain

Every Codex Task must trace to approved sources.

Required source chain:

```text
Manuscript Chapter
        ↓
Appendix
        ↓
Index
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

Accepted source files include:

```text
Book 02 manuscript chapters
Appendices A–H
indexes/
core-specs/
approved templates
accepted previous Codex task outputs
```

Unacceptable sources include:

```text
memory only
conversation-only instruction
unreviewed prompt
AI guess
product assumption
engineering convenience
UI-first interpretation
database-first interpretation
```

---

# 6. Required Directory Structure

The `codex-tasks/` directory should contain:

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

Each wave directory should contain:

```text
README.md
task files
```

---

# 7. Codex Task ID Format

Codex task IDs use this format:

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
    implementation wave

{sequence}
    three-digit sequence number inside the wave
```

Task file naming:

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

# 8. Codex Task Status Vocabulary

Codex tasks use controlled statuses.

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

Status rules:

```text
Draft
    task exists but is not ready for implementation

Ready
    task has approved sources, scope, tests and acceptance criteria

In Progress
    task is being implemented

Blocked
    task cannot continue due to missing dependency or failed gate

Implemented
    expected outputs were created

Tested
    required tests passed

Accepted
    human review accepted the task

Rejected
    output failed acceptance

Deferred
    task is intentionally postponed

Superseded
    task has been replaced by another task
```

Only `Ready` tasks may be implemented.

Only `Tested` tasks may be reviewed for acceptance.

Only `Accepted` tasks may be treated as complete.

---

# 9. Codex Wave Structure

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
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
core-specs/
```

---

# 10. Wave Directory Responsibilities

## 10.1 wave-0/

Repository and specification scaffold.

Purpose:

```text
create required directories
create README files
create templates
create validation scaffold
create Codex task scaffold
```

No business functionality should be implemented in Wave 0.

## 10.2 wave-1/

Foundation Core.

Purpose:

```text
Identity
Organization
User
Permission
Knowledge
Policy partial
Capability cross-cutting partial
```

## 10.3 wave-2/

Professional Core.

Purpose:

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence partial
```

## 10.4 wave-3/

Business Execution Core.

Purpose:

```text
Customer
Order
Matter
Workflow Contract
Task
Event
Notification partial
Business Responsibility cross-cutting partial
```

## 10.5 wave-4/

AI Governance and Review.

Purpose:

```text
AI Agent Identity
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Review Record
AI Governance Agent
Classification Assistant baseline
Trademark Status Summary baseline
Codex Implementation Agent constraints
Spec Consistency Review Agent baseline
```

## 10.6 wave-5/

Product Consumption Baseline.

Purpose:

```text
MarkReg consumption contract
MarkOrbit Lite consumption contract
Workplace consumption contract
AI Agent consumption contract
Codex consumption contract
Core consumption API baseline
```

## 10.7 wave-6/

Growth Core Baseline.

Purpose:

```text
Communication
Agent
Service Provider
Routing
Opportunity
Partner reserved
Service Network reserved
```

## 10.8 wave-7/

Validation, hardening and release.

Purpose:

```text
metadata validation
source traceability validation
domain/object/service/event consistency validation
API and contract validation
Agent Contract validation
Codex task source validation
fixture tests
prohibited-overreach checks
release candidate report
```

---

# 11. Required Task File Metadata

Each task file must begin with metadata.

```text
# Codex Task — {Task Title}

**Task ID:** B02-CX-W{wave}-{sequence}
**Task Type:** Repository | Scaffold | Spec | Implementation | Test | Validation | Release
**Wave:** Wave 0 | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5 | Wave 6 | Wave 7
**Package:** {Task Package}
**Status:** Draft
**Version:** 0.1.0
**Source Specifications:** ...
**Related Indexes:** ...
**Related core-specs:** ...
**Dependencies:** ...
**Expected Outputs:** ...
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 12. Required Task Sections

Every Codex task must include:

```text
1. Objective
2. Source Specifications
3. Scope
4. Out of Scope
5. Dependencies
6. Expected Outputs
7. Implementation Instructions
8. Test Requirements
9. Fixture Requirements
10. Validation Requirements
11. Prohibited Overreach
12. Acceptance Criteria
13. Review Notes
14. Revision Notes
```

Implementation tasks may also include:

```text
Objects Affected
Services Affected
Events Affected
Contracts Affected
API Surfaces Affected
AI Agents Affected
Workflow Usage
Product Consumers
MVP Depth
```

---

# 13. Task Package Map

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

# 14. Matrix-to-Codex Rule

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

A Codex task without a matrix row is not implementation-ready unless it is one of:

```text
repository scaffold task
template scaffold task
validation task
release task
```

---

# 15. Source Specification Requirements

Every Codex task must cite source specifications.

Required source references may include:

```text
manuscript chapter
appendix
index file
core-spec file
template file
accepted previous task output
```

Each source reference should include:

```text
source path
source section if applicable
reason for use
```

A task must be blocked if its required source specification is missing.

---

# 16. Dependency Rules

Every task must define dependencies.

Dependency types:

```text
source dependency
directory dependency
template dependency
spec dependency
validation dependency
fixture dependency
task dependency
review dependency
release dependency
```

Dependency states:

```text
Required
Optional
Mocked
Deferred
Not Applicable
```

A task with unmet required dependencies must remain `Blocked` or `Draft`.

---

# 17. Expected Output Rules

Every task must define expected outputs.

Expected outputs may include:

```text
directories
README files
templates
domain specs
object specs
service specs
event specs
contract specs
API specs
agent specs
workflow specs
cross-cutting specs
validation specs
test fixtures
validation reports
implementation artifacts
release reports
```

Expected outputs must be specific and path-based.

Example:

```text
Expected Outputs:
- core-specs/domains/README.md
- core-specs/domains/_template.md
- validation report confirming files exist
```

---

# 18. Test Requirements

Every task must define test requirements.

Allowed test types:

```text
path existence test
metadata validation test
schema validation test
source traceability test
domain baseline test
object ownership test
service-object mapping test
service-event mapping test
event naming test
contract completeness test
API permission test
agent contract completeness test
workflow contract test
fixture test
snapshot test
prohibited-overreach test
acceptance checklist test
```

A task cannot be accepted without tests unless explicitly marked documentation-only and reviewed.

---

# 19. Fixture Requirements

Tasks must define fixture requirements.

Fixture requirement values:

```text
Required
Optional
Not Required
Deferred
```

If fixtures are required, define:

```text
fixture category
fixture path
valid cases
invalid cases
permission failure cases
policy failure cases
review-required cases
AI audit cases
prohibited-overreach cases
expected results
```

Fixtures must not contain sensitive production data.

---

# 20. Validation Requirements

Each task must define validation requirements.

Validation may include:

```text
repository validation
metadata validation
source traceability validation
domain validation
object validation
service validation
event validation
contract validation
API validation
agent validation
workflow validation
cross-cutting validation
Codex task validation
fixture validation
prohibited-overreach validation
release readiness validation
```

Validation specs belong to:

```text
core-specs/validation/
```

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

Every task must include task-specific prohibited overreach.

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

# 23. Initial Wave 0 Task List

Wave 0 should begin with:

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

Wave 0 must be accepted before implementation waves begin.

---

# 24. Required README Files

Before detailed task files are generated, create:

```text
codex-tasks/wave-0/README.md
codex-tasks/wave-1/README.md
codex-tasks/wave-2/README.md
codex-tasks/wave-3/README.md
codex-tasks/wave-4/README.md
codex-tasks/wave-5/README.md
codex-tasks/wave-6/README.md
codex-tasks/wave-7/README.md
```

Each wave README must define:

```text
wave purpose
scope
out of scope
task list
dependencies
expected outputs
validation requirements
prohibited overreach
acceptance criteria
```

---

# 25. Codex Execution Rules

Codex may execute a task only if:

```text
task status is Ready
source specifications exist
dependencies are satisfied
expected outputs are defined
tests are defined
fixture requirements are defined or explicitly not required
prohibited overreach is defined
acceptance criteria are defined
```

Codex must stop or request review if:

```text
source specification is missing
scope conflicts with source specs
dependency is missing
expected output is ambiguous
task would change architecture
task would implement deferred scope
task would bypass review or audit
task would expose reserved boundary as MVP
```

---

# 26. Review and Acceptance Rules

Task acceptance requires human review.

Review should check:

```text
source compliance
scope compliance
output completeness
test results
fixture results
validation results
prohibited-overreach results
documentation completeness
```

Review outcomes:

```text
Accepted
Rejected
Blocked
Needs Revision
Deferred
Superseded
```

Accepted tasks must record:

```text
accepted outputs
reviewer
review date
validation results
known limitations
next task dependencies
```

---

# 27. Release Relationship

Codex tasks feed release readiness.

Release readiness requires:

```text
Wave 0 scaffold accepted
required templates accepted
source traceability validation passed
metadata validation passed
domain baseline validation passed
object ownership validation passed
service-event mapping validation passed
contract completeness validation passed
API contract validation passed
Agent Contract validation passed
workflow contract validation passed
prohibited-overreach validation passed
fixture strategy accepted
test strategy accepted
release candidate report generated
```

---

# 28. Prohibited Behavior

This directory must not:

```text
allow Codex to define architecture
allow source-less tasks
allow vague implementation prompts
allow tasks without acceptance criteria
allow tasks without tests
allow tasks without prohibited-overreach rules
allow implementation from manuscript prose without core-specs
allow deferred scope to become MVP
allow product UI implementation inside Core tasks
allow AI Agents without Agent Contracts
allow official filing automation in MVP
allow external marketplace implementation in Core MVP
```

---

# 29. Acceptance Criteria

The `codex-tasks/README.md` file is accepted when:

```text
[ ] It defines the purpose of codex-tasks/.
[ ] It states Codex implements approved Core specifications.
[ ] It states Codex does not define Core architecture.
[ ] It distinguishes Codex Task from architecture and product idea.
[ ] It defines directory boundary.
[ ] It defines required source chain.
[ ] It defines required directory structure.
[ ] It defines task ID format.
[ ] It defines task status vocabulary.
[ ] It defines wave structure.
[ ] It defines wave directory responsibilities.
[ ] It defines required task metadata.
[ ] It defines required task sections.
[ ] It defines task package map.
[ ] It defines matrix-to-Codex rule.
[ ] It defines source specification requirements.
[ ] It defines dependency rules.
[ ] It defines expected output rules.
[ ] It defines test requirements.
[ ] It defines fixture requirements.
[ ] It defines validation requirements.
[ ] It defines prohibited overreach rules.
[ ] It defines acceptance gate sequence.
[ ] It lists initial Wave 0 tasks.
[ ] It defines required wave README files.
[ ] It defines Codex execution rules.
[ ] It defines review and acceptance rules.
[ ] It defines release relationship.
[ ] It defines prohibited behavior.
```

---

# 30. Next Action

After this README is accepted, generate:

```text
codex-tasks/_template.md
```

Then generate wave README files:

```text
codex-tasks/wave-0/README.md
codex-tasks/wave-1/README.md
codex-tasks/wave-2/README.md
codex-tasks/wave-3/README.md
codex-tasks/wave-4/README.md
codex-tasks/wave-5/README.md
codex-tasks/wave-6/README.md
codex-tasks/wave-7/README.md
```

Do not generate detailed task files before the task template exists.

---

# 31. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for codex-tasks/. Defines task purpose, source chain, task ID rules, wave structure, package map, gates, validation, prohibited overreach and next template handoff. |

---

**End of README**
