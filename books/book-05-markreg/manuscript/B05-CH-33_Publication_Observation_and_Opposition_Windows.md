# B05-CH-33 — Publication, Observation and Opposition Windows

**Status:** Part V Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part V — Examination, Publication and Disputes

## Chapter Purpose

A filing may pass examination yet remain exposed to third-party observation, opposition or other publication-stage challenge.

CH33 answers:

> When a right enters publication, how does MarkReg verify the window, explain the exposure, monitor new events and prevent silence from being mistaken for final registration?

```text
Official publication event
→ Publication Window
→ monitoring and third-party event detection
→ no challenge, observation or opposition
→ verified closure or adversarial handoff
```

Publication is a procedural event, not a registration outcome.

---

## 1. User Question and Primary Action

**User question:** Has the application been published, how long is the challenge window, and is any action required now?

**Primary action:** Confirm the monitoring and decision plan, then respond if a sourced third-party event occurs.

The Product should make waiting states understandable rather than display a generic `pending` label.

---

## 2. Publication Window Artifact

A Publication Window is a versioned Product artifact referencing the official publication event.

It should contain:

- affected application, filing unit and jurisdiction;
- official publication identifier and date;
- source and retrieval time;
- window type;
- opening and closing date;
- calculation rule and jurisdiction-pack version;
- time zone and cutoff assumptions;
- monitoring source and frequency;
- responsible owner;
- expected next official event;
- extension or suspension information where applicable;
- detected observations, oppositions or corrections;
- closure evidence and verification status.

```text
Publication Window
≠ guarantee of no challenge
≠ registration
≠ final enforceable scope
```

---

## 3. Window Types

Depending on the jurisdiction and proceeding, the Product may need to represent:

- public observation or comment period;
- opposition period;
- extension period;
- publication for registration;
- publication of an amendment;
- international or regional designation opposition period;
- post-registration challenge window;
- re-publication after correction;
- suspended or restarted window.

The Product should use jurisdiction-specific labels while preserving one controlled window model.

---

## 4. Source and Date Authority

The authoritative window should be based on:

- official publication record;
- official notice;
- authenticated office portal;
- official gazette or bulletin;
- tribunal or procedural direction;
- verified provider evidence when the official source is not yet accessible.

A provider estimate may support planning but should not silently become the official closing date.

If publication is corrected or repeated, the Product must determine whether the window changed and preserve the professional decision.

---

## 5. Monitoring Plan

A monitoring plan should identify:

- official source or connector;
- retrieval cadence;
- expected event types;
- responsible person or service;
- escalation rule;
- evidence retained for each check;
- outage and stale-source handling;
- final closure-verification method.

Monitoring is not only a scheduled search. It is a governed responsibility with evidence that checks occurred.

---

## 6. Observation and Opposition Detection

A detected third-party event should preserve:

- event type and source;
- party identity as reported;
- represented organization and counsel where known;
- affected application and scope;
- grounds or issue summary;
- filing date;
- procedural status;
- deadline and response requirement;
- source Documents;
- verification status;
- conflict-check and provider needs;
- immediate client Communication requirement.

The Product must distinguish:

```text
Possible challenge signal
Filed observation
Filed opposition
Accepted or validated opposition
Unverified party report
Official proceeding opened
```

---

## 7. No-Challenge State

The absence of a detected challenge is not enough to close a window.

Closure should require:

- the sourced closing date has passed;
- applicable extensions or suspensions have been checked;
- monitoring is current;
- no challenge is recorded in the authoritative source;
- any provider or office confirmation required by policy is obtained;
- the next official stage is known or explicitly pending.

The Product may then display `Window closed — no challenge found as of [verified time]`.

It should not display `registered` until an authoritative registration event exists.

---

## 8. Pre-Opposition Contact

A third party may contact the applicant before or during a formal window.

MarkReg should distinguish:

- informal concern;
- demand letter;
- proposed coexistence discussion;
- request for extension;
- notice of intended opposition;
- formal opposition filing.

Informal contact may justify professional review and preservation of Communications. It does not automatically create a formal opposition state.

---

## 9. Extension and Cooling-Off Decisions

Where sourced procedures allow extensions, cooling-off or suspension, the Product should record:

- who may request or consent;
- filing and response deadlines;
- effect on the underlying proceeding;
- fees and provider scope;
- negotiation purpose;
- expiry and restart conditions;
- client and professional authority;
- official acknowledgement.

A negotiation plan does not extend a deadline unless the required procedural effect is verified.

---

## 10. Commercial and Responsibility Effects

Publication-stage work may require:

- monitoring service;
- notice review;
- conflict check;
- opposition defense quote;
- local counsel appointment;
- evidence preservation;
- urgent response preparation;
- settlement or coexistence work;
- executive or brand-owner decision.

The Product should show which work is included, newly quoted, contingent or pending authorization.

The deadline owner and professional owner must be explicit even when the client has not yet accepted full defense scope.

---

## 11. Client Experience

The client view should answer:

- what publication means;
- the verified opening and closing dates;
- whether a challenge has been detected;
- what monitoring is active;
- whether any decision or fee is required;
- what happens if no challenge occurs;
- what happens if an opposition is filed;
- the current source and verification time.

The Product should avoid celebratory registration language before the official registration event.

---

## 12. `EMBERLOOP` European Union Publication

The EU application enters an official publication window.

MarkReg creates Publication Window EU v1 with:

- official publication date and identifier;
- sourced opposition closing date;
- weekly official-source monitoring;
- responsible EU provider and internal professional;
- client explanation that publication is not registration;
- a contingency task for opposition triage.

Before the window closes, the provider reports a third-party contact. MarkReg records it as `informal concern — formal source pending`.

Two days later, the official source shows a filed opposition affecting selected cooking-equipment goods.

The Product creates:

- Official Event Snapshot EU-OPP v1;
- verified opposition source Documents;
- affected-scope mapping;
- response and representation deadlines;
- conflict-check request;
- adversarial Matter-creation request;
- urgent client Communication.

The opposition does not alter the US or UK application states.

---

## 13. `EMBERLOOP` United Kingdom Publication

The UK publication window remains monitored.

No opposition is detected. At the sourced closing date, MarkReg performs a final official-source refresh and records:

```text
Window closed
No challenge found as of verified time
Registration-stage event pending
```

The Product does not yet create a Registration outcome. Part VI begins only when the official registration event is verified.

---

## 14. Conformance Scenarios

### MR-SCN-33A — Informal threat before formal filing

**Given** a third party emails a threat to oppose but no official proceeding exists.  
**When** the client opens the application.  
**Then** MarkReg displays an informal concern, preserves the Communication, requests professional review and keeps the formal opposition state closed.  
**Evidence retained:** original message, sender identity, review decision and later official search.

### MR-SCN-33B — Window correction

**Given** an official correction republishes the application and may restart the window.  
**When** the corrected event is received.  
**Then** MarkReg creates a new Publication Window version, invalidates the prior closing-date assumption and requires deadline verification before any closure status is shown.

### MR-SCN-33C — Monitoring outage near closing date

**Given** the official source is unavailable on the expected closing date.  
**When** the Product attempts final verification.  
**Then** it displays `closure unverified`, preserves the outage evidence, escalates according to policy and does not assume no challenge.

### MR-SCN-33D — Opposition affects selected goods

**Given** a verified opposition is limited to selected goods.  
**When** the adversarial context opens.  
**Then** MarkReg maps the affected scope, preserves unaffected goods and jurisdictions, and prevents the entire portfolio from being labelled opposed.

---

## 15. AI Assistance

AI may:

- summarize publication notices;
- calculate candidate windows from sourced rules;
- compare publication versions;
- detect likely third-party events;
- classify informal and formal Communications;
- prepare client explanations;
- map challenged goods and classes;
- generate monitoring summaries.

AI must not:

- establish a deadline without governed verification;
- declare that no opposition exists from a failed or stale search;
- treat an informal threat as a formal proceeding;
- promise registration after publication;
- authorize an extension or settlement;
- decide adversarial strategy.

---

## 16. Failure Modes to Reject

```text
Publication shown as registration
Provider estimate shown as official closing date
Monitoring task without responsible owner or evidence
No search result treated as verified no opposition
Informal email shown as formal opposition
Corrected publication does not invalidate old deadline
Opposition in one jurisdiction applied to the whole portfolio
Negotiation assumed to suspend the proceeding
```

---

## 17. Minimum Publication Window Lock

```text
Publication is a sourced event,
not a registration outcome.

Every window preserves
opening event, closing rule,
source, retrieval, owner,
monitoring and closure evidence.

Informal concern,
formal observation,
filed opposition and
accepted proceeding remain distinct.

No-challenge status requires
verified closure, not silence.
```

---

## 18. Handoff to Opposition and Adversarial Matters

A verified opposition, observation or comparable challenge produces a sourced event, affected-scope map, deadlines, conflict and provider needs, client Communication and a request for the appropriate formal Matter.

CH34 defines the adversarial Product journey, including positions, pleadings, evidence, settlement, Human Decision, professional responsibility and governed filing.