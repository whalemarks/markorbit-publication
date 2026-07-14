# Appendix G — MarkReg Conformance Profiles

**Status:** Controlled Reader Draft — PF-04 Reconciled; PF-05 and PF-08 Evidence Pending  
**Primary sources:** CH46–CH47, B05-SPEC-0001 v0.2 and B05-SPEC-0003 v0.2  
**Reader purpose:** allow a Product edition or implementation to state honestly which MarkReg capabilities it supports and which tests are required.

## G.1 Conformance Rule

Not every implementation must launch the full lifecycle.

```text
partial scope + accurate profile statement
= permitted

partial scope + Full-Lifecycle claim
= non-conforming
```

A profile states tested Product behavior. It does not grant production or protected-action authority.

## G.2 Required Conformance Statement

A declaration must identify:

- Product and implementation version;
- supported profile or profiles;
- supported jurisdictions, services and proceeding types;
- relevant Jurisdiction Pack and Rule versions;
- supported applicant types and filing routes;
- participant surfaces;
- required Human roles and qualifications;
- Owning Service and Execution dependencies;
- provider and connector routes;
- excluded stages and known limitations;
- scenario, evaluation and validation status;
- production authority state;
- external protected-action authority state.

Marketing claims must not exceed this statement.

## G.3 Profile Inventory

### Profile 1 — Foundation

Minimum capability:

- MarkReg Product identity and non-goals;
- Books 01–04 authority boundaries;
- participant and AI role distinctions;
- Product, formal, Execution, provider and official-state distinctions;
- source, version, Review, approval and correction principles;
- organization and permission context.

This profile does not support a user-facing trademark service journey by itself.

**Minimum scenarios:** MR-SCN-01, 09, 10, 11, 18, 22, 35, 36, 40 and 41.

### Profile 2 — Guided Decision

Includes Foundation plus:

- Business Context and Need Brief;
- jurisdiction and route candidates;
- filing units and applicant context;
- classification and goods/services guidance;
- purpose-limited search and risk;
- Recommendation Set, Option Set and Proposal;
- Human correction and Review.

External filing is not supported.

**Minimum additional scenarios:** MR-SCN-02, 03, 04, 13 and 14.

### Profile 3 — Commercial Intake

Includes Guided Decision plus:

- transparent price basis and Quote;
- exact-version Client Acceptance;
- Commercial Instruction;
- Formal Intake and Requirement Set;
- dimensional Readiness Assessment;
- Handoff Envelope to formal work.

The profile may stop at governed Handoff.

**Minimum additional scenarios:** MR-SCN-05, 06, 07, 08, 15 and 28.

### Profile 4 — Filing Preparation

Includes Commercial Intake plus:

- Filing Package Candidate;
- source lineage and material diff;
- client factual confirmation;
- Professional Review;
- version-specific Filing Approval;
- provider Capability Need and route candidates.

Execution and official submission may remain outside scope.

**Minimum additional scenarios:** MR-SCN-16, 17, 18, 19 and 20.

### Profile 5 — Governed Filing

Includes Filing Preparation plus:

- Human route or provider Selection;
- appointment, instruction and Provider Acceptance;
- governed manual, provider or connector Execution;
- stable idempotency identity;
- sent, delivery, provider and official acknowledgement states;
- unknown state, reconciliation and duplicate safety;
- official evidence return.

The declaration must identify supported offices, providers and connectors.

**Minimum additional scenarios:** MR-SCN-21, 22, 23, 24 and 25.

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

The declaration must state supported proceeding types.

**Minimum additional scenarios:** MR-SCN-10, 23, 26, 27, 28 and 29.

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

One view must preserve independent right histories.

**Minimum additional scenarios:** MR-SCN-12, 30, 31, 32 and 33.

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

Full-Lifecycle does not mean every jurisdiction or proceeding is supported.

**Minimum additional scenarios:** MR-SCN-34 through MR-SCN-41, plus every applicable zero-tolerance scenario.

## G.4 Profile Evidence Matrix

| Evidence | Foundation | Guided Decision | Commercial Intake | Filing Preparation | Governed Filing | Post-Filing | Portfolio Continuity | Full-Lifecycle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| constitutional rules | required | required | required | required | required | required | required | required |
| artifact lineage | boundary level | recommendation | commercial | package and approval | Execution and evidence | event and response | right and obligation | complete |
| participant matrix | required | required | required | required | required | required | required | required |
| scenario evidence | constitutional | recommendation | intake and commercial | Review and approval | unknown and duplicate safety | event, deadline and Communication | renewal and ownership | all families |
| official evidence | none | none | none | none | required | required | required | required |
| jurisdiction evidence | boundary only | guidance rules | price and Intake rules | package rules | execution rules | proceeding rules | maintenance rules | all supported scope |
| metrics | boundary defects | user and recommendation | commercial and readiness | package quality | reliability and safety | deadline and Communication | lifecycle continuity | layered model |
| failure recovery | permission and correction | version change | expired Quote and payment | invalid approval | reconciliation and retry | corrected notice | owner and recordal conflict | complete |

## G.5 Zero-Tolerance Requirements

A profile cannot pass if an applicable zero-tolerance scenario fails.

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
- publication status treated as production authority.

## G.6 Profile Dependency Rule

Profiles are cumulative only where the declared service journey consumes the earlier capability.

A Post-Filing implementation may ingest an existing official Matter without offering Guided Decision to end users, but it must still conform to the Foundation rules and every earlier artifact, approval or Execution contract it consumes.

The declaration must state whether prior-stage records are:

- created by this Product edition;
- imported through a Handoff;
- referenced from an Owning Service;
- unsupported.

## G.7 Partial-Profile Example

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

- filing preparation and submission are outside scope;
- no official filing status is produced;
- professional and Owning Service Handoffs are required;
- applicable Foundation, Guided Decision and Commercial Intake scenarios pass.

It may not claim filing automation or Full-Lifecycle support.

## G.8 Full-Lifecycle Example

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

- which jurisdictions and service types are supported;
- which provider and connector routes are operational;
- where Human professional action is mandatory;
- which proceedings are excluded;
- which scenarios and Pack versions were tested;
- whether production and protected-action gates are approved separately.

## G.9 Upgrade Rule

```text
feature exists
≠ profile supported

feature exists
+ source, authority, failure and scenario evidence
→ profile candidate

profile candidate
+ controlled Review
→ declared support
```

Moving upward requires evidence for every added capability and applicable zero-tolerance scenario.

## G.10 Non-Conforming Claims

Examples include:

- global support from one generic country form;
- Full-Lifecycle claim where the Product stops at filing;
- official status without office evidence;
- autonomous professional advice without eligible Review;
- provider-network claim without appointment and acceptance controls;
- AI legal certainty from model confidence;
- publication RC status presented as production authority;
- hidden unsupported jurisdictions or excluded services;
- profile declaration without scenario results.

## G.11 PF-04 Scenario Matrix

| Profile | Core scenario range | Additional controls before RC1 |
| --- | --- | --- |
| Foundation | 01, 09–11, 18, 22, 35, 36, 40, 41 | PF-08 structural validation |
| Guided Decision | Foundation + 02–04, 13, 14 | PF-05 jurisdiction guidance evidence |
| Commercial Intake | Guided + 05–08, 15, 28 | PF-05 fee and commercial evidence |
| Filing Preparation | Commercial + 16–20 | package and approval validation |
| Governed Filing | Filing + 21–25 | supported route and official evidence |
| Post-Filing | relevant prior + 10, 23, 26–29 | proceeding-specific Pack evidence |
| Portfolio Continuity | relevant prior + 12, 30–33 | maintenance and recordal Pack evidence |
| Full-Lifecycle | all applicable scenarios | PF-05, PF-07 and PF-08 complete |

## G.12 Reconciliation Status

```text
Profile scope normalized: COMPLETE
Participant and surface requirements mapped: COMPLETE
Minimum MR-SCN sets assigned: COMPLETE
Zero-tolerance requirements assigned: COMPLETE
Partial-profile example: COMPLETE
Full-Lifecycle example: COMPLETE
PF-04 Appendix G work: COMPLETE
PF-05 jurisdiction and service evidence: PENDING
PF-07 publication integration: PENDING
PF-08 scenario and structural validation: PENDING
```

Appendix G is a controlled reader draft reconciled for PF-04. A profile becomes operationally meaningful only when its jurisdiction, service, validation and authority evidence also pass.