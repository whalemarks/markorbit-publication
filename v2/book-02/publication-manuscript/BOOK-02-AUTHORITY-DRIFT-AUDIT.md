# Book 02 — Authority Drift Audit

## 1. Audit question

This audit asks whether the v2 publication reconstruction or current `markorbit-core` engineering baseline silently changes the frozen allocation of authority.

The frozen traceability lock is:

```text
Domains define responsibility areas.
Objects describe state.
Services own behavior.
API Contracts expose governed access.
Events preserve trace.
Workflows coordinate execution.
Workflow Contracts constrain execution.
Agents assist within governed boundaries.
Codex implements traced specifications.
```

The v2 publication lock is:

```text
Core defines shared meaning.
Workplace preserves business sovereignty.
Owning Services establish formal state.
Book 03 Execution governs work.
Professional and official authority remain external where required.
```

## 2. Audit dimensions

The audit separates:

```text
Business Sovereignty
Semantic Authority
Formal-state Authority
Physical Custody
Legal / Evidentiary / Professional Authority
```

A system may hold one dimension without holding the others.

## 3. Findings matrix

| Area | Frozen baseline | v2 / engineering interpretation | Drift finding |
|---|---|---|---|
| Core semantic authority | Book 02 defines Core Domains, Objects, Services and Contracts. | v2 keeps Core as shared semantic constitution. | no drift identified |
| business decisions | business responsibility remains outside Core. | Workplace and Product retain policy and commercial decisions. | clarification, not drift |
| formal-state mutation | owning Services own behavior and mutation. | v2 explicitly assigns formal-state authority to Owning Services. | reinforced |
| Workflow authority | Workflows coordinate; Workflow Contracts validate and route; no direct mutation. | Book 03 owns execution runtime, Review, Approval, Apply and Reconciliation. | reinforced; runtime moved out of Core |
| Events | completed-fact trace, not command. | v2 treats Return and Event evidence as non-canonical until validation. | compatible |
| AI / Agents | governed assistance; forbidden protected actions. | Brain results remain typed, candidate and non-canonical. | reinforced |
| Permission / Policy | gate protected behavior. | v2 separates permission from professional authority and task Assignment. | compatible; new terms remain candidate |
| Human Review | required for protected or uncertain work. | v2 separates Review, Decision, Approval and Apply. | explanatory expansion |
| Customer relationship | frozen Customer/Partner/Communication semantics. | v2 adds Relationship Owner as contextual candidate role. | no active drift; proposal needed before activation |
| Provider | frozen Service Provider Domain/Object/Service. | v2 distinguishes Provider Organization, responsible professional and Contributor. | compatible profile clarification |
| Knowledge | frozen Knowledge Domain/Object/Service/API. | v2 decomposes Source, Document, Claim and Version conceptually. | potential semantic expansion; no active drift |
| Task / Assignment | frozen Task and Assignment Workflow. | v2 proposes Work Package and Assignment object/lifecycle. | high proposal risk; not activated |
| Opportunity / Need | frozen Opportunity. | v2 introduces Need before Opportunity. | candidate addition; no active drift |
| Product / Workplace | implementation architecture redirected to Book 04. | v2 references Workplace sovereignty and Product Installation. | external dependency, not frozen change |
| payment | Order and Evidence references; no custody authority. | v2 states orchestration is not custody. | reinforced |

## 4. High-risk name collisions

### 4.1 Task versus Work Package

Frozen Core contains Task as a business-execution Domain/Object/Service/API.

The v2 manuscript describes Work Package as a bounded, implementation-neutral production contract.

```text
Task
≠ Work Package by assertion
```

Possible outcomes:

- Work Package is an F1 composition of Task, Workflow Contract, Evidence and Permission;
- Work Package is an F2 Task profile;
- Work Package is an F3 new shared contract;
- Work Package changes Task meaning and becomes F4.

Until decided, implementation must not rename Task or introduce Work Package as an equivalent public export.

### 4.2 Assignment Workflow versus Assignment object

The frozen baseline contains an Assignment Workflow and Workflow Contract. It does not by that fact establish a canonical Assignment Object.

```text
workflow named Assignment
≠ canonical Assignment lifecycle object
```

Creating offer, acceptance, suspension, expiry and revocation fields in Core would require field-level governance.

### 4.3 Service Provider versus Provider role

The frozen baseline models Service Provider as a Domain/Object/Service. The v2 manuscript often uses Provider as an Organization profile or Engagement role.

Potential drift occurs if one implementation treats every contributor as a Service Provider or every Provider employee as professionally authorized.

Required lock:

```text
Provider Organization
≠ Responsible Professional
≠ Contributor
≠ Professional Authority
```

### 4.4 Knowledge object versus Claim system

Frozen Knowledge has Domain/Object/Service/API contracts. The v2 Source–Document–Claim–Version model may be:

- an internal Knowledge representation;
- several profiles;
- a new set of Core Objects.

The manuscript currently labels it as explanatory/candidate. Engineering must not split the frozen Knowledge Object publicly without a proposal and migration plan.

### 4.5 Agent versus Brain

Frozen Agent contracts govern assisted behavior. Brain is a later architectural layer that produces Retrieval, Inference, Recommendation, Candidate and Explanation results.

```text
Agent
≠ Brain
≠ model
≠ professional actor
```

No drift is present while Brain remains outside the frozen Core and its results remain non-canonical.

### 4.6 Opportunity versus Need

Frozen Opportunity is active. Need is a new pre-route concept.

Implementing `Need` as an alias for Opportunity would erase the distinction the v2 manuscript is trying to preserve. Implementing it as a new root object would expand frozen scope.

Both choices require governance.

## 5. Workplace sovereignty dependency

The frozen baseline predates the fuller Workplace sovereignty model later accepted in Book 04 and the Architecture Canon.

A later architecture assessment already considered whether Workplace sovereignty required a Book 02 Change Proposal. The current v2 manuscript treats Workplace as a business-sovereignty boundary without rewriting frozen Core.

The safe rule remains:

```text
Workplace business sovereignty
≠ Core semantic authority
≠ Owning Service formal-state authority
```

If Core must exchange a stable Workplace reference, the proposal should add only the minimum reference contract required for interoperability rather than importing Book 04 Product policy.

## 6. Engineering drift checks

The current `markorbit-core` package states:

- it implements Book 02;
- it is not MarkReg, Lite, Book 03 or Book 04;
- it has no production database or external connectors;
- it does not grant AI approval authority;
- the full Workflow Runtime is excluded;
- production readiness is not accepted.

These statements align with the frozen authority model.

The current package export boundary also separates public contracts from internal source files. No evidence was identified that a v2 candidate has been added to the public package as an approved canonical contract.

## 7. Historical-status documentation risk

The engineering repository contains accumulated task-history statements, some of which describe earlier incomplete states after the top-level current state reports semantic completion.

This can cause readers to select the wrong authority snapshot.

Risk classification:

```text
Documentation clarity risk
not semantic authority drift by itself
```

Recommended repair is meaning-preserving documentation consolidation.

## 8. Drift alarms for future PR review

A future PR should be treated as possible authority drift when it:

- adds a candidate term to the public Core export map;
- changes a frozen Object or Service name;
- adds a lifecycle without a Change Proposal;
- lets Workflow or Agent mutate parent state directly;
- converts Return or model output into official truth;
- treats Membership, Entitlement or Certification as task authority;
- treats Provider listing as appointment;
- grants AI professional or payment authority;
- moves Product pricing, ranking or UI policy into Core;
- changes a status matrix or required field without migration evidence.

## 9. Audit verdict

```text
Active semantic authority drift identified: NO
Candidate pressure against frozen scope: YES
Highest-risk candidate cluster: Work Package / Assignment / Outcome / Professional Authority
Workplace sovereignty contradiction identified: NO
Book 03 runtime absorbed into Core: NO
AI authority expansion identified: NO
Payment custody expansion identified: NO
Formal Change Proposals required before candidate activation: YES
```

The publication manuscript is currently safe because it repeatedly labels new concepts as candidate, profile or external boundary. That safety depends on preserving those labels through implementation and future editorial work.
