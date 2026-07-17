# PORTFOLIO-PLN-0005 — Seven PDF Review Editions

## Input baseline

```text
PORTFOLIO-RC-01
Visual system: PORTFOLIO-VISUAL-0001
Rendering specification: PORTFOLIO-RENDER-0001
Profile: pdf-review
```

## Build sequence

```text
rebuild candidates
→ assemble front matter and manuscript
→ normalize render-local asset paths
→ convert Markdown to semantic HTML
→ apply locked 6 x 9 CSS
→ render searchable PDF
→ inspect PDF structure and text
→ rasterize every page at low resolution
→ flag low-content pages
→ render first / middle / last page previews
→ bind output hashes
```

## Preflight gates

- exactly seven PDF files;
- every PDF opens without repair;
- every page is 6 x 9 inches within tolerance;
- every PDF has extractable text;
- no unexpected empty pages;
- candidate release gate remains `NOT GRANTED`;
- no font binary is committed;
- no frozen manuscript or freeze manifest changes.

## Review boundary

The output is a review artifact. Cover refinement, typography substitution, pagination correction and final print production remain possible after review. No output from this task is authorized for public or commercial distribution.
