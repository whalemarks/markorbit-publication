# B04-PLN-0014 — Integrated Candidate Baseline Preparation

## Purpose

Prepare a deterministic, traceable and separately generated Book 04 vNext candidate without mutating RC1.

## Integration architecture

```text
immutable RC1 chapter
+ chapter-routed accepted amendment controls
+ provenance header
= generated vNext candidate chapter
```

The generated candidate is a review object. It is not an accepted baseline until a later Owner gate.

## Work sequence

1. discover exactly forty RC1 chapter files by CH00–CH39 identifiers;
2. register each chapter in B04-PROV-0001;
3. route correction sources from B04-CORR-0001 through B04-CORR-0004;
4. generate one candidate chapter for each RC1 chapter;
5. add a machine-readable provenance header and an integrated control section;
6. generate a candidate index and build report;
7. validate source immutability, chapter completeness and amendment attribution.

## Candidate directory

```text
books/book-04-workplace-product-architecture/vnext/candidate-01/
```

Generated outputs are intentionally excluded from RC1 paths.

## Editorial rule

The first generated candidate preserves RC1 prose and attaches the controlling vNext correction material at the exact chapter boundary. A later editorial pass may weave those controls into paragraph-level prose, but only while retaining the same provenance and supersession records.

This staged method prevents silent rewriting and makes every semantic change reviewable.

## Gates

```text
INTEGRATION-01 — deterministic candidate preparation
→ INTEGRATION-02 — paragraph-level editorial integration
→ full candidate review
→ Owner acceptance decision
→ optional freeze and publication preparation
```

## Protected boundaries

No change to RC1, B04-TOC-V0.1, Book 02, Architecture Canon, Decision Register or Books 05–07 frozen sources.
