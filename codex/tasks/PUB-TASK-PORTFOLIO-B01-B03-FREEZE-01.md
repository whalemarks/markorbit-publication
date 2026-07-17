# PUB-TASK-PORTFOLIO-B01-B03-FREEZE-01

## Title

Freeze Book 01 and Book 03 Release Candidate 1 baselines

## Objective

Bring the seven-book MarkOrbit publication portfolio into one consistent controlled state by freezing the already accepted Book 01 and Book 03 RC1 baselines.

## Inputs

- Book 01 RC1 manuscript and publication apparatus;
- Book 03 RC1 manuscript and publication apparatus;
- accepted Books 01–04 portfolio baseline;
- current Publication Roadmap and book status records;
- existing frozen baselines for Books 02 and 04–07.

## Required work

1. Inventory all controlled Markdown files under each book's `manuscript/` and `publication/` directories.
2. Verify Book 01 contains the Preface, Contents, Chapters 1–9 and Appendices A–C.
3. Verify Book 03 contains CH00–CH34 and Appendices A–H.
4. Generate a deterministic `FREEZE-MANIFEST.md` for each book with per-file SHA-256 bindings.
5. Record formal freeze decisions and reviews.
6. Update Book 01, Book 03 and portfolio status records.
7. Add continuous validation so any later modification to the frozen sets fails without an explicit change proposal.

## Acceptance criteria

```text
Book 01 accepted RC1 content inventory: PASS
Book 01 chapter sequence: 9 / 9
Book 01 appendices: A–C / 3
Book 03 accepted RC1 content inventory: PASS
Book 03 chapter sequence: CH00–CH34 / 35
Book 03 appendices: A–H / 8
Per-file SHA-256 coverage: PASS
Book 01 freeze: GRANTED
Book 03 freeze: GRANTED
Seven-book portfolio frozen-baseline coverage: 7 / 7
Public/commercial distribution: NOT AUTHORIZED
Implementation or deployment: NOT AUTHORIZED
```

## Boundary

This task does not rewrite accepted prose and does not authorize public release, commercial distribution, implementation, deployment or External Protected Action.
