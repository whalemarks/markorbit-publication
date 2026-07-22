# Book 02 — Current Core Implementation Mapping

## 1. Repositories and authority

Publication authority:

```text
whalemarks/markorbit-publication
books/book-02-core-specification/
B02-BASELINE-V0.1
```

Engineering implementation:

```text
whalemarks/markorbit-core
package: @markorbit/core
version: 0.1.0
```

The implementation repository states that Book 02 remains specification authority and that implementation convenience may not redefine it.

```text
Publication specification
≠ implementation repository
```

A difference must be classified before either side changes.

## 2. Current engineering baseline

The current top-level engineering records identify:

```text
Current task state: CORE-TASK-061
Book 02 MVP semantic baseline: COMPLETE via CORE-TASK-060
Engineering distribution baseline: @markorbit/core@0.1.0
Production readiness: NOT ACCEPTED
First intended consumer: whalemarks/markorbit-execution
```

The public package boundary exposes:

```text
@markorbit/core
@markorbit/core/objects
@markorbit/core/events
@markorbit/core/tasks
@markorbit/core/contracts
@markorbit/core/services
@markorbit/core/api
@markorbit/core/workflows
@markorbit/core/governance
```

It intentionally excludes arbitrary source paths, tests, fixtures, database adapters, UI code, external connectors and a full Workflow Runtime.

## 3. Structural contract mapping

The implementation manifest records 26 baseline Domains and a 187-entry contract index across 12 families.

| Contract family | Current indexed count |
|---|---:|
| foundation | 6 |
| Domain | 26 |
| Object | 26 |
| Service | 26 |
| API | 34 |
| Event catalog | 12 |
| Workflow contract/catalog | 16 |
| Permission | 8 |
| Policy | 8 |
| AI governance | 8 |
| Common | 10 |
| Test | 7 |
| **Total** | **187** |

The 34 API entries include canonical Domain APIs and retained compatibility scaffolds. The 16 Workflow entries include canonical contracts and retained catalog compatibility entries.

## 4. Frozen Domain-to-implementation coverage

The engineering registry covers the 26 frozen Domains:

```text
Identity
Organization
User
Permission
Policy
Knowledge
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Customer
Matter
Order
Opportunity
Workflow Contract
Task
Event
Notification
Communication
Partner
Agent
Service Provider
Service Network
Routing
```

For each Domain, the accepted structural baseline includes Domain, Object, Service and API contract evidence. This is structural and semantic package evidence; it does not imply complete Product behavior or production deployment.

## 5. Service behavior mapping

The engineering history distinguishes contract skeleton coverage from executable Service-owned behavior.

By `CORE-TASK-055`, the repository recorded:

```text
18 Must Build Service foundations complete
at the locked MVP behavior depth
```

The implementation sequence includes governed foundations for:

- Customer;
- Brand;
- Trademark;
- Jurisdiction;
- Classification;
- Document;
- Evidence;
- Matter;
- Order;
- Opportunity;
- Event;
- Task;
- Workflow Contract;
- Communication;
- Identity;
- Organization;
- User;
- Permission;
- Policy.

The exact count depends on the acceptance model because some responsibilities overlap semantically and the historical manifest contains task-by-task status notes. The top-level current state, final completion audit and package boundary must control over stale intermediate notes.

## 6. Frozen contract-to-code evidence map

| Frozen source family | Current implementation evidence | Mapping status |
|---|---|---|
| Domain registry | `src` Domain registry and fixtures | implemented at baseline contract level |
| Objects | public-reference/base types, Object contracts and validators | implemented at governed MVP baseline |
| Services | service skeletons plus selected executable lifecycle/scope behavior | implemented to locked MVP acceptance depth |
| APIs | governed API boundary specifications and fixtures through CORE-TASK-057A–C | accepted semantic boundary, not API server |
| Events | event primitive, event catalog and exact MVP alias lock | accepted contract evidence, not message infrastructure |
| Workflows | Customer Intake and Trademark Application workflow evidence plus contract catalog | accepted MVP workflow semantics, not full runtime |
| Status Contracts | state/transition contract fixtures and validators | represented through contract and workflow validation evidence |
| Common References | reference types and resolution behavior | accepted minimum-depth behavior |
| Versioning and Errors | common contracts, safe-error and version validation | accepted governed behavior |
| Idempotency | common contract and executable enforcement evidence | accepted governed behavior |
| Permission and Policy | contract skeletons, context validation and service foundations | accepted baseline; Product decisions remain external |
| Human Review | common contract and review hooks | accepted boundary, not professional decision engine |
| AI governance | eight governance contract skeletons, source inventory and boundary tests | accepted contract layer; no model execution or approval authority |
| Fixtures and tests | required fixture manifest, unit/fixture/consumer tests | engineering evidence |
| distribution | package export manifest and consumer proof | internal engineering baseline only |

## 7. Implementation exclusions that remain authoritative

The current engineering repository expressly excludes:

- Product UI and Product applications;
- MarkReg and Lite behavior;
- Book 03 Execution System runtime;
- trademark business logic;
- full Workflow Engine;
- production database connections;
- API server and external integrations;
- AI agents with autonomous approval authority;
- production readiness;
- external protected actions.

Therefore:

```text
contract exported
≠ runtime available

fixture passes
≠ production readiness

Service method exists
≠ Product business policy accepted

Workflow evidence exists
≠ Book 03 Execution implemented
```

## 8. v2 candidate implementation status

The following v2 candidates must not be inferred from similarly named engineering artifacts.

| v2 candidate | Existing implementation neighbour | Current conclusion |
|---|---|---|
| Need | Opportunity, Routing and Knowledge contracts | no canonical Need contract identified |
| Engagement | Partner, Service Provider, Service Network and Routing | no canonical Engagement lifecycle identified |
| Work Package | Task and Workflow Contract | no approved Work Package contract identified |
| Assignment | Assignment Workflow contract/catalog | no separately approved Assignment object identified |
| Contribution | Document, Evidence, Task and Event | no canonical Contribution lifecycle identified |
| Outcome | result envelopes, Evidence and formal Service state | no canonical Outcome object identified |
| Professional Authority | Identity, Permission, Policy, Human Review | no platform-created professional-authority contract accepted |
| Relationship Owner | Customer, Partner, Organization | no canonical role contract identified |
| Delivery Owner | Workflow, Matter, Task | no canonical role contract identified |
| Capability Certification | Capability, Evidence and governance | no accepted certification lifecycle identified |
| Production Authorization | Permission, Policy and AI governance | no accepted production-authorization object identified |
| Resale Authorization | Permission, Partner and Order | no accepted shared resale-authorization contract identified |

Implementation work for these terms would be semantic expansion and must follow Book 02 governance.

## 9. Current package and publication version relation

```text
Frozen specification version: 0.1.0
Engineering package version: 0.1.0
Engineering baseline ID: book-02-mvp-engineering-baseline@0.1.0
```

Matching version numbers do not prove complete equivalence by themselves. The implementation repository supplies traceability, fixtures and acceptance audits as evidence.

A future Book 02 Change Proposal may require:

- a new specification version;
- a new package minor or major version;
- compatibility declarations;
- consumer migration;
- fixture updates;
- Book 03 integration changes.

## 10. Documentation-quality finding

`README.md` and `CORE-MANIFEST.md` preserve a long historical task log. Some intermediate sections state that the MVP was incomplete, while their current headers state semantic completion through CORE-TASK-060 and distribution through CORE-TASK-061.

This is not necessarily semantic drift, but it creates reading risk.

Recommended maintenance classification:

```text
Documentation-only / Metadata-only
```

Recommended action in the engineering repository:

- keep one current-state summary at the top;
- move task history into a versioned implementation history or changelog;
- label intermediate completion statements as historical;
- keep production-readiness exclusions visible.

This cleanup must not change accepted semantics.

## 11. Implementation mapping verdict

```text
Implementation repository identified: YES
Package baseline identified: YES
Frozen 26-Domain coverage identified: YES
187-contract structural baseline identified: YES
Engineering semantic baseline claimed complete: YES
Production readiness accepted: NO
Book 03 Execution runtime implemented in Core: NO
Candidate v2 semantics implemented as approved Core: NO EVIDENCE IDENTIFIED
Implementation allowed to redefine Book 02: NO
```

The current engineering baseline materially implements the frozen v0.1 contract system. It does not implement or activate the v2 candidate semantic set.
