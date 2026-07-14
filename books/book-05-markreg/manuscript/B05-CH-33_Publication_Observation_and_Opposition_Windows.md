# B05-CH-33 — Publication, Observation and Opposition Windows

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part V — Examination, Publication and Disputes

## Chapter Purpose

Publication may open a third-party challenge period even after examination has progressed.

CH33 answers:

> Has publication been verified, which challenge window is open, who monitors it, and what evidence is required before the Product may show either opposition or no-challenge closure?

```text
MR-E05 publication event
→ MR-C04 Publication Window Context
→ MR-E06 Deadline Record
→ monitoring
→ verified challenge or verified no-challenge closure
```

Publication is not registration.

## 1. User Question and Primary Action

**User question:** Is the application published, when does the window close and is any action required?

**Primary action:** Confirm monitoring responsibility and respond only to a sourced third-party event.

Waiting must be explained with dates, sources and next verification, not hidden behind `pending`.

## 2. Publication Window Context

`MR-C04 Publication Window Context` records:

- application, filing unit and jurisdiction;
- official publication identifier and date;
- source and retrieval time;
- window type and applicable Rule version;
- opening, closing, time zone and cutoff;
- extensions, suspensions, republication or restart conditions;
- monitoring source, cadence and owner;
- detected challenge signals and verification state;
- closure evidence and next official stage.

```text
Publication Window
≠ guarantee of no challenge
≠ registration
≠ final enforceable scope
```

## 3. Source and Deadline Authority

The window derives from the official publication record, notice, gazette, authenticated portal or tribunal direction.

Provider advice may support planning but does not silently become the official closing date.

For `MR-SCN-26`, republication or correction creates a new Context version and re-evaluates the prior closing date.

For `MR-SCN-27`, conflicting deadline advice remains visible until professionally resolved.

## 4. Monitoring Responsibility

A monitoring plan identifies:

- official source or connector;
- cadence and expected event types;
- responsible owner and backup;
- evidence retained for each check;
- outage and stale-source handling;
- escalation rule;
- final closure verification.

A scheduled search without an accountable owner and retained evidence is not governed monitoring.

## 5. Challenge States

The Product distinguishes:

```text
possible challenge signal
informal concern or threat
filed observation
filed opposition
verified or accepted proceeding
official proceeding event
```

Informal contact may require Review, preservation and deadline analysis. It does not create a formal opposition state.

A verified challenge must map the affected goods, services, classes and jurisdictions without changing unrelated scope.

## 6. No-Challenge Closure

No-challenge closure requires:

1. the sourced closing date has passed;
2. extensions, suspensions and corrections have been checked;
3. monitoring is current;
4. no challenge appears in the authoritative source;
5. the final check and checked time are retained;
6. the next official stage is known or explicitly pending.

The correct Product projection is:

```text
Window closed — no challenge found as of [verified time]
Registration event pending
```

Silence or a failed search is not closure.

## 7. Extension, Cooling-Off and Negotiation

Where sourced procedures allow extension, cooling-off or suspension, preserve:

- requesting and consenting authority;
- filing and response deadlines;
- procedural effect and official evidence;
- fees and provider scope;
- negotiation purpose;
- expiry and restart conditions.

Negotiation does not extend or suspend a deadline unless the procedural effect is verified.

## 8. Commercial and Participant Effects

Publication-stage work may create monitoring, opposition triage, conflict, local counsel, Evidence and settlement scope beyond the initial Quote.

The Product must show included, newly quoted, contingent and unauthorized work separately.

The client sees the verified window, challenge state, decision need and next event. Professionals and providers see only the scope required for their assigned work.

## 9. `EMBERLOOP` — `EL-26`

### European Union

The official source verifies publication and later a filed opposition affecting selected cooking-equipment goods.

MarkReg creates or updates:

- Publication Window EU;
- Official Event Snapshot EU-OPP;
- affected-scope map;
- response and representation deadlines;
- conflict and provider checks;
- request for an adversarial Matter;
- urgent client Communication.

The opposition does not change the US or UK states.

### United Kingdom

At the sourced closing date, a final official-source refresh finds no challenge.

```text
Window closed
No challenge found as of verified time
Registration-stage event pending
```

Part VI may open only after a separate official registration event is verified.

## 10. Controlled Scenarios

- `MR-SCN-10` — stale official status;
- `MR-SCN-26` — corrected or republished event;
- `MR-SCN-27` — conflicting deadline advice;
- `MR-SCN-28` — silence does not authorize action;
- `MR-SCN-33` — one challenged right does not change unrelated rights.

## 11. AI Assistance

AI may summarize publication records, calculate candidate windows from sourced Rules, compare versions, classify informal and formal Communications and map challenged scope.

AI may not establish the deadline alone, declare no opposition from a stale or failed search, treat an informal threat as a proceeding, promise registration, or authorize extension, settlement or adversarial strategy.

## 12. Chapter Lock

```text
Publication is a sourced event,
not a registration outcome.

Every window preserves
source, opening, closing Rule,
owner, monitoring and closure evidence.

Informal concern and
formal proceeding remain distinct.

No-challenge status requires
verified closure, not silence.
```

## 13. Handoff to CH34

A verified EU opposition produces an Official Event Snapshot, affected-scope map, deadlines, provider and conflict needs, client Communication and an adversarial Matter request.

CH34 governs the resulting Adversarial Context, Evidence, pleadings, settlement authority and procedural outcomes.