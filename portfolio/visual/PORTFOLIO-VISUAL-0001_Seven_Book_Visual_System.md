# PORTFOLIO-VISUAL-0001 — Seven-Book Visual System

## Design intent

The MarkOrbit series should read as one governed knowledge system rather than seven unrelated books. The visual language is restrained, technical and editorial: strong hierarchy, generous whitespace, clear diagrams and minimal decoration.

## Series architecture

Every cover and title page uses four stable elements:

1. `MARKORBIT` series signature;
2. two-digit book number;
3. canonical book title;
4. one book-specific identifier token.

The seven identifiers are semantic labels, not mandatory colors:

| Book | Identifier | Role |
| --- | --- | --- |
| Book 01 | OS | system thesis |
| Book 02 | CORE | normative specification |
| Book 03 | EXEC | execution model |
| Book 04 | WORK | workplace and product architecture |
| Book 05 | REG | registry product |
| Book 06 | LITE | lightweight product |
| Book 07 | NET | service network |

Color may distinguish books, but no meaning may depend on color alone. Every identifier must remain visible in monochrome output.

## Cover system

- portrait master ratio aligned to the selected print trim;
- series signature at the top;
- book number and identifier form the primary navigation device;
- title occupies the main field;
- no decorative image is required;
- optional diagrams must come from controlled repository assets and have recorded rights provenance;
- spine repeats book number, short title and series signature;
- back cover reserves areas for summary, author/publisher metadata and ISBN barcode only after owner decisions are resolved.

## Typography roles

Font binaries are not stored in the repository. Rendering environments must resolve fonts from an approved, licensed font map.

- Display: modern sans serif, medium or semibold.
- Body: highly legible serif or humanist sans serif.
- Interface labels and captions: sans serif.
- Code and identifiers: monospaced.
- CJK fallback: licensed family with complete Simplified Chinese punctuation and glyph coverage.

Fallback order must be explicit in the render profile. Missing fonts are a build failure, not a silent substitution.

## Page architecture

- Base print trim: 6 × 9 in.
- Mirrored margins; inner margin greater than outer margin.
- Body measure target: 55–75 Latin characters per line.
- Baseline rhythm must remain consistent across headings, body, tables and captions.
- Chapters begin on recto pages in print output.
- Running heads show short book title on verso and chapter title on recto.
- Front matter uses lower-case Roman pagination; body uses Arabic pagination.

## Hierarchy

- H1: chapter title, page break before.
- H2: primary section.
- H3: secondary section.
- H4 and deeper: use sparingly; convert excessive depth into labeled blocks where possible.
- Architecture identifiers, equations and governed terms retain source spelling.

## Content components

### Figures

- sequential per book using existing controlled identifiers where available;
- caption below figure;
- source/provenance note required when externally sourced;
- minimum effective raster resolution: 300 ppi for print;
- vector preferred for diagrams;
- alt text required for EPUB.

### Tables

- repeat header rows across pages;
- avoid vertical rules unless structurally necessary;
- never reduce body text below the minimum print size to force fit;
- wide tables may rotate or become landscape inserts only through the render profile.

### Code and structured text

- preserve whitespace and identifiers;
- line numbers disabled by default;
- long lines wrap only when semantics remain intact;
- code blocks may split across pages only at safe boundaries.

### Callouts

Allowed types:

```text
Definition
Decision
Constraint
Example
Warning
Owner Decision Required
```

Each type uses a text label and border treatment; color is supplementary.

## Accessibility

- logical heading order;
- sufficient text/background contrast;
- meaningful link text;
- alt text for informative images;
- decorative images marked accordingly;
- EPUB reading order follows source order;
- tables retain header semantics.

## Rights and provenance

No image, illustration or font enters a release candidate without a recorded source, license or ownership basis. Unresolved rights block publication rendering approval.

## Authority boundary

This specification authorizes visual and rendering preparation only. It does not authorize publication, ISBN procurement, distribution, implementation, deployment or modification of frozen prose.
