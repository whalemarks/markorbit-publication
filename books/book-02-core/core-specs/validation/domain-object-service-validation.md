# Domain Object Service Validation

**Spec ID:** B02-VALIDATION-DOMAIN-OBJECT-SERVICE  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/domain-object-service-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Level 2 — Ownership and Alignment Validation  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate alignment between Domains, Objects and Services in MarkOrbit Core.

It checks whether each Core domain has:

```text
clear responsibility
valid object model
single or clearly defined owning service
correct service behavior boundary
API and workflow traceability
Permission / Policy governance where protected
Event trace where state changes
Tests where MVP implementation is required
```

This validation prevents the most common Core implementation drift:

```text
objects owning behavior
services crossing domain ownership
API layer becoming the business layer
workflow layer becoming the service layer
agents mutating state
unowned MVP behavior
duplicate service ownership
```

---

# 2. Core Lock

```text
Domains define responsibility areas.
Objects describe state.
Services own behavior.
Objects do not execute business behavior.
API layer routes and validates.
Workflow layer coordinates services.
Agent layer prepares but does not mutate protected state.
Owning services mutate state.
Task Service creates active Tasks.
Event Service records trace.
Permission Service owns Permission evaluation.
Policy Service owns Policy evaluation.
Codex must preserve domain, object and service ownership.
```

---

# 3. Validation Scope

This validation covers:

```text
26 Core Domains
Domain category consistency
Domain responsibility boundaries
Object ownership
Object state fields
Service ownership
Service behavior boundaries
Service-to-API alignment
Service-to-workflow alignment
Service-to-event alignment
Service-to-test alignment
MVP Must Build Now coverage
Stub Now domain ownership
```

This validation does not cover:

```text
database physical schema optimization
ORM implementation style
UI component design
external integration behavior
production scalability
commercial workflow completeness
```

---

# 4. Required Source Files

Validation must inspect:

```text
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
```

Validation should also inspect:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/workflows/
core-specs/contracts/api/
core-specs/contracts/workflows/
codex-tasks/
```

---

# 5. Domain Baseline

Validate that the 26 baseline domains are preserved.

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
[ ] Domain name is stable.
[ ] Domain category is stable.
[ ] Domain responsibility is clear.
[ ] Domain does not duplicate another domain.
[ ] Domain maps to object(s) or explicitly documents why not.
[ ] Domain maps to owning service or explicit stub owner.
[ ] Domain maps to API Contract where externally accessible.
[ ] Domain maps to tests if Must Build Now.
```

Failure conditions:

```text
domain renamed casually
domain category changed without review
new domain added without review
Capability treated as domain
Business Responsibility treated as domain
Communication double-counted as two domains
```

---

# 6. Domain Responsibility Validation

Every domain must have a clear responsibility boundary.

Required checks:

```text
[ ] Domain responsibility can be stated in one sentence.
[ ] Domain responsibility does not overlap materially with another domain.
[ ] Domain ownership is not split across unrelated services.
[ ] Domain behavior is not hidden in API validators.
[ ] Domain behavior is not hidden in workflow validators.
[ ] Domain behavior is not hidden in agent code.
```

Examples:

```text
Customer owns customer/account relationship state.
Brand owns brand identity state.
Trademark owns trademark record state.
Matter owns professional execution context.
Order owns commercial/service order context.
Task owns active work item state.
Event owns trace record state.
Communication owns communication draft/review/send state.
```

Architecture violation:

```text
Workflow owns Customer behavior.
API owns Trademark behavior.
Agent owns Task completion behavior.
Object owns Order lifecycle behavior.
```

---

# 7. Object Validation Rules

Objects describe state.

Objects may include:

```text
reference IDs
status
attributes
relationships
timestamps
version fields
policy visibility metadata
audit context
AI context where applicable
human review metadata where applicable
```

Objects must not include:

```text
unguarded behavior execution
direct permission bypass
policy bypass
event emission behavior
workflow orchestration behavior
agent execution behavior
external integration calls
```

Checks:

```text
[ ] Object has public reference ID.
[ ] Object does not expose raw database ID publicly.
[ ] Object fields match domain responsibility.
[ ] Object lifecycle fields map to owning service behavior.
[ ] Object protected fields map to Policy.
[ ] Object state changes map to Events.
[ ] Object version fields are preserved where applicable.
```

Architecture violation:

```text
object method submits filing
object method sends communication
object method creates Event directly
object method completes Task directly
object exposes database ID as public reference
```

---

# 8. Service Validation Rules

Services own behavior.

Services may:

```text
validate domain invariants
mutate owned objects
coordinate with other services through explicit contracts
evaluate or call Permission/Policy hooks
create Events through Event Service or approved event integration
create active Tasks only if Task Service
create Communications only if Communication Service
return safe errors
preserve idempotency and versioning
```

Services must not:

```text
own another domain's behavior without explicit coordination
bypass API/Workflow/Common Contracts
bypass Permission or Policy
emit unsafe Events
expose raw database IDs
return unsafe errors
allow AI to decide protected actions
```

Checks:

```text
[ ] Service maps to domain.
[ ] Service owns defined behavior.
[ ] Service does not duplicate another service.
[ ] Service uses Permission/Policy where protected.
[ ] Service uses Idempotency where duplicate-sensitive.
[ ] Service records Event trace where state changes.
[ ] Service returns Error Contract failures.
[ ] Service preserves Versioning where applicable.
```

---

# 9. Owning Service Matrix

Validate the owning service baseline.

| Domain | Owning Service |
|---|---|
| Identity | Identity Service |
| Organization | Organization Service |
| User | User Service |
| Permission | Permission Service |
| Policy | Policy Service |
| Knowledge | Knowledge Service or safe stub owner |
| Brand | Brand Service |
| Trademark | Trademark Service |
| Jurisdiction | Jurisdiction Service |
| Classification | Classification Service |
| Document | Document Service |
| Evidence | Evidence Service |
| Customer | Customer Service |
| Matter | Matter Service |
| Order | Order Service |
| Opportunity | Opportunity Service or safe stub owner |
| Workflow Contract | Workflow Contract Service |
| Task | Task Service |
| Event | Event Service |
| Notification | Notification Service or safe stub owner |
| Partner | Partner Service or safe stub owner |
| Agent | Agent Service or Agent Registry Service |
| Service Provider | Service Provider Service or safe stub owner |
| Service Network | Service Network Service or safe stub owner |
| Routing | Routing Service or safe stub owner |
| Communication | Communication Service |

Failure conditions:

```text
Must Build Now domain has no owning service.
Two services claim primary ownership over the same domain without boundary.
Stub domain has no safe owner.
Service name exists but no behavior responsibility is defined.
```

---

# 10. MVP Must Build Now Validation

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

For each Must Build Now domain, validate:

```text
[ ] Domain exists.
[ ] Object spec exists or is explicitly represented in TRACEABILITY.md.
[ ] Service spec exists or owning service is explicitly defined.
[ ] API Contract exists.
[ ] Test Contract mapping exists.
[ ] Implementation depth is defined.
[ ] Permission/Policy is mapped where protected.
[ ] Idempotency is mapped where duplicate-sensitive.
[ ] Event trace is mapped where state-changing.
[ ] Error/Versioning is mapped.
```

Blocked if:

```text
MVP domain lacks owning service.
MVP domain lacks API Contract.
MVP domain lacks test mapping.
MVP state-changing domain lacks Event trace.
MVP protected domain lacks Permission/Policy trace.
```

---

# 11. Stub Now Domain Validation

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

For each Stub Now domain, validate:

```text
[ ] Domain exists.
[ ] Safe owner or stub owner exists.
[ ] API Contract or stub API Contract exists.
[ ] Production behavior is not implied.
[ ] NotImplemented / preview-only / validation-only behavior is explicit.
[ ] Permission/Policy hooks are preserved where protected.
[ ] Future implementation note exists.
```

Architecture violation:

```text
stub domain performs production behavior
stub routing selects provider finally
stub notification sends real messages
stub knowledge certifies professional truth
stub agent runtime executes protected actions
```

---

# 12. Cross-Domain Relationship Validation

Validate relationships are explicit and do not create ownership ambiguity.

Expected relationships:

```text
Customer may relate to Brand, Matter, Order, Communication.
Brand may relate to Trademark.
Trademark may relate to Jurisdiction, Classification, Document, Evidence, Matter.
Matter may relate to Customer, Trademark, Order, Task, Communication.
Order may relate to Customer, Matter and service scope.
Document may relate to Trademark, Matter, Evidence or Communication.
Evidence may relate to Trademark, Document or Matter.
Workflow Contract may relate to Workflow, Task plan and Event trace.
Task may relate to Matter, Trademark, Communication or Workflow Contract.
Communication may relate to Customer, Matter, Order or Trademark.
Event may relate to any subject reference but does not own the subject.
```

Checks:

```text
[ ] Relationship uses public references.
[ ] Relationship does not imply ownership transfer.
[ ] Relationship does not bypass owning service.
[ ] Relationship does not imply Permission.
[ ] Relationship visibility follows Policy.
```

Architecture violation:

```text
event owns subject state
document owns trademark behavior
matter mutates customer without Customer Service
communication sends itself without Communication Service rules
```

---

# 13. Service Collaboration Validation

Services may collaborate, but collaboration must be explicit.

Allowed collaboration examples:

```text
Workflow Contract Service coordinates Customer Service, Trademark Service, Task Service and Event Service.
Communication Service may request Human Review validation and Event trace.
Task Service may link task to Matter or Communication by reference.
Document Service may attach document reference to Matter or Trademark through owning service-approved behavior.
```

Checks:

```text
[ ] Collaboration uses service boundary.
[ ] Collaboration preserves owning service.
[ ] Collaboration preserves Permission/Policy.
[ ] Collaboration records Event trace where state changes.
[ ] Collaboration uses safe errors.
```

Architecture violation:

```text
service directly updates another service's owned object without approved boundary
service creates another domain's event directly without owner/event integration
service uses another domain's database ID directly
```

---

# 14. Lifecycle Validation

Objects with lifecycle states must have service-owned transitions.

Required lifecycle examples:

```text
Customer status
Trademark lifecycle/status
Matter status
Order status
Document status
Evidence status
Task status
Communication status
Workflow Contract preview/apply status
Event visibility/status if any
```

Checks:

```text
[ ] Lifecycle states are defined.
[ ] Lifecycle transitions are owned by service.
[ ] Protected transitions require Permission/Policy.
[ ] Professional/external-facing transitions require Human Review where applicable.
[ ] Duplicate-sensitive transitions require Idempotency.
[ ] Transitions record Event trace.
```

Architecture violation:

```text
status changed by API directly
status changed by workflow directly without owning service
agent completes status transition
human review record alone changes status automatically
```

---

# 15. Permission / Policy Alignment

Validate:

```text
[ ] Protected service actions require Permission.
[ ] Policy-controlled data requires Policy.
[ ] Cross-organization relationships require Policy.
[ ] Restricted fields are marked or traceable.
[ ] Redaction sets restricted_fields_omitted.
[ ] Non-disclosure can return NotFound where required.
[ ] Permission and Policy remain separate.
```

Blocked if:

```text
MVP service action is protected but has no Permission mapping.
MVP service output includes restricted data but has no Policy mapping.
```

---

# 16. Idempotency Alignment

Validate duplicate-sensitive service actions.

Required duplicate-sensitive actions:

```text
create Customer
create Brand
create Trademark
create Matter
create Order
create Document
create Evidence
create Task
create Communication
workflow apply
routing selection stub if exposed
```

Checks:

```text
[ ] Idempotency is required.
[ ] Same key + same semantic request replays safely.
[ ] Same key + different semantic request conflicts safely.
[ ] Replay creates no duplicate objects.
[ ] Replay creates no duplicate Tasks, Communications or Events.
```

Blocked if:

```text
duplicate-sensitive MVP service action has no Idempotency trace.
```

---

# 17. Event Alignment

Validate state-changing service actions.

Checks:

```text
[ ] State-changing service actions trace to Event.
[ ] Event source_service is owning service.
[ ] Event payload is safe.
[ ] Event visibility follows Permission/Policy.
[ ] Event reference is trace only.
[ ] Event is not used as command.
```

Architecture violation:

```text
API emits Event directly
Workflow emits Event directly
Agent emits Event directly
Event reference triggers behavior
Event payload leaks restricted data
```

---

# 18. API Alignment

Validate:

```text
[ ] API Contract maps to owning service.
[ ] API validator does not own service behavior.
[ ] API does not mutate domain state directly.
[ ] API does not emit Event directly.
[ ] API does not create active Task directly.
[ ] API failures use Error Contract.
[ ] API versions use Versioning Contract.
```

Blocked if:

```text
MVP API Contract has no owning service mapping.
MVP API protected operation lacks Permission/Policy mapping.
```

---

# 19. Workflow Alignment

Validate:

```text
[ ] Workflow maps to Workflow Contract.
[ ] Workflow Contract maps to owning services.
[ ] Workflow preview has no side effects.
[ ] Workflow apply requires Idempotency.
[ ] Workflow task plan maps to Task Service.
[ ] Workflow does not create active Task directly.
[ ] Workflow does not emit Event directly.
[ ] Workflow does not send Communication directly.
[ ] Workflow does not certify professional truth.
```

Architecture violation:

```text
workflow owns domain behavior
workflow creates active Task directly
workflow emits Event directly
workflow sends communication
workflow submits official filing
workflow certifies registrability or deadline
```

---

# 20. Agent Alignment

Validate:

```text
[ ] Agent output maps to AI Context.
[ ] Agent source use maps to Permission/Policy.
[ ] Agent output affecting protected action maps to Human Review.
[ ] Agent does not mutate protected state.
[ ] Agent does not emit Events.
[ ] Agent does not create or complete active Tasks.
[ ] Agent does not send Communications.
[ ] Agent does not certify professional truth.
```

Architecture violation:

```text
agent owns service behavior
agent completes Task
agent sends Communication
agent selects final provider
agent certifies evidence sufficiency
agent emits Event
```

---

# 21. Test Alignment

Validate:

```text
[ ] Every Must Build Now domain has test mapping.
[ ] Every protected service action has negative Permission/Policy tests.
[ ] Every duplicate-sensitive action has Idempotency tests.
[ ] Every state-changing action has Event trace tests.
[ ] Every API boundary has validator tests.
[ ] Every workflow boundary has validator tests.
[ ] Every agent forbidden action has boundary tests.
[ ] Every safe error and version rule has tests.
```

Blocked if:

```text
MVP service behavior has no tests.
MVP protected behavior has no negative tests.
MVP duplicate-sensitive behavior has no idempotency tests.
```

---

# 22. Validation Procedure

Perform validation in this order:

```text
1. Confirm required source files exist.
2. Validate 26-domain baseline.
3. Validate domain responsibility statements.
4. Validate object ownership and public references.
5. Validate owning service matrix.
6. Validate Must Build Now coverage.
7. Validate Stub Now safety.
8. Validate cross-domain relationships.
9. Validate service collaboration boundaries.
10. Validate lifecycle transitions.
11. Validate Permission/Policy alignment.
12. Validate Idempotency alignment.
13. Validate Event alignment.
14. Validate API alignment.
15. Validate Workflow alignment.
16. Validate Agent alignment.
17. Validate Test alignment.
18. Classify findings.
19. Produce validation report.
```

---

# 23. Finding Classification

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
Blocked = Must Build Now domain/object/service mapping missing.
Architecture Violation = ownership boundary breach.
Warning = Stub/future mapping incomplete but not blocking.
Out of Scope = valid but outside MVP.
Deferred = valid future-phase mapping.
Pass = complete for current phase and depth.
```

---

# 24. Required Evidence

Every finding must include:

```text
domain
object if applicable
service if applicable
source file
missing or inconsistent mapping
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Communication object can be marked sent by Workflow layer.
Status: Architecture Violation
Domain: Communication
Affected Service: Communication Service
Required Fix: Route send/review transition through Communication Service and Human Review gate.
Codex Impact: Block TASK-008 and TASK-010 until fixed.
```

---

# 25. Architecture Violation Triggers

The following always fail validation:

```text
Must Build Now domain has no owning service.
Object exposes raw database ID publicly.
Object owns business behavior.
API mutates domain state directly.
API emits Events directly.
Workflow owns domain behavior.
Workflow creates active Tasks directly.
Workflow emits Events directly.
Workflow sends Communication directly.
Agent mutates protected state.
Agent creates or completes active Task.
Agent sends Communication.
Agent emits Events.
Service bypasses Permission/Policy.
Duplicate-sensitive service action lacks Idempotency.
State-changing service action lacks Event trace.
Human Review directly executes downstream action.
```

---

# 26. Acceptance Criteria

Domain Object Service Validation passes only if:

```text
[ ] Required source files exist.
[ ] 26-domain baseline is preserved.
[ ] Every domain has clear responsibility.
[ ] Must Build Now domains have object/service/API/test trace.
[ ] Stub Now domains have safe stub ownership.
[ ] Objects describe state only.
[ ] Services own behavior.
[ ] Owning service matrix is consistent.
[ ] Cross-domain relationships use references and do not imply ownership transfer.
[ ] Lifecycle transitions are service-owned.
[ ] Permission/Policy alignment exists for protected behavior.
[ ] Idempotency alignment exists for duplicate-sensitive behavior.
[ ] Event alignment exists for state-changing behavior.
[ ] API alignment preserves service ownership.
[ ] Workflow alignment preserves coordination-only role.
[ ] Agent alignment preserves non-execution role.
[ ] Test alignment exists for MVP behavior.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now areas.
```

---

# 27. Validation Report Template

```text
Validation: Domain Object Service
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Domains / Objects / Services

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Domain:
- Object:
- Service:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 28. Codex Usage

Codex must use this validation:

```text
before implementing domain services
before implementing API validators
before implementing workflow validators
before implementing MVP execution spine
after adding or changing object specs
after adding or changing service specs
during PR review
```

Codex must not:

```text
invent service ownership
put behavior into objects
put behavior into API validators
put behavior into workflow validators
mutate state from agents
use missing service specs as reason to bypass ownership
```

---

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Domain Object Service Validation. Defines domain baseline, responsibility checks, object validation, service validation, owning service matrix, MVP/stub coverage, cross-domain relationships, lifecycle, Permission/Policy, Idempotency, Event, API, Workflow, Agent and Test alignment checks. |

---

**End of Domain Object Service Validation**
