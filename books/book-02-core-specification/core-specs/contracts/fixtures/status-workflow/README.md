# Status Workflow Fixture Pack

## Purpose
Provides deterministic publication fixtures for Status Contracts and Workflow Component Contracts.

## Canonical source
Fixtures demonstrate contract behavior and consume canonical status/component specifications; they do not define architecture.

## Directory structure
- `status/trademark/`, `status/order/`, `status/matter/`, `status/task/`
- `workflow/`
- `manifest.json`

## Fixture envelope
Each case uses fixture_id, fixture_version, fixture_type, target_contract_id, target_spec_id, case_type, synthetic, contains_production_data, input, and expected.

## Fixture types
StatusMatrix, StatusTransition, WorkflowStateDefinition, WorkflowTransitionDefinition, WorkflowTransitionValidation.

## Case types
`positive` and `negative`.

## Decision-only versus performed-result semantics
Decision-only StatusTransition fixtures have `status_transition_result: null` and no Event expectation. Performed-result fixtures require Allowed decision, performed=true, status_changed=true, Event proof, audit proof, and performed_at.

## Synthetic data policy
All data is synthetic, non-production, safe to commit, and contains no real customer, trademark, agent, email, phone, credential, token, password, official record, or secret.

## Manifest rules
The manifest must exactly match fixture files and fixture envelope metadata.

## Versioning
Fixture version is v0.1.0 for this publication pack.

## Validator usage
Run `python ../../../../../tools/validate_status_workflow_contract_fixtures.py` from repository root.

## Prohibited use
Do not use as production runtime fixture data, seed data, service implementation, external action authorization, or typed implementation mapping.
