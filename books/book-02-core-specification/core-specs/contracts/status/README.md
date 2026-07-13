# Status Contracts

## Purpose
Status Contracts define enforceable request, validation decision, and owner-Service result shapes for parent-owned controlled status values.

## Canonical ownership
A Status Contract consumes a Controlled State Value Specification. It does not own current state, perform mutation, or create a separate status source of truth.

## Directory inventory
- `status-transition-contract.md` — shared transition request, decision, and result contract.
- `trademark-status-contract.md` — Trademark status contract.
- `order-status-contract.md` — Order status contract.
- `matter-status-contract.md` — Matter status contract.
- `task-status-contract.md` — Task status contract.

## Contract-to-spec relationship
The canonical values and transition matrices remain in [Controlled State Values](../../controlled-state-values/index.md). Domain contracts must match those specifications exactly.

## Status transition boundary
The contract validates and routes. The owning Service performs mutation and emits/audits the result.

## Fixture relationship
The canonical publication fixture pack is [Status Workflow Fixtures](../fixtures/status-workflow/index.md).

## Versioning rule
Contract versions may clarify guards and shapes but cannot silently expand canonical state truth.

## Prohibited use
No independent Status Core Object, Workflow State mapping, runtime engine, endpoint path change, or protected external action authorization is created here.
