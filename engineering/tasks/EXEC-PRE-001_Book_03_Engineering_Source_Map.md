# EXEC-PRE-001 — Book 03 Engineering Source Map and Repository Readiness

## Purpose

Convert the frozen Book 03 RC1 publication baseline into a controlled engineering source map before the dedicated Execution implementation repository is initialized.

## Authority

- `books/book-03-execution-system/README.md`
- `books/book-03-execution-system/FREEZE-MANIFEST.md`
- `books/book-03-execution-system/manuscript/B03-CH-00_Preface.md` through `B03-CH-34_Codex_Execution_Roadmap.md`
- Book 02 implementation evidence in `whalemarks/markorbit-core`, completed through CORE-TASK-060

## Required outputs

1. A chapter-to-engineering-asset source map covering CH00–CH34.
2. A machine-readable registry of the eight MVP workflows and their execution depths.
3. A locked authority and repository-boundary decision.
4. A deterministic validator and GitHub Actions workflow.
5. A next-task decision consistent with Book 03 CH34.

## Locked conclusions

- Book 03 is the normative source for Execution coordination and governance.
- Book 02 remains authoritative for Core meaning, owning Services and formal mutations.
- Execution implementation must live in a dedicated repository boundary.
- `markorbit-core`, Product repositories, Integration repositories and the publication repository must not absorb Execution runtime behavior.
- Depth A contains Intake Execution, Application Preparation and Communication Review.
- Depth B contains Provider Routing Preparation, Office Action Response Preparation, Renewal Preparation, Assignment Preparation and Evidence Review Preparation.
- Depth C external protected actions remain deferred.
- The next formal task is `EXEC-TASK-001 — Initialize Execution Repository`.

## Exclusions

This task does not:

- modify frozen Book 03 manuscript or publication files;
- create runtime code;
- create a Workflow Engine;
- create Product UI;
- add a database, queue, worker or connector;
- enable external Communication send, filing, payment, provider engagement or autonomous professional execution;
- redefine Book 02 contracts.

## Acceptance

- all 35 chapter identifiers are mapped exactly once;
- all eight MVP workflow identifiers are registered exactly once;
- execution depths are `depth-a` or `depth-b` only for the eight workflows;
- deferred protected actions are explicit;
- the repository boundary is dedicated and excludes Core, Product, Integration and publication repositories;
- the next formal task is exactly `EXEC-TASK-001`;
- frozen Book 03 files are unchanged;
- validation passes.