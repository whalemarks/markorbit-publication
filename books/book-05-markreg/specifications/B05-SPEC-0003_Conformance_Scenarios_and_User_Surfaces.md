# B05-SPEC-0003 — Conformance Scenarios and User-Surface Contract

## Status

- **Status:** Controlled Specification v0.2 — Full-Lifecycle Scenario and Surface Reconciliation
- **Applies to:** CH07–CH47
- **Workstream:** PF-04
- **Purpose:** Convert MarkReg constitutional rules, lifecycle controls and participant boundaries into observable behavior and minimum conformance tests
- **Controlled dependencies:** B05-SPEC-0001 v0.2, B05-SPEC-0002 v0.2, B05-TOC-V0.1 and MR-CR-01 through MR-CR-08

## 1. Conformance Principle

A Product statement is not sufficient unless its behavior can be observed.

```text
principle
→ scenario
→ expected surface behavior
→ authority boundary
→ retained evidence
→ pass or fail result
```

Conformance scenarios do not grant authority. They test whether the Product preserves authority correctly.

## 2. Scenario Record Contract

Every controlled scenario must identify:

| Field | Requirement |
| --- | --- |
| scenario ID | stable `MR-SCN-*` identifier |
| family | risk and lifecycle category |
| source chapters | chapters that define the behavior |
| controlled records | relevant B05-SPEC-0001 identifiers |
| participants | actors whose views or actions are tested |
| Given | observable precondition |
| When | triggering action or event |
| Then | required Product behavior |
| authority boundary | action or conclusion the Product must not assume |
| evidence retained | minimum audit, source and version evidence |
| external-action result | permitted, blocked, pending Review or not applicable |
| profile applicability | minimum conformance profiles that must test it |
| severity | standard, high-risk or zero-tolerance |

A scenario version changes when its expected behavior, authority boundary or minimum evidence changes materially.

## 3. Severity and Failure Classes

### 3.1 Standard

Failure creates confusion, rework or incomplete Product behavior but does not by itself create a protected external effect.

### 3.2 High-risk

Failure may create an incorrect decision, disclosure, deadline, package or official-state claim.

### 3.3 Zero-tolerance

The following are release or pilot stop conditions:

- external action without active exact-version approval;
- duplicate legal or financial effect;
- official status or deadline represented without sufficient source evidence;
- confidential evidence or private organization information exposed outside purpose;
- AI, administrator, coordinator or client acting as an eligible professional without recorded authority;
- provider or participant access beyond the accepted engagement or organization context;
- approval applied to a superseded artifact;
- unsafe retry while external effect is unknown.

A zero-tolerance scenario may pass only when the protected effect is blocked or safely reconciled.

## 4. Controlled Scenario Registry

Existing IDs `MR-SCN-01` through `MR-SCN-10` are preserved.

### Family A — Identity, Applicant and Authority

#### MR-SCN-01 — Applicant ambiguity

- **Given:** the selected operating subsidiary conflicts with portfolio evidence showing the parent as owner.
- **When:** recommendation, Intake, renewal or recordal reaches identity confirmation.
- **Then:** preserve both sources, show affected work, ask the smallest material question and block the affected protected action until resolved or professionally reviewed.
- **Boundary:** MarkReg does not choose the owner.
- **Evidence:** source records, user answer, professional Decision and affected versions.
- **Chapters / records:** CH12, CH39–CH41; MR-C07, MR-C08, MR-B01, MR-D02.
- **Severity:** high-risk.

#### MR-SCN-02 — Conflicting mark variants

- **Given:** a logo differs from the variant used in the approved Proposal or search.
- **When:** Intake or Filing Package validation occurs.
- **Then:** create a new filing-unit candidate and invalidate affected search, Quote, package and readiness assumptions.
- **Boundary:** visual comparison is not Filing Approval.
- **Evidence:** both files, comparison, user selection and reviewer disposition.
- **Chapters / records:** CH11, CH15, CH19, CH23; MR-A03, MR-A08, MR-A11, MR-D02.
- **Severity:** high-risk.

#### MR-SCN-11 — Signatory or representative authority expired

- **Given:** a signatory, delegation or representative appointment has expired or lacks scope.
- **When:** a Document, approval or Communication is requested.
- **Then:** block only the affected action and identify the authority evidence required.
- **Boundary:** role membership is not current authority.
- **Evidence:** role, delegation, expiry, attempted action and replacement authority.
- **Chapters / records:** CH05, CH20, CH24, CH44; MR-D03, MR-G06.
- **Severity:** zero-tolerance where external action would follow.

#### MR-SCN-12 — Chain-of-title gap

- **Given:** current business ownership cannot be connected to the official owner through a complete transaction chain.
- **When:** renewal, recordal, licensing or portfolio advice is prepared.
- **Then:** expose the missing link, separate contractual and official state and block unsupported ownership claims.
- **Boundary:** missing ownership evidence is not filled by inference.
- **Evidence:** known links, missing link, affected rights and professional Decision.
- **Chapters / records:** CH39–CH42; MR-C08, MR-A28, MR-V03, MR-D09.
- **Severity:** high-risk.

### Family B — Recommendation and Scope

#### MR-SCN-03 — Country-bundle comparison

- **Given:** the user requests “Europe” without specifying legal territories.
- **When:** jurisdiction options are prepared.
- **Then:** compare EU, UK and relevant national routes with separate scope, fees, representation and consequences.
- **Boundary:** a bundle is not one legal right.
- **Evidence:** jurisdictions considered, assumptions, source versions and selected option.
- **Chapters / records:** CH09–CH10; MR-A03, MR-A04.
- **Severity:** standard.

#### MR-SCN-04 — Class uncertainty

- **Given:** a business spans hardware, software and online retail.
- **When:** class candidates are generated.
- **Then:** separate primary, related, optional and unsupported classes and require Review where material.
- **Boundary:** automated classification is not final professional advice.
- **Evidence:** business description, class source, confidence and reviewer changes.
- **Chapters / records:** CH13; MR-A03, MR-D02.
- **Severity:** high-risk.

#### MR-SCN-13 — Material business change after recommendation

- **Given:** launch markets, products or timing change after a Recommendation Set is reviewed.
- **When:** the user edits the business objective.
- **Then:** create a new Need Brief version and identify affected jurisdiction, scope, search, Quote and package records.
- **Boundary:** prior acceptance does not silently apply to new facts.
- **Evidence:** old and new facts, dependency impact and supersession links.
- **Chapters / records:** CH08–CH18; MR-A02–MR-A07, MR-G05.
- **Severity:** high-risk.

#### MR-SCN-14 — Client selects a non-recommended option

- **Given:** the client chooses an option that the professional marked higher risk or lower coverage.
- **When:** the selection is confirmed.
- **Then:** preserve the recommendation, record the informed client Decision and carry explicit consequences forward.
- **Boundary:** Product recommendation is not the client Decision.
- **Evidence:** options, explanation, Decision actor, time and affected scope.
- **Chapters / records:** CH09–CH16; MR-A03, MR-A04, MR-D01, MR-D02.
- **Severity:** standard.

### Family C — Quote, Acceptance and Payment

#### MR-SCN-05 — Invalid POA

- **Given:** a POA has an unauthorized signatory or unacceptable execution form.
- **When:** Document validation occurs.
- **Then:** mark it invalid for the stated purpose, identify a replacement and block only the affected readiness dimension.
- **Boundary:** upload does not establish legal validity.
- **Evidence:** original file, rule version, defect, replacement request and accepted version.
- **Chapters / records:** CH20–CH21; MR-A09, MR-A10.
- **Severity:** high-risk.

#### MR-SCN-06 — Expired Quote

- **Given:** acceptance is attempted after Quote validity expires.
- **When:** the client submits acceptance.
- **Then:** prevent acceptance, preserve the attempt and require repricing or an authorized extension.
- **Boundary:** Product workflow cannot extend commercial validity.
- **Evidence:** Quote version, expiry, attempted acceptance and revised terms.
- **Chapters / records:** CH17–CH18; MR-A06, MR-D01.
- **Severity:** high-risk.

#### MR-SCN-07 — Official-fee change after acceptance

- **Given:** an official fee changes after acceptance but before action.
- **When:** the active Pack changes.
- **Then:** assess Quote terms, show variance and require revised acceptance where policy requires.
- **Boundary:** no silent repricing.
- **Evidence:** old and new sources, Quote terms, variance and Decision.
- **Chapters / records:** CH17–CH18, CH39, CH45; MR-A06, MR-G04, MR-D01.
- **Severity:** high-risk.

#### MR-SCN-08 — Missing payment

- **Given:** professional work is ready but required payment is not confirmed.
- **When:** readiness or Execution entry is assessed.
- **Then:** show professional readiness separately and keep commercial or Execution readiness blocked.
- **Boundary:** payment is not Filing Approval; approval is not payment.
- **Evidence:** terms, payment source, readiness and attempted action.
- **Chapters / records:** CH17–CH22, CH27; MR-A10, MR-A12, MR-D03.
- **Severity:** zero-tolerance where unpaid action is prohibited.

#### MR-SCN-15 — Duplicate payment risk

- **Given:** a timeout occurs after a payment request may have been accepted.
- **When:** retry is requested.
- **Then:** open reconciliation, preserve the stable identity and block a second charge until state is known.
- **Boundary:** technical uncertainty is not payment failure.
- **Evidence:** request identity, gateway evidence, timestamps and reconciliation result.
- **Chapters / records:** CH17, CH29; MR-C02, MR-A18.
- **Severity:** zero-tolerance.

### Family D — Review, Approval and Package Integrity

#### MR-SCN-09 — Professional override

- **Given:** a controlled rule warns that an item is unacceptable.
- **When:** an eligible professional confirms a sourced exception.
- **Then:** allow a reasoned, scoped and versioned override with expiry or revalidation conditions.
- **Boundary:** only authorized Human Review may override the rule.
- **Evidence:** warning, source, reviewer, reason, scope and expiry.
- **Chapters / records:** CH13–CH15, CH21, CH45; MR-D02, MR-G02.
- **Severity:** high-risk.

#### MR-SCN-16 — Package changed after confirmation or approval

- **Given:** a mark file, applicant, goods/services item, route or fee changes after confirmation or Filing Approval.
- **When:** the changed package is opened or sent.
- **Then:** show the material diff, invalidate affected Review or approval and require a new exact-version Decision.
- **Boundary:** approval never floats to a changed package.
- **Evidence:** prior and new versions, diff, invalidation and new Decisions.
- **Chapters / records:** CH23–CH24, CH32, CH39–CH40; MR-A11, MR-D03, MR-G05.
- **Severity:** zero-tolerance.

#### MR-SCN-17 — Incomplete Professional Review

- **Given:** required issues, evidence or source checks remain unresolved.
- **When:** Filing Approval is requested.
- **Then:** show incomplete Review and block approval unless a defined conditional path is valid.
- **Boundary:** structural completeness is not Professional Review.
- **Evidence:** checklist, unresolved items, reviewer and Decision state.
- **Chapters / records:** CH21, CH24, CH32; MR-A10, MR-D02, MR-D03.
- **Severity:** zero-tolerance.

#### MR-SCN-18 — Delegated approval expires

- **Given:** approval authority was delegated for a limited time or scope.
- **When:** the delegate attempts to approve outside that limit.
- **Then:** block approval and route to an eligible approver.
- **Boundary:** delegation cannot create qualification or unlimited authority.
- **Evidence:** delegation, scope, expiry and attempted action.
- **Chapters / records:** CH24, CH44; MR-D03, MR-G06.
- **Severity:** zero-tolerance.

### Family E — Provider Routing, Access and Engagement

#### MR-SCN-19 — Provider conflict or unavailability

- **Given:** the preferred provider has a conflict or cannot meet the required timeline.
- **When:** routing is reviewed.
- **Then:** preserve the failed candidate, present eligible alternatives and require Human Selection.
- **Boundary:** recommendation is not appointment.
- **Evidence:** Capability Need, eligibility, conflict, availability and Selection.
- **Chapters / records:** CH25–CH26; MR-C01, MR-A14, MR-D04.
- **Severity:** high-risk.

#### MR-SCN-20 — Provider proposes a material change

- **Given:** an instructed provider proposes a material scope, wording, route or deadline change.
- **When:** the proposal is received.
- **Then:** create a new candidate version and return it to professional, client and approval gates as applicable.
- **Boundary:** provider advice cannot silently mutate approved scope.
- **Evidence:** provider proposal, reason, affected package and Decisions.
- **Chapters / records:** CH26–CH27, CH32, CH39; MR-A16, MR-D05, MR-D02, MR-D03.
- **Severity:** zero-tolerance where protected action would change.

#### MR-SCN-21 — Provider receipt without acceptance

- **Given:** delivery is confirmed but the provider has not accepted the engagement.
- **When:** the Product evaluates execution readiness.
- **Then:** show `received — acceptance pending` and block provider execution.
- **Boundary:** delivery and Provider Acceptance are different states.
- **Evidence:** delivery, provider response and acceptance Decision.
- **Chapters / records:** CH26–CH28; MR-E02, MR-D05.
- **Severity:** high-risk.

#### MR-SCN-22 — Provider over-access

- **Given:** a provider appointed for one Matter requests unrelated client, portfolio or margin data.
- **When:** access is evaluated.
- **Then:** deny the excess access and preserve the accepted purpose and engagement scope.
- **Boundary:** provider relationship is purpose-limited.
- **Evidence:** requested fields, engagement, policy and access Decision.
- **Chapters / records:** CH26, CH44; MR-G06.
- **Severity:** zero-tolerance.

### Family F — Submission, Unknown State and Duplicate Safety

#### MR-SCN-23 — Technical success without official receipt

- **Given:** a connector or provider reports technical success without official acknowledgement.
- **When:** filing state is displayed or retry is considered.
- **Then:** show sent or provider-reported state, open reconciliation and do not claim official filing.
- **Boundary:** submission is not official acknowledgement.
- **Evidence:** request, transmission, provider report, source search and final reconciliation.
- **Chapters / records:** CH28–CH29; MR-E01–MR-E04, MR-C02.
- **Severity:** zero-tolerance.

#### MR-SCN-24 — Unsafe retry could duplicate an application

- **Given:** external effect is unknown after timeout.
- **When:** retry is requested.
- **Then:** block blind retry and reconcile using stable idempotency and official or provider evidence.
- **Boundary:** unknown is not failed.
- **Evidence:** request identity, timestamps, search results and retry Decision.
- **Chapters / records:** CH29; MR-C02, MR-A18.
- **Severity:** zero-tolerance.

#### MR-SCN-25 — Return Envelope consumed twice

- **Given:** a receiving Product already consumed a Return Envelope.
- **When:** the same envelope is submitted again.
- **Then:** return the existing formal reference and create no duplicate Order, Matter or action.
- **Boundary:** Return does not create repeated formal effect.
- **Evidence:** envelope ID, correlation ID, first result and retry result.
- **Chapters / records:** CH22, CH43; MR-A12, MR-A30.
- **Severity:** zero-tolerance.

### Family G — Official Events, Deadlines and Communication

#### MR-SCN-10 — Stale official status

- **Given:** a status was retrieved too long ago for the current purpose.
- **When:** a deadline-sensitive journey is opened.
- **Then:** label it stale and require source refresh or professional verification.
- **Boundary:** Product projection is not current official truth.
- **Evidence:** source, retrieval time, refresh attempt and result.
- **Chapters / records:** CH30, CH36, CH38; MR-E05, MR-E06.
- **Severity:** zero-tolerance for protected action.

#### MR-SCN-26 — Corrected official notice

- **Given:** an official notice or event is corrected or superseded.
- **When:** the correction is captured.
- **Then:** link both versions, recalculate affected deadlines and re-evaluate Decisions, packages and Communications.
- **Boundary:** correction history is not overwritten.
- **Evidence:** prior and corrected source, affected records and new Decisions.
- **Chapters / records:** CH30–CH36; MR-E05, MR-E06, MR-A25.
- **Severity:** high-risk.

#### MR-SCN-27 — Conflicting deadline advice

- **Given:** provider advice conflicts with a current official source.
- **When:** a Deadline Record is prepared.
- **Then:** preserve both sources, apply hierarchy, use a conservative internal target and require professional verification.
- **Boundary:** provider statement is not official deadline authority.
- **Evidence:** sources, Pack version, calculation and reviewer Decision.
- **Chapters / records:** CH36, CH38, CH45; MR-E06, MR-G02, MR-D02.
- **Severity:** zero-tolerance.

#### MR-SCN-28 — Client silence before required Decision

- **Given:** a material client Decision is overdue.
- **When:** deadline or escalation policy is reached.
- **Then:** escalate or apply only a previously authorized bounded default; otherwise keep the action blocked.
- **Boundary:** silence is not approval, abandonment or settlement authority.
- **Evidence:** requests, delivery, policy, escalation and resulting Decision.
- **Chapters / records:** CH18, CH36, CH44; MR-D01, MR-D07, MR-A25.
- **Severity:** zero-tolerance where external action would follow.

#### MR-SCN-29 — Corrected client Communication

- **Given:** a sent Communication contains wrong scope, date or status.
- **When:** the error is identified.
- **Then:** preserve the original, issue a linked correction and record delivery and acknowledgement separately.
- **Boundary:** sent history is not rewritten.
- **Evidence:** original, correction, approval, recipients and delivery states.
- **Chapters / records:** CH29, CH36, CH44; MR-A25, MR-D11.
- **Severity:** high-risk.

### Family H — Registration, Renewal, Ownership and Portfolio

#### MR-SCN-30 — Certificate differs from current official record

- **Given:** a certificate file conflicts with current official scope, owner or status.
- **When:** the Right Baseline is prepared.
- **Then:** preserve the certificate as evidence, prefer current verified official data for the baseline and expose the difference.
- **Boundary:** certificate is not automatically the current register.
- **Evidence:** certificate, current source, diff and reviewer verification.
- **Chapters / records:** CH37; MR-E08, MR-B01, MR-V01.
- **Severity:** high-risk.

#### MR-SCN-31 — Partial renewal or owner mismatch

- **Given:** only part of the registered scope will be renewed or the official owner is inconsistent.
- **When:** a Renewal Package is prepared.
- **Then:** show the scope reduction or ownership dependency and require exact-version Renewal Approval.
- **Boundary:** reminder, payment or package preparation is not renewal.
- **Evidence:** Right Baseline, obligation, package diff, owner sources and approval.
- **Chapters / records:** CH38–CH40; MR-B01, MR-B02, MR-A26, MR-D08.
- **Severity:** high-risk.

#### MR-SCN-32 — Assignment signed but not recorded

- **Given:** transaction Documents are signed but official ownership has not changed.
- **When:** portfolio, renewal or provider instructions are displayed.
- **Then:** show contractual effect and official recordal state separately.
- **Boundary:** signed assignment is not recorded ownership.
- **Evidence:** transaction, effective date, recordal package and official source.
- **Chapters / records:** CH40–CH41; MR-C08, MR-A27, MR-V03, MR-E09.
- **Severity:** high-risk.

#### MR-SCN-33 — One challenged right in a portfolio

- **Given:** one registration is challenged while other rights remain active.
- **When:** a Portfolio Continuity View is generated.
- **Then:** preserve the challenged right’s Adversarial Context without changing unrelated rights.
- **Boundary:** portfolio aggregation does not create one global legal state.
- **Evidence:** independent Right Baselines, dispute source and view mapping.
- **Chapters / records:** CH35, CH42; MR-C05, MR-B01, MR-V04.
- **Severity:** high-risk.

### Family I — Embedded Experience, Permission and AI

#### MR-SCN-34 — Lite private note handed to Workplace

- **Given:** a Lite case contains personal notes and approved client facts.
- **When:** the journey is handed into an organization Workplace.
- **Then:** transfer only purpose-approved facts and artifacts; keep personal notes local.
- **Boundary:** local context is not organization truth or automatically transferable.
- **Evidence:** Handoff scope, included and excluded fields and user instruction.
- **Chapters / records:** CH43; MR-A12, MR-C10.
- **Severity:** zero-tolerance for private-data exposure.

#### MR-SCN-35 — Deep link opened in wrong organization

- **Given:** an authorized user opens a link while active in another organization context.
- **When:** access is evaluated.
- **Then:** block protected content and require an authorized context switch.
- **Boundary:** identity alone is not organization permission.
- **Evidence:** expected and active organization, role, purpose and access result.
- **Chapters / records:** CH43–CH44; MR-C10, MR-G06.
- **Severity:** zero-tolerance.

#### MR-SCN-36 — AI request lacks valid Pack or sources

- **Given:** AI is asked for a current jurisdiction rule without an active Pack or source set.
- **When:** the task is evaluated.
- **Then:** produce a research or verification request rather than a current legal conclusion.
- **Boundary:** model memory is not current law or Professional Review.
- **Evidence:** task context, missing sources, output classification and Human disposition.
- **Chapters / records:** CH45; MR-G01–MR-G07, MR-D02.
- **Severity:** zero-tolerance where protected action depends on the answer.

#### MR-SCN-37 — Organization overlay conflicts with active rule

- **Given:** organization policy permits an action the active Jurisdiction Pack blocks.
- **When:** readiness or package generation occurs.
- **Then:** preserve both sources, apply the authoritative rule and escalate the overlay conflict.
- **Boundary:** organization custom is not law.
- **Evidence:** Pack version, overlay version, conflict and Decision.
- **Chapters / records:** CH45; MR-G01–MR-G04, MR-D12.
- **Severity:** high-risk.

### Family J — Metrics, Conformance and Publication Claims

#### MR-SCN-38 — Faster journey creates more defects

- **Given:** a new interaction reduces completion time but increases late blockers or package corrections.
- **When:** Product performance is reviewed.
- **Then:** reject the speed-only success claim and investigate the quality loss.
- **Boundary:** activity or speed is not Product quality.
- **Evidence:** metric definitions, segmented results, defects and release Decision.
- **Chapters / records:** CH46; MR-C11, MR-G08, MR-D13.
- **Severity:** high-risk.

#### MR-SCN-39 — Partial profile claims Full-Lifecycle

- **Given:** an implementation supports only Guided Decision or Commercial Intake.
- **When:** a conformance or marketing statement is published.
- **Then:** require the supported profile, exclusions and authority limits to be stated accurately.
- **Boundary:** feature presence is not Full-Lifecycle conformance.
- **Evidence:** implemented records, scenario results and declared profile.
- **Chapters / records:** CH47; MR-G10, MR-D13.
- **Severity:** high-risk.

#### MR-SCN-40 — Publication status treated as production authority

- **Given:** Book 05 reaches Complete Draft or Release Candidate status.
- **When:** a stakeholder attempts to infer deployment or filing authority.
- **Then:** block the inference and require separate implementation, operational and protected-action gates.
- **Boundary:** publication is not production authorization.
- **Evidence:** publication state, implementation conformance and authority Decision.
- **Chapters / records:** CH47; MR-G09, MR-G10, MR-D13.
- **Severity:** zero-tolerance.

#### MR-SCN-41 — Local implementation redefines a Core object

- **Given:** implementation proposes a local shared-object meaning inconsistent with Book 02.
- **When:** conformance review occurs.
- **Then:** record an Upstream Finding or Change Proposal and reject silent local redefinition.
- **Boundary:** Product implementation cannot amend frozen Core semantics.
- **Evidence:** proposed meaning, upstream baseline, conflict and disposition.
- **Chapters / records:** CH47; MR-G09, MR-G10.
- **Severity:** high-risk.

## 5. Constitutional Rule Coverage

| Rule | Required scenarios |
| --- | --- |
| MR-CR-01 — recommendation is not Decision | MR-SCN-03, 04, 14, 39 |
| MR-CR-02 — readiness is not approval | MR-SCN-05, 08, 17, 21 |
| MR-CR-03 — approval is not Execution | MR-SCN-16, 18, 23, 40 |
| MR-CR-04 — submission is not official acknowledgement | MR-SCN-23, 24, 29, 31 |
| MR-CR-05 — projection is not official truth | MR-SCN-10, 26, 27, 30, 33 |
| MR-CR-06 — AI does not replace Human Review | MR-SCN-09, 18, 36, 37 |
| MR-CR-07 — Product-local records do not silently become formal objects | MR-SCN-25, 34, 35, 41 |
| MR-CR-08 — lineage, version, responsibility and supersession | MR-SCN-02, 13, 16, 26, 29, 32 |

Every implementation profile must test the rules it consumes, including at least one negative or blocked-path case.

## 6. Participant and Surface Contract

### 6.1 Required Surface Context

Every material surface must identify:

- represented organization or personal context;
- participant identity and active role;
- client, applicant, owner, portfolio or Matter reference;
- purpose;
- Product journey and artifact version;
- source and freshness where status or rule is displayed;
- visible authority and action rights;
- requested action and consequence;
- next participant or return route;
- blockers, expiry and unresolved uncertainty.

### 6.2 Participant Classes

| Participant | Primary contribution | Prohibited assumption |
| --- | --- | --- |
| client contact | business facts and client Decisions | Professional Review or Filing Approval |
| applicant or owner representative | identity, ownership and authority evidence | authority beyond represented entity |
| professional | judgment, strategy and governed work | client commercial authority automatically |
| reviewer | quality, source, evidence, scope and risk Review | Execution or provider appointment |
| approver | bounded exact-version approval | power to edit the approved record silently |
| coordinator | collect, route, remind, reconcile and escalate | professional strategy authority by default |
| account owner | relationship and commercial continuity | legal or filing authority automatically |
| finance participant | payment, payable, tax and refund facts | access to unrelated evidence or strategy |
| provider | accepted engagement work and return evidence | portfolio-wide or organization-wide access |
| administrator | role and policy configuration | silent impersonation of accountable actors |
| AI assistant | extraction, comparison, draft and explanation | identity, permission, Review, approval or external authority |

### 6.3 Visibility Classes

- **client visible:** reviewed scope, options, client-facing price, status and decisions;
- **professional restricted:** legal analysis, evidence assessment, amendments and strategy;
- **organization private:** margin, provider comparison, internal policy and private Knowledge;
- **provider purpose-limited:** accepted instructions, required facts, Documents and return evidence;
- **finance restricted:** payment, tax, payable, refund and reconciliation data;
- **personal local:** Lite notes and personal learning;
- **official-source public:** sourced office data with retrieval context;
- **confidential evidence:** purpose- and participant-restricted evidence.

Visibility is field-, purpose-, organization- and relationship-specific.

### 6.4 Material Action Rights

| Action | Client | Professional / reviewer | Approver | Coordinator | Finance | Provider | Administrator | AI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| provide or correct facts | within authority | yes with source | no | collect or propose | payment facts | request or return task facts | no | extract or flag |
| choose commercial option | authorized client | advise | policy approval only | coordinate | confirm conditions | no | no | explain |
| create professional strategy | no | eligible professional | no | suggestion only | no | proposal within engagement | no | draft candidate |
| perform Professional Review | no | eligible reviewer | no | no | no | only if separately eligible and appointed | no | no |
| grant Filing Approval | no | only if separately authorized | yes | no | no | no | no | no |
| select provider | if organization policy permits | recommend or review | approve if required | coordinate | cost input | no | no | compare evidence |
| accept provider engagement | no | no unless provider role | no | no | no | appointed provider | no | no |
| execute protected action | no | through governed route | no | coordinate only | payment gate | accepted provider | no | no |
| verify official event | acknowledge | yes | no | reconcile | no | report with evidence | no | summarize source |
| send protected Communication | confirm or approve where required | prepare or approve if authorized | approve where required | send if authorized | financial only | engagement only | no | draft only |

The actual permission must also satisfy jurisdiction, qualification, organization policy, delegation, relationship and accepted engagement.

## 7. Role Switching and Delegation

When one person holds several roles, each material action records:

- active role;
- represented organization or party;
- authority basis;
- exact action;
- scope and version;
- time and expiry;
- conflict or independence state.

Delegation must record delegator, delegate, role, purpose, scope, start, expiry, subdelegation rule and acceptance.

Delegation cannot create professional qualification, client authority, provider appointment or organization relationship that does not otherwise exist.

## 8. Lifecycle Surface Matrix

| Chapters | Primary surface | Primary user question | Required visible distinction | Primary action |
| --- | --- | --- | --- | --- |
| CH07 | lifecycle orientation | where am I in the lifecycle? | Product, formal, Execution and official state | open the correct journey |
| CH08–CH10 | need and market strategy | what protection path is sensible? | business objective, recommendation and client Decision | confirm Need Brief or select option |
| CH11–CH15 | filing scope and risk | what exactly should be filed? | filing units, candidate scope, search and risk | confirm or request professional Review |
| CH16–CH18 | Proposal and commercial | what am I buying and accepting? | Proposal, Quote, acceptance, instruction and payment | accept exact version or request revision |
| CH19–CH22 | Intake and Handoff | what is missing and what happens next? | facts, Documents, readiness, approval and formal objects | resolve blocker or authorize Handoff |
| CH23–CH24 | package and approval | what version will be acted on? | candidate, Review, confirmation and approval | review, confirm or approve exact version |
| CH25–CH27 | provider and route | who may perform the work and by which route? | capability, recommendation, Selection, appointment and acceptance | select, appoint or accept |
| CH28–CH29 | submission and recovery | what happened externally? | sent, delivery, provider report, acknowledgement and unknown | reconcile, communicate or retry safely |
| CH30–CH32 | examination and response | what did the office raise and what should we do? | official source, Issue Set, strategy, package and Decision | select strategy, review or approve response |
| CH33–CH36 | publication and dispute | is there a challenge and what authority is required? | signal, proceeding, deadline, settlement and official closure | decide, approve, file or communicate |
| CH37–CH38 | registration and maintenance | what right exists and what remains due? | registration, certificate, Right Baseline and obligation | verify baseline or accept responsibility |
| CH39–CH41 | renewal, recordal and transaction | what must change or continue? | reminder, package, approval, contractual effect and official update | approve scoped action or resolve dependency |
| CH42 | portfolio | which rights need action and why? | independent rights, signals, risk and action candidates | select next portfolio action |
| CH43 | standalone and embedded | what context entered and where will the result return? | Product Session, Handoff, permission and Return | continue, pause or return typed result |
| CH44 | participant surfaces | what may this participant see or do? | visibility, role, delegation and action right | complete role-specific action |
| CH45 | jurisdiction and AI | which source and rule version supports this? | official source, Pack, overlay, provider advice and AI output | verify, Review, release or escalate rule |
| CH46 | metrics and MVP | is the Product safer and more useful? | speed, quality, safety, outcome and scope | approve next bounded increment |
| CH47 | conformance | what profile is actually supported? | publication, implementation, production and protected-action gates | publish an accurate conformance statement |

## 9. Communication Surface Contract

A Communication must distinguish:

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

Before sending, the surface must show recipients, purpose, language, confidentiality, source basis, attachments and approving role.

A correction must link to the original rather than overwrite it.

## 10. Embedded and Cross-Product Surface Contract

A Handoff or Return surface must show:

- source and destination Product or Workplace;
- purpose and permission scope;
- inherited facts and sources;
- accepted, stale, conflicting or excluded context;
- Product journey and artifact version;
- expected Return type;
- expiry;
- correlation and idempotency identity.

A URL or deep link does not carry authority by itself.

## 11. AI Surface Contract

AI output must be presented as one of:

- extraction candidate;
- comparison candidate;
- explanation draft;
- recommendation candidate;
- rule-change candidate;
- evaluation or anomaly candidate.

The surface must identify source context, Pack or rule version where relevant, uncertainty, Human disposition and prohibited use.

AI may not appear as client, professional, reviewer, approver, provider, official office or Owning Service.

## 12. Minimum Scenario Sets by Conformance Profile

| Profile | Minimum required scenario IDs |
| --- | --- |
| Foundation | 01, 09, 10, 11, 18, 22, 35, 36, 40, 41 |
| Guided Decision | Foundation plus 02, 03, 04, 13, 14 |
| Commercial Intake | Guided Decision plus 05, 06, 07, 08, 15, 28 |
| Filing Preparation | Commercial Intake plus 16, 17, 18, 19, 20 |
| Governed Filing | Filing Preparation plus 21, 22, 23, 24, 25 |
| Post-Filing | relevant earlier profiles plus 10, 23, 26, 27, 28, 29 |
| Portfolio Continuity | relevant earlier profiles plus 12, 30, 31, 32, 33 |
| Full-Lifecycle | all scenario families, including 34–41 |

A profile may require additional jurisdiction-specific tests under B05-SPEC-0004.

## 13. Scenario Execution Evidence

A conformance run should retain:

- Product and implementation version;
- declared profile;
- Jurisdiction Pack and rule versions;
- scenario version;
- test data classification;
- participant roles and organization context;
- observed behavior;
- blocked or permitted action;
- evidence and audit references;
- pass, fail, conditional or not-applicable result;
- reviewer;
- defect or Upstream Finding reference;
- re-test result.

Synthetic or fixture scenarios do not authorize production use.

## 14. Pass and Fail Rules

A scenario passes only when:

- required behavior is observable;
- prohibited authority is not assumed;
- source and version evidence is retained;
- participant visibility is purpose-limited;
- external action is blocked or permitted correctly;
- failure and correction behavior is testable.

A Product fails the declared profile when:

- a required zero-tolerance scenario fails;
- a required scenario is untested without documented exception;
- marketing or conformance claims exceed the tested scope;
- participant or AI surfaces hide responsibility;
- source, version or audit evidence cannot be produced.

## 15. Publication Projections

- Appendix B projects state domains, authority transitions and scenario references.
- Appendix C projects participant visibility and action rights.
- Appendix E projects the priority scenario catalog.
- Appendix G projects conformance profiles and minimum tests.

This specification governs if a publication projection conflicts with it.

## 16. PF-04 Completion Decision

```text
B05-SPEC-0003 applies through CH47: YES
Existing MR-SCN-01–10 preserved: YES
Scenario registry extended through MR-SCN-41: YES
Zero-tolerance cases identified: YES
Constitutional rules mapped: YES
Participant and visibility contracts defined: YES
Role switching and delegation defined: YES
Lifecycle surfaces mapped through CH47: YES
Communication, embedded and AI surfaces defined: YES
Minimum scenario sets by profile defined: YES
Appendix B, C, E and G reconciliation required before closure: YES
```

PF-04 closes only when those four appendix projections and B05-REV-0016 pass.