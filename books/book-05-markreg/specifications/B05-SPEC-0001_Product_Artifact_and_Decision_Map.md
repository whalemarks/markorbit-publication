# B05-SPEC-0001 — MarkReg Product Artifact and Decision Map

## Status

- **Status:** Controlled Specification v0.3 — PF-06D Whole-Book Reconciled
- **Applies to:** Book 05 CH07–CH47; Parts I–VII
- **Authority:** Book 05 Product specification
- **Supersedes:** Controlled Specification v0.2
- **Publication projections:** Appendix A and the state/authority portions of Appendix B
- **PF-06D change:** registers `MR-C12 Applicant and Authority Context` and reconciles the complete record range.

## 1. Purpose and Boundary

This specification defines the canonical MarkReg Product-local Artifacts, Contexts, Decisions, Evidence records, Baselines, Views and Governance records.

It does not redefine Core Objects, formal Order or Matter records, shared Document, Review, Approval, Communication or financial records, Book 03 Execution, provider systems, official records or Owning Service authority.

## 2. Constitutional Rules

| Rule ID | Rule |
| --- | --- |
| MR-CR-01 | Recommendation is not Decision. |
| MR-CR-02 | Product readiness is not Approval. |
| MR-CR-03 | Approval is not Execution. |
| MR-CR-04 | Submission is not official acknowledgement. |
| MR-CR-05 | Product projection is not Official Truth without source Evidence. |
| MR-CR-06 | AI Assistance never replaces accountable Human Review. |
| MR-CR-07 | Product-local records do not silently become formal shared objects. |
| MR-CR-08 | Every material record has source lineage, version identity, responsibility and supersession rules. |

## 3. Record Classes

| Prefix | Class |
| --- | --- |
| `MR-A` | Product Artifact |
| `MR-C` | scoped Context |
| `MR-D` | accountable Decision |
| `MR-E` | Evidence or source-backed record |
| `MR-B` | Baseline or obligation record |
| `MR-V` | View or Projection |
| `MR-G` | Governance and configuration record |

The prefix describes Product meaning. It does not grant authority.

## 4. Canonical Lineages

### 4.1 New filing

```text
MR-A01 Business Context Snapshot
→ MR-A02 Need Brief
→ MR-A03 Recommendation Set
→ MR-A04 Option Set
→ MR-C12 Applicant and Authority Context where identity or authority is material
→ MR-A05 Proposal
→ MR-A06 Quote
→ MR-D01 Client Acceptance
→ MR-A07 Commercial Instruction
→ MR-A08 Formal Intake
→ MR-A09 Requirement Set
→ MR-A10 Readiness Assessment
→ MR-A12 Handoff Envelope
→ MR-A11 Filing Package Candidate
→ MR-D02 Professional Decision
→ MR-D03 Filing Approval
→ MR-A16 Provider Instruction or MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-E05 Official Event Snapshot
→ MR-B01 Right Baseline or another sourced outcome
```

### 4.2 Examination and response

```text
MR-E05 Official Event Snapshot
→ MR-C03 Examination Context
→ MR-A19 Issue Set
→ MR-A20 Response Option Set
→ MR-D06 Response Strategy Decision
→ MR-A21 Response Strategy
→ MR-A22 Response Package Candidate
→ MR-D03 Filing Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-V02 Outcome Snapshot
```

### 4.3 Publication and adversarial work

```text
MR-E05 Official Event Snapshot
→ MR-C04 Publication Window Context
→ MR-C05 Adversarial Context
→ MR-A23 Evidence Plan
→ MR-A24 Adversarial Package Candidate
→ MR-D07 Adversarial or Settlement Decision
→ MR-D03 Filing Approval where protected filing follows
→ later MR-E05 Official Event Snapshots
→ MR-C06 Remedy Context where needed
→ MR-V02 Outcome Snapshot
```

### 4.4 Renewal

```text
MR-B01 Right Baseline
→ MR-B02 Maintenance Obligation Set
→ MR-A10 Readiness Assessment
→ MR-A26 Renewal Package Candidate
→ MR-D08 Renewal Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-E09 Official Update Evidence
→ updated MR-B01 Right Baseline
```

### 4.5 Recordal and transaction

```text
MR-B01 Right Baseline
→ MR-C07 Recordal Context or MR-C08 Transaction Context
→ MR-A28 Affected-Right Set
→ MR-V03 Chain-of-Title View
→ MR-A27 Recordal Package Candidate
→ MR-D09 Recordal Approval
→ MR-A17 Execution Request
→ MR-E09 Official Update Evidence
→ updated MR-B01 Right Baseline and MR-V03 Chain-of-Title View
```

### 4.6 Portfolio and cross-Product

```text
independent MR-B01 Right Baselines
+ MR-B02 Maintenance Obligation Sets
+ sourced lifecycle records
→ MR-V04 Portfolio Continuity View
→ MR-A29 Portfolio Action Plan
→ service-specific accountable Decisions
→ MR-A12 Handoff Envelope
→ MR-C10 Product Session
→ MR-A30 Return Envelope
```

## 5. Product Artifact Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-A01 | Business Context Snapshot | business, brand, market, timing, budget, risk and organization context |
| MR-A02 | Need Brief | the problem and intended protection before formal filing data |
| MR-A03 | Recommendation Set | jurisdiction, route, filing-unit, class, scope, search, timing and risk recommendations |
| MR-A04 | Option Set | alternatives, trade-offs, exclusions, cost and next actions |
| MR-A05 | Proposal | recommended service configuration and alternatives |
| MR-A06 | Quote | versioned priced scope, validity, currency, tax and later-stage fees |
| MR-A07 | Commercial Instruction | authorized request to proceed within accepted commercial scope |
| MR-A08 | Formal Intake | service-specific facts for professional preparation |
| MR-A09 | Requirement Set | documents, signatures, evidence, deadlines and jurisdiction conditions |
| MR-A10 | Readiness Assessment | purpose-specific structural, commercial, professional, document, payment, approval and execution readiness |
| MR-A11 | Filing Package Candidate | exact version proposed for filing |
| MR-A12 | Handoff Envelope | typed transfer of versions, responsibilities, warnings, deadlines and expected return evidence |
| MR-A13 | Lifecycle Projection | user-facing lifecycle summary derived from controlled source records |
| MR-A14 | Routing Recommendation | comparison of eligible provider or execution-route candidates |
| MR-A15 | Provider Appointment Candidate | proposed provider engagement scope and authority basis |
| MR-A16 | Provider Instruction | bounded approved task sent to an appointed provider |
| MR-A17 | Execution Request | request for governed protected action through Book 03 or an execution-capable service |
| MR-A18 | Recovery and Reconciliation Plan | investigation and correction plan for unknown, partial, rejected or conflicting effects |
| MR-A19 | Issue Set | separately scoped examination or official-notice issues |
| MR-A20 | Response Option Set | response alternatives, amendments, evidence, cost and consequences |
| MR-A21 | Response Strategy | selected professional approach to each issue |
| MR-A22 | Response Package Candidate | arguments, amendments, evidence, forms and instructions proposed for response filing |
| MR-A23 | Evidence Plan | facts to prove, evidence sources, owners, periods, gaps and admissibility concerns |
| MR-A24 | Adversarial Package Candidate | pleading, defense, opposition, appeal or cancellation materials |
| MR-A25 | Communication Packet | purpose-limited reviewed status, decision or outcome communication |
| MR-A26 | Renewal Package Candidate | verified right, scope, owner, fee, document and route details for renewal |
| MR-A27 | Recordal Package Candidate | current and proposed official data, documents and affected rights for recordal |
| MR-A28 | Affected-Right Set | independent rights included, excluded or unresolved in a change or transaction |
| MR-A29 | Portfolio Action Plan | prioritized filing, maintenance, renewal, evidence, recordal, monitoring and non-renewal actions |
| MR-A30 | Return Envelope | typed idempotent outcome, blocker, reference and next-action return |

## 6. Scoped Context Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-C01 | Capability Need | jurisdiction, service, deadline, language, qualification, conflict and relationship constraints |
| MR-C02 | Reconciliation Context | expected result, attempt identity, evidence and duplicate-risk scope |
| MR-C03 | Examination Context | official notice, affected scope, deadline, source and professional responsibility |
| MR-C04 | Publication Window Context | publication event, challenge window, source and monitoring uncertainty |
| MR-C05 | Adversarial Context | parties, grounds, affected rights, procedure, authority, cost and settlement scope |
| MR-C06 | Remedy Context | appeal, review, correction, restoration, cancellation or invalidation scope |
| MR-C07 | Recordal Context | current official data, proposed change and affected jurisdictions |
| MR-C08 | Transaction Context | assignment, merger, succession or other transaction parties, rights, dates and effects |
| MR-C09 | Licence Context | licensed rights, scope, territory, term, quality control, use evidence and termination |
| MR-C10 | Product Session | actor, role, organization, entry mode, step, visible versions, warnings, pause and return route |
| MR-C11 | Pilot Context | edition, organizations, users, services, jurisdictions, fallback and stop conditions |
| MR-C12 | Applicant and Authority Context | proposed applicant, ownership rationale, instructor, signatory, payer, authority source and conflicts |

## 7. Evidence and Source-Backed Record Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-E01 | Submission Evidence | what was sent, when, through which route and under which attempt identity |
| MR-E02 | Delivery Evidence | technical delivery or transmission result |
| MR-E03 | Provider Report | provider-reported receipt, acceptance, filing or outcome |
| MR-E04 | Official Acknowledgement Evidence | official receipt, filing number, acceptance, rejection or procedural acknowledgement |
| MR-E05 | Official Event Snapshot | sourced official notice, status, publication, decision or event at a retrieval time |
| MR-E06 | Deadline Record | official date, calculation basis, uncertainty, internal target, extension and responsibility |
| MR-E07 | Source Record | authority, publication/effective date, retrieval, language, immutable reference and supersession |
| MR-E08 | Registration Outcome Record | official registered scope, owner, number, date, limitations and certificate relationship |
| MR-E09 | Official Update Evidence | verified renewal, recordal, correction, cancellation, expiry or other official update |

## 8. Baseline and Obligation Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-B01 | Right Baseline | reviewed operational baseline for one independent application or registration |
| MR-B02 | Maintenance Obligation Set | sourced duties, calculated dates, internal targets, evidence needs and responsibility |
| MR-B03 | Use-Evidence Coverage Record | goods/services, territory, period, owner/licensee, sources and gaps |
| MR-B04 | Provider Capability Evidence Record | service, jurisdiction, qualification, experience, recency, relationship and limits |

## 9. View and Projection Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-V01 | Filing and Scope Diff View | recommended, approved, acknowledged and registered scope comparison |
| MR-V02 | Outcome Snapshot | sourced procedural outcome, interpretation, consequence and next action |
| MR-V03 | Chain-of-Title View | applicant, owners, transactions, recordals, gaps and proposed owner |
| MR-V04 | Portfolio Continuity View | independent rights, stages, obligations, evidence and risks without merged legal state |
| MR-V05 | Participant Surface Projection | role- and purpose-limited fields and actions |

## 10. Governance and Configuration Register

| ID | Record | Controlled meaning |
| --- | --- | --- |
| MR-G01 | Jurisdiction Pack | jurisdiction-, service- and stage-specific sources, rules, forms, fees and Product behavior |
| MR-G02 | Rule Record | one sourced operational rule, conditions, exceptions, status, owner and tests |
| MR-G03 | Pack Version Record | coherent reviewed source, rule, form, fee and migration version |
| MR-G04 | Rule Change Candidate | detected change, evidence, impact, urgency and verification |
| MR-G05 | Organization Overlay | private review, provider, commercial, deadline and communication policy |
| MR-G06 | AI Task Context | model purpose, inputs, Pack version, sources, confidentiality and prohibited conclusions |
| MR-G07 | AI Output Record | material AI output basis, model/time, sources, uncertainty and Human disposition |
| MR-G08 | Metric Definition | metric purpose, owner, source, calculation, segmentation, limitation and decision use |
| MR-G09 | Evaluation Record | evaluation set, expected behavior, result, reviewer and limitations |
| MR-G10 | Conformance Statement | supported profile, jurisdictions, services, participants, dependencies, exclusions and validation |

## 11. Accountable Decision Register

| ID | Decision | Accountable actor | Exact scope | Does not equal |
| --- | --- | --- | --- | --- |
| MR-D01 | Client Acceptance | authorized client actor | exact Quote version and commercial scope | payment, changed scope or filing |
| MR-D02 | Professional Decision | eligible professional | recommendation, readiness, evidence, strategy or override | client authority or Execution |
| MR-D03 | Filing Approval | authorized Human role | exact package, jurisdiction, route, purpose and expiry | Execution or official filing |
| MR-D04 | Human Selection | authorized organization actor | selected provider or route | appointment, instruction or acceptance |
| MR-D05 | Provider Acceptance | appointed provider | accepted engagement, scope, fee and deadline | official submission or office acceptance |
| MR-D06 | Response Strategy Decision | eligible professional plus client where needed | selected response, amendment, evidence and consequence | Response Filing Approval |
| MR-D07 | Adversarial or Settlement Decision | authorized client and eligible professional roles | pleading, defense, withdrawal, limitation, settlement or remedy authority | signed settlement, filing or official closure |
| MR-D08 | Renewal Approval | authorized owner/client and organization role | exact right, scope, owner, package, fee, route and timing | filed renewal or renewed right |
| MR-D09 | Recordal Approval | authorized client/owner and organization role | exact change, rights, documents, jurisdictions and route | signed transaction or official update |
| MR-D10 | Non-Renewal Decision | authorized owner/client role | one identified right and understood consequence | official lapse before it occurs |
| MR-D11 | Communication Approval | authorized reviewer or sender | exact recipients, purpose, language, attachments and version | delivery, acknowledgement or official outcome |
| MR-D12 | Pack Release Approval | accountable professional owner | exact Pack version and effective scope | legal enactment or official publication |
| MR-D13 | Pilot or Release Decision | authorized Product/publication reviewer | profile, scope, evidence, exceptions and stop conditions | production or protected-action authority unless separately granted |

## 12. `MR-C12` Registration Decision

`Applicant and Authority Context` is canonical because it carries independent responsibility, source conflict, Human Decision, downstream invalidation and cross-stage lineage.

It records, as applicable:

- proposed applicant and stable reference;
- legal identity, entity type, address and jurisdiction;
- ownership rationale and relationship to the brand;
- existing portfolio-owner comparison;
- instructor, signatory and payer identities;
- authority source, scope, validity and conflicts;
- client confirmation and Professional Decision;
- affected Requirements, Packages, Approvals and later recordal risks.

`MR-C12` does not create or modify an official owner, applicant, Organization, Client, Matter or representative appointment.

`MR-C01` remains exclusively `Capability Need`.

## 13. Formal and External Objects Not Owned by MarkReg

MarkReg may reference but does not own:

- Core Organization, User, Client, Contact, Brand and Trademark Objects;
- formal Order, Matter, Task, Workflow and responsibility records;
- formal Document, Evidence, Review, Approval, Communication, payment, invoice and refund records;
- Book 03 Execution Context, attempt, idempotency, Event and failure state;
- provider identity, appointment, invoice and provider-system records;
- official applications, registrations, proceedings, laws, forms, fees, notices and register records.

## 14. Version, Supersession and Change Propagation

Every material record retains stable ID, version, purpose, scope, source references, responsible actor, Review, Decision or Approval state, validity, supersession, affected rights and downstream references.

A changed upstream value does not silently mutate an accepted Quote, approved Package, formal Order or Matter, provider instruction, Execution attempt, official record or sent Communication.

Minimum propagation includes:

| Change | Minimum response |
| --- | --- |
| applicant, owner, instructor or signatory | update `MR-C12`; invalidate affected authority, Requirements, Packages, Approvals and recordal assumptions |
| jurisdiction or route | regenerate Pack, provider, fee, form, Document, timing and readiness dependencies |
| mark or scope | re-evaluate filing units, search, class, wording, fee, Package and Approval |
| fee, form or Rule | identify affected draft, accepted and approved records and apply explicit variance or revalidation |
| corrected official event | preserve both versions; update Context, Deadline and affected strategy or Communication |
| Package after Approval | invalidate exact-version Approval and block Execution |
| provider material change | create a new candidate or instruction version |
| unknown external effect | open `MR-C02`; block unsafe retry |
| official owner or right state | update verified Baseline and linked obligations without rewriting history |
| permission, organization or purpose | re-evaluate visibility, Handoff, Session and Return scope |

## 15. Service-Family Conformance

A supported service family defines entry conditions, minimum source facts, canonical records, Pack dependencies, Human Review and Decision gates, formalization and Execution route, provider and official Evidence, failure and correction behavior, outcome mapping, future obligations, participant rights and observable scenarios.

A page, form, fee table, AI prompt, provider listing or reminder alone is not service-family support.

## 16. Appendix Projection Contract

Appendix A and Appendix B must retain controlled IDs and record classes, preserve source and authority boundaries, distinguish Product-local, formal, Execution, provider and official state, and avoid introducing an unregistered canonical record.

Where a projection conflicts with this specification, this specification controls until reviewed correction.

## 17. PF-06D Completion State

```text
Applies through CH47: YES
MR-A01–MR-A30: RECONCILED
MR-C01–MR-C12: RECONCILED
MR-D01–MR-D13: RECONCILED
MR-E01–MR-E09: RECONCILED
MR-B01–MR-B04: RECONCILED
MR-V01–MR-V05: RECONCILED
MR-G01–MR-G10: RECONCILED
MR-C12 Applicant and Authority Context: REGISTERED
Architecture Canon or Books 02–04 amendment required: NO
```

This specification does not authorize implementation, production deployment or External Protected Action.
