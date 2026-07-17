# B04-DEC-0002 — Candidate 01 Review Decision

## Decision

```text
REVISE — generate Candidate 02 before Owner Acceptance.
```

## Basis

Candidate 01 passes structural generation, provenance and architecture-regression checks, but fails the editorial acceptance standard because chapter-number routing does not always correspond to the accepted RC1 chapter purpose and because internal editorial/control text can become reader-visible.

## What is accepted

- deterministic discovery of RC1 CH00–CH39;
- complete provenance-bearing generation;
- immutable RC1 protection;
- use of Owner-Accepted vNext authority controls;
- Candidate 01 as a diagnostic full-book review object;
- the bounded Candidate 02 repair scope in `B04-AUD-0002`.

## What is not accepted

- Candidate 01 as final Book 04 vNext prose;
- number-only editorial routing;
- generic insertion placement;
- reader-visible editorial instructions or validation result blocks;
- Owner Acceptance, freeze, publication or implementation authority.

## Candidate 02 authorization

Owner merge of this decision authorizes:

```text
PUB-TASK-B04-VNEXT-CANDIDATE-02
Route-Aware Editorial Regeneration
```

Candidate 02 must use an explicit route manifest rather than assuming editorial module number equals RC1 chapter identity.

## Architecture disposition

```text
Reopen WP-A–WP-F: NO
Immediate Book 02 Change Proposal: NO
Architecture Canon conflict: NO
Editorial regeneration required: YES
```

## Gate effect

This decision closes Candidate Review 01. It does not grant Book 04 vNext Owner Acceptance or any publication, implementation, deployment or External Protected Action authority.