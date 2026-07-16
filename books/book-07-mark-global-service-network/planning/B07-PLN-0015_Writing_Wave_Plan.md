# B07-PLN-0015 — Writing Wave Plan

## Status

```text
Candidate — executable only after Owner acceptance of B07-TOC-V0.1
```

## Wave Structure

### Wave 1 — Constitution and Network Identity

```text
B07-CH-00–B07-CH-06
```

Focus: reader orientation, Product constitution, managed-network identity, Workplace sovereignty, participants, connection and portability.

### Wave 2 — Supply Formation

```text
B07-CH-07–B07-CH-11
```

Focus: Provider Profile, Capability, Evidence, Verification, multi-provider portfolios, service packages and admission.

### Wave 3 — Procurement and Commercial Offers

```text
B07-CH-12–B07-CH-15
```

Focus: aggregated demand, procurement, cost layers, offers, price changes and routing neutrality.

### Wave 4 — Routing and Choice

```text
B07-CH-16–B07-CH-20
```

Focus: Capability Need projection, R1–R3, eligibility, Candidate Route Set, recommendation, bounded alternatives, user disposition and Provider Acceptance.

### Wave 5 — Funds, Fulfillment and Return

```text
B07-CH-21–B07-CH-25
```

Focus: Network Engagement, funds checkpoints, milestones, Evidence, incidents, replacement and typed Return.

### Wave 6 — Trust and Governance

```text
B07-CH-26–B07-CH-29
```

Focus: Relationship Provenance, introductions, Trust, network learning, disputes, suspension, retirement and appeals.

### Wave 7 — MVP and Evolution

```text
B07-CH-30–B07-CH-33
```

Focus: MVP 0, journeys/scenarios, cross-product boundaries, implementation prerequisites and the global capability flywheel.

## Branching Rule

Use one branch per coherent Writing Wave, not one branch per chapter.

Candidate branch pattern:

```text
agent/book-07-writing-wave-1-ch00-06
agent/book-07-writing-wave-2-ch07-11
agent/book-07-writing-wave-3-ch12-15
agent/book-07-writing-wave-4-ch16-20
agent/book-07-writing-wave-5-ch21-25
agent/book-07-writing-wave-6-ch26-29
agent/book-07-writing-wave-7-ch30-33
```

## Chapter Acceptance Rule

Each chapter must include:

- controlled chapter metadata;
- chapter purpose;
- reader-facing explanation;
- Product and authority boundaries;
- relevant controlled IDs and distinctions;
- one or more operational examples;
- failure and unknown-state handling where relevant;
- chapter conclusion;
- no implementation claims beyond the accepted Baseline.

## Wave Review Rule

Every Wave PR must confirm:

```text
chapter count complete
controlled IDs covered
no upstream redefinition
no schema/API/runtime implementation
no autonomous appointment
no payment-custody authorization
no External Protected Action
```

## Gate

Acceptance of the Chapter Map authorizes Wave 1 drafting only. Each later Wave begins after the preceding Wave is merged and reviewed.
