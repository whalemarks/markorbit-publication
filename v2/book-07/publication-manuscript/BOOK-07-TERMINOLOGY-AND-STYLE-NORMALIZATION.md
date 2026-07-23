# Book 07 v2 — Terminology and Style Normalization

## 1. Purpose

The first full draft was written across eight reconstruction batches. The core model is consistent, but publication requires one controlled vocabulary and one editorial voice.

This document establishes the normalization rules for the next pass. It is an editorial guide, not a new semantic baseline.

## 2. Primary terminology

Use the following forms consistently.

| Preferred term | Meaning in Book 07 | Avoid as casual substitute |
|---|---|---|
| MGSN | Mark Global Service Network | marketplace, directory, exchange |
| Originating Workplace | Workplace projecting the Need and retaining the customer relationship | buyer, client firm, requester when role matters |
| Provider Organization | accountable Organization supplying the service | contact, vendor, agent as universal label |
| Provider Workplace | provider-owned operating context | provider account when sovereignty matters |
| MGSN Connection | controlled boundary between a Workplace and MGSN | integration, sync, open access |
| Capability Need | bounded demand projected to MGSN | job, order, request when semantic precision matters |
| Capability Claim | provider assertion of what it can supply | qualification |
| Professional Qualification | externally grounded recognized status | MGSN approval, platform badge |
| Professional Authority | authority to perform a professional act in the relevant scope | qualification alone |
| MGSN Qualification | network permission for a specific Capability under current rules | licence, legal authority |
| Eligibility | current route-level decision for an exact Need | permanent provider status |
| Candidate Route Set | bounded set of materially different eligible routes | provider list, directory |
| Recommendation | explainable preferred route among eligible alternatives | assignment, appointment, instruction |
| User Disposition | user response to a Recommendation | Provider Acceptance |
| Provider Allocation | pending request to a Provider to accept a route | engagement activation |
| Provider Acceptance | explicit Provider commitment to the exact engagement conditions | delivery confirmation |
| Instruction Package | versioned, attributable operational handoff | attachment bundle |
| Service Package | admitted reusable commercial and service baseline | quote alone |
| Milestone | observable fulfillment stage with Evidence and acceptance criteria | activity update |
| Provider Return | typed evidence package returned by the Provider | email, status update |
| Evidence | attributable material supporting an assertion or state | proof when absolute certainty is not warranted |
| Owning Service | service holding formal business-state authority | MGSN by default |
| Trust | service-specific, evidence-backed, time-bound operating confidence | reputation score |
| Incident | governed review of a potentially material deviation or risk | complaint as proven failure |
| Dispute | bounded contested issue requiring an authority-appropriate forum | incident synonym |
| External Protected Action | action requiring specific authority and controls | routine automation |

## 3. Capitalization

Capitalize terms when they refer to defined MarkOrbit concepts or controlled roles:

- Organization;
- Workplace;
- Capability;
- Capability Need;
- Service Package;
- Provider Return;
- Evidence;
- Eligibility;
- Recommendation;
- Provider Allocation;
- Provider Acceptance;
- Instruction Package;
- Trust;
- Incident;
- Dispute;
- Owning Service;
- External Protected Action.

Use lowercase when the word is generic rather than a defined concept.

Examples:

```text
The provider sent evidence by email.
The Evidence item was linked to the Milestone.

The team recommended a meeting.
The MGSN Recommendation identified Route B.
```

Do not capitalize every operational noun. Over-capitalization makes the book read like an API manual.

## 4. Hyphenation and compound forms

Use:

- cross-border;
- service-specific;
- evidence-backed;
- purpose-limited;
- engagement-scoped;
- matter-specific;
- customer-facing;
- provider-side;
- demand-side;
- supply-side;
- relationship-preserved;
- professional-service;
- official-fee;
- long-form;
- whole-book;
- first-draft;
- no-route;
- safe-stop;
- re-verification;
- re-admission;
- re-routing.

Use `Matter` only where referring to the defined business object or formal operating context. Use `matter` for generic prose where no semantic distinction is needed.

## 5. Preferred verbs

Use verbs that preserve state and authority.

### For MGSN

Preferred:

- records;
- verifies;
- evaluates;
- qualifies under network rules;
- forms a Candidate Route Set;
- recommends;
- allocates;
- coordinates;
- monitors;
- receives a Return;
- reviews completeness;
- restricts;
- escalates;
- supports correction or replacement.

Avoid unless specifically justified:

- appoints;
- authorizes professional action;
- certifies legal qualification;
- decides official status;
- guarantees;
- owns the customer;
- owns the Provider relationship;
- holds funds;
- files;
- settles legal liability.

### For Providers

Preferred:

- claims a Capability;
- accepts or declines an Allocation;
- performs the service;
- exercises professional judgment;
- returns Evidence;
- corrects;
- cooperates with replacement;
- remains accountable within accepted scope.

### For the Originating Workplace

Preferred:

- retains the customer relationship;
- projects a Capability Need;
- confirms a route;
- provides or obtains customer authority;
- approves commercial changes where authorized;
- validates the operational context;
- reconciles the Return with the Matter.

## 6. Distinction formulas

The manuscript uses inequality formulas effectively, but they should be selective.

Retain formulas when they introduce or close a major boundary.

Preferred pattern:

```text
A
≠ B
```

Avoid stacking more than four lines unless the sequence itself is the argument.

Keep the following as recurring anchor formulas:

```text
Recommendation
≠ Appointment

Provider Acceptance
≠ Customer Instruction

Payment
≠ Performance

Provider Return
≠ Official Truth

Return Accepted
≠ Formal State Updated

Data Portability
≠ Authority Portability
```

Other distinctions should usually be explained in prose after their primary chapter.

## 7. Use of English Product terms

The manuscript is currently English-language, but its editorial logic should still avoid unnecessary jargon.

Use a defined Product term when it carries a real distinction. Use ordinary language where no semantic loss occurs.

Examples:

Prefer:

> The provider has not yet accepted the work.

Over:

> The Provider Acceptance object has not transitioned to Active.

Prefer:

> The route must be checked again because the deadline changed.

Over:

> Eligibility requires recomputation after Need Version mutation.

The book may name the model after explaining the operating problem. It should not lead with internal object grammar.

## 8. Chapter opening standard

Each chapter should open with one of the following:

1. a recognizable operating scene;
2. a practical contradiction;
3. a question a professional operator would ask;
4. a failure that exposes the chapter’s distinction.

Avoid openings that begin with:

- schema definitions;
- long lists;
- abstract governance declarations;
- repeated explanations of what MGSN is not.

Recommended opening rhythm:

```text
Operating reality
→ hidden risk
→ chapter question
→ governing distinction
```

## 9. Chapter body standard

Each chapter should generally contain:

- operating problem;
- principal distinction;
- model or lifecycle;
- participant implications;
- failure and recovery;
- transition to the next chapter.

Not every chapter needs the same number of sections. Mechanical uniformity should not replace narrative judgment.

## 10. Chapter ending standard

End chapters by advancing the chain.

Preferred:

> Once the Provider has accepted the route, the network still needs a versioned instruction that shows exactly what may be done. The next chapter explains that handoff.

Avoid endings that merely restate every lock introduced in the chapter.

The final `Product principle` section may remain where it performs synthesis, but repeated boilerplate should be shortened.

## 11. Lists and tables

Use prose for argument. Use lists for bounded reference material.

Convert a long list into a table when the reader needs to compare dimensions, roles, states or evidence types.

Good table candidates:

- participant responsibilities;
- authority layers;
- route types;
- package cost layers;
- Return types;
- Incident severity;
- dispute forums;
- metric families.

Avoid lists exceeding twelve items in the main narrative unless the completeness of the inventory is itself important.

Move extensive inventories to appendices or reference boxes.

## 12. Examples

Use generalized examples drawn from international professional-service operations.

Preferred example pattern:

```text
Situation
→ hidden ambiguity
→ unsafe shortcut
→ governed response
```

Examples must not fabricate:

- current law;
- jurisdiction-specific filing requirements;
- official fees;
- qualification rules;
- actual production capability;
- real Provider performance;
- customer facts.

Where a legal or professional rule is necessary, describe it as jurisdiction-dependent unless supported by reviewed authority.

## 13. Authority language

Always identify the source of authority.

Instead of:

> The provider is authorized.

Prefer:

> The provider’s professional status has been verified for the stated service scope, and Matter-specific appointment remains to be confirmed.

Instead of:

> MGSN approves the filing.

Prefer:

> MGSN records that the required operational checks are complete; the authorized customer or professional actor must still approve the protected action.

Use `may`, `can`, `should` and `must` carefully:

- `must` for manuscript constitutional locks or required control logic;
- `should` for recommended Product or editorial practice;
- `may` for permitted alternatives;
- `can` for capability, not authority unless the authority source is explicit.

## 14. Funds language

Keep separate:

- amount quoted;
- invoice issued;
- payment requested;
- payment received;
- funds cleared;
- funds allocated;
- Provider funded;
- official fee reportedly paid;
- official receipt received;
- settlement authorized;
- settlement executed;
- reconciliation completed.

Avoid `paid` without identifying:

- who paid;
- whom;
- for what layer;
- whether the funds cleared;
- what Evidence exists.

Do not use `escrow`, `trust account`, `client money`, `custody` or `funds release` as ordinary Product language unless the legal and operating basis is specifically established.

## 15. Trust language

Use service-specific statements.

Preferred:

> The Provider has strong recent Evidence for routine filing Returns in this jurisdiction.

Avoid:

> The Provider is highly trusted.

Distinguish:

- relationship confidence;
- verified qualification;
- recent performance;
- recovery behavior;
- current Eligibility;
- unresolved Incident or Dispute.

Do not use stars, global ranks or generalized `best provider` language.

## 16. Incident and dispute language

Use allegation-neutral language before findings.

Preferred states:

- concern reported;
- Incident opened;
- Evidence under review;
- protective restriction applied;
- finding substantiated, partially substantiated, not substantiated or unresolved;
- dispute referred to an appropriate forum.

Avoid:

- guilty;
- fraudulent;
- negligent;
- liable;
- misconduct established;

unless the relevant authority has actually made that determination and the publication is entitled to rely on it.

## 17. AI language

AI may be described as assisting with:

- extraction;
- comparison;
- classification;
- completeness checks;
- stale-data detection;
- draft explanation;
- anomaly flags;
- evidence organization.

AI must not be described as independently:

- granting qualification;
- clearing conflicts;
- appointing Providers;
- approving customer instructions;
- authorizing payments;
- deciding incidents or disputes;
- determining liability;
- updating official or formal state;
- executing External Protected Actions.

Use:

```text
AI-assisted
human-reviewed
source-backed
scope-bounded
```

where those facts are actually part of the described model.

## 18. Cross-book references

Use reader-facing references rather than repository-facing references.

Preferred:

> Book 03 explains how governed execution handles review, recovery and safe retry.

Avoid in publication prose:

> See B03-F2-RUNTIME-014.

Internal identifiers may remain in source registers and editorial notes, not in the main reader-facing manuscript unless included in a technical appendix.

## 19. Editorial normalization checklist

For every chapter, verify:

- title matches the chapter’s actual argument;
- opening begins from an operating problem;
- primary defined terms use the preferred form;
- capitalization is intentional;
- repeated inequality formulas are reduced;
- long lists are justified or converted;
- authority source is explicit;
- funds language is typed;
- failure mode includes recovery;
- AI role remains assistive;
- conclusion advances to the next chapter;
- no current law or production capability is invented.

## 20. Normalization verdict

```text
Core vocabulary: STABLE
Capitalization: REQUIRES PASS
Hyphenation: REQUIRES PASS
Authority language: MOSTLY CONSISTENT, REQUIRES FINAL REVIEW
Funds language: CONSISTENT, REQUIRES LEGAL/OPERATING REVIEW
Trust and incident language: CONSISTENT
AI authority boundaries: CONSISTENT
Reader-facing style: REQUIRES DENSITY REDUCTION
Cross-book references: REQUIRES PUBLICATION PASS
```

This guide should govern the chapter-level editorial revisions that follow the continuity audit.