# Appendix E — Priority Conformance Scenarios

**Status:** Controlled Reader Draft — PF-04 Reconciled  
**Primary sources:** B05-SPEC-0003 v0.2 and chapter Given/When/Then scenarios  
**Reader purpose:** provide a compact catalog of observable tests for the constitutional, lifecycle, participant and publication boundaries of MarkReg.

## E.1 Scenario Rule

Every controlled test retains:

```text
Given
→ When
→ Then
→ authority boundary
→ evidence retained
→ pass or fail
```

A principle without observable behavior is not conformance evidence.

## E.2 Severity

| Severity | Meaning |
| --- | --- |
| standard | incomplete or confusing Product behavior without immediate protected external effect |
| high-risk | may create incorrect scope, Decision, disclosure, package, deadline or status |
| zero-tolerance | must block release or pilot continuation until corrected or safely reconciled |

Zero-tolerance failures include unauthorized external action, duplicate legal or financial effect, unsafe retry, unsourced official truth, confidential-data exposure, expired or wrong-version approval and AI or non-qualified actors replacing accountable Human roles.

## E.3 Controlled Scenario Index

### Identity and authority

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-01 | applicant or owner ambiguity | preserve sources, ask targeted question and block affected action | high-risk |
| MR-SCN-02 | conflicting mark variant | create new filing-unit candidate and invalidate affected downstream versions | high-risk |
| MR-SCN-11 | signatory or authority expired | block exact action and request current authority evidence | zero-tolerance where external action follows |
| MR-SCN-12 | chain-of-title gap | expose missing link and separate business, contractual and official ownership | high-risk |

### Recommendation and scope

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-03 | country bundle hides legal territories | show independent routes, rights, costs and consequences | standard |
| MR-SCN-04 | class uncertainty | separate primary, related, optional and unsupported candidates | high-risk |
| MR-SCN-13 | business facts change after recommendation | version Need Brief and identify affected recommendations, Quotes and packages | high-risk |
| MR-SCN-14 | client selects non-recommended option | preserve recommendation and record informed client Decision | standard |

### Commercial, payment and Documents

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-05 | invalid POA | classify defect and block only affected readiness | high-risk |
| MR-SCN-06 | expired Quote | prevent acceptance and require approved extension or repricing | high-risk |
| MR-SCN-07 | official fee changes after acceptance | show variance and apply controlled commercial path | high-risk |
| MR-SCN-08 | payment missing | keep payment, professional readiness and approval separate | zero-tolerance where action is prohibited |
| MR-SCN-15 | duplicate payment risk | reconcile before retry using stable identity | zero-tolerance |

### Review and approval

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-09 | professional override | permit only sourced, reasoned, scoped and versioned Human override | high-risk |
| MR-SCN-16 | package changes after confirmation or approval | show diff, invalidate affected Decisions and require new approval | zero-tolerance |
| MR-SCN-17 | Professional Review incomplete | block approval or use a defined conditional path | zero-tolerance |
| MR-SCN-18 | delegated approval expired | block and route to eligible approver | zero-tolerance |

### Provider and engagement

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-19 | provider conflict or unavailable | preserve failed candidate, show alternatives and require Human Selection | high-risk |
| MR-SCN-20 | provider proposes material change | create new candidate and return to Review and approval gates | zero-tolerance where action changes |
| MR-SCN-21 | provider received but not accepted | show acceptance pending and block provider execution | high-risk |
| MR-SCN-22 | provider requests excessive access | deny outside accepted purpose and engagement | zero-tolerance |

### Submission and duplicate safety

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-23 | technical success without official receipt | retain sent or provider-reported state and reconcile | zero-tolerance |
| MR-SCN-24 | retry may duplicate application | block blind retry while effect is unknown | zero-tolerance |
| MR-SCN-25 | Return Envelope consumed twice | return existing formal reference and create no duplicate | zero-tolerance |

### Official events, deadlines and Communication

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-10 | official status stale | label stale and require source refresh or verification | zero-tolerance for protected action |
| MR-SCN-26 | official notice corrected | link versions and re-evaluate deadlines, Decisions and Communications | high-risk |
| MR-SCN-27 | provider and official deadline conflict | preserve sources, use hierarchy and require professional verification | zero-tolerance |
| MR-SCN-28 | client silence before Decision | escalate or use only a previously authorized bounded default | zero-tolerance |
| MR-SCN-29 | incorrect client Communication | preserve original and issue linked correction | high-risk |

### Registration and portfolio continuity

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-30 | certificate conflicts with current register | preserve certificate evidence and use current source for Right Baseline | high-risk |
| MR-SCN-31 | partial renewal or owner mismatch | show dependency and require exact Renewal Approval | high-risk |
| MR-SCN-32 | assignment signed but not recorded | separate contractual effect from official ownership | high-risk |
| MR-SCN-33 | one challenged right in portfolio | preserve independent right histories | high-risk |

### Embedded experience, permission and AI

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-34 | Lite private notes in Handoff | transfer only purpose-approved facts and artifacts | zero-tolerance |
| MR-SCN-35 | deep link opened in wrong organization | block content and require authorized context switch | zero-tolerance |
| MR-SCN-36 | AI request lacks valid Pack or sources | return research or verification need, not current rule conclusion | zero-tolerance where action depends on it |
| MR-SCN-37 | organization overlay conflicts with Pack | apply authoritative rule and escalate overlay conflict | high-risk |

### Metrics, conformance and publication claims

| ID | Scenario | Expected Product behavior | Severity |
| --- | --- | --- | --- |
| MR-SCN-38 | faster journey creates more defects | reject speed-only success claim and investigate quality loss | high-risk |
| MR-SCN-39 | partial profile claims Full-Lifecycle | correct profile, scope, exclusions and authority statement | high-risk |
| MR-SCN-40 | publication treated as production authority | block inference and require separate operational gates | zero-tolerance |
| MR-SCN-41 | implementation redefines Core object | record Upstream Finding or Change Proposal | high-risk |

## E.4 Constitutional Rule Coverage

| Rule | Scenario coverage |
| --- | --- |
| MR-CR-01 — recommendation is not Decision | 03, 04, 14, 39 |
| MR-CR-02 — readiness is not approval | 05, 08, 17, 21 |
| MR-CR-03 — approval is not Execution | 16, 18, 23, 40 |
| MR-CR-04 — submission is not official acknowledgement | 23, 24, 29, 31 |
| MR-CR-05 — projection is not official truth | 10, 26, 27, 30, 33 |
| MR-CR-06 — AI does not replace Human Review | 09, 18, 36, 37 |
| MR-CR-07 — Product-local records do not silently become formal objects | 25, 34, 35, 41 |
| MR-CR-08 — lineage, version, responsibility and supersession | 02, 13, 16, 26, 29, 32 |

## E.5 Zero-Tolerance Set

The minimum zero-tolerance set is:

```text
MR-SCN-11 — expired authority
MR-SCN-15 — duplicate payment risk
MR-SCN-16 — approval applied to changed package
MR-SCN-17 — incomplete required Review
MR-SCN-18 — expired delegated approval
MR-SCN-20 — provider silently changes approved work
MR-SCN-22 — provider over-access
MR-SCN-23 — technical success represented as official receipt
MR-SCN-24 — unsafe retry
MR-SCN-25 — duplicate Return consumption
MR-SCN-27 — unverified deadline conflict
MR-SCN-28 — silence treated as authority
MR-SCN-34 — private Lite data over-transfer
MR-SCN-35 — wrong-organization access
MR-SCN-36 — AI current-rule conclusion without controlled sources
MR-SCN-40 — publication status treated as production authority
```

A declared profile cannot pass when one of its applicable zero-tolerance scenarios fails.

## E.6 Profile Minimums

| Profile | Required scenario families |
| --- | --- |
| Foundation | identity, authority, source, permission, AI and publication boundary |
| Guided Decision | Foundation plus recommendation and scope |
| Commercial Intake | Guided Decision plus Quote, payment and Documents |
| Filing Preparation | Commercial Intake plus Review, approval and provider-selection preparation |
| Governed Filing | Filing Preparation plus engagement, submission, unknown state and duplicate safety |
| Post-Filing | relevant prior families plus official events, deadlines and Communication |
| Portfolio Continuity | relevant prior families plus registration, renewal, ownership and portfolio independence |
| Full-Lifecycle | every applicable family and all zero-tolerance cases |

The exact IDs are controlled by B05-SPEC-0003 v0.2 and projected in Appendix G.

## E.7 Scenario Execution Record

A test result should retain:

- Product and implementation version;
- declared profile;
- jurisdiction and Pack versions;
- scenario ID and version;
- participant roles and organization context;
- test data classification;
- observed behavior;
- blocked or permitted action;
- evidence and audit references;
- pass, fail, conditional or not-applicable result;
- reviewer and re-test result.

Fixture success is not production authorization.

## E.8 Failing Conformance Examples

The following are automatically non-conforming:

- one generic status hides sent, provider-reported and official states;
- client confirmation is recorded as Professional Review;
- approval survives a material package change;
- provider receives organization-wide access by default;
- retry creates duplicate legal or payment effect;
- official deadline is shown without a current source basis;
- AI output is presented as approved professional advice;
- a partial implementation markets itself as Full-Lifecycle;
- Release Candidate publication status is represented as authority to file.

## E.9 Reconciliation Status

```text
MR-SCN-01–10 preserved: COMPLETE
MR-SCN-11–41 added: COMPLETE
Scenario families consolidated: COMPLETE
Duplicate scenarios removed or merged: COMPLETE
Zero-tolerance cases identified: COMPLETE
MR-CR coverage mapped: COMPLETE
Profile minimums mapped: COMPLETE
PF-04 Appendix E work: COMPLETE
PF-05 jurisdiction-specific tests: PENDING
PF-06 editorial compression: PENDING
PF-08 validation: PENDING
```

Appendix E is a controlled reader draft reconciled for PF-04. B05-SPEC-0003 remains authoritative if a conflict exists.