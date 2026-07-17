# B04-PLN-0020 — Candidate 02 Route-Aware Regeneration

## Decision basis

`B04-DEC-0002` rejected Candidate 01 as final prose because numeric-only routing, permissive extraction and generic placement produced chapter mismatch and reader-text leakage. The accepted WP-A–WP-F architecture remains valid.

## Method

```text
immutable RC1 chapter
+ reviewed target-title assertion
+ explicit target-to-module route
+ typed reader-facing extraction
+ chapter-specific placement
+ exact provenance
= B04-vNEXT-CANDIDATE-02
```

## Reviewed routing corrections

- CH01 is apparatus only.
- CH01 conceptual module is composed into CH02.
- CH18 Capability module is routed to actual Capability chapter CH15.
- CH15 Intelligence module is routed into recommendation context CH17.
- CH18 RC1 remains intact; CH19 retains the Human Review module.
- CH28 Asset Library remains intact.
- Content / Artifact / Version / Render / Edit / Delivery modules are routed to actual CH29–CH31 topics.
- Portability is composed into cross-Orbit governance CH37.
- Conformance and final responsibility-chain prose are separately composed into CH38 and CH39.

## Extraction rules

Only explicit reader-facing fields are admitted. Retain, replace, normalize, supersede, placement, authority, continuity and batch-result fields remain build controls and may not enter candidate prose.

## Outputs

- `B04-ROUTE-0001` route manifest;
- route-aware Candidate 02 builder;
- Candidate 02 validator and workflow;
- complete CH00–CH39 review artifact;
- route report, source manifest and build report;
- `B04-REV-0018` generation review.

## Gate

Successful generation authorizes a second full-book review only. It does not grant final Owner Acceptance or freeze.
