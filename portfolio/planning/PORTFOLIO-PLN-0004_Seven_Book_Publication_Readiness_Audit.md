# PORTFOLIO-PLN-0004 — Seven-Book Publication Readiness Audit

## Purpose

Establish the actual publication readiness of all seven frozen books before any front-matter, copyediting, rendering or release work begins.

## Audit dimensions

1. **Front matter** — title page, series page, copyright page, edition/version statement, author/project note, preface/introduction and table of contents.
2. **Publication apparatus** — glossary, index, figures/tables register, appendices, source notes and bibliography/reference handling.
3. **Cross-book consistency** — titles, book numbers, terminology, active cross-references and frozen-baseline identifiers.
4. **Visual production** — cover brief, series identity, typography, diagram treatment and image licensing status.
5. **Rendering readiness** — deterministic source order, PDF/EPUB/print configuration, link validation, page-break controls and output checks.
6. **Release governance** — copyright owner, edition metadata, ISBN decision, distribution channels, release authorization and archival package.

## Rating model

- `READY`: sufficiently complete for the next production stage;
- `PARTIAL`: useful material exists but requires normalization or completion;
- `MISSING`: no reliable publication asset was found;
- `DECISION`: an Owner/publisher decision is required rather than editorial completion.

## Execution sequence

```text
inventory frozen sources
→ detect publication assets
→ assess six dimensions per book
→ classify portfolio-wide blockers
→ define common work before book-specific work
→ authorize the next bounded task only
```

## Expected decision

The audit is diagnostic. It must not edit frozen content or prematurely declare the seven books release-ready. Its expected output is a prioritized closeout sequence, beginning with common front matter and publication metadata unless the evidence shows a more fundamental blocker.
