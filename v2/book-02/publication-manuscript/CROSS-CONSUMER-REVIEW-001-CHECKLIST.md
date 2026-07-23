# CROSS-CONSUMER-REVIEW-001 — Field, Lifecycle and Ownership Checklist

## Purpose

Compare fixture-level results from Execution, MarkReg and Lite before any profile advances toward a formal Book 02 Change Proposal.

## Required consumers

```text
whalemarks/markorbit-execution
MarkReg consumer proof
Lite consumer proof
```

At least two consumers must reach reproducible L2 fixture proof. Publication examples alone do not satisfy the gate.

## Evidence intake

For each consumer, record:

- repository and commit or PR;
- fixture version;
- validator version;
- profiles consumed;
- positive and negative fixture counts;
- state-separation tests;
- shared fields used;
- local extension fields;
- rejected fields;
- ownership assumptions;
- unresolved gaps.

## Field comparison

For every profile field classify:

```text
Used identically by all consumers
Used identically by two consumers
Semantically similar but different
Consumer-local
Book 03 runtime-only
External-authority reference
Unused
Conflicting
```

A field is a shared-contract candidate only when its name, meaning, requiredness, authority and version behavior are stable across consumers.

## Lifecycle comparison

Compare whether consumers require the same states and transitions.

### Production Authorization

Prefer frozen Permission status and Policy decisions. Flag any consumer requesting a separate lifecycle.

### Work Package

Determine whether package identity survives Task replacement and whether package-level acceptance is genuinely shared.

### Bilateral Assignment

Compare:

```text
Offered
Accepted
Declined
Expired
Active
Suspended
Revoked
Completed
Cancelled
Replaced
```

Record which transitions are necessary, who owns them and which evidence is required.

### Contribution

Compare submission, correction, withdrawal and supersession behavior.

### Outcome

Compare acceptance purpose, expiry, correction and formalization references without allowing formal-state collapse.

## Ownership review

For each record answer:

1. Which service creates it?
2. Which service may change its state?
3. Which service may reject or correct it?
4. Which service owns referenced artifacts?
5. Which actor supplies acceptance evidence?
6. Which record is authoritative for formal state?
7. Which fields are projections rather than owned content?
8. What survives cancellation or revocation?

## Authority review

Reject any model where:

- Permission creates professional qualification;
- Assignment creates professional authority;
- Human Review completion creates Apply authority;
- Outcome mutates formal state;
- Provider listing creates appointment;
- public data creates consent or customer relationship;
- AI model capability creates execution authority.

## Product-locality test

A field should remain Product-local when it primarily expresses:

- UI or presentation;
- pricing, margin or commission;
- ranking;
- channel or campaign behavior;
- country-specific filing package detail;
- Product workflow convenience;
- local analytics;
- implementation technology.

## F0–F4 decision per concept

```text
F0 — frozen contract already covers it
F1 — safe composition
F2 — shared profile or specialization
F3 — new shared addition candidate
F4 — frozen semantic change
```

The review must document rejected lower classes before recommending F3 or F4.

## Compatibility gate

For any recommended shared contract, document:

- identifier and version;
- backward and forward compatibility;
- frozen consumer impact;
- migration requirement;
- public export impact;
- fixture changes;
- rollback behavior;
- deprecation plan.

## Decision outcomes

The review may conclude:

```text
RETAIN_AS_PROFILE
RETAIN_PRODUCT_LOCAL
RETAIN_BOOK_03_RUNTIME
ADVANCE_TO_PRE_PROPOSAL
ADVANCE_TO_FORMAL_CHANGE_PROPOSAL
REJECT
MORE_EVIDENCE_REQUIRED
```

## Minimum acceptance threshold

A concept may advance only when:

- two independent L2 consumers exist;
- shared fields and lifecycle are stable;
- ownership is explicit;
- authority boundaries pass negative tests;
- F0–F2 alternatives are insufficient;
- compatibility impact is documented;
- no frozen semantic is silently renamed;
- legal/professional review is available where required.

## Required output

Produce a table for each profile:

| Dimension | Execution | MarkReg | Lite | Shared conclusion |
|---|---|---|---|---|
| identity |  |  |  |  |
| required fields |  |  |  |  |
| lifecycle |  |  |  |  |
| owner |  |  |  |  |
| authority |  |  |  |  |
| correction |  |  |  |  |
| versioning |  |  |  |  |
| local extensions |  |  |  |  |
| decision |  |  |  |  |

## Constitutional lock

```text
Cross-consumer repetition
≠ automatic Core admission.

Shared meaning must be proven,
not inferred from repeated nouns.
```
