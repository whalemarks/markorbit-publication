# PUB-TASK-B04-VNEXT-PUBLICATION-PREP-01

## Title

Materialize Accepted Manuscript and Prepare Freeze Candidate

## Objective

Materialize the Owner-accepted `B04-vNEXT-CANDIDATE-04` manuscript as repository-controlled files and prepare a verifiable freeze candidate without changing the immutable RC1 baseline.

## Required work

1. Run `tools/build_book04_vnext_candidate_04.py` deterministically.
2. Copy CH00–CH39 into `books/book-04-workplace-product-architecture/accepted-vnext/manuscript/`.
3. Copy the accepted candidate index, source manifest, route report, transform report and build report into `accepted-vnext/`.
4. Generate a SHA-256 materialization manifest covering every accepted-vNext file.
5. Verify the materialized files byte-for-byte match a fresh Candidate 04 build.
6. Record publication-preparation status and freeze readiness.

## Protected boundaries

- Do not modify `books/book-04-workplace-product-architecture/manuscript/` RC1 files.
- Do not modify the Architecture Canon, Decision Register, Book 02 or Books 05–07 frozen manuscripts.
- Do not authorize freeze, publication, distribution, implementation, deployment or External Protected Action.

## Acceptance result

```text
Accepted chapters materialized: 40 / 40
Candidate 04 byte-equivalence: PASS
Materialization manifest coverage: PASS
RC1 source modifications: 0
Publication freeze readiness: YES
Freeze authorization: NOT YET GRANTED
```
