# Chapter 04 — From Guide or Product Intent to Capability Request

Users do not think in execution contracts. They think in goals:

- “Help me choose the right countries.”
- “Prepare this application.”
- “Review whether this evidence is enough.”
- “Find a suitable provider.”
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
- which provider or attorney is appointed;
- what evidence must be returned;
- whether the user is asking for a quote, preparation or immediate filing.

An AI system may infer some of these facts. It must not silently convert inference into authority.

```text
Natural-language Intent
≠ Complete Capability Request
≠ Customer Instruction
≠ Protected-action Approval
```

## 2. Guide, Product and Execution have different jobs

### Guide

Guide helps a person understand a situation, reduce uncertainty and make decisions. It may:

- ask high-value questions;
- retrieve rules and options;
- explain trade-offs;
- recommend routes;
- identify missing facts;
- prepare structured choices.

Guide does not become Workflow merely because the conversation is multi-step. It does not gain authority merely because the user follows its advice.

### Product

A Product provides the domain experience. Lite may help create content or qualify a commercial opportunity. MarkReg may guide service selection and formal intake. Sites may capture a public request. The Product determines what the user sees and which capabilities are available in that installation.

A Product may initiate a request, but it should not invent authority that belongs to a Workplace, customer, professional or Owning Service.

### Execution

Execution receives a sufficiently structured request and governs how the requested outcome may be produced, reviewed, approved, applied and evidenced.

```text
Guide explains and prepares
Product frames the experience
Execution governs the work
Owning Service validates formal state
```

These roles may be tightly integrated in the user interface, but their semantic responsibilities remain distinct.

## 3. Capability Request as the entry contract

A Capability Request binds the intended outcome to the conditions under which work may begin.

A robust request may contain:

```text
Capability identifier and version
Requester
Represented Workplace and role
Product Installation
Purpose
Expected Outcome
Input references and exact versions
Jurisdiction and procedure
Risk classification
Entitlement
Data and disclosure scope
Required professional qualification
Review policy
Allowed implementation bindings
Deadline and urgency
Commercial constraints
Memory and learning policy
Expiry, cancellation and revocation policy
```

The request does not need to expose all of this complexity to the user. The system may derive or inherit fields under explicit policy. It must preserve the distinction among confirmed facts, authorized reuse, source-derived candidates, inference, recommendation and Unknown.

## 4. The request is for an outcome, not a performer

A calling Product should generally request the required Capability or Outcome rather than hard-code who must perform it.

For example:

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

There are legitimate exceptions. A customer may require a named lawyer. A Workplace may use an existing Provider. A conflict rule may exclude certain performers. These are request constraints, not reasons to collapse Capability into one permanent implementation.

```text
Capability
≠ One Tool
≠ One Model
≠ One Person
≠ One Provider
```

This abstraction allows implementations to improve while keeping the promised outcome and governance stable.

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
→ Validation
```

At each stage, the system should retain the epistemic status of the information.

For example:

```text
Country: United States
Status: User-confirmed

Primary Goods: pet shampoo and grooming products
Status: User-confirmed business description

Likely Class: 3
Status: AI inference, professional review required

Mark Type: word mark
Status: candidate assumption, user confirmation required
```

This allows the experience to remain conversational while preventing hidden assumptions from becoming filing data.

## 6. Few questions, high information gain

The goal is not to force users through long forms. It is to ask only the questions that materially change the route, authority, cost or risk.

High-value clarification questions include:

- Are you seeking information, preparation, review or formal execution?
- Who should own or apply for the right?
- Which mark version must be used?
- Which countries and goods are essential?
- Is there an official notice or deadline?
- Has the customer approved the commercial scope?
- Does the actor have authority to instruct the service?
- Are original, notarized or legalized documents available?
- Is an existing Provider relationship required?

Each question should have a reason. The interface can explain:

- what the answer changes;
- whether the question can be deferred;
- what assumption would otherwise apply;
- who must confirm it;
- whether professional advice is required.

This is more intelligent than either a blank prompt or a rigid universal form.

## 7. Request validation occurs before assignment

Once a Capability Request candidate exists, Execution validates whether work may proceed.

Validation may check:

- mandatory inputs are present;
- references resolve to current versions;
- requester and represented role are known;
- Workplace and Product Installation permit the Capability;
- the purpose is allowed;
- data use and disclosure are within scope;
- the expected outcome is sufficiently bounded;
- risk and review policies are resolved;
- the deadline is feasible;
- prohibited actions are not embedded;
- dependencies are available;
- commercial prerequisites are clear.

An invalid request should fail or return for clarification before assignment. It should not become an informal exception that the assignee must discover later.

```text
Request Accepted for Validation
≠ Request Validated
≠ Work Assigned
```

## 8. Capability Request does not replace Workflow

A Capability Request expresses a governed need for an outcome. A Workflow coordinates how a broader goal may progress through stages. The relationship can take several forms.

### One request within a Workflow

A renewal Workflow may invoke separate Capabilities for deadline verification, evidence review, document preparation, customer communication and formal submission.

### A request that creates a bounded Workflow

A complex request may instantiate a Workflow template after validation.

### A request fulfilled without a multi-step Workflow

A deterministic data validation Capability may execute as a bounded operation with review and evidence but no elaborate Workflow.

Therefore:

```text
Capability Request
≠ Workflow

Workflow
≠ Capability
```

The first defines what governed outcome is requested. The second coordinates a goal and its stages.

## 9. Capability Request does not equal Assignment

After validation, the system still needs to determine who or what is eligible.

```text
Validated Capability Request
→ Eligibility Evaluation
→ Implementation Candidate Set
→ Route Recommendation
→ Selection
→ Assignment or Invocation
```

A person can be capable but unavailable. A Provider can be listed but conflicted. An AI model can be technically suitable but prohibited for the data. A Contributor can be certified but not authorized for independent production.

The request should therefore avoid naming an assignee unless the route has already been properly selected and constrained.

## 10. Requests are versioned and expirable

A request may become stale when:

- inputs change;
- a deadline passes;
- the customer changes scope;
- fees change materially;
- the selected mark or applicant changes;
- a new conflict appears;
- the implementation version is withdrawn;
- the Product policy changes;
- the supporting Knowledge becomes stale.

Execution should preserve request versions and define revalidation triggers.

```text
Capability Request v1 Validated
≠ Capability Request v2 Validated
```

This is critical when approvals or assignments were based on the earlier version.

## 11. Cancellation and revocation start at the request boundary

The requester or authorized actor may cancel a request before work begins. Once work is assigned or external action occurs, cancellation becomes more complex.

Execution must determine:

- whether an Assignment was accepted;
- whether work or review was performed;
- whether compensation is earned;
- whether data access must be revoked;
- whether external disclosure occurred;
- whether a Provider can be recalled;
- whether the underlying Matter needs correction;
- which evidence must remain.

Revocation ends future authority. It does not erase historical evidence.

## 12. Examples of correctly bounded requests

### AI-assisted customer update

```text
Capability:
Draft customer status update

Outcome:
A factual email draft based on validated Matter events

Mode:
M2 AI assist

Restrictions:
No sending, no new legal conclusion, no fee commitment

Review:
Relationship Owner review required
```

### Evidence review preparation

```text
Capability:
Prepare use-evidence candidate set

Outcome:
Organized evidence matrix for professional sufficiency review

Restrictions:
Contributor may not decide final legal sufficiency

Review:
Qualified professional required
```

### Provider filing execution

```text
Capability:
Submit approved filing package and return official evidence

Inputs:
Exact approved package version

Requirements:
Provider appointment, acceptance, cost approval,
professional authority and idempotency key

Evidence Contract:
Official receipt, application number and fee evidence
```

The three requests may appear inside one customer journey. They remain different governed actions.

## 13. The entry-boundary principle

> Natural intent should be easy to express, but consequential work should begin only through a validated Capability Request that preserves context, scope, authority and evidence requirements.

This principle allows MarkOrbit to be conversational without becoming casual about execution.
