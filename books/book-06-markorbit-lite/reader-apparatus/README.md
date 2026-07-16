# Book 06 Reader Apparatus

## Identity

```text
Book: Book 06 — MarkOrbit Lite
Record set: B06-APP-0001–B06-APP-0007
Status: Candidate — accepted on RC Hardening B owner merge
Purpose: reader navigation, controlled-term explanation, semantic figures and coverage indexes
Creates Product authority: NO
Creates implementation authority: NO
Changes B06-TOC-V0.1: NO
```

## Authority boundary

The Reader Apparatus is an editorial projection of the accepted Book 06 Product Charter, Product Baseline, Chapter Map and manuscript.

```text
Product Charter and Owner Decisions
→ B06-SPEC-0001–0004
→ B06-TOC-V0.1 and B06-CH-00–B06-CH-33
→ B06-APP reader aids
```

Where an appendix, glossary entry, index term or figure appears to conflict with a Specification, the Specification controls.

The `B06-APP-*` identifiers are publication identifiers. They are not new `ML-*` Product records, database tables, APIs, services, policies or implementation commitments.

## Reader apparatus set

1. [B06-APP-0001 — Controlled Term Glossary](B06-APP-0001_Controlled_Term_Glossary.md)
2. [B06-APP-0002 — Core Distinction Matrix](B06-APP-0002_Core_Distinction_Matrix.md)
3. [B06-APP-0003 — Abbreviations and Controlled ID Guide](B06-APP-0003_Abbreviations_and_Controlled_ID_Guide.md)
4. [B06-APP-0004 — Figure Register and Semantic Diagrams](B06-APP-0004_Figure_Register_and_Semantic_Diagrams.md)
5. [B06-APP-0005 — Controlled Record Coverage](B06-APP-0005_Controlled_Record_Coverage.md)
6. [B06-APP-0006 — Journey, Scenario, Handoff and Acceptance Coverage](B06-APP-0006_Journey_Scenario_Handoff_and_Acceptance_Coverage.md)
7. [B06-APP-0007 — Subject Index](B06-APP-0007_Subject_Index.md)

## Suggested reading order

### First-time reader

```text
CH00 Preface
→ CH01 Table of Contents
→ APP-0001 Glossary
→ APP-0002 Distinction Matrix
→ CH02–CH06 Product Constitution
→ selected Product loop
→ APP-0004 Figures
```

### Product and architecture review

```text
CH03–CH06
→ CH07–CH11
→ APP-0002 Distinction Matrix
→ APP-0004 Figures 01–04 and 08–12
→ APP-0005 Controlled Record Coverage
→ B06-SPEC-0001–0004
```

### Implementation preparation

```text
CH08–CH11
→ CH17–CH31
→ APP-0003 Controlled ID Guide
→ APP-0005 Record Coverage
→ APP-0006 Journey / Scenario / Contract / Acceptance Coverage
→ Specifications
```

This route helps identify accepted meanings and observable behavior. It does not authorize implementation.

### Editorial and publication review

```text
CH00–CH33
→ APP-0001 terminology
→ APP-0002 distinctions
→ APP-0004 figures
→ APP-0007 subject index
→ RC Hardening C source and rendered validation
```

## Stable reference convention

Reader-apparatus anchors use stable prefixes:

```text
b06-term-*          glossary terms
b06-distinction-*   distinction entries
b06-figure-*        semantic figures
b06-index-*         subject-index sections
```

Editorial anchors improve navigation but do not create controlled Product IDs.

## Figure convention

The figures are semantic diagrams written in Mermaid so GitHub can render them directly.

They intentionally avoid:

- database schemas;
- API endpoints;
- deployment topology;
- provider selection;
- model selection;
- infrastructure commitments;
- automatic authority transfer.

Rendered-output and cross-format validation remains part of RC Hardening C.

## Publication boundary

The Reader Apparatus does not authorize:

- Release Candidate status;
- implementation specifications or ADR acceptance;
- production deployment;
- public or commercial distribution;
- autonomous professional action;
- External Protected Action.
