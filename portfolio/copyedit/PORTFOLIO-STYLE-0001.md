# PORTFOLIO-STYLE-0001 — MarkOrbit Publication Style Sheet

## Canonical series titles

1. **MarkOrbit — The Operating System for Global Brand Services**
2. **MarkOrbit Core Specification**
3. **MarkOrbit Execution System**
4. **MarkOrbit Workplace and Product Architecture**
5. **MarkReg**
6. **MarkOrbit Lite**
7. **Mark Global Service Network**

Use `Book 01` through `Book 07` when a numbered series reference is required. Do not use historical six-book numbering in active publication material.

## Canonical architecture terms

Capitalize these terms when they name defined architecture entities or governed concepts:

- Organization
- Workplace
- Product
- Product Installation
- Product Projection
- Owning Service
- Human Review
- External Protected Action
- Capability
- Skill
- Assistant
- Artifact
- Document
- Delivery
- Publish
- Evidence
- Provider
- Customer

Lowercase ordinary-language uses when they do not refer to the defined architecture concept.

## Protected distinctions

Publication editing must preserve these distinctions:

```text
Organization ≠ Workplace
Product ≠ Product Installation ≠ Product Projection
AI recommendation ≠ Human Review ≠ formal-state mutation
Delivery ≠ Publish ≠ official acceptance
Routing ≠ selection ≠ appointment
collaboration ≠ authority transfer
Workplace portability ≠ platform-network portability
```

## Typography and punctuation

- Use an em dash with surrounding spaces for title subtitles: `MarkOrbit — ...`.
- Use en dashes for closed numeric or chapter ranges: `CH00–CH34`, `Books 01–07`.
- Use serial commas in English prose when they improve clarity.
- Preserve code, equations, identifiers and quoted source language exactly.
- Do not replace architecture operators such as `≠`, `→` or `←` with prose.
- Remove trailing whitespace during rendering.
- Normalize repeated blank lines to a maximum of two outside code blocks.

## References

- Prefer `Book 04, Chapter 20` or a stable repository identifier when chapter numbering is controlled.
- Do not create page-number references before final pagination.
- A reference to a renamed or moved chapter must be corrected in the publication overlay and recorded in the findings ledger.
- A reference whose correction changes meaning is not a copyedit.

## Semantic-change gate

```text
CHANGE PROPOSAL REQUIRED
```

Use this classification whenever a proposed correction would change a definition, responsibility, authority boundary, lifecycle order, requirement or interpretation.

## Overlay boundary

The following are safe publication-overlay operations:

- title capitalization;
- punctuation and spacing;
- known book-title normalization;
- stable chapter-label normalization;
- link-target correction where the target is unambiguous;
- removal of accidental duplicate spaces or blank lines.

The following are not safe overlay operations:

- changing definitions;
- changing responsibility or authority;
- changing lifecycle order;
- adding or removing substantive requirements;
- resolving an ambiguous cross-book conflict.
