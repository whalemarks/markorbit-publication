# External Professional Qualification — Source and Privacy Review Plan

## 1. Status

```text
Research track: B02-CP-RESEARCH-A1
Formal Change Proposal: NOT OPENED
Legal conclusion: NOT PROVIDED
Production implementation: NOT AUTHORIZED
```

This plan defines the evidence and review needed before MarkOrbit may propose a shared reference contract for externally issued professional qualifications.

Core may represent an external qualification. It must not issue, renew, suspend or revoke the qualification.

## 2. Target records

Possible records include:

- lawyer or attorney admission;
- trademark-agent or patent-agent registration;
- notarial authority;
- authorized representative registration;
- regulated accountant or other professional credential where relevant;
- organization licence where professional authority is organization-based.

The review must not assume that the same credential categories or effects exist in every jurisdiction.

## 3. Source hierarchy

Potential source classes:

```text
S1 — official regulator or court register
S2 — official professional-body register
S3 — official licence or certificate supplied by the professional
S4 — authoritative organization confirmation
S5 — provider-supplied statement
S6 — public directory or commercial database
S7 — customer or third-party statement
S8 — inferred or AI-extracted candidate
```

A lower-class source must not be presented as equivalent to an official source.

```text
Provider says qualified
≠ regulator confirms current qualification
```

## 4. Minimum source fields

A qualification reference candidate should preserve:

```text
subject identity reference
credential type
credential identifier
issuing authority
jurisdiction
source class
source location or Document reference
source publication or retrieval time
external status as reported
platform verification status
verification method
last verified time
next recheck time
restrictions or scope reference
source rights and use restrictions
reviewer reference
```

## 5. External state versus platform verification state

Two state tracks must remain separate.

### External status candidate

Possible examples:

```text
Active
Restricted
Suspended
Expired
Revoked
Unknown
```

These labels may not be universal and require jurisdiction-specific mapping.

### Platform verification status

Research candidates:

```text
Unverified
SourceLocated
VerifiedCurrent
VerifiedWithRestriction
VerificationStale
SourceUnavailable
Conflicted
Rejected
```

```text
Platform verification status
≠ external credential status
```

MarkOrbit may control only its verification record.

## 6. Privacy questions

The review must determine:

- whether credential identifiers are personal data;
- whether disciplinary or suspension data is sensitive or restricted;
- whether public-register data may be copied or only referenced;
- whether historical disciplinary data may be retained after reinstatement;
- whether the professional must be notified;
- whether customer or Provider Workplaces may view the full record;
- whether cross-border transfer restrictions apply;
- whether automated monitoring is permitted;
- whether data may be used for ranking, training or marketing;
- which deletion, correction and objection rights apply.

## 7. Rights and database-use questions

For each source:

- Is automated crawling permitted?
- Is there an API or bulk-data licence?
- May MarkOrbit store the full result or only a reference and verification timestamp?
- May the record be redistributed to Products or customers?
- May screenshots or certificates be retained?
- Are there attribution requirements?
- Is model training permitted?
- Must stale copies be deleted after source correction?

```text
Publicly visible
≠ unrestricted reuse
≠ training permission
```

## 8. Purpose limitation

Permitted purposes may differ:

```text
provider onboarding
Matter-specific eligibility
professional-authority verification
customer disclosure
internal risk control
public directory display
network ranking
marketing
AI training
```

Approval for one purpose does not authorize all others.

## 9. Conflict and privileged-information boundary

Conflict clearance may be required before a professional is eligible for a Matter.

The qualification reference should not store privileged conflict details.

Preferred pattern:

```text
conflict check performed
result: clear / blocked / review required / unknown
checked by authorized actor
checked at time
Matter scope reference
restricted reason omitted
```

The platform should preserve the decision and trace without exposing confidential client relationships.

## 10. Verification cadence

Recheck frequency should depend on:

- source reliability;
- credential type;
- known update cadence;
- materiality of the planned action;
- last verified time;
- expiry date;
- source availability;
- disciplinary or restriction signal;
- upcoming protected action.

A current source check may be required immediately before a reserved action even when the scheduled recheck date has not arrived.

## 11. Correction and dispute process

A professional or source authority may dispute the platform record.

Required process:

```text
correction request received
→ preserve disputed version
→ restrict reliance where material
→ obtain source evidence
→ authorized review
→ correct or reject request
→ notify affected consumers
→ reassess active Eligibility and Assignments
```

A correction must not silently rewrite historical decisions.

## 12. AI boundaries

AI may:

- extract credential candidates;
- identify possible source matches;
- compare identifiers;
- flag stale or conflicting records;
- summarize public status.

AI must not:

- declare a qualification current without governed verification;
- infer professional authority from name similarity;
- infer appointment or conflict clearance;
- issue or revoke qualification;
- expose disciplinary details outside permitted scope.

```text
AI match
≠ verified credential
```

## 13. Jurisdiction research template

For each jurisdiction, document:

```yaml
jurisdiction_review:
  jurisdiction_reference_id: string
  profession_type: string
  issuing_authority: string
  official_register_available: boolean
  register_access_method: string
  credential_identifier_format: string
  public_status_fields: list[string]
  restricted_fields: list[string]
  source_terms_reviewed: boolean
  privacy_basis_reviewed: boolean
  permitted_storage: string
  permitted_redistribution: string
  verification_cadence: string
  appointment_separate_from_qualification: boolean
  reserved_actions: list[string]
  professional_reviewer_reference_id: string
  legal_review_reference_id: string
```

## 14. Initial jurisdiction sample requirement

Before any formal proposal, review at least three structurally different systems, for example:

- one jurisdiction with a public lawyer or attorney register;
- one jurisdiction with a separate trademark-agent register;
- one jurisdiction where filing representation is organization-based, limited or not publicly searchable.

The examples must be researched from current authoritative sources at the time of the formal review. This publication batch does not supply those legal conclusions.

## 15. Negative fixture requirements

Reject a qualification reference when:

```text
issuing authority absent
source class absent
subject identity unresolved
credential identifier inferred from name only
platform verification and external status are merged
stale verification used for protected action
restriction data exposed without permission
Provider listing treated as qualification
qualification treated as Matter appointment
AI candidate treated as verified
source terms prohibit the intended storage or reuse
```

## 16. Formal proposal entry criteria

`B02-CP-RESEARCH-A1` may become a formal Change Proposal only after:

1. three-jurisdiction source review;
2. legal and professional review;
3. privacy and source-rights review;
4. external-state/platform-verification split confirmed;
5. stable minimum field set identified;
6. at least two independent consumers identified;
7. correction and dispute process defined;
8. positive and negative fixtures drafted;
9. Owning Service and mutation authority proposed;
10. compatibility and migration impact assessed.

## 17. Review-plan verdict

```text
Source hierarchy defined: YES
Privacy questions defined: YES
Rights questions defined: YES
Jurisdiction conclusions completed: NO
Legal review completed: NO
Professional review completed: NO
Formal proposal gate passed: NO
Research may proceed: YES
```
