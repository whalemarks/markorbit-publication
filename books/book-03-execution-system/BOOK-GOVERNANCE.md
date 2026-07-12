# Book 03 Governance

## 1. Purpose

Book 03 defines how approved Book 02 Core contracts become governed operational execution.

It may define execution coordination, context assembly, Workflow behavior, Task handoff, Human Review, Communication preparation, gate evaluation, retry governance, safe failure, version control, agent assistance and audit.

It must not redefine Core architecture or Product behavior.

## 2. Source Precedence

The source-of-truth order is:

```text
1. Approved Book 02 and Book 03 canonical manuscripts
2. Approved architecture and review decisions
3. Approved exports from markorbit-core
4. Approved fixtures and validators
5. Tests expressing approved acceptance criteria
6. Implementation code
7. Code comments and assumptions
```

Lower levels must not silently redefine higher levels.

## 3. Layer Boundary

```text
Core defines.
Execution coordinates.
Integration connects.
Products consume.
Humans review.
AI assists.
Owning Services mutate.
Events trace.
```

### Core

Owns canonical Domains, Objects, Services, contracts, controlled values and authoritative state.

### Execution

Owns coordination, context assembly, gates, preview, allowed apply, Service delegation, safe failure and audit correlation.

### Integration

Owns controlled external transport and provider-specific behavior.

### Product

Owns user journeys, presentation and interaction. Product must consume, not invent, Execution semantics.

## 4. Canonical Terminology

Use these forms consistently:

| Preferred term | Editorial rule |
|---|---|
| Core, Execution, Integration, Product | Capitalize when referring to architecture layers |
| Workflow, Task, Communication, Event, Service | Capitalize when referring to governed MarkOrbit concepts |
| Human Review, Permission, Policy | Capitalize as governance primitives |
| owning Service | Capitalize Service |
| preview, apply | Lower-case in prose; use code formatting when operation names need emphasis |
| protected action | Lower-case |
| Human–AI | Use an en dash |
| AI assistant, agent | Lower-case except at sentence start or in titles |
| Event trace | Capitalize Event when referring to the governed concept |
| professional truth | Lower-case |
| Product UI / Product surface | Product remains capitalized |
| Depth A, Depth B, Depth C | Book 03 MVP governance labels only |

Avoid competing variants unless quoting an external source.

## 5. Execution Authority

Book 03 must preserve:

- preparation is not approval;
- approval is not authorization for unrelated action;
- approval is not execution;
- internal preparation is not external effect;
- a Task plan is not an active Task;
- draft is not send;
- send is not delivery;
- capability is not authority;
- AI confidence is not Human Review;
- Workflow observation is not a Domain Event.

## 6. AI and Agent Boundary

AI assistants and agents may prepare, extract, summarize, compare, draft and identify gaps.

They may not independently:

- approve or reject;
- satisfy Human Review or quorum;
- send or submit;
- pay;
- engage or instruct a provider;
- mutate protected state;
- bypass Permission or Policy;
- emit governed Events;
- define professional truth.

## 7. MVP Boundary

Current workflow depth is fixed by Chapters 31–33:

- Depth A: Intake, Application Preparation and Communication Review — approved internal apply only.
- Depth B: Provider Routing, Office Action Response, Renewal, Assignment and Evidence Review — preview only.
- Depth C: external send, filing, payment, provider commitment, recordal and autonomous professional action — deferred.

Product design, connector availability or AI capability may not expand this depth.

## 8. Editorial Rules

- Define a concept fully once, then use the canonical term and cross-reference.
- Keep chapter-specific boundary statements; avoid repeating the entire global non-goal list.
- Use tables for distinctions and matrices.
- Use code blocks only for durable rules, execution paths or boundary locks.
- Preserve Book 02 dependency links, but do not treat a missing standalone link as authority to invent a contract.
- Historical review records remain historical and should not be rewritten to reflect later status.
- Appendices provide terminology and cross-book navigation; they do not create new Core contracts.

## 9. Change Control

Review is required before any change that:

- adds a workflow;
- changes workflow depth;
- adds an allowed mutation;
- enables external action;
- changes Human Review;
- changes Service or Event ownership;
- introduces a new Core concept;
- expands agent tools or authority;
- activates a production connector;
- changes the MVP release gate.

## 10. Codex Boundary

Codex may scaffold, organize, validate, implement approved tasks and prepare review materials.

Codex must not:

- define new architecture without approval;
- expand MVP scope;
- resolve professional truth;
- approve protected action;
- send, file, pay or engage providers;
- mutate state outside owning Services;
- start the next acceptance task in the same pull request without approval.
