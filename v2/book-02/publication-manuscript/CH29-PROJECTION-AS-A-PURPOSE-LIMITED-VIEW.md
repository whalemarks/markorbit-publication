# CH29 — Projection as a Purpose-limited View

## Projection exists because access and ownership are different

MarkOrbit must let Products, Workplaces, providers, customers and public interfaces see useful information without copying the entire source object or transferring authority over it.

Projection is the shared mechanism for that purpose.

```text
Projection
= a purpose-limited, source-linked view
```

It is not a duplicate authoritative record and not a transfer of business ownership.

```text
Projection
≠ Source Object
≠ Ownership Transfer
≠ Relationship Transfer
≠ Mutation Authority
≠ Unlimited Reuse
```

## A Projection must identify its source

Every consequential Projection should preserve:

- source object and type;
- source-owning service or Workplace;
- source version;
- projecting actor or service;
- recipient context;
- declared purpose;
- visible and redacted fields;
- permitted actions;
- onward-sharing rule;
- effective time and expiry;
- freshness state;
- correction and revocation behavior.

The recipient should be able to tell what is being shown and what remains outside the view.

```text
View is complete for its purpose
≠ Source record is fully disclosed
```

## Projection is not replication by default

A Product may cache a Projection for performance, indexing or offline access. The local copy remains subordinate to the source contract.

It must preserve:

- source reference;
- projection version;
- last refresh time;
- stale or conflicted state;
- permitted local transformations;
- correction route.

```text
cached locally
≠ locally authoritative
```

If the source changes, the Product should refresh, expire or mark the Projection stale. It should not silently evolve a parallel truth.

## Purpose controls the visible fields

The same source object may produce different Projections.

A public trademark Projection may show:

- mark;
- jurisdiction;
- class;
- public status;
- public owner name where permitted.

A delivery Projection for a professional provider may additionally show:

- applicant details;
- relevant documents;
- deadlines;
- approved instruction scope.

A finance Projection may show:

- Order reference;
- invoice category;
- approved amount;
- settlement status.

```text
same source
+ different purpose
= different Projection
```

The platform should not create one “full record” view and rely on users to ignore fields they do not need.

## Projection profiles

The Book 02 reconciliation identifies several useful profiles:

```text
Demand Projection
Capability Projection
Asset Projection
Audience Projection
Capacity Projection
```

These should normally remain profiles over one Projection mechanism.

### Demand Projection

Shows a required outcome or service need without necessarily exposing the customer identity.

```text
Demand visible
≠ Customer disclosed
```

### Capability Projection

Shows what an actor or Workplace may be able to deliver, with scope, evidence and validity.

```text
Capability projected
≠ eligible for this task
≠ assigned
```

### Asset Projection

Shows a trademark or other asset for discovery, review or transaction analysis.

```text
Asset projected
≠ ownership proved
≠ resale authorized
```

### Audience Projection

Shows a governed audience segment or reach estimate.

```text
Audience available
≠ marketing consent granted
```

### Capacity Projection

Shows time-sensitive production availability.

```text
Capacity visible
≠ provider accepted work
```

## Projection does not create a relationship

Lite may project a public trademark record or a service signal. MarkReg may receive a controlled customer context. A provider network may see a Need or Capability Projection.

None of these events automatically creates:

- Customer status;
- marketing consent;
- Relationship Owner status;
- Contracting Party status;
- Provider Appointment;
- Professional Authority.

```text
Projected to a Workplace
≠ owned by that Workplace
```

## Projection and public records

Public records may be broadly accessible, but accessibility does not remove purpose, freshness or interpretation limits.

A public Projection should preserve:

- public-source reference;
- retrieval and effective date;
- display purpose;
- limitation or disclaimer where needed;
- correction and takedown route;
- whether the information is official, derived or inferred.

```text
Publicly accessible
≠ current
≠ verified for every use
≠ permission for unrestricted profiling
```

A public trademark record can support research or opportunity discovery without creating a customer relationship or permission to send commercial communications.

## Projection and derived content

A Projection may include normalized or derived values, such as:

- translated labels;
- computed age;
- status summary;
- deadline candidate;
- risk indicator;
- opportunity score.

Derived values must remain distinguishable from source facts.

```text
Source Field
≠ Normalized Field
≠ Derived Candidate
≠ Recommendation
```

A user-facing interface may present them together, but the underlying semantic status must remain available to reviewers and auditors.

## Projection and authority ceiling

A Projection should state what the recipient may do with it.

Possible action scopes include:

```text
View Only
Annotate Locally
Create Candidate
Request Clarification
Prepare Handoff
Use in Approved Work Package
Publish Approved Subset
```

It should not imply:

```text
Edit Source
Contact Customer
Approve Payment
Submit Official Action
Create Formal State
```

Unless those permissions arise from a separate authority contract.

## Revocation and expiry

Projection may end because:

- purpose completed;
- Engagement ended;
- consent withdrawn;
- Product Installation removed;
- data became stale;
- source corrected;
- provider replaced;
- security or privacy incident occurred.

Revocation should address:

- future access;
- cached copies;
- onward sharing;
- pending Work Packages;
- retention obligations;
- audit evidence.

```text
Projection revoked
≠ historical access erased
```

The system should preserve that access occurred while preventing unauthorized future use.

## Correction propagation

When the source changes, the Projection should support:

```text
Source Correction
→ Impact Detection
→ Projection Refresh or Withdrawal
→ Recipient Notification where material
→ Downstream Decision Review where required
```

A corrected Projection does not silently rewrite completed decisions. It identifies which Decisions, Contributions or public outputs relied on the earlier version.

## Projection and AI

AI may summarize, transform or explain a Projection. It does not gain broader access or disclosure authority.

```text
AI can read Projection
≠ AI may retrieve full source
≠ AI may retain it in memory
≠ AI may train on it
```

The AI result should preserve source reference, projection purpose, visible-field boundary and result type.

## Cross-book boundary

Book 03 governs how a Projection is used in a Capability Request, Work Package, Assignment, Review or Apply path.

Book 05 uses Projection for trademark, customer, provider and lifecycle views.

Book 06 uses Projection for public content, trademark supply, demand, audience and opportunity experiences.

Book 02 defines the shared contract and prevents visibility from becoming ownership or authority.

## Candidate status

Projection is an existing shared mechanism. Demand, Capability, Asset, Audience and Capacity forms remain explanatory or Product-level profiles unless future interoperability requires formal controlled profiles.

## Constitutional rule

```text
Projection exposes only the information
needed for an authorized purpose,
while preserving source, version,
ownership, rights, expiry and correction.

Visibility never transfers authority by implication.
```
