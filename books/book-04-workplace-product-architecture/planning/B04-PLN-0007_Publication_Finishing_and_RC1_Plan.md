# B04-PLN-0007 — Publication Finishing and RC1 Plan

**Date:** 2026-07-14  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture  
**Chapter Map:** B04-TOC-V0.1  
**Working branch:** `review/book-04-publication-finishing`  
**Status:** Completed — Owner Final Publication Review Pending

## 1. Purpose

Complete the publication-finishing work that remains after the merged CH00–CH39 full-book architecture review and prepare Book 04 Release Candidate 1.

The merge of B04-REV-0003 is treated as owner acceptance of the complete Draft 1 architecture and targeted review revisions. It does not by itself establish final publication readiness.

## 2. Locked Architecture Boundaries

The following remain unchanged:

```text
Core defines shared meaning.
Execution governs coordinated work.
Workplace provides authorized organization context.
Products compose focused user journeys.
MGSN connects independent organizational Orbits.
Owning Services change and record formal business facts.
Humans remain professionally accountable.
AI assists under explicit governance.
```

The chapter map, Book 02 semantics, Book 03 Execution authority, Product boundaries, and protected-action boundaries may not be changed silently during editorial finishing.

## 3. Workstreams

### WS-1 — Native-English and Compression Edit

Review CH00–CH39 in controlled packs for:

- grammatical correctness;
- natural professional English;
- sentence economy;
- repeated explanation that does not add reference value;
- consistent capitalization and hyphenation;
- consistent responsibility verbs;
- consistent distinction language;
- intact professional meaning.

Architecture locks, failure modes, conformance rules, and chapter-boundary summaries may remain intentionally repeated.

### WS-2 — Diagrams and Visual Architecture Assets

Create a canonical figure register and reusable Mermaid-based architecture figures covering:

- the independent Orbit model;
- Workplace boundaries;
- authorized context assembly;
- Prepared Action to governed Execution;
- Product independence and Handoffs;
- Artifact lifecycle;
- formalization and outcome feedback;
- Private First network expansion;
- evidence, selection, Routing, instruction, and acceptance;
- decentralized ecosystem learning.

### WS-3 — Citation and Source Reconciliation

Create a consolidated source and authority note that distinguishes:

- Architecture Canon authority;
- Book 01 operating-system principles;
- frozen Book 02 Core semantics;
- owner-accepted Book 03 Execution authority;
- Book 04 architectural interpretation;
- downstream Product publications;
- illustrative examples that are not legal advice or implementation specifications.

### WS-4 — Glossary Reconciliation

Create a Book 04 glossary that:

- reuses frozen Core and accepted Execution meanings;
- identifies Book 04-specific architectural terms;
- records prohibited conflations;
- points readers to the primary chapters for each term.

### WS-5 — Subject Index

Create a practical subject index organized alphabetically with chapter-level references. The index should prioritize architectural concepts, responsibility boundaries, governance rules, Product profiles, Artifact operations, and network concepts rather than every ordinary word occurrence.

### WS-6 — Cross-Book Final Reconciliation

Create a reconciliation matrix covering:

- Book 01 → Book 04 principle continuity;
- Book 02 → Book 04 semantic consumption;
- Book 03 → Book 04 execution handoff;
- Book 04 → Books 05–07 downstream boundaries;
- explicit findings on whether any upstream amendment is required.

### WS-7 — RC1 Packaging and Validation

Prepare:

- publication assets and navigation;
- updated manifest, status, governance, and `publication.yaml`;
- B04-REV-0004 publication-finishing review;
- structural and editorial validation report;
- Release Candidate 1 status with remaining owner publication gate.

## 4. Editing Packs

```text
Pack A — CH00–CH06
Pack B — CH07–CH12
Pack C — CH13–CH19
Pack D — CH20–CH27
Pack E — CH28–CH32
Pack F — CH33–CH39
```

Each pack must preserve chapter titles, section numbering, fenced-code balance, and cross-chapter progression.

## 5. Required Publication Assets

Create under `books/book-04-workplace-product-architecture/publication/`:

- `B04-PUB-0001_Editorial_Style_and_Terminology.md`
- `B04-PUB-0002_Source_and_Authority_Notes.md`
- `B04-PUB-0003_Glossary.md`
- `B04-PUB-0004_Subject_Index.md`
- `B04-PUB-0005_Figure_Register.md`
- `B04-PUB-0006_Cross-Book_Reconciliation.md`
- `B04-PUB-0007_RC1_Checklist.md`

Create reusable figures under `books/book-04-workplace-product-architecture/figures/`.

## 6. Validation Gates

Before RC1:

1. CH00–CH39 remain exactly forty files.
2. Every first heading matches B04-TOC-V0.1.
3. Numbered sections remain sequential where used.
4. Markdown fences remain balanced.
5. Canonical responsibility language remains intact.
6. No Book 02 or Book 03 amendment is implied.
7. No external protected action is authorized.
8. All publication assets exist and are linked from Book 04 navigation.
9. Glossary and index references point to existing chapters.
10. Final publication readiness remains subject to the owner publication gate.

## 7. Expected Final State

```text
Book 04 Release Candidate 1
→ architecture accepted
→ publication finishing completed
→ RC validation passed
→ owner final publication review pending
```

No pull request may be merged without explicit owner instruction.

## 8. Completion Record

All seven workstreams and RC1 validation gates are complete. See `reviews/B04-REV-0004_Publication_Finishing_and_RC1_Review.md`. The remaining gate is owner final publication approval and merge.
