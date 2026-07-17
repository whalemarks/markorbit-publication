# PORTFOLIO-RENDER-0001 — Rendering Specification

## Inputs

The only manuscript input is `PORTFOLIO-RC-01`, regenerated deterministically from the seven frozen baselines, shared front matter and `PORTFOLIO-OVERLAY-0001`.

## Build stages

```text
regenerate PORTFOLIO-RC-01
→ verify candidate manifests
→ resolve approved fonts and rights records
→ assemble format-specific source
→ render
→ run structural and visual preflight
→ bind outputs with SHA-256
→ create review package
```

## PDF review profile

- PDF 1.7 or later;
- embedded fonts required;
- selectable text required;
- tagged headings, links and alt text where supported;
- bookmarks generated from H1–H3;
- internal links preserved;
- page size follows 6 × 9 in trim for book PDFs;
- no crop marks in screen-review PDFs;
- deterministic metadata excludes volatile build timestamps where possible.

## Print profile

- trim: 6 × 9 in;
- bleed: 0.125 in only for elements intended to reach the edge;
- CMYK conversion belongs to the final print-provider profile, not the source manuscript;
- all fonts embedded;
- effective raster resolution at least 300 ppi;
- rich black and total ink limits remain provider-specific owner decisions;
- cover spine width cannot be finalized before page count, paper and binding are selected;
- barcode area remains reserved until ISBN and publisher decisions are resolved.

## EPUB profile

- EPUB 3;
- reflowable layout by default;
- semantic landmarks and navigation document required;
- CSS must not depend on proprietary fonts;
- alt text required for informative figures;
- tables must remain usable on narrow screens;
- page-number references are excluded until a stable print pagination map exists;
- MathML or accessible text representation required for equations.

## Source ordering

For every book:

```text
00-SERIES-PAGE.md
01-MARKORBIT-PROJECT.md
02-BOOK-FRONT-MATTER.md
manuscript in controlled order
publication apparatus in declared order
```

Figures remain linked assets unless the renderer requires controlled embedding.

## Determinism

The build must record:

- source commit SHA;
- release-candidate artifact digest;
- render-profile version;
- renderer and dependency versions;
- resolved font family names and license-record identifiers;
- output SHA-256;
- preflight result.

A build that silently substitutes fonts, loses links, changes heading order or omits a controlled source file fails.

## Preflight gates

```text
candidate manifest verification: PASS
font resolution: PASS
image rights/provenance: PASS
broken internal links: 0
missing figures: 0
heading-order blockers: 0
unresolved overflow: 0
output manifest coverage: 100%
owner legal metadata unresolved: BLOCK RELEASE, NOT REVIEW RENDER
```

## Output naming

```text
markorbit-book-01-review.pdf
markorbit-book-01.epub
markorbit-book-01-print.pdf
...
markorbit-book-07-review.pdf
```

Versioned release names are assigned only after Owner Acceptance and release authorization.

## Authority boundary

Rendering outputs are review artifacts until a separate release decision authorizes publication and distribution.
