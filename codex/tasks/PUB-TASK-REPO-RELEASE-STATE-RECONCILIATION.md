# PUB-TASK-REPO-RELEASE-STATE-RECONCILIATION

## Status

```text
AUTHORIZED
EXECUTION IN PROGRESS ON TASK BRANCH
```

## Purpose

Reconcile repository publication state after completion and permanent freeze of Book 06 and Book 07 Release Candidate 1 baselines.

The task repairs governance metadata and release pointers only. It does not modify any frozen reader-facing chapter, Reader Apparatus, Product Specification, Chapter Map, Product Charter or Architecture Canon content.

## Authoritative release identities

```text
Book 05 RC1 release pointer:
release/book-05-rc1

Book 06 RC1 content baseline:
7ce03755e03bb4876768a34a4ee3d2c3b74bddb1
Book 06 freeze activation commit:
4fce03cb7380117417b1ad479c743ef31a65b6c6
Book 06 release pointer:
release/book-06-rc1

Book 07 RC1 content baseline:
7ab3ea3e01b42afda8b2f675e514b91df436e47d
Book 07 Owner Decision activation commit:
2f59951ceacfde3ed379e6de5dad602a192f48e3
Book 07 freeze activation commit:
3d3469a5845c352a2d73f698ffc085d5abb3aa85
Book 07 release pointer:
release/book-07-rc1
```

## Required work

1. Create the missing Book 06 and Book 07 release branches from the exact freeze activation commits.
2. Replace conditional and pre-merge Book 07 state with accepted-and-frozen state.
3. Reconcile repository README, book registry and Publication Manifest with actual Book 01–07 status.
4. Correct stale Book 01–03 gate descriptions without modifying manuscripts.
5. Add a repository-level release-state validator and pull-request workflow.
6. Record the next controlled publication gate as the Book 04 Workplace Sovereignty vNext correction.

## Acceptance criteria

```text
AC-01 release/book-06-rc1 resolves to 4fce03cb7380117417b1ad479c743ef31a65b6c6
AC-02 release/book-07-rc1 resolves to 3d3469a5845c352a2d73f698ffc085d5abb3aa85
AC-03 Book 07 machine state is release_candidate_1_frozen
AC-04 Book 07 freeze activation commit contains no placeholder
AC-05 root and books registries report Book 06 and Book 07 as approved and frozen
AC-06 Publication Manifest reports the current portfolio gate accurately
AC-07 no frozen reader-facing inputs are changed
AC-08 automated release-state validation passes
```

## Scope boundary

Not authorized:

- Book 01–07 manuscript changes;
- Book 02 semantic changes;
- Architecture Canon or Decision Register changes;
- Product Specification or Chapter Map changes;
- database, API, payment, routing, Trust-runtime or production implementation;
- public/commercial distribution;
- autonomous professional action;
- External Protected Action.

## Next gate

After this task is merged and release-state validation passes:

```text
MO-ARCH-PLN-001
→ Book 04 Workplace Sovereignty vNext Correction
→ WP-A Canon and terminology reconciliation
```
