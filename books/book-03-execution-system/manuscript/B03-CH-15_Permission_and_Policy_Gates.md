# B03-CH-15 — Permission and Policy Gates

## Chapter Purpose

This chapter defines how Book 03 coordinates Permission and Policy as independent gates before protected execution.

Permission asks:

```text
May this actor attempt this operation against this target?
```

Policy asks:

```text
Does the current context allow, restrict, redact, downgrade,
hide or require review for this operation and data scope?
```

Both may be required.

Neither replaces the other.

Neither is owned by Workflow, Product, AI, Human Review or the target service.

The central rules are:

```text
Permission Service evaluates Permission.
Policy Service evaluates Policy.
Owning Service enforces the decisions.
Execution coordinates the gates.
Unknown or stale decisions fail closed where required.
```

---

## 1. Dependency Baseline

This chapter extends:

- [Chapter 09 — Execution Object and State Model](B03-CH-09_Execution_Object_and_State_Model.md)
- [Chapter 10 — Workflow Coordination Model](B03-CH-10_Workflow_Coordination_Model.md)
- [Chapter 12 — Review and Approval Lifecycle](B03-CH-12_Review_and_Approval_Lifecycle.md)

It consumes:

- [Permission Context Contract](../../book-02-core-specification/core-specs/contracts/common/permission-context.md)
- [Policy Context Contract](../../book-02-core-specification/core-specs/contracts/common/policy-context.md)
- [Permission API Contract](../../book-02-core-specification/core-specs/contracts/api/permission-api-contract.md)
- [Policy API Contract](../../book-02-core-specification/core-specs/contracts/api/policy-api-contract.md)
- [Human Review Contract](../../book-02-core-specification/core-specs/contracts/common/human-review.md)
- [Reference Contract](../../book-02-core-specification/core-specs/contracts/common/references.md)
- [Audit Context Contract](../../book-02-core-specification/core-specs/contracts/common/audit-context.md)
- [Error Contract](../../book-02-core-specification/core-specs/contracts/common/errors.md)
- [Versioning Contract](../../book-02-core-specification/core-specs/contracts/common/versioning.md)
- [AI Context Contract](../../book-02-core-specification/core-specs/contracts/common/ai-context.md)
- [Implementation Depth Matrix](../../book-02-core-specification/core-specs/implementation/implementation-depth-matrix.md)
- [Developer Start Here](../../book-02-core-specification/core-specs/DEVELOPER_START_HERE.md)

Book 03 consumes decisions and coordinates enforcement. It does not define or evaluate rules.

---

## 2. Gate Boundary

A gate has four responsibilities:

```text
1. identify required evaluation;
2. obtain a valid decision from the owning service;
3. preserve decision scope, freshness and safe trace;
4. ensure the owning service enforces the outcome.
```

Execution must not:

- grant Permission;
- write Policy rules;
- infer a decision;
- treat missing evaluation as allowed;
- expose rule internals;
- ask AI to bypass restriction;
- use Human Review as substitute for Permission;
- use administrator status as universal bypass.

---

## 3. Permission Context

Permission Context identifies:

- intended operation;
- actor type and reference;
- organization;
- agent identity where applicable;
- target object;
- required Permission keys;
- decision reference;
- decision;
- evaluation time;
- expiry;
- safe reason.

Permission Context carries the request and result.

It does not evaluate.

A populated context is not proof of Permission.

### 3.1 Controlled Decisions

Book 02 defines:

- Allowed;
- Denied;
- Conditional;
- NotEvaluated;
- Expired;
- Invalid;
- Unknown.

Protected behavior may continue only when the owning service accepts the decision for the exact operation.

Conditional must be resolved unless the owning contract explicitly allows conditional behavior.

Denied, Expired, Invalid and NotEvaluated stop protected behavior.

Unknown fails closed.

### 3.2 Permission Scope

Permission is scoped by:

- actor;
- organization;
- target;
- operation;
- required keys;
- time;
- decision version;
- cross-organization context.

Permission to read does not imply Permission to update.

Permission to draft does not imply Permission to send.

Permission to create a Task does not imply Permission to complete it.

---

## 4. Policy Context

Policy Context identifies:

- intended operation;
- actor and organization;
- agent identity;
- target;
- required Policy scopes;
- requested data access;
- evaluated data access;
- decision;
- restriction mode;
- omitted fields;
- Human Review requirement;
- evaluation time;
- expiry;
- safe reason.

Policy Context carries the request and result.

It does not implement Policy rules.

### 4.1 Controlled Decisions

Book 02 defines:

- Allowed;
- Denied;
- Restricted;
- Downgraded;
- RequiresHumanReview;
- NotEvaluated;
- Expired;
- Invalid;
- Unknown.

### 4.2 Restriction Modes

Book 02 defines modes including:

- Allow;
- Deny;
- Redact;
- OmitFields;
- DowngradeAccess;
- RequireHumanReview;
- ReturnNotFound;
- ReturnEmpty;
- Escalate;
- Unknown.

Execution must preserve the restriction.

It must not convert Restricted into Allowed because enough information remains to continue.

---

## 5. Required Evaluation Sequence

The baseline sequence is:

```text
Operation request
→ build Permission Context
→ Permission Service evaluates
→ validate Permission decision
→ build Policy Context with allowed reference
→ Policy Service evaluates
→ validate Policy decision
→ Human Review if Policy requires
→ owning service enforces
→ Event/Audit trace
```

Some read or diagnostic paths may have contract-specific ordering.

Book 03 follows the owning contracts.

The sequence does not mean Policy is subordinate to Permission. It means both are independent gates in the operation path.

---

## 6. Decision Freshness

Permission and Policy decisions may expire or become stale.

Freshness may depend on:

- operation risk;
- target state;
- actor role;
- organization membership;
- recipient;
- data scope;
- cross-organization relationship;
- Policy version;
- contract version;
- time;
- Human Review status.

A decision from preview is not guaranteed valid at apply.

A decision for one target is not valid for another.

A decision for internal draft is not valid for external send.

Execution must obtain or validate current decisions at the protected boundary.

---

## 7. Owning-Service Enforcement

Permission Service and Policy Service return decisions.

The target owning service enforces them for its operation.

For example:

- Task Service enforces create, assign or transition gates;
- Communication Service enforces draft, approve, prepare-send or send gates;
- Workflow Contract Service enforces preview/apply gates;
- Event Service enforces Event visibility;
- Document Service enforces Document access and mutation;
- Matter Service enforces Matter changes.

Workflow cannot force an owning service to accept Allowed if the decision does not match the operation.

Product cannot force a service by enabling a button.

---

## 8. Permission and Human Review

Human Review does not grant Permission.

An authorized reviewer may still lack Permission to perform the downstream action.

Examples:

```text
Reviewer may approve content
but may not send Communication.

Reviewer may approve evidence analysis
but may not submit filing.

Reviewer may approve provider recommendation
but may not commit commercial spend.
```

Execution rechecks Permission after review.

---

## 9. Policy and Human Review

Policy may require Human Review.

This means:

```text
Policy decision permits consideration only after accountable review.
```

It does not mean:

- review overrides all other Policy;
- review grants Permission;
- review removes redaction;
- review executes action;
- review authorizes a changed version automatically.

After review, the owning service confirms:

- correct scope;
- correct version;
- correct reviewer;
- current Policy;
- current Permission;
- current target state.

---

## 10. Data Scope, Redaction and Omission

Policy may limit data exposure.

Possible results include:

- full allowed scope;
- reduced scope;
- redacted fields;
- omitted field groups;
- empty response;
- NotFound substitution;
- review required;
- denial.

Execution must preserve:

- requested scope;
- evaluated scope;
- restricted-field omission;
- omitted groups where safe;
- decision reference;
- safe explanation.

AI and Product must use the evaluated scope.

They must not reconstruct hidden fields.

### 10.1 NotFound Substitution

Policy may require ReturnNotFound to avoid revealing object existence.

Execution must not distinguish “exists but restricted” in a way that defeats Policy.

### 10.2 Safe Explanation

A safe explanation may state:

```text
The requested operation is not available under the current access context.
```

It must not reveal internal Policy logic.

---

## 11. Conditional and Downgraded Outcomes

Conditional Permission requires owning-service resolution.

Downgraded Policy may allow a narrower operation.

Examples:

- read summary but not full record;
- draft but not send;
- preview but not apply;
- internal use but not external disclosure;
- propose provider candidates but not select;
- prepare Task plan but not create active Tasks.

Execution should expose the allowed lower-risk path without implying the original operation succeeded.

---

## 12. Cross-Organization Gate

Cross-organization operations require special care.

Context may include:

- user organization;
- target organization;
- customer relationship;
- partner relationship;
- provider relationship;
- Matter access;
- Communication participants;
- shared-document Policy;
- agent capability.

A relationship reference does not itself grant Permission or Policy allowance.

Execution must not use network membership as universal access.

---

## 13. Agent Gate

Agent capability is not Permission.

Agent registry status is not Policy allowance.

AI or agent execution requires:

- Agent identity;
- registry key;
- Agent Contract;
- allowed capability;
- Permission;
- Policy;
- evaluated data scope;
- AI Context;
- Human Review where required;
- downstream service boundary.

A Communication Agent capable of drafting cannot send.

A Workflow Agent capable of preview cannot apply.

A Routing Agent capable of candidate comparison cannot select finally.

---

## 14. Gate Outcomes in Execution State

Permission and Policy remain separate dimensions in the Execution Progress View.

Safe derived conditions may include:

- Permission evaluation required;
- Permission denied;
- Conditional Permission unresolved;
- Policy evaluation required;
- Policy restricted;
- reduced data scope;
- Human Review required by Policy;
- gate decision expired;
- owning-service enforcement pending.

Execution must not reduce them to:

```text
Access = Yes / No
```

when the contract contains restriction and downgrade meaning.

---

## 15. Failure and Recovery

Permission failures may include:

- invalid key;
- decision expired;
- reference invalid;
- actor mismatch;
- organization mismatch;
- target denied.

Policy failures may include:

- scope invalid;
- decision expired;
- context mismatch;
- restricted field violation;
- cross-organization restriction;
- Human Review required.

Recovery depends on the safe next step:

- request Permission;
- request Policy review;
- request Human Review;
- reduce data scope;
- change operation;
- validate reference;
- use owning service;
- no action available.

Retry without changed authority or context is not useful.

---

## 16. Audit and Event Trace

Audit should preserve:

- intended operation;
- actor;
- organization;
- agent;
- target;
- required keys/scopes;
- decision references;
- safe decision outcome;
- restriction mode;
- omitted fields;
- Human Review;
- time and expiry;
- owning-service enforcement result;
- Event references.

PermissionEvaluated may be emitted by Permission Service.

PolicyEvaluated may be emitted by Policy Service.

API, Workflow and AI do not emit those Events directly.

Event payload must not expose rule internals.

---

## 17. Worked Example: External Evidence Sharing

A user wants to share an Evidence Package with a foreign provider.

### 17.1 Permission

Permission Service evaluates:

- actor;
- organization;
- Evidence reference;
- intended operation: external share;
- required Permission keys.

Permission returns Allowed.

### 17.2 Policy

Policy Service evaluates:

- provider relationship;
- jurisdiction;
- data category;
- requested full Evidence scope;
- external disclosure Policy.

Policy returns Restricted with:

- OmitFields;
- Human Review required;
- reduced evaluated data scope.

### 17.3 Review

An authorized human reviews the redacted package and intended recipient.

Review approves the redacted version only.

### 17.4 Owning-Service Enforcement

Document/Evidence and Communication Services enforce:

- redacted version;
- provider recipient;
- current decisions;
- review;
- send boundary.

The full package is not exposed.

Permission Allowed did not bypass Policy.

Review did not restore omitted fields.

---

## 18. Gate Invariants

1. Permission and Policy are independent.
2. Permission Service evaluates Permission.
3. Policy Service evaluates Policy.
4. Context does not grant a decision.
5. Allowed must have a valid reference.
6. Decisions are operation- and target-specific.
7. Expired decisions fail closed.
8. Unknown fails closed where required.
9. Conditional must be resolved.
10. Restricted and Downgraded must be enforced.
11. Policy may require Human Review.
12. Human Review does not grant Permission.
13. Human Review does not bypass Policy.
14. Owning service enforces.
15. Product does not infer access.
16. Agent capability does not equal Permission.
17. Agent registry does not equal Policy.
18. AI uses evaluated data scope.
19. Hidden fields are not reconstructed.
20. Event trace does not expose rule internals.

---

## 19. Gate Anti-Patterns

- Permission Allowed becomes Policy Allowed.
- Policy Allowed becomes Permission Allowed.
- Administrator bypasses all gates.
- Missing evaluation defaults to Allowed.
- Expired decision is reused.
- Review overrides denial.
- AI reconstructs omitted fields.
- Product button determines authority.
- Agent capability bypasses Permission.
- Cross-organization relationship grants all access.
- Conditional is treated as Allowed.
- Restricted is shown as success.
- Policy internals are exposed in error.
- Workflow emits evaluation Events.

---

## 20. MVP Depth

The MVP should support:

- Permission Context;
- Policy Context;
- decision references;
- controlled decisions;
- freshness;
- target and operation scope;
- restriction modes;
- redaction/omission;
- Human Review requirement;
- agent context;
- safe errors;
- owning-service enforcement;
- audit and Event references.

Book 02 sets:

- general Permission hooks at Level 2;
- real Permission enforcement for protected MVP actions at Level 3;
- Policy schema at Level 1;
- contextual Policy hooks at Level 2.

The MVP does not require:

- full Policy authoring;
- advanced rule editor;
- universal authorization engine;
- Product access-control UI;
- AI policy decision;
- cross-organization federation platform.

---

## 21. Non-Goals of This Chapter

This chapter does not define:

- Permission keys;
- Policy scopes;
- Permission rules;
- Policy rules;
- role assignment;
- authentication;
- authorization engine implementation;
- Product UI;
- compliance certification;
- AI gate authority;
- bypass rules;
- new Events.

It defines how Execution coordinates existing decisions.

---

## 22. Chapter Conclusion

Protected execution requires two independent questions:

```text
May the actor attempt it?
Does context allow it, restrict it or require review?
```

Permission answers the first.

Policy answers the second.

Human Review may satisfy a Policy-required accountability gate.

Owning Service enforces.

Execution coordinates.

AI and Product consume only the allowed scope.

The next chapter defines the final Part II boundary: how AI and agents hand prepared work, context and recommendations to authorized humans and governed services without becoming execution authority.
