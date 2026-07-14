# B05-CH-39 — Renewal Preparation and Governed Renewal

**Status:** Part VI Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — Registration and Portfolio Continuity

## Chapter Purpose

Renewal is a protected lifecycle action. It requires right identification, owner verification, scope confirmation, deadline control, fee transparency, authority, provider or connector readiness, approval, filing evidence and official acknowledgement.

The central progression is:

```text
Renewal Obligation
→ Renewal Intake
→ Renewal Package Candidate
→ Professional Review
→ Client Confirmation
→ Renewal Approval
→ Governed Filing
→ Official Acknowledgement
→ Updated Right Baseline
```

```text
Calendar Reminder
≠ Renewal Instruction
≠ Renewal Approval
≠ Renewal Filing
≠ Renewed Right
```

---

## 1. User Question and Primary Action

**User question:** Which rights should be renewed, under whose name, for which scope, at what cost, and before which verified deadline?

**Primary action:** Confirm the renewal scope and owner, resolve blockers, approve the exact Renewal Package Candidate and authorize governed filing.

---

## 2. Renewal Starts from a Verified Right

The Product should verify:

- office and jurisdiction;
- registration number;
- registered owner;
- current status;
- registered classes and scope;
- ordinary renewal date;
- opening date;
- grace period and surcharge;
- active proceedings;
- pending recordals;
- representative requirement;
- official fee source;
- provider requirement.

A copied spreadsheet row is not sufficient authority for renewal.

---

## 3. Renewal Intake Is Narrow but Material

Renewal Intake should ask only what is necessary to determine:

- whether the right should be renewed;
- whether all or selected classes remain commercially relevant;
- whether the owner or address changed;
- whether any assignment, merger or name change is pending;
- whether local representation continues;
- whether use or declaration requirements apply;
- who may instruct and approve;
- who will pay;
- whether late filing or restoration is involved.

Prior data may be reused, but material facts must be reconfirmed.

---

## 4. Renewal Package Candidate

The package should preserve:

- right identity and official source;
- registered owner and address;
- renewal scope by class;
- proposed limitation or deletion;
- required declarations;
- required evidence and Documents;
- representative and provider;
- ordinary and late deadlines;
- official, professional and provider fees;
- currency, tax and validity;
- payment condition;
- unresolved recordal or dispute;
- source versions;
- package version;
- approval requirements.

---

## 5. Full and Partial Renewal

Where permitted, a client may renew:

- all classes;
- selected classes;
- a limited scope;
- selected related rights.

The Product should show:

- what will continue;
- what will lapse or be removed;
- irreversible consequences;
- cost differences;
- portfolio gaps;
- related rights that remain unaffected.

A package selection must not hide independent right and class consequences.

---

## 6. Owner Verification and Pending Recordal

Possible states include:

```text
Official owner confirmed
Name change pending
Address change pending
Assignment signed but not recorded
Merger evidence available
Ownership disputed
Instructor differs from owner
```

The Product should rely on jurisdiction rules and professional review to determine whether renewal may proceed:

- under the current official owner;
- together with a recordal;
- after recordal;
- with explanatory evidence;
- through restoration or special procedure.

It should not assume one universal sequence.

---

## 7. Renewal Fees and Commercial Control

The price model should separate:

- official renewal fee;
- per-class or per-right fee;
- late surcharge;
- professional fee;
- provider fee;
- recordal fee;
- evidence or declaration work;
- translation, notarization or legalization;
- tax and bank charge;
- contingency.

A provider quote excluding late fees or recordal work must not be presented as a complete renewal total.

---

## 8. Renewal Approval

Renewal Approval should identify:

- exact package version;
- right and jurisdiction;
- owner basis;
- classes and scope;
- ordinary or late route;
- fees and currency;
- payment condition;
- provider or connector route;
- decision-maker and authority;
- approval time;
- expiry or invalidation conditions.

A scope or owner change after approval may require a new package and approval.

---

## 9. Filing and Acknowledgement

Renewal filing reuses Part IV controls:

```text
Approved Renewal Package
→ Governed Execution Request
→ Sent or Provider Accepted
→ Official Acknowledgement
→ Updated Official Record
```

The Product should distinguish:

- provider says filed;
- office delivery confirmed;
- renewal accepted;
- deficiency issued;
- renewal recorded;
- certificate or extract updated;
- unknown status.

---

## 10. Renewal Failure and Recovery

Failure may arise from:

- wrong right or owner;
- missed ordinary deadline;
- payment failure;
- class mismatch;
- recordal dependency;
- provider non-response;
- office rejection;
- duplicate filing;
- acknowledgement absence.

Retry and restoration decisions should preserve idempotency, prior effects, fee movement, deadline state and renewed approval.

---

## 11. Updated Right Baseline

After sourced renewal acknowledgement, the Product creates a new Right Baseline version containing:

- renewed term or next date;
- renewed scope;
- owner and representative state;
- official evidence;
- fees and filing references;
- unresolved obligations;
- next maintenance actions.

The old baseline remains auditable.

---

## 12. Reference Journey — RIVERKITE

Six registrations approach renewal.

The Product produces six independent Renewal Package Candidates:

- four ordinary renewals under confirmed owners;
- one renewal with a pending assignment;
- one right under cancellation challenge.

For the pending assignment jurisdiction, the jurisdiction pack and local professional conclude that renewal may be filed under the current official owner while the assignment recordal proceeds in parallel. The Product therefore creates:

```text
Renewal Package Candidate v2
+ Linked Assignment Recordal Context
+ Explicit Owner Basis
```

The cancellation challenge remains visible but does not automatically block renewal. Client approval covers five renewals; the sixth is held pending budget decision.

---

## 13. Reference Journey — EMBERLOOP

The UK registration is not yet within the renewal window. MarkReg does not create a filing package prematurely.

It retains:

- verified future renewal date;
- evidence-collection recommendation;
- owner and representative state;
- calendar responsibility.

The Product shows `Not Yet Open`, not `Ready to Renew`.

---

## 14. Conformance Scenarios

### Scenario A — Client selects only some classes

**Given** a multi-class registration  
**When** the client elects partial renewal  
**Then** the package shows continuing and lapsing scope and requires version-specific approval.

### Scenario B — Assignment signed but unrecorded

**Given** a signed assignment and a different official owner  
**When** renewal preparation begins  
**Then** the Product creates a recordal dependency and follows the jurisdiction-specific professional decision rather than assuming the assignee may file.

### Scenario C — Provider quote excludes late surcharge

**Given** the ordinary deadline has passed  
**When** the provider quote contains only ordinary fees  
**Then** the Product blocks final quote and approval until late-fee treatment is resolved.

### Scenario D — Provider reports filing without official evidence

**Given** a provider states renewal was filed  
**When** no official acknowledgement is available  
**Then** the Product shows provider-reported filing and continues reconciliation.

---

## 15. AI Assistance Boundary

AI may:

- assemble renewal candidates;
- compare owner and scope;
- calculate candidate fees and dates;
- identify recordal dependencies;
- prepare package diffs;
- summarize choices.

AI may not:

- decide ownership;
- select rights to abandon;
- authorize partial renewal;
- waive late fees;
- approve filing;
- declare renewal effective without sourced acknowledgement.

---

## 16. Minimum Renewal Lock

```text
Renewal is a protected action.

Right identity, owner, scope,
deadline, fees, authority,
approval, filing and acknowledgement
remain explicit and versioned.

A pending recordal or dispute
is evaluated by jurisdiction and right,
not by a universal shortcut.
```

---

## 17. Handoff to Changes and Recordals

The output is an approved or completed Renewal Package with an updated Right Baseline.

CH40 defines how name, address, representative, limitation, correction and other official-record changes are prepared and governed.