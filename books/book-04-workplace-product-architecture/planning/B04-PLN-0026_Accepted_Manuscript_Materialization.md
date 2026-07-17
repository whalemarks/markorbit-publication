# B04-PLN-0026 — Accepted Manuscript Materialization

## Purpose

Convert the accepted Candidate 04 build from an ephemeral Actions artifact into a repository-controlled Book 04 vNext manuscript directory.

## Source of truth

```text
B04-vNEXT-CANDIDATE-04
Owner Acceptance: ACCEPT
Accepted chapters: CH00–CH39
```

## Materialized layout

```text
accepted-vnext/
  CANDIDATE-INDEX.md
  SOURCE-MANIFEST.md
  ROUTE-REPORT.md
  TRANSFORM-REPORT.md
  BUILD-REPORT.md
  MATERIALIZATION-MANIFEST.md
  manuscript/CH00.md … CH39.md
```

## Method

- generate Candidate 04 from accepted repository inputs;
- copy only generated accepted files;
- compute SHA-256 for every copied file;
- compare every materialized file with a fresh deterministic build;
- reject any unapproved content difference;
- preserve RC1 and all architecture authorities unchanged.

## Gate

Materialization may establish freeze readiness. It does not itself freeze or authorize publication or distribution.
