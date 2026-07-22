# Book 02 — Chapter and Contract Disposition Matrix

## 1. Purpose

This matrix classifies the 36 v2 publication chapters against the frozen `B02-BASELINE-V0.1` corpus.

Disposition labels:

```text
E — explanatory restatement of frozen meaning
M — merged explanation from several frozen sources
P — profile or composition over frozen semantics
C — candidate addition; not active Core
X — external boundary clarification owned by another Book or layer
```

No row in this matrix authorizes a frozen-file edit or Core activation.

## 2. Chapter-level disposition

| v2 chapter | Primary frozen source cluster | Disposition | Audit conclusion |
|---|---|---:|---|
| CH01 Core Is Shared Meaning | manuscript CH02–CH06; `business-responsibility.md`; Book governance | E/M | Restates frozen Core purpose and business-responsibility boundary. |
| CH02 Authority Must Remain Separated | Identity, Permission, Policy, Human Review, Service ownership | M/P | Frozen contracts support authority separation; five-dimensional authority vocabulary is explanatory and partly cross-book. |
| CH03 Candidate Before Canonical | Evidence, Knowledge, Human Review, status/workflow fixtures | M/P | Candidate discipline is consistent with fail-closed frozen contracts; universal Candidate model is not separately activated. |
| CH04 What Belongs in Core | `BASELINE.md`; governance; change-proposal rules | E | Direct explanation of the frozen admission and exclusion boundary. |
| CH05 Person, Organization, Workplace and Membership | Identity, Organization, User, Permission; Book 04 Workplace | P/X | Organization/User are frozen. Person, Workplace and Membership require profile or cross-book mapping, not silent Core objects. |
| CH06 Customer, Contact and Relationship | Customer, Organization, User, Partner, Communication | M/P/C | Customer and Contact-like references compose from frozen semantics. Relationship Owner remains candidate. |
| CH07 Product Installation and Entitlement | Permission, Policy, Organization; Book 04 Product Installation | P/X | Entitlement can compose from Permission/Policy. Product Installation remains Book 04 authority unless a shared reference proposal is approved. |
| CH08 References and Identity Continuity | Identity, Organization, Common References, Evidence | E/M/P | Stable references and candidate resolution align with frozen contracts. Resolution Candidate remains a profile. |
| CH09 Product, Capability, Workflow and Tool | Capability cross-cutting spec; Workflow Contract; Agent governance | E/M/X | Capability and Workflow distinctions are frozen-compatible. Product and Tool ownership remain outside Core runtime. |
| CH10 Order, Matter, Work Package and Assignment | Order, Matter, Task, Assignment Workflow | M/C | Order and Matter are frozen. Work Package and Assignment as shared objects are candidates. |
| CH11 Evidence, Claim, Decision and Formal State | Evidence, Knowledge, Status Contracts, Human Review, Services | M/P/C | Evidence and state ownership are frozen. Claim and Decision envelopes may be profiles; broader contracts require review. |
| CH12 Projection, Handoff, Return and Correction | Workflow Contracts, Common References, Events, Evidence | P/C/X | Concepts are compatible boundary profiles but are not frozen root objects. Book 03 owns runtime. |
| CH13 Capability Definition | Capability cross-cutting spec; AI governance; Contracts | E/M/P | Durable Capability contract is frozen-compatible; expanded field envelope is explanatory. |
| CH14 Skill, Tool, Service and Implementation Profiles | Capability, Agents, Services, APIs | P/X | Service is frozen; Skill, Tool and Implementation Profile remain implementation or profile concepts. |
| CH15 Proficiency, M-mode and R-tier | AI governance, Human Review, Permission, Policy | C/X | L/M/R vocabularies are not activated frozen controlled values. M-mode runtime belongs Book 03. |
| CH16 Certification, Qualification and Production Authorization | Identity, Permission, Policy, Agent governance | C/P | Credential-like representation may compose; Certification and Production Authorization require formal proposal analysis. |
| CH17 Need Before Opportunity | Opportunity, Customer, Routing, Knowledge | C/P | Opportunity is frozen; Need is not. Need remains F3 candidate. |
| CH18 Opportunity as Potential Value Route | Opportunity Domain/Object/Service/API | E/P | Restates and broadens frozen Opportunity without changing its active contract. Product-local Opportunity profiles remain local. |
| CH19 Engagement as Collaboration Boundary | Partner, Service Network, Service Provider, Routing, Communication | C/P | Frozen collaboration semantics exist, but Engagement as a shared lifecycle is candidate. |
| CH20 Contextual Engagement Roles | Identity, Organization, Permission, Partner, Service Provider | P/C | Contextual roles compose from frozen identity and permission references; controlled role vocabulary remains candidate. |
| CH21 Work Package | Task, Workflow Contract, Assignment Workflow, Evidence | C | A distinct bounded Work Package contract is not frozen and requires Change Proposal analysis. |
| CH22 Assignment | Assignment Workflow, Task, Permission, Policy | C/P | Frozen Assignment Workflow exists; Assignment as a canonical object/lifecycle is not established. |
| CH23 Contribution, Review and Outcome | Evidence, Document, Human Review, Task, Events | C/P | Contribution and Outcome are candidates. Typed Review is strongly supported by frozen Human Review contracts. |
| CH24 Compensation and Settlement | Order, Evidence, Event, Common Audit/Idempotency | P/X/C | Settlement references may compose; custody and financial runtime remain excluded. New compensation lifecycle requires proposal review. |
| CH25 Data References and Refinery Ownership | Common References, Document, Evidence, Event, Knowledge | P/X | Data Product and Refinery are profiles or external implementation concerns, not active frozen root objects. |
| CH26 Knowledge Sources, Documents, Claims and Versions | Knowledge, Document, Evidence, Common Versioning | M/C | Frozen Knowledge exists. Source/Document/Claim/Version decomposition may require a controlled profile or Change Proposal. |
| CH27 Typed Brain Results | Knowledge, Agent, AI governance, Permission, Policy | P/C/X | Typed results are governance profiles. Brain runtime and model behavior remain outside Core. |
| CH28 Data, Knowledge and Brain Separation | Core boundary; Knowledge; Agents; Service ownership | E/M/X | Constitutional separation aligns with frozen responsibility rules and Book 03/04 boundaries. |
| CH29 Purpose-limited Projection | Common References, Permission, Policy, Service Network | P/C/X | Projection is a cross-book profile; visibility does not transfer ownership. Core activation remains unapproved. |
| CH30 Typed Handoff and Return | Workflow Contracts, Events, Evidence, Communication | P/C/X | Boundary contracts are compatible with frozen workflow rules; runtime remains Book 03. |
| CH31 Provider and Contributor | Service Provider, Partner, Agent, Task, Assignment Workflow | P/C | Provider exists as frozen Domain/Object/Service. Contributor is contextual and not an active permanent actor type. |
| CH32 Public, Shared and Product-local Records | Domains, Common References, Permission/Policy, Book governance | E/P/X | Restates shared-contract boundary and keeps Product-local records outside Core. |
| CH33 Version Every Contract and Record | Common Versioning, API Contracts, Status Contracts, Events | E/M | Strong frozen support. Multiple version dimensions are explanatory refinements. |
| CH34 Compatibility, Deprecation and Migration | Versioning, Errors, Validation, Traceability, tests | M/P | Frozen contracts support version and fail-closed behavior; migration governance is expanded publication guidance. |
| CH35 F0–F4 Admission Gate | `BASELINE.md`; Change Proposal mechanism; reconciliation method | E/P | Formalizes the publication reconciliation method without changing the frozen Change Proposal rule. |
| CH36 Ten-year Core Lock | manuscript boundary/principles; governance; baseline | E/M | Closing synthesis of frozen constitutional boundaries. |

## 3. Frozen contract-family disposition

| Frozen family | v2 use | Disposition |
|---|---|---|
| Domain contracts | preserved as responsibility classifications | retained |
| Object contracts | preserved as state and identity definitions | retained |
| Service contracts | preserved as behavior and mutation ownership | retained |
| API contracts | preserved as governed access envelopes | retained |
| Event contracts | preserved as completed-fact and trace records | retained |
| Workflow Contracts | preserved as validation and routing boundaries | retained; runtime reassigned to Book 03 |
| Status Contracts | preserved without renaming values or transitions | retained |
| Common references | expanded through explanatory Reference and Projection discussion | retained plus profiles |
| versioning and errors | expanded into compatibility and migration chapters | retained plus explanatory governance |
| Human Review | expanded into typed Review/Decision distinction | retained plus profile candidates |
| Permission and Policy | expanded into authority and Production Authorization analysis | retained; new authorization types remain candidates |
| AI Context and Agent governance | expanded into Brain-result and Human–AI explanations | retained; no autonomous authority |
| deterministic fixtures | treated as frozen conformance evidence | retained |
| validators | treated as enforcement of approved semantics | retained |

## 4. Candidate-only chapter content

The following v2 terms are not represented as active canonical root objects in the frozen baseline:

```text
Need
Engagement
Work Package
Assignment object
Contribution
Outcome
Professional Authority
Relationship Owner
Delivery Owner
Capability Certification
Production Authorization
Resale Authorization
Brain Result
Data Product
Projection object
Handoff object
Return object
```

Some have close frozen analogues, profiles or workflow records. Similarity does not authorize semantic identity.

## 5. Cross-book content

The following v2 explanations rely on accepted post-freeze architecture and must not be back-written into Book 02 without governance:

- Workplace business sovereignty;
- Product Installation;
- cross-Product Projection;
- Book 03 Implementation Binding, Assignment runtime, Review, Approval, Apply and Reconciliation;
- MarkReg-specific lifecycle and provider packages;
- Lite-specific content, marketplace and Opportunity profiles;
- Knowledge staging and Brain implementation architecture.

These may remain publication reconciliation context while the frozen Core stays unchanged.

## 6. Disposition verdict

```text
Frozen meaning contradicted by v2 chapter: NONE IDENTIFIED
Frozen lifecycle silently replaced: NO
Frozen Object silently renamed: NO
Candidate presented as active Core: NO
Cross-book runtime moved into Core: NO
Chapters requiring candidate Change Proposal analysis: YES
Frozen replacement authorized: NO
```

The v2 manuscript is therefore best classified as a publication-grade explanatory and candidate layer over `B02-BASELINE-V0.1`, not a new Core baseline.
