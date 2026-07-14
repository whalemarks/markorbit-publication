# B05-PLN-0002 — Dependency Map

## 1. Dependency Rule

Book 05 consumes the Books 01–04 Portfolio Baseline.

It does not reinterpret that baseline merely because a Product journey would be easier to describe with looser language.

## 2. Book Dependencies

### Book 01 — Why and Principles

Book 01 supplies:

- the industry-level need for shared operating infrastructure;
- the Operating System position;
- the independent Orbit principle;
- the distinction between organization improvement and industry infrastructure;
- the principle that organizations retain clients, data, Knowledge, relationships, and responsibility.

### Book 02 — Shared Meaning

Book 02 supplies the Frozen Core semantics, including shared identity, Customer, Brand, Trademark, Order, Matter, Task, Document, Evidence, Communication, Routing, Capability, Knowledge, Event, responsibility, service, and contract concepts.

Book 05 must consume these concepts through their accepted contracts. Product screens and Product-local state do not redefine them.

### Book 03 — Governed Work

Book 03 supplies:

- Execution Context;
- Workflow coordination;
- Task lifecycle;
- Review and approval;
- permission and Policy gates;
- Communication execution;
- Event trace;
- application preparation;
- provider Routing preparation;
- office action response preparation;
- renewal preparation;
- assignment preparation;
- evidence review preparation;
- idempotency, retry, safe failure, and observability.

Book 05 describes how the Product uses these patterns. It does not create a second Execution System.

### Book 04 — Organization Context and Product Composition

Book 04 supplies:

- Workplace as the operating environment of the Organization Orbit;
- Product independence;
- authorized context;
- private Knowledge and data boundaries;
- Assistant, Guide, and AI Agent boundaries;
- Candidate Before Canonical;
- Prepared Action and Human Review handoffs;
- Artifact, Document, Render, Delivery, Publish, Formalization, and Outcome boundaries;
- private-first MGSN interfaces;
- cross-Product lifecycle continuity.

Book 05 must conform to the MarkReg architectural profile in B04-CH-24.

## 3. Canonical Product Dependencies

```text
Organization and Workplace context
        ↓
MarkReg Product journey
        ↓
Prepared Action, Artifact, and Review
        ↓
Book 03 governed Execution
        ↓
Owning Service, connector, provider, or external system
        ↓
Official or formal outcome
        ↓
MarkReg projection and Workplace continuity
```

## 4. MGSN Dependency

Book 07 will define the full network architecture.

Book 05 may define only the MarkReg-side need and handoff:

```text
Capability Need
→ private partner check
→ candidate discovery
→ evidence and comparison
→ Human Selection
→ appointment preparation
→ approval where required
→ governed instruction
→ provider acceptance
```

## 5. Jurisdiction and Knowledge Dependencies

MarkReg consumes versioned jurisdiction Knowledge and Product configuration.

Every recommendation should preserve, where applicable:

- source;
- jurisdiction;
- effective or checked date;
- rule version;
- assumptions;
- confidence;
- alternatives;
- professional review requirement.

## 6. Product-Owned State Boundary

MarkReg may own Product-specific state such as:

- recommendation session;
- option comparison;
- intake progress;
- missing-information view;
- filing-package preparation state;
- Product navigation and presentation preferences.

It must reference rather than duplicate formal Core and Execution objects where shared meaning or authority is required.

## 7. Upstream Finding Protocol

A Book 05 finding is classified as:

```text
Product-specific decision
→ resolve inside Book 05

Upstream editorial correction
→ record for a separate upstream editorial task

Upstream Change Proposal
→ use the applicable Book 02, Book 03, or Book 04 governance path
```

No upstream change is currently required.
