# B03-CH-31 — Execution MVP Boundary

**Status:** Release Candidate 1

## Chapter Purpose

An Execution System MVP must be small enough to build, test and govern.

It must also be complete enough to prove that MarkOrbit can coordinate real professional work without collapsing Core, Execution, Integration and Product responsibilities into one application.

The governing principle is:

```text
Minimize scope.
Do not minimize governance.
Prove the execution boundaries before expanding execution depth.
```

The MarkOrbit Execution MVP is not a reduced version of every future capability.

It is the smallest governed execution system that can:

- consume approved Book 02 contracts;
- assemble bounded execution context;
- produce side-effect-free previews;
- coordinate selected internal preparation effects through owning Services;
- create accountable Human Review gates;
- preserve version, Permission, Policy, idempotency and audit context;
- expose safe failures and uncertainty;
- keep AI and agents within assistance boundaries;
- stop before external legal, financial, communicative or professional commitment.

This chapter defines the boundary of that MVP.

It does not define the complete workflow inventory, implementation architecture, database design, API surface, Product UI, production rollout plan or Codex task sequence. Those subjects are addressed by later chapters and their owning books or repositories.

The core boundary is:

```text
Book 02 defines Core contracts and authority.
Book 03 coordinates the smallest governed execution depth.
Integration connects through approved boundaries.
Book 04 presents Product experiences.
Humans remain accountable.
AI assists.
Owning Services mutate.
Events trace governed facts.
```

---

## 1. Dependency Baseline

This chapter applies the complete execution architecture established in Parts I–IV, especially:

- [Chapter 03 — Position Between Core and Product](B03-CH-03_Position_Between_Core_and_Product.md)
- [Chapter 05 — Execution Boundary](B03-CH-05_Execution_Boundary.md)
- [Chapter 07 — From Core Contracts to Execution Runtime](B03-CH-07_From_Core_Contracts_to_Execution_Runtime.md)
- [Chapter 08 — Execution Layer Overview](B03-CH-08_Execution_Layer_Overview.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 11 — Task Lifecycle Model](B03-CH-11_Task_Lifecycle_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)
- [Chapter 13 — Communication Execution Boundary](B03-CH-13_Communication_Execution_Boundary.md)
- [Chapter 14 — Event Trace, Audit and Replay](B03-CH-14_Event_Trace_Audit_and_Replay.md)
- [Chapter 15 — Permission and Policy Gates](B03-CH-15_Permission_and_Policy_Gates.md)
- [Chapter 16 — Human–AI Execution Handoff](B03-CH-16_Human_AI_Execution_Handoff.md)
- [Chapter 25 — Idempotency and Retry Governance](B03-CH-25_Idempotency_and_Retry_Governance.md)
- [Chapter 26 — Error Handling and Safe Failure](B03-CH-26_Error_Handling_and_Safe_Failure.md)
- [Chapter 27 — Versioning and Change Control](B03-CH-27_Versioning_and_Change_Control.md)
- [Chapter 28 — Human Review Governance](B03-CH-28_Human_Review_Governance.md)
- [Chapter 29 — Agent-Assisted Execution Governance](B03-CH-29_Agent-Assisted_Execution_Governance.md)
- [Chapter 30 — Execution Observability and Audit](B03-CH-30_Execution_Observability_and_Audit.md)

Its Part III workflow-pattern baseline is:

- [Chapter 17 — Intake Execution Pattern](B03-CH-17_Intake_Execution_Pattern.md)
- [Chapter 18 — Application Preparation Pattern](B03-CH-18_Application_Preparation_Pattern.md)
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)
- [Chapter 20 — Provider Routing Preparation Pattern](B03-CH-20_Provider_Routing_Preparation_Pattern.md)
- [Chapter 21 — Office Action Response Preparation Pattern](B03-CH-21_Office_Action_Response_Preparation_Pattern.md)
- [Chapter 22 — Renewal Preparation Pattern](B03-CH-22_Renewal_Preparation_Pattern.md)
- [Chapter 23 — Assignment Preparation Pattern](B03-CH-23_Assignment_Preparation_Pattern.md)
- [Chapter 24 — Evidence Review Preparation Pattern](B03-CH-24_Evidence_Review_Preparation_Pattern.md)

Its approved planning baseline includes:

- [MVP Execution Boundary](../planning/B03-PLN-0007_MVP_Execution_Boundary.md)
- [Review Gate Model](../planning/B03-PLN-0008_Review_Gate_Model.md)
- [Book 02 Dependency Map](../planning/B03-PLN-0005_Book_02_Dependency_Map.md)
- [Book 04 Boundary Map](../planning/B03-PLN-0006_Book_04_Boundary_Map.md)

Its primary Book 02 dependencies are:

- approved Core Domains, Objects and Services;
- Workflow Contract and Workflow Specification depth;
- Task contracts;
- Communication contracts;
- Event contracts;
- Permission and Policy Context;
- Human Review;
- idempotency;
- versioning;
- errors and safe validation;
- AI Context and Agent governance;
- audit context.

Book 02 remains authoritative.

Where a required Core contract is absent, ambiguous or inconsistent, the MVP must stop, stub, preview or route the gap back to Book 02. Book 03 must not repair the gap by inventing local Core truth.

---

## 2. What MVP Means

MVP means **minimum viable proof of the Execution System architecture**.

It does not mean:

- minimum professional quality;
- minimum security;
- minimum review;
- minimum audit;
- incomplete authority checks;
- temporary permission bypass;
- prototype behavior presented as production truth;
- broad automation with a small interface;
- a Product demonstration that hides missing Services.

The MVP is viable only if the boundaries are real.

A workflow that appears complete but mutates Core directly is not viable.

A communication feature that approves and sends in one hidden action is not viable.

An AI assistant that produces a professional conclusion without accountable review is not viable.

An implementation that cannot distinguish preview from apply is not viable.

An apparently successful operation without version, idempotency and trace is not viable.

The governing interpretation is:

```text
The MVP reduces the number and depth of supported execution paths.
It does not reduce the integrity of each supported path.
```

---

## 3. MVP Position in the MarkOrbit System

The Execution MVP occupies a narrow position.

```text
Book 02 Core Specification
    defines objects, contracts, Services, controlled values and authority
        ↓
Book 03 Execution MVP
    coordinates context, preview, Tasks, review, apply and trace
        ↓
Integration boundaries
    connect approved Services and external systems
        ↓
Book 04 Workplace and Product Architecture
    provides organization context and presents governed user journeys, controls and operational views
```

The Execution MVP does not become:

- the Core data model;
- the Product shell;
- the external connector layer;
- the professional knowledge authority;
- the provider marketplace;
- the filing portal;
- the payment system;
- the autonomous-agent runtime.

It proves that these responsibilities can remain separate while still producing useful operational progress.

---

## 4. The MVP Boundary Statement

The current MVP boundary is:

```text
The MVP may coordinate internal preparation and review.
It may create only those internal governed effects explicitly owned by approved Services.
It may not perform external professional commitment or irreversible protected action.
Preview is the default.
Apply is enabled only for selected internal preparation workflows.
All broader workflow patterns remain preview-only until separately approved.
```

The boundary has three execution depths.

These depths are Book 03 governance labels for explaining current scope. They do not create new Book 02 controlled values.

### Depth A — Apply-Enabled Internal Preparation

Selected Workflows may coordinate approved internal Core effects through owning Services.

The current set is:

1. Intake Execution;
2. Application Preparation;
3. Communication Review.

Even at this depth:

- Workflow does not mutate Core directly;
- apply does not file;
- apply does not pay;
- apply does not engage a provider;
- Communication Review does not send;
- AI does not approve;
- external legal effect does not occur.

### Depth B — Governed Preview Only

Selected patterns may validate, organize, compare, prepare and request review, but apply remains disabled.

The current set is:

1. Provider Routing Preparation;
2. Office Action Response Preparation;
3. Renewal Preparation;
4. Assignment Preparation;
5. Evidence Review Preparation.

These patterns may demonstrate execution semantics without creating protected downstream effects.

### Depth C — Deferred Protected Execution

The following remain outside the current MVP:

- external Communication send;
- official filing or submission;
- payment;
- provider selection and engagement;
- provider instruction dispatch;
- assignment recordal;
- renewal submission;
- office action response submission;
- Evidence certification;
- autonomous professional action;
- unrestricted Core mutation;
- autonomous Event emission.

Chapter 32 defines the workflow set in more detail.

---

## 5. Why the MVP Uses Multiple Depths

A single “implemented” or “not implemented” label is insufficient.

Some workflows can safely prove internal coordination before external action exists.

Other workflows become dangerous as soon as apply is treated as enabled.

For example:

- Intake can create or link governed internal records through owning Services.
- Application Preparation can build a governed workspace and active preparation Tasks.
- Communication Review can create a draft and record review status.
- Provider Routing cannot safely apply until selection, commercial approval, engagement and instruction boundaries exist.
- Office Action Response cannot safely apply if apply could be mistaken for legal strategy approval or submission.
- Renewal cannot safely apply without governed deadline, eligibility, fee, payment and filing boundaries.
- Assignment cannot safely apply if internal preparation is confused with legal effect or official recordal.
- Evidence Review cannot safely apply if organization is confused with authenticity, sufficiency or admissibility.

The multi-depth model allows the architecture to mature without pretending that every workflow has the same readiness.

---

## 6. Depth A — Allowed Internal Effects

Depth A apply may coordinate only effects already owned and validated by approved Services.

### 6.1 Intake Execution

Depending on the governing contract, Intake apply may coordinate:

- Customer creation or update;
- Brand creation or linkage;
- Matter creation;
- draft or scoped Order creation;
- Document validation or linkage;
- active Task creation;
- Communication draft creation;
- Event references from owning Services.

It may not represent these effects as:

- client acceptance;
- legal engagement;
- payment approval;
- filing authorization;
- provider appointment;
- professional conclusion.

### 6.2 Application Preparation

Application Preparation apply may coordinate:

- Trademark record creation or update;
- Brand linkage;
- Jurisdiction reference validation;
- draft or review-required Classification state;
- Document and Evidence linkage;
- Matter or Order preparation context;
- active preparation Tasks;
- review requirements;
- Event references from owning Services.

It may not:

- finalize professional classification by automation;
- certify filing readiness as legal advice;
- authorize filing;
- submit to an authority;
- pay official or provider fees.

### 6.3 Communication Review

Communication Review apply may coordinate:

- scoped draft creation;
- review request;
- review-status transition;
- reviewer note recording;
- follow-up Task creation;
- Event references from owning Services.

It may not:

- send;
- mark sent;
- infer delivery;
- infer receipt;
- expand recipients;
- replace the approved version;
- make an external commitment.

### 6.4 Internal Does Not Mean Low Risk

Internal effects still require:

- current version;
- Permission;
- Policy;
- Human Review where required;
- idempotency;
- safe failure;
- audit context;
- Service ownership.

The absence of external action does not remove governance.

---

## 7. Depth B — Allowed Preview Outputs

A preview-only workflow may return:

- validated request context;
- source and version references;
- missing-information list;
- readiness analysis;
- candidate options;
- comparison factors;
- review questions;
- risk flags;
- deadline context with limitations;
- Task plan preview;
- Communication outline;
- Human Review requirement;
- warnings;
- safe errors;
- explicit unsupported or unavailable result.

A preview-only workflow must not:

- create active Tasks;
- create or mutate Core records;
- create an external Communication;
- select a provider;
- approve a strategy;
- certify a deadline;
- certify Evidence;
- initiate payment;
- submit or file;
- emit governed Events;
- claim that apply occurred.

### 7.1 Preview Must State Its Depth

A preview should communicate its boundary clearly.

For example:

```text
This result is a governed preparation preview.
No protected action was performed.
No provider was selected.
No Communication was sent.
No payment or filing occurred.
Apply is not enabled for this workflow depth.
```

### 7.2 Preview Is Still Governed

Preview is side-effect free, but it is not governance free.

Preview must still respect:

- Permission;
- Policy;
- data minimization;
- versioning;
- source trace;
- AI disclosure;
- safe error exposure;
- Product boundary.

A user must not gain access to restricted information merely because the operation is called preview.

---

## 8. Outputs the MVP May Claim

The MVP may make exact, bounded claims such as:

- input validated against the supported contract;
- preview prepared;
- required information is missing;
- duplicate candidate identified;
- Human Review is required;
- draft created by Communication Service;
- review status updated by the owning Service;
- Task created by Task Service;
- internal object reference created or linked by the owning Service;
- operation blocked by Permission or Policy;
- version conflict detected;
- prior idempotent result returned;
- operation partially completed;
- external outcome remains uncertain;
- Event reference returned by the owning Service.

The MVP must not claim:

- legal sufficiency;
- registrability;
- deadline certainty without approved authority;
- Evidence authenticity or admissibility;
- provider suitability as final professional truth;
- provider engagement;
- successful payment;
- official submission;
- official acceptance;
- Communication delivery;
- assignment legal effect;
- completed renewal;
- autonomous approval.

Claims must describe the actual governed effect, not the intended business outcome.

---

## 9. Core Dependency Boundary

The MVP consumes Book 02.

It does not define new:

- Core Domains;
- Core Objects;
- Service ownership;
- API Contracts;
- Workflow Contracts;
- Event types;
- Task statuses;
- Permission models;
- Policy models;
- Human Review values;
- idempotency semantics;
- Error values;
- AI authority.

### 9.1 Dependency Gaps

If a required dependency is missing, the MVP response may be:

- unsupported;
- not implemented;
- preview only;
- blocked;
- awaiting Book 02 contract;
- requiring manual governed handling.

It must not create a local substitute that later becomes accidental Core truth.

### 9.2 Contract Version

Every supported execution path must identify the compatible contract version.

Unknown or incompatible versions fail safely.

### 9.3 Core Implementation Repository

A typed Core implementation may provide contract definitions, validators, fixtures and export surfaces.

That implementation does not, by itself, activate Book 03 execution.

Execution readiness still requires:

- approved consumption rules;
- owning Services;
- review gates;
- error and idempotency behavior;
- operational trace;
- scope-specific acceptance.

---

## 10. Workflow Boundary

Workflow coordinates.

Workflow does not own the records it touches.

The MVP Workflow layer may:

- assemble execution context;
- validate references;
- choose the allowed next coordination step;
- produce preview;
- request Human Review;
- prepare Task plans;
- invoke approved Services during allowed apply;
- correlate results;
- return Event references;
- stop safely.

It may not:

- mutate Core objects directly;
- bypass Service validation;
- invent status transitions;
- emit Domain Events directly;
- send Communication;
- perform official filing;
- execute payment;
- create provider commitments;
- treat Product interaction as authority.

### 10.1 Workflow Instance Is Not Domain Truth

A Workflow state may explain coordination progress.

It must not replace the authoritative status of:

- Trademark;
- Matter;
- Order;
- Communication;
- Task;
- payment;
- filing;
- provider service.

### 10.2 No Hidden Workflow Engine Expansion

The MVP must not add broad Workflow Engine behavior merely to support one pattern.

New transition, scheduling, compensation or runtime behavior requires explicit governance and Book 02 alignment.

---

## 11. Service and Mutation Boundary

Owning Services remain responsible for:

- validating object state;
- enforcing object invariants;
- applying authorized mutation;
- enforcing idempotency;
- returning exact results;
- producing or causing governed Events;
- preserving version relationships;
- rejecting unsupported operations.

Execution may request.

The Service decides under its contract.

### 11.1 No Direct Persistence From Workflow

Workflow must not write database records or construct authoritative object state directly.

### 11.2 Partial Apply

Where an apply can produce more than one Service result, the response must distinguish:

- completed effects;
- unchanged objects;
- failed effects;
- blocked steps;
- uncertain effects;
- created references;
- continuation requirements.

The MVP must not claim atomicity that the owning contracts do not provide.

### 11.3 No Synthetic Event

Execution must not emit an Event merely to make an operation appear complete.

---

## 12. Task Boundary

The MVP may prepare Task plans in preview.

A Task plan is not an active Task.

Only Task Service may create, update, complete, cancel or archive an active Task.

### 12.1 Allowed Task Use

Depth A apply may request active Tasks for:

- missing information;
- professional review;
- Document collection;
- Classification review;
- Evidence review;
- Communication review;
- follow-up preparation;
- reconciliation.

### 12.2 Duplicate Protection

Task creation must use the applicable idempotency and duplicate-candidate rules.

A lost response must not create a second active Task.

### 12.3 Task Completion

An AI assistant or Workflow must not mark a protected Task complete merely because a draft exists.

Completion belongs to the Task contract and authorized actor or Service.

---

## 13. Human Review Boundary

Human Review is mandatory wherever the governing contract requires accountable judgment.

The MVP must prove that review is:

- explicit;
- version-bound;
- scope-bound;
- action-bound;
- attributable;
- Permission and Policy governed;
- visible to apply;
- stale when material content changes.

### 13.1 Review Does Not Execute

Approval does not:

- create the final external effect;
- send;
- file;
- pay;
- select or engage a provider;
- mutate unrelated state.

### 13.2 Review Depth

The MVP may support ordinary review and escalation patterns needed by the supported Workflows.

It does not need to implement every future quorum, delegation, override or specialist-review model before proving the base architecture.

It must not, however, weaken a review requirement because an advanced model is unavailable.

### 13.3 No Product-Level Approval Shortcut

A generic confirmation control must not be treated as Human Review unless the exact subject, version, actor, decision and scope are captured under the approved contract.

---

## 14. Communication Boundary

The MVP includes Communication preparation and review.

It excludes production send.

This boundary is deliberate.

Communication send requires separate governance for:

- sender identity;
- recipient set;
- channel;
- attachments;
- approval conditions;
- current Permission;
- current Policy;
- idempotency;
- provider result;
- delivery;
- uncertainty;
- Event trace.

The MVP may prove that a Communication package can reach:

```text
drafted
→ reviewed
→ approved for a defined future send purpose
```

It must stop before:

```text
transmitted
→ delivered
→ received
```

### 14.1 Manual Export Does Not Prove Send

A copyable or downloadable draft is still a draft.

Opening an external mail client is not send confirmation.

### 14.2 Future Send

Production send may enter a later phase only through:

- Communication Service ownership;
- explicit scope approval;
- separate readiness review;
- integration governance;
- safe retry and reconciliation;
- Book 03 change control.

---

## 15. External Action Boundary

The current MVP stops before external protected action.

Excluded external actions include:

- official trademark filing;
- office action response submission;
- renewal filing;
- assignment recordal;
- provider instruction;
- provider engagement;
- payment;
- external Evidence disclosure;
- signed acceptance;
- legal or commercial commitment;
- Communication send.

### 15.1 External Read vs External Act

An approved read-only integration may provide reference data or status for preparation.

Reading external information does not authorize acting externally.

### 15.2 External Outcome

The MVP must not manufacture an external outcome from internal readiness.

Examples:

```text
filing package ready
≠ filed

provider recommendation ready
≠ provider appointed

payment data prepared
≠ payment made

Communication approved
≠ Communication sent
```

### 15.3 Production Connector Presence

Even if a connector exists technically, the MVP must not use it for a protected action unless that action is explicitly in scope and separately approved.

---

## 16. Permission and Policy Boundary

Every MVP operation must evaluate applicable Permission and Policy.

This applies to:

- preview;
- object access;
- source retrieval;
- draft preparation;
- Task creation;
- review;
- apply;
- audit;
- AI assistance.

### 16.1 Preview Does Not Bypass Access Control

A preview may reveal sensitive candidate data, client information, provider terms or Evidence.

It must remain permission-filtered.

### 16.2 Fail Closed

Protected apply fails closed when:

- Permission cannot be verified;
- Policy evaluation is unavailable;
- required Human Review is missing;
- version is stale;
- object state is incompatible;
- idempotency is uncertain.

### 16.3 No MVP Administrator Bypass

The MVP must not depend on a hidden universal administrator role to make demonstrations succeed.

Any override is separately governed and outside ordinary MVP flow.

---

## 17. Idempotency, Retry and Safe Failure Boundary

The MVP must demonstrate correct behavior when operations repeat or fail.

It must support the distinctions between:

- first attempt;
- retry;
- idempotent replay;
- continuation;
- reconciliation;
- terminal stop.

### 17.1 Required Proof

At minimum, the MVP should prove that:

- repeated Task creation does not create duplicate active Tasks;
- repeated internal apply returns or reconciles the existing result;
- changed semantic input conflicts with the old idempotency scope;
- uncertain outcomes do not trigger blind repetition;
- partial completion remains visible;
- safe failure states the next governed action.

### 17.2 No External Retry Proof Through Real Harm

The MVP does not need to perform real payment, filing or send to demonstrate retry architecture.

Those cases may be tested through fixtures, simulations or disabled integration boundaries until separately approved.

### 17.3 Failure Is Part of MVP Viability

An MVP that works only on the happy path does not prove the Execution System.

---

## 18. Version and Change Boundary

The MVP must be version-aware from the beginning.

Supported execution must preserve:

- Workflow Contract version;
- subject version;
- draft version;
- review version;
- apply version;
- relevant Policy and Permission context;
- AI assistance version where material.

### 18.1 No Latest-Version Shortcut

The system must not silently apply the latest object or draft when the review covered an earlier version.

### 18.2 Scope Expansion

A workflow may move from preview-only to apply-enabled only through controlled change.

The change must identify:

- new effects;
- owning Services;
- new risks;
- review requirements;
- integration requirements;
- Event behavior;
- migration or in-flight impact;
- acceptance evidence.

### 18.3 Compatibility

Unknown compatibility blocks protected apply.

---

## 19. Event, Trace and Audit Boundary

The MVP must preserve execution trace without becoming an Event Bus project.

### 19.1 Required Trace

For supported apply, an authorized observer should be able to determine:

- operation;
- actor;
- versions;
- Permission and Policy result;
- Human Review;
- Service calls;
- completed effects;
- blocked or uncertain effects;
- Event references;
- safe next action.

### 19.2 Event Ownership

Owning Services or the approved Event boundary emit governed Events.

Workflow correlates references.

### 19.3 No Event Sourcing Requirement

The MVP does not require Event Sourcing.

It requires governed Event and audit semantics.

### 19.4 Replay

Audit replay is read-only and must not recreate effects.

---

## 20. AI and Agent Boundary

AI and agents may assist the MVP by:

- extracting structured information;
- summarizing source Documents;
- comparing versions;
- detecting missing fields;
- preparing options;
- drafting Communications;
- preparing Task plans;
- assembling review packages;
- explaining safe errors;
- preparing reconciliation questions.

They may not:

- approve;
- satisfy Human Review;
- define professional truth;
- select or engage a provider;
- certify a deadline;
- certify Evidence;
- send;
- submit;
- pay;
- mutate protected state;
- complete protected Tasks;
- bypass Permission or Policy;
- emit governed Events independently.

### 20.1 AI Must Be Optional to Core Correctness

The MVP must remain governable when AI is unavailable.

The safe fallback is human-controlled preparation, not removal of the gate.

### 20.2 Agent Tool Access

The default MVP agent tool set should be read, analyze and prepare oriented.

Any mutation-capable tool must still enforce Service-owned gates independently.

### 20.3 No Autonomous Execution Claim

The MVP must not be marketed or documented as autonomous professional execution.

---

## 21. Data, Document, Evidence and Knowledge Boundary

The MVP may organize and reference data.

It must not confuse presence with truth.

### 21.1 Data

Supplied data may be:

- unverified;
- stale;
- contradictory;
- inferred;
- incomplete;
- restricted.

The MVP should preserve source and confidence limitations.

### 21.2 Documents

A Document reference does not prove legal validity, signature validity or official acceptability.

### 21.3 Evidence

Evidence preparation may organize and compare materials.

It may not certify:

- authenticity;
- ownership;
- sufficiency;
- admissibility;
- official acceptance.

### 21.4 Knowledge

Knowledge may support preparation when source and version are identified.

Missing or conflicting Knowledge should result in disclosure, review or block—not fabricated certainty.

---

## 22. Integration Boundary

Integration connects approved Services to external systems.

The Execution MVP does not own external-system semantics.

### 22.1 Current Scope

The current MVP may support:

- fixture-backed or simulated integration behavior;
- approved read-only reference retrieval;
- disabled protected-action connectors;
- validation of connector contracts;
- explicit not-enabled responses.

### 22.2 Production External Effects

Production send, payment, filing and provider commitment require separate readiness and approval.

### 22.3 Connector Result

A connector response is interpreted by the owning Service.

Workflow must not convert a technical response directly into legal, financial or professional status.

### 22.4 Secret and Data Control

Credentials, external payloads and confidential data remain outside Workflow prose and must follow security governance.

---

## 23. Observability Boundary

The MVP must be observable enough to prove its own boundaries.

It should expose:

- preview vs apply;
- Workflow and Service ownership;
- review requirement and decision;
- version;
- gate outcomes;
- attempts and idempotency;
- partial and uncertain outcomes;
- Event references;
- AI or agent assistance;
- disabled or unsupported actions.

### 23.1 No Dashboard Dependency

The MVP does not require a complete operational dashboard.

The semantics must exist before the Product presentation.

### 23.2 Boundary Violations Must Be Testable

The system should make it possible to detect attempts to:

- mutate directly from Workflow;
- send from Communication Review;
- apply a preview-only workflow;
- reuse stale approval;
- emit an Event from an agent;
- bypass Permission or Policy;
- create duplicate Tasks.

### 23.3 Metrics Do Not Define Completion

A high completion rate does not justify widening the MVP boundary.

---

## 24. Security and Privacy Boundary

The MVP is not exempt from security because its scope is small.

It must preserve:

- organization separation;
- Matter separation;
- least privilege;
- restricted Document and Evidence access;
- safe error exposure;
- audit access control;
- external-content distrust;
- agent tool restrictions;
- secret protection;
- retention and deletion Policy.

### 24.1 Test and Fixture Data

Fixtures should avoid unnecessary real personal or confidential data.

### 24.2 Production-Like Demonstration

A demonstration environment must not create hidden production effects.

### 24.3 Export

Exporting a review package, audit result or Document bundle may itself be a protected action.

---

## 25. Product Boundary

Book 04 owns forms, navigation, review screens, dashboards, notifications and user experience. It must consume the workflow depth and preserve preview, review, internal apply and external effect as separate meanings. A Product control cannot enable a capability that Execution has not approved.

## 26. MVP Environment and Rollout Boundary

The MVP should progress through controlled environments.

A conceptual progression is:

```text
contracts and fixtures
→ deterministic validation
→ read-only preview
→ internal apply in controlled environment
→ limited pilot
→ broader internal consumption
→ separately approved external action
```

This is not a deployment architecture.

### 26.1 Fixture and Contract Stage

This stage proves:

- structures;
- controlled values;
- validators;
- boundaries;
- expected errors;
- deterministic examples.

### 26.2 Preview Stage

This stage proves:

- context assembly;
- gap analysis;
- review requirements;
- safe output;
- no side effects.

### 26.3 Controlled Internal Apply

This stage proves selected Service-owned internal mutations.

### 26.4 Pilot

A pilot should be scoped by:

- organization;
- Matter type;
- workflow;
- user group;
- data class;
- environment;
- time.

### 26.5 No Automatic Promotion

Passing one stage does not automatically enable the next.

---

## 27. Scope Change Governance

The MVP boundary must not drift through convenience changes.

Scope expansion includes:

- enabling apply for a preview-only workflow;
- adding external send;
- adding payment;
- adding filing;
- adding provider engagement;
- granting agent mutation;
- introducing a new Core object or Event;
- changing Human Review requirements;
- adding a production connector;
- allowing automatic retry of protected action.

Every expansion requires:

1. explicit proposal;
2. Book 02 dependency review;
3. effect and risk analysis;
4. Service ownership;
5. Permission and Policy review;
6. Human Review model;
7. idempotency and safe failure;
8. version and migration impact;
9. Event and audit behavior;
10. acceptance evidence;
11. Product boundary review;
12. controlled activation.

A successful demonstration is not sufficient scope-change authority.

---

## 28. MVP Proof Obligations

The Execution MVP should prove the architecture through observable behavior.

### 28.1 Contract Consumption

The implementation consumes approved Book 02 contracts without redefining them.

### 28.2 Preview Safety

Preview is side-effect free and permission-filtered.

### 28.3 Apply Separation

Apply exists only for approved Depth A workflows.

### 28.4 Service Ownership

All mutation is performed by owning Services.

### 28.5 Task Separation

Task plans and active Tasks remain distinct.

### 28.6 Human Review

Protected decisions bind to exact versions, scope and intended action.

### 28.7 Communication Lock

Communication Review cannot send.

### 28.8 Preview-Only Lock

Depth B workflows reject apply without side effects.

### 28.9 Idempotency

Repeated internal apply does not duplicate effects.

### 28.10 Safe Failure

Errors, blocks, partial completion and uncertainty remain distinguishable.

### 28.11 Version Control

Stale review or changed content blocks protected apply.

### 28.12 Event Authority

Workflow and agents do not emit governed Events independently.

### 28.13 AI Boundary

AI assists but cannot approve or perform protected action.

### 28.14 Audit

An authorized actor can reconstruct the supported execution path.

### 28.15 Product Independence

The execution semantics can be tested without relying on a particular UI.

Chapter 33 converts these proof obligations into an implementation-readiness assessment.

---

## 29. MVP Non-Goals

The current Execution MVP does not include:

- full trademark lifecycle automation;
- all 26 Core Domains at full business depth;
- production official filing;
- production Communication send;
- payment execution;
- provider marketplace commitment;
- provider instruction dispatch;
- autonomous legal strategy;
- automated deadline certification;
- automated Evidence certification;
- autonomous AI agents;
- unrestricted Workflow Engine;
- Event Bus implementation;
- Event Sourcing;
- database architecture;
- full integration platform;
- Product UI;
- reporting suite;
- organization-wide administrator bypass;
- complete exception and compensation framework;
- production-scale observability tooling;
- final publication or legal-operating procedures.

A non-goal may become a future phase only through explicit governance.

---

## 30. Governance Examples

### 30.1 Intake Apply

A user submits applicant information and a logo.

The MVP may:

1. validate the supported request;
2. identify missing or conflicting data;
3. produce preview;
4. request Human Review where required;
5. apply through Customer, Brand, Matter, Document and Task Services;
6. return created references and Event references.

It may not:

- accept legal engagement;
- authorize payment;
- select a provider;
- file an application.

### 30.2 Application Preparation Apply

A reviewed application workspace is ready for internal preparation apply.

The MVP may:

- create or link internal Trademark and Matter references;
- store reviewed preparation state through owning Services;
- create active preparation Tasks;
- preserve the approved version;
- return safe warnings.

It must state:

```text
Internal preparation applied.
No official filing occurred.
```

### 30.3 Communication Review

An AI-assisted client update is prepared.

The MVP may:

- create a draft;
- route Human Review;
- record approval for the exact package;
- create a follow-up Task.

The MVP must stop before send.

### 30.4 Provider Routing

The workflow compares three providers.

The MVP may return:

- candidate preview;
- comparison factors;
- missing quote terms;
- review requirement;
- provider inquiry outline.

Apply remains disabled.

No provider is selected or contacted.

### 30.5 Renewal Preview

The workflow identifies a possible renewal window and missing Evidence.

The MVP may prepare:

- source references;
- date context;
- uncertainty;
- Task plan;
- Human Review questions.

It may not certify the deadline, pay or file.

### 30.6 Apply Request Against Preview-Only Workflow

A caller requests apply for Assignment Preparation.

The safe result is:

```text
Apply is not enabled for the current workflow depth.
No assignment effect, recordal, Task activation, Communication or Event was created.
Preview remains available.
```

### 30.7 Stale Review

A Communication attachment changes after approval.

The MVP blocks apply, identifies the version mismatch and requests renewed review.

### 30.8 Duplicate Task Request

A repeated Intake apply requests the same review Task.

Task Service returns the existing Task reference under the same idempotency scope.

No duplicate active Task is created.

---

## 31. Boundary Acceptance Rules

The Execution MVP remains inside its approved boundary when:

1. Book 02 remains the source of Core truth;
2. Workflow coordinates but does not own mutation;
3. Depth A is limited to selected internal preparation effects;
4. Depth B remains preview-only and side-effect free;
5. external protected action remains deferred;
6. Communication Review does not send;
7. Task plans do not become active Tasks without Task Service;
8. Human Review binds exact version, scope and intended action;
9. Permission and Policy apply to preview and apply;
10. idempotency prevents duplicate internal effects;
11. uncertainty triggers reconciliation rather than blind retry;
12. stale versions block protected apply;
13. owning Services return Event references;
14. Workflow and agents do not emit governed Events directly;
15. AI remains optional assistance and never professional authority;
16. audit can reconstruct each supported apply;
17. Product surfaces cannot expand execution depth;
18. integration presence does not activate external action;
19. scope changes require explicit review and activation;
20. unsupported Core gaps route back to Book 02.

A violation of any of these rules is not a minor MVP shortcut.

It is a boundary failure.

---

## 32. Implementation Boundary

This chapter defines the MVP boundary, not code, persistence, APIs, Workflow Engine internals, connectors, deployment or Product UI. Chapters 32–34 define workflow depth, readiness and sequencing. Any implementation that needs broader authority must stop and enter change control.

## 33. Chapter Result

The MarkOrbit Execution MVP is intentionally narrow.

It proves that professional work can move from structured input to governed internal preparation and review without transferring authority to Workflow, Product or AI.

The operating rule is:

```text
Use Book 02 contracts.
Default to preview.
Enable apply only for approved internal preparation workflows.
Let owning Services mutate.
Bind Human Review to exact versions and actions.
Keep Communication send, payment, provider commitment and filing outside the current MVP.
Keep broader workflows preview-only.
Trace governed facts.
Fail safely.
Expand only through explicit change control.
```

The MVP is successful when it demonstrates disciplined execution, not when it appears to automate the largest number of actions.

The next chapter defines the precise workflow set and current depth assigned to each workflow: **Chapter 32 — MVP Execution Workflow Set**.
