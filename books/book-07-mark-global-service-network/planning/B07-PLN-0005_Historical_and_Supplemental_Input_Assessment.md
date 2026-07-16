# B07-PLN-0005 — Historical and Supplemental Input Assessment

## Status

```text
Draft for Owner Review
```

## Purpose

Earlier provider, pricing, assignment and supply-center concepts contain useful demand evidence, but they must be reconciled with:

- platform ownership of MGSN;
- central hub topology;
- three delivery routes;
- platform procurement and funds control;
- external-route continuity limits.

## Classification Rules

```text
KEEP
REFRAME
PRODUCT-LOCAL
MOVE TO CORE OR OWNING SERVICE
MOVE TO EXECUTION
MOVE TO WORKPLACE
DEFER
REJECT
```

## Assessment

| Historical concept | Classification | Current treatment |
| --- | --- | --- |
| Global service-provider inventory | KEEP / REFRAME | Platform-owned governed supply pool, not user-owned address book |
| Provider legal identity and contacts | KEEP | Source-linked and permission-controlled network identity |
| Country and jurisdiction coverage | KEEP | Scoped Capability coverage with freshness and evidence |
| Service-category coverage | KEEP | Governed taxonomy and provider Capability profile |
| Provider qualification | KEEP / REFRAME | Claim, evidence, verification and expiry remain separate |
| One universal provider rating | REJECT | Replace with multidimensional contextual platform Trust and evidence |
| Public five-star reviews | REJECT / DEFER | Not suitable as primary Trust model |
| Provider private pricing | KEEP / REFRAME | Platform procurement input, access-controlled and not automatically user-visible |
| Country price table | REFRAME | Service package, jurisdiction, provider cost, official fee, tax and validity structure |
| User-visible fixed price | PRODUCT-LOCAL | Platform or Product offer, not identical to provider cost |
| Global agent center | REFRAME | User-facing gateway into platform-governed global capability |
| User-owned global partner center | REJECT AS MGSN IDENTITY | User may hold external routes, preferences and notes, but does not own MGSN supply |
| User's existing foreign associate | KEEP / SPLIT BY ROUTE | May remain External Self-Managed, or enter MGSN only after platform admission and commercial agreement |
| User import of provider into Lite/Workplace | REFRAME | Not required for an external route; a private contact does not create MGSN supply |
| Same provider used outside and inside MGSN | KEEP / REFRAME | Two distinct routes with different price, funds, responsibility, evidence and guarantees |
| ServiceProvider table as canonical authority | REJECT | Early implementation idea only; cannot represent all route, identity and ownership meanings |
| CaseAssignment | MOVE TO OWNING SERVICE / EXECUTION | MGSN may prepare or reference allocation but must not duplicate Matter/Task/Workflow authority |
| Provider assignment status | REFRAME | Separate matching, user confirmation, allocation, instruction and provider acceptance |
| Provider availability | KEEP | Service-, deadline- and time-scoped state |
| Conflict check | KEEP | Distinct gate with purpose-limited disclosure |
| Open bidding request | REJECT | Conflicts with closed operation and confidentiality |
| Lowest-price wins | REJECT | Price is important but cannot override capability, risk and fulfillment |
| Platform negotiated prices | KEEP | Core platform value and supply-attraction mechanism |
| Platform Recommended Best Route | KEEP | Default optimized route with explanation and user confirmation |
| Automatic matching | KEEP / REFRAME | May preselect a route; does not equal autonomous provider appointment |
| User final choice | KEEP / REFRAME | Confirm, reject, adjust or choose external route within defined boundaries |
| Platform margin | KEEP AS COMMERCIAL HYPOTHESIS | Must include support, failure, funds and risk cost |
| Referral fee | DEFER | Requires neutrality, disclosure and legal review |
| Transaction commission | DEFER | Possible model, not Product identity |
| Paid provider placement | REJECT OR STRICTLY ISOLATE | Must not masquerade as professional fit or routing evidence |
| Provider subscription | DEFER | May support verification or services but not eligibility authority |
| Demand-side subscription | DEFER | Possible access and management model |
| Platform-managed payment | KEEP / REFRAME | Funds lifecycle, milestones, release, refund and settlement require governed model |
| Direct payment to external provider | KEEP AS R1 CONSEQUENCE | User bears payment and non-performance risk; MGSN guarantees do not apply |
| Direct payment to MGSN provider | REJECT AS DEFAULT MANAGED FLOW | Bypasses platform funds and fulfillment controls |
| Escrow label | DEFER | Legal characterization must not be assumed |
| Official-fee advance | KEEP | Requires purpose separation, evidence and reconciliation |
| Provider milestone payment | KEEP | Evidence-based release candidate |
| Automatic provider allocation | DEFER / SERVICE-MODEL SPECIFIC | Only possible under accepted standing mandate; not implied by matching |
| Platform-recommended provider | KEEP | Default Product experience, explainable and governed |
| User-preferred MGSN provider | KEEP | Preference remains subject to admission, conflict, availability, procurement and risk gates |
| Masked provider contact | KEEP AS EXPERIENCE CANDIDATE | Supports staged disclosure and bypass control |
| Direct Communication | REFRAME | Platform-mediated or stage-permitted inside MGSN; unrestricted lateral networking is not created |
| Provider replacement | KEEP | Core continuity and risk-control capability for managed routes |
| Provider suspension | KEEP | Platform governance responsibility with review and appeal |
| External route replacement | USER RESPONSIBILITY | No implied MGSN replacement guarantee |
| Manual upload of external receipts/status | KEEP / MOVE TO PRODUCT CONTINUITY | Reconnects external work to Workplace/MarkReg with source and confidence labels |
| Network data aggregation | KEEP | Platform asset subject to source rights, privacy and scope |
| Public provider ranking | REJECT | Conflicts with contextual Trust and closed-network strategy |
| AI matching | KEEP / REFRAME | Decision support under eligibility, evidence and user confirmation |
| AI automatic appointment | REJECT AS DEFAULT | High-risk authority drift |
| Public demand board | REJECT | Conflicts with confidentiality and closed operation |
| Service procurement dashboard | KEEP | Core platform/operator surface |
| Funds and settlement dashboard | KEEP | Core operational and risk-control surface |
| Provider self-service portal | KEEP | Controlled claim, evidence, acceptance, milestone and settlement interface |
| User service workspace | KEEP | Need, route, offer, payment, status, approval and outcome interface |

## Design Consequence

The historical material supports:

```text
platform supply
+ platform procurement
+ platform matching
+ user confirmation
+ platform funds control
+ platform fulfillment governance
+ external-route manual continuity
+ independent provider responsibility
```

It does not support:

- unrestricted public marketplace;
- user ownership of MGSN supply;
- forced import of external providers;
- silent MGSN guarantees for external routes;
- one provider object that erases route differences;
- automatic appointment merely because a provider ranks first.

## Implementation Boundary

No historical table or field name is accepted as schema authority.

The Charter and controlled baseline must first determine:

- authoritative records;
- route types and projections;
- relationship to Book 02 Core;
- formal state ownership;
- matching and confirmation boundaries;
- external-route evidence return;
- interface and Handoff contracts;
- legal funds model;
- Product versus network responsibility.

## Gate

This classification may be accepted as part of Pre-Writing Audit v0.1.

It does not authorize schema, APIs, payment implementation, provider allocation or manuscript drafting.