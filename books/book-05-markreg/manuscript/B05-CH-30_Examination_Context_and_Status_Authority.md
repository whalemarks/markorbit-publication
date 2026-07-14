# B05-CH-30 — Examination Context and Status Authority

**Status:** Part V Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part V — Examination, Publication and Disputes

## Chapter Purpose

Part IV ends when a filing or other protected action has been reconciled to reliable evidence.

Part V begins when an office, tribunal, provider, opposing party or verified external source creates a new event that may change scope, deadline, cost, risk or outcome.

The first Product question is:

> What happened, according to which authority, when was it verified, and what professional context must now be opened?

```text
Official or external event
→ source verification
→ Official Event Snapshot
→ Examination Context
→ issue and deadline extraction
→ professional triage
```

A displayed status is not authoritative merely because it looks current.

---

## 1. User Question and Primary Action

**User question:** What is the current procedural event, what does it mean for this right, and what must happen next?

**Primary action:** Review the sourced event summary and open the required professional triage.

The Product must show:

- source and retrieval time;
- affected application, registration, proceeding or filing unit;
- event type;
- stated deadline and its authority;
- whether the event is verified, stale, conflicting or incomplete;
- the responsible professional and immediate next action.

---

## 2. The Examination Context

An Examination Context is a Product-local, versioned working context for a verified post-filing event.

It references rather than replaces:

- the formal Matter;
- official application or proceeding identifiers;
- Filing Package and response-package versions;
- official notices and registry records;
- provider Communications;
- deadlines and responsible actors;
- prior decisions and approvals.

```text
Examination Context
≠ official file
≠ formal Matter
≠ legal conclusion
≠ response strategy
≠ outcome
```

The applicable Owning Service remains authoritative for formal Matter and Document records.

---

## 3. Official Event Snapshot

The Product should create an Official Event Snapshot containing:

| Field | Minimum requirement |
| --- | --- |
| event identity | stable Product event identifier |
| affected right | official identifier, jurisdiction, route and filing unit |
| event type | examination notice, formality request, publication, opposition, decision, status change or other sourced event |
| source | office notice, official portal, official register, tribunal record, verified provider evidence or other identified source |
| source authority | official, provider-reported, party-reported or inferred |
| source version | notice date, document version, portal record or retrieval version |
| retrieval | timestamp, method and actor or connector |
| effective date | stated event date where available |
| deadline | stated or calculated date with source and rule version |
| attachments | source Documents and hashes or stable references |
| confidence | verified, interpretation-required, stale, conflicting, incomplete or unavailable |
| supersession | prior snapshot or event replaced by this event |

The snapshot preserves what the source said. Interpretation belongs to later professional work.

---

## 4. Source Hierarchy

The Product should distinguish source strength rather than combine every statement into one status.

A typical hierarchy is:

```text
Official notice or tribunal document
→ authenticated official portal record
→ official public register
→ verified provider filing or receipt evidence
→ provider or party report
→ client report
→ Product inference
```

The hierarchy is contextual. A formal notice may control a response obligation even when a public register has not yet updated.

The Product must preserve both records and explain the difference.

---

## 5. Product Projection and Official Truth

MarkReg may display a user-friendly projection such as:

```text
Response required
Publication open
Opposition pending
Decision issued
Status needs verification
```

Every projection must retain:

- underlying source;
- retrieval time;
- interpretation status;
- responsible reviewer where interpretation is material;
- known conflicts;
- next verification trigger.

MR-CR-05 applies: Product projection is not official truth without source evidence.

---

## 6. Event Types

Part V may receive:

- formality deficiency;
- examination report;
- office action or provisional refusal;
- request for clarification, amendment or evidence;
- acceptance or approval for publication;
- publication or opposition-window opening;
- opposition, observation or third-party submission;
- suspension, stay or procedural hold;
- hearing, conference or case-management direction;
- refusal, partial refusal, acceptance or other decision;
- appeal or review availability;
- cancellation, invalidation or revocation event;
- corrected or superseding notice;
- official status change with no attached notice;
- provider-reported event awaiting official verification.

The event type controls which Product journey may open next.

---

## 7. Event State

An event may be:

```text
Detected
Source pending
Source received
Verification required
Verified
Interpretation required
Triaged
Decision pending
Action in preparation
Action filed
Outcome pending
Superseded
Closed
Unknown
```

These are Product states. They do not rename official procedural states.

---

## 8. Deadline Extraction

A deadline record should contain:

- triggering event;
- stated date or calculation basis;
- jurisdiction-pack and rule version;
- calendar, time zone and cutoff assumptions;
- extension or restoration information where sourced;
- official and internal safety dates;
- verification status;
- responsible deadline owner;
- escalation path;
- affected action and consequence.

A date extracted by AI is a candidate until verified under the applicable policy.

---

## 9. Conflicting Dates and Statuses

Conflicts may include:

- notice date differs from portal date;
- provider states a deadline that differs from the notice;
- register shows pending while a decision has issued;
- two notices appear to govern the same issue;
- corrected notice changes the response period;
- local counsel and internal calculation use different time zones.

The Product must:

1. preserve each source;
2. identify the conflict;
3. block unsupported certainty;
4. assign professional verification;
5. record the adopted date and reason;
6. retain the superseded calculation.

---

## 10. Corrected and Superseding Events

A later notice may correct:

- applicant or mark details;
- issue description;
- affected classes or items;
- deadline;
- cited rights;
- procedural route;
- hearing information;
- decision outcome.

A corrected notice creates a new Official Event Snapshot.

It may invalidate:

- prior issue extraction;
- response strategy;
- client decision;
- price or provider scope;
- response package;
- approval;
- scheduled Execution action.

No prior event should be deleted merely because it was superseded.

---

## 11. Opening the Professional Context

A verified event should produce or update:

- affected Matter reference;
- Examination Context version;
- Issue Set candidate;
- deadline records;
- required professional role;
- provider need or existing provider context;
- commercial change indicator;
- client Communication requirement;
- immediate blockers and unknowns.

The Product may request creation of a new Matter when the event becomes a distinct adversarial or appellate proceeding. The Owning Service decides and records the formal object.

---

## 12. Participant Views

### Client view

Show:

- plain-language event summary;
- verified source date;
- affected right and scope;
- immediate deadline;
- whether a decision is required;
- expected next step and possible cost change;
- responsible professional.

### Professional view

Show:

- original source Documents;
- official identifiers;
- extracted issues and dates;
- source conflicts;
- filing-package and prior decision lineage;
- provider Communications;
- rule and jurisdiction-pack versions;
- review and escalation controls.

### Provider view

Show only the appointed scope, source notice, relevant history, deadline and requested professional action.

---

## 13. `EMBERLOOP` Continuation

Three post-filing paths now diverge.

### United States

The official source provides a non-final examination notice affecting the word-mark application. The notice contains a goods/services clarification issue and a cited-right concern requiring professional analysis.

MarkReg creates:

- US Official Event Snapshot v1;
- Examination Context US v1;
- two Issue Set candidates;
- an official response deadline and an earlier internal target;
- a professional triage request to the appointed US provider.

The Product does not describe the application as refused or abandoned.

### European Union

The official register and publication record show that the application has entered publication. MarkReg opens a publication-window context and records the opposition end date from the sourced official event.

### United Kingdom

The official record shows publication with no adverse event yet. MarkReg displays an active observation window and schedules verification at the end of the period.

These are three independent procedural contexts. One status does not overwrite the others.

---

## 14. Conformance Scenarios

### MR-SCN-30A — Provider report before official source

**Given** a provider emails that an examination notice has issued but no official notice or portal copy is available.  
**When** MarkReg displays the event.  
**Then** it labels the event provider-reported, requests official evidence, permits urgent professional preparation if authorized, and prevents the report from being displayed as verified official truth.  
**Evidence retained:** provider Communication, retrieval attempts, source status and later official record.

### MR-SCN-30B — Corrected notice changes deadline

**Given** a verified notice is later replaced by an official correction with a different deadline.  
**When** the corrected source is received.  
**Then** MarkReg creates a new snapshot, invalidates the prior deadline and affected readiness, alerts the deadline owner and preserves the old calculation.  
**Authority boundary:** the Product does not silently choose between conflicting official records.

### MR-SCN-30C — Stale public status

**Given** a public register status has not changed for ninety days while a deadline-sensitive Matter is active.  
**When** the user opens the Matter.  
**Then** MarkReg labels the status stale, surfaces the last verified event, and requests official or professional refresh before protected action relies on it.

---

## 15. AI Assistance

AI may:

- classify likely event type;
- extract identifiers, dates, issues and cited records;
- compare notices and detect corrections;
- summarize plain-language impact;
- identify source conflicts;
- prepare an Issue Set candidate;
- recommend a verification or routing task.

AI must not:

- establish the controlling deadline alone;
- declare a legal refusal, acceptance or abandonment without source;
- decide professional meaning;
- waive verification;
- create a binding response strategy;
- communicate a final legal conclusion without authorized review.

---

## 16. Failure Modes to Reject

```text
Provider email shown as official notice
Public register treated as fresher than a formal notice without analysis
Old notice overwritten by corrected notice
Extracted date treated as verified deadline
One country status applied to a multi-country portfolio
Status label used without source and retrieval time
Examination event treated as final refusal
Product creates a new formal Matter by renaming a local state
AI interpretation shown as legal conclusion
```

---

## 17. Minimum Examination Context Lock

```text
Every post-filing event preserves
source, authority, retrieval time,
affected right, deadline, version,
conflict and supersession.

Official Event Snapshot
is not professional interpretation.

Examination Context
is not the official file or formal Matter.

Product projections remain sourced,
time-bounded and reviewable.

AI may extract and explain.
Authorized professionals verify,
interpret and decide.
```

---

## 18. Handoff to Office-Action Triage

The output is a verified or explicitly qualified Official Event Snapshot, an Examination Context, deadline candidates and an initial Issue Set.

CH31 determines how the issues are classified, how scope and consequence are assessed, and which response strategies are presented for accountable Human Decision.