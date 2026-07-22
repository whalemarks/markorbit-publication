# Book 02 — Change Proposal Priority Register

## 1. Purpose

This register sequences the formal analysis needed after the v2 publication reconstruction.

It does not create or approve a Change Proposal. It identifies which candidate clusters should be investigated first and what evidence is required before a proposal is opened.

Priority levels:

```text
P0 — authority or state integrity risk; analyze before downstream adoption
P1 — high cross-Product value with material semantic impact
P2 — useful shared profile; composition should be tested first
P3 — Product-local or implementation concern unless further evidence appears
```

## 2. Priority register

| Priority | Candidate package | Preliminary class | Why it matters | Immediate output |
|---:|---|---:|---|---|
| P0 | Professional Authority boundary | F3/F4 | Prevents platform identity, qualification, appointment and professional action authority from collapsing. | authority-source and appointment model; legal/professional review |
| P0 | Work Package / Assignment / Contribution / Outcome | F3/F4 | Defines the shared production chain consumed by Book 03, MarkReg, Lite and networks. Incorrect admission can redefine Task, Workflow and formal completion. | frozen Task/Workflow field comparison and object-decomposition decision |
| P0 | Production Authorization / Eligibility relation | F3/F4 | Controls who or what may enter production and prevents Certification, Entitlement or model capability from becoming task authority. | Permission/Policy mapping and transition matrix |
| P1 | Need / Opportunity relation | F3 | Preserves pre-commercial outcome need without corrupting frozen Opportunity. | Need lifecycle and conversion semantics |
| P1 | Engagement and contextual roles | F3 | Supports multi-Workplace, white-label and Provider collaboration while preserving customer relationship and formal authority. | duplication test against Order, Matter, Partner, Service Network and Assignment |
| P1 | Knowledge Source / Document / Claim / Version | F2/F3/F4 | Needed for source-governed Knowledge and Brain, but may split the frozen Knowledge Object. | Knowledge internal-profile versus Core-object decision |
| P1 | Relationship Owner / Delivery Owner | F2/F3 | Makes customer and delivery continuity explicit without treating either as ownership of every record. | contextual role contract and conflict matrix |
| P2 | Capability Certification | F3 | Supports assessment and network trust, but must not imply legal qualification. | certification scheme profile and Evidence requirements |
| P2 | typed Brain Result | F2/F3 | Supports interoperable Retrieval, Inference, Recommendation, Candidate and Explanation outputs. | profile envelope and non-canonical acceptance rules |
| P2 | Projection / Handoff / Return | F2/F3 | Common boundary language is useful across Products and Workplaces. | test composition over Common References, Workflow Contracts, Events and Evidence |
| P2 | Data Product | F2/F3 | Useful for shared datasets and releases, but likely belongs to Data architecture rather than Core root objects. | versioned publication profile and ownership boundary |
| P3 | Resale Authorization | F2/F3 | May be important for trademark transactions but may remain Product-local. | cross-Product demand evidence before proposal |
| P3 | L1–L5, M0–M5, R0–R4 controlled values | F2/F4 | Useful governance vocabulary; global freezing may create unnecessary migration and policy coupling. | decide Core values versus Book 03/Product policy profiles |

## 3. Proposed analysis packages

### CP-A — Professional Authority and Production Control

Scope:

```text
Professional Authority
Professional Qualification reference
Capability Certification
Production Authorization
Eligibility
Assignment authority ceiling
```

Required questions:

- Which authority is externally granted?
- Which record may Core represent but never issue?
- Which service verifies current credential state?
- How are appointment, conflict clearance and jurisdiction represented?
- How does Production Authorization differ from Permission and Policy?
- What expires or is revoked when a credential changes?

Exit condition:

```text
No actor, model, Provider listing or Certification
can be mistaken for authority to perform a reserved action.
```

### CP-B — Governed Production Object Chain

Scope:

```text
Work Package
Assignment
Contribution
Review reference
Outcome
```

Required comparison:

```text
Frozen Task
Frozen Workflow Contract
Frozen Assignment Workflow
Document
Evidence
Event
Status result envelopes
```

Possible decisions:

- F1 composition only;
- F2 profiles over Task, Document and Evidence;
- F3 new contracts;
- F4 revision of Task or Workflow semantics.

Exit condition:

```text
Book 03 can consume one stable production contract
without Core becoming the Execution Runtime.
```

### CP-C — Need, Engagement and Ownership Roles

Scope:

```text
Need
Engagement
Relationship Owner
Delivery Owner
contextual participant roles
```

Required comparison:

- Opportunity;
- Customer;
- Partner;
- Service Provider;
- Service Network;
- Routing;
- Communication;
- Order;
- Matter.

Exit condition:

```text
Multi-party collaboration is representable
without transferring customer relationship,
professional authority or formal-state ownership.
```

### CP-D — Knowledge and Typed Intelligence

Scope:

```text
Knowledge Source
Knowledge Document
Knowledge Claim
Knowledge Version
Citation
Brain Result profiles
```

Required questions:

- Can the frozen Knowledge Object contain these as internal records or profiles?
- Which items require cross-Product stable identifiers?
- Which claims may remain Knowledge-service-local?
- How are source authority, rights, freshness and conflict represented?
- How does a Brain result become a Knowledge Candidate?
- What review is required before promotion?

Exit condition:

```text
Knowledge becomes traceable
without Brain output becoming canonical
or Core becoming the Knowledge repository.
```

### CP-E — Boundary Transfer Profiles

Scope:

```text
Projection
Handoff
Return
Correction
```

Composition test:

- Common References;
- Permission and Policy context;
- Workflow Contract;
- Event;
- Evidence;
- Communication;
- versioning and errors.

These concepts should remain F2 profiles if composition supplies stable interoperability without a new authoritative lifecycle.

## 4. Sequencing dependencies

Recommended order:

```text
CP-A Professional Authority
→ CP-B Production Object Chain
→ CP-C Need and Engagement
→ CP-D Knowledge and Brain
→ CP-E Boundary Transfer Profiles
→ lower-priority commercial and controlled-value decisions
```

Reason:

- CP-A determines authority ceilings used by CP-B.
- CP-B establishes the work units used inside Engagement.
- CP-C establishes collaboration and ownership context.
- CP-D determines what evidence and intelligence may support those records.
- CP-E standardizes cross-boundary exchange only after object ownership is stable.

## 5. Proposal template requirements

Every formal proposal must use the frozen Change Proposal mechanism and include:

```text
Proposal ID
Problem statement
Frozen sources
Proposed class and alternatives
Exact semantic delta
Object / profile decision
Identifier
Required fields
Lifecycle
Owning Service
Mutation authority
Permission / Policy / Review requirements
Event and audit behavior
API impact
Workflow impact
Book 03 impact
Product impact
Compatibility
Migration
Positive fixtures
Negative fixtures
Rollback
Non-goals
Owner decision
```

## 6. Rejection criteria

A proposal should be rejected or returned to Product-local scope when:

- only one Product needs it;
- the concept is primarily UI, pricing, ranking or workflow policy;
- existing contracts can compose it safely;
- ownership or lifecycle is unclear;
- it imports Book 03 runtime into Core;
- it grants authority through a score, model or platform badge;
- no compatibility or migration plan exists;
- it cannot define negative fixtures;
- the long-term maintenance cost exceeds interoperability value.

## 7. Implementation gate

No engineering task should implement a candidate public contract before proposal acceptance.

Safe pre-proposal work is limited to:

- repository research;
- field inventories;
- mapping documents;
- Product-local experiments behind noncanonical interfaces;
- Simulation fixtures;
- rejected-alternative analysis.

```text
Prototype
≠ Core contract

Local type
≠ approved public export

Passing test
≠ semantic acceptance
```

## 8. Priority verdict

```text
P0 analysis packages: 3
P1 analysis packages: 4
P2 profile decisions: 4
P3 deferred decisions: 2
Candidate automatically approved: 0
Production implementation authorized: NO
Frozen baseline version increment authorized: NO
```

The next controlled program should begin with CP-A and CP-B research artifacts, not with a single omnibus change that activates all v2 nouns.
