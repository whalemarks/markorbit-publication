# B03-CH-34 — Codex Execution Roadmap

**Status:** Release Candidate 1

## Chapter Purpose

The Execution MVP is ready for implementation planning only when implementation can proceed without allowing Codex, engineers, Products or agents to invent missing authority.

This chapter converts the Book 03 architecture, governance model, workflow depths and readiness criteria into a controlled implementation roadmap.

The governing principle is:

```text
Codex implements approved contracts.
Codex does not invent architecture.
Each task proves one bounded execution capability.
Each gate must pass before execution depth expands.
```

The roadmap is deliberately staged.

It begins with canonical-source alignment, contract consumption, fixtures and boundary tests. It then introduces side-effect-free preview coordination, implements the eight approved MVP workflow previews, enables only the three approved internal apply paths, and finally adds controlled AI assistance, observability and pilot-readiness evidence.

It does not authorize:

- Product UI implementation;
- production Communication send;
- official filing or submission;
- payment;
- provider engagement or instruction;
- assignment recordal;
- renewal filing;
- autonomous professional execution;
- unrestricted Workflow Engine behavior;
- Event Bus or Event Sourcing;
- local redefinition of Book 02 Core contracts.

The core implementation path is:

```text
canonical sources locked
→ repository and governance initialized
→ Core contracts consumed
→ execution primitives and depth registry added
→ preview boundary proven
→ eight workflow previews implemented
→ governance gates integrated
→ three internal apply paths enabled
→ AI assistance constrained
→ trace and pilot evidence completed
→ MVP readiness reviewed
```

This roadmap is not a commitment to implement all future Execution capabilities.

It is a controlled path to the smallest governed execution system defined by Chapters 31–33.

---

## 1. Dependency Baseline

This roadmap depends directly on:

- [Chapter 31 — Execution MVP Boundary](B03-CH-31_Execution_MVP_Boundary.md)
- [Chapter 32 — MVP Execution Workflow Set](B03-CH-32_MVP_Execution_Workflow_Set.md)
- [Chapter 33 — MVP Implementation Readiness](B03-CH-33_MVP_Implementation_Readiness.md)

It also depends on:

- the complete Part II Execution Architecture;
- the eight Part III workflow patterns;
- the complete Part IV Execution Governance model;
- the approved Book 02 Core contracts;
- a typed Core implementation surface that remains consistent with Book 02;
- owning-Service contracts for any internal mutation;
- explicit Product and Integration boundaries.

The implementation roadmap must treat the following as separate authorities:

```text
Book 02 — MarkOrbit Core Specification
    normative source for Core meaning

Book 03 — MarkOrbit Execution System
    normative source for execution coordination and governance

markorbit-core
    typed implementation of approved Book 02 contracts

Execution implementation repository
    consumer and coordinator of Core contracts

Book 04 — MarkOrbit Workplace and Product Architecture
    organization-context and Product consumer of Execution results
```

If the typed implementation conflicts with the approved publication contract, implementation must stop and route the conflict to governance review.

Code does not silently overrule the books.

---

## 2. Canonical Source Precedence

Codex needs a clear source-of-truth order.

The recommended precedence is:

```text
1. Approved Book 02 and Book 03 canonical manuscripts
2. Approved architecture decisions and task specifications
3. Approved exported contracts from markorbit-core
4. Approved fixtures and validation rules
5. Tests expressing the approved acceptance criteria
6. Implementation code
7. Code comments and developer assumptions
```

Lower levels must not redefine higher levels.

### 2.1 Publication Authority

Book 02 and Book 03 define meaning, ownership, boundaries and non-goals.

They do not necessarily define every implementation field or package structure.

Where implementation detail is required, Codex may choose the smallest conventional structure that preserves the approved semantics.

### 2.2 Core Implementation Authority

`markorbit-core` should provide typed exports, validators, fixtures and contract references.

Execution should consume those exports rather than copy and fork them.

If a required export is absent, the correct response may be:

```text
blocked by Core dependency
```

not:

```text
reimplemented locally in Execution
```

### 2.3 Task Specification Authority

Each Codex task should identify:

- canonical sources;
- permitted files or modules;
- required behavior;
- forbidden behavior;
- test requirements;
- exact acceptance criteria;
- next gate.

A task prompt is not allowed to broaden the MVP beyond this chapter.

---

## 3. Repository Boundary

Execution implementation should live in a dedicated implementation boundary.

The final repository name is a governance and release decision. The architectural requirement is that Execution implementation must not be hidden inside:

- `markorbit-core`;
- a Product repository;
- MarkReg UI code;
- Lite UI code;
- an integration connector repository;
- the publication repository.

A dedicated boundary prevents Execution coordination from becoming accidental Core or Product logic.

### 3.1 Publication Repository

The publication repository owns:

- Book 03 manuscripts;
- governance documents;
- planning documents;
- architecture reviews;
- publication status;
- changelog.

It should not contain production runtime code.

### 3.2 Core Repository

`markorbit-core` owns:

- typed Core contracts;
- Core registries;
- validators;
- Core fixtures;
- Core contract tests;
- approved Core implementation surfaces.

It should not implement Book 03 Workflow coordination or Product behavior.

### 3.3 Execution Repository

The Execution repository should own:

- execution context assembly;
- workflow-depth registry;
- preview coordinators;
- internal apply coordinators;
- gate orchestration;
- safe execution results;
- idempotency and retry coordination;
- audit correlation;
- workflow fixtures;
- boundary tests;
- AI assistance adapters constrained by approved governance.

It should not own canonical Core object meaning.

### 3.4 Product Repository

Product repositories should consume Execution APIs or application services.

They must not contain hidden execution truth or bypass gates.

### 3.5 Integration Repository or Boundary

Integration owns external transport and provider-specific behavior.

The current Execution MVP may consume disabled, fixture-backed or approved read-only integration surfaces.

It may not activate protected external effects.

---

## 4. Roadmap Structure

The roadmap is divided into seven implementation phases.

```text
Phase 0 — Source and Repository Governance
Phase 1 — Execution Foundation
Phase 2 — Governance Gate Foundation
Phase 3 — MVP Workflow Preview Set
Phase 4 — Depth A Internal Apply
Phase 5 — AI and Agent Assistance Boundary
Phase 6 — Observability, Pilot and MVP Readiness
```

Each phase has:

- a purpose;
- prerequisites;
- Codex task groups;
- a gate;
- prohibited shortcuts.

A phase is complete only when its gate passes.

Codex must not start the next phase in the same pull request merely because the current task appears small.

---

## 5. Phase 0 — Source and Repository Governance

### 5.1 Purpose

Phase 0 creates the implementation boundary and locks canonical sources before runtime behavior begins.

This phase prevents the repository from starting as an improvised Workflow Engine or Product backend.

### 5.2 Phase 0 Tasks

#### EXEC-TASK-001 — Initialize Execution Repository

Create:

- repository purpose;
- governance principles;
- architecture boundary;
- supported toolchain;
- lint, formatting, typecheck and test baseline;
- initial source and test structure;
- version marker;
- contribution rules.

Required repository statement:

```text
This repository implements Book 03 execution coordination.

It does not redefine Book 02 Core contracts.
It is not a Product UI repository.
It is not an external filing, payment or Communication-send system.
It does not grant autonomous AI authority.
```

#### EXEC-TASK-002 — Canonical Source Manifest

Add a machine-readable or strongly structured manifest identifying:

- Book 02 canonical source location;
- Book 03 canonical source location;
- supported Book 02 contract version;
- supported Book 03 manuscript version;
- `markorbit-core` dependency version;
- approved MVP workflow set;
- current workflow depths;
- explicitly deferred actions.

The manifest should fail validation when required source identifiers are absent.

#### EXEC-TASK-003 — Repository Boundary Architecture Note

Document:

- Core vs Execution vs Integration vs Product;
- Service ownership;
- Workflow coordination;
- Event ownership;
- AI boundary;
- external-action exclusions.

#### EXEC-TASK-004 — Execution Change-Control Rules

Add repository rules for:

- workflow-depth change;
- protected-action change;
- new Service dependency;
- new mutation capability;
- new Event type request;
- agent tool expansion;
- production connector proposal.

#### EXEC-TASK-005 — Initial Fixture and Validation Harness

Create the common mechanism for:

- execution fixtures;
- fixture manifest;
- fixture validation;
- deterministic test loading;
- invalid-fixture tests.

No workflow implementation is added yet.

### 5.3 Phase 0 Gate

Phase 0 passes when:

- repository purpose is explicit;
- canonical source precedence is documented;
- Core and Product boundaries are documented;
- workflow depths are locked;
- deferred actions are listed;
- tests, lint and typecheck pass;
- no runtime, UI, database or external connector is added.

### 5.4 Prohibited Shortcuts

Do not:

- create workflow execution before the depth registry exists;
- copy Core contracts locally;
- add Product endpoints “for demonstration”;
- add a database because later tasks may need one;
- introduce an agent framework;
- activate a production connector.

---

## 6. Phase 1 — Execution Foundation

### 6.1 Purpose

Phase 1 creates the smallest typed Execution foundation needed by all workflows.

It should remain contract-oriented and side-effect free.

### 6.2 Phase 1 Tasks

#### EXEC-TASK-006 — Execution Workflow Depth Registry

Add the controlled MVP registry:

```text
intake-execution → depth-a
application-preparation → depth-a
communication-review → depth-a

provider-routing-preparation → depth-b
office-action-response-preparation → depth-b
renewal-preparation → depth-b
assignment-preparation → depth-b
evidence-review-preparation → depth-b
```

The registry must explicitly reject:

- unregistered workflow type;
- Depth B apply;
- external protected action;
- Product-defined depth override.

#### EXEC-TASK-007 — Execution Operation Base Contract

Define the smallest typed operation identity required to coordinate:

- operation id;
- workflow type;
- depth;
- semantic request reference;
- subject and target references;
- actor and sponsor references;
- version references;
- created time;
- metadata boundary.

Do not define a new Core object.

#### EXEC-TASK-008 — Execution Context Contract

Define the execution context consumed by coordinators.

It may reference:

- Core objects;
- current versions;
- Permission context;
- Policy context;
- Human Review context;
- idempotency context;
- audit context;
- AI assistance context.

Context fields should reference approved Core contracts wherever possible.

#### EXEC-TASK-009 — Execution Preview Result Contract

Define a side-effect-free preview result capable of expressing:

- normalized context;
- missing information;
- warnings;
- review requirements;
- source references;
- version basis;
- unsupported conditions;
- explicit no-effect statement;
- AI assistance disclosure.

#### EXEC-TASK-010 — Execution Apply Result Contract

Define a bounded internal apply result capable of expressing:

- created or updated Service references;
- existing results returned;
- blocked effects;
- partial completion;
- uncertain effects;
- Event references from owning Services;
- explicit external-action false statements;
- next allowed action.

This contract does not enable apply by itself.

#### EXEC-TASK-011 — Safe Execution Error Contract

Add Execution-level consumption and projection of approved Error semantics.

It must distinguish:

- validation failure;
- Permission denial;
- Policy block;
- Human Review required;
- version conflict;
- unsupported workflow depth;
- idempotency conflict;
- partial completion;
- uncertain outcome;
- dependency unavailable.

Do not invent a competing Core Error system.

#### EXEC-TASK-012 — Workflow Registration Validator

Validate that each registered workflow declares:

- depth;
- purpose;
- preview support;
- apply support;
- allowed effects;
- prohibited effects;
- required gates;
- Service dependencies;
- AI boundary;
- audit expectation.

#### EXEC-TASK-013 — Common Execution Fixtures

Add fixtures for:

- valid Depth A workflow;
- valid Depth B workflow;
- unknown workflow;
- unsupported apply;
- missing version;
- missing actor;
- safe preview;
- safe failure.

### 6.3 Phase 1 Gate

Phase 1 passes when:

- all eight workflows are registered;
- depth is immutable at runtime;
- preview and apply result contracts exist;
- unsupported apply is representable;
- safe errors are typed;
- fixtures and validators pass;
- no workflow-specific business logic exists;
- no mutation occurs.

---

## 7. Phase 2 — Governance Gate Foundation

### 7.1 Purpose

Phase 2 integrates the governance controls that every workflow must consume before implementation expands.

These controls must exist before Depth A apply.

### 7.2 Phase 2 Tasks

#### EXEC-TASK-014 — Core Contract Consumption Boundary

Create an adapter or import boundary that consumes approved exports from `markorbit-core`.

It should:

- pin the supported version;
- expose only required contracts;
- prevent local mutation of registry constants;
- fail clearly when a required export is missing.

#### EXEC-TASK-015 — Version Snapshot and Compatibility Check

Add execution support for:

- source version references;
- preview version;
- review version;
- apply version;
- stale-version detection;
- explicit compatibility result.

Do not implement a general version-management platform.

#### EXEC-TASK-016 — Permission Gate Coordinator

Add a coordinator that consumes Permission results before:

- preview access;
- internal apply;
- review;
- audit access.

It must default to deny or safe block when required Permission cannot be established.

#### EXEC-TASK-017 — Policy Gate Coordinator

Add a coordinator that consumes Policy results for:

- data processing;
- AI assistance;
- Document and Evidence access;
- internal apply;
- external-action prohibition;
- audit exposure.

It must fail closed for protected apply.

#### EXEC-TASK-018 — Human Review Binding

Add the minimum review binding required by the MVP:

- subject;
- exact version;
- intended action;
- reviewer;
- decision;
- scope;
- conditions;
- decision time;
- stale or superseded state.

Do not implement every future review model.

#### EXEC-TASK-019 — Idempotency Coordination

Add the semantic-operation and idempotency consumption needed for Depth A internal effects.

It must distinguish:

- existing result replay;
- safe new attempt;
- conflict;
- partial continuation;
- reconciliation required.

#### EXEC-TASK-020 — Audit Correlation Context

Add correlation for:

- operation;
- workflow;
- attempt;
- actor;
- sponsor;
- versions;
- review;
- Services;
- Event references;
- AI assistance.

Do not add an Event Bus.

#### EXEC-TASK-021 — Governance Gate Composition

Create a deterministic gate composition order for internal apply:

```text
workflow depth
→ input validation
→ object and version state
→ Permission
→ Policy
→ Human Review
→ idempotency
→ owning-Service request
```

The composition must return safe blocked results rather than throw uncontrolled errors.

#### EXEC-TASK-022 — Governance Negative Test Pack

Add tests proving that:

- missing Permission blocks;
- missing Policy blocks;
- stale version blocks;
- missing review blocks;
- AI cannot satisfy review;
- Depth B apply blocks;
- Product-provided depth override blocks;
- Workflow cannot emit Event;
- external-action request blocks.

### 7.3 Phase 2 Gate

Phase 2 passes when:

- gates are reusable across all workflows;
- current versions are bound;
- Human Review is exact-version and action-bound;
- idempotency is semantic;
- audit correlation exists;
- negative tests pass;
- no Service mutation has yet been enabled through workflow code.

---

## 8. Phase 3 — MVP Workflow Preview Set

### 8.1 Purpose

Phase 3 implements side-effect-free preview for all eight MVP workflows.

Preview is implemented before internal apply so that input, gaps, versions, review requirements and safe failure become stable first.

### 8.2 Common Preview Requirements

Every preview must:

- consume a registered workflow;
- validate supported input;
- enforce Permission and Policy;
- identify source versions;
- produce no mutation;
- create no active Task;
- emit no governed Event;
- disclose AI assistance;
- state that no protected external action occurred;
- return safe errors.

### 8.3 Phase 3 Tasks

#### EXEC-TASK-023 — Intake Execution Preview

Implement preview for:

- normalized intake;
- missing data;
- duplicate candidates;
- Document presence;
- preliminary internal readiness;
- review needs;
- Task plan preview.

No Customer, Brand, Matter, Order, Task or Communication is created.

#### EXEC-TASK-024 — Application Preparation Preview

Implement preview for:

- applicant and mark context;
- jurisdiction references;
- Classification readiness;
- goods/services warnings;
- Document checklist;
- Evidence gaps;
- review needs.

No Trademark preparation state is mutated.

#### EXEC-TASK-025 — Communication Review Preview

Implement preview for:

- draft package;
- recipient set;
- attachment references;
- source references;
- version comparison;
- AI assistance disclosure;
- review requirement.

No draft object or review decision is created unless a later internal apply task explicitly permits it.

#### EXEC-TASK-026 — Provider Routing Preparation Preview

Implement:

- provider candidate comparison;
- quote-version comparison;
- missing term detection;
- capability gaps;
- confidentiality warnings;
- advisory recommendation.

No provider is selected or contacted.

#### EXEC-TASK-027 — Office Action Response Preparation Preview

Implement:

- source Document validation;
- issue extraction;
- deadline-source disclosure;
- missing Evidence;
- strategy options;
- review questions.

No strategy is approved and no response is submitted.

#### EXEC-TASK-028 — Renewal Preparation Preview

Implement:

- renewal-window context;
- source and confidence disclosure;
- owner mismatch warning;
- Document and Evidence gaps;
- fee-source limitations;
- review questions.

No deadline is certified, no payment occurs and no renewal is filed.

#### EXEC-TASK-029 — Assignment Preparation Preview

Implement:

- party references;
- mark list;
- Document checklist;
- signature and authority gaps;
- jurisdiction requirements;
- recordal-readiness warnings.

No ownership record changes and no recordal occurs.

#### EXEC-TASK-030 — Evidence Review Preparation Preview

Implement:

- Evidence inventory;
- source and date extraction;
- mark-use mapping;
- goods/services mapping;
- contradiction and missing-evidence flags;
- review questions.

No authenticity, admissibility or sufficiency conclusion is recorded as final.

#### EXEC-TASK-031 — Preview-Only Apply Lock

Add a common locked response for every Depth B workflow.

The response must state:

```text
Apply is not enabled for the current workflow depth.
No protected action or authoritative mutation occurred.
```

#### EXEC-TASK-032 — Cross-Workflow Preview Fixture Pack

Add valid and invalid fixtures for all eight previews.

#### EXEC-TASK-033 — Preview Boundary Test Pack

Prove that previews do not:

- mutate Core;
- create active Tasks;
- create review decisions;
- send Communications;
- select providers;
- submit;
- pay;
- emit governed Events.

### 8.4 Phase 3 Gate

Phase 3 passes when:

- all eight previews are available;
- every preview is side-effect free;
- every preview is version-aware;
- every preview identifies review needs;
- every Depth B apply is blocked;
- no external protected action exists;
- preview acceptance tests pass.

At this gate, the five Depth B workflows have reached the current MVP target.

---

## 9. Phase 4 — Depth A Internal Apply

### 9.1 Purpose

Phase 4 enables internal apply only for:

1. Intake Execution;
2. Application Preparation;
3. Communication Review.

Apply must coordinate owning Services.

Workflow must not mutate Core directly.

### 9.2 Phase 4 Tasks

#### EXEC-TASK-034 — Internal Apply Coordinator Base

Add the common internal apply sequence:

```text
validate depth
→ revalidate current versions
→ Permission
→ Policy
→ Human Review
→ idempotency
→ call owning Services
→ correlate results
→ return Event references
→ state prohibited external effects did not occur
```

#### EXEC-TASK-035 — Task Plan to Task Service Boundary

Define the conversion boundary between:

- preview Task plan;
- Task Service request;
- active Task result.

It must prevent Workflow or AI from creating active Tasks independently.

#### EXEC-TASK-036 — Review Request and Decision Service Boundary

Implement the minimum Service-owned review request and review-decision interaction needed by Depth A workflows.

The implementation must preserve:

- exact version;
- intended action;
- reviewer;
- decision;
- conditions;
- stale behavior.

#### EXEC-TASK-037 — Intake Internal Apply

Implement the approved internal Intake effects through owning Services.

Allowed effects may include:

- Customer linkage or creation;
- Brand linkage or creation;
- preliminary Matter creation;
- approved draft Order creation;
- Document linkage;
- active Task creation;
- follow-up Communication draft request.

Required output:

```text
Internal intake preparation applied.
No legal engagement, payment, provider instruction or filing occurred.
```

#### EXEC-TASK-038 — Application Preparation Internal Apply

Implement approved internal preparation effects through owning Services.

Allowed effects may include:

- Trademark preparation record;
- Brand and applicant linkage;
- jurisdiction and Classification references;
- Document and Evidence linkage;
- active preparation Tasks;
- review state.

Required output:

```text
Internal application preparation applied.
No official filing or payment occurred.
```

#### EXEC-TASK-039 — Communication Review Internal Apply

Implement:

- draft creation through Communication Service;
- review request;
- review decision recording;
- exact package-version binding;
- follow-up Task creation where permitted.

Required lock:

```text
No Communication send capability is available in this workflow.
```

#### EXEC-TASK-040 — Partial Completion Result Coordination

Add governed handling for:

- one Service succeeds;
- another Service blocks;
- a response is lost;
- an effect is uncertain;
- continuation is required.

Do not pretend cross-Service atomicity.

#### EXEC-TASK-041 — Internal Apply Idempotency and Retry Pack

Add tests for:

- repeated Intake apply;
- repeated Application Preparation apply;
- repeated Communication draft request;
- duplicate Task prevention;
- same key with changed semantic request;
- lost response reconciliation;
- blocked blind retry.

#### EXEC-TASK-042 — Depth A External-Action Lock Pack

Prove that Depth A cannot:

- send;
- file;
- pay;
- select or engage provider;
- mark official status;
- emit Events directly from Workflow;
- allow AI approval.

#### EXEC-TASK-043 — Depth A Audit Reconstruction

Add testable audit reconstruction for each Depth A workflow.

An authorized observer must be able to identify:

- request;
- actor;
- versions;
- gates;
- review;
- Service effects;
- Event references;
- external effects that did not occur.

### 9.3 Phase 4 Gate

Phase 4 passes when:

- all three Depth A workflows apply only internal Service-owned effects;
- stale review blocks apply;
- idempotency prevents duplicate effects;
- partial completion is visible;
- Event references come from Services;
- Communication send remains impossible;
- no filing, payment or provider commitment occurs;
- audit reconstruction passes.

At this gate, the three Depth A workflows have reached the current MVP target.

---

## 10. Phase 5 — AI and Agent Assistance Boundary

### 10.1 Purpose

Phase 5 adds AI assistance only after deterministic preview, governance gates and internal apply boundaries are stable.

AI is not required for Core correctness.

### 10.2 Phase 5 Tasks

#### EXEC-TASK-044 — AI Assistance Context

Add a typed assistance context referencing:

- workflow;
- purpose;
- source references;
- source versions;
- allowed assistance;
- prohibited authority;
- Human Review requirement;
- audit reference.

#### EXEC-TASK-045 — Structured AI Output Boundary

Define safe structured outputs for:

- extraction;
- summary;
- comparison;
- missing-field analysis;
- draft;
- review questions;
- source limitations.

The output must remain a draft or advisory result.

#### EXEC-TASK-046 — AI Source Attribution and Limitation

Require material AI-assisted output to preserve:

- source references;
- source versions;
- unsupported claims;
- missing source;
- conflict;
- generation version;
- human-edit status where applicable.

#### EXEC-TASK-047 — Agent Tool Allowlist

If an agent interface is added, allow only the smallest approved tool set.

The default should be:

- read;
- validate;
- compare;
- prepare;
- request Human Review.

Mutation-capable tools must remain separately gated by owning Services.

#### EXEC-TASK-048 — Protected-Action Refusal Pack

Add tests proving AI and agents cannot:

- approve;
- satisfy quorum;
- send;
- submit;
- pay;
- engage provider;
- complete protected Task;
- mutate Core directly;
- emit governed Events;
- bypass Permission or Policy.

#### EXEC-TASK-049 — AI Unavailable and Incomplete Output

Implement safe fallback to human-controlled preparation when:

- AI is unavailable;
- output is malformed;
- extraction is incomplete;
- source conflict exists;
- confidence is insufficient;
- Policy prohibits AI processing.

#### EXEC-TASK-050 — Prompt-Injection and Context-Isolation Tests

Add tests for:

- external content attempting to instruct the agent;
- cross-Matter data access;
- unauthorized tool request;
- secret request;
- recipient expansion;
- provider-instruction attempt.

### 10.3 Phase 5 Gate

Phase 5 passes when:

- AI assistance is optional;
- source and version trace exist;
- incomplete AI output fails safely;
- agents remain inside explicit authority;
- protected-action refusal tests pass;
- Human Review remains required;
- no autonomous execution is introduced.

---

## 11. Phase 6 — Observability, Pilot and MVP Readiness

### 11.1 Purpose

Phase 6 proves that the implemented MVP is observable, auditable and suitable for a controlled pilot.

It does not create a broad production platform.

### 11.2 Phase 6 Tasks

#### EXEC-TASK-051 — Execution Trace Projection

Add a read-only correlated projection for:

- operation;
- workflow;
- attempt;
- versions;
- gates;
- review;
- Service effects;
- Event references;
- AI assistance;
- current safe next action.

This projection is not Core truth and must not mutate execution.

#### EXEC-TASK-052 — Boundary Violation Signals

Make attempts to perform prohibited actions observable:

- Depth B apply;
- Communication send;
- filing;
- payment;
- provider engagement;
- stale-approval reuse;
- agent Event emission;
- Permission or Policy bypass.

#### EXEC-TASK-053 — Audit Query Fixture Pack

Add authorized audit-query fixtures for:

- successful preview;
- successful internal apply;
- blocked apply;
- stale review;
- idempotent replay;
- partial completion;
- uncertain outcome;
- AI-assisted preparation.

#### EXEC-TASK-054 — MVP Readiness Test Suite

Create the consolidated test suite derived from Chapters 31–33.

It must include:

- positive paths;
- negative paths;
- boundary violations;
- failure paths;
- version and idempotency paths;
- AI refusal;
- audit reconstruction.

#### EXEC-TASK-055 — Controlled Pilot Configuration

Define a pilot configuration constrained by:

- environment;
- organization;
- workflow set;
- user group;
- fixture or approved test data;
- AI enabled or disabled;
- external connectors disabled;
- time window;
- rollback or stop condition.

#### EXEC-TASK-056 — MVP Readiness Report

Produce a machine-checkable and human-readable report stating:

- implemented workflow depth;
- Book 02 contract versions;
- test results;
- known gaps;
- deferred actions;
- boundary violations detected;
- pilot constraints;
- release recommendation.

#### EXEC-TASK-057 — Execution MVP Release Candidate Gate

Run:

- tests;
- fixture validation;
- typecheck;
- lint;
- boundary review;
- Core dependency review;
- publication alignment review.

No broad release occurs automatically.

### 11.3 Phase 6 Gate

Phase 6 passes when:

- all MVP workflows meet their target depth;
- boundary tests pass;
- audit reconstruction passes;
- AI remains constrained;
- external connectors remain disabled for protected action;
- pilot scope is explicit;
- known gaps are documented;
- governance approves the release candidate.

---

## 12. Task Dependency Map

The high-level dependency map is:

```text
Phase 0
    ↓
Phase 1 — common types, depth registry, fixtures
    ↓
Phase 2 — versions, gates, review, idempotency, audit
    ↓
Phase 3 — all eight previews
    ↓
Phase 4 — three internal apply workflows
    ↓
Phase 5 — constrained AI and agent assistance
    ↓
Phase 6 — observability, pilot and readiness report
```

Some work may be prepared in parallel, but acceptance must preserve the gate order.

For example:

- AI prompt experiments may occur outside the release path;
- Product mockups may be created separately;
- connector fixtures may be prepared;
- Service contracts may continue in `markorbit-core`.

Those activities must not be merged into the Execution release path before their dependencies pass.

---

## 13. Core Dependency Gates

The Execution roadmap depends on continued `markorbit-core` work.

The minimum Core dependency gate should confirm approved coverage for:

- domain registry;
- object base;
- Event primitive and catalog;
- Task primitive;
- Workflow Contract primitive and catalog;
- Service contract skeletons;
- API contract skeletons;
- Permission contract skeletons;
- Policy contract skeletons;
- AI Governance contract skeletons;
- validation contracts and fixture validation;
- versioning, idempotency, errors, audit and Human Review.

### 13.1 Skeleton-Level Dependency

A skeleton may be enough for:

- repository structure;
- fixture validation;
- preview contracts;
- boundary tests;
- unsupported responses.

It may not be enough for deep Service-owned apply.

### 13.2 Service-Level Dependency

Depth A apply requires enough owning-Service behavior to:

- validate;
- reject;
- apply;
- return exact result;
- enforce idempotency;
- preserve version;
- return Event or audit reference.

### 13.3 Missing Core Dependency

A missing dependency should result in:

```text
Execution task blocked by Core contract gap.
```

The gap should be raised as a separate Core task.

Execution must not add the missing Core contract locally.

---

## 14. Codex Task Contract

Every Codex task in this roadmap should use a consistent task contract.

### 14.1 Required Task Header

```text
Repository:
Task ID:
Task name:
Phase:
Canonical sources:
Purpose:
Current dependency state:
```

### 14.2 Required Scope

The task must identify:

- files to create;
- files to modify;
- contracts to consume;
- behavior to implement;
- tests to add;
- fixtures to update;
- documentation to update.

### 14.3 Required Non-Goals

Every task should explicitly restate relevant non-goals.

Typical non-goals include:

- no Product UI;
- no database unless explicitly approved;
- no API server unless explicitly approved;
- no external connector;
- no production send;
- no filing;
- no payment;
- no provider engagement;
- no Event Bus;
- no autonomous agent;
- no new Core Domain;
- no direct Workflow mutation.

### 14.4 Required Validation

Typical validation includes:

```text
pnpm test
pnpm validate:fixtures
pnpm lint
pnpm typecheck
git diff --check
git status --short
```

The actual commands may differ by repository, but the task must list them.

### 14.5 Required Final Summary

Codex should report:

- created files;
- modified files;
- implemented behavior;
- test results;
- fixture counts where applicable;
- boundary confirmations;
- commit identifier;
- pull request state;
- next recommended task.

### 14.6 No Hidden Next Task

Codex must not start the next task in the same branch or pull request unless the task specification explicitly groups them.

---

## 15. Branch and Pull Request Governance

The recommended rule is:

```text
One primary acceptance outcome per pull request.
```

A pull request may contain multiple micro-steps only when they:

- share the same boundary;
- share the same test gate;
- cannot be reviewed meaningfully in isolation;
- do not cross phases.

### 15.1 Branch Naming

A branch should identify the task or controlled task pack.

Example:

```text
exec-task-023-intake-preview
```

The exact convention belongs to repository governance.

### 15.2 Pull Request Description

The pull request should include:

- task ID;
- purpose;
- canonical source references;
- allowed effects;
- prohibited effects;
- test results;
- boundary confirmation;
- known gaps.

### 15.3 Review Order

Review should occur in this order:

1. boundary;
2. contract alignment;
3. effect ownership;
4. negative tests;
5. positive behavior;
6. code quality;
7. documentation.

A technically elegant implementation that violates the boundary must be rejected.

---

## 16. Definition of Done

A task is done only when:

1. scope is complete;
2. non-goals remain absent;
3. contracts are consumed rather than copied;
4. fixtures match implementation;
5. tests include negative behavior;
6. typecheck and lint pass;
7. documentation reflects the change;
8. changelog or roadmap state is updated;
9. boundary confirmation is explicit;
10. no next task is partially started;
11. the working tree is clean;
12. the pull request is reviewable.

A task is not done merely because:

- code compiles;
- a demo works;
- a happy-path test passes;
- Codex says the feature is complete;
- a Product can display the result.

---

## 17. Acceptance Gate Model

The roadmap uses six gates.

### Gate E0 — Repository Governed

Required:

- canonical sources;
- boundary;
- workflow depths;
- fixture harness;
- no runtime drift.

### Gate E1 — Foundation Ready

Required:

- operation, context, preview, apply and error contracts;
- workflow registry;
- validators;
- no mutation.

### Gate E2 — Governance Gates Ready

Required:

- version;
- Permission;
- Policy;
- Human Review;
- idempotency;
- audit;
- negative tests.

### Gate E3 — Preview Set Ready

Required:

- eight previews;
- side-effect-free behavior;
- Depth B apply lock;
- source and version disclosure;
- preview acceptance tests.

### Gate E4 — Internal Apply Ready

Required:

- three Depth A apply paths;
- Service-owned mutation;
- Task boundary;
- review binding;
- idempotency;
- partial completion;
- audit reconstruction;
- external-action locks.

### Gate E5 — AI Assistance Ready

Required:

- source trace;
- optional AI;
- safe fallback;
- tool restrictions;
- refusal tests;
- no protected authority.

### Gate E6 — MVP Release Candidate

Required:

- complete readiness suite;
- pilot constraints;
- observability;
- known-gap report;
- external actions disabled;
- governance approval.

---

## 18. Stop Conditions

Codex or engineers must stop when:

- Book 02 contract is missing;
- contract version is unknown;
- Service ownership is ambiguous;
- a task requires a new Core Domain;
- Product behavior would define execution truth;
- external action is needed to make a demo appear complete;
- Human Review semantics are unclear;
- idempotency cannot distinguish duplicate effect;
- a connector outcome cannot be reconciled;
- AI authority would need to expand;
- a Depth B workflow would need mutation;
- Event ownership is unclear;
- a prohibited effect appears in tests or fixtures.

The correct response is:

```text
Blocked by governance dependency.
```

not an improvised implementation.

---

## 19. Deferred Roadmap

The following capabilities are deliberately outside the current task roadmap:

### 19.1 Production Communication Send

Requires:

- sender identity;
- recipient authorization;
- exact package approval;
- send Service;
- provider integration;
- delivery semantics;
- resend and reconciliation;
- security and confidentiality review;
- production incident handling.

### 19.2 Provider Engagement and Instruction

Requires:

- provider selection authority;
- conflict and capability review;
- commercial approval;
- confidentiality and data-transfer controls;
- instruction Communication;
- acknowledgment;
- payment relationship;
- Event and audit.

### 19.3 Payment

Requires:

- financial Service ownership;
- beneficiary and amount verification;
- separation of duties;
- idempotency;
- uncertain-payment reconciliation;
- refund or compensation governance;
- security review.

### 19.4 Official Filing and Submission

Requires:

- exact package authorization;
- deadline review;
- official or provider connector;
- submission identity;
- external receipt;
- uncertain-outcome reconciliation;
- duplicate-filing prevention;
- incident handling.

### 19.5 Assignment and Renewal External Apply

Requires the general external-action governance plus domain-specific legal and professional review.

### 19.6 Autonomous Agent Execution

Requires a separate future governance package.

This chapter grants no authority for autonomous approval, send, filing, payment, provider engagement, protected mutation or Event emission.

---

## 20. Relationship to Book 04

Book 04 may begin Product planning while this roadmap is implemented.

However, Product work must consume stable execution semantics.

A safe parallel model is:

```text
Execution defines:
    depth
    preview
    apply
    review
    errors
    versions
    effects
    audit

Product defines:
    user journey
    screen
    interaction
    explanation
    notification
    accessibility
```

Product must not:

- enable a disabled apply;
- collapse preview and apply;
- label internal preparation as filing;
- label approval as send;
- treat AI output as professional decision;
- hide uncertainty;
- create direct database mutation;
- bypass Service ownership.

A Product mockup may show future states.

It must clearly identify them as future or disabled.

---

## 21. Relationship to Integration

Integration may prepare:

- connector contracts;
- fixtures;
- read-only reference access;
- disabled-action responses;
- simulated error conditions.

Integration must not activate protected external action merely because the Execution roadmap reaches Gate E4 or E6.

External action requires a separate readiness gate and change-control package.

The Execution MVP should be able to prove safe disabled behavior before production connectors exist.

---

## 22. Relationship to AI Governance

AI work may proceed only after deterministic boundaries are stable.

The order matters:

```text
first define what the workflow may do
then define what AI may assist with
```

not:

```text
first build an agent
then discover what authority it needs
```

AI tasks should remain subordinate to:

- workflow depth;
- Permission;
- Policy;
- Human Review;
- versioning;
- Service ownership;
- audit;
- safe failure.

AI quality improvements do not automatically expand execution authority.

---

## 23. MVP Release Decision

Completion of EXEC-TASK-001 through EXEC-TASK-057 does not automatically mean broad production release.

The release decision should answer:

1. Are all eight workflows at their approved depth?
2. Are all Depth B apply requests blocked?
3. Are all external protected actions disabled?
4. Do the three Depth A workflows mutate only through owning Services?
5. Are Human Review and version binding effective?
6. Does idempotency prevent duplicate internal effects?
7. Are partial and uncertain outcomes visible?
8. Are Event references Service-owned?
9. Can audit reconstruct the supported path?
10. Can AI be disabled without breaking governance?
11. Do negative tests prove boundary preservation?
12. Is the pilot scope limited and reversible?
13. Are Core dependency gaps documented?
14. Has Product interpretation been reviewed?
15. Has governance approved the release candidate?

The possible decisions are:

```text
approve controlled pilot
approve fixture and preview use only
approve internal apply for selected workflows only
defer pending Core dependency
reject due to boundary failure
```

---

## 24. Roadmap Change Governance

This roadmap is versioned.

A change requires review when it:

- adds or removes a workflow;
- changes workflow depth;
- changes allowed effects;
- enables external action;
- changes Human Review;
- changes Service ownership;
- adds an agent tool;
- adds a production connector;
- changes Event authority;
- changes Product or Integration boundary;
- changes gate order;
- changes release criteria.

Editorial clarification does not automatically require implementation migration.

Material change does.

Active tasks should remain pinned or be explicitly updated according to Chapter 27.

---

## 25. Governance Examples

### 25.1 Codex Attempts to Add Send During Communication Review

The task is EXEC-TASK-039.

Codex discovers that a mail provider library is easy to add.

Correct response:

```text
Do not add the provider library.
Communication Review internal apply ends at draft and review state.
Production send is outside the current MVP.
```

### 25.2 Missing Task Service Contract

EXEC-TASK-035 requires active Task creation, but the Task Service export is not sufficiently defined.

Correct response:

```text
Stop the task.
Raise a Core dependency task.
Keep Task plan preview available.
Do not create a local Task object in Execution.
```

### 25.3 Product Requests Apply for Renewal

Renewal Preparation is Depth B.

Correct response:

```text
Return the common preview-only apply lock.
Do not add renewal mutation to satisfy the Product.
Initiate change control if the roadmap should expand.
```

### 25.4 Agent Attempts to Emit an Event

An agent tool proposes emitting `core-review-completed`.

Correct response:

```text
Reject the direct Event action.
The owning review or Task Service must perform the governed mutation
and return the applicable Event reference.
```

### 25.5 Core Contract Changes Mid-Task

A Book 02 contract or `markorbit-core` export changes during an active task.

Correct response:

1. identify the pinned version;
2. assess compatibility;
3. update the task only through approved change control;
4. rerun fixtures and tests;
5. do not silently consume the latest version.

### 25.6 Happy Path Passes but Negative Test Fails

Intake apply succeeds, but duplicate requests create two active Tasks.

Correct response:

```text
The task is not complete.
The idempotency boundary failed.
Do not merge.
```

---

## 26. Governance Rules

The Codex Execution Roadmap is correct when:

1. Book 02 and Book 03 remain canonical;
2. Execution has a dedicated implementation boundary;
3. Core contracts are consumed rather than copied;
4. repository governance precedes runtime behavior;
5. common execution contracts precede workflow implementation;
6. governance gates precede internal apply;
7. preview precedes apply;
8. all eight workflows reach only their approved depth;
9. five workflows remain preview-only;
10. three workflows apply only internal Service-owned effects;
11. Communication send remains disabled;
12. filing, payment and provider engagement remain deferred;
13. Workflow never mutates Core directly;
14. Events come from owning Services or approved boundaries;
15. Human Review remains exact-version and action-bound;
16. Permission and Policy fail closed;
17. idempotency prevents duplicate effects;
18. safe failure preserves partial and uncertain truth;
19. AI is added after deterministic governance and remains optional;
20. agents cannot perform protected action;
21. negative tests are required for every boundary;
22. observability proves the boundary rather than redefining truth;
23. one pull request has one primary acceptance outcome;
24. missing Core dependencies block rather than trigger local invention;
25. roadmap expansion follows change control;
26. completion of tasks does not automatically authorize broad production release.

---

## 27. Product Boundary

Book 04 may plan Product releases in parallel, but it must consume stable Execution semantics and may not redefine workflow depth, Service ownership, Human Review, Event authority or external-action readiness.

## 28. Implementation Boundary

This chapter defines task sequence and gates, not the final repository name, framework, package layout, database, transport, deployment, monitoring vendor, model provider, connector or Product UI. Technical choices are valid only when they preserve the approved boundaries.

## 29. Book 03 Completion Result

This chapter completes **Part V — MVP Execution System** and the main body of **Book 03 — MarkOrbit Execution System**.

Book 03 now defines:

```text
why Execution exists
where Execution sits
what Execution owns
how Execution coordinates
how Workflow, Tasks, Review, Communication and Events interact
how Human and AI responsibilities remain separated
how eight professional workflow patterns behave
how retry, failure, versioning, review, agents and audit are governed
what the Execution MVP includes
which workflows may apply
which workflows remain preview-only
what must be true before implementation
how Codex must implement the MVP in controlled phases
```

The final operating rule is:

```text
Core defines.
Execution coordinates.
Integration connects.
Products consume.
Humans review.
AI assists.
Owning Services mutate.
Events trace.
Codex implements only what governance has approved.
```

The roadmap authorizes controlled implementation planning.

It does not authorize external protected action, autonomous professional execution or uncontrolled Product expansion.
