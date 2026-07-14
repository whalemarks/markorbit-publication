# B05-CH-43 — Standalone, Embedded and Cross-Product Experience

**Status:** Part VII Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VII — Product Experience and Evolution

## Chapter Purpose

Parts II–VI define what MarkReg must do across the trademark lifecycle.

CH43 answers:

> How may the same governed MarkReg journey appear as a standalone Product, inside Lite, inside a professional Workplace, or beside another Product without creating duplicate authority, hidden state, or broken return paths?

```text
One Product journey
→ multiple permitted entry surfaces
→ one controlled context
→ typed Handoff and Return
→ no duplicated formal authority
```

An embedded experience is another surface for the same Product contract. It is not a second implementation of the lifecycle.

---

## 1. User Question and Primary Action

**User question:** Where am I, what context am I acting in, what may I do here, and where will the result return?

**Primary action:** Continue the governed MarkReg journey or return a typed result to the calling Product or Workplace.

Every surface must make visible:

- the current organization or personal context;
- the active client, brand, portfolio, Matter or opportunity context;
- the MarkReg journey and current step;
- the source of inherited information;
- the user’s role and action rights;
- whether the view is standalone or embedded;
- which formal system owns the current business fact;
- the next valid action;
- the return destination.

---

## 2. Experience Modes

MarkReg may appear in four controlled modes.

| Mode | Primary use | Context owner | Return behavior |
| --- | --- | --- | --- |
| standalone | user starts and completes a MarkReg journey directly | MarkReg Product context plus linked formal objects | remains in MarkReg or opens a governed external context |
| Lite embedded | an individual or small team starts from Lite | Lite supplies personal or local context; MarkReg owns Product journey state | returns result and next actions to Lite |
| Workplace embedded | an organization starts from its Workplace | Workplace supplies organization, identity, client and responsibility context | returns typed Product result to Workplace |
| cross-Product handoff | another Product requests a MarkReg capability or journey | calling Product retains its own context; MarkReg receives purpose-limited input | returns a typed outcome, reference or next-action candidate |

These modes may share components and APIs. They must not share unbounded data or bypass authority.

---

## 3. Standalone MarkReg

Standalone MarkReg provides a complete Product experience for users who enter directly.

It must still resolve:

- identity;
- organization or personal operating context;
- client and applicant relationships;
- permission and responsibility;
- data provenance;
- formal Order and Matter links;
- provider and Owning Service boundaries;
- communication channels;
- return and export behavior.

Standalone does not mean isolated.

It may consume shared Core objects and Execution capabilities, but it does not become the Workplace or Owning Service.

### 3.1 Standalone entry examples

A user may start from:

- a new trademark application need;
- an existing registration;
- an official notice;
- a renewal reminder;
- a portfolio review;
- an uploaded certificate;
- a request from a client;
- an imported historical matter.

The Product must establish the correct entry context before presenting actions.

### 3.2 Direct entry safety

Direct entry must not silently create:

- a client record owned by another organization;
- a formal Order;
- a Matter;
- an applicant or owner relationship;
- provider appointment;
- filing authority;
- deadline responsibility.

Those facts require the relevant Owning Service, approval or Handoff.

---

## 4. Lite-Embedded Experience

MarkOrbit Lite may provide a lightweight personal Workplace, local database, personal case library and personalized Knowledge context.

When MarkReg is embedded in Lite:

- Lite may prefill known personal, client, brand and portfolio context;
- the user must see which information came from Lite;
- local or personal information remains scoped to the user’s Lite context;
- MarkReg creates Product-local candidates rather than silently formalizing them;
- formal business actions still require the relevant organization, provider or Owning Service;
- returned results may enrich the local case and Knowledge context subject to provenance and permission.

### 4.1 Local continuity

A Lite user may pause a journey and continue later.

The saved state must identify:

- Product journey ID;
- current version;
- local context version;
- unresolved questions;
- source snapshots;
- expiry and revalidation needs;
- formal references, if any;
- whether local changes have not yet been handed off.

### 4.2 Personalization boundary

Personalization may change:

- ordering of questions;
- recommended explanation depth;
- preferred display language;
- reusable organization-specific templates;
- evidence suggestions;
- commonly used provider candidates;
- reminder presentation.

Personalization must not change legal rules, source truth, approval requirements or professional responsibility.

---

## 5. Workplace-Embedded Experience

A professional Workplace is the organization’s independent operating orbit.

When MarkReg is embedded in a Workplace, the Workplace may supply:

- organization identity;
- users and roles;
- clients and contacts;
- responsibility assignments;
- commercial policy;
- private provider relationships;
- Knowledge and template access;
- Matter and Order references;
- communication and audit context.

MarkReg supplies the Product journey, Product artifacts, recommendations, options, controlled packages and lifecycle views.

### 5.1 Embedded shell and Product interior

The Workplace shell may control:

- navigation;
- identity and role;
- organization branding;
- notification center;
- task inbox;
- organization-level search;
- access to related Products.

The MarkReg interior controls:

- Product step sequence;
- Product-local validation;
- Product artifact versions;
- chapter-defined user actions;
- Product explanations;
- MarkReg-specific readiness and next-action logic.

The shell may host the Product. It may not rewrite the Product contract silently.

### 5.2 Organization policy overlays

A Workplace may apply organization policy such as:

- required reviewer level;
- discount approval threshold;
- preferred private providers;
- internal deadline buffers;
- evidence handling restrictions;
- communication approval rules;
- local language requirements;
- escalation routes.

Policy overlays must be identifiable, versioned and distinguishable from jurisdiction rules and Product defaults.

---

## 6. Cross-Product Experience

Other Products may request MarkReg capabilities without absorbing MarkReg.

Examples include:

- a brand-management Product requests a filing recommendation;
- a transaction Product requests a chain-of-title review;
- a monitoring Product opens an opposition candidate;
- a client-service Product starts a renewal proposal;
- a portfolio Product requests coverage-gap analysis.

The calling Product must state a purpose.

MarkReg must accept only the minimum context required for that purpose.

---

## 7. Typed Handoff Envelope

Every cross-context entry should use a typed Handoff Envelope.

Minimum fields include:

| Field | Meaning |
| --- | --- |
| handoff ID | stable identity for retries and trace |
| source Product or Workplace | caller identity |
| destination | MarkReg Product and requested journey |
| purpose | why MarkReg is being invoked |
| initiating actor | Human or system actor |
| organization context | relevant operating orbit |
| client or portfolio references | linked context without uncontrolled copying |
| supplied facts | values and source references |
| supplied artifacts | versioned documents or Product artifacts |
| permission scope | what MarkReg may read and use |
| requested result | expected candidate, package, review or reference |
| return route | destination for returned result |
| expiry | when inherited context must be revalidated |
| correlation ID | cross-system audit continuity |

A Handoff Envelope is not approval, instruction, appointment or execution authority.

---

## 8. Context Acceptance

MarkReg must not automatically trust every supplied value.

On receipt it should classify context as:

- accepted for display;
- accepted for recommendation;
- requires client confirmation;
- requires professional verification;
- requires official-source verification;
- stale;
- conflicting;
- outside purpose;
- prohibited from reuse.

Inherited facts keep their source and checked date.

A conflict opens a resolution step rather than overwriting one value with another.

---

## 9. Product Session and Resume Contract

A Product Session records the user’s current interaction with a versioned journey.

It includes:

- session ID;
- Product journey ID;
- actor and role;
- organization context;
- entry mode;
- active step;
- visible artifact versions;
- unsaved local edits;
- unresolved warnings and blockers;
- last confirmed decision;
- pause reason;
- resume eligibility;
- return route.

The Product Session is not the formal Matter state.

A session may expire while the Matter remains active.

On resume, MarkReg must check whether:

- jurisdiction rules changed;
- official status changed;
- a deadline changed;
- another actor created a newer artifact version;
- approval expired;
- the user’s permissions changed;
- the calling context was superseded.

---

## 10. Return Envelope

When an embedded or cross-Product journey reaches a valid return point, MarkReg creates a Return Envelope.

It may contain:

- recommendation or Option Set;
- Proposal reference;
- accepted Quote reference;
- Handoff status;
- Filing Package Candidate reference;
- Filing Approval reference;
- official acknowledgement reference;
- Outcome Snapshot;
- Right Baseline;
- Portfolio Action Plan;
- blockers and unresolved questions;
- next-action candidates;
- source and version metadata.

The receiving surface must not display a candidate as a formal outcome.

---

## 11. Navigation and Deep Links

A governed deep link should identify:

- destination Product;
- journey or artifact reference;
- expected organization context;
- purpose;
- requested view;
- expiry;
- one-time or reusable status.

The destination must recheck identity and permission.

A URL alone must not carry authority or sensitive facts.

---

## 12. Cross-Surface State Rules

The same journey may be visible in several surfaces, but only one canonical Product version exists.

The Product must prevent:

- parallel unmerged drafts presented as one version;
- a Lite copy silently overwriting a Workplace-approved package;
- a client-facing view exposing internal margin or provider notes;
- a provider view exposing unrelated client records;
- a stale embedded page showing an expired approval as current;
- a Return Envelope creating duplicate Order or Matter records.

Conflicting edits require explicit merge, supersession or rejection.

---

## 13. Visibility of Authority

Every action surface should answer:

1. Is this a Product candidate or a formal object?
2. Who owns the formal fact?
3. Who may edit it?
4. Who must review it?
5. Who may approve it?
6. What external effect may follow?
7. What evidence will confirm that effect?

Buttons should reflect the actual next action.

Examples:

- `Save draft`, not `Create application`;
- `Request professional review`, not `Approve legally`;
- `Send for client confirmation`, not `Accept for client`;
- `Create filing instruction candidate`, not `File now`;
- `Open official source`, not `Verify automatically`.

---

## 14. EMBERLOOP Cross-Product Experience

`EMBERLOOP` begins in a Workplace portfolio view.

The organization opens MarkReg as an embedded Product with:

- client reference;
- three brand variants;
- target markets;
- internal account owner;
- private provider preferences;
- existing UK Right Baseline;
- active US and EU Matter references.

MarkReg accepts the context through a Handoff Envelope.

The client later opens a purpose-limited confirmation link. The client sees filing scope, cost and required decisions, but not internal margin or provider-comparison notes.

A professional returns to the same journey through the Workplace task inbox. MarkReg detects a newer EU opposition event and blocks use of the stale portfolio summary.

After review, MarkReg returns:

- updated Outcome Snapshots;
- a UK Maintenance Obligation Set reference;
- a US next-action candidate;
- an EU dispute-status reference;
- no unsupported consolidated “global status”.

---

## 15. RIVERKITE Lite-to-Workplace Transition

A professional first analyzes `RIVERKITE` in Lite using a local case library.

The local journey identifies:

- six registrations;
- a chain-of-title gap;
- two weak use-evidence categories;
- a renewal cluster;
- one cancellation defense.

The user later hands the work into the organization’s Workplace.

The Handoff Envelope includes only approved client facts, source references and candidate artifacts. Personal notes marked private are not transferred.

The Workplace resolves organization roles, commercial policy and formal Matter links.

MarkReg then creates organization-scoped renewal and recordal candidates without duplicating the local case history as formal truth.

---

## 16. Conformance Scenarios

### Scenario A — stale embedded page

**Given** a user leaves a Filing Approval page open in a Workplace tab  
**And** a newer package version is approved elsewhere  
**When** the user attempts execution  
**Then** MarkReg blocks the action  
**And** displays the newer version and required re-review.

### Scenario B — Lite private note

**Given** a Lite case contains personal annotations  
**When** the user hands the case to an organization Workplace  
**Then** only purpose-approved facts and artifacts are transferred  
**And** private annotations remain local.

### Scenario C — deep link in wrong organization

**Given** a professional opens a valid MarkReg deep link while active in another organization  
**When** context does not match  
**Then** MarkReg does not open the protected journey  
**And** requires an authorized context switch.

### Scenario D — duplicate return

**Given** a Return Envelope was already consumed to create an Order reference  
**When** the receiving Product retries consumption  
**Then** the existing result is returned  
**And** no duplicate Order is created.

### Scenario E — cross-Product overreach

**Given** another Product requests a portfolio recommendation  
**When** it also sends unrelated client financial data  
**Then** MarkReg rejects or ignores the excess data  
**And** records the purpose limitation.

---

## 17. AI Assistance

AI may assist with:

- identifying likely entry journeys;
- summarizing inherited context;
- detecting conflicting versions;
- suggesting the next Product step;
- translating surface explanations;
- comparing Return Envelope versions;
- detecting missing return routes.

AI may not:

- select the operating organization;
- expand permission scope;
- merge conflicting facts silently;
- transfer private Lite information without instruction;
- convert a candidate into a formal object;
- create approval or external authority;
- claim a cross-surface state is current without revalidation.

---

## 18. Failure Modes

MarkReg fails this chapter if:

- embedded mode creates a second lifecycle implementation;
- standalone mode bypasses Workplace or Owning Service authority;
- Lite personalization changes legal rules;
- deep links bypass identity or permission checks;
- Product Sessions are treated as formal Matter state;
- context is copied without provenance or purpose;
- return results are not idempotent;
- client, professional and provider views expose the same unrestricted data;
- the user cannot tell where a result will return.

---

## 19. Minimum Product Lock

A conforming MarkReg edition must provide:

1. explicit standalone, embedded and cross-Product modes;
2. visible operating context and entry mode;
3. typed Handoff and Return Envelopes;
4. source-preserving context acceptance;
5. Product Session pause and resume checks;
6. idempotent return consumption;
7. identity and permission revalidation for deep links;
8. separation of Product-local and formal state;
9. purpose-limited data transfer;
10. observable conformance behavior.

---

## 20. Next Handoff

CH43 defines where MarkReg appears and how context travels.

CH44 defines what each participant may see, contribute, review, approve and communicate within those surfaces.