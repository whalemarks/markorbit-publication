# B03-CH-33 — MVP Implementation Readiness

**Status:** Release Candidate 1

## Chapter Purpose

A manuscript boundary is not implementation readiness.

The MarkOrbit Execution MVP becomes implementation-ready only when the selected workflow set can be translated into code without forcing engineers, Products, agents or integrations to invent authority that belongs to Core contracts, owning Services or Human Review.

The governing principle is:

```text
Do not begin implementation because the workflow is desirable.
Begin implementation only when the contracts, owners, gates, effects, failures and audit requirements are ready enough to prevent boundary drift.
```

This chapter defines the readiness criteria for moving the Book 03 Execution MVP from architecture to implementation.

It answers:

- what must be ready in Book 02;
- what must be ready in Execution;
- what Services must own;
- what Workflows may coordinate;
- what Human Review must capture;
- what AI may assist with;
- what Product may consume;
- what tests must prove;
- what is still blocked or deliberately deferred.

Implementation readiness is not the same as full production readiness.

It is the minimum governed condition under which Codex, engineers or automation may begin implementing the MVP without collapsing the MarkOrbit architecture.

The core readiness path is:

```text
workflow selected
→ Book 02 dependencies checked
→ Service ownership confirmed
→ preview and apply depth confirmed
→ Permission, Policy and Human Review gates defined
→ version, idempotency and error behavior specified
→ Event and audit expectations defined
→ AI and Product boundaries confirmed
→ acceptance tests written
→ unsupported actions locked
→ implementation may begin
```

---

## 1. Dependency Baseline

This chapter depends directly on:

- [Chapter 31 — Execution MVP Boundary](B03-CH-31_Execution_MVP_Boundary.md)
- [Chapter 32 — MVP Execution Workflow Set](B03-CH-32_MVP_Execution_Workflow_Set.md)

It also depends on the governance chapters:

- [Chapter 25 — Idempotency and Retry Governance](B03-CH-25_Idempotency_and_Retry_Governance.md)
- [Chapter 26 — Error Handling and Safe Failure](B03-CH-26_Error_Handling_and_Safe_Failure.md)
- [Chapter 27 — Versioning and Change Control](B03-CH-27_Versioning_and_Change_Control.md)
- [Chapter 28 — Human Review Governance](B03-CH-28_Human_Review_Governance.md)
- [Chapter 29 — Agent-Assisted Execution Governance](B03-CH-29_Agent-Assisted_Execution_Governance.md)
- [Chapter 30 — Execution Observability and Audit](B03-CH-30_Execution_Observability_and_Audit.md)

It must remain consistent with the Part III workflow patterns:

- Intake Execution;
- Application Preparation;
- Communication Review;
- Provider Routing Preparation;
- Office Action Response Preparation;
- Renewal Preparation;
- Assignment Preparation;
- Evidence Review Preparation.

Its primary Book 02 dependencies are:

- Core Domain Registry;
- Core Object contracts;
- Core Service contracts;
- Workflow Contract primitive;
- Task primitive and Task Service contract;
- Communication contract and Communication Service contract;
- Event contract and Event catalog;
- Permission and Policy contracts;
- Human Review contract;
- versioning, idempotency and error contracts;
- AI governance contracts;
- audit context.

Book 03 may define readiness criteria.

Book 03 must not fill missing Book 02 contracts with local implementation shortcuts.

---

## 2. What Implementation Readiness Means

Implementation readiness means the MVP can be built with controlled ambiguity.

It does not mean every future workflow is complete.

It does not mean every Product screen is designed.

It does not mean production connectors are available.

It does not mean official filing, payment or external send are ready.

It means the implementation team can build the current MVP without guessing the following:

- which workflows are in scope;
- which workflows can apply;
- which effects are allowed;
- which effects are prohibited;
- which Services own mutations;
- which gates must pass;
- which versions are bound;
- which errors stop execution;
- which retries are safe;
- what audit must record;
- where AI must stop;
- what Product must not imply.

Readiness is a governance condition.

A feature can be technically easy and not implementation-ready.

A feature can be commercially important and not implementation-ready.

A feature can be impressive in a demo and still be outside the MVP boundary.

---

## 3. Readiness Levels

The Execution MVP should use readiness levels to avoid premature implementation.

These levels are explanatory governance labels. They do not create new Book 02 controlled values unless later formalized.

### 3.1 Level 0 — Concept Only

The workflow or capability is described conceptually.

It lacks one or more of:

- Core contract;
- Service owner;
- effect boundary;
- Human Review gate;
- idempotency;
- error handling;
- audit model.

It must not be implemented as executable behavior.

### 3.2 Level 1 — Contract Candidate

The required Core contract shape is known, but not fully approved or implemented.

It may support drafting, review and fixtures.

It must not drive production execution.

### 3.3 Level 2 — Fixture and Validation Ready

The contract has deterministic examples, validators and boundary tests.

It may support:

- fixture-based preview;
- developer testing;
- documentation examples;
- boundary verification.

It still may not be ready for Service-owned mutation.

### 3.4 Level 3 — Preview Ready

The workflow can assemble governed context and return side-effect-free preview.

It may support:

- validation;
- gap detection;
- readiness analysis;
- review questions;
- AI-assisted preparation where allowed.

It must not apply.

### 3.5 Level 4 — Internal Apply Ready

The workflow may perform approved internal effects through owning Services.

It requires:

- Service ownership;
- Permission and Policy checks;
- Human Review where required;
- version binding;
- idempotency;
- safe failure;
- Event and audit references;
- tests proving prohibited external action remains blocked.

This is the highest readiness level for the current Depth A workflows.

### 3.6 Level 5 — External Protected Action Ready

The workflow can perform externally consequential action such as send, submit, pay, file or instruct.

This level is outside the current Execution MVP.

It requires separate future governance, integration readiness, reconciliation, incident handling and production controls.

### 3.7 Current MVP Target

The current target is:

```text
Depth A workflows → Level 4 Internal Apply Ready
Depth B workflows → Level 3 Preview Ready
Depth C actions → below implementation scope
```

---

## 4. Global Readiness Criteria

No workflow is implementation-ready unless the following global conditions are satisfied.

### 4.1 Boundary Is Explicit

The implementation must know whether the workflow is:

- apply-enabled internally;
- preview-only;
- deferred.

Ambiguous apply behavior is not allowed.

### 4.2 Book 02 Dependencies Are Identified

Every workflow must identify its required Core contracts and owning Services.

Missing dependencies must be marked.

### 4.3 Service Ownership Exists

Any mutation must be delegated to an owning Service.

Workflow implementation must not write authoritative state directly.

### 4.4 Permission and Policy Gates Exist

The workflow must identify where access and action gates occur.

A temporary bypass for implementation convenience is not readiness.

### 4.5 Human Review Is Defined

Where Human Review is required, the implementation must know:

- subject;
- version;
- reviewer;
- decision;
- scope;
- conditions;
- expiry or stale behavior where applicable.

### 4.6 Version Binding Exists

The workflow must bind source, preview, review and apply versions.

### 4.7 Idempotency Exists

Any supported apply must define its semantic operation and idempotency scope.

### 4.8 Safe Failure Exists

The implementation must know how to stop without creating false success, duplicate effects or hidden uncertainty.

### 4.9 Event and Audit Expectations Exist

The implementation must know which references and decisions must be traceable.

### 4.10 AI Boundary Exists

The implementation must know what AI may prepare and what AI may not decide.

### 4.11 Product Boundary Exists

The implementation must not depend on Product UI to enforce execution truth.

### 4.12 Tests Exist Before Expansion

Readiness requires tests for prohibited behavior, not only successful behavior.

---

## 5. Book 02 Dependency Readiness

Book 03 implementation depends on Book 02 being sufficiently stable.

### 5.1 Required Contract Surfaces

For the current MVP, Book 02 should provide or approve:

- Core Domain Registry;
- object base contract;
- Event primitive and catalog;
- Task primitive and Task Service skeleton;
- Workflow Contract primitive and workflow catalog;
- Communication contract skeleton;
- Permission contract skeleton;
- Policy contract skeleton;
- Human Review contract;
- AI Governance contract skeleton;
- versioning contract;
- idempotency contract;
- error contract;
- audit context contract.

Where a contract is only skeleton-level, the implementation must keep behavior correspondingly shallow.

Skeleton contracts support validation and boundary proof.

They do not authorize deep production behavior.

### 5.2 Contract Readiness Questions

For each dependency, ask:

1. Does the contract exist?
2. Does it define enough structure for this workflow?
3. Does it define ownership?
4. Does it define allowed and prohibited behavior?
5. Does it define controlled values where needed?
6. Does it support validation?
7. Does it support fixtures?
8. Does it identify non-goals?
9. Is its version known?
10. Is implementation allowed to consume it?

If any answer is no, the workflow must reduce depth, stop, or return the gap to Book 02.

### 5.3 No Local Contract Invention

Implementation must not introduce local substitutes for:

- Task status;
- Communication state;
- Event type;
- Permission result;
- Policy result;
- Review decision;
- AI authority;
- object lifecycle;
- external outcome.

A local type used temporarily for implementation testing must not become public contract or Product semantics.

---

## 6. Service Ownership Readiness

Execution coordinates.

Services own behavior.

### 6.1 Required Service Capabilities

For Depth A workflows, owning Services must be ready enough to support:

- validation of requested mutation;
- object or draft creation where allowed;
- active Task creation;
- review request or review-state handling;
- idempotent response;
- version check;
- error response;
- Event reference or audit reference;
- refusal of unsupported action.

### 6.2 Service Stub vs Service Contract

A stub may be acceptable for fixture-level or preview-level testing.

A stub is not sufficient for internal apply unless it enforces the relevant boundaries.

A dangerous stub is one that always returns success.

### 6.3 Service Must Reject Unsupported Effects

For example:

- Communication Service must reject send in the current MVP;
- Task Service must prevent duplicate active Tasks under the same semantic request;
- Provider-related Services must not create engagement;
- Filing-related Services must not submit.

### 6.4 Service Result Must Be Exact

A Service response should distinguish:

- created;
- existing returned;
- unchanged;
- blocked;
- failed safely;
- uncertain;
- unsupported.

A generic success response is not sufficient for governed execution.

---

## 7. Workflow Contract Readiness

Each workflow needs a defined contract, even if there is no full engine.

### 7.1 Required Workflow Metadata

Each workflow should define:

- id;
- name;
- depth;
- purpose;
- supported inputs;
- required references;
- allowed preview outputs;
- allowed apply effects;
- prohibited effects;
- review gates;
- Service dependencies;
- idempotency scope;
- version requirements;
- failure modes;
- audit expectations;
- AI boundary.

### 7.2 No Hidden Transition

All transition from preview to apply must be explicit.

For Depth B workflows, apply must return a safe unsupported result.

### 7.3 Workflow Contract Version

Implementation must know which Workflow Contract version governs a run.

Changing the contract requires change control.

### 7.4 Workflow Does Not Become Service

The workflow implementation must not own:

- object mutation;
- Task mutation;
- Communication mutation;
- Event emission;
- official status;
- payment state;
- provider commitment.

---

## 8. Preview Readiness

Preview is the safest execution depth but still requires readiness.

### 8.1 Preview Requirements

A preview implementation must:

- validate supported input;
- check Permission for data access;
- apply Policy for data use;
- identify versions;
- disclose source limitations;
- return missing fields;
- identify unsupported scope;
- preserve AI disclosure where used;
- avoid side effects;
- avoid creating active Tasks;
- avoid emitting governed Events.

### 8.2 Preview Determinism

A preview may change when source versions change.

It should therefore identify the version basis.

For fixture tests, deterministic examples should exist.

### 8.3 Preview Boundary Tests

Tests must prove preview does not:

- mutate objects;
- create Tasks;
- send Communications;
- select providers;
- submit filings;
- pay;
- emit Events.

### 8.4 Preview Output Quality

A preview should be useful enough to support Human Review or next preparation.

It should not be a generic placeholder.

---

## 9. Internal Apply Readiness

Internal apply is the deepest current MVP behavior.

### 9.1 Apply Preconditions

Before internal apply, Execution must verify:

- workflow is Depth A;
- input is valid;
- source versions are current or compatible;
- Permission allows the operation;
- Policy allows the operation;
- required Human Review exists;
- idempotency scope is valid;
- owning Services are available;
- prohibited external effects are disabled.

### 9.2 Apply Effects

Internal apply may coordinate only effects defined in Chapter 32.

Examples:

- Customer or Brand linkage for Intake;
- internal Trademark preparation state for Application Preparation;
- Communication draft or review state for Communication Review;
- active Task creation where allowed.

### 9.3 Apply Output

Apply output must state:

- what was created or updated;
- what already existed;
- what was blocked;
- what was not attempted;
- which Event or audit references were returned;
- whether any part is uncertain;
- what next action is allowed.

### 9.4 Apply Boundary Tests

Tests must prove:

- Depth B apply is rejected;
- external send is unavailable;
- filing is unavailable;
- payment is unavailable;
- provider engagement is unavailable;
- stale review blocks apply;
- idempotent replay does not duplicate effects;
- missing Permission or Policy blocks apply.

### 9.5 No Partial Hidden Success

If one Service effect completes and another fails, the result must preserve partial completion.

It must not return a generic failure that hides completed effects.

---

## 10. Human Review Readiness

Human Review readiness is required before any workflow can claim governed approval.

### 10.1 Minimum Review Contract

Implementation must capture:

- review subject;
- version;
- intended action;
- reviewer identity;
- decision;
- decision time;
- scope;
- conditions where applicable;
- stale or supersession relationship.

### 10.2 Review State and Apply

Apply must verify the review still applies.

It must fail safely when:

- reviewed version differs from apply version;
- subject changed;
- intended action changed;
- approval expired;
- decision was revoked;
- conditions are unsatisfied;
- reviewer is not eligible under current gates.

### 10.3 Review Request vs Review Decision

A review request is not approval.

A reviewer comment is not necessarily approval.

A Product confirmation is not approval unless captured under the Human Review contract.

### 10.4 MVP Scope

The MVP may implement a basic review model.

It does not need to implement every future quorum, delegation, dissent or override model.

But it must not fake them.

Unsupported review complexity must stop or escalate.

---

## 11. Permission and Policy Readiness

Permission and Policy readiness protects both preview and apply.

### 11.1 Preview Access

Preview may expose sensitive data.

Permission and Policy must apply before preview output is returned.

### 11.2 Apply Authority

Apply requires stronger gates than preview where protected effects occur.

### 11.3 Policy Unavailable

If a required Policy evaluation is unavailable, protected apply fails closed.

### 11.4 No Default Allow

Implementation must not default to allow when Permission or Policy result is missing.

### 11.5 Test Obligations

Tests must include:

- denied preview access;
- denied apply;
- Policy block;
- unavailable Policy;
- restricted Document or Evidence access;
- AI processing restricted by Policy.

---

## 12. Versioning Readiness

Versioning must be present from the beginning.

### 12.1 Required Version Surfaces

Implementation should identify versions for:

- workflow contract;
- input package;
- subject object;
- draft Communication;
- attachments;
- review package;
- apply request;
- relevant Knowledge;
- AI output where material.

### 12.2 Stale Version Behavior

A stale version must not be applied silently.

Implementation must return:

```text
version conflict
review stale
preview stale
regeneration required
renewed review required
```

as applicable.

### 12.3 Test Obligations

Tests must include:

- draft changed after review;
- attachment changed after approval;
- goods/services changed after application preparation review;
- Knowledge version changed before protected apply;
- Workflow Contract version mismatch.

### 12.4 Historical Preservation

The system must preserve which version governed the decision.

It must not render old decisions using only current content.

---

## 13. Idempotency and Retry Readiness

Implementation readiness requires duplicate protection.

### 13.1 Required Idempotency Areas

For Depth A, idempotency is required for:

- Customer or Brand creation or linkage;
- Matter creation;
- Trademark preparation state;
- Task creation;
- Communication draft creation;
- review request creation;
- internal apply result.

### 13.2 Retry Classification

Implementation must distinguish:

- replay existing result;
- retry safe before effect;
- continue partial completion;
- require reconciliation;
- reject conflict;
- fail terminally.

### 13.3 Test Obligations

Tests must include:

- same key and same semantic request returns existing result;
- same key and different semantic request fails;
- repeated Task creation does not duplicate active Task;
- lost Service response can be reconciled;
- retry does not send, file or pay.

### 13.4 No Blind Automatic Retry

The MVP must not implement unbounded automatic retry for protected effects.

---

## 14. Error and Safe Failure Readiness

Errors must be safe, specific and actionable.

### 14.1 Required Error Classes

Implementation should distinguish:

- validation failure;
- Permission denial;
- Policy block;
- Human Review required;
- version conflict;
- unsupported workflow depth;
- idempotency conflict;
- Service failure;
- partial completion;
- uncertain outcome;
- AI output incomplete;
- external action prohibited.

### 14.2 Safe Error Output

An error output should state, where permitted:

- what was requested;
- why it stopped;
- what happened;
- what did not happen;
- what remains uncertain;
- what action may occur next.

### 14.3 Security-Safe Error Exposure

Errors must not expose:

- secrets;
- internal stack traces;
- hidden Policy logic;
- confidential unrelated data;
- private review notes;
- prompt internals;
- restricted provider terms.

### 14.4 Test Obligations

Tests must include:

- validation error;
- denied access;
- stale version;
- unsupported apply;
- partial apply failure;
- AI unavailable;
- connector disabled;
- external action attempted and blocked.

---

## 15. Event and Audit Readiness

The MVP must preserve trace without overbuilding event infrastructure.

### 15.1 Required Audit Context

Supported workflows must trace:

- operation;
- actor;
- versions;
- Permission and Policy outcomes;
- Human Review;
- Service effects;
- idempotency;
- errors;
- AI assistance;
- Event or audit references.

### 15.2 Event Ownership

Events must come from owning Services or approved Event boundaries.

Workflow and agents must not independently emit governed Events.

### 15.3 Audit Replay

Audit replay must be read-only.

### 15.4 Test Obligations

Tests must prove:

- Event references are returned only from owning Service results;
- no Event is emitted for preview-only workflows;
- no send Event exists in Communication Review;
- no filing Event exists in Application Preparation;
- audit identifies the approved version used for apply.

---

## 16. AI and Agent Readiness

AI and agents are useful only if their boundaries are implemented.

### 16.1 Allowed AI Assistance

Implementation may support:

- extraction;
- summarization;
- comparison;
- missing-field detection;
- draft generation;
- review-question generation;
- safe-error explanation;
- preparation of Task plans.

### 16.2 Required AI Controls

The implementation must preserve:

- AI assistance disclosure;
- source references;
- output version;
- limitations;
- Human Review requirement;
- restricted data handling;
- blocked protected actions.

### 16.3 Agent Tool Readiness

Any agent-accessible tool must specify:

- read or mutation classification;
- permitted scope;
- Permission and Policy enforcement;
- idempotency;
- audit;
- prohibited actions.

### 16.4 Test Obligations

Tests must prove AI or agents cannot:

- approve;
- satisfy review;
- send;
- submit;
- pay;
- select provider;
- complete protected Task;
- mutate protected state directly;
- emit governed Events;
- bypass Permission or Policy.

### 16.5 AI Unavailable

AI unavailability must degrade to human-controlled work.

It must not remove the workflow.

---

## 17. Product Consumption Readiness

The Execution MVP may be implemented before Book 04 Workplace and Product surfaces are complete.

However, the execution output must be safe for Product consumption.

### 17.1 Product-Ready Semantics

Outputs must distinguish:

- preview;
- apply;
- blocked;
- failed safely;
- review required;
- approved;
- internal applied;
- external action not performed;
- uncertain;
- unsupported.

### 17.2 Product Must Not Infer

The Product should not need to infer that:

- send did not happen;
- filing did not happen;
- payment did not happen;
- provider was not selected;
- Evidence was not certified.

The execution response should say so.

### 17.3 Product Mislabeling Prevention

Implementation should provide exact language or flags to prevent unsafe labels.

For example:

```text
internalPreparationApplied: true
externalSubmissionOccurred: false
communicationSent: false
```

The exact field names belong to implementation contracts.

The semantic requirement belongs to Book 03.

### 17.4 Test Obligations

Tests should verify outputs cannot be reasonably interpreted as external completion when only internal apply occurred.

---

## 18. Integration Readiness

External integration is mostly deferred in the current MVP.

### 18.1 Allowed Integration Readiness

The MVP may include:

- fixture-backed integrations;
- read-only status checks;
- disabled connector responses;
- contract validation;
- simulated external errors;
- explicit not-enabled behavior.

### 18.2 Disallowed Integration Behavior

The MVP must not perform:

- production send;
- production filing;
- production payment;
- provider instruction;
- official recordal;
- external Evidence disclosure;

unless a later phase explicitly approves that action.

### 18.3 Connector Disabled Test

Every deferred connector must fail safely with a clear boundary response.

### 18.4 Read-Only Integration

A read-only integration must still enforce Permission, Policy, source version and data minimization.

---

## 19. Security and Privacy Readiness

MVP scope does not reduce security obligations.

### 19.1 Required Controls

Implementation must address:

- organization separation;
- Matter separation;
- least privilege;
- restricted Document access;
- Evidence confidentiality;
- safe error exposure;
- audit access;
- external content distrust;
- AI data processing Policy;
- secret protection;
- export control.

### 19.2 Fixture Safety

Fixtures should avoid real confidential or personal data unless explicitly approved and governed.

### 19.3 Prompt and Tool Security

AI and agent implementations must treat external text as data, not instruction authority.

### 19.4 Test Obligations

Tests should include:

- unauthorized Matter access;
- restricted Document preview;
- prompt-injection-like input;
- tool attempt outside authority envelope;
- export attempt without Permission.

---

## 20. Observability Readiness

The MVP must be observable enough to prove that it stayed inside its boundary.

### 20.1 Required Signals

Implementation should expose or record:

- workflow depth;
- preview or apply;
- Service calls;
- Human Review state;
- blocked actions;
- disabled connectors;
- AI assistance;
- idempotency result;
- version conflict;
- partial completion;
- safe failure;
- Event references.

### 20.2 Boundary Observability

It must be possible to detect:

- attempted send;
- attempted filing;
- attempted payment;
- attempted provider engagement;
- attempted apply for Depth B workflow;
- attempted Event emission by Workflow or agent;
- attempted stale approval reuse.

### 20.3 Operational Minimalism

The MVP does not require a complete monitoring platform.

It requires enough trace and test visibility to prove governance.

---

## 21. Test Readiness

Tests define implementation trust.

### 21.1 Test Categories

The MVP should include tests for:

- contract validation;
- fixture parity;
- preview behavior;
- apply behavior;
- unsupported apply;
- Permission and Policy gates;
- Human Review binding;
- version conflict;
- idempotency;
- safe failure;
- Event ownership;
- AI boundary;
- Product-safe output;
- connector disabled behavior;
- security and privacy restrictions.

### 21.2 Negative Tests

Negative tests are as important as positive tests.

The system must prove it does not:

- send;
- file;
- pay;
- select provider;
- emit Events directly from Workflow;
- accept stale approval;
- treat AI as reviewer;
- bypass Permission or Policy;
- create duplicate Tasks.

### 21.3 Fixture Tests

Fixtures should cover:

- happy path;
- missing data;
- stale version;
- denied Permission;
- Policy block;
- review required;
- unsupported apply;
- idempotent replay;
- partial completion;
- AI output incomplete.

### 21.4 Acceptance Tests

Each workflow should have acceptance tests derived from Chapter 32.

---

## 22. Documentation Readiness

Implementation should not proceed without developer-facing documentation.

Required documentation includes:

- workflow depth matrix;
- allowed effects;
- prohibited effects;
- Core dependencies;
- Service ownership;
- apply preconditions;
- review requirements;
- error behavior;
- AI boundary;
- audit requirements;
- Product interpretation notes;
- non-goals.

Documentation is not a substitute for tests.

But undocumented boundaries are likely to drift.

---

## 23. Change Control Readiness

The MVP boundary must be protected during implementation.

### 23.1 Scope Change Triggers

Change control is required if implementation proposes to:

- enable apply for Depth B workflow;
- send Communication;
- file or submit;
- pay;
- engage provider;
- complete protected Task automatically;
- add mutation-capable agent tool;
- create new Event type;
- create new Core object;
- change review requirement;
- weaken Permission or Policy;
- add production connector.

### 23.2 Pull Request Boundary

Implementation pull requests should state:

- workflow depth affected;
- allowed effects;
- prohibited effects preserved;
- tests added;
- Book 02 dependencies used;
- boundary changes, if any.

### 23.3 No Mixed Expansion

A readiness task should not combine:

- contract creation;
- Service mutation;
- Product UI;
- connector activation;
- AI agent expansion;

unless explicitly approved.

Controlled sequencing is part of readiness.

---

## 24. Workflow Readiness Assessment

### 24.1 Intake Execution

Current target:

```text
Level 4 — Internal Apply Ready
```

Implementation may begin when:

- Customer, Brand, Matter, Document and Task ownership are clear;
- duplicate detection and idempotency exist;
- Permission and Policy gates exist;
- no engagement, payment, provider or filing effect is possible;
- audit can reconstruct created internal references.

Primary risk:

```text
intake being mistaken for accepted professional engagement
```

Required lock:

```text
Intake apply must state no legal engagement, provider instruction, payment or filing occurred.
```

### 24.2 Application Preparation

Current target:

```text
Level 4 — Internal Apply Ready
```

Implementation may begin when:

- Trademark preparation, Brand linkage, Classification references, Document and Task effects have owning Services;
- Human Review binding is clear;
- stale package behavior exists;
- no official filing can occur;
- no final professional classification is automated.

Primary risk:

```text
internal readiness being mistaken for filing authority
```

Required lock:

```text
Application Preparation apply must state no official filing occurred.
```

### 24.3 Communication Review

Current target:

```text
Level 4 — Internal Apply Ready
```

Implementation may begin when:

- Communication draft and review states are Service-owned;
- approved package version is bound;
- changed content or attachment blocks approval reuse;
- send is technically unavailable in the workflow;
- no send Event can be produced.

Primary risk:

```text
approval being mistaken for send
```

Required lock:

```text
Communication Review must not transmit externally.
```

### 24.4 Provider Routing Preparation

Current target:

```text
Level 3 — Preview Ready
```

Implementation may begin when:

- provider data access is Permission and Policy controlled;
- quote and capability versions are identified;
- preview output discloses missing data;
- apply returns unsupported;
- no provider selection, engagement or instruction effect exists.

Primary risk:

```text
recommendation being mistaken for provider selection
```

Required lock:

```text
No provider selected or contacted.
```

### 24.5 Office Action Response Preparation

Current target:

```text
Level 3 — Preview Ready
```

Implementation may begin when:

- office action Document version is bound;
- deadline source limitations are visible;
- AI extraction limitations are disclosed;
- review questions are generated;
- apply returns unsupported;
- no submission occurs.

Primary risk:

```text
strategy preview being mistaken for legal strategy approval
```

Required lock:

```text
No response submitted and no deadline certified.
```

### 24.6 Renewal Preparation

Current target:

```text
Level 3 — Preview Ready
```

Implementation may begin when:

- Trademark record and renewal Knowledge versions are bound;
- date source and confidence are disclosed;
- fee and Document gaps are identified;
- apply returns unsupported;
- no payment or filing occurs.

Primary risk:

```text
renewal window preview being mistaken for deadline certification
```

Required lock:

```text
No payment or renewal filing occurred.
```

### 24.7 Assignment Preparation

Current target:

```text
Level 3 — Preview Ready
```

Implementation may begin when:

- party and Document versions are bound;
- authority and signature gaps are surfaced;
- apply returns unsupported;
- no ownership record changes;
- no recordal is submitted.

Primary risk:

```text
package preparation being mistaken for legal transfer or recordal
```

Required lock:

```text
No ownership change or official recordal occurred.
```

### 24.8 Evidence Review Preparation

Current target:

```text
Level 3 — Preview Ready
```

Implementation may begin when:

- Evidence Document versions and source metadata are bound;
- confidentiality Policy is enforced;
- AI extraction is disclosed;
- review questions are produced;
- apply returns unsupported;
- no sufficiency certification occurs.

Primary risk:

```text
Evidence organization being mistaken for authenticity or sufficiency certification
```

Required lock:

```text
No Evidence sufficiency decision was made.
```

---

## 25. Readiness Checklist

Before implementation begins for any workflow, confirm:

```text
[ ] Workflow depth is explicit.
[ ] Book 02 dependencies are identified.
[ ] Owning Services are identified.
[ ] Allowed effects are listed.
[ ] Prohibited effects are listed.
[ ] Preview behavior is side-effect free.
[ ] Apply behavior is defined only if Depth A.
[ ] Permission gates are defined.
[ ] Policy gates are defined.
[ ] Human Review gates are defined.
[ ] Version surfaces are defined.
[ ] Idempotency scope is defined.
[ ] Error and safe failure behavior is defined.
[ ] Event and audit expectations are defined.
[ ] AI assistance boundary is defined.
[ ] Product interpretation boundary is defined.
[ ] Integration boundary is defined.
[ ] Security and privacy requirements are defined.
[ ] Negative tests are planned.
[ ] Unsupported actions fail safely.
[ ] Scope-change triggers are documented.
```

A workflow missing any critical item must not move to deeper execution.

---

## 26. Implementation Sequencing

The safest implementation order is:

```text
1. Contract and fixture alignment
2. Workflow depth registry
3. Preview validators
4. Safe unsupported apply responses for Depth B
5. Task plan and active Task boundary
6. Human Review request and decision binding
7. Depth A internal apply through owning Services
8. Idempotency and retry tests
9. Version conflict tests
10. Event and audit reference tests
11. AI assistance boundaries
12. Product-safe output contract
13. Security and privacy tests
14. Readiness review
```

This order prevents the most common drift:

```text
building Product-visible automation before governance exists
```

or:

```text
building apply behavior before preview, review and failure are stable
```

---

## 27. Readiness Failure Modes

Implementation is not ready if any of the following appears:

- a Workflow writes Core state directly;
- a Product button creates protected effects without Service ownership;
- preview creates active Tasks;
- Communication approval sends a message;
- Provider Routing selects or contacts a provider;
- Application Preparation files;
- Renewal Preparation pays;
- Assignment Preparation changes ownership;
- Evidence Review certifies sufficiency;
- AI is treated as reviewer;
- stale version applies successfully;
- Permission or Policy defaults to allow;
- errors return generic success or generic failure;
- retry duplicates an active Task;
- Event is emitted by Workflow;
- connector performs production external action;
- unsupported apply creates partial state;
- tests cover only happy paths.

A readiness failure must stop implementation or reduce workflow depth.

---

## 28. Minimal Readiness Decision

A readiness decision should produce one of the following outcomes.

### 28.1 Ready for Fixture Implementation

The workflow may be represented in fixtures and validation only.

### 28.2 Ready for Preview Implementation

The workflow may return side-effect-free preview.

### 28.3 Ready for Internal Apply Implementation

The workflow may coordinate selected Service-owned internal effects.

### 28.4 Not Ready

The workflow must remain conceptual or be routed back to Book 02.

### 28.5 Deferred

The workflow or action is intentionally excluded from the current MVP.

The decision should identify:

- reason;
- missing dependency;
- risk;
- required future work;
- owner;
- boundary lock.

---

## 29. Current MVP Readiness Decision

The current Book 03 readiness decision is:

```text
Ready for implementation planning with controlled scope.
```

More specifically:

```text
Intake Execution:
Target readiness — Internal Apply Ready, subject to Service ownership and tests.

Application Preparation:
Target readiness — Internal Apply Ready, subject to Service ownership and tests.

Communication Review:
Target readiness — Internal Apply Ready, but send remains disabled.

Provider Routing Preparation:
Target readiness — Preview Ready only.

Office Action Response Preparation:
Target readiness — Preview Ready only.

Renewal Preparation:
Target readiness — Preview Ready only.

Assignment Preparation:
Target readiness — Preview Ready only.

Evidence Review Preparation:
Target readiness — Preview Ready only.
```

This is not approval for:

- production send;
- filing;
- payment;
- provider engagement;
- official submission;
- assignment recordal;
- autonomous agent execution;
- full Product launch.

The MVP may move to implementation planning only if Chapter 34 preserves this controlled sequence.

---

## 30. Governance Rules

MVP Implementation Readiness is correct when:

1. implementation begins from Book 02 contracts rather than Product wishes;
2. workflow depth determines allowed behavior;
3. Depth A supports only approved internal Service-owned effects;
4. Depth B supports only preview and safe unsupported apply;
5. Depth C actions remain deferred;
6. owning Services perform all mutation;
7. Workflow never writes Core state directly;
8. Task plans remain distinct from active Tasks;
9. Human Review is version-bound and action-bound;
10. Permission and Policy fail closed;
11. stale versions block apply;
12. idempotency prevents duplicate effects;
13. partial completion remains visible;
14. safe failure identifies what did and did not happen;
15. Events come only from owning Services or approved Event boundary;
16. AI remains advisory and optional to correctness;
17. Product outputs are safe to present without implying external action;
18. connectors remain disabled for protected external effects;
19. negative tests prove prohibited behavior stays prohibited;
20. scope expansion requires change control;
21. readiness is reassessed when contracts, Services, Policies, Workflows or AI capabilities change.

---

## 31. Product Boundary

Book 04 may use the readiness model to decide which workflows appear, which controls remain disabled and how internal apply is explained. Product readiness remains a separate decision and cannot broaden execution depth.

## 32. Implementation Boundary

This chapter defines readiness criteria, not repository structure, code, APIs, storage, deployment, Service internals, Event infrastructure, Product UI or Codex task files. Chapter 34 translates readiness into implementation sequence.

## 33. Chapter Result

The MVP is implementation-ready only when it can be built without boundary invention.

The operating rule is:

```text
Start with contracts and fixtures.
Make workflow depth explicit.
Prove preview before apply.
Enable internal apply only through owning Services.
Bind Human Review to version and action.
Fail closed on Permission, Policy and stale state.
Keep external protected actions disabled.
Keep AI advisory.
Test prohibited behavior.
Expand only through change control.
```

The current MVP may move into controlled implementation planning.

It is not approved for external action, autonomous execution or broad Product launch.

The next chapter translates the readiness model into a staged implementation path for Codex and engineering work: **Chapter 34 — Codex Execution Roadmap**.
