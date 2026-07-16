# B07-SPEC-0002 — MGSN Product-Local Record Catalog

## Status

```text
Candidate
Implementation-neutral
Not Core
Not database schema
```

## Record Rule

Every `MG-*` record is a controlled Product-local meaning. It may later map to one or more database records, events, projections or service contracts, but this publication does not choose that implementation.

## MG-N — Network Participation and Connection

| ID | Record | Meaning |
| --- | --- | --- |
| MG-N01 | Network Participation | Organization-level participation state in MGSN |
| MG-N02 | Workplace Connection | Authorized Workplace connection or Gateway configuration |
| MG-N03 | Participant Role Enablement | Contextual Demand and/or Supply role enablement |
| MG-N04 | Participation Terms Acceptance | Versioned acceptance of network rules and commercial conditions |
| MG-N05 | Connection Permission Scope | Approved projection, view and action scope |
| MG-N06 | Participation Exit or Portability Request | Controlled withdrawal, export and continuing-obligation request |

## MG-C — Capability and Supply

| ID | Record | Meaning |
| --- | --- | --- |
| MG-C01 | Provider Network Profile | MGSN-local provider projection linked to a Core Organization |
| MG-C02 | Capability Claim | Provider assertion of a service capability |
| MG-C03 | Capability Evidence | Evidence supporting a claim |
| MG-C04 | Capability Verification | Platform review result and scope |
| MG-C05 | Qualification Status | Current professional or jurisdiction qualification projection |
| MG-C06 | Availability Declaration | Current capacity, timing and service availability |
| MG-C07 | Supply Portfolio Entry | Provider placement in a jurisdiction/service portfolio |
| MG-C08 | Service Package Admission | Approved service scope, conditions and delivery expectations |

## MG-P — Procurement and Service Offer

| ID | Record | Meaning |
| --- | --- | --- |
| MG-P01 | Procurement Term Set | Platform-provider negotiated commercial terms |
| MG-P02 | Official Fee and Disbursement Model | Source-qualified official and third-party cost structure |
| MG-P03 | Service Scope Definition | Standardized included/excluded service scope |
| MG-P04 | Platform Cost and Risk Layer | Platform service, support and risk allocation layer |
| MG-P05 | Demand-Side Offer | User-facing service offer and price |
| MG-P06 | Offer Validity | Expiry, assumptions and change conditions |
| MG-P07 | Price Exception | Reviewed deviation from standard procurement or offer |
| MG-P08 | Commercial Reconciliation | Cost, charge, refund and adjustment reconciliation projection |

## MG-R — Routing, Recommendation and Selection

| ID | Record | Meaning |
| --- | --- | --- |
| MG-R01 | Capability Need Projection | Authorized MGSN projection of a need owned by an Originating Workplace or Product |
| MG-R02 | Route Choice | R1, R2 or R3 route decision context |
| MG-R03 | Eligibility Assessment | Provider/service eligibility result |
| MG-R04 | Conflict and Availability Check | Current provider conflict and capacity result |
| MG-R05 | Candidate Route Set | Governed eligible route candidates |
| MG-R06 | Routing Recommendation | Explainable Recommended Route and bounded alternatives |
| MG-R07 | User Route Disposition | Confirm, reject, rematch, preferred-provider or R1 choice |
| MG-R08 | Provider Allocation and Acceptance | Platform allocation followed by provider acceptance or refusal |

## MG-F — Funds, Fulfillment and Return

| ID | Record | Meaning |
| --- | --- | --- |
| MG-F01 | Managed Network Engagement | MGSN-local engagement linking authorized projections without replacing Order or Matter |
| MG-F02 | Funds Requirement | Amount, purpose, currency, due timing and authority prerequisites |
| MG-F03 | Funds Allocation | Purpose-specific allocation projection, not the Finance ledger |
| MG-F04 | Release Condition | Evidence or milestone required before release |
| MG-F05 | Provider Commitment | Provider confirmation of scope, timing and conditions |
| MG-F06 | Fulfillment Milestone | Expected and observed delivery milestone |
| MG-F07 | Fulfillment Evidence | Provider or source Evidence supporting progress or completion |
| MG-F08 | Fulfillment Observation | Platform observation; not automatically formal Matter truth |
| MG-F09 | Return Envelope | Typed return to the Originating Workplace or Product |
| MG-F10 | Settlement and Reconciliation Projection | Network settlement/refund/dispute projection linked to Finance authority |

## MG-T — Trust, Relationship and Network Learning

| ID | Record | Meaning |
| --- | --- | --- |
| MG-T01 | Relationship Provenance | Who introduced whom and the pre-existing relationship context |
| MG-T02 | Attribution Period | Time-bounded invitation or relationship attribution |
| MG-T03 | Private Preference | Workplace-controlled preferred-provider or route preference |
| MG-T04 | Delivery Performance Evidence | Source-aware performance Evidence |
| MG-T05 | Trust Dimension Assessment | Multidimensional, service-specific, correctable assessment |
| MG-T06 | Network Learning Candidate | Candidate procurement, routing or supply improvement |
| MG-T07 | Incentive Eligibility | Eligibility for a bounded invitation or contribution incentive |
| MG-T08 | Provider Evolution Decision | Reward, increased scope, restriction, suspension or retirement consequence |

## MG-E — Exception, Restriction and Governance

| ID | Record | Meaning |
| --- | --- | --- |
| MG-E01 | Network Incident | Delay, non-performance, disclosure, funds or conduct incident |
| MG-E02 | Correction Request | Required correction and deadline |
| MG-E03 | Replacement Decision | Controlled provider replacement decision |
| MG-E04 | Dispute Case | Product-local dispute coordination record |
| MG-E05 | Restriction | Service, jurisdiction, visibility or participation restriction |
| MG-E06 | Suspension | Temporary network participation or supply suspension |
| MG-E07 | Retirement | Controlled removal from future active supply |
| MG-E08 | Appeal and Governance Review | Review of admission, restriction, suspension or Trust consequence |

## Cardinality and Ownership Locks

```text
Core Organization
≠ MG-C01 Provider Network Profile

Capability Claim
≠ Capability Verification

Candidate Route Set
≠ Routing Recommendation

Routing Recommendation
≠ User Route Disposition

User Route Disposition
≠ Provider Allocation

Provider Allocation
≠ Provider Acceptance

Funds Allocation
≠ Finance ledger posting

Fulfillment Observation
≠ formal Matter status

Trust Dimension Assessment
≠ universal public score

Relationship Provenance
≠ ownership of another participant
```

## Promotion Lock

No `MG-*` record becomes Core merely because more than one Product references it. Promotion requires repeated cross-product need, explicit semantic review, ownership analysis and the Book 02 Change Proposal process where applicable.
