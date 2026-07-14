# B05-SPEC-0004 — Jurisdiction Pack and Commercial Control Contract

## Status

- **Status:** Controlled Specification v0.2
- **Applies to:** CH09–CH46
- **Workstream:** PF-05 — Jurisdiction and Commercial Reconciliation
- **Purpose:** Define the minimum jurisdiction, rule, form, fee, service-support and commercial controls required before MarkReg may guide, prepare, execute or continue a trademark-service journey.
- **Authority boundary:** A Jurisdiction Pack is a controlled Product dependency. It is not law, legal advice, an official office, provider appointment, Filing Approval or production authority.

## 1. Contract Objective

A jurisdiction name, fee table, provider profile or AI-generated answer is not enough to claim support.

```text
supported jurisdiction/service/stage
= scoped Pack version
+ controlled sources and rules
+ service-specific Product behavior
+ professional ownership
+ commercial control
+ scenario evidence
+ maintenance and suspension process
```

Support must be declared at the level of:

- jurisdiction or regional authority;
- service family;
- lifecycle stage;
- applicant or owner type;
- route;
- language;
- Pack version;
- support state;
- effective period;
- known exclusions.

A Pack that supports new filing preparation does not automatically support opposition, renewal, recordal or assignment.

---

## 2. Controlled Record Alignment

This specification consumes B05-SPEC-0001 v0.2.

| Contract concept | Controlled record |
| --- | --- |
| Jurisdiction Pack | MR-G01 |
| Source Record | MR-G02 and MR-E07 |
| Rule Record | MR-G03 |
| Change Candidate | MR-G04 |
| Organization Overlay | MR-G05 |
| Provider Advice Record | MR-G06 |
| AI Output Record | MR-G07 |
| Metric or evaluation evidence | MR-G08–G10 |
| Pack Release Approval | MR-D12 |
| Pilot or release Decision | MR-D13 |
| Deadline Record | MR-E06 |
| Quote and Price Basis | MR-A05–MR-A07 |
| Maintenance Obligation Set | MR-B02 |
| Renewal Package Candidate | MR-A26 |
| Recordal and Transaction records | MR-C07–C09, MR-A27–A28 |

The controlled record identifies Product meaning. It does not grant external authority.

---

## 3. Pack Identity Contract

Every Pack version must declare:

| Field | Required meaning |
| --- | --- |
| Pack ID | stable identity across versions |
| Pack version | immutable released version |
| jurisdiction | country, region, treaty or authority scope |
| official authority | relevant office or authority |
| service family | filing, response, opposition, renewal, recordal or other supported service |
| lifecycle stages | exact supported stages |
| applicant or owner types | covered legal and factual categories |
| route types | direct, regional, international or other route |
| languages | source, official and Product-supported languages |
| effective period | known effective start and end or review condition |
| support state | research, guidance, preparation, execution, lifecycle, suspended or retired |
| exclusions | expressly unsupported matters |
| professional owner | accountable rule owner |
| reviewers | required professional or operational reviewers |
| release approval | MR-D12 reference |
| next review | date or event trigger |

One Pack may contain several service modules, but each module must retain its own state and evidence.

---

## 4. Pack Support States

### 4.1 Research Only

Permitted:

- source collection;
- internal comparison;
- Change Candidate creation;
- professional research.

Not permitted:

- client-facing current-rule claims;
- recommendation reliance;
- package preparation as conforming work;
- protected action.

### 4.2 Guidance Capable

Requires:

- reviewed Source and Rule Records;
- source dates and scope;
- known limitations;
- user-facing explanations;
- professional escalation path;
- relevant guidance scenarios.

Permitted:

- explanation;
- candidate questions;
- source-backed options;
- recommendation assistance.

Not permitted:

- unsupported filing or later-stage package execution.

### 4.3 Preparation Capable

Requires Guidance Capable plus:

- exact Requirement Set;
- document and form rules;
- fee-unit rules;
- package schema;
- Review requirements;
- blocker and override behavior;
- material-diff behavior;
- preparation scenarios.

Permitted:

- controlled package candidates;
- client factual confirmation;
- Professional Review;
- approval request preparation.

Not permitted:

- Execution unless the module is also Execution Capable.

### 4.4 Execution Capable

Requires Preparation Capable plus:

- approved provider, connector or manual route contract;
- Filing Approval or service-specific approval contract;
- idempotency identity;
- submission-evidence contract;
- acknowledgement expectations;
- unknown-state and reconciliation behavior;
- duplicate-safety scenarios;
- operational owner and disable mechanism.

Permitted:

- approved protected action through the declared route.

Execution Capable does not mean every provider or connector route is supported.

### 4.5 Lifecycle Capable

Requires relevant earlier state plus:

- official-event continuation;
- deadlines and responsibility;
- outcome mapping;
- maintenance or later-stage obligations;
- renewal, recordal, dispute or portfolio continuation as declared;
- historical version preservation;
- change monitoring and suspension rules.

A lifecycle-capable new-filing Pack may still exclude opposition, cancellation or transaction services.

### 4.6 Suspended

A module must be suspended when a material condition prevents safe current use, including:

- required source unavailable or stale beyond policy;
- unresolved source conflict;
- fee or form change not yet validated;
- provider or connector route unavailable;
- legal or operational rule uncertainty;
- failed zero-tolerance scenario;
- missing professional ownership;
- incident requiring stop.

Suspension blocks new dependent protected actions. Existing Matters remain visible and require an explicit continuation plan.

### 4.7 Retired

A retired Pack version remains available for historical lineage but may not drive new work.

---

## 5. Source Contract

Every material source must retain:

- source ID;
- issuing authority or author;
- source type;
- title and scope;
- original language;
- official location or immutable retained reference where permitted;
- publication date;
- effective date;
- retrieval date and time;
- version or checksum identity;
- supersession status;
- confidentiality or use restriction;
- reviewer;
- interpretation notes.

Source authority should be classified, for example:

1. legislation, regulation or treaty;
2. official office rule, notice, fee schedule or form;
3. official manual or guidance;
4. official system validation or direct authority confirmation;
5. published decision or authoritative case law where applicable;
6. verified local professional advice;
7. controlled organization experience;
8. secondary commentary;
9. unverified public content.

The hierarchy informs Review. It does not eliminate context-specific professional judgment.

---

## 6. Rule Record Contract

Each material Rule Record must identify:

- rule ID;
- Pack and module;
- human-readable rule statement;
- machine-readable condition where used;
- affected Product stages;
- input fields;
- output, warning, blocker or calculation;
- source links;
- exceptions;
- effective date;
- expiry or review trigger;
- status;
- confidence dimensions;
- professional owner;
- test scenarios;
- change history.

Rule status may be:

- draft;
- under verification;
- active;
- active with limitation;
- disputed;
- temporarily suspended;
- superseded;
- withdrawn;
- unknown after detected change.

Only permitted active states may drive protected Product behavior.

---

## 7. Service-Family Modules

### 7.1 New Filing

Minimum contract:

- applicant and owner eligibility;
- priority and filing-basis rules;
- representation and provider requirements;
- mark types and representation files;
- classification and goods/services practice;
- item, class, character or page-count fee units;
- search options and limitations;
- documents and signatures;
- official forms and declarations;
- filing-package schema;
- filing route;
- acknowledgement identifiers;
- correction and rejection behavior;
- future official stages and later-stage fees.

### 7.2 Examination and Response

Minimum contract:

- official event types and evidence;
- issue categories;
- affected-scope mapping;
- response and amendment routes;
- evidence and declaration rules;
- deadline basis and extensions;
- response-package schema;
- Review and client Decision requirements;
- filing and acknowledgement route;
- appeal or review entry points;
- outcome mapping and Communication.

### 7.3 Publication, Opposition and Adversarial Work

Minimum contract:

- publication evidence;
- observation or opposition windows;
- extensions or cooling-off periods;
- party and standing requirements;
- pleading and evidence stages;
- provider capability and conflict requirements;
- settlement authority;
- cost and fee stages;
- official procedural closure;
- appeal, cancellation or invalidation entry points;
- independent Matter and deadline behavior.

### 7.4 Registration and Maintenance

Minimum contract:

- registration event and scope fields;
- certificate availability and format;
- registration-stage fees;
- use, declaration and evidence duties;
- local-representation continuity;
- maintenance events;
- source-backed deadlines;
- current official owner and address verification;
- Right Baseline update behavior;
- vulnerability and escalation conditions.

### 7.5 Renewal

Minimum contract:

- ordinary, early, grace and restoration windows;
- official deadline basis;
- right, class and scope verification;
- partial renewal and limitation behavior;
- owner, address and representative checks;
- required documents and declarations;
- use or evidence dependencies;
- official, provider and professional fees;
- surcharge logic;
- payment conditions;
- Renewal Package schema;
- Renewal Approval;
- execution and acknowledgement;
- renewed-right evidence and Right Baseline update.

### 7.6 Changes and Recordals

Minimum contract:

- name and address change routes;
- representative appointment, change or revocation;
- correction versus substantive change;
- affected-right scope;
- forms and supporting documents;
- signatures, certification, notarization, legalization and translation;
- sequencing with renewal or dispute work;
- partial official results;
- correction and rejection behavior;
- official recordal evidence.

### 7.7 Assignment, Merger, Succession and Licensing

Minimum contract:

- transaction type;
- parties and authority;
- effective date;
- affected rights and partial scope;
- chain-of-title dependencies;
- contractual document requirements;
- office recordal requirement or optionality;
- license recordal and quality-control considerations where applicable;
- tax or stamp considerations where within supported scope;
- official and professional fees;
- confidentiality and evidence restrictions;
- official recordal evidence;
- contractual effect versus official effect.

### 7.8 Portfolio and Monitoring

Minimum contract:

- supported official and monitoring sources;
- independent-right preservation;
- signal versus official-event distinction;
- deadline and obligation aggregation rules;
- coverage-gap logic;
- evidence and vulnerability indicators;
- service-action candidates;
- non-renewal Decision support;
- no automatic infringement or protected-action conclusion.

---

## 8. Deadline Contract

Every deadline-sensitive module must define:

- triggering official event;
- source hierarchy;
- event date and receipt date distinctions;
- calculation method;
- included and excluded days;
- timezone;
- local holidays or office calendar where applicable;
- statutory, official, calculated, internal and reminder dates;
- extension or grace rules;
- correction behavior;
- responsible reviewer;
- conservative handling when disputed.

A reminder date is not the official deadline.

A provider-reported deadline must not override a conflicting official source without Review.

---

## 9. Form and Document Version Contract

Every material official form or filing schema must retain:

- form ID and version;
- authority;
- service and purpose;
- effective date;
- required fields;
- declarations;
- signature type;
- attachment rules;
- accepted file formats;
- submission route;
- superseded version;
- test evidence.

A detected form change creates a Change Candidate.

Before release, impact assessment must identify:

- open package candidates;
- reviewed packages;
- approved but unexecuted packages;
- provider instructions;
- connector schemas;
- rendered outputs;
- client confirmations;
- re-signature needs.

Historical packages retain their original form version.

---

## 10. Pack Change Workflow

```text
change signal
→ source capture
→ Change Candidate
→ affected-rule and artifact analysis
→ professional verification
→ Rule and Pack revision
→ scenario tests
→ Pack Release Approval
→ release
→ affected-journey revalidation
```

A Pack update must not silently mutate:

- accepted Quote;
- Commercial Instruction;
- Formal Intake;
- reviewed or approved package;
- provider instruction;
- completed submission evidence;
- official outcome;
- historical Right Baseline.

Affected work must be classified as:

- no action required;
- informational update;
- new work only;
- open draft revalidation;
- reviewed package revalidation;
- approval invalidation;
- commercial repricing;
- operational suspension;
- future-obligation update.

---

## 11. Organization Overlay Contract

An Organization Overlay may define:

- internal review level;
- private provider preferences;
- internal deadline buffers;
- templates;
- risk tolerance;
- pricing policy;
- exchange-rate policy;
- discount authority;
- Communication approval;
- local operating language.

It must remain distinguishable from:

- official rule;
- jurisdiction interpretation;
- MarkReg Product default;
- provider-specific requirement;
- client instruction.

An overlay may be stricter than a Pack. It may not silently weaken a mandatory jurisdiction rule.

---

## 12. Provider Advice Contract

Provider advice must retain:

- provider identity;
- professional or organizational capacity;
- date;
- jurisdiction and service scope;
- affected rule or package;
- source basis where provided;
- commercial interest or conflict consideration;
- reviewer disposition;
- expiry or recheck trigger.

Provider advice may evidence current practice. It does not become official truth automatically.

---

## 13. Commercial Component Model

### 13.1 Component Classes

| Component | Meaning | Default visibility |
| --- | --- | --- |
| official fee | fee payable to an official authority | client visible |
| mandatory third-party cost | legalization, courier, translation or other mandatory external cost | client visible or specifically estimated |
| professional fee | organization charge for professional work | client visible |
| provider pass-through | external provider charge passed to client | client visible or summarized under approved policy |
| internal provider cost | procurement cost paid by the organization | organization private |
| tax | applicable tax with inclusive/exclusive treatment | client visible |
| currency adjustment | controlled conversion, spread or buffer charged | client visible when charged |
| contingency | specifically described possible cost | client visible |
| later-stage fee | future examination, publication, registration, response, renewal, recordal or dispute charge | client visible as included, excluded, estimated or unknown |
| discount | approved reduction | client visible; approval evidence private |
| credit or payment term | approved timing concession | client visible; internal risk basis private |
| margin | internal commercial measure | organization private |

No internal cost or margin may be mislabeled as official fee.

### 13.2 Price Basis

Every price component should retain:

- component ID;
- service and stage;
- fee-driving units;
- amount and currency;
- source or policy;
- effective date;
- tax treatment;
- visibility;
- estimation status;
- provider and organization context;
- supersession link.

---

## 14. Service Price Models

### 14.1 New Filing

Fee drivers may include:

- jurisdiction and route;
- filing unit;
- class count;
- goods/services item count;
- applicant type;
- priority claim;
- search or drafting scope;
- document and provider requirements;
- filing and later registration stages.

### 14.2 Examination and Response

Fee drivers may include:

- issue type and count;
- class or item scope;
- amendment complexity;
- evidence and declaration work;
- response route;
- hearing, appeal or extension;
- provider and official fees.

### 14.3 Opposition and Disputes

Fee drivers may include:

- proceeding stage;
- grounds;
- evidence volume;
- pleading rounds;
- hearing or settlement work;
- extension or cooling-off period;
- local counsel and official fees;
- security for costs where applicable and supported.

### 14.4 Registration and Maintenance

Fee drivers may include:

- registration-stage official fee;
- class or item units;
- certificate or document delivery;
- declaration or use evidence;
- local representation continuity;
- monitoring or maintenance service.

### 14.5 Renewal

Fee drivers may include:

- right and class count;
- ordinary, grace or restoration period;
- surcharge;
- owner or address correction;
- evidence or declaration;
- provider cost;
- official fee;
- certificate or updated extract.

### 14.6 Changes and Transactions

Fee drivers may include:

- right count;
- jurisdiction count;
- transaction type;
- party count;
- partial scope;
- document and certification complexity;
- translation or legalization;
- sequencing with renewal or dispute;
- provider and official fee.

A one-price “recordal” label is non-conforming when materially different services or fee units are hidden.

---

## 15. Quote Contract

Every Quote must identify:

- Quote ID and version;
- service family and stage;
- jurisdictions and routes;
- affected filing units, rights, classes, items or parties;
- component amounts and currencies;
- tax-inclusive or tax-exclusive treatment;
- exchange-rate source or organization policy;
- rate timestamp and validity;
- Quote validity and expiry;
- assumptions;
- inclusions and exclusions;
- later-stage fees;
- provider pass-through treatment;
- official-fee and provider-cost variance treatment;
- payment schedule;
- refund and cancellation treatment;
- discount or exception approval;
- prior or superseded Quote;
- required client acceptance scope.

A Quote version is immutable after issue. Changes create a new version.

---

## 16. Visibility and Disclosure Contract

| Information | Client | Professional | Finance | Provider | Organization management |
| --- | --- | --- | --- | --- | --- |
| official fee and source basis | yes | yes | yes | relevant only | yes |
| client professional fee | yes | yes where needed | yes | no by default | yes |
| provider pass-through charged | yes or approved summary | yes | yes | own engagement only | yes |
| internal provider cost | no | only if role permits | yes where needed | own payable only | yes |
| margin | no | no by default | permitted finance roles | no | permitted management roles |
| discount shown to client | yes | relevant scope | yes | no | yes |
| discount approval evidence | no | only if role permits | yes | no | yes |
| exchange-rate policy explanation | yes | yes | yes | relevant only | yes |
| private provider comparison | no | permitted professional roles | cost data only | no | permitted management roles |

Visibility remains field-, purpose- and role-specific.

---

## 17. Exchange-Rate Contract

The organization must define:

- permitted rate sources;
- base and quote currencies;
- spread or buffer policy;
- rounding rule;
- refresh frequency;
- rate timestamp;
- Quote validity relationship;
- repricing threshold;
- gain and loss treatment;
- client-visible explanation;
- accounting authority.

MarkReg may calculate from the policy. It may not invent the policy or hide margin inside official fees.

---

## 18. Discount, Credit and Margin Authority

A discount must identify:

- amount or percentage;
- affected components;
- reason;
- approving role;
- minimum-margin or exception rule;
- expiry or one-time condition;
- affected Quote version.

Credit terms must identify:

- approved limit;
- payment schedule;
- responsible payer;
- expiry;
- suspension conditions;
- approving role.

A client-visible discount must not alter official-fee labels.

---

## 19. Payment Readiness

Payment schedules may include:

- full prepayment;
- deposit plus balance;
- filing-stage and registration-stage payments;
- response or dispute milestones;
- renewal or recordal stage payments;
- recurring portfolio payments;
- approved credit terms.

Commercial readiness must show the exact condition currently required.

```text
payment received
≠ Professional Review
≠ Filing Approval
≠ provider acceptance
≠ official acknowledgement
```

Actual receipts, refunds and accounting remain owned by the authoritative financial service.

---

## 20. Fee, Form and Rule Variance

When a fee, form or rule changes after a commercial or professional artifact is created, MarkReg must determine:

1. which Pack and source version changed;
2. effective date and uncertainty;
3. affected service and stage;
4. affected open artifacts;
5. whether the Quote remains valid;
6. whether accepted terms allocate the variance;
7. whether the change exceeds an approved threshold;
8. whether client re-acceptance is required;
9. whether Professional Review or approval is invalidated;
10. whether payment or refund adjustment is required;
11. whether execution must be suspended;
12. whether completed historical records remain unchanged.

No amount, form or approved package may be silently changed after acceptance or approval.

---

## 21. Refund, Cancellation and Failed Action

Commercial policy must distinguish:

- unperformed professional work;
- completed professional work;
- refundable and non-refundable official fees;
- provider cancellation charges;
- currency differences;
- client-caused delay or invalid instruction;
- organization or provider failure;
- duplicate or rejected payment;
- failed action before and after official receipt;
- partial service completion;
- work superseded by rule or form change;
- portfolio-level prepaid services.

The Product records and explains the applicable policy. It does not create the accounting event.

---

## 22. AI Assistance Contract

AI may assist with:

- source comparison;
- candidate Rule Record extraction;
- missing-field detection;
- fee-unit mapping;
- Pack-version comparison;
- affected-artifact analysis;
- client explanation drafting;
- scenario generation;
- anomaly detection.

Every material AI task must receive:

- purpose;
- jurisdiction and service;
- Pack and Rule versions;
- approved source set;
- organization overlay if permitted;
- confidentiality limits;
- expected output type;
- prohibited conclusions.

Material output retains MR-G07 lineage and Human disposition.

AI may not:

- invent a current rule or fee;
- release a Pack;
- mark a disputed rule active;
- decide an effective date without evidence;
- generalize one provider’s advice;
- alter a Quote or approved package silently;
- grant Review, approval or execution authority;
- claim a Pack supports a stage that has not passed its evidence gate.

---

## 23. Pack-to-Profile Evidence

| Conformance profile | Minimum Pack evidence |
| --- | --- |
| Foundation | authority and source-boundary rules; no service support claim required |
| Guided Decision | Guidance Capable module for each declared jurisdiction/service |
| Commercial Intake | guidance plus current price, Intake, Requirement and commercial-variance rules |
| Filing Preparation | Preparation Capable module with forms, documents, package and Review behavior |
| Governed Filing | Execution Capable module with route, evidence, reconciliation and duplicate safety |
| Post-Filing | service-specific lifecycle module for every declared proceeding type |
| Portfolio Continuity | registration, maintenance, renewal, recordal and transaction modules as declared |
| Full-Lifecycle | all declared modules, Pack change governance, AI controls and applicable scenario evidence |

A Profile may not claim a jurisdiction/service combination above the Pack module’s support state.

---

## 24. Controlled Validation Archetypes

These archetypes validate the contract structure. They are not current law for any real jurisdiction.

### Archetype A — Direct New-Filing Module

Characteristics:

- one official office;
- direct filing;
- class-based official fees;
- local provider required;
- signed POA accepted as scan;
- separate registration-stage fee;
- official acknowledgement returned by provider.

Expected evidence:

- filing Guidance, Preparation and Execution states may be tested;
- registration and renewal support remain undeclared unless separate modules pass;
- Quote discloses filing and later registration stages;
- provider cost and internal margin remain private;
- filing is not presented as acknowledged until official evidence returns.

### Archetype B — Renewal with Ownership Recordal Dependency

Characteristics:

- existing registered right;
- renewal deadline in a grace-sensitive period;
- official owner differs from current business owner;
- recordal may be filed before, with or separately from renewal;
- separate official and provider fees;
- partial official outcomes possible.

Expected evidence:

- current Right Baseline and Deadline Record required;
- renewal and recordal packages remain distinct;
- Renewal Approval and Recordal Approval remain distinct;
- Quote shows ordinary renewal, surcharge and recordal components;
- signed assignment does not prove official owner update;
- one action may proceed only where the active Pack permits the sequencing.

Both archetypes must pass their applicable MR-SCN scenarios before a support claim is made.

---

## 25. Minimum Conformance Scenarios

PF-05 evidence must include, where applicable:

- MR-SCN-03 — route and jurisdiction comparison;
- MR-SCN-04 — classification uncertainty;
- MR-SCN-05 — invalid POA;
- MR-SCN-06 — expired Quote;
- MR-SCN-07 — official-fee change;
- MR-SCN-08 — payment separation;
- MR-SCN-10 — stale official status;
- MR-SCN-12 — official owner conflict;
- MR-SCN-15 — later-stage fee disclosure;
- MR-SCN-26 — deadline-source conflict;
- MR-SCN-30 — registration-scope or certificate conflict;
- MR-SCN-31 — renewal deadline and partial renewal;
- MR-SCN-32 — assignment versus official recordal;
- MR-SCN-37 — current rule without valid Pack;
- MR-SCN-38 — stale fee or source conflict;
- MR-SCN-39 — AI output without source mapping.

A failed applicable zero-tolerance scenario suspends the affected support claim.

---

## 26. Commercial Conformance Tests

A commercial flow conforms only when it demonstrates:

- expired Quote versions cannot be accepted silently;
- fee, form and rule changes trigger impact assessment;
- tax and currency treatment are visible;
- discounts and credit require correct authority;
- internal provider cost and margin remain restricted;
- payment remains separate from Review, approval and official effect;
- later-stage fees are not misleadingly represented as included;
- renewal, recordal and dispute prices retain service-specific fee drivers;
- partial completion and refunds preserve component history;
- historical Quotes and packages retain their original versions.

---

## 27. Release and Suspension Decision

A module may be released only when:

1. Pack identity and scope are complete;
2. sources and material rules are reviewed;
3. forms, fees and deadlines are current enough for the declared state;
4. Product behavior and participant surfaces are defined;
5. commercial visibility and variance rules are defined;
6. applicable scenarios pass;
7. professional and operational owners accept responsibility;
8. MR-D12 records Pack Release Approval;
9. suspension and rollback are possible.

Pack Release Approval does not authorize production deployment or a specific external action.

---

## 28. Failure Modes

The contract fails when:

- a country name is treated as full support;
- one filing Pack is reused for renewal or opposition without evidence;
- historical Quotes or packages are rewritten after a rule change;
- provider advice becomes official truth automatically;
- organization policy is presented as law;
- official fees contain hidden margin;
- client surfaces expose internal cost or provider comparison without authority;
- later-stage fees are omitted or represented as included inaccurately;
- a renewal or recordal price hides material fee drivers;
- a Pack remains active after a material source or route failure;
- AI provides current-rule conclusions without controlled context;
- support state exceeds tested evidence.

---

## 29. PF-05 Decision

```text
Pack identity and exact support states: DEFINED
Service modules through filing, disputes, maintenance, renewal and transactions: DEFINED
Source, Rule, Form and Change contracts: DEFINED
Commercial component and visibility model: DEFINED
Later-stage price models: DEFINED
Fee, form and rule variance behavior: DEFINED
AI assistance boundaries: DEFINED
Profile evidence mapping: DEFINED
Controlled validation archetypes: DEFINED
Appendix F projection required: YES
Appendix G PF-05 evidence reconciliation required: YES
PF-05 Review required: YES
```

This specification remains subordinate to the Books 01–04 Portfolio Baseline and does not authorize unrestricted implementation, production deployment or external protected action.