# B03-CH-09 — Execution Object and State Model

## Chapter Purpose

This chapter defines how Book 03 describes execution subjects, operational progress, state observations, transition requests, and outcomes without creating a second object model beside Book 02 Core.

The central problem is structural.

Execution must answer questions such as:

```text
Which objects are involved?
What state is each object in?
Which state is authoritative?
What work is pending?
Which transition was requested?
Which gate is blocking progress?
What changed?
What can Product safely show?
```

But Book 03 does not own Core Object meaning or lifecycle. It must not introduce an `ExecutionObject` that duplicates Trademark, Matter, Order, Task, Communication, Workflow Contract, Event, Human Review, or other Book 02 objects. It must not create a universal state list that replaces object-specific and contract-specific controlled values.

The Book 03 model is therefore reference-based and projection-based:

```text
Core Objects remain authoritative.
Contracts define valid interactions and controlled outcomes.
Execution observes, correlates, requests, coordinates and explains.
Products consume a safe projection.
```

The model in this chapter is conceptual. It does not define a new schema, database table, API payload, service, or source of truth.

---

## 1. Dependency Baseline

This chapter extends [Chapter 08 — Execution Layer Overview](B03-CH-08_Execution_Layer_Overview.md) and consumes the following Book 02 sources:

- [Core Object Specifications README](../../book-02-core-specification/core-specs/objects/README.md) — canonical object meaning, ownership, lifecycle, state, service, Event, contract, and Product-consumer rules.
- [Object Index](../../book-02-core-specification/indexes/object-index.md) — the implementation-facing inventory of Core Objects and their ownership.
- [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md) — the Domain → Object → Service → Contract → Workflow → Event → Test chain.
- [Workflow Contract Object](../../book-02-core-specification/core-specs/objects/workflow-contract.md) — Workflow Contract meaning, lifecycle, state, transition, guard, service, Event, and audit rules.
- [Task Object](../../book-02-core-specification/core-specs/objects/task.md) — Task meaning, ownership, lifecycle, assignment, status, review, and audit rules.
- [Matter Object](../../book-02-core-specification/core-specs/objects/matter.md) — Matter meaning, status, participants, execution trace, and ownership boundary.
- [Trademark Object](../../book-02-core-specification/core-specs/objects/trademark.md) — Trademark meaning, status, lifecycle, references, and service boundary.
- [Communication Object](../../book-02-core-specification/core-specs/objects/communication.md) — Communication meaning, status, review distinction, and audit boundary.
- [Event Object](../../book-02-core-specification/core-specs/objects/event.md) — Event meaning, append orientation, source, visibility, and separation from workflows, tasks, communications, and logs.
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md) — typed and cross-domain references, validation authority, visibility, and safe exposure.
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md) — operation, actor, subject, target, governance, correlation, idempotency, source, timestamp, and Event-reference trace.
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md) — version fields, compatibility, workflow version preservation, migration, and fail-closed behavior.
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md) — safe state/conflict errors, next steps, and retryability.
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md) — review status, decision, Event relationship, and version rules.
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md) — duplicate-sensitive operation and replay boundaries.
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md) — controlled Task status and governed transition response.
- [Workflow Contract API Contract](../../book-02-core-specification/core-specs/contracts/api/workflow-contract-api-contract.md) — preview, apply, task-plan, application status, idempotency, and Event-reference behavior.
- [Event API Contract](../../book-02-core-specification/core-specs/contracts/api/event-api-contract.md) — safe Event read, correlation, and audit-trail boundaries.
- [Execution System Blueprint](../planning/B03-PLN-0002_Execution_System_Blueprint.md)
- [Book 02 Dependency Map](../planning/B03-PLN-0005_Book_02_Dependency_Map.md)

The Book 02 Object Index declares objects including Workflow State, Workflow Transition, Task Status, Matter Status, Order Status, and Trademark Status. Some companion object files referenced by existing specs are not present at their expected canonical paths in the current Book 02 tree.

Book 03 must not fill those gaps by invention.

Until Book 02 supplies or confirms the missing specifications, Chapter 09 relies on:

- the Object Index;
- existing primary Object Specifications;
- existing Common Contracts;
- existing API and Workflow Contracts;
- controlled values already defined in those sources.

Missing Core specification detail remains a Book 02 dependency issue.

---

## 2. The Model Boundary

Book 02 defines a Core Object as professional meaning before data structure.

Every implementation-ready Core Object must have:

- professional meaning;
- an owner;
- a lifecycle;
- controlled state where applicable;
- service relationships;
- Event relationships;
- contract relationships.

An object is not automatically a table, DTO, JSON payload, API response, UI form, spreadsheet row, or external record.

Book 03 preserves that rule.

Execution may coordinate work around Core Objects, but it does not acquire ownership merely because it references several objects at once.

For example, an application-preparation path may involve:

- Trademark;
- Brand;
- Jurisdiction;
- Classification Recommendation;
- Document;
- Matter;
- Order;
- Workflow Contract;
- Task;
- Human Review;
- Event.

That does not justify a new giant object that copies all of them.

The Execution layer needs a governed view across references, not a replacement aggregate that becomes a competing source of truth.

---

## 3. State Is Plural

“Execution state” is often spoken of as if it were one value.

In MarkOrbit it is not.

A single operational path may simultaneously have:

```text
Trademark state
Matter state
Order state
Workflow Contract state
Workflow preview or application status
Task state
Human Review status and decision
Permission decision
Policy decision
Communication state
Error and retry condition
Event and audit trace
Product presentation state
```

These states have different owners and meanings.

They must not be flattened into one universal status such as:

```text
Pending
In Progress
Done
```

A flat status may hide that:

- the Task is complete but the Matter is still active;
- Human Review is approved but no Communication was sent;
- Workflow preview is complete but apply was never requested;
- the workflow application is applied but a downstream service rejected one operation;
- the Product shows “ready” while Permission or Policy has changed;
- an Event exists for a completed fact but does not authorize a new action.

The Execution Object and State Model therefore treats operational progress as a composition of separately governed state sources.

---

## 4. Four Layers of State Meaning

The model distinguishes four layers.

| Layer | Meaning | Authority | May Book 03 write it? |
|---|---|---|---|
| Core Object State | Professional lifecycle state of Trademark, Matter, Order, Task, Communication, Workflow Contract, and other Core Objects | Owning Object Specification and owning Service | No |
| Contract Outcome | Controlled result of validation, preview, apply, review, Permission, Policy, error, idempotency, or another governed interaction | Applicable Book 02 Contract and owning evaluator/service | No; Book 03 consumes it |
| Execution Progress View | A time-bounded coordination view assembled from references, observed states, contract outcomes, trace, and pending work | Derived by Execution under Book 03 rules; not Core truth | It may derive and expose the view, but not replace source state |
| Product Presentation State | User-facing interpretation, label, grouping, or control state | Book 04 Product System, constrained by the Execution outcome | Product may present; it must not redefine Core or Execution truth |

The layers must remain distinguishable.

```text
Core state says what the owned object is.
Contract outcome says what a governed interaction returned.
Execution view says what coordinated work currently requires.
Product state says how an allowed result is presented.
```

A change in one layer does not automatically change the others.

---

## 5. Core Object Authority

Every Core Object has one primary owner or an explicitly declared cross-cutting owner.

Secondary relationships do not transfer ownership.

Execution must therefore ask:

```text
Which object owns this fact?
Which service owns this state change?
Which contract exposes the allowed interaction?
Which Event proves the completed change?
```

Examples:

| Fact or action | Authority |
|---|---|
| Trademark professional status | Trademark Object and Trademark Service |
| Matter status | Matter Object and Matter Service |
| Order status | Order Object and Order Service |
| Active Task status | Task Object and Task Service |
| Workflow Contract state/application | Workflow Contract Object, Contract, and Service |
| Communication status or send result | Communication Object and Communication Service |
| Review status and decision | Human Review Contract plus owning-service reliance rules |
| Event record | Event Service or the state-changing owning Service under the Event specification |

Book 03 may coordinate a request to the authority. It may observe the response. It may preserve the trace. It may derive a progress explanation.

It may not assign itself ownership.

---

## 6. Reference-Based Execution

Execution should carry references to Core Objects rather than duplicate their meaning.

The Reference Contract provides:

- typed references;
- object type;
- object reference ID;
- reference domain;
- safe label;
- optional observed status;
- owner-service information;
- restricted-field omission;
- cross-domain relationship references;
- validation results.

The important rules are:

```text
The owning Service validates its own reference.
A valid reference does not imply read Permission.
A readable reference does not imply mutation Permission.
Reference status does not replace authoritative object state.
Safe labels must not expose restricted data.
Event references are trace, not commands.
```

An Execution path may hold a set of references such as:

```text
trademark reference
matter reference
order reference
workflow contract reference
task references
Human Review reference
communication reference
event references
```

This set is not a new Core Object. It is the subject map used to locate authorized sources and preserve coordination.

### 6.1 Reference Validation Is Continuous

A reference that was valid during preview may become invalid, restricted, archived, revoked, or context-mismatched before apply.

Execution must validate references at the point required by the governing contract.

It must not assume:

```text
validated once = valid forever
readable = mutable
visible = unrestricted
linked = owned
Event exists = action authorized
```

### 6.2 Embedded Copies Are Not Authority

A workflow result, Task summary, AI summary, audit view, or Product cache may include an object's safe label or observed status.

That embedded value is not automatically current.

When a protected decision depends on current state, Execution must resolve the authorized source again or use a versioned snapshot explicitly allowed by contract.

---

## 7. The Execution Progress View

Book 03 needs a way to explain coordinated progress without creating a new authoritative object.

This chapter calls that conceptual result the **Execution Progress View**.

The term describes a projection responsibility. It does not define a Core Object, persistent schema, API resource, or service.

The view should be able to answer:

| Question | Required source |
|---|---|
| What work is being coordinated? | Workflow/Task context and subject references |
| Which Core Objects are involved? | Reference Contract and Object Index |
| What state was observed? | Owning services or contract-valid snapshots |
| When and under which version? | Versioning and audit context |
| What is requested but not yet applied? | Workflow preview, task plan, or transition request |
| Which gates have outcomes? | Permission, Policy, Human Review, validation, idempotency |
| What is blocking or missing? | Safe Error Contract and governing workflow |
| Which owning Service acted? | Service result and audit source |
| What changed? | Previous/current state response and allowed Event references |
| What can happen next? | Contract-valid next step, not an AI guess |
| What may Product display? | Safe, permissioned, policy-compliant projection |

An Execution Progress View is therefore a joined interpretation of governed sources.

It must expose its limits:

- observation time;
- source scope;
- version scope;
- omitted or restricted fields;
- unresolved dependencies;
- AI involvement;
- review requirement;
- stale or refresh-required conditions where known.

---

## 8. State Dimensions, Not a Universal Enum

Execution progress should be understood as a state vector with independent dimensions.

### 8.1 Subject State

The authoritative or contract-valid observed state of each referenced Core Object.

Examples:

- Trademark status;
- Matter status;
- Order status;
- Communication status;
- Task status.

### 8.2 Workflow State

The status of the applicable Workflow Contract, preview, task-plan preparation, or workflow application.

Book 02 already defines controlled values such as:

- Workflow Contract: Draft, Active, Deprecated, Suspended, Archived;
- Preview: Completed, Partial, NotApplicable, PolicyRestricted, PermissionDenied, RequiresHumanReview, Error;
- Application: Applied, PartiallyApplied, NotApplied, PolicyRestricted, PermissionDenied, RequiresHumanReview, Conflict, Error;
- Task plan: Completed, Partial, NoTaskSuggested, PolicyRestricted, PermissionDenied, RequiresHumanReview, Error.

Book 03 should use those values where they apply instead of inventing synonyms.

### 8.3 Task State

Task status belongs to Task.

Book 02 defines controlled Task values including:

- Draft;
- Open;
- Assigned;
- InProgress;
- Waiting;
- Blocked;
- UnderReview;
- Completed;
- Cancelled;
- Archived.

A completed Task does not imply that its Matter, Order, Communication, workflow, filing, or other professional outcome is complete.

### 8.4 Review State

Human Review has its own status and decision.

Review status may include Requested, InReview, Completed, Rejected, Escalated, Expired, Cancelled, or NotRequired.

Review decision may include Approved, Rejected, Revised, Escalated, NeedsMoreInformation, or NotApplicable.

A completed or approved review does not execute the downstream action.

### 8.5 Governance State

Permission and Policy results remain separate.

Execution must not compress them into a generic “authorized” flag that hides whether:

- Permission allowed;
- Policy allowed;
- Policy restricted or redacted;
- Policy required Human Review;
- an unknown result failed closed.

### 8.6 Failure and Retry Condition

An operation may have a safe error, conflict, retryable failure, or non-retryable failure.

This condition describes the attempted operation. It does not automatically become the lifecycle state of every referenced object.

### 8.7 Trace Condition

Execution may know that:

- no authoritative action occurred;
- delegation was attempted;
- an owning Service succeeded;
- an owning Service rejected;
- Event references were returned;
- an Event is restricted;
- audit context is partial.

Trace condition explains evidence availability. It is not a business state.

---

## 9. Derived Execution Conditions

For coordination and Product consumption, Book 03 may derive explanations such as:

- ready for evaluation;
- missing required context;
- waiting for Human Review;
- blocked by Permission;
- restricted by Policy;
- transition requested;
- delegated to owning Service;
- failed safely;
- retry may be available;
- completed with trace;
- refresh required.

These phrases are not a new canonical state enum.

They are derived conditions that must point back to their sources.

For example:

```text
Waiting for Human Review
  derived from:
    human_review_required = true
    no acceptable completed review reference
    current Permission/Policy context
    applicable workflow step
```

Or:

```text
Completed with trace
  derived from:
    owning-service success response
    expected current state where applicable
    required Event references or audit context
    no unresolved protected downstream action
```

If sources disagree or are incomplete, Execution should expose uncertainty or a safe unresolved condition. It must not choose the most convenient status.

---

## 10. The Governed Transition Path

Execution may request a state transition. It does not perform the transition directly.

The canonical path is:

```text
1. Resolve the target Core Object reference.
2. Read or validate the current authorized state.
3. Resolve the owning Service and applicable contract.
4. Assemble actor, organization, Permission, Policy, review,
   version, idempotency and audit context.
5. Submit a transition request to the owning Service.
6. Owning service validates the transition.
7. Owning service accepts or rejects.
8. If accepted, owning Service changes state.
9. Owning service or Event Service records allowed Event trace.
10. Execution receives previous/current state and trace references.
11. Execution refreshes its Progress View.
12. Product receives a safe projection.
```

The Task API demonstrates this boundary: a Task status transition routes through Task Service and returns previous and current status. Task completion does not imply Matter, Order, Communication, or filing completion.

The same principle applies across Core Objects.

### 10.1 Requested State Is Not Current State

A requested transition must be kept separate from the current authoritative state.

```text
requested_status = Completed
```

does not mean:

```text
current_status = Completed
```

until the owning Service accepts the request.

### 10.2 Review Is Not Transition

A Human Review decision may satisfy one gate for a transition.

It does not change the target object by itself.

After review, Execution must refresh:

- source state;
- Permission;
- Policy;
- version;
- other required gates.

Then it may request the owning Service action.

### 10.3 Event Is Not Transition Authority

An Event may prove that a transition occurred.

An Event reference does not grant authority to repeat, reverse, or infer a new transition.

---

## 11. Observation Time, Version and Staleness

Execution works with observations made at particular times and under particular versions.

A view can become stale because:

- another actor changed the object;
- a Task was reassigned;
- a review expired;
- Permission changed;
- Policy changed;
- a document version changed;
- the Workflow Contract was deprecated;
- a service completed or rejected an operation;
- an external dependency changed;
- the Product cached an earlier projection.

The model must therefore preserve enough information to distinguish:

```text
current authoritative state
observed state at a known time
requested future state
historical state shown for audit
derived Product presentation
```

### 11.1 Preview Does Not Lock State

Workflow preview evaluates a possible path from the context available at preview time.

It does not reserve or lock all referenced object states.

Apply must revalidate.

### 11.2 Versions Preserve Meaning

Workflow application must preserve the Workflow Contract version used.

Contract and schema versions must not be silently changed. Historical records must preserve the version that governed the operation. Unsupported or removed versions must fail safely.

### 11.3 Conflicts Are Valid Outcomes

If current state differs from the state required by a transition, the owning contract may return:

- StateInvalid;
- StateTransitionNotAllowed;
- Conflict;
- DuplicateRejected;
- IdempotencyConflict.

Execution should expose the safe conflict and next step. It must not overwrite the newer state or retry blindly.

---

## 12. Multi-Object Coordination Without a Giant Aggregate

Professional execution usually spans several Core Objects.

Book 03 coordinates them through a reference graph and readiness conditions.

It should not copy their fields into a monolithic execution record and declare that copy authoritative.

A multi-object view should preserve:

- each object reference;
- each object's owner;
- the state source for each observation;
- the version and observation time where relevant;
- the cross-domain relationship;
- Permission and Policy limits;
- the operation that depends on the state;
- the Event or audit reference proving a completed change.

### 12.1 Partial Progress Is Normal

Different objects may advance at different times.

For example:

```text
Trademark reference valid
Matter active
Order confirmed
Document requirement incomplete
Classification recommendation under review
Task assigned
Workflow preview completed
Workflow apply not requested
```

The correct execution condition may be:

```text
Application preparation is blocked by missing Document context
and pending Classification Human Review.
```

It is not:

```text
Application = InProgress
```

unless an owning Book 02 object or contract defines that exact meaning.

### 12.2 Readiness Is Derived

Readiness is often a governed predicate over multiple sources.

It may depend on:

- required references;
- allowed object states;
- required documents;
- evidence;
- completed review;
- Permission;
- Policy;
- Workflow Contract version;
- absence of blocking conflicts.

A readiness result is not a new professional fact. It is a derived execution condition used to determine whether the next governed request may be made.

---

## 13. Workflow, Task, Review and Business Outcome Must Stay Separate

Several controlled statuses may look similar while representing different facts.

| Status source | Example | What it proves | What it does not prove |
|---|---|---|---|
| Workflow preview | Completed | Preview finished | Workflow applied or business work completed |
| Workflow application | Applied | Contract application accepted | Every downstream business objective completed |
| Task | Completed | Task Service accepted Task completion | Matter, Order, Communication, filing, or legal outcome completed |
| Human Review | Completed / Approved | Accountable review occurred and decision was recorded | Downstream action executed |
| Communication | Approved draft or sent status | Communication-specific state | Matter or professional conclusion completed |
| Event reference | Event exists | A producer recorded an allowed fact | New command is authorized |
| Product label | Ready / Done | Product interpretation of allowed outcome | Core state changed |

This separation is essential for truthful execution.

A system that collapses these statuses will create false completion.

---

## 14. Failure, Retry and State

Failure belongs to the attempted operation unless the owning object defines a corresponding lifecycle transition.

For example:

```text
Document upload failed
```

does not necessarily mean:

```text
Matter failed
Trademark failed
Workflow failed permanently
```

The Error Contract distinguishes safe next steps and retryability.

A retryable operation may succeed later without semantic change.

A non-retryable operation requires changed input, review, authority, or escalation.

Execution should preserve:

- the failed operation;
- safe error category and code;
- affected references;
- correlation;
- whether the error is retryable;
- required next step;
- whether any partial service action occurred;
- Event or audit references where allowed;
- the current authoritative state after failure.

Retry must not assume that state remained unchanged. It must revalidate applicable sources and idempotency context.

---

## 15. Audit and State Reconstruction

Audit Context connects an execution path without becoming the Core Object itself.

It may preserve:

- operation name and category;
- operation result;
- actor and organization;
- AI or agent participation;
- subject and target references;
- Permission and Policy decision references;
- Human Review reference;
- correlation and causation;
- idempotency;
- Event references;
- source;
- requested and completed timestamps.

This information helps answer:

```text
What was attempted?
Against which object?
Under which authority?
Using which version and context?
What did the owning Service return?
Which trace supports the result?
```

Audit Context may reference Events but does not create them. Event success or failure may also need to remain distinct from business-operation success.

Chapter 14 will define trace, audit and replay boundaries in detail.

---

## 16. Human and AI State Interpretation

Humans and AI may help interpret state, but neither may silently replace the owning source.

### 16.1 AI Assistance

AI may:

- summarize multiple object states;
- identify missing references;
- compare observed and required states;
- explain a safe error;
- propose a next-step checklist;
- summarize Event and audit trace;
- identify possible staleness;
- prepare review context.

AI must disclose:

- source scope;
- missing context;
- observation limits;
- version limits where known;
- policy omissions;
- whether Human Review is required.

AI must not:

- create a Core Object;
- set authoritative object state;
- complete a Task;
- infer approval from silence;
- convert review status into downstream completion;
- resolve a conflict by choosing a preferred value;
- treat a Product label as Core truth;
- emit an Event;
- claim that a protected transition occurred without owning-service evidence.

### 16.2 Human Review

Human Review can evaluate evidence and record a decision.

It remains separate from:

- Permission;
- Policy;
- state mutation;
- Task completion;
- Communication sending;
- workflow apply;
- official submission.

The owning Service decides whether the review satisfies the action requirement.

---

## 17. Product Projection

Book 04 products need a view that users can understand.

Product may present:

- current visible source state;
- observed-at time;
- pending transition;
- required next action;
- waiting-for-review condition;
- blocking Permission or Policy outcome;
- retry availability;
- partial completion;
- latest allowed trace;
- restricted-field omission.

Product must not:

- overwrite Core state through a display label;
- hide that a value is derived;
- represent requested state as current state;
- treat cached state as current without refresh rules;
- merge independent statuses into false completion;
- infer Human Review;
- expose restricted state detail;
- use an Event as a command;
- allow AI text to become an authoritative badge.

A Product label may simplify language, but the underlying Execution Progress View must retain the source distinction.

---

## 18. Worked Example: Trademark Application Preparation

Consider an application-preparation path involving:

- Trademark;
- Matter;
- Order;
- Jurisdiction;
- Classification Recommendation;
- Document;
- Workflow Contract;
- Tasks;
- Human Review;
- Events.

### 18.1 Initial Observation

Execution resolves the references and obtains authorized observations:

```text
Trademark: valid reference; current status from Trademark Service
Matter: active
Order: confirmed
Jurisdiction Requirement: current version identified
Classification Recommendation: prepared; Human Review required
Required Document: missing
Workflow Contract: active
Workflow preview: Completed
Task plan: Completed
Active Tasks:
  - collect document: Assigned
  - review classification: UnderReview
Workflow apply: not requested
```

### 18.2 Derived Progress View

Execution may derive:

```text
Application preparation is not ready for apply.

Blocking conditions:
- required Document missing;
- Classification Human Review incomplete.

Current work:
- Document collection Task assigned;
- Classification review Task under review.

No protected application submission has occurred.
```

This is a coordination explanation.

It is not a new Trademark state, Matter state, Order state, or universal “Application” state.

### 18.3 AI Participation

AI may summarize the missing information and prepare a customer-facing draft requesting the Document.

The draft is not approved or sent.

### 18.4 State Change

The user supplies the Document.

Execution requests Document Service to record it under the applicable contract. If accepted:

- Document Service owns the new Document state;
- allowed Event trace is recorded;
- Execution refreshes the reference and readiness conditions.

The Human Reviewer then completes the Classification review. The recorded decision does not apply the workflow.

Execution refreshes Permission, Policy, object state, Workflow Contract version, review, and idempotency context before apply.

### 18.5 Apply Outcome

Workflow Contract Service may return:

```text
application_status = Applied
created_task_reference_ids = [...]
event_reference_ids = [...]
```

This proves the workflow application result.

It does not prove that an official filing was submitted or that the Matter is complete.

The Product may show:

```text
Application preparation workflow applied.
Next tasks created.
Official submission not completed.
```

That presentation remains truthful because each state source is preserved.

---

## 19. State Invariants

Every Execution state model must preserve these invariants:

1. Core Object meaning and lifecycle remain in Book 02.
2. Every authoritative state has an owning object/service or governing contract.
3. Execution references objects; it does not clone their authority.
4. A valid reference does not imply read or mutation Permission.
5. Observed state is time- and version-bounded.
6. Requested state is not current state.
7. Preview does not lock state or perform apply.
8. Apply revalidates current state and gates.
9. Human Review is not downstream execution.
10. Task completion is not Matter, Order, Communication, filing, or professional completion.
11. Workflow application is not universal business completion.
12. Event reference is trace, not command.
13. Derived execution conditions cite their sources.
14. Product labels do not become Core state.
15. AI interpretation does not become professional or state truth.
16. Partial progress remains visible.
17. Conflict and safe failure are valid outcomes.
18. Retry revalidates state, version, authority, and idempotency.
19. Missing Book 02 state specifications are routed back to Book 02.
20. No Book 03 term silently becomes a new Core Object.

---

## 20. Handoff to Later Chapters

Chapter 09 defines the shared state discipline for the remaining Execution Architecture chapters.

| Chapter | State responsibility |
|---|---|
| 10 — Workflow Coordination Model | Workflow preview, apply, pause, resume, delegation, partial application, and conflict |
| 11 — Task Lifecycle Model | Task plan, active Task creation, assignment, status transition, review, completion, cancellation, and archive |
| 12 — Review and Approval Lifecycle | Review request, status, decision, expiry, revision, and post-review revalidation |
| 13 — Communication Execution Boundary | Draft, reviewed, approved, sent, failed, and recorded Communication distinctions |
| 14 — Event Trace, Audit and Replay | Event observation, correlation, reconstruction, and no-command replay boundary |
| 15 — Permission and Policy Gates | Independent decision state, fail-closed behavior, restriction, redaction, and review requirement |
| 16 — Human–AI Execution Handoff | AI output status, provenance, human acceptance/rejection, and authority transfer limits |

Later chapters may add detail. They must not collapse the state layers defined here.

---

## 21. State Anti-Patterns

### 21.1 The Universal Status Field

One `status` value attempts to represent object, workflow, Task, review, Permission, Policy, error, and Product state.

### 21.2 The Execution Super-Object

A new object copies Trademark, Matter, Order, Task, Communication, review, and Event fields and becomes the practical source of truth.

### 21.3 Requested Equals Current

A transition request is displayed or stored as if the owning Service already accepted it.

### 21.4 Completed Means Everything

A completed preview, Task, review, or workflow application is treated as universal business completion.

### 21.5 Event-Driven Mutation Without Contract

An observed Event directly changes another object's state without an explicit command and owning-service contract.

### 21.6 Cached Product Truth

A Product cache or badge overrides a newer Core state or hides observation time.

### 21.7 AI-Repaired State

AI resolves conflicting sources by choosing or generating the value that appears most plausible.

### 21.8 Review as State Mutation

A review decision directly changes the target object's lifecycle state.

### 21.9 Retry from Stale State

A failed operation is repeated without refreshing source state, version, Permission, Policy, Human Review, and idempotency.

### 21.10 Book 03 Fills Book 02 Gaps

A missing Core status specification is silently defined inside an Execution chapter or Product implementation.

Each anti-pattern creates false authority.

---

## 22. MVP Depth

The Book 03 MVP needs enough state discipline to prevent unsafe execution.

It should support:

- typed Core references;
- owning-service validation;
- contract-valid observed state;
- workflow preview/application outcomes;
- Task status observation and governed transition requests;
- Human Review status and decision references;
- Permission and Policy outcomes;
- safe errors and retryability;
- version and observation context;
- idempotency context for duplicate-sensitive operations;
- Event and audit references;
- derived progress explanations;
- Product-safe projections.

It does not require:

- a new Execution Object database;
- a universal execution-state schema;
- Event sourcing;
- a state synchronization platform;
- a distributed cache invalidation system;
- a generic state machine engine;
- a full workflow engine;
- a Product dashboard;
- autonomous state reconciliation by AI;
- completion of missing Book 02 Object Specifications inside Book 03.

The MVP goal is a truthful, reference-based progress view and a governed transition path.

---

## 23. Non-Goals of This Chapter

This chapter does not define:

- `ExecutionObject` as a Core Object;
- a persistent Execution Progress View schema;
- database tables or storage rules;
- authoritative object fields;
- new object lifecycle values;
- new Workflow, Task, Matter, Order, Trademark, Communication, Review, or Event statuses;
- missing Book 02 status object specifications;
- API endpoints;
- service interfaces;
- concurrency implementation;
- event-sourcing architecture;
- UI labels, colors, pages, or controls;
- automated state mutation;
- AI authority to resolve state;
- Product ownership of state truth.

It defines how Book 03 coordinates and explains state while Book 02 remains authoritative.

---

## 24. Chapter Conclusion

Execution needs a view of objects and state, but it does not need another source of truth.

The safe model is:

```text
Reference Core Objects
→ observe authorized state
→ preserve time and version
→ separate requested from current
→ consume contract outcomes
→ derive a bounded progress view
→ request transitions through owning Services
→ preserve Event and audit trace
→ expose a safe Product projection
```

Core Object state remains authoritative.

Contract outcomes remain controlled.

Execution Progress View remains derived and source-linked.

Product presentation remains a consumer.

Human Review remains accountable review, not mutation.

AI remains interpretation and preparation, not authority.

This state discipline prevents false completion, stale execution, ownership drift, and Product-owned truth.

The next chapter applies the model to workflow coordination: how preview, apply, sequencing, delegation, pause, resume, partial application, failure, and retry operate without turning Workflow into a new owner of Core state.
