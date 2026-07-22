# Book 02 — Frozen Baseline File Inventory

## 1. Audit purpose

This record identifies the actual frozen Book 02 authority that the v2 publication manuscript must reconcile against.

It replaces the earlier architecture-level phrase “accepted frozen baseline” with repository-resolved identifiers, commits, paths and file families.

This record does not modify the frozen baseline.

## 2. Normative baseline identity

```text
Baseline ID: B02-BASELINE-V0.1
Specification version: 0.1.0
Status: Frozen Core Specification Baseline
Normative content commit: a0a31c9a784854c8943eee448337cb91ad316bb4
Normative source: merge of PR #22
Freeze-governance source: merge of PR #23
Portfolio acceptance source: merge of PR #32
Canonical path: books/book-02-core-specification/
```

The baseline record states that the content merged through PR #22 is normative. PR #23 established the freeze rule and Change Proposal mechanism. PR #32 later recorded that the Book 02 corpus was preserved byte-for-byte and validated 393 files unchanged during the Books 01–04 Portfolio Baseline review.

## 3. Authority chain

```text
PR #22 content baseline
→ commit a0a31c9a784854c8943eee448337cb91ad316bb4
→ PR #23 freeze governance
→ B02-BASELINE-V0.1
→ PR #32 portfolio baseline acceptance
→ current frozen Book 02 authority
```

The recommended tag recorded in `BASELINE.md` is:

```text
book-02-core-baseline-v0.1
```

The commit remains authoritative even if the tag is absent.

## 4. Frozen scope declared by the baseline

The baseline explicitly freezes:

- Core Domains;
- Core Objects;
- Core Services;
- Service ownership;
- canonical status values;
- approved transition matrices;
- Workflow Contract components;
- API Contracts;
- Status Contracts;
- Common Contracts;
- Permission and Policy boundaries;
- Human Review boundaries;
- Event and audit rules;
- AI governance boundaries;
- canonical fixtures;
- publication validators.

The following changes therefore require a formal Book 02 Change Proposal:

- adding, removing or renaming a Core Object;
- changing Object or Service ownership;
- changing canonical status values or transition matrices;
- changing required Contract fields or API payload semantics;
- changing Permission, Policy, Human Review or Approval boundaries;
- changing Event semantics or Workflow mutation authority;
- promoting a Product rule into Core;
- introducing a new cross-Product canonical object;
- changing normative behavior existing implementations must follow.

## 5. Corpus inventory sources

The exact corpus is recoverable from three repository sources.

### 5.1 Canonical migration inventory

`codex/reports/book-02-migration-report.md` enumerates the canonical Book 02 tree moved into:

```text
books/book-02-core-specification/
```

The report preserves the initial file-by-file inventory and confirms that the internal directory structure was not flattened.

### 5.2 Final baseline additions

PR #22 added the final Status Contract, Workflow component and deterministic fixture coverage that became part of the normative content commit.

PR #22 changed 84 files, including:

- shared Status Transition Contract;
- Trademark, Order, Matter and Task Status Contracts;
- Workflow State Definition Contract;
- Workflow Transition Definition Contract;
- 32 deterministic status/workflow fixtures;
- canonical status matrices;
- status/workflow validators and tests;
- traceability and manifest updates.

### 5.3 Portfolio preservation validation

PR #32 recorded:

```text
Book 02: 393 files unchanged; no semantic amendment
```

That review classified Book 02 as `PASS`, preserved the baseline byte-for-byte and concluded that no Book 02 Change Proposal was required for the Books 01–04 Portfolio Baseline.

## 6. File-family inventory

The frozen corpus is organized into the following authoritative families.

| Family | Canonical location | Frozen role |
|---|---|---|
| baseline and governance | `BASELINE.md`, `BOOK-*`, `publication.yaml`, `CHANGELOG.md` | baseline identity, ownership, status and freeze governance |
| manuscript | `manuscript/B02-CH-00` through `B02-CH-31` | normative narrative explanation of Core |
| appendices | `appendices/B02-APP-A` through `B02-APP-H` | glossary and Domain, Object, Service, Event, API, Agent and task indexes |
| planning | `planning/` | accepted positioning, architecture blueprint, domain map, execution matrix and fix plans |
| traceability | `core-specs/TRACEABILITY.md` | Domain-to-Object-to-Service-to-API-to-Event-to-Workflow-to-Agent-to-Test mapping |
| Domains | `core-specs/domains/` | 26 responsibility areas |
| Objects | `core-specs/objects/` | canonical state and identity specifications |
| Services | `core-specs/services/` | behavior and mutation ownership specifications |
| APIs | `core-specs/api/` and `core-specs/contracts/api/` | governed access and payload contracts |
| Events | `core-specs/events/` | completed-fact and audit trace specifications |
| Workflows | `core-specs/workflows/` | execution-flow specifications |
| Workflow Contracts | `core-specs/contracts/workflows/` | governed workflow boundaries and components |
| Status Contracts | `core-specs/contracts/status/` | canonical statuses and transition rules |
| Common Contracts | `core-specs/contracts/common/` | references, versioning, errors, idempotency, audit, AI, permission, policy and Human Review context |
| Test Contracts | `core-specs/contracts/tests/` | specification acceptance contracts |
| fixtures | `core-specs/contracts/fixtures/` | deterministic positive and negative evidence |
| agents | `core-specs/agents/` | governed AI-assistance boundaries |
| validation | `core-specs/validation/` | publication and contract validation rules |
| implementation guidance | `core-specs/implementation/` | MVP cut and implementation-depth matrix |
| Codex tasks | `codex-tasks/` and `core-specs/codex/` | traced implementation sequence, not architecture authority |
| reviews | `core-specs/reviews/` | accepted review and gate records |
| indexes | `indexes/` | navigational indexes |
| editorial | `editorial/` | editorial protocol and chapter template |
| Change Proposals | `change-proposals/` | post-freeze semantic change mechanism |

## 7. Frozen Domain registry

The frozen traceability model contains 26 canonical Domains:

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

`Communication` appears in two traceability perspectives but counts once.

## 8. Frozen workflow set

The frozen specification contains eight primary workflows and corresponding Workflow Contracts:

```text
Customer Intake
Trademark Application
Office Action Response
Provider Routing
Communication Review
Renewal
Assignment
Evidence Review
```

These are frozen specification artifacts. They do not make Core a Workflow Runtime and do not authorize external protected action.

## 9. Frozen manuscript structure

The frozen manuscript contains 32 files:

```text
B02-CH-00 Preface
B02-CH-01 Table of Contents
B02-CH-02 through B02-CH-31 substantive chapters
```

Its major arc is:

```text
why Core exists
→ position, boundary and principles
→ value flow and ontology
→ kernel, layers and responsibility
→ Domains, Objects, Services and execution primitives
→ Contracts, Identity, Capability, Knowledge and business responsibility
→ Domain, Object, Service, Event and AI specifications
→ consumption, MVP boundary, priority, matrix and implementation roadmap
```

## 10. Post-baseline repository comparison

A repository comparison from the normative baseline commit to current `main` shows Book 02 changes under the canonical frozen path limited to freeze and publication-governance records, including:

- `BASELINE.md`;
- `BOOK-MANIFEST.md`;
- `BOOK-STATUS.md`;
- `CHANGELOG.md`;
- `publication.yaml`;
- `change-proposals/`;
- the accepted status/workflow review record.

No frozen manuscript or `core-specs` semantic file modification was identified in that comparison.

The v2 publication reconstruction is stored separately under:

```text
v2/book-02/publication-manuscript/
```

It therefore does not overwrite the canonical frozen tree.

## 11. Maintenance classes

Ordinary maintenance remains limited to meaning-preserving work classified as:

```text
Documentation-only
Link-only
Formatting-only
Metadata-only
Validator-restoration-only
```

A publication rewrite, new object, changed lifecycle, changed ownership or changed authority boundary does not qualify merely because it is written in Markdown.

## 12. Inventory verdict

```text
Normative baseline identified: YES
Normative content commit identified: YES
Freeze PR identified: YES
Portfolio acceptance identified: YES
Canonical path identified: YES
Frozen scope identified: YES
Corpus preservation evidence identified: YES
Frozen manuscript directly modified by v2 reconstruction: NO
Frozen Core replacement authorized: NO
```

The remaining exact-trace task is not to discover what the baseline is. It is to map every v2 thesis and candidate semantic to this known baseline and determine its disposition.
