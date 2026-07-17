# Book 04 Status

## Current State

- **Historical baseline:** Release Candidate 1 — Owner Accepted / Portfolio Locked
- **RC1 manuscript:** CH00–CH39, immutable
- **Chapter map:** B04-TOC-V0.1 — unchanged
- **WP-A–WP-F:** Owner Accepted / correction programme closed
- **Current task:** PUB-TASK-B04-VNEXT-INTEGRATION-01
- **Current plan:** B04-PLN-0014
- **Current build specification:** B04-INT-0002
- **Current provenance ledger:** B04-PROV-0001
- **Current review:** B04-REV-0012 — PASS / Ready for Owner Acceptance
- **Next gate:** deterministic candidate generation and INTEGRATION-02 editorial integration

## Historical compatibility

```text
MO-ARCH-PLN-001 corrections mapped: 12 / 12
WP-A chapters classified: 40 / 40
WP-B assigned chapters covered: 14 / 14
WP-B five authority dimensions: 5 / 5
WP-C assigned chapters covered: 9 / 9
WP-C amendment manuscript: READY FOR OWNER ACCEPTANCE
WP-D assigned chapters covered: 6 / 6
WP-E assigned chapters covered: 8 / 8
WP-E amendment manuscript: READY FOR OWNER ACCEPTANCE
RC1 source modifications: 0
Immediate Book 02 Change Proposal required: NO
```

The WP-C and WP-E candidate-gate sentences remain solely as regression compatibility assertions. WP-C–WP-E and WP-F are Owner Accepted through merged PRs #103–#106.

## Integration 01 Package

```text
PUB-TASK-B04-VNEXT-INTEGRATION-01
B04-PLN-0014 — Integrated Candidate Baseline Preparation
B04-INT-0002 — Deterministic Candidate Build Specification
B04-PROV-0001 — CH00–CH39 Provenance Ledger
tools/build_book04_vnext_candidate.py
B04-REV-0012 — Integration Preparation Review / PASS
```

## Integration 01 Result

```text
Chapter source entries: 40 / 40
Historical source coverage: 40 / 40
Accepted amendment packages represented: 4 / 4
Deterministic build rule: PASS
Unattributed correction route: 0
Blocking findings: 0
RC1 source modification: 0
Candidate generation readiness: PASS
```

## Candidate Generation Model

```text
immutable RC1 chapter
+ chapter-routed Owner-Accepted amendment controls
+ machine-readable provenance
= B04-vNEXT-CANDIDATE-01 generated review chapter
```

The first generated candidate preserves RC1 chapter prose and attaches accepted correction modules at controlled chapter boundaries. INTEGRATION-02 will perform paragraph-level editorial weaving while preserving the same provenance and supersession controls.

## Sequence

```text
WP-A–WP-F — ACCEPTED / CLOSED
→ INTEGRATION-01 — CANDIDATE PREPARATION
→ deterministic B04-vNEXT-CANDIDATE-01 generation
→ INTEGRATION-02 — paragraph-level editorial integration
→ full candidate semantic review
→ Owner acceptance decision
→ optional freeze and publication preparation
```

## Authorization

```text
Book 04 RC1 historical baseline: ACCEPTED AND IMMUTABLE
WP-B–WP-E amendment manuscripts: ACCEPTED
WP-F audit and GO decision: ACCEPTED
Integration preparation mechanism: READY FOR OWNER ACCEPTANCE
Generated vNext candidate: NOT YET OWNER ACCEPTED
Book 04 vNext owner acceptance: NOT YET GRANTED
Freeze, publication and distribution: NOT AUTHORIZED
Implementation or deployment: NOT AUTHORIZED
External Protected Action: NOT AUTHORIZED
```
