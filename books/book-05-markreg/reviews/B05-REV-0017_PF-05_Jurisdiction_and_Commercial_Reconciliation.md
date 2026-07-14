# B05-REV-0017 — PF-05 Jurisdiction and Commercial Reconciliation

## Review Status

- **Status:** Complete
- **Scope:** B05-SPEC-0004 v0.2, Appendix F and the PF-05 portion of Appendix G
- **Workstream:** PF-05 — Jurisdiction and Commercial Reconciliation
- **Review type:** jurisdiction support, source, rule, form, fee, commercial visibility, later-stage service and AI-governance review
- **Decision:** PF-05 accepted and closed; PF-06 Editorial Finishing authorized

## 1. Reviewed Records

- `specifications/B05-SPEC-0004_Jurisdiction_Pack_and_Commercial_Control_Contract.md`
- `appendices/B05-APP-F_Minimum_Jurisdiction_Pack_Checklist.md`
- `appendices/B05-APP-G_MarkReg_Conformance_Profiles.md`
- B05-SPEC-0001 v0.2 controlled-record model
- B05-SPEC-0003 v0.2 scenario and profile model
- CH09–CH21, CH30–CH46

## 2. Review Questions

The review tested whether PF-05:

1. defines jurisdiction support at service and lifecycle-stage level;
2. defines exact Pack identity and support states;
3. covers new filing, examination, disputes, registration, maintenance, renewal, recordal, transaction and portfolio services;
4. preserves source, Rule, form and Pack version lineage;
5. defines fee, form and Rule change impact;
6. preserves accepted Quote and approved Package versions;
7. separates official fees, client prices, provider costs and margin;
8. covers later-stage price models;
9. keeps payment, Review, approval and official effect distinct;
10. keeps provider advice and Organization Overlay separate from official rules;
11. constrains AI to Pack-bound, source-backed assistance;
12. maps Pack evidence to Conformance Profiles;
13. produces a faithful reader checklist in Appendix F;
14. prevents Profile claims from exceeding Pack evidence;
15. preserves Books 01–04 authority boundaries.

## 3. Pack Identity and Scope

B05-SPEC-0004 v0.2 requires every Pack version to declare:

- stable Pack identity and immutable version;
- jurisdiction and official authority;
- service family and lifecycle stages;
- applicant or owner types;
- route and language scope;
- effective period;
- support state;
- exclusions;
- professional owner and reviewers;
- Pack Release Approval;
- next-review trigger.

A country label alone cannot establish support.

**Result:** PASS.

## 4. Support-State Review

The following states are defined:

```text
Research Only
Guidance Capable
Preparation Capable
Execution Capable
Lifecycle Capable
Suspended
Retired
```

Each state defines what is permitted, what evidence is required and what remains prohibited.

The model prevents:

- guidance from being represented as execution;
- filing support from implying renewal or opposition support;
- suspended modules from driving new protected actions;
- retired versions from disappearing from historical lineage.

**Result:** PASS.

## 5. Service-Family Coverage

The controlled specification covers:

- new filing;
- examination and response;
- publication, opposition and adversarial work;
- registration and maintenance;
- renewal;
- changes and recordals;
- assignment, merger, succession and licensing;
- portfolio and monitoring.

Later-stage services have their own requirements and fee drivers rather than inheriting a generic new-filing contract.

**Result:** PASS.

## 6. Source and Rule Governance

The specification defines:

- source authority classes;
- publication, effective and retrieval dates;
- version or checksum identity;
- supersession;
- confidentiality and use restrictions;
- Rule Record fields;
- active, limited, disputed, suspended and superseded states;
- professional ownership;
- scenario evidence;
- change history.

Provider advice and organization experience remain distinguishable from official sources.

**Result:** PASS.

## 7. Deadline Review

The contract separates:

- triggering event;
- event date;
- receipt date;
- statutory or official deadline;
- calculated date;
- internal target;
- reminder date;
- extension, grace and restoration periods;
- timezone and office calendar;
- source conflict and correction.

A reminder date cannot be represented as an official deadline.

**Result:** PASS.

## 8. Form and Package Version Review

A form or schema change creates a Change Candidate and impact assessment.

Affected work may include:

- open drafts;
- reviewed packages;
- approved but unexecuted packages;
- provider instructions;
- connector schemas;
- rendered outputs;
- client confirmations;
- signature requirements.

Historical packages retain the form version used at the time.

**Result:** PASS.

## 9. Commercial Component Review

The specification distinguishes:

- official fee;
- mandatory third-party cost;
- professional fee;
- provider pass-through;
- internal provider cost;
- tax;
- currency adjustment;
- contingency;
- later-stage fee;
- discount;
- credit term;
- margin.

Internal cost or margin may not be labeled as official fee.

**Result:** PASS.

## 10. Visibility Review

The visibility matrix keeps:

- official and client-facing charges visible to the client;
- internal provider costs restricted;
- margin restricted;
- provider comparisons private;
- provider access limited to its own engagement;
- finance access limited to required commercial information.

Visibility remains field-, purpose-, organization- and role-specific.

**Result:** PASS.

## 11. Later-Stage Pricing Review

Separate price drivers are defined for:

- new filing;
- examination and response;
- opposition and dispute;
- registration and maintenance;
- renewal;
- changes and transactions.

The specification rejects one generic renewal or recordal price where material right, class, party, document, surcharge, provider or official-fee differences are hidden.

**Result:** PASS.

## 12. Quote and Variance Review

Every Quote retains:

- immutable ID and version;
- exact service and stage;
- fee-driving units;
- component amounts and currencies;
- tax and exchange-rate basis;
- validity and expiry;
- assumptions, inclusions and exclusions;
- later-stage fees;
- variance treatment;
- payment, refund and cancellation rules;
- approval and supersession references.

Fee, form or Rule changes trigger impact assessment rather than silent mutation.

**Result:** PASS.

## 13. Payment and Financial Authority Review

The contract preserves:

```text
payment received
≠ Professional Review
≠ Filing Approval
≠ Provider Acceptance
≠ official acknowledgement
```

MarkReg records and explains payment conditions but does not become the authoritative accounting service.

**Result:** PASS.

## 14. AI Review

AI may assist with source comparison, Rule extraction, fee-unit mapping, impact analysis and explanation drafting only when Pack, source, purpose and confidentiality context are supplied.

AI may not:

- invent a current rule or fee;
- release a Pack;
- activate a disputed rule;
- decide an unsupported effective date;
- generalize provider advice;
- modify Quote or package silently;
- grant authority;
- claim unsupported service coverage.

**Result:** PASS.

## 15. Controlled Archetype A — Direct New Filing

The non-jurisdictional archetype tests:

- direct filing;
- class-based official fees;
- local provider requirement;
- scanned POA;
- separate registration-stage fee;
- provider-returned official acknowledgement.

The model correctly supports separate Guidance, Preparation and Execution claims without implying renewal, opposition or full-lifecycle coverage.

The Quote distinguishes filing and later registration stages, and internal provider cost remains private.

**Result:** PASS.

## 16. Controlled Archetype B — Renewal with Ownership Recordal Dependency

The archetype tests:

- existing registered right;
- grace-sensitive renewal;
- business owner differing from official owner;
- renewal and recordal sequencing;
- separate fees and approvals;
- partial official outcomes.

The model preserves:

- current Right Baseline;
- sourced Deadline Record;
- separate Renewal and Recordal Packages;
- separate Renewal and Recordal Approvals;
- ordinary, surcharge and recordal price components;
- assignment document versus official owner update;
- Pack-dependent sequencing.

**Result:** PASS.

This confirms that B05-SPEC-0004 v0.2 is not limited to new filing.

## 17. Scenario Alignment

The PF-05 contract maps to applicable scenarios including:

- MR-SCN-03–08;
- MR-SCN-10 and 12;
- MR-SCN-15;
- MR-SCN-26;
- MR-SCN-30–32;
- MR-SCN-37–39.

A failed applicable zero-tolerance scenario suspends the affected support claim.

**Result:** PASS.

## 18. Profile Evidence Review

Appendix G now prevents a Profile claim from exceeding Pack evidence:

| Profile | Required evidence |
| --- | --- |
| Guided Decision | Guidance Capable modules |
| Commercial Intake | current price, Intake and variance rules |
| Filing Preparation | Preparation Capable forms and packages |
| Governed Filing | Execution Capable route and evidence |
| Post-Filing | proceeding-specific Lifecycle Capable modules |
| Portfolio Continuity | declared maintenance, renewal, recordal and transaction modules |
| Full-Lifecycle | explicit state for every declared module plus change and AI governance |

**Result:** PASS.

## 19. Appendix F Review

Appendix F provides a reader checklist for:

- Pack identity and support state;
- sources and rules;
- all service families;
- deadlines and forms;
- commercial components and service prices;
- Quote, visibility and variance;
- AI governance;
- Profile evidence;
- validation archetypes;
- scenario evidence.

It remains subordinate to B05-SPEC-0004 v0.2.

**Result:** PASS.

## 20. Architecture Boundary Review

PF-05 does not:

- redefine Book 02 Core semantics;
- create a parallel Book 03 Execution authority;
- absorb Book 04 Workplace permissions or private commercial policy;
- make provider advice official truth;
- authorize AI professional action;
- authorize production deployment or external action.

**Result:** PASS.

No Architecture Canon, Book 02, Book 03 or Book 04 semantic amendment is required.

## 21. PF-05 Decision

```text
B05-SPEC-0004 v0.2 applies through later lifecycle stages: YES
Exact Pack identity and support states: YES
Service modules through portfolio continuity: YES
Source, Rule, Form and change governance: YES
Commercial component separation: YES
Client/internal visibility separation: YES
Later-stage pricing coverage: YES
Quote and variance lineage: YES
Payment authority boundary: YES
AI boundary: YES
Controlled archetypes: PASS
Appendix F reconciled: YES
Appendix G PF-05 evidence reconciled: YES
PF-05 complete: YES
PF-06 Editorial Finishing authorized: YES
PF-01B still open: YES
Release Candidate 1 ready: NO
```

## 22. Next Controlled Work

PF-06 must perform whole-book terminology, compression and native-English editing while preserving:

- controlled IDs;
- constitutional rules;
- official-source and authority boundaries;
- reference-journey final states;
- scenario behavior;
- Pack and commercial contracts.

PF-01B remains an independent RC1 blocker.

PF-07 figures and apparatus, PF-08 validation and PF-09 Release Candidate review remain open.