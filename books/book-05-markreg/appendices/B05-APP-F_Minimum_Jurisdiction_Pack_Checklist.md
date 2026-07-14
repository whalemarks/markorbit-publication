# Appendix F — Minimum Jurisdiction Pack Checklist

**Status:** Controlled Reader Draft — PF-05 Reconciled  
**Primary sources:** B05-SPEC-0004 v0.2, CH09–CH21, CH30–CH45  
**Reader purpose:** determine whether a jurisdiction, service and lifecycle stage is genuinely supported, what level of support exists, and what evidence is still missing.

## F.1 Support Rule

A country name, office link, fee table or provider profile does not constitute support.

```text
supported jurisdiction/service/stage
= scoped Pack module
+ reviewed sources and rules
+ professional owner
+ tested Product behavior
+ commercial controls
+ maintenance and suspension process
```

Support must be stated at the service-module level.

Examples:

- `Jurisdiction X — new filing — Preparation Capable`;
- `Jurisdiction X — renewal — Guidance Capable only`;
- `Jurisdiction X — opposition — unsupported`;
- `Jurisdiction Y — recordal — Suspended pending form verification`.

---

## F.2 Pack Identity Checklist

- [ ] stable Pack ID;
- [ ] immutable Pack version;
- [ ] jurisdiction or regional authority;
- [ ] official office or authority;
- [ ] exact service family;
- [ ] lifecycle stages covered;
- [ ] applicant or owner types;
- [ ] filing or action routes;
- [ ] source, official and Product languages;
- [ ] effective period;
- [ ] support state;
- [ ] exclusions and known gaps;
- [ ] professional owner;
- [ ] required reviewers;
- [ ] Pack Release Approval reference;
- [ ] release date and next-review trigger.

A Pack with several service modules must state each module independently.

---

## F.3 Support-State Checklist

### Research Only

- [ ] sources may be collected internally;
- [ ] no client-facing current-rule claim;
- [ ] no conforming recommendation or package claim;
- [ ] no protected action.

### Guidance Capable

- [ ] reviewed source and rule records;
- [ ] effective and retrieval dates;
- [ ] user-facing explanations;
- [ ] limitations and uncertainty visible;
- [ ] professional escalation path;
- [ ] applicable guidance scenarios pass.

### Preparation Capable

- [ ] all Guidance Capable requirements;
- [ ] Requirement Set;
- [ ] document and form rules;
- [ ] fee-driving units;
- [ ] package schema;
- [ ] Review and blocker behavior;
- [ ] material-diff behavior;
- [ ] preparation scenarios pass.

### Execution Capable

- [ ] all Preparation Capable requirements;
- [ ] supported provider, connector or manual route;
- [ ] approval contract;
- [ ] stable idempotency identity;
- [ ] submission and acknowledgement evidence;
- [ ] unknown-state and reconciliation behavior;
- [ ] duplicate-safety scenarios;
- [ ] operational owner and disable mechanism.

### Lifecycle Capable

- [ ] official-event continuation;
- [ ] deadlines and responsibility;
- [ ] outcome mapping;
- [ ] maintenance or later-stage obligations;
- [ ] declared renewal, recordal, dispute or portfolio continuation;
- [ ] historical version retention;
- [ ] source-change and suspension process.

### Suspended or Retired

- [ ] suspension or retirement reason;
- [ ] affected services and stages;
- [ ] open-Matter continuation plan;
- [ ] new-action restriction;
- [ ] historical version retained;
- [ ] reactivation or replacement condition.

---

## F.4 Source Checklist

- [ ] current legislation, regulation or treaty basis identified where material;
- [ ] official office rules and practice guidance identified;
- [ ] current official fee source captured;
- [ ] current forms and filing requirements captured;
- [ ] official deadlines and window rules sourced;
- [ ] source language and translation limitations recorded;
- [ ] publication, effective and retrieval dates recorded;
- [ ] source version or checksum retained;
- [ ] superseded source retained;
- [ ] provider advice distinguished from official source;
- [ ] organization experience distinguished from jurisdiction rule;
- [ ] unresolved source conflict visible;
- [ ] confidentiality or source-use restrictions recorded.

---

## F.5 Rule Record Checklist

- [ ] stable Rule ID;
- [ ] human-readable statement;
- [ ] machine-readable condition where used;
- [ ] affected Product stages;
- [ ] input fields;
- [ ] warning, blocker, calculation or output;
- [ ] source references;
- [ ] exceptions;
- [ ] effective date;
- [ ] review or expiry trigger;
- [ ] active, limited, disputed, suspended or superseded status;
- [ ] confidence dimensions;
- [ ] professional owner;
- [ ] test scenarios;
- [ ] change history.

Only permitted active states may drive protected action.

---

## F.6 New Filing Checklist

- [ ] applicant eligibility and identity fields;
- [ ] owner, priority and signatory requirements;
- [ ] direct, regional or international routes;
- [ ] local-representation requirement;
- [ ] mark types and representation files;
- [ ] classification edition and local deviations;
- [ ] goods/services wording practice;
- [ ] item, class, character or page-count fee units;
- [ ] search options and limitations;
- [ ] official and professional fee components;
- [ ] POA, signature, original, notarization, legalization and translation;
- [ ] form and filing-package schema;
- [ ] provider or connector route;
- [ ] acknowledgement evidence and identifiers;
- [ ] correction and rejection behavior;
- [ ] registration-stage and later-stage fees.

---

## F.7 Examination and Response Checklist

- [ ] official event types and evidence;
- [ ] issue categories and affected scope;
- [ ] response and amendment options;
- [ ] evidence and declaration requirements;
- [ ] official deadline basis and extensions;
- [ ] provider or representative requirements;
- [ ] response-package schema;
- [ ] Professional Review and client Decision requirements;
- [ ] filing and acknowledgement route;
- [ ] appeal or review entry points;
- [ ] stage-specific fees;
- [ ] Outcome Snapshot and Communication mapping.

---

## F.8 Publication and Dispute Checklist

- [ ] publication evidence;
- [ ] observation or opposition window;
- [ ] extensions or cooling-off periods;
- [ ] party and standing requirements;
- [ ] pleading and evidence stages;
- [ ] hearing and settlement routes;
- [ ] settlement authority;
- [ ] provider capability and conflict rules;
- [ ] official, provider and professional fee stages;
- [ ] appeal, cancellation or invalidation routes;
- [ ] official closure evidence;
- [ ] independent Matter and deadline behavior.

---

## F.9 Registration and Maintenance Checklist

- [ ] registration event and registered scope;
- [ ] approved-versus-registered scope comparison;
- [ ] certificate availability and format;
- [ ] certificate-versus-current-register rule;
- [ ] registration-stage fees;
- [ ] use, declaration or evidence duties;
- [ ] local-representation continuity;
- [ ] maintenance events;
- [ ] official, calculated, internal and reminder dates;
- [ ] current official owner and address verification;
- [ ] Right Baseline update behavior;
- [ ] vulnerability and escalation conditions.

---

## F.10 Renewal Checklist

- [ ] ordinary renewal window;
- [ ] early renewal availability;
- [ ] grace and restoration periods;
- [ ] official deadline source;
- [ ] right, class and scope verification;
- [ ] partial renewal or limitation;
- [ ] current owner, address and representative checks;
- [ ] use, declaration or evidence dependencies;
- [ ] required documents and signatures;
- [ ] ordinary, surcharge and restoration fees;
- [ ] provider and professional fees;
- [ ] Renewal Package schema;
- [ ] Renewal Approval;
- [ ] payment and execution route;
- [ ] official acknowledgement;
- [ ] renewed-right evidence and Right Baseline update.

---

## F.11 Changes and Recordals Checklist

- [ ] name and address changes;
- [ ] representative appointment, change or revocation;
- [ ] correction versus substantive change;
- [ ] affected-right scope;
- [ ] forms and supporting documents;
- [ ] signatures and authority;
- [ ] certification, notarization, legalization and translation;
- [ ] sequencing with renewal or dispute;
- [ ] partial official results;
- [ ] correction and rejection behavior;
- [ ] official, provider and professional fees;
- [ ] official recordal evidence.

---

## F.12 Assignment, Merger, Succession and Licensing Checklist

- [ ] transaction type;
- [ ] parties and authority;
- [ ] effective date;
- [ ] affected rights and partial scope;
- [ ] chain-of-title dependencies;
- [ ] contractual documents;
- [ ] office recordal requirement or optionality;
- [ ] licence recordal where applicable;
- [ ] quality-control or use conditions where within scope;
- [ ] tax, stamp or other mandatory costs where supported;
- [ ] confidentiality and evidence restrictions;
- [ ] official and professional fees;
- [ ] contractual effect separated from official effect;
- [ ] official recordal evidence.

---

## F.13 Portfolio and Monitoring Checklist

- [ ] supported official and monitoring sources;
- [ ] independent-right preservation;
- [ ] signal versus official-event distinction;
- [ ] deadline and obligation aggregation;
- [ ] coverage-gap logic;
- [ ] evidence and vulnerability indicators;
- [ ] action-candidate logic;
- [ ] non-renewal Decision support;
- [ ] no automatic infringement conclusion;
- [ ] no protected action from monitoring signal alone.

---

## F.14 Deadline Checklist

- [ ] triggering official event;
- [ ] source hierarchy;
- [ ] event date and receipt date distinctions;
- [ ] calculation method;
- [ ] included and excluded days;
- [ ] timezone;
- [ ] office calendar and holidays where applicable;
- [ ] extension, grace and restoration rules;
- [ ] official, calculated, internal and reminder dates;
- [ ] correction behavior;
- [ ] responsible reviewer;
- [ ] conservative handling of disputes.

A reminder date must never be displayed as the official deadline.

---

## F.15 Form and Document Version Checklist

- [ ] form or schema ID;
- [ ] version;
- [ ] authority and purpose;
- [ ] effective date;
- [ ] required fields and declarations;
- [ ] signature type;
- [ ] attachment rules;
- [ ] file formats;
- [ ] submission route;
- [ ] superseded version;
- [ ] test evidence;
- [ ] affected open package discovery;
- [ ] re-signature or re-confirmation rule;
- [ ] historical version retained.

---

## F.16 Commercial Component Checklist

- [ ] official fee identified separately;
- [ ] mandatory third-party cost identified;
- [ ] professional fee identified;
- [ ] provider pass-through treatment identified;
- [ ] internal provider cost restricted;
- [ ] tax treatment;
- [ ] currency and exchange-rate policy;
- [ ] later-stage and optional fees;
- [ ] contingency described;
- [ ] discounts and credit authority;
- [ ] margin restricted;
- [ ] component effective dates;
- [ ] component visibility;
- [ ] source or policy lineage.

No internal cost or margin may be labeled as official fee.

---

## F.17 Service Price Checklist

### New filing

- [ ] route, filing unit, class, item and applicant drivers;
- [ ] search and drafting scope;
- [ ] document and provider requirements;
- [ ] registration-stage and later-stage fees.

### Examination and dispute

- [ ] issue or proceeding stage;
- [ ] amendment and evidence complexity;
- [ ] hearing, extension or appeal;
- [ ] provider and official fees.

### Renewal

- [ ] right and class count;
- [ ] ordinary, grace or restoration period;
- [ ] surcharge;
- [ ] owner correction or evidence dependency;
- [ ] updated extract or certificate.

### Recordal and transaction

- [ ] right and jurisdiction count;
- [ ] transaction type and party count;
- [ ] partial scope;
- [ ] document, certification and translation complexity;
- [ ] sequencing with other work;
- [ ] provider and official fees.

---

## F.18 Quote Checklist

- [ ] Quote ID and immutable version;
- [ ] exact service and stage;
- [ ] jurisdictions and routes;
- [ ] affected filing units, rights, classes, items or parties;
- [ ] component amounts and currencies;
- [ ] tax treatment;
- [ ] exchange-rate source and timestamp;
- [ ] validity and expiry;
- [ ] assumptions;
- [ ] inclusions and exclusions;
- [ ] later-stage fees;
- [ ] provider pass-through policy;
- [ ] official-fee and provider-cost variance rule;
- [ ] payment schedule;
- [ ] refund and cancellation rule;
- [ ] discount or exception approval;
- [ ] superseded Quote reference;
- [ ] exact client acceptance scope.

A changed Quote must become a new version.

---

## F.19 Visibility Checklist

- [ ] official fee visible to client;
- [ ] professional fee visible to client;
- [ ] tax and charged currency adjustment visible;
- [ ] later-stage fee inclusion or exclusion visible;
- [ ] provider pass-through visible or summarized under approved policy;
- [ ] internal provider cost hidden from unauthorized client roles;
- [ ] margin hidden from client and provider;
- [ ] discount approval evidence restricted;
- [ ] provider comparison restricted;
- [ ] finance does not require unrelated legal evidence.

---

## F.20 Fee, Form and Rule Change Checklist

- [ ] changed Pack and source version identified;
- [ ] effective date verified or uncertainty recorded;
- [ ] affected services and stages identified;
- [ ] affected Quotes and packages identified;
- [ ] accepted-term variance rule applied;
- [ ] repricing threshold checked;
- [ ] client re-acceptance determined;
- [ ] Review or approval invalidation determined;
- [ ] payment or refund adjustment determined;
- [ ] execution suspension determined;
- [ ] historical records left unchanged;
- [ ] affected users and owners notified appropriately.

---

## F.21 AI Governance Checklist

- [ ] AI task purpose defined;
- [ ] jurisdiction and service defined;
- [ ] Pack and Rule versions supplied;
- [ ] approved source set supplied;
- [ ] Organization Overlay scope controlled;
- [ ] confidentiality restrictions supplied;
- [ ] prohibited conclusions defined;
- [ ] material output retained as MR-G07;
- [ ] source mapping present;
- [ ] Human Review disposition present;
- [ ] AI cannot release Pack or activate disputed rule;
- [ ] AI cannot alter Quote or package silently.

---

## F.22 Pack-to-Profile Checklist

| Profile | Minimum Pack state or evidence |
| --- | --- |
| Foundation | source and authority boundaries only |
| Guided Decision | Guidance Capable for every declared jurisdiction/service |
| Commercial Intake | current pricing, Intake, Requirement and variance rules |
| Filing Preparation | Preparation Capable with forms, packages and Review behavior |
| Governed Filing | Execution Capable with route, evidence, reconciliation and duplicate safety |
| Post-Filing | service-specific lifecycle module for each declared proceeding |
| Portfolio Continuity | declared registration, maintenance, renewal, recordal and transaction modules |
| Full-Lifecycle | all declared modules plus change, AI and scenario governance |

A Profile cannot exceed the support state of its Pack modules.

---

## F.23 Controlled Validation Archetypes

These are structure tests, not current law.

### Archetype A — Direct New Filing

Expected proof:

- new-filing module reaches declared Guidance, Preparation or Execution state;
- class-based fees and local-provider requirement are represented;
- filing and later registration fees are separated;
- provider cost and margin remain private;
- official acknowledgement requires evidence;
- renewal and dispute support are not implied.

### Archetype B — Renewal with Ownership Recordal Dependency

Expected proof:

- current Right Baseline and Deadline Record exist;
- renewal and recordal packages remain separate;
- Renewal Approval and Recordal Approval remain separate;
- ordinary, surcharge and recordal fees are visible;
- signed assignment does not prove official owner update;
- sequencing follows the active Pack module;
- partial official outcomes are supported.

---

## F.24 Minimum Scenario Evidence

At minimum, applicable modules should test:

- MR-SCN-03–08;
- MR-SCN-10 and 12;
- MR-SCN-15;
- MR-SCN-26;
- MR-SCN-30–32;
- MR-SCN-37–39.

A failed applicable zero-tolerance scenario suspends the affected support claim.

---

## F.25 Readiness Decision

| State | Reader meaning |
| --- | --- |
| research only | information collection only |
| guidance capable | sourced explanation and candidate guidance |
| preparation capable | reviewed packages may be prepared |
| execution capable | declared approved route may execute |
| lifecycle capable | declared later stages are maintained |
| suspended | current use blocked by a material issue |
| retired | historical lineage only |

The declaration must be service- and stage-specific.

---

## F.26 Reconciliation Status

```text
B05-SPEC-0004 v0.2 alignment: COMPLETE
Exact Pack identity and support states: COMPLETE
New filing through portfolio service modules: COMPLETE
Later-stage commercial model: COMPLETE
Fee, form and rule change behavior: COMPLETE
AI governance: COMPLETE
Pack-to-Profile mapping: COMPLETE
Controlled validation archetypes: COMPLETE
PF-05 Appendix F work: COMPLETE
PF-06 native-English and compression edit: PENDING
PF-07 figure and reader integration: PENDING
PF-08 structural and scenario validation: PENDING
```

Appendix F is a controlled reader projection. B05-SPEC-0004 v0.2 governs if a conflict exists.