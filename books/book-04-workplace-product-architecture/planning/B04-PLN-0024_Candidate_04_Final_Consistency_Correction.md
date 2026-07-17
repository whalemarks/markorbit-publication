# B04-PLN-0024 — Candidate 04 Final Consistency Correction

## Purpose

Produce the final consistency-corrected Book 04 vNext acceptance candidate without reopening the accepted architecture or editorial consolidation programme.

## Source

- deterministic Candidate 03 output;
- `B04-AUD-0004` and `B04-DEC-0004`;
- immutable RC1 provenance carried through Candidate 02 and Candidate 03.

## Execution sequence

1. Generate Candidate 03 into a temporary source directory.
2. Assert CH00–CH39 completeness and Candidate 03 provenance.
3. Apply the two authorized reader-facing replacements:
   - CH01 navigation/title/description synchronization;
   - CH22 transition synchronization.
4. Preserve every other generated chapter byte-for-byte apart from Candidate 04 provenance/status metadata.
5. Scan all reader-facing prose for superseded Lite-as-Workplace wording.
6. Verify Product Installation placement, CH23 heading, CH37 portability structure and prior closed findings remain intact.
7. Write Candidate 04 index, source manifest, transform report and build report.
8. Run protected-source diff validation.
9. Upload the complete Candidate 04 artifact for final Owner Acceptance review.

## Acceptance conditions

```text
CH00–CH39 complete
CH01 synchronized
CH22 synchronized
CH23 remains Workplace Product
superseded Lite-as-Workplace reader findings = 0
all Candidate 03 architecture and consolidation controls retained
RC1 modifications = 0
blocking findings = 0
Owner Acceptance readiness = YES
```

## Protected boundary

This plan does not authorize modification of RC1, publication apparatus, Architecture Canon, Decision Register, Book 02, Books 05–07 frozen sources, implementation repositories or production systems.