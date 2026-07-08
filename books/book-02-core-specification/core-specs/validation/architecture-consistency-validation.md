# Architecture Consistency Validation

**Spec ID:** B02-VALIDATION-ARCHITECTURE-CONSISTENCY  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/architecture-consistency-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Level 2 — Structural and Boundary Validation  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate the architectural consistency of Book 02 — MarkOrbit Core Specification.

It checks whether the Core architecture remains internally consistent across:

```text
principles
domains
objects
services
contracts
APIs
workflows
agents
events
tests
Codex tasks
MVP implementation scope
```

This validation exists to prevent architecture drift before Codex implementation expands.

---

# 2. Core Lock

```text
Architecture validation protects Core boundaries.
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
Domains define responsibility areas.
Objects describe state.
Services own behavior.
API Contracts expose governed access.
Workflow Contracts constrain execution.
Agents assist within governed capability boundaries.
Events preserve trace.
Tests verify behavior.
Codex implements traced specifications.
Codex does not define architecture.
```

---

# 3. Validation Scope

This validation checks:

```text
Core role consistency
layer responsibility consistency
domain classification consistency
object/service ownership consistency
contract boundary consistency
API/service boundary consistency
workflow/service boundary consistency
agent governance consistency
event trace consistency
Permission/Policy governance consistency
MVP scope consistency
Codex task consistency
```

This validation does not check:

```text
runtime performance
database schema performance
UI implementation
production infrastructure
commercial pricing
external filing integration correctness
foreign provider SLA
payment execution
```

---

# 4. Required Source Files

Validation must inspect the following files:

```text
core-specs/reviews/book-02-core-review.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/contracts/MANIFEST.md
core-specs/contracts/index.md
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
core-specs/validation/index.md
```

Validation should also inspect:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/agents/
core-specs/workflows/
codex-tasks/
```

---

# 5. Canonical Architecture Rules

The following rules must remain consistent everywhere.

## 5.1 Canonical Flow

```text
Principles define
↓
Core provides
↓
Business owns
↓
Workplace operates
↓
Network connects
↓
Applications deliver
```

## 5.2 Core Responsibility Rule

```text
Core provides primitives, contracts and governed execution boundaries.
Core does not own product-specific business experience.
Core does not own external marketplace execution.
Core does not replace professional judgment.
```

## 5.3 Implementation Responsibility Rule

```text
Contracts constrain.
Services implement.
Workflows coordinate.
Agents assist.
Events trace.
Tests verify.
Codex implements.
```

## 5.4 Service Ownership Rule

```text
Owning Services own behavior.
API layer routes and validates.
Workflow layer coordinates.
Agent layer prepares.
Task Service creates active Tasks.
Event Service records trace.
Communication Service owns Communication behavior.
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
```

---

# 6. Layer Consistency Checks

Validate that the following layers do not cross their responsibilities.

| Layer | Allowed | Not Allowed |
|---|---|---|
| Principles | Define direction and constraints | Implement behavior |
| Core | Provide primitives/contracts | Own product UI or marketplace operations |
| Domain | Define responsibility area | Execute workflows directly |
| Object | Describe state | Own behavior |
| Service | Own behavior | Bypass contracts/governance |
| API Contract | Govern access | Mutate domain state directly |
| Workflow Contract | Constrain workflow execution | Own domain behavior |
| Workflow | Coordinate services | Create active Tasks directly or emit Events directly |
| Agent | Prepare, draft, suggest, summarize | Approve, send, select, submit, certify, complete |
| Event | Preserve trace | Trigger commands |
| Test | Verify behavior | Redefine architecture |
| Codex Task | Implement scoped specs | Define architecture |

---

# 7. Domain Classification Consistency

Validate the 26 baseline Core Domains remain stable.

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

Checks:

```text
[ ] All 26 domains appear in TRACEABILITY.md.
[ ] All 26 domains appear in API Contract index or are intentionally documented.
[ ] Each domain has one owning service or explicitly documented stub owner.
[ ] No extra domain is introduced without architecture review.
[ ] Capability and Business Responsibility are treated as cross-cutting systems, not added to the 26-domain baseline.
[ ] Communication is counted once even if it appears in both execution and collaboration perspectives.
```

Failure conditions:

```text
new domain added without review
domain renamed casually
domain moved between categories without review
Capability added as a 27th domain
Business Responsibility added as a 28th domain
Communication double-counted
```

---

# 8. Object / Service Consistency Checks

Validate:

```text
[ ] Objects describe state.
[ ] Services own behavior.
[ ] Every MVP object has an owning service.
[ ] Every MVP service maps to at least one domain.
[ ] No object spec contains ungoverned service behavior.
[ ] No service bypasses Permission/Policy where protected.
[ ] No service emits unsafe Events.
[ ] No service exposes database IDs in public references.
```

Architecture violations:

```text
object mutates itself as active behavior
API owns business behavior
workflow owns domain behavior
agent owns domain behavior
service bypasses contracts
```

---

# 9. Contract Consistency Checks

Validate:

```text
[ ] Common Contracts are used by API, Workflow, Agent and tests.
[ ] API Contracts reference Common Contracts.
[ ] Workflow Contracts reference Common Contracts.
[ ] Test Contracts reference Common Contracts.
[ ] Error Contract applies to all failure paths.
[ ] Reference Contract hides database IDs.
[ ] Permission Context and Policy Context remain separate.
[ ] Idempotency Contract applies to duplicate-sensitive operations.
[ ] Versioning Contract applies to contracts and records.
```

Failure conditions:

```text
Permission and Policy merged into one vague access flag
errors represented as raw strings only
references represented by database IDs
workflow apply missing idempotency
unsupported version accepted silently
```

---

# 10. API Boundary Consistency Checks

Validate:

```text
[ ] API layer validates request and response shape.
[ ] API layer routes to owning service.
[ ] API layer does not mutate domain state directly.
[ ] API layer does not emit Events directly.
[ ] API layer does not create active Tasks directly.
[ ] API layer uses Permission and Policy hooks.
[ ] API layer uses safe errors.
[ ] API layer rejects unsupported versions.
```

Architecture violations:

```text
API creates Customer without Customer Service
API emits customer-created Event directly
API creates Task directly
API bypasses Permission/Policy
API accepts raw database ID as public reference
```

---

# 11. Workflow Boundary Consistency Checks

Validate:

```text
[ ] Workflow layer coordinates services.
[ ] Workflow layer does not own domain behavior.
[ ] Workflow preview has no side effects.
[ ] Workflow apply requires idempotency.
[ ] Workflow layer may prepare Task plans.
[ ] Active Tasks are created only by Task Service.
[ ] Workflow layer does not emit Events directly.
[ ] Workflow layer does not send Communications directly.
[ ] Workflow layer does not submit official filings.
[ ] Workflow layer does not certify professional truth.
```

Architecture violations:

```text
workflow creates active Task directly
workflow emits Event directly
workflow sends external communication
workflow certifies trademark registrability
workflow applies official filing
workflow treats preview as apply
```

---

# 12. Agent Governance Consistency Checks

Validate:

```text
[ ] AI enhances professionals.
[ ] AI does not define professional truth.
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] Agent output does not equal Human Review.
[ ] Agents may prepare, summarize, draft, suggest and compare.
[ ] Agents must not approve, send, select, submit, certify, complete, mutate protected state or emit Events.
[ ] AI output carries AI Context.
[ ] AI output preserves Policy omissions.
[ ] Human Review remains required for protected actions.
```

Architecture violations:

```text
AI approves filing readiness
AI sends customer communication
AI selects provider finally
AI submits official filing
AI certifies deadline
AI certifies registrability
AI creates or completes active Task
AI emits Event
```

---

# 13. Event Consistency Checks

Validate:

```text
[ ] Events preserve trace.
[ ] Events are not commands.
[ ] Event references do not trigger downstream actions.
[ ] Events are emitted only by owning services.
[ ] API layer does not emit Events directly.
[ ] Workflow layer does not emit Events directly.
[ ] Agent layer does not emit Events directly.
[ ] Event visibility follows Permission and Policy.
[ ] Event payloads are safe.
```

Architecture violations:

```text
event reference triggers task completion
event reference sends communication
event emitted by API layer
event emitted by workflow layer
event emitted by agent layer
restricted event payload leaks
```

---

# 14. Permission / Policy Consistency Checks

Validate:

```text
[ ] Permission and Policy are separate systems.
[ ] Permission approval does not imply Policy approval.
[ ] Policy allowance does not imply Permission approval.
[ ] Unknown Permission fails closed.
[ ] Unknown Policy fails closed for policy-controlled behavior.
[ ] PolicyRestrictedBlock blocks.
[ ] PolicyRestrictedRedact redacts and sets restricted_fields_omitted.
[ ] PolicyRequiresHumanReview preserves review gate.
[ ] PolicyNonDisclosureNotFound hides object existence where required.
```

Architecture violations:

```text
default Permission allowed
default Policy allowed
Permission/Policy collapsed into one boolean
redaction silently hides fields without disclosure
Human Review bypasses Permission
Human Review bypasses Policy
```

---

# 15. MVP Scope Consistency Checks

Validate that MVP implementation follows:

```text
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
```

Must Build Now:

```text
Identity
Organization
User
Permission
Policy
Customer
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Matter
Order
Workflow Contract
Task
Event
Communication
```

MVP workflows:

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Stub Now:

```text
Knowledge
Notification
Opportunity
Partner
Agent
Service Provider
Service Network
Routing
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

Architecture violations:

```text
full workflow engine implemented before MVP spine
full policy engine implemented before MVP spine
full agent runtime implemented before MVP spine
external filing integration implemented in MVP Core
payment execution implemented in MVP Core
provider marketplace settlement implemented in MVP Core
```

---

# 16. Codex Task Consistency Checks

Validate:

```text
[ ] Codex tasks follow CODEX-TASK-INDEX.md.
[ ] TASK-001 through TASK-010 exist.
[ ] Tasks cite source specs.
[ ] Tasks include scope and out-of-scope.
[ ] Tasks include forbidden shortcuts.
[ ] Tasks include acceptance criteria.
[ ] Tasks preserve MVP cut.
[ ] Tasks preserve implementation depth.
[ ] Tasks do not define new architecture.
```

Failure conditions:

```text
task lacks source files
task expands scope without approval
task implements deferred capability
task skips negative tests
task treats Codex as architect
```

---

# 17. Validation Procedure

Perform validation in this order:

```text
1. Verify required source files exist.
2. Verify canonical flow and Core responsibility language.
3. Verify 26-domain baseline.
4. Verify layer responsibilities.
5. Verify object/service ownership.
6. Verify contract boundaries.
7. Verify API boundary rules.
8. Verify workflow boundary rules.
9. Verify agent governance rules.
10. Verify event trace rules.
11. Verify Permission/Policy rules.
12. Verify MVP scope and implementation depth.
13. Verify Codex task consistency.
14. Classify findings.
15. Produce validation report.
```

---

# 18. Finding Classification

Use the following statuses:

```text
Pass
Warning
Blocked
Architecture Violation
Out of Scope
Deferred
```

Classification rules:

```text
Architecture Violation = boundary breach or unsafe governance.
Blocked = required MVP file/spec/test missing.
Warning = future or non-blocking inconsistency.
Out of Scope = valid but outside MVP.
Deferred = valid later-phase item.
Pass = no material issue.
```

---

# 19. Required Evidence

Each finding must include evidence:

```text
file path
section or heading where possible
affected layer
affected domain/service/contract/task
why it matters
required fix
Codex impact
```

Example:

```text
Finding: Workflow layer creates active Task directly.
Status: Architecture Violation
Evidence: <file path>
Affected Layer: Workflow / Task
Required Fix: Route active Task creation through Task Service.
Codex Impact: Block TASK-010 until fixed.
```

---

# 20. Architecture Violation Triggers

The following always fail validation:

```text
API layer mutates domain state directly.
API layer emits Events directly.
Workflow layer owns domain behavior.
Workflow layer creates active Tasks directly.
Workflow layer emits Events directly.
Agent layer mutates protected state.
Agent layer emits Events.
Agent sends external communication.
Agent selects provider finally.
Agent submits official filing.
Agent certifies deadlines.
Agent certifies registrability.
Agent certifies evidence sufficiency.
Permission defaults to allowed.
Policy defaults to allowed.
Unsupported version is silently accepted.
Raw database IDs appear in public responses.
Unsafe stack traces appear in errors.
Production data is used as fixtures.
Codex task defines architecture instead of implementing specs.
```

---

# 21. Acceptance Criteria

Architecture Consistency Validation passes only if:

```text
[ ] Required source files exist.
[ ] Canonical architecture flow is preserved.
[ ] Core responsibility boundary is preserved.
[ ] 26-domain baseline is preserved.
[ ] Layer responsibilities are preserved.
[ ] Object/service ownership is preserved.
[ ] Common/API/Workflow/Test Contract boundaries are preserved.
[ ] API layer routes to owning services and does not mutate directly.
[ ] Workflow layer coordinates and does not own behavior.
[ ] Workflow layer does not create active Tasks directly.
[ ] Workflow layer does not emit Events directly.
[ ] Agent boundaries are preserved.
[ ] Events remain trace, not commands.
[ ] Permission and Policy remain separate and fail closed.
[ ] MVP scope is respected.
[ ] Implementation depth is respected.
[ ] Codex tasks do not define architecture.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now areas.
```

---

# 22. Validation Report Template

```text
Validation: Architecture Consistency
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Book 02 Core Architecture

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- <file / section>

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 23. Codex Usage

Codex must use this validation:

```text
before starting implementation expansion
after generating new Core specs
after modifying Codex tasks
before implementing TASK-010 MVP Execution Spine
during PR review
```

Codex must not use this validation to:

```text
invent new domains
rename architecture layers
deepen implementation scope
bypass MVP cut
skip source specs
```

---

# 24. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Architecture Consistency Validation. Defines canonical architecture checks, layer/domain/object/service/API/workflow/agent/event/Permission/Policy/MVP/Codex consistency checks, violation triggers, procedure, evidence requirements and report template. |

---

**End of Architecture Consistency Validation**
