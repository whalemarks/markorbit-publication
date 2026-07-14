# Appendix G — MarkReg Conformance Profiles

**Status:** Controlled Scaffold — content completion pending PF-04, PF-05 and PF-08  
**Primary sources:** CH46–CH47 and the complete Book 05 manuscript  
**Reader purpose:** allow an edition or implementation to state honestly which MarkReg capabilities it supports.

## G.1 Conformance Rule

Not every implementation must launch the full lifecycle.

A partial implementation may conform if it declares its supported profile, exclusions, jurisdictions, services, Human roles and authority limits accurately.

```text
Partial scope + accurate conformance statement
= permitted

Partial scope + full-lifecycle marketing claim
= non-conforming
```

## G.2 Profile Inventory

### Profile 1 — Foundation

Minimum scope:

- MarkReg Product identity and non-goals;
- Books 01–04 authority boundaries;
- user, professional, provider and AI role distinctions;
- Product-local, formal, Execution and official state distinctions;
- source, version, Review and approval principles.

This profile does not by itself support a user-facing trademark service journey.

### Profile 2 — Guided Decision

Includes Foundation plus:

- Business Context and Need Brief;
- jurisdiction and route candidates;
- filing-unit candidates;
- applicant and authority context;
- classification and goods/services guidance;
- purpose-limited search and risk assessment;
- Recommendation Set, Option Set and Proposal;
- Human correction and professional Review where required.

External filing is not supported.

### Profile 3 — Commercial Intake

Includes Guided Decision plus:

- transparent price basis and Quote;
- exact-version Client Acceptance;
- Commercial Instruction;
- service-specific Formal Intake;
- Requirement Set;
- dimensional Readiness Assessment;
- Handoff Envelope to formal Order, Matter or professional work.

The profile may stop at governed Handoff.

### Profile 4 — Filing Preparation

Includes Commercial Intake plus:

- Filing Package Candidate;
- package source lineage and diff;
- client factual confirmation;
- Professional Review;
- version-specific Filing Approval;
- provider Capability Need and route candidates.

Execution and official submission may remain outside scope.

### Profile 5 — Governed Filing

Includes Filing Preparation plus:

- Human provider or route selection;
- appointment, instruction and Provider Acceptance;
- governed manual, provider or connector Execution route;
- stable idempotency identity;
- sent, delivery, provider and official acknowledgement states;
- failure, unknown state, reconciliation and duplicate safety;
- official evidence return.

The profile must declare supported offices, providers and connectors.

### Profile 6 — Post-Filing

Includes relevant earlier profiles plus selected:

- Official Event Snapshots;
- examination and Issue Sets;
- Response Strategy and Response Package;
- deadlines and client decisions;
- publication and opposition windows;
- adversarial or remedy contexts;
- governed response filing;
- Outcome Snapshot and corrected Communication.

The implementation must state which proceeding types are supported.

### Profile 7 — Portfolio Continuity

Includes relevant earlier profiles plus:

- Registration Outcome and Right Baseline;
- certificate and official-record distinctions;
- Maintenance Obligation Sets;
- renewal packages;
- changes and recordals;
- assignment, licensing and chain of title;
- use evidence and vulnerability;
- portfolio continuity views and action plans.

One portfolio view must preserve independent jurisdiction and right histories.

### Profile 8 — Full-Lifecycle

Includes Profiles 1–7 plus:

- cross-stage artifact and state continuity;
- standalone, Lite, Workplace and cross-Product surfaces;
- participant-specific visibility and action rights;
- governed Jurisdiction Pack and Rule versioning;
- Pack-bound AI assistance;
- quality, safety and lifecycle metrics;
- pilot, stop, rollback and evolution controls;
- complete conformance and correction behavior.

Full-Lifecycle does not mean every jurisdiction or every proceeding is supported.

## G.3 Required Conformance Statement

A Product edition or implementation should publish:

- Product name and version;
- supported profile or profiles;
- supported jurisdictions and services;
- relevant Jurisdiction Pack versions;
- supported applicant types and routes;
- participant surfaces;
- required Human roles and qualifications;
- Owning Service and Execution dependencies;
- provider and connector routes;
- excluded lifecycle stages;
- known limitations;
- scenario and evaluation status;
- production authority state;
- external protected-action authority state.

## G.4 Profile Evidence Matrix

| Evidence | Foundation | Guided Decision | Commercial Intake | Filing Preparation | Governed Filing | Post-Filing | Portfolio Continuity | Full-Lifecycle |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| constitutional rules | required | required | required | required | required | required | required | required |
| artifact lineage | basic | recommendation | commercial | package and approval | execution and evidence | event and response | right and obligation | complete |
| Human authority matrix | required | required | required | required | required | required | required | required |
| jurisdiction-pack evidence | not necessarily | required for guidance | required for price and intake | required for package | required for execution | required for proceeding | required for maintenance | complete supported scope |
| conformance scenarios | constitutional | recommendation | intake and commercial | Review and approval | failure and duplicate safety | deadline and official event | renewal and ownership | all priority families |
| official evidence | none | none | none | none | required | required | required | required |
| metrics and evaluation | boundary checks | user and recommendation | commercial and readiness | package quality | reliability and safety | outcome communication | lifecycle continuity | complete layered model |

## G.5 Non-Conforming Claims

Examples include:

- claiming global support from one generic country form;
- claiming Full-Lifecycle when the Product stops at filing;
- claiming official status without sourced office evidence;
- claiming automatic professional advice without eligible Review;
- claiming provider-network support without appointment and acceptance controls;
- claiming AI legal certainty from model confidence;
- treating publication status as production authority;
- hiding unsupported jurisdictions or excluded services.

## G.6 Upgrade Rule

Moving from one profile to another requires evidence for the added capabilities.

```text
feature exists
≠ profile supported

feature exists
+ authority, source, failure, scenario and operational evidence
→ profile candidate

profile candidate
+ controlled review
→ declared support
```

## G.7 Completion Work

PF-04, PF-05 and PF-08 must:

1. map each profile to controlled artifacts, states and scenarios;
2. define minimum jurisdiction and service evidence;
3. identify zero-tolerance failures;
4. create a conformance checklist suitable for RC1 and later implementation projects;
5. verify that publication and marketing claims cannot exceed declared support;
6. test at least one partial-profile and one Full-Lifecycle conformance example.

This appendix becomes publication-ready only after the conformance checklist and structural validation pass.