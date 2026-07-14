# Publication Governance

## Repository Ownership

This repository owns publication governance for MarkOrbit publications. It defines repository-level structure, shared publication standards, review organization, release organization, and Codex task boundaries.

## Book Ownership

Each book owns its manuscript, book-specific specifications, book-specific editorial files, and book-specific release notes.

## Codex Boundaries

Codex does not define MarkOrbit architecture.

Codex may only implement explicit repository tasks that are provided by a human operator. Codex work must preserve existing book content unless a task explicitly authorizes content changes.

## Architecture Change Control

Architecture changes require human approval. Repository maintenance, publication scaffolding, and placeholder files must not introduce architectural decisions.

## Portfolio Baseline Governance

A Portfolio Baseline review may reconcile titles, wording, publication status and cross-book boundaries.

It must classify each finding as:

- PASS;
- EDITORIAL CORRECTION;
- CHANGE PROPOSAL REQUIRED.

A Portfolio Baseline review may not silently modify frozen Book 02 semantics.

After a Portfolio Baseline is locked, downstream books must record upstream findings rather than directly rewriting accepted upstream architecture.

## Owner Acceptance Effect

Merge of the Portfolio Baseline pull request establishes the candidate baseline as the active Books 01–04 publication baseline.

It does not authorize implementation, deployment or external protected action.

