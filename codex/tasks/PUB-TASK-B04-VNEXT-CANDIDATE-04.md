# PUB-TASK-B04-VNEXT-CANDIDATE-04

## Title

Final Navigation and Transition Consistency Correction

## Objective

Generate `B04-vNEXT-CANDIDATE-04` from Candidate 03 by correcting only the two reader-facing inconsistencies accepted in `B04-DEC-0004`:

1. synchronize CH01 Table of Contents with the accepted CH23 title and Workplace Product definition;
2. synchronize the CH22 transition into CH23 with the same definition.

Then scan the complete CH00–CH39 reader-facing manuscript for the superseded Lite-as-Workplace phrase and produce a final acceptance-candidate artifact.

## Authorized scope

- build Candidate 03 deterministically as the source candidate;
- replace `Lite as a Lightweight Workplace` with `Lite as a Lightweight Workplace Product` in generated CH01 navigation text;
- replace reader-facing descriptions that identify Lite itself as a Workplace with wording that identifies Lite as a Workplace Product;
- replace the stale CH22 transition asking how Lite operates as a lightweight Workplace;
- scan all generated reader-facing prose for superseded Lite-as-Workplace wording;
- preserve all other Candidate 03 content and provenance;
- add Candidate 04 provenance, reports, validator and CI;
- update Book 04 status and roadmap controls.

## Prohibited scope

- no RC1 manuscript modification;
- no new architecture correction;
- no changes to WP-A–WP-F, Integration 01–02C, Architecture Canon, Decision Register or Book 02;
- no broad copyediting, title redesign or semantic rewriting outside the two accepted consistency corrections;
- no freeze, publication, deployment, implementation or External Protected Action authorization.

## Required result

```text
Source Candidate 03 chapters: 40 / 40
Candidate 04 chapters generated: 40 / 40
CH01 navigation corrections: PASS
CH22 transition correction: PASS
Superseded Lite-as-Workplace reader findings: 0
Candidate 03 content preservation exceptions: 2 / 2 authorized
Reader-text leakage findings: 0
Architecture authority regression: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
Owner Acceptance readiness: YES
```

## Deliverables

- `B04-PLN-0024` execution plan;
- `B04-TRANSFORM-0002` bounded transform manifest;
- Candidate 04 builder and validator;
- Candidate 04 GitHub Actions workflow;
- `B04-REV-0022` generation review;
- complete CH00–CH39 review artifact with source and transform reports;
- updated Book 04 status and publication roadmap.

## Gate effect

Owner merge accepts Candidate 04 generation as the final consistency-corrected acceptance candidate. Final Book 04 vNext Owner Acceptance remains a separate explicit decision.