# B03-CH-07 — From Core Contracts to Execution Runtime

## Chapter Purpose

This chapter explains how MarkOrbit moves from **Core contracts** to **Execution Runtime**.

Book 02 defines Core contracts. These contracts describe what is valid, owned, constrained, reviewable, permissioned, policy-bound and traceable. But a contract is not yet execution. A contract must be interpreted, coordinated, checked, paused, resumed, reviewed, recorded and exposed to product surfaces.

Book 03 defines that transition.

The transition can be summarized as:

```text
Core Contract
↓
Execution Context
↓
Runtime Coordination
↓
Review / Permission / Policy Gates
↓
Protected Action or Safe Pause
↓
Event Trace / Audit Record
↓
Product-Consumable Outcome
```

This chapter does not define implementation code. It does not define a workflow engine. It does not define database schema, queues, workers, API endpoints, product screens or technical tools.

It defines the architectural path by which Core contracts become governed execution.

---

## 1. What Is a Core Contract?

A Core contract is a stable rule, structure or boundary defined by Book 02.

It may describe:

- a domain boundary;
- an object responsibility;
- a service responsibility;
- a workflow contract;
- a task contract;
- an API contract;
- an Event contract;
- a permission requirement;
- a policy requirement;
- a Human Review boundary;
- an AI and agent governance rule;
- an idempotency requirement;
- an error contract;
- a versioning rule;
- a validation rule.

Core contracts define what MarkOrbit may rely on.

They answer questions such as:

```text
What exists?
Who owns it?
What is valid?
What is allowed?
What is blocked?
What must be reviewed?
What must be traced?
What can AI do?
What must AI never do?
```

But Core contracts are deliberately not the runtime itself.

A workflow contract can define the allowed shape of a workflow, but it does not by itself move work forward. A task contract can define task behavior, but it does not decide whether a specific task is ready. An Event contract can define Event semantics, but it does not decide when an execution step should record a trace. A permission rule can define a boundary, but it must still be evaluated inside a live Execution Context.

Execution Runtime is where these contracts are applied.

---

## 2. What Is Execution Runtime?

Execution Runtime is the operational environment in which MarkOrbit coordinates work according to Core contracts.

It is not a single product, page, queue, database table or workflow engine. It is the governed runtime behavior of the system.

Execution Runtime is where MarkOrbit decides:

```text
Which workflow is active?
Which task is current?
Which actor is acting?
Which context applies?
Which contract must be consumed?
Which gate must run?
Which review is required?
Which action is protected?
Which outcome is allowed?
Which trace must be recorded?
Which failure path is safe?
```

Execution Runtime turns static contracts into live operational behavior.

For example:

```text
Core Contract:
  Communication sending requires proper authority and review.

Execution Runtime:
  A specific message for a specific matter is currently a draft.
  AI assisted the draft.
  Human Review is required.
  The reviewer has not approved it.
  The send action is blocked.
  The blocked state is visible.
  The reason is recorded.
```

This is execution.

It is not merely workflow documentation, and it is not product UI. It is governed runtime behavior.

---

## 3. Why Runtime Must Be Governed

Execution Runtime must be governed because professional work carries consequences.

A runtime that only optimizes for speed may move too fast. A runtime that only optimizes for automation may bypass judgment. A runtime that only optimizes for convenience may blur the line between draft and approval. A runtime that only optimizes for AI capability may mistake suggestion for authority.

MarkOrbit cannot allow that.

A governed runtime must ensure that:

- Core contracts are respected;
- Execution Context is sufficient;
- Human Review is real;
- permission and policy gates are evaluated;
- AI assistance is visible and bounded;
- protected actions cannot proceed casually;
- failures are safe;
- state changes are traceable;
- product surfaces cannot bypass execution rules.

Governance is not an afterthought. It is part of runtime.

Without governance, MarkOrbit would become a set of disconnected automations.

With governance, MarkOrbit becomes a professional execution system.

---

## 4. The Contract-to-Runtime Path

The transition from Core contracts to Execution Runtime follows a controlled path.

```text
1. Contract Selection
2. Context Assembly
3. Runtime State Resolution
4. Gate Evaluation
5. Execution Decision
6. Protected Action or Safe Pause
7. Trace Recording
8. Product Outcome Exposure
```

Each step matters.

---

## 5. Contract Selection

Execution first identifies which Core contracts apply.

For example, a communication workflow may require:

```text
Communication contract
Task contract
Human Review boundary
Permission contract
Policy contract
Event contract
AI governance rule
```

A render workflow may require:

```text
Artifact reference
Template readiness
Permission check
Review requirement
Render status rule
Failure and retry rule
Output trace rule
```

A distillation workflow may require:

```text
Knowledge source reference
Validation rule
Human Review boundary
Publication rule
Capability candidate boundary
Versioning rule
Audit requirement
```

Execution should not guess the applicable contracts. It should derive them from the workflow, task, source object, actor and action type.

If the required contract is missing, execution should not invent it. It should mark an open dependency for Core review.

---

## 6. Context Assembly

After selecting contracts, Execution assembles the Execution Context.

The context includes the operational frame needed to apply contracts safely:

- source object;
- workflow;
- task;
- actor;
- role;
- current state;
- business facts;
- documents;
- evidence;
- communication history;
- AI involvement;
- review requirement;
- permission and policy conditions;
- trace requirements;
- failure and retry status.

This context determines how contracts apply.

A permission rule without context is incomplete. A review requirement without context is hollow. An AI output without context is risky. A task without context is just a label.

Chapter 06 defined the core rule:

```text
Context before action.
```

Execution Runtime is where that rule becomes operational.

---

## 7. Runtime State Resolution

Execution then resolves the current runtime state.

It asks:

```text
Where is this work now?
Is it preparing?
Is it waiting for information?
Is it waiting for review?
Is it blocked?
Is it approved?
Is it ready for protected action?
Has it failed?
Is it retryable?
Has it completed?
```

Runtime state must be derived from Core-valid facts and Execution Context, not from product convenience.

A product screen may display state, but it should not invent state.

Runtime state should distinguish:

```text
draft from approved;
approved from sent;
suggested from decided;
review requested from review completed;
failed from completed;
blocked from waiting;
retry from new action.
```

If these distinctions collapse, execution becomes unsafe.

---

## 8. Gate Evaluation

Execution evaluates gates.

The main gates are:

- validation gate;
- permission gate;
- policy gate;
- Human Review gate;
- communication boundary;
- protected action boundary;
- AI boundary;
- Event trace boundary;
- idempotency gate;
- safe failure gate.

A gate can allow execution, block execution, pause execution, request missing context, route to review, or send execution into failure handling.

A gate is not merely a warning.

If a gate is required, runtime must respect it.

### 8.1 Validation Gate

Checks whether required information is structurally complete.

Example:

```text
Required document missing → cannot proceed.
```

### 8.2 Permission Gate

Checks whether the actor is allowed to perform or request the action.

Example:

```text
User can draft but cannot approve.
```

### 8.3 Policy Gate

Checks whether organizational, jurisdictional or workflow policy allows the action.

Example:

```text
Provider instruction requires supervisor review.
```

### 8.4 Human Review Gate

Checks whether an authorized Human Reviewer has completed review.

Example:

```text
AI draft cannot be sent until reviewed.
```

### 8.5 Communication Boundary

Checks whether a message can move from internal draft to external communication.

Example:

```text
Reviewed draft may be approved for sending, but sending must still be recorded.
```

### 8.6 Protected Action Boundary

Checks whether the action has external, legal, financial, professional or state-changing consequences.

Example:

```text
Submitting, sending, publishing, provider instruction and protected state mutation require stronger governance.
```

### 8.7 AI Boundary

Checks whether AI is being used only as assistance.

Example:

```text
AI can prepare a checklist but cannot approve completion.
```

### 8.8 Idempotency Gate

Checks whether the action is a retry or duplicate.

Example:

```text
Do not send the same approved communication twice.
```

### 8.9 Failure Gate

Checks whether execution can retry, pause, escalate or fail safely.

Example:

```text
Render failed; preserve input and error state, allow retry if safe.
```

These gates are how contracts become runtime governance.

---

## 9. Execution Decision

After gates are evaluated, Execution makes an execution decision.

Possible decisions include:

```text
continue
pause
block
request review
request missing information
retry
fail safely
prepare output
approve transition
execute protected action
record outcome
```

This decision is not professional truth by itself. It is a runtime decision based on Core contracts, Execution Context and governance gates.

For example:

```text
Runtime may decide that a communication is ready for review.
Runtime may not decide that the legal position is correct unless required Human Review has occurred.
```

Execution Runtime decides whether work can proceed.

It does not replace professional judgment.

---

## 10. Protected Action or Safe Pause

If all required gates pass, runtime may proceed to the allowed action.

If gates do not pass, runtime must pause safely.

This distinction is critical.

A safe pause is not failure. It is governed restraint.

Examples:

```text
Missing evidence → pause and request evidence.
Review required → pause and route to reviewer.
Permission denied → block protected action.
AI uncertainty → mark for Human Review.
Render failure → record failure and allow retry if safe.
Communication not approved → remain draft.
```

The runtime must never silently convert an unsafe situation into completion.

In a professional system, stopping correctly is part of executing correctly.

---

## 11. Trace Recording

Execution records what happened.

Trace recording may include:

- state transition;
- review request;
- review outcome;
- blocked action;
- protected action;
- failure;
- retry;
- AI-assisted step;
- communication approval;
- artifact render;
- publish handoff;
- human decision.

Book 03 consumes Book 02 Event contracts for this purpose. It does not redefine Event semantics.

The record must support future review, audit and replay.

A trace should preserve the distinction between:

```text
AI prepared.
Human Reviewed.
System executed.
Event recorded.
```

This distinction is essential for trust.

---

## 12. Product Outcome Exposure

Finally, Execution exposes a product-consumable outcome.

This does not mean defining product UI.

It means products can safely consume the execution result.

Examples:

```text
Task is waiting for review.
Communication is approved but not sent.
Render job failed and can be retried.
Publish package is ready for human-confirmed handoff.
Evidence is missing.
Workflow is blocked by policy.
AI draft is available for Human Review.
```

Book 04 may later decide how these outcomes appear to users.

Book 03 defines what the outcomes mean.

---

## 13. Runtime Does Not Mean Automation

Execution Runtime is often misunderstood as automation.

It is not.

Runtime can include automation, but automation is only one possible behavior.

The Execution Runtime may:

- prepare;
- route;
- suggest;
- pause;
- validate;
- block;
- request review;
- record;
- retry;
- escalate;
- expose status.

It does not exist only to accelerate action.

In professional systems, a runtime that pauses correctly is as valuable as a runtime that proceeds correctly.

For example:

```text
A workflow that stops an unreviewed communication is working.
A permission gate that blocks unauthorized publishing is working.
A review gate that sends a draft back for revision is working.
A failure state that prevents false completion is working.
```

Execution Runtime is not judged only by how much it automates.

It is judged by whether it coordinates work safely.

---

## 14. Runtime and Human Review

Human Review is one of the most important runtime gates.

At runtime, Human Review should not be a static label. It should be an operational state and decision point.

Runtime must know:

- what requires review;
- why review is required;
- who may review;
- what context the reviewer needs;
- what outcomes are allowed;
- what happens after approval;
- what happens after rejection;
- how the review is recorded.

A proper runtime review flow looks like this:

```text
Execution prepares review item
↓
Review context is assembled
↓
Authorized reviewer reviews
↓
Reviewer approves, rejects or requests revision
↓
Execution records outcome
↓
Runtime proceeds, pauses or loops accordingly
```

An improper runtime review flow looks like this:

```text
AI generates output
↓
System marks it reviewed
↓
Execution proceeds
```

Book 03 must reject the improper pattern.

Human Review is runtime governance, not cosmetic approval.

---

## 15. Runtime and AI Assistance

AI can participate in runtime, but only under boundary.

At runtime, AI may help:

- prepare a draft;
- summarize evidence;
- extract facts;
- suggest missing fields;
- generate a checklist;
- compare options;
- propose next actions;
- identify risk;
- prepare review context.

Runtime must track AI participation.

It should know:

```text
Where did AI assist?
What did AI produce?
Which source materials were used?
Was the output edited?
Was the output reviewed?
Was the output accepted or rejected?
Can it be used externally?
```

AI output should not silently become execution state.

For example:

```text
AI-generated response draft
```

is not the same as:

```text
approved response ready for external communication
```

Runtime must preserve that difference.

The rule is:

```text
AI can help create runtime inputs.
AI cannot authorize runtime outcomes.
```

---

## 16. Runtime and Communications

Communications are one of the clearest examples of contract-to-runtime transformation.

Core may define Communication contracts and review boundaries.

Runtime applies them to a specific message.

Example:

```text
Core:
  External communication requires authority, review and trace.

Runtime:
  A draft email was generated for Matter M.
  AI assisted the first draft.
  The assigned user edited it.
  Human Review is required because it contains legal position and fee information.
  Review is pending.
  Send is blocked.
  The product surface may show "Waiting for Review".
```

After review:

```text
Runtime:
  Reviewer approved version 3.
  Permission check passed.
  Policy check passed.
  Send boundary is satisfied.
  User may send or local send process may proceed.
  Sending result must be recorded.
```

This is why runtime matters.

It turns general contracts into specific operational decisions.

---

## 17. Runtime and Future Artifact / Render / Publish Patterns

Future Artifact, Render and Publish flows also move from Core contracts to runtime.

At runtime, the system must know:

```text
What artifact is being prepared?
Which source object does it use?
Which data version does it use?
Was AI used?
Does it require review?
Can it be rendered?
Can it be delivered?
Can it be published?
What output was produced?
What trace is required?
```

A render job is not only technical processing. At execution level, Render is a governed runtime action.

Runtime must know:

```text
Is the source artifact ready?
Is the template approved?
Is the actor allowed to render?
Is review required before render or before delivery?
Which version is rendered?
What happens if rendering fails?
Can the job be retried?
Where is the output recorded?
Can the output be delivered or published?
```

Publishing is even more sensitive because it creates external visibility. A safe Publish Runtime pattern is:

```text
Artifact prepared
↓
Publish package generated
↓
Human Review if required
↓
User confirms platform and content
↓
Local/manual handoff
↓
User completes or confirms publication
↓
Published URL or status recorded
↓
Audit trace preserved
```

An unsafe pattern is:

```text
AI generates content
↓
System auto-publishes to external platform
↓
No human confirmation
↓
No trace
```

Book 03 must reject the unsafe pattern.

These future flows should remain provider-neutral and product-neutral inside Book 03.

---

## 18. Runtime and Future Distillery Workflows

Distillery is another future example of contract-to-runtime transformation.

At architecture level, Mo Distillery is a knowledge production system. At execution level, it becomes a governed distillation runtime.

A safe Distillery Runtime may look like this:

```text
Source material intake
↓
Source classification
↓
Extraction
↓
Structure proposal
↓
Validation
↓
Human Review
↓
Approval
↓
Publication to Mo Brain / Capability Catalog / Skill Library
↓
Trace and versioning
```

Runtime must know:

- source material;
- extraction goal;
- knowledge output type;
- validation requirement;
- reviewer;
- approval state;
- publication destination;
- version;
- trace.

Distilled knowledge should not silently become canonical.

Book 03 can define this runtime pattern later, while Book 02 retains Knowledge and Capability boundaries and Book 04 later defines product surfaces.

---

## 19. Runtime and Product Surfaces

Product surfaces consume runtime outcomes.

They should not decide runtime governance.

For example, a product may show:

```text
Waiting for context
Waiting for review
Blocked by policy
Ready to send
Render failed
Retry available
Publish package ready
AI draft available
Human approval required
```

But those states should come from the Execution Runtime, not be invented by the UI.

Product may decide:

- how to display the status;
- how to organize the page;
- how to guide the user;
- what copy to use;
- which buttons to show;
- how to visualize trace.

Product should not decide:

- whether review is required;
- whether AI output counts as approval;
- whether permission can be bypassed;
- whether an Event is emitted;
- whether sending is protected;
- whether failure can be ignored.

The runtime provides the safe operational meaning. Product provides the experience.

---

## 20. Runtime Observability

A runtime must be observable.

If execution state is hidden, users cannot trust it. If review gates are invisible, work will stall. If AI assistance is not marked, users may overtrust output. If failures are hidden, users may assume completion. If traces are unavailable, audit and quality control fail.

Runtime observability should answer:

```text
What is active?
What is blocked?
What needs review?
Who must act?
What did AI prepare?
What did a human approve?
What failed?
What was retried?
What was sent?
What was recorded?
What can happen next?
```

Observability is not merely an interface requirement. It is an execution requirement.

Products may visualize it, but Execution must make it available.

---

## 21. Runtime Anti-Patterns

The following anti-patterns should be avoided.

### 21.1 Contractless Runtime

```text
A workflow proceeds without identifying which Core contracts apply.
```

### 21.2 Contextless Runtime

```text
A task moves state without matter, actor, review or policy context.
```

### 21.3 Product-Owned Runtime

```text
A screen decides whether review is required or whether a message can be sent.
```

### 21.4 AI-Authorized Runtime

```text
AI output automatically approves or completes a protected action.
```

### 21.5 Log-Only Runtime

```text
The system writes unstructured logs but does not preserve governed Event trace.
```

### 21.6 Success-Biased Runtime

```text
The workflow assumes success and hides failure, retry or blocked states.
```

### 21.7 Tool-Defined Runtime

```text
A renderer, publish tool or AI framework dictates the execution model.
```

Each anti-pattern weakens governance.

---

## 22. Minimum Runtime for Book 03 MVP

The Book 03 MVP should define the smallest safe runtime.

It should include:

```text
Execution Context
Runtime State
Workflow Coordination
Task Lifecycle
Review Gates
Communication Boundary
Permission / Policy Gates
Human–AI Handoff
Event Trace / Audit
Safe Failure
Retry / Idempotency
Basic Observability
```

It should not include:

```text
full product UI
full workflow engine implementation
full renderer system
full publish automation
full Distillery pipeline
digital human execution
all external integrations
autonomous agent operation
```

The goal is not to build the most complete runtime.

The goal is to define the smallest runtime that prevents unsafe execution.

---

## 23. Runtime Checklist

Before an execution pattern is accepted into Book 03, it should answer:

```text
Which Core contracts does it consume?
What Execution Context is required?
What runtime states are possible?
Which gates apply?
Where is Human Review required?
Where may AI assist?
Where must AI stop?
Which action is protected?
What happens if gates fail?
What is recorded?
What is product-consumable?
What remains outside Book 03?
```

If these questions cannot be answered, the pattern is not ready.

---

## 24. Non-Goals of This Chapter

This chapter does not define:

- a workflow engine;
- runtime code;
- database schema;
- API endpoints;
- queue architecture;
- worker implementation;
- product UI;
- renderer implementation;
- publish plugin implementation;
- specific technical tools;
- new Core contracts;
- new Event semantics;
- autonomous agent execution.

It defines the architectural transition from Core contracts to governed Execution Runtime.

---

## 25. Chapter Conclusion

Core contracts are necessary, but they are not enough.

MarkOrbit needs Execution Runtime to apply those contracts inside real operational work.

Execution Runtime assembles context, resolves state, evaluates gates, coordinates review, blocks unsafe action, supports safe failure, records trace, and exposes product-consumable outcomes.

The path is:

```text
Core Contract
↓
Execution Context
↓
Runtime State
↓
Gate Evaluation
↓
Execution Decision
↓
Protected Action or Safe Pause
↓
Trace / Audit
↓
Product-Consumable Outcome
```

Core defines what is valid.

Execution Runtime makes valid work safely operable.

Product surfaces make operable work usable.

This closes Part I of Book 03. The next part can now move from foundation to architecture: the layers, objects, states, workflows, tasks, review gates, communications, Events, permissions and human–AI handoffs that make the Execution System work.
