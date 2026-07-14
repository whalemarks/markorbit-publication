# B05-PLN-0004 — Publication Finishing Pack

## Status

- **Pack ID:** B05-PUBLICATION-FINISHING-PACK-001
- **Status:** Active — PF-02 complete; PF-03 authorized
- **Source reviews:** B05-REV-0012, B05-REV-0013 and B05-REV-0014
- **Scope:** Book 05 CH00–CH47 and controlled publication assets
- **Target:** Release Candidate 1 candidate
- **Independent RC1 blocker:** PF-01B CH02–CH47 metadata normalization

## 1. Purpose

This pack converts the complete CH00–CH47 manuscript into a coherent, validated and reviewable publication candidate without changing the MarkReg Product constitution silently.

The pack is editorial and specification-reconciliation work.

It is not software implementation, production deployment or authorization for protected external action.

## 2. Workstream Sequence

```text
PF-01 metadata normalization
+ PF-02 artifact and decision map extension
→ PF-03 reference journey consolidation
→ PF-04 scenario and user-surface consolidation
→ PF-05 jurisdiction and commercial reconciliation
→ PF-06 terminology, compression and native-English editing
→ PF-07 figures and publication apparatus
→ PF-08 structural and rendered validation
→ PF-09 Release Candidate and owner publication gate
```

PF-01B may be completed independently, but it must close before PF-08 and PF-09.

Workstreams may use one or more pull requests, but each PR must retain a clear review boundary.

### 2.1 Controlled Execution Tranches

Completed tranches:

```text
PF-01A — Front Matter metadata and active chapter-map correction
PF-07A — Back Matter, Appendix A–G and publication-apparatus architecture
PF-02 — full-lifecycle Product artifact and Decision reconciliation
```

PF-01A includes:

- CH00–CH01 metadata normalization;
- removal of active candidate wording from CH01;
- addition of the Back Matter sequence to CH01.

PF-01A does not close PF-01. CH02–CH47 metadata still requires PF-01B normalization and validation.

PF-07A includes:

- Appendix A–G paths and controlled scaffolds;
- publication record inventory B05-PUB-0001 through B05-PUB-0008;
- Back Matter ordering and source-of-truth rules;
- initial glossary, subject index and figure plan;
- RC1 checklist architecture.

PF-07A does not close PF-07. Final appendix content, figures, glossary/index and rendered publication remain incomplete.

PF-02 includes:

- B05-SPEC-0001 v0.2 applying through CH47;
- controlled record classes for artifacts, contexts, Decisions, Evidence, Baselines, Views and Governance;
- six lifecycle lineages;
- full-lifecycle version, supersession and change propagation;
- Appendix A reconciliation;
- Appendix B PF-02 state and authority mapping;
- B05-REV-0014 acceptance.

## 3. PF-01 — Metadata Normalization

### Tasks

- normalize CH00–CH47 status labels;
- replace historical `Candidate` chapter-map labels with `B05-TOC-V0.1 — Owner Accepted`;
- remove candidate wording from CH01 narrative;
- reconcile Book 05 status, manifest, YAML, README and review indexes;
- preserve historical review records rather than rewriting their decisions.

### Acceptance

- all forty-eight chapter headers use the controlled chapter map;
- no active chapter presents B05-TOC-V0.1 as a candidate;
- active status records agree.

### Current progress

- CH00–CH01: normalized under PF-01A;
- CH02–CH47: pending PF-01B review and normalization;
- PF-01 overall: open;
- PF-01B is required before PF-08 and PF-09 but does not block PF-03–PF-05 substantive specification work.

## 4. PF-02 — Product Artifact and Decision Map Extension

### Tasks

Extend B05-SPEC-0001 through CH47, including:

- Review and provider-routing Decisions;
- instruction, acceptance, submission and acknowledgement records;
- failure and reconciliation contexts;
- Official Event, Examination, Issue and Response records;
- Publication, Adversarial and Remedy contexts;
- Deadline, Outcome and Communication records;
- Registration, Right Baseline and maintenance records;
- renewal, recordal, transaction and chain-of-title records;
- portfolio, session, return, Pack, Rule, metric and conformance records.

### Acceptance

- every material record named in CH08–CH47 is registered or explicitly classified as local/non-canonical;
- lineage, owner, source, Review, approval, supersession and formalization targets are defined;
- constitutional rules remain unchanged unless a controlled decision says otherwise.

### Completion result

```text
B05-SPEC-0001 v0.2 applies through CH47: YES
Controlled record classes defined: YES
Existing identifiers preserved: YES
Later lifecycle identifiers assigned: YES
New filing lineage: COMPLETE
Examination and response lineage: COMPLETE
Publication and adversarial lineage: COMPLETE
Renewal lineage: COMPLETE
Recordal and transaction lineage: COMPLETE
Portfolio and cross-Product lineage: COMPLETE
Appendix A reconciliation: COMPLETE
Appendix B PF-02 state mapping: COMPLETE
B05-REV-0014 acceptance: COMPLETE
PF-02: CLOSED
```

## 5. PF-03 — Reference Journey Consolidation

### Tasks

- extend `EMBERLOOP` through CH47;
- extend `RIVERKITE` through CH47;
- create a chapter-to-case matrix;
- reconcile case facts, versions, jurisdictions and outcomes;
- remove any accidental contradiction or unsupported final status;
- reconcile Appendix D with B05-SPEC-0002.

### Acceptance

- both cases have one controlled timeline;
- all independent jurisdiction and right states remain consistent;
- chapter examples cite the controlled case state;
- Appendix D is a faithful reader projection.

### Current progress

- authorized by B05-REV-0014;
- current substantive workstream;
- open.

## 6. PF-04 — Scenario and User-Surface Consolidation

### Tasks

- extend B05-SPEC-0003 applicability through CH47;
- index priority Given/When/Then scenarios;
- map scenarios to chapters, controlled records and constitutional rules;
- consolidate client, professional, reviewer, approver, coordinator, finance and provider surfaces;
- identify minimum conformance tests per implementation profile;
- reconcile Appendices B, C, E and G.

### Acceptance

- every high-risk constitutional boundary has observable scenarios;
- user-surface responsibilities do not conflict across chapters;
- scenario IDs and chapter references validate.

## 7. PF-05 — Jurisdiction and Commercial Reconciliation

### Tasks

- reconcile B05-SPEC-0004 with maintenance, renewal, recordal and transaction controls;
- add rule-version, fee-change, form-change and AI-assistance relationships from CH45;
- reconcile official, provider, organization and client-visible price concepts;
- preserve historical Quote and Package versions;
- reconcile Appendix F.

### Acceptance

- Jurisdiction Pack minimum contract supports Parts II–VI;
- commercial controls cover both pre-filing and later-stage services;
- fee and rule changes have explicit impact and revalidation behavior.

## 8. PF-06 — Terminology, Compression and Native-English Editing

### Tasks

- normalize controlled capitalization and defined terms;
- reduce repeated constitutional explanation;
- shorten repetitive lists where tables or references are clearer;
- improve chapter transitions and native-English flow;
- preserve legal and architecture meaning;
- review client-facing examples for clarity.

### Acceptance

- no semantic change without an explicit review note;
- defined terms are used consistently;
- each chapter has a distinct purpose and progression;
- repetition is reduced without removing required boundaries.

## 9. PF-07 — Figures and Publication Apparatus

### Tasks

Create and complete:

- Appendix A–G reader-reference set;
- Back Matter and Appendix Map;
- figure register;
- lifecycle and architecture diagrams;
- artifact and decision lineage diagram;
- state and authority diagram;
- reference journey diagrams;
- jurisdiction and AI governance diagram;
- metrics and MVP sequence diagram;
- terminology and editorial guide;
- source and authority notes;
- glossary;
- subject index;
- cross-book reconciliation;
- conformance and publication checklist.

### Acceptance

- Appendix A–G are reconciled with controlled specifications and chapters;
- figures are reusable and referenced from relevant chapters;
- glossary and index cover defined Product terms;
- source notes explain authority boundaries;
- publication checklist is complete enough for RC review.

### Current progress

- Back Matter structure: locked under B05-PUB-0006;
- Appendix A–G paths and scaffolds: created;
- publication record inventory B05-PUB-0001–0008: created;
- initial glossary, subject index and figure plan: created;
- Appendix A PF-02 reconciliation: complete;
- Appendix B PF-02 state and authority mapping: complete;
- Appendix B PF-04 scenario mapping: pending;
- Appendices C–G substantive reconciliation: pending assigned workstreams;
- controlled figures and final reader assets: pending;
- PF-07 overall: open.

## 10. PF-08 — Structural and Rendered Validation

### Tasks

Validate:

- manuscript count and numbering;
- filenames and headings;
- internal links;
- fenced code blocks;
- duplicate headings;
- specification and review references;
- glossary links;
- figure references;
- manifest and YAML agreement;
- rendered Markdown and target publication formats.

### Acceptance

- automated and manual checks pass or have documented exceptions;
- rendered output has no broken structure, tables, figures or links;
- validation evidence is retained;
- PF-01B metadata normalization is complete.

## 11. PF-09 — Release Candidate and Owner Publication Gate

### Tasks

- rerun complete-manuscript review after PF-01 through PF-08;
- resolve or record remaining findings;
- package Release Candidate 1 artifacts;
- present owner publication decision;
- update repository and Book 05 status only after approval.

### Acceptance

- RC checklist passes;
- no unresolved blocking architecture, editorial or validation finding;
- PF-01B is complete;
- owner decision is recorded;
- implementation and external-action boundaries remain explicit.

## 12. Explicit Non-Goals

This pack does not:

- write software requirements or code;
- select implementation technology;
- deploy MarkReg;
- connect production official systems;
- appoint providers;
- perform filings, payments or Communications;
- authorize autonomous AI action;
- modify Book 02 without Change Proposal;
- modify Book 03 or Book 04 authority silently.

## 13. Completion Decision

`B05-PUBLICATION-FINISHING-PACK-001` is complete only when PF-01 through PF-09 have controlled evidence and the owner publication gate is resolved.

Current decision:

```text
PF-01A: COMPLETE
PF-01B: OPEN
PF-02: COMPLETE
PF-03: AUTHORIZED AND ACTIVE NEXT
PF-04–PF-09: OPEN
```

Until all gates close, Book 05 remains Complete Draft 1 rather than Release Candidate 1.
