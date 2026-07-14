# B03-CH-18 — Application Preparation Pattern

**Status:** Release Candidate 1

## Chapter Purpose

The Application Preparation Pattern turns governed intake context into a reviewable trademark application workspace without turning preparation into official filing authority.

Chapter 17 established that Intake may structure a request, expose missing information and coordinate allowed Core records. This chapter begins only when there is enough governed context to evaluate application preparation.

It answers:

```text
Which applicant and Brand context are in scope?
What mark is proposed for protection?
Which jurisdiction questions are resolved and which remain open?
What classification work is supported by the source facts?
Which Documents and Evidence are available?
Which Matter and Order context applies?
What can be prepared through preview?
Which professional conclusions require Human Review?
What may be applied through owning Services?
Why does an applied preparation workflow still stop before official filing?
```

The central distinction is:

```text
Application preparation creates governed readiness context.
Filing authorization permits a specific protected submission.
Official filing performs the external action.
These are three different outcomes.
```

A correct Application Preparation Pattern may finish with gaps, review required, route decision required, commercial confirmation required or a safe pause. It does not have to reach filing readiness.

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 11 — Task Lifecycle Model](B03-CH-11_Task_Lifecycle_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)
- [Chapter 15 — Permission and Policy Gates](B03-CH-15_Permission_and_Policy_Gates.md)
- [Chapter 16 — Human–AI Execution Handoff](B03-CH-16_Human_AI_Execution_Handoff.md)
- [Chapter 17 — Intake Execution Pattern](B03-CH-17_Intake_Execution_Pattern.md)

Its primary Book 02 sources are:

- [Trademark Application Workflow](../../book-02-core-specification/core-specs/workflows/trademark-application-workflow.md)
- [Trademark Application Workflow Contract](../../book-02-core-specification/core-specs/contracts/workflows/trademark-application-workflow-contract.md)
- [Workflow Specifications Index](../../book-02-core-specification/core-specs/workflows/index.md)
- [Workflow Contract Index](../../book-02-core-specification/core-specs/contracts/workflows/index.md)
- [Trademark API Contract](../../book-02-core-specification/core-specs/contracts/api/trademark-api-contract.md)
- [Brand API Contract](../../book-02-core-specification/core-specs/contracts/api/brand-api-contract.md)
- [Jurisdiction API Contract](../../book-02-core-specification/core-specs/contracts/api/jurisdiction-api-contract.md)
- [Classification API Contract](../../book-02-core-specification/core-specs/contracts/api/classification-api-contract.md)
- [Document API Contract](../../book-02-core-specification/core-specs/contracts/api/document-api-contract.md)
- [Evidence API Contract](../../book-02-core-specification/core-specs/contracts/api/evidence-api-contract.md)
- [Matter API Contract](../../book-02-core-specification/core-specs/contracts/api/matter-api-contract.md)
- [Order API Contract](../../book-02-core-specification/core-specs/contracts/api/order-api-contract.md)
- [Task API Contract](../../book-02-core-specification/core-specs/contracts/api/task-api-contract.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Idempotency Contract](../../book-02-core-specification/core-specs/contracts/common/idempotency.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)

Book 02 owns the Workflow, contract, Objects, Services, controlled values, validation rules and test requirements. This chapter describes their operational composition as a pattern. It does not introduce a second application contract or a universal filing-readiness field.

---

## 2. Pattern Position

The pattern normally follows governed Intake.

```text
Intake context
→ Application Preparation Pattern
→ application workspace and active preparation Tasks
→ professional reviews and missing-information loops
→ separate filing authorization boundary
→ external submission outside this pattern
```

It may also connect to:

- Communication Review for customer questions or filing-instruction drafts;
- Provider Routing Preparation where external provider support may be needed;
- Evidence Review Preparation where Evidence requires separate analysis;
- Office Action Response Preparation after an official action exists;
- Task and Human Review lifecycles throughout preparation.

The pattern begins only when the request has a recognizable application-preparation intent.

It must not manufacture that intent merely because a Trademark or Brand record exists.

---

## 3. The Application Preparation Lock

The pattern is governed by this lock:

```text
The Workflow coordinates application preparation.
Owning services own their records and behavior.
Preview has no side effects.
Apply requires Idempotency and current gates.
Classification suggestions are not final professional classification.
Document and Evidence references do not prove official sufficiency.
A prepared workspace is not filing authorization.
The Workflow never submits an official application.
```

This lock prevents several unsafe collapses.

### 3.1 Brand Is Not Trademark Application

A Brand may exist without:

- an intended filing;
- an applicant;
- a selected mark representation;
- target jurisdictions;
- goods and services;
- commercial authorization.

### 3.2 Trademark Record Is Not Official Application

A Core Trademark record represents governed state inside MarkOrbit.

It is not proof that:

- an application was filed;
- an office received it;
- a filing number exists;
- filing fees were paid;
- a provider was instructed.

Only the owning Service and verified external result may support those facts.

### 3.3 Suggested Classification Is Not Final Classification

A suggestion may help organize goods and services.

It is not:

- professional approval;
- guaranteed office acceptance;
- a complete jurisdiction-specific specification;
- filing authorization.

### 3.4 Document Presence Is Not Sufficiency

A logo, identity document, Power of Attorney or priority document may exist while remaining:

- inaccessible under Policy;
- stale;
- mismatched to the applicant;
- incomplete;
- unreviewed;
- unusable for the intended jurisdiction;
- valid only for another purpose.

### 3.5 Commercial Readiness Is Not Professional Readiness

An Order may describe service scope and price context while professional preparation remains incomplete.

Conversely, professional material may be prepared while payment, engagement or provider commitment remains unauthorized.

---

## 4. Application Preparation Context

Execution assembles a bounded context from existing sources.

| Context area | Required distinction |
|---|---|
| Customer | Requesting or represented party versus applicant |
| Applicant | Proposed legal owner versus contact or payer |
| Brand | Commercial identity versus the exact mark to be filed |
| Trademark | Proposed mark representation and governed internal record |
| Jurisdiction | Target reference and unresolved route or local-rule questions |
| Classification | Source description, suggestions, reviewed result and finalization boundary |
| Document | Reference, metadata, content access and intended use |
| Evidence | Source support, intended use and sufficiency boundary |
| Matter | Professional work context |
| Order | Requested commercial scope and authorization state |
| Workflow | Preview/apply operation and contract version |
| Governance | Permission, Policy and Human Review |
| AI | Capability, sources, output mode and limitations |
| Trace | Correlation, prior review and service-owned outcome references |

This is an execution view, not a new Core object.

### 4.1 Customer, Applicant and Contact

These roles must not be collapsed.

The Customer may be:

- the applicant;
- a parent company;
- an agency;
- a representative;
- a payer;
- another authorized party.

The contact may provide instructions without being the applicant.

Execution should preserve exactly which role is declared, inferred, unknown or awaiting verification.

### 4.2 Brand and Mark Representation

The commercial Brand context may include several possible marks:

- word mark;
- device mark;
- combined mark;
- slogan;
- another supported mark type.

The pattern must identify the exact candidate representation being prepared.

A Brand name plus a logo does not automatically answer whether one or multiple applications are intended.

---

## 5. Preparation Areas

Application preparation is composed of six coordinated areas.

```text
1. Applicant and authority preparation
2. Mark representation preparation
3. Jurisdiction context preparation
4. Classification preparation
5. Document and Evidence preparation
6. Matter, Order and Task alignment
```

Each area can be ready, missing, conflicting, restricted, review-required or not applicable.

No single area determines the entire application outcome.

---

## 6. Applicant and Authority Preparation

This area identifies the proposed applicant and the source supporting that identity.

Execution may organize:

- applicant name;
- applicant type;
- country or region;
- address or other contract-supported details;
- Customer relationship;
- Brand owner statement;
- authority or representation Documents;
- conflicting identity sources;
- missing verification items.

It must distinguish:

- declared applicant;
- proposed applicant;
- verified Core reference;
- Document-extracted name;
- AI-normalized text;
- reviewer-confirmed result.

### 6.1 Name Normalization

Formatting may be normalized while the source remains visible.

Execution must not silently:

- translate a legal name into a new legal identity;
- choose between conflicting company names;
- substitute a trading name for the legal applicant;
- assume the Brand owner and applicant are identical;
- treat the payer as owner.

Material uncertainty should create a gap or review Task.

### 6.2 Authority Is Scope-Bound

An authority Document may support a specific jurisdiction, action, representative or time period.

Its existence does not create unrestricted authority.

Professional or official-use readiness may require Human Review under the owning contracts.

---

## 7. Mark Representation Preparation

Execution determines which candidate mark representation is in scope.

Preparation may include:

- mark type;
- mark text;
- logo Document reference;
- language or transliteration notes;
- representation version;
- safe description;
- mismatch or ambiguity warnings;
- link to Brand context.

It must not certify:

- distinctiveness;
- registrability;
- availability;
- ownership;
- office acceptance;
- exact protection scope.

### 7.1 Version Integrity

If a logo or combined mark changes materially, prior review may no longer apply.

The pattern should preserve:

- reviewed version;
- current version;
- source reference;
- change summary;
- need for renewed review.

A Product thumbnail must not become the authoritative representation merely because it is visible.

### 7.2 One Request, Multiple Candidate Applications

A single intake may imply multiple applications because of:

- different mark representations;
- different applicants;
- different jurisdictions;
- different commercial scopes.

The pattern may identify candidate separation.

It must not create multiple official instructions without explicit governed scope.

---

## 8. Jurisdiction Context Preparation

Jurisdiction preparation resolves target references and identifies unanswered jurisdiction-specific questions.

It may organize:

- proposed countries, regions or systems;
- source of the request;
- direct versus international-route questions;
- applicant or priority context;
- jurisdiction-specific Document questions;
- classification constraints requiring professional review;
- route dependencies;
- unresolved strategy questions.

It does not make the final route decision by itself.

### 8.1 Geographic Language Is Often Ambiguous

Statements such as “Europe,” “international,” “worldwide” or “the United States market” may express business intent rather than a legally precise filing route.

Execution should preserve:

- the original request;
- candidate interpretations;
- questions blocking a precise scope;
- who must decide;
- which review is required.

AI may explain alternatives from governed sources. It may not make the final strategy decision.

### 8.2 Jurisdiction Reference Is Not Current Legal Advice

A valid Jurisdiction reference supports governed lookup.

It does not prove that:

- every applicable rule has been retrieved;
- a fee is current;
- a filing basis is correct;
- a deadline is certified;
- a route is commercially or legally optimal.

Freshness and professional review remain necessary where required.

---

## 9. Classification Preparation

Classification is a professional preparation area with strong AI-assistance potential and a hard finalization boundary.

The pattern may coordinate:

- business and product descriptions;
- existing goods and services;
- suggested Nice classes;
- candidate items;
- missing descriptions;
- jurisdiction-specific questions;
- source references;
- review requirements;
- versioned recommendation material.

### 9.1 Source Description Before Class Suggestion

A useful classification process begins with what the applicant actually provides or intends to provide.

Execution should distinguish:

- stated current activity;
- stated planned activity;
- website-derived description;
- prior filing language;
- AI inference;
- suggested class;
- reviewer-approved result.

A polished class list built on an unsupported business description is not reliable preparation.

### 9.2 Suggestion Modes

AI or a governed service may prepare:

- candidate classes;
- candidate items;
- coverage gaps;
- duplicative items;
- questions about ambiguous goods;
- jurisdiction-specific validation questions;
- comparison with prior reviewed classifications.

Every suggestion should preserve its mode and source scope.

### 9.3 Finalization Boundary

Final professional classification may require:

- current target jurisdiction;
- exact goods and services;
- reviewed items;
- applicant instructions;
- policy-allowed sources;
- authorized reviewer;
- version match;
- owning-service acceptance.

AI confidence cannot replace these conditions.

### 9.4 Broader Is Not Automatically Better

The pattern must not optimize blindly for maximum class or item count.

Preparation may need to balance:

- actual business scope;
- intended expansion;
- jurisdiction rules;
- cost context;
- evidence or use strategy;
- professional risk;
- applicant instructions.

These are decision inputs, not an autonomous optimization objective.

---

## 10. Document and Evidence Preparation

Documents and Evidence must remain separate even when they refer to the same source material.

A Document is governed by Document Service.

Evidence is governed by Evidence Service and an intended evidentiary use context.

Preparation may include:

- logo Document;
- applicant identity or company Document;
- authority Document;
- priority Document;
- use-related Evidence;
- source Document references;
- jurisdiction reference;
- metadata and access status;
- missing item list;
- review requirement.

### 10.1 Reference Validation

A valid reference means the reference can be evaluated under contract.

It does not mean:

- raw content may be read;
- the file is authentic;
- the file matches the applicant;
- the office will accept it;
- professional sufficiency is established.

### 10.2 Content Access

Policy may permit:

- metadata only;
- safe preview;
- safe summary;
- restricted professional access;
- no existence disclosure.

The preparation result must not imply full inspection if access was downgraded.

### 10.3 Evidence Use

An Evidence summary may assist review.

It does not conclude:

- legal sufficiency;
- authenticity;
- admissibility;
- official acceptance;
- filing readiness.

Where Evidence is material, the pattern may hand off to Chapter 24’s Evidence Review Preparation Pattern.

---

## 11. Matter and Order Alignment

Matter and Order contexts connect professional work and commercial scope without collapsing them.

The pattern may determine:

- existing or proposed application Matter;
- requested service scope;
- jurisdiction and class-count basis;
- professional Tasks;
- missing commercial confirmation;
- related Order reference;
- mismatch between professional and ordered scope.

### 11.1 Scope Mismatch

Examples include:

- two jurisdictions prepared but one jurisdiction ordered;
- three classes suggested but one class authorized;
- a device mark added after a word-mark scope was quoted;
- priority claim work required but not included;
- a provider-dependent service not yet routed.

The result should expose the mismatch.

It must not silently expand the Order or reduce professional requirements.

### 11.2 Payment Boundary

Order context may show that payment or approval is required.

The Application Preparation Pattern does not execute payment or infer payment authority.

Commercial confirmation and professional review remain distinct gates.

---

## 12. Workflow Preview

Preview is the preferred way to assemble the application workspace.

It may:

- validate request and references;
- identify applicant and mark gaps;
- resolve jurisdiction questions that can be safely resolved;
- prepare classification suggestions;
- identify Document and Evidence gaps;
- assess Matter and Order alignment;
- prepare a Task plan;
- summarize AI assistance;
- expose Policy omissions;
- identify Human Review requirements;
- return warnings and safe errors.

Preview must not:

- create Trademark or Brand state;
- create or update Matter or Order;
- attach Documents or Evidence;
- create active Tasks;
- finalize classification;
- certify filing readiness;
- send filing instructions;
- submit an official application;
- emit Events.

### 12.1 Preview Output Must Be Exact

A useful preview distinguishes:

| Outcome | Meaning |
|---|---|
| Preview ready | The current request can be evaluated without side effects |
| Missing inputs | Named information is required for a stated next decision |
| Review required | An authorized human decision is required |
| Policy restricted | Output or action is blocked, redacted or downgraded |
| Permission denied | The actor cannot perform the protected operation |
| Not applicable | The Workflow does not apply to the current context |
| Apply ready | Contract-specific requirements for apply appear satisfied now |

“Apply ready” still does not mean “filing ready.”

---

## 13. Application Readiness Model

Readiness should be stated against a specific boundary.

A conceptual view may separate:

| Readiness boundary | Question |
|---|---|
| Workspace readiness | Can the application-preparation context be assembled? |
| Record readiness | May owning Services create or link scoped Core records? |
| Task readiness | Is there enough context for Task Service to create active preparation Tasks? |
| Professional review readiness | Is a stable package available for a named reviewer and scope? |
| Commercial readiness | Does the Order context authorize the intended service scope? |
| Filing-instruction readiness | Is a reviewed, version-bound instruction package available for a separate protected action? |
| Official filing result | Has an external submission actually occurred and been verified? |

These are conceptual responsibility labels, not new Core statuses.

### 13.1 Filing Readiness Is Composite

A filing-readiness review may need to consider:

- applicant;
- mark representation;
- jurisdiction;
- classification;
- Documents;
- Evidence where applicable;
- Matter;
- Order;
- Permission;
- Policy;
- professional review;
- provider or submission route;
- current version;
- current external requirements.

The Workflow does not certify the composite result autonomously.

### 13.2 Readiness Can Expire

A previously reviewed package may become stale because:

- the mark changed;
- applicant details changed;
- goods or services changed;
- jurisdiction scope changed;
- a Document expired;
- fees or official requirements changed;
- commercial authorization changed;
- Policy or Permission changed;
- a different provider or route was selected.

Execution revalidates before relying on prior review.

---

## 14. Human Review Gates

Human Review is required where the governing contract or Policy makes a professional conclusion protected.

Possible review scopes include:

- confirm proposed applicant identity for the stated application;
- approve version 4 of the mark representation;
- approve classification version 3 for named jurisdictions;
- review Document package for the intended filing use;
- review Evidence use summary;
- confirm Matter and Order scope alignment;
- confirm a filing-instruction package is ready for a separate submission action.

Each review must identify:

- exact subject references;
- source scope;
- version;
- intended jurisdiction;
- missing or restricted context;
- AI involvement;
- intended downstream action;
- reviewer role;
- decision and conditions.

Human Review does not submit the application.

After review, Execution refreshes state, version, Permission and Policy.

---

## 15. Apply Through Owning Services

Apply coordinates allowed Core preparation effects.

| Preparation result | Owning service |
|---|---|
| Trademark creation or update | Trademark Service |
| Brand link or scoped creation | Brand Service |
| Jurisdiction reference validation | Jurisdiction Service |
| Draft or review-required Classification state | Classification Service |
| Document validation or linkage | Document Service |
| Evidence validation or linkage | Evidence Service |
| Matter creation or update | Matter Service |
| Order context update | Order Service |
| Active preparation Tasks | Task Service |
| Event trace | Owning service or Event Service integration |

The Workflow layer must not mutate these records directly.

### 15.1 Apply Requirements

Apply requires:

- supported Workflow Contract version;
- current actor and organization;
- required references or creation context;
- idempotency key;
- Permission Context;
- Policy Context;
- valid Human Review where required;
- safe errors;
- AI Context where AI assisted;
- current target state.

### 15.2 Apply Outcomes

Apply may return:

- created or linked references;
- active Task references;
- review still required;
- restricted fields omitted;
- safe warnings;
- idempotency replay status;
- Event references as trace;
- partial or blocked preparation outcome where the contract permits it.

It must not return an official filing result because the pattern performs no filing.

---

## 16. Task Plan and Active Tasks

The preview may prepare Tasks such as:

- confirm applicant identity;
- confirm mark type;
- confirm exact representation;
- clarify target jurisdictions;
- clarify direct or international-route question;
- obtain goods and services description;
- prepare Classification suggestion;
- conduct professional Classification review;
- collect applicant Documents;
- collect authority or priority Documents;
- review Evidence context;
- align Matter and Order scope;
- prepare filing-instruction package;
- perform filing-readiness review.

A Task plan is not an active Task.

Only Task Service creates active Tasks during an allowed apply.

AI may suggest task structure but may not assign, transition or complete Tasks autonomously.

Completing all preparation Tasks does not prove an application was filed.

---

## 17. AI-Assisted Application Preparation

AI may:

- summarize intake and application context;
- extract stated applicant or mark information;
- compare mark versions;
- suggest Classification candidates;
- identify goods and services gaps;
- identify jurisdiction questions;
- summarize Document or Evidence metadata within Policy;
- detect inconsistencies;
- prepare minimum next questions;
- prepare review checklists;
- draft a filing-instruction package for review.

AI must not:

- choose the final applicant;
- decide ownership;
- determine registrability;
- finalize classification;
- certify jurisdiction strategy;
- certify official requirements or deadlines;
- certify Document or Evidence sufficiency;
- approve filing readiness;
- select a provider finally;
- send instructions;
- submit an application;
- execute payment;
- mutate protected state;
- emit Events.

### 17.1 Recommendation Must Preserve Alternatives

Where multiple routes or classifications remain plausible, AI should present bounded alternatives and decision factors.

It should not hide uncertainty by selecting a single “best” answer without authority.

### 17.2 Human Editing and Versioning

If a human edits AI-prepared material:

- the current version changes;
- source and authorship distinctions remain;
- prior review may become stale;
- the edited result requires the applicable review gate.

---

## 18. Idempotency, Retry and Duplicate Safety

Apply must use idempotency.

The same key and same semantic request should replay without duplicating:

- Trademark;
- Brand linkage;
- Matter;
- Order changes;
- Document or Evidence links;
- active Tasks;
- Events.

The same key with materially different applicant, mark, jurisdiction, classification, Document, Evidence or version context should conflict safely.

Idempotency does not decide whether two separately authorized applications represent the same commercial filing intent. That remains an owning-domain and review question.

A retry after a technical failure, a replay of the same apply, and a continuation after new information must remain distinct.

---

## 19. Trace and Audit

Trace should make the preparation path reconstructable.

It may include:

- source Intake reference;
- Workflow preview;
- Permission and Policy evaluations;
- AI assistance;
- Human Review;
- owning-service changes;
- Classification suggestion or review references;
- Document and Evidence linkage;
- Matter and Order alignment;
- Task creation;
- idempotent replay;
- blocked or safe failure outcome.

The Workflow does not emit Events directly.

Event references represent completed facts and are not commands to file.

Audit context should answer:

```text
Which application package was evaluated?
Which versions and sources were used?
What was suggested by AI?
What was approved by a human?
Which owning Service changed each record?
What remained missing or restricted?
Why was the pattern allowed, paused or blocked?
Which separate action is required next?
```

---

## 20. Safe Failure and Recovery

Controlled failures may include:

- validation failure;
- invalid reference;
- Permission denied;
- Policy restricted;
- Human Review required;
- idempotency key required;
- idempotency conflict;
- unsupported version;
- invalid state;
- not found under non-disclosure;
- conflict;
- internal safe error.

Errors must not expose:

- database identifiers;
- restricted applicant or Trademark data;
- raw Document or Evidence content;
- restricted Classification sources;
- Policy internals;
- Permission internals;
- prompts;
- hidden reasoning;
- stack traces.

A recoverable result should state, where allowed:

- affected preparation area;
- missing or conflicting condition;
- current stable references;
- required responsible role;
- next allowed action;
- whether a new preview is required;
- whether prior review remains valid.

---

## 21. Example — Multi-Jurisdiction Word and Logo Request

A customer asks to register its name and logo in the United States and the European market for software and consulting services.

### 21.1 Intake Context

Chapter 17 may have established:

- Customer reference;
- Brand context;
- uploaded logo Document;
- proposed Matter;
- initial service scope;
- missing applicant confirmation.

### 21.2 Application Preview

The preview identifies:

- two candidate mark representations: word and combined logo;
- proposed applicant name requires confirmation;
- “European market” requires a precise jurisdiction or route decision;
- product and service descriptions are too broad for final Classification;
- logo Document reference is valid but official-use sufficiency is unreviewed;
- the Order scope covers one application, while the request may imply multiple applications;
- professional Classification and scope review are required.

### 21.3 AI Assistance

AI may prepare:

- a comparison of the two mark representations;
- candidate software and consulting classes;
- questions needed to distinguish goods from services;
- route questions for professional review;
- an Order-scope mismatch summary;
- a draft request for missing information.

These remain suggestions and drafts.

### 21.4 Review

Authorized humans separately review:

- applicant identity;
- jurisdiction scope;
- Classification version;
- mark/application count;
- Document package;
- commercial scope.

Each review is version-bound.

### 21.5 Apply

If current gates allow, owning Services may:

- create or update Trademark preparation records;
- link the Brand;
- validate Jurisdiction references;
- record draft or review-required Classification state;
- link Documents;
- align Matter and Order context;
- create active preparation Tasks.

### 21.6 Result

A safe result may state:

```text
Application workspace applied.
Two candidate applications remain under reviewed scope.
Official filing is not authorized or performed.
A separate filing-instruction decision and protected submission action are required.
```

This is successful application preparation.

---

## 22. Pattern Acceptance Checklist

The Application Preparation Pattern is correct when:

- [ ] Customer, applicant, contact and payer roles remain distinct;
- [ ] Brand context is not confused with the exact mark representation;
- [ ] proposed Trademark state is not presented as an official filing;
- [ ] jurisdiction language is resolved or explicitly left open;
- [ ] route strategy is not finalized without governed authority;
- [ ] source business descriptions remain visible beneath Classification suggestions;
- [ ] AI suggestions remain non-final;
- [ ] professional Classification finalization is review-gated;
- [ ] Document reference validity is not treated as content access or sufficiency;
- [ ] Evidence assistance is not treated as legal sufficiency;
- [ ] Matter and Order scope are aligned without silent expansion;
- [ ] payment and provider commitment remain outside the pattern;
- [ ] preview has no side effects;
- [ ] apply uses current versions, Idempotency, Permission and Policy;
- [ ] owning Services perform all mutations;
- [ ] Task Service alone creates active Tasks;
- [ ] Human Review is scope- and version-bound;
- [ ] a prepared workspace is not called filing-ready without the required composite review;
- [ ] filing readiness is not treated as filing authorization;
- [ ] the Workflow does not submit an application;
- [ ] Event references remain trace only;
- [ ] safe failures provide a governed recovery path where allowed.

---

## 23. Product Boundary

Book 04 may present applicant, mark, jurisdiction, Classification, Document and readiness workflows. It must preserve the distinction among preparation, professional review, filing authorization and official filing. Book 03 does not define wizards, recommendations or filing controls.

## 24. Implementation Boundary

This pattern adds no universal filing-readiness object, Classification rule, jurisdiction decision engine, fee model, provider selection, filing connector, payment capability or Product UI. Implementation returns to Book 02 contracts and owning Services.

## 25. Chapter Result

The Application Preparation Pattern creates a governed workspace for professional application work.

```text
Resolve the applicant without assuming authority.
Identify the mark without collapsing Brand and application.
Prepare jurisdiction context without pretending strategy is settled.
Suggest Classification without converting suggestion into professional truth.
Link Documents and Evidence without certifying sufficiency.
Align Matter, Order and Tasks without executing payment or filing.
Apply only through owning Services.
Stop before official submission.
```

The pattern succeeds when the next decision is exact, reviewable and traceable.

The next chapter defines the **Communication Review Pattern**, where prepared language must move through versioned Human Review and a separate send boundary without allowing drafting, approval and transmission to collapse into one action.
