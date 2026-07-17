# B07-PLN-0017 — Reader Apparatus and Publication Validation Plan

## Purpose

Book 07 is a controlled Product Book with dense terminology and IDs. It requires navigational apparatus tailored to MGSN rather than a generic appendix copied from earlier books.

## Required apparatus

### APP-A — Controlled Terminology Glossary

Must define at least:

- Organization;
- Workplace;
- Product Installation;
- Projection;
- Handoff;
- Return;
- Owning Service;
- Originating Workplace;
- Execution Provider Workplace;
- MGSN Connection / Gateway;
- MGSN Network;
- Managed Network Engagement;
- Capability Claim, Evidence, Verification, Qualification and Availability;
- Candidate Route Set, Recommendation, User Disposition, Allocation and Provider Acceptance;
- Relationship Provenance;
- Trust;
- Incident, Correction, Replacement, Dispute, Restriction, Suspension and Retirement.

### APP-B — Product-Local Record Index

Index all 56 records by family:

```text
MG-N — Network Participation and Connection
MG-C — Capability and Supply
MG-P — Procurement and Service Offer
MG-R — Routing, Recommendation and Selection
MG-F — Funds, Fulfillment and Return
MG-T — Trust, Relationship and Network Learning
MG-E — Exception, Restriction and Governance
```

Each entry should point to its principal specification and primary manuscript chapter.

### APP-C — Reference Journey Index

List MG-J01–MG-J08 with:

- short title;
- primary chapters;
- route type;
- principal records and contracts;
- normal, exception or dual-role classification.

### APP-D — Conformance Scenario Index

List MG-SCN-01–MG-SCN-32 grouped by:

- participation and privacy;
- capability and supply;
- procurement and offers;
- routing and choice;
- funds and fulfillment;
- Trust and relationships;
- dual roles and governance.

### APP-E — Handoff / Return and Acceptance Index

Index:

- MG-HC-01–MG-HC-10;
- MG-AC-01–MG-AC-16;
- source, target and authority boundary;
- primary manuscript chapter.

### APP-F — Product and Implementation Boundary Notice

A concise reader-facing statement must clarify that publication acceptance does not itself authorize:

- filing or official acts;
- Provider appointment;
- payment custody or funds release;
- automated Trust sanctions;
- production deployment;
- cross-Workplace access beyond governed scope.

## Optional apparatus

- Part-level reading paths for Product, operations, finance, provider and governance readers;
- list of recurring controlled formulas and distinctions;
- implementation-prerequisite checklist derived from CH32;
- abbreviation index if abbreviations are used in the final manuscript.

## Publication validation

Final validation must confirm:

```text
Chapter sequence: CH00–CH33 continuous
Glossary terms resolved: 100%
Product-local records indexed: 56 / 56
Journeys indexed: 8 / 8
Scenarios indexed: 32 / 32
Handoff / Return contracts indexed: 10 / 10
MVP Acceptance Criteria indexed: 16 / 16
Broken internal references: 0
Duplicate controlled IDs: 0
Unresolved placeholders: 0
Implementation authorization leakage: 0
```

## Gate

Reader apparatus may be prepared alongside editorial hardening. Release Candidate review begins only after the apparatus and final validation are complete.
