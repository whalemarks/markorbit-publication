# PORTFOLIO-PLN-0004 — Common Series Front Matter

## Purpose

Close the portfolio-wide front-matter gap identified by `PORTFOLIO-AUD-0001` without modifying any frozen manuscript.

## Package model

```text
common series page
+ common project introduction
+ book-specific title / edition / legal metadata object
= render-ready front-matter input
```

## Controlled assets

- `portfolio/front-matter/SERIES-PAGE.md`
- `portfolio/front-matter/MARKORBIT-PROJECT.md`
- `portfolio/front-matter/books/BOOK-01.md` through `BOOK-07.md`
- `portfolio/front-matter/release-metadata.json`
- `portfolio/decisions/PORTFOLIO-DEC-0002_Front_Matter_Owner_Decisions.md`

## Rules

1. Frozen prose remains unchanged.
2. Front matter is an overlay consumed by later rendering tasks.
3. Unknown legal or commercial facts remain explicitly unresolved.
4. No ISBN is requested or assigned in this task.
5. No publication or distribution authorization is implied.

## Exit criteria

Seven book objects and all shared assets validate; unresolved fields remain visible and cannot silently enter a release build.
