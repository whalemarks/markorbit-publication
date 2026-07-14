# B05-PLN-0004 — Publication Finishing Pack

## Status

- **Pack ID:** B05-PUBLICATION-FINISHING-PACK-001
- **Status:** Active — PF-02 through PF-05 complete; PF-06 authorized
- **Source reviews:** B05-REV-0012 through B05-REV-0017
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
+ PF-04 scenario and user-surface consolidation
+ PF-05 jurisdiction and commercial reconciliation
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
- controlled classes and full-lifecycle IDs;
- lifecycle lineages, versioning and supersession;
- Appendix A;
- Appendix B state and authority mapping;
- B05-REV-0014.

### PF-03 — Reference Journeys

Completed:

- B05-SPEC-0002 v0.2 through CH47;
- `EMBERLOOP` and `RIVERKITE` identities, steps and final states;
- CH08–CH47 chapter matrix;
- Appendix D;
- B05-REV-0015.

### PF-04 — Scenarios and User Surfaces

Completed:

- B05-SPEC-0003 v0.2 through CH47;
- `MR-SCN-01–41`;
- zero-tolerance controls;
- participant, visibility, action-right and delegation contracts;
- lifecycle surfaces and eight conformance profiles;
- Appendices B, C, E and PF-04 portion of G;
- B05-REV-0016.

### PF-05 — Jurisdiction and Commercial Reconciliation

Completed:

- B05-SPEC-0004 v0.2 through later lifecycle services;
- exact Pack identity and support states;
- Research, Guidance, Preparation, Execution and Lifecycle support levels;
- source, Rule, deadline, form and Pack-change contracts;
- new filing, response, dispute, registration, maintenance, renewal, recordal, transaction and portfolio modules;
- official, client, provider, tax, currency, discount, credit, internal-cost and margin separation;
- later-stage price models;
- immutable Quote, fee/form/Rule variance and revalidation behavior;
- Pack-bound AI assistance;
- Pack-to-Profile evidence;
- Appendix F;
- PF-05 portion of Appendix G;
- B05-REV-0017.

## 4. PF-01 — Metadata Normalization

```text
PF-01A CH00–CH01: COMPLETE
PF-01B CH02–CH47: OPEN
PF-01 overall: OPEN
```

PF-01B is required before PF-08 and PF-09 but does not block PF-06 editorial work.

## 5. PF-02 — Artifact and Decision Map

```text
B05-SPEC-0001 v0.2: PASS
Appendix A: PASS
Appendix B state mapping: PASS
PF-02: CLOSED
```

## 6. PF-03 — Reference Journeys

```text
EMBERLOOP and RIVERKITE timelines: PASS
Independent jurisdiction and right states: PASS
Appendix D: PASS
PF-03: CLOSED
```

Final case locks remain:

```text
EMBERLOOP — UK registered; US under examination; EU in opposition; Japan/Australia candidates only
RIVERKITE — four ordinary renewals; one ownership-linked renewal; one cancellation defense; evidence/licence actions open
```

## 7. PF-04 — Scenarios and User Surfaces

```text
B05-SPEC-0003 v0.2: PASS
MR-SCN-01–41: PASS
Participant and surface contracts: PASS
Eight profile minimum test sets: PASS
Appendices B, C, E and G: PASS FOR PF-04
PF-04: CLOSED
```

## 8. PF-05 — Jurisdiction and Commercial Controls

### Acceptance result

```text
B05-SPEC-0004 v0.2: PASS
Pack identity and support states: PASS
Service modules through portfolio continuity: PASS
Source, Rule, Form and change governance: PASS
Commercial component and visibility separation: PASS
Later-stage pricing: PASS
Quote and variance lineage: PASS
AI boundary: PASS
Controlled archetypes: PASS
Appendix F: PASS
Appendix G PF-05 evidence: PASS
PF-05: CLOSED
```

A jurisdiction/service claim cannot exceed the support state of its Pack module.

## 9. PF-06 — Editorial Finishing

### Status

Authorized by B05-REV-0017 and now the next substantive workstream.

### Tasks

- normalize controlled terminology and capitalization;
- reduce repeated constitutional explanations;
- improve chapter transitions;
- perform native-English editing;
- review client-facing examples;
- preserve controlled IDs, scenario behavior and case final states;
- record any semantic issue rather than silently editing architecture.

### Acceptance

- terminology agrees across manuscript, specifications and appendices;
- repetition is reduced without removing authority boundaries;
- chapter purpose and progression remain distinct;
- no controlled ID or legal-state meaning changes silently;
- editorial Review records material changes and unresolved findings.

## 10. PF-07 — Figures and Publication Apparatus

```text
Back Matter architecture: COMPLETE
Appendix A: COMPLETE FOR PF-02
Appendices B/C/E: COMPLETE FOR PF-04
Appendix D: COMPLETE FOR PF-03
Appendix F: COMPLETE FOR PF-05
Appendix G: COMPLETE FOR PF-04/PF-05
Figures: PLANNED, NOT CREATED
Glossary and Subject Index: INITIAL DRAFTS
PF-07 overall: OPEN
```

## 11. PF-08 — Structural and Rendered Validation

Validate:

- manuscript count, filenames, headings and numbering;
- internal links and fenced blocks;
- controlled IDs, scenario IDs and Profile sets;
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
PF-04: COMPLETE
PF-05: COMPLETE
PF-06: AUTHORIZED AND NEXT
PF-07–PF-09: OPEN
```

Until all gates close, Book 05 remains Complete Draft 1 rather than Release Candidate 1.