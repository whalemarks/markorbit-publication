# B05-PLN-0004 — Publication Finishing Pack

## Status

- **Pack ID:** B05-PUBLICATION-FINISHING-PACK-001
- **Status:** Active — PF-02 and PF-03 complete; PF-04 authorized
- **Source reviews:** B05-REV-0012 through B05-REV-0015
- **Scope:** Book 05 CH00–CH47 and controlled publication assets
- **Target:** Release Candidate 1 candidate
- **Independent RC1 blocker:** PF-01B CH02–CH47 metadata normalization

## 1. Purpose

This pack converts the complete CH00–CH47 manuscript into a coherent, validated and reviewable publication candidate without silently changing the MarkReg Product constitution.

It is editorial and controlled-specification work. It is not software implementation, production deployment or authorization for protected external action.

## 2. Workstream Sequence

```text
PF-01 metadata normalization
+ PF-02 artifact and Decision reconciliation
+ PF-03 reference journey consolidation
→ PF-04 scenario and user-surface consolidation
→ PF-05 jurisdiction and commercial reconciliation
→ PF-06 terminology, compression and native-English editing
→ PF-07 figures and publication apparatus
→ PF-08 structural and rendered validation
→ PF-09 Release Candidate and owner publication gate
```

PF-01B may be completed independently, but it must close before PF-08 and PF-09.

## 3. Completed Tranches

### PF-01A — Front Matter

Completed:

- CH00–CH01 metadata normalization;
- removal of active candidate wording;
- reader-facing Back Matter sequence in CH01.

Open:

- CH02–CH47 metadata normalization under PF-01B.

### PF-07A — Publication Architecture

Completed:

- Appendix A–G paths and controlled scaffolds;
- B05-PUB-0001 through B05-PUB-0008;
- Back Matter ordering and source-of-truth rules;
- initial glossary, subject index and figure plan;
- RC1 checklist architecture.

Open:

- final figures, glossary/index, reader assets and rendered publication.

### PF-02 — Product Artifact and Decision Map

Completed:

- B05-SPEC-0001 v0.2 through CH47;
- controlled classes for artifacts, contexts, Decisions, evidence, baselines, views and governance;
- six lifecycle lineages;
- version, supersession and change propagation;
- Appendix A reconciliation;
- Appendix B state and authority mapping;
- B05-REV-0014 acceptance.

### PF-03 — Reference Journey Consolidation

Completed:

- B05-SPEC-0002 v0.2 through CH47;
- locked `EMBERLOOP` and `RIVERKITE` identities;
- stable `EL-*` and `RK-*` step timelines;
- CH08–CH47 chapter-to-journey matrix;
- final reviewed state locks;
- RIVERKITE urgent-deadline and wider-renewal count reconciliation;
- Appendix D reconciliation;
- B05-REV-0015 acceptance.

## 4. PF-01 — Metadata Normalization

### Tasks

- normalize all forty-eight chapter headers;
- use `B05-TOC-V0.1 — Owner Accepted` consistently;
- preserve historical review records;
- reconcile active status, manifest, YAML and navigation.

### Current result

```text
PF-01A CH00–CH01: COMPLETE
PF-01B CH02–CH47: OPEN
PF-01 overall: OPEN
```

PF-01B is required before PF-08 and PF-09 but does not block PF-04 and PF-05 substantive work.

## 5. PF-02 — Artifact and Decision Map

### Acceptance result

```text
B05-SPEC-0001 v0.2 through CH47: PASS
Controlled IDs and record classes: PASS
Lifecycle lineages: PASS
Appendix A: PASS
Appendix B state mapping: PASS
PF-02: CLOSED
```

## 6. PF-03 — Reference Journeys

### Acceptance result

```text
EMBERLOOP identity and CH08–CH47 timeline: PASS
RIVERKITE identity and CH08–CH47 timeline: PASS
Independent jurisdictions and rights: PASS
No invented official outcomes: PASS
Chapter-to-journey matrix: PASS
Appendix D: PASS
PF-03: CLOSED
```

### Final case locks

```text
EMBERLOOP
- UK registered
- US under examination
- EU in opposition
- Japan and Australia candidates only

RIVERKITE
- six independent rights
- four ordinary renewals
- one ownership-linked renewal
- one cancellation defense
- evidence and licence actions open
```

## 7. PF-04 — Scenario and User-Surface Consolidation

### Status

Authorized by B05-REV-0015 and now the next substantive workstream.

### Tasks

- extend B05-SPEC-0003 through CH47;
- assign stable scenario IDs;
- map scenarios to constitutional rules, controlled records and journey step IDs;
- consolidate client, professional, reviewer, approver, coordinator, finance, provider, administrator and AI surfaces;
- define minimum conformance tests per implementation profile;
- reconcile Appendix B scenario references;
- reconcile Appendix C participant rights;
- reconcile Appendix E priority scenarios;
- reconcile Appendix G conformance profiles.

### Acceptance

- every high-risk constitutional boundary has observable scenarios;
- surface responsibilities do not conflict across chapters;
- scenario IDs, chapter references and journey references validate;
- partial implementation profiles state scope honestly.

## 8. PF-05 — Jurisdiction and Commercial Reconciliation

### Tasks

- extend B05-SPEC-0004 to maintenance, renewal, recordal and transaction services;
- add rule-version, fee-change, form-change and AI-assistance relationships;
- reconcile official, provider, organization and client-visible prices;
- preserve historical Quote and Package versions;
- reconcile Appendix F.

## 9. PF-06 — Editorial Finishing

### Tasks

- normalize controlled terminology and capitalization;
- reduce repeated constitutional explanation;
- improve transitions and native-English flow;
- preserve legal and architecture meaning;
- review client-facing examples.

## 10. PF-07 — Figures and Publication Apparatus

### Current progress

```text
Back Matter architecture: COMPLETE
Appendix A PF-02 reconciliation: COMPLETE
Appendix B state mapping: COMPLETE
Appendix D PF-03 reconciliation: COMPLETE
Appendices B/C/E/G PF-04 work: OPEN
Appendix F PF-05 work: OPEN
Figures: PLANNED, NOT CREATED
Glossary and Subject Index: INITIAL DRAFTS
PF-07 overall: OPEN
```

## 11. PF-08 — Structural and Rendered Validation

Validate:

- manuscript count, filenames, headings and numbering;
- internal links and fenced blocks;
- specification, review, glossary and figure references;
- manifest and YAML agreement;
- Markdown and target rendered formats;
- PF-01B completion.

## 12. PF-09 — RC1 and Owner Publication Gate

RC1 requires:

- PF-01 through PF-08 completion;
- no unresolved blocking architecture, editorial or validation finding;
- owner publication decision;
- explicit implementation and external-action boundaries.

## 13. Explicit Non-Goals

This pack does not:

- write software requirements or code;
- deploy MarkReg;
- connect production official systems;
- appoint providers;
- perform filings, payments or Communications;
- authorize autonomous AI action;
- modify Books 02–04 silently.

## 14. Current Decision

```text
PF-01A: COMPLETE
PF-01B: OPEN — RC1 BLOCKER
PF-02: COMPLETE
PF-03: COMPLETE
PF-04: AUTHORIZED AND NEXT
PF-05–PF-09: OPEN
```

Until all gates close, Book 05 remains Complete Draft 1 rather than Release Candidate 1.