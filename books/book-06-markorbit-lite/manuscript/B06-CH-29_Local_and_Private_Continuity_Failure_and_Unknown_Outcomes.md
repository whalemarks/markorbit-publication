# B06-CH-29 — Local and Private Continuity, Failure and Unknown Outcomes

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — MarkOrbit Gateways and Continuity  
**Primary controls:** ML-H02, ML-E04, ML-SCN-23–ML-SCN-24

## Chapter Purpose

This chapter explains how Lite preserves continuity when information remains local or private, when a destination requests more information, when a Handoff is rejected or blocked, when systems fail, and when the external outcome is unknown.

The central proposition is:

> Continuity means preserving enough trustworthy context to continue safely; it does not mean synchronizing everything or pretending uncertain outcomes are complete.

A resilient Lite Product must make incomplete, blocked and unknown states visible rather than hiding them behind optimistic automation.

## 1. Continuity is not universal synchronization

The easiest technical model is often:

```text
collect everything
→ upload everything
→ centralize everything
→ let every feature read everything
```

That model is unsuitable for professional trademark work.

The user's working context may include:

- public sources;
- Organization Internal records;
- Personal Private notes;
- Client Restricted information;
- Matter Restricted documents;
- Network Shared data;
- Local Only files;
- data that may be processed locally but not synchronized;
- data that may be summarized but not disclosed;
- data that may be disclosed only after client approval.

Therefore:

```text
available on device
≠ available to Lite cloud services

readable by a local component
≠ authorized for AI use

used to prepare a local Artifact
≠ authorized for Handoff

synchronized
≠ shareable with every destination
```

Continuity must preserve these differences.

## 2. Hybrid minimization

Hybrid minimization means that Lite uses the smallest appropriate combination of local and shared processing for the current purpose.

A journey may operate as follows:

```text
Local Only customer file
→ local extraction of required fields
→ user inspection
→ minimized structured package
→ explicit disclosure decision
→ destination Handoff
```

The full source file may remain local.

Only the necessary fields, representation or approved derivative may move.

Hybrid minimization asks:

- can the purpose be achieved locally?
- does the destination need the source or only a verified field?
- can an identifier or reference replace a copy?
- can the customer identity remain withheld at the current stage?
- can the user approve the exact disclosure before transfer?
- can the destination request more information later if needed?

The goal is not maximum localization or maximum cloud use.

The goal is minimum necessary exposure with sufficient continuity.

## 3. Local files and Local Vault participation

A local file may contribute to Lite without becoming a universal platform Asset.

Possible participation states include:

- visible only to the user;
- readable by a local component;
- indexed locally;
- referenced by metadata only;
- summarized locally;
- included in a specific Review Package;
- disclosed to one destination under explicit authorization;
- prohibited from synchronization;
- retired or removed from future use.

A Local Vault may preserve:

- file reference;
- local path or secure identifier;
- checksum or version indicator;
- classification;
- controller;
- allowed purposes;
- allowed processors;
- disclosure conditions;
- expiry;
- last verification time.

It should not imply that the platform owns the file or may copy it freely.

## 4. Derived information inherits restrictions

A common mistake is to protect the source file but treat its extracted text or summary as unrestricted.

Restrictions may follow the information into:

- Source Observation;
- Signal;
- Candidate;
- Structured Content;
- Artifact;
- Memory Candidate;
- Handoff Envelope;
- Return presentation.

Example:

```text
Matter Restricted document
→ locally extracted deadline
→ Today Attention Item
```

The deadline may be displayed to an authorized user.

It does not automatically become:

- an Organization-wide fact;
- a public Knowledge item;
- a customer-development signal;
- a provider-routing disclosure;
- an authoritative deadline without destination validation.

```text
derived
≠ unrestricted
```

## 5. `ML-SCN-24` — local access does not imply synchronization

The blocking scenario is:

> A local file is readable, but synchronization is not authorized.

Expected Product behavior:

- the file remains local;
- local processing respects allowed purpose;
- no upload occurs;
- no hidden remote embedding or AI call receives the content;
- generated local outputs preserve classification;
- a proposed Handoff shows what would be disclosed;
- user or policy approval is required before transfer;
- denied disclosure leaves the journey usable where possible.

A conforming Product should be able to say:

```text
This source was used locally to prepare the draft.
The source file has not been uploaded.
The following three fields are proposed for disclosure to MarkReg.
```

## 6. Private continuity across sessions

Personal Private and Local Only information may help the same user continue work later.

Continuity may preserve:

- the last inspected Candidate;
- a local reference;
- an unfinished Artifact Draft;
- a user disposition;
- missing-information checklist;
- selected Handoff destination;
- an unsent Prepared Action.

The Product must not expose that continuity to another user or Organization merely because both use the same platform.

When a user changes Organization context, Lite should re-evaluate:

- access;
- allowed sources;
- local references;
- Customer and Matter scope;
- memory visibility;
- Handoff permissions.

```text
same person
+ different Organization context
→ different authorized Product context
```

## 7. More-information requests are part of the journey

A destination often cannot accept the first Handoff.

It may return:

```text
more_information_required
```

That is not a generic failure.

The Return should identify:

- which information is missing;
- why it is necessary;
- who may supply it;
- which source or document type is acceptable;
- whether the request changes urgency;
- whether previous Review remains valid;
- whether disclosure authorization is required;
- the destination reference and expiry.

Lite may then create a Continuation State:

```text
MarkReg requires confirmed applicant address
→ local/client source identified
→ user requests customer confirmation
→ corrected information returned
→ continuation Handoff
```

The Product should not fill missing information with inference merely to keep the workflow moving.

## 8. Rejection is not technical failure

A destination may reject a Handoff because:

- the request is outside scope;
- the need is not sufficiently qualified;
- duplicate formal state exists;
- authority is absent;
- conflict or policy blocks the request;
- data disclosure is not permitted;
- the selected destination is wrong;
- the request is stale;
- the user or Organization lacks access.

Rejection should preserve:

- destination;
- reason;
- source Handoff;
- whether correction is possible;
- whether another destination is appropriate;
- whether the Candidate or Artifact should be retired;
- whether a Safety / Privacy Finding is required.

A rejected Handoff may still produce Product value by preventing unsafe or duplicate formal work.

## 9. Blocked states

A request may be blocked by:

- permission;
- policy;
- missing Human Review;
- missing final confirmation;
- client restriction;
- Local Only rule;
- expired authorization;
- conflict;
- protected-action gate;
- destination unavailability.

The Product should preserve specific states such as:

```text
blocked_by_permission
blocked_by_policy
review_required
confirmation_required
source_disclosure_not_authorized
protected_action_gate_required
```

A single `blocked` label may be used in a summary, but the underlying reason must remain inspectable.

## 10. Technical failure

Technical failure means the requested operation did not complete because the system or connection failed.

Examples:

- destination API unavailable;
- local vault temporarily locked;
- rendering process failed;
- network connection interrupted before request submission;
- authentication expired;
- response could not be parsed.

Technical failure must remain distinct from:

- professional rejection;
- policy block;
- user cancellation;
- destination unsupported result;
- unknown external outcome.

The Product should record:

- operation attempted;
- exact version;
- failure time;
- whether the destination received the request;
- whether retry is safe;
- whether user action is required;
- correlation or request identifier;
- data exposure that may already have occurred.

## 11. Unknown external outcome

Unknown external outcome is one of the most important continuity states.

It applies when Lite cannot determine whether the destination completed the consequential action.

Examples:

- a Communication request timed out after submission;
- a Publish request lost the response;
- a provider-routing request may have been received;
- an Execution request returned no acknowledgement;
- a manual user action was reported but not evidenced;
- a local-to-cloud transfer was interrupted after partial upload.

The correct state is:

```text
unknown_external_outcome
```

It must not be translated into:

- completed;
- failed;
- safe to retry;
- customer did not respond;
- destination rejected.

## 12. Why blind retry is dangerous

Retry may cause:

- duplicate customer messages;
- duplicate public posts;
- duplicate Product Sessions;
- duplicate Opportunities;
- duplicate provider requests;
- duplicate payments;
- duplicate filings or protected actions.

Before retry, Lite or the destination must attempt reconciliation using:

- request identifier;
- destination reference;
- timestamp;
- recipient;
- exact version;
- idempotency key where available;
- destination search;
- acknowledgement evidence;
- manual confirmation.

```text
no response from destination
≠ destination did nothing
```

## 13. Reconciliation after unknown outcomes

A reconciliation flow may be:

```text
unknown external outcome
→ freeze automatic retry
→ inspect request and destination references
→ query destination status
→ inspect Communication / Publish / Execution evidence
→ classify as completed / failed / blocked / still unknown
→ update Return presentation
→ continue or escalate
```

If the outcome remains unknown, the Product should:

- show the uncertainty;
- identify possible consequences;
- prevent conflicting actions;
- assign or suggest a reconciliation step;
- preserve evidence;
- avoid optimistic metrics.

## 14. Version and synchronization conflicts

Local and shared state may diverge.

Examples:

- a local Artifact Draft was edited after a cloud Review;
- a local customer address differs from the formal Customer record;
- two devices edited the same Preference Candidate;
- an old local template was used after the shared Asset was retired;
- a Return projection is older than the destination record.

The Product should not silently choose the newest timestamp as truth.

Conflict resolution should consider:

- authority source;
- version lineage;
- responsible owner;
- review status;
- classification;
- correction records;
- destination formal state;
- whether merging is semantically safe.

Possible results include:

```text
local version retained as draft
shared formal state retained as authority
manual review required
new combined version created
stale local version retired
```

## 15. Expired, suppressed and retired states

Continuity includes knowing when not to continue.

### Expired

The source, permission, candidate set, price or approval is no longer current.

### Suppressed

The subject must not appear in a given journey, ranking, outreach or disclosure path.

Examples:

- opt-out;
- duplicate prospect suppression;
- conflict restriction;
- customer-development prohibition.

### Retired

The item remains in history but must not be used for future generation, recommendation or action.

```text
retired
≠ erased history
```

These states should propagate to downstream Candidates, Artifacts and Handoffs where relevant.

## 16. Failure should not destroy continuity

A failed destination request should not force the user to reconstruct the journey.

Lite may preserve:

- source Candidate;
- exact Artifact Version;
- user decisions;
- Handoff package;
- destination response or failure;
- information already supplied;
- missing information;
- safe next options.

The continuation should begin from the last trustworthy state.

```text
failure
→ preserve trusted context
→ identify uncertain consequence
→ choose safe recovery
```

It should not begin from an empty chat prompt.

## 17. Local and private Handoff example

A user has a signed power of attorney stored in a Local Vault.

MarkReg requests authority information.

### Local inspection

Lite confirms locally:

- file exists;
- checksum matches the previously inspected version;
- document appears to relate to the named applicant;
- source is Matter Restricted;
- cloud synchronization is not generally authorized.

### Disclosure proposal

Lite prepares:

```text
Destination: MarkReg
Purpose: applicant authority validation
Proposed disclosure: exact POA file and checksum
Scope: named Product Session only
Expiry: current intake cycle
User confirmation required: YES
```

### Decision

The user authorizes disclosure for that Product Session.

The file is transferred under the specific Handoff.

This does not make the POA available to:

- other Organizations;
- MGSN candidate discovery;
- content generation;
- public publication;
- unrelated Matters.

## 18. `ML-SCN-23` — destination revalidation and Return

The blocking scenario requires:

> Lite sends a MarkReg, MGSN, Review or Communication Handoff; the destination revalidates, and the returned result retains origin and source.

A conforming result must show:

- source Lite record;
- exact Handoff version;
- destination;
- destination decision;
- formal reference where applicable;
- source and result time;
- missing information or limitations;
- destination ownership of formal state;
- Return presentation in Lite.

Failure to preserve this lineage creates false continuity.

## 19. Safety and privacy findings

`ML-E04 Safety / Privacy Finding` should be created when the journey reveals:

- unauthorized upload;
- excess disclosure;
- restricted information in the wrong package;
- local-only data sent remotely;
- opt-out ignored;
- stale authority reused;
- unknown outcome shown as completed;
- blind retry attempted;
- cross-Organization exposure;
- retired Asset used;
- formal state copied and independently mutated.

The finding should identify:

- affected record and version;
- source and destination;
- severity;
- actual or potential exposure;
- containment;
- correction;
- downstream impact;
- prevention measure.

Blocking an unsafe action is a Product success, not a failure of convenience.

## 20. Common failure patterns

### Failure 1 — automatic local upload

A file is indexed locally and silently uploaded for AI processing.

Why it fails:

- local access is treated as synchronization permission.

### Failure 2 — derived summary loses classification

A restricted document is summarized, and the summary becomes Organization-wide content.

Why it fails:

- restrictions did not follow the information.

### Failure 3 — unknown shown as failed

The Product retries a message because no send acknowledgement returned.

Why it fails:

- the customer may receive duplicates.

### Failure 4 — unknown shown as completed

The Product reports successful publication without destination evidence.

Why it fails:

- metrics and user decisions rely on false state.

### Failure 5 — rejection erased

A destination rejection is removed and the Candidate returns to Today unchanged.

Why it fails:

- the user repeats an invalid action;
- learning and accountability disappear.

### Failure 6 — newest timestamp wins

A recent local edit overwrites authoritative destination state.

Why it fails:

- recency is confused with authority.

## 21. Conformance questions

A conforming implementation should answer:

- Where is the source information stored?
- What classification applies?
- May it be processed locally?
- May it be synchronized?
- May it be disclosed to this destination?
- What exact fields or files will leave the local boundary?
- Who authorized disclosure?
- What derived records inherit restrictions?
- What information did the destination request?
- Is the Handoff rejected, blocked, failed or unknown?
- Is retry safe?
- How is duplicate consequence prevented?
- Which version is authoritative?
- How are local/shared conflicts resolved?
- What happens when permission expires?
- How are suppression and retirement propagated?
- Can the user resume from the last trustworthy state?

## Chapter Conclusion

A trustworthy Lite Product does not promise that every step will succeed.

It promises that the user can understand:

- what is known;
- what is local or restricted;
- what was disclosed;
- what destination decided;
- what failed;
- what remains unknown;
- what may safely happen next.

```text
continuity
= trustworthy context + explicit boundary + typed result + safe next step
```

This principle completes Part VI.

Lite becomes a low-friction gateway not by removing governance, but by carrying the right context across governance boundaries without losing responsibility, privacy or uncertainty.