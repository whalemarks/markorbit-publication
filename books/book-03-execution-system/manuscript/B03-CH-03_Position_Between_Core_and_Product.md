# B03-CH-03 — Position Between Core and Product

**Status:** Release Candidate 1

## Chapter Purpose

This chapter defines the architectural position of Book 03.

Book 03 sits between **Book 02 — MarkOrbit Core Specification** and **Book 04 — MarkOrbit Workplace and Product Architecture**.

It does not replace either of them. It does not dilute Core. It does not become a product manual. Its role is to define how Core contracts become governed execution patterns that future product surfaces can safely consume.

The position is simple:

```text
Book 02 — Core Specification
  defines the stable professional kernel.

Book 03 — Execution System
  coordinates governed operational execution.

Book 04 — Workplace and Product Architecture
  provides organization context and composes execution through Products, interfaces and applications.
```

This position matters because MarkOrbit is not a single app. It is an architecture for professional trademark work. If Core, Execution and Product are not separated, the system will drift into either an overgrown Core, an uncontrolled workflow layer, or a product-driven architecture where each interface invents its own rules.

Book 03 prevents that drift.

---

## 1. The Three-Layer Relationship

Book 03 exists inside a three-layer relationship.

```text
Core
↓
Execution
↓
Product
```

Each layer has a different responsibility.

```text
Core defines what is valid.
Execution defines how valid things operate.
Product defines how users interact with operation.
```

This relationship should not be reversed.

A product surface should not define Core contracts. A workflow screen should not define professional truth. An AI assistant should not define approval. A renderer should not define business rules. A publishing tool should not define communication authority.

Book 03 protects this separation by defining the execution layer before product surfaces are built.

---

## 2. What Core Owns

Book 02 owns the Core Specification.

Core is the stable professional kernel of MarkOrbit. It defines the foundational concepts that execution and products must respect.

Core owns:

- domains;
- objects;
- services;
- API contracts;
- workflow contracts;
- event contracts;
- permission and policy primitives;
- Human Review boundaries;
- AI context and agent governance;
- idempotency;
- errors;
- versioning;
- validation rules;
- traceability rules;
- MVP Core boundary.

Core answers:

```text
What exists?
Who owns it?
What is valid?
What is constrained?
What is allowed?
What is forbidden?
What must be reviewed?
What must be traceable?
```

Book 03 consumes these answers.

It does not rewrite them.

For example, if Book 02 defines that AI output is not Human Review, Book 03 must preserve that rule in every execution pattern. If Book 02 defines that agents cannot emit Events, Book 03 cannot create an execution shortcut that allows agents to emit Events. If Book 02 defines a workflow contract boundary, Book 03 cannot convert that boundary into product-specific convenience logic.

Core remains the source of architectural truth.

---

## 3. What Execution Owns

Book 03 owns the Execution System.

Execution is not Core and not Product. It is the operational coordination layer.

Execution owns:

- execution context;
- workflow coordination;
- workflow contract consumption;
- task lifecycle;
- review gates;
- approval boundaries;
- communication execution boundary;
- event trace behavior;
- audit and replay behavior;
- permission and policy gates in operation;
- idempotency and retry behavior;
- safe failure behavior;
- human–AI handoff;
- execution observability;
- execution MVP boundary.

Execution answers:

```text
How does work move?
When does work pause?
When must review happen?
When is a draft only a draft?
When is a protected action allowed?
How is execution traced?
How does failure remain safe?
Where may AI assist?
Where must AI stop?
```

Execution does not define the underlying Core objects. It defines how approved Core contracts are coordinated in operational sequences.

For example:

```text
Core may define a Task object.
Execution defines how a task moves from prepared to reviewed to completed.

Core may define Human Review.
Execution defines where a review gate stops a workflow.

Core may define Communication contracts.
Execution defines when a message remains a draft and when sending becomes protected execution.

Core may define Event contracts.
Execution defines how execution traces are observed and audited.
```

Book 03 is therefore the place where professional operation becomes repeatable without becoming blind automation.

---

## 4. What Product Owns

Book 04 owns Workplace and Product Architecture.

Workplace provides the authorized organization context through which users experience and operate MarkOrbit. Focused Products and operating surfaces may include:

- Lite;
- MarkReg;
- MGSN interfaces;
- organization-specific applications;
- local plugins;
- publishing assistants;
- dashboards;
- Workflow screens;
- Review screens;
- reporting surfaces;
- approved integrations.

Product owns:

- user experience;
- screens;
- navigation;
- interaction design;
- product packaging;
- product modules;
- application flows;
- user-facing labels;
- product onboarding;
- surface-specific behavior;
- commercialization of capabilities.

Product answers:

```text
How does the user see this?
How does the user operate this?
Which product exposes this capability?
What is the user journey?
What is the interface?
What is packaged for release?
```

Book 03 does not answer those questions in detail.

Book 03 may state that a review gate exists. Book 04 defines how a reviewer sees that gate through authorized Workplace and Product surfaces. Book 03 may define that communication sending is protected execution. Book 04 and the relevant Product specification may design the confirmation interface, warning copy, preview screen or send-button behavior.

The boundary is:

```text
Execution defines the governance.
Product designs the experience.
```

This is why Workplace is not the subject of Book 03.

Workplace is the organization-level operating environment of an independent Orbit. It exposes Product and operating surfaces that may consume the Execution System, but Workplace does not define Execution semantics.

---

## 5. Why This Separation Is Necessary

The separation between Core, Execution and Product is necessary for four reasons.

### 5.1 It protects Core stability

If every workflow detail enters Core, Core becomes unstable.

Business execution changes more often than Core concepts. Product surfaces change even more often. Core must remain stable enough to support many products, workflows and future capabilities.

Book 03 allows execution patterns to evolve without turning Core into a procedural manual.

### 5.2 It prevents product-driven architecture

If products define execution rules, each product will eventually create its own version of truth.

Workplace might define one task lifecycle. Client Portal might define another. A publishing plugin might define a different communication boundary. A provider-facing tool might define its own review status.

This would create inconsistency.

Book 03 establishes one execution system that product surfaces consume.

### 5.3 It keeps AI inside governance

AI is useful, but AI cannot be allowed to become a hidden execution authority.

If AI behavior is embedded directly into product surfaces, users may not know where suggestion ends and approval begins. If agents are connected directly to workflows without execution governance, protected actions may become unsafe.

Book 03 makes human–AI handoff explicit.

The boundary is simple:

```text
AI may draft, suggest, prepare, check and summarize.
AI does not approve, send, submit, mutate protected state, emit Events, or define professional truth.
```

This fuller authority rule is defined in the execution principles. Here it matters because it shows why Execution must sit between Core and Product: product convenience must not become AI authority.

### 5.4 It enables repeatable operation across products

MarkOrbit will not have only one application.

The same execution pattern may later appear in:

- Lite;
- Workplace;
- client-facing tools;
- partner-facing tools;
- provider-routing tools;
- reporting dashboards;
- local publish assistants;
- API-driven integrations.

If Book 03 defines execution once, products can reuse consistent patterns.

This improves quality, auditability and implementation discipline.

---

## 6. Execution as the Contract Consumer

Book 03 should be understood as the **contract consumer layer**.

Book 02 produces contracts.

Book 03 consumes them.

```text
Book 02 provides:
  workflow contracts
  API contracts
  event contracts
  permission / policy contracts
  Human Review boundaries
  AI and agent governance
  idempotency / error / versioning contracts
  validation rules

Book 03 consumes them to define:
  workflow coordination
  task movement
  review gates
  communication boundaries
  protected execution
  event trace behavior
  retry / failure behavior
  human–AI handoff
```

This prevents Book 03 from creating its own parallel contract system.

If execution needs a contract that Book 02 has not defined, Book 03 should not invent it. It should mark the need as an open dependency or future Core review item.

The rule is:

```text
Execution may identify Core needs.
Execution may not silently redefine Core.
```

---

## 7. Execution as the Product Input

Book 03 is also the input layer for Book 04.

Products need stable execution patterns before they can be designed well.

For example, before designing a review screen, the product system needs to know:

- what a review gate is;
- who can review;
- what evidence is required;
- what outcomes are allowed;
- what happens after approval;
- what happens after rejection;
- what must be audited;
- whether AI output is visible;
- whether AI output can be accepted, edited or rejected;
- whether communication sending is protected.

Book 03 defines these operational patterns.

Book 04 can then define how authorized Workplace and Product surfaces expose them.

This avoids the common mistake of designing screens before defining execution responsibility.

In MarkOrbit, product design should not start from buttons. It should start from governed execution.

---

## 8. Future Concepts Inside This Boundary

Some newer Mo concepts also follow this separation.

### 8.1 Artifact, Render, Edit and Publish

Mo Artifact, Render, Edit and Publish should not collapse Book 03 into a product or tool manual.

At the Book 03 level, they may appear only as execution flows and governance boundaries:

```text
Artifact Execution Flow:
  how a business artifact is prepared, reviewed, rendered and recorded.

Render Execution Flow:
  how a structured artifact becomes a file through a governed render job.

Publish Execution Boundary:
  how a publish package is prepared, reviewed, handed to a user, and recorded.
```

But the product surfaces belong later.

Book 03 should not define the UI of a render studio, video editor, publish assistant, or asset browser. It should only define the execution behavior these product surfaces must respect.

### 8.2 Distillery

Mo Distillery is a knowledge production system. It converts knowledge sources into structured knowledge artifacts, capabilities, skills, workflow fragments, rules, FAQs, and reusable professional knowledge assets.

At the Book 03 level, Distillery may later become a governed execution pattern:

```text
knowledge source intake
↓
distillation workflow
↓
structure extraction
↓
validation
↓
Human Review
↓
publication to Mo Brain / Capability Catalog / Skill Library
↓
audit and reuse
```

But even here, Book 03 should define the governed execution pattern, not product UI and not implementation pipeline.

These future concepts are important, but they must remain inside the Core / Execution / Product boundary.

---

## 9. Boundary Examples

The following examples show how Core, Execution and Product differ.

### 9.1 Trademark application preparation

```text
Core:
  defines Trademark, Matter, Document, Task, Workflow Contract, Permission, Policy and Event contracts.

Execution:
  defines intake preparation, task sequencing, review gates, document readiness, communication boundary and filing-preparation trace.

Product:
  shows a filing workspace, checklist, document upload area, progress view and user prompts.
```

### 9.2 Office action response

```text
Core:
  defines Matter, Evidence, Document, Human Review, AI Context, Communication and Task contracts.

Execution:
  defines analysis preparation, evidence review, draft response review, professional approval, communication boundary and traceability.

Product:
  provides the response drafting interface, evidence viewer, client approval panel and delivery workflow.
```

### 9.3 AI-assisted communication

```text
Core:
  defines AI Context, Human Review, Communication contracts, Permission, Policy and audit requirements.

Execution:
  defines draft generation, review gate, approval boundary, send boundary and recording behavior.

Product:
  presents the draft editor, review button, warning state, send confirmation and message history.
```

### 9.4 Rendered sales material

```text
Core:
  may define source business objects, permissions, references and audit requirements.

Execution:
  defines artifact preparation, render job, review before delivery, output recording and usage trace.

Product:
  provides a PDF generator, image export button, video render panel or download page.
```

### 9.5 Local publish assistant

```text
Core:
  defines user, permission, communication, artifact reference and audit constraints.

Execution:
  defines publish package preparation, human confirmation, platform handoff, publish status recording and failure handling.

Product:
  provides a local plugin, browser extension or manual publish assistant.
```

These examples show why Book 03 must exist. They also show why Book 03 must not become Book 04.

---

## 10. Execution Boundaries Are Stronger Than Product Convenience

Product convenience must never override execution governance.

A product may want a one-click action. The Execution System must determine whether that action is allowed.

A product may want AI to complete a task. The Execution System must determine whether the task requires Human Review.

A product may want to send a message immediately. The Execution System must determine whether the communication is still a draft, requires approval, or can proceed.

A product may want to show an event in the timeline. The Execution System must respect whether the event is an observed trace, a system-emitted Event, or a protected state transition.

This is the reason Book 03 belongs between Core and Product.

Product makes execution usable.

Execution makes product safe.

Core makes execution valid.

---

## 11. Relationship to MVP

This positioning also protects MVP discipline.

Book 03 should not expand the MVP simply because future product surfaces are attractive.

Mo Artifact, Render, Edit, Publish, Distillery, Stock Asset Connectors, local publish plugins and digital humans may all become valuable later. But their presence in architecture discussion does not automatically place them in the current MVP.

Book 03 may describe future execution boundaries for these concepts, but it must distinguish:

```text
current execution MVP
future execution pattern
future product surface
research-only item
implementation task
```

This is especially important for tools and integrations.

A tool may be promising. It may even have a strong POC path. But tools do not define MarkOrbit. They are replaceable providers, workers, adapters or references.

The architecture decides whether a tool has a place.

The tool does not decide the architecture.

---

## 12. Non-Goals of This Chapter

This chapter does not define:

- new Core domains;
- new Core objects;
- new Core services;
- new API contracts;
- new workflow contracts;
- new event types;
- product UI;
- Workplace screens;
- portal flows;
- renderer implementation;
- publishing plugin implementation;
- technical tool selection;
- full Artifact model;
- full Distillery pipeline;
- Lite release scope;
- Book 04 Workplace and Product composition.

Those topics belong to their proper layers.

This chapter only defines the position of Book 03 between Core and Product.

---

## 13. Chapter Conclusion

Book 03 is the layer that turns Core validity into governed operation and prepares that operation for Product consumption.

Its position can be summarized as:

```text
Core defines the professional kernel.
Execution coordinates governed operation.
Product surfaces deliver user experience.
```

Book 03 must therefore stay faithful to two boundaries:

```text
Do not redefine Core.
Do not become Product.
```

When Book 03 holds this position, MarkOrbit gains a stable execution layer that can support many future products without fragmenting its professional architecture.

The next chapter turns this position into execution principles.
