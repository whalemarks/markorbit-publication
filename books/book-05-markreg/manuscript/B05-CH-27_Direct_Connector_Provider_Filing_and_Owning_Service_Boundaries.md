# B05-CH-27 — Direct Connector, Provider Filing and Owning Service Boundaries

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH26 produced an accepted provider Instruction or approved direct route.

CH27 defines how approved work enters governed Execution without moving authority into MarkReg:

```text
EL-20 / CH27
approved package
+ active Filing Approval
+ accepted route or provider
+ credentials, payment and idempotency conditions
→ MR-A17 Execution Request
→ Book 03 governed Execution
```

MarkReg owns the focused Product journey. It does not become the Workflow engine, connector, provider, credential owner, filing transaction owner or official office.

## 1. Product Question and Primary Action

**Product question:** Through which approved route may the protected filing action occur, and who controls that action?

**Primary action:** Request or authorize the permitted Execution step only after route-specific gates pass.

The interface must identify the actor and external effect before exposing an action.

## 2. Execution Routes

| Route | Protected-action actor |
| --- | --- |
| direct connector | authorized connector or filing-capable service using controlled credentials |
| provider filing | appointed and accepting provider |
| internal professional | eligible professional using organization credentials |
| Owning Service | filing-capable service owning the formal transaction |
| assisted manual filing | eligible Human using an official portal under governed Task and evidence return |
| unavailable | no route currently satisfies the requirements |

A route label must not conceal who performs the action.

## 3. Responsibility Boundaries

### MarkReg

MarkReg prepares and displays the package, carries stable references and approvals, requests Execution, shows returned evidence and maintains a sourced Product projection.

It does not automatically own credentials, official accounts, formal Documents, funds, provider engagement or official records.

### Book 03 Execution

Book 03 governs Tasks, Workflows, protected-action gates, credentials, connector invocation, retries, compensation, Communications, Events and return evidence.

Book 05 supplies the MarkReg Product contract; it does not create a second Execution engine.

### Provider

An appointed provider may prepare office-specific forms, file under accepted professional authority, pay official fees under agreed terms, receive correspondence and return evidence.

### Owning Service

A filing-capable Owning Service may own the formal transaction, connector attempt, payment record, identifier, acknowledgement evidence, retry and reconciliation state.

### Official Office

The office controls official receipt, filing date, application number, fee acceptance, formal requirements and later official status.

## 4. Execution Request Contract

`MR-A17 Execution Request` identifies:

- exact package and Filing Approval versions;
- jurisdiction, route and protected action;
- actor or service authorized to execute;
- provider acceptance where applicable;
- credential owner and permitted scope;
- fee and payment authority;
- required Documents and originals;
- active Pack and connector version;
- deadline and office-availability context;
- stable idempotency key;
- prior attempt and duplicate-risk check;
- expected return evidence and reconciliation owner.

The request does not itself prove that Execution began or succeeded.

## 5. Connector and Credential Boundary

A connector may authenticate, validate a payload, transmit data and files, initiate authorized payment and receive technical or official responses.

A connector may not decide applicant ownership, grant Professional Review or Filing Approval, or convert transport success into official success.

Credentials retain owner, purpose, environment, scope, permitted user or service, authentication time, expiry and action evidence. Credentials must not be copied into the Filing Package or exposed to clients or providers.

## 6. Payload Transformation

The approved package may be transformed into connector JSON/XML, portal fields, local-language forms, provider worksheets, file bundles or payment instructions.

Transformation preserves source lineage and provides a reviewable diff where meaning may change.

```text
Technical mapping ≠ authority to alter legal scope
```

## 7. Pre-Execution Validation

Immediately before protected action, verify:

1. exact approved package;
2. active Filing Approval and conditions;
3. permitted route and actor;
4. credential availability;
5. Provider Acceptance where applicable;
6. payment and official-fee authority;
7. required Documents and originals;
8. Pack, connector and form versions;
9. deadline and office availability;
10. idempotency identity and prior attempts.

An earlier green Readiness result is insufficient if material inputs changed.

## 8. Manual Filing Remains Governed

A Human using an official portal remains inside governed Execution. The Task retains the package, actor, credential boundary, entered values or permitted screenshots, fees, action time, returned receipt or error and unresolved reconciliation.

Manual does not mean unaudited.

## 9. Route Change

A failed connector or unavailable provider does not authorize another route automatically.

Before substitution, determine:

- whether Filing Approval covered the alternative;
- whether routing, Selection, appointment and acceptance are complete;
- whether fees or Documents changed;
- whether transformation altered meaning;
- whether deadline and duplicate risk permit the switch;
- which new Decisions are required.

## 10. `EMBERLOOP` — `EL-20`

The US word-mark package enters the accepted private-provider route. The EU package enters a supported governed-service connector route. The UK package enters an eligible professional’s manual official-portal route.

The three routes retain separate Filing Approvals, credentials, fee records, attempts, evidence and official identifiers.

## 11. Controlled Scenarios

### `MR-SCN-20` — Provider proposes a material change

A meaning-changing provider or route transformation returns to professional and approval gates before Execution.

### `MR-SCN-23` — Technical success without official receipt

A connector transport success with no official acknowledgement is displayed as sent or acknowledgement unknown. It opens reconciliation and blocks an unsafe retry.

## 12. AI Assistance

AI may map package fields, compare payloads, identify missing route prerequisites, explain technical errors and summarize returned evidence.

AI may not access uncontrolled credentials, choose an unauthorized route, approve a meaning-changing transformation, commit funds or perform a protected action without governed authority.

## 13. Chapter Lock

```text
MarkReg owns the Product journey.
Book 03 governs Execution.
Connectors transmit under controlled credentials.
Providers act under accepted engagement.
Owning Services own formal transaction facts.
Official offices control official outcomes.
Technical success ≠ official receipt.
Route failure ≠ authority to switch routes.
```

## 14. Handoff to CH28

CH27 produces `MR-A17 Execution Request` and route-specific Execution attempts.

CH28 classifies `MR-E01 Submission Evidence`, `MR-E02 Delivery Evidence`, `MR-E03 Provider Report` and `MR-E04 Official Acknowledgement Evidence` without collapsing their authority.
