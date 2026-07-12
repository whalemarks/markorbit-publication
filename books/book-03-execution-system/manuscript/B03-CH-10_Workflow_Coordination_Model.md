# B03-CH-10 — Workflow Coordination Model

## Chapter Purpose

This chapter defines how Book 03 coordinates Workflow Contracts without turning Workflow into a new owner of Core behavior or state.

Chapter 08 mapped the Execution layer. Chapter 09 separated Core Object state, Contract outcomes, derived Execution progress and Product presentation. Chapter 10 now defines the operational path that connects those sources.

The model must answer:

```text
Which Workflow Contract applies?
What may be previewed?
What must be reviewed?
When may apply be requested?
Which services own the effects?
How are Tasks created?
How are partial outcomes represented?
How does execution pause, resume, fail and retry?
What trace proves the result?
```

The model is contract-led and service-delegated.

```text
Workflow coordinates.
Workflow Contract constrains.
Owning Services act.
Task Service creates active Tasks.
Human Review gates protected work.
Events preserve trace.
```

This chapter does not define a workflow engine or a new Workflow schema.

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 08 — Execution Layer Overview](B03-CH-08_Execution_Layer_Overview.md)
- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)

It consumes:

- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Workflow Contract Object](../../book-02-core-specification/core-specs/objects/workflow-contract.md)
- [Workflow Contract API Contract](../../book-02-core-specification/core-specs/contracts/api/workflow-contract-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [Core Traceability Matrix](../../book-02-core-specification/core-specs/TRACEABILITY.md)
- [MVP Cut v0.1](../../book-02-core-specification/core-specs/implementation/mvp-cut-v0.1.md)

Book 03 coordinates only approved Workflow Contracts and existing controlled outcomes. Missing Workflow or transition definitions remain Book 02 dependencies.

---

## 2. Workflow Coordination Boundary

Workflow coordination owns sequencing and dependency management.

It does not own:

- domain meaning;
- object state;
- service behavior;
- active Task state;
- Human Review authority;
- Permission or Policy decisions;
- Communication transmission;
- official submission;
- Event emission;
- professional truth.

A workflow may request service behavior through governed contracts. It may collect service outcomes. It may decide whether the next contract-defined step is eligible for evaluation.

It may not perform the service behavior itself.

The boundary is:

```text
Workflow decides what should be coordinated next.
Owning Service decides whether and how its behavior occurs.
```

---

## 3. Coordination Lifecycle

A governed workflow path uses seven coordination stages.

```text
1. Resolve
2. Preview
3. Review
4. Apply
5. Delegate
6. Observe
7. Expose outcome
```

Not every path reaches Apply.

A valid path may stop during resolution, preview, review or gate evaluation.

### 3.1 Resolve

Execution identifies:

- Workflow Contract reference and version;
- target object references;
- owning Services;
- required Common Contracts;
- required Permission and Policy scopes;
- Human Review requirements;
- idempotency requirements;
- expected Task-plan and Event behavior.

### 3.2 Preview

Preview evaluates applicability and proposed steps without protected side effects.

### 3.3 Review

If policy or professional risk requires Human Review, the workflow pauses and preserves the review context.

### 3.4 Apply

Apply is a protected, duplicate-sensitive request to Workflow Contract Service.

### 3.5 Delegate

Workflow Contract Service coordinates allowed calls to owning Services. Active Task creation routes through Task Service.

### 3.6 Observe

Execution receives service results, Task references, application status, safe errors and Event references.

### 3.7 Expose Outcome

Execution derives a source-linked progress view for Product and future coordination.

---

## 4. Preview Model

Preview is assistance.

It may explain:

- whether a Workflow Contract appears applicable;
- visible proposed steps;
- missing context;
- required references;
- proposed Task plan;
- review requirements;
- Permission or Policy restrictions;
- omitted fields;
- source scope;
- expected next action.

Preview must not:

- apply the workflow;
- create active Tasks;
- mutate Core Objects;
- send Communications;
- select a provider finally;
- submit a filing;
- emit Events;
- certify professional truth.

Book 02 controls preview outcomes such as Completed, Partial, NotApplicable, PolicyRestricted, PermissionDenied, RequiresHumanReview, Error and Unknown.

Book 03 should preserve those outcomes.

### 4.1 Preview Is Time-Bounded

Preview describes a possible path from the state observed at preview time.

It does not reserve:

- object state;
- Task capacity;
- reviewer authority;
- Permission;
- Policy;
- service availability;
- Workflow Contract version.

Apply must revalidate.

### 4.2 Preview Explanation Is Not a Contract Change

AI or Product may explain the preview in simpler language.

The explanation does not alter:

- applicability;
- step order;
- review requirement;
- omitted fields;
- protected-action boundary;
- owning-service responsibility.

---

## 5. Step Coordination

Workflow steps come from the applicable Workflow Contract.

A step may describe:

- source condition;
- required references;
- required validation;
- required service;
- review gate;
- Permission and Policy gate;
- proposed Task type;
- allowed outcome;
- safe failure;
- next eligible step.

A workflow may coordinate branching where the contract allows it.

It must not invent new professional branches at runtime.

### 5.1 Eligibility Is Not Completion

A step may be eligible because its prerequisites appear satisfied.

That does not mean the step completed.

### 5.2 Skipped Steps Need Meaning

An apply result may return skipped steps with safe reasons.

Skipping must be contract-valid.

A step must not be silently skipped because:

- AI considered it low risk;
- Product hid it;
- data was inconvenient;
- a prior run succeeded;
- the service was unavailable;
- Human Review was slow.

### 5.3 Parallel Coordination Does Not Merge Ownership

Independent steps may be evaluated or delegated in parallel where contracts permit.

Parallel execution does not authorize:

- shared state mutation outside owning Services;
- inconsistent versions;
- duplicated Tasks;
- duplicated Events;
- bypassed gates.

---

## 6. Apply Model

Apply requests governed effects.

Apply requires:

- current Workflow Contract version;
- current target references;
- validated context;
- Permission;
- Policy;
- Human Review where required;
- idempotency key;
- apply scope;
- Task creation mode where applicable;
- audit and correlation context.

The apply request routes through Workflow Contract Service.

The service may return:

- workflow application reference;
- application status;
- created Task references;
- skipped steps;
- applied time;
- restricted-field omission;
- Event references;
- idempotency result.

Book 02 controls application outcomes including Applied, PartiallyApplied, NotApplied, PolicyRestricted, PermissionDenied, RequiresHumanReview, Conflict, Error and Unknown.

### 6.1 Apply Is Not Business Completion

Applied means that Workflow Contract Service accepted the governed application.

It does not prove:

- every downstream service completed;
- every Task completed;
- every review completed;
- a Communication was sent;
- an official filing occurred;
- a Matter closed;
- a professional objective succeeded.

### 6.2 Apply Must Revalidate

Apply must not trust a stale preview.

It rechecks:

- target references;
- current object state;
- Workflow Contract status and version;
- Permission;
- Policy;
- Human Review;
- idempotency;
- service eligibility;
- contract compatibility.

---

## 7. Service Delegation

Workflow coordinates services through their contracts.

It does not mutate service-owned state.

For every delegated action, the workflow must know:

- owning Service;
- request contract;
- target reference;
- allowed operation;
- gate evidence;
- version;
- idempotency behavior;
- expected safe response;
- expected trace.

Possible outcomes include:

- accepted;
- rejected;
- blocked;
- requires review;
- conflict;
- partial;
- retryable failure;
- non-retryable failure.

Execution must preserve the service result rather than translate every rejection into a generic workflow error.

### 7.1 Delegation Order

Contract-defined dependencies determine order.

For example:

```text
Document validation
→ Classification review
→ filing-readiness review
→ protected submission handoff
```

The workflow may not reverse the order merely because later information is already available.

### 7.2 Delegation Does Not Transfer Authority

Passing review, Permission and Policy context to a service does not force success.

The owning Service applies its own state and contract rules.

---

## 8. Task Plan and Active Task Boundary

Workflow preview or task-plan preparation may propose work.

A proposed Task may include:

- type;
- title;
- subject reference;
- suggested owner role;
- due-date basis;
- priority;
- review requirement;
- source step;
- policy restriction.

A task plan is not an active Task.

Active creation routes through Task Service after applicable gates.

```text
Proposed Task
→ reviewed/allowed Task plan
→ Task Service create request
→ active Task reference or safe rejection
```

Idempotent apply must not duplicate Tasks.

Chapter 11 defines the full Task lifecycle.

---

## 9. Review Coordination

A workflow may identify a Review Gate.

It may:

- assemble review evidence;
- identify the required reviewer role;
- create or reference a review request through the owning contract;
- pause;
- consume the recorded outcome;
- revalidate after review.

It may not:

- perform Human Review;
- mark AI output as reviewed;
- approve on behalf of a reviewer;
- treat review completion as downstream execution.

After a review outcome, Execution refreshes:

- target state;
- Workflow Contract version;
- Permission;
- Policy;
- review validity;
- other changed context.

Chapter 12 defines this lifecycle.

---

## 10. Permission and Policy Coordination

Workflow uses Permission and Policy as independent gates.

```text
PermissionAllowed does not imply PolicyAllowed.
PolicyAllowed does not imply PermissionAllowed.
Unknown Permission fails closed.
Unknown Policy fails closed where policy-controlled.
```

Policy may:

- block;
- redact;
- omit;
- downgrade;
- require Human Review.

Workflow must preserve the restriction in preview, apply and Product outcome.

It must not ask AI to reconstruct omitted fields.

---

## 11. Partial Application

Partial application is a first-class outcome.

It means some allowed effects occurred while others did not.

A partial outcome should preserve:

- completed delegations;
- rejected delegations;
- skipped steps;
- active Task references created;
- state changes accepted by owning Services;
- unresolved review;
- safe errors;
- Event references;
- retryable and non-retryable portions.

Partial application must not be exposed as full completion.

### 11.1 No Rollback by Assumption

Book 03 must not assume that all partial effects can be reversed.

Rollback requires an owning-service contract.

If no rollback contract exists, Execution records the partial result and routes the next authorized action.

### 11.2 Retry Scope Must Be Bounded

Retry should target only allowed incomplete operations.

It must not duplicate completed effects.

---

## 12. Pause and Resume

A workflow may pause because of:

- missing context;
- missing document or evidence;
- Human Review;
- Permission or Policy restriction;
- service unavailability;
- conflict;
- unsupported version;
- non-retryable error;
- required external human action.

Pause is not failure unless the governing contract says so.

A resumable path must preserve:

- workflow application reference;
- current source references;
- completed and incomplete steps;
- review references;
- safe errors;
- versions;
- idempotency context;
- trace;
- required next action.

Resume must revalidate changed conditions.

A resume action is not a promise to continue from exactly the same state.

---

## 13. Failure and Retry

Workflow failure should identify the failed operation and safe next step.

The Error Contract may direct:

- fix request;
- validate reference;
- request Permission;
- request Policy review;
- request Human Review;
- use owning Service;
- retry later;
- check downstream service;
- contact support.

Retryability means the same semantic request may succeed later.

It does not mean gates may be skipped.

Before retry, Execution checks:

- current object state;
- completed effects;
- idempotency result;
- Workflow Contract version;
- Permission;
- Policy;
- Human Review;
- service condition.

Same idempotency key with a different semantic request must fail safely.

---

## 14. Versioning and Change Control

Workflow coordination is version-aware.

Execution preserves:

- Workflow Contract reference;
- Workflow Contract version;
- applicable Common Contract versions;
- API version where used;
- source versions relevant to the action;
- version used by AI output where it is consumed.

Workflow versions must not silently:

- reorder protected steps;
- remove gates;
- expand AI capability;
- change Event meaning;
- change Task creation behavior;
- change professional outcomes.

A breaking change requires Book 02 version governance.

A paused workflow resumed under a different version requires compatibility review or explicit migration.

---

## 15. Event and Audit Trace

Workflow does not emit authoritative Events directly.

Owning services emit Events for completed facts where specifications allow.

Workflow application may return Event references.

Task Service may emit Task-created Events.

Execution uses Audit Context to connect:

- workflow request;
- actor;
- target;
- Permission and Policy decisions;
- Human Review;
- idempotency;
- service delegations;
- application result;
- Event references;
- timestamps.

Event references remain trace, not commands.

Chapter 14 defines replay boundaries.

---

## 16. AI-Assisted Workflow Coordination

AI may assist with:

- applicability explanation;
- context summary;
- missing-information detection;
- proposed step explanation;
- task-plan preparation;
- review-context preparation;
- safe error explanation;
- audit-trace summary.

AI must not:

- apply a workflow;
- change a Workflow Contract;
- create active Tasks;
- perform Human Review;
- select a provider finally;
- send Communications;
- submit official filings;
- mutate Core state;
- emit Events;
- certify completion.

AI output remains a preview or preparation input.

---

## 17. Worked Example: Office Action Response Preparation

A response-preparation workflow may involve:

- Trademark;
- Matter;
- deadline context;
- official document;
- evidence;
- Communication draft;
- Tasks;
- Human Review.

### 17.1 Preview

Execution resolves the Workflow Contract and current references.

Preview may identify:

- deadline verification required;
- official document missing or present;
- evidence gaps;
- proposed research Task;
- proposed drafting Task;
- Human Review requirement;
- Permission and Policy restrictions.

No active Task or Communication is created by preview.

### 17.2 Review and Apply

After required context exists:

- deadline is confirmed by an authorized source and reviewer;
- evidence context is reviewed;
- Permission and Policy are evaluated;
- apply is requested with idempotency.

Workflow Contract Service may delegate active Task creation to Task Service and draft creation to Communication Service where allowed.

### 17.3 Partial Outcome

Suppose:

- research Task created;
- draft-preparation Task created;
- Communication draft rejected because a required recipient context is missing.

The outcome is PartiallyApplied.

Execution exposes:

```text
Research and drafting Tasks created.
Communication draft not created.
Recipient context required.
No external Communication sent.
No official response submitted.
```

This is truthful coordination.

---

## 18. Workflow Invariants

1. Workflow uses an approved Contract.
2. Workflow coordinates; owning Services act.
3. Preview has no protected side effects.
4. Apply is protected and idempotent.
5. Apply revalidates current context.
6. Proposed Tasks are not active Tasks.
7. Task Service creates active Tasks.
8. Human Review is not apply or downstream execution.
9. Permission and Policy remain independent.
10. Partial application remains visible.
11. Completed steps are not repeated blindly.
12. Retry preserves idempotency and current state.
13. Workflow does not send Communications directly.
14. Workflow does not submit filings directly.
15. Workflow does not emit Events directly.
16. Applied is not universal completion.
17. Version changes do not silently alter execution.
18. Product does not own workflow truth.
19. AI does not apply or approve.
20. Missing Book 02 workflow rules are routed back to Book 02.

---

## 19. Workflow Anti-Patterns

### 19.1 Preview With Side Effects

Preview creates Tasks, drafts, Events or state changes.

### 19.2 Workflow God Service

Workflow owns domain state and implements every behavior.

### 19.3 Apply From Stale Preview

Apply uses old state and old gate results.

### 19.4 Silent Partial Success

Some effects occur, but Product displays complete.

### 19.5 Task Plan Equals Task

AI or preview output creates active work.

### 19.6 Review Equals Apply

Approval triggers effects without revalidation.

### 19.7 Retry Everything

A partial workflow reruns completed effects.

### 19.8 Version Drift

Paused work resumes under changed rules without compatibility review.

### 19.9 Event as Next-Step Command

An Event reference automatically executes a new step.

### 19.10 AI Chooses the Branch

AI invents a professional branch not authorized by the Workflow Contract.

---

## 20. MVP Depth

The MVP coordination model should support:

- Workflow Contract resolution;
- preview validation;
- apply validation;
- task-plan preparation;
- service delegation boundaries;
- Permission and Policy gates;
- Human Review gates;
- idempotent apply;
- partial outcomes;
- safe pause;
- safe errors;
- bounded retry;
- version preservation;
- Event references;
- Product-safe outcomes.

It does not require:

- a distributed workflow engine;
- dynamic workflow design;
- arbitrary runtime branching;
- production scheduling infrastructure;
- automated external execution;
- universal rollback;
- Event sourcing;
- autonomous agents;
- Product UI.

---

## 21. Non-Goals of This Chapter

This chapter does not define:

- new Workflow Contracts;
- Workflow Contract fields;
- service APIs;
- worker or queue topology;
- database state;
- scheduling algorithms;
- distributed transactions;
- rollback implementation;
- Product screens;
- autonomous routing;
- official submission automation;
- Communication send infrastructure;
- new Event types;
- new Task statuses.

It defines governed coordination of existing Book 02 contracts.

---

## 22. Chapter Conclusion

Workflow coordination turns contract-valid intent into an observable sequence of governed requests.

The model is:

```text
Resolve
→ Preview
→ Review if required
→ Apply with current gates and idempotency
→ Delegate to owning Services
→ Observe complete, partial, blocked or failed outcomes
→ Preserve trace
→ Expose a truthful Product result
```

Workflow does not own the objects it coordinates.

Applied does not mean everything is complete.

Partial progress is visible.

Pause is governed.

Retry is bounded.

Human Review remains separate from execution.

AI remains preparation.

The next chapter defines the Task lifecycle that Workflow depends on: how proposed work becomes an active Task, how assignment and status transitions occur, and why Task completion must remain separate from business completion.
