# CH07 — Workflow, Work Package and Step Must Remain Distinct

## 1. Coordination fails when every unit is called a task

Professional systems often use one generic word—task—for several very different things:

- a business objective;
- a lifecycle process;
- a bounded deliverable;
- a technical action;
- a human assignment;
- a review request;
- an external instruction.

This creates unclear responsibility, weak evidence and unsafe automation.

Book 03 therefore separates:

```text
Workflow
≠ Work Package
≠ Step
≠ Assignment
≠ Contribution
≠ Protected Action
```

## 2. Workflow coordinates a governed goal

A Workflow is the coordinated path toward a defined business or professional goal.

Examples include:

- preparing and filing a trademark application;
- responding to an Office Action;
- completing a renewal;
- validating a transaction;
- producing and approving a marketing pack;
- resolving an Unknown external submission state.

A Workflow should identify:

- the originating objective;
- relevant Workplace and Product context;
- affected formal objects;
- stages and dependencies;
- decision points;
- required Work Packages;
- review and approval gates;
- external actions;
- evidence requirements;
- completion and cancellation rules;
- recovery routes.

A Workflow is not merely a sequence diagram. It is a governed coordination model.

## 3. Work Package defines a bounded Outcome

A Work Package is a unit of production, review or professional contribution that can be assigned, accepted, reviewed and compensated independently.

It should specify:

- the exact Outcome;
- scope and exclusions;
- source objects and versions;
- required Capability;
- risk level;
- allowed implementation classes;
- data scope;
- deadline;
- review requirement;
- acceptance criteria;
- compensation basis where relevant;
- revision and escalation rules.

A useful Work Package is written around an Outcome, not vague activity.

Poor definition:

> Handle the US application.

Better definition:

> Verify the applicant identity and produce an evidence-backed applicant record candidate for professional review. This package excludes customer communication, final applicant approval and filing submission.

## 4. Step is an executable stage

A Step is a smaller stage or action within a Workflow or Work Package.

Examples include:

- validate a required field;
- extract an applicant name;
- compare two document versions;
- request missing evidence;
- render a Preview;
- call a connector;
- record a Return;
- run a deterministic check.

A Step may be automated or human-assisted. It usually does not carry the full commercial or professional meaning of a Work Package.

```text
Step Completed
≠ Work Package Accepted
≠ Workflow Goal Achieved
```

## 5. Assignment binds a performer to a Work Package

An Assignment is not the Work Package itself.

The Work Package exists as a defined need. The Assignment records that a specific Person, system, team or Provider has accepted responsibility for all or part of it.

```text
Work Package Defined
→ Eligibility
→ Selection
→ Assignment Offered
→ Assignment Accepted
```

Several Assignments may contribute to one Work Package when:

- work is parallelized;
- separate professional perspectives are required;
- a primary performer and Reviewer are distinct;
- fallback or escalation is activated.

## 6. Contribution records returned work

A Contribution is what an assigned performer submits.

It should preserve:

- the Assignment;
- performer;
- Capability and authority context;
- source versions;
- tools or models used;
- output;
- evidence;
- uncertainty;
- completion statement;
- limitations;
- submission time.

```text
Contribution Submitted
≠ Contribution Accepted
≠ Work Package Complete
```

## 7. Workflow and formal-state objects remain separate

A Workflow may coordinate work around an Order, Matter, Customer or Trademark, but it does not become those objects.

```text
Workflow State
≠ Order State
≠ Matter State
≠ Official State
```

For example, a filing Workflow may be completed from Execution’s perspective after validated evidence has been returned to the Owning Service. The Matter may still remain pending official examination.

## 8. A Workflow can span Products without becoming a Product

A customer journey may begin in Lite, formalize in MarkReg, display progress through Sites and use MGSN for local professional fulfilment.

Execution can coordinate the cross-product path, but it does not collapse the Products.

```text
Cross-product Workflow
≠ Single Product Ownership
```

Each Product retains its experience and domain boundary. Each Owning Service retains formal-state authority.

## 9. A Workflow may invoke multiple Capabilities

A single Workflow often requires different Capabilities.

Example:

```text
Application Workflow
→ Applicant Verification Capability
→ Goods Classification Capability
→ Search Interpretation Capability
→ Filing Package Preparation Capability
→ Professional Review Capability
→ Provider Routing Capability
→ Submission Evidence Validation Capability
```

Each Capability Request should remain identifiable. This allows:

- separate eligibility;
- separate implementation binding;
- separate review;
- separate evidence;
- separate failure recovery.

## 10. A Capability Request may exist without a full Workflow

Not every request needs lifecycle orchestration.

Examples include:

- one-time data normalization;
- isolated document comparison;
- internal translation review;
- a bounded visual-quality check;
- a simulation assessment.

```text
Capability Request
≠ Workflow Required in Every Case
```

The system should not create unnecessary process overhead for simple, reversible work.

## 11. Workflow stages are not automatically Work Packages

A stage such as “Preparation” may contain several independently assignable Outcomes.

Likewise, a Work Package may span several technical Steps.

```text
Workflow Stage
≠ Work Package

Work Package
≠ Single Step
```

These distinctions support accurate capacity, compensation and failure analysis.

## 12. Dependencies must be typed

Work may depend on:

- required input;
- customer decision;
- professional review;
- commercial approval;
- external Provider acceptance;
- document arrival;
- official event;
- payment checkpoint;
- completion of another Work Package.

A generic “blocked” state does not explain what is needed.

Recommended dependency states include:

```text
Awaiting Input
Awaiting Customer Decision
Awaiting Review
Awaiting Approval
Awaiting Provider Acceptance
Awaiting External Evidence
Awaiting Funds Checkpoint
Awaiting Reconciliation
```

## 13. Parallel work must preserve synthesis responsibility

Some Work Packages require multiple perspectives, such as:

- visual design;
- trademark continuity;
- commercial fit;
- jurisdiction-specific legal review.

Parallel Contributions should not be averaged into an anonymous vote.

Execution should identify:

- each perspective;
- each finding;
- conflicts;
- required synthesis;
- the Delivery Owner or qualified final authority.

```text
Multiple Contributions
≠ Collective Approval
```

## 14. Review is a separate path

Review may occur at Step, Contribution, Work Package, package or Workflow level.

The system should record exactly what was reviewed.

```text
One Step Reviewed
≠ Entire Work Package Reviewed

Work Package Reviewed
≠ Workflow Approved for Apply
```

Material changes after Review may require re-review.

## 15. Workflow templates and Workflow instances differ

A Workflow Template defines a reusable pattern. A Workflow Instance applies that pattern to a specific context.

```text
Template
≠ Active Workflow
```

A template may define:

- expected stages;
- standard Work Packages;
- default review gates;
- common evidence requirements;
- known failure routes.

The instance binds:

- actual objects;
- participants;
- jurisdiction;
- versions;
- deadlines;
- current decisions;
- deviations.

## 16. Template changes do not rewrite active history

When a template improves, active or completed instances should not be silently rewritten.

The system should preserve:

- template version at creation;
- approved migrations;
- instance-specific deviations;
- historical evidence.

```text
New Template Version
≠ Prior Workflow History Replaced
```

## 17. Dynamic Workflows still require controlled change

Professional work cannot always be fully predicted. New issues may arise from:

- official notices;
- Provider requirements;
- customer changes;
- evidence defects;
- deadline changes;
- source conflicts.

Execution may add or amend Work Packages, but material change should identify:

- reason;
- source event;
- scope impact;
- cost impact;
- deadline impact;
- required approval;
- invalidated review or assignment.

```text
Workflow Adaptation
≠ Silent Scope Expansion
```

## 18. Completion must be defined at each level

### Step completion

The stage ran and produced its expected technical result.

### Contribution submission

A performer returned work.

### Work Package acceptance

The bounded Outcome met acceptance criteria.

### Workflow completion

The coordinated execution goal was reached according to the Workflow contract.

### Formal-state completion

The applicable Owning Service or official source validated the business or legal state.

```text
Step Complete
≠ Work Package Accepted
≠ Workflow Complete
≠ Formal State Complete
```

## 19. Cancellation must respect level and external effect

Cancelling a Workflow may require:

- stopping unstarted Work Packages;
- revoking Assignments;
- compensating completed work;
- preserving Contributions;
- recalling Provider instructions where possible;
- checking whether external action already occurred;
- notifying Relationship Owners;
- reconciling funds and evidence.

Deleting the Workflow object is never a safe cancellation model.

## 20. Workflow visibility should be role-specific

A customer may need a simple lifecycle view. A Contributor should see only the assigned Work Package. A Reviewer needs the relevant evidence and review scope. A Delivery Owner needs dependency and recovery visibility.

```text
One Workflow
≠ Everyone Sees Everything
```

The underlying distinctions remain even when Products present simplified views.

## 21. Metrics should respect the hierarchy

Useful metrics include:

- Step failure rate;
- Work Package revision rate;
- Assignment acceptance time;
- Review turnaround;
- Workflow cycle time;
- external reconciliation time;
- formal Outcome success.

A single “task completion rate” hides where quality or delay actually occurs.

## 22. Chapter locks

```text
Workflow
≠ Work Package
≠ Step

Work Package
≠ Assignment

Assignment
≠ Contribution

Contribution Submitted
≠ Outcome Accepted

Workflow State
≠ Formal State

Parallel Contribution
≠ Collective Approval

Template Change
≠ Active History Rewrite

Workflow Adaptation
≠ Silent Scope Expansion

Step Complete
≠ Workflow Complete
```
