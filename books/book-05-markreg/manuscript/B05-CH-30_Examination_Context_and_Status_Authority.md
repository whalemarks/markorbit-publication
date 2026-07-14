# B05-CH-30 — Examination Context and Status Authority

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part V — Examination, Publication and Disputes

## Chapter Purpose

Part V begins only when a sourced event changes the procedural context of an application, registration or proceeding.

CH30 answers:

> What happened, according to which source, when was it verified, which right and scope are affected, and which professional context must now open?

```text
sourced event
→ MR-E05 Official Event Snapshot
→ scoped professional Context
→ MR-E06 deadline candidates
→ issue or monitoring work
```

A Product status is a projection. It is not Official Truth.

## 1. User Question and Primary Action

**User question:** What is the latest verified event, what does it affect and what must happen next?

**Primary action:** Review the sourced event and route it to the required professional owner.

The surface must show source, retrieval time, affected right, event type, deadline status, uncertainty and next action.

## 2. Official Event Snapshot

`MR-E05 Official Event Snapshot` preserves what the source reports before professional interpretation changes its meaning.

Minimum fields include:

- jurisdiction, office and official identifier;
- affected application, registration, filing unit or proceeding;
- event type and event date;
- source type, source reference and immutable Document or record;
- retrieval time and retrieval method;
- stated deadline or calculation trigger;
- verified, stale, conflicting, incomplete or interpretation-required state;
- prior snapshot and supersession link;
- responsible professional and next verification trigger.

A later correction creates a new snapshot. It does not overwrite the earlier source.

## 3. Source Hierarchy

The Product preserves the difference between:

```text
official notice or tribunal Document
authenticated official portal record
official public register
verified provider-returned official evidence
provider or party report
client report
Product or AI inference
```

The strongest source depends on the event. A formal notice may control a response obligation before a public register updates.

Provider or party reports may justify urgent review, but they remain qualified until stronger evidence is obtained.

## 4. Contexts Opened by the Event

One Official Event Snapshot may open or update:

- `MR-C03 Examination Context`;
- `MR-C04 Publication Window Context`;
- `MR-C05 Adversarial Context`;
- `MR-C06 Remedy Context`;
- a new formal Matter request where the proceeding has a separate identity.

The Product Context references the formal Matter and source records. It does not replace them.

## 5. Status and State Boundaries

```text
Event detected ≠ event verified
Event verified ≠ professional interpretation
Professional interpretation ≠ strategy
Strategy ≠ Filing Approval
Action filed ≠ official outcome
Product projection ≠ Official Truth
```

Client labels such as `Response required`, `Publication open` or `Opposition pending` must remain traceable to their source and checked time.

## 6. Deadline Candidate

A deadline candidate records:

- triggering event and source;
- stated date or sourced calculation basis;
- Jurisdiction Pack and Rule version;
- time zone, calendar and cutoff;
- extension, suspension or restoration conditions;
- official date and internal safety target;
- verification status;
- owner, escalation and consequence.

An AI-extracted date remains a candidate until governed verification is complete.

## 7. Corrected, Conflicting and Stale Events

For `MR-SCN-10`, stale status must be labelled and refreshed before deadline-sensitive action relies on it.

For `MR-SCN-26`, a corrected notice must:

1. preserve both source versions;
2. supersede the affected Snapshot and Deadline Record;
3. identify affected Issue Sets, Decisions, Packages and Communications;
4. require renewed Review or approval where needed.

For `MR-SCN-27`, conflicting deadline advice remains visible until an eligible professional applies the source hierarchy and records the adopted basis.

## 8. Participant Surfaces

The client sees the verified event, affected scope, immediate deadline, decision need and next action.

The professional sees the original source, prior Package and Decision lineage, source conflicts, Pack version and review controls.

A provider sees only the appointed Matter scope, source notice, deadline and requested task.

Visibility does not change authority.

## 9. `EMBERLOOP` — `EL-23`

The three jurisdictions open independent post-filing contexts:

```text
United States
- sourced non-final examination notice
- goods/services clarification issue
- cited-right concern
- response deadline and professional triage

European Union
- sourced publication event
- later verified opposition event
- publication and adversarial contexts remain distinct

United Kingdom
- sourced publication event
- active monitoring window
- no adverse event assumed before final verification
```

The US application is not described as refused or abandoned. EU opposition does not change the US or UK states.

`RIVERKITE` uses the same controls when the official identifiers, owner fields and challenge source are verified under `RK-02`.

## 10. Controlled Scenarios

- `MR-SCN-10` — stale official status;
- `MR-SCN-23` — technical or provider success without official evidence;
- `MR-SCN-26` — corrected official notice;
- `MR-SCN-27` — conflicting deadline advice.

These replace chapter-local scenario numbering.

## 11. AI Assistance

AI may extract identifiers, dates and issue candidates; compare source versions; prepare plain-language summaries; and flag missing evidence.

AI may not establish the controlling deadline alone, convert a provider report into Official Truth, decide professional meaning, declare refusal or abandonment without source, or send a final legal conclusion without authorized Review.

## 12. Chapter Lock

```text
Every post-filing event preserves
source, authority, retrieval time,
affected scope, deadline, version,
conflict and supersession.

Official Event Snapshot
is not professional interpretation.

A Product Context
is not the official file or formal Matter.
```

## 13. Handoff to CH31

CH30 produces sourced Official Event Snapshots, scoped professional Contexts and deadline candidates.

CH31 converts the US Examination Context into a verified Issue Set, Response Option Set and accountable Response Strategy Decision.