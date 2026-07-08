# Validation Specification Template

**Repository:** `book-02-core`  
**Directory:** `core-specs/validation/`  
**Template ID:** B02-TPL-VALIDATION  
**Template Type:** Validation Specification Template  
**Source References:** Book 02 manuscript; Appendices A–H; indexes/; core-specs/; indexes/codex-task-index.md  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# How to Use This Template

Copy this template to the appropriate validation category directory.

Recommended locations:

```text
core-specs/validation/repository/{validation-name}.md
core-specs/validation/metadata/{validation-name}.md
core-specs/validation/traceability/{validation-name}.md
core-specs/validation/domain/{validation-name}.md
core-specs/validation/object/{validation-name}.md
core-specs/validation/service/{validation-name}.md
core-specs/validation/event/{validation-name}.md
core-specs/validation/contract/{validation-name}.md
core-specs/validation/api/{validation-name}.md
core-specs/validation/agent/{validation-name}.md
core-specs/validation/workflow/{validation-name}.md
core-specs/validation/cross-cutting/{validation-name}.md
core-specs/validation/codex/{validation-name}.md
core-specs/validation/fixtures/{validation-name}.md
core-specs/validation/release/{validation-name}.md
```

Use lowercase kebab-case filenames.

Examples:

```text
repository-structure-validation.md
publication-metadata-validation.md
source-traceability-validation.md
domain-baseline-validation.md
object-ownership-validation.md
service-event-mapping-validation.md
agent-contract-validation.md
prohibited-overreach-validation.md
release-readiness-validation.md
```

This template is for Core Validation Specifications only.

Do not use this template for:

```text
product QA scripts
UI testing plans
production monitoring dashboards
performance benchmarking
database migration tests
third-party vendor acceptance tests
manual checklist notes without source traceability
```

Validation may later be implemented as tests or scripts, but this template defines Core-level validation meaning first.

---

# Validation Specification — {Validation Name}

**Spec ID:** B02-VAL-{VALIDATION-ID}  
**Spec Type:** Validation  
**Validation Name:** {Validation Name}  
**Validation Category:** Repository | Metadata | Source Traceability | Domain | Object | Service | Event | Contract | API | Agent | Workflow | Cross-Cutting | Codex Task | Fixture | Prohibited Overreach | Release Readiness  
**Validation Target:** {Artifact Type or Directory}  
**Source References:** {Source Files}  
**Related Indexes:** indexes/{index}.md  
**Related core-specs:** core-specs/{path}  
**Related Codex Tasks:** codex-tasks/{task}  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase/Wave:** Wave 0 | Wave 1 | Wave 2 | Wave 3 | Wave 4 | Wave 5 | Wave 6 | Wave 7  
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Describe why this validation exists.

The purpose should answer:

```text
What Core consistency, governance or readiness issue does this validation protect?
Which artifacts does it check?
What failure would this validation prevent?
Why is this validation required before Codex implementation or release acceptance?
```

Example format:

```text
The {Validation Name} validates ...
It exists so that ...
It prevents ...
It is required before ...
```

---

# 2. Validation Meaning

Define the canonical meaning of this validation.

```text
{Validation Name} means ...
```

The meaning must be Core-level and source-traceable.

Do not define validation as:

```text
a product QA task
a UI testing task
a database unit test only
a production monitoring alert
a performance benchmark
an unreviewed script
```

Preferred definition pattern:

```text
This validation checks whether ...
```

---

# 3. Validation Category

Select one canonical category.

```text
Repository Validation
Metadata Validation
Source Traceability Validation
Domain Validation
Object Validation
Service Validation
Event Validation
Contract Validation
API Validation
Agent Validation
Workflow Validation
Cross-Cutting Validation
Codex Task Validation
Fixture Validation
Prohibited Overreach Validation
Release Readiness Validation
```

Explain why the category is correct.

```text
This validation belongs to {Validation Category} because ...
```

---

# 4. Validation Target

Define the validation target.

Allowed targets include:

```text
repository structure
publication metadata
manuscript chapters
appendices
indexes
core-specs directory
domain specs
object specs
service specs
event specs
contract specs
API specs
agent specs
workflow specs
cross-cutting specs
Codex task files
fixtures
implementation artifacts
release package
```

Use this structure:

```text
Target Type:
    ...

Target Path:
    ...

Target Files:
    - ...
    - ...

Target Scope:
    single file / directory / cross-directory / full repository / release package
```

The target must be specific enough to test.

---

# 5. Source References

List all required source references.

Use this format:

| Source | Source Type | Required | Notes |
|--------|-------------|----------|-------|
| {Source Path} | manuscript / appendix / index / core-spec / codex-task / fixture / implementation | Yes / No | {Notes} |

Required source chain for implementation-relevant validation:

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

If a validation does not require the full chain, state why.

---

# 6. Scope

Define what is inside this validation.

```text
This validation checks:
- ...
- ...
- ...
```

The scope should include architectural consistency, source traceability, metadata, ownership, contract completeness, governance or release readiness.

It should not include unrelated product QA, UI behavior, infrastructure monitoring or performance testing unless explicitly tied to Core acceptance.

---

# 7. Boundary

Define validation boundary.

## 7.1 In Boundary

```text
- ...
- ...
```

## 7.2 Out of Boundary

```text
- ...
- ...
```

## 7.3 Boundary Notes

Explain boundary-sensitive distinctions.

Examples:

```text
This validation checks ...
This validation does not decide ...
This validation blocks ...
This validation warns ...
```

---

# 8. Validation Inputs

Define required inputs.

Use this format:

| Input | Meaning | Required | Source | Notes |
|-------|---------|----------|--------|-------|
| {Input Name} | {Meaning} | Yes / No | {Source} | {Notes} |

Common validation inputs:

```text
file path
document metadata
spec metadata
source reference list
index entries
core-spec entries
Codex task entries
expected output list
acceptance checklist
fixture files
implementation artifact list
```

---

# 9. Validation Rules

Define validation rules.

Use checklist format.

```text
[ ] ...
[ ] ...
[ ] ...
```

Rules should be deterministic where possible.

Rules should distinguish between:

```text
required checks
conditional checks
advisory checks
release-blocking checks
```

Example:

```text
[ ] Every object spec must declare Owning Domain/System.
[ ] The owner must be one of the 26 baseline Core Domains or an explicitly declared cross-cutting system.
[ ] Product names must not be used as Core Object owners.
```

---

# 10. Validation Procedure

Define how validation should be performed.

Use this structure:

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

Procedure may include:

```text
read target files
parse metadata
load related indexes
compare expected entries
check required sections
check cross-references
check status values
check prohibited patterns
produce validation report
```

Do not specify vendor-specific CI configuration unless required by a later implementation task.

---

# 11. Expected Outputs

Define validation outputs.

Required output fields:

```text
validation_id
validation_name
target
source_files
status
severity
findings
passed_checks
failed_checks
warnings
critical_issues
recommended_actions
review_required
timestamp
validator
```

Allowed validation statuses:

```text
Passed
PassedWithWarnings
Failed
Blocked
NotRun
```

Use this output structure:

```text
Output Type:
    Validation Report

Output Format:
    Markdown / JSON / YAML / Test Report / Other

Required Output File:
    {path}
```

---

# 12. Failure Conditions

Define what causes validation failure.

Use this format:

| Failure Condition | Severity | Blocking | Notes |
|------------------|----------|----------|-------|
| {Condition} | Info / Warning / Error / Critical | Yes / No | {Notes} |

Common failure conditions:

```text
missing source reference
missing metadata
invalid status value
invalid MVP depth
unowned object
service without related objects
mutating service without event
event without source service
API without contract
Agent without Agent Contract
workflow without Workflow Contract
Codex task without source spec
reserved boundary production-enabled
26-domain baseline changed
```

---

# 13. Error Severity

Use controlled severity levels.

```text
Info
Warning
Error
Critical
```

## 13.1 Info

Non-blocking informational note.

## 13.2 Warning

Potential inconsistency requiring review but not necessarily blocking.

## 13.3 Error

Blocking issue for acceptance of the affected artifact.

## 13.4 Critical

Architecture-breaking, governance-breaking or release-blocking issue.

Critical examples:

```text
26-domain baseline changed
AI Agent without Agent Contract
Codex task without source specification
mutating service without event
reserved boundary production-enabled
Core meaning defined by API or UI
```

---

# 14. Review and Escalation Rules

Define review and escalation rules.

Use this structure:

```text
Info:
    action:
    owner:

Warning:
    action:
    owner:

Error:
    action:
    owner:
    acceptance impact:

Critical:
    action:
    owner:
    release impact:
```

Critical findings must not be bypassed by Codex.

---

# 15. Audit and Reporting Rules

Define audit and reporting requirements.

```text
Audit Required: Yes / No

Audit Trigger:
- ...

Audit Object:
- Validation Report
- Review Record
- Approval Record
- Codex Task Record

Reporting Required: Yes / No

Report Consumer:
- Editorial Review
- Architecture Review
- Codex Task Review
- Release Gate
- Implementation Team
```

Validation reports should be stored or referenced by the related Codex task or release gate.

---

# 16. Fixture Requirements

Define fixture requirements.

```text
Fixtures Required: Yes / No
```

If fixtures are required, list them.

```text
Required Fixtures:
- ...
- ...
```

Fixture rules:

```text
[ ] Fixtures contain no sensitive production data.
[ ] Fixtures match source specs.
[ ] Fixtures include minimum valid cases.
[ ] Fixtures include invalid cases.
[ ] Fixtures are deterministic.
```

If no fixture is required, state:

```text
This validation does not require fixtures because ...
```

---

# 17. Codex Usage

Define how Codex may use this validation.

Codex may:

```text
generate validation scripts
generate test fixtures
check source references
check metadata
check ownership
check mappings
check contracts
check prohibited overreach
produce validation reports
```

Codex must not:

```text
define new architecture
change domain baseline
invent missing specs
auto-approve high-risk changes
ignore failed validation
implement deferred scope
```

Related Codex Tasks:

```text
- B02-CX-W{wave}-{sequence} — {Task Title}
```

---

# 18. Release Gate Usage

Define whether this validation is part of a release gate.

```text
Release Gate Usage:
    none / Wave 0 Gate / Wave 1 Gate / Wave 2 Gate / Wave 3 Gate / Wave 4 Gate / Wave 5 Gate / Wave 6 Gate / Wave 7 Gate / Release Candidate Gate
```

Gate behavior:

```text
Blocks Release: Yes / No
Blocks Codex Acceptance: Yes / No
Blocks Implementation: Yes / No
Blocks Publication: Yes / No
```

State what happens if validation fails.

---

# 19. MVP Scope

Define MVP scope.

```text
MVP includes:
- ...
- ...
```

## 19.1 MVP Phase or Wave

```text
Phase/Wave: {Phase or Wave}
```

## 19.2 MVP Depth

```text
Depth: Must Implement | Partial Implement | Reserved Boundary | Deferred
```

## 19.3 MVP Acceptance Summary

```text
MVP acceptance requires:
- ...
- ...
```

---

# 20. Deferred Scope

Define explicitly deferred scope.

```text
Deferred:
- ...
- ...
```

Deferred validation must not be treated as required for MVP unless a later approved task changes scope.

---

# 21. Data and Implementation Notes

Provide implementation-facing notes without defining vendor-specific infrastructure.

Allowed notes:

```text
validation should be deterministic
validation should produce structured report
validation should support line-based findings when possible
validation should fail closed for Critical issues
validation should distinguish warning from blocking error
validation should not require production data
validation should run before Codex acceptance
```

Prohibited notes:

```text
vendor-specific CI configuration
physical database schema
production monitoring design
UI test automation details
unreviewed auto-fix behavior
```

---

# 22. Prohibited Overreach

This validation spec must not be used to:

```text
define Core meaning through validation rules
silently change the 26-domain baseline
treat Capability or Business Responsibility as ordinary domains
allow Codex to invent architecture
allow source-less implementation
allow unowned objects
allow services without events when mutating
allow APIs without contracts
allow Agents without Agent Contracts
allow AI outputs without review and audit
allow reserved scope to become MVP
turn validation into product QA only
require production data for validation
auto-approve Critical findings
```

Add validation-specific prohibited overreach:

```text
- ...
- ...
```

---

# 23. Acceptance Criteria

This Validation Specification is accepted only if:

```text
[ ] It defines validation purpose.
[ ] It defines validation meaning.
[ ] It identifies validation category.
[ ] It defines validation target.
[ ] It lists source references.
[ ] It defines scope.
[ ] It defines boundary.
[ ] It defines validation inputs.
[ ] It defines validation rules.
[ ] It defines validation procedure.
[ ] It defines expected outputs.
[ ] It defines failure conditions.
[ ] It defines error severity.
[ ] It defines review and escalation rules.
[ ] It defines audit and reporting rules.
[ ] It defines fixture requirements or explicit no-fixture reason.
[ ] It defines Codex usage.
[ ] It defines release gate usage.
[ ] It defines MVP scope.
[ ] It defines deferred scope.
[ ] It includes data and implementation notes.
[ ] It defines prohibited overreach.
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial validation specification created from B02-TPL-VALIDATION. |

---

**End of Validation Specification**
