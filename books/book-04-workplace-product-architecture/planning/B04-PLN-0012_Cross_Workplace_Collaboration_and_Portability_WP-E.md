# B04-PLN-0012 — Cross-Workplace Collaboration and Portability WP-E

## Status
Candidate controlled plan.

## Purpose
Define the final thematic amendment package before full-book integration review.

## Scope
CH12, CH27, CH32–CH37.

## Control model
Cross-Workplace collaboration is a governed exchange between independent authority boundaries. It does not collapse those boundaries.

```text
Originating Workplace
→ scoped authorization
→ typed Handoff
→ destination acceptance
→ Execution Provider Workplace action
→ typed Return
→ originating acceptance
```

## Required rules
1. Access is purpose-limited, time-bounded, role-bounded and auditable.
2. Handoff requires explicit scope, provenance, destination and acceptance state.
3. Return requires provenance and originating acceptance before local reliance or formal-state mutation.
4. Revocation stops future access but does not erase valid historical evidence.
5. Export must distinguish portable organization-controlled records from restricted, licensed or platform-owned assets.
6. Migration must preserve identity references, provenance, audit history and unresolved obligations.
7. Platform-owned Provider Supply, Routing assets and Network Trust assets are not exported as Workplace property.
8. Participant-specific relationship history and evidence may be portable only to the extent authorized and legally permitted.

## Portability classes
- Portable: organization identity/configuration, organization-controlled customer and relationship data, private Knowledge, organization-authored templates, authorized Artifacts and audit exports.
- Conditionally portable: licensed content, third-party records, Provider evidence, derived intelligence and shared collaboration records.
- Non-portable as owned assets: platform shared Provider Supply, global Routing models, network-wide Trust assets, platform security controls and other participants' private data.

## Gate
Owner merge authorizes WP-F full-book impact review and next-version decision. It does not authorize automatic migration, deletion, production export or an integrated baseline.