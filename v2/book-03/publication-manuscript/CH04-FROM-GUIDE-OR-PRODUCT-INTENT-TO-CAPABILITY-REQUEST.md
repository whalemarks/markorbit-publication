# Chapter 04 — From Guide or Product Intent to Capability Request

Users do not think in execution contracts. They think in goals:

- “Help me choose the right countries.”
- “Prepare this application.”
- “Review whether this evidence is enough.”
- “Find a suitable Provider.”
- “Send the client an update.”
- “Create a marketing pack for this trademark.”

A professional operating system must accept these natural expressions without treating them as immediate authorization to act.

The bridge between human intent and governed work is the **Capability Request**.

## 1. Why a prompt is not an execution request

A prompt can be ambiguous, incomplete and exploratory. That is often appropriate during conversation. It is not sufficient for consequential work.

The instruction:

> File this trademark in the United States.

may leave unresolved:

- who the applicant is;
- which mark version is intended;
- which goods are included;
- what filing basis applies;
- whether the customer approved the cost;
- whether a search or professional review was completed;
- who is permitted to sign;
- which Provider or attorney is appointed;
- what Evidence must be returned;
- whether the user is asking for a quote, preparation or immediate filing.

An AI system may infer some facts. It must not silently convert inference into authority.

```text
Natural-language Intent
≠ Complete Capability Request
≠ Customer Instruction
≠ Protected-action Approval
```

## 2. Guide, Product, Context Compiler and Execution have different jobs

### Guide

Guide helps a person understand a situation, reduce uncertainty and make decisions. It may ask high-value questions, retrieve rules, explain trade-offs, recommend routes and identify missing facts.

Guide does not become Workflow merely because the conversation is multi-step. It does not gain authority merely because the user follows its advice.

### Product

A Product frames the domain experience. Lite may help create content or qualify a commercial opportunity. MarkReg may guide service selection and formal intake. Sites may capture a public request.

A Product may initiate a request. It cannot invent authority that belongs to a Workplace, customer, professional or Owning Service.

### Context Compiler

The Context Compiler turns approved and source-attributed context into the bounded execution context needed for one request.

It may resolve:

- represented Workplace and role;
- Product Installation and entitlement;
- current Capability versions;
- confirmed facts and authorized reuse;
- relevant Data and Knowledge references;
- active policy and jurisdiction scope;
- memory permissions;
- risk, deadline and commercial constraints;
- unresolved contradictions and Unknowns.

The Context Compiler does not create new facts, confirmation or authority. It assembles an attributable context package.

### Execution

Execution receives a sufficiently structured request and governs how the requested outcome may be produced, composed, reviewed, approved, applied and evidenced.

```text
Guide explains and prepares
Product frames the experience
Context Compiler assembles bounded context
Execution governs the work
Owning Service validates formal state
```

These roles may appear through one interface. Their semantic responsibilities remain distinct.

## 3. Capability Request as the entry contract

A Capability Request binds the intended outcome to the conditions under which work may begin.

A robust request may contain:

```text
Capability identifier and version
Requester and represented role
Workplace and Product Installation
Purpose and expected Outcome
Input references and exact versions
Context Package reference
Jurisdiction and procedure
Risk and control tier
Entitlement and Data scope
Required Professional Qualification
Review policy
Allowed implementation classes
Deadline and urgency
Commercial constraints
Capability Budget
Memory and learning policy
Expiry, cancellation and revocation policy
```

The interface does not need to expose all fields at once. Fields may be derived or inherited under explicit policy. The request must preserve the difference among confirmed facts, authorized reuse, source-derived Candidates, inference, Recommendation and Unknown.

## 4. The request is for an outcome, not a performer

A calling Product should generally request the required Capability or Outcome rather than hard-code who must perform it.

```text
Requested Outcome:
Review the proposed goods list for filing readiness
under the stated jurisdiction and selected strategy.
```

Execution can then evaluate permitted implementations:

- deterministic validation;
- AI-assisted normalization;
- certified Contributor preparation;
- internal team review;
- qualified professional approval;
- hybrid production.

A customer may require a named lawyer. A Workplace may require an existing Provider. A conflict rule may exclude certain performers. These are request constraints, not reasons to collapse Capability into one permanent implementation.

```text
Capability
≠ one Tool
≠ one model
≠ one Person
≠ one Provider
```

## 5. Request construction from progressive understanding

A request often develops through several stages:

```text
Unstructured Intent
→ Extracted Facts
→ Candidate Interpretation
→ Material Clarification
→ Route Recommendation
→ User or Professional Decision
→ Capability Request Candidate
→ Context Compilation
→ Validation
```

At each stage, the system should retain epistemic status.

```text
Country: United States
Status: User-confirmed

Primary Goods: pet shampoo and grooming products
Status: User-confirmed business description

Likely Class: 3
Status: AI inference, professional review required

Mark Type: word mark
Status: Candidate assumption, user confirmation required
```

This allows the experience to remain conversational without turning hidden assumptions into filing data.

## 6. Few questions, high information gain

The goal is not to force users through long forms. It is to ask only questions that materially change route, authority, cost, disclosure or risk.

High-value questions include:

- Are you seeking information, preparation, review or formal execution?
- Who should own or apply for the right?
- Which mark version must be used?
- Which countries and goods are essential?
- Is there an official notice or deadline?
- Has the customer approved the commercial scope?
- Does the actor have authority to instruct the service?
- Are original, notarized or legalized documents available?
- Is an existing Provider relationship required?

The interface may explain what an answer changes, whether it can be deferred, which assumption would otherwise apply and who must confirm it.

## 7. Request validation occurs before composition or Assignment

Once a Capability Request Candidate exists, Execution validates whether work may proceed.

Validation may check:

- mandatory inputs are present;
- references resolve to current versions;
- requester and represented role are known;
- Workplace and Product Installation permit the Capability;
- purpose and Data use are allowed;
- expected Outcome is sufficiently bounded;
- risk and review policies are resolved;
- deadline is feasible;
- dependencies are available;
- prohibited actions are not embedded;
- commercial prerequisites are clear;
- Capability version remains active.

An invalid request should fail or return for clarification before composition or Assignment.

```text
Request accepted for validation
≠ Request validated
≠ Capability composed
≠ Work assigned
```

## 8. Capability Request does not replace Workflow

A Capability Request expresses a governed need for an Outcome. A Workflow coordinates how a broader goal progresses through stages.

A renewal Workflow may invoke separate Capabilities for deadline verification, Evidence review, document preparation, customer communication and formal submission.

A complex request may instantiate a bounded Workflow after validation. A deterministic validation request may require no elaborate Workflow.

```text
Capability Request ≠ Workflow
Workflow ≠ Capability
```

## 9. Composition is a bounded runtime decision

Some validated requests need only one Capability. Others require a controlled composition.

The default composition pattern is:

```text
one Primary Capability
+ zero to three Supporting Capabilities
+ zero or one Critic Capability
+ Capability Budget
+ explicit Conflict handling
```

The Primary Capability owns the main decision structure. Supporting Capabilities answer bounded decision nodes. A Critic Capability examines a declared risk or assumption.

The Capability Budget may limit:

- active Capability count;
- context size;
- Tool calls;
- time and cost;
- review burden;
- escalation depth.

The purpose is to avoid two opposite errors: using one method for every problem and loading so many methods that the result becomes noisy, contradictory and unauditable.

```text
more Capabilities loaded
≠ better answer

Capability Composition
≠ Professional Authority
≠ Approval to act
```

## 10. Conflict must remain visible

Source or Composite Capabilities may disagree.

One method may optimize for speed. Another may prioritize reversibility. One source may assume abundant capital. Another may assume scarcity. One legal source may describe formal rules while local practice produces exceptions.

A composition record should preserve:

- competing recommendations;
- assumptions and scope;
- supporting Evidence;
- consequences of each route;
- resolution authority;
- selected route and rationale;
- unresolved Unknowns.

The model should not average incompatible methods into false consensus.

## 11. Request, Composition and Assignment remain separate

After validation and, where needed, composition, the system still determines who or what is eligible.

```text
Validated Capability Request
→ Composition Plan
→ Eligibility Evaluation
→ Implementation Candidate Set
→ Route Recommendation
→ Selection
→ Assignment or Invocation
```

A Person can be capable but unavailable. A Provider can be listed but conflicted. A model can be technically suitable but prohibited for the Data. A Contributor can be certified but not authorized for independent production.

## 12. Requests are versioned and expirable

A request may become stale when inputs, deadline, scope, fees, mark, applicant, conflict, implementation, policy or supporting Knowledge changes.

Execution should preserve request versions and define revalidation triggers.

```text
Capability Request v1 validated
≠ Capability Request v2 validated
```

This is critical when an earlier version supported an Assignment, approval or Provider instruction.

## 13. Session Receipt

Each consequential execution session should produce a bounded Session Receipt.

The Receipt may preserve:

- request and Capability versions;
- compiled Context Package;
- Composition Plan and conflicts;
- selected Skills, implementations and Tools;
- source references;
- material model and policy versions;
- human decisions and review dispositions;
- Action and Invocation evidence;
- Outcome status and Unknowns;
- Capability Budget used;
- learning and memory disposition.

```text
Session Receipt
≠ raw conversation archive
≠ formal state
≠ automatic Reflection
```

Its purpose is reconstruction: what context and versions were used, what happened, who decided and what may safely proceed next.

## 14. Cancellation and revocation begin at the request boundary

The requester or authorized actor may cancel before work begins. Once work is assigned or external action occurs, cancellation may require compensation review, Data-access revocation, Provider recall, Matter correction and Evidence retention.

Revocation ends future authority. It does not erase historical Evidence.

## 15. Learning handoff remains separate from runtime

A completed session may produce Evidence for future learning, but runtime does not rewrite the Capability.

A controlled handoff may create:

```text
Outcome and Session Receipt
→ Reflection Candidate
→ Case or Principle Candidate
→ Capability Change Proposal
```

The user or authorized reviewer should confirm material Reflection. Rights, confidentiality and de-identification must be resolved before broader reuse.

```text
Outcome ≠ automatic Capability upgrade
Session Receipt ≠ shared learning permission
```

## 16. Three bounded examples

### AI-assisted customer update

```text
Capability:
Draft customer status update

Outcome:
A factual email draft based on validated Matter events

Mode:
AI assist

Restrictions:
No sending, no new legal conclusion, no fee commitment

Review:
Relationship Owner review required
```

### Evidence review preparation

```text
Capability:
Prepare use-evidence Candidate set

Outcome:
Organized Evidence matrix for professional sufficiency review

Restrictions:
Contributor may not decide final legal sufficiency

Review:
Qualified professional required
```

### Provider filing execution

```text
Capability:
Submit approved filing package and return official Evidence

Inputs:
Exact approved package version

Requirements:
Provider Appointment, Acceptance, cost approval,
Professional Authority and idempotency key

Evidence Contract:
Official receipt, application number and fee Evidence
```

The three requests may appear inside one customer journey. They remain separate governed actions.

## 17. The entry-boundary principle

> Natural intent should be easy to express, but consequential work should begin only through a validated Capability Request that preserves context, versions, scope, authority, composition and Evidence requirements.

This principle allows MarkOrbit to be conversational without becoming casual about execution.