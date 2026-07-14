# Appendix B — Lifecycle State and Authority Matrix

**Status:** Controlled Reader Draft — PF-02 State Mapping and PF-04 Scenario Indexing Reconciled  
**Primary sources:** CH07, CH21–CH47, B05-SPEC-0001 v0.2 and B05-SPEC-0003 v0.2  
**Reader purpose:** show which state domain is being described, who may change it, what evidence supports it, and which scenarios test the boundary.

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

## B.2 State Domains, Authority and Scenario References

| State domain | Examples | Controlled records | Typical authority | Priority scenarios |
| --- | --- | --- | --- | --- |
| Product journey | draft, blocked, ready for Review, superseded | MR-A01–A30, MR-C10 | MarkReg plus accountable users | MR-SCN-13, 25, 34, 35 |
| recommendation | candidate, reviewed, selected, rejected | MR-A03, MR-A04, MR-D01, MR-D02 | eligible professional and authorized client | MR-SCN-03, 04, 14 |
| commercial | Quote valid, accepted, expired; payment pending | MR-A05–A07 and formal finance records | client, commercial and finance services | MR-SCN-06, 07, 08, 15 |
| formal work | Order open, Matter active, Review pending | formal Owning Service records referenced by MR-A12 | Owning Service and Workplace | MR-SCN-25, 41 |
| readiness | complete, conditional, blocked, expired | MR-A09, MR-A10 | Product assessment plus reviewer | MR-SCN-05, 08, 17 |
| approval | client confirmed, Review complete, approval active or invalid | MR-D01–D13 and formal approval records | authorized Human role | MR-SCN-11, 16, 17, 18 |
| routing and provider | candidate, selected, instructed, accepted, declined | MR-C01, MR-A14–A16, MR-D04, MR-D05 | organization and appointed provider | MR-SCN-19–22 |
| Execution | prepared, started, failed, unknown, reconciled | MR-A17, MR-C02, MR-A18 and Book 03 records | Book 03 Execution and execution-capable service | MR-SCN-23–25 |
| transmission | sent, delivered, failed, duplicate-risk, unknown | MR-E01, MR-E02, MR-C02 | connector, provider, portal and Execution evidence | MR-SCN-15, 23, 24 |
| provider report | received, accepted, reported filed | MR-E03 | identified provider | MR-SCN-21, 23 |
| official acknowledgement | office received, identifier issued, correction required | MR-E04 | official authority or verified official evidence | MR-SCN-23, 24, 29 |
| official lifecycle | examination, publication, opposition, registration, cancellation | MR-E05, MR-E08, MR-E09, MR-B01 | official authority | MR-SCN-10, 26, 27, 30, 33 |
| professional interpretation | risk, strategy, evidence sufficiency, remedy viability | MR-D02, MR-A19–A24, MR-C03–C06 | eligible professional | MR-SCN-04, 09, 17, 27 |
| client projection | action required, waiting for office, registered scope | MR-A13, MR-V01, MR-V02, MR-A25 | controlled Product projection | MR-SCN-10, 26, 29, 30 |
| continuing obligation | renewal due, use evidence weak, recordal pending | MR-B02, MR-B03, MR-E06 | official rule, source and assigned responsibility | MR-SCN-27, 31 |
| ownership and transaction | owner verified, assignment signed, recordal pending | MR-C07–C09, MR-A27, MR-A28, MR-V03 | parties, professional and official office | MR-SCN-01, 12, 31, 32 |
| portfolio | coverage gap, challenged right, action plan | MR-V04, MR-A29, MR-D10 | Product view plus per-right Decisions | MR-SCN-33, 39 |
| governance and rule | rule active, disputed, Pack released, AI reviewed | MR-G01–G10, MR-D12, MR-D13 | professional owner and governance | MR-SCN-36–41 |

## B.3 Key State Distinctions

| Distinction | Controlled reading | Test scenarios |
| --- | --- | --- |
| recommendation vs Decision | MR-A03/A04 propose; MR-D01/D02 records accountable choice | 03, 04, 14 |
| readiness vs approval | MR-A10 describes conditions; MR-D03 grants bounded authority | 05, 08, 17 |
| approval vs Execution | MR-D03 permits an exact action; MR-A17 and Book 03 coordinate it | 16, 18, 23 |
| sent vs delivered | MR-E01 may exist without MR-E02 | 21, 23 |
| provider receipt vs acceptance | delivery does not establish MR-D05 | 21 |
| provider report vs official acknowledgement | MR-E03 requires reconciliation to MR-E04 | 23, 24 |
| acknowledgement vs registration | MR-E04 confirms procedure, not MR-E08 outcome | 23, 30 |
| registered vs certificate available | MR-E08 may exist without certificate file | 30 |
| certificate vs current register | certificate may be stale; MR-B01 uses current sources | 30 |
| renewal prepared vs approved | MR-A26 is candidate; MR-D08 authorizes exact action | 31 |
| renewal filed vs renewed | submission or acknowledgement does not prove MR-E09 effect | 23, 31 |
| assignment signed vs owner updated | MR-C08 and MR-E09 remain separate | 32 |
| signal vs legal conclusion | monitoring opens Review; it does not create infringement or filing authority | 33 |
| Product Session vs Matter | MR-C10 is interaction context, not formal Matter state | 34, 35 |
| Return Envelope vs formal object | MR-A30 returns references; receiving service consumes idempotently | 25 |
| rule detected vs active | MR-G04 requires MR-D12 before protected Product use | 36, 37 |
| AI output vs professional conclusion | MR-G07 records assistance; MR-D02 remains accountable | 09, 36 |
| publication vs production authority | publication state does not grant operational authority | 40 |

## B.4 Authority and Transition Matrix

| Transition | May prepare | Must review or confirm | May authorize or accept | Minimum evidence |
| --- | --- | --- | --- | --- |
| Business Context → Need Brief | MarkReg or user | user; professional where material | user confirmation | MR-A01/A02 and source lineage |
| Recommendation → selected option | MarkReg and professional | professional where material | authorized client actor | MR-A03/A04, MR-D01/D02 |
| Quote → accepted | commercial surface | client verifies exact version | authorized client actor | MR-A06, MR-D01 |
| Intake → ready for Review | MarkReg and coordinator | coordinator and professional | no external authority | MR-A08–A10 |
| package → reviewed | professional preparer | eligible reviewer | MR-D02 | exact version, source and diff |
| reviewed package → Filing Approval | Product requests | client and professional conditions | authorized approver | MR-D03 tied to exact version |
| provider candidate → selected | MarkReg recommends | conflict, eligibility and availability | authorized organization actor | MR-C01, MR-A14, MR-D04 |
| selected provider → accepted | organization instructs | provider checks scope and conflict | appointed provider | MR-A15/A16, MR-D05 |
| approved request → Execution | MarkReg prepares | entry validation | existing exact approval | MR-A17, MR-D03 and Book 03 records |
| sent → official acknowledgement | provider or connector reports | reconciliation or official verification | no Product authority | MR-E01–E04, MR-C02 |
| official notice → Examination Context | MarkReg ingests | professional verifies source and scope | responsibility assigned separately | MR-E05/E06, MR-C03 |
| Issue Set → Response Strategy | MarkReg and professional propose | professional and client where material | MR-D06 | MR-A19–A21 and deadline evidence |
| response package → filed | professional prepares | Review and confirmation | MR-D03 | MR-A22, MR-A17, MR-E01–E04 |
| adversarial option → action | professional prepares | client and professional authority | MR-D07 and MR-D03 where filing follows | MR-C05/C06, MR-A23/A24 |
| registration → Right Baseline | MarkReg projects | responsible professional verifies | no creation of official right | MR-E08, MR-V01, MR-B01 |
| obligation → renewal filing | MarkReg and professional prepare | right, owner, fee and payment Review | MR-D08 | MR-B01/B02, MR-A26, MR-E01–E04 |
| transaction → official recordal | parties and professional prepare | authority and chain Review | MR-D09 | MR-C07/C08, MR-A27/A28, MR-E09 |
| Product result → Return | MarkReg prepares | permission, version and destination | receiving service consumes idempotently | MR-C10, MR-A30 |
| rule signal → Pack release | crawler, provider or user signals | source, impact and professional Review | MR-D12 | MR-E07, MR-G01–G04 |
| evaluation → release Decision | Product team analyzes | conformance and stop-condition Review | MR-D13 | MR-C11, MR-G08–G10 |

## B.5 Unknown, Conflict and Correction States

| State | Required behavior | Scenario references |
| --- | --- | --- |
| source unavailable | disclose missing authority and restrict dependent claim or action | 10, 36 |
| source conflict | preserve sources, apply hierarchy and escalate | 27, 37 |
| provider report awaiting evidence | keep provider-reported state, not official | 23 |
| technical effect unknown | open reconciliation and block blind retry | 15, 23, 24 |
| deadline disputed | show conflict, conservative target and reviewer | 27 |
| rule changed and unverified | mark disputed and block protected use | 07, 36, 37 |
| approval invalidated | preserve history and require a new exact-version Decision | 16, 18 |
| official event corrected | link snapshots and re-evaluate Decisions and Communications | 26, 29 |
| owner conflict | block unsupported renewal or recordal assumptions | 01, 12, 31 |
| chain gap | expose missing link and limit ownership claims | 12, 32 |
| organization mismatch | block access, Handoff or Return | 34, 35 |

Unknown does not mean failed, successful or safe to retry.

## B.6 Client-Facing Label Rules

Preferred examples:

- `Provider reports filing completed — official receipt pending`;
- `Response sent — office acknowledgement pending`;
- `Registration verified — certificate file not yet available`;
- `Renewal filed — renewed register entry pending`;
- `Ownership documents signed — recordal not yet verified`;
- `Publication detected — opposition deadline under verification`.

Non-conforming examples include:

- `Filed` based only on a draft, instruction or technical result;
- `Registered` based only on publication or allowance;
- `Renewed` based only on payment or submission;
- `Owner updated` based only on an assignment;
- `No opposition` based only on absence of a signal.

## B.7 Profile Scenario Minimums

| Profile | State-boundary scenario minimum |
| --- | --- |
| Foundation | 10, 11, 18, 22, 35, 36, 40 |
| Guided Decision | 01–04, 13, 14 |
| Commercial Intake | 05–08, 15, 28 |
| Filing Preparation | 16–20 |
| Governed Filing | 21–25 |
| Post-Filing | 10, 23, 26–29 |
| Portfolio Continuity | 12, 30–33 |
| Full-Lifecycle | all applicable state families |

Jurisdiction-specific tests may add requirements under B05-SPEC-0004.

## B.8 Reconciliation Status

```text
State domains mapped: COMPLETE
Authority transitions mapped: COMPLETE
Unknown and correction states mapped: COMPLETE
Client-facing label rules mapped: COMPLETE
MR-SCN references mapped: COMPLETE
Profile scenario minimums mapped: COMPLETE
PF-02 state work: COMPLETE
PF-04 scenario indexing: COMPLETE
Final figure integration: PENDING PF-07
Native-English and compression edit: PENDING PF-06
Structural and rendered validation: PENDING PF-08
```

Appendix B is a controlled reader draft reconciled for PF-02 and PF-04. It becomes publication-ready only after the remaining publication-finishing gates pass.