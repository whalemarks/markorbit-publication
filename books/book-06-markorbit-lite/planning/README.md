# Book 06 Planning

## Current stage

```text
Pre-Writing Audit — COMPLETE
→ Product Charter v0.3 — ACCEPTED
→ Product Baseline v0.1 — ACCEPTED
→ Chapter Map B06-TOC-V0.1 — ACCEPTED
→ Waves 1–7 / CH00–CH33 — ACCEPTED
→ Whole-Book Complete Draft 1 — OWNER ACCEPTED ON B06-REV-0013 MERGE
→ Release Candidate Hardening — NEXT
```

## Planning records

- [B06-PLN-0001 — Pre-Writing Audit](B06-PLN-0001_Pre-Writing_Audit.md)
- [B06-PLN-0002 — Authority and Source Map](B06-PLN-0002_Authority_and_Source_Map.md)
- [B06-PLN-0003 — Supplemental Idea Assessment](B06-PLN-0003_Supplemental_Idea_Assessment.md)
- [B06-PLN-0004 v0.3 — Product Charter](B06-PLN-0004_Product_Charter_Candidate.md)
- [B06-PLN-0005 v0.3 — Owner Decision Matrix](B06-PLN-0005_Product_Charter_Owner_Decision_Matrix.md)
- [B06-PLN-0006 — Commercial Plan and MVP Experiment](B06-PLN-0006_Commercial_Plan_and_MVP_Experiment_Candidate.md)
- [B06-PLN-0007 — Chapter Map / B06-TOC-V0.1](B06-PLN-0007_Chapter_Map_Candidate.md)
- [B06-PLN-0008 — Release Candidate Hardening Plan](B06-PLN-0008_Release_Candidate_Hardening_Plan.md)

## Whole-book review result

`B06-REV-0013` finds:

```text
34 / 34 chapter files present
Whole-book continuity: PASS
Product Charter coverage: PASS
Product Baseline coverage: PASS
Cross-Book boundaries: PASS
Blocking findings: 0
Major findings: 0
Upstream findings: 0
RC hardening requirements: 6
```

The six requirements concern metadata, reader-facing governance cleanup, controlled terms, repetition/cross-references, reader apparatus and source/render validation. They do not require Product Charter, Product Baseline or Chapter Map changes.

## Release Candidate hardening order

```text
Work Package A
Editorial and Structural Normalization

→ Work Package B
Reader Apparatus

→ Work Package C
Source, Render and RC Review
```

Each package should use one coherent branch and Draft PR, not one branch per chapter.

## Next task

```text
agent/book-06-rc-hardening-a-editorial-structure
```

Work Package A must normalize chapter headers, remove internal merge-state language from reader-facing prose, standardize controlled-term presentation and reduce avoidable repetition without changing Product meaning.

Release Candidate acceptance, implementation, production and external-action authority remain separate gates.
