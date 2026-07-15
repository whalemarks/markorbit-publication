# B06-SPEC-0002 — Reference Journeys and State Transitions

## 1. Identity

```text
Specification: B06-SPEC-0002
Version: v0.1
Status: Candidate — accepted as Product Baseline on owner merge
Controlled journeys: ML-J01–ML-J04
```

## 2. Journey standard

Every reference journey must identify:

- initiating authority and source;
- active Organization, user, customer/trademark/Matter scope;
- Product-local records created;
- user decisions and Human Review;
- destination Handoff and expected Return;
- safe stop, rejection, expiry and unknown states;
- feedback, memory and reuse treatment;
- records that remain externally owned.

A journey success is not defined only by activity volume.

## 3. `ML-J01` — Existing Customer Portfolio Opportunity

### Goal

Turn authorized customer and trademark context into a relevant service opportunity, a trustworthy customer work product and a governed service Handoff.

### Flow

```text
authorized Customer / Trademark projection
→ ML-O01 Source Observation
→ ML-O02 Customer / Trademark Signal
→ ML-O03 Service-Value Candidate
→ ML-O07 Recommendation Presentation
→ ML-S04 User Disposition
→ ML-W01 Structured Content
→ ML-W02 / W03 Artifact Draft and Version
→ ML-W06 Development Package
→ ML-W05 Prepared Action
→ final user confirmation
→ ML-H06 Communication Handoff or confirmed manual contact
→ customer response
→ ML-O08 Qualification Result
→ ML-H07 Opportunity request and/or ML-H03 MarkReg Handoff
→ ML-H02 returned result presentation
→ ML-M01/M02 feedback and correction
```

### Required states

- candidate explained;
- accepted, deferred, rejected, suppressed or corrected;
- work product ready/blocked/incomplete;
- contact confirmed/not performed;
- response, no response, rejection or unknown;
- qualified/not qualified;
- Handoff accepted/rejected/more information required;
- returned formal reference.

### Safe stops

- stale or missing source;
- no customer/Matter access;
- conflicting trademark status;
- no lawful purpose to contact;
- missing professional review;
- user rejects the opportunity;
- destination rejects the Handoff.

## 4. `ML-J02` — Historical Customer Reactivation

### Goal

Use authorized relationship history and a current trigger to prepare a respectful, relevant reactivation action.

### Flow

```text
authorized historical relationship
+ current service/trademark trigger
→ ML-O04 Reactivation Candidate
→ source, freshness and contactability review
→ ML-O07 Recommendation
→ ML-W06 Development Package
→ recipient and channel confirmation
→ Communication Handoff or manual action
→ response / no response / opt-out / invalid contact
→ qualification
→ formal service Handoff where appropriate
```

### Controls

- past relationship does not imply current permission for every channel;
- stale contact information must be marked;
- opt-out and suppression override growth ranking;
- no response does not imply rejection or consent;
- historical private data must not become platform prospect supply.

## 5. `ML-J03` — Prospect Candidate Development

### Goal

Turn an authorized public or user-owned source into an explainable prospect candidate without pretending it is a Customer, Qualified Lead or formal Opportunity.

### Flow

```text
authorized source
→ ML-O01 Observation
→ ML-O05 Prospect Candidate
→ source / freshness / duplicate / contactability inspection
→ service relevance explanation
→ ML-O08 Qualification Result
→ ML-W06 Development Package
→ final recipient/channel confirmation
→ outreach
→ response / no response / invalid / opt-out
→ formal Customer or Opportunity request only when justified
```

### Controls

```text
publicly discoverable ≠ contactable by every channel
contact found ≠ current or accurate
signal detected ≠ purchase intent
Prospect Candidate ≠ Customer
user acceptance ≠ formal Opportunity
```

Platform-supplied prospects must preserve source, replacement, duplicate and suppression treatment defined by the relevant commercial experiment.

## 6. `ML-J04` — Case-to-Work-Product

### Goal

Convert authorized case experience into an audience-specific work product without exposing restricted facts or treating one result as universal law.

### Flow

```text
authorized case context
→ ML-M06 Case Lesson Candidate
→ Human Review and scope decision
→ ML-M07 Reusable Asset Candidate or ML-M08 Knowledge Contribution Candidate
→ approved source set and audience
→ ML-W01 Structured Content
→ ML-W02/W03 Artifact
→ ML-W04 Review Package
→ ML-W07/W08 Render
→ ML-W09 Delivery/Publish Package Candidate
→ user-confirmed or governed distribution
→ ML-H02 result presentation
→ ML-M01/M02 feedback and correction
```

### Controls

- client and Matter facts remain restricted;
- anonymization alone does not create publication permission;
- Evidence is not automatically reusable content;
- approved internal Asset is not automatically public;
- later legal or factual correction must retire affected versions.

## 7. Cross-journey variants

The following are variants, not new constitutional loops:

- recurring or daily content supply;
- quotation and fee explanation;
- trademark layout proposal;
- returned MarkReg result creating a new customer action;
- MGSN Capability Need created from a qualified service gap;
- local/private case retrieval supporting a work product;
- small-team review and responsibility assignment.

Variants must still map to one or more `ML-J01–J04` journeys and `ML-SCN-*` scenarios.

## 8. State-transition rules

### Candidate state

```text
observed
→ explained
→ inspected
→ accepted_for_preparation / deferred / rejected / suppressed / corrected
→ qualified_for_handoff
→ handed_off
→ expired / retired
```

### Work-product state

```text
candidate
→ draft
→ versioned
→ review_required
→ ready_for_confirmation / blocked / incomplete
→ handed_off
→ returned_result_observed
→ reused / corrected / retired
```

### External action result

```text
not_requested
→ prepared
→ confirmed
→ accepted_by_destination
→ completed / failed / blocked / unknown
```

An `unknown` result must not be silently changed to completed or automatically retried.

## 9. Journey acceptance

A reference journey conforms only when:

- every material record has source and scope;
- formal objects remain externally owned;
- required decisions and confirmation are visible;
- Handoff and Return are typed;
- failure and unknown states are preserved;
- feedback does not automatically become shared truth.
