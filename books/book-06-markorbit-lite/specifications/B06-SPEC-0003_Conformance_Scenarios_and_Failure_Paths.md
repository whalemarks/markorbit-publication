# B06-SPEC-0003 — Conformance Scenarios and Failure Paths

## 1. Identity

```text
Specification: B06-SPEC-0003
Version: v0.1
Status: Candidate — accepted as Product Baseline on owner merge
Controlled scenarios: ML-SCN-01–ML-SCN-24
```

## 2. Scenario rule

A scenario PASS demonstrates observable Product behavior, not merely a UI element or feature claim.

Severity:

- **BLOCKING** — violation invalidates the affected capability or pilot;
- **MAJOR** — must be corrected before a baseline or release;
- **STANDARD** — expected conforming behavior.

## 3. Customer and Service Growth

| ID | Scenario | Expected result | Severity |
| --- | --- | --- | --- |
| ML-SCN-01 | Authorized portfolio reveals a valid maintenance/service gap | Explainable `ML-O03`; work product and Handoff can be prepared | STANDARD |
| ML-SCN-02 | Source is stale or conflicting | Candidate shows warning or is blocked; no confident recommendation | MAJOR |
| ML-SCN-03 | User lacks customer or Matter access | No restricted facts exposed; preparation blocked | BLOCKING |
| ML-SCN-04 | User accepts a Service-Value Candidate | Candidate remains Product-local until Opportunity Service returns formal reference | BLOCKING |
| ML-SCN-05 | Customer response confirms a real need | Qualification result may prepare MarkReg/Opportunity Handoff | STANDARD |
| ML-SCN-06 | Revenue value conflicts with client interest or professional risk | Client interest/risk controls ranking and action | BLOCKING |

## 4. Historical customer and prospect development

| ID | Scenario | Expected result | Severity |
| --- | --- | --- | --- |
| ML-SCN-07 | Historical customer contact is stale | Contactability limitation visible; user must verify | MAJOR |
| ML-SCN-08 | Historical customer opted out | Candidate suppressed; no outreach package prepared | BLOCKING |
| ML-SCN-09 | Public source produces Prospect Candidate | Source, freshness, relevance and limitations preserved | STANDARD |
| ML-SCN-10 | Contact detail exists but channel permission is unknown | No claim that contact is permitted; final channel decision required | BLOCKING |
| ML-SCN-11 | Duplicate prospect appears across sources | Deduplicate or show shared identity; preserve provenance | MAJOR |
| ML-SCN-12 | Platform prospect is invalid | Record invalid result and commercial replacement evidence without creating Customer | STANDARD |

## 5. Professional work products

| ID | Scenario | Expected result | Severity |
| --- | --- | --- | --- |
| ML-SCN-13 | AI generates raw text | Remains Content/draft; not represented as approved Artifact | BLOCKING |
| ML-SCN-14 | Artifact is rendered successfully | Render result exists; professional approval still separate | BLOCKING |
| ML-SCN-15 | Render fails or deterministic fields mismatch | Work product remains incomplete/failed; entitlement not falsely fulfilled | MAJOR |
| ML-SCN-16 | Publish Package is ready | Product shows ready-for-confirmation, not published | BLOCKING |
| ML-SCN-17 | User edits after review | New Artifact Version requires review/confirmation as applicable | MAJOR |
| ML-SCN-18 | External publication outcome is unknown | Preserve unknown; no blind retry or completed state | BLOCKING |

## 6. Cases, memory and reusable capability

| ID | Scenario | Expected result | Severity |
| --- | --- | --- | --- |
| ML-SCN-19 | Case contains Client/Matter Restricted facts | Restricted facts excluded or use blocked | BLOCKING |
| ML-SCN-20 | User wants to reuse a successful case | Create lesson/Asset candidate; no universal rule inferred | MAJOR |
| ML-SCN-21 | Personal preference is repeatedly observed | Remains candidate until explicit acceptance and scope | STANDARD |
| ML-SCN-22 | Organization memory promotion requested | Organization review and provenance required | BLOCKING |

## 7. Handoff, local data and formal state

| ID | Scenario | Expected result | Severity |
| --- | --- | --- | --- |
| ML-SCN-23 | Lite sends MarkReg/MGSN/Review/Communication Handoff | Destination revalidates; returned result retains origin and source | BLOCKING |
| ML-SCN-24 | Local file is readable but synchronization is not authorized | Local access does not imply upload, sharing or authority | BLOCKING |

## 8. Required cross-scenario assertions

Every scenario set must additionally demonstrate:

- Today item is not an active Task;
- Service-Value Candidate and Prospect Candidate are not formal Opportunities;
- Artifact is not Document or Evidence;
- Handoff is not approval;
- Return is not Lite-owned formal truth;
- User confirmation is not Human Review;
- content count and lead count alone cannot pass MVP 0;
- blocked unsafe action counts as a Product success.

## 9. Failure-path preservation

The Product must preserve at least:

```text
stale
incomplete
unsupported
blocked_by_permission
blocked_by_policy
review_required
rejected
failed
unknown_external_outcome
expired
suppressed
retired
```

Flattening these states into `Done`, `Failed` or `Not interested` is non-conforming.

## 10. Baseline result

A Product Baseline review passes only if all BLOCKING scenarios are explicitly represented and no Specification grants formal authority to Lite.
