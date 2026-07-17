# PUB-TASK-B04-VNEXT-CANDIDATE-01

## Title

Apply Editorial Weave Inputs and Generate the Full Book 04 vNext Candidate Manuscript

## Purpose

Generate the first complete, continuously readable Book 04 vNext candidate from the immutable RC1 manuscript and the Owner-Accepted editorial weave inputs `B04-EDIT-0001`, `B04-EDIT-0002` and `B04-EDIT-0003`.

## Sources

- Book 04 RC1 CH00–CH39;
- `B04-PROV-0001`;
- accepted WP-B–WP-E amendments and correction ledgers;
- `B04-EDIT-0001` — CH00–CH12;
- `B04-EDIT-0002` — CH13–CH27;
- `B04-EDIT-0003` — CH28–CH39;
- Architecture Canon vNext.1 and Decision Register.

## Required outputs

1. deterministic weave-application tool;
2. forty generated candidate chapters in a clean build directory;
3. candidate index, source-hash manifest and build report;
4. semantic and structural validation;
5. review record and Owner gate;
6. GitHub Actions artifact containing the complete candidate manuscript.

## Candidate rule

```text
immutable RC1 chapter
+ chapter-specific accepted weave prose
+ hidden machine-readable provenance
= continuously readable vNext Candidate 01 chapter
```

The generated reader-facing manuscript must not expose mechanical correction-ledger tables or `Integrated vNext Control Route` appendices. Provenance remains available through hidden comments and the build manifest.

## Acceptance criteria

```text
RC1 chapters discovered: 40 / 40
Editorial weave modules discovered: 40 / 40
Candidate chapters generated: 40 / 40
Candidate chapters with provenance: 40 / 40
Reader-visible correction-route appendices: 0
Duplicate chapter identities: 0
Missing chapter identities: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
```

## Gate effect

Owner merge accepts the generation mechanism and Candidate 01 as a controlled full-book review object. It does not grant final Book 04 vNext acceptance, freeze, publication, implementation, deployment or External Protected Action authority.
