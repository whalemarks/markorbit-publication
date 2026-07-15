# B06-SPEC-0004 — Handoff, Work-Product, MVP and Historical Reconciliation

## 1. Identity

```text
Specification: B06-SPEC-0004
Version: v0.1
Status: Candidate — accepted as Product Baseline on owner merge
Scope: Handoff contracts, Artifact production, MVP evaluation, commercial experiments and historical V1 reconciliation
```

## 2. Work-product production mapping

```text
authorized data / Knowledge / case context
→ ML-W01 Structured Content
→ ML-W02 Artifact Draft
→ ML-W03 immutable Artifact Version
→ ML-W04 Review Package where required
→ ML-W07 Render Request
→ ML-W08 Render Result
→ optional governed Edit producing a new version
→ ML-W09 Delivery / Publish Package Candidate
→ ML-W05 Prepared Action and exact-purpose confirmation
→ governed/manual operation
→ ML-H02 Return presentation
→ ML-M01/M02 feedback and correction
```

Required boundaries:

```text
Content ≠ Artifact
Artifact ≠ Document
Artifact ≠ Evidence
Artifact ≠ file
Render complete ≠ approved
Edit ≠ invisible mutation of an approved version
Publish Package ready ≠ published
user-reported outcome ≠ platform-confirmed outcome
```

## 3. Handoff contracts — `ML-HC-01–HC-08`

| ID | Destination | Minimum package | Returned result |
| --- | --- | --- | --- |
| ML-HC-01 | MarkReg | customer/applicant/trademark context, need, source, selected version, missing information, authority context | Product Session reference, request for information, rejection, lifecycle result |
| ML-HC-02 | MGSN | Capability Need, jurisdiction/service, constraints, authorized context and disclosure scope | minimized candidate set, unsupported, more information required |
| ML-HC-03 | Human Review | exact Artifact/Action version, sources, claims, audience and decision requested | approved, rejected, revisions required, limited approval |
| ML-HC-04 | Communication Service | draft, exact recipients, channel, purpose, attachments and send consequence | accepted, failed, blocked or unknown send result |
| ML-HC-05 | Opportunity Service | qualified candidate, customer/prospect reference, evidence and proposed owner | formal Opportunity reference or rejection |
| ML-HC-06 | Task / Execution | proposed work, actor, authority, dependencies, review and protected action context | Task/Workflow reference, blocked, failed or result |
| ML-HC-07 | Delivery / Publish | selected Artifact version, account/audience, rights, approval and evidence requirements | delivered/published evidence, failed, blocked or unknown |
| ML-HC-08 | Knowledge Governance | contribution candidate, provenance, scope, contradiction and review need | accepted Knowledge reference, rejected or revisions required |

No destination must trust Lite's qualification without revalidation.

## 4. MVP 0 acceptance criteria — `ML-AC-01–AC-12`

MVP 0 is the **Customer Opportunity-to-Governed-Service Loop**.

| ID | Criterion | Requirement |
| --- | --- | --- |
| ML-AC-01 | Authorized context | Small customer/trademark set with explicit Organization and access scope |
| ML-AC-02 | Opportunity relevance | At least one timely, explainable Service-Value Candidate |
| ML-AC-03 | Source quality | Source, freshness, confidence and missing information visible |
| ML-AC-04 | Work-product value | User receives and uses or meaningfully edits a trustworthy work product |
| ML-AC-05 | User action | Final user confirmation precedes consequential customer action |
| ML-AC-06 | Typed response | Response, no response, rejection, correction and unknown are distinguishable |
| ML-AC-07 | Qualification | Real need can be distinguished from activity or weak interest |
| ML-AC-08 | Governed Handoff | Qualified need accepted or explicitly rejected by MarkReg/another destination |
| ML-AC-09 | Return continuity | Returned result appears in Lite without loss of origin or false state |
| ML-AC-10 | Capability accumulation | Feedback/correction or reusable candidate is preserved with scope |
| ML-AC-11 | Safety and privacy | No blocking scenario violation; unsafe action is stopped |
| ML-AC-12 | Product/commercial evidence | Recurring use, cost and plan evidence collected without redefining Product identity |

Pass rule:

```text
ML-AC-01–AC-11: mandatory
ML-AC-12: evidence collected; commercial threshold remains experiment-specific
content volume alone: insufficient
prospect volume alone: insufficient
```

## 5. Commercial experiments

`ML-E05 Commercial Experiment` may define:

- price;
- billing period;
- trial;
- content frequency or format mix;
- Prospect Candidate quantity or replacement rules;
- Artifact/Render quotas;
- support and review level;
- channel, region or edition;
- cost and gross-margin hypothesis.

The RMB 99 plan and recurring/daily content remain one candidate experiment. They do not bind every Lite edition.

## 6. Historical V1 model reconciliation

The early V1 model is discovery evidence. Its self-description as “final” does not override Books 01–05 or Product Charter v0.3.

| Historical concept | Disposition | Current interpretation |
| --- | --- | --- |
| User / Organization | MOVE TO OWNING SERVICE | Shared identity and organization context; Lite consumes authorized projection |
| primaryRole / membershipLevel / Role / UserRole | REFRAME | Separate organization role, permission, subscription plan and partner/provider qualification |
| Membership and benefit flags | REFRAME | Commercial plan and entitlement; does not grant formal authority |
| PartnerAccount | MOVE TO OWNING SERVICE | Partner/network/commercial qualification, primarily MGSN or platform services |
| TokenAccount / TokenLog | DEFER | Implementation/commercial metering; not Product semantics |
| UserMemory | PRODUCT-LOCAL + REFRAME | `ML-M03–M05`; provenance, scope, review and promotion required |
| AISkill / AISkillRun | MOVE TO OWNING SERVICE | Capability/AI/Execution records; Lite requests and presents results |
| ComplianceRule | MOVE TO OWNING SERVICE | Policy, Review and compliance governance |
| TrademarkAsset universal table | REJECT AS UNIVERSAL MODEL | Split trademark reference, ownership, listing/transaction participation, Artifact and storage policy |
| TrademarkTag | PRODUCT-LOCAL | Candidate classification/tagging with source/confidence; no canonical truth by default |
| TrademarkPackage | REFRAME | Professional Work Product / Artifact, versioned and reviewed |
| AssetInquiry | REFRAME | Communication/customer/prospect candidate; private inquiry must not leak into platform pool |
| Customer | MOVE TO OWNING SERVICE | Formal Customer/Contact remains Core-owned |
| ReferralLink / ReferralClick | DEFER | Commercial attribution and analytics experiment |
| Order | MOVE TO OWNING SERVICE | Order/Matter lifecycle outside Lite |
| Commission | MOVE TO OWNING SERVICE | Finance/commercial service; private self-deal exclusions remain policy input |
| Opportunity | MOVE TO OWNING SERVICE | Formal Opportunity external; `ML-O03/O04/O05` remain candidates |
| OpportunityFollowUp | REFRAME | Product-local preparation/observation until formal Communication/Task/Opportunity update |
| CountryService / CountryPrice | MOVE TO OWNING SERVICE | Product catalog, MarkReg or MGSN source; sensitive prices minimized |
| ServiceProvider / CaseAssignment | MOVE TO OWNING SERVICE | MGSN Trust/Routing and governed execution |
| FileDocument | REJECT AS COLLAPSED MODEL | File, Document, Evidence and Artifact must remain distinct |
| AuditLog | KEEP | Shared audit requirement; Lite events participate but do not own universal audit truth |
| Local-ready fields / Local API | DEFER + KEEP PRINCIPLE | Hybrid minimization and future implementation; local access does not imply sync |
| Private asset/customer exclusions | KEEP | Policy and conformance requirements preventing unauthorized platform use |
| One `isListed` switch | REJECT | Visibility, participation, rights, routing and ownership require separate governed meaning |

## 7. Reconciliation rules

Historical concepts may enter implementation only after they map to:

- an accepted `ML-*` Product record;
- an existing Core/Execution/Workplace/MarkReg/MGSN object;
- a commercial experiment;
- a later implementation specification or ADR.

No historical table name is reserved as the implementation schema.

## 8. Product Baseline effect

Owner merge accepts:

- B06-SPEC-0001–0004 v0.1;
- all controlled `ML-*` ranges listed in the Specification index;
- ML-J01–J04;
- ML-SCN-01–24;
- ML-HC-01–HC-08;
- ML-AC-01–AC-12;
- the historical reconciliation dispositions.

It authorizes preparation of a **Chapter Map Candidate**.

It does not authorize manuscript drafting, implementation, production, autonomous professional action or External Protected Action.
