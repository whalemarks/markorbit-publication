# B07-CH-23 — Fulfillment Milestones and Evidence

## 1. Fulfillment is more than a status label

A managed service cannot be governed by a single field such as `in progress` or `completed`.

MGSN needs typed milestones tied to expected evidence.

Examples include:

- instruction accepted;
- documents checked;
- application prepared;
- filing submitted;
- official receipt received;
- office action reviewed;
- response filed;
- publication confirmed;
- registration completed;
- certificate delivered.

The exact milestones vary by service and jurisdiction.

## 2. Milestone definition

A Fulfillment Milestone should identify:

- engagement and service scope;
- milestone type;
- responsible participant;
- expected date or time window;
- required preconditions;
- expected evidence;
- acceptance or validation rule;
- dependency on another milestone;
- escalation threshold;
- current observation status.

A milestone is a network coordination object. It does not replace the authoritative Matter or Task state.

## 3. Expected Evidence

Expected Evidence defines what should be returned to support a claimed outcome.

It may include:

- official receipt;
- filing confirmation;
- stamped document;
- correspondence from an authority;
- provider work product;
- courier proof;
- invoice or disbursement proof;
- translation or legalization certificate;
- structured provider declaration;
- source-qualified status extract.

The requirement should specify source, format, freshness and minimum content.

## 4. Evidence quality

Evidence is not equally reliable merely because it is attached to an engagement.

MGSN should distinguish:

```text
official-source evidence
provider-produced evidence
third-party evidence
customer-supplied evidence
operator observation
unverified assertion
```

Quality assessment may consider:

- source identity;
- authenticity indicators;
- completeness;
- date and freshness;
- connection to the relevant engagement;
- consistency with other evidence;
- whether verification is possible;
- whether the evidence is provisional or final.

## 5. Fulfillment Observation

A Fulfillment Observation records what the network currently knows about progress.

Possible observations include:

- expected;
- reported complete;
- evidence received;
- evidence incomplete;
- evidence disputed;
- overdue;
- blocked;
- corrected;
- replaced;
- unknown.

```text
Provider reports completion
≠ verified milestone

Verified milestone
≠ authoritative Matter state
```

The Originating Workplace and the relevant Owning Service decide how verified evidence affects formal state.

## 6. Deadline monitoring

Deadline control must distinguish:

- legal deadline;
- provider target;
- platform operating target;
- customer-requested target;
- internal review buffer;
- evidence-return deadline.

A missed internal target may not mean a legal deadline was missed, but it can still trigger escalation.

Deadline monitoring should expose uncertainty rather than creating false precision when the external source is unclear.

## 7. Partial and conditional completion

Complex services often finish in stages.

For example:

- filing completed but receipt pending;
- official fee paid but authority acknowledgement pending;
- response submitted but annex confirmation missing;
- registration granted but certificate delivery pending.

The model should represent partial completion without prematurely declaring the whole engagement complete.

## 8. External self-managed evidence

R1 external routes may also return evidence into the Workplace through the External Route Evidence Bridge.

Such evidence must remain source-qualified:

```text
external upload
→ source classification
→ validation
→ accepted, provisional, disputed or unknown result
```

MGSN must not imply that an external provider was governed by the platform when it was not.

## 9. Learning without overreach

Verified fulfillment evidence can later support Trust and network learning, but raw observations must not automatically become performance judgments.

Context matters:

- service type;
- jurisdiction;
- complexity;
- customer-caused delay;
- authority-caused delay;
- provider responsibility;
- evidence quality.

## 10. Product boundary

This chapter defines milestone and evidence semantics. It does not authorize official-source scraping, automatic legal conclusions, formal-state mutation, external filing or production monitoring.
