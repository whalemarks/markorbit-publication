# Appendix A — Execution Glossary

This glossary locks the preferred Book 03 terminology. Definitions are concise by design. Detailed treatment remains in the cited chapters and in approved Book 02 contracts.

## System Layers

### Core

The canonical layer that defines domains, objects, Services, contracts, controlled values and authoritative rules. Book 03 consumes Core; it does not redefine it.

### Execution

The coordination layer that turns approved Core capabilities into governed operational progress across context, Workflows, Tasks, Human Review, Communications, Services and Events.

### Integration

The controlled connection layer between MarkOrbit Services and external providers, authorities, channels or systems. Integration transports and observes; it does not independently define professional truth.

### Product

The user-facing layer that presents execution journeys, controls and results. Product consumes Execution semantics and must not invent authority or execution depth.

### Execution System

The complete Book 03 responsibility area for coordinating governed work between Core and Product.

### Execution Runtime

The operational behavior through which Execution consumes contracts, assembles context, evaluates gates, coordinates Services and returns governed results. It is not a new Core Domain.

## Context and State

### Execution Context

The versioned, permission-filtered set of references, actors, sources, gates and intended actions required to coordinate one execution operation. It is a conceptual execution view unless formalized by an approved contract.

### Execution Object

A Book 03 conceptual view of the references and runtime information needed for coordination. It is not automatically a canonical Core Object.

### Execution State

The coordination condition of an execution operation, distinct from the authoritative lifecycle state of the underlying Core objects.

### Semantic Operation

The real governed intent being performed, independent of technical retries, requests or process invocations.

### Version Snapshot

The exact versions of subjects, sources, contracts, review packages and intended actions used at a decision or execution point.

### Compatibility

The degree to which a changed version can be consumed without altering governed structure, behavior, professional meaning, authority or historical interpretation.

## Workflow and Tasks

### Workflow

A governed coordination structure that consumes approved contracts, evaluates gates, sequences preparation and delegates mutation to owning Services.

### Workflow Contract

The Core-defined contract that specifies a Workflow's identity, supported steps, gates, effects and boundaries.

### Workflow Coordination

Execution behavior that assembles context, selects allowed next steps and delegates work without taking ownership of Core mutation.

### Workflow Depth

A Book 03 MVP label describing current execution capability: Depth A for approved internal apply, Depth B for governed preview only, and Depth C for deferred protected action.

### Preview

A side-effect-free execution operation that validates, organizes, compares or prepares information without authoritative mutation or external effect.

### Apply

A protected execution request that revalidates current gates and delegates approved effects to owning Services.

### Task Plan

A preview of proposed work. It is not an active Task.

### Active Task

A governed Task created and owned by Task Service under approved contracts.

### Owning Service

The Service responsible for validating and performing an authoritative mutation and returning the governed result and applicable Event references.

## Governance

### Protected Action

An action that may create legal, financial, communicative, security, data or authoritative state consequences and therefore requires current authority and gates.

### Human Review

An accountable examination by an eligible person of an exact subject, version, scope and intended action.

### Approval

A Human Review decision allowing the reviewed subject to proceed within stated scope and conditions. Approval is not execution.

### Authorization

Current Permission and Policy authority to perform a protected action. Authorization is distinct from professional approval.

### Review Gate

The point at which execution must obtain or validate Human Review before continuing.

### Permission

The actor-specific authority to access information or request an action.

### Policy

The governing rule set that constrains data use, action, review, retention, security and other execution behavior.

### Fail Closed

The rule that protected execution stops when required authority, state, version or gate cannot be established.

### Safe Failure

A truthful, bounded execution result that preserves confirmed effects, exposes uncertainty and identifies the next governed action.

### Graceful Degradation

Continued availability of a narrower safe capability when a non-essential capability is unavailable. Governance gates may not be degraded.

### Override

A separately governed exception to a blocked condition. It is not an administrator bypass and does not remove unrelated gates.

## Retry and Change

### Idempotency

The property that repeated handling of the same semantic operation does not create duplicate effects.

### Retry

A later permitted attempt after failure, interruption or changed condition.

### Idempotent Replay

Return or reuse of an existing governed result without repeating the underlying effect.

### Continuation

Resume from a verified safe checkpoint after partial progress.

### Reconciliation

A governed process for determining whether an uncertain effect occurred.

### Partial Completion

An execution outcome in which some governed effects completed while others did not.

### Uncertain Outcome

A condition in which available evidence cannot establish whether an effect occurred.

### Change Control

The governed process for proposing, assessing, approving, activating, migrating, deprecating or reversing a version change.

### Migration

A governed move of references, data or execution context from one version to another without rewriting historical facts.

### Rollback

A new governed decision to restore a prior approved version or behavior. It does not automatically undo external effects.

## Communication and Events

### Communication

A governed message package with content, participants, recipients, attachments, purpose, channel and lifecycle.

### Communication Package

The exact versioned combination of body, subject, recipients, attachments, sender, channel and purpose presented for review or send.

### Send

A protected action performed through Communication Service and the approved Integration boundary. Approval for send is not send.

### Delivery

Evidence that a provider or channel delivered a Communication. Delivery is distinct from send and receipt.

### Event

A governed fact emitted by an owning Service or approved Event boundary.

### Domain Event

An Event that records a meaningful domain change. A log, tool call or Workflow observation is not automatically a Domain Event.

### Event Trace

The correlated Event and execution references used to understand what occurred across an operation.

### Audit Context

The actor, purpose, version, authority, review and correlation information required to interpret an execution fact.

### Audit Replay

Read-only reconstruction of historical execution. It must not repeat effects.

## AI and Agents

### AI Assistant

A software capability that extracts, summarizes, compares, drafts or recommends under governed context. It does not own professional authority.

### Agent

A software actor that may select or sequence permitted steps and call approved tools within an explicit authority envelope.

### Agent Authority Envelope

The bounded purpose, data scope, tools, operations, time, cost, review and stop conditions governing one agent's participation.

### Human–AI Handoff

The structured transfer of sources, versions, outputs, limitations and unresolved decisions between AI-assisted preparation and accountable Human Review.

### AI Assistance Disclosure

The trace identifying where AI materially assisted preparation and which sources, versions and limitations applied.

### Professional Truth

A professionally accountable conclusion that cannot be created merely by AI confidence, Product presentation or technical success.

## Observability and MVP

### Observability

The ability to understand current execution state and behavior from governed signals.

### Monitoring

Ongoing inspection of selected signals against expected operational or governance conditions.

### Audit

The preserved evidence required to reconstruct accountable execution after the fact.

### Execution MVP

The smallest governed implementation that proves Book 03 boundaries: eight previews, three internal apply paths, current gates, Service ownership, safe failure and audit, with external protected actions deferred.

### Depth A

Apply-enabled internal preparation for Intake, Application Preparation and Communication Review. No external protected action occurs.

### Depth B

Governed preview only for Provider Routing, Office Action Response, Renewal, Assignment and Evidence Review.

### Depth C

Deferred protected execution, including send, filing, payment, provider engagement, official recordal and autonomous professional action.
