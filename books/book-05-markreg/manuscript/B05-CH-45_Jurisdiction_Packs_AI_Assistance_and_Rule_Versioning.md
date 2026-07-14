# B05-CH-45 — Jurisdiction Packs, AI Assistance and Rule Versioning

**Status:** Part VII Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VII — Product Experience and Evolution

## Chapter Purpose

CH44 defines role-specific participation.

CH45 answers:

> How does MarkReg provide jurisdiction-specific guidance and AI assistance without treating model memory, stale web content, organization custom or provider advice as current official law?

```text
Source evidence
→ controlled rule interpretation
→ Jurisdiction Pack version
→ Product behavior
→ professional validation
→ monitored change and revalidation
```

Jurisdiction intelligence is a governed dependency, not hidden Product code.

---

## 1. User Question and Primary Action

**User question:** Which rule version supports this recommendation, how reliable is it, and what must be rechecked before action?

**Primary action:** Use the current permitted Jurisdiction Pack or escalate the rule for verification.

Every rule-sensitive surface should be able to expose:

- jurisdiction;
- service and lifecycle stage;
- rule or requirement;
- source type;
- source reference;
- checked date;
- effective date, if known;
- pack version;
- confidence and verification status;
- professional owner;
- affected Product behavior;
- next review date or trigger.

---

## 2. Jurisdiction Pack Purpose

A Jurisdiction Pack is the controlled configuration and Knowledge package that allows MarkReg to behave appropriately for a defined jurisdiction, service and time.

It may define:

- filing routes;
- applicant eligibility;
- classification and item rules;
- document and signature requirements;
- representative requirements;
- official fee structures;
- quantity limits and surcharges;
- examination and response stages;
- publication and challenge windows;
- evidence requirements;
- registration-stage fees;
- maintenance and renewal obligations;
- ownership and recordal requirements;
- source and verification rules;
- provider capability requirements;
- Product questions, warnings and blockers.

A Pack does not replace the official office, law, professional judgment or current source verification.

---

## 3. Pack Scope

A Pack must declare its scope.

Minimum scope fields include:

| Field | Meaning |
| --- | --- |
| jurisdiction | country, region or treaty context |
| authority | relevant office or authority |
| service family | filing, response, opposition, renewal, recordal or other defined service |
| lifecycle stages | stages covered |
| applicant types | covered applicant categories |
| route types | direct, regional, international or local route |
| language scope | official and supported working languages |
| effective period | date range or open effective state |
| exclusions | matters not covered |
| professional owner | accountable reviewer |

One jurisdiction may require multiple Packs.

One Pack must not pretend to cover all trademark procedures merely because it uses the jurisdiction name.

---

## 4. Source Hierarchy

Sources should be classified by authority and purpose.

A common hierarchy is:

1. current official legislation, regulation or treaty text;
2. current official office rules, fee schedules, forms and notices;
3. official practice manuals and guidance;
4. official system validation and direct office confirmation;
5. published decisions or authoritative case law where applicable;
6. verified local professional advice;
7. controlled organization experience and prior cases;
8. secondary commentary;
9. unverified public content.

The hierarchy is not mechanical.

A lower-level source may be necessary where official material is unavailable, but its limitation must remain visible.

---

## 5. Source Record

Each material source should have a Source Record containing:

- source ID;
- title;
- issuing authority or author;
- source type;
- jurisdiction;
- language;
- original location;
- retrieved copy or immutable reference where permitted;
- publication date;
- effective date;
- retrieval date and time;
- checksum or version identity;
- access method;
- supersession status;
- confidentiality or license restriction;
- reviewer;
- notes on interpretation.

A web address alone is not sufficient provenance.

---

## 6. Rule Record

A Pack should express operational rules as controlled Rule Records.

A Rule Record may contain:

- rule ID;
- natural-language statement;
- machine-readable condition;
- affected Product stage;
- source links;
- source excerpts or mapped clauses within permitted limits;
- exceptions;
- effective date;
- expiry or review trigger;
- confidence;
- verification status;
- professional owner;
- test scenarios;
- change history.

The machine-readable form must not hide the human-readable legal or operational meaning.

---

## 7. Pack Version

A Pack version identifies a coherent reviewed set of sources, rules, forms, fees and Product behavior.

It should include:

- version ID;
- release date;
- effective date;
- prior version;
- included Rule Records;
- fee-table version;
- form and template versions;
- professional approval;
- known gaps;
- migration and revalidation instructions;
- affected journeys and artifacts.

A new version does not automatically invalidate every historical decision.

The Product must determine whether a change is:

- informational only;
- relevant to new journeys;
- relevant to open unapproved work;
- relevant to approved but unexecuted work;
- relevant to already filed or completed work;
- relevant to future maintenance obligations.

---

## 8. Rule Status

A Rule Record may be:

- draft;
- under verification;
- active;
- active with limitation;
- disputed;
- temporarily suspended;
- superseded;
- withdrawn;
- unknown after detected change.

Only permitted statuses may drive protected Product actions.

An `unknown after detected change` rule should produce a blocker or professional verification requirement, not silent reuse.

---

## 9. Change Detection

Changes may be detected through:

- official publication monitoring;
- office website or fee-table comparison;
- direct connector schema change;
- official form change;
- provider notice;
- professional observation;
- case outcome;
- validation failure;
- user-reported discrepancy;
- scheduled source recheck;
- controlled crawling or source ingestion.

Detection is not adoption.

A detected change creates a Change Candidate.

---

## 10. Rule Change Workflow

```text
Change signal
→ source capture
→ Change Candidate
→ impact assessment
→ professional verification
→ Rule Record revision
→ Pack version candidate
→ tests
→ approval
→ release
→ affected-journey revalidation
```

The workflow should preserve:

- who detected the change;
- old and new source evidence;
- affected rules;
- affected Product behavior;
- effective date uncertainty;
- urgent temporary controls;
- final approval;
- communication to affected users.

---

## 11. Impact Assessment

A rule change may affect:

- new recommendations;
- Quote validity;
- official fees;
- document requirements;
- filing-package schema;
- provider capability;
- deadline calculations;
- pending response strategy;
- renewal obligation;
- client Communication;
- completed historical artifacts.

The Product should identify affected artifact versions and journeys.

It must not rewrite historical records to make them appear created under the new rule.

---

## 12. Fee and Form Changes

Fee tables and official forms are high-risk controlled dependencies.

A fee change should trigger review of:

- open Proposal and Quote versions;
- accepted but unexecuted instructions;
- provider payables;
- client variance rules;
- payment sufficiency;
- refund or supplementary payment conditions.

A form change should trigger review of:

- required fields;
- declarations;
- signature type;
- attachment format;
- connector schema;
- rendered Filing Package;
- approved but unexecuted packages.

A new fee or form does not automatically authorize use.

---

## 13. Organization Overlay

An organization may maintain an overlay containing:

- preferred explanations;
- internal review requirements;
- private provider rules;
- commercial policy;
- internal deadline buffers;
- templates;
- known practice notes;
- risk tolerance;
- local operating language.

The overlay must remain distinguishable from:

- official rule;
- jurisdiction interpretation;
- MarkReg Product default;
- provider-specific requirement;
- client-specific instruction.

Overlay conflicts should be visible and escalated.

---

## 14. Provider-Specific Knowledge

Provider advice may supplement a Pack when:

- the source and provider are identified;
- the advice has a date and scope;
- conflicts and commercial interest are considered;
- official material is checked where available;
- professional validation is recorded;
- the advice is not generalized beyond its scope.

Provider advice may be valuable evidence of current practice. It is not official truth merely because the provider is local.

---

## 15. AI Assistance Contract

AI may assist MarkReg by:

- explaining rules in user-appropriate language;
- mapping business facts to candidate requirements;
- detecting missing information;
- suggesting Rule Records for review;
- comparing source or Pack versions;
- identifying affected artifacts;
- drafting questions, warnings and checklists;
- summarizing provider advice;
- proposing conformance scenarios;
- ranking issues for professional attention.

AI output remains a candidate unless a defined deterministic or professionally approved rule permits direct Product use.

---

## 16. AI Input Context

An AI task should receive only the context required for its purpose.

The task context should identify:

- user role;
- purpose;
- jurisdiction and service;
- Pack version;
- source set;
- permitted organization overlay;
- relevant Product artifact versions;
- confidentiality limits;
- expected output type;
- prohibited conclusions.

The model should not rely on unstated memory for current jurisdiction rules.

---

## 17. AI Output Record

Material AI output should retain:

- output ID;
- task purpose;
- model and system version;
- input references;
- Pack and rule versions;
- generated time;
- confidence or uncertainty indicators;
- citations or source mapping;
- Human Review status;
- accepted, modified or rejected outcome;
- downstream artifacts affected.

The Product need not expose hidden model reasoning.

It must expose the basis needed for professional verification.

---

## 18. Confidence and Uncertainty

Confidence should be multidimensional.

Useful dimensions include:

- source authority;
- source freshness;
- rule clarity;
- fact completeness;
- jurisdiction coverage;
- interpretation stability;
- model agreement;
- professional validation status.

One generic percentage must not imply legal certainty.

The Product should present uncertainty as an action:

- verify official source;
- ask a missing question;
- obtain local advice;
- refresh fee data;
- require professional review;
- block protected action.

---

## 19. Citation and Explanation

Where a recommendation materially depends on a rule, the professional surface should support access to:

- rule statement;
- source reference;
- effective or checked date;
- Pack version;
- relevant exception;
- professional interpretation;
- change history.

Client-facing explanations may be shorter but should not remove material qualifications.

---

## 20. EMBERLOOP Rule Versioning

For `EMBERLOOP`, the UK maintenance view uses a Pack version released after registration.

The new version changes the internal evidence reminder but not the official renewal deadline.

MarkReg:

- preserves the original filing and registration Pack versions;
- applies the new maintenance Pack to future obligations;
- does not rewrite historical recommendations;
- shows the changed reminder logic;
- requires no new Filing Approval because no protected action is being executed.

For the EU opposition, provider advice conflicts with a recently updated official procedural notice.

The rule enters `disputed` status until professional verification resolves the conflict. The Product blocks deadline automation but preserves the earliest credible internal target.

---

## 21. RIVERKITE Rule Versioning

For `RIVERKITE`, an official fee table changes while four renewal packages are open.

MarkReg identifies:

- two Quotes still in draft;
- one accepted instruction with a fee-variance clause;
- one package approved but unpaid;
- one late-renewal candidate in a different rule period.

Each package is reassessed separately.

The system does not apply the new fee to a historical completed renewal or assume the same effective date for every jurisdiction.

---

## 22. Conformance Scenarios

### Scenario A — stale fee table

**Given** a Quote uses a superseded official fee table  
**When** the user attempts acceptance  
**Then** MarkReg blocks acceptance  
**And** produces a revised Quote or documented exception path.

### Scenario B — provider advice conflicts with official source

**Given** a provider states a deadline different from current official guidance  
**When** the conflict is detected  
**Then** the rule is marked disputed  
**And** an accountable professional must verify it.

### Scenario C — AI without pack context

**Given** an AI request asks for a current filing requirement  
**When** no valid Pack or source set is supplied  
**Then** AI may propose a research task  
**But** may not provide the requirement as a current Product rule.

### Scenario D — historical artifact

**Given** an application was filed under Pack v2  
**When** Pack v4 becomes active  
**Then** the historical filing record remains linked to v2  
**And** only future applicable obligations use v4.

### Scenario E — organization overlay conflict

**Given** organization policy permits a document form that the active Pack rejects  
**When** readiness is assessed  
**Then** the jurisdiction rule controls the blocker  
**And** the overlay conflict is reported.

---

## 23. AI Prohibitions

AI may not:

- invent a source;
- present model memory as current law;
- mark an unverified Rule Record active;
- conceal source conflict;
- select an effective date without evidence;
- apply one jurisdiction rule to another silently;
- replace eligible professional validation;
- approve a Pack release;
- execute a protected action;
- rewrite historical Pack lineage.

---

## 24. Failure Modes

MarkReg fails this chapter if:

- jurisdiction logic is hidden only in application code;
- sources have no retrieval or effective dates;
- Pack updates overwrite historical decisions;
- provider advice becomes official truth automatically;
- organization custom is presented as law;
- AI answers current-rule questions without controlled context;
- confidence is a single misleading score;
- rule changes do not identify affected journeys;
- fee and form changes do not revalidate approved work;
- unknown rules continue to drive protected actions.

---

## 25. Minimum Product Lock

A conforming MarkReg edition must provide:

1. scoped and versioned Jurisdiction Packs;
2. controlled Source and Rule Records;
3. source hierarchy and freshness metadata;
4. rule status and change workflow;
5. impact assessment and affected-artifact discovery;
6. separate organization overlays and provider advice;
7. Pack-bound AI task context;
8. auditable AI output records for material work;
9. multidimensional uncertainty and required actions;
10. professional validation before high-risk rule activation.

---

## 26. Next Handoff

CH45 defines how Product behavior is grounded in controlled jurisdiction intelligence.

CH46 defines how MarkReg measures whether that behavior produces quality, safety and user value, and how an MVP should be sequenced.