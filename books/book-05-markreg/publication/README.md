# Book 05 Publication Apparatus

## Status

- **Book state:** Release Candidate 1 — effective upon owner merge of the PF-09 pull request
- **RC1 content baseline:** `9da21c4b2325d35710a1ba1acd9be9ca42d988b3`
- **Publication-finishing pack:** B05-PUBLICATION-FINISHING-PACK-001 — complete at RC1 upon owner merge
- **Owner Decision:** B05-PUB-0010
- **Latest Review:** B05-REV-0029
- **Final publication:** not approved

Publication records organize and project controlled content. They do not create Product authority or silently amend Specifications.

## Inventory

| ID | Record | Status |
| --- | --- | --- |
| B05-PUB-0001 | Editorial Style and Terminology | Controlled Editorial Standard v0.2 |
| B05-PUB-0002 | Source and Authority Notes | Controlled Reader Source Notice v1.0 |
| B05-PUB-0003 | Glossary | Controlled Glossary v0.3 |
| B05-PUB-0004 | Subject Index | Controlled Subject Index v0.3 |
| B05-PUB-0005 | Figure Register | Controlled Figure Register v1.0 — 11 retained / 1 merged |
| B05-PUB-0006 | Back Matter and Appendix Map | Controlled Back Matter Map v0.2 |
| B05-PUB-0007 | Cross-Book Reconciliation | Controlled Reconciliation v0.2 |
| B05-PUB-0008 | RC1 Checklist | Controlled Checklist v1.0 — complete upon owner merge |
| B05-PUB-0009 | Term Variation and Editorial Audit | Controlled Audit v0.2 — closed |
| B05-PUB-0010 | Owner RC1 and Publication Decision | RC1 approved upon owner merge; final publication not approved |
| B05-VAL-0001 | Structural and Rendered Validation | Controlled Validation Baseline v1.0 — PASS |

## Exact RC1 Baseline

```text
RC1 content baseline:
9da21c4b2325d35710a1ba1acd9be9ca42d988b3

Validated PF-08 head:
6a210eb40d939eeea6f799c1be7435de7d5dd3aa
```

The PF-09 merge commit is the owner-decision integration event. It does not silently replace the exact RC1 content baseline.

## Back Matter Order

```text
CH47
→ Appendix A–G
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

Production-control records need not appear as reader chapters in every final edition.

## Figure and Rendered Validation

```text
Planned Figure identities: 12
Retained Figure sources: 11
B05-FIG-05: merged into B05-FIG-03
Rendered SVG files: 11
Validation PDF pages: 360
```

All retained Figure sources passed Mermaid parsing, SVG rendering, grayscale scanning, caption, source, accessibility and boundary checks.

## Accepted Validation Evidence

```text
B05-VAL-0001: PASS
B05-REV-0028: ACCEPTED
GitHub Actions run: 29388824396
Checks: 579 / 579 PASS
Warnings: 0
Errors: 0
Artifact ID: 8332449944
Artifact digest:
sha256:f463f4230df2fb9d147a80dcdc0b1638c501636f1ef826b988441295838d95ff
```

Generated outputs:

```text
HTML bytes: 623,202
PDF bytes: 948,073
PDF pages: 360
Selectable-text characters: 475,563
PDF navigation annotations: 135
```

Generated files are validation artifacts. They are not final-publication files and do not authorize public distribution.

## Page-Reference and Change Rule

Chapter, Appendix, Specification, publication and Figure identifiers remain the stable source references.

Final-edition pagination may change without changing controlled identity. A material change to manuscript meaning, Specification, Appendix, Figure, controlled ID, reference journey or authority boundary creates a new candidate baseline and requires renewed validation.

## Authority Order

1. Architecture Canon and accepted Books 01–04;
2. owner-accepted Book 05 structure and Reviews;
3. B05-SPEC-0001–0004 v0.3;
4. RC1 manuscript content baseline;
5. Appendix, publication and Figure projections;
6. rendered/exported outputs.

Rendered convenience never changes controlled meaning.

## Gate Result

```text
PF-01–PF-08: COMPLETE
PF-09: COMPLETE UPON OWNER MERGE
Release Candidate 1: APPROVED UPON OWNER MERGE
Final publication: NOT APPROVED
Public/commercial distribution: NOT APPROVED
Implementation / production / External Protected Action: NOT AUTHORIZED
```

A later final-publication Decision must identify the exact release files and distribution scope.