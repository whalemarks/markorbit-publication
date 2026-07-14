# Book 05 Publication Apparatus

## Status

- **Book status:** Complete Draft 1 — Publication Finishing Active
- **Publication stage:** PF-06 Editorial Finishing
- **Current pack:** B05-PUBLICATION-FINISHING-PACK-001
- **Completed editorial tranche:** PF-06A — editorial baseline and term audit
- **Next editorial tranche:** PF-06B — CH00–CH22
- **Independent RC1 blocker:** PF-01B CH02–CH47 metadata normalization

## Purpose

This directory contains the reader-facing and editorial apparatus required to turn the controlled manuscript into a Release Candidate.

Publication records may explain, organize and project the controlled manuscript. They do not create Product authority or silently amend specifications.

## Inventory

| ID | Record | Purpose | Current status |
| --- | --- | --- | --- |
| B05-PUB-0001 | Editorial Style and Terminology | control voice, capitalization, artifact names, authority language, compression and transitions | Controlled Editorial Standard v0.2 — PF-06A complete |
| B05-PUB-0002 | Source and Authority Notes | explain source hierarchy and legal/official authority boundaries | controlled scaffold — PF-07/PF-08 open |
| B05-PUB-0003 | Glossary | provide reader definitions and controlled-term references | Controlled Working Glossary v0.2 — PF-06A reconciled |
| B05-PUB-0004 | Subject Index | provide reader navigation | Controlled Working Index v0.2 — PF-06A reconciled |
| B05-PUB-0005 | Figure Register | define and track publication figures | controlled scaffold — figures not created |
| B05-PUB-0006 | Back Matter and Appendix Map | lock final order and relation between appendices and publication records | controlled baseline |
| B05-PUB-0007 | Cross-Book Reconciliation | reconcile Book 05 with Books 01–04 and downstream Books 06–07 | controlled scaffold |
| B05-PUB-0008 | RC1 Checklist | define Release Candidate completion evidence | controlled scaffold |
| B05-PUB-0009 | Term Variation and Editorial Audit | record terminology, repetition, transition and native-English findings | Controlled Audit v0.1 — PF-06A complete |

## Editorial Batch Sequence

```text
PF-06A — COMPLETE
- B05-PUB-0001 v0.2
- B05-PUB-0003 v0.2
- B05-PUB-0004 v0.2
- B05-PUB-0009 v0.1
- B05-REV-0018

PF-06B — NEXT
- CH00–CH22
- metadata CH02–CH22

PF-06C
- CH23–CH47
- metadata CH23–CH47

PF-06D
- specifications, appendices and publication apparatus
- whole-book term and transition closure
```

PF-06A establishes the rules. It does not represent the manuscript as line-edited.

## Back Matter Order

```text
CH47 — Conclusion
→ Appendix A — Full-Lifecycle Artifact and Decision Map
→ Appendix B — Lifecycle State and Authority Matrix
→ Appendix C — Participant Visibility and Action Rights Matrix
→ Appendix D — Reference Journeys
→ Appendix E — Priority Conformance Scenarios
→ Appendix F — Minimum Jurisdiction Pack Checklist
→ Appendix G — MarkReg Conformance Profiles
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

Editorial Style, Term Variation Audit, Cross-Book Reconciliation and RC1 Checklist support publication production but do not need to appear as reader chapters in every rendered edition.

## Authority Rule

Where sources conflict, authority follows this order:

1. repository Architecture Canon and accepted Books 01–04 baseline;
2. owner-accepted Book 05 chapter map and Review decisions;
3. controlled Book 05 specifications;
4. reviewed active manuscript;
5. reviewed appendices and publication apparatus;
6. rendered or exported publication files.

Rendered convenience and editorial polish may not change controlled meaning.

## Completion Gate

This directory is publication-complete only when:

- PF-01 through PF-08 close;
- PF-06B through PF-06D complete;
- the Glossary and Subject Index are reconciled against the edited CH00–CH47 manuscript and Appendix A–G;
- figures are created and referenced;
- source and authority notes cover all material source classes;
- cross-book reconciliation passes;
- structural and rendered validation passes;
- B05-PUB-0008 records RC1 readiness.

Until then, the files remain controlled standards, working records, scaffolds or baselines rather than final publication assets.