# PORTFOLIO-PLN-0004 — Seven-Book Release Candidates

## Build model

Each candidate is generated under `.artifacts/portfolio-release-candidates-01/book-XX/` with:

```text
00-SERIES-PAGE.md
01-MARKORBIT-PROJECT.md
02-BOOK-FRONT-MATTER.md
manuscript/
publication/ (when present)
figures/ (when present)
CANDIDATE-MANIFEST.md
```

## Source mapping

- Book 01: `books/book-01-operating-system/manuscript/`
- Book 02: `books/book-02-core-specification/manuscript/`
- Book 03: `books/book-03-execution-system/manuscript/`
- Book 04: `books/book-04-workplace-product-architecture/accepted-vnext/manuscript/`
- Book 05: `books/book-05-markreg/manuscript/`
- Book 06: `books/book-06-markorbit-lite/manuscript/`
- Book 07: `books/book-07-mark-global-service-network/manuscript/`

Existing `publication/` and `figures/` directories are copied as candidate support assets when present.

## Overlay discipline

Only operations declared in `PORTFOLIO-OVERLAY-0001` may change generated manuscript bytes. Expected total: 18 corrections.

## Release gate

Legal and commercial fields marked `OWNER DECISION REQUIRED` remain visible. Candidate generation may proceed, but release authorization remains blocked.
