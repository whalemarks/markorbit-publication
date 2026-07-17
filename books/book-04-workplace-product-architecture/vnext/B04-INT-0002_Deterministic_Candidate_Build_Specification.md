# B04-INT-0002 — Deterministic Candidate Build Specification

## Candidate identity

```text
Candidate ID: B04-vNEXT-CANDIDATE-01
Status: GENERATED REVIEW CANDIDATE
Authority: none beyond accepted source controls
```

## Source precedence

1. RC1 supplies the historical chapter body and structure.
2. WP-B controls Workplace authority and data-boundary meaning.
3. WP-C controls Product Installation, Projection, Handoff and Return meaning.
4. WP-D controls MarkReg, Lite, Sites and MGSN interfaces.
5. WP-E controls cross-Workplace collaboration, exit and portability.
6. Later sources in this list refine overlapping earlier amendment controls but may not weaken them.

## Generated chapter structure

Each candidate chapter contains:

```text
provenance header
RC1 chapter body
integrated vNext control section, when routed
source attribution footer
```

The control section is generated from the chapter module in the accepted amendment manuscript. It is not an unreviewed paraphrase.

## Discovery rules

- Search the RC1 manuscript directory recursively.
- Identify chapters by a unique `CH00` through `CH39` token in the filename.
- Exactly one source file must resolve for every chapter.
- Duplicate or missing chapter identities fail the build.

## Routing rules

- Read B04-CORR-0001 through B04-CORR-0004.
- A chapter is routed to an amendment only when its CH identifier appears in the corresponding correction ledger.
- Extract the amendment chapter module beginning at the heading containing that CH identifier and ending before the next same-level chapter heading.
- Every inserted control module must record amendment and ledger identities.

## Output rules

- Candidate files are named `CHxx.md` under `vnext/candidate-01/manuscript/`.
- `CANDIDATE-INDEX.md` records all forty outputs.
- `BUILD-REPORT.md` records source counts, routed controls and failures.
- Repeated builds from the same repository commit must be byte-for-byte stable.

## Acceptance requirements

```text
RC1 chapters discovered: 40 / 40
Candidate chapters generated: 40 / 40
Accepted amendments registered: 4 / 4
Unattributed inserted controls: 0
Duplicate chapter identities: 0
Missing chapter identities: 0
RC1 mutations: 0
```

## Status boundary

Generated files are review candidates only. Generation does not grant Owner acceptance, freeze, publication authority or implementation authority.
