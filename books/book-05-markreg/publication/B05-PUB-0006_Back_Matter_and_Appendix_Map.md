# B05-PUB-0006 — Back Matter and Appendix Map

## Status

- **Status:** Controlled Baseline
- **Decision:** Book 05 will use both reader-facing Appendix A–G and independent publication apparatus
- **Authority:** B05-REV-0012, B05-PLN-0004 and owner direction following PR #43
- **Applies to:** Book 05 publication finishing and all rendered editions

## 1. Decision

Book 05 must not end at CH47 without reader-reference material.

The final publication architecture is:

```text
Front Matter
→ CH00–CH47
→ Appendix A–G
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

Editorial Style, Cross-Book Reconciliation and RC1 Checklist are controlled production records. They may be included in a repository or professional edition but do not need to appear as reader chapters in every rendered edition.

## 2. Why Appendices and Publication Apparatus Are Separate

Appendices answer:

> What compact reference does the reader need while using the book?

Publication apparatus answers:

> How is the book edited, sourced, indexed, illustrated, reconciled and validated?

The two functions should not be collapsed.

```text
Appendix = reader-facing reference projection
Publication record = editorial and release control
Specification = controlled Product truth
```

## 3. Final Reader-Facing Back Matter

### Appendix A — Full-Lifecycle Artifact and Decision Map

Reader need: identify the major artifacts, decisions, lineage, owners and formalization boundaries.

Controlled source: B05-SPEC-0001 after PF-02.

### Appendix B — Lifecycle State and Authority Matrix

Reader need: distinguish Product, formal, Execution, provider, official, professional and client-facing states.

Controlled sources: CH07, CH21–CH42 and the extended artifact/scenario contracts.

### Appendix C — Participant Visibility and Action Rights Matrix

Reader need: understand what clients, professionals, reviewers, approvers, coordinators, finance users, providers, administrators and AI may see and do.

Controlled source: B05-SPEC-0003 after PF-04.

### Appendix D — Reference Journeys

Reader need: follow `EMBERLOOP` and `RIVERKITE` across the complete lifecycle without rereading every chapter.

Controlled source: B05-SPEC-0002 after PF-03.

### Appendix E — Priority Conformance Scenarios

Reader need: test whether an edition or implementation preserves the constitutional and safety boundaries.

Controlled source: B05-SPEC-0003 after PF-04.

### Appendix F — Minimum Jurisdiction Pack Checklist

Reader need: determine whether a jurisdiction/service is sufficiently sourced, configured, reviewed and operable.

Controlled source: B05-SPEC-0004 after PF-05.

### Appendix G — MarkReg Conformance Profiles

Reader need: state supported Product depth honestly and distinguish partial implementation from Full-Lifecycle conformance.

Controlled sources: CH46–CH47 and the completed conformance checklist.

## 4. Final Publication Apparatus

### B05-PUB-0001 — Editorial Style and Terminology

Controls terminology, capitalization, state language, source language, repetition and native-English editing.

### B05-PUB-0002 — Source and Authority Notes

Explains the authority of architecture records, specifications, official sources, provider evidence, organization Knowledge, scenarios and AI outputs.

### B05-PUB-0003 — Glossary

Defines reader-facing terms while preserving Book 02 Core authority and Book 05 artifact distinctions.

### B05-PUB-0004 — Subject Index

Provides stable chapter and appendix navigation and later rendered page references.

### B05-PUB-0005 — Figure Register

Controls the identity, purpose, source and status of reusable diagrams.

### B05-PUB-0007 — Cross-Book Reconciliation

Confirms Book 05 conformance with Books 01–04 and boundaries with Books 06–07.

### B05-PUB-0008 — RC1 Checklist

Records whether the manuscript, specifications, appendices, apparatus, figures, validation and owner gate support Release Candidate 1.

## 5. Repository Structure

```text
books/book-05-markreg/
├── manuscript/
│   └── CH00–CH47
├── specifications/
│   └── B05-SPEC-0001–0004
├── appendices/
│   ├── B05-APP-A ... B05-APP-G
│   └── README.md
├── figures/
│   └── B05-FIG-01 ... B05-FIG-12
├── publication/
│   ├── B05-PUB-0001 ... B05-PUB-0008
│   └── README.md
├── planning/
└── reviews/
```

The `figures/` directory will be created when the first controlled figure source is added.

## 6. Source-of-Truth Matrix

| Reader asset | Controlled source of truth | May simplify | May create new rule |
| --- | --- | --- | --- |
| Appendix A | B05-SPEC-0001 | yes | no |
| Appendix B | extended artifact/state/scenario controls | yes | no |
| Appendix C | B05-SPEC-0003 and CH44 | yes | no |
| Appendix D | B05-SPEC-0002 | yes | no |
| Appendix E | B05-SPEC-0003 | yes | no |
| Appendix F | B05-SPEC-0004 | yes | no |
| Appendix G | CH46–CH47 and conformance checklist | yes | no |
| Glossary | Book 02 terms plus reviewed Book 05 usage | yes | no |
| Subject Index | final manuscript and appendices | navigation only | no |
| Figures | referenced controlled chapters/specifications | visual only | no |

## 7. Version and Reconciliation Rule

Every appendix and publication record should retain:

- record ID;
- status;
- source baseline;
- last reconciliation review;
- known gaps;
- superseded-by reference where applicable;
- rendered-edition inclusion status.

When a specification changes materially:

1. identify affected appendices, glossary terms, index entries and figures;
2. mark them for revalidation;
3. preserve the prior publication baseline;
4. do not silently alter a released edition.

## 8. Edition Rule

A repository edition may include all controlled publication records.

A reader PDF or print edition should normally include:

- Appendix A–G;
- Source and Authority Notes;
- Glossary;
- Subject Index;
- figure captions and registered figures.

An implementation-oriented edition may additionally include:

- Cross-Book Reconciliation;
- conformance and RC1 checklists;
- specification identifiers and extended traceability.

All editions must preserve the same Product and authority meaning.

## 9. Completion States

A Back Matter file may be:

- planned;
- controlled scaffold;
- controlled draft;
- reconciled candidate;
- RC1;
- superseded.

Creating a file path does not complete the content.

The current Appendix A–G and publication records are controlled scaffolds except this Back Matter Map, which is the controlled structural baseline.

## 10. Change Control

Changing the Appendix A–G inventory or the reader-facing order requires:

- a recorded editorial reason;
- impact assessment on CH01, manifests, figures and rendered formats;
- confirmation that no specification authority is moved into an appendix;
- publication review.

Minor wording and navigation improvements do not require a chapter-map change.

## 11. Acceptance Criteria

This Back Matter architecture is accepted when:

1. the paths and titles are recorded in active Book 05 manifests and navigation;
2. CH01 includes the reader-facing Appendix A–G sequence;
3. B05-PLN-0004 reflects the structural lock;
4. B05-REV-0013 confirms no conflict with Book 04 or prior books;
5. Appendix and publication files state their non-authoritative relationship to specifications;
6. the later RC1 review verifies full content and rendered order.

## 12. Boundary

This map does not:

- declare Appendix A–G complete;
- close PF-02 through PF-08;
- make Book 05 RC1;
- authorize final publication;
- authorize implementation or external protected action.

It removes ambiguity about what Book 05 must contain before RC1.