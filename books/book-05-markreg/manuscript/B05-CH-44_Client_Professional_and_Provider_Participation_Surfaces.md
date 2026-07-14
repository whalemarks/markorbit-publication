# B05-CH-44 — Client, Professional and Provider Participation Surfaces

**Status:** Part VII Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part VII — Product Experience and Evolution

## Chapter Purpose

CH43 defines where MarkReg may appear.

CH44 answers:

> How does MarkReg let clients, professionals, reviewers, approvers, coordinators, finance users and providers participate in one lifecycle without exposing the wrong information or allowing one role to assume another role’s authority?

```text
Same lifecycle
→ role-specific surface
→ purpose-limited information
→ explicit action rights
→ accountable review and communication
```

A simplified screen must not simplify away responsibility.

---

## 1. User Question and Primary Action

**User question:** What may I see, contribute, decide or communicate at this step?

**Primary action:** Complete the role-appropriate action or hand the step to the accountable participant.

Every participation surface must show:

- participant role;
- represented organization or client;
- current purpose;
- visible information scope;
- requested action;
- decision consequence;
- deadline or target date;
- next participant;
- audit and communication effect.

---

## 2. Participant Types

MarkReg commonly serves:

| Participant | Typical responsibility |
| --- | --- |
| client contact | supplies business facts and confirms commercial or factual choices |
| applicant or owner representative | confirms identity, authority and ownership facts |
| professional | gives professional judgment and prepares governed work |
| reviewer | checks quality, law, evidence, scope or risk |
| approver | grants bounded internal or filing authority |
| coordinator | manages information, providers, documents and deadlines |
| account owner | maintains client relationship and commercial continuity |
| finance participant | confirms payment, cost and invoice conditions |
| external provider | accepts bounded engagement and performs agreed work |
| organization administrator | configures roles and policy, not case outcomes |
| AI assistant | assists within visible limits and never becomes an accountable actor |

One person may hold multiple roles, but each action must record the role used.

---

## 3. Surface Contract

Each participant surface should define:

1. purpose;
2. visible objects and fields;
3. editable fields;
4. permitted decisions;
5. prohibited actions;
6. required evidence;
7. communication behavior;
8. expiry and revalidation;
9. next handoff.

The same object may have different views without creating different truths.

---

## 4. Client Surface

The client surface should help a non-specialist make informed decisions without presenting internal complexity as a raw case system.

It may show:

- business objective;
- recommended and alternative jurisdictions;
- filing-unit and class choices;
- goods/services in business language and filing language;
- assumptions and exclusions;
- fee breakdown appropriate for the client;
- required documents and facts;
- status supported by source;
- pending decisions;
- next deadline and consequence;
- reviewed outcome communications.

It should not expose by default:

- internal margin;
- provider ranking notes;
- conflict-search details unrelated to the client decision;
- private organization Knowledge;
- other clients’ examples or evidence;
- internal reviewer comments;
- credential or connector details;
- unreviewed AI reasoning.

### 4.1 Client actions

A client may:

- provide or correct facts;
- upload requested material;
- select among presented options;
- accept a Quote version;
- issue a Commercial Instruction;
- confirm a package version;
- choose a reviewed response or settlement option;
- approve a bounded factual or commercial decision;
- acknowledge an outcome Communication.

A client action does not automatically become Professional Review or Filing Approval.

### 4.2 Client language

The surface should translate technical state into clear consequences.

Example:

```text
Office status: opposition filed and accepted
What this means: the EU application is now in a formal dispute process
What is needed: choose a defense approach and confirm the evidence plan
What it does not mean: the application has already been refused
```

---

## 5. Professional Surface

The professional surface must retain the detail required for accountable judgment.

It may include:

- official source and retrieval evidence;
- jurisdiction-pack version;
- Product artifact lineage;
- issue and scope matrices;
- amendment redlines;
- evidence provenance;
- deadline records;
- provider reports and conflicts;
- comparable options and assumptions;
- AI suggestions with confidence and source;
- review history;
- approval status;
- formal object references.

### 5.1 Professional actions

A professional may:

- validate source and rule applicability;
- amend recommendations;
- create or revise professional strategy;
- reject AI or provider suggestions;
- define evidence needs;
- request client decisions;
- prepare governed packages;
- submit for Review or Filing Approval;
- escalate uncertainty;
- record a professional override with reasons.

Professional authority remains jurisdiction-, organization- and role-dependent.

---

## 6. Reviewer Surface

The reviewer surface focuses on differences, risk and unresolved issues.

It should provide:

- artifact version under Review;
- prior reviewed version;
- material diff;
- source changes;
- unresolved warnings;
- affected jurisdictions and rights;
- proposed external effect;
- reviewer checklist;
- conflict and independence indicators;
- decision options.

Reviewer decisions include:

- approve Review result;
- approve with conditions;
- return for revision;
- escalate;
- decline due to conflict or insufficient authority.

Review does not itself execute or create official effect.

---

## 7. Approver Surface

An approver must see exactly what authority is requested.

The approval request should identify:

- action type;
- artifact version;
- jurisdiction and route;
- affected rights or classes;
- provider or connector route;
- fee and payment condition;
- deadline;
- unresolved risk;
- required conditions;
- expiry;
- consequence of approval.

Approval choices should be explicit:

- approve this version;
- approve with stated conditions;
- reject;
- request changes;
- delegate to an eligible approver;
- abstain due to conflict.

A generic `Approve` button without scope is non-conforming.

---

## 8. Coordinator Surface

The coordinator surface supports operational continuity without converting coordination into professional authority.

It may include:

- missing information;
- document request status;
- provider availability;
- task ownership;
- deadline and internal target;
- client follow-up;
- payment status;
- communication delivery;
- acknowledgement reconciliation;
- escalation path.

A coordinator may route, remind, collect and reconcile.

A coordinator may not make professional strategy, client decision or Filing Approval unless separately authorized in that role.

---

## 9. Finance Surface

The finance surface should show the commercial facts needed for payment and reconciliation.

It may include:

- accepted Quote version;
- official and professional fee components;
- provider payable;
- currency and exchange-rate basis;
- tax treatment;
- discount and approval reference;
- payment requirement;
- received, pending, failed or refunded amount;
- payment-to-action linkage;
- duplicate-payment risk;
- later-stage fees.

Finance users should not need access to unrelated legal evidence or confidential dispute strategy.

Payment confirmation is not filing authority.

---

## 10. Provider Surface

The provider surface is purpose-limited to the accepted engagement.

It may show:

- provider appointment and accepted scope;
- applicant and mark information required for the task;
- approved package or response version;
- relevant documents;
- deadlines and requested confirmation;
- communication channel;
- fee and billing terms appropriate to the engagement;
- required acknowledgement evidence;
- change-request mechanism.

It should not expose:

- internal provider comparisons;
- other providers’ quotes;
- unrelated Matter history;
- internal margin;
- unrelated clients or portfolio rights;
- personal Lite notes;
- organization-wide Knowledge without permission.

### 10.1 Provider actions

A provider may:

- accept or decline the engagement;
- disclose conflict or availability issues;
- request missing information;
- propose a change;
- acknowledge receipt;
- report execution state;
- return official evidence;
- submit invoice or cost evidence;
- communicate a sourced official event.

A provider proposal does not silently modify an approved package.

---

## 11. Visibility Classes

Information may be classified as:

| Visibility class | Typical content |
| --- | --- |
| client visible | decisions, scope, reviewed status and client-facing fees |
| professional restricted | legal analysis, evidence assessment and internal strategy |
| organization private | margin, provider ranking and internal policy |
| provider purpose-limited | accepted engagement inputs and outputs |
| finance restricted | payment, tax, payable and refund information |
| personal local | Lite-only notes and personal learning |
| official-source public | office records subject to source and freshness |
| confidential evidence | restricted evidence requiring purpose and access controls |

Visibility is field- and purpose-specific, not merely page-specific.

---

## 12. Action Rights Matrix

A conforming Product should maintain a configurable rights matrix.

| Action | Client | Professional | Reviewer | Approver | Coordinator | Provider |
| --- | --- | --- | --- | --- | --- | --- |
| provide facts | yes | yes | comment | no | collect | request |
| choose commercial option | yes | advise | review | policy only | coordinate | no |
| create strategy | no | yes | review | no | no | propose only |
| confirm package facts | yes | yes | review | no | coordinate | request change |
| perform Professional Review | no | eligible only | yes | no | no | only if appointed and eligible |
| grant Filing Approval | no | only if authorized | no | yes | no | no |
| execute filing | no | through governed route | no | no | coordinate | if accepted and instructed |
| confirm official outcome | acknowledge | verify | review | no | reconcile | report with evidence |

Actual rights depend on jurisdiction, organization policy and engagement.

---

## 13. Delegation and Representation

Delegation must record:

- delegating actor;
- receiving actor;
- role delegated;
- scope;
- reason;
- start and expiry;
- prohibited subdelegation;
- accepted or declined status;
- audit reference.

Delegation does not transfer professional qualification or client authority that the recipient does not possess.

The Product must not allow silent impersonation.

An administrator may assist with account access but may not act as the client, professional or approver without a recorded role basis.

---

## 14. Multi-Party Decisions

Some decisions require more than one participant.

Examples:

- client confirms commercial scope;
- professional confirms legal strategy;
- finance confirms payment condition;
- approver grants Filing Approval;
- provider accepts engagement.

MarkReg should show a decision chain rather than one aggregated `approved` state.

```text
Client confirmed
+ Professional Review complete
+ Payment condition satisfied
+ Filing Approval active
+ Provider accepted
≠ Official filing completed
```

---

## 15. Communication Surfaces

A Communication surface should distinguish:

- draft;
- reviewed draft;
- approved Communication;
- sent;
- delivered;
- failed;
- acknowledged;
- corrected or superseded.

Recipients, purpose, language, attachments, source references and confidentiality must be visible before send.

Role-specific templates may assist but may not replace Review where required.

---

## 16. Consent and Purpose Change

When information was collected for one purpose, reuse for another purpose may require:

- a new permission basis;
- client notice;
- professional Review;
- redaction;
- provider restriction;
- new retention policy.

Example:

Use evidence collected for a US declaration should not automatically be disclosed in an EU opposition without a new purpose and evidence decision.

---

## 17. EMBERLOOP Participation Views

For `EMBERLOOP`:

- the client sees three country outcomes, decisions and client-facing costs;
- the US professional sees examination issues, evidence and response history;
- the EU dispute professional sees opposition pleadings and settlement authority;
- the UK maintenance coordinator sees Right Baseline and future obligations;
- finance sees accepted commercial terms and payment status;
- each provider sees only its accepted jurisdiction engagement;
- organization management sees portfolio-level progress and risk without unrestricted evidence access.

No participant receives a false single global status.

---

## 18. RIVERKITE Participation Views

For `RIVERKITE`:

- the client executive sees portfolio decisions and consequences;
- the ownership specialist sees transaction documents and chain-of-title gaps;
- the renewal coordinator sees renewal deadlines and package readiness;
- the cancellation-defense professional sees evidence and proceeding scope;
- the license reviewer sees license terms and quality-control obligations;
- providers see only the affected registrations and accepted tasks.

The six rights remain independent even when displayed in one portfolio surface.

---

## 19. Conformance Scenarios

### Scenario A — client attempts professional approval

**Given** a client confirms a response strategy  
**When** the response requires Professional Review and Filing Approval  
**Then** MarkReg records the client decision  
**And** does not mark either professional gate complete.

### Scenario B — provider requests broader portfolio access

**Given** a provider is appointed for one EU opposition  
**When** it requests access to unrelated US and UK matters  
**Then** access is denied unless a new purpose and engagement are approved.

### Scenario C — coordinator changes legal strategy

**Given** a coordinator identifies a missing argument  
**When** the coordinator edits the strategy  
**Then** the edit is captured as a suggestion  
**And** an eligible professional must adopt or reject it.

### Scenario D — delegated approver expires

**Given** approval authority was delegated for seven days  
**When** the delegate opens the request after expiry  
**Then** the Product blocks approval  
**And** routes the request to an eligible approver.

### Scenario E — corrected client communication

**Given** a client received a status message with the wrong class scope  
**When** the error is discovered  
**Then** MarkReg issues a linked correction Communication  
**And** preserves the original delivery history.

---

## 20. AI Assistance

AI may assist with:

- adapting explanations to participant role;
- summarizing the information visible to that role;
- detecting excessive disclosure;
- identifying missing decision participants;
- drafting purpose-limited Communications;
- comparing role-specific views for inconsistency;
- suggesting escalation.

AI may not:

- assume another participant’s identity;
- infer client consent from silence;
- grant access;
- perform Professional Review;
- grant approval;
- accept provider engagement;
- send protected Communications without authority;
- expose hidden reasoning or restricted data.

---

## 21. Failure Modes

MarkReg fails this chapter if:

- every participant sees the same unrestricted screen;
- client confirmation is treated as professional approval;
- administrators can impersonate accountable participants silently;
- provider access is organization-wide by default;
- finance requires access to dispute evidence;
- delegation has no scope or expiry;
- one aggregated approval hides incomplete gates;
- corrected Communications overwrite history;
- evidence is reused for a new purpose without control.

---

## 22. Minimum Product Lock

A conforming MarkReg edition must provide:

1. role- and purpose-specific surfaces;
2. visible represented organization and role;
3. field-level visibility classes;
4. configurable action-right matrices;
5. separate client, professional, reviewer, approver, coordinator, finance and provider actions;
6. scoped delegation with expiry;
7. multi-party decision chains;
8. governed Communication states;
9. purpose-change controls;
10. observable access and authority scenarios.

---

## 23. Next Handoff

CH44 defines who may participate and how authority remains visible.

CH45 defines the source-backed jurisdiction rules and AI controls that inform those participants.