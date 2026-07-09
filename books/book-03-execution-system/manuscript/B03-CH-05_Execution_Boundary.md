# B03-CH-05 — Execution Boundary

## Chapter Purpose

This chapter defines the boundary of the MarkOrbit Execution System.

Book 03 exists between Core and Product. That position is only useful if its boundary is explicit. Without a clear boundary, Execution will either drift upward into Core, downward into Product, or sideways into implementation details, tool selection and uncontrolled automation.

The Execution Boundary answers four questions:

```text
1. What does Execution own?
2. What does Execution consume?
3. What does Execution produce?
4. What must Execution never do?
```

The short answer is:

```text
Execution owns governed operational coordination.
Execution consumes Core contracts.
Execution produces product-consumable execution patterns and traceable operational outcomes.
Execution must not redefine Core, become Product, or authorize AI beyond governance.
```

This chapter applies the principles from Chapter 04 as practical boundary tests.

---

## 1. Boundary Definition

The Execution System is the governed operational layer that coordinates valid Core contracts into repeatable, reviewable, permission-aware and traceable work.

It sits here:

```text
Book 02 — Core Specification
  ↓
Book 03 — Execution System
  ↓
Book 04 — Product System
```

Its boundary can be defined as:

```text
Execution begins when valid Core contracts need to be coordinated into operational work.

Execution ends when a product surface, integration or application consumes an approved execution pattern or a traceable operational outcome.
```

Execution does not begin by inventing data. It does not begin by defining a domain. It does not begin by choosing a UI. It begins when Core-defined objects, services, contracts, permissions, policies, Events and review rules need to move through operational sequences.

Execution does not end by drawing a screen. It does not end by packaging a product. It ends by producing governed behavior that products can expose safely.

---

## 2. What Execution Owns

Execution owns operational coordination.

This includes:

- Execution Context;
- workflow coordination;
- workflow contract consumption;
- task lifecycle;
- review gates;
- approval boundaries;
- communication boundaries;
- protected action boundaries;
- permission and policy gates in operation;
- Event trace behavior;
- audit and replay behavior;
- retry and idempotency behavior;
- error handling and safe failure;
- versioning in execution;
- human-AI handoff;
- execution observability;
- MVP execution boundary;
- execution pattern definitions.

These are not product features. They are not Core primitives. They are execution responsibilities.

For example, Execution may define:

```text
A communication remains a draft until review and send-boundary requirements are satisfied.
```

Execution may define:

```text
A protected action cannot proceed while a required review gate is open.
```

Execution may define:

```text
A workflow step must record trace information when it pauses, fails, retries or completes.
```

Execution may define:

```text
AI may prepare a draft, but Human Review and policy gates decide whether execution may continue.
```

These are proper execution concerns.

---

## 3. What Execution Consumes

Execution consumes Book 02.

It consumes Core definitions but does not own them.

Execution may consume:

- Core domains;
- Core objects;
- Core services;
- workflow contracts;
- API contracts;
- Event contracts;
- task contracts;
- permission contracts;
- policy contracts;
- Human Review rules;
- AI context rules;
- agent governance rules;
- validation rules;
- idempotency rules;
- error contracts;
- versioning contracts;
- audit requirements.

The principle is:

```text
Execution consumes Core.
Execution does not redefine Core.
```

If an execution pattern needs something not defined by Core, it must not silently create it. It should mark the gap as an open dependency.

Examples:

```text
If a workflow needs a new Event type, Book 03 should not invent that Event.
It should mark the need as a future Book 02 Event review item.

If a task lifecycle needs a new protected state, Book 03 should not redefine Task.
It should identify the need as a Core dependency.

If a communication flow needs a new permission rule, Book 03 should not create the permission primitive.
It should require Book 02 policy / permission review.
```

Book 03 may reveal Core needs. It may not bypass Core ownership.

---

## 4. What Execution Produces

Execution produces governed execution patterns and operational outcomes.

A governed execution pattern is a reusable structure for moving work safely through the system.

Examples include:

- intake execution pattern;
- application preparation pattern;
- office action response preparation pattern;
- evidence review pattern;
- provider routing preparation pattern;
- renewal preparation pattern;
- assignment preparation pattern;
- communication review pattern;
- artifact preparation pattern;
- render execution pattern;
- publish boundary pattern;
- distillation workflow pattern.

Execution also produces operational outcomes, such as:

- task state movement;
- review request;
- review outcome;
- blocked execution;
- approved execution;
- failed execution;
- retry attempt;
- communication-ready state;
- artifact-ready state;
- audit trace;
- replayable execution record.

These outputs are not necessarily user-facing screens. They are product-consumable execution results.

A product may later display them, but Book 03 defines their governed behavior.

---

## 5. What Execution Must Never Do

Execution must not cross five hard boundaries.

### 5.1 It must not redefine Core

Book 03 must not create or redefine:

- Core domains;
- Core objects;
- Core services;
- API contracts;
- workflow contracts;
- Event contracts;
- permission primitives;
- policy primitives;
- Human Review definitions;
- AI / agent authority;
- validation rules;
- Core MVP scope.

Execution can consume these. It can identify gaps. It can propose future review. But it cannot redefine them.

### 5.2 It must not become Product

Book 03 must not define:

- Workplace screens;
- Client Portal screens;
- Partner Center UI;
- Provider Network UI;
- API Console UI;
- navigation;
- product onboarding;
- product packaging;
- pricing;
- release plans;
- application-specific user flows;
- UI components;
- interface copy;
- front-end behavior.

Execution may define a review gate. Product may later design how that gate appears.

Execution may define a communication boundary. Product may later design the draft editor, approval screen and send confirmation.

Execution may define render execution. Product may later design the render panel, template selector or download button.

### 5.3 It must not become Implementation

Book 03 must not define:

- database schema;
- code modules;
- queue implementation;
- worker architecture;
- framework selection;
- third-party tool integration;
- deployment details;
- API endpoint implementation;
- file storage implementation;
- renderer engine implementation;
- plugin code.

Implementation may later use Book 03. Book 03 does not implement.

### 5.4 It must not become Research

Book 03 must not turn into a technical radar or tool selection manual.

It should not evaluate video renderers, PDF engines, TTS providers, stock asset APIs or publish automation projects inside the manuscript.

Research belongs under research documents.

Execution may define provider-neutral boundaries:

```text
Render execution should be provider-agnostic.
Publish execution should remain human-confirmed in early stages.
Stock asset usage should preserve source and rights trace.
```

But Execution should not choose or promote a specific tool as architecture.

### 5.5 It must not expand AI authority

Book 03 must never grant AI or agents authority to:

- approve;
- send;
- submit;
- mutate protected state;
- emit Events;
- bypass review;
- bypass permission or policy;
- define professional truth;
- commit the user externally.

This boundary is absolute.

AI may assist execution, but it cannot become the authority of execution.

---

## 6. Core Boundary Test

The boundary between Core and Execution is the most important boundary in Book 03.

Core owns definitions.

Execution owns coordination.

```text
Core:
  What is a Task?
  What is a Workflow Contract?
  What is an Event?
  What is Human Review?
  What is a Permission?
  What is a Policy?
  What can an Agent do?
  What is valid?

Execution:
  When does a task move?
  When does a workflow pause?
  When is review required?
  When is communication protected?
  How is an Event trace consumed?
  How is retry handled?
  How does AI hand off to Human Review?
  How does execution remain safe?
```

Book 03 must be careful not to turn operational examples into hidden Core definitions.

For example, if Book 03 says:

```text
A communication cannot be sent until it passes review.
```

that is an execution rule consuming Human Review and Communication boundaries.

But if Book 03 says:

```text
Communication has these new Core states...
```

that would cross into Book 02 territory.

The writing discipline is:

```text
Use Core terms.
Do not redefine Core terms.
Mark new Core needs as dependencies.
```

---

## 7. Product Boundary Test

The boundary between Execution and Product protects product consistency.

Execution defines governed behavior.

Product defines user experience.

```text
Execution:
  review gate
  communication boundary
  task lifecycle
  trace behavior
  protected action
  failure and retry
  AI handoff

Product:
  screen
  button
  page
  dashboard
  wizard
  notification design
  user flow
  interface copy
```

This means Book 03 may say:

```text
A reviewer must see sufficient context before approving a protected action.
```

But Book 03 should not define the layout of the review screen.

Book 03 may say:

```text
A user must confirm before a publish package is externally published.
```

But Book 03 should not define the browser extension interface.

Book 03 may say:

```text
Execution should record whether a rendered artifact was delivered.
```

But Book 03 should not define the download page UI.

This keeps Book 03 product-consumable without becoming Book 04.

---

## 8. AI and Agent Boundary Test

AI and agents create the greatest boundary risk because they can appear to perform work end-to-end.

The Execution System must separate assistance from authority.

AI may:

- prepare drafts;
- suggest next actions;
- summarize documents;
- identify missing information;
- classify content;
- draft communications;
- prepare checklists;
- compare options;
- generate structured notes;
- propose workflow paths.

AI may not:

- approve;
- submit;
- send;
- finalize professional conclusions;
- mutate protected state;
- emit Events;
- override policies;
- act as Human Review;
- determine professional truth.

Agents may coordinate assistance, but they must remain inside permission, policy, review and Event boundaries.

A safe AI-assisted execution pattern looks like this:

```text
User or workflow requests assistance
↓
AI prepares output
↓
System labels output as AI-assisted
↓
Human reviews
↓
Permission and policy gates run
↓
Protected action proceeds or is blocked
↓
Execution trace records the result
```

An unsafe pattern looks like this:

```text
AI prepares output
↓
AI approves output
↓
AI sends or submits
↓
System records completion
```

Book 03 must reject the unsafe pattern.

---

## 9. Communication Boundary Test

Communication is one of the most sensitive execution areas.

A communication can create client expectations, legal risk, provider obligations, fee commitments, deadline consequences, or reputational harm.

The Execution System must therefore distinguish between:

```text
message idea
draft
reviewed draft
approved communication
sent communication
recorded communication
```

A draft is not a sent communication.

An AI draft is not a reviewed communication.

A reviewed communication is not necessarily sent.

A sent communication must be recorded.

The communication boundary should include:

- who created the draft;
- whether AI assisted;
- who reviewed it;
- what was approved;
- whether sending is permitted;
- when it was sent;
- through which channel;
- what was recorded;
- whether follow-up is required.

Book 03 defines this boundary. Product later decides how users interact with it.

---

## 10. Event Boundary Test

Events are part of traceability. But not every log or note is an Event.

The Execution System must treat Events as governed traces that consume Book 02 Event contracts.

Execution may observe:

- workflow started;
- task created;
- review requested;
- review completed;
- communication approved;
- communication sent;
- protected action blocked;
- execution failed;
- retry scheduled;
- artifact rendered;
- publish package prepared;
- human decision recorded.

But Book 03 must not invent Event semantics outside Book 02.

The Event boundary is:

```text
Book 02 defines Event contracts.
Book 03 consumes Event contracts for trace, audit and replay.
Products display Event history.
Agents cannot emit Events.
```

This keeps the execution record trustworthy.

---

## 11. Future Execution Boundary Examples

The following future concepts are important, but they must remain inside the Book 03 boundary.

### 11.1 Artifact Boundary

Mo Artifact is a business output. It may be a PDF report, recommendation page, filing checklist, quote proposal, video project, client email, message draft, publish package, case report, or other deliverable.

At the Execution level, Artifact concerns include:

- how an artifact is prepared;
- what source data it uses;
- whether it requires review;
- whether it can be rendered;
- whether it can be delivered;
- whether it can be published;
- how usage is recorded;
- how versions are preserved;
- how audit trace is maintained.

Book 03 may define these execution boundaries.

But Book 03 should not define the full Artifact data model, product UI, renderer implementation or release scope.

### 11.2 Render Boundary

Mo Render turns structured artifacts into files or pages, such as PDF, PNG, MP3, MP4, HTML pages, previews or download packages.

At the Execution level, Render is not about choosing a renderer. It is about governing a render job.

Execution may define:

- render request;
- render input readiness;
- template readiness;
- permission to render;
- review requirement before delivery;
- render status;
- render failure;
- retry;
- output recording;
- versioning;
- delivery trace.

Execution should not define the renderer engine, framework, deployment method or technical pipeline.

### 11.3 Edit Boundary

Mo Edit modifies existing media or materials.

At the Execution level, Edit concerns include:

- source material identity;
- user authorization;
- edit request;
- edit output;
- review before external use;
- versioning;
- audit;
- failure handling.

Book 03 should not define a video editor product or media-processing implementation.

### 11.4 Publish Boundary

Mo Publish is distribution support.

Publishing is sensitive because it creates external visibility.

The Execution System should therefore define a strong publish boundary. Early-stage publish should be:

```text
manual or local;
human-confirmed;
permission-aware;
traceable;
not cloud auto-publishing by default.
```

Execution may define publish package preparation, review requirement, human confirmation, platform handoff, published URL recording, failure handling and audit trail.

Execution must not define platform automation code, account login handling, cookie management, cloud auto-publish, browser extension UI or platform-specific implementation.

### 11.5 Distillery Boundary

Mo Distillery is a knowledge production system.

At the Execution level, Distillery concerns include:

- source intake;
- source classification;
- extraction workflow;
- validation;
- Human Review;
- approval;
- publication to Mo Brain;
- capability / skill candidate creation;
- traceability;
- versioning;
- audit.

Book 03 may define a future Distillation Workflow.

But Book 03 must not turn Distillery into a product UI, a full implementation pipeline, or a replacement for Core Knowledge definitions.

---

## 12. Execution Boundary Review Checklist

Every Book 03 execution pattern should be checked against the following questions.

### 12.1 Core Boundary

```text
Does this pattern redefine a Core domain?
Does it invent a Core object?
Does it create a new service boundary?
Does it invent a workflow contract?
Does it invent an Event?
Does it change permission or policy primitives?
Does it expand AI / Agent authority?
```

If yes, stop and mark a Book 02 dependency.

### 12.2 Product Boundary

```text
Does this pattern define a screen?
Does it define UI layout?
Does it define navigation?
Does it define a product module?
Does it define a user-facing release feature?
Does it define product packaging?
```

If yes, move that content to Book 04 planning.

### 12.3 Implementation Boundary

```text
Does this pattern choose a framework?
Does it define code modules?
Does it define database schema?
Does it define worker deployment?
Does it define API endpoints?
Does it integrate a third-party tool?
```

If yes, move that content to implementation planning or research.

### 12.4 AI Boundary

```text
Does this pattern allow AI to approve?
Does it allow AI to send?
Does it allow AI to submit?
Does it allow AI to mutate protected state?
Does it allow AI to emit Events?
Does it treat AI output as Human Review?
```

If yes, reject or rewrite.

### 12.5 Execution Fit

```text
Does this pattern coordinate valid Core contracts?
Does it define task movement, review, communication, trace, retry or safe failure?
Does it preserve Human Review?
Does it preserve auditability?
Does it remain product-consumable?
```

If yes, it likely belongs in Book 03.

---

## 13. Non-Goals of This Chapter

This chapter does not define:

- the full Book 02 Core model;
- new Core domains;
- new Core objects;
- new API contracts;
- new Event contracts;
- product screens;
- Workplace behavior;
- Client Portal behavior;
- Provider Network UI;
- renderer implementation;
- publish plugin implementation;
- technical tool selection;
- database schema;
- release scope;
- autonomous AI execution.

It defines the Execution Boundary only.

---

## 14. Chapter Conclusion

The Execution Boundary keeps MarkOrbit structurally honest.

It allows Book 03 to define governed operation without redefining Core, becoming Product, or drifting into implementation.

The boundary can be summarized as:

```text
Execution owns governed coordination.
Execution consumes Core contracts.
Execution produces product-consumable execution patterns.
Execution preserves Human Review, permission, policy and audit.
Execution allows AI assistance but not AI authority.
Execution does not define Product UI or implementation tools.
```

When this boundary holds, MarkOrbit can grow without losing control.

Core remains stable. Execution remains governed. Products remain consistent. AI remains useful but not authoritative. Professional trademark work remains reviewable, traceable and safe.

The next chapter defines the operational frame that makes this boundary usable: Execution Context.
