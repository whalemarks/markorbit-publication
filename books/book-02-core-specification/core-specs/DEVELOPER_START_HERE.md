# Developer Start Here

**Spec ID:** B02-DEVELOPER-START-HERE  
**Spec Type:** Developer Entry Guide  
**Spec File:** core-specs/DEVELOPER_START_HERE.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Review:** core-specs/reviews/book-02-core-review.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Codex Governance:** core-specs/codex/CODEX-TASK-INDEX.md  
**Status:** Draft  
**Version:** 0.1.0  
**Guide Version:** v0.1.0  
**MVP Phase:** Phase 0–1 — Developer and Codex Entry  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file is the required starting point for any developer or Codex task working on Book 02 — MarkOrbit Core Specification.

It explains:

```text
what MarkOrbit Core is
what must be read first
what must be implemented first
what must not be changed
how to avoid architecture drift
how to run implementation work safely
how to summarize completed work
```

This file exists because Book 02 is large. Developers and Codex must not start from random files or implement from assumptions.

---

# 2. Core Lock

```text
Developers implement traced Core specifications.
Codex implements traced Core specifications.
Developers and Codex do not define architecture.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
Owning services own behavior.
Permission and Policy govern protected actions.
AI remains bounded by Agent Governance.
Events preserve trace.
Tests prevent architecture drift.
```

---

# 3. One-Minute Architecture Summary

MarkOrbit Core is not a single trademark application product.

It is the professional operating kernel for trademark and international IP service execution.

Canonical flow:

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

Implementation flow:

```text
Domains define responsibility areas.
Objects describe state.
Services own behavior.
API Contracts expose governed access.
Workflow Contracts constrain execution.
Workflows coordinate Services.
Agents assist within boundaries.
Events preserve trace.
Tests verify behavior.
Codex implements the specs.
```

Core principle:

```text
Contracts constrain.
Services implement.
Workflows coordinate.
Tests verify.
Products consume.
```

---

# 4. Required Reading Order

Before implementing anything, read these files in order.

## 4.1 Required Architecture Entry

```text
core-specs/reviews/book-02-core-review.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
```

## 4.2 Required Contract Entry

```text
core-specs/contracts/README.md
core-specs/contracts/index.md
core-specs/contracts/MANIFEST.md
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
```

## 4.3 Required Implementation Entry

```text
core-specs/codex/CODEX-TASK-INDEX.md
codex-tasks/README.md
codex-tasks/_template.md
```

If the Codex Task Index does not exist yet, create it before starting implementation tasks.

---

# 5. What To Build First

The first implementation target is not the full platform.

The first target is the MVP execution spine:

```text
Customer
↓
Brand / Trademark
↓
Matter / Order
↓
Document / Evidence
↓
Workflow Contract
↓
Task
↓
Communication
↓
Event
↓
Permission / Policy
↓
Tests
```

Required first capabilities:

```text
Reference Contract
Error Contract
Permission Context
Policy Context
Idempotency
Audit Context
Versioning
Common Contract Tests
Permission Policy Tests
Idempotency Event Tests
Error Versioning Tests
API Validator Scaffold
Workflow Validator Scaffold
Agent Boundary Tests
```

---

# 6. What Not To Build First

Do not start with:

```text
full UI
full workflow engine
full policy engine
full agent runtime
external filing integration
payment execution
provider marketplace settlement
advanced analytics
large-scale service network optimization
production notification integrations
public open API portal
```

These are future phases, not MVP Core foundation.

---

# 7. Must Build Now

Follow:

```text
core-specs/implementation/mvp-cut-v0.1.md
```

Must Build Now domains:

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

Must Build Now workflows:

```text
Customer Intake Workflow
Trademark Application Workflow
Communication Review Workflow
```

Must Build Now tests:

```text
Common Contract Tests
API Contract Tests for MVP APIs
Workflow Contract Tests for MVP workflows
Agent Boundary Tests for MVP agents
Permission Policy Tests
Idempotency Event Tests
Error Versioning Tests
```

---

# 8. Stub Now

The following should exist only as safe interfaces, placeholders or validation hooks in MVP:

```text
Knowledge
Notification
Opportunity
Partner
Agent
Service Provider
Service Network
Routing
Office Action Response Workflow
Provider Routing Workflow
Renewal Workflow
Assignment Workflow
Evidence Review Workflow
Routing Agent
full Agent Registry runtime
```

Stub rules:

```text
- Validate shape.
- Validate references.
- Return safe errors.
- Preserve Permission and Policy hooks.
- Do not fake production behavior.
- Do not create hidden side effects.
```

---

# 9. Document Only / Defer

Document-only or deferred items must not be implemented unless a later task explicitly moves them into scope.

Document Only:

```text
full policy engine
full agent runtime orchestration
full workflow engine
external official filing integrations
foreign associate live network integrations
provider marketplace settlement
advanced analytics
multi-product app marketplace
public developer API portal
```

Defer:

```text
renewal production workflow
assignment production workflow
office action response production workflow
evidence review production workflow
provider routing production workflow
foreign agent onboarding automation
partner-facing mini program
client self-service filing portal
billing and invoice automation
external storage integrations
communication delivery integrations
```

---

# 10. Never Implement in MVP

The following are architecture violations in MVP:

```text
AI submitting official filings
AI certifying legal deadlines
AI certifying trademark registrability
AI deciding evidence sufficiency as professional truth
AI selecting service provider as final decision
AI sending external communication without human review
API layer mutating domain state directly
Workflow layer creating active Tasks outside Task Service
Workflow layer emitting domain Events directly
Agent layer emitting Events directly
Event references triggering commands
Permission bypass for convenience
Policy bypass for convenience
production data fixtures
raw database IDs in public responses
unsafe stack traces in API responses
silent unsupported-version acceptance
silent historical-version rewriting
```

---

# 11. Ownership Rules

Always preserve these ownership rules:

```text
Identity Service owns Identity behavior.
Organization Service owns Organization behavior.
User Service owns User behavior.
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Customer Service owns Customer behavior.
Brand Service owns Brand behavior.
Trademark Service owns Trademark behavior.
Jurisdiction Service owns Jurisdiction behavior.
Classification Service owns Classification behavior.
Document Service owns Document behavior.
Evidence Service owns Evidence behavior.
Matter Service owns Matter behavior.
Order Service owns Order behavior.
Workflow Contract Service owns workflow preview/apply behavior.
Task Service owns active Task creation.
Event Service owns Event retrieval and event record behavior.
Communication Service owns Communication behavior.
Agent Service owns agent identity and capability registry behavior.
```

Rules:

```text
API layer routes.
Workflow layer coordinates.
Agent layer prepares.
Owning Service mutates.
Event preserves trace.
```

---

# 12. Permission / Policy Rules

Every protected action must check Permission.

Every policy-controlled action or output must check Policy.

Canonical rule:

```text
Permission approval is not Policy approval.
Policy allowance is not Permission approval.
Unknown Permission fails closed.
Unknown Policy fails closed for policy-controlled behavior.
```

Do not implement:

```text
temporary permission bypass
admin bypass without policy
policy disabled by default
mock permission that always allows without test assertion
mock policy that always allows without test assertion
```

---

# 13. AI Rules

AI may:

```text
summarize
draft
classify
compare
suggest
identify gaps
prepare task plan
prepare communication draft
prepare workflow preview explanation
summarize audit trace
```

AI must not:

```text
approve
send
select
submit
certify
complete
mutate protected state
emit events
```

Any AI-assisted output must preserve:

```text
AI Context
source scope
capability scope
policy omissions
human review requirement where applicable
```

---

# 14. Human Review Rules

Human Review is required for protected professional or external-facing actions.

Examples:

```text
customer-facing communication
external communication
classification recommendation finalization
evidence sufficiency conclusion
provider selection
workflow apply where protected
filing readiness confirmation
deadline confirmation
```

Core rule:

```text
Human Review records accountable review.
Human Review does not execute downstream action by itself.
Owning services decide whether review satisfies action requirements.
```

---

# 15. Idempotency / Event Rules

Duplicate-sensitive operations require:

```text
idempotency_key
```

Required behavior:

```text
same key + same semantic request = safe replay
same key + different semantic request = IdempotencyConflict
replay creates no duplicate objects
replay creates no duplicate Tasks
replay creates no duplicate Communications
replay creates no duplicate Events
```

Event rules:

```text
Events are trace, not commands.
Events are emitted only by owning services.
API layer must not emit Events directly.
Workflow layer must not emit Events directly.
Agent layer must not emit Events directly.
Event visibility follows Policy.
```

---

# 16. Error / Versioning Rules

Errors must be safe.

Errors must not expose:

```text
database IDs
stack traces
restricted data
policy internals
permission internals
prompt internals
hidden reasoning
secrets or tokens
```

Versioning rules:

```text
contract_version is required
schema_version is required where applicable
unsupported versions fail closed
historical versions must not be silently rewritten
```

---

# 17. Test Rules

Every implementation task must include tests or explain why tests are not applicable.

Required test categories:

```text
positive path tests
negative path tests
invalid reference tests
PermissionDenied tests
PolicyRestricted tests
redaction tests
AI forbidden-action tests
HumanReviewRequired tests
idempotency replay tests
idempotency conflict tests
event ownership tests
event reference not command tests
safe error tests
VersionUnsupported tests
```

Do not accept implementation that only has happy-path tests.

---

# 18. Codex Task Rules

Each Codex task must include:

```text
task purpose
source files read
scope
out of scope
files to modify
implementation steps
required tests
forbidden shortcuts
acceptance criteria
final summary format
```

Codex must not:

```text
create architecture
rename Core concepts casually
invent new ownership boundaries
skip source specs
implement untraced behavior
deepen implementation depth without approval
```

---

# 19. Recommended First Task Sequence

```text
TASK-001-common-contract-foundation
TASK-002-contract-fixture-system
TASK-003-common-contract-tests
TASK-004-permission-policy-hooks
TASK-005-idempotency-event-trace
TASK-006-error-versioning-validation
TASK-007-api-validator-scaffold
TASK-008-workflow-validator-scaffold
TASK-009-agent-boundary-tests
TASK-010-mvp-execution-spine
```

Do not start MVP business behavior before the core contract and test foundation exists.

---

# 20. Developer Pull Request Checklist

Before opening a PR or submitting a Codex task result:

```text
[ ] Source specs were read and cited.
[ ] Implementation matches TRACEABILITY.md.
[ ] Implementation matches mvp-cut-v0.1.md.
[ ] Implementation matches implementation-depth-matrix.md.
[ ] No new architecture boundary was invented.
[ ] API layer does not mutate domain state directly.
[ ] Workflow layer does not create active Tasks directly.
[ ] API / Workflow / Agent layers do not emit Events directly.
[ ] Permission and Policy fail closed.
[ ] AI forbidden actions are blocked.
[ ] Human Review gates are preserved.
[ ] Idempotency replay/conflict is handled where required.
[ ] Errors are safe.
[ ] Unsupported versions fail closed.
[ ] Tests include negative cases.
[ ] No production data fixtures are used.
```

---

# 21. Required Final Summary Format

Every Codex or developer task should end with:

```text
Summary
- What was implemented.
- Which specs were used.
- Which files changed.
- Which behavior is real enforcement.
- Which behavior remains stubbed.

Tests
- Commands run.
- Results.

Boundary Confirmation
- Permission/Policy fail closed.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Idempotency replay/conflict verified.
- Events are trace, not commands.
- Errors are safe.
- Unsupported versions fail closed.

Deferred
- What remains out of scope.
- What should be implemented next.
```

---

# 22. Acceptance Criteria

This Developer Start Here guide is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It summarizes architecture.
[ ] It defines required reading order.
[ ] It defines what to build first.
[ ] It defines what not to build first.
[ ] It defines Must Build Now.
[ ] It defines Stub Now.
[ ] It defines Document Only / Defer.
[ ] It defines Never Implement in MVP.
[ ] It defines ownership rules.
[ ] It defines Permission / Policy rules.
[ ] It defines AI rules.
[ ] It defines Human Review rules.
[ ] It defines Idempotency / Event rules.
[ ] It defines Error / Versioning rules.
[ ] It defines Test rules.
[ ] It defines Codex task rules.
[ ] It defines first task sequence.
[ ] It defines PR checklist.
[ ] It defines required final summary format.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Developer Start Here guide. Defines entry reading order, architecture summary, MVP scope, ownership rules, governance rules, test rules, Codex task rules, PR checklist and summary format. |

---

**End of Developer Start Here**
