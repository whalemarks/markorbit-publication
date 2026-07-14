# B05-REV-0016 — PF-04 Scenario and User-Surface Reconciliation

## Review Status

- **Status:** Complete
- **Scope:** B05-SPEC-0003 v0.2; Appendices B, C, E and G
- **Workstream:** PF-04 — Scenario and User-Surface Consolidation
- **Decision:** PF-04 accepted; PF-05 authorized

## 1. Review Purpose

This review determines whether Book 05 now has one controlled, observable and full-lifecycle contract for:

- conformance scenarios;
- state and authority boundaries;
- participant visibility and action rights;
- embedded and cross-Product surfaces;
- AI assistance surfaces;
- conformance profiles and minimum test sets.

The review does not establish implementation, production or external-action authority.

## 2. Material Reviewed

- `specifications/B05-SPEC-0003_Conformance_Scenarios_and_User_Surfaces.md`
- `appendices/B05-APP-B_Lifecycle_State_and_Authority_Matrix.md`
- `appendices/B05-APP-C_Participant_Visibility_and_Action_Rights_Matrix.md`
- `appendices/B05-APP-E_Priority_Conformance_Scenarios.md`
- `appendices/B05-APP-G_MarkReg_Conformance_Profiles.md`
- B05-SPEC-0001 v0.2
- B05-SPEC-0002 v0.2
- CH07 and CH21–CH47

## 3. Scenario Registry

B05-SPEC-0003 preserves `MR-SCN-01` through `MR-SCN-10` and extends the registry through `MR-SCN-41`.

The registry covers:

1. identity, applicant and authority;
2. recommendation and scope;
3. commercial, payment and Documents;
4. Review, approval and package integrity;
5. provider routing and engagement;
6. submission, unknown state and duplicate safety;
7. official events, deadlines and Communication;
8. registration, renewal, ownership and portfolio;
9. embedded experience, permission and AI;
10. metrics, conformance and publication claims.

Each scenario identifies Given, When, Then, authority boundary, evidence, chapters, controlled records and severity.

**Result:** PASS.

## 4. Constitutional Rule Coverage

The review confirms scenario coverage for all eight MarkReg constitutional rules:

```text
MR-CR-01 — recommendation is not Decision
MR-CR-02 — readiness is not approval
MR-CR-03 — approval is not Execution
MR-CR-04 — submission is not official acknowledgement
MR-CR-05 — Product projection is not official truth without source
MR-CR-06 — AI does not replace accountable Human Review
MR-CR-07 — Product-local records do not silently become formal objects
MR-CR-08 — material records retain lineage, version, responsibility and supersession
```

Every rule has multiple scenario references, including blocked or negative paths.

**Result:** PASS.

## 5. Zero-Tolerance Safety Review

The controlled zero-tolerance set covers:

- expired or insufficient authority;
- duplicate payment, filing or Return effect;
- approval applied to changed work;
- incomplete required Review;
- expired delegated approval;
- provider silent change or over-access;
- technical success represented as official acknowledgement;
- unsafe retry while effect is unknown;
- deadline conflict without verification;
- client silence treated as authority;
- private Lite data transferred outside purpose;
- wrong-organization access;
- AI current-rule conclusion without controlled sources;
- publication status treated as production authority.

A declared profile cannot pass when an applicable zero-tolerance scenario fails.

**Result:** PASS.

## 6. Participant Contract Review

Appendix C and B05-SPEC-0003 distinguish:

- client contact;
- applicant or owner representative;
- professional;
- reviewer;
- approver;
- coordinator;
- account owner;
- finance participant;
- provider;
- administrator;
- AI assistant.

One person may hold several roles, but each material action retains the active role, represented organization, authority basis, scope, version and expiry.

Client confirmation, Professional Review, Filing Approval, payment confirmation, provider acceptance and official effect remain separate.

**Result:** PASS.

## 7. Visibility Review

The controlled visibility classes are:

- client visible;
- professional restricted;
- organization private;
- provider purpose-limited;
- finance restricted;
- personal local;
- official-source public;
- confidential evidence.

Visibility is field-, purpose-, organization- and relationship-specific.

The Product does not allow:

- provider access to unrelated portfolio or margin data;
- finance access to unrelated legal evidence;
- client access to internal provider comparison by default;
- Workplace transfer of private Lite notes without purpose;
- administrator impersonation;
- AI expansion of access scope.

**Result:** PASS.

## 8. Action Rights Review

The action-right matrix separates:

- fact provision and correction;
- commercial option selection;
- professional strategy;
- Professional Review;
- Filing Approval;
- provider Selection;
- Provider Acceptance;
- protected Execution;
- official-event verification;
- Jurisdiction Pack release;
- protected Communication.

The matrix states that actual permission also depends on jurisdiction, professional qualification, organization policy, delegation, relationship and engagement.

**Result:** PASS.

## 9. Lifecycle Surface Review

B05-SPEC-0003 maps user surfaces from CH07 through CH47, including:

- need and recommendation;
- scope and risk;
- Proposal and commercial confirmation;
- Intake and Handoff;
- package and approval;
- provider and route;
- submission and recovery;
- examination and response;
- publication and dispute;
- registration and maintenance;
- renewal, recordal and transaction;
- portfolio;
- standalone, embedded and cross-Product experience;
- participant surfaces;
- Jurisdiction Pack and AI;
- metrics, MVP and conformance.

Every surface must expose context, version, source, authority, next action and return route where applicable.

**Result:** PASS.

## 10. Communication and Embedded Experience

The specification preserves Communication states:

```text
draft
→ reviewed
→ approved
→ sent
→ delivered
→ failed
→ acknowledged
→ corrected or superseded
```

It also defines Handoff and Return surface requirements for purpose, permission, inherited context, source, expiry, correlation and idempotency.

A URL, deep link or Product Session does not carry authority by itself.

**Result:** PASS.

## 11. AI Surface Review

AI output is limited to:

- extraction candidate;
- comparison candidate;
- explanation draft;
- recommendation candidate;
- rule-change candidate;
- evaluation or anomaly candidate.

The surface must expose source context, Pack or Rule version where relevant, uncertainty, Human disposition and prohibited use.

AI may not appear as client, professional, reviewer, approver, provider, official office or Owning Service.

**Result:** PASS.

## 12. Conformance Profile Review

Appendix G defines eight profiles:

1. Foundation;
2. Guided Decision;
3. Commercial Intake;
4. Filing Preparation;
5. Governed Filing;
6. Post-Filing;
7. Portfolio Continuity;
8. Full-Lifecycle.

Each profile now has:

- capability scope;
- required authority and source behavior;
- minimum scenario IDs;
- zero-tolerance requirements;
- declaration requirements;
- exclusions and limitations.

The profile dependency rule allows a later-stage Product to consume prior-stage formal records through Handoff without pretending to implement every earlier user journey.

**Result:** PASS.

## 13. Partial and Full-Lifecycle Claims

The review confirms:

- a partial profile may conform when its scope and exclusions are accurate;
- Full-Lifecycle does not mean every jurisdiction or proceeding;
- feature existence does not establish profile support;
- profile support requires source, authority, failure and scenario evidence;
- publication status does not establish production authority;
- marketing claims may not exceed the controlled conformance statement.

**Result:** PASS.

## 14. Appendix Reconciliation

### Appendix B

State domains, authority transitions, unknown states, label rules and scenario references are reconciled.

### Appendix C

Participant roles, visibility, action rights, delegation, communication and surface exclusions are reconciled.

### Appendix E

`MR-SCN-01–41`, severity, zero-tolerance cases, constitutional coverage and profile families are reconciled.

### Appendix G

Profile scope, evidence, scenario minimums, examples and non-conforming claims are reconciled for PF-04.

PF-05 jurisdiction and service evidence and PF-08 validation remain open.

**Result:** PASS.

## 15. Upstream and Architecture Review

PF-04 does not:

- redefine Book 02 Core semantics;
- create a parallel Book 03 Execution authority;
- absorb Book 04 Workplace permission or responsibility;
- convert MGSN into an open provider marketplace;
- grant AI professional authority;
- create production or external-action authority.

No Architecture Canon, Book 02, Book 03 or Book 04 semantic amendment is required.

**Result:** PASS.

## 16. Remaining Work

PF-04 does not complete:

- PF-01B chapter metadata normalization;
- PF-05 jurisdiction, commercial, fee, form and Rule-version reconciliation;
- PF-06 whole-book terminology and native-English editing;
- PF-07 figures and final publication apparatus;
- PF-08 scenario execution and rendered validation;
- PF-09 RC1 and owner publication gate.

## 17. Decision

```text
B05-SPEC-0003 v0.2 through CH47: ACCEPTED
MR-SCN-01–41 registry: ACCEPTED
Zero-tolerance set: ACCEPTED
Participant and visibility contract: ACCEPTED
Action-right matrix: ACCEPTED
Lifecycle surface matrix: ACCEPTED
Embedded, Communication and AI surfaces: ACCEPTED
Appendix B PF-04 reconciliation: ACCEPTED
Appendix C PF-04 reconciliation: ACCEPTED
Appendix E PF-04 reconciliation: ACCEPTED
Appendix G PF-04 reconciliation: ACCEPTED
PF-04: COMPLETE
PF-05: AUTHORIZED
Release Candidate 1: NOT YET
Unrestricted implementation: NOT AUTHORIZED
Production deployment: NOT AUTHORIZED
External protected action: NOT AUTHORIZED
```

Merge of this review may close PF-04 and authorize PF-05 Jurisdiction and Commercial Reconciliation.