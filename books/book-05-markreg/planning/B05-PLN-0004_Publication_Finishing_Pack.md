# B05-PLN-0004 — Publication Finishing Pack

## Status

- **Pack ID:** B05-PUBLICATION-FINISHING-PACK-001
- **Status:** Active — PF-01 through PF-07 complete
- **Source Reviews:** B05-REV-0012 through B05-REV-0027
- **Scope:** Book 05 CH00–CH47 and controlled publication assets
- **Target:** Release Candidate 1 candidate
- **Current substantive gate:** PF-08 — Structural and Rendered Validation

## 1. Purpose

This pack converts the complete CH00–CH47 manuscript into a coherent, validated and reviewable publication candidate without silently changing the MarkReg Product constitution.

It is publication work. It is not software implementation, deployment or authorization for an External Protected Action.

## 2. Workstream Sequence

```text
PF-01 metadata normalization
+ PF-02 artifact and Decision reconciliation
+ PF-03 reference journey consolidation
+ PF-04 scenario and user-surface consolidation
+ PF-05 jurisdiction and commercial reconciliation
+ PF-06 editorial finishing
+ PF-07 figures and publication apparatus
→ PF-08 structural and rendered validation
→ PF-09 Release Candidate and owner publication gate
```

## 3. Completed Work

```text
PF-01 — CH00–CH47 metadata complete
PF-02 — B05-SPEC-0001 v0.3
PF-03 — B05-SPEC-0002 v0.3
PF-04 — B05-SPEC-0003 v0.3
PF-05 — B05-SPEC-0004 v0.3
PF-06 — CH00–CH47 editorial finishing and whole-book closure
PF-07 — controlled figures, Source notes, Reader Notice and layout inputs
```

Accepted publication-finishing Reviews:

```text
B05-REV-0013 — publication architecture
B05-REV-0014–0017 — PF-02–PF-05
B05-REV-0018–0026 — PF-06
B05-REV-0027 — PF-07
```

## 4. Preserved Locks

```text
Recommendation ≠ Decision
Readiness ≠ Approval
Approval ≠ Execution
Human Selection ≠ provider appointment or acceptance
Provider Report ≠ Official Truth
Submission ≠ official acknowledgement
Registration ≠ certificate availability
Renewal Approval ≠ renewed right
Signed transaction ≠ official owner update
Visibility ≠ action right
Model memory ≠ current law
Pilot ≠ production
Publication ≠ implementation or protected-action authority
```

Reference states remain:

```text
EMBERLOOP — UK registered; US under examination; EU opposition; Japan/Australia future-action candidates
RIVERKITE — four ordinary renewals; one ownership-linked renewal; one cancellation defense; title/Evidence/licence work open
```

## 5. PF-07 — Figures and Publication Apparatus

**Status:** COMPLETE

### Final disposition

```text
planned Figure identities: 12
retained controlled sources: 11
B05-FIG-05: merged into B05-FIG-03
renumbering: none
```

### Delivered

- `figures/README.md` source and visual grammar;
- B05-FIG-01–04 and B05-FIG-06–12 Controlled Figure Source v1.0 files;
- captions, controlled source references and intended placements;
- Mermaid source for every retained Figure;
- text accessibility descriptions;
- source-level grayscale and legibility review;
- simplification and authority-boundary notes;
- B05-PUB-0002 Controlled Reader Source Notice v1.0;
- final Reader Notice;
- internal, external, provider, organization, AI and Figure citation conventions;
- B05-PUB-0005 Figure Register v1.0;
- B05-PUB-0006 Back Matter Map v0.2;
- stable Glossary, Subject Index and Figure page-reference inputs;
- B05-PUB-0008 RC1 Checklist v0.3;
- B05-REV-0027.

### Acceptance result

```text
Every planned Figure has a disposition: PASS
Every retained Figure has source, caption and accessibility evidence: PASS
No Figure creates a new semantic or authority claim: PASS
Source and Reader Notices complete: PASS
Page-reference inputs ready for layout: PASS
PF-07 Review: PASS
```

Actual Mermaid parsing, rendered grayscale, page fit, links, pagination and target-format output remain PF-08.

## 6. PF-08 — Structural and Rendered Validation

**Status:** AUTHORIZED AND NEXT

### Structural scope

- validate 48 manuscript files and Appendix A–G;
- validate eleven retained Figure source files and one merged disposition;
- validate filenames, headings, numbering and metadata;
- validate Markdown links and fenced blocks;
- validate `MR-*`, `MR-SCN-*`, `EL-*`, `RK-*` and Conformance Profiles;
- validate Manifest, Status, README, YAML and roadmap agreement.

### Rendered scope

- parse and render every Mermaid Figure;
- generate the target publication output;
- inspect page breaks, navigation and Back Matter order;
- inspect actual grayscale, accessibility, font size and page fit;
- confirm no Figure or text truncation;
- add and validate rendered page numbers and anchors;
- retain a separate PF-08 validation Review.

PF-08 is not complete merely because source files exist.

## 7. PF-09 — RC1 and Owner Publication Gate

**Status:** OPEN

Requires:

- PF-01 through PF-08 completion;
- no blocking architecture, semantic, structural or rendered finding;
- baseline commit and publication inventory;
- owner Release Candidate Decision;
- explicit final-publication, implementation and External Protected Action boundaries.

## 8. Current Decision

```text
PF-01–PF-07: COMPLETE
PF-08: AUTHORIZED AND NEXT
PF-09: OPEN
Release Candidate 1: NOT AUTHORIZED
Final publication: NOT AUTHORIZED
Implementation / production / External Protected Action: NOT AUTHORIZED
```

Until PF-08 and PF-09 close, Book 05 remains Complete Draft 1.