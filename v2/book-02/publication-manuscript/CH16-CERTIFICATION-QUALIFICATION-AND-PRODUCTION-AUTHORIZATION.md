# CH16 — Certification, Qualification and Production Authorization

## Evidence, credentials and permission are different things

Professional platforms often make a dangerous jump:

```text
performed well
→ certified
→ qualified
→ authorized
```

These transitions are not automatic.

Book 02 requires the following distinctions:

```text
Capability Evidence
≠ Certification
≠ Professional Qualification
≠ Production Authorization
≠ Task-specific Eligibility
≠ Assignment
≠ Professional Authority
```

Each record answers a different question and may be issued by a different authority.

## Capability Evidence

Capability Evidence records observed performance.

It may come from:

- simulation;
- scenario assessment;
- supervised production;
- accepted Contributions;
- review findings;
- correction and recovery history;
- recent work diversity.

Capability Evidence should preserve scope, date, evaluator, scenario or work context, M-mode, R-tier and limitations.

```text
Capability Evidence
≠ permission to perform production work
```

## Certification

Certification states that an actor or implementation met a defined standard for a declared scope.

A Certification should identify:

- certification scheme and version;
- subject;
- Capability scope;
- jurisdiction and language;
- evidence basis;
- assessor;
- issue and expiry dates;
- conditions;
- suspension and revocation status.

Certification can be useful for routing and eligibility. It cannot create a government licence or reserved professional right.

```text
MarkOrbit Certified
≠ Government Licensed
```

## Professional Qualification

Professional Qualification is an externally or institutionally recognized credential relevant to regulated or reserved work.

Examples may include:

- lawyer admission;
- trademark-agent registration;
- notarial authority;
- accounting or other regulated qualification.

The record should preserve:

- issuing authority;
- credential identifier;
- jurisdiction;
- current status;
- effective period;
- restrictions;
- verification source;
- last verification time.

```text
credential uploaded
≠ credential verified
≠ credential current
```

Core may define a common credential envelope. It cannot grant the qualification.

## Assessor Authorization

An assessor may need separate permission to evaluate a Capability or issue a Certification.

The fact that someone is excellent at performing work does not necessarily authorize them to certify others.

```text
Capability to perform
≠ authority to assess
≠ authority to certify
```

Assessor Authorization should be scoped and versioned like other governed permissions.

## Production Authorization

Production Authorization answers:

> May this actor or implementation participate in real production work within a declared boundary?

A proposed record may include:

- subject;
- Capability scope;
- jurisdiction;
- allowed Work Package classes;
- M-mode;
- maximum R-tier;
- data class;
- Tool access ceiling;
- contact rules;
- supervision requirement;
- effective period;
- suspension and revocation conditions.

Production Authorization is stronger than Certification because it permits entry into real work. It still does not create Assignment or professional authority.

```text
Production Authorized
≠ Assigned
≠ Approved for this action
≠ Professionally Authorized
```

## Eligibility is task specific

Even a certified and production-authorized actor may be ineligible for a particular task because of:

- conflict of interest;
- jurisdiction;
- language;
- capacity;
- expired credential;
- unavailable reviewer;
- insufficient data permission;
- case complexity;
- current suspension;
- commercial or security constraints.

```text
Authorized generally
≠ eligible now
```

Book 03 owns the runtime eligibility decision.

## Assignment is still required

Eligibility identifies a valid candidate. Assignment creates the bounded authorization to perform a particular Work Package.

```text
Eligible
≠ Assigned
```

This preserves the ability to manage data access, deadlines, compensation, revocation and accountability at the exact work level.

## Professional Authority remains contextual

A qualified professional does not automatically have authority over every Matter.

Professional Authority may also require:

- current qualification;
- jurisdiction;
- conflict clearance;
- customer or organization appointment;
- Provider acceptance;
- exact matter scope;
- authority to sign, submit or advise.

```text
Qualified
≠ Appointed
≠ Authorized for this Matter
```

## AI and system authorization

AI and deterministic implementations can hold evaluated Production Authorization for bounded work classes. They cannot hold legal professional qualification or become the accountable professional authority.

Their authorization must bind:

- model, rule or service version;
- Capability version;
- Tool set;
- data scope;
- M-mode;
- allowed action class;
- review and stop conditions;
- expiry and reevaluation triggers.

```text
Model benchmark passed
≠ AI production authorization
```

## Suspension and revocation

Certification, qualification verification and Production Authorization need independent lifecycle states.

Possible states include:

```text
Candidate
Active
Restricted
Suspended
Expired
Revoked
Superseded
```

A suspension should trigger review of active Assignments, data access and pending Contributions. It should not erase historical Evidence.

```text
Authorization revoked
≠ prior work erased
```

## Candidate status

Capability Certification and Production Authorization remain candidate shared semantics pending field-level frozen-baseline mapping and formal Core Change Proposal review. Professional Qualification may use an existing credential structure or a controlled profile.

Nothing in this chapter activates a credential, authorization lifecycle or universal level system.

## Constitutional rule

```text
Evidence shows what was observed.
Certification records achievement against a standard.
Qualification comes from the applicable authority.
Production Authorization permits bounded real work.
Eligibility applies those records to a current task.
Assignment authorizes the exact work.
Professional Authority remains separately grounded.
```
