# B04-INT-0001 — Integrated Candidate Baseline Manifest

## Purpose

Define the inputs, order, provenance and acceptance controls for the future integrated Book 04 vNext Candidate Baseline.

## Source order

1. Historical source: Book 04 RC1 CH00–CH39 and B04-TOC-V0.1;
2. Authority correction: B04-VNEXT-WPB-0001 and B04-CORR-0001;
3. Product participation correction: B04-VNEXT-WPC-0001 and B04-CORR-0002;
4. Product/network interface correction: B04-VNEXT-WPD-0001 and B04-CORR-0003;
5. Collaboration and portability correction: B04-VNEXT-WPE-0001 and B04-CORR-0004;
6. Full-book audit and decision: B04-AUD-0001 and B04-DEC-0001.

## Integration rules

- Do not edit the RC1 directory in place.
- Create a separate candidate-baseline directory.
- Preserve CH00–CH39 numbering unless a controlled decision authorizes structural change.
- Integrate amendment text into the relevant chapter rather than appending untraceable prose.
- Record every superseded RC1 passage and its amendment source.
- Preserve terms exactly where they express canonical distinctions.
- Resolve duplicate explanatory material without weakening authority boundaries.
- Preserve examples only when they do not imply ownership, authority or automatic-state transitions inconsistent with vNext.
- Maintain a machine-checkable chapter provenance ledger.

## Candidate acceptance requirements

```text
Integrated chapters: 40 / 40
Amendment sources incorporated: 4 / 4
Supersession entries resolved: 100%
Blocking contradiction: 0
Unattributed amendment insertion: 0
RC1 source mutation: 0
Book 02 semantic change: 0 unless separately authorized
```

## Candidate status

```text
Integrated candidate: NOT YET CREATED
Integration preparation: AUTHORIZED AFTER WP-F OWNER MERGE
Owner acceptance: REQUIRED AFTER INTEGRATION
Freeze/publication: NOT AUTHORIZED
```