# Book 05 Publication Apparatus

## Status

- **Book state:** Complete Draft 1 — PF-07 source apparatus complete
- **Current stage:** PF-08 — Structural and Rendered Validation
- **Current pack:** B05-PUBLICATION-FINISHING-PACK-001
- **Latest completed Review:** B05-REV-0026; PF-07 Review added in this branch

Publication records organize and project controlled content. They do not create Product authority or silently amend Specifications.

## Inventory

| ID | Record | Status |
| --- | --- | --- |
| B05-PUB-0001 | Editorial Style and Terminology | Controlled Editorial Standard v0.2 |
| B05-PUB-0002 | Source and Authority Notes | Controlled Reader Source Notice v1.0 — PF-07 complete |
| B05-PUB-0003 | Glossary | Controlled Glossary v0.3 — stable layout inputs complete |
| B05-PUB-0004 | Subject Index | Controlled Subject Index v0.3 — stable layout inputs complete |
| B05-PUB-0005 | Figure Register | Controlled Figure Register v1.0 — 11 retained / 1 merged |
| B05-PUB-0006 | Back Matter and Appendix Map | Controlled Back Matter Map v0.2 — PF-07 reconciled |
| B05-PUB-0007 | Cross-Book Reconciliation | Controlled Reconciliation v0.2 — complete |
| B05-PUB-0008 | RC1 Checklist | Controlled Checklist v0.3 — PF-07 updated; PF-08/PF-09 open |
| B05-PUB-0009 | Term Variation and Editorial Audit | Controlled Audit v0.2 — closed |

## PF-07 Deliverables

```text
Twelve planned figure identities reviewed
→ eleven controlled Mermaid source files retained
→ B05-FIG-05 merged into B05-FIG-03
→ captions and controlled source references complete
→ accessibility descriptions complete
→ source-level grayscale and legibility review complete
→ Source and Authority Notes complete
→ final Reader Notice complete
→ citation convention complete
→ stable Glossary/Index/Figure page-reference inputs complete
```

Actual Mermaid parsing, page fit, grayscale output, links, anchors, page numbers and target-format rendering remain PF-08.

## Back Matter Order

```text
CH47
→ Appendix A–G
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

Editorial Standard, Term Audit, Cross-Book Reconciliation and RC1 Checklist are production-control records and need not appear as reader chapters in every edition.

## Figure Inventory

```text
B05-FIG-01–04: retained
B05-FIG-05: merged into B05-FIG-03
B05-FIG-06–12: retained

controlled figure sources: 11
rendered figure validation: PF-08
```

The `figures/` directory contains the source, caption, placement intent, accessibility description, grayscale notes and authority boundary for every retained figure.

## Page-Reference Rule

Chapter, Appendix, Specification, publication and Figure identifiers remain the stable source references.

PF-08 may add rendered page numbers and anchors after pagination stabilizes. Repagination changes the presentation reference, not the controlled identity.

## Authority Order

1. Architecture Canon and accepted Books 01–04;
2. owner-accepted Book 05 structure and Reviews;
3. B05-SPEC-0001–0004 v0.3;
4. reviewed active manuscript;
5. Appendix, publication and Figure projections;
6. rendered/exported outputs.

Rendered convenience never changes controlled meaning.

## Current Gate

```text
PF-01–PF-07: COMPLETE after PF-07 Review
PF-08 structural and rendered validation: NEXT
PF-09 owner RC1 Decision: OPEN
Release Candidate 1: NO
Final publication: NO
Implementation / production / External Protected Action: NOT AUTHORIZED
```

PF-08 must validate file inventory, links, controlled IDs, Mermaid fences, actual figure rendering, accessibility, pagination, Back Matter order and non-truncation.