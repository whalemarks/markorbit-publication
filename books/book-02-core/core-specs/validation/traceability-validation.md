# Traceability Validation

**Spec ID:** B02-VALIDATION-TRACEABILITY  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/traceability-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Codex Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Level 2 — Required Mapping and Gap Validation  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate traceability across MarkOrbit Core.

Traceability validation checks whether each Core concept can be followed from architecture to implementation readiness:

```text
Domain
↓
Object
↓
Service
↓
API Contract
↓
Workflow Contract
↓
Workflow
↓
Event
↓
Agent Boundary
↓
Test Contract
↓
Codex Task
```

The goal is to ensure that Codex implementation does not start from isolated files, missing mappings or unowned behavior.

---

# 2. Core Lock

```text
Traceability connects Core layers.
Domains define responsibility areas.
Objects describe state.
Services own behavior.
API Contracts expose governed access.
Workflow Contracts constrain execution.
Workflows coordinate execution.
Events preserve trace.
Agents assist within governed boundaries.
Tests verify behavior.
Codex implements traced specifications.
Untraced behavior must not be implemented.
Missing traceability blocks MVP expansion where the item is Must Build Now.
```

---

# 3. Validation Scope

This validation checks traceability for:

```text
26 Core Domains
MVP Domains
Stub Domains
Domain Objects
Core Services
API Contracts
Workflow Contracts
Workflow Specs
Event Specs
Agent Specs
Common Contracts
Test Contracts
Codex Tasks
MVP Implementation Spine
```

This validation does not check:

```text
runtime code correctness
UI behavior
commercial workflow completeness
external official filing correctness
payment execution
production infrastructure
```

---

# 4. Required Source Files

Validation must inspect:

```text
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
core-specs/validation/architecture-consistency-validation.md
```

Validation should also inspect directories:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/agents/
core-specs/workflows/
core-specs/contracts/api/
core-specs/contracts/workflows/
core-specs/contracts/tests/
codex-tasks/
```

---

# 5. Traceability Principles

Traceability must follow these principles:

```text
Every Must Build Now domain must trace to object, service, API contract and tests.
Every protected behavior must trace to Permission and Policy.
Every duplicate-sensitive behavior must trace to Idempotency.
Every state-changing behavior must trace to Event trace.
Every AI-assisted behavior must trace to Agent Governance and AI Context.
Every external-facing or professional action must trace to Human Review.
Every API must trace to an owning service.
Every workflow must trace to workflow contract and owning services.
Every Codex task must trace to source specs and acceptance criteria.
```

---

# 6. Baseline Domain Traceability

Validate the 26-domain baseline.

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
[ ] Each domain appears in TRACEABILITY.md.
[ ] Each domain has an implementation category in mvp-cut-v0.1.md.
[ ] Each domain has a depth classification in implementation-depth-matrix.md.
[ ] Each Must Build Now domain has an API Contract.
[ ] Each Must Build Now domain has or points to an owning Service.
[ ] Each Stub Now domain has safe stub expectations.
[ ] No unclassified domain appears in MVP tasks.
```

---

# 7. MVP Domain Traceability

Must Build Now domains require complete traceability.

| Domain | Required Trace |
|---|---|
| Identity | Domain → Object → Service → API Contract → Permission/Policy where protected → Tests |
| Organization | Domain → Object → Service → API Contract → Permission/Policy → Tests |
| User | Domain → Object → Service → API Contract → Permission/Policy → Tests |
| Permission | Domain → Object → Service → API Contract → Permission Context → Tests |
| Policy | Domain → Object → Service → API Contract → Policy Context → Tests |
| Customer | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Brand | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Trademark | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Jurisdiction | Domain → Object → Service → API Contract → Workflows → Tests |
| Classification | Domain → Object → Service → API Contract → Workflows → Human Review → Tests |
| Document | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Evidence | Domain → Object → Service → API Contract → Workflows → Human Review → Tests |
| Matter | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Order | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Workflow Contract | Domain → Object → Service → API Contract → Workflow Contracts → Tests |
| Task | Domain → Object → Service → API Contract → Workflows → Events → Tests |
| Event | Domain → Object → Service → API Contract → Event Trace → Tests |
| Communication | Domain → Object → Service → API Contract → Communication Review Workflow → Human Review → Events → Tests |

Failure condition:

```text
Any Must Build Now domain with no API Contract, owning service or test contract mapping is Blocked.
```

---

# 8. Stub Domain Traceability

Stub Now domains do not require full implementation, but must have safe traceability.

Stub Now domains:

```text
Knowledge
Notification
Opportunity
Partner
Agent
Service Provider
Service Network
Routing
```

Required trace:

```text
domain
API contract or stub API contract
service owner or stub owner
safe not-implemented behavior
Permission/Policy hook where protected
tests or validation note
future implementation note
```

Failure condition:

```text
Stub domain silently behaves like production.
Stub domain has no owner.
Stub domain is used by MVP spine without safe boundary.
```

---

# 9. Object Traceability Checks

Validate:

```text
[ ] Every MVP object maps to exactly one primary owning service.
[ ] Every object uses public reference IDs.
[ ] No object exposes database IDs.
[ ] Every object with protected fields maps to Policy.
[ ] Every object with lifecycle change maps to Events.
[ ] Every object with AI-assisted output maps to AI Context.
[ ] Every object requiring professional accountability maps to Human Review.
```

Architecture violation:

```text
object owns behavior directly
object has no owning service
object exposes raw database ID as public identity
```

---

# 10. Service Traceability Checks

Validate:

```text
[ ] Every MVP service maps to one or more domains.
[ ] Every MVP service maps to API Contract where externally accessible.
[ ] Every MVP service maps to Event trace where it changes state.
[ ] Every protected service action maps to Permission and Policy.
[ ] Every duplicate-sensitive service action maps to Idempotency.
[ ] Every service failure maps to Error Contract.
[ ] Every service contract maps to Versioning where applicable.
```

Failure condition:

```text
state-changing service action has no Event trace
protected service action has no Permission/Policy trace
duplicate-sensitive service action has no Idempotency trace
```

---

# 11. API Contract Traceability Checks

Validate all 26 API Contracts.

Checks:

```text
[ ] Each API Contract maps to a domain.
[ ] Each API Contract maps to an owning service.
[ ] Each MVP API Contract maps to API validator task TASK-007.
[ ] Each protected API operation maps to Permission and Policy.
[ ] Each create/apply operation maps to Idempotency.
[ ] Each list/search operation maps to Pagination and Policy count behavior.
[ ] Each API failure maps to Error Contract.
[ ] Each API version maps to Versioning Contract.
[ ] Event API maps to Event trace and visibility rules.
```

Architecture violation:

```text
API Contract mutates domain state without owning service trace
API Contract emits Events directly
API Contract lacks Permission/Policy for protected action
```

---

# 12. Workflow Contract Traceability Checks

Validate workflow traceability for MVP and stub workflows.

MVP workflows:

```text
customer-intake-workflow
trademark-application-workflow
communication-review-workflow
```

Stub workflows:

```text
office-action-response-workflow
provider-routing-workflow
renewal-workflow
assignment-workflow
evidence-review-workflow
```

Checks:

```text
[ ] Each workflow spec maps to a workflow contract.
[ ] Each workflow contract maps to owning services.
[ ] Each MVP workflow maps to TASK-008 and TASK-010.
[ ] Each workflow preview maps to no-side-effect validation.
[ ] Each workflow apply maps to Idempotency.
[ ] Each workflow task plan maps to Task Service.
[ ] Each workflow event trace maps to Event Service.
[ ] Each AI-assisted workflow step maps to AI Context and Agent Governance.
[ ] Each protected workflow step maps to Permission/Policy.
[ ] Each professional/external-facing step maps to Human Review.
```

Architecture violation:

```text
workflow contract creates active Tasks directly
workflow contract emits Events directly
workflow contract permits AI final decision
workflow preview has side effects
```

---

# 13. Event Traceability Checks

Validate:

```text
[ ] Every state-changing MVP service action traces to Event Service.
[ ] Every Event spec maps to Event Object and Event API Contract.
[ ] Event references map to Reference Contract.
[ ] Event payload maps to Policy visibility rules.
[ ] Event failures map to Error Contract.
[ ] Event schema maps to Versioning Contract.
[ ] Event tests map to idempotency-event-tests.md.
```

Required event trace for MVP spine:

```text
customer-created
brand-created
trademark-created
matter-created
order-created
document-created
document-attached
evidence-created
workflow-contract-previewed
workflow-contract-applied
task-created
task-updated
communication-created
communication-reviewed
permission-evaluated
policy-evaluated
```

Failure condition:

```text
state change without trace
event trace without visibility policy
event reference treated as command
```

---

# 14. Agent Traceability Checks

Validate:

```text
[ ] Every Agent spec maps to Agent Governance.
[ ] Every Agent spec maps to AI Context.
[ ] Every Agent spec maps to Permission/Policy where it uses protected sources.
[ ] Every Agent spec maps to Human Review where output affects protected action.
[ ] Every Agent forbidden action maps to agent-boundary-tests.md.
[ ] Every Agent-related error maps to Error Contract.
```

Agent specs:

```text
ai-agent-governance
agent-registry
knowledge-agent
task-agent
communication-agent
workflow-agent
routing-agent
audit-agent
```

Failure condition:

```text
agent can approve/send/select/submit/certify/complete
agent output equals Human Review
agent identity implies Permission
agent capability implies Permission
agent emits Events
```

---

# 15. Common Contract Traceability Checks

Validate common contracts are used by all relevant layers.

Common Contracts:

```text
references
errors
pagination
audit-context
ai-context
human-review
permission-context
policy-context
idempotency
versioning
```

Checks:

```text
[ ] References used by API, Workflow, Event, Object and Tests.
[ ] Errors used by API, Workflow, Agent, Event and Tests.
[ ] Pagination used by list/search APIs.
[ ] Audit Context used by Event and Workflow trace.
[ ] AI Context used by Agent and AI-assisted workflow/API output.
[ ] Human Review used by protected professional/external-facing actions.
[ ] Permission Context used by protected actions.
[ ] Policy Context used by policy-controlled data/output.
[ ] Idempotency used by duplicate-sensitive create/apply operations.
[ ] Versioning used by contracts, events and records.
```

Failure condition:

```text
any common contract exists but is not referenced by consuming layers
protected behavior not traced to Permission/Policy
duplicate-sensitive operation not traced to Idempotency
```

---

# 16. Test Contract Traceability Checks

Validate:

```text
[ ] common-contract-tests.md maps to TASK-003.
[ ] api-contract-tests.md maps to TASK-007.
[ ] workflow-contract-tests.md maps to TASK-008.
[ ] agent-boundary-tests.md maps to TASK-009.
[ ] permission-policy-tests.md maps to TASK-004.
[ ] idempotency-event-tests.md maps to TASK-005.
[ ] error-versioning-tests.md maps to TASK-006.
[ ] MVP execution tests map to TASK-010.
```

Test coverage must include:

```text
positive cases
negative cases
PermissionDenied
PolicyRestricted
AI forbidden actions
HumanReviewRequired
IdempotencyConflict
VersionUnsupported
safe errors
event reference not command
```

Failure condition:

```text
Must Build Now behavior has no test trace
test exists but not linked to task
task exists but not linked to test contract
```

---

# 17. Codex Task Traceability Checks

Validate:

```text
[ ] TASK-001 maps to Common Contracts.
[ ] TASK-002 maps to Fixture System.
[ ] TASK-003 maps to Common Contract Tests.
[ ] TASK-004 maps to Permission/Policy.
[ ] TASK-005 maps to Idempotency/Event.
[ ] TASK-006 maps to Error/Versioning.
[ ] TASK-007 maps to API Validators.
[ ] TASK-008 maps to Workflow Validators.
[ ] TASK-009 maps to Agent Boundary Tests.
[ ] TASK-010 maps to MVP Execution Spine.
```

Each task must include:

```text
required source files
scope
out of scope
forbidden shortcuts
required tests
acceptance criteria
final summary format
```

Failure condition:

```text
task lacks required source mapping
task implements untraced behavior
task expands scope beyond MVP cut
```

---

# 18. MVP Spine Traceability Checks

Validate the MVP spine:

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

Checks:

```text
[ ] Customer traces to Customer Service and API Contract.
[ ] Brand/Trademark trace to owning services and API Contracts.
[ ] Matter/Order trace to owning services and API Contracts.
[ ] Document/Evidence trace to owning services and API Contracts.
[ ] Workflow Contract traces to workflow contracts and Workflow Contract Service.
[ ] Task traces to Task Service only for active task creation.
[ ] Communication traces to Communication Service.
[ ] Event trace routes through Event Service.
[ ] Permission/Policy trace applies to protected actions.
[ ] Tests trace the whole spine.
```

Failure condition:

```text
any spine step lacks owning service
workflow bypasses Task Service
workflow/API/agent bypasses Event Service
Permission/Policy missing from protected spine action
```

---

# 19. Validation Procedure

Perform validation in this order:

```text
1. Confirm required source files exist.
2. Confirm 26-domain baseline trace.
3. Confirm MVP domain trace.
4. Confirm Stub Now domain trace.
5. Confirm object-to-service trace.
6. Confirm service-to-contract trace.
7. Confirm API-to-service trace.
8. Confirm workflow-to-service trace.
9. Confirm event trace.
10. Confirm agent governance trace.
11. Confirm common contract consumption.
12. Confirm test contract trace.
13. Confirm Codex task trace.
14. Confirm MVP spine trace.
15. Classify findings.
16. Produce validation report.
```

---

# 20. Finding Classification

Use:

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
Blocked = required Must Build Now trace is missing.
Architecture Violation = trace shows boundary breach.
Warning = future/stub trace incomplete but not blocking.
Out of Scope = valid but beyond MVP.
Deferred = valid later-phase trace.
Pass = trace complete for current depth.
```

---

# 21. Required Evidence

Every finding must include:

```text
source file
missing or inconsistent trace
affected domain/service/contract/workflow/agent/task
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Customer API Contract has no owning service trace.
Status: Blocked
Affected Area: Customer / API / Service
MVP Category: Must Build Now
Required Fix: Add Customer Service mapping in TRACEABILITY.md and API validator source list.
Codex Impact: Block TASK-007 and TASK-010.
```

---

# 22. Architecture Violation Triggers

The following always fail validation:

```text
Untraced behavior implemented by Codex.
Must Build Now domain without owning service.
MVP API without owning service trace.
MVP workflow without workflow contract trace.
Protected behavior without Permission/Policy trace.
Duplicate-sensitive operation without Idempotency trace.
State-changing behavior without Event trace.
AI-assisted behavior without Agent Governance trace.
External-facing or professional action without Human Review trace.
API layer or Workflow layer directly emits Events.
Workflow layer directly creates active Tasks.
Agent mutates state or emits Events.
Event reference treated as command.
```

---

# 23. Acceptance Criteria

Traceability Validation passes only if:

```text
[ ] Required source files exist.
[ ] 26-domain baseline is traced.
[ ] Must Build Now domains have required trace.
[ ] Stub Now domains have safe stub trace.
[ ] MVP objects trace to owning services.
[ ] MVP services trace to API Contracts.
[ ] State-changing actions trace to Events.
[ ] Protected actions trace to Permission/Policy.
[ ] Duplicate-sensitive operations trace to Idempotency.
[ ] AI-assisted behavior traces to Agent Governance and AI Context.
[ ] Human Review gates are traced.
[ ] API Contracts trace to owning services.
[ ] Workflow specs trace to Workflow Contracts.
[ ] Workflow Contracts trace to owning services.
[ ] Test Contracts trace to Codex tasks.
[ ] TASK-001 through TASK-010 trace to source specs.
[ ] MVP spine trace is complete.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now areas.
```

---

# 24. Validation Report Template

```text
Validation: Traceability
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Book 02 Core Traceability

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- <file / mapping / section>

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 25. Codex Usage

Codex must use this validation:

```text
before implementing any new behavior
before implementing API validators
before implementing workflow validators
before implementing MVP execution spine
after modifying TRACEABILITY.md
after adding new task files
during PR review
```

Codex must not:

```text
implement untraced behavior
invent missing service owners
assume API behavior without contract trace
assume workflow behavior without workflow contract trace
expand MVP because trace is missing
treat validation as permission to change architecture
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Traceability Validation. Defines domain, object, service, API, workflow, event, agent, common contract, test contract, Codex task and MVP spine traceability checks, violation triggers, procedure and report template. |

---

**End of Traceability Validation**
