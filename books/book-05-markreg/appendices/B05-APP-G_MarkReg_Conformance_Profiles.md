# Appendix G — MarkReg Conformance Profiles

**Status:** Controlled Reader Draft — PF-04 and PF-05 Reconciled; PF-08 Validation Pending  
**Primary sources:** CH46–CH47, B05-SPEC-0001 v0.2, B05-SPEC-0003 v0.2 and B05-SPEC-0004 v0.2  
**Reader purpose:** allow a Product edition or implementation to state honestly which MarkReg capabilities, jurisdictions, services and lifecycle stages it supports.

## G.1 Conformance Rule

Not every implementation must launch the full lifecycle.

```text
partial scope + accurate profile statement
= permitted

partial scope + Full-Lifecycle claim
= non-conforming
```

A profile states tested Product behavior. It does not grant production or protected-action authority.

---

## G.2 Required Conformance Statement

A declaration must identify:

- Product and implementation version;
- supported profile or profiles;
- supported jurisdictions, services and proceeding types;
- exact Jurisdiction Pack, module and Rule versions;
- Pack support state for each jurisdiction/service/stage;
- supported applicant or owner types and routes;
- participant surfaces;
- required Human roles and qualifications;
- Owning Service and Execution dependencies;
- provider, connector and manual routes;
- excluded stages and known limitations;
- scenario, evaluation and validation status;
- suspended or retired modules;
- production authority state;
- external protected-action authority state.

Marketing claims must not exceed this statement.

---

## G.3 Profile Inventory

### Profile 1 — Foundation

Minimum capability:

- MarkReg Product identity and non-goals;
- Books 01–04 authority boundaries;
- participant and AI role distinctions;
- Product, formal, Execution, provider and official-state distinctions;
- source, version, Review, approval and correction principles;
- organization and permission context.

**Minimum Pack evidence:** source and authority boundary rules only. No jurisdiction/service support claim is required.

**Minimum scenarios:** MR-SCN-01, 09, 10, 11, 18, 22, 35, 36, 40 and 41.

This profile does not support a user-facing trademark service journey by itself.

### Profile 2 — Guided Decision

Includes Foundation plus:

- Business Context and Need Brief;
- jurisdiction and route candidates;
- filing units and applicant context;
- classification and goods/services guidance;
- purpose-limited search and risk;
- Recommendation Set, Option Set and Proposal;
- Human correction and Review.

**Minimum Pack evidence:** each declared jurisdiction/service module must be at least Guidance Capable.

**Minimum additional scenarios:** MR-SCN-02, 03, 04, 13, 14, 37 and 38.

External filing is not supported.

### Profile 3 — Commercial Intake

Includes Guided Decision plus:

- transparent Price Basis and Quote;
- exact-version Client Acceptance;
- Commercial Instruction;
- Formal Intake and Requirement Set;
- dimensional Readiness Assessment;
- governed Handoff to formal work.

**Minimum Pack evidence:** current fee-driving units, official-fee sources, later-stage fee disclosure, Intake requirements, document rules and commercial variance behavior.

**Minimum additional scenarios:** MR-SCN-05, 06, 07, 08, 15, 28 and 38.

The profile may stop at governed Handoff.

### Profile 4 — Filing Preparation

Includes Commercial Intake plus:

- Filing Package Candidate;
- source and form lineage;
- material diff;
- client factual confirmation;
- Professional Review;
- version-specific Filing Approval;
- provider Capability Need and route candidates.

**Minimum Pack evidence:** each declared filing module must be Preparation Capable, including form, document, package and Review behavior.

**Minimum additional scenarios:** MR-SCN-16, 17, 18, 19, 20 and 37.

Execution and official submission may remain outside scope.

### Profile 5 — Governed Filing

Includes Filing Preparation plus:

- Human route or provider Selection;
- appointment, instruction and Provider Acceptance;
- governed manual, provider or connector Execution;
- stable idempotency identity;
- sent, delivery, provider and official acknowledgement states;
- unknown state, reconciliation and duplicate safety;
- official evidence return.

**Minimum Pack evidence:** each declared route must be Execution Capable with provider or connector scope, submission evidence, acknowledgement, reconciliation, suspension and rollback behavior.

**Minimum additional scenarios:** MR-SCN-21, 22, 23, 24, 25, 37 and 38.

The declaration must identify supported offices, providers and connectors.

### Profile 6 — Post-Filing

Includes relevant earlier profiles plus selected:

- Official Event Snapshots;
- examination and Issue Sets;
- Response Strategy and Response Package;
- deadlines and client Decisions;
- publication and opposition windows;
- adversarial or remedy contexts;
- governed response filing;
- Outcome Snapshot and corrected Communication.

**Minimum Pack evidence:** a service-specific Lifecycle Capable module for each declared proceeding type, including deadline, response, fee, provider and official-outcome rules.

**Minimum additional scenarios:** MR-SCN-10, 23, 26, 27, 28, 29, 37, 38 and 39.

The declaration must state supported proceeding types.

### Profile 7 — Portfolio Continuity

Includes relevant earlier profiles plus:

- Registration Outcome and Right Baseline;
- certificate and official-record distinctions;
- Maintenance Obligation Sets;
- renewal packages;
- changes and recordals;
- assignment, licensing and chain of title;
- use evidence and vulnerability;
- Portfolio Continuity View and Action Plan.

**Minimum Pack evidence:** declared registration, maintenance, renewal, recordal and transaction modules must be Guidance, Preparation, Execution or Lifecycle Capable at the level actually claimed.

**Minimum additional scenarios:** MR-SCN-12, 30, 31, 32, 33, 37 and 38.

One view must preserve independent right histories.

### Profile 8 — Full-Lifecycle

Includes Profiles 1–7 plus:

- cross-stage artifact and state continuity;
- standalone, Lite, Workplace and cross-Product surfaces;
- participant-specific visibility and action rights;
- governed Jurisdiction Pack and Rule versioning;
- Pack-bound AI assistance;
- layered quality and lifecycle metrics;
- pilot, stop, rollback and evolution controls;
- complete conformance and correction behavior.

**Minimum Pack evidence:** every declared jurisdiction/service/stage must have an explicit support state, current Pack version, scenario evidence, professional owner and suspension process. Unsupported services remain exclusions.

**Minimum additional scenarios:** MR-SCN-34 through MR-SCN-41, all applicable PF-05 scenarios and every applicable zero-tolerance scenario.

Full-Lifecycle does not mean every jurisdiction or every proceeding is supported.

---

## G.4 Profile Evidence Matrix

| Evidence | Foundation | Guided Decision | Commercial Intake | Filing Preparation | Governed Filing | Post-Filing | Portfolio Continuity | Full-Lifecycle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| constitutional rules | required | required | required | required | required | required | required | required |
| artifact lineage | boundary | recommendation | commercial | package and approval | Execution and evidence | event and response | right and obligation | complete |
| participant matrix | required | required | required | required | required | required | required | required |
| scenario evidence | constitutional | recommendation | Intake and commercial | Review and approval | unknown and duplicate safety | event, deadline and Communication | renewal and ownership | all families |
| official evidence | none | none | none | none | required | required | required | required |
| Pack state | boundary only | Guidance Capable | guidance plus commercial rules | Preparation Capable | Execution Capable | proceeding Lifecycle Capable | declared later-stage modules | all declared modules |
| fee evidence | none | explanation if shown | current components and variance | package-linked | route-linked | stage-linked | renewal/recordal linked | all declared stages |
| form evidence | none | none unless shown | requirement level | exact form/schema | executable version | proceeding-specific | renewal/recordal specific | all declared stages |
| metrics | boundary defects | user and recommendation | commercial and readiness | package quality | reliability and safety | deadline and Communication | lifecycle continuity | layered model |
| failure recovery | permission | version change | expired Quote and payment | invalid approval | reconciliation and retry | corrected notice | owner and recordal conflict | complete |

---

## G.5 Pack Support-State Limit

A Profile claim cannot exceed its Pack evidence.

| Pack module state | Maximum permitted claim |
| --- | --- |
| Research Only | internal research only |
| Guidance Capable | explanation and candidate guidance |
| Preparation Capable | governed preparation and Review |
| Execution Capable | approved action through declared route |
| Lifecycle Capable | declared later-stage continuity |
| Suspended | no new dependent protected action |
| Retired | historical lineage only |

Examples:

- a Preparation Capable renewal module may support renewal-package drafting but not renewal filing;
- an Execution Capable new-filing module does not imply opposition support;
- a Lifecycle Capable registration module does not imply assignment recordal support;
- a suspended fee module blocks affected new Quotes or protected actions.

---

## G.6 Required Jurisdiction and Service Evidence

Every declared jurisdiction/service combination must identify:

- Pack ID and version;
- module and support state;
- effective period;
- Source and Rule Records;
- professional owner;
- supported applicant or owner types;
- supported routes;
- forms and document versions;
- fee table and fee-driving units;
- deadline rules where applicable;
- provider, connector or manual route;
- applicable scenario results;
- known exclusions;
- suspension and review trigger.

A generic country form cannot satisfy this requirement.

---

## G.7 Commercial Evidence by Profile

### Guided Decision

When costs are shown, the surface must distinguish estimates and known exclusions.

### Commercial Intake

Must prove:

- immutable Quote versions;
- official, professional, provider, tax and currency components;
- later-stage fee disclosure;
- discount and credit authority;
- client versus internal visibility;
- fee-change and repricing behavior.

### Governed Filing

Must additionally prove:

- payment gate and Filing Approval remain distinct;
- provider payable and client price remain distinguishable;
- duplicate payment and failed-action handling;
- official acknowledgement is not inferred from payment.

### Post-Filing and Portfolio Continuity

Must prove stage-specific prices for:

- examination or response;
- opposition or remedy;
- registration-stage work;
- maintenance and declarations;
- renewal and surcharges;
- recordals and transactions.

---

## G.8 Zero-Tolerance Requirements

A Profile cannot pass if an applicable zero-tolerance scenario fails.

Minimum zero-tolerance coverage includes:

- expired or insufficient authority;
- wrong-version approval;
- incomplete required Review;
- provider over-access;
- technical success represented as official acknowledgement;
- duplicate payment, filing or Return effect;
- unsafe retry;
- unverified deadline conflict;
- client silence treated as authority;
- private Lite data transferred without purpose;
- wrong-organization access;
- AI current-rule conclusion without controlled sources;
- publication status treated as production authority;
- Pack support claimed above its evidence state;
- hidden margin inside official fee;
- silent fee, form or rule mutation after acceptance or approval.

---

## G.9 Profile Dependency Rule

Profiles are cumulative only where the declared journey consumes earlier capability.

A Post-Filing implementation may ingest an existing official Matter without offering Guided Decision, but it must conform to Foundation rules and every earlier artifact, approval, commercial or Execution contract it consumes.

The declaration must state whether prior-stage records are:

- created by this edition;
- imported through a Handoff;
- referenced from an Owning Service;
- unsupported.

---

## G.10 Partial-Profile Example

A conforming Commercial Intake edition may support:

```text
Need Brief
→ Recommendation Set
→ Option Set
→ Proposal
→ Quote
→ Client Acceptance
→ Formal Intake
→ Readiness Assessment
→ governed Handoff
```

It must state:

- supported Guidance Capable jurisdiction modules;
- filing preparation and submission are outside scope;
- no official filing status is produced;
- professional and Owning Service Handoffs are required;
- applicable scenarios pass;
- price and later-stage exclusions are visible.

It may not claim filing automation or Full-Lifecycle support.

---

## G.11 Full-Lifecycle Example

A Full-Lifecycle candidate may support:

```text
Need and recommendation
→ commercial Intake
→ package and approval
→ governed filing
→ official events and response
→ registration and maintenance
→ renewal, recordal and portfolio continuity
→ embedded experience, rules, metrics and evolution
```

It still must declare:

- exact supported jurisdiction/service modules;
- Pack state per module;
- supported provider and connector routes;
- mandatory Human roles;
- excluded proceedings;
- tested scenarios and Pack versions;
- suspended modules;
- separate production and protected-action gates.

---

## G.12 Upgrade Rule

```text
feature exists
≠ Profile supported

feature exists
+ source, Pack, authority, commercial, failure and scenario evidence
→ Profile candidate

Profile candidate
+ controlled Review
→ declared support
```

Moving upward requires evidence for every added capability and every applicable zero-tolerance scenario.

---

## G.13 Non-Conforming Claims

Examples include:

- global support from one generic country form;
- Full-Lifecycle claim where the Product stops at filing;
- official status without office evidence;
- autonomous professional advice without eligible Review;
- provider-network claim without appointment and acceptance controls;
- AI legal certainty from model confidence;
- publication RC status presented as production authority;
- hidden unsupported jurisdictions or excluded services;
- Profile declaration without scenario results;
- jurisdiction support without Pack module and support state;
- renewal or recordal support inferred from a new-filing Pack;
- client price presented as official fee;
- suspended module presented as active.

---

## G.14 Profile Control Matrix

| Profile | Core scenarios | Minimum jurisdiction/commercial evidence before RC1 |
| --- | --- | --- |
| Foundation | 01, 09–11, 18, 22, 35, 36, 40, 41 | boundary rules only |
| Guided Decision | Foundation + 02–04, 13, 14, 37, 38 | Guidance Capable modules |
| Commercial Intake | Guided + 05–08, 15, 28 | current fee, Intake and variance evidence |
| Filing Preparation | Commercial + 16–20 | Preparation Capable forms and packages |
| Governed Filing | Filing + 21–25 | Execution Capable route and official evidence |
| Post-Filing | relevant prior + 10, 23, 26–29, 37–39 | proceeding Lifecycle Capable modules |
| Portfolio Continuity | relevant prior + 12, 30–33, 37, 38 | maintenance, renewal, recordal and transaction modules |
| Full-Lifecycle | all applicable scenarios | all declared modules, PF-07 and PF-08 complete |

---

## G.15 Reconciliation Status

```text
Profile scope and scenario requirements: COMPLETE
Participant and surface requirements: COMPLETE
Pack support-state limits: COMPLETE
Jurisdiction and service evidence: COMPLETE
Commercial evidence by Profile: COMPLETE
PF-04 Appendix G work: COMPLETE
PF-05 Appendix G work: COMPLETE
PF-07 publication integration: PENDING
PF-08 scenario and structural validation: PENDING
```

Appendix G is a controlled reader draft reconciled through PF-05. A Profile becomes operationally meaningful only when its declared Pack modules, scenario evidence and authority gates pass.