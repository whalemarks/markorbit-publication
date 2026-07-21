# Chapter 14 — Clarification with Fewer Questions and More Inference

Traditional professional intake often begins with a long form.

The form asks the user to choose countries, classes, goods, mark types, filing routes, budgets, timelines and professional options before the user understands why those choices matter.

This transfers the burden of expertise to the person seeking help.

A conversational AI system can reduce the burden, but only if it does more than replace form fields with chat messages. Asking the same thirty questions one by one is not intelligence. It is a slower form.

Lite should infer what it can, expose the inference and ask only the questions that materially change the matching route.

```text
free-form demand
→ structured candidate interpretation
→ impact analysis of unknowns
→ high-value clarification
→ user confirmation or correction
→ route-ready Request
```

The objective is not to eliminate questions. It is to maximize useful inference while preserving the user’s right to understand and correct the system.

## 1. Why fewer questions matter

Every question has a cost.

The user may:

- not know the answer;
- not understand the terminology;
- select an arbitrary option;
- abandon the process;
- provide inconsistent answers;
- assume the platform has already given legal advice;
- mistake a required field for a required business decision.

A short process is not automatically better. The correct measure is:

```text
information gained
÷
user effort and decision burden
```

A useful question changes candidate generation, ranking, disclosure, legal review or commercial route. A low-value question can be deferred until a later stage.

## 2. Inference should begin from existing context

Lite may already know relevant context from governed sources:

- the buyer’s business description;
- existing customer records;
- prior Requests;
- uploaded product materials;
- selected trademark or keyword;
- target website or market;
- current Inventory;
- prior rejected candidates;
- Workplace preferences;
- channel and budget history;
- jurisdiction Knowledge;
- language and communication context.

The system should not ask the user to repeat information already known and current.

It should also avoid using information from another Workplace or relationship without authority.

```text
available somewhere in the platform
≠ available for this Request
```

## 3. Separate extraction, inference and recommendation

The system should distinguish three operations.

### Extraction

Extraction identifies information explicitly stated by the user.

Example:

> “We need a short English name for coffee equipment in the United States.”

Extracted:

- language: English;
- style: short;
- industry: coffee equipment;
- jurisdiction: United States.

### Inference

Inference derives likely structure from context.

Possible inference:

- Class 11 may be relevant for certain coffee machines;
- additional classes may be relevant depending on goods and services;
- an existing US registration may be preferred if speed is important.

These are not user statements.

### Recommendation

Recommendation proposes a decision or route.

Example:

- prioritize registered Class 11 assets first;
- include a secondary search for new-filing candidates;
- ask whether retail services or coffee products are also planned.

```text
Extracted
≠ Inferred
≠ Recommended
```

The interface should make the distinction visible.

## 4. Confidence alone is not enough

An inference may have high statistical confidence but low decision safety.

For example, “skincare” strongly suggests Class 3. Yet a buyer may also need retail, medical, device or educational services.

Lite should consider:

- confidence;
- consequence of error;
- reversibility;
- cost of asking;
- cost of proceeding incorrectly;
- whether the inference narrows rights or supply;
- whether professional judgment is required.

A low-consequence style preference may be inferred and offered for correction. A class or legal-coverage decision may require explicit confirmation or professional review.

## 5. Questions should be ranked by route impact

A high-value clarification question affects one or more of:

- available inventory pools;
- legal scope;
- jurisdiction;
- price range;
- transaction speed;
- confidentiality;
- disclosure permissions;
- buyer decision criteria;
- professional-review needs;
- acquisition versus filing route.

A useful sequence might ask:

1. Is an existing registration required, preferred or optional?
2. Which market must be covered first?
3. Which actual products or services will use the mark?
4. Is exact wording more important than legal scope or speed?
5. What budget range is realistic including transfer and professional costs?

Questions about color preference, visual mood or slogan can often follow after viable legal-commercial routes are known.

## 6. Offer choices that reveal trade-offs

Users often answer better when presented with understandable priorities rather than technical fields.

Lite may ask:

```text
Which matters most for the first shortlist?

A. Exact or near-exact name
B. Strong fit with the industry and audience
C. Existing registration and useful goods coverage
D. Lower price and faster transaction
E. Balanced options across all four
```

The response does not create a permanent rule. It guides the first route and can be revised after the buyer sees candidates.

Another example:

```text
For the United States and China, would you prefer:

A. One name with viable routes in both markets
B. An existing right in either market plus a filing strategy for the other
C. Separate marks if that produces better options
D. Show all routes with trade-offs
```

These choices expose the real decision rather than asking the user to guess a complex legal structure.

## 7. Clarification can be progressive

Not every question belongs at intake.

A progressive sequence may be:

### Stage 1 — discovery

Clarify:

- business category;
- naming direction;
- main jurisdiction;
- budget and timeline;
- existing-right preference.

### Stage 2 — shortlist refinement

Clarify:

- exact goods;
- acceptable variants;
- visual and semantic preferences;
- price flexibility;
- transfer complexity tolerance.

### Stage 3 — inquiry preparation

Clarify:

- buyer identity disclosure;
- decision maker;
- seller-contact route;
- due-diligence expectations;
- commercial terms.

### Stage 4 — transaction or filing handoff

Clarify:

- contracting party;
- payment route;
- transfer documents;
- professional authority;
- filing or recordal requirements.

Progressive clarification prevents the first conversation from becoming a complete transaction intake.

## 8. The system should explain why it is asking

A question becomes easier when the user understands its effect.

Instead of:

> Select the relevant Nice classes.

Lite may say:

> Your products appear to center on cosmetics, so Class 3 is likely important. Retail services or beauty devices may require additional coverage. Which products will carry the mark first?

Instead of:

> Choose public or private.

Lite may say:

> A private Request protects your launch plans but reaches fewer sellers. A network Request may find more options while keeping your identity hidden. Which exposure level fits this search?

The explanation should remain concise and avoid presenting uncertain recommendations as law.

## 9. Confirmation should be granular

The user should not have to approve an entire AI-generated Request as one block.

A structured confirmation can show:

```text
Confirmed by user
Extracted from message
Inferred — please confirm
Recommended default
Unknown — affects route
Optional for later
```

The user may accept most fields and correct one.

Granular confirmation produces better provenance and reduces the tendency to accept a polished but inaccurate summary.

## 10. Silence is not confirmation

If the user does not correct an inference, that does not necessarily mean agreement.

The system may use low-risk defaults for exploration, but should not convert silence into:

- final goods specification;
- permission to publish buyer demand;
- consent to disclose identity;
- acceptance of price;
- authority to contact sellers;
- professional instruction;
- commitment to purchase.

```text
No objection
≠ informed confirmation
```

## 11. Contradictions should be surfaced, not silently resolved

A buyer may say:

- exact name is essential;
- budget is very low;
- registration must already exist in two countries;
- completion is needed within days.

These constraints may conflict.

Lite should identify the contradiction and offer routes:

```text
Route A — exact name, but likely new filing and longer timeline
Route B — existing registration, with more name flexibility
Route C — one jurisdiction first, second jurisdiction later
Route D — higher budget for scarce matching supply
```

The system should not hide the conflict by producing poor candidates that appear to satisfy everything.

## 12. User language should remain the primary interface

The internal model may use classes, goods taxonomies, semantic vectors and jurisdiction profiles. The user should not be forced to speak in system ontology.

The user may say:

- “smart home lights”;
- “coffee shop brand”;
- “a name that sounds Japanese but is easy in English”;
- “something energetic for sportswear.”

Lite should translate these expressions into candidate internal structure and ask for confirmation where the translation matters.

The system should preserve the original wording because it contains nuance that normalized fields may lose.

## 13. Professional review should be triggered by consequence

AI-assisted clarification may be enough for early matching. Professional input may be required when:

- goods and classes materially affect candidate viability;
- the buyer requires specific legal coverage;
- several jurisdictions are involved;
- transliteration or meaning creates risk;
- the proposed acquisition route is unusual;
- a candidate is being presented as transaction-ready;
- the buyer seeks clearance or legal availability conclusions;
- confidentiality or conflict rules are complex.

A professional may review the Request itself before reviewing candidates.

This is a legitimate paid contribution when it creates production value.

## 14. Clarification should learn from rejection without overfitting

When the buyer rejects candidates, Lite can ask a focused follow-up:

- Was the problem the sound, meaning, look, legal scope, price or seller condition?
- Is this a hard exclusion or a preference?
- Should the Request be updated for all future candidates?

One rejection should not automatically rewrite the buyer profile. The buyer should confirm durable preference changes.

```text
Observed rejection
≠ permanent preference
```

## 15. Clarification history is evidence

The system should retain:

- original user statements;
- extracted fields;
- AI inferences;
- questions asked;
- user confirmations;
- corrections;
- professional comments;
- Request versions;
- reasons for material route changes.

This history helps explain why certain candidates were searched and presented.

It also helps resolve disputes where the buyer later says that a key requirement was misunderstood.

## 16. Low-friction does not mean hidden complexity

The product should absorb complexity without concealing material trade-offs.

A simple interface can still show:

- what is known;
- what is assumed;
- what remains uncertain;
- which question changes the route;
- why professional review may be needed;
- what will happen next.

The user should experience fewer decisions, not fewer rights to understand the decision.

## 17. Example: reducing a long intake to three questions

Suppose the buyer says:

> “We are launching a premium pet-care line in the US. We want a short, friendly English name and would prefer to buy something registered. Budget around USD 6,000.”

Lite extracts:

- premium pet-care line;
- United States;
- short friendly English name;
- existing registration preferred;
- budget approximately USD 6,000.

It may infer:

- goods may involve pet shampoos, grooming preparations, food, accessories or retail services;
- several classes may be relevant;
- exact product scope will materially affect candidate suitability.

Instead of a twenty-field form, Lite asks:

1. Which products will carry the mark first: grooming products, food, accessories or several of these?
2. Is an existing registration mandatory, or may we include exceptional new-filing names?
3. Which matters more: a very friendly name or broader useful goods coverage?

The answers create a first matching route. Additional legal and transaction details can follow only when a viable candidate appears.

## 18. Failure modes

The clarification model fails when:

- chat reproduces a long form question by question;
- AI fills every unknown automatically;
- extracted and inferred facts are not distinguished;
- confidence is treated as permission;
- the system asks questions already answered in governed context;
- private context from another Workplace is reused;
- silence becomes confirmation;
- contradictory constraints are hidden;
- the user is forced to learn Nice Classification before receiving help;
- every rejection permanently changes the buyer profile;
- professional review is skipped because the interface feels conversational;
- “fewer questions” becomes a marketing claim masking weak due diligence.

## 19. Product and technical implications

Lite needs:

- free-form conversation capture;
- structured extraction;
- inference provenance;
- confidence and consequence assessment;
- route-impact scoring for unknowns;
- question selection;
- concise trade-off options;
- progressive intake stages;
- granular confirmation;
- contradiction detection;
- original-language retention;
- Request versioning;
- review escalation;
- clarification audit history;
- correction and deletion controls.

The clarification engine should propose Request updates. The Request Owning Service or responsible Product workflow should control accepted state changes.

## 20. Commercial implications

Better clarification can improve:

- time to first shortlist;
- user completion;
- candidate relevance;
- professional-review efficiency;
- buyer trust;
- conversion from Request to Inquiry;
- demand intelligence;
- inventory recruitment decisions.

It can also reduce revenue from unnecessary consultations or form-filling services. That is not a reason to preserve avoidable friction.

Professional value should move toward judgment, risk, negotiation and execution rather than charging users for translating basic needs into internal fields.

## 21. Metrics that matter

Useful measures include:

- questions asked before first viable shortlist;
- percentage of fields extracted versus manually entered;
- inference correction rate;
- high-impact unknowns remaining at presentation;
- Request abandonment;
- time to clarification;
- candidate rejection caused by misunderstood requirements;
- professional escalation rate;
- user comprehension of trade-offs;
- later dispute or correction rate.

A low question count is not success if the recommendations are wrong.

## 22. The operating principle

```text
Infer what the evidence supports
Show the inference
Ask what changes the route
Explain the trade-off
Preserve Unknown
Require confirmation where consequence is high
```

> Lite should feel easier than a professional form because the system carries more of the reasoning burden—not because it hides uncertainty or makes decisions on the buyer’s behalf.