# PUB-TASK-PORTFOLIO-RELEASE-CANDIDATES-01

## Objective
Generate seven deterministic publication release-candidate overlays from the frozen Books 01–07 baselines without modifying any frozen source file.

## Inputs
- seven frozen book baselines;
- common series and project front matter;
- seven book-specific front-matter objects;
- `PORTFOLIO-OVERLAY-0001` with 18 approved safe corrections.

## Work
1. Create one candidate directory for each book.
2. Add the common series page, project introduction and book-specific front matter.
3. Copy the controlled frozen manuscript and available publication/figure assets.
4. Apply exactly 18 approved copyedit corrections to generated copies only.
5. Generate per-book manifests, SHA-256 bindings and portfolio build report.
6. Preserve unresolved legal metadata as explicit release blockers.

## Acceptance
```text
Books generated: 7 / 7
Approved overlay corrections applied: 18 / 18
Semantic changes: 0
Frozen manuscript modifications: 0
Candidate manifests: 7 / 7
Candidate release authorization: NOT GRANTED
```

## Boundary
These are review and rendering-input candidates. They do not authorize publication, ISBN procurement, distribution, implementation or deployment.
