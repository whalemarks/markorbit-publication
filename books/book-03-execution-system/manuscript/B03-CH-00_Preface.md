# B03-CH-00 — Preface

**Status:** Release Candidate 1

MarkOrbit requires more than a correct Core and more than a usable Product.

A professional operating system must also explain how valid contracts become accountable work: how context is assembled, how Workflows coordinate, how Tasks are created, how Human Review is requested, how Communications are prepared, how protected actions are gated, how failures stop safely, how Events preserve trace, and how AI assists without becoming the professional authority.

That is the purpose of **Book 03 — MarkOrbit Execution System**.

## Why This Book Exists

Book 02 defines the MarkOrbit Core: canonical domains, objects, Services, contracts, controlled values and governance rules. Those definitions are necessary, but they do not by themselves coordinate an operational journey.

Book 04 defines Workplace and Product Architecture: organization context, Product composition, user journeys, operating surfaces, controls, notifications and presentation. These responsibilities are necessary, but they must not invent execution meaning or bypass governance.

Book 03 occupies the layer between them:

```text
Book 02 — Core defines.
Book 03 — Execution coordinates.
Integration connects.
Book 04 — Workplace provides context and Products consume.
Humans review.
AI assists.
Owning Services mutate.
Events trace.
```

Execution turns contract-valid capability into governed operational progress. It coordinates without taking ownership away from Core Services, and it exposes enough structure for Products to present work without redefining it.

## What Book 03 Defines

This book defines:

- the position and boundary of the Execution System;
- Execution Context and runtime coordination;
- Workflow, Task, review, Communication and Event relationships;
- Permission, Policy and Human Review gates;
- Human–AI handoff and agent-assisted execution boundaries;
- eight recurring professional execution patterns;
- idempotency, retry, safe failure, versioning and change control;
- execution observability and audit;
- the current Execution MVP boundary;
- a controlled implementation roadmap.

The book uses trademark operations as the primary professional context, but its execution principles are broader. They apply wherever structured data, professional judgment, external consequence and accountable action must remain separate.

## What Book 03 Does Not Define

Book 03 does not redefine Book 02 Core contracts.

It does not define organization-specific Workplace context, Product UI, Product navigation or user-experience behavior. Those belong to Book 04 and the dedicated Product publications.

It does not define production connectors, payment processing, official filing, external Communication send, provider engagement or autonomous professional execution.

It does not grant AI or agents authority to approve, send, submit, pay, mutate protected state, bypass Permission or Policy, or define professional truth.

Where an execution requirement depends on a missing Core contract, Book 03 identifies the dependency and routes it back to Book 02. It does not create local substitutes that could become accidental Core truth.

## How to Read This Book

The book is organized into five parts.

**Part I — Execution System Foundation** explains why Execution exists, where it sits and which principles control it.

**Part II — Execution Architecture** defines the coordination model: execution context, state, Workflow, Task, review, Communication, Event trace, Permission, Policy and Human–AI handoff.

**Part III — Execution Patterns** applies that architecture to eight recurring professional patterns: Intake, Application Preparation, Communication Review, Provider Routing, Office Action Response, Renewal, Assignment and Evidence Review.

**Part IV — Execution Governance** defines how repetition, failure, change, Human Review, agents and observability remain controlled.

**Part V — MVP Execution System** establishes the current implementation boundary. Three workflows may coordinate approved internal preparation effects through owning Services. Five remain governed previews. External protected action remains deferred.

Readers concerned with architecture should begin with Parts I and II. Workflow designers should continue through Part III. Governance and AI teams should focus on Part IV. Engineering and implementation planners should use Part V only after accepting the earlier boundaries.

## Terminology

This book uses capitalized architectural terms consistently:

- **Core**, **Execution**, **Integration** and **Product** identify system layers or responsibilities.
- **Workflow**, **Task**, **Communication**, **Event** and **Service** identify governed MarkOrbit concepts.
- **Human Review**, **Permission** and **Policy** identify governance primitives.
- **preview** and **apply** identify execution operations and remain lower-case in prose.
- **protected action** identifies an action that requires explicit authority and current gates.
- **AI assistant** and **agent** identify software capabilities; neither term implies professional authority.
- **owning Service** identifies the Service that validates and performs an authoritative mutation.

Appendix A provides the complete working glossary.

## Publication and Implementation Status

This manuscript is the complete Book 03 Draft 1 baseline.

It is intended to support architecture review, controlled implementation planning and later publication editing. It is not, by itself, production authorization. Implementation must return to approved Book 02 contracts, the current workflow-depth boundary and repository-level acceptance gates.

The central discipline of Book 03 is simple:

```text
Preparation is not approval.
Approval is not execution.
Internal execution is not external effect.
Capability is not authority.
Trace is not truth unless the owning boundary supports it.
```

MarkOrbit becomes dependable when those distinctions remain visible in both architecture and operation.
