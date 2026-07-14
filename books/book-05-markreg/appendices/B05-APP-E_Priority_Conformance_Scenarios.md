# Appendix E — Priority Conformance Scenarios

**Status:** Controlled Scaffold — content completion pending PF-04  
**Primary sources:** B05-SPEC-0003 and chapter Given/When/Then scenarios  
**Reader purpose:** provide a compact set of observable tests for the constitutional and lifecycle boundaries of MarkReg.

## E.1 Scenario Format

Each final scenario must identify:

```text
Given
When
Then
Authority boundary
Evidence retained
Relevant constitutional rule
Relevant chapter and artifact
```

A principle without observable behavior is not sufficient conformance evidence.

## E.2 Priority Scenario Families

### A. Identity, Applicant and Authority

- applicant differs from organization profile;
- parent and subsidiary ownership conflict;
- signatory authority is missing or expired;
- official owner differs from current business owner;
- chain-of-title link is incomplete.

Expected behavior: retain conflicting sources, ask the smallest material question, require eligible Review or authority evidence, and block affected protected action.

### B. Recommendation and Scope

- jurisdiction recommendation changes after market facts change;
- mark variant changes after search;
- class recommendation is uncertain;
- goods/services item exceeds a jurisdiction limit;
- client selects a non-recommended option.

Expected behavior: preserve prior versions, explain consequences, create new downstream scope, and avoid silent mutation.

### C. Quote, Acceptance and Payment

- Quote expires before acceptance;
- official fee changes after acceptance;
- discount lacks approval;
- payment is missing or duplicated;
- later-stage fees were excluded from the accepted scope.

Expected behavior: identify the exact Quote version and terms, reprice or apply the controlled variance path, preserve payment state separately from Filing Approval, and prevent duplicate financial effect.

### D. Documents and Formal Intake

- uploaded POA is invalid;
- scan is accepted for preparation but original is required later;
- translation or notarization requirement changes;
- reused client fact is stale;
- document is valid for one jurisdiction but not another.

Expected behavior: classify the defect and permitted use, identify affected packages, and block only the relevant purpose.

### E. Review and Approval

- package changes after client confirmation;
- Professional Review is incomplete;
- approval applies to an older version;
- delegated approver authority expires;
- coordinator or AI attempts to act as professional approver.

Expected behavior: invalidate the affected approval, preserve history, and route to an eligible Human role.

### F. Provider Routing and Engagement

- preferred provider has a conflict;
- provider is unavailable;
- provider proposes a material change;
- provider receives but does not accept instruction;
- provider requests access outside the engagement.

Expected behavior: keep recommendation, selection, appointment, instruction, receipt and acceptance distinct; restrict access by purpose.

### G. Submission, Unknown State and Duplicate Safety

- connector reports technical success without official receipt;
- provider says filed but provides no evidence;
- timeout occurs after possible payment;
- retry could create a duplicate application;
- Return Envelope is consumed twice.

Expected behavior: enter unknown or reconciliation state, block unsafe retry, use stable idempotency identity, and return the existing result where appropriate.

### H. Official Events, Deadlines and Communication

- official notice is corrected;
- provider deadline conflicts with official source;
- publication window appears closed but has not been verified;
- client status message contains the wrong scope;
- client silence occurs before a required decision.

Expected behavior: retain source hierarchy and correction history, preserve the earliest credible internal target where necessary, issue a linked corrected Communication, and never treat silence as approval.

### I. Registration and Maintenance

- certificate file differs from current official record;
- registration scope differs from approved filing scope;
- renewal reminder differs from official deadline;
- one class is not renewed;
- official owner must be corrected before or with renewal.

Expected behavior: create or update the Right Baseline, keep official, calculated and internal dates separate, and produce jurisdiction-specific packages.

### J. Assignment, Licensing and Portfolio

- assignment is signed but not recorded;
- licence is mistaken for transfer;
- one right is challenged while others remain active;
- use evidence is weak for only part of the specification;
- monitoring signal is treated as infringement conclusion.

Expected behavior: preserve contractual and official effects, independent right histories, evidence granularity and Human Review.

### K. Jurisdiction Packs and AI

- current rule is requested without a valid Pack;
- fee table is stale;
- official source conflicts with provider advice;
- organization overlay conflicts with active rule;
- AI output lacks source mapping.

Expected behavior: block or escalate high-risk use, mark rule conflict or uncertainty, and require source-backed professional validation.

### L. Conformance and Publication Claims

- partial implementation claims full-lifecycle support;
- marketing claims global automation from three jurisdictions;
- publication RC status is treated as production authority;
- local implementation redefines a Core object;
- future edition weakens Human approval.

Expected behavior: correct the conformance claim, record an upstream finding where required, and preserve implementation and authority gates.

## E.3 Minimum Constitutional Scenario Set

The final appendix must contain at least one passing and one failing scenario for each rule:

| Rule | Minimum tested behavior |
| --- | --- |
| MR-CR-01 | recommendation is not Decision |
| MR-CR-02 | Product readiness is not approval |
| MR-CR-03 | approval is not Execution |
| MR-CR-04 | submission is not official acknowledgement |
| MR-CR-05 | Product projection is not official truth without source |
| MR-CR-06 | AI does not replace accountable Human Review |
| MR-CR-07 | Product-local artifacts do not silently become formal shared objects |
| MR-CR-08 | every material artifact has lineage, version, responsibility and supersession |

## E.4 Scenario Index Fields

PF-04 should assign each scenario:

- stable scenario ID;
- risk category;
- lifecycle stage;
- participant roles;
- affected artifacts;
- preconditions;
- expected Product response;
- blocked or permitted external action;
- retained evidence;
- source chapter;
- implementation profile applicability.

## E.5 Completion Work

PF-04 must:

1. extend B05-SPEC-0003 through CH47;
2. remove duplicate scenarios while preserving material distinctions;
3. assign stable IDs;
4. map scenarios to Appendix B and C matrices;
5. identify zero-tolerance safety cases;
6. define the minimum test set for each conformance profile.

This appendix becomes publication-ready only after the controlled scenario index passes full-book review.