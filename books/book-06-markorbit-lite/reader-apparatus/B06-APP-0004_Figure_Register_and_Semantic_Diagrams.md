# B06-APP-0004 — Figure Register and Semantic Diagrams

## Status and authority

```text
Record: B06-APP-0004
Type: Reader-facing figure register
Status: Candidate — accepted on RC Hardening B owner merge
Figure format: GitHub-renderable Mermaid
Semantic review: COMPLETE FOR HARDENING B
Cross-format rendered validation: DEFERRED TO HARDENING C
Creates implementation architecture: NO
```

These figures explain accepted Book 06 relationships. They do not select database, API, model, provider, deployment or infrastructure design.

## Figure register

| Figure | Title | Primary reading | Semantic status |
| --- | --- | --- | --- |
| B06-FIG-01 | Lite position in MarkOrbit | CH03–CH06, CH26–CH29 | reviewed |
| B06-FIG-02 | Four connected Product loops | CH05, CH33 | reviewed |
| B06-FIG-03 | Today daily operating sequence | CH07–CH11 | reviewed |
| B06-FIG-04 | Observation to Candidate and Disposition | CH09–CH10 | reviewed |
| B06-FIG-05 | Growth sources and reference journeys | CH12–CH16 | reviewed |
| B06-FIG-06 | Professional work-product lifecycle | CH17–CH21 | reviewed |
| B06-FIG-07 | Case, memory, Asset and Knowledge paths | CH22–CH25 | reviewed |
| B06-FIG-08 | Common Handoff and Return model | CH11, CH26–CH29 | reviewed |
| B06-FIG-09 | Local/Private Hybrid Minimization | CH08, CH29 | reviewed |
| B06-FIG-10 | MVP 0 Customer Opportunity-to-Governed-Service Loop | CH30–CH31 | reviewed |
| B06-FIG-11 | Product identity to fulfillment evidence | CH32 | reviewed |
| B06-FIG-12 | Change classification ladder | CH33 | reviewed |

---

## <a id="b06-figure-01"></a>B06-FIG-01 — Lite position in MarkOrbit

```mermaid
flowchart LR
    U[Trademark professional<br/>or small Organization] --> L[MarkOrbit Lite<br/>daily Product surface]
    W[Workplace<br/>Organization context] -. authorized context .-> L
    C[Core<br/>shared meaning and formal objects] -. projections and references .-> L
    L -->|typed Handoff| MR[MarkReg<br/>trademark Product lifecycle]
    L -->|Capability Need Handoff| MG[MGSN<br/>Trust and Routing]
    L -->|Review / Communication / Opportunity / Task request| OS[Owning Services and Execution]
    MR -->|typed Return| L
    MG -->|typed Return| L
    OS -->|typed Return| L
```

**Semantic locks**

```text
Lite owns Product experience, candidates, preparation and continuity.
Owning Services own formal business truth.
Display or integration does not transfer ownership.
```

---

## <a id="b06-figure-02"></a>B06-FIG-02 — Four connected Product loops

```mermaid
flowchart TB
    T[Today and Continuation] --- G[Customer and Service Growth]
    T --- W[Professional Work Products]
    T --- M[Professional Memory and Business Assets]
    T --- H[MarkOrbit Ecosystem Handoff]
    G --> W
    W --> H
    H --> M
    M --> G
```

**Semantic locks**

- the loops are connected, not a mandatory linear workflow;
- Today is a daily cockpit, not the Product identity;
- no loop absorbs formal lifecycle ownership.

---

## <a id="b06-figure-03"></a>B06-FIG-03 — Today daily operating sequence

```mermaid
flowchart LR
    AC[Authorized Context] --> SO[Source Observations and Returns]
    SO --> AT[Today Snapshot and Attention Items]
    AT --> UD[User Disposition]
    UD --> PA[Prepared Action or Work Product]
    PA --> HR{Review / confirmation required?}
    HR -->|yes| HC[Human decision and exact confirmation]
    HR -->|no| NH[Permitted next Handoff]
    HC --> NH
    NH --> DR[Destination Result / Return]
    DR --> CT[Continuation, feedback, correction or retirement]
```

**Semantic locks**

```text
Today item ≠ active Task
Recommendation ≠ Decision
Prepared Action ≠ execution
Return ≠ Lite-owned formal truth
```

---

## <a id="b06-figure-04"></a>B06-FIG-04 — Observation to Candidate and Disposition

```mermaid
flowchart LR
    S[Authorized Source] --> O[ML-O01 Source Observation]
    O --> SG[ML-O02 Customer / Trademark Signal]
    SG --> C[Candidate family]
    C --> R[ML-O07 Recommendation Presentation]
    R --> D{ML-S04 User Disposition}
    D -->|accept for preparation| P[Work Product / Prepared Action]
    D -->|defer| DF[Deferred]
    D -->|reject| RJ[Rejected]
    D -->|suppress| SP[Suppressed]
    D -->|correct| CR[Correction Record]
    P --> Q[ML-O08 Qualification Result]
    Q --> H[Formalization Handoff where justified]
```

**Semantic locks**

- extraction does not create canonical truth;
- Candidate acceptance does not create formal Opportunity;
- qualification remains Product-local until destination acceptance.

---

## <a id="b06-figure-05"></a>B06-FIG-05 — Growth sources and reference journeys

```mermaid
flowchart TB
    A[Level A<br/>Existing Customer Opportunity] --> J1[ML-J01<br/>Portfolio Opportunity]
    B[Level B<br/>Historical Customer Reactivation] --> J2[ML-J02<br/>Reactivation]
    C[Level C<br/>User-Owned Prospect Candidate] --> J3[ML-J03<br/>Prospect Development]
    D[Level D<br/>Platform-Supplied Prospect Candidate] --> J3
    J1 --> DP[Development Package]
    J2 --> DP
    J3 --> DP
    DP --> CC[Confirmed Customer / Prospect Action]
    CC --> RS[Typed Response]
    RS --> Q[Qualification Result]
    Q --> FH[MarkReg / Opportunity / other formal Handoff]
```

**Semantic locks**

```text
Existing customer value is preferred before cold prospect volume.
Prospect Candidate ≠ purchase intent.
Relationship history ≠ current channel permission.
```

---

## <a id="b06-figure-06"></a>B06-FIG-06 — Professional work-product lifecycle

```mermaid
flowchart LR
    P[Purpose and Audience] --> AC[Authorized Context and Sources]
    AC --> SC[ML-W01 Structured Content]
    SC --> AD[ML-W02 Artifact Draft]
    AD --> AV[ML-W03 Immutable Version]
    AV --> RP[ML-W04 Review Package]
    RP --> RR{Review Result}
    RR -->|revision required| AD
    RR -->|approved within scope| RQ[ML-W07 Render Request]
    RQ --> RT[ML-W08 Render Result]
    RT --> RD[ML-W10 Readiness Result]
    RD --> PK[ML-W09 Delivery / Publish Package]
    PK --> CF[Exact-purpose confirmation]
    CF --> OP[Manual or governed operation]
    OP --> OUT[Outcome Observation]
    OUT --> FB[Feedback / Correction / Reuse / Retirement]
```

**Semantic locks**

```text
Content ≠ Artifact
Artifact ≠ Document / Evidence / file
Render complete ≠ approved
Package ready ≠ externally completed
```

---

## <a id="b06-figure-07"></a>B06-FIG-07 — Case, memory, Asset and Knowledge paths

```mermaid
flowchart TB
    CC[Authorized Case Context] --> CL[ML-M06 Case Lesson Candidate]
    OB[Observed behavior or explicit instruction] --> PC[ML-M03 Preference Candidate]
    CL --> HR[Human Review and scope decision]
    PC --> PA[Explicit personal acceptance]
    HR --> PM[ML-M04 Personal Memory Candidate]
    HR --> OM[ML-M05 Organization Memory Candidate]
    HR --> RA[ML-M07 Reusable Asset Candidate]
    HR --> KC[ML-M08 Knowledge Contribution Candidate]
    OM --> OR[Organization Review]
    RA --> AR[Rights, scope and Review]
    KC --> KG[Knowledge Governance Handoff]
    OR --> AO[Accepted Organization Memory]
    AR --> AA[Approved Reusable Asset]
    KG --> KR[Accepted / limited / revised / rejected Knowledge result]
```

**Semantic locks**

```text
case experience ≠ universal rule
personal memory ≠ Organization memory
Reusable Asset ≠ canonical Knowledge
anonymized ≠ authorized for publication
```

---

## <a id="b06-figure-08"></a>B06-FIG-08 — Common Handoff and Return model

```mermaid
sequenceDiagram
    participant U as User / Organization
    participant L as MarkOrbit Lite
    participant D as Destination Owning Service
    U->>L: Inspect exact Candidate / Artifact / Action
    U->>L: Review and confirmation where required
    L->>D: Versioned, minimized Handoff Envelope
    D->>D: Revalidate identity, authority, scope and duplicates
    alt accepted
        D-->>L: Formal reference or accepted result
    else more information required
        D-->>L: Missing information and continuation request
    else rejected or blocked
        D-->>L: Typed reason and safe alternatives
    else failed or unknown
        D-->>L: Failure or unknown external outcome
    end
    L-->>U: Sourced Return presentation and next safe step
```

**Semantic locks**

```text
Handoff ≠ destination acceptance
accepted request ≠ completed action
unknown outcome ≠ safe to retry
```

---

## <a id="b06-figure-09"></a>B06-FIG-09 — Local/Private Hybrid Minimization

```mermaid
flowchart LR
    LF[Local Only / Personal Private source] --> LP[Authorized local processing]
    LP --> DI[Minimum necessary derived information]
    DI --> UI[User inspection]
    UI --> DC{Disclosure authorized for this purpose?}
    DC -->|no| LC[Continue locally or stop]
    DC -->|yes| HP[Minimized Handoff Package]
    HP --> DS[Destination revalidation]
    DS --> RT[Typed Return]
```

**Semantic locks**

```text
readable locally ≠ synchronized
local processing ≠ remote AI permission
derived information retains restrictions
one authorized disclosure ≠ general sharing authority
```

---

## <a id="b06-figure-10"></a>B06-FIG-10 — MVP 0 Customer Opportunity-to-Governed-Service Loop

```mermaid
flowchart LR
    AC[ML-AC-01<br/>Authorized Context] --> OR[ML-AC-02/03<br/>Relevant, sourced opportunity]
    OR --> WP[ML-AC-04<br/>Useful Work Product]
    WP --> UA[ML-AC-05<br/>Confirmed User Action]
    UA --> TR[ML-AC-06<br/>Typed Response]
    TR --> Q[ML-AC-07<br/>Qualification]
    Q --> GH[ML-AC-08<br/>Governed Handoff]
    GH --> RC[ML-AC-09<br/>Return Continuity]
    RC --> CA[ML-AC-10<br/>Capability Accumulation]
    CA --> EV[ML-AC-12<br/>Product and Commercial Evidence]
    SA[ML-AC-11<br/>Safety and Privacy] -. mandatory across every transition .-> AC
    SA -.-> WP
    SA -.-> GH
    SA -.-> CA
```

**Semantic locks**

- `ML-AC-01–AC-11` are mandatory;
- `ML-AC-12` collects experiment-specific evidence;
- content volume or prospect volume alone cannot pass MVP 0.

---

## <a id="b06-figure-11"></a>B06-FIG-11 — Product identity to fulfillment evidence

```mermaid
flowchart LR
    PI[Product Identity<br/>what Lite is] --> PE[Product Edition<br/>who/context served]
    PE --> CP[Commercial Plan<br/>price, limits, support]
    CP --> EN[Entitlement Window<br/>what may be received or used]
    EN --> FO[Fulfillment Observation<br/>what was actually delivered]
    FO --> EE[Product and Economic Evidence]
    EE -. evidence may change plan .-> CP
    EE -. evidence may propose Increment .-> IN[Product Increment]
```

**Semantic locks**

```text
Product identity ≠ Commercial Plan
payment ≠ authority
file generated ≠ entitlement fulfilled
commercial evidence may change plan without silently changing constitution
```

---

## <a id="b06-figure-12"></a>B06-FIG-12 — Change classification ladder

```mermaid
flowchart TB
    A[Class A<br/>Editorial clarification] --> B[Class B<br/>Implementation change]
    B --> C[Class C<br/>Product Increment]
    C --> D[Class D<br/>Product Baseline change]
    D --> E[Class E<br/>Constitutional change]
    A -. no controlled meaning change .-> AR[Editorial review]
    B -. conformance evidence .-> IR[Implementation review / ADR]
    C -. map to records, scenarios and evidence .-> PR[Product Increment review]
    D -. version Specifications .-> BO[Owner acceptance]
    E -. revise Charter and cross-Book review .-> CO[Explicit constitutional decision]
```

**Semantic locks**

- a change is classified by meaning and responsibility, not development effort;
- Class D and E cannot enter through an ordinary implementation PR;
- price, provider and UI changes do not automatically change Product identity.

## Figure review rule

Each figure was checked against the Product Charter, `B06-SPEC-0001–0004` and the cited chapters for:

- ownership direction;
- Candidate/formal-state separation;
- Human decision visibility;
- typed Handoff and Return;
- failure and unknown states;
- commercial/Product separation;
- local/private boundaries;
- absence of implementation commitments.

Hardening C must validate Mermaid rendering, PDF/equivalent rendering, legibility, page breaks, links and font substitution before Release Candidate review.
