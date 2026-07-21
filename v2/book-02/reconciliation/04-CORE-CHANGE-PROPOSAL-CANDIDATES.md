# Core Change Proposal Candidates

## Status

This file identifies candidate proposals only. It grants no semantic authority.

## CP-CANDIDATE-01 — Need

### Problem

Opportunity and Order do not fully represent an unresolved required outcome.

### Candidate meaning

A Need is an originating expression that a Person or Workplace requires an outcome, resource, capability, asset, capacity or professional route.

### Why shared

Lite buyer requests, Workplace demand projection, MarkReg service intake and MGSN capability demand require one non-commercial origin concept.

### Open questions

- Is Need already represented by an existing request/intake object?
- Does Need need formal lifecycle or only immutable versions?
- Which service owns Need state?

## CP-CANDIDATE-02 — Engagement

### Problem

Opportunity is too early and Order is too narrow to represent an agreed multi-party collaboration boundary.

### Candidate meaning

An Engagement records participants, engagement-specific roles, purpose, disclosure scope, responsibility, commercial arrangement, relationship protection, professional authority and termination.

### Risk

Engagement could become an oversized container duplicating Order, Matter, Contract and Assignment.

### Admission condition

Admit only after proving a minimal contract that does not absorb Product policy.

## CP-CANDIDATE-03 — Work Package

### Problem

Task or Step alone does not express a bounded unit that can be assigned, priced, reviewed and accepted independently.

### Candidate meaning

A Work Package is a bounded requested contribution with defined inputs, output contract, eligibility, deadline, access scope, review policy and compensation reference.

### Boundary

```text
Workflow = orchestration
Work Package = assignable unit
Step = execution stage
Task = Product or workflow work record
```

## CP-CANDIDATE-04 — Assignment and Contribution

### Problem

The platform must distinguish authority to perform work from the work actually submitted.

### Candidate meanings

Assignment authorizes an actor to perform a Work Package under scoped conditions.

Contribution records the submitted artifact, verification, opinion, decision input or labor result.

### Risk

Existing task-assignment and evidence objects may already cover part of this meaning.

### Admission condition

Map the frozen task, actor, evidence and review contracts field by field before proposing additions.

## CP-CANDIDATE-05 — Outcome

### Problem

A Contribution is not necessarily accepted, and accepted work is not necessarily formal business state.

### Candidate meaning

Outcome is the reviewed result assembled from one or more Contributions and accepted for a declared purpose.

### Lock

```text
accepted Outcome
≠ formal-state mutation
```

Formal mutation still requires the Owning Service and applicable Apply path.

## CP-CANDIDATE-06 — Engagement responsibility roles

### Candidate controlled roles

```text
Relationship Owner
Delivery Owner
Professional Authority
Contracting Party
Payment Receiver
Solution Orchestrator
Capability Contributor
```

### Recommendation

Start as a versioned controlled role vocabulary attached to Engagement and Outcome references. Do not create seven new root objects.

## CP-CANDIDATE-07 — Capability credential family

### Candidate contracts

```text
Capability Certification
Professional Qualification
Assessor Authorization
Production Authorization
```

### Recommendation

Use a common credential envelope where possible. Treat Production Authorization separately if its lifecycle grants, restricts or revokes real-production access.

### Required checks

- issuer authority;
- subject;
- capability and jurisdiction scope;
- level;
- evidence;
- effective and expiry dates;
- status;
- revocation reason;
- verification source.

## CP-CANDIDATE-08 — Shared controlled vocabularies

Candidate vocabularies:

```text
L1–L5
M0–M5
R0–R4
P0–P4
EngagementRoleType
OutcomeDisposition
CredentialStatus
```

### Recommendation

Do not promote all values simultaneously. First determine which values are stable cross-product semantics and which remain policy presets.

## Concepts not recommended for Core admission now

```text
Resource Profile
Need Profile
Workplace Health
Trademark Inventory
Listing
Buyer Inquiry
Transaction Opportunity
Candidate Route Set
Provider Package
Case Fixture
Simulation Persona
Commission Claim
Marketplace Ranking
```

These can be expressed through profiles, specializations, projections or Product-local records.

## Recommended proposal sequence

```text
1. semantic field mapping against frozen Core
2. Work Package / Assignment / Contribution / Outcome cluster
3. Engagement and engagement-role vocabulary
4. Need
5. credential and Production Authorization cluster
6. controlled value sets
```

The work cluster should be assessed first because Books 03 and 05 depend on it most directly. Engagement should follow because Books 04, 06 and 07 depend on its role and relationship semantics.
