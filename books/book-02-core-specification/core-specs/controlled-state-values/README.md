# Controlled State Value Specifications

## Purpose

This directory defines parent-owned controlled state values, meanings, transition constraints and governance rules.

## Canonical rule

A Controlled State Value Specification defines the legal
values and transition semantics of a parent-owned state field.

It has no independent identity.
It is not an aggregate root.
It does not mutate itself.

## Ownership rule

Parent Object owns state truth.
Owning Service performs mutation.
Workflow Contract may constrain mutation.
Permission and Policy govern mutation.
Human Review governs sensitive decisions.
Event records the outcome.
Product consumes the result.
AI may explain or recommend only.

## Directory inventory

- [Trademark Status Values](trademark-status-values.md)
- [Order Status Values](order-status-values.md)
- [Matter Status Values](matter-status-values.md)
- [Task Status Values](task-status-values.md)

## Prohibited use

Do not treat status values as independent objects, create independent status IDs, create an independent status repository/table as source of truth, allow Product UI to add statuses, allow AI to invent states, bypass the owning Service, or treat unvalidated official status as professional truth.
