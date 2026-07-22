# Book 02 — Candidate-to-Frozen Mapping

## 1. Purpose

This register maps the strongest v2 candidate semantics to their nearest frozen Book 02 contracts.

A nearby frozen concept is evidence for composition or profile analysis. It is not evidence that the candidate is already active.

Classification used here:

```text
F1 — composition of frozen semantics may be sufficient
F2 — shared profile or controlled specialization is likely
F3 — candidate shared contract requires formal review
F4 — proposed change would alter frozen meaning, lifecycle or authority
```

## 2. Candidate mapping

| Candidate | Nearest frozen semantics | Gap observed | Preliminary class | Required next gate |
|---|---|---|---:|---|
| Need | Opportunity, Customer, Knowledge, Routing | Frozen Opportunity begins after potential value is identifiable; no neutral pre-route outcome requirement lifecycle is explicit. | F3 | Define purpose, lifecycle, ownership and Need-to-Opportunity relation. |
| Engagement | Partner, Service Provider, Service Network, Routing, Communication, Order, Matter | Frozen collaboration records exist, but no single governed multi-party collaboration boundary with contextual roles and continuity. | F3 | Prove it does not duplicate Order, Matter, Contract, Workflow or Assignment. |
| Work Package | Task, Workflow Contract, Assignment Workflow, Evidence | Frozen Task is actionable work and Workflow Contract governs flow; no implementation-neutral bounded production contract is explicit. | F3/F4 | Map fields and lifecycle against Task before any new object proposal. |
| Assignment | Assignment Workflow, Task, Permission, Policy, Service Provider | Frozen workflow exists, but a canonical Assignment object with offer, acceptance, expiry, suspension and revocation is not explicit. | F3/F4 | Determine whether Workflow instance plus Task/Permission composition is sufficient. |
| Contribution | Document, Evidence, Task, Event, Human Review | Frozen artifacts and Evidence can represent submissions; no general attributable production-result lifecycle is explicit. | F2/F3 | Test a profile over Document/Evidence before proposing a root object. |
| Outcome | Evidence, Human Review, status result envelopes, Matter/Order/Task state | Frozen accepted results are distributed by contract; no implementation-neutral accepted Outcome assembly contract is explicit. | F3 | Define purpose-specific acceptance and prevent formal-state substitution. |
| Professional Authority | Identity, User, Permission, Policy, Human Review, Service Provider | Frozen governance denies agent autonomy but does not fully model externally granted professional authority, appointment and jurisdiction. | F3/F4 | Highest-priority authority proposal; legal/professional review required. |
| Relationship Owner | Customer, Partner, Organization, Communication, Permission | Frozen customer and partner semantics exist; no contextual customer-relationship stewardship role is explicit. | F2/F3 | Define as contextual role and prove it does not imply ownership of a person. |
| Delivery Owner | Workflow Contract, Task, Matter, Service Provider, Routing | Frozen coordination ownership is distributed; no cross-Work-Package delivery-continuity role is explicit. | F2/F3 | Keep separate from Matter owner, professional authority and formal-state owner. |
| Capability Certification | Capability, Identity, Agent registry, Evidence, Human Review | Frozen Capability and Evidence exist; no governed certification lifecycle with assessor, expiry and revocation is explicit. | F3/F4 | Separate platform certification from legal qualification before proposal. |
| Production Authorization | Permission, Policy, Agent governance, Human Review, Capability | Frozen permission/policy can gate actions, but no subject-plus-Capability production scope and expiry contract is explicit. | F3/F4 | Define relation to Permission, Eligibility, Assignment and professional authority. |
| Resale Authorization | Permission, Policy, Partner, Service Provider, Order | Frozen permission and commercial references can partly express it; asset-specific resale authority is not explicit. | F2/F3 | Keep Product-local unless several Products require one stable contract. |

## 3. Supporting profile candidates

The following terms are useful but should first be tested as profiles rather than root objects:

| Profile candidate | Likely frozen base |
|---|---|
| Provider | Organization / Service Provider profile |
| Contributor | Task, Assignment Workflow or Engagement role |
| Contact Role | User or Identity reference in Customer/Organization context |
| Contracting Party | Organization role linked to Order or external contract reference |
| Payment Receiver | Organization role plus payment/settlement reference |
| Transaction Opportunity | Opportunity profile |
| Maintenance Opportunity | Opportunity profile |
| Listing | public or Asset Projection profile |
| Data Product | versioned Document/Knowledge/reference publication profile |
| Brain Result | typed AI/Knowledge result envelope |
| Projection | purpose-limited Common Reference profile |
| Handoff | Workflow boundary profile |
| Return | Event/Evidence/result-envelope profile |

## 4. Candidate dependency graph

Several candidates should not be proposed independently.

```text
Need
→ Opportunity
→ Engagement
→ Work Package
→ Assignment
→ Contribution
→ Review
→ Outcome
```

Authority candidates form a separate control chain:

```text
Capability Evidence
→ Capability Certification
→ Production Authorization
→ task-specific Eligibility
→ Assignment
→ Professional Authority where externally required
```

Ownership-role candidates form another cluster:

```text
Relationship Owner
Delivery Owner
Professional Authority
Formal-state Owning Service
```

These roles must remain separate even when one actor holds several of them.

## 5. Change-risk assessment

### Highest semantic risk

```text
Professional Authority
Production Authorization
Assignment
Work Package
Outcome
```

These can change who may act, what counts as completion and which service may mutate state. They should be treated as F4 until field-level analysis proves a lower class.

### Medium semantic risk

```text
Need
Engagement
Contribution
Capability Certification
Relationship Owner
Delivery Owner
```

These may become stable shared contracts, but profile and composition options must be exhausted first.

### Lower or Product-local priority

```text
Resale Authorization
Transaction Opportunity
Listing
Data Product
Brain Result
```

These should remain profiles or Product-local records unless independent consumers demonstrate a stable interoperability requirement.

## 6. Frozen-name collision controls

Candidate work must avoid misleading reuse of frozen names.

```text
Assignment Workflow
≠ canonical Assignment object

Task
≠ Work Package by default

Service Provider
≠ every Contributor

Knowledge Object
≠ Knowledge Claim automatically

Agent
≠ Brain Result

Opportunity
≠ Need
```

A proposal that declares two terms equivalent must include field, lifecycle, authority and migration evidence.

## 7. Candidate evidence package

Each candidate proposal should include:

1. at least two independent Product or layer use cases;
2. exact frozen sources and nearest existing contracts;
3. rejected F0, F1 and F2 alternatives;
4. proposed identifier and required fields;
5. lifecycle and transition matrix;
6. Owning Service and mutation authority;
7. Evidence, Review and correction rules;
8. Book 03 execution impact;
9. compatibility and migration impact;
10. positive and negative conformance fixtures;
11. legal or professional review where authority is involved;
12. explicit non-goals.

## 8. Mapping verdict

```text
Candidates mapped to frozen neighbours: 12 / 12
Candidate already active merely by name similarity: 0
Candidate safe for silent implementation: 0
Candidates requiring formal field-level analysis: 12 / 12
Immediate frozen replacement required: NO
```

The mapping supports a controlled Change Proposal program. It does not support activating the v2 candidate vocabulary as a package-wide schema in one batch.
