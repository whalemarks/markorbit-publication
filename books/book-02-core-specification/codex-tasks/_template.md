# Codex Task Template

**Repository:** `book-02-core`  
**Directory:** `codex-tasks/`  
**Template ID:** B02-TPL-CODEX-TASK  
**Template Type:** Codex Task Template  
**Source Appendix:** B02-APP-H — Codex Task Index  
**Source Index:** indexes/codex-task-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the relevant wave directory.

Recommended locations:

```text
codex-tasks/wave-0/{task_id}_{short-kebab-title}.md
codex-tasks/wave-1/{task_id}_{short-kebab-title}.md
codex-tasks/wave-2/{task_id}_{short-kebab-title}.md
codex-tasks/wave-3/{task_id}_{short-kebab-title}.md
codex-tasks/wave-4/{task_id}_{short-kebab-title}.md
codex-tasks/wave-5/{task_id}_{short-kebab-title}.md
codex-tasks/wave-6/{task_id}_{short-kebab-title}.md
codex-tasks/wave-7/{task_id}_{short-kebab-title}.md
```

Use the canonical task file naming rule:

```text
{task_id}_{short-kebab-title}.md
```

Examples:

```text
B02-CX-W0-001_create-repository-scaffold.md
B02-CX-W0-003_create-core-specs-scaffold.md
B02-CX-W1-001_implement-identity-domain-spec.md
B02-CX-W4-002_implement-agent-contract-spec.md
B02-CX-W7-007_run-prohibited-overreach-check.md
```

This template is for controlled Codex tasks only.

Do not use this template for:

```text
architecture decisions
new domain proposals
product PRDs
UI design requests
database-first designs
broad implementation prompts
prompt-only AI behavior
unapproved integration shortcuts
production deployment instructions without specs
```

A Codex Task implements approved specifications.

A Codex Task does not define Core architecture.

---

# Codex Task — {Task Title}

**Task ID:** B02-CX-W{wave}-{sequence}  
**Task Type:** Repository | Scaffold | Spec | Implementation | Test | Validation | Release  
**Wave:** Wave 0 | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5 | Wave 6 | Wave 7  
**Package:** Repository Scaffold | Index Scaffold | Spec Scaffold | Template Scaffold | Foundation Core | Professional Core | Business Execution Core | AI Governance | Product Consumption Baseline | Growth Core Baseline | Fixtures and Tests | Validation | Release  
**Status:** Draft  
**Version:** 0.1.0  
**Source Specifications:** {Source Files}  
**Related Indexes:** indexes/{index}.md  
**Related core-specs:** core-specs/{path}  
**Related Validation Specs:** core-specs/validation/{validation}.md  
**Dependencies:** {Task IDs or Source Dependencies}  
**Expected Outputs:** {Output Paths}  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred | Not Applicable  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Objective

Define the exact objective of this Codex task.

The objective should answer:

```text
What should Codex create, modify, validate or test?
Which approved specifications authorize this task?
What implementation gap does this task close?
What acceptance result is expected?
```

Example format:

```text
This task instructs Codex to ...
It is authorized by ...
It is required before ...
The task is complete when ...
```

The objective must be narrow, source-bound and testable.

---

# 2. Source Specifications

List all approved sources that authorize this task.

Use this format:

| Source | Source Type | Required | Purpose |
|--------|-------------|----------|---------|
| {path} | manuscript / appendix / index / core-spec / template / accepted task output | Yes / No | {Why this source is needed} |

Acceptable source specifications include:

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

If any required source is missing, the task must remain `Draft` or `Blocked`.

---

# 3. Scope

Define what is inside this task.

```text
This task includes:
- ...
- ...
- ...
```

Scope must be specific, file-oriented and source-bound.

Use path-level descriptions where possible.

---

# 4. Out of Scope

Define what is explicitly outside this task.

```text
This task does not include:
- ...
- ...
- ...
```

Common out-of-scope items:

```text
new architecture
new domains
new object meanings
new service responsibilities
new event semantics
product UI
physical database schema
external integrations
official filing automation
full marketplace implementation
deferred scope
production deployment
```

---

# 5. Dependencies

List dependencies.

Use this format:

| Dependency | Dependency Type | State | Required | Notes |
|------------|-----------------|-------|----------|-------|
| {Dependency} | source / directory / template / spec / validation / fixture / task / review / release | Required / Optional / Mocked / Deferred / Not Applicable | Yes / No | {Notes} |

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

A task with unmet required dependencies must remain `Blocked` or `Draft`.

---

# 6. Expected Outputs

List exact outputs.

Use this format:

| Output Path | Output Type | Required | Notes |
|-------------|-------------|----------|-------|
| {path} | directory / README / template / spec / fixture / test / validation report / release report / implementation artifact | Yes / No | {Notes} |

Expected outputs must be path-based and testable.

Examples:

```text
core-specs/domains/README.md
core-specs/domains/_template.md
codex-tasks/wave-0/README.md
core-specs/validation/repository/repository-structure-validation.md
```

---

# 7. Objects Affected

List Core Objects affected by this task.

Use this format:

| Object | Operation | Source Spec | Notes |
|--------|-----------|-------------|-------|
| {Object Name} | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no Core Objects are affected, state:

```text
No Core Objects are affected by this task.
```

Codex must not invent object meanings.

---

# 8. Services Affected

List Core Services affected by this task.

Use this format:

| Service | Operation | Source Spec | Notes |
|---------|-----------|-------------|-------|
| {Service Name} | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no Core Services are affected, state:

```text
No Core Services are affected by this task.
```

Codex must not invent service responsibilities.

---

# 9. Events Affected

List Core Events affected by this task.

Use this format:

| Event | Operation | Source Spec | Notes |
|-------|-----------|-------------|-------|
| {Event Name} | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no Core Events are affected, state:

```text
No Core Events are affected by this task.
```

Codex must not invent event semantics.

---

# 10. Contracts Affected

List Core Contracts affected by this task.

Use this format:

| Contract | Contract Type | Operation | Source Spec | Notes |
|----------|---------------|-----------|-------------|-------|
| {Contract Name} | Data / Service / Event / API / Workflow / Agent / Permission / Policy / Review / AI Governance / Codex / Validation | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no Core Contracts are affected, state:

```text
No Core Contracts are affected by this task.
```

---

# 11. API Surfaces Affected

List API surfaces affected by this task.

Use this format:

| API | Exposure Level | Operation | Source Spec | Notes |
|-----|----------------|-----------|-------------|-------|
| {API Name} | No API / Internal API / Product API / Agent API / Integration API / Admin API | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no APIs are affected, state:

```text
No API surfaces are affected by this task.
```

Codex must not create APIs without approved services and contracts.

---

# 12. AI Agents Affected

List AI, system or Codex agents affected by this task.

Use this format:

| Agent | Agent Type | Operation | Source Spec | Notes |
|-------|------------|-----------|-------------|-------|
| {Agent Name} | AI Agent / System Agent / Codex Agent / Validation Agent | create spec / update spec / validate / test / not applicable | {path} | {Notes} |

If no agents are affected, state:

```text
No Agents are affected by this task.
```

Agent-related tasks must preserve:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Allowed Capabilities
Prohibited Capabilities
Human Review Rule
Audit Rule
```

---

# 13. Workflow Usage

Define workflow usage.

```text
Workflow usage:
    none / creates workflow spec / updates workflow spec / validates workflow / tests workflow / consumes workflow
```

Related workflows:

```text
- ...
```

If no workflow usage is required, state:

```text
This task does not affect Core Workflows.
```

Codex must not create workflow states or transitions outside approved workflow specs.

---

# 14. Product Consumers

Classify affected product consumers.

## 14.1 MVP Consumers

```text
- MarkReg
- MarkOrbit Lite
- Workplace
- AI Agents
- Codex Implementation
```

## 14.2 Partial Consumers

```text
- MGSN
- Opportunity Engine baseline
- Brand Asset Vault baseline
```

## 14.3 Future Consumers

```text
- Partner Center
- Client Portal
- Service Platform
- External Integrations
- Reporting Consumers
```

If product consumers are not relevant, state:

```text
No product consumers are directly affected by this task.
```

Products may consume Core outputs.

Products must not redefine Core meaning.

---

# 15. MVP Depth

Define MVP depth for the task.

```text
MVP Depth:
    Must Implement | Partial Implement | Reserved Boundary | Deferred | Not Applicable
```

Explain:

```text
This task is classified as {MVP Depth} because ...
```

Reserved or Deferred scope must not be production-enabled in MVP.

---

# 16. Implementation Instructions

Provide precise implementation instructions for Codex.

Use step format:

```text
Step 1:
    ...

Step 2:
    ...

Step 3:
    ...

Step 4:
    ...
```

Instructions must be:

```text
source-bound
path-specific
scope-limited
testable
reviewable
```

Instructions must not ask Codex to invent architecture.

---

# 17. Test Requirements

Define tests required for acceptance.

Use this format:

| Test | Test Type | Required | Expected Result |
|------|-----------|----------|-----------------|
| {Test Name} | path existence / metadata / source traceability / schema / domain baseline / object ownership / service-event mapping / event naming / contract completeness / API permission / agent contract / workflow contract / fixture / snapshot / prohibited-overreach / acceptance checklist | Yes / No | {Expected Result} |

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

# 18. Fixture Requirements

Define fixture requirements.

```text
Fixtures Required:
    Required | Optional | Not Required | Deferred
```

If fixtures are required, define:

| Fixture | Fixture Category | Path | Required | Notes |
|---------|------------------|------|----------|-------|
| {Fixture Name} | identity / organization / user / permission / knowledge / brand / trademark / jurisdiction / classification / document / customer / order / matter / task / event / AI output / agent contract / routing / communication / Codex task | {path} | Yes / No | {Notes} |

Fixture cases should include where relevant:

```text
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

If no fixture is required, state:

```text
No fixture is required because ...
```

---

# 19. Validation Requirements

List validation requirements.

Use this format:

| Validation | Validation Category | Required | Source Spec | Notes |
|------------|---------------------|----------|-------------|-------|
| {Validation Name} | Repository / Metadata / Source Traceability / Domain / Object / Service / Event / Contract / API / Agent / Workflow / Cross-Cutting / Codex Task / Fixture / Prohibited Overreach / Release Readiness | Yes / No | {path} | {Notes} |

Common validation requirements:

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

---

# 20. Prohibited Overreach

Define general and task-specific prohibited overreach.

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

Task-specific prohibited overreach:

```text
- ...
- ...
```

---

# 21. Acceptance Criteria

This Codex Task is accepted only if:

```text
[ ] Objective is satisfied.
[ ] All required source specifications are cited.
[ ] Scope is followed.
[ ] Out-of-scope items are not implemented.
[ ] Required dependencies are satisfied or explicitly mocked.
[ ] Expected outputs exist.
[ ] Required metadata is present.
[ ] Required tests pass.
[ ] Required fixtures exist or explicit no-fixture reason is accepted.
[ ] Required validations pass.
[ ] No prohibited overreach is detected.
[ ] MVP depth is preserved.
[ ] Deferred scope remains deferred.
[ ] Review notes are recorded.
[ ] Human acceptance is recorded.
```

Add task-specific acceptance criteria:

```text
[ ] ...
[ ] ...
```

---

# 22. Review Notes

Record review notes.

```text
Reviewer:
Review Date:
Review Outcome: Accepted | Rejected | Blocked | Needs Revision | Deferred | Superseded
Validation Summary:
Known Limitations:
Required Follow-Up:
Next Task Dependencies:
```

Task acceptance requires human review.

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex task created from B02-TPL-CODEX-TASK. |

---

# 24. Completion Record

Complete this section only after implementation and review.

```text
Implementation Status:
Implemented Outputs:
Test Results:
Validation Results:
Prohibited Overreach Result:
Acceptance Status:
Accepted By:
Accepted Date:
Release Notes:
```

---

**End of Codex Task**
