# B05-SPEC-0004 — Jurisdiction Pack and Commercial Control Contract

## Status

- **Status:** Controlled Specification v0.3 — PF-06D Record-Reconciled
- **Applies to:** CH09–CH46
- **Supersedes:** Controlled Specification v0.2
- **Record authority:** B05-SPEC-0001 v0.3
- **Purpose:** define the jurisdiction, Rule, form, fee, service-support and commercial controls required before MarkReg may guide, prepare, execute or continue a trademark-service journey.

A Jurisdiction Pack is a controlled Product dependency. It is not law, legal advice, an official office, provider appointment, Filing Approval or production authority.

## 1. Support Contract

```text
supported jurisdiction / service / stage
= scoped Pack Version
+ controlled Source and Rule Records
+ service-specific Product behavior
+ professional ownership
+ commercial control
+ scenario Evidence
+ maintenance, suspension and retirement process
```

Support is declared by jurisdiction, authority, service family, stage, applicant/owner type, route, language, Pack Version, support state, effective period and exclusions.

A filing-preparation module does not automatically support opposition, renewal, recordal, transaction or later-stage work.

## 2. Controlled Record Alignment

| Contract concept | Current record |
| --- | --- |
| Jurisdiction Pack | MR-G01 |
| Rule Record | MR-G02 |
| Pack Version Record | MR-G03 |
| Rule Change Candidate | MR-G04 |
| Organization Overlay | MR-G05 |
| AI Task Context | MR-G06 |
| AI Output Record | MR-G07 |
| Metric Definition | MR-G08 |
| Evaluation Record | MR-G09 |
| Conformance Statement | MR-G10 |
| Source Record | MR-E07 |
| Pack Release Approval | MR-D12 |
| Pilot or Release Decision | MR-D13 |
| Deadline Record | MR-E06 |
| Proposal, Quote and Commercial Instruction | MR-A05–MR-A07 |
| Applicant and Authority Context | MR-C12 |
| Maintenance Obligation Set | MR-B02 |
| Renewal Package Candidate | MR-A26 |
| Recordal / Transaction / Licence | MR-C07–MR-C09, MR-A27–MR-A28 |

Provider advice is sourced Evidence or an input to a Rule/Pack review. It is not `MR-G06`; `MR-G06` is reserved for AI Task Context.

## 3. Pack Identity

Every released Pack Version declares:

- stable Pack ID and immutable version;
- jurisdiction and official authority;
- service family and exact lifecycle stages;
- covered applicant or owner types;
- routes and languages;
- effective period;
- support state and exclusions;
- professional owner and reviewers;
- `MR-D12 Pack Release Approval`;
- next review date or trigger;
- affected journeys, forms, fees and scenarios.

One Pack may contain several modules, but each module retains its own support state and Evidence.

## 4. Support States

### Research Only

Permits source collection, comparison, change candidates and professional research. It does not support current-rule client claims, conforming recommendations, Package preparation or protected action.

### Guidance Capable

Requires reviewed Sources and Rules, dates, scope, limitations, explanations, escalation and guidance scenarios. It permits source-backed explanation and recommendation candidates, not unsupported preparation or action.

### Preparation Capable

Requires Guidance plus exact Requirements, Document/form rules, fee units, Package schema, Review, blockers, material-diff behavior and scenarios. It permits candidate Packages and Approval preparation, not Execution.

### Execution Capable

Requires Preparation plus approved provider/connector/manual route, service-specific Approval, idempotency, Submission Evidence, acknowledgement expectations, unknown-state recovery, duplicate safety, operational ownership and disable capability.

It permits only the approved protected action through the declared route. It does not mean all routes are supported or production is generally authorized.

### Lifecycle Capable

Requires relevant earlier support plus official-event continuation, Deadlines, outcomes, obligations, declared later-stage services, version history, monitoring and suspension rules.

### Suspended

Blocks new dependent protected action when a material source, Rule, form, fee, route, ownership, scenario or safety condition is unresolved. Existing Matters remain visible and require an explicit continuation plan.

### Retired

Remains available for historical lineage but cannot drive new work.

## 5. Source and Rule Contract

`MR-E07 Source Record` retains authority/author, type, title, jurisdiction, language, location or immutable reference, publication/effective/retrieval dates, version/checksum, supersession, restriction, reviewer and interpretation notes.

Source authority may include:

1. legislation, regulation or treaty;
2. official office Rule, notice, fee schedule or form;
3. official manual or guidance;
4. official system validation or direct confirmation;
5. authoritative decision or case law where applicable;
6. verified local professional advice;
7. controlled organization experience;
8. secondary commentary;
9. unverified public content.

`MR-G02 Rule Record` retains Human-readable meaning, machine condition where used, inputs, outputs, affected stage, sources, exceptions, effective period, status, owner, tests and history.

Permitted Rule states include draft, under verification, active, active with limitation, disputed, suspended, superseded, withdrawn and unknown after detected change. Only permitted active states may drive protected behavior.

## 6. Service Modules

A service module defines entry facts, eligibility, sources, Rules, Requirements, fees, Package, Review/Decision gates, formalization/Execution route, expected Evidence, failure/correction behavior, outcome mapping and future obligations.

Minimum modules include:

- new filing;
- examination and response;
- publication, opposition and adversarial work;
- registration and maintenance;
- renewal;
- changes and recordals;
- assignment, merger, succession and licensing;
- portfolio and monitoring.

New-filing modules must consume `MR-C12` when applicant, owner, instructor or signatory is material.

## 7. Deadline, Form and Document Controls

A Deadline-sensitive module identifies triggering event, source hierarchy, event/receipt distinctions, calculation, timezone, office calendar, official/calculated/internal/reminder dates, extensions, correction and responsible reviewer.

```text
Reminder ≠ official Deadline
Provider advice ≠ official Deadline authority
```

Every material official form or schema retains identity, authority, service, effective date, fields, declarations, signature, attachments, accepted formats, route, supersession and test Evidence.

A form change creates `MR-G04 Rule Change Candidate` and identifies affected drafts, reviewed/approved Packages, provider instructions, connector schemas, rendered outputs, client confirmations and re-signature needs.

## 8. Rule and Pack Change Workflow

```text
change signal
→ MR-E07 Source Record
→ MR-G04 Rule Change Candidate
→ affected-Rule and Artifact analysis
→ professional verification
→ MR-G02 / MR-G03 revision
→ scenario tests
→ MR-D12 Pack Release Approval
→ release
→ affected-journey revalidation
```

A new Pack does not silently mutate an accepted Quote, Commercial Instruction, Formal Intake, approved Package, provider instruction, completed submission, official outcome or historical Right Baseline.

Affected work is classified as no action, informational, new-work only, draft revalidation, reviewed-Package revalidation, Approval invalidation, repricing, suspension or future-obligation update.

## 9. Organization Overlay and Provider Advice

`MR-G05 Organization Overlay` may define stricter review, provider preference, internal buffers, templates, risk tolerance, price policy, exchange-rate policy, discount authority, Communication approval and operating language.

It remains distinguishable from official Rule, professional interpretation, Product default, provider-specific requirement and client instruction. It cannot silently weaken a mandatory Rule.

Provider advice retains provider identity/capacity, date, jurisdiction/service scope, affected Rule or Package, sources, commercial interest/conflict, reviewer disposition and recheck trigger. It may Evidence current practice, but it is not Official Truth automatically.

## 10. Commercial Component Model

| Component | Meaning | Default visibility |
| --- | --- | --- |
| Official Fee | payable to official authority | client visible |
| Mandatory Third-Party Cost | required courier, legalization, translation or external cost | client visible or specifically estimated |
| Professional Fee | organization charge for professional work | client visible |
| Provider Pass-Through | external provider charge passed to client | client visible or approved summary |
| Internal Provider Cost | private procurement cost | organization private |
| Tax | applicable inclusive/exclusive treatment | client visible |
| Currency Adjustment | controlled conversion, spread or buffer charged | client visible when charged |
| Contingency | specifically described possible cost | client visible |
| Later-Stage Fee | future response, registration, renewal, recordal or dispute charge | included, excluded, estimated or unknown |
| Discount | approved reduction | client visible; approval Evidence private |
| Credit / Payment Term | approved timing concession | client visible; risk basis private |
| Margin | internal commercial measure | organization private |

Internal cost or Margin must never be labelled Official Fee.

Every component retains identity, service/stage, fee-driving units, amount/currency, source/policy, effective date, tax, visibility, estimation, provider/organization context and supersession.

## 11. Service Price Models

Fee drivers may include jurisdiction, route, filing unit, class/item count, applicant type, priority, search/drafting, Documents, issue/proceeding stage, Evidence, extensions, provider, official fees, registration stage, ordinary/grace/restoration period, right count, transaction type, party count, partial scope, certification, translation, legalization and sequencing.

A generic one-price label is non-conforming when it hides materially different service or fee units.

## 12. Quote and Variance Contract

Every `MR-A06 Quote` identifies version, service/stage, jurisdiction/route, affected units/rights/classes/parties, components/currencies, tax, exchange-rate basis/time, validity, assumptions, inclusions/exclusions, later-stage fees, pass-through treatment, variance rules, payment/refund/cancellation, discount approval, prior version and required Acceptance scope.

A Quote is immutable after issue. Change creates a new version.

Fee, form or Rule variance identifies:

- affected Quote and Commercial Instruction;
- whether the variance was accepted in advance;
- supplementary payment, refund or repricing path;
- whether client Acceptance, Professional Review or Approval must be renewed;
- effect on Package, provider instruction and Execution.

## 13. Visibility and Financial Authority

Visibility remains field-, purpose-, role- and relationship-specific.

Clients see appropriate Official Fees, Professional Fees, charged pass-through, Tax, Currency Adjustment, discounts and later-stage treatment. They do not see private Margin, provider comparison or Internal Provider Cost unless an explicit authorized policy says otherwise.

Finance access does not grant professional or filing authority. Payment does not equal Filing Approval.

Discount, credit and exchange-rate policies identify source, approver, scope, thresholds, timing and client-visible explanation. MarkReg may calculate from policy but may not invent it or hide Margin in Official Fees.

## 14. AI Contract

`MR-G06 AI Task Context` supplies only purpose-required role, jurisdiction/service, Pack Version, Source set, permitted Overlay, Artifact versions, confidentiality limits, expected output and prohibited conclusions.

`MR-G07 AI Output Record` retains task, model/version, input references, Pack/Rule versions, time, uncertainty, citations/source mapping, Human disposition and affected downstream records.

AI may extract, compare, draft, explain, classify or flag candidates. It may not use unstated model memory as current law, release a Pack, approve a Quote/Package, perform Professional Review or authorize protected action.

## 15. Support and Conformance Claim

A Support Claim identifies Product/version, Profile, jurisdiction, service, stage, Pack Version, module support state, route, Human roles, scenarios/evaluation, limitations and production/external-action status.

```text
Support Claim
≤ module Pack Support State
≤ scenario and Evaluation Evidence
≤ operational and authority gates
```

Marketing may not exceed `MR-G10 Conformance Statement`.

## 16. PF-06D Reconciliation State

```text
Support states and service modules: PRESERVED
Source / Rule / Pack mapping: RECONCILED
AI Task and Output mapping: RECONCILED
Metric / Evaluation / Conformance mapping: RECONCILED
MR-C12 new-filing identity dependency: ADDED
Commercial component model: PRESERVED
Quote and variance controls: PRESERVED
Appendix F and G semantic audit: PASS — NO CHANGE REQUIRED
Architecture Canon or Books 02–04 amendment required: NO
```

This specification does not authorize implementation, production deployment or External Protected Action.
