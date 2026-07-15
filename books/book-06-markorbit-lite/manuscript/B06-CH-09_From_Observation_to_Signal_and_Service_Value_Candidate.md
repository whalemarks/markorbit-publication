# B06-CH-09 — From Observation to Signal and Service-Value Candidate

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part II — The Daily Operating Model

## Chapter Purpose

This chapter explains how MarkOrbit Lite turns raw observations into explainable Product-local candidates without pretending that a detected change is already a verified client need or formal Opportunity.

The central proposition is:

> A source observation becomes useful only after it is linked to authorized context, interpreted for a defined professional purpose, tested against uncertainty and expressed as a bounded candidate.

The controlled sequence is:

```text
Source Observation
→ Customer / Trademark Signal
→ Service-Value, Reactivation, Prospect or Work-Product Candidate
→ Recommendation Presentation
→ User inspection and qualification
```

## 1. Data Changes Do Not Speak for Themselves

A system may detect:

- a registration anniversary;
- a new company product;
- a change in trademark status;
- a missing jurisdiction in a portfolio;
- an unanswered customer message;
- a public filing by a potential customer;
- a new legal or procedural update;
- a returned request from MarkReg;
- a stale work product;
- an expired provider quotation.

These are observations.

They do not automatically establish:

- legal obligation;
- customer need;
- purchase intention;
- professional recommendation;
- urgency;
- commercial value;
- permission to contact;
- formal work.

```text
change detected
≠ problem verified
≠ service needed
≠ customer willing to buy
```

Lite must preserve this distinction from the first record.

## 2. `ML-O01 Source Observation`

A Source Observation is a normalized, source-linked statement about something detected.

It should identify:

- the source;
- source type;
- retrieval or effective time;
- observed subject;
- observed value or change;
- previous value where available;
- transformation or extraction method;
- confidence;
- contradictions;
- freshness;
- allowed purpose.

Examples:

```text
Official register retrieved on 2026-07-15
shows status X for trademark Y.
```

```text
Customer website retrieved on 2026-07-15
shows a new product line under brand Z.
```

```text
Internal relationship record shows no recorded contact
for customer A during the last twelve months.
```

The Observation should not contain an unsupported conclusion such as:

> Customer A needs a new filing immediately.

That conclusion belongs to a later candidate stage.

## 3. Normalization Does Not Create Canonical Truth

Lite may normalize:

- names;
- dates;
- status labels;
- jurisdiction codes;
- service categories;
- contact fields;
- product descriptions;
- document references.

Normalization improves comparison. It does not make the data authoritative.

A public website may use a brand name informally.

A company directory may contain an outdated contact.

An unofficial status feed may lag behind an office register.

An AI extraction may misread a date or party name.

```text
normalized value
≠ verified fact
```

The Observation retains its source authority and limitations.

## 4. A Signal Connects Observation to Authorized Subject Context

`ML-O02 Customer / Trademark Signal` links an Observation to an authorized customer, trademark, relationship or portfolio context.

For example:

```text
Observation:
A registration anniversary is approaching.

Signal:
This registration belongs to Customer A,
Customer A is within the active Organization scope,
and no completed maintenance service is currently projected.
```

Another example:

```text
Observation:
A public company has launched product P under brand B.

Signal:
The company is not a Customer,
but the product/brand combination may be relevant
to the Organization's service geography and expertise.
```

The Signal should preserve:

- subject linkage method;
- whether the link is verified or inferred;
- relationship ownership;
- duplicate or conflict information;
- data classification;
- purpose;
- confidence and missing facts.

## 5. Signal Types Should Remain Distinct

Different observations support different candidate paths.

### Portfolio signal

Links a current Customer or Trademark to a possible service gap, risk or next step.

### Relationship signal

Links an inactive or under-served customer to a current, relevant trigger.

### Prospect signal

Links a public or user-owned source to a possible target organization or person.

### Work-product signal

Indicates that a report, explanation, proposal, content item or other professional result may be useful.

### Return signal

Connects a destination result to the originating Lite journey.

One signal may support more than one candidate, but the Product should not collapse their meanings.

## 6. `ML-O03 Service-Value Candidate`

A Service-Value Candidate explains a possible professional service need.

It should answer:

1. Which customer, trademark or relationship is involved?
2. Which Observation and Signal support the candidate?
3. What professional or commercial value may exist?
4. What is uncertain?
5. What harm could result from acting incorrectly?
6. What additional information is required?
7. Which work product could help the user or customer decide?
8. Which formal destination may eventually own the work?

A useful candidate may say:

> This Customer’s registration appears to be approaching a maintenance period. The official source was retrieved on the stated date. Existing records do not show a completed maintenance service. Verify ownership, current status and jurisdiction-specific requirements before contacting the customer.

The candidate remains Product-local.

```text
Service-Value Candidate
≠ formal Opportunity
≠ professional conclusion
≠ customer instruction
```

## 7. Service Value Is Broader Than Sales Value

A candidate may create value by:

- preventing a missed action;
- identifying a service need;
- clarifying a customer decision;
- correcting inaccurate data;
- improving a work product;
- reducing unnecessary work;
- preserving client trust;
- identifying that no action should be taken.

Revenue may result, but the candidate should not be ranked solely by expected fee.

For example, a high-fee filing possibility may be inappropriate if:

- the customer does not need the protection;
- ownership is unclear;
- the source is stale;
- the risk is not understood;
- the client has opted out of contact;
- the proposed route is not commercially reasonable.

```text
service value
= client value + professional quality + suitable commercial value
```

## 8. `ML-O04 Reactivation Candidate`

A Reactivation Candidate combines:

- an authorized historical relationship;
- a current relevant trigger;
- contactability and suppression context;
- a reason to reconnect respectfully.

It should not be generated merely because a customer has been inactive.

Weak logic:

> No contact for six months; send a sales message.

Stronger logic:

> The Organization previously served this customer. A current source shows a new brand launch in a jurisdiction relevant to the prior relationship. Contact details are stale and channel permission is unknown. Prepare a reactivation package only after verification.

Past business does not create permanent permission.

## 9. `ML-O05 Prospect Candidate`

A Prospect Candidate is a candidate organization or person derived from an authorized public or user-owned source.

It should preserve:

- source;
- source date;
- identity confidence;
- duplicate treatment;
- why the subject may be relevant;
- known contactability;
- channel limitations;
- whether the candidate was supplied by the platform or the user;
- suppression or replacement rules.

It must not be described as:

- an intention customer;
- a qualified lead;
- a Customer;
- an Opportunity;
- a guaranteed contact.

```text
public signal
→ possible relevance
→ Prospect Candidate
→ Human qualification
→ possible outreach
→ response
→ only then possible qualified need
```

## 10. `ML-O06 Work-Product Candidate`

Sometimes the next useful result is not customer contact but preparation.

A Work-Product Candidate may propose:

- a portfolio review;
- a client-facing explanation;
- a fee comparison;
- a trademark layout proposal;
- a case summary;
- a reusable article;
- a short video;
- a follow-up message;
- a MarkReg intake summary.

The candidate should identify:

- purpose;
- audience;
- source set;
- required claims;
- expected format;
- Review need;
- intended destination.

It does not become an Artifact merely because AI produced text.

## 11. Candidate Creation Requires Interpretation

A reliable candidate may combine several factors:

```text
Observation
+ authorized subject context
+ business relationship
+ professional rule or Knowledge
+ source freshness
+ service history
+ user preference
+ risk and uncertainty
→ Candidate
```

Interpretation may involve AI, deterministic rules, human input or a combination.

The Product should preserve which elements were:

- explicit facts;
- calculated;
- inferred;
- AI-proposed;
- user-confirmed;
- professionally reviewed.

This makes later correction possible.

## 12. One Observation May Produce Multiple Candidates

A new product launch may support:

- an existing customer portfolio opportunity;
- a historical customer reactivation;
- a Prospect Candidate;
- a customer-facing article;
- a trademark layout proposal;
- a MarkReg pre-intake preparation.

The Product should not automatically create all of them.

It should consider:

- active relationship;
- user intent;
- data permission;
- relevance;
- duplication;
- current workload;
- confidence;
- likely value;
- risk.

Candidate generation is selective composition, not uncontrolled expansion.

## 13. Multiple Observations May Support One Candidate

A Service-Value Candidate may require several sources:

```text
official trademark status
+ customer portfolio record
+ service history
+ customer website
+ jurisdiction Knowledge
→ explainable candidate
```

The candidate should preserve each source and any contradiction.

If one source says the registration is active and another says it has expired, the Product should not hide the conflict behind one confidence score.

It may:

- block the candidate;
- request verification;
- present alternative interpretations;
- lower confidence;
- require Human Review.

## 14. Stale and Conflicting Sources Must Change Behavior

`ML-SCN-02` requires that stale or conflicting sources produce a warning or block confident recommendation.

A Product should not merely display a small icon while continuing the same action path.

Depending on consequence, it may:

- prevent external contact;
- require source refresh;
- exclude the item from ranking;
- create a verification Prepared Action;
- show a historical-only label;
- route to Human Review.

```text
stale source
≠ normal candidate with cosmetic warning
```

## 15. Missing Access Must Stop Restricted Candidate Creation

`ML-SCN-03` requires that a user without Customer or Matter access does not receive restricted facts.

The Product may still display a minimized indication such as:

> Additional authorized context is required.

It must not expose:

- customer identity;
- Matter details;
- restricted documents;
- confidential case facts;
- private communication.

Blocked preparation is a successful safety outcome.

## 16. Client Interest and Professional Risk Override Revenue Ranking

`ML-SCN-06` is a blocking scenario.

Suppose the Product estimates that one service could generate more revenue than another.

If the higher-revenue option:

- provides little client value;
- creates unnecessary filing cost;
- carries unverified assumptions;
- ignores a conflict;
- risks professional harm;

then revenue cannot control ranking.

The candidate should explain the safer or more suitable route, including a recommendation not to proceed where appropriate.

## 17. Candidate State Must Be Explicit

The controlled candidate lifecycle is:

```text
observed
→ explained
→ inspected
→ accepted_for_preparation
   / deferred
   / rejected
   / suppressed
   / corrected
→ qualified_for_handoff
→ handed_off
→ expired / retired
```

These states describe Product-local handling.

They do not imply:

- Customer acceptance;
- Opportunity creation;
- Task completion;
- Communication sending;
- MarkReg acceptance;
- official action.

## 18. Expiry and Retirement Are Different

A candidate may expire because:

- source freshness window passed;
- commercial timing passed;
- contact data became stale;
- user-defined defer period ended without refresh.

A candidate may be retired because:

- it was based on an error;
- a formal result resolved the issue;
- a newer candidate superseded it;
- policy prohibits further action;
- the user or reviewer determined it is not reusable.

These states support audit and learning.

## 19. Corrections Should Affect the Right Scope

A user may correct:

- the customer relationship;
- mark ownership;
- contact permission;
- source interpretation;
- service history;
- candidate reason;
- confidence;
- intended destination.

The correction should identify:

- affected Observation, Signal or Candidate;
- whether related candidates are impacted;
- whether a source record should be refreshed;
- whether a Memory Candidate is appropriate;
- whether formal external records require separate correction.

Lite must not silently mutate records owned elsewhere.

## 20. Minimum Conforming Observation-to-Candidate Flow

A minimum conforming Product should demonstrate:

1. a source-linked `ML-O01` Observation;
2. authorized subject linkage in `ML-O02`;
3. at least one distinct candidate type;
4. explicit source freshness and confidence;
5. visible missing information;
6. stale/conflicting-source behavior;
7. permission-blocked behavior;
8. candidate lifecycle states;
9. no direct creation of formal Opportunity;
10. no claim that Prospect Candidate is purchase intent;
11. client-interest precedence;
12. correction and expiry handling.

## Chapter Conclusion

MarkOrbit Lite creates value not by detecting more changes, but by converting the right observations into bounded, explainable candidates under the correct professional context.

```text
Observation
+ authorized subject context
+ purpose
+ professional interpretation
+ uncertainty
→ Signal
→ Candidate
```

The next chapter explains how candidates are presented, ranked, inspected and qualified by the user without turning recommendation into decision or approval.