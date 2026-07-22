# CH32 — Public, Shared and Product-local Records

## Not every useful record belongs in Core

A multi-product platform generates many kinds of records.

Some must be understood across the whole platform. Some are intended for public use. Others exist only because one Product has a particular workflow, interface, commercial model or experiment.

Book 02 therefore requires every proposed record to be classified as:

```text
Public Contract or Public Projection
Shared Semantic Record
Product-local Record or Profile
```

These categories may reference one another, but they do not carry the same stability, authority or compatibility obligations.

```text
Widely used
≠ Core-owned

Publicly visible
≠ shared mutable record

Product-local
≠ semantically ungoverned
```

## Public records are governed disclosures

A public record is a purpose-approved representation intended for audiences outside the originating private context.

Examples include:

- public service pages;
- approved trademark Listings;
- public provider or capability profiles;
- educational articles;
- public fee or procedure summaries;
- published reports or directories.

A public record should preserve:

- publisher and accountable Workplace;
- source references;
- publication purpose;
- approved content version;
- public fields and redactions;
- rights and consent;
- professional review where required;
- effective time and freshness;
- correction, withdrawal and archival behavior.

```text
Approved for public display
≠ approved for every channel or later reuse
```

Public availability does not erase provenance, rights or correction duties.

## Public Projection and source record remain separate

A public page may display information from official data, Knowledge Claims, Product records and approved content.

The page is a Projection or publication artifact. It should not become a competing authoritative source merely because users discover it through search.

```text
Public Projection
≠ Official Source
≠ Source Object
```

Where practical, the interface should distinguish:

- official source fact;
- normalized or translated presentation;
- professional interpretation;
- AI-assisted explanation;
- date last checked.

## Shared semantic records exist for interoperability

A shared semantic record is justified where independent Products or platform layers must exchange a stable meaning and where local duplication would create dangerous divergence.

Examples already present or strongly established include:

- Person;
- Organization;
- Workplace;
- Membership;
- Customer and Contact references;
- Opportunity;
- Order;
- Matter;
- Review and Evidence;
- Product Installation;
- Projection;
- Handoff;
- Return;
- Settlement references.

Shared does not mean centrally editable by everyone.

```text
Shared semantics
≠ shared write authority
```

Each formal record still has an Owning Service, authority and lifecycle.

## Product-local records support differentiated experiences

A Product-local record exists because a Product needs a specialized workflow, interface or commercial behavior that does not yet require platform-wide interoperability.

Examples include:

```text
Trademark Inventory
Listing
Buyer Inquiry
Transaction Opportunity
Candidate Route Set
Provider Package
Case Fixture
Commission Claim
Content Brief
Campaign Asset
```

These records may reference Core concepts without becoming Core roots.

```text
Product-local record
+ Core references
= governed specialization
```

Product-local records can evolve faster and support experiments without forcing migrations across unrelated systems.

## Product-local does not mean private invention of shared meaning

A Product may add fields and lifecycle states for its own purpose. It must not redefine the meaning of a shared reference.

For example:

- a Listing may reference a Trademark but cannot redefine ownership;
- a Buyer Inquiry may reference a Customer or Contact but cannot create marketing permission by itself;
- a Provider Package may reference Handoff and Evidence without changing Provider Appointment semantics;
- a Transaction Opportunity may specialize Opportunity without becoming a second incompatible Opportunity universe.

```text
Local profile
≠ alternate Core definition
```

## The F0–F4 admission test

When a local concept appears useful across Products, it should enter the controlled admission process:

```text
F0 — already covered
F1 — composition of existing semantics
F2 — explanatory profile or specialization
F3 — candidate shared addition
F4 — formal Core Change Proposal required
```

The evaluation should ask:

1. Do at least two independent Products need the same stable meaning?
2. Can existing references and composition express it safely?
3. Does the concept have a durable lifecycle and authority boundary?
4. Would local implementations create material interoperability risk?
5. Is it independent of one Product's pricing, interface or algorithm?
6. Can compatibility, versioning and migration be defined?
7. Does the benefit justify enlarging Core?

```text
Repeated Product use
≠ automatic Core admission
```

## Profiles are often better than new roots

Many concepts can remain profiles over existing records:

- Provider as an Organization profile;
- Contributor as an Assignment or Engagement role;
- Transaction Opportunity as an Opportunity profile;
- Listing as an Asset Projection profile;
- Trademark Request as a Need profile;
- Evidence Return as a Return profile;
- Professional Qualification as a Credential specialization.

Profiles preserve interoperability while avoiding parallel identity and lifecycle universes.

```text
New noun
≠ new root object required
```

## Shared controlled vocabularies need governance

Some cross-product needs may be satisfied by controlled values rather than new objects, such as:

- role types;
- M0–M5 collaboration modes;
- R0–R4 review tiers;
- epistemic states;
- source authority classes;
- Projection purposes;
- Return types.

A controlled vocabulary still requires:

- identifier;
- definition;
- version;
- allowed use;
- compatibility;
- deprecation;
- owner.

```text
Value set
≠ informal labels in user interfaces
```

## Public, shared and local versions are independent

A Product-local record may change without a Core version change. A public Projection may require refresh when its source changes. A shared contract may require migration even when the displayed Product remains unchanged.

The platform should distinguish:

```text
Core Contract Version
Shared Record Version
Product-local Schema Version
Public Projection Version
Content Version
```

```text
Product release
≠ Core semantic change by default
```

## Ownership and correction

Each category requires a clear correction route.

### Public record

The publisher corrects or withdraws the publication and preserves source and approval history.

### Shared semantic record

The Owning Service validates and applies the correction under the shared contract.

### Product-local record

The Product-owning service corrects its local record and assesses effects on referenced shared objects or public Projections.

```text
Local correction
≠ source correction
≠ formal-state correction
```

The platform must trace which layer was wrong.

## Data duplication and derived local state

Products may maintain indexes, caches and derived state. These should be labeled by purpose and source.

Examples include:

- search index;
- recommendation score;
- display summary;
- opportunity rank;
- freshness indicator;
- local processing state.

```text
Derived local state
≠ shared business fact
```

A recommendation score should not be written back as a universal property of the customer, trademark or provider.

## Public content needs stronger source discipline

Publication can amplify error far beyond an internal record.

Before public release, the responsible Product should consider:

- source authority;
- currentness;
- rights and quotation limits;
- personal or customer data;
- professional-review requirement;
- AI disclosure;
- jurisdictional scope;
- correction and update ownership.

```text
Content useful for internal research
≠ ready for public professional publication
```

## White-label and multi-Workplace use

A shared Product may generate records for several Workplaces. The platform must preserve:

- represented Workplace;
- Relationship Owner;
- Contracting Party;
- publisher identity;
- branding and disclosure policy;
- data and customer boundaries.

```text
Shared Product infrastructure
≠ shared customer ownership
```

A Product-local record in one Workplace should not become visible to another simply because both use the same Product.

## AI-generated local records

AI may create Product-local drafts, scores, candidates and explanations. Their type and status should remain explicit.

```text
AI-generated local record
≠ shared semantic record
≠ public-approved content
```

Promotion to shared or public status requires the applicable source, rights, review and approval controls.

## Migration from local to shared

When a local concept passes the admission test, migration should include:

```text
Local Schema Inventory
→ Semantic Comparison
→ Authority and Lifecycle Design
→ Change Proposal
→ Conformance Fixtures
→ Mapping and Backfill Plan
→ Compatibility Window
→ Consumer Migration
→ Deprecation Evidence
```

Historical local records should not be reclassified silently. The migration must preserve original meaning and identify records that cannot be safely mapped.

## Core must remain smaller than the platform

The number of Product-local records will always exceed the number of shared Core records.

That is healthy.

Products change as markets, user behavior, AI models and operating methods change. Core should change only where durable interoperability and authority discipline require it.

```text
Core completeness
≠ absorbing every Product concept
```

Core is complete when it provides the stable grammar needed for safe composition, not when it contains every possible noun.

## Constitutional rule

```text
Public records are governed disclosures.
Shared records carry stable interoperable meaning.
Product-local records support differentiated experience and policy.

Every record must declare its category,
owner, authority, version and correction route.

Product desire alone never promotes a local concept into Core.
```
