# B05-SPEC-0003 — Conformance Scenarios and User-Surface Contract

## Status

- **Status:** Controlled Draft
- **Applies to:** CH08–CH22
- **Purpose:** Convert Product principles into observable behavior

## 1. Scenario Format

Every material Product behavior should be expressible as:

```text
Given
When
Then
Authority boundary
Evidence retained
```

## 2. Priority Conformance Scenarios

### MR-SCN-01 — Applicant ambiguity

**Given** the user selects an operating subsidiary while existing portfolio records show the parent as owner.  
**When** the recommendation or intake reaches applicant confirmation.  
**Then** MarkReg displays the conflict, explains affected jurisdictions and documents, asks one targeted question, and blocks filing readiness until resolved or professionally overridden.  
**Authority boundary:** the Product does not choose the owner.  
**Evidence retained:** both source records, user response, professional decision, and affected artifact versions.

### MR-SCN-02 — Conflicting mark variants

**Given** the user uploads a logo different from the version used in the approved proposal.  
**When** Formal Intake is validated.  
**Then** MarkReg identifies the difference, creates a new candidate filing unit, and invalidates affected search, quote, and readiness assumptions.  
**Authority boundary:** visual similarity detection is assistance, not filing approval.  
**Evidence retained:** both files, comparison result, user selection, reviewer decision.

### MR-SCN-03 — Country-bundle comparison

**Given** the user requests “Europe” without specifying countries.  
**When** jurisdiction options are prepared.  
**Then** MarkReg compares EU, UK, and selected national routes without hiding separate scope, fees, representation, timing, and post-Brexit consequences.  
**Authority boundary:** a bundle is a comparison device, not one legal right.  
**Evidence retained:** jurisdictions considered, assumptions, versioned fee sources, selected option.

### MR-SCN-04 — Class uncertainty

**Given** a product spans hardware, software, and online retail activity.  
**When** class candidates are generated.  
**Then** MarkReg separates primary, related, optional, and unsupported classes; shows why each is suggested; and requests professional review where ambiguity is material.  
**Authority boundary:** automated classification is not final legal advice.  
**Evidence retained:** source business description, class-version source, confidence, reviewer changes.

### MR-SCN-05 — Invalid POA

**Given** a POA is uploaded with an unauthorized signatory or unacceptable signature form.  
**When** document validation occurs.  
**Then** MarkReg marks the document invalid for the stated purpose, explains the defect, identifies the acceptable replacement, and blocks the affected readiness dimension only.  
**Authority boundary:** file upload does not establish legal validity.  
**Evidence retained:** original file, validation rule version, defect, replacement request, later accepted version.

### MR-SCN-06 — Expired quote

**Given** a client attempts to accept a Quote after its validity period.  
**When** acceptance is submitted.  
**Then** MarkReg prevents acceptance of the expired version, preserves the attempted action, and requests repricing or explicit approved extension.  
**Authority boundary:** the Product cannot extend commercial validity without authority.  
**Evidence retained:** quote version, expiry, attempted acceptance, approval or revised quote.

### MR-SCN-07 — Official-fee change after acceptance

**Given** an official fee changes after client acceptance but before filing.  
**When** the relevant jurisdiction pack is updated.  
**Then** MarkReg evaluates the accepted quote terms, shows the variance, identifies who bears it, and requires revised acceptance when the commercial policy requires it.  
**Authority boundary:** no silent repricing.  
**Evidence retained:** old and new fee sources, quote terms, variance calculation, decision.

### MR-SCN-08 — Missing payment

**Given** professional preparation is complete but required payment has not been received.  
**When** filing readiness is evaluated.  
**Then** MarkReg shows professional readiness as ready and commercial/execution readiness as blocked.  
**Authority boundary:** payment status does not replace filing approval.  
**Evidence retained:** payment terms, payment status source, readiness result.

### MR-SCN-09 — Professional override

**Given** an automated rule warns that an item is unacceptable.  
**When** an authorized professional determines that a sourced local exception applies.  
**Then** MarkReg permits a reasoned override limited to the affected item and version.  
**Authority boundary:** only authorized Human Review can override the rule.  
**Evidence retained:** original warning, source, reviewer, reason, scope, expiry condition.

### MR-SCN-10 — Stale official status

**Given** the Product displays an official status retrieved 90 days ago.  
**When** a user opens a deadline-sensitive journey.  
**Then** MarkReg labels the status stale, prevents it from being treated as current authority, and requests source refresh or professional verification.  
**Authority boundary:** Product projection is not current official truth without timely source evidence.  
**Evidence retained:** source URL or identifier, retrieval time, refresh attempt, verified result.

## 3. CH08–CH22 User-Surface Matrix

| Chapter | User question resolved | Minimum information requested | Reused context | Options / explanation shown | Professional intervention | Primary user action | Next-state explanation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CH08 | What do I actually need? | objective, markets, product, timing, use, risk, budget | organization, client, brand, portfolio | interpreted need and assumptions | correct material ambiguity | confirm or edit Need Brief | recommendation can now be prepared |
| CH09 | Where and by which route? | launch markets and priorities | Need Brief, existing rights | required, recommended, optional, deferred routes | route suitability and local constraints | compare and select priorities | selected route feeds scope and cost |
| CH10 | Which market package is sensible? | budget and expansion preference | jurisdiction options | transparent bundles and independent consequences | exception and dependency review | choose or customize bundle | bundle becomes an Option Set, not one right |
| CH11 | What exactly should be filed? | mark forms and intended use | brand assets, prior filings | word, device, composite, local-language and variant units | filing-unit strategy | select candidate units | search, classes, and fees update |
| CH12 | Who should own and authorize it? | unresolved ownership and signatory facts | organization and portfolio records | conflicts, consequences, alternatives | ownership and authority judgment | confirm applicant and signatory | requirements regenerate where affected |
| CH13 | Which classes matter? | product/service facts not already known | business and filing-unit context | primary, related, optional and uncertain classes | material classification review | accept, remove, or ask for review | goods/services drafting begins |
| CH14 | Which goods and services should be claimed? | launch products and scope preference | classes, markets, business facts | mandatory, recommended, optional, local variants | wording and scope review | choose scope or request revision | fee and search scope update |
| CH15 | Should we search and what does risk mean? | risk tolerance and timing | marks, classes, jurisdictions | search modes, limitations, risk findings | interpretation and strategy | order search or proceed with recorded risk | recommendation and proposal update |
| CH16 | Which service option should I choose? | preference among confirmed options | all prior recommendation artifacts | comparable options, assumptions, exclusions | option suitability | select or request revision | selected scope enters quotation |
| CH17 | What will it cost? | billing/tax facts only if unresolved | scope, provider, fee, currency policy | official, professional, provider, tax and later fees | pricing approval or exception | review cost breakdown | valid Quote can be accepted |
| CH18 | What am I accepting and instructing? | authorized acceptance and any conditions | valid Quote and authority context | exact scope, expiry, payment and change rules | authority or exception review | accept Quote and issue instruction | Order trigger conditions become visible |
| CH19 | What formal facts are still needed? | only missing service-specific facts | confirmed strategy and organization data | progress, assumptions, conflicts and missing items | professional sufficiency review | complete or delegate intake | Requirement Set can be finalized |
| CH20 | Which documents and signatures are acceptable? | document-specific missing facts | applicant, jurisdiction, provider and service | scans/originals, signature, translation and legalization rules | validity review | upload, replace, sign or arrange original | document readiness updates |
| CH21 | Why are we not ready? | no new data unless resolving a blocker | all artifacts and formal statuses | separate readiness dimensions, blockers, warnings and expiry | override or approval | resolve blocker, accept risk, or request review | exact gate to handoff is shown |
| CH22 | What happens after confirmation? | final responsibility and handoff confirmation | accepted versions and readiness | Order, Matter, payment and Execution boundaries | final responsibility validation | authorize permitted handoff | formal references and expected return evidence shown |

## 4. Common Interaction Rules

1. Do not re-ask an authorized fact unless its source is stale, ambiguous, conflicting, or insufficient for the current purpose.
2. Always distinguish inferred values from user-confirmed and professionally approved values.
3. Display the consequence of changing a material answer before applying the change.
4. Show one primary next action and the reason it is available or blocked.
5. Preserve alternatives and prior versions after a selection.
6. Never collapse commercial, professional, documentary, approval, payment, execution, and official status into one generic progress percentage.
