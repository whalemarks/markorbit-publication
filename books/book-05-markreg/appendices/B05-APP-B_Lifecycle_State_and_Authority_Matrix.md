# Appendix B — Lifecycle State and Authority Matrix

**Status:** Controlled Appendix Draft — PF-02 State Mapping Complete; PF-04 Scenario Indexing Pending  
**Primary sources:** CH07, CH21–CH42, B05-SPEC-0001 v0.2 and B05-SPEC-0003  
**Reader purpose:** show which state domain is being described, who may change it, which controlled records support it, and what external effect it carries.

## B.1 Core Rule

MarkReg must never collapse every lifecycle dimension into one status.

```text
Product state
≠ commercial state
≠ formal business state
≠ approval state
≠ Execution state
≠ provider-reported state
≠ official state
≠ professional interpretation
≠ client-facing projection
```

A surface may summarize several dimensions, but it must preserve the underlying source, record class and authority.

## B.2 State Domains and Controlled Records

| State domain | Examples | Controlled records | Typical authority | External effect |
| --- | --- | --- | --- | --- |
| Product journey | draft, incomplete, ready for Review, blocked, superseded | MR-A01–A30, MR-C10 | MarkReg plus accountable users | none by itself |
| recommendation | candidate, reviewed, revised, rejected, selected | MR-A03, MR-A04, MR-D02 | eligible professional and authorized user | decision support only |
| commercial | Quote draft, valid, accepted, expired; payment pending or received | MR-A05–A07, MR-D01; formal finance records outside MarkReg | commercial, client and finance services | commercial effect only under applicable terms |
| formal work | Order open, Matter active, Task assigned, Review pending | formal Core/Workplace/Owning Service records referenced by MR-A12 | Owning Services and Workplace | organizational effect, not office effect |
| readiness | structurally complete, commercially blocked, professionally conditional, execution ready | MR-A09, MR-A10 | Product assessment plus accountable reviewer | no protected action authority |
| approval | client confirmed, Professional Review complete, Filing Approval active or invalidated | MR-D01–D13 and formal approval records | authorized Human role or accepted provider | authorizes only stated scope and next step |
| routing and provider | candidate, selected, appointment prepared, instructed, received, accepted, declined, change requested | MR-C01, MR-A14–A16, MR-D04, MR-D05, MR-B04 | organization and appointed provider | provider relationship effect only |
| Execution | prepared, queued, started, failed, unknown, reconciled | MR-A17, MR-C02, MR-A18 plus Book 03 records | Book 03 Execution and execution-capable service | coordinated operational effect |
| transmission | sent, delivery confirmed, failed, duplicated-risk, unknown | MR-E01, MR-E02, MR-C02 | connector, provider, professional portal and Execution evidence | no official effect without source evidence |
| provider report | received, accepted, reported filed, provider outcome reported | MR-E03 | identified provider | evidence strength varies; not automatically official truth |
| official acknowledgement | received by office, filing number issued, rejected, correction required | MR-E04 | official authority or verified official evidence | procedural effect supported by evidence |
| official lifecycle | filed, under examination, published, opposed, registered, cancelled, expired | MR-E05, MR-E08, MR-E09, MR-B01 | official authority | authoritative official state at the sourced time |
| professional interpretation | low risk, response recommended, evidence insufficient, appeal viable | MR-D02, MR-A19–A24, MR-C03–C06 | eligible professional | advice and strategy, not official outcome |
| client projection | action required, waiting for office, registered-scope summary | MR-A13, MR-V01, MR-V02, MR-A25 | MarkReg from controlled source records | explanatory and communicative only |
| continuing obligation | renewal due, declaration required, use evidence weak, recordal pending | MR-B02, MR-B03, MR-E06 | official rule plus verified calculation and responsibility | future duty; reminder is not the deadline |
| ownership and transaction | current owner verified, assignment signed, recordal pending, chain gap | MR-C07–C09, MR-A27, MR-A28, MR-V03, MR-D09 | client, professional, transaction parties and official office | contractual and official effects remain separate |
| portfolio | covered, gap identified, duplicate candidate, action planned, non-renewal decided | MR-V04, MR-A29, MR-D10 | Product view plus authorized decisions per right | no merged global legal state |
| governance and rule | rule active, disputed, superseded; Pack released; AI output reviewed | MR-G01–G10, MR-D12, MR-D13 | professional owner and Product/publication governance | Product configuration or declared support only |

## B.3 Key State Distinctions

| Distinction | Controlled reading |
| --- | --- |
| recommendation vs decision | MR-A03 or MR-A04 may propose; MR-D01, MR-D02 or another accountable Decision records the choice |
| readiness vs approval | MR-A10 describes conditions; MR-D03 or another approval grants bounded authority |
| approval vs Execution | MR-D03 permits an exact action; MR-A17 and Book 03 coordinate it |
| sent vs delivered | MR-E01 may exist without MR-E02 |
| delivered vs provider received | technical delivery does not prove provider receipt or Human attention |
| provider received vs Provider Acceptance | MR-D05 requires the provider’s accepted engagement and conditions |
| provider reported filed vs officially acknowledged | MR-E03 requires reconciliation to MR-E04 or other official evidence |
| officially acknowledged vs registered | MR-E04 begins or confirms a procedure; MR-E08 records a later registration outcome |
| registered vs certificate available | MR-E08 may be verified before or without a certificate file |
| certificate vs current official record | certificate evidence may become operationally stale; MR-B01 must use current verified sources |
| renewal prepared vs approved | MR-A26 is a candidate; MR-D08 grants bounded renewal authority |
| renewal filed vs renewed right | MR-E01 or MR-E04 does not itself prove MR-E09 official renewal effect |
| assignment signed vs official owner updated | MR-C08 transaction effect and MR-E09 recordal effect remain separate |
| monitoring signal vs legal conclusion | a signal may update MR-V04 or open Review; it does not create infringement or filing authority |
| Product Session vs Matter state | MR-C10 records interaction context; the formal Matter remains owned outside MarkReg |
| Return Envelope vs formal object | MR-A30 returns typed references; the receiving Owning Service controls formal creation and idempotency |
| rule detected vs rule active | MR-G04 is a Change Candidate; MR-D12 is required before a new Pack rule drives protected Product behavior |
| AI output vs professional conclusion | MR-G07 records AI assistance and Human disposition; MR-D02 remains accountable |

## B.4 Authority and Transition Matrix

| Transition | May propose or prepare | Must review or confirm | May authorize or accept | Minimum evidence / controlled records |
| --- | --- | --- | --- | --- |
| Business Context → confirmed Need Brief | MarkReg or user | user; professional where material | user confirmation | MR-A01, MR-A02 and source lineage |
| Recommendation → selected option | MarkReg and professional | eligible professional where material; client understands trade-offs | client or authorized organization actor | MR-A03, MR-A04, MR-D01/D02 as applicable |
| Quote draft → accepted | commercial surface | client verifies exact version | authorized client actor | MR-A06 and MR-D01 |
| Commercial Instruction → formal work candidate | MarkReg | commercial, payment and authority checks | Owning Service creates formal object | MR-A07 and MR-A12 |
| Intake incomplete → ready for Review | MarkReg and coordinator | coordinator and professional | no external authority | MR-A08–A10 |
| package candidate → reviewed | professional preparer | eligible reviewer | MR-D02 Review result | MR-A11 or service-specific package, source lineage and diff |
| reviewed package → Filing Approval | Product may request | client and professional conditions as applicable | authorized approver | MR-D03 tied to exact package version |
| provider candidate → selected | MarkReg may recommend | conflict, eligibility, availability and relationship Review | authorized organization actor | MR-C01, MR-A14, MR-B04 and MR-D04 |
| selected provider → accepted engagement | organization prepares appointment and instruction | provider checks scope and conflict | appointed provider | MR-A15, MR-A16 and MR-D05 |
| approved request → Execution started | MarkReg prepares MR-A17 | Execution entry validation | existing approval permits only exact request | MR-A12, MR-D03, idempotency identity and Book 03 records |
| sent → official acknowledgement | provider, connector or portal may report | reconciliation or official-source verification | no additional Product authority | MR-E01–E04 and MR-C02 when uncertain |
| official notice → verified Examination Context | MarkReg may ingest | eligible professional verifies source and affected scope | responsibility accepted under organization policy | MR-E05, MR-E06 and MR-C03 |
| Issue Set → Response Strategy | MarkReg and professional may propose | eligible professional; client where a material choice is required | MR-D06 | MR-A19–A21 and deadline evidence |
| Response Package → filed response | professional prepares | Review and client confirmation as applicable | MR-D03 | MR-A22, MR-A17 and MR-E01–E04 |
| publication signal → verified window | monitoring may signal | official-source and Pack verification | no protected action from signal alone | MR-C04, MR-E05 and MR-E06 |
| adversarial strategy → filed or settled action | professional prepares | client and professional authority checks | MR-D07 plus MR-D03 where filing follows | MR-C05/C06, MR-A23/A24 and exact terms |
| registration event → Right Baseline | MarkReg may project | responsible professional or team verifies scope | no creation of official right | MR-E08, MR-V01 and MR-B01 |
| obligation signal → verified Maintenance Obligation | MarkReg may calculate | Pack/source and professional verification | responsibility assigned separately | MR-B02 and MR-E06 |
| renewal candidate → renewal filing | MarkReg and professional prepare | right, owner, fees, package and payment reviewed | MR-D08 | MR-B01/B02, MR-A26, MR-A17 and MR-E01–E04 |
| transaction document → official recordal | client and professional prepare | authority, affected rights and chain of title reviewed | MR-D09 | MR-C07/C08, MR-A27/A28, MR-V03 and MR-E09 |
| portfolio signal → Portfolio Action Plan | MarkReg may propose | professional and client Review per action | service-specific Decisions | MR-V04, MR-A29 and independent Right Baselines |
| Product work → returned result | MarkReg prepares | permission, purpose, version and destination validated | receiving service consumes idempotently | MR-C10 and MR-A30 |
| rule change signal → active Pack version | crawler, provider, user or Product may signal | source capture, impact assessment, tests and professional Review | MR-D12 | MR-E07 and MR-G01–G04 |
| evaluation → pilot/release decision | Product team may analyze | conformance and stop-condition Review | MR-D13 | MR-C11 and MR-G08–G10 |

## B.5 Unknown, Conflict and Correction States

| State | Required Product behavior | Supporting records |
| --- | --- | --- |
| source unavailable | disclose missing authority and restrict dependent claims or actions | MR-E07, MR-G02 |
| source conflict | preserve both sources, apply hierarchy and escalate | MR-E07, MR-G02, MR-D02 |
| provider report awaiting evidence | retain as provider-reported, not official | MR-E03 |
| technical outcome unknown | open Reconciliation Context and block blind retry | MR-C02, MR-A18, MR-E01/E02 |
| deadline disputed | show source conflict, conservative internal target and responsible reviewer | MR-E06, MR-D02 |
| rule changed and unverified | mark affected rule unknown/disputed and block protected use | MR-G04, MR-D12 |
| approval invalidated by change | preserve prior approval history and require a new exact-version decision | MR-D03 or service-specific approval |
| official event corrected | link prior and corrected snapshots; re-evaluate affected decisions and Communications | MR-E05, MR-E06, MR-A25 |
| owner identity conflict | block unsupported renewal or recordal assumptions and open resolution | MR-B01, MR-C07/C08, MR-V03 |
| chain-of-title gap | expose missing link and limit claims of current ownership | MR-V03, MR-A28 |
| permission or organization mismatch | block surface access, Handoff or Return until context is corrected | MR-A12, MR-C10, MR-A30 |

Unknown does not mean failed, successful or safe to retry.

## B.6 Client-Facing Label Rules

A client label should state both the observed state and its authority where confusion is possible.

Preferred examples:

- `Provider reports filing completed — official receipt pending`;
- `Response sent — office acknowledgement pending`;
- `Registration verified — certificate file not yet available`;
- `Renewal filed — renewed register entry pending`;
- `Ownership documents signed — recordal not yet verified`;
- `Publication detected — opposition deadline under verification`.

Non-conforming examples include:

- `Filed` based only on a draft or provider instruction;
- `Registered` based only on publication or allowance;
- `Renewed` based only on payment or submission;
- `Owner updated` based only on an assignment document;
- `No opposition` based only on absence of a monitoring signal.

## B.7 PF-02 and PF-04 Status

```text
State domains mapped to controlled record IDs: COMPLETE
Authority transitions mapped to controlled Decisions: COMPLETE
Unknown and conflict states mapped: COMPLETE
Client-facing overstatement rules mapped: COMPLETE
PF-02 portion of Appendix B: COMPLETE
Given/When/Then scenario IDs: PENDING PF-04
Implementation-profile scenario minimums: PENDING PF-04
Final figure integration: PENDING PF-07
Native-English and compression edit: PENDING PF-06
```

Appendix B is a controlled reader draft. It becomes publication-ready only after PF-04 scenario indexing and later publication validation pass.
