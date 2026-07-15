# Appendix E — Priority Conformance Scenarios

**Status:** Controlled Reader Draft v0.3 — PF-06D Reconciled  
**Primary source:** B05-SPEC-0003 v0.3  
**Record authority:** B05-SPEC-0001 v0.3  
**Reader purpose:** provide a compact catalog of observable tests for MarkReg’s constitutional, lifecycle, participant and publication boundaries.

## E.1 Scenario Rule

```text
Given
→ When
→ Then
→ authority boundary
→ Evidence retained
→ pass or fail
```

A principle without observable behavior is not Conformance Evidence.

## E.2 Severity

| Severity | Meaning |
| --- | --- |
| standard | incomplete or confusing behavior without immediate protected external effect |
| high-risk | may create incorrect scope, Decision, disclosure, Package, Deadline or status |
| zero-tolerance | blocks the applicable Profile, pilot or release until corrected or safely reconciled |

## E.3 Controlled Scenario Index

### Identity, authority and scope

| ID | Scenario | Expected behavior | Key current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-01 | applicant or owner ambiguity | preserve sources and block affected action until resolved or reviewed | MR-C12, MR-D02 | high-risk |
| MR-SCN-02 | conflicting mark variant | create new filing-unit candidate and invalidate affected versions | MR-A03, MR-A08, MR-A11, MR-D03 | high-risk |
| MR-SCN-03 | country bundle hides territories | show independent routes, rights, costs and consequences | MR-A03, MR-A04 | standard |
| MR-SCN-04 | class uncertainty | separate primary, related, optional and unsupported candidates | MR-A03, MR-D02 | high-risk |
| MR-SCN-11 | signatory or authority expired | block exact action and request current authority Evidence | MR-C12, MR-D03, MR-D11, MR-V05 | zero-tolerance |
| MR-SCN-12 | chain-of-title gap | expose missing link and separate contractual and official ownership | MR-C08, MR-A28, MR-V03, MR-D09 | high-risk |
| MR-SCN-13 | business facts change | version Need Brief and identify affected downstream records | MR-A01–MR-A07 | high-risk |
| MR-SCN-14 | non-recommended option selected | preserve recommendation and record informed client Decision | MR-A03, MR-A04, MR-D01, MR-D02 | standard |

### Commercial, Documents and Approval

| ID | Scenario | Expected behavior | Key current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-05 | invalid POA | classify defect and block only affected readiness | MR-A09, MR-A10, MR-C12 | high-risk |
| MR-SCN-06 | expired Quote | prevent acceptance and require approved extension or repricing | MR-A06, MR-D01 | high-risk |
| MR-SCN-07 | official fee changes | show version impact and controlled variance path | MR-A06, MR-G01–MR-G04, MR-D01 | high-risk |
| MR-SCN-08 | payment missing | keep payment, professional readiness and Approval separate | MR-A10, MR-A12, MR-D03 | zero-tolerance where action is prohibited |
| MR-SCN-09 | professional override | permit only sourced, scoped and versioned eligible-Human override | MR-D02, MR-G02 | high-risk |
| MR-SCN-15 | duplicate payment risk | reconcile before retry using stable identity | MR-C02, MR-A18 | zero-tolerance |
| MR-SCN-16 | Package changes after Approval | show diff, invalidate affected Decisions and require new Approval | MR-A11, MR-D03 | zero-tolerance |
| MR-SCN-17 | Professional Review incomplete | block Approval unless a valid conditional path exists | MR-A10, MR-D02, MR-D03 | zero-tolerance |
| MR-SCN-18 | delegated Approval expired | block and route to eligible approver | MR-C12, MR-D03, MR-V05 | zero-tolerance |

### Provider, submission and recovery

| ID | Scenario | Expected behavior | Key current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-19 | provider conflict or unavailable | preserve failed candidate, show alternatives and require Human Selection | MR-C01, MR-A14, MR-D04 | high-risk |
| MR-SCN-20 | provider proposes material change | create new candidate and return to Review and Approval | MR-A16, MR-D05, MR-D02, MR-D03 | zero-tolerance |
| MR-SCN-21 | provider received but not accepted | show acceptance pending and block provider Execution | MR-E02, MR-D05 | high-risk |
| MR-SCN-22 | provider requests excessive access | deny outside accepted engagement and purpose | MR-A15, MR-A16, MR-D05, MR-V05 | zero-tolerance |
| MR-SCN-23 | technical success without official receipt | retain sent/provider state and reconcile | MR-E01–MR-E04, MR-C02 | zero-tolerance |
| MR-SCN-24 | retry may duplicate application | block blind retry while effect is unknown | MR-C02, MR-A18 | zero-tolerance |
| MR-SCN-25 | Return Envelope consumed twice | return existing reference and create no duplicate | MR-A12, MR-C10, MR-A30 | zero-tolerance |

### Official events, Communication and portfolio

| ID | Scenario | Expected behavior | Key current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-10 | official status stale | label stale and require refresh or verification | MR-E05, MR-E06 | zero-tolerance for protected action |
| MR-SCN-26 | official notice corrected | link versions and re-evaluate Deadlines, Decisions and Communications | MR-E05, MR-E06, MR-A25, MR-D11 | high-risk |
| MR-SCN-27 | conflicting Deadline advice | preserve sources, apply hierarchy and require verification | MR-E06, MR-G01–MR-G03, MR-D02 | zero-tolerance |
| MR-SCN-28 | client silence | escalate or use only a pre-authorized bounded default | MR-D01, MR-D07, MR-A25, MR-D11 | zero-tolerance |
| MR-SCN-29 | incorrect Communication | preserve original and issue linked correction | MR-A25, MR-D11 | high-risk |
| MR-SCN-30 | certificate conflicts with register | preserve certificate and use current source for Baseline | MR-E08, MR-V01, MR-B01 | high-risk |
| MR-SCN-31 | partial renewal or owner mismatch | expose dependency and require exact Renewal Approval | MR-B01, MR-B02, MR-C12, MR-A26, MR-D08 | high-risk |
| MR-SCN-32 | assignment signed but not recorded | separate contractual effect from official ownership | MR-C08, MR-C07, MR-A27, MR-V03, MR-E09 | high-risk |
| MR-SCN-33 | one challenged right | preserve independent right histories | MR-C05, MR-B01, MR-V04 | high-risk |

### Embedded experience, AI and publication claims

| ID | Scenario | Expected behavior | Key current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-34 | Lite private notes in Handoff | transfer only purpose-approved facts and Artifacts | MR-A12, MR-C10, MR-A30, MR-V05 | zero-tolerance |
| MR-SCN-35 | deep link in wrong organization | block content and require authorized context switch | MR-C10, MR-V05 | zero-tolerance |
| MR-SCN-36 | AI lacks valid Pack or sources | return research or verification need, not current-rule conclusion | MR-G01–MR-G03, MR-G06, MR-G07, MR-D02 | zero-tolerance |
| MR-SCN-37 | Organization Overlay conflicts with Pack | apply authoritative Rule and escalate conflict | MR-G01–MR-G05, MR-D12 | high-risk |
| MR-SCN-38 | faster journey creates defects | reject speed-only success claim | MR-G08, MR-G09, MR-C11, MR-D13 | high-risk |
| MR-SCN-39 | partial Profile claims Full-Lifecycle | correct Profile, scope, exclusions and authority statement | MR-G10, MR-D13 | high-risk |
| MR-SCN-40 | publication treated as production authority | block inference and require separate operational gates | MR-G09, MR-G10, MR-D13 | zero-tolerance |
| MR-SCN-41 | implementation redefines Core | record upstream finding and reject silent redefinition | MR-G10, MR-D13 | high-risk |

## E.4 Constitutional Rule Coverage

| Rule | Scenario coverage |
| --- | --- |
| MR-CR-01 — Recommendation is not Decision | 03, 04, 14, 39 |
| MR-CR-02 — readiness is not Approval | 05, 08, 17, 21 |
| MR-CR-03 — Approval is not Execution | 16, 18, 23, 40 |
| MR-CR-04 — submission is not official acknowledgement | 23, 24, 29, 31 |
| MR-CR-05 — projection is not Official Truth | 10, 26, 27, 30, 33 |
| MR-CR-06 — AI does not replace Human Review | 09, 18, 36, 37 |
| MR-CR-07 — Product-local records do not silently become formal objects | 25, 34, 35, 41 |
| MR-CR-08 — lineage, version, responsibility and supersession | 02, 13, 16, 26, 29, 32 |

## E.5 Profile Minimums

| Profile | Minimum scenario set |
| --- | --- |
| Foundation | 01, 09, 10, 11, 18, 22, 35, 36, 40, 41 |
| Guided Decision | Foundation plus 02, 03, 04, 13, 14 |
| Commercial Intake | Guided Decision plus 05, 06, 07, 08, 15, 28 |
| Filing Preparation | Commercial Intake plus 16, 17, 18, 19, 20 |
| Governed Filing | Filing Preparation plus 21, 22, 23, 24, 25 |
| Post-Filing | relevant earlier set plus 10, 23, 26, 27, 28, 29 |
| Portfolio Continuity | relevant earlier set plus 12, 30, 31, 32, 33 |
| Full-Lifecycle | every applicable scenario 01–41 |

Any applicable zero-tolerance failure blocks the Profile claim.

## E.6 Scenario Execution Record

A result retains Product and implementation version, declared Profile, Pack versions, scenario ID/version, participants, organization, test data classification, observed behavior, blocked/permitted action, Evidence, result, reviewer and re-test.

Fixture success is not production authorization.

## E.7 PF-06D Reconciliation State

```text
MR-SCN-01–MR-SCN-41 identities: PRESERVED
Behavior and severity: PRESERVED
Current record associations: RECONCILED
MR-C12 applicant/authority mapping: RECONCILED
Profile minimums: RECONCILED
PF-04/PF-05/PF-06 editorial work: COMPLETE
PF-08 validation: OPEN
```

B05-SPEC-0003 v0.3 remains authoritative. Appendix E does not authorize implementation, production deployment or External Protected Action.
