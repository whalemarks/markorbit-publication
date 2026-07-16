# Book 06 Planning

## Current stage

```text
Pre-Writing Audit — COMPLETE
→ Product Charter v0.3 — ACCEPTED
→ Product Baseline v0.1 — ACCEPTED
→ Chapter Map B06-TOC-V0.1 — ACCEPTED
→ Waves 1–7 / CH00–CH33 — ACCEPTED
→ Whole-Book Complete Draft 1 — ACCEPTED
→ RC Hardening A — OWNER ACCEPTED ON B06-REV-0014 MERGE
→ RC Hardening B — READER APPARATUS — AUTHORIZED NEXT
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

`B06-REV-0013` confirms:

```text
34 / 34 chapter files present
Whole-book continuity: PASS
Product Charter coverage: PASS
Product Baseline coverage: PASS
Cross-Book boundaries: PASS
Blocking findings: 0
Major findings: 0
Upstream findings: 0
```

## RC Hardening A result

`B06-REV-0014` confirms:

```text
34 / 34 chapter headers normalized
23 chapter files modified
CH01 internal drafting-wave details removed
CH33 reader-facing evolution sequence applied
Chapter ID/title/order changes: 0
Controlled meaning changes: 0
Blocking / major / upstream findings: 0
```

Closed on merge:

```text
RC-H01 — chapter metadata normalization
RC-H02 — reader-facing governance cleanup
RC-H04 — repetition and cross-reference hardening
```

## Remaining hardening order

```text
Work Package B
Reader Apparatus
- RC-H03 controlled terms and distinction apparatus
- RC-H05 figures, appendices and index

→ Work Package C
Source, Render and RC Review
- RC-H06 source, citation and rendered validation
```

Each package uses one coherent branch and Draft PR, not one branch per chapter.

## Next task

```text
agent/book-06-rc-hardening-b-reader-apparatus
```

Release Candidate acceptance, implementation, production and external-action authority remain separate gates.