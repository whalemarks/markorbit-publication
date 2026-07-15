# Appendix G — MarkReg Conformance Profiles

**Status:** Controlled Reader Draft v0.3 — PF-06D Reconciled; PF-08 Validation Pending  
**Primary sources:** CH46–CH47 and B05-SPEC-0001, 0003 and 0004 v0.3  
**Reader purpose:** allow an edition or implementation to state honestly which MarkReg capabilities, jurisdictions, services and stages it supports.

## G.1 Conformance Rule

```text
partial scope + accurate Profile statement
= permitted

partial scope + Full-Lifecycle claim
= non-conforming
```

A Profile describes tested Product behavior. It does not grant production or External Protected Action authority.

## G.2 Required Conformance Statement

`MR-G10 Conformance Statement` identifies:

- Product and implementation version;
- supported Profile(s);
- jurisdictions, services and proceedings;
- exact Pack/module/Rule versions and Support States;
- supported applicant/owner types and routes;
- participant surfaces and required Human roles;
- Owning Service and Execution dependencies;
- provider, connector and manual routes;
- excluded stages and known limitations;
- scenario, Evaluation and validation state;
- suspended or retired modules;
- implementation, production and protected-action authority state.

Marketing claims cannot exceed the Statement.

## G.3 Profile Inventory

### 1 — Foundation

Minimum:

- Product identity and non-goals;
- Books 01–04 boundaries;
- participant, applicant/authority and AI role distinctions;
- Product, formal, Execution, provider and official-state distinctions;
- Source, version, Review, Approval and correction principles;
- organization and permission context.

Minimum scenarios: 01, 09, 10, 11, 18, 22, 35, 36, 40 and 41.

No user-facing service journey is supported by Foundation alone.

### 2 — Guided Decision

Foundation plus:

- Business Context and Need Brief;
- jurisdiction/route and filing-unit candidates;
- `MR-C12 Applicant and Authority Context`;
- classification and goods/services guidance;
- purpose-limited search and risk;
- Recommendation Set, Option Set and Proposal;
- Human correction and Review.

Each declared module is at least Guidance Capable.

Additional scenarios: 02, 03, 04, 13, 14, 37 and 38.

### 3 — Commercial Intake

Guided Decision plus:

- transparent price basis and Quote;
- exact-version Client Acceptance;
- Commercial Instruction;
- Formal Intake and Requirement Set;
- dimensional Readiness Assessment;
- governed Handoff.

Pack Evidence includes fee units, Official Fee Sources, later-stage disclosure, Intake/Document Rules and variance behavior.

Additional scenarios: 05, 06, 07, 08, 15, 28 and 38.

### 4 — Filing Preparation

Commercial Intake plus:

- Filing Package Candidate and diff;
- client factual confirmation;
- Professional Review;
- exact-version Filing Approval;
- Capability Need and route candidates.

Declared filing modules are Preparation Capable.

Additional scenarios: 16, 17, 18, 19, 20 and 37.

### 5 — Governed Filing

Filing Preparation plus:

- Human Selection;
- appointment, Provider Instruction and Provider Acceptance;
- governed provider, connector or manual Execution;
- idempotency;
- submission, delivery, provider and official acknowledgement states;
- unknown-state reconciliation and duplicate safety;
- official Evidence Return.

Each declared route is Execution Capable and explicitly named.

Additional scenarios: 21, 22, 23, 24, 25, 37 and 38.

### 6 — Post-Filing

Relevant earlier Profile contracts plus selected:

- Official Event Snapshots;
- examination, Issue Set and response;
- Deadlines and client Decisions;
- publication/opposition windows;
- adversarial/remedy Contexts;
- governed response filing;
- Outcome Snapshot and corrected Communication.

Each proceeding type has a Lifecycle Capable module at the exact claimed scope.

Additional scenarios: 10, 23, 26, 27, 28, 29, 37, 38 and 39.

### 7 — Portfolio Continuity

Relevant earlier Profile contracts plus:

- Registration Outcome, scope diff and Right Baseline;
- certificate/official-record distinction;
- Maintenance Obligations and Use-Evidence Coverage;
- Renewal Packages and Renewal Approval;
- `MR-C12` owner/authority verification where material;
- recordal, transaction, licence and Chain-of-Title View;
- Portfolio Continuity View and Action Plan.

Each later-stage module declares its actual Guidance, Preparation, Execution or Lifecycle Support State.

Additional scenarios: 12, 30, 31, 32, 33, 37 and 38.

### 8 — Full-Lifecycle

Profiles 1–7 plus:

- cross-stage lineage and state continuity;
- standalone, Lite, Workplace and cross-Product surfaces;
- Participant Surface Projections and action rights;
- governed Pack and Rule versioning;
- Pack-bound AI Assistance;
- layered metrics, Evaluation, pilot, stop and rollback controls;
- complete Conformance and correction behavior.

Every declared jurisdiction/service/stage has explicit Support State, Pack Version, scenario Evidence, professional owner and suspension process.

Full-Lifecycle does not mean every jurisdiction or proceeding is supported.

## G.4 Evidence Matrix

| Evidence | Foundation | Guided | Commercial | Preparation | Filing | Post-Filing | Portfolio | Full |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| constitutional Rules | required | required | required | required | required | required | required | required |
| record lineage | boundary | recommendation | commercial | Package/Approval | Execution/Evidence | event/response | right/obligation | complete |
| participant matrix | required | required | required | required | required | required | required | required |
| scenarios | constitutional | recommendation | Intake/commercial | Review/Approval | unknown/duplicate | event/Deadline | renewal/title | all applicable |
| official Evidence | none | none | none | none | required | required | required | required |
| Pack State | boundary | Guidance | guidance + commercial | Preparation | Execution | Lifecycle by proceeding | declared later-stage modules | all declared modules |
| metrics | boundary defects | user/recommendation | commercial/readiness | Package quality | reliability/safety | Deadline/Communication | continuity | layered |
| recovery | permission | version change | expired Quote/payment | invalid Approval | reconciliation/retry | corrected notice | owner/recordal conflict | complete |

## G.5 Pack-State Limit

| Pack module state | Maximum permitted claim |
| --- | --- |
| Research Only | internal research only |
| Guidance Capable | explanation and candidate guidance |
| Preparation Capable | governed preparation and Review |
| Execution Capable | approved action through declared route |
| Lifecycle Capable | declared later-stage continuity |
| Suspended | no new dependent protected action |
| Retired | historical lineage only |

A Profile claim cannot exceed Pack Evidence.

## G.6 Required Jurisdiction and Service Evidence

Every declared combination identifies Pack ID/version, module, Support State, effective period, Sources/Rules, professional owner, applicant/owner types, routes, forms/Documents, fee units, Deadline Rules, provider/connector/manual route, scenario results, exclusions and suspension trigger.

A generic country form is insufficient.

## G.7 Commercial and Authority Evidence

Commercial Intake and later Profiles demonstrate immutable Quote versions, separated Official/Professional/Provider/Tax/Currency components, later-stage disclosure, discount/credit authority, client/internal visibility, fee-change behavior and payment/Approval separation.

Governed Filing additionally demonstrates duplicate-payment handling and that payment or Provider Report does not establish official acknowledgement.

Publication, pilot, release and implementation remain separate:

```text
Book publication
≠ implementation release
≠ production deployment
≠ External Protected Action authority
```

## G.8 Zero-Tolerance Rule

A Profile cannot pass if an applicable zero-tolerance scenario fails, including expired authority, wrong-version Approval, incomplete Review, provider over-access, unsupported official state, duplicate effect, unsafe retry, unverified Deadline conflict, silence treated as authority, private data over-transfer, wrong-organization access, AI current-rule claim without Sources, publication treated as production, support claim above Pack Evidence, hidden Margin or silent Rule/fee/form mutation.

## G.9 Profile Dependency Rule

Profiles are cumulative only where the journey consumes earlier capabilities. A Post-Filing edition may ingest an existing formal Matter without offering Guided Decision, but it must conform to Foundation and every earlier record, Approval, commercial or Execution contract it consumes.

Prior-stage records are declared as created by this edition, imported through Handoff, referenced from an Owning Service or unsupported.

## G.10 Conformance Review Record

A Profile review records:

- `MR-G10 Conformance Statement`;
- applicable scenario results;
- Pack/module Evidence;
- `MR-G08 Metric Definitions` and `MR-G09 Evaluation Records`;
- `MR-C11 Pilot Context` where applicable;
- `MR-D13 Pilot or Release Decision`;
- unresolved findings and exceptions;
- implementation, production and protected-action authority states.

## G.11 PF-06D Reconciliation State

```text
Profiles 1–8: PRESERVED
Current Specification versions: RECONCILED
MR-C12 applicant/authority coverage: ADDED
Scenario minimums and Pack limits: RECONCILED
Publication / implementation / production separation: RECONCILED
PF-08 validation: OPEN
```

Appendix G does not certify any implementation or authorize production or External Protected Action.
