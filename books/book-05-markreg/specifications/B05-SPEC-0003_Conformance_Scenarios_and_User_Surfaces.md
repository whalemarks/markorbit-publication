# B05-SPEC-0003 — Conformance Scenarios and User-Surface Contract

## Status

- **Status:** Controlled Specification v0.3 — PF-06D Record-Reconciled
- **Applies to:** CH07–CH47
- **Supersedes:** Controlled Specification v0.2
- **Dependencies:** B05-SPEC-0001 v0.3, B05-SPEC-0002 v0.3, B05-TOC-V0.1 and MR-CR-01–MR-CR-08
- **Purpose:** make Product, authority, state, source and failure requirements observable.

## 1. Conformance Principle

```text
principle
→ scenario
→ observable surface behavior
→ authority boundary
→ retained Evidence
→ pass or fail
```

Scenarios test authority. They do not grant it.

## 2. Scenario Record Contract

Each scenario identifies stable ID, family, chapters, controlled records, Given/When condition, expected behavior, prohibited assumption, minimum Evidence, Profile applicability and severity.

Severity:

- **standard:** failure creates confusion or rework;
- **high-risk:** failure may create incorrect Decision, disclosure, Deadline, Package or status;
- **zero-tolerance:** failure may create unauthorized, duplicate, unsourced or unsafe external effect and blocks the applicable Profile, pilot or release.

## 3. Controlled Scenario Registry

| ID | Scenario | Required behavior | Current records | Severity |
| --- | --- | --- | --- | --- |
| MR-SCN-01 | Applicant ambiguity | preserve competing owner sources; require resolution or Professional Review before affected protected action | MR-C12, MR-C07, MR-C08, MR-B01, MR-D02 | high-risk |
| MR-SCN-02 | Conflicting mark variants | create a new filing-unit candidate and invalidate affected search, Quote, readiness, Package and Approval assumptions | MR-A03, MR-A08, MR-A11, MR-D02, MR-D03 | high-risk |
| MR-SCN-03 | Country-bundle comparison | compare territories, routes, fees, representation and consequences without merging rights | MR-A03, MR-A04 | standard |
| MR-SCN-04 | Class uncertainty | separate primary, related, optional and unsupported classes and require Review where material | MR-A03, MR-D02 | high-risk |
| MR-SCN-05 | Invalid POA | mark the Document invalid for its purpose, request replacement and block only affected readiness | MR-A09, MR-A10, MR-C12 | high-risk |
| MR-SCN-06 | Expired Quote | prevent acceptance and require repricing or authorized extension | MR-A06, MR-D01 | high-risk |
| MR-SCN-07 | Official-fee change after acceptance | assess version impact, disclose variance and require revised acceptance where policy requires | MR-A06, MR-G01, MR-G02, MR-G03, MR-G04, MR-D01 | high-risk |
| MR-SCN-08 | Missing payment | show professional readiness separately and keep commercial or Execution readiness blocked | MR-A10, MR-A12, MR-D03 | zero-tolerance |
| MR-SCN-09 | Professional override | allow only a reasoned, sourced, scoped and versioned eligible-Human override | MR-D02, MR-G02 | high-risk |
| MR-SCN-10 | Stale official status | label stale state and require source refresh or professional verification | MR-E05, MR-E06 | zero-tolerance |
| MR-SCN-11 | Signatory or representative authority expired | block only the affected action and request current authority Evidence | MR-C12, MR-D03, MR-D11, MR-V05 | zero-tolerance |
| MR-SCN-12 | Chain-of-title gap | expose missing links and separate contractual from official state | MR-C08, MR-A28, MR-V03, MR-D09 | high-risk |
| MR-SCN-13 | Material business change after recommendation | create a new Need Brief and identify all affected downstream versions | MR-A01–MR-A07 | high-risk |
| MR-SCN-14 | Client selects a non-recommended option | preserve recommendation and record informed client Decision with consequences | MR-A03, MR-A04, MR-D01, MR-D02 | standard |
| MR-SCN-15 | Duplicate payment risk | open reconciliation and block a second charge while state is unknown | MR-C02, MR-A18 | zero-tolerance |
| MR-SCN-16 | Package changed after confirmation or Approval | show material diff, invalidate prior Review or Approval and require a new exact-version Decision | MR-A11, MR-D03 | zero-tolerance |
| MR-SCN-17 | Incomplete Professional Review | block Filing Approval until required issues, Evidence and sources are resolved or a valid conditional path exists | MR-A10, MR-D02, MR-D03 | zero-tolerance |
| MR-SCN-18 | Delegated Approval expires | block out-of-scope Approval and route to an eligible approver | MR-C12, MR-D03, MR-V05 | zero-tolerance |
| MR-SCN-19 | Provider conflict or unavailability | preserve failed candidate, show eligible alternatives and require Human Selection | MR-C01, MR-A14, MR-D04 | high-risk |
| MR-SCN-20 | Provider proposes a material change | create a new candidate and return it to professional, client and Approval gates | MR-A16, MR-D05, MR-D02, MR-D03 | zero-tolerance |
| MR-SCN-21 | Provider receipt without acceptance | show received—acceptance pending and block provider Execution | MR-E02, MR-D05 | high-risk |
| MR-SCN-22 | Provider over-access | deny excess fields and preserve accepted purpose and engagement scope | MR-A15, MR-A16, MR-D05, MR-V05 | zero-tolerance |
| MR-SCN-23 | Technical success without official receipt | show sent or provider-reported state, open reconciliation and do not claim official filing | MR-E01–MR-E04, MR-C02 | zero-tolerance |
| MR-SCN-24 | Unsafe retry could duplicate an application | block blind retry and reconcile using stable identity and Evidence | MR-C02, MR-A18 | zero-tolerance |
| MR-SCN-25 | Return Envelope consumed twice | return the existing reference and create no duplicate Order, Matter, payment or action | MR-A12, MR-C10, MR-A30 | zero-tolerance |
| MR-SCN-26 | Corrected official notice | link both versions, recalculate Deadlines and re-evaluate affected Decisions, Packages and Communications | MR-E05, MR-E06, MR-A25, MR-D11 | high-risk |
| MR-SCN-27 | Conflicting deadline advice | preserve both sources, apply hierarchy, use conservative internal target and require verification | MR-E06, MR-G01, MR-G02, MR-G03, MR-D02 | zero-tolerance |
| MR-SCN-28 | Client silence before required Decision | escalate or apply only a previously authorized bounded default; otherwise keep blocked | MR-D01, MR-D07, MR-A25, MR-D11 | zero-tolerance |
| MR-SCN-29 | Corrected client Communication | preserve original, issue linked correction and record delivery and acknowledgement separately | MR-A25, MR-D11 | high-risk |
| MR-SCN-30 | Certificate differs from current official record | preserve certificate as Evidence, prefer current verified data and expose the diff | MR-E08, MR-V01, MR-B01 | high-risk |
| MR-SCN-31 | Partial renewal or owner mismatch | show scope reduction or ownership dependency and require exact-version Renewal Approval | MR-B01, MR-B02, MR-C12, MR-A26, MR-D08 | high-risk |
| MR-SCN-32 | Assignment signed but not recorded | show contractual effect and official recordal state separately | MR-C08, MR-C07, MR-A27, MR-V03, MR-E09 | high-risk |
| MR-SCN-33 | One challenged right in a portfolio | preserve the challenged right’s Context without changing unrelated rights | MR-C05, MR-B01, MR-V04 | high-risk |
| MR-SCN-34 | Lite private note handed to Workplace | transfer only purpose-approved facts and Artifacts; keep private notes local | MR-A12, MR-C10, MR-A30, MR-V05 | zero-tolerance |
| MR-SCN-35 | Deep link opened in wrong organization | block protected content and require an authorized context switch | MR-C10, MR-V05 | zero-tolerance |
| MR-SCN-36 | AI request lacks valid Pack or sources | produce a research or verification request rather than a current legal conclusion | MR-G01, MR-G02, MR-G03, MR-G06, MR-G07, MR-D02 | zero-tolerance |
| MR-SCN-37 | Organization Overlay conflicts with active Rule | preserve both sources, apply the authoritative Rule and escalate the conflict | MR-G01–MR-G05, MR-D12 | high-risk |
| MR-SCN-38 | Faster journey creates more defects | reject speed-only success claim and investigate quality loss | MR-G08, MR-G09, MR-C11, MR-D13 | high-risk |
| MR-SCN-39 | Partial profile claims Full-Lifecycle | require accurate Profile, exclusions and authority limits | MR-G10, MR-D13 | high-risk |
| MR-SCN-40 | Publication status treated as production authority | block the inference and require separate implementation, operational and protected-action gates | MR-G09, MR-G10, MR-D13 | zero-tolerance |
| MR-SCN-41 | Local implementation redefines a Core object | record an upstream finding and reject silent local redefinition | MR-G10, MR-D13 | high-risk |

## 4. Constitutional Rule Coverage

| Rule | Minimum scenarios |
| --- | --- |
| MR-CR-01 — Recommendation is not Decision | 03, 04, 14, 39 |
| MR-CR-02 — readiness is not Approval | 05, 08, 17, 21 |
| MR-CR-03 — Approval is not Execution | 16, 18, 23, 40 |
| MR-CR-04 — submission is not official acknowledgement | 23, 24, 29, 31 |
| MR-CR-05 — projection is not Official Truth | 10, 26, 27, 30, 33 |
| MR-CR-06 — AI does not replace Human Review | 09, 18, 36, 37 |
| MR-CR-07 — Product-local records do not silently become formal objects | 25, 34, 35, 41 |
| MR-CR-08 — lineage, version, responsibility and supersession | 02, 13, 16, 26, 29, 32 |

Every Profile tests at least one negative or blocked path for each constitutional Rule it consumes.

## 5. Participant and Surface Contract

Every material surface identifies:

- represented organization or personal context;
- participant identity and active role;
- client, applicant, owner, portfolio or Matter reference;
- purpose and Product journey;
- exact Artifact version;
- source and freshness where status or Rule is shown;
- visible authority and action rights;
- consequence, next participant or Return route;
- blockers, expiry and unresolved uncertainty.

### Participant classes

| Participant | Primary contribution | Prohibited assumption |
| --- | --- | --- |
| client contact | business facts and client Decisions | Professional Review or Filing Approval |
| applicant or owner representative | identity, ownership and authority Evidence | authority beyond represented entity |
| professional | judgment, strategy and governed work | client commercial authority automatically |
| reviewer | quality, source, Evidence, scope and risk Review | Execution or provider appointment |
| approver | bounded exact-version Approval | silent editing of approved record |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy by default |
| account owner | relationship and commercial continuity | legal or filing authority automatically |
| finance participant | payment, payable, tax and refund facts | unrelated Evidence or strategy access |
| provider | accepted engagement work and return Evidence | portfolio- or organization-wide access |
| administrator | role and policy configuration | silent impersonation |
| AI assistant | extraction, comparison, draft and explanation | identity, permission, Review, Approval or external authority |

Visibility is field-, purpose-, organization- and relationship-specific. `MR-V05 Participant Surface Projection` does not grant action rights.

## 6. Role Switching and Delegation

Each material action records active role, represented organization or party, authority basis, exact action, scope, version, time, expiry and conflict state.

Delegation cannot create qualification, client authority, provider appointment or organization relationship that does not otherwise exist.

## 7. Lifecycle Surface Matrix

| Range | Primary surface question | Required distinction |
| --- | --- | --- |
| CH07–CH15 | where am I and what should be protected? | Product, formal, Execution and official state; recommendation and Decision |
| CH16–CH22 | what am I buying and what remains missing? | Proposal, Quote, acceptance, instruction, payment, Intake, readiness and Handoff |
| CH23–CH29 | what version will be acted on and what happened externally? | candidate, Review, Approval, routing, acceptance, sent, acknowledgement and unknown |
| CH30–CH36 | what did the office or opponent do and what should follow? | source, Issue, strategy, Package, Deadline, settlement and closure |
| CH37–CH42 | what right exists and what remains due? | registration, certificate, Baseline, renewal, recordal, transaction and portfolio |
| CH43–CH47 | what context, participant, Rule, metric and Profile is actually supported? | Session, Return, visibility, Pack, AI, pilot, Conformance and authority gates |

## 8. Communication Contract

```text
draft
→ reviewed draft
→ approved Communication
→ sent
→ delivered
→ failed
→ acknowledged
→ corrected or superseded
```

Correction links to the original. It does not overwrite sent history.

## 9. Embedded, Cross-Product and AI Contract

A Handoff or Return surface shows source, destination, purpose, permission, inherited sources, accepted/stale/conflicting context, journey version, expected Return, expiry and correlation identity.

A URL or deep link does not carry authority.

AI output is visibly classified as extraction, comparison, explanation, recommendation, Rule-change, evaluation or anomaly candidate. It identifies source context, Pack/Rule version, uncertainty, Human disposition and prohibited use.

## 10. Minimum Scenario Sets by Conformance Profile

| Profile | Minimum required scenarios |
| --- | --- |
| Foundation | 01, 09, 10, 11, 18, 22, 35, 36, 40, 41 |
| Guided Decision | Foundation plus 02, 03, 04, 13, 14 |
| Commercial Intake | Guided Decision plus 05, 06, 07, 08, 15, 28 |
| Filing Preparation | Commercial Intake plus 16, 17, 18, 19, 20 |
| Governed Filing | Filing Preparation plus 21, 22, 23, 24, 25 |
| Post-Filing | relevant earlier scenarios plus 10, 23, 26, 27, 28, 29 |
| Portfolio Continuity | relevant earlier scenarios plus 12, 30, 31, 32, 33 |
| Full-Lifecycle | all applicable scenarios 01–41 |

Any applicable zero-tolerance failure blocks the Profile claim.

## 11. PF-06D Reconciliation State

```text
MR-SCN-01–MR-SCN-41 identities: PRESERVED
Scenario behavior and severity: PRESERVED
Current B05-SPEC-0001 IDs: RECONCILED
MR-C12 applicant and authority scenarios: RECONCILED
Participant Surface Projection: RECONCILED
Appendix E projection: RECONCILED UNDER PF-06D
Architecture Canon or Books 02–04 amendment required: NO
```

This specification does not authorize implementation, production deployment or External Protected Action.
