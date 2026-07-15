# Book 05 Publication Apparatus

## Status

- **Book state:** Complete Draft 1 — PF-08 complete
- **Current stage:** PF-09 — Owner RC1 and Publication Decision
- **Current pack:** B05-PUBLICATION-FINISHING-PACK-001
- **Latest completed Review:** B05-REV-0028

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
| B05-PUB-0008 | RC1 Checklist | Controlled Checklist v0.4 — PF-08 complete / PF-09 open |
| B05-PUB-0009 | Term Variation and Editorial Audit | Controlled Audit v0.2 — closed |
| B05-VAL-0001 | Structural and Rendered Validation | Controlled Validation Baseline v1.0 — PASS |

## Back Matter Order

```text
CH47
→ Appendix A–G
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

The validation edition contains this complete reader sequence. Production-control records need not appear as reader chapters in every final edition.

## Figure and Rendered Validation

```text
Planned Figure identities: 12
Retained Figure sources: 11
B05-FIG-05: merged into B05-FIG-03
Rendered SVG files: 11
Validation PDF pages: 360
```

All retained Figure sources passed Mermaid parsing, SVG rendering, grayscale scanning, caption, source, accessibility and boundary checks.

## PF-08 Evidence

```text
B05-VAL-0001: PASS
B05-REV-0028: ACCEPTED
GitHub Actions run: 29388230449
Checks: 573 / 573 PASS
Warnings: 0
Errors: 0
Artifact digest: sha256:2a582f53a95bc50a2d9159ff6f8cf3a11e3811ccfc4bd96ed42adbd29e980e00
```

Generated outputs:

```text
HTML bytes: 623,202
PDF bytes: 948,073
PDF pages: 360
Selectable-text characters: 475,563
PDF navigation annotations: 135
```

Generated files are validation artifacts. They are not RC1 or final-publication files.

## Page-Reference Rule

Chapter, Appendix, Specification, publication and Figure identifiers remain the stable source references.

The validation edition confirms navigation and stable identifiers. Final edition pagination may still change during PF-09 publication packaging without changing controlled identity.

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
PF-01–PF-08: COMPLETE
PF-09 owner RC1 Decision: AUTHORIZED AND NEXT
Release Candidate 1: NOT YET AUTHORIZED
Final publication: NOT AUTHORIZED
Implementation / production / External Protected Action: NOT AUTHORIZED
```

PF-09 must record the exact baseline commit and the owner release Decision.
