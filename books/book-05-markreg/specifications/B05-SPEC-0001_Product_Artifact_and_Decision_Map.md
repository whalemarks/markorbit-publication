# B05-SPEC-0001 — MarkReg Product Artifact and Decision Map

## Status

- **Status:** Controlled Specification v0.2 — Full-Lifecycle Reconciled
- **Applies to:** Book 05 CH07–CH47; Parts I–VII
- **Authority:** Book 05 Product specification
- **Supersedes:** B05-SPEC-0001 Controlled Draft limited to Parts I–IV
- **Publication projections:** Appendix A and the PF-02 portion of Appendix B

## 1. Purpose

This specification defines the canonical MarkReg Product-local artifacts, contexts, evidence records, baselines, views, governance records and accountable decisions used across the full trademark lifecycle.

It establishes:

- controlled identifiers;
- purpose and owner;
- source inputs;
- Review and approval requirements;
- version and supersession behavior;
- formalization targets;
- downstream consumers;
- state and authority boundaries.

It does not redefine Core Objects, formal Order or Matter records, shared Document or Review records, Book 03 Execution state, provider systems, official records, or Owning Service authority.

## 2. Constitutional Rules

| Rule ID | Rule |
| --- | --- |
| MR-CR-01 | Recommendation is not Decision. |
| MR-CR-02 | Product readiness is not approval. |
| MR-CR-03 | Approval is not execution. |
| MR-CR-04 | Submission is not official acknowledgement. |
| MR-CR-05 | Product projection is not official truth without source evidence. |
| MR-CR-06 | AI assistance never replaces accountable Human Review. |
| MR-CR-07 | Product-local records do not silently become formal shared objects. |
| MR-CR-08 | Every material record has source lineage, version identity, responsibility and supersession rules. |

These eight rules remain unchanged. Later chapters and appendices may explain them but may not weaken them.

## 3. Controlled Record Classes

| Prefix | Class | Meaning | Examples |
| --- | --- | --- | --- |
| `MR-A` | Product artifact | versioned work product prepared or presented by MarkReg | Need Brief, Quote, Filing Package Candidate |
| `MR-C` | scoped context | bounded facts, purpose and participants for a journey or proceeding | Examination Context, Recordal Context |
| `MR-D` | accountable decision | Human or accepted external choice with stated authority and scope | Client Acceptance, Filing Approval |
| `MR-E` | evidence or source-backed record | evidence of a source, transmission, official event or calculation basis | Submission Evidence, Official Event Snapshot |
| `MR-B` | baseline or obligation record | reviewed continuing state used for future lifecycle work | Right Baseline, Maintenance Obligation Set |
| `MR-V` | view or projection | derived, purpose-specific presentation that does not own formal truth | Lifecycle Projection, Portfolio Continuity View |
| `MR-G` | governance and configuration record | controlled rule, Pack, AI, metric, evaluation or conformance record | Rule Record, Metric Definition |

The class indicates Product meaning. It does not grant authority.

## 4. Canonical Journey Lineages

### 4.1 New Filing Journey

```text
MR-A01 Business Context Snapshot
→ MR-A02 Need Brief
→ MR-A03 Recommendation Set
→ MR-A04 Option Set
→ MR-A05 Proposal
→ MR-A06 Quote
→ MR-D01 Client Acceptance
→ MR-A07 Commercial Instruction
→ MR-A08 Formal Intake
→ MR-A09 Requirement Set
→ MR-A10 Readiness Assessment
→ MR-A12 Handoff Envelope
→ MR-A11 Filing Package Candidate
→ MR-D02 Professional Decision / Review result
→ MR-D03 Filing Approval
→ MR-A16 Provider Instruction or MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-E05 Official Event Snapshot
→ MR-B01 Right Baseline or another sourced outcome
```

### 4.2 Examination and Response Journey

```text
MR-E05 Official Event Snapshot
→ MR-C03 Examination Context
→ MR-A19 Issue Set
→ MR-A20 Response Option Set
→ MR-A21 Response Strategy
→ MR-D06 Response Strategy Decision
→ MR-A22 Response Package Candidate
→ MR-D03 Filing Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ MR-V02 Outcome Snapshot
```

### 4.3 Publication and Adversarial Journey

```text
MR-E05 Official Event Snapshot
→ MR-C04 Publication Window Context
→ MR-C05 Adversarial Context
→ MR-A23 Evidence Plan
→ MR-A24 Adversarial Package Candidate
→ MR-D07 Adversarial or Settlement Decision
→ MR-D03 Filing Approval where a protected filing follows
→ MR-E05 later Official Event Snapshots
→ MR-C06 Remedy Context where needed
→ MR-V02 Outcome Snapshot
```

### 4.4 Renewal Journey

```text
MR-B01 Right Baseline
→ MR-B02 Maintenance Obligation Set
→ MR-A10 Readiness Assessment
→ MR-A26 Renewal Package Candidate
→ MR-D08 Renewal Approval
→ MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E04 Official Acknowledgement Evidence
→ updated MR-B01 Right Baseline
```

### 4.5 Recordal and Transaction Journey

```text
MR-B01 Right Baseline
→ MR-C07 Recordal Context or MR-C08 Transaction Context
→ MR-A28 Affected-Right Set
→ MR-V03 Chain-of-Title View
→ MR-A27 Recordal Package Candidate
→ MR-D09 Recordal Approval
→ MR-A17 Execution Request
→ MR-E04 Official Acknowledgement Evidence
→ updated MR-B01 Right Baseline and MR-V03 Chain-of-Title View
```

### 4.6 Portfolio and Cross-Product Journey

```text
independent MR-B01 Right Baselines
+ MR-B02 Maintenance Obligation Sets
+ sourced lifecycle records
→ MR-V04 Portfolio Continuity View
→ MR-A29 Portfolio Action Plan
→ accountable service-specific Decisions
→ typed MR-A12 Handoff Envelope
→ MR-C10 Product Session
→ MR-A30 Return Envelope
```

Not every journey uses every record. A service may enter later in the lifecycle, but equivalent source, version, responsibility, Review, approval, execution and evidence boundaries remain mandatory.

## 5. Product Artifact Register

| ID | Artifact | Purpose | Product owner | Source inputs | Review / approval | Supersession | Formalization target / main consumers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MR-A01 | Business Context Snapshot | Capture business, brand, market, timing, budget, risk and organization context. | Product journey | authorized Workplace and user facts | user correction; professional Review when material | new snapshot on material change | none; Need Brief and Recommendation Set |
| MR-A02 | Need Brief | State the problem before requesting formal filing data. | Product journey | MR-A01 and user answers | user confirmation or professional correction | newer confirmed version | none; Recommendation Set and Proposal |
| MR-A03 | Recommendation Set | Record jurisdiction, route, filing-unit, class, goods/services, search, timing and risk recommendations. | Product journey | Need Brief, Pack rules and portfolio context | accountable professional Review for material advice | versioned; prior versions retained | selected scope may later formalize; Option Set and Intake |
| MR-A04 | Option Set | Present alternatives, trade-offs, exclusions, estimated consequences and next actions. | Product journey | Recommendation Set and price inputs | professional or commercial Review as required | replaced when scope, fees or assumptions change | none; Proposal and user selection |
| MR-A05 | Proposal | Explain recommended service configuration and alternatives. | Product journey | Option Set | internal commercial and professional Review | revised Proposal | may lead to Quote; client and professional |
| MR-A06 | Quote | State priced scope, validity, currency, tax, inclusions, exclusions, later-stage fees and payment terms. | commercial Product surface | approved price components | commercial approval under organization policy | expires or is replaced | Order pricing terms; client, finance and sales |
| MR-A07 | Commercial Instruction | Record the authorized request to proceed within accepted commercial scope. | Product journey | Client Acceptance, payment terms and authority context | authorized client or organization actor | explicit change only | Order or Matter trigger candidate; operations and finance |
| MR-A08 | Formal Intake | Collect service-specific facts for professional preparation. | Product journey | confirmed recommendations, client facts and reused context | user completion and professional validation | versioned on material fact change | formal facts through Owning Services; preparation team |
| MR-A09 | Requirement Set | Define documents, signatures, translations, certification, originals, evidence, deadlines and jurisdiction conditions. | Product journey | Intake and active Jurisdiction Pack | professional Review where required | re-evaluated on rule or fact change | Document and Task requirements; user and coordinator |
| MR-A10 | Readiness Assessment | Evaluate structural, commercial, professional, documentary, payment, approval and execution readiness. | Product journey | Intake, Requirements, payment and Review state | named reviewer for overrides | expires on source, fee, rule or fact change | gate evidence; user, professional and Execution |
| MR-A11 | Filing Package Candidate | Assemble the exact version proposed for filing. | Product journey | approved Intake, Documents and Requirements | Professional Review, client confirmation and Filing Approval as applicable | new version on material change | formal Filing Package or Document references; approver and Execution |
| MR-A12 | Handoff Envelope | Carry stable references, approved versions, warnings, responsibilities, deadlines and expected return evidence across boundaries. | Product journey | accepted commercial and professional records | handoff validation | new envelope for changed purpose or version | Order, Matter, Execution, Workplace or another Product |
| MR-A13 | Lifecycle Projection | Present a user-facing lifecycle summary derived from controlled source records. | Product experience | Evidence, Baselines, Contexts and Views | interpretation Review where material | newer projection; prior communication retained where sent | explanatory only; client and professional surfaces |
| MR-A14 | Routing Recommendation | Compare eligible private-first provider or route candidates. | Product journey | MR-C01 Capability Need and provider evidence | Human Review under organization policy | refreshed on evidence, conflict, availability or scope change | Human Selection; authorized organization actor |
| MR-A15 | Provider Appointment Candidate | Prepare the proposed engagement scope and authority basis. | Product journey | Human Selection, approved scope and commercial terms | organization and professional checks | replaced before appointment if scope changes | provider appointment through owning relationship service |
| MR-A16 | Provider Instruction | Carry the bounded approved task to an appointed provider. | Product journey | appointment, exact package version and approval | governed instruction authority | corrected or superseded instruction retained | provider engagement; provider and coordinator |
| MR-A17 | Execution Request | Request a protected action through Book 03 Execution or an execution-capable service. | Product journey | active approval, route, idempotency key and package references | Execution entry validation | new request only for changed purpose or safe retry identity | Book 03 Execution; Execution service and audit |
| MR-A18 | Recovery and Reconciliation Plan | Define how an unknown, partial, rejected or conflicting execution result will be investigated and corrected. | Product journey with Execution | failure evidence and expected result | accountable operational or professional Review | closes or is replaced on new evidence | reconciliation Tasks and Communications |
| MR-A19 | Issue Set | Extract and separately scope examination or official-notice issues. | Product journey | Official Event Snapshot and notice evidence | eligible professional verification | revised when notice or interpretation changes | Response Option Set and strategy |
| MR-A20 | Response Option Set | Present response alternatives, amendments, evidence needs, cost and consequences. | Product journey | Issue Set, Pack rules and professional analysis | professional Review | revised with new facts, rules or authority | client and professional decision support |
| MR-A21 | Response Strategy | Define the selected professional approach to each issue. | eligible professional within Product journey | Response Option Set, evidence and client instructions | professional authorship; client decision where required | new strategy version on material change | Response Package and Matter strategy reference |
| MR-A22 | Response Package Candidate | Assemble arguments, amendments, evidence, forms and instructions for a response filing. | Product journey | Response Strategy, evidence and Requirements | Professional Review, client confirmation and Filing Approval | material change invalidates prior approval | formal response Documents and Execution request |
| MR-A23 | Evidence Plan | Define facts to prove, evidence sources, owners, periods, gaps and admissibility concerns. | professional Product surface | proceeding context and existing evidence | eligible professional Review | revised as scope or evidence changes | evidence collection Tasks and Adversarial Package |
| MR-A24 | Adversarial Package Candidate | Assemble pleading, defense, observation, opposition, appeal or cancellation materials. | Product journey | Adversarial or Remedy Context, strategy and Evidence Plan | Professional Review, client authority and Filing Approval | material change creates new version | formal proceeding Documents and Execution request |
| MR-A25 | Communication Packet | Prepare a purpose-limited, reviewed status, decision or outcome communication. | Product journey | source records, decision records and recipient context | Communication Review where required | corrected communication links to prior version | formal Communication through Owning Service |
| MR-A26 | Renewal Package Candidate | Assemble verified right, scope, owner, fee, document and route details for renewal. | Product journey | Right Baseline, Maintenance Obligations and active Pack | professional, client, finance and approval gates as applicable | updated on right, fee, owner or rule change | formal renewal Documents and Execution request |
| MR-A27 | Recordal Package Candidate | Assemble current and proposed official data, supporting documents and affected rights for recordal. | Product journey | Recordal or Transaction Context, Chain-of-Title View and Requirements | professional and authority Review; Recordal Approval | updated on party, right, document or rule change | formal recordal Documents and Execution request |
| MR-A28 | Affected-Right Set | Identify independent rights included, excluded or unresolved in a transaction or change initiative. | Product journey | official records, transaction facts and client instruction | professional and client confirmation | revised when scope or official data changes | Recordal Packages, pricing and portfolio views |
| MR-A29 | Portfolio Action Plan | Prioritize filing, maintenance, renewal, evidence, recordal, monitoring and non-renewal actions. | Product journey | Portfolio Continuity View, client strategy and constraints | professional and client decisions per action | versioned planning horizon | service-specific journeys and Handoff Envelopes |
| MR-A30 | Return Envelope | Return typed outcomes, blockers, references and next actions to Lite, Workplace or another Product. | Product journey | completed or paused Product Session and controlled records | return validation and permission check | idempotent return identity; newer return version if changed | calling Product or Workplace |

## 6. Scoped Context Register

| ID | Context | Purpose | Required scope and source | Main consumers |
| --- | --- | --- | --- | --- |
| MR-C01 | Capability Need | Define jurisdiction, service, deadline, language, qualification, conflict and relationship constraints before provider discovery. | Product need, approved scope and organization policy | Routing Recommendation and MGSN/private network query |
| MR-C02 | Reconciliation Context | Bound investigation of a technical, provider, payment or official-state uncertainty. | expected result, attempt identity, evidence and duplicate-risk scope | Recovery Plan, Execution and audit |
| MR-C03 | Examination Context | Bind an official notice, affected filing scope, deadline, source and professional responsibility. | Official Event Snapshot and Matter references | Issue Set and Response Strategy |
| MR-C04 | Publication Window Context | Represent publication event, challenge type, verified opening/closing basis and watch uncertainty. | official publication evidence and Pack rules | monitoring, Deadline Record and client Communication |
| MR-C05 | Adversarial Context | Define parties, role, grounds, affected rights, procedure, authority, costs and settlement scope. | official proceeding evidence, client and professional facts | Evidence Plan, Adversarial Package and decisions |
| MR-C06 | Remedy Context | Bound appeal, review, correction, restoration, cancellation or invalidation route without creating a general litigation Product. | official outcome, standing, grounds, deadline and Pack version | Remedy options, client decision and package preparation |
| MR-C07 | Recordal Context | Define current official data, proposed change, affected jurisdictions and required official updates. | Right Baseline, official records and client facts | Affected-Right Set and Recordal Package |
| MR-C08 | Transaction Context | Define assignment, merger, licence or other transaction parties, rights, dates, documents and intended effects. | transaction documents, party authority and official records | Chain-of-Title View and Recordal Context |
| MR-C09 | Licence Context | Define licensed rights, goods/services, territory, term, quality control, use evidence and termination conditions. | licence instrument, official rights and client facts | use-evidence assessment and portfolio action |
| MR-C10 | Product Session | Record actor, role, organization, entry mode, active step, visible versions, warnings, pause and return route. | authenticated context and Handoff Envelope | resume checks and Return Envelope |
| MR-C11 | Pilot Context | Bound Product edition, organizations, users, services, jurisdictions, providers, fallback and stop conditions. | approved pilot plan and conformance profile | metrics, evaluation and release decision |

## 7. Evidence and Source-Backed Record Register

| ID | Record | What it proves | Source / verification | Supersession and use |
| --- | --- | --- | --- | --- |
| MR-E01 | Submission Evidence | what payload or package was sent, when, through which route and under which attempt identity | connector, portal, provider or professional evidence | retained per attempt; does not prove official receipt |
| MR-E02 | Delivery Evidence | technical delivery or transmission result | transport, provider channel or system receipt | may be corrected; does not prove provider acceptance or official effect |
| MR-E03 | Provider Report | provider-reported receipt, acceptance, filing or outcome | identified provider, time, scope and attachments | classified by evidence strength; not automatically official truth |
| MR-E04 | Official Acknowledgement Evidence | official receipt, filing number, acceptance, rejection or other recognized procedural acknowledgement | official office, authenticated official account or verified official artifact | corrected or superseded with linked history |
| MR-E05 | Official Event Snapshot | sourced official notice, status, publication, decision or event at a retrieval time | official source or verified evidence with retrieval metadata | later snapshot supersedes for current view but history remains |
| MR-E06 | Deadline Record | official date, calculation basis, source hierarchy, uncertainty, internal target, extension and responsibility | official notice or rule, Pack version and professional verification | recalculated only with preserved prior basis and affected decisions |
| MR-E07 | Source Record | identify authority, publication/effective date, retrieval, immutable copy or checksum, language and supersession | controlled source ingestion and professional Review | source versions remain linked to rules and historical decisions |
| MR-E08 | Registration Outcome Record | official registered scope, owner, number, date, limitations, disclaimers and certificate relationship | official register and registration evidence | supports Right Baseline; later record change does not rewrite historical outcome |
| MR-E09 | Official Update Evidence | prove renewal, recordal, correction, cancellation, expiry or other official-record change | official register, notice or verified certificate/receipt | updates relevant Baseline only after verification |

## 8. Baseline and Obligation Register

| ID | Record | Purpose | Review and update rule | Consumers |
| --- | --- | --- | --- | --- |
| MR-B01 | Right Baseline | provide the reviewed operational baseline for one independent application or registration | verified from official source; new version on material official change | maintenance, renewal, recordal, transaction and portfolio work |
| MR-B02 | Maintenance Obligation Set | record sourced official duties, calculated dates, internal targets, evidence needs, responsibility and uncertainty | recalculated on Pack, official event or Right Baseline change | reminders, renewal, evidence and risk review |
| MR-B03 | Use-Evidence Coverage Record | map goods/services, territory, period, owner/licensee, source and gaps | professional Review; new evidence adds versions without erasing gaps | declarations, defense, cancellation and portfolio planning |
| MR-B04 | Provider Capability Evidence Record | preserve service, jurisdiction, qualification, experience, recency, relationship and limitations | source and checked date required; expires or is superseded | private-first routing and Human Selection |

## 9. View and Projection Register

| ID | View | Purpose | Authority boundary | Consumers |
| --- | --- | --- | --- | --- |
| MR-V01 | Filing and Scope Diff View | compare recommended, approved, acknowledged and officially registered scope | derived comparison; source records remain authoritative | client, reviewer and portfolio team |
| MR-V02 | Outcome Snapshot | present sourced procedural outcome, interpretation, consequence and next action | does not create or close official procedure | client, professional and Communication Packet |
| MR-V03 | Chain-of-Title View | show original applicant, registered owner, transactions, recordals, gaps and proposed owner | derived from official and transaction evidence; gaps remain explicit | recordal, transaction and portfolio work |
| MR-V04 | Portfolio Continuity View | combine independent rights, stages, obligations, evidence and risks without merging legal states | each underlying right and source remains independently authoritative | Portfolio Action Plan and management surfaces |
| MR-V05 | Participant Surface Projection | present role- and purpose-limited fields and actions | visibility does not change ownership or authority | client, professional, reviewer, approver, coordinator, finance and provider |

## 10. Governance and Configuration Register

| ID | Record | Purpose | Required control | Main consumers |
| --- | --- | --- | --- | --- |
| MR-G01 | Jurisdiction Pack | control jurisdiction-, service- and stage-specific rules, forms, fees and Product behavior | scope, professional owner, version, gaps and approval | recommendations, Requirements, fees, deadlines and packages |
| MR-G02 | Rule Record | express one sourced operational rule, condition, exceptions and tests | source links, effective date, status, owner and change history | Product validation and professional explanation |
| MR-G03 | Pack Version Record | identify a coherent reviewed set of rules, sources, forms, fees and migration instructions | approval, prior version, affected journeys and known gaps | Product runtime and historical lineage |
| MR-G04 | Rule Change Candidate | preserve detected change, old/new evidence, impact, urgency and verification | detection is not adoption; professional Review required | Pack release workflow and affected-artifact revalidation |
| MR-G05 | Organization Overlay | control private review, provider, commercial, deadline and communication policy | versioned and distinguishable from official rule | Workplace-embedded Product behavior |
| MR-G06 | AI Task Context | bound model purpose, inputs, Pack version, source set, confidentiality and prohibited conclusions | minimum necessary context and role permission | AI-assisted Product task |
| MR-G07 | AI Output Record | retain material AI output basis, model/time, sources, uncertainty and Human disposition | accepted, modified or rejected state; no hidden authority | professional Review, audit and learning |
| MR-G08 | Metric Definition | define metric purpose, owner, source, calculation, segmentation, limitation and decision use | versioned definition and data-quality checks | Product review and pilot governance |
| MR-G09 | Evaluation Record | record evaluation set, expected behavior, result, reviewer and limitation | controlled cases including failures and edge cases | AI, Product and release decision |
| MR-G10 | Conformance Statement | declare supported profile, jurisdictions, services, participants, dependencies, exclusions and validation state | evidence-backed and versioned; marketing may not exceed it | users, reviewers, release and implementation teams |

## 11. Accountable Decision Register

| ID | Decision | Accountable actor | Exact scope | Evidence and invalidation | Does not equal |
| --- | --- | --- | --- | --- | --- |
| MR-D01 | Client Acceptance | authorized client actor | exact Quote version and commercial scope | acceptance record; invalid if Quote expired or changed | changed-scope instruction, payment or filing |
| MR-D02 | Professional Decision | eligible professional | recommendation, readiness, evidence, strategy or override | artifact version, reason, sources and qualification | client authority or Execution |
| MR-D03 | Filing Approval | authorized Human role | exact package, jurisdiction, route, purpose and expiry | reviewed version and active conditions; material change invalidates | Execution or official filing |
| MR-D04 | Human Selection | authorized organization actor | selected provider or execution route | candidate evidence, conflict, availability and reason | appointment, instruction or acceptance |
| MR-D05 | Provider Acceptance | appointed provider | accepted engagement, scope, fee and deadline | provider response and any conditions | official submission or office acceptance |
| MR-D06 | Response Strategy Decision | eligible professional plus client authority where needed | selected response, amendment, evidence and consequence | Issue Set, options, deadline and decision record | Response Filing Approval or official acceptance |
| MR-D07 | Adversarial or Settlement Decision | authorized client and eligible professional roles | pleading, defense, withdrawal, limitation, settlement or remedy authority | exact proceeding, terms, scope, deadline and conflicts | signed settlement, filed document or official closure |
| MR-D08 | Renewal Approval | authorized owner/client and organization role | exact right, scope, owner, package, fee, route and timing | Right Baseline, package version and payment conditions | filed renewal or renewed right |
| MR-D09 | Recordal Approval | authorized client/owner and organization role | exact change, affected rights, documents, jurisdictions and route | authority, Chain-of-Title View and package version | signed transaction or official update |
| MR-D10 | Non-Renewal Decision | authorized owner/client role | one identified right and understood consequence | Right Baseline, deadline, alternatives and acknowledgment | official lapse before it occurs |
| MR-D11 | Communication Approval | authorized reviewer or sender under policy | exact recipient, purpose, language, attachments and version | source and confidentiality checks; correction links retained | delivery, acknowledgment or official outcome |
| MR-D12 | Pack Release Approval | accountable professional owner | exact Pack version and effective scope | source Review, tests, impact and migration plan | legal enactment or official-office publication |
| MR-D13 | Pilot or Release Decision | authorized Product/publication reviewer | defined profile, scope, evidence, exceptions and stop conditions | evaluation and conformance evidence | production or protected-action authority unless separately granted |

## 12. External and Formal Objects Not Owned by MarkReg

The following may be referenced or displayed but remain outside Product-local ownership:

- Organization, User, Client, Contact, Brand and Trademark Core Objects;
- formal Order, Matter, Task, Workflow and responsibility records;
- formal Document, Evidence, Review, Approval, Communication, payment, invoice and refund records;
- Book 03 Execution Context, attempt, idempotency, Event and failure state;
- provider identity, appointment, invoice and provider-system records;
- official application, registration, proceeding and register records;
- official laws, rules, forms, fee schedules, notices and decisions.

MarkReg may prepare candidates, typed references and projections. Owning Services and external authorities create or change the formal facts.

## 13. Non-Canonical and Local Records

The following do not require a new B05-SPEC-0001 ID unless future Review shows that they cross a material boundary:

- transient UI filters, sort choices and unopened help text;
- temporary draft wording that is fully contained in a canonical package version;
- local annotations that do not leave a permitted personal or organization context;
- cached copies used only for performance and retaining source identity;
- presentation-only charts derived from a registered View;
- individual checklist rows already governed by a canonical Requirement Set;
- provider or office portal screens preserved only as Evidence attachments;
- implementation logs already governed by Book 03 or an Owning Service.

A local record becomes a candidate for canonical registration when it carries independent responsibility, approval, external effect, reusable source meaning or cross-Product lineage.

## 14. Version and Supersession Rules

Every material controlled record must carry, as applicable:

- stable record identifier and class;
- record version;
- created and last-updated timestamps;
- purpose and scope;
- source references and source versions;
- responsible actor and represented organization;
- Review status;
- decision or approval status;
- validity, expiry and revalidation conditions;
- superseded-by reference;
- affected independent rights and jurisdictions;
- downstream records already created from it;
- formal object or external evidence references;
- correction and conflict history.

A downstream record identifies the exact upstream versions it consumed. Updating an upstream record does not silently mutate an accepted Quote, approved package, formal Order, Matter, provider instruction, Execution attempt, official record or sent Communication.

## 15. Change Propagation

| Change | Minimum Product response |
| --- | --- |
| Applicant or owner identity changes | invalidate affected ownership, authority, document, signature, price, readiness, package, recordal and chain-of-title assumptions |
| Jurisdiction or route changes | regenerate provider, fees, forms, documents, timing, Pack, Requirements and readiness dependencies |
| Mark variant changes | re-evaluate filing units, search, classes, goods/services, image requirements, package, evidence and cost |
| Goods/services or class scope changes | update search, fee, package, approval, response, registered-scope diff and maintenance implications |
| Official fee or provider cost changes | identify affected draft, accepted and approved commercial records; apply explicit variance and reapproval rules |
| Jurisdiction rule or form version changes | identify affected journeys and require the defined degree of revalidation before protected action |
| Official notice is corrected or superseded | preserve prior event, update Examination/Proceeding Context, recalculate Deadline Record and invalidate affected strategy or Communication |
| Client chooses another option | preserve prior choice and create new downstream scope and versions |
| Professional override occurs | retain original recommendation, override reason, actor, evidence and affected downstream records |
| Package changes after approval | invalidate the affected approval and block Execution until the exact new version is reviewed and approved |
| Provider proposes a change | create a new candidate or instruction version; do not mutate the approved package silently |
| Execution outcome is unknown | open Reconciliation Context; block unsafe retry until duplicate risk and external state are assessed |
| Official owner changes | update verified Right Baseline and affected maintenance, renewal, transaction and portfolio records without rewriting historical ownership |
| A right is cancelled, expires or is not renewed | preserve the former baseline and decision history; update current portfolio and obligation views with sourced effect |
| Permission, organization or purpose changes | re-evaluate visibility, Handoff scope, Product Session and Return Envelope; do not transfer unauthorized local context |

## 16. Service-Family Conformance

A service family is supported only when MarkReg defines:

1. entry conditions;
2. minimum source facts;
3. canonical Product records and decisions;
4. applicable Jurisdiction Pack and source dependencies;
5. professional Review and accountable decision gates;
6. formalization and Execution route;
7. expected provider and official evidence;
8. unknown, failure, reconciliation and correction behavior;
9. outcome and state mapping;
10. future obligations and lifecycle continuation;
11. participant visibility and action rights;
12. observable conformance scenarios.

A page, form, provider listing, fee table, AI prompt or reminder alone does not constitute service-family support.

## 17. Appendix Projection Contract

Appendix A may summarize the controlled records and lineages in this specification.

Appendix B may map lifecycle states and authority to these records.

The appendices must:

- retain controlled IDs;
- preserve record class;
- identify source and authority boundaries;
- distinguish Product-local, formal, Execution, provider and official state;
- avoid introducing an unregistered canonical record;
- identify any remaining PF-03, PF-04 or PF-05 dependency.

Where an appendix and this specification conflict, this specification controls until a reviewed update resolves the conflict.

## 18. PF-02 Completion Decision

```text
Applies through CH47: YES
Later-stage Product records assigned controlled IDs: YES
Decisions assigned controlled IDs: YES
Contexts, Evidence, Baselines, Views and Governance separated: YES
Formal and external objects excluded from Product ownership: YES
Version and supersession rules reconciled: YES
Change propagation extended through portfolio continuity: YES
Appendix A reconciliation authorized: YES
Appendix B PF-02 state mapping authorized: YES
PF-03 reference-journey completion: STILL REQUIRED
PF-04 scenario and participant completion: STILL REQUIRED
PF-05 Jurisdiction Pack and commercial completion: STILL REQUIRED
Architecture Canon or Book 02–04 amendment required: NO
```
