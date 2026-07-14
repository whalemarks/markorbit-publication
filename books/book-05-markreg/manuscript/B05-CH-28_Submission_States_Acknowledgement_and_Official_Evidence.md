# B05-CH-28 — Submission States, Acknowledgement and Official Evidence

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH27 defined permitted Execution routes and actors.

CH28 classifies what happened after an attempt and which source proves the current state:

```text
EL-21 / CH28
MR-A17 Execution Request
→ MR-E01 Submission Evidence
→ MR-E02 Delivery Evidence
→ MR-E03 Provider Report
→ MR-E04 Official Acknowledgement Evidence or unknown state
→ sourced Product projection
```

Submission is not official acknowledgement. Acknowledgement is not registration.

## 1. Product Question and Primary Action

**Product question:** Was the filing officially received, and what evidence proves the current state?

**Primary action:** Review returned evidence or resolve an unknown, rejected or correction-required result.

A generic `Filed` label is insufficient when the evidence proves only transmission or provider reporting.

## 2. State Model

Use distinct states such as:

```text
Prepared
Approved
Queued
Execution started
Sent
Delivery confirmed
Provider received
Provider accepted
Provider reports submitted
Office response pending
Officially acknowledged
Rejected before acknowledgement
Correction required
Cancelled before submission
Unknown
Reconciled
```

One attempt may have several simultaneous dimensions: package, Execution, provider, payment, transmission, office and Product projection.

## 3. Evidence Classes

### `MR-E01 Submission Evidence`

Proves which payload or package was sent, when, through which route and under which attempt identity. It does not prove official receipt.

### `MR-E02 Delivery Evidence`

Proves technical delivery or transmission. It does not prove Provider Acceptance or official effect.

### `MR-E03 Provider Report`

Records provider-reported receipt, acceptance, filing or result with time, scope and attachments. Evidence strength must be classified.

### `MR-E04 Official Acknowledgement Evidence`

Records official receipt, filing number, acceptance, rejection or another recognized procedural acknowledgement from an official source or verified official artifact.

## 4. State Boundaries

```text
Prepared ≠ Approved
Approved ≠ Queued
Queued ≠ Execution started
Execution started ≠ Sent
Sent ≠ Delivery confirmed
Delivery confirmed ≠ Provider Acceptance
Provider reports submitted ≠ Officially acknowledged
Officially acknowledged ≠ Registered
```

Every state transition retains source, actor, time, package version, attempt identity and evidence.

## 5. Official Acknowledgement Contract

Where available, `MR-E04` records:

- office and jurisdiction;
- application, filing or receipt identifier;
- official filing date and time;
- applicant and filing unit;
- classes or scope;
- fee receipt or acceptance state;
- acknowledgement type;
- official source or Document;
- receipt or retrieval time;
- language and verification status;
- relationship to the submitted package.

A provider’s internal reference must not be displayed as the official application number.

## 6. Filing Date and Fee Evidence

The official filing date may differ from transmission time, remain provisional, depend on requirements or payment, or later be corrected.

Do not infer it solely from a send timestamp.

Payment states also remain separate:

```text
Payment initiated
Funds debited
Provider funded
Office fee paid
Office fee accepted
Payment rejected
Refund pending
Payment unknown
```

Funds leaving an account do not prove official fee acceptance.

## 7. Rejection, Correction and Unknown

A pre-acknowledgement rejection records source, affected package, retry safety and whether an external effect may already exist.

An immediate correction request identifies affected content, deadline, package-version impact, required Review or confirmation and whether the original filing date may be preserved.

`Unknown` is required when a timeout, missing provider response, unresolved payment, delayed official database, unverifiable identifier or duplicate risk prevents a reliable conclusion.

Unknown triggers reconciliation, not optimistic completion.

## 8. Client-Facing Projection

A user surface may simplify states to:

```text
Preparing filing
Approved for filing
Submission in progress
Sent — awaiting official receipt
Provider reports submitted — official evidence pending
Officially filed — receipt verified
Correction required
Submission issue under review
```

Opening the projection should expose source and checked time.

## 9. `EMBERLOOP` — `EL-21`

- The US provider returns a verified official receipt and application number.
- The UK manual route returns an official portal receipt linked to the approved package.
- The EU connector reports technical success, but no official acknowledgement is initially available.

US and UK may be shown as officially acknowledged. EU remains `Sent — awaiting official receipt` until reconciliation recovers or verifies official evidence.

## 10. Controlled Scenarios

### `MR-SCN-21` — Provider receipt without acceptance

Delivery or receipt is shown separately and does not permit provider Execution until `MR-D05 Provider Acceptance` exists.

### `MR-SCN-23` — Technical success without official receipt

Technical or provider success without `MR-E04` opens reconciliation, blocks an official-filing claim and prevents blind retry.

## 11. AI Assistance

AI may extract identifiers and dates, compare acknowledgement content with the package, classify responses, translate notices and identify missing evidence.

AI may not invent identifiers, infer official filing dates without evidence, treat delivery as acknowledgement or mark an unknown attempt complete.

## 12. Chapter Lock

```text
Every state has a source and evidence class.
Provider Report ≠ Official Truth.
Sent or technical success ≠ official acknowledgement.
Official acknowledgement ≠ registration.
Unknown is a valid state requiring reconciliation.
```

## 13. Handoff to CH29

CH28 preserves submission and acknowledgement states.

CH29 opens `MR-C02 Reconciliation Context` and `MR-A18 Recovery and Reconciliation Plan` for unknown, partial, rejected or conflicting results.
