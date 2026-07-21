# Object and Contract Classification

## 1. Root business objects

The following concepts may justify independent identifiers and lifecycle because they represent durable business meaning across Products.

### Existing or presumed existing

```text
Person
Organization
Workplace
Customer
Contact
Relationship
Matter
Order
Opportunity
Product Installation
Capability Definition
Evidence
Projection
Handoff
Return
```

### Strong v2 candidates

```text
Need
Engagement
Work Package
Assignment
Contribution
Outcome
```

A candidate must not be admitted merely because it appears in several manuscripts. It must prove that existing objects cannot represent the same meaning without distortion.

## 2. Contextual roles, not identity types

The following should normally be controlled roles attached to an Engagement, Order, Assignment or Outcome:

```text
Demand Originator
Relationship Owner
Contracting Party
Payment Receiver
Solution Orchestrator
Capability Contributor
Professional Authority
Delivery Owner
Reviewer
Assessor
```

They must not become permanent Person or Workplace types. The same actor may hold different roles in different engagements.

## 3. Profiles and views

The following are best treated as profiles, projections or calculated views unless implementation demonstrates a stable independent lifecycle:

```text
Resource Profile
Need Profile
Capability Profile
Capacity Profile
Asset Profile
Workplace Health
Capability Coverage
Demand Projection
Capability Projection
Asset Projection
Audience Projection
Capacity Projection
Candidate Route Set
Provider Trust View
```

A profile may use a shared schema without becoming a formal business object.

## 4. Credentials and authorizations

Credential semantics should use one shared envelope with explicit subtype and issuer.

```text
Credential
├── Capability Certification
├── Professional Qualification
├── Assessor Authorization
└── Organization or Provider Accreditation
```

Production Authorization is different from an informational credential because it grants access to real work under a defined authority boundary. It may require its own lifecycle:

```text
requested
→ verified
→ supervised
→ active
→ restricted
→ suspended
→ expired
→ revoked
```

The lifecycle remains candidate until approved through a Core Change Proposal.

## 5. Controlled value sets

The following should initially be shared controlled vocabularies rather than independent objects:

```text
L1–L5 proficiency level
M0–M5 human–AI collaboration mode
R0–R4 risk tier
P0–P4 production authorization level
Engagement role type
Review decision type
Outcome disposition
Credential status
Projection visibility
```

Each value set needs:

- identifier and version;
- definition;
- allowed transitions where applicable;
- compatibility policy;
- deprecation policy.

## 6. Product-local specializations

The following remain Product-local or domain-local unless future interoperability requires promotion:

```text
Trademark Inventory
Trademark Listing
Buyer Inquiry
Transaction Opportunity
Commission Claim
Content Project
Marketing Pack
Candidate Route Set
Provider Package
Case Fixture
Simulation Persona
Marketplace Ranking
```

They should reference shared Core objects rather than redefine them.

Examples:

```text
Trademark Request
= Need specialization

Transaction Opportunity
= Opportunity specialization

Listing
= Projection over a Trademark Inventory context

Evidence Return
= Return profile

Instruction Package
= Handoff payload profile
```

## 7. Formal-state ownership

Admission to Core never means Core stores or mutates every instance.

Suggested ownership pattern:

| Concept | Semantic authority | Formal-state owner |
| --- | --- | --- |
| Need | Core contract | originating Product Owning Service |
| Engagement | Core contract | collaboration/engagement Owning Service |
| Order | Core contract | commercial Owning Service |
| Work Package | Core contract | Execution or production Owning Service |
| Assignment | Core contract | Execution Owning Service |
| Contribution | Core contract | Execution/contribution Owning Service |
| Outcome | Core contract | originating delivery Owning Service |
| Certification | Core credential contract | certification Owning Service |
| Production Authorization | Core authorization contract | production-governance Owning Service |
| Professional Qualification | Core credential profile | qualification-verification Owning Service |

## 8. Object-chain lock

The v2 chain is retained as a semantic distinction, not necessarily one mandatory workflow:

```text
Need
→ Opportunity
→ Engagement
→ Order
→ Work Package
→ Assignment
→ Contribution
→ Review
→ Outcome
→ Settlement
→ Evidence
```

Valid variations include:

- a Need resolved without a customer Order;
- an Engagement formed for expert review only;
- a Work Package created for platform data verification;
- a Contribution produced in simulation with no Settlement;
- an MGSN Handoff generated from a Matter rather than a new Order.

Core must define meaning without forcing every Product into one commercial sequence.
