# Contracts — MANIFEST

**Spec ID:** B02-CONTRACT-MANIFEST  
**Spec Type:** Contract Layer Manifest  
**Contract File:** core-specs/contracts/MANIFEST.md  
**Contract Category:** Core Contracts  
**Related Index:** core-specs/contracts/index.md  
**Related Contract Layers:** Common Contracts; API Contracts; Workflow Contracts; Test Contracts  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 0–5 — Core Contract Packaging  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This MANIFEST defines the canonical packaging checklist for the MarkOrbit Core Contract layer.

It is used to verify that the contract layer is complete enough to be:

```text
reviewed
packaged
versioned
handed to Codex
implemented
tested
published as part of Book 02
```

This file is a packaging and completeness manifest. It does not replace:

```text
core-specs/contracts/index.md
core-specs/contracts/common/index.md
core-specs/contracts/api/index.md
core-specs/contracts/workflows/index.md
core-specs/contracts/tests/index.md
```

---

# 2. Core Lock

```text
MANIFEST verifies contract-layer completeness.
Contracts define governed interaction boundaries.
Common Contracts provide shared primitives.
API Contracts define request and response boundaries.
Workflow Contracts define governed execution patterns.
Test Contracts verify Core behavior.
Owning services own behavior.
Permission and Policy govern protected actions.
AI remains bounded by Agent Governance.
Events preserve trace.
```

---

# 3. Package Root

```text
core-specs/contracts/
```

Expected package name:

```text
markorbit-core-contracts-v0.1.0
```

Expected package scope:

```text
Common Contracts
API Contracts
Workflow Contracts
Test Contracts
Contract Indexes
Contract README files
Contract Templates
MANIFEST
```

---

# 4. Top-Level Files

```text
core-specs/contracts/README.md
core-specs/contracts/template.md
core-specs/contracts/index.md
core-specs/contracts/MANIFEST.md
```

Checklist:

```text
[ ] README.md exists.
[ ] template.md exists.
[ ] index.md exists.
[ ] MANIFEST.md exists.
```

---

# 5. Common Contracts Manifest

Expected files:

```text
core-specs/contracts/common/README.md
core-specs/contracts/common/template.md
core-specs/contracts/common/index.md
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/pagination.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/versioning.md
```

Checklist:

```text
[ ] Common README exists.
[ ] Common template exists.
[ ] Common index exists.
[ ] Reference Contract exists.
[ ] Error Contract exists.
[ ] Pagination Contract exists.
[ ] Audit Context Contract exists.
[ ] AI Context Contract exists.
[ ] Human Review Contract exists.
[ ] Permission Context Contract exists.
[ ] Policy Context Contract exists.
[ ] Idempotency Contract exists.
[ ] Versioning Contract exists.
```

Required status:

```text
All Common Contracts are Must Implement or Must Maintain.
```

---

# 6. API Contracts Manifest

Expected API layer files:

```text
core-specs/contracts/api/README.md
core-specs/contracts/api/template.md
core-specs/contracts/api/index.md
```

Foundation API Contracts:

```text
core-specs/contracts/api/identity-api-contract.md
core-specs/contracts/api/organization-api-contract.md
core-specs/contracts/api/user-api-contract.md
core-specs/contracts/api/permission-api-contract.md
core-specs/contracts/api/policy-api-contract.md
core-specs/contracts/api/knowledge-api-contract.md
```

Professional API Contracts:

```text
core-specs/contracts/api/brand-api-contract.md
core-specs/contracts/api/trademark-api-contract.md
core-specs/contracts/api/jurisdiction-api-contract.md
core-specs/contracts/api/classification-api-contract.md
core-specs/contracts/api/document-api-contract.md
core-specs/contracts/api/evidence-api-contract.md
```

Business Execution API Contracts:

```text
core-specs/contracts/api/customer-api-contract.md
core-specs/contracts/api/matter-api-contract.md
core-specs/contracts/api/order-api-contract.md
core-specs/contracts/api/opportunity-api-contract.md
core-specs/contracts/api/workflow-contract-api-contract.md
core-specs/contracts/api/task-api-contract.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/api/notification-api-contract.md
core-specs/contracts/api/communication-api-contract.md
```

Collaboration Network API Contracts:

```text
core-specs/contracts/api/agent-api-contract.md
core-specs/contracts/api/service-provider-api-contract.md
core-specs/contracts/api/routing-api-contract.md
core-specs/contracts/api/partner-api-contract.md
core-specs/contracts/api/service-network-api-contract.md
```

Checklist:

```text
[ ] API README exists.
[ ] API template exists.
[ ] API index exists.
[ ] 6 Foundation API Contracts exist.
[ ] 6 Professional API Contracts exist.
[ ] 9 Business Execution API Contracts exist.
[ ] 5 Collaboration Network API Contracts exist.
[ ] Total 26 domain API Contracts exist.
```

Required status:

```text
All 26 API Contracts are Must Implement for Core interface completeness.
```

---

# 7. Workflow Contracts Manifest

Expected workflow layer files:

```text
core-specs/contracts/workflows/README.md
core-specs/contracts/workflows/template.md
core-specs/contracts/workflows/index.md
```

Must Implement Workflow Contracts:

```text
core-specs/contracts/workflows/customer-intake-workflow-contract.md
core-specs/contracts/workflows/trademark-application-workflow-contract.md
core-specs/contracts/workflows/office-action-response-workflow-contract.md
core-specs/contracts/workflows/provider-routing-workflow-contract.md
core-specs/contracts/workflows/communication-review-workflow-contract.md
```

Should Implement Workflow Contracts:

```text
core-specs/contracts/workflows/renewal-workflow-contract.md
core-specs/contracts/workflows/assignment-workflow-contract.md
core-specs/contracts/workflows/evidence-review-workflow-contract.md
```

Checklist:

```text
[ ] Workflow README exists.
[ ] Workflow template exists.
[ ] Workflow index exists.
[ ] Customer Intake Workflow Contract exists.
[ ] Trademark Application Workflow Contract exists.
[ ] Office Action Response Workflow Contract exists.
[ ] Provider Routing Workflow Contract exists.
[ ] Communication Review Workflow Contract exists.
[ ] Renewal Workflow Contract exists.
[ ] Assignment Workflow Contract exists.
[ ] Evidence Review Workflow Contract exists.
[ ] Total 8 Workflow Contracts exist.
```

---

# 8. Test Contracts Manifest

Expected test layer files:

```text
core-specs/contracts/tests/README.md
core-specs/contracts/tests/template.md
core-specs/contracts/tests/index.md
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/agent-boundary-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
```

Checklist:

```text
[ ] Test README exists.
[ ] Test template exists.
[ ] Test index exists.
[ ] Common Contract Tests exist.
[ ] API Contract Tests exist.
[ ] Workflow Contract Tests exist.
[ ] Agent Boundary Tests exist.
[ ] Permission Policy Tests exist.
[ ] Idempotency Event Tests exist.
[ ] Error Versioning Tests exist.
[ ] Total 7 Test Contract files exist, excluding README/template/index.
```

---

# 9. Required Cross-References

Every API Contract should reference:

```text
Reference Contract
Error Contract
Permission Context Contract
Policy Context Contract
Versioning Contract
Idempotency Contract where duplicate-sensitive
Pagination Contract where list/search is supported
AI Context Contract where AI-assisted behavior is supported
Human Review Contract where protected review gates exist
Audit Context Contract where event trace appears
```

Every Workflow Contract should reference:

```text
Workflow Contract Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service where AI-assisted behavior is supported
Reference Contract
Error Contract
Permission Context Contract
Policy Context Contract
AI Context Contract
Human Review Contract
Idempotency Contract
Versioning Contract
```

Every Test Contract should reference:

```text
source contracts being tested
Common Contracts used by the tested behavior
related API/Workflow/Agent/Event/Service specs
deterministic fixture rules
positive and negative test rules
```

---

# 10. Required Governance Checks

Package is acceptable only if the contract layer preserves:

```text
No database ID exposure.
No restricted data leakage.
No Permission bypass.
No Policy bypass.
No AI autonomous protected action.
No hidden Human Review requirement.
No duplicate side effects on idempotent replay.
No direct Event emission from API/Workflow/Agent layers.
No Event reference treated as command.
No unsafe error.
No unsupported version accepted silently.
No historical version rewritten silently.
```

---

# 11. Codex Handoff Checklist

Before handing this package to Codex:

```text
[ ] Confirm top-level contract files exist.
[ ] Confirm all Common Contracts exist.
[ ] Confirm all 26 API Contracts exist.
[ ] Confirm all 8 Workflow Contracts exist.
[ ] Confirm all Test Contracts exist.
[ ] Confirm each layer has README, template and index.
[ ] Confirm Permission/Policy governance is present.
[ ] Confirm AI boundaries are present.
[ ] Confirm Human Review governance is present.
[ ] Confirm Idempotency/Event governance is present.
[ ] Confirm Error/Versioning governance is present.
[ ] Confirm Test Contracts cover negative cases.
[ ] Confirm no file assigns business behavior ownership to contracts.
[ ] Confirm no workflow creates active Tasks outside Task Service.
[ ] Confirm no API/Workflow/Agent layer emits Events directly.
```

---

# 12. Package Acceptance Matrix

```yaml
package_acceptance:
  top_level:
    required: true
    files_expected: 4
    status: pending_review

  common_contracts:
    required: true
    files_expected: 13
    status: pending_review

  api_contracts:
    required: true
    files_expected: 29
    domain_api_contracts_expected: 26
    status: pending_review

  workflow_contracts:
    required: true
    files_expected: 11
    workflow_contracts_expected: 8
    status: pending_review

  test_contracts:
    required: true
    files_expected: 10
    test_contracts_expected_excluding_readme_template_index: 7
    status: pending_review

  governance:
    permission_policy_required: true
    ai_boundary_required: true
    human_review_required: true
    idempotency_event_required: true
    error_versioning_required: true
    status: pending_review
```

---

# 13. Version Notes

```text
Manifest Version: v0.1.0
Contract Layer Version: v0.1.0
Book: Book 02 — MarkOrbit Core Specification
Package: markorbit-core-contracts-v0.1.0
```

Versioning rules:

```text
- New required contract file requires MANIFEST update.
- Removed required contract file requires MANIFEST version bump.
- Renamed contract file requires MANIFEST version bump.
- Breaking change in contract inventory requires MANIFEST version bump.
- Historical package manifests must not be silently rewritten.
```

---

# 14. Acceptance Criteria

This MANIFEST is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines package root.
[ ] It lists top-level files.
[ ] It lists Common Contracts.
[ ] It lists API Contracts.
[ ] It lists Workflow Contracts.
[ ] It lists Test Contracts.
[ ] It defines required cross-references.
[ ] It defines governance checks.
[ ] It defines Codex handoff checklist.
[ ] It defines package acceptance matrix.
[ ] It defines version notes.
```

---

# 15. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Contracts MANIFEST. Defines contract package root, top-level/common/API/workflow/test inventories, cross-reference expectations, governance checks, Codex handoff checklist, package acceptance matrix and version rules. |

---

**End of Contracts MANIFEST**


# PUB-TASK-B02-003 Status/Workflow Contract Fixture Coverage

Contract Layer Map additions: `contracts/status/`, `contracts/fixtures/status-workflow/`, and `contracts/workflows/components/`. Traceability: Controlled State Value Specification -> Status Contract -> API Contract -> Fixture -> Validator -> future typed implementation. Workflow Component Specification -> Workflow Component Contract -> Workflow Contract/API Contract -> Fixture -> Validator -> future typed implementation.
