# B03-CH-08 — Execution Layer Overview

## Chapter Purpose

This chapter begins Part II — Execution Architecture.

Part I established why the Execution System exists, where it sits, the principles that govern it, its boundary, the role of Execution Context, and the path from Core contracts to runtime. This chapter now turns that foundation into an execution-layer map.

The map answers five practical questions:

```text
What responsibilities exist inside the Execution layer?
How do those responsibilities connect?
Which Book 02 contracts constrain each responsibility?
Which owning Service may perform state-changing behavior?
What outcome may be exposed to Product without moving governance into Product?
```

The component names in this chapter are architectural responsibility areas. They do not create new Core domains, objects, services, APIs, schemas, queues, workers, or product modules.

The purpose is orientation. Chapters 09–16 define the individual execution concerns in greater detail.

---

## 1. Dependency Baseline

This chapter consumes the following Book 02 sources:

- [Developer Start Here](../../book-02-core-specification/core-specs/DEVELOPER_START_HERE.md) — the implementation flow, ownership rules, and governance rules.
- [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md) — the Domain → Object → Service → Contract → Workflow → Event → Test chain and the layer responsibility map.
- [Core Specifications README](../../book-02-core-specification/core-specs/README.md) — the boundary and purpose of implementation-ready Core specifications.
- [Contract Layer Index](../../book-02-core-specification/core-specs/contracts/index.md) — Common, API, Workflow, and Test Contract responsibilities.
- [Common Contract Index](../../book-02-core-specification/core-specs/contracts/common/index.md) — shared reference, error, audit, AI, Human Review, Permission, Policy, idempotency, and versioning requirements.
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md) — universal workflow, preview, apply, task-plan, Event, Permission, Policy, AI, and Human Review rules.
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md) — governed workflow boundaries and their service, Event, review, and policy dependencies.
- [MVP Cut v0.1](../../book-02-core-specification/core-specs/implementation/mvp-cut-v0.1.md) — the first executable workflow and governance cut.
- [Implementation Depth Matrix](../../book-02-core-specification/core-specs/implementation/implementation-depth-matrix.md) — the permitted MVP depth for workflows, Events, agents, Permission, Policy, Human Review, and related controls.

It also applies the Book 03 planning boundaries in:

- [Execution System Blueprint](../planning/B03-PLN-0002_Execution_System_Blueprint.md)
- [Book 02 Dependency Map](../planning/B03-PLN-0005_Book_02_Dependency_Map.md)
- [Book 04 Boundary Map](../planning/B03-PLN-0006_Book_04_Boundary_Map.md)
- [MVP Execution Boundary](../planning/B03-PLN-0007_MVP_Execution_Boundary.md)

These files are the working dependency baseline for Draft 1. If Book 02 changes a source contract, ownership rule, or MVP depth, the corresponding Book 03 mapping must be reviewed.

---

## 2. The Execution Layer in One View

The Execution layer coordinates a governed path from an accepted request or observed condition to a safe operational outcome.

```text
Accepted request or observed condition
↓
Contract and source resolution
↓
Execution Context assembly
↓
Workflow and task coordination
↓
Validation / Permission / Policy / Human Review gates
↓
Owning-service action or safe pause
↓
Event references, audit context and execution outcome
↓
Product-consumable status and next action
```

This is not a promise that every path will complete.

A correct execution path may:

- proceed;
- request missing information;
- prepare a preview;
- create a task plan;
- route work to Human Review;
- delegate an allowed action to an owning Service;
- pause;
- block;
- return a safe failure;
- expose a retry option;
- report completion with trace references.

The layer exists to choose among those outcomes under contract. Its success criterion is not maximum automation. Its success criterion is governed coordination.

---

## 3. Coordination Without Ownership Drift

Book 02 defines a strict implementation flow:

```text
Domains define responsibility.
Objects describe state.
Services own behavior.
Contracts constrain access and execution.
Workflows coordinate services.
Agents assist.
Events preserve trace.
Tests verify behavior.
Products consume.
```

Book 03 must preserve that flow during operation.

| Execution concern | Book 02 owner or constraint | Book 03 responsibility |
|---|---|---|
| Domain and object state | Domain, Object, and owning Service specs | Resolve the applicable source and context; do not mutate directly |
| Workflow behavior | Workflow Spec and Workflow Contract | Coordinate preview/apply sequencing under the contract |
| Active Task creation | Task Service | Prepare a task plan and delegate active creation |
| Communication behavior | Communication Service and communication-related contracts | Coordinate draft, review, approval boundary, send handoff, and trace |
| Permission evaluation | Permission Service and Permission Context | Require and consume the evaluation; do not grant permission |
| Policy evaluation | Policy Service and Policy Context | Require and consume the evaluation; do not approve policy |
| Human Review | Human Review Contract plus owning-service acceptance rule | Route review, preserve evidence, and consume the recorded outcome |
| State-changing action | Owning Service | Delegate only after applicable gates pass |
| Event record | Owning Service or Event Service | Preserve and expose Event references; do not emit directly |
| AI or agent output | AI Context, capability limits, and agent governance | Use as bounded preparation input; never treat it as authority |
| Product presentation | Book 04 Product System | Expose safe execution outcomes without defining UI |

The central architectural test is simple:

```text
If an Execution responsibility starts owning professional truth,
domain state, Permission, Policy, Human Review authority, active Tasks,
Communications, or Events, it has crossed the Core boundary.
```

---

## 4. Conceptual Component Map

The Execution layer can be understood through nine responsibility areas.

```text
1. Entry and Condition Interpretation
2. Contract and Source Resolution
3. Execution Context Assembly
4. Workflow Coordination
5. Task Planning and Activation Boundary
6. Governance Gate Evaluation
7. Owning-Service Action or Safe Pause
8. Trace, Audit and Observability
9. Product Outcome Exposure
```

Human and AI participation crosses several of these areas, but it is not a bypass lane. AI assistance remains inside the same contracts and gates as any other input.

The nine areas are conceptual. A future implementation may combine or separate technical components. Technical packaging does not change the responsibilities.

---

## 5. Entry and Condition Interpretation

Execution begins only after an input has a recognized operational meaning.

An input may originate from:

- a user action exposed by a Product surface;
- an API request accepted under an API Contract;
- a workflow preview or apply request;
- a scheduled or resumed work item;
- a Human Review outcome;
- a retry request;
- an observed Event reference;
- an authorized manual handoff.

This responsibility interprets the input. It does not execute the requested business action.

For example:

```text
“Send this message”
```

must not become an immediate send command. Execution must determine:

- which Communication is referenced;
- which actor is requesting the action;
- which Permission and Policy contexts apply;
- whether Human Review is required and satisfied;
- which version was approved;
- whether the request is duplicate-sensitive;
- which service owns transmission;
- what trace must be preserved.

An observed Event also does not automatically become a command. Book 02 defines Events as trace of completed facts. Execution may use an allowed Event reference as context or as a condition for evaluation, but it must not invent command authority from the Event.

The output of entry interpretation is a bounded execution request with enough meaning to resolve its contracts and context. This phrase describes a responsibility, not a new Core object or schema.

---

## 6. Contract and Source Resolution

Before coordinating work, Execution must know which sources govern it.

Resolution identifies:

- the subject reference;
- the owning domain and service;
- the applicable API or Workflow Contract;
- the applicable Common Contracts;
- contract and schema versions;
- required Permission and Policy contexts;
- Human Review requirements;
- idempotency requirements;
- Event and audit requirements;
- testable failure boundaries.

The [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md) provides the cross-layer path. Execution consumes that path instead of reconstructing architecture from product behavior.

A valid resolution should be able to state:

```text
This workflow contract applies.
These services own the affected behavior.
These common contracts constrain the request.
These gates are required.
These versions are supported.
These Event references may be returned as trace.
These tests define the expected boundary.
```

If the applicable source cannot be resolved, Execution should not guess. It should stop with an explicit dependency or safe error.

Contract resolution prevents a common failure mode: a product or workflow performing an action merely because an interface exposes a button or an AI model suggests a next step.

---

## 7. Execution Context Assembly

After resolving sources, the layer assembles the Execution Context defined in Chapter 06.

The context combines the facts needed by the remaining execution path:

- subject and source references;
- actor and role;
- organization and business context;
- current workflow and task context;
- applicable contract versions;
- Permission and Policy contexts;
- Human Review requirements and evidence;
- AI participation and provenance;
- communication context where applicable;
- audit and correlation context;
- retry and idempotency context;
- safe failure information.

Context assembly must preserve provenance. It must distinguish supplied facts, Core-owned facts, AI-prepared material, human decisions, service outcomes, and Event references.

The context is not a second source of truth. When a Core-owned fact changes, Execution must use the authorized source or a versioned snapshot allowed by contract. It must not silently overwrite the Core fact inside execution-only state.

Chapter 09 will examine the relationship between execution concepts and Core-owned state. Chapter 08 establishes only the placement: context sits between source resolution and governed coordination.

---

## 8. Workflow Coordination

Workflow coordination determines the operational sequence under an approved Workflow Contract.

It may coordinate:

- validation;
- preview;
- required service calls;
- task-plan preparation;
- review routing;
- protected apply;
- safe pause;
- retry;
- outcome assembly.

It must preserve the Book 02 rules:

```text
Workflow coordinates.
Owning Services mutate.
Preview has no side effects.
Apply is protected and duplicate-sensitive.
Task plan is not active Task.
Workflow does not emit Events directly.
Workflow does not send Communications directly.
Workflow does not submit official filings.
```

### 8.1 Preview Path

Preview explains what would be required or what could happen.

A preview may return:

- missing inputs;
- applicable steps;
- a proposed task plan;
- required reviews;
- policy restrictions;
- possible service dependencies;
- expected trace;
- safe explanations.

Preview does not create active Tasks, send Communications, mutate Core state, emit Events, or certify a professional conclusion.

### 8.2 Apply Path

Apply requests governed execution.

Apply must revalidate the current context rather than assuming that a previous preview is still valid. It must check version, Permission, Policy, Human Review, idempotency, and current source state before delegating any allowed action.

Preview and apply are therefore related but distinct paths.

```text
Preview describes a governed possibility.
Apply requests governed effects.
```

Chapter 10 will define the Workflow Coordination Model in detail.

---

## 9. Task Planning and Activation Boundary

Execution often identifies work that must be performed, but identifying work is not the same as creating an active Task.

A task plan may describe:

- task type;
- subject reference;
- required owner role;
- priority;
- due-date basis;
- review requirement;
- policy restrictions;
- source workflow step.

The Task Service owns active Task creation.

This boundary prevents workflow previews, AI suggestions, and product interactions from silently creating operational commitments.

The path is:

```text
Execution prepares task plan
↓
Applicable gates are evaluated
↓
Task Service receives an allowed creation request
↓
Task Service creates or rejects the active Task
↓
Owning service records the resulting trace
```

Chapter 11 will define task readiness, activation, progress, completion, cancellation, and failure coordination without moving Task ownership into Book 03.

---

## 10. Governance Gate Evaluation

Governance gates determine whether the path may proceed.

The gate stack may include:

1. structural validation;
2. source and version validation;
3. Permission evaluation;
4. Policy evaluation;
5. Human Review validation;
6. idempotency validation;
7. protected-action validation;
8. safe-error and disclosure validation.

The gates are related, but they are not interchangeable.

```text
Valid shape is not Permission.
Permission is not Policy.
Policy allowance is not Human Review.
Human Review is not downstream execution.
AI confidence is none of the above.
```

Each required gate must produce a contract-valid outcome. Unknown Permission fails closed. Unknown Policy fails closed for policy-controlled behavior. Human Review must be performed by an authorized human and recorded. Review does not itself execute the downstream action.

A gate failure may:

- block;
- require redaction;
- require missing context;
- require Human Review;
- return a safe error;
- preserve a retryable state;
- escalate an unresolved dependency.

It must not be converted into silent success.

Chapters 12 and 15 will define review/approval lifecycle and Permission/Policy gates in detail.

---

## 11. Owning-Service Action or Safe Pause

After gates are evaluated, Execution has two broad outcomes:

```text
Delegate an allowed action to the owning Service
or
pause safely without pretending completion
```

Delegation does not guarantee success. The owning Service still applies its own contract, state, and validation rules.

Examples include:

- Task Service creates an active Task;
- Communication Service creates or transmits an allowed Communication;
- Document Service attaches or retrieves an allowed Document;
- Evidence Service records an allowed Evidence operation;
- Matter Service performs an allowed Matter transition;
- Event Service or the state-changing owning Service records the trace allowed by Book 02.

If the service rejects the request, Execution records and exposes the safe failure. It must not override the service merely because earlier gates passed.

A safe pause is a first-class operational result. It preserves enough context to explain why work stopped and what authorized action may happen next.

---

## 12. Trace, Audit and Observability

Execution must make its path inspectable.

The trace should allow an authorized reviewer to distinguish:

- the request that entered;
- the contracts and versions resolved;
- the context used;
- AI-assisted material;
- Human Review evidence and outcome;
- Permission and Policy results;
- workflow preview or apply;
- owning-service delegation;
- failure or retry;
- resulting Event references;
- final exposed outcome.

Execution does not emit authoritative Events directly. It consumes Event references returned by owning Services or Event Service and associates them with the execution path.

Audit Context and correlation references connect the steps without turning Book 03 into an event-sourcing system.

The MVP does not require:

- a streaming event bus;
- a production replay engine;
- a workflow telemetry platform;
- an audit dashboard;
- Event sourcing as the system of record.

It does require enough structured trace to answer:

```text
What was requested?
What was allowed?
What was blocked?
Who reviewed?
What did AI prepare?
Which service acted?
What failed or retried?
Which Event references prove the outcome?
```

Chapter 14 defines Event Trace, Audit and Replay. Chapter 30 later addresses execution observability and audit governance.

---

## 13. Product Outcome Exposure

Product surfaces need usable outcomes, but they must not invent execution meaning.

Execution may expose a product-consumable result such as:

- ready for review;
- missing required context;
- blocked by Permission;
- restricted by Policy;
- changes requested;
- approved but not executed;
- delegated to an owning Service;
- safely failed;
- retry available;
- completed with trace references.

The result should use safe public references, allowed fields, supported versions, and policy-compliant disclosure. Restricted details must be omitted or redacted as required.

Book 04 may decide:

- how the result is displayed;
- which guidance appears;
- which controls are visible;
- how the user navigates the next action;
- how trace is visualized.

Book 04 must not decide whether a gate passed, whether Human Review is valid, whether AI output is authoritative, or whether a protected action occurred.

Execution supplies operational meaning. Product supplies interaction.

---

## 14. Human–AI Participation Across the Layer

AI and agents may assist in several responsibility areas:

| Responsibility area | Permitted assistance |
|---|---|
| Entry interpretation | summarize intent, classify the request, identify missing facts |
| Contract resolution | retrieve candidate sources, explain applicable constraints |
| Context assembly | summarize evidence, organize provenance, identify gaps |
| Workflow preview | explain steps, prepare a proposed task plan |
| Review preparation | organize evidence, draft review questions, compare versions |
| Communication preparation | prepare a draft for review |
| Trace and audit | summarize an authorized audit trail |
| Product outcome support | prepare an explanation of an already-governed outcome |

AI and agents must not:

- grant Permission;
- approve Policy;
- satisfy Human Review;
- create active Tasks;
- send Communications;
- select a provider finally;
- submit filings;
- approve payments;
- certify deadlines, registrability, evidence sufficiency, or authority;
- mutate protected state;
- emit authoritative Events;
- convert a blocked path into success.

AI output remains an input to Execution Context. It never becomes a second execution authority.

Chapter 16 defines the Human–AI Execution Handoff in detail.

---

## 15. Four Core Execution Paths

The component map supports four recurring paths.

### 15.1 Preview

```text
Resolve sources
→ assemble context
→ validate
→ prepare governed preview
→ expose requirements and restrictions
```

No protected side effect occurs.

### 15.2 Apply

```text
Resolve current sources
→ rebuild or refresh context
→ evaluate all required gates
→ enforce idempotency
→ delegate to owning Services
→ preserve trace
→ expose outcome
```

Apply must not rely blindly on an earlier preview.

### 15.3 Review Return

```text
Receive recorded Human Review outcome
→ confirm reviewer authority and evidence
→ refresh Permission, Policy and source state
→ continue, revise, reject or pause
```

Review does not execute the action by itself.

### 15.4 Failure and Retry

```text
Receive safe failure
→ preserve allowed context and trace
→ determine whether retry is permitted
→ reuse or reject idempotency context as required
→ re-evaluate changed gates
→ delegate again or remain paused
```

Retry is governed continuation, not a new opportunity to bypass the failed rule.

---

## 16. MVP Depth of the Layer

The Execution layer must respect the Book 02 implementation-depth limits.

| Concern | Book 02 MVP depth | Book 03 implication |
|---|---|---|
| Workflow | Level 2 generally; selected Level 3 safety | Define preview/apply coordination and protected gate behavior, not a full workflow engine |
| Event | Level 2 generally; selected Level 3 tests | Preserve safe Event references and no-direct-emission rules, not event-platform infrastructure |
| Agent | Level 1/2 | Validate identity, capability, context, forbidden actions, and Human Review preservation |
| Permission | Level 2 hooks; Level 3 for protected MVP actions | Require real blocking for protected actions |
| Policy | Level 1 schema; Level 2 contextual hooks | Preserve restriction, redaction, and Human Review requirements without building a full policy-authoring platform |
| Human Review | Level 2 | Validate review reference, requirement, status, and owning-service acceptance |
| Idempotent apply | Level 3 where duplicate-sensitive | Prevent duplicate objects, Tasks, Communications, selections, and Events |
| Product UI | Outside Book 03 | Expose outcomes only; defer interaction design to Book 04 |

The MVP Execution layer is therefore a safe coordination spine.

It is not:

- a distributed orchestration platform;
- a dynamic workflow designer;
- an autonomous agent runtime;
- a full policy engine;
- a production event bus;
- a general-purpose task platform;
- a Product UI specification.

---

## 17. Worked Path: AI-Assisted Communication Review

A communication review request illustrates how the responsibility areas cooperate.

```text
1. Product submits a request concerning a Communication reference.
2. Execution resolves the Communication, Workflow and Common Contracts.
3. Execution assembles actor, Matter, document, Permission, Policy,
   AI, Human Review, version and audit context.
4. AI may prepare or revise a draft under AI Context.
5. Workflow preview explains required review, restrictions and next steps.
6. Human Review evaluates the approved evidence and draft version.
7. Execution receives the recorded review outcome.
8. Permission, Policy, version and current state are re-evaluated.
9. If all required gates pass, Execution delegates the allowed send
   request to Communication Service.
10. Communication Service accepts or rejects under its own contract.
11. The owning Service records authoritative trace.
12. Execution exposes sent, blocked, failed or retryable status with
    allowed Event references.
```

Several distinctions remain visible:

```text
AI draft is not approved content.
Approved content is not sent content.
Human Review is not send execution.
Workflow coordination is not Communication ownership.
Event reference is not a command.
Product status is not the source of execution truth.
```

This is the value of the layer map: every step has a responsibility and every protected boundary remains explicit.

---

## 18. Cross-Layer Invariants

Every later Execution Architecture chapter must preserve these invariants:

1. Source and contract resolution precede protected coordination.
2. Execution Context preserves provenance and does not replace Core truth.
3. Workflow coordinates; owning Services mutate.
4. Preview has no protected side effects.
5. Apply revalidates current context and required gates.
6. Task plan is not an active Task.
7. Permission, Policy, and Human Review remain distinct.
8. AI assistance never satisfies an authority gate.
9. Human Review does not execute downstream action.
10. Workflow and agent layers do not emit authoritative Events.
11. Event references are trace, not commands.
12. Safe pause and safe failure are valid execution outcomes.
13. Retry preserves idempotency and re-evaluates changed conditions.
14. Product consumes execution outcomes but does not define their truth.
15. Implementation packaging may change; responsibility boundaries may not drift silently.

These invariants are the acceptance test for the component map.

---

## 19. Part II Chapter Map

The rest of Part II expands the overview without changing its ownership rules.

| Chapter | Focus |
|---|---|
| 09 — Execution Object and State Model | How execution concepts reference Core-owned objects and represent operational progress without creating a competing source of truth |
| 10 — Workflow Coordination Model | Preview, apply, sequencing, service delegation, pause, resume, and failure |
| 11 — Task Lifecycle Model | Task plan, activation boundary, readiness, assignment, completion, and cancellation coordination |
| 12 — Review and Approval Lifecycle | Review request, evidence, reviewer authority, outcome, revision, and post-review revalidation |
| 13 — Communication Execution Boundary | Draft, review, approve, send handoff, record, and audit |
| 14 — Event Trace, Audit and Replay | Event observation, trace assembly, audit evidence, and controlled replay boundaries |
| 15 — Permission and Policy Gates | Independent evaluations, fail-closed behavior, restriction, redaction, and review requirements |
| 16 — Human–AI Execution Handoff | Assistance provenance, transfer of responsibility, review, acceptance, rejection, and downstream limits |

Chapter 08 provides the shared map. The later chapters supply the detailed models.

---

## 20. Architecture Anti-Patterns

The following patterns violate the Execution layer:

### 20.1 Orchestration Owns Everything

A workflow component stores domain truth, creates Tasks, sends Communications, and emits Events directly.

### 20.2 Product-Owned Gates

A Product button or screen state determines that Permission, Policy, or Human Review has passed.

### 20.3 Event-as-Command

An observed Event automatically triggers a protected action without contract and gate evaluation.

### 20.4 Plan-as-Task

A workflow preview or AI-produced task plan becomes active work without Task Service.

### 20.5 Review-as-Execution

A review approval directly sends, submits, pays, publishes, or mutates state.

### 20.6 AI Fast Lane

AI output bypasses normal gates because it has a high confidence score or came from an approved model.

### 20.7 Stale Preview Apply

Apply relies on an old preview without rechecking source state, versions, Permission, Policy, Human Review, or idempotency.

### 20.8 Trace Without Ownership

Execution writes an authoritative Event as a substitute for calling the owning Service.

Each anti-pattern collapses a responsibility boundary that Book 02 requires Book 03 to preserve.

---

## 21. Non-Goals of This Chapter

This chapter does not define:

- new Core domains, objects, services, APIs, Events, or contracts;
- an Execution Context schema;
- authoritative execution-state values;
- a workflow engine;
- a queue or worker architecture;
- database tables;
- service deployment topology;
- product screens or navigation;
- a policy authoring system;
- an event bus or event-sourcing platform;
- autonomous agent execution;
- external communication, filing, payment, or publication automation;
- detailed workflow, task, review, communication, Event, Permission, Policy, or AI handoff models.

Those detailed execution concerns belong to Chapters 09–16, while Core definitions remain in Book 02 and product design remains in Book 04.

---

## 22. Chapter Conclusion

The Execution layer is a governed coordination map, not a new owner of professional truth.

Its responsibility path is:

```text
interpret
→ resolve
→ assemble context
→ coordinate
→ evaluate gates
→ delegate or pause
→ preserve trace
→ expose outcome
```

At every state-changing boundary, the owning Service remains authoritative. Permission, Policy, Human Review, idempotency, versioning, errors, and Event trace remain independent contract concerns. AI may help prepare the path, but it cannot authorize the path. Product may expose the result, but it cannot define the result.

This overview establishes the architecture for Part II.

The next chapter examines the most delicate part of that architecture: how Book 03 can describe execution objects and operational state without creating a competing source of truth beside Book 02 Core.
