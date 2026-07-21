# Chapter 04 — Capability Is Not a Feature

A software product is usually described by its features. It has search, filing, reminders, dashboards, document upload, messaging, image generation or analytics. This language is useful when comparing screens and functions, but it is too shallow for a professional operating system.

A feature tells us what an interface can do. A Capability tells us what reliable outcome the system can help a user produce.

That distinction appears subtle until the work becomes consequential.

A button labelled “Generate filing strategy” may produce a polished answer. Yet the system still has to know which jurisdiction is relevant, whether the customer has used the mark, whether the applicant owns prior registrations, whether a local attorney is required, whether the advice relies on current rules, what assumptions remain unverified, and who is accountable for the recommendation. The feature is visible. The real capability is hidden behind it.

MarkOrbit must be designed around the hidden part.

## 1. The feature trap

Feature-led products often succeed at demonstration and fail in sustained professional use.

A demonstration rewards speed, novelty and apparent intelligence. Professional work rewards reliability, traceability, appropriate judgment, controlled authority and usable delivery.

Consider five familiar product features:

```text
AI search
AI classification
AI filing recommendation
AI evidence review
AI content generation
```

Each may appear to be a complete function. None is a complete professional Capability without additional contracts.

An AI search feature needs a definition of the search objective, source coverage, update date, matching methods, treatment of non-identical marks, goods relationships, transliteration, confidence and review responsibility.

An AI classification feature needs jurisdiction, edition, office practice, acceptable wording, item-count rules, dependency between classes and a way to preserve the customer's actual commercial scope.

An AI filing recommendation needs business objectives, current and planned markets, budget, risk tolerance, applicant structure, use status, urgency and a distinction between mandatory and optional recommendations.

An AI evidence review feature needs the legal maintenance event, goods scope, evidence date, authenticity, source, image manipulation risk and professional disposition.

An AI content feature needs to distinguish verified trademark facts from invented brand concepts, promotional claims from legal status, and visual inspiration from evidence of use.

When these conditions are ignored, a product may have many features and very little dependable capability.

## 2. Capability begins with an outcome contract

A MarkOrbit Capability should be defined by the result it promises to help produce.

The result must be understandable before the implementation is chosen.

For example:

```text
Capability: Assess United States post-registration maintenance readiness

Outcome:
A sourced, reviewable assessment of filing window, required declaration,
current owner, registered goods, evidence readiness, unresolved risks,
recommended next action and professional-review requirement.
```

The implementation may combine:

- official trademark data;
- jurisdiction knowledge;
- date calculation;
- document extraction;
- evidence classification;
- a language model;
- deterministic checks;
- a trained user;
- an expert reviewer;
- an authorized United States attorney.

Those components may change. The outcome contract should remain stable enough for the Product, user, reviewer and customer to understand what is being requested and what counts as success.

A Capability Definition therefore needs more than a title. It needs:

```text
identity and version
purpose and user outcome
accepted inputs
required facts and assumptions
source and knowledge dependencies
implementation modes
risk and qualification restrictions
human and AI responsibilities
review policy
output artifacts
acceptance criteria
failure and escalation conditions
evidence requirements
compatibility expectations
```

This is why Capability belongs above individual prompts, tools and workflows.

## 3. Capability is not Skill

The word skill is often used broadly. In MarkOrbit it should have a narrower meaning.

A Skill is one implementation method used by a person, AI agent or system to perform part of a Capability.

A trademark-status parser may be a Skill. A prompt that drafts a customer explanation may be a Skill. A script that validates a filing window may be a Skill. A human review checklist may be represented as a procedural Skill.

The Capability is the stable outcome that these Skills support.

```text
Capability
= what reliable professional result is required

Skill
= one method for producing part of that result
```

This distinction protects MarkOrbit from dependence on a particular model or implementation fashion.

If a better model replaces the current model, the Capability remains. If deterministic software becomes safer than AI for a calculation, the binding changes. If a jurisdiction requires a locally qualified professional, the implementation route changes again. The Product should continue asking for the same governed outcome.

## 4. Capability is not Tool

A Tool executes an operation.

A browser retrieves a page. A crawler captures content. A database runs a query. An image model generates a visual. A PDF parser extracts text. An email connector sends a message.

Tools have operational permissions and technical failure modes. They do not by themselves define professional meaning.

A crawler can collect an office notice, but it does not decide whether the notice remains current. A database can retrieve a registration date, but it does not decide which maintenance rule applies. An image model can create packaging, but it does not decide whether the result is legally safe or whether it misrepresents real commercial use.

The Capability layer determines why the Tool is invoked, what inputs are permitted, what output is expected, which validation follows and whether the result may affect formal state.

## 5. Capability is not Workflow

A Workflow coordinates a sequence of actions toward a goal.

One Workflow may invoke several Capabilities. One Capability may also appear in many Workflows.

For example, `VerifyTrademarkOwnership` may be used in:

- filing intake;
- maintenance preparation;
- assignment due diligence;
- marketplace listing;
- certificate delivery;
- dispute review.

The Capability should not be duplicated for each workflow. The workflows provide context, timing and sequence; the Capability provides the stable outcome contract.

The inverse also matters. A workflow named “File a trademark” does not prove that all required capabilities exist. It may simply connect forms and emails while leaving essential judgment informal.

## 6. Capability is not Product

A Product packages capabilities for a user segment and commercial promise.

Lite, MarkReg and MGSN expose different combinations of capability.

Lite may use matching, content creation, opportunity discovery and customer follow-up capabilities. MarkReg may use intake, search, filing preparation, evidence review and delivery capabilities. MGSN may use provider eligibility, route recommendation, instruction validation and Return verification capabilities.

The same underlying capability can appear through different interfaces and commercial models.

This prevents Product teams from rebuilding professional logic independently and creating contradictory results.

## 7. The same capability can have different execution modes

A Capability is stable, but its implementation can vary with risk, user proficiency, jurisdiction and authority.

MarkOrbit uses a human–AI collaboration spectrum:

```text
M0 — human only
M1 — AI reference
M2 — AI assist
M3 — AI draft, human approve
M4 — AI execute under governance
M5 — hybrid professional network
```

A low-risk formatting capability may operate at M4. A standard customer email may use M3. A difficult legal assessment may remain M1 or M2. A filing requiring a local attorney may use M5.

The Product should not advertise one fixed level of “AI automation” for every case. The mode is a governed decision.

## 8. Capability separates access from competence

One of the strongest ideas behind MarkOrbit is that users may gain immediate access to professional capability before they personally possess the full competence.

A small agency may not have a United States maintenance specialist. Through MarkOrbit it can still access:

- official data;
- current knowledge;
- a guided assessment workflow;
- AI assistance;
- evidence checklists;
- a certified reviewer;
- an authorized lawyer for protected action.

The user gains operating leverage without pretending that every participant has the same expertise or legal authority.

Over time, repeated use may help the user develop personal competence. The system should record the difference between assisted access and demonstrated ability.

## 9. Capability creates a common language for supply and demand

Without a capability language, customers ask for broad outcomes and providers describe themselves with broad titles.

```text
Customer request: “Help me protect my brand internationally.”
Provider claim: “We are a global full-service IP firm.”
```

Neither statement is precise enough for reliable matching.

A capability-centered system can decompose the demand:

- determine priority countries;
- evaluate filing basis;
- identify classes and goods;
- search conflicting marks;
- prepare applicant information;
- obtain and validate documents;
- appoint qualified local counsel;
- monitor deadlines;
- review office actions;
- manage registration and maintenance.

It can then ask which Workplaces, people, systems and providers are eligible for each part.

This is the foundation for a professional network that routes work by evidence rather than marketing language alone.

## 10. Capability creates a better investment unit

Features are easy to add and easy to copy. A dependable Capability is harder to build.

It requires:

- trusted data;
- maintained knowledge;
- a stable contract;
- tests and fixtures;
- user guidance;
- execution policy;
- professional review;
- evidence from real outcomes;
- continuous correction.

A portfolio of reusable capabilities compounds across Products.

Investment in `VerifyTrademarkStatus` benefits Lite opportunity discovery, MarkReg delivery, MGSN instructions, customer reporting and training simulations. Investment in a product-specific page may benefit only one interface.

This does not mean every capability deserves equal investment. The platform must choose capabilities with high reuse, meaningful demand and a clear path to reliable outcomes.

## 11. Capability can still become bureaucracy

A capability-centered architecture has its own danger: excessive abstraction.

A team may spend months defining taxonomies and contracts without producing a useful result. It may divide simple work into hundreds of artificial units. It may create versioning and governance requirements for concepts that should remain ordinary Product behavior.

MarkOrbit should resist that outcome.

A Capability deserves first-class treatment when:

- users can understand and value the outcome;
- the outcome recurs;
- more than one Product or workflow may reuse it;
- implementation may vary;
- risk or authority requires governance;
- evidence can improve the result over time.

Otherwise the behavior may remain a local feature, workflow step or implementation detail.

## 12. The practical test

Before calling something a Capability, MarkOrbit should ask:

```text
What outcome is promised?
Who needs it?
What facts are required?
What can go wrong?
Who may perform it?
What review is required?
What evidence proves completion?
Can another Product reuse it?
Can the implementation change without changing the promise?
```

If those questions cannot be answered, the platform probably has a feature idea rather than a Capability.

The long-term strategic choice is therefore clear:

> MarkOrbit should compete by making difficult professional outcomes accessible, reliable and governable—not by accumulating the largest menu of visible features.
