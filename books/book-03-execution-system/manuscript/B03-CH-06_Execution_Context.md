# B03-CH-06 — Execution Context

**Status:** Release Candidate 1

## Chapter Purpose

This chapter defines **Execution Context**.

Execution Context is the operational frame within which MarkOrbit executes work. It gathers the minimum information, constraints, actors, state, permissions, policies, review requirements, AI boundaries and trace requirements needed for a workflow, task or protected action to proceed safely.

Without Execution Context, execution becomes fragmented. A task may move without knowing why it exists. A review may happen without sufficient evidence. A communication may be sent without knowing whether it was approved. An AI output may be used without knowing its source, limits or review status. A product surface may show an action without knowing whether that action is permitted.

Execution Context prevents this.

It answers:

```text
What is being executed?
Why is it being executed?
For whom is it being executed?
Which Core objects and contracts apply?
Which state is current?
Which rules constrain the action?
Which Human Review is required?
Where may AI assist?
What must be traced?
What happens if execution cannot continue?
```

Execution Context is not a new Core object. It is not a product screen. It is not an implementation data model. It is an execution-level construct that organizes the information needed to coordinate Core contracts safely.

The central rule is:

```text
Context before action.
```

---

## 1. Why Execution Context Is Necessary

Professional execution is rarely a single isolated action.

A trademark task may depend on:

- the client;
- the matter;
- the mark;
- the jurisdiction;
- the class;
- the goods or services;
- the deadline;
- the document set;
- the evidence set;
- the provider;
- the communication history;
- the responsible user;
- the review status;
- the permission and policy state;
- the AI assistance history;
- the current workflow contract;
- the Event trace.

If execution ignores this surrounding context, it may produce unsafe outcomes.

For example:

```text
A renewal reminder without jurisdiction context may be incomplete.

An office action response draft without evidence context may be misleading.

A provider instruction without approval context may create an unauthorized commitment.

A communication draft without client and matter context may use the wrong facts or wrong deadline.

An AI-generated recommendation without review context may appear more final than it is.
```

Execution Context exists so that operational steps are not executed in isolation.

---

## 2. Execution Context Is Not Core

Execution Context consumes Core, but it does not redefine Core.

Book 02 owns the underlying concepts:

- Identity;
- Organization;
- User;
- Permission;
- Policy;
- Knowledge;
- Brand;
- Trademark;
- Jurisdiction;
- Classification;
- Document;
- Evidence;
- Customer;
- Matter;
- Order;
- Opportunity;
- Workflow Contract;
- Task;
- Event;
- Notification;
- Partner;
- Agent;
- Service Provider;
- Service Network;
- Routing;
- Communication.

Book 03 may coordinate these concepts inside an Execution Context.

But Book 03 must not turn Execution Context into a new Core domain unless Book 02 later approves such a concept.

The boundary is:

```text
Core defines the objects.
Execution Context gathers the relevant objects for operation.
```

For example:

```text
Core defines Matter.
Execution Context identifies which Matter the current execution belongs to.

Core defines Task.
Execution Context identifies which Task is active, blocked, reviewed or completed.

Core defines Permission and Policy.
Execution Context identifies which gates apply to the current execution step.

Core defines Event.
Execution Context identifies which traces must be recorded or consumed.
```

Execution Context is therefore a coordination frame, not a replacement for Core architecture.

---

## 3. Execution Context Is Not Product State

Execution Context is also not a product screen or front-end state container.

A product may display parts of the Execution Context:

- current task;
- next action;
- missing evidence;
- review status;
- communication preview;
- deadline warning;
- approval requirement;
- AI-generated draft;
- Event history.

But the product surface does not own the context itself.

The same Execution Context may be consumed by:

- Workplace;
- Client Portal;
- Partner Center;
- Provider Network;
- Lite;
- local publish assistant;
- reporting dashboard;
- API integration;
- internal operations tool.

If each product defines its own execution context, the system becomes inconsistent.

The principle is:

```text
Execution Context is product-consumable.
It is not product-owned.
```

Product surfaces can decide how to show context, but they should not redefine what execution requires.

---

## 4. Components of Execution Context

An Execution Context should include the minimum necessary operational frame.

This chapter describes the components conceptually. It does not define a schema.

### 4.1 Execution Identity

Execution must know what is being executed.

This may include:

```text
execution identity
workflow reference
task reference
matter reference
source object reference
execution type
execution version
```

The purpose is not to define database fields. The purpose is to ensure that execution is traceable and not ambiguous.

An execution step should not be detached from the workflow, task, matter or source object that caused it.

### 4.2 Actor Context

Execution must know who or what is participating.

Actor context may include:

- user;
- organization;
- role;
- reviewer;
- assignee;
- requester;
- service provider;
- partner;
- agent;
- AI assistant;
- system process.

Actor context matters because execution authority depends on who is acting.

For example:

```text
A user may draft.
A reviewer may approve.
A system process may schedule.
An AI assistant may suggest.
A service provider may respond.

But not all actors may execute protected actions.
```

### 4.3 Business Context

Execution must know the business object it belongs to.

This may include:

- customer;
- matter;
- order;
- opportunity;
- trademark;
- jurisdiction;
- class;
- goods or services;
- document set;
- evidence set;
- provider relationship;
- communication thread.

Business context prevents generic execution from ignoring professional facts.

### 4.4 Workflow Context

Execution must know where it is inside the workflow.

This includes:

- active workflow contract;
- current workflow state;
- current task;
- previous task;
- next expected task;
- blocked state;
- pause reason;
- retry status;
- completion criteria.

Workflow context is what allows execution to move safely rather than randomly.

### 4.5 Review Context

Execution must know whether Human Review is required.

Review context may include:

- review gate;
- reviewer role;
- required evidence;
- review status;
- review outcome;
- review notes;
- approval boundary;
- rejection reason;
- revision request;
- review timestamp.

This context is essential for protected actions.

If review is required, execution must not proceed until review is completed.

### 4.6 Permission and Policy Context

Execution must know which permission and policy gates apply.

This may include:

- actor permission;
- organization policy;
- jurisdiction policy;
- client instruction policy;
- communication policy;
- protected action policy;
- AI usage policy;
- publishing policy;
- provider instruction policy.

Permission and policy context prevents execution from treating availability as authorization.

A button may exist. A workflow may be ready. A draft may be complete. But execution may still be forbidden.

### 4.7 Communication Context

Execution must know whether a communication is internal, draft, reviewed, approved, sent or recorded.

Communication context may include:

- channel;
- audience;
- draft source;
- AI assistance status;
- review status;
- send approval;
- sent timestamp;
- recipient;
- related matter;
- follow-up requirement;
- audit record.

This protects the boundary between preparation and external commitment.

### 4.8 AI Context

Execution must know where AI participated.

AI context may include:

- AI-generated draft;
- AI summary;
- AI recommendation;
- source materials used;
- uncertainty note;
- instruction reference;
- human edits;
- Human Review status;
- accepted, rejected or modified AI output;
- prohibited action boundary.

AI context is necessary because AI assistance must remain distinguishable from human decision.

The rule is:

```text
AI involvement must be visible where it affects execution.
AI output must not be silently converted into approval.
```

### 4.9 Event and Audit Context

Execution must know what must be traced.

Event and audit context may include:

- prior Events;
- expected Events;
- trace requirements;
- audit trail;
- replay requirements;
- Event source;
- Event actor;
- Event timestamp;
- failure trace;
- retry trace.

Execution Context should make traceability operational.

It should allow MarkOrbit to answer:

```text
What happened?
Who acted?
What was reviewed?
What was approved?
What failed?
What was retried?
What was sent?
What was generated by AI?
What was decided by a human?
```

### 4.10 Artifact Context

If execution involves a business artifact, context may include:

- artifact type;
- source object;
- source data;
- version;
- render status;
- review status;
- delivery status;
- usage status;
- publish status;
- related output files.

This is useful for future Artifact, Render, Edit and Publish execution patterns.

However, Book 03 should not define the full Artifact product model here. It should only identify the execution context needed for governed operation.

---

## 5. Context Before Action

A key execution rule is:

```text
Context before action.
```

Before execution proceeds, the system should know whether it has enough context.

For example:

```text
Before drafting:
  Does the system know the matter, task, jurisdiction and source materials?

Before review:
  Does the reviewer have the draft, evidence, source data and risk notes?

Before sending:
  Is the communication approved, addressed correctly, permissioned and recorded?

Before rendering:
  Is the artifact ready, versioned and allowed to be rendered?

Before publishing:
  Is the publish package reviewed, human-confirmed and traceable?

Before AI assistance:
  Are the source materials, user intent and prohibited boundaries clear?
```

If context is missing, execution should not guess silently.

It should:

- pause;
- request missing information;
- route to a human;
- mark uncertainty;
- block protected action;
- record the reason.

This is how Execution Context supports safe failure.

---

## 6. Context Changes During Execution

Execution Context is not static.

It changes as work moves.

Examples:

```text
A draft is created.
Evidence is supplemented.
A reviewer requests revision.
A task is reassigned.
A policy check fails.
A communication is approved.
A render job completes.
A retry succeeds.
A deadline warning appears.
An AI output is rejected.
A human decision is recorded.
```

The Execution System must preserve meaningful context changes.

This does not mean every minor UI action becomes an Event. But meaningful execution changes should be traceable and, where required, versioned.

The key distinction is:

```text
Context can change.
Protected history should not disappear.
```

Execution should avoid overwriting important operational facts in ways that make review and audit impossible.

---

## 7. Context and State

Execution Context and Execution State are related but not identical.

Execution State describes where work is in its lifecycle.

Execution Context describes the surrounding information needed to understand and govern that state.

For example:

```text
Execution State:
  Review Required

Execution Context:
  Which document requires review?
  Which reviewer role is required?
  Which evidence is attached?
  Which AI output was used?
  Which policy requires review?
  What happens if review is rejected?
```

Another example:

```text
Execution State:
  Communication Ready

Execution Context:
  Who is the recipient?
  Which matter is referenced?
  Who approved the message?
  Is sending permitted?
  Which channel will be used?
  What must be recorded after sending?
```

State without context is not enough.

Context gives state meaning.

---

## 8. Context and Review

Human Review depends on context.

A reviewer cannot meaningfully approve what they cannot understand.

Therefore, a review gate should carry enough Execution Context for the reviewer to evaluate the action.

At minimum, a review context should show:

- what is being reviewed;
- why review is required;
- what source materials are relevant;
- what AI assistance was used;
- what evidence supports the action;
- what risks or uncertainties exist;
- what outcomes are available;
- what happens after approval or rejection.

This matters because Human Review is not a rubber stamp.

The Execution System must not reduce review to a button without context.

A review button without context is not a review gate.

---

## 9. Context and AI Assistance

AI needs context to assist, but AI also creates context that must be governed.

When AI is used, Execution Context should identify:

```text
What did AI receive?
What did AI produce?
Which sources were used?
What uncertainty remains?
Who reviewed it?
Was it accepted, edited or rejected?
Can it be used externally?
```

AI assistance should not be invisible.

If a communication draft was AI-assisted, the review context should make that visible. If an evidence summary was generated by AI, the reviewer should know that. If an AI recommendation was rejected, that outcome should be preserved where relevant.

The principle is:

```text
AI may enrich Execution Context.
AI must not replace Execution Context.
```

AI cannot act safely without context, and AI output cannot be safely used without context.

---

## 10. Context and Permissions

Execution Context must include permission and policy information because execution authority is context-dependent.

A user may be allowed to do one action but not another.

For example:

```text
A user may edit a draft but not approve it.
A reviewer may approve a communication but not submit a filing.
A finance user may confirm payment but not approve a legal position.
A system process may create a task but not close a professional review.
An AI assistant may suggest but not execute.
```

The same action may also be allowed or blocked depending on:

- matter status;
- client instruction;
- jurisdiction;
- risk level;
- deadline proximity;
- organization policy;
- required evidence;
- review outcome.

Permission cannot be evaluated in isolation.

Execution Context gives permission and policy gates enough information to operate correctly.

---

## 11. Context and Communications

Communication is one of the clearest examples of why Execution Context is needed.

A communication should not be evaluated only as text.

It also requires context:

```text
Who is the recipient?
Which matter does it concern?
Is the deadline correct?
Is the legal position reviewed?
Is the fee information approved?
Is the provider instruction authorized?
Was the text AI-assisted?
Has the client approved the underlying decision?
Is this an internal note or external message?
What channel will be used?
What must be recorded after sending?
```

A message without context can be dangerous.

Execution Context turns a message from raw text into a governed communication candidate.

Only after the required context, review, permission and send boundary are satisfied can it become an external communication.

---

## 12. Context and Future Artifact Flows

Future Mo Artifact flows will also depend on Execution Context.

A PDF, image, video, recommendation page, publish package or case report is not just a file. It is a business output derived from data, knowledge, templates, AI assistance and user decisions.

Execution Context should help identify:

- source object;
- source data;
- template used;
- AI-generated content;
- version;
- reviewer;
- delivery status;
- publish status;
- usage trace;
- risk notes.

This protects MarkOrbit from treating outputs as isolated files.

For example:

```text
A quote proposal PDF should know which quote data it used.
A trademark recommendation video should know which trademark listing it represents.
A publish package should know which artifact it came from and whether it was reviewed.
A case report should know which evidence and decisions support it.
```

Book 03 can define these as execution-context requirements. Book 04 and implementation can later decide how to expose and store them.

---

## 13. Context and Future Distillery Workflows

Mo Distillery also requires Execution Context.

A distillation workflow should know:

- source material;
- source type;
- license or usage boundary;
- extraction goal;
- knowledge unit target;
- validation requirements;
- reviewer;
- approval status;
- publication destination;
- version;
- trace.

This matters because distilled knowledge may become reusable capability.

If a book, official guide, case decision or SOP is transformed into a rule, FAQ, Skill or Workflow Fragment, MarkOrbit must know how that transformation happened and who validated it.

Execution Context helps keep knowledge production governed.

A distilled output should not silently become canonical knowledge. It should pass through source tracking, validation, Human Review and publication boundaries.

---

## 14. Minimum Context for the Execution MVP

The Execution MVP should not attempt to capture every possible context field.

It should focus on the smallest safe context frame.

At minimum, MVP Execution Context should support:

```text
execution identity
source object reference
active workflow / task reference
actor / role
current state
required review gate
permission / policy check result
AI assistance marker
communication boundary marker
Event / audit trace reference
failure / retry status
```

This is enough to support safe execution without overbuilding.

Future versions may expand context for artifacts, rendering, publishing, distillation, provider routing, advanced observability and product-specific displays.

But the MVP should not confuse completeness with safety.

The goal is not to capture everything.

The goal is to capture what execution needs in order to avoid unsafe action.

---

## 15. Context Anti-Patterns

The following anti-patterns should be avoided.

### 15.1 Contextless Action

```text
A task is completed without knowing which workflow and matter it belongs to.
```

### 15.2 Review Without Context

```text
A reviewer clicks approve without seeing evidence, source data, AI involvement or consequence.
```

### 15.3 AI Output Without Provenance

```text
An AI-generated recommendation is used without recording source materials or review status.
```

### 15.4 Product-Owned Context

```text
Each product surface defines its own workflow state, review status and communication boundary.
```

### 15.5 Silent Context Overwrite

```text
A revised draft replaces an approved version without preserving the approval history.
```

### 15.6 Permission Without Context

```text
The system checks only the user's role but ignores matter status, policy, review requirement or protected action type.
```

### 15.7 Artifact Without Source

```text
A generated PDF or video is delivered without knowing which data, template, version or approval it used.
```

These anti-patterns all create execution risk.

---

## 16. Execution Context Checklist

Before an execution step proceeds, Book 03 patterns should ask:

```text
What is the source object?
Which workflow or task is active?
Who is acting?
What role or authority do they have?
What state is the execution in?
Which Core contracts apply?
Is Human Review required?
Has Human Review been completed?
Which permission and policy gates apply?
Was AI involved?
Is this internal preparation or protected external action?
What must be recorded?
What happens if this step fails?
What version is being used?
What trace must be preserved?
```

If these questions cannot be answered, execution should pause, request more information, or route to Human Review.

---

## 17. Non-Goals of This Chapter

This chapter does not define:

- a database schema for Execution Context;
- a new Core domain;
- a new Core object;
- an implementation model;
- a product screen;
- a context API;
- a UI state store;
- a workflow engine;
- a renderer model;
- a publishing plugin;
- a full Distillery data model;
- autonomous AI context execution.

Those topics belong to Core review, Workplace and Product Architecture, research or implementation.

This chapter only defines Execution Context as an operational concept for Book 03.

---

## 18. Chapter Conclusion

Execution Context is the frame that makes execution safe.

It gathers enough information for MarkOrbit to understand what is being executed, why it is being executed, who is acting, which Core contracts apply, which review gates matter, which permissions and policies constrain the action, where AI participated, what must be traced, and whether execution can proceed.

Execution Context does not redefine Core and does not belong to Product. It is the coordination frame that allows Core contracts to become governed operation.

The central rule is:

```text
Context before action.
```

When MarkOrbit follows this rule, execution becomes safer, more reviewable, more auditable and more consistent across future product surfaces.

The next chapter explains how this context supports the transition from Core contracts to Execution Runtime.
