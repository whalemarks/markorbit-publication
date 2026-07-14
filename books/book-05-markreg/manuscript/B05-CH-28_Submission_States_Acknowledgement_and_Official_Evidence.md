# B05-CH-28 — Submission States, Acknowledgement and Official Evidence

**Status:** Part IV Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH27 defines the permitted execution routes and authority boundaries.

CH28 answers:

> What happened after the protected action was attempted, which source proves it, and when may MarkReg present a filing as officially acknowledged?

```text
Approved execution attempt
→ technical or provider response
→ official acknowledgement or unresolved state
→ sourced Product projection
```

Submission is not official acknowledgement. Acknowledgement is not registration.

---

## 1. User Question and Primary Action

**User question:** Was the application actually received by the office, and what evidence proves the current state?

**Primary action:** Review the returned evidence or resolve an unknown, rejected or correction-required state.

A generic `Filed` label is insufficient when the evidence only proves that data was sent.

---

## 2. Submission-State Model

The minimum state model includes:

```text
Prepared
Approved
Queued
Execution started
Sent
Delivery confirmed
Provider received
Provider accepted
Office response pending
Officially acknowledged
Rejected before acknowledgement
Correction required
Cancelled before submission
Unknown
Reconciled
```

The Product may display a simplified client label, but it must preserve the underlying state and source.

---

## 3. State Dimensions

One filing attempt may have several simultaneous dimensions:

| Dimension | Example |
| --- | --- |
| package | approved v6 |
| execution | connector completed |
| provider | accepted instruction |
| payment | official funds debited, acceptance unknown |
| transmission | sent |
| office | no acknowledgement yet |
| Product projection | awaiting official receipt |

Collapsing these into one status creates false certainty.

---

## 4. Prepared and Approved

`Prepared` means the Filing Package Candidate exists.

`Approved` means Filing Approval covers that exact version.

Neither state proves that a protected action started.

---

## 5. Queued and Execution Started

`Queued` means governed Execution accepted the request for processing.

`Execution started` means the selected actor or connector began the protected action.

These states should preserve:

- execution reference;
- actor or service;
- start time;
- route;
- package version;
- idempotency key.

---

## 6. Sent and Delivery Confirmed

`Sent` means the payload, files or instruction left the controlled sender.

`Delivery confirmed` means a technical or communication layer confirms delivery to the destination endpoint or provider.

Neither proves that the office accepted the application.

---

## 7. Provider Received and Provider Accepted

For a provider route:

- provider received means the provider confirms receipt;
- provider accepted means it accepted the instruction scope;
- provider submitted means it reports performing the filing action;
- official acknowledgement still requires office evidence or verified provider-returned evidence.

The Product should not treat a provider’s earlier acceptance as later filing evidence.

---

## 8. Official Acknowledgement

An official acknowledgement should preserve, where available:

- office and jurisdiction;
- application or receipt number;
- filing date and time;
- applicant;
- mark or filing unit reference;
- classes or scope;
- fee receipt or status;
- acknowledgement type;
- official source or document;
- retrieval or receipt time;
- source language;
- verification status;
- relationship to the submitted package.

The official record remains authoritative.

---

## 9. Evidence Hierarchy

A Product may receive:

1. direct official electronic response;
2. official receipt or certificate document;
3. official database record;
4. verified provider-returned official evidence;
5. provider statement without attached official evidence;
6. technical delivery receipt;
7. internal user statement.

The Product should identify the evidence level rather than present every source as equivalent.

---

## 10. Official Identifier

An application number, filing number or receipt identifier should record:

- identifier type;
- issuing authority;
- exact value;
- jurisdiction;
- related package and Matter;
- source evidence;
- issue or retrieval time;
- correction or supersession history.

A provider’s internal reference must not be displayed as the official application number.

---

## 11. Filing Date

The filing date may be:

- granted immediately;
- provisional pending requirements;
- different from transmission time;
- corrected by the office;
- unavailable until acknowledgement;
- affected by time zone, office calendar or payment.

MarkReg must not infer the official filing date solely from the send timestamp.

---

## 12. Fee Evidence

The Product should distinguish:

```text
Payment initiated
Funds debited
Provider funded
Office fee paid
Office fee accepted
Payment rejected
Refund pending
Payment status unknown
```

An amount leaving a bank account does not prove official fee acceptance.

---

## 13. Rejection Before Acknowledgement

A pre-acknowledgement rejection may result from:

- invalid payload;
- unsupported file;
- authentication failure;
- fee failure;
- provider refusal;
- missing required field;
- office validation error;
- duplicate detection;
- expired session;
- unavailable service.

The rejection record must identify source, affected package, retry safety and whether any official effect may already exist.

---

## 14. Correction Required

A response may require correction without fully rejecting the filing.

The Product should identify:

- correction source;
- deadline;
- affected content;
- whether a new package version is required;
- whether professional Review or client confirmation is required;
- whether the original filing date may be preserved;
- who may send the correction.

CH30 and later chapters govern substantive post-filing examination. CH28 covers immediate submission and acknowledgement corrections.

---

## 15. Unknown State

`Unknown` is required when:

- transmission result is ambiguous;
- timeout occurs after send;
- provider response is missing;
- payment was debited but receipt absent;
- official search has not yet updated;
- returned identifier cannot be verified;
- duplicate risk prevents immediate retry.

Unknown must trigger reconciliation, not optimistic completion.

---

## 16. Product Projection

The client-facing Product may display:

```text
Preparing filing
Approved for filing
Submission in progress
Sent — awaiting official receipt
Officially filed — receipt verified
Correction required
Submission issue under review
```

Every projection should expose source and checked time when opened.

---

## 17. Event and Evidence Linkage

Each state transition should link:

- prior state;
- triggering Event;
- actor or service;
- timestamp;
- package version;
- result;
- evidence;
- interpretation status;
- next action;
- supersession or reconciliation.

The Product projection is derived from this trace.

---

## 18. `EMBERLOOP` Reference Journey

For `EMBERLOOP`:

- the US provider returns an official USPTO receipt and application number;
- the EU connector returns technical success but the acknowledgement is delayed, so the Product shows `Sent — awaiting official receipt`;
- the UK manual filing returns a portal receipt that is reviewed and linked to the approved package.

Only the US and UK applications may initially be shown as officially acknowledged. The EU filing remains unresolved until evidence arrives or reconciliation confirms the result.

---

## 19. Conformance Scenario — Provider Says Filed Without Receipt

**Given** the provider emails `filed successfully` but supplies no official receipt or application number.  
**When** MarkReg evaluates the returned evidence.  
**Then** it records the provider statement, shows `provider reports submitted — official evidence pending`, requests the expected evidence, and prevents the statement from becoming verified official acknowledgement.  
**Authority boundary:** provider reporting is evidence, but the office controls official receipt.  
**Evidence retained:** message, instruction reference, requested evidence, later official receipt or reconciliation outcome.

---

## 20. AI Assistance

AI may:

- extract identifiers and dates from returned documents;
- compare acknowledgement content with the package;
- classify technical and office responses;
- identify missing evidence;
- translate and summarize notices;
- propose next-state explanations.

AI may not invent an identifier, infer official filing date without evidence, treat delivery as acknowledgement, decide substantive legal effect, or mark an unresolved attempt complete.

---

## 21. Minimum Chapter Lock

```text
Prepared is not approved.
Approved is not queued.
Queued is not sent.
Sent is not delivered.
Delivered is not officially acknowledged.
Acknowledged is not registered.

Every state preserves source,
time, actor, package version and evidence.

Unknown is a valid state and requires
reconciliation before retry or completion.
```

---

## 22. Handoff to CH29

CH28 defines observable submission and acknowledgement states.

CH29 defines idempotency, duplicate prevention, partial failure, safe retry, reconciliation, client and provider Communication, Event trace and audit continuity.