# B04-PLN-0019 — Candidate 01 Full-Book Review

## Status

Controlled review plan for `PUB-TASK-B04-VNEXT-CANDIDATE-REVIEW-01`.

## Review method

Candidate 01 is regenerated in a clean directory and inspected against the immutable RC1 chapter map and accepted editorial modules.

The review is not limited to file counts. It tests whether each inserted passage belongs to the chapter in which it appears, whether editorial instructions leaked into reader prose and whether insertion created a continuous argument.

## Review sequence

```text
regenerate Candidate 01
→ verify 40 / 40 structure and provenance
→ compare RC1 chapter identity with editorial-module intent
→ scan reader-visible text for control-language leakage
→ inspect high-risk chapter transitions
→ test canonical authority distinctions
→ classify findings
→ decide Candidate 01 acceptance or Candidate 02 repair
```

## Finding classes

- **B1 — structural blocker:** chapter-map or route mismatch;
- **B2 — reader-text blocker:** internal editorial or validation text visible to readers;
- **M1 — semantic major:** correct concept placed in the wrong argument;
- **M2 — continuity major:** generic insertion interrupts rather than integrates;
- **E1 — editorial:** duplication, abrupt transition or title mismatch;
- **N1 — non-blocking:** provenance or formatting improvement.

## High-risk checks

- CH01 is the accepted Table of Contents and must not receive conceptual chapter prose;
- CH15 is Capability Discovery, not the planned standalone Intelligence chapter;
- CH18 is Prepared Action / governed Execution, not the primary Capability-placement chapter;
- CH22 is Product Embedding and Cross-Product Context, not the controlling Product Installation chapter;
- CH28 is Asset Library, not Content / Artifact / Document;
- CH29–CH31 require explicit route reconciliation rather than blind number matching;
- CH39 must not expose batch result or validator text.

## Decision standard

Owner Acceptance requires all B1 and B2 findings to be zero and all M1/M2 findings to have reviewed resolution.

## Expected outcome

Candidate 01 is expected to remain a valid diagnostic review object. A bounded Candidate 02 is expected to be required; the architecture correction programme does not need to reopen.