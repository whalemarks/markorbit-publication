# core-specs/validation/

**Repository:** `book-02-core`  
**Directory:** `core-specs/validation/`  
**Document:** `core-specs/validation/README.md`  
**Book:** Book 02 — MarkOrbit Core Specification  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Directory Purpose

The `core-specs/validation/` directory contains validation specifications for MarkOrbit Core.

Validation specifications define how Book 02 artifacts, appendices, indexes, `core-specs/`, `codex-tasks/`, and later implementation artifacts are checked for architectural consistency, source traceability, contract completeness, governance compliance and prohibited overreach.

This directory exists to make the Core Specification system executable and reviewable.

It does not create Core meaning.

It verifies that Core meaning is preserved.

Validation specifications may be consumed by:

```text
editorial review
architecture review
Codex tasks
test suites
release checks
implementation gates
CI validation scripts
human acceptance reviews
```

---

# 2. Canonical Validation Rule

Book 02 uses the following canonical rule:

```text
Validation protects Core meaning.
Validation does not define Core meaning.
Validation must trace every implementation artifact back to approved specifications.
```

Therefore:

```text
No source trace, no acceptance.
No ownership validation, no Core Object.
No service-event validation, no executable Service.
No contract validation, no API or Agent execution.
No prohibited-overreach check, no Codex acceptance.
No release readiness check, no implementation release.
```

---

# 3. Validation Is Not Implementation

Validation is not automatically:

```text
feature implementation
product QA
UI testing
database testing
third-party integration testing
performance benchmarking
production monitoring
analytics reporting
```

Validation may later include technical tests, but this directory defines Core-level validation meaning first.

Implementation-specific tests must follow this layer.

---

# 4. Directory Boundary

## 4.1 validation/ Owns

This directory owns:

```text
Validation Specification files
validation purpose
validation scope
validation rules
source traceability checks
metadata checks
domain baseline checks
object ownership checks
service-object checks
service-event checks
event naming checks
event payload contract checks
contract completeness checks
API contract checks
agent contract checks
workflow contract checks
cross-cutting classification checks
Codex source reference checks
fixture requirements
prohibited-overreach checks
release readiness checks
acceptance gates
validation report requirements
```

## 4.2 validation/ Does Not Own

This directory does not own:

```text
Core Domain meaning
Core Object meaning
Core Service responsibility
Core Event semantics
API design
Agent behavior
Workflow state design
product QA strategy
physical infrastructure
production monitoring
implementation code
```

Those belong to other specification or implementation layers.

---

# 5. Source Chain

Every Validation Specification file must cite its source chain.

Required source chain:

```text
Book 02 manuscript
Appendices A–H
indexes/
core-specs/
codex-task-index.md
core-specs/validation/{validation-name}.md
codex-tasks/{task}.md
```

Key source files:

```text
B02-APP-A — Glossary
B02-APP-B — Core Domain Index
B02-APP-C — Core Object Index
B02-APP-D — Core Service Index
B02-APP-E — Event Index
B02-APP-F — API Index
B02-APP-G — Agent Index
B02-APP-H — Codex Task Index

indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/codex-task-index.md
```

---

# 6. Required Validation Spec Groups

Validation Specification files should be grouped by responsibility.

Expected directory structure:

```text
core-specs/validation/README.md
core-specs/validation/_template.md

core-specs/validation/repository/
core-specs/validation/metadata/
core-specs/validation/traceability/
core-specs/validation/domain/
core-specs/validation/object/
core-specs/validation/service/
core-specs/validation/event/
core-specs/validation/contract/
core-specs/validation/api/
core-specs/validation/agent/
core-specs/validation/workflow/
core-specs/validation/cross-cutting/
core-specs/validation/codex/
core-specs/validation/fixtures/
core-specs/validation/release/
```

Each subdirectory should contain validation specs for the corresponding category.

---

# 7. Validation Categories

This directory uses the following validation categories.

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

A validation spec must use one canonical category.

---

# 8. Validation Spec Metadata

Each Validation Specification file must begin with metadata.

```text
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
**MVP Phase/Wave:** Wave 0–7
**MVP Depth:** Must Implement | Partial Implement | Reserved Boundary | Deferred
**Owner:** MarkOrbit Publications Editorial Board
```

---

# 9. Validation Spec Required Sections

Every Validation Specification must include the following sections.

```text
1. Purpose
2. Validation Meaning
3. Validation Category
4. Validation Target
5. Source References
6. Scope
7. Boundary
8. Validation Inputs
9. Validation Rules
10. Validation Procedure
11. Expected Outputs
12. Failure Conditions
13. Error Severity
14. Review and Escalation Rules
15. Audit and Reporting Rules
16. Fixture Requirements
17. Codex Usage
18. Release Gate Usage
19. MVP Scope
20. Deferred Scope
21. Data and Implementation Notes
22. Prohibited Overreach
23. Acceptance Criteria
24. Revision Notes
```

---

# 10. Validation Target Rules

Every validation spec must define the target.

Allowed validation targets include:

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

Validation target must be specific enough to test.

---

# 11. Source Traceability Rules

Every implementation-relevant artifact must trace to approved sources.

Required trace chain:

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

Validation must fail when:

```text
source chapter is missing
source appendix is missing
source index is missing
core-spec is missing
Codex task lacks source reference
implementation artifact is not task-bound
test does not reference expected output
acceptance criteria are missing
```

---

# 12. Repository Validation Rules

Repository validation checks the expected repository structure.

Required top-level files and directories:

```text
README.md
publication.yaml
CHANGELOG.md
editorial/
planning/
manuscript/
appendices/
indexes/
core-specs/
codex-tasks/
releases/
```

Required `core-specs/` directories:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
core-specs/cross-cutting/
core-specs/validation/
```

Required `codex-tasks/` directories:

```text
codex-tasks/wave-0/
codex-tasks/wave-1/
codex-tasks/wave-2/
codex-tasks/wave-3/
codex-tasks/wave-4/
codex-tasks/wave-5/
codex-tasks/wave-6/
codex-tasks/wave-7/
```

---

# 13. Metadata Validation Rules

Metadata validation checks whether files identify themselves correctly.

Metadata checks should include:

```text
document ID
spec ID
spec type
title
source chapter
source appendix or index
status
version
owner
MVP phase or wave
MVP depth
related files
revision notes
```

Metadata validation must fail when:

```text
required metadata is missing
file status is invalid
version format is invalid
source reference is missing
MVP depth is missing
spec type does not match directory
file path conflicts with metadata
```

---

# 14. Domain Validation Rules

Domain validation protects the 26-domain baseline.

Required checks:

```text
[ ] Baseline Core Domain count equals 26.
[ ] Foundation Domains count equals 6.
[ ] Professional Domains count equals 6.
[ ] Business Execution Domains count equals 8.
[ ] Collaboration Network Domains count equals 6.
[ ] Capability is not counted as a baseline Core Domain.
[ ] Business Responsibility is not counted as a baseline Core Domain.
[ ] Every domain spec references indexes/domain-index.md.
[ ] Every domain spec has category, MVP phase and MVP depth.
[ ] Every domain spec lists objects, services, events and contracts.
[ ] Reserved domains are not production-enabled in MVP.
```

Validation must fail when a task or spec silently adds, removes, renames, merges or splits baseline domains.

---

# 15. Object Validation Rules

Object validation protects ownership and meaning.

Required checks:

```text
[ ] Every object has one owning domain or explicit cross-cutting system.
[ ] Every object has professional meaning.
[ ] Every object has lifecycle or explicit limited lifecycle.
[ ] Every operational object has state model or explicit no-state reason.
[ ] Every object lists related services.
[ ] Every object lists related events or explicit no-event reason.
[ ] Every object lists related contracts.
[ ] AI objects define review and audit requirements.
[ ] Codex objects define source specification requirements.
[ ] No object is only a database table.
[ ] No object is only a UI component.
```

Validation must fail for unowned objects.

---

# 16. Service Validation Rules

Service validation protects governed capability.

Required checks:

```text
[ ] Every service has an owning domain or explicit cross-cutting system.
[ ] Every service has Core responsibility.
[ ] Every service defines inputs.
[ ] Every service defines outputs.
[ ] Every service lists objects read or explicit no-read reason.
[ ] Every service lists objects created or updated or explicit no-mutation reason.
[ ] Every mutating service emits events or states explicit no-event reason.
[ ] Every service lists required contracts.
[ ] Every service defines permission rules.
[ ] Policy-sensitive services define policy rules.
[ ] High-risk services define review rules.
[ ] AI-assisted services define Agent Contract and audit requirements.
[ ] Every service defines failure behavior.
[ ] Mutating services define idempotency and safety rules.
[ ] No service is only a UI action.
[ ] No service is only a database operation.
```

---

# 17. Event Validation Rules

Event validation protects event meaning and traceability.

Required checks:

```text
[ ] Every event has meaningful past-tense name.
[ ] Every event has source domain or system.
[ ] Every event has source service or explicit governed external source.
[ ] Every event has trigger.
[ ] Every event has payload contract reference.
[ ] Every event lists related objects.
[ ] Every event lists consumer domains or services.
[ ] AI events define Agent Contract and audit requirements.
[ ] Workflow events reference workflow-related objects.
[ ] High-risk events define review or audit rules.
[ ] Every event defines retention requirement.
[ ] No event is only a log.
[ ] No event is only a UI click.
[ ] No event is only an analytics ping.
```

---

# 18. Contract Validation Rules

Contract validation protects integration and automation safety.

Required checks:

```text
[ ] Every contract has category.
[ ] Every contract has owner.
[ ] Every contract cites source specs.
[ ] Every contract defines participants.
[ ] Every contract defines fields and meaning.
[ ] Every contract defines validation rules.
[ ] Every applicable contract defines permission, policy, review and audit rules.
[ ] Every event contract references event spec.
[ ] Every service contract references service spec.
[ ] Every API contract references API and service specs.
[ ] Every agent contract references agent spec.
[ ] Every workflow contract references workflow spec.
[ ] Every Codex task contract defines source references and prohibited overreach.
[ ] Every contract defines versioning and compatibility.
[ ] No contract silently defines new Core meaning.
```

---

# 19. API Validation Rules

API validation protects consumption boundaries.

Required checks:

```text
[ ] Every API has owning service.
[ ] Every API has exposure level.
[ ] Every API has consumer classification.
[ ] Every API has input contract reference.
[ ] Every API has output contract reference.
[ ] Every API defines permission rules.
[ ] Policy-sensitive APIs define policy rules.
[ ] High-risk APIs define review and audit rules.
[ ] Mutating APIs define event side effects.
[ ] Agent APIs reference Agent Contract rules.
[ ] APIs define error contract rules.
[ ] APIs define rate and safety constraints.
[ ] APIs define versioning and compatibility.
[ ] No API defines Core meaning.
[ ] No API bypasses Core Services.
[ ] Reserved APIs are not production-enabled in MVP.
```

---

# 20. Agent Validation Rules

Agent validation protects AI governance.

Required checks:

```text
[ ] Every agent has Agent Identity.
[ ] Every agent has Agent Contract.
[ ] Every agent has owning domain or system.
[ ] Every agent has allowed capabilities.
[ ] Every agent has prohibited capabilities.
[ ] Every agent has authorized knowledge rules.
[ ] Every agent has object access rules.
[ ] Every agent has service access rules.
[ ] Every agent has event access rules.
[ ] Every agent has API access rules.
[ ] Every agent has risk level.
[ ] High-risk agents require human review.
[ ] Every AI Agent has audit requirement.
[ ] Agent outputs use controlled output statuses.
[ ] Reserved agents are not production-enabled in MVP.
[ ] No prompt is treated as an Agent.
[ ] AI does not replace professional responsibility.
```

---

# 21. Workflow Validation Rules

Workflow validation protects execution integrity.

Required checks:

```text
[ ] Every workflow has Workflow Contract reference.
[ ] Every workflow has state model.
[ ] Every workflow has transition rules.
[ ] Every transition invokes governed service.
[ ] Every workflow has task rules.
[ ] Review-sensitive workflows define review rules.
[ ] Approval-sensitive workflows define approval rules.
[ ] Every workflow defines responsibility rules.
[ ] Every workflow maps events.
[ ] Every workflow lists objects used.
[ ] AI-assisted workflows define Agent Contract and audit rules.
[ ] Workflows define failure behavior.
[ ] Workflows define idempotency and safety.
[ ] No workflow is only product UI flow.
[ ] No workflow bypasses Core Services.
[ ] Reserved workflows are not production-enabled in MVP.
```

---

# 22. Cross-Cutting Validation Rules

Cross-cutting validation protects classification integrity.

Required checks:

```text
[ ] Capability is classified as cross-cutting.
[ ] Business Responsibility is classified as cross-cutting.
[ ] Cross-cutting specs do not change the 26-domain baseline.
[ ] Cross-cutting specs list participating domains.
[ ] Cross-cutting specs list objects, services, events and contracts or explicit no-item reasons.
[ ] Cross-cutting specs define governance rules.
[ ] Cross-cutting specs define review and audit rules where applicable.
[ ] Cross-cutting specs define MVP and deferred scope.
```

Validation must fail when a cross-cutting system is silently promoted to an ordinary baseline Core Domain.

---

# 23. Codex Task Validation Rules

Codex task validation protects implementation control.

Required checks:

```text
[ ] Every Codex task has task ID.
[ ] Every task ID follows B02-CX-W{wave}-{sequence}.
[ ] Every task has wave and package.
[ ] Every task has source specifications.
[ ] Every task has dependencies or explicit no-dependency reason.
[ ] Every task has expected outputs.
[ ] Every task has test requirements.
[ ] Every task has fixture requirements or explicit no-fixture reason.
[ ] Every task has prohibited-overreach rules.
[ ] Every task has acceptance criteria.
[ ] No task changes Core architecture.
[ ] No task invents domains, objects, services, events, APIs or agents.
[ ] No task implements deferred scope without approval.
```

---

# 24. Fixture Validation Rules

Fixtures validate implementation behavior without production data.

Fixture validation must check:

```text
[ ] Fixtures contain no sensitive production data.
[ ] Fixtures match source specs.
[ ] Fixtures include minimum valid cases.
[ ] Fixtures include invalid cases.
[ ] Fixtures include permission failure cases where relevant.
[ ] Fixtures include policy failure cases where relevant.
[ ] Fixtures include review-required cases where relevant.
[ ] Fixtures include AI audit cases where relevant.
[ ] Fixtures include prohibited-overreach cases where relevant.
[ ] Fixtures are deterministic.
```

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

---

# 25. Prohibited Overreach Validation Rules

Prohibited-overreach validation checks that Codex and implementation do not exceed approved scope.

Required checks:

```text
[ ] No new baseline Core Domain is added.
[ ] No Core Domain is renamed, merged or split without architecture release.
[ ] No unowned Core Object is created.
[ ] No service is created without ownership and object relationship.
[ ] No mutating service lacks events.
[ ] No event is created without source service.
[ ] No API bypasses Core Services.
[ ] No Agent runs without Agent Contract.
[ ] No AI output bypasses review and audit.
[ ] No reserved boundary is production-enabled in MVP.
[ ] No product UI is implemented inside Core specs.
[ ] No physical database schema is treated as Core meaning.
[ ] No Codex task defines architecture.
```

---

# 26. Release Readiness Validation Rules

Release readiness validation checks whether the repository may move to implementation or release candidate.

Required checks:

```text
[ ] Appendices A–H are complete.
[ ] indexes/ is complete.
[ ] core-specs/ README files are complete.
[ ] core-specs/ templates are complete.
[ ] codex-task-index.md is complete.
[ ] codex-tasks/ scaffold exists.
[ ] Wave 0 tasks are generated.
[ ] Source traceability checks pass.
[ ] Metadata checks pass.
[ ] Domain baseline checks pass.
[ ] Object ownership checks pass.
[ ] Service-event checks pass.
[ ] Contract completeness checks pass.
[ ] API exposure checks pass.
[ ] Agent governance checks pass.
[ ] Workflow contract checks pass.
[ ] Prohibited-overreach checks pass.
[ ] Fixture strategy exists.
[ ] Test strategy exists.
[ ] Acceptance gate sequence exists.
```

---

# 27. Validation Severity Levels

Validation findings should use controlled severity levels.

```text
Info
Warning
Error
Critical
```

## Info

Non-blocking informational note.

## Warning

Potential inconsistency requiring review but not necessarily blocking.

## Error

Blocking issue for acceptance of the affected artifact.

## Critical

Architecture-breaking, governance-breaking or release-blocking issue.

Examples of Critical issues:

```text
26-domain baseline changed
AI Agent without Agent Contract
Codex task without source specification
mutating service without event
reserved boundary production-enabled
Core meaning defined by API or UI
```

---

# 28. Validation Output Requirements

Validation output should be structured.

Required fields:

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

Validation statuses:

```text
Passed
PassedWithWarnings
Failed
Blocked
NotRun
```

---

# 29. Review and Escalation Rules

Validation failures must be reviewed according to severity.

```text
Info:
    no escalation required

Warning:
    editorial or spec review recommended

Error:
    artifact cannot be accepted until fixed

Critical:
    architecture review required
    implementation or release blocked
```

Critical findings must not be bypassed by Codex.

---

# 30. Codex Usage Rules

Codex may use validation specs to:

```text
generate validation scripts
generate test fixtures
check source references
check metadata
check object ownership
check service-event mappings
check API contracts
check Agent Contracts
check workflow contracts
check prohibited overreach
produce validation reports
```

Codex must not use validation specs to:

```text
define new architecture
change domain baseline
invent missing specs
auto-approve high-risk changes
ignore failed validation
implement deferred scope
```

---

# 31. High-Priority Validation Specs

Initial validation specs should include:

```text
repository-structure-validation.md
publication-metadata-validation.md
source-traceability-validation.md
domain-baseline-validation.md
object-ownership-validation.md
service-event-mapping-validation.md
event-naming-validation.md
contract-completeness-validation.md
api-contract-validation.md
agent-contract-validation.md
workflow-contract-validation.md
cross-cutting-classification-validation.md
codex-task-source-validation.md
fixture-integrity-validation.md
prohibited-overreach-validation.md
release-readiness-validation.md
```

---

# 32. MVP Depth Rules

Validation specs must preserve MVP depth.

Allowed values:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

Core governance validation is generally `Must Implement`.

Advanced fixture or integration validation may be `Partial Implement` or `Deferred`.

---

# 33. Data and Implementation Notes

Validation specs may include implementation-facing notes.

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

# 34. Prohibited Behavior

This directory must not:

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

---

# 35. Acceptance Criteria

The `core-specs/validation/README.md` file is accepted when:

```text
[ ] It defines the purpose of core-specs/validation/.
[ ] It states validation protects Core meaning but does not define Core meaning.
[ ] It distinguishes validation from implementation and product QA.
[ ] It defines directory boundary.
[ ] It defines source chain requirements.
[ ] It defines required validation spec groups.
[ ] It defines validation categories.
[ ] It defines required metadata.
[ ] It defines required sections.
[ ] It defines validation target rules.
[ ] It defines source traceability rules.
[ ] It defines repository validation rules.
[ ] It defines metadata validation rules.
[ ] It defines domain validation rules.
[ ] It defines object validation rules.
[ ] It defines service validation rules.
[ ] It defines event validation rules.
[ ] It defines contract validation rules.
[ ] It defines API validation rules.
[ ] It defines agent validation rules.
[ ] It defines workflow validation rules.
[ ] It defines cross-cutting validation rules.
[ ] It defines Codex task validation rules.
[ ] It defines fixture validation rules.
[ ] It defines prohibited-overreach validation rules.
[ ] It defines release readiness validation rules.
[ ] It defines validation severity levels.
[ ] It defines validation output requirements.
[ ] It defines review and escalation rules.
[ ] It defines Codex usage rules.
[ ] It lists high-priority validation specs.
[ ] It defines MVP depth rules.
[ ] It defines data and implementation notes.
[ ] It defines prohibited behavior.
```

---

# 36. Next Action

After this README is accepted, generate:

```text
core-specs/validation/_template.md
```

Do not generate detailed validation specs before the template exists.

---

# 37. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial README for core-specs/validation/. Defines directory purpose, validation categories, source traceability, repository/metadata/domain/object/service/event/contract/API/agent/workflow/cross-cutting/Codex/fixture/release validation rules, severity levels and template handoff. |

---

**End of README**


# PUB-TASK-B02-003 Status/Workflow Contract Fixture Coverage

Contract Layer Map additions: `contracts/status/`, `contracts/fixtures/status-workflow/`, and `contracts/workflows/components/`. Traceability: Controlled State Value Specification -> Status Contract -> API Contract -> Fixture -> Validator -> future typed implementation. Workflow Component Specification -> Workflow Component Contract -> Workflow Contract/API Contract -> Fixture -> Validator -> future typed implementation.
