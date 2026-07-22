# Chapter 20 — Failure and Recovery Are Core Product Paths

Professional services do not fail only when a final filing is rejected.

They can fail when:

- a Provider stops responding;
- a customer never receives a deadline message;
- an original document is lost;
- a fee changes after approval;
- a payment is deducted but not reconciled;
- an office portal times out;
- a filing may have been submitted twice;
- a certificate contains the wrong owner;
- a translation is rejected;
- an AI-generated public page becomes stale;
- a conversion route sends the wrong user into the wrong service;
- responsibility remains hidden in one employee's inbox.

A Product that models only the successful path forces real failures into email, spreadsheets and memory.

MarkReg should make failure and recovery part of the ordinary architecture.

```text
Failure signal
→ containment
→ source and impact verification
→ responsibility assignment
→ customer and professional communication
→ recovery options
→ approval and authorized action
→ evidence-backed resolution
→ learning and prevention
```

## 1. Failure is a typed state, not a red label

A generic status such as `Problem` is not enough.

An Exception record should preserve:

- exception type;
- source and detection time;
- affected Customer, Order, Matter, Work Package, Package, Provider or public content;
- known and Unknown facts;
- deadline and financial exposure;
- rights and jurisdictions affected;
- current containment;
- accountable Recovery Owner;
- professional and commercial responsibility;
- customer communication need;
- recovery options;
- approval requirements;
- evidence required for closure;
- prevention candidate.

## 2. Failure classes should remain distinct

MarkReg may encounter several broad classes.

### Source and status failure

- stale official data;
- conflicting sources;
- Provider statement without evidence;
- incorrect Product projection;
- certificate and register mismatch.

### Identity and authority failure

- wrong applicant;
- incorrect owner;
- signatory lacks authority;
- expired POA;
- wrong Provider or representative;
- contributor acts outside scope.

### Document and evidence failure

- missing page;
- illegible scan;
- rejected POA;
- invalid legalization;
- insufficient specimen;
- wrong translation;
- lost original.

### Deadline failure

- miscalculated date;
- missed reminder;
- customer delay;
- Provider delay;
- courier delay;
- grace period misunderstood;
- no verified recovery route.

### Execution failure

- connector timeout;
- portal error;
- duplicate submission risk;
- wrong Package version used;
- Provider did not accept;
- fee not paid;
- official acknowledgement missing.

### Commercial failure

- payment failed;
- currency shortfall;
- unexpected official fee;
- customer disputes scope;
- Provider requests prepayment;
- refund or cancellation conflict.

### Communication failure

- message sent to wrong person;
- material risk omitted;
- translation misunderstood;
- correction not propagated;
- white-label responsibility confused;
- Provider bypasses the Relationship Owner.

### Growth and content failure

- stale fee or deadline page;
- misleading SEO title;
- GEO answer drops an exception;
- CTA implies a guarantee;
- intent model routes a renewal need into a new filing;
- duplicate or low-quality lead outreach;
- content correction does not reach derivative pages.

These categories may intersect, but they should not be collapsed into one root cause before verification.

## 3. Detection should not depend on confession

Failure signals may come from:

- official source change;
- deterministic validation;
- Provider Return gap;
- customer complaint;
- missed acknowledgement threshold;
- payment reconciliation;
- duplicate identifier;
- review finding;
- contributor report;
- public-page monitoring;
- AI discrepancy detection;
- audit sampling;
- delivery comparison.

A professional system should make it safe for internal staff, contributors and Providers to report a possible failure before blame is assigned.

```text
Failure Signal
≠ Proven Fault
```

## 4. Containment comes before optimistic status updates

Immediate containment may include:

- pause external action;
- prevent duplicate retry;
- freeze the affected Package version;
- stop public distribution;
- revoke inappropriate access;
- preserve email, logs and files;
- identify approaching deadlines;
- notify the Delivery Owner;
- create a conservative internal target;
- suspend an unreliable route.

Containment should minimize additional harm while the facts remain uncertain.

## 5. Unknown external effect needs reconciliation

One of the most dangerous states is:

> We do not know whether the action took effect.

Examples include:

- portal timed out after payment;
- Provider says filed but provides no receipt;
- courier delivered but office intake is unknown;
- recordal submitted but not visible;
- payment left the account but Provider says unpaid.

The Product should use:

```text
Attempt evidence
+ external identifiers
+ payment and communication evidence
+ official or Provider verification
→ reconciled result
```

```text
Unknown Submission State
≠ Safe to Retry
```

Retry may create duplicate filings, duplicate fees or conflicting records.

## 6. Provider silence is a governed exception

A Provider workflow should define:

```text
Instruction Sent
→ Acknowledgement Due
→ Acceptance Due
→ Action Due
→ Return Due
```

Silence should trigger staged action:

- automated reminder;
- human follow-up;
- alternate contact;
- internal escalation;
- deadline-risk review;
- replacement-route assessment;
- customer update;
- fund and document recovery.

Provider replacement should not be automatic where the first Provider may already have acted.

## 7. Rejected documents require a recovery context

When an office or Provider rejects a document, MarkReg should preserve:

- rejecting authority;
- exact reason;
- source notice;
- affected action and deadline;
- document version;
- whether the defect was customer, Provider, system or rule-related;
- correction options;
- additional formality;
- cost and courier requirement;
- who must act;
- prevention lesson.

```text
Corrected Document
≠ Rejection History Erased
```

The rejection may affect Capability evidence, checklist design and future Intake questions.

## 8. Missed action does not automatically mean abandonment

When an action may have been missed, the Product should not immediately promise recovery or declare the right lost.

```text
Verify official state
→ preserve evidence
→ identify ordinary, late, restoration and re-filing routes
→ obtain qualified opinion where required
→ compare cost, rights and timing
→ present customer choices
→ record instruction and approval
→ execute and monitor
```

Possible conclusions include:

```text
Action still timely
Late route available
Restoration or petition available
Belated document filing available
Re-filing is the safer route
No viable recovery identified
Professional opinion required
```

## 9. Customer delay and service responsibility must be separated

A deadline may be missed because:

- the customer did not provide evidence;
- the Workplace sent an unclear request;
- the reminder was late;
- the Provider failed to act;
- the official system was unavailable;
- responsibility was never assigned;
- several causes combined.

The incident record should preserve contribution to the failure without using blame as a substitute for recovery.

Customer responsibility does not erase a service provider's duty to communicate clearly and escalate where the Engagement requires it.

## 10. Payment failure is not professional unreadiness

A Matter may be:

```text
Professionally Ready but Commercially Blocked
Commercially Paid but Professionally Not Ready
Provider Prepayment Pending
Official Fee Payment Failed
Payment Deducted but Unreconciled
Refund Review Required
```

The Product should not show a filing as ready merely because money was received.

Likewise, professional preparation should not silently continue into unapproved external cost.

```text
Payment Received
≠ Filing Approved

Work Prepared
≠ Additional Fee Approved
```

## 11. Fee and scope changes require amendment

An exception may change:

- official fee;
- Provider fee;
- currency;
- required document;
- number of classes;
- recovery route;
- timeline;
- professional scope.

The Product should create a visible amendment containing:

- cause;
- source;
- changed amount or scope;
- prior and new versions;
- deadline impact;
- available alternatives;
- customer and professional approvals.

A Provider cannot silently expand the customer's accepted service merely because an office raises a new issue.

## 12. Duplicate and conflicting instructions need authority resolution

The same request may appear through:

- customer email;
- Lite Handoff;
- staff note;
- online form;
- Provider message;
- duplicate Order;
- old instruction sheet.

The system should compare:

- actor;
- represented authority;
- Matter and Package;
- version;
- timestamp;
- intended action;
- prior execution state;
- idempotency key.

```text
Latest Message
≠ Automatically Controlling Instruction
```

A later message from an unauthorized person should not override an approved instruction.

## 13. Incorrect official or Product status needs correction propagation

A wrong status may have already affected:

- customer dashboard;
- internal deadline plan;
- invoice or quote;
- maintenance reminder;
- public content;
- transaction due diligence;
- Portfolio view;
- AI recommendation.

Correction requires:

```text
Correct source
→ identify affected projections and decisions
→ assess harm and deadline
→ update formal state through Owning Service
→ correct customer and public views
→ notify responsible parties
→ preserve old and corrected versions
```

Editing one screen is not a complete recovery.

## 14. Growth and conversion failures require the same discipline

A public content incident may include:

- outdated official fee;
- incorrect POA requirement;
- wrong maintenance window;
- claim that registration is guaranteed;
- content page still indexed after withdrawal;
- chatbot creates an unsuitable recommendation;
- conversion form treats interest as instruction;
- marketing automation contacts a partner-owned customer directly.

Recovery may require:

- unpublish or add warning;
- disable affected CTA;
- stop campaign or outreach;
- identify derivative pages and answer blocks;
- correct source and Claim Ledger;
- notify users who relied on the claim where feasible;
- re-review open Quotes and Intakes;
- preserve incident evidence;
- change the test or release gate.

```text
Marketing Error
≠ Lower-consequence Error by Default
```

A public false deadline may affect many users before any Matter exists.

## 15. Severity should reflect harm and spread

Severity may consider:

- right or deadline consequence;
- reversibility;
- number of affected customers or pages;
- confidential-data exposure;
- financial exposure;
- official-state impact;
- professional-responsibility implications;
- time to contain;
- likelihood of recurrence.

A small internal formatting error and a public incorrect legal deadline should not follow the same incident path.

## 16. Recovery authority remains explicit

The Recovery Owner coordinates the incident but may not possess every authority required.

Recovery may require:

- customer Decision;
- professional opinion;
- Provider acceptance;
- commercial amendment;
- refund approval;
- privacy or security response;
- official correction filing;
- public-content approval.

```text
Recovery Owner
≠ Unlimited Authority
```

## 17. Customer communication during failure must be honest

A responsible incident update should explain:

- what happened or may have happened;
- what is verified;
- what remains Unknown;
- immediate containment;
- rights, cost and deadline exposure;
- available options;
- next accountable actor;
- time of next update.

The Product should avoid:

- false certainty;
- premature blame;
- unexplained silence;
- optimistic completion labels;
- promises of recovery before professional verification.

## 18. Recovery completion needs evidence

An incident should not close because someone says it is fixed.

Closure criteria may include:

- official or external result validated;
- customer informed;
- financial adjustment completed;
- document replaced;
- public content corrected or de-indexing initiated;
- duplicate risk resolved;
- affected Decisions revalidated;
- responsibility and prevention actions recorded;
- remaining limitation accepted.

```text
Workaround Applied
≠ Incident Fully Resolved
```

## 19. Post-incident learning must remain contextual

A completed incident may improve:

- Requirement Sets;
- checklists;
- Work Package design;
- Capability definitions;
- Provider routing;
- review depth;
- communication templates;
- public-content refresh rules;
- conversion tests;
- fallback routes.

But one incident should not automatically become canonical policy.

```text
Incident Correlation
≠ General Rule
```

Learning needs review, provenance and scope.

## 20. Failure should affect routing and authorization

Repeated incidents may trigger:

- higher review rate;
- narrower Production Authorization;
- Provider probation;
- reduced task complexity;
- mandatory refresher learning;
- suspended public publishing;
- additional source validation;
- replacement of a connector or route.

The affected person or Provider should have access to the relevant evidence and a fair correction or appeal process.

## 21. Resilience requires fallback routes

A mature Product may prepare alternatives for:

- Provider unavailability;
- official portal outage;
- payment route failure;
- original-document courier delay;
- translation capacity shortage;
- reviewer bottleneck;
- public-content source outage;
- AI service failure.

Fallback routes still require eligibility, authority and evidence. A backup should not become an unreviewed shortcut.

## 22. Product implications

MarkReg requires:

- typed Exception records;
- detection signals;
- containment controls;
- Unknown-state reconciliation;
- Provider-silence thresholds;
- rejected-document recovery;
- missed-action route comparison;
- payment and amendment handling;
- duplicate-instruction resolution;
- correction propagation;
- growth and content incident response;
- severity and Recovery Owner;
- evidence-backed closure;
- post-incident learning and routing impact;
- governed fallback routes.

## 23. Commercial implications

Recovery capability supports:

- credible lifecycle service;
- premium monitoring;
- Provider replacement policies;
- service guarantees with bounded terms;
- lower complaint and refund cost;
- stronger partner trust;
- better retention.

The Product should not promise that every error or missed deadline can be cured. Commercial terms should distinguish:

- prevention duty;
- response standard;
- included recovery work;
- additional official or professional fees;
- refund and remediation conditions;
- events outside reasonable control.

## 24. Operating principle

```text
Detect early
Contain before guessing
Preserve evidence
Assign responsibility
Verify external effect
Explain Unknowns
Compare recovery routes
Obtain authority
Correct every affected projection
Close with evidence
Learn without overgeneralizing
```

> Failure is not an edge case outside MarkReg. The ability to stop harm, recover responsibly and explain what happened is part of the Product's core promise.