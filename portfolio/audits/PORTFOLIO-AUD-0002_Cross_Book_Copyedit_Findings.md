# PORTFOLIO-AUD-0002 — Cross-Book Publication Copyedit Findings

## Summary

```text
Books scanned: 7 / 7
Controlled Markdown files scanned: 267
Findings recorded: 18
Safe normalization findings: 1
Broken local-link findings: 17
Ambiguous semantic findings: 0
Frozen manuscript modifications: 0
Semantic changes applied: 0
```

## Book coverage

| Book | Files scanned | Findings |
| --- | ---: | ---: |
| Book 01 | 23 | 1 |
| Book 02 | 32 | 0 |
| Book 03 | 43 | 0 |
| Book 04 | 40 | 17 |
| Book 05 | 60 | 0 |
| Book 06 | 35 | 0 |
| Book 07 | 34 | 0 |

## Finding 1 — Book number normalization

- Source: `books/book-01-operating-system/manuscript/13_Appendix_C.md`
- Line: 23
- Found: `Book 1`
- Publication form: `Book 01`
- Classification: `SAFE_NORMALIZATION`

## Findings 2–18 — Book 04 relative links

The frozen Book 04 vNext manuscript is located under:

```text
accepted-vnext/manuscript/
```

Links inherited from the historical RC1 manuscript still assume that the manuscript directory is directly below the book root. In a rendered release candidate, these links require one additional parent traversal.

### Publication apparatus links

In `CH01.md`, normalize:

```text
../publication/...  →  ../../publication/...
```

Affected objects:

- B04-PUB-0001 Editorial Style and Terminology
- B04-PUB-0002 Source and Authority Notes
- B04-PUB-0003 Glossary
- B04-PUB-0004 Subject Index
- B04-PUB-0005 Figure Register
- B04-PUB-0006 Cross-Book Reconciliation
- B04-PUB-0007 RC1 Checklist

### Figure links

Normalize:

```text
../figures/...  →  ../../figures/...
```

Affected chapters and figures:

- CH03 — B04-FIG-01
- CH04 — B04-FIG-02
- CH13 — B04-FIG-03
- CH18 — B04-FIG-04
- CH27 — B04-FIG-05
- CH30 — B04-FIG-06
- CH32 — B04-FIG-07
- CH33 — B04-FIG-08
- CH34 — B04-FIG-09
- CH36 — B04-FIG-10

## Classification decision

All 18 findings are unambiguous publication-layer corrections. They do not change architecture meaning, authority, lifecycle order or requirements.

```text
Safe for publication overlay: 18 / 18
CHANGE PROPOSAL REQUIRED: 0 / 18
Direct frozen-source modification: NOT PERMITTED
```
