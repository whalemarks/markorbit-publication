# B06-CH-27 — MGSN Capability Need and Provider Boundaries

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part VI — MarkOrbit Gateways and Continuity  
**Primary controls:** ML-H04, ML-HC-02

## Chapter Purpose

This chapter explains how Lite expresses a service capability need to the Mark Global Service Network without becoming a provider directory, routing authority, appointment system or cross-Organization collaboration owner.

The central proposition is:

> Lite may describe the capability that is needed; MGSN owns how trusted capability is discovered, minimized, routed and returned.

The gateway must help a small trademark professional reach broader global capacity without exposing unnecessary customer information or pretending that a candidate provider has been selected or appointed.

## 1. Why Lite needs an MGSN gateway

An independent trademark professional or small agency may identify a valid customer need but lack the required execution capability.

Examples include:

- a jurisdiction outside the user's direct service coverage;
- a specialized opposition, cancellation or customs matter;
- a local-language or local-representation requirement;
- a document legalization or notarization requirement;
- a search, investigation or Evidence need;
- a filing volume or timing constraint;
- a need for a specific professional qualification;
- an urgent local response where existing provider coverage is unavailable.

Lite may know:

- the customer objective;
- the jurisdiction;
- the service category;
- the timing;
- the known constraints;
- the required output;
- the user's commercial or confidentiality preferences.

Lite should not independently claim to know:

- which provider is trustworthy;
- whether a provider remains qualified;
- whether a provider is available;
- whether a conflict exists;
- whether a price is current;
- whether a provider may receive the customer identity;
- whether a provider has accepted appointment;
- whether cross-Organization collaboration has begun.

Those are MGSN and destination responsibilities.

The correct pattern is:

```text
qualified service gap
→ Capability Need
→ minimized MGSN Handoff
→ Trust and Routing evaluation
→ candidate or unsupported Return
→ user inspection and next governed step
```

## 2. `ML-H04` is a Capability Need Handoff

`ML-H04 MGSN Capability Need Handoff` is not a provider order.

It says:

> Lite has identified a bounded service capability requirement and is asking MGSN to evaluate whether suitable capability can be returned under the allowed disclosure scope.

It does not say:

- a provider has been chosen;
- a provider has been appointed;
- a price has been accepted;
- customer data may be disclosed;
- a Matter has been assigned;
- cross-Organization collaboration is active;
- the service can be delivered;
- Trust requirements are satisfied.

```text
Capability Need
≠ provider search result
≠ provider recommendation
≠ appointment
≠ assignment
≠ service acceptance
```

## 3. Capability Need is about the work, not the provider name

A useful Capability Need begins with the work to be accomplished.

It should describe:

- jurisdiction or region;
- service category;
- procedural stage;
- required professional capability;
- language capability;
- expected deliverable;
- timing and urgency;
- required authority or qualification;
- confidentiality level;
- communication or collaboration constraints;
- commercial constraints where permitted;
- information that remains unknown.

Example:

```text
Jurisdiction: Brazil
Service: opposition response support
Stage: pre-deadline assessment
Required capability: local trademark counsel
Language: Portuguese and English
Timing: preliminary view within three business days
Disclosure: anonymized mark and goods only at candidate stage
Commercial constraint: request current fee structure before customer approval
```

This is stronger than:

```text
Find a Brazilian lawyer
```

The second statement hides the service, risk, timing and disclosure rules.

## 4. Minimum disclosure is the default

MGSN discovery should begin with the least information needed to evaluate capability.

A staged disclosure model may be:

### Stage 1 — Capability discovery

Share:

- jurisdiction;
- service type;
- stage;
- urgency;
- language;
- broad subject category;
- required qualification;
- high-level constraints.

Do not share by default:

- customer name;
- full mark details;
- adverse party;
- confidential Evidence;
- internal budget;
- private communication;
- unrelated Matters.

### Stage 2 — Candidate inspection

After MGSN returns a minimized candidate set, the user may inspect:

- capability scope;
- verified qualification indicators;
- jurisdiction coverage;
- service categories;
- availability signals;
- permitted commercial information;
- conflict-check requirements;
- disclosure prerequisites.

### Stage 3 — conflict and suitability check

Additional information may be disclosed under a specific purpose and authorization.

### Stage 4 — appointment or collaboration

Only after the appropriate decisions, permissions, commercial terms and destination controls may a provider receive the necessary full context.

```text
candidate discovery
≠ authority to disclose full client data
```

## 5. `ML-HC-02` minimum package

A conforming MGSN Handoff should preserve:

### 5.1 Origin

- Lite Session;
- Organization;
- initiating user;
- source Customer/Trademark/Matter references where authorized;
- source Service-Value Candidate or MarkReg need;
- return address.

### 5.2 Capability definition

- jurisdiction;
- service type;
- procedural stage;
- required deliverable;
- professional qualification;
- language;
- timing;
- expected service depth;
- excluded service categories.

### 5.3 Constraints

- urgency;
- confidentiality;
- conflict sensitivity;
- client preference;
- collaboration preference;
- communication requirements;
- permitted commercial disclosure;
- prohibited destinations;
- data residency or Local-only limits.

### 5.4 Disclosure scope

- information included now;
- information deliberately withheld;
- conditions for later disclosure;
- data classification;
- controller;
- expiry of permission.

### 5.5 Missing information

- unconfirmed deadline;
- unknown adverse party;
- incomplete applicant identity;
- unclear service scope;
- customer approval still required;
- budget not yet accepted.

A missing field must not be guessed merely to obtain more candidates.

## 6. MGSN owns Trust and Routing

MGSN is responsible for network-level questions that Lite must not duplicate.

These include:

- provider identity;
- Organization identity;
- capability claims;
- qualification status;
- Trust signals;
- jurisdiction coverage;
- service taxonomy;
- availability;
- routing eligibility;
- conflict-check process;
- collaboration depth;
- network participation rules;
- provider suspension or retirement;
- cross-Organization disclosure controls.

Lite may present a sourced MGSN result.

Lite must not maintain an independent provider score and represent it as authoritative MGSN Trust.

```text
Lite preference
≠ MGSN Trust

historical provider use
≠ current qualification

low price
≠ suitability
```

## 7. The returned candidate set

MGSN may return a minimized candidate set.

A useful Return may contain:

- candidate provider or Organization reference;
- capability match reason;
- jurisdiction and service match;
- Trust or qualification indicators permitted for display;
- availability status or limitation;
- conflict-check requirements;
- commercial information allowed at this stage;
- data required for the next step;
- source and freshness;
- ranking explanation or absence of ranking;
- unsupported or partial-match warnings.

The Return should not expose hidden network data merely because Lite asked for a candidate.

Candidate count is not the primary quality measure.

```text
many providers
≠ suitable capability
```

One explainable, eligible candidate may be more useful than fifty unverified names.

## 8. No automatic provider appointment

A provider candidate must pass additional steps before appointment.

Depending on the service, these may include:

- user inspection;
- customer approval;
- conflict check;
- price confirmation;
- scope confirmation;
- availability confirmation;
- confidentiality terms;
- authority or engagement terms;
- formal order or Matter creation;
- provider acceptance;
- Task or Workflow creation.

Therefore:

```text
MGSN candidate returned
≠ provider selected

provider selected by user
≠ provider appointed

commercial terms shown
≠ commercial terms accepted

provider accepted
≠ External Protected Action authorized
```

Lite may prepare the next action, but the relevant destination owns the formal state.

## 9. User preference and Organization policy

Lite may hold bounded preference candidates such as:

- preferred working language;
- preference for electronic certificates;
- preference for fixed-fee quotations;
- preferred communication cadence;
- preference for providers already used by the Organization.

Those preferences may influence the Capability Need.

They do not override:

- qualification;
- Trust;
- conflict;
- jurisdiction rules;
- customer interest;
- network policy;
- current availability.

An Organization may also define approved-provider policies.

Lite should reference those policies rather than convert them into hidden personal preference.

## 10. Commercial information is purpose-limited

Provider pricing may be sensitive, dynamic and scoped.

A candidate Return may contain:

- current reference fee;
- date and currency;
- included services;
- excluded services;
- official fees;
- taxes;
- validity period;
- volume assumptions;
- confidential or Organization-only restrictions.

Lite must not treat an old provider price as a current promise.

```text
historical price
≠ current quote

reference fee
≠ final engagement price
```

The user may use permitted commercial information to prepare a customer option, but a formal quotation or order remains governed by the relevant service.

## 11. Unsupported, partial and more-information results

MGSN may return:

### Unsupported

No suitable capability is currently available under the stated constraints.

This is a valid result.

Lite should not fill the gap with an unverified internet contact and present it as MGSN capability.

### Partial match

A candidate may match jurisdiction and service but not timing, language or qualification depth.

The mismatch must remain visible.

### More information required

MGSN may need:

- more precise service stage;
- clearer deadline;
- adverse-party identity for conflict evaluation;
- applicant type;
- required qualification;
- desired deliverable;
- permitted disclosure scope.

Lite should request only what is necessary for the next routing step.

### Rejected or blocked

The request may be blocked by:

- permission;
- policy;
- network participation rules;
- prohibited disclosure;
- unsupported jurisdiction;
- expired source context.

### Failed or unknown

A technical failure or unknown outcome must not be turned into an empty candidate list without explanation.

## 12. Return into Today

Today may display:

- MGSN needs more information;
- suitable capability was not found;
- a candidate set is available;
- conflict data is required;
- candidate availability has expired;
- customer approval is needed before disclosure;
- a provider-selection decision is pending;
- the next step belongs in MarkReg, Opportunity, Order or Execution.

The Today item should identify:

- the Capability Need;
- source customer or service context;
- Return freshness;
- disclosure stage;
- user decision required;
- destination for the next formal step.

It must not display:

```text
provider appointed
```

unless the destination Owning Service has returned that formal result.

## 13. A complete example

A client needs an urgent cancellation defense in a jurisdiction not covered by the user's existing network.

### In Lite

The user qualifies the need and prepares:

```text
jurisdiction
service stage
deadline source and confidence
required local counsel capability
language
expected preliminary deliverable
anonymized subject summary
customer identity withheld at candidate stage
```

### In MGSN

MGSN returns:

- two capability candidates;
- one partial candidate unavailable before the deadline;
- one candidate requiring adverse-party identity for conflict check;
- current commercial information with a seven-day validity period.

### Back in Lite

Today shows:

- candidate-match reasons;
- the unavailable candidate as ineligible for the current timing;
- the conflict information request;
- a prepared customer approval message;
- a next-step Handoff option.

Lite does not automatically reveal the customer name or claim that a provider has been appointed.

## 14. Common failure patterns

### Failure 1 — turning MGSN into a public directory

Lite exposes provider names without Trust, scope, freshness or disclosure controls.

Why it fails:

- capability is reduced to a contact list;
- network governance disappears;
- stale or suspended providers remain visible.

### Failure 2 — price-first routing

The cheapest candidate is automatically ranked first.

Why it fails:

- qualification, timing, conflict and customer interest are ignored.

### Failure 3 — full customer disclosure at discovery stage

The entire Matter file is sent to every potential provider.

Why it fails:

- confidentiality and purpose limitation are breached;
- conflict and network controls are bypassed.

### Failure 4 — treating a candidate as appointed

The UI says “agent assigned” after candidate return.

Why it fails:

- user/customer decision and provider acceptance are skipped.

### Failure 5 — shadow Trust scoring

Lite computes its own opaque “best lawyer” score from historical use and presents it as authoritative.

Why it fails:

- MGSN Trust meaning is redefined;
- users cannot inspect the basis or freshness.

## 15. Conformance questions

A conforming implementation should answer:

- What exact capability is needed?
- Why is MGSN required?
- What information is disclosed at the current stage?
- What information remains withheld?
- Which user and Organization authorized the Handoff?
- Which constraints affect routing?
- Who owns Trust and Routing?
- How fresh is the candidate set?
- Does a candidate fully or partially match?
- What is required before conflict checking or appointment?
- Has the customer approved additional disclosure?
- Which destination owns provider selection and appointment?
- What happens when no capability is available?
- What happens when the Return is stale or unknown?

## Chapter Conclusion

The MGSN gateway expands the user's reach without pretending that Lite owns the network.

```text
Lite expresses the need
MGSN evaluates trusted capability
Human and formal services decide the engagement
Lite preserves continuity
```

The result is not merely access to more provider names.

It is governed access to suitable capability under explicit disclosure, Trust and routing boundaries.

That is the correct role of `ML-H04` and `ML-HC-02`.