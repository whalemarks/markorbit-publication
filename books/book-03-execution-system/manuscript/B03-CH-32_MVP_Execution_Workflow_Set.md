# B03-CH-32 — MVP Execution Workflow Set

**Status:** Release Candidate 1

## Chapter Purpose

Chapter 31 defined the boundary of the MarkOrbit Execution MVP.

This chapter defines the concrete workflow set inside that boundary.

The governing principle is:

```text
A workflow is not MVP-ready because it is valuable.
It is MVP-ready only when its execution depth, effects, gates, owners and stop conditions are explicit.
```

The MVP Execution Workflow Set contains the first group of workflows that can prove the Book 03 execution model without creating uncontrolled legal, financial, communicative or external effects.

The workflow set is divided into three depths:

```text
Depth A — Apply-enabled internal preparation
Depth B — Governed preview only
Depth C — Deferred protected execution
```

This chapter defines:

- which workflows are in the MVP;
- which depth each workflow currently occupies;
- which effects are allowed;
- which effects are prohibited;
- which Core dependencies must exist;
- which Human Review gates apply;
- how AI may assist;
- how Product must consume the workflow without expanding it;
- how each workflow may advance to a deeper execution level in a future phase.

This chapter does not define workflow engine implementation, API routes, database schema, Product screens, connector behavior, queue workers or external filing operations.

The core MVP workflow matrix is:

```text
Depth A — apply-enabled internal preparation:
1. Intake Execution
2. Application Preparation
3. Communication Review

Depth B — governed preview only:
4. Provider Routing Preparation
5. Office Action Response Preparation
6. Renewal Preparation
7. Assignment Preparation
8. Evidence Review Preparation

Depth C — deferred protected execution:
external send, filing, payment, provider engagement, official submission,
assignment recordal, renewal submission, autonomous agent execution
```

The purpose of the MVP set is not to automate everything.

It is to prove that execution can be governed.

---

## 1. Dependency Baseline

This chapter depends on the MVP boundary established in:

- [Chapter 31 — Execution MVP Boundary](B03-CH-31_Execution_MVP_Boundary.md)

It also depends on the execution patterns defined in:

- [Chapter 17 — Intake Execution Pattern](B03-CH-17_Intake_Execution_Pattern.md)
- [Chapter 18 — Application Preparation Pattern](B03-CH-18_Application_Preparation_Pattern.md)
- [Chapter 19 — Communication Review Pattern](B03-CH-19_Communication_Review_Pattern.md)
- [Chapter 20 — Provider Routing Preparation Pattern](B03-CH-20_Provider_Routing_Preparation_Pattern.md)
- [Chapter 21 — Office Action Response Preparation Pattern](B03-CH-21_Office_Action_Response_Preparation_Pattern.md)
- [Chapter 22 — Renewal Preparation Pattern](B03-CH-22_Renewal_Preparation_Pattern.md)
- [Chapter 23 — Assignment Preparation Pattern](B03-CH-23_Assignment_Preparation_Pattern.md)
- [Chapter 24 — Evidence Review Preparation Pattern](B03-CH-24_Evidence_Review_Preparation_Pattern.md)

Its governance dependencies include:

- [Chapter 25 — Idempotency and Retry Governance](B03-CH-25_Idempotency_and_Retry_Governance.md)
- [Chapter 26 — Error Handling and Safe Failure](B03-CH-26_Error_Handling_and_Safe_Failure.md)
- [Chapter 27 — Versioning and Change Control](B03-CH-27_Versioning_and_Change_Control.md)
- [Chapter 28 — Human Review Governance](B03-CH-28_Human_Review_Governance.md)
- [Chapter 29 — Agent-Assisted Execution Governance](B03-CH-29_Agent-Assisted_Execution_Governance.md)
- [Chapter 30 — Execution Observability and Audit](B03-CH-30_Execution_Observability_and_Audit.md)

Its primary Book 02 dependencies are:

- Core Domain and Object contracts;
- Workflow Contract primitive;
- Task contracts;
- Communication contracts;
- Event contracts;
- Permission and Policy contracts;
- Human Review contracts;
- versioning, idempotency and error contracts;
- AI governance contracts;
- audit context.

Book 02 remains authoritative.

The workflow set described here may not introduce new Core Domains, Objects, Services, Event types, Task statuses, Permission semantics, Policy semantics or AI authority.

---

## 2. Workflow Set Selection Criteria

A workflow belongs in the MVP set only if it satisfies defined selection criteria.

### 2.1 It Uses Existing Core Contracts

The workflow must consume existing or approved Book 02 contracts.

If the required Core contract does not exist, the workflow may remain:

```text
unsupported
preview-only
fixture-backed
manual-only
deferred
```

It must not invent local Core truth.

### 2.2 It Has a Defined Execution Depth

Every workflow must clearly state whether it is:

```text
Depth A — apply-enabled internal preparation
Depth B — preview only
Depth C — deferred protected execution
```

A workflow may not have ambiguous apply behavior.

### 2.3 It Has a Clear Effect Boundary

The workflow must define:

- what it may read;
- what it may preview;
- what it may prepare;
- what it may request;
- what it may mutate through owning Services;
- what it must not do.

### 2.4 It Has Owning Services

Any mutation must belong to an approved owning Service.

Workflow may coordinate.

Workflow does not own mutation.

### 2.5 It Has Human Review Gates

Where professional judgment is required, the workflow must expose Human Review rather than bypass it.

### 2.6 It Has Safe Failure

The workflow must be able to stop safely when:

- validation fails;
- Permission is denied;
- Policy is blocked;
- version is stale;
- Human Review is missing;
- idempotency conflicts;
- external outcome is uncertain;
- AI output is incomplete;
- required Core dependency is missing.

### 2.7 It Is Observable

The workflow must produce enough trace to explain:

- what was requested;
- what version was used;
- what was previewed;
- what was applied;
- what was blocked;
- what remains uncertain;
- which Service owns each effect.

### 2.8 It Does Not Depend on Product UI

The workflow must be testable as execution semantics independent of a specific Product screen.

Book 04 may later present the workflow, but Product does not define execution meaning.

---

## 3. MVP Workflow Depth Matrix

The MVP workflow set is governed by the following matrix.

| Workflow | Current MVP depth | Apply enabled? | External action? | Primary purpose |
|---|---:|---:|---:|---|
| Intake Execution | Depth A | Yes, internal only | No | Convert structured intake into governed internal preparation context |
| Application Preparation | Depth A | Yes, internal only | No | Create or update internal application preparation state |
| Communication Review | Depth A | Yes, internal only | No send | Prepare and review Communication package |
| Provider Routing Preparation | Depth B | No | No | Compare provider candidates and expose review questions |
| Office Action Response Preparation | Depth B | No | No | Prepare strategy and response package preview |
| Renewal Preparation | Depth B | No | No | Analyze renewal readiness, deadline context and missing requirements |
| Assignment Preparation | Depth B | No | No | Prepare assignment package and recordal readiness preview |
| Evidence Review Preparation | Depth B | No | No | Organize and analyze Evidence for Human Review |

Depth C is not a workflow list in this chapter. It is the set of protected actions deferred from the MVP.

Examples include:

- Communication send;
- official filing;
- official submission;
- payment;
- provider engagement;
- provider instruction dispatch;
- assignment recordal;
- renewal filing;
- office action response filing;
- autonomous agent execution.

---

## 4. Common Workflow Contract Requirements

Every MVP workflow must define a common execution contract.

A workflow contract should identify:

- workflow type;
- workflow depth;
- subject and target;
- allowed inputs;
- required Core references;
- version requirements;
- Permission and Policy gates;
- Human Review requirements;
- allowed preview output;
- allowed apply effects, if any;
- prohibited effects;
- idempotency scope;
- safe failure behavior;
- audit and Event expectations;
- AI assistance limits;
- Product boundary.

This does not require a complete workflow engine.

It requires that each supported workflow has enough governance definition to be executed consistently.

### 4.1 Preview Contract

Every workflow must support a preview contract before apply.

Preview should be:

- side-effect free;
- version-aware;
- Permission-filtered;
- Policy-aware;
- source-traceable;
- safe for missing data;
- explicit about unresolved issues;
- explicit about disabled apply.

### 4.2 Apply Contract

Only Depth A workflows may have apply in the current MVP.

Apply must:

- revalidate current state;
- revalidate versions;
- revalidate Permission and Policy;
- verify Human Review where required;
- use idempotency;
- call owning Services;
- return exact created or updated references;
- preserve partial completion;
- expose safe failure;
- return Event references only from owning Services.

### 4.3 Stop Contract

Every workflow must define when it stops.

A stop may result from:

- unsupported workflow depth;
- missing Core dependency;
- missing source;
- invalid input;
- stale version;
- missing review;
- Permission denial;
- Policy block;
- idempotency conflict;
- unsafe external action request;
- AI output uncertainty;
- external result uncertainty.

The stop result must be truthful and actionable.

---

## 5. Workflow 1 — Intake Execution

### 5.1 Purpose

Intake Execution converts incoming client or partner information into a governed internal preparation context.

It exists to prevent raw intake from becoming uncontrolled business action.

The central distinction is:

```text
information received
≠ information verified
≠ engagement accepted
≠ Matter ready for professional action
```

### 5.2 Current MVP Depth

```text
Depth A — Apply-enabled internal preparation
```

Apply is enabled only for approved internal effects.

### 5.3 Allowed Inputs

The workflow may consume:

- customer or partner submitted information;
- brand or mark information;
- applicant or owner data;
- contact details;
- jurisdiction interest;
- service interest;
- uploaded logo or Documents;
- preliminary goods/services description;
- source channel;
- intake notes;
- AI-extracted structured fields, if allowed.

### 5.4 Allowed Preview

Preview may return:

- normalized intake summary;
- missing required information;
- duplicate-candidate warnings;
- unsupported jurisdiction or service warnings;
- Document presence and type validation;
- preliminary Matter or Order readiness;
- Human Review requirements;
- suggested next preparation steps;
- Task plan preview;
- safe errors.

Preview must not create authoritative records.

### 5.5 Allowed Apply Effects

Apply may coordinate through owning Services:

- Customer creation or linkage;
- Brand creation or linkage;
- preliminary Matter creation;
- draft or scoped Order creation, where approved;
- Document linkage;
- active Task creation for missing information or review;
- Communication draft creation for follow-up;
- governed Event references returned by owning Services.

### 5.6 Prohibited Effects

Intake Execution may not:

- accept legal engagement;
- approve the client;
- approve the service scope as professional advice;
- approve fees;
- request payment;
- select a provider;
- file or submit;
- send external Communication;
- certify information accuracy;
- create provider commitment.

### 5.7 Required Gates

Intake apply requires:

- valid source and actor context;
- supported service scope;
- Permission to create or link internal records;
- Policy permission for data processing;
- versioned intake package;
- idempotency for record and Task creation;
- Human Review where intake quality, conflict or professional acceptance requires it.

### 5.8 AI Assistance

AI may:

- extract fields;
- classify missing information;
- summarize uploaded Documents;
- detect duplicate candidates;
- prepare follow-up questions;
- draft internal intake notes.

AI may not:

- accept the client;
- determine legal eligibility;
- approve service scope;
- decide conflict of interest as final truth;
- create professional conclusions;
- bypass Human Review.

### 5.9 MVP Acceptance

Intake Execution is MVP-ready when:

- duplicate intake does not create duplicate active records or Tasks;
- missing data results in governed Task or safe stop;
- created references are returned by owning Services;
- no external effect occurs;
- audit can reconstruct the intake-to-internal-preparation path.

---

## 6. Workflow 2 — Application Preparation

### 6.1 Purpose

Application Preparation creates a governed internal preparation state for a trademark application or similar filing package.

It does not file.

It does not certify legal sufficiency.

It does not make final professional strategy decisions without Human Review.

The central distinction is:

```text
application package prepared internally
≠ application approved for filing
≠ official filing submitted
```

### 6.2 Current MVP Depth

```text
Depth A — Apply-enabled internal preparation
```

Apply is enabled only for internal preparation effects.

### 6.3 Allowed Inputs

The workflow may consume:

- Brand or mark reference;
- Trademark reference;
- applicant or owner reference;
- jurisdiction reference;
- goods/services proposal;
- Classification references;
- Document references;
- Evidence references;
- priority or claim information;
- intake context;
- client instructions;
- AI-assisted extraction;
- Knowledge references.

### 6.4 Allowed Preview

Preview may return:

- application preparation summary;
- missing required fields;
- jurisdiction requirement checklist;
- Classification readiness;
- goods/services warnings;
- Document checklist;
- Evidence gaps;
- draft Task plan;
- Human Review requirements;
- filing-readiness limitations;
- safe error output.

### 6.5 Allowed Apply Effects

Apply may coordinate through owning Services:

- Trademark record creation or update;
- Brand linkage;
- applicant or owner reference linkage;
- jurisdiction and Classification reference linkage;
- Document and Evidence linkage;
- internal application-preparation state;
- active Tasks for Classification, Document or review work;
- Communication draft for client follow-up;
- Event references from owning Services.

### 6.6 Prohibited Effects

Application Preparation may not:

- file;
- submit to an authority;
- pay official or provider fee;
- certify registrability;
- certify final classification;
- certify deadline;
- engage a provider;
- send instructions externally;
- create official status;
- mark application as filed.

### 6.7 Required Gates

Apply requires:

- current versions of source objects;
- Permission for internal preparation;
- applicable Policy;
- Human Review for professional classification or filing package readiness where required;
- idempotency for object and Task creation;
- safe failure for missing or conflicting data;
- audit context.

### 6.8 AI Assistance

AI may:

- suggest Classification candidates;
- summarize jurisdiction requirements;
- extract applicant data;
- prepare checklist;
- compare goods/services wording;
- identify missing Documents;
- draft client questions.

AI may not:

- finalize professional classification;
- certify legal sufficiency;
- approve filing;
- submit;
- define professional truth.

### 6.9 MVP Acceptance

Application Preparation is MVP-ready when:

- internal preparation apply creates only approved internal state;
- stale package or changed goods/services blocks protected apply;
- Human Review is visible and version-bound;
- no official filing effect is created;
- audit distinguishes preparation from filing.

---

## 7. Workflow 3 — Communication Review

### 7.1 Purpose

Communication Review governs preparation, review and approval of a Communication package.

It is intentionally separated from send.

The central distinction is:

```text
draft created
≠ reviewed
≠ approved for send
≠ sent
≠ delivered
≠ received
```

### 7.2 Current MVP Depth

```text
Depth A — Apply-enabled internal preparation
```

Apply is enabled for internal draft and review state only.

Production send remains excluded.

### 7.3 Allowed Inputs

The workflow may consume:

- Communication purpose;
- recipient candidate;
- Matter or Order reference;
- source Documents;
- draft body;
- subject line;
- attachment references;
- channel candidate;
- prior correspondence;
- AI-generated draft;
- reviewer notes.

### 7.4 Allowed Preview

Preview may return:

- draft summary;
- recipient and attachment warnings;
- missing source references;
- AI assistance disclosure;
- version comparison;
- review requirement;
- send-scope warning;
- safe error output.

### 7.5 Allowed Apply Effects

Apply may coordinate through owning Services:

- Communication draft creation;
- draft version creation;
- review request;
- review decision recording;
- reviewer notes where permitted;
- follow-up Task creation;
- approved-for-future-send state where explicitly allowed by Communication Service;
- Event references from owning Services.

### 7.6 Prohibited Effects

Communication Review may not:

- send;
- resend;
- mark sent;
- infer delivery;
- infer receipt;
- expand recipient scope;
- attach unreviewed Documents to an approved package;
- accept legal or commercial terms;
- commit to provider or client externally.

### 7.7 Required Gates

Apply requires:

- exact Communication package version;
- Permission for draft and review;
- Policy for recipient, attachment and confidentiality;
- Human Review where required;
- AI assistance disclosure where material;
- idempotency for draft and review operations;
- safe failure for stale version or changed attachment.

### 7.8 AI Assistance

AI may:

- draft;
- translate;
- summarize source;
- compare draft versions;
- identify missing attachments;
- prepare review questions.

AI may not:

- approve;
- send;
- represent that Human Review occurred;
- decide recipient authorization;
- certify professional correctness.

### 7.9 MVP Acceptance

Communication Review is MVP-ready when:

- draft, review and approval state are distinguishable;
- changed content or attachment invalidates or suspends the prior approval;
- send is not possible through this workflow;
- no external Communication is transmitted;
- audit identifies the exact approved package.

---

## 8. Workflow 4 — Provider Routing Preparation

### 8.1 Purpose

Provider Routing Preparation compares possible providers and prepares routing questions.

It does not select, engage or instruct a provider.

The central distinction is:

```text
provider candidate preview
≠ provider selected
≠ provider engaged
≠ provider instructed
≠ provider paid
```

### 8.2 Current MVP Depth

```text
Depth B — Governed preview only
```

Apply is disabled.

### 8.3 Allowed Inputs

The workflow may consume:

- jurisdiction;
- service type;
- Matter scope;
- provider references;
- provider capability data;
- quote data;
- historical performance data where governed;
- confidentiality constraints;
- client preferences;
- Knowledge references.

### 8.4 Allowed Preview

Preview may return:

- candidate provider list;
- comparison factors;
- missing quote terms;
- capability gaps;
- conflict or availability warnings;
- fee comparison;
- review questions;
- recommendation rationale as advisory;
- safe error output.

### 8.5 Prohibited Effects

Provider Routing Preparation may not:

- select provider as final decision;
- create provider engagement;
- send instruction;
- disclose client Documents;
- accept terms;
- pay provider;
- create binding commercial commitment;
- update provider status as chosen;
- emit provider-selection Event.

### 8.6 Required Gates

Preview requires:

- Permission to view provider data;
- Policy for confidentiality and data sharing;
- versioned provider and quote data;
- disclosure of missing or stale provider data;
- AI assistance boundaries;
- safe handling of unsupported jurisdictions.

### 8.7 AI Assistance

AI may:

- compare providers;
- identify missing quote terms;
- summarize strengths and weaknesses;
- flag conflicts;
- prepare reviewer questions.

AI may not:

- select provider;
- engage provider;
- negotiate;
- instruct;
- define provider suitability as final truth.

### 8.8 Future Advancement Conditions

To move to apply-enabled depth, this workflow requires:

- provider selection contract;
- engagement authorization;
- Communication or instruction send governance;
- fee approval;
- confidentiality and data-transfer Policy;
- Human Review model;
- idempotency for instruction and engagement;
- Event and audit contracts.

Until those exist, apply remains disabled.

---

## 9. Workflow 5 — Office Action Response Preparation

### 9.1 Purpose

Office Action Response Preparation organizes official action content, issues, deadlines, sources, strategy options and response-package readiness.

It does not approve strategy or submit a response.

The central distinction is:

```text
response package preview
≠ professional strategy approved
≠ response authorized
≠ official response submitted
```

### 9.2 Current MVP Depth

```text
Depth B — Governed preview only
```

Apply is disabled.

### 9.3 Allowed Inputs

The workflow may consume:

- office action Document;
- official status;
- deadline source;
- cited marks or references;
- client facts;
- Evidence;
- prior arguments;
- Knowledge references;
- jurisdiction requirements;
- draft response content;
- AI extraction.

### 9.4 Allowed Preview

Preview may return:

- extracted issue list;
- deadline context with confidence and source;
- missing Evidence;
- strategy options;
- draft argument outline;
- risk flags;
- required review questions;
- source conflict warnings;
- response package checklist.

### 9.5 Prohibited Effects

The workflow may not:

- certify deadline;
- select final strategy;
- approve response;
- submit response;
- send to authority or provider;
- create legal conclusion as final truth;
- mark office action resolved;
- create official status;
- create external Communication.

### 9.6 Required Gates

Preview requires:

- source Document version;
- official or provider source reference where available;
- Permission to access Matter and Documents;
- Policy for AI processing and confidentiality;
- disclosure of AI extraction limitations;
- Human Review requirement for professional strategy.

### 9.7 AI Assistance

AI may:

- extract refusal grounds;
- summarize official text;
- compare cited references;
- prepare argument candidates;
- identify missing Evidence;
- generate review questions.

AI may not:

- decide legal strategy;
- certify deadline;
- approve response;
- submit;
- define professional truth.

### 9.8 Future Advancement Conditions

Apply requires future contracts for:

- response strategy approval;
- response package versioning;
- official or provider submission;
- deadline certification or review;
- external send;
- filing connector behavior;
- idempotency and reconciliation;
- Event and audit.

Until then, the workflow remains preview-only.

---

## 10. Workflow 6 — Renewal Preparation

### 10.1 Purpose

Renewal Preparation analyzes renewal readiness, timing, required Documents, fees, Evidence and missing decisions.

It does not renew.

It does not pay.

It does not file.

The central distinction is:

```text
renewal readiness preview
≠ renewal authorized
≠ renewal paid
≠ renewal filed
≠ renewal accepted
```

### 10.2 Current MVP Depth

```text
Depth B — Governed preview only
```

Apply is disabled.

### 10.3 Allowed Inputs

The workflow may consume:

- Trademark record;
- registration date;
- renewal period source;
- jurisdiction;
- owner information;
- Evidence;
- fee information;
- Power of Attorney or authorization Document;
- provider quote;
- client instruction;
- Knowledge references.

### 10.4 Allowed Preview

Preview may return:

- renewal window analysis;
- source and confidence;
- missing Documents;
- fee estimate with limitations;
- Evidence requirement warnings;
- owner mismatch warnings;
- Task plan preview;
- Human Review questions;
- safe error output.

### 10.5 Prohibited Effects

Renewal Preparation may not:

- certify deadline as final professional truth;
- authorize renewal;
- request or execute payment;
- file renewal;
- instruct provider;
- send official Communication;
- mark renewed;
- create official status.

### 10.6 Required Gates

Preview requires:

- versioned Trademark and jurisdiction data;
- source trace for date and fee;
- Permission and Policy for viewing records;
- disclosure of missing or conflicting Knowledge;
- Human Review for final renewal decision.

### 10.7 AI Assistance

AI may:

- identify likely renewal window;
- summarize requirements;
- compare Documents;
- prepare client questions;
- organize Evidence.

AI may not:

- certify deadline;
- approve renewal;
- pay;
- file;
- communicate externally.

### 10.8 Future Advancement Conditions

Apply requires future contracts for:

- renewal authorization;
- fee approval;
- payment;
- filing or provider instruction;
- deadline certification or review;
- external connector;
- idempotency and reconciliation;
- Event trace.

Until then, apply remains disabled.

---

## 11. Workflow 7 — Assignment Preparation

### 11.1 Purpose

Assignment Preparation organizes assignment parties, Documents, signatures, jurisdiction requirements and recordal readiness.

It does not record assignment.

It does not establish legal transfer by itself.

The central distinction is:

```text
assignment package prepared
≠ assignment legally effective
≠ assignment recordal filed
≠ official record updated
```

### 11.2 Current MVP Depth

```text
Depth B — Governed preview only
```

Apply is disabled.

### 11.3 Allowed Inputs

The workflow may consume:

- assignor and assignee references;
- Trademark references;
- assignment agreement;
- signature Documents;
- corporate information;
- jurisdiction requirements;
- Power of Attorney;
- notarization or legalization requirements;
- fee information;
- client instruction;
- Evidence of authority.

### 11.4 Allowed Preview

Preview may return:

- party and mark summary;
- Document checklist;
- missing signature or authority issues;
- jurisdiction-specific requirements;
- notarization or legalization questions;
- recordal readiness warnings;
- Task plan preview;
- Human Review questions.

### 11.5 Prohibited Effects

Assignment Preparation may not:

- change ownership record as legal truth;
- file assignment recordal;
- instruct provider;
- send official documents externally;
- certify signature validity;
- certify transfer effectiveness;
- mark official record updated;
- create payment or fee obligation.

### 11.6 Required Gates

Preview requires:

- versioned Documents;
- party references;
- Permission and Policy for sensitive corporate and rights data;
- disclosure of missing authority Evidence;
- Human Review requirement.

### 11.7 AI Assistance

AI may:

- extract parties;
- compare listed marks;
- identify missing signatures;
- summarize jurisdiction requirements;
- prepare review questions.

AI may not:

- certify legal effect;
- approve transfer;
- alter ownership;
- submit recordal;
- define professional truth.

### 11.8 Future Advancement Conditions

Apply requires future contracts for:

- ownership-change authority;
- assignment package approval;
- official recordal;
- provider instruction;
- payment;
- Document authenticity review;
- external submission;
- Event and audit.

Until then, apply remains disabled.

---

## 12. Workflow 8 — Evidence Review Preparation

### 12.1 Purpose

Evidence Review Preparation organizes Evidence for human assessment.

It supports review.

It does not certify authenticity, admissibility or sufficiency.

The central distinction is:

```text
Evidence organized
≠ Evidence authenticated
≠ Evidence sufficient
≠ Evidence approved for filing
```

### 12.2 Current MVP Depth

```text
Depth B — Governed preview only
```

Apply is disabled.

### 12.3 Allowed Inputs

The workflow may consume:

- Evidence Documents;
- screenshots;
- invoices;
- product pages;
- advertisements;
- platform records;
- use dates;
- jurisdiction and class context;
- mark reference;
- owner reference;
- source metadata;
- client statements.

### 12.4 Allowed Preview

Preview may return:

- Evidence inventory;
- date and source extraction;
- mark-use mapping;
- jurisdiction mapping;
- goods/services mapping;
- missing Evidence warnings;
- contradiction flags;
- source-quality notes;
- review questions;
- Task plan preview.

### 12.5 Prohibited Effects

Evidence Review Preparation may not:

- certify authenticity;
- certify admissibility;
- certify sufficiency;
- approve filing use;
- submit Evidence;
- create official record;
- alter rights status;
- define final professional conclusion.

### 12.6 Required Gates

Preview requires:

- Document version;
- source trace;
- Permission and Policy for Evidence access;
- confidentiality controls;
- AI assistance disclosure;
- Human Review for sufficiency or filing use.

### 12.7 AI Assistance

AI may:

- extract dates;
- group Evidence;
- detect mark visibility;
- map Evidence to goods/services;
- identify gaps;
- prepare review package.

AI may not:

- certify Evidence;
- decide admissibility;
- approve use;
- submit.

### 12.8 Future Advancement Conditions

Apply requires future contracts for:

- Evidence sufficiency review;
- Evidence bundle approval;
- filing package integration;
- source authenticity policy;
- external submission;
- Event and audit.

Until then, apply remains disabled.

---

## 13. Cross-Workflow Rules

All MVP workflows share the following rules.

### 13.1 Preview Before Apply

Every apply-enabled workflow must support preview before apply.

Apply without preview may be allowed only if an explicit future contract defines the equivalent validation and review path.

### 13.2 Current Gates Before Apply

Before apply, Execution must revalidate:

- version;
- Permission;
- Policy;
- Human Review;
- idempotency;
- object state;
- supported workflow depth.

### 13.3 Workflow Depth Cannot Be Overridden by Product

A Product may not enable apply for a preview-only workflow.

### 13.4 Unsupported Means Safe Stop

Unsupported depth or action returns a safe stop, not a partial implementation.

### 13.5 AI Cannot Upgrade Depth

An AI recommendation cannot convert Depth B to Depth A.

### 13.6 External Integration Cannot Upgrade Depth

The existence of a connector cannot enable external action unless the workflow depth and governance allow it.

### 13.7 Service Ownership

Any mutation must be delegated to the owning Service.

### 13.8 Event Ownership

Events must come from owning Services or approved Event boundaries.

### 13.9 Audit

Every supported workflow must preserve enough audit context to reconstruct the supported execution path.

---

## 14. Workflow State Expectations

The MVP should avoid pretending to define a full Workflow Engine.

However, each workflow should still expose a minimum coordination state.

A conceptual state set may include:

- initialized;
- preview prepared;
- blocked;
- review required;
- review requested;
- approved for internal apply;
- apply requested;
- partially applied;
- applied internally;
- preview only;
- unsupported apply requested;
- reconciliation required;
- failed safely;
- superseded or cancelled.

These are explanatory labels unless formalized by Book 02.

### 14.1 Preview-Only State

Preview-only workflows should clearly report:

```text
preview prepared
apply disabled for current workflow depth
```

### 14.2 Applied Internally

Depth A workflows should clearly report:

```text
internal preparation applied
no external protected action occurred
```

### 14.3 Blocked

Blocked states should identify the governing reason where the actor is authorized to see it.

### 14.4 Superseded

If a newer version replaces the reviewed package, the older package becomes stale for apply.

---

## 15. Human Review Gate Matrix

The MVP workflow set should use Human Review proportionately.

| Workflow | Review requirement |
|---|---|
| Intake Execution | Required where acceptance, conflict, data quality or professional scope is uncertain |
| Application Preparation | Required for professional classification, package readiness and filing-related conclusions |
| Communication Review | Required before approval of reviewed Communication package |
| Provider Routing Preparation | Required before selection or engagement in future phase; preview discloses review need |
| Office Action Response Preparation | Required for legal strategy and response package approval |
| Renewal Preparation | Required for deadline, eligibility and authorization decisions |
| Assignment Preparation | Required for legal effect, party authority and recordal readiness |
| Evidence Review Preparation | Required for sufficiency, authenticity, admissibility or filing use |

In the MVP:

- Depth A workflows may create or request review state internally;
- Depth B workflows may identify review requirements but cannot apply protected outcomes;
- no workflow may treat AI output as review.

---

## 16. AI Assistance Matrix

AI assistance is allowed only as preparation.

| Workflow | Allowed AI assistance | Prohibited AI authority |
|---|---|---|
| Intake | extraction, normalization, missing-field detection | client acceptance, conflict decision |
| Application Preparation | classification suggestions, checklist, extraction | final classification, filing approval |
| Communication Review | draft, translate, compare, summarize | approve, send, recipient authorization |
| Provider Routing | compare, summarize, flag gaps | select, engage, instruct |
| OA Response | extract issues, prepare outline | legal strategy approval, submission |
| Renewal | summarize requirements, identify likely window | deadline certification, payment, filing |
| Assignment | extract parties, checklist | certify legal transfer, recordal |
| Evidence Review | group, extract, map, flag gaps | certify authenticity or sufficiency |

The matrix is intentionally conservative.

Future expansion requires AI Governance review, not Product preference.

---

## 17. Event and Audit Matrix

Every workflow must distinguish between:

- preview trace;
- apply trace;
- Service Events;
- review Events;
- external references;
- audit context.

| Workflow | MVP Event expectation |
|---|---|
| Intake Execution | Events only from Services creating or linking internal records and Tasks |
| Application Preparation | Events only from Services updating preparation state, Documents, Tasks or review |
| Communication Review | Events only from Communication, Task or Review Services; no send Event |
| Provider Routing Preparation | No provider selection Event; preview trace only |
| OA Response Preparation | No submission Event; preview trace only |
| Renewal Preparation | No renewal filing or payment Event; preview trace only |
| Assignment Preparation | No ownership-change or recordal Event; preview trace only |
| Evidence Review Preparation | No Evidence sufficiency Event unless future Service contract supports it; preview trace only |

Workflow may correlate references.

Workflow does not emit governed Domain Events directly.

---

## 18. Idempotency Matrix

The MVP should define idempotency at the supported effect boundaries.

### 18.1 Depth A

Idempotency is required for:

- internal record creation;
- Document linkage;
- Task creation;
- Communication draft creation;
- review request creation;
- internal apply result.

### 18.2 Depth B

Preview requests should be reproducible and version-aware.

A repeated preview may regenerate analysis if source versions changed, but it must disclose the version basis.

### 18.3 Prohibited Idempotency Misuse

An idempotency key for preview cannot be reused to apply.

An idempotency key for draft creation cannot be reused for send.

An idempotency key for provider comparison cannot be reused for provider engagement.

---

## 19. Safe Failure Matrix

Each workflow must expose safe failure states.

Examples:

| Workflow | Typical safe failure |
|---|---|
| Intake | missing applicant data; duplicate candidate; unsupported service |
| Application Preparation | stale goods/services; missing jurisdiction requirement; classification conflict |
| Communication Review | draft changed after review; recipient restricted; attachment missing |
| Provider Routing | provider data stale; quote incomplete; confidentiality Policy block |
| OA Response | deadline source uncertain; office action extraction incomplete |
| Renewal | renewal window source missing; owner mismatch; fee source stale |
| Assignment | missing authority evidence; signature mismatch; party conflict |
| Evidence Review | source unsupported; date missing; mark not visible; confidentiality restriction |

Safe failure must say what did not happen.

For example:

```text
No Communication was sent.
No provider was selected.
No filing occurred.
No official status was changed.
```

---

## 20. Versioning Matrix

Every workflow must preserve version context.

| Workflow | Critical version surfaces |
|---|---|
| Intake | intake package, uploaded Documents, extracted fields |
| Application Preparation | Trademark, Classification, goods/services, Documents, package |
| Communication Review | body, subject, recipients, attachments, source Documents |
| Provider Routing | provider profile, quote, terms, service scope |
| OA Response | office action, deadline source, Evidence, response draft |
| Renewal | registration data, renewal rule, fee source, owner data |
| Assignment | assignment agreement, signatures, party data, mark list |
| Evidence Review | Evidence files, source metadata, extracted dates, mark mapping |

A changed critical version may require new preview, new review or safe stop.

---

## 21. Product Consumption Matrix

Book 04 may present each workflow differently, but Product must consume the depth accurately.

| Workflow | Product must show |
|---|---|
| Intake | internal preparation state, missing information, no engagement acceptance |
| Application Preparation | preparation readiness, no filing |
| Communication Review | draft/review/approval distinction, no send |
| Provider Routing | candidate comparison, no selection |
| OA Response | strategy preview, no submission |
| Renewal | readiness preview, no renewal filed |
| Assignment | package preview, no legal transfer or recordal |
| Evidence Review | organized Evidence, no sufficiency certification |

Product language must avoid false completion.

Unsafe labels include:

- filed;
- sent;
- renewed;
- assigned;
- provider selected;
- legally approved;
- evidence accepted;
- deadline certified;

unless the corresponding future governed action actually exists and completed.

---

## 22. Workflow Advancement Governance

A workflow may advance to a deeper execution level only through change control.

### 22.1 From Depth B to Depth A

A Depth B workflow may become internal-apply-enabled only if:

- allowed internal effects are defined;
- owning Services exist;
- idempotency is defined;
- Human Review gates are defined;
- Permission and Policy are defined;
- Event and audit expectations exist;
- safe failure is tested;
- Product boundary is reviewed.

### 22.2 From Depth A to External Apply

A workflow may perform external protected action only if:

- external-action contract exists;
- Integration boundary exists;
- send, payment, filing or provider instruction semantics exist;
- reconciliation exists;
- retry governance exists;
- Human Review and authorization are exact;
- external Event and audit references exist;
- operational monitoring exists;
- incident and rollback boundaries are defined.

### 22.3 Agent Advancement

Agent capability may advance only if:

- AI Governance permits it;
- tool governance enforces it;
- protected-action boundary remains explicit;
- evaluation includes refusal behavior;
- Human Review remains effective.

### 22.4 No Implicit Advancement

A workflow does not advance because:

- users request it;
- Product adds a button;
- a connector becomes available;
- AI output improves;
- a demo succeeds;
- a developer adds a Service call.

---

## 23. MVP Acceptance Tests by Workflow

This chapter is not a test specification, but the workflow set implies acceptance obligations.

### 23.1 Intake Execution

Must prove:

- preview returns missing information;
- apply creates or links only internal records;
- duplicate request does not duplicate active Task;
- unsupported service stops safely;
- no external action occurs.

### 23.2 Application Preparation

Must prove:

- preview detects missing fields;
- apply creates internal preparation state only;
- stale package blocks apply;
- Human Review state is version-bound;
- no filing occurs.

### 23.3 Communication Review

Must prove:

- draft, review and approval states are distinct;
- changed attachment blocks prior approval;
- send is unavailable;
- review decision is attributable;
- no send Event occurs.

### 23.4 Provider Routing Preparation

Must prove:

- preview compares candidates;
- missing quote terms are disclosed;
- apply is rejected as disabled;
- no provider selection Event occurs.

### 23.5 Office Action Response Preparation

Must prove:

- official action extraction can be incomplete;
- deadline uncertainty is disclosed;
- apply is disabled;
- no response submission occurs.

### 23.6 Renewal Preparation

Must prove:

- source and date confidence are disclosed;
- apply is disabled;
- no payment or renewal filing occurs.

### 23.7 Assignment Preparation

Must prove:

- party and Document gaps are surfaced;
- apply is disabled;
- no ownership record is changed.

### 23.8 Evidence Review Preparation

Must prove:

- Evidence can be organized without certification;
- source gaps are disclosed;
- apply is disabled;
- no sufficiency decision is recorded as final.

Chapter 33 develops implementation readiness more fully.

---

## 24. MVP Workflow Non-Goals

The workflow set does not include:

- complete trademark lifecycle automation;
- prosecution management end to end;
- official submission;
- production send;
- payment;
- provider marketplace operations;
- evidence certification;
- autonomous deadline management;
- automated legal strategy;
- full Task workload management;
- complete status synchronization;
- external document signing;
- official recordal;
- automatic renewal;
- automatic assignment;
- autonomous AI execution.

These may become future capabilities only after explicit boundary expansion.

---

## 25. Governance Examples

### 25.1 Workflow Depth Violation

A Product calls apply on Provider Routing Preparation.

Correct result:

```text
Apply disabled for current workflow depth.
No provider was selected.
No instruction was sent.
No external Communication was created.
Preview remains available.
```

### 25.2 Internal Apply Success

Application Preparation apply creates internal Trademark preparation state and a Classification review Task.

Correct result:

```text
Internal preparation applied.
Trademark preparation reference created.
Classification review Task created.
No filing occurred.
```

### 25.3 Communication Approval Without Send

A reviewer approves a Communication package.

Correct result:

```text
Communication package approved for the defined future send purpose.
No send was attempted.
Approved package version is recorded.
```

### 25.4 Stale Evidence Preview

Evidence Review preview was generated from Evidence version `v2`. The user uploads `v3`.

Correct result:

```text
Prior Evidence preview is stale.
Regenerate preview before review.
No sufficiency decision exists.
```

### 25.5 AI Provider Recommendation

AI ranks Provider A first.

Correct result:

```text
Provider recommendation prepared for review.
No provider was selected or instructed.
Recommendation is advisory and source-limited.
```

### 25.6 Renewal Deadline Uncertainty

Renewal Preparation cannot verify an official deadline source.

Correct result:

```text
Renewal window cannot be certified.
Preview identifies source uncertainty.
Human Review required.
No payment or filing occurred.
```

---

## 26. Governance Rules

The MVP Execution Workflow Set is correct when:

1. each workflow has an explicit depth;
2. Depth A apply creates only approved internal effects;
3. Depth B remains preview-only and side-effect free;
4. Depth C protected actions remain deferred;
5. every workflow consumes Book 02 contracts rather than inventing Core truth;
6. every mutation goes through the owning Service;
7. every Task creation goes through Task Service;
8. Communication Review does not send;
9. Provider Routing does not select or engage providers;
10. OA Response does not approve strategy or submit;
11. Renewal does not pay or file;
12. Assignment does not change ownership or recordal;
13. Evidence Review does not certify sufficiency;
14. Human Review is explicit and version-bound where required;
15. AI remains advisory and cannot upgrade workflow depth;
16. Product cannot enable apply beyond the workflow depth;
17. idempotency prevents duplicate internal effects;
18. safe failure identifies what did not happen;
19. Event references come from owning Services;
20. audit reconstructs supported execution paths;
21. scope advancement requires explicit change control;
22. unsupported actions stop safely.

---

## 27. Product Boundary

Book 04 may present the eight workflows differently, but it must preserve each workflow's approved depth and the explicit no-effect statements. Interface design cannot turn a Depth B preview into apply.

## 28. Implementation Boundary

This chapter defines the workflow set and its semantics, not engine code, Services, APIs, storage, queues, connectors, Product UI or deployment. Implementation follows Chapters 31, 33 and 34.

## 29. Chapter Result

The MVP Execution Workflow Set contains eight workflows.

Three are apply-enabled for internal preparation only.

Five are preview-only.

All external protected actions remain deferred.

The operating rule is:

```text
Intake, Application Preparation and Communication Review may apply only internal Service-owned effects.
Provider Routing, OA Response, Renewal, Assignment and Evidence Review remain governed previews.
No send, filing, payment, provider commitment, official recordal or autonomous agent execution occurs.
Every workflow must preserve version, review, Permission, Policy, idempotency, safe failure and audit.
```

The workflow set is not designed to maximize automation.

It is designed to prove the MarkOrbit execution model without crossing professional boundaries prematurely.

The next chapter defines whether the MVP is implementation-ready and what must be true before this workflow set can move from manuscript to code: **Chapter 33 — MVP Implementation Readiness**.
