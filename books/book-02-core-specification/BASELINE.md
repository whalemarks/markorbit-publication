# Book 02 Core Specification Baseline

Baseline ID: B02-BASELINE-V0.1
Book: Book 02 — MarkOrbit Core Specification
Specification Version: 0.1.0
Status: Frozen Core Specification Baseline
Content Baseline Commit: a0a31c9a784854c8943eee448337cb91ad316bb4
Content Baseline Source: Merge of PR #22
Freeze Governance: Effective upon merge of PUB-TASK-B02-FREEZE
Owner: MarkOrbit Publications Editorial Board

## Baseline meaning

The content merged through PR #22 is the normative
Book 02 v0.1 Core specification baseline.

This baseline may be consumed by markorbit-core,
Book 03, Book 04, Mo Lite, MarkReg, Mo Crawl and
other MarkOrbit projects.

Consumption does not authorize silent modification.

## Frozen scope

Frozen scope includes:

- Core domains
- Core Objects
- Core Services
- Service ownership
- canonical status values
- approved transition matrices
- Workflow Contract components
- API Contracts
- Status Contracts
- Common Contracts
- Permission and Policy boundaries
- Human Review boundaries
- Event and audit rules
- AI governance boundaries
- canonical fixtures
- publication validators

## Freeze rule

No semantic change may be made directly to frozen scope
without an accepted Book 02 Change Proposal. Every semantic baseline change requires an explicit Book 02 Change Proposal.

## What remains permitted

The following maintenance work may be handled through ordinary maintenance PRs when it does not change meaning:

- spelling and grammar;
- broken internal links;
- formatting defects;
- duplicate text;
- incorrect file references;
- metadata corrections that do not change meaning;
- validator defects that only restore enforcement of already-approved semantics;
- explicit errata that do not introduce new requirements.

These repairs must be marked as one of:

```text
Documentation-only
Link-only
Formatting-only
Metadata-only
Validator-restoration-only
```

## What requires Change Proposal

The following require a Book 02 Change Proposal before publication work changes the frozen scope:

- adding, removing, or renaming a Core Object;
- changing Object ownership;
- changing Service ownership;
- changing a canonical status value;
- changing a transition matrix;
- changing API payload semantics;
- changing Contract required fields;
- changing decision vocabulary;
- changing Permission, Policy, Human Review, or Approval boundaries;
- changing Event semantics;
- changing Workflow mutation authority;
- promoting a new product rule into a Core rule;
- introducing a new cross-product canonical object;
- changing normative behavior that existing implementations must follow.

## What belongs elsewhere

| Content | Target location |
| --- | --- |
| implementation architecture | Book 04 |
| typed implementation mapping | Book 04 or code repository |
| runtime contracts and validators | relevant code repository |
| Mo Crawl | Mo Crawl project / Book 04 |
| Information Engine | corresponding project / Book 04 |
| Value Factory and Value Object | corresponding project / Book 04 |
| Mo Intelligence and recommendation | corresponding project / Book 04 |
| Mo Lite product behavior | Mo Lite repository |
| MarkReg trademark workflows | MarkReg repository |
| product UI and user journey | product repository |
| deployment and infrastructure | project repository |
| implementation defects | implementation backlog |
| possible specification defect | Book 02 Change Proposal backlog |

## Relationship to implementation

Book 02 is not automatically rewritten when code differs.

A difference between Book 02 and implementation must first
be classified as:

1. implementation defect;
2. incomplete implementation;
3. product-specific extension;
4. specification ambiguity;
5. proposed specification change.

## Recommended baseline tag

Recommended repository tag:

```text
book-02-core-baseline-v0.1
```

The repository tag may be created after the freeze PR is merged.
The normative content baseline commit remains
a0a31c9a784854c8943eee448337cb91ad316bb4.
