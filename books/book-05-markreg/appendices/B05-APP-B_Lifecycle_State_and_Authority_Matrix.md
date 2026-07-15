# Appendix B — Lifecycle State and Authority Matrix

**Status:** Controlled Reader Draft v0.3 — PF-06D Reconciled  
**Primary sources:** CH07, CH21–CH47, B05-SPEC-0001 v0.3 and B05-SPEC-0003 v0.3  
**Reader purpose:** show which state domain is described, who may change it, what Evidence supports it and which scenarios test the boundary.

## B.1 Core Rule

```text
Product state
≠ commercial state
≠ formal business state
≠ Approval state
≠ Execution state
≠ provider-reported state
≠ official state
≠ professional interpretation
≠ client-facing Projection
```

## B.2 State Domains

| Domain | Current records | Typical authority | Priority scenarios |
| --- | --- | --- | --- |
| Product journey | MR-A01–A30, MR-C10 | MarkReg plus accountable users | 13, 25, 34, 35 |
| applicant and authority | MR-C12, MR-D02 | authorized client/owner and eligible professional | 01, 05, 11, 18, 31 |
| recommendation | MR-A03, MR-A04, MR-D01, MR-D02 | eligible professional and authorized client | 03, 04, 14 |
| commercial | MR-A05–A07 and formal finance records | client, commercial and finance services | 06, 07, 08, 15 |
| formal work | formal Order, Matter, Review and responsibility records referenced by MR-A12 | Owning Service and Workplace | 25, 41 |
| readiness | MR-A09, MR-A10 | Product assessment plus reviewer | 05, 08, 17 |
| Approval | MR-D01–D13 and formal Approval records | authorized Human roles | 11, 16, 17, 18 |
| routing and provider | MR-C01, MR-A14–A16, MR-D04, MR-D05 | organization and appointed provider | 19–22 |
| Execution | MR-A17, MR-C02, MR-A18 plus Book 03 | Book 03 / execution-capable service | 23–25 |
| transmission | MR-E01, MR-E02 | route and Execution Evidence | 15, 23, 24 |
| Provider Report | MR-E03 | identified provider | 21, 23 |
| official acknowledgement | MR-E04 | official authority or verified official Evidence | 23, 24, 29 |
| official lifecycle | MR-E05, MR-E08, MR-E09, MR-B01 | official authority | 10, 26, 27, 30, 33 |
| professional interpretation | MR-D02, MR-A19–A24, MR-C03–C06 | eligible professional | 04, 09, 17, 27 |
| client Projection | MR-A13, MR-V01, MR-V02, MR-A25 | controlled Product View | 10, 26, 29, 30 |
| continuing obligation | MR-B02, MR-B03, MR-E06 | official Rule, Source and assigned responsibility | 27, 31 |
| ownership and transaction | MR-C12, MR-C07–C09, MR-A27–A28, MR-V03 | parties, professional and official authority | 01, 12, 31, 32 |
| portfolio | MR-V04, MR-A29, MR-D10 | Product View plus per-right Decisions | 33, 39 |
| rule and Conformance | MR-G01–G10, MR-D12, MR-D13 | professional owner and governance | 36–41 |

## B.3 Key Distinctions

| Distinction | Controlled reading |
| --- | --- |
| applicant candidate vs official applicant/owner | MR-C12 records Product context; official records remain external |
| Recommendation vs Decision | MR-A03/A04 propose; MR-D01/D02 records accountable choice |
| readiness vs Approval | MR-A10 describes conditions; MR-D03 grants bounded authority |
| Approval vs Execution | MR-D03 permits exact action; MR-A17 and Book 03 coordinate it |
| sent vs delivered | MR-E01 may exist without MR-E02 |
| provider receipt vs acceptance | delivery does not establish MR-D05 |
| Provider Report vs official acknowledgement | MR-E03 requires reconciliation to MR-E04 |
| acknowledgement vs registration | MR-E04 does not prove MR-E08 |
| registration vs certificate | MR-E08 may exist without certificate availability |
| certificate vs current register | certificate may be stale; MR-B01 uses current verified Sources |
| renewal prepared vs approved vs renewed | MR-A26, MR-D08 and MR-E09 are separate |
| assignment signed vs owner updated | MR-C08, MR-C07 and MR-E09 remain separate |
| signal vs legal conclusion | monitoring opens Review; it does not create protected action |
| Product Session vs Matter | MR-C10 is interaction state, not formal Matter state |
| Return vs formal effect | MR-A30 returns references; receiving service consumes idempotently |
| detected Rule vs active Pack | MR-G04 requires MR-D12 before protected use |
| AI output vs professional conclusion | MR-G07 assists; MR-D02 remains accountable |
| publication vs production | publication state does not grant operational authority |

## B.4 Transition and Authority Matrix

| Transition | Prepare | Review / confirm | Authorize / accept | Minimum Evidence |
| --- | --- | --- | --- | --- |
| Business Context → Need Brief | Product or user | user / professional if material | user confirmation | MR-A01/A02 |
| applicant context → confirmed candidate | Product and user | professional where material | authorized client/owner | MR-C12, MR-D02 |
| Recommendation → selected option | Product/professional | professional | authorized client | MR-A03/A04, MR-D01/D02 |
| Quote → accepted | commercial surface | client verifies exact version | authorized client | MR-A06, MR-D01 |
| Intake → ready for Review | Product/coordinator | coordinator/professional | no external authority | MR-A08–A10 |
| Package → reviewed | professional preparer | eligible reviewer | MR-D02 | exact version and diff |
| reviewed Package → Filing Approval | Product requests | client/professional conditions | authorized approver | MR-D03 |
| provider candidate → selected | Product recommends | conflict/eligibility/availability | organization actor | MR-C01, MR-A14, MR-D04 |
| selected provider → accepted | organization instructs | provider checks | appointed provider | MR-A15/A16, MR-D05 |
| approved request → Execution | Product prepares | entry validation | active exact Approval | MR-A17 plus Book 03 |
| sent → official acknowledgement | route reports | reconciliation/verification | no Product authority | MR-E01–E04, MR-C02 |
| official notice → Context | Product ingests | professional verifies | responsibility assigned separately | MR-E05/E06, MR-C03–C06 |
| response option → strategy | Product/professional | professional/client where needed | MR-D06 | MR-A19–A21 |
| renewal Package → action | Product/professional | right, owner, fee and payment | MR-D08 | MR-B01/B02, MR-A26 |
| transaction → recordal | parties/professional | authority and title chain | MR-D09 | MR-C07/C08, MR-A27/A28 |
| Product result → Return | Product prepares | permission/version/destination | receiving service consumes | MR-C10, MR-A30 |
| Rule signal → Pack release | source process | Source/impact/professional Review | MR-D12 | MR-E07, MR-G01–G04 |
| evaluation → release Decision | Product team | Conformance and stop conditions | MR-D13 | MR-C11, MR-G08–G10 |

## B.5 Unknown and Correction States

Unknown, stale, conflicting or corrected states remain explicit. They trigger Source refresh, conservative Deadline handling, reconciliation, new exact-version Decision, access block or linked correction as applicable.

```text
Unknown ≠ failed
Unknown ≠ successful
Unknown ≠ safe to retry
```

## B.6 Client-Facing Labels

Preferred:

- `Provider reports submission — official receipt pending`;
- `Response sent — office acknowledgement pending`;
- `Registration verified — certificate file not yet available`;
- `Renewal request acknowledged — renewed register entry pending`;
- `Ownership documents signed — official recordal not yet verified`.

Generic `Filed`, `Registered`, `Renewed` or `Owner updated` is non-conforming when the required Evidence state is absent.

## B.7 PF-06D Reconciliation State

```text
State domains and transitions: RECONCILED
MR-C12 applicant/authority state: ADDED
Current Specification IDs: RECONCILED
Scenario references: RECONCILED
Client-facing labels: RECONCILED
Figures: OPEN — PF-07
Structural/rendered validation: OPEN — PF-08
```

Appendix B is a reader projection. It does not create authority, implementation or External Protected Action.
