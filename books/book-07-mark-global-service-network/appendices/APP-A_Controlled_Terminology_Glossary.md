# APP-A — Controlled Terminology Glossary

## Purpose

This glossary provides reader-facing definitions for recurring controlled terms in Book 07. It supports navigation and interpretation; it does not replace the Active Canon, Core specifications or `B07-SPEC-0001–0004`.

## Authority and workspace terms

### Organization

The stable participant identity. An Organization may act in a Demand Role, Supply Role or both, while permissions, financial contexts and conflicts remain separated.

Primary chapters: CH05–CH06.

### Workplace

The Organization-scoped business-sovereignty and Product-operation boundary for customer relationships, private Knowledge, permissions, approvals and authorized projections.

Primary chapters: CH04–CH06.

### Product Installation

A deployed or configured Product context connected to a Workplace. It does not by itself own the shared MGSN Network.

Primary chapters: CH04, CH06, CH32.

### Originating Workplace

The Workplace that owns the customer relationship and originates the Capability Need. It controls purpose, disclosure, internal commercial context and User Disposition.

Primary chapters: CH04, CH16, CH20, CH25.

### Execution Provider Workplace

The provider-side Workplace responsible for professional performance, internal operations, professional judgment and provider-side Evidence.

Primary chapters: CH04, CH21, CH23, CH25.

### Owning Service

The authoritative service permitted to create or mutate a defined formal business state. Receipt of a Return does not bypass Owning Service validation.

Primary chapters: CH01, CH04, CH25, CH32.

### MGSN Connection / Gateway

The Workplace-scoped interface and permission boundary through which a Product projects needs and receives controlled results.

Primary chapters: CH02, CH04, CH06, CH32.

### MGSN Network

The platform-owned managed network governing admitted supply, procurement, routing, funds and fulfillment projections, Trust and network governance.

Primary chapters: CH02–CH03, CH32.

## Cross-boundary information terms

### Projection

A purpose-limited view of source information. Projection does not transfer ownership or unrestricted access to the source record.

Primary chapters: CH04, CH16.

### Handoff

An authorized transmission to another Product, Workplace or responsibility boundary. Sending a Handoff does not mean the destination accepted or executed it.

Primary chapters: CH04, CH20–CH25; APP-E.

### Return

A typed, source-qualified response carrying an outcome, Evidence, uncertainty and next-action context back to the originating boundary.

Primary chapters: CH23–CH25; APP-E.

### Evidence

Source-aware material supporting a Claim, milestone, outcome, Trust assessment or governance decision. Evidence must retain source, scope, date and authority quality.

Primary chapters: CH08, CH23, CH25, CH27.

### Verification

A governed assessment of Evidence. Verification states what was checked, against which source, by whom, when and with what uncertainty.

Primary chapter: CH08.

## Supply terms

### Provider Network Profile

The MGSN-local provider representation linked to a stable Organization. It is not the Organization itself or a public marketing profile.

Controlled record: `MG-C01`.
Primary chapter: CH07.

### Capability Claim

A provider assertion that it can perform a defined service in a defined context. A Claim is not proof, Verification, Qualification or Availability.

Controlled record: `MG-C02`.
Primary chapters: CH07–CH08.

### Qualification

The current service- and jurisdiction-specific determination that a provider may perform a Capability through MGSN under applicable controls.

Controlled record: `MG-C05`.
Primary chapters: CH08, CH18.

### Availability

The time-sensitive declaration or assessment that a qualified provider can take the present work under the required timing and capacity conditions.

Controlled record: `MG-C06`.
Primary chapters: CH08, CH18.

### Supply Portfolio Entry

The network-governed placement of an admitted provider Capability in a defined jurisdiction and service portfolio.

Controlled record: `MG-C07`.
Primary chapter: CH09.

### Service Package

The admitted, versioned service definition covering scope, exclusions, deliverables, assumptions, Evidence, timing and commercial conditions.

Controlled record: `MG-C08`.
Primary chapters: CH10, CH14.

## Commercial and routing terms

### Capability Need Projection

The minimum-necessary MGSN projection of a service need owned by an Originating Workplace or authorized Product.

Controlled record: `MG-R01`.
Primary chapter: CH16.

### R1 — External Self-Managed Route

A route managed outside MGSN provider, procurement, funds, fulfillment and replacement controls. MGSN may support limited continuity and an external Evidence bridge.

Primary chapters: CH17, CH20, CH25.

### R2 — MGSN Recommended Managed Route

The default managed route in which MGSN evaluates admitted supply, recommends a route, obtains User Disposition and coordinates Provider Acceptance and fulfillment.

Primary chapters: CH17–CH21.

### R3 — MGSN Managed Preferred-Provider Route

A managed route that considers the Originating Workplace's preferred provider while retaining admission, Qualification, conflict, Availability, procurement and risk gates.

Primary chapters: CH17–CH20, CH26.

### Candidate Route Set

The temporary, need-specific set of eligible routes that survived required gates. It is not a permanent provider ranking.

Controlled record: `MG-R05`.
Primary chapter: CH19.

### Recommendation

The explainable MGSN proposal of one best-supported route and, where useful, up to two materially different alternatives.

Controlled record: `MG-R06`.
Primary chapter: CH19.

### User Disposition

The authorized Originating Workplace decision to confirm, reject, rematch, request a preferred provider, choose R1, defer or cancel.

Controlled record: `MG-R07`.
Primary chapter: CH20.

### Provider Allocation

The platform decision preparing a selected provider route for instruction, subject to readiness and acceptance controls.

Controlled record family: `MG-R08`.
Primary chapter: CH20.

### Provider Acceptance

The provider's explicit acceptance, conditional acceptance or refusal of a defined engagement. Acceptance is not completion.

Controlled record family: `MG-R08`, `MG-F05`.
Primary chapters: CH20–CH21.

### Managed Network Engagement

The MGSN-local operating envelope linking an authorized need, selected route, accepted offer, provider commitment, funds conditions, milestones and Return obligations.

Controlled record: `MG-F01`.
Primary chapter: CH21.

## Fulfillment and governance terms

### Funds Requirement

The amount, purpose, currency, timing and authority prerequisites required before a defined engagement or action may proceed.

Controlled record: `MG-F02`.
Primary chapter: CH22.

### Fulfillment Milestone

A typed checkpoint in the accepted Service Package or Engagement with expected actor, timing, Evidence and escalation conditions.

Controlled record: `MG-F06`.
Primary chapter: CH23.

### Fulfillment Observation

MGSN's source-qualified observation of progress or deviation. It is not automatically official or Matter truth.

Controlled record: `MG-F08`.
Primary chapter: CH23.

### Return Envelope

The typed package carrying outcomes, Evidence, uncertainty, next actions and provenance to the receiving Workplace or Product.

Controlled record: `MG-F09`.
Primary chapter: CH25.

### Relationship Provenance

The governed record of who introduced whom, prior relationship context, consent, scope and bounded attribution.

Controlled record: `MG-T01`.
Primary chapter: CH26.

### Trust

A multidimensional, service-specific, jurisdiction-specific, source-aware, time-scoped, correctable and appealable assessment used in routing and governance.

Controlled record: `MG-T05`.
Primary chapter: CH27.

### Network Learning Candidate

A proposed insight derived from governed records that may inform procurement, routing, service design or provider review after contextual assessment.

Controlled record: `MG-T06`.
Primary chapter: CH28.

### Provider Evolution Decision

A formal network decision to maintain, expand, narrow, remediate, restrict, suspend, retire or restore a provider scope.

Controlled record: `MG-T08`.
Primary chapter: CH28.

### Incident

A material deviation from an accepted engagement requiring review. An Incident is not automatically proof of fault.

Controlled record: `MG-E01`.
Primary chapter: CH24.

### Correction

A governed request to repair a defined deficiency without silently expanding the original scope.

Controlled record: `MG-E02`.
Primary chapter: CH24.

### Replacement

A controlled change of responsible provider after engagement, preserving authorization, Evidence, deadlines, funds and continuity.

Controlled record: `MG-E03`.
Primary chapter: CH24.

### Dispute

A governed case for material disagreement concerning scope, quality, Evidence, funds, attribution, Trust or responsibility.

Controlled record: `MG-E04`.
Primary chapter: CH29.

### Restriction

A scoped narrowing of a Capability, route, visibility or activity.

Controlled record: `MG-E05`.
Primary chapters: CH28–CH29.

### Suspension

A temporary disabling of participation, allocation or supply scope, subject to review and possible restoration.

Controlled record: `MG-E06`.
Primary chapters: CH28–CH29.

### Retirement

The governed ending of a defined active network role or supply scope.

Controlled record: `MG-E07`.
Primary chapters: CH28–CH29.

### Appeal and Governance Review

The controlled review of an admission, Trust, Restriction, Suspension, Retirement or other material adverse decision.

Controlled record: `MG-E08`.
Primary chapter: CH29.

## Controlling distinctions

```text
Organization ≠ Provider Network Profile
Capability Claim ≠ Evidence ≠ Verification
Qualification ≠ Availability
Recommendation ≠ User Disposition
User Disposition ≠ Provider Allocation
Provider Allocation ≠ Provider Acceptance
Provider Acceptance ≠ completion
Projection ≠ Handoff ≠ Return
Funds Allocation ≠ Finance ledger
Fulfillment Observation ≠ formal Matter truth
Return received ≠ formal-state mutation
Relationship Provenance ≠ counterparty ownership
Trust ≠ universal public score
Product publication ≠ implementation authority
```