# Status Workflow Contract Fixture Validation

Spec ID: B02-VAL-STATUS-WORKFLOW-CONTRACT-FIXTURES
Spec Type: Validation Specification
Validation Category: Fixture
Status: Draft
Version: 0.1.0
Owner: MarkOrbit Publications Editorial Board

# Target
Validate status contracts, workflow component contracts, fixture manifest, fixture envelopes, canonical matrices, scenario decisions, and protected-action fail-closed behavior.

# Source References
Controlled State Value Specifications, Workflow Component Specifications, Status Contracts, Workflow Component Contracts, and `contracts/fixtures/status-workflow/manifest.json`.

# Input
Publication markdown contracts and deterministic JSON fixtures.

# Validation Procedure
Run `python tools/validate_status_workflow_contract_fixtures.py`.

# Failure Conditions
Missing files, Spec ID drift, Contract Version absence, value/matrix drift, missing component fields, invalid manifest, orphan fixtures, non-synthetic data, production data, invalid decisions, Workflow mutation, unauthorized protected action, or secret-like fields.

# Severity
Release-blocking for Book 02 contract-layer publication.

# Fixture Requirements
Fixtures are deterministic, synthetic, non-production, stable JSON with no secrets or real customer/official data.

# Release Gate Usage
Required before accepting PUB-TASK-B02-003 and before future typed implementation mapping consumes this pack.

# Prohibited Overreach
Validator does not define architecture, runtime engine, database schema, production seed data, Service mutation, or external action authorization.

# Acceptance Criteria
Validator and negative validator tests pass; canonical values and transition matrices do not drift; Workflow validation remains route-only with `mutation_performed=false`.
