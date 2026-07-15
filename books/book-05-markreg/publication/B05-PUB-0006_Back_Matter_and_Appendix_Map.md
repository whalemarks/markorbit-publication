# B05-PUB-0006 — Back Matter and Appendix Map

## Status

- **Status:** Controlled Back Matter Map v0.2 — PF-07 reconciled
- **Decision:** Book 05 uses reader-facing Appendix A–G and independent publication apparatus
- **Authority:** B05-REV-0013, B05-REV-0026 and B05-PLN-0004
- **Applies to:** repository, reader PDF, print and implementation-oriented editions
- **Rendered order validation:** pending PF-08

## 1. Reader Architecture

Book 05 must not end at CH47 without compact reader-reference and source material.

The controlled reader order is:

```text
Front Matter
→ CH00–CH47
→ Appendix A–G
→ Source and Authority Notes
→ Glossary
→ Subject Index
→ Figure Register
```

Editorial Style, Term Audit, Cross-Book Reconciliation, publication planning, Reviews and the RC1 Checklist are production controls. A repository or implementation-oriented edition may include them, but a general reader edition need not render them as chapters.

## 2. Asset Classes

```text
Specification = controlled Product truth
Appendix = reader-facing reference projection
Figure = controlled visual projection
Publication apparatus = source, editorial, navigation and release control
Rendered edition = presentation of the controlled baseline
```

No later projection may silently change an earlier authority.

## 3. Reader-Facing Appendix Inventory

| Appendix | Reader purpose | Controlling source | PF-07 state |
| --- | --- | --- | --- |
| A — Full-Lifecycle Artifact and Decision Map | identify records, Decisions, lineages and formalization boundaries | B05-SPEC-0001 v0.3 | content reconciled; FIG-02/03 available |
| B — Lifecycle State and Authority Matrix | distinguish Product, formal, Approval, Execution, provider, official and projection states | CH07, B05-SPEC-0001/0003 v0.3 | content reconciled; FIG-04 available |
| C — Participant Visibility and Action Rights Matrix | understand participant visibility, contribution and prohibited assumptions | CH44 and B05-SPEC-0003 v0.3 | content reconciled; FIG-09 available |
| D — Reference Journeys | follow EMBERLOOP and RIVERKITE without rereading every chapter | B05-SPEC-0002 v0.3 | content reconciled; FIG-12 available |
| E — Priority Conformance Scenarios | test constitutional, lifecycle, participant and publication boundaries | B05-SPEC-0003 v0.3 | content reconciled |
| F — Minimum Jurisdiction Pack Checklist | determine whether a jurisdiction/service/stage is sourced and supportable | B05-SPEC-0004 v0.3 | content reconciled; FIG-10 available |
| G — MarkReg Conformance Profiles | state supported Product depth honestly | CH46–CH47 and B05-SPEC-0003/0004 v0.3 | content reconciled; FIG-11 available |

Appendix A–G remain reader projections. They do not create Rules, authority, official truth or implementation permission.

## 4. Publication Apparatus Inventory

| Record | Purpose | Current state |
| --- | --- | --- |
| B05-PUB-0001 | Editorial Style and Terminology | Controlled Editorial Standard v0.2 |
| B05-PUB-0002 | Source and Authority Notes and Reader Notice | Controlled Reader Source Notice v1.0 — PF-07 complete |
| B05-PUB-0003 | Glossary | Controlled Glossary v0.3; stable layout references available |
| B05-PUB-0004 | Subject Index | Controlled Index v0.3; stable layout references available |
| B05-PUB-0005 | Figure Register | Controlled Figure Register v1.0; 11 retained and 1 merged |
| B05-PUB-0006 | Back Matter and Appendix Map | Controlled Back Matter Map v0.2 |
| B05-PUB-0007 | Cross-Book Reconciliation | Controlled Reconciliation v0.2 |
| B05-PUB-0008 | RC1 Checklist | Controlled Checklist v0.2; PF-08/PF-09 open |
| B05-PUB-0009 | Term Variation and Editorial Audit | Controlled Audit v0.2 — closed |

## 5. Controlled Figure Inventory

```text
B05-FIG-01–04: retained
B05-FIG-05: merged into B05-FIG-03
B05-FIG-06–12: retained

retained source files: 11
separate rendered assets: pending PF-08
```

The figure directory contains the source, caption, placement intent, accessibility description, grayscale notes and authority boundary for every retained figure.

## 6. Repository Structure

```text
books/book-05-markreg/
├── manuscript/
│   └── B05-CH-00 ... B05-CH-47
├── specifications/
│   └── B05-SPEC-0001 ... B05-SPEC-0004
├── appendices/
│   └── B05-APP-A ... B05-APP-G
├── figures/
│   ├── README.md
│   └── eleven retained B05-FIG source files
├── publication/
│   └── B05-PUB-0001 ... B05-PUB-0009
├── planning/
└── reviews/
```

## 7. Source-of-Truth Matrix

| Reader asset | Controlled source of truth | May simplify | May create new Rule or authority |
| --- | --- | --- | --- |
| Appendix A | B05-SPEC-0001 | yes | no |
| Appendix B | B05-SPEC-0001/0003 and reviewed chapters | yes | no |
| Appendix C | B05-SPEC-0003 and CH44 | yes | no |
| Appendix D | B05-SPEC-0002 | yes | no |
| Appendix E | B05-SPEC-0003 | yes | no |
| Appendix F | B05-SPEC-0004 | yes | no |
| Appendix G | CH46–CH47 and B05-SPEC-0003/0004 | yes | no |
| Glossary | Book 02 terms plus reviewed Book 05 usage | yes | no |
| Subject Index | final manuscript, Appendices and Figures | navigation only | no |
| Figures | cited chapters, Specifications and Appendices | visual layout only | no |
| rendered page number | stable source identifier and final pagination | presentation only | no |

## 8. Page-Reference Input Contract

The stable page-reference inputs are:

- chapter identifiers and headings;
- Appendix identifiers and headings;
- Specification identifiers;
- controlled terms in B05-PUB-0003;
- Subject Index entries in B05-PUB-0004;
- B05-FIG identifiers and placement intent;
- reader Back Matter order.

PF-08 may add rendered page numbers, anchors, bookmarks, footnotes or endnotes after pagination stabilizes.

```text
stable identifier
→ rendered page or anchor

rendered page number
≠ controlled identity
```

A later repagination changes the rendered reference, not the underlying controlled source.

## 9. Edition Rule

A reader PDF or print edition should normally include:

- Appendix A–G;
- Source and Authority Notes and final Reader Notice;
- Glossary;
- Subject Index;
- retained figures and captions;
- a Figure Register or figure list.

An implementation-oriented edition may additionally include:

- controlled Specifications;
- Cross-Book Reconciliation;
- Conformance and RC1 checklists;
- extended source and Review traceability.

All editions must preserve the same Product and authority meaning.

## 10. Version and Change Control

Every Appendix, Figure and publication record should retain:

- stable ID;
- status and version;
- source baseline;
- latest reconciliation Review;
- known gaps;
- supersession or merge disposition;
- reader-edition inclusion status.

When a Specification changes materially:

1. identify affected Appendices, terms, Index entries and Figures;
2. mark them for revalidation;
3. preserve the prior publication baseline;
4. issue a reviewed update rather than silently altering a released edition.

Changing Appendix A–G inventory or reader order requires a recorded editorial reason and impact review. Moving a figure during layout does not change its controlled meaning.

## 11. PF-07 Completion State

```text
Appendix A–G inventory and reader order: COMPLETE
Source and Authority Notes: COMPLETE
Final Reader Notice: COMPLETE
Glossary and Subject Index stable page-reference inputs: COMPLETE
Twelve figure dispositions: COMPLETE
Eleven retained controlled figure sources: COMPLETE
Figure captions and accessibility text: COMPLETE
Source-level grayscale and legibility review: COMPLETE
Rendered order, page fit, links and pagination: OPEN — PF-08
```

## 12. Authority Boundary

This map does not:

- make Book 05 RC1;
- authorize final publication;
- validate rendered Mermaid or PDF output;
- authorize implementation, production deployment or External Protected Action.

It completes the PF-07 source and publication-apparatus baseline for later validation.