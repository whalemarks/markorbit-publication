# PUB-TASK-B04-VNEXT-CANDIDATE-02

## Title

Route-Aware Editorial Regeneration

## Objective

Generate `B04-vNEXT-CANDIDATE-02` from the immutable Book 04 RC1 manuscript and the Owner-Accepted editorial weave inputs, correcting the chapter-routing, reader-text leakage and placement defects recorded in `B04-AUD-0002`.

## Inputs

- Book 04 RC1 CH00–CH39;
- `B04-EDIT-0001`, `B04-EDIT-0002`, `B04-EDIT-0003`;
- `B04-AUD-0002` and `B04-DEC-0002`;
- `B04-ROUTE-0001` explicit route manifest;
- Architecture Canon vNext.1 and accepted WP-A–WP-F controls.

## Required work

1. Preserve RC1 source files without modification.
2. Discover exactly forty RC1 files and exactly forty editorial modules.
3. Route modules by reviewed chapter purpose rather than numeric identity alone.
4. Treat CH01 as publication apparatus only.
5. Use typed extraction that admits only reader-facing fields.
6. Support explicit placement modes per target chapter.
7. Support reviewed composed prose for structurally mismatched routes.
8. Record exact source modules, operation and placement in hidden provenance.
9. Reject editorial instructions, batch results and validation text in reader prose.
10. Generate CH00–CH39, an index, route report, source manifest and build report.
11. Run Candidate 01, Candidate Review 01, Integration 01–02C, WP-A–WP-F and release-state regressions.
12. Create a Draft PR. Do not merge.

## Acceptance criteria

```text
RC1 chapters discovered: 40 / 40
Editorial modules discovered: 40 / 40
Target chapters generated: 40 / 40
Apparatus-only chapters: 1 / 1
Explicit route entries: 40 / 40
Accepted editorial modules represented: 40 / 40
Reader-text leakage findings: 0
Unresolved numeric-only routes: 0
Duplicate chapter identities: 0
Missing chapter identities: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
```

## Authority boundary

Candidate 02 is a controlled review object. Task completion does not grant final Book 04 vNext Owner Acceptance, freeze, publication, implementation, deployment or External Protected Action authority.
