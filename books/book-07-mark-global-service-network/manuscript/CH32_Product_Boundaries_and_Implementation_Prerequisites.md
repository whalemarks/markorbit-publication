# B07-CH-32 — Product Boundaries and Implementation Prerequisites

## 1. Publication authority is not implementation authority

Book 07 defines the Product meaning of MGSN. It does not by itself authorize production routing, funds custody, provider instruction, automated Trust decisions or any official act.

```text
Product publication
≠ implementation specification
≠ legal authorization
≠ production deployment
```

A conformant implementation must inherit the boundaries defined by Core, Execution, Workplace, MarkReg, Lite, Finance and applicable law.

## 2. Core boundary

Core provides shared semantic and capability authority, including:

- controlled identifiers and record meanings;
- jurisdiction, service and Capability definitions;
- rules, sources and versioning;
- identity, permission and audit protocols;
- shared evaluation and recommendation capabilities;
- Handoff and Return contracts;
- connector and governed-execution infrastructure.

Core does not become the business owner of an Originating Workplace's Customer, Order or Matter merely because MGSN calls a Core capability.

Any implementation that changes a frozen Core object, state, transition, Owning Service or Event contract requires the appropriate controlled Change Proposal.

## 3. Workplace boundary

The Originating Workplace owns the customer relationship and originating business context.

It controls:

- the purpose of the network request;
- what information may be projected;
- who may confirm a route;
- internal quote and margin decisions;
- receipt and use of Return information;
- internal professional and commercial responsibility.

The Execution Provider Workplace owns its internal personnel, operating records, professional work and provider-side responsibility.

MGSN may coordinate between them, but it does not collapse the two Workplaces into one tenant or shared customer record.

## 4. MGSN Connection and Network boundary

The MGSN Connection or Gateway is the Workplace-scoped interface.

The MGSN Network is the platform-owned managed network responsible for:

- admitted supply;
- procurement terms;
- Candidate Route Sets;
- recommendation;
- allocation coordination;
- funds and fulfillment projections;
- Trust and network governance.

```text
Connection configuration
≠ ownership of the Network
```

The implementation must prevent the Gateway from becoming an unrestricted provider export or peer-to-peer contact graph.

## 5. MarkReg and Lite boundary

MarkReg may originate a Capability Need from an Order or Matter, receive a candidate route, record user disposition and validate a Return.

MarkReg remains the authoritative Product for its trademark-service lifecycle. MGSN does not take ownership of MarkReg's Matter truth.

Lite may originate a smaller Capability Need, present a recommended managed route and continue into MarkReg or another Product through a governed Handoff.

Lite must not independently decide provider qualification, conflict, procurement truth, funds release or official completion.

## 6. Execution boundary

External instruction, filing, communication, funds movement and official action require governed Execution authority.

MGSN may prepare:

- an instruction package;
- an allocation decision;
- an acceptance request;
- a milestone expectation;
- a release-condition projection.

It may not treat preparation as execution.

```text
Prepared instruction
≠ sent instruction

Provider allocated
≠ Provider accepted

Release condition observed
≠ funds released
```

Unknown external outcomes must remain unknown until supported by authoritative Evidence.

## 7. Finance boundary

MGSN needs funds-control semantics, but it is not the authoritative Finance ledger.

Finance or an authorized financial service must own:

- receipt truth;
- custody status;
- payable and receivable truth;
- official-fee disbursement;
- refund and adjustment truth;
- settlement completion;
- accounting entries;
- financial reconciliation.

MGSN may hold purpose-specific projections and conditions needed for route and fulfillment coordination.

It may not infer a universal escrow, client-money or payment-institution license from the Product model.

## 8. Legal and regulatory prerequisites

Before production funds and service execution, implementation must determine the applicable model for each operating entity and jurisdiction.

Relevant prerequisites may include:

- contractual role of the platform;
- agency, referral, procurement or managed-service characterization;
- client-money or trust-account rules;
- payment-service regulation;
- tax collection, invoicing and withholding;
- foreign-exchange controls;
- sanctions and restricted-party screening;
- anti-money-laundering obligations;
- professional-conduct rules;
- data-protection and cross-border transfer rules;
- consumer and unfair-commercial-practice rules;
- refund, cancellation and dispute requirements.

These are implementation gates, not details that can be deferred after launch.

## 9. Provider and professional prerequisites

Provider activation must have a defined process for:

- legal identity;
- Organization and responsible-person verification;
- professional qualification;
- insurance where required;
- service-specific Evidence;
- conflict capability;
- data-security obligations;
- subcontracting disclosure;
- acceptance authority;
- complaints and disciplinary information where lawful;
- restriction, suspension and appeal.

A Provider Network Profile is not a substitute for professional due diligence.

## 10. Procurement and pricing prerequisites

Implementation must define:

- who negotiates provider terms;
- who accepts procurement commitments;
- official-fee update sources;
- exchange-rate policy;
- validity and repricing rules;
- provider-cost confidentiality;
- demand-side pricing authority;
- related-party disclosure;
- margin and routing-neutrality review;
- reconciliation after variable disbursements.

The same numeric price cannot be assumed to represent provider cost, official fee, platform price and customer price.

## 11. Data and security prerequisites

Production design must prove:

- Workplace-scoped authorization;
- purpose-limited Projection;
- progressive disclosure;
- provider-side access expiry;
- secure Evidence and Document exchange;
- operator access logging;
- separation of demand and supply roles;
- retention and deletion rules;
- export and portability boundaries;
- incident response;
- model and AI isolation;
- secrets and connector credential protection.

The platform's ownership of MGSN does not remove its duty to minimize access.

## 12. Trust and governance prerequisites

Trust automation requires special caution.

Before automated scoring or adverse action, implementation must define:

- evidence sources;
- service and jurisdiction scope;
- time decay and freshness;
- correction rights;
- human review thresholds;
- explanation requirements;
- bias and self-dealing controls;
- appeal and restoration;
- treatment of missing data;
- separation from qualification and Availability.

A single global score should not become a hidden route or sanction authority.

## 13. Technical prerequisites

A future implementation package should include, at minimum:

- authoritative object and ownership mapping;
- API and Event contracts;
- role and permission matrix;
- Handoff and Return schemas;
- idempotency and duplicate-safety rules;
- unknown-outcome and retry policy;
- audit and provenance model;
- source and Evidence model;
- fixture and conformance tests;
- observability and incident controls;
- migration and rollback plan;
- security and privacy review.

These belong in implementation specifications and ADRs, not in the Product Book.

## 14. MVP implementation gate

Before MVP 0 can operate on real external matters, the project must establish:

1. selected jurisdictions and service packages;
2. admitted pilot providers;
3. authorized Originating Workplaces;
4. operator roles and escalation;
5. legal and financial operating model;
6. protected-action approvals;
7. Finance integration or controlled manual process;
8. Evidence and Return requirements;
9. incident and replacement process;
10. conformance coverage for MG-SCN-01–32 and MG-AC-01–16.

## 15. Product rule

MGSN implementation may proceed only through explicit authority, owned interfaces and validated prerequisites. The Product vision is not weakened by these gates; the gates are what make a managed professional network credible.