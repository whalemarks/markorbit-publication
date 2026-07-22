# Chapter 03 — Customer Relationship Modes

MarkReg must be able to serve customers directly without requiring every partner Workplace to surrender its customer relationship.

That requirement is strategic, architectural and commercial.

A platform that supports only direct self-operated service will appear to compete with the agencies, firms and professionals it expects to adopt the Product. A platform that supports only software access may fail to prove complete delivery. A platform that uses “white-label” to hide responsibility may create customer and legal risk.

MarkReg therefore supports several explicit relationship modes.

```text
Direct self-operated service
White-label delivery
Co-delivery
Bounded capability fulfillment
```

The mode determines who owns the relationship, who contracts, who communicates, who receives payment, who delivers, who acts professionally and what happens when the service fails.

## 1. Relationship roles must be recorded separately

Every material Engagement should identify at least:

```text
Demand Originator
Relationship Owner
Contracting Party
Payment Receiver
Solution Orchestrator
Delivery Owner
Professional Authority
Owning Service
```

Additional roles may include:

- customer instructor;
- applicant or owner;
- signatory;
- internal production team;
- Contributor;
- Reviewer;
- local Provider;
- complaint handler;
- refund decision-maker;
- communication owner.

One participant may hold several roles. The roles remain distinct because they answer different questions.

### Demand Originator

Who identified or introduced the need?

### Relationship Owner

Who holds the continuing business relationship with the customer?

### Contracting Party

Who agrees to provide the service under the applicable terms?

### Payment Receiver

Who receives the customer's payment for the relevant scope?

### Solution Orchestrator

Who designs and coordinates the delivery route?

### Delivery Owner

Who is accountable for assembling and delivering the promised Outcome?

### Professional Authority

Who may exercise the legally or professionally reserved judgment or action?

### Owning Service

Which service preserves the formal business state created or changed by the process?

```text
Payment Receiver
≠ Relationship Owner
≠ Delivery Owner
≠ Professional Authority
```

## 2. Direct self-operated service

In direct mode, a MarkReg-operated Workplace serves the customer under its own business identity.

It may hold:

- the customer relationship;
- the service contract;
- pricing and invoicing responsibility;
- customer communication;
- delivery coordination;
- complaint and recovery responsibility.

The MarkReg-operated Workplace may still rely on external Providers for jurisdiction-specific work. Direct service does not turn the platform or Workplace into the Professional Authority in every country.

A typical structure is:

```text
Customer
→ MarkReg-operated Workplace
→ MarkReg Product and internal production
→ MGSN Connection or approved external route
→ local Professional Authority
→ official office
```

### Direct-mode strengths

- one visible commercial counterparty;
- complete lifecycle ownership;
- consistent service standards;
- direct Product learning;
- clearer recovery responsibility;
- faster implementation of new capabilities.

### Direct-mode risks

- partner distrust;
- platform self-preference;
- confusion between Product and commercial operation;
- cross-Workplace data leakage;
- over-centralization of customer relationships;
- hidden related-party routing.

Direct mode should therefore remain one explicit Workplace route, not the default ownership rule of the ecosystem.

## 3. White-label delivery

In white-label mode, the originating Workplace normally remains the customer-facing business.

The originating Workplace may remain:

- Relationship Owner;
- Contracting Party;
- customer communication owner;
- Payment Receiver;
- commercial approver.

MarkReg supplies agreed software, production, orchestration, Review or fulfillment capabilities behind that relationship.

```text
Customer
→ Originating Workplace brand and relationship
→ MarkReg white-label capability
→ approved professional and Provider route
→ evidence returned to Originating Workplace
→ customer delivery
```

### What white-label may conceal

White-label may conceal unnecessary operational complexity and the use of a backend Product brand where contract and law permit.

### What white-label must not conceal

It must not hide:

- the identity of a lawyer, agent or other professional where disclosure is required;
- the Contracting Party;
- who receives customer funds;
- who bears Delivery responsibility;
- material subcontracting or data processing where disclosure is required;
- complaint and escalation routes;
- a related-party commercial interest where it affects recommendation.

```text
White-label
≠ fictitious identity
≠ concealed Professional Authority
≠ silent customer transfer
```

## 4. White-label responsibility must be complete

A white-label Engagement should define:

- customer-facing brand;
- whether MarkReg is disclosed;
- whether external Providers are disclosed and when;
- scope supplied by MarkReg;
- scope retained by the originating Workplace;
- who obtains Customer Instruction;
- who approves recommendations and changes;
- who communicates with the customer;
- who may contact the customer directly;
- who approves additional fees;
- who handles complaints;
- who bears correction and recovery cost;
- what data MarkReg may retain;
- what evidence must return;
- how the relationship ends.

An incomplete white-label agreement creates invisible gaps. Each party may believe the other owns customer communication, deadline monitoring or final evidence validation.

## 5. Co-delivery

Co-delivery openly divides responsibility between the originating Workplace and MarkReg.

A possible structure is:

```text
Originating Workplace
→ customer context, relationship and commercial approval

MarkReg
→ solution design, production orchestration and quality control

External Provider
→ local professional action

Originating Workplace or agreed Delivery Owner
→ customer-facing Outcome and continuing relationship
```

Co-delivery is useful when:

- the originating Workplace has the customer relationship but lacks production scale;
- MarkReg has standardized capability but needs customer or industry context;
- the service requires a local Provider;
- both brands or teams should be visible;
- responsibility should be divided by lifecycle stage.

## 6. Co-delivery is not “everyone is responsible”

The phrase “joint responsibility” often hides operational ambiguity.

A co-delivery plan should allocate concrete duties:

| Responsibility | Example owner |
|---|---|
| customer objective and commercial context | originating Workplace |
| applicant and document collection | originating Workplace or MarkReg, as agreed |
| strategy and option design | MarkReg plus qualified professional Review |
| local legal advice or filing | appointed Provider |
| package assembly and quality control | MarkReg |
| customer approval | originating Workplace obtains and records |
| additional-fee approval | identified commercial approver |
| external evidence validation | MarkReg Owning Service or agreed formal-state service |
| customer delivery and complaint handling | named Delivery Owner |

When a deadline, fee increase, document rejection or Provider silence occurs, the escalation owner must already be known.

## 7. Bounded capability fulfillment

A Workplace may need one MarkReg capability rather than a complete service.

Examples include:

- official-status verification;
- deadline verification;
- search-result triage;
- goods and services review;
- mark-description preparation;
- evidence screening;
- certificate validation;
- Provider instruction review;
- transaction due diligence;
- recordal package preparation.

The bounded service produces a defined work product or Review. It does not imply complete Matter ownership.

```text
One accepted Work Package
≠ complete lifecycle Engagement
```

## 8. Bounded scope must identify what remains outside

A bounded capability offer should state:

- exact input required;
- exact output;
- jurisdiction and service scope;
- source and freshness assumptions;
- review level;
- exclusions;
- validity period;
- permitted use;
- whether external action is included;
- what the recipient remains responsible for.

For example, “US Section 8 evidence screening” may include:

- review of supplied screenshots and product pages;
- identification of apparent specimen issues;
- a structured recommendation for professional review.

It may exclude:

- verification of actual use dates;
- legal opinion on fraud or abandonment;
- preparation of declarations;
- attorney signature;
- official filing.

The recipient should not mistake a useful bounded result for a complete service.

## 9. Relationship mode may change, but not silently

A journey may begin in one mode and move to another.

Examples:

- a white-label partner asks MarkReg to contract directly with the customer for a complex dispute;
- a bounded status review becomes a complete maintenance service;
- a co-delivery engagement becomes direct service after the customer requests transfer;
- a direct customer appoints its own external counsel while MarkReg continues orchestration.

A mode change should create an explicit amendment or new Engagement identifying:

- customer consent;
- effective time;
- transferred and retained scope;
- Relationship Owner;
- Contracting Party;
- pricing and payment;
- data access;
- communication;
- open obligations;
- document custody;
- complaint and recovery responsibility.

```text
More direct contact
≠ customer relationship transferred automatically
```

## 10. Customer choice remains protected

Relationship protection does not make the customer property.

A customer may choose to:

- remain with the originating Workplace;
- contract directly with another qualified party;
- appoint a preferred local professional;
- move the Matter;
- terminate the service;
- request a direct transition.

The architecture should preserve provenance, attribution, agreed compensation and non-circumvention while respecting lawful customer choice.

```text
Introduction
≠ perpetual ownership of the customer
```

## 11. Non-circumvention must be bounded

A defensible non-circumvention rule should identify:

- protected customer, opportunity or scope;
- original source;
- prohibited conduct;
- permitted operational contact;
- duration;
- customer-choice exception;
- pre-existing relationship exception;
- survival after termination;
- attribution or compensation remedy;
- dispute process.

A broad rule forbidding every future interaction may be commercially unfair and difficult to enforce. A vague rule provides little protection.

## 12. Communication rights are mode-specific

The system should distinguish whether MarkReg or a Provider may:

- contact only the originating Workplace;
- contact the customer for document collection;
- join a customer meeting;
- send operational updates;
- provide professional advice directly;
- send invoices;
- market unrelated services;
- retain the contact for future use.

Access to customer data for current delivery does not create future marketing permission.

```text
Operational contact
≠ independent prospecting right
```

## 13. Data access follows delivery responsibility

Each participant receives the minimum information needed for its role.

A local Provider may need:

- applicant information;
- mark and goods version;
- filing basis;
- relevant documents;
- deadline;
- approved instruction;
- communication route.

It may not need:

- the customer's entire portfolio;
- internal margin;
- unrelated correspondence;
- other Providers' pricing;
- private Workplace strategy;
- complete AI memory.

The mode determines data scope but does not remove privacy and confidentiality requirements.

## 14. Pricing and payment do not define the relationship by themselves

A partner may collect the full customer price and pay MarkReg a production fee. MarkReg may collect a defined direct-service fee. A Provider may be paid through an agreed route.

The payment path should not be used to infer every business role.

```text
Receives payment
≠ owns customer relationship automatically
≠ bears every delivery obligation automatically
```

Each quotation and agreement should identify:

- customer-facing price;
- included service;
- MarkReg fee;
- Provider and official costs;
- partner margin or commission where applicable;
- Payment Receiver;
- refund responsibility;
- additional-fee approval.

This chapter does not authorize platform payment custody or escrow.

## 15. Professional Authority remains independent of brand presentation

The customer may experience one service brand while formal professional work is performed by another identified professional or organization.

The service mode must preserve:

- jurisdiction-specific qualification;
- conflict check;
- engagement or appointment;
- POA or representation authority;
- scope of legal advice;
- filing or response authority;
- professional responsibility.

```text
Customer-facing brand
≠ Professional Authority
```

## 16. A mode-specific failure example

Assume an originating agency purchases white-label filing support for a customer.

The agency sends scanned documents. MarkReg prepares the package. The local Provider later states that an original POA is mandatory and the filing deadline is approaching.

A governed mode should already answer:

- who asks the customer for the original;
- whether the Provider may contact the customer;
- who explains the deadline risk;
- who approves courier cost;
- whether filing may proceed with a scan and later original;
- who makes the professional judgment;
- who bears cost if the initial requirement was wrong;
- how the customer is updated;
- what happens if the original is late.

Without a defined mode, the issue becomes a chain of unanswered email and shifted responsibility.

## 17. Mode selection should be explainable

MarkReg may recommend a service mode based on:

- existing customer relationship;
- Workplace capability;
- desired brand presentation;
- jurisdiction and professional requirements;
- need for complete lifecycle responsibility;
- partner preference;
- communication policy;
- cost and margin;
- data sensitivity;
- recovery capacity.

The recommendation should disclose platform or affiliated commercial interest.

The originating Workplace may reject the recommended route and use internal or approved external capability where permitted.

## 18. Product and technical implications

MarkReg requires:

- typed Engagement mode;
- versioned responsibility matrix;
- Relationship Owner and attribution records;
- Contracting Party and Payment Receiver fields;
- communication permissions;
- customer transition events;
- data-scope policies;
- white-label branding configuration;
- professional-identity disclosure blocks;
- fee decomposition;
- complaint and recovery routing;
- non-circumvention and survival terms;
- evidence-return obligations;
- audit of role changes.

## 19. Commercial implications

The four modes expand MarkReg's addressable market.

- Direct service supports full-margin self-operated delivery.
- White-label supports agency adoption without customer loss.
- Co-delivery supports complex services and shared expertise.
- Bounded capability fulfillment supports modular use and gradual adoption.

The economics should reward real delivery and orchestration. They should not make customer capture the hidden objective of Product adoption.

## 20. The chapter lock

```text
Direct service
≠ ecosystem default ownership

White-label
≠ concealed responsibility

Co-delivery
≠ undefined shared responsibility

Bounded capability
≠ full Matter ownership

Operational access
≠ customer relationship transfer
```

> MarkReg can scale across independent businesses only when every service mode makes customer relationship, contract, payment, delivery and professional authority explicit before the work becomes difficult.