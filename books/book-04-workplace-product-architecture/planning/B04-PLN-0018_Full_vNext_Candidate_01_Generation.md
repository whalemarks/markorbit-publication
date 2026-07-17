# B04-PLN-0018 — Full vNext Candidate 01 Generation

## Objective

Produce one complete CH00–CH39 Book 04 vNext review manuscript by applying all accepted editorial weave inputs to the immutable RC1 source set.

## Build stages

1. discover and normalize historical RC1 chapter identifiers;
2. parse exactly one editorial weave module for every CH00–CH39 chapter;
3. extract candidate prose from `Weave text`, canonical equations and named insertions;
4. weave the candidate prose into the introductory argument of the RC1 chapter;
5. replace RC1 maturity metadata only in the generated copy;
6. record RC1 source path, source hash and editorial source in hidden provenance;
7. generate an index, source manifest and build report;
8. validate semantic locks and protected-source boundaries;
9. publish the generated candidate as a GitHub Actions review artifact.

## Placement policy

The first candidate uses a deterministic editorial placement policy:

- preserve the chapter title and RC1 argument order;
- place accepted weave prose at the first natural section boundary after the chapter introduction;
- keep inserted prose reader-facing and continuous, without correction-route headings;
- keep provenance machine-readable through HTML comments and the manifest;
- defer fine-grained copyediting and local paragraph movement to the full-candidate review.

This policy gives reviewers one stable full-book object before line-by-line editorial refinement.

## Maturity boundary

Candidate 01 is a review manuscript. It is not the accepted vNext baseline, a frozen release, a publication-ready edition or an implementation specification.

## Completion result required

```text
RC1 chapters discovered: 40 / 40
Editorial weave modules discovered: 40 / 40
Candidate chapters generated: 40 / 40
Candidate chapters with provenance: 40 / 40
Full chapter sequence: CH00–CH39
Reader-visible correction-route appendices: 0
RC1 source modifications: 0
Blocking findings: 0
```
