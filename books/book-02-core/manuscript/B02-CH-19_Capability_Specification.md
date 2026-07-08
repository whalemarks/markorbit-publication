# Book 02

# 19 — Capability Specification

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-19

**Chapter Title:** Capability Specification

**Part:** Part III — Core Specification System

**Chapter Type:** Specification

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

**Related Planning Documents:**

- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-PLN-0004 — Core Execution Matrix v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template

---

# 1. Chapter Purpose

This chapter defines the Capability Specification of the MarkOrbit Core.

Chapter 18 defined Identity.

Identity answers:

> Who or what is acting, represented, responsible or connected?

Capability answers:

> What can this actor, system, service, AI agent, human professional, partner, agent or service provider do?

Capability is one of the most important concepts in MarkOrbit because the platform is not only a data system.

It is a professional operating system.

It must know:

- what the Core can do;
- what a Core Service can do;
- what an AI agent can do;
- what a human professional can do;
- what a foreign agent can do;
- what a service provider can do;
- what a product may consume;
- what a workflow may invoke;
- what requires permission;
- what requires review;
- what is risky;
- what is verified;
- what is only claimed;
- what is suitable for routing or recommendation.

Without Capability Specification, MarkOrbit would treat all services, agents, AI tools and professional actors as flat resources.

That would make routing unreliable, AI unsafe, product consumption inconsistent and Codex implementation shallow.

This chapter defines Capability as a governed Core concept.

---

# 2. Core Question

This chapter answers one question:

> How shall MarkOrbit represent, govern, verify, consume and execute capabilities across Core Services, AI agents, human professionals, agents, service providers, products and workflows?

The answer is:

> MarkOrbit shall define Capability as a governed, scoped, provider-linked and contract-consumable ability that can be executed by Core Services, AI agents, human professionals, agents, service providers or workflows under defined identity, knowledge, permission, policy, risk, review and audit rules.

Capability is not only a function.

Capability is not only a skill label.

Capability is not only a service item.

Capability is not only an AI tool.

Capability is a governed ability in the Core.

---

# 3. Scope

## 3.1 In Scope

This chapter defines:

- Capability Specification purpose;
- Capability Model application;
- capability ontology;
- capability object types;
- Core Capability;
- Core Service Capability;
- AI Capability;
- Human Professional Capability;
- Agent Capability;
- Service Provider Capability;
- Product Consumption Capability;
- Workflow / Execution Capability;
- capability provider;
- capability consumer;
- capability scope;
- capability condition;
- capability risk;
- capability permission;
- capability review;
- capability quality;
- capability verification;
- capability lifecycle;
- capability matching;
- capability events;
- capability services;
- capability contracts;
- AI usage;
- product consumption;
- MVP boundary;
- `core-specs/` requirements;
- Codex implementation rules.

## 3.2 Out of Scope

This chapter does not define:

- product feature lists;
- product pricing packages;
- service provider commercial plans;
- full marketplace service catalog;
- complete AI prompt library;
- vendor-specific tool implementation;
- full HR skill management;
- training curriculum;
- detailed workflow operations;
- complete API endpoints;
- database schema;
- implementation code.

Those belong to product documents, Book 06, implementation specifications or later `core-specs/`.

---

# 4. Capability Definition

In the MarkOrbit Core, Capability means:

> a governed ability that may be provided by a system, service, AI agent, human professional, organization, agent, service provider or workflow, and may be consumed under defined scope, conditions, permission, policy, risk, review and contract rules.

This definition includes:

- what can be done;
- who or what can do it;
- under what scope;
- under what conditions;
- for which objects;
- using which knowledge;
- with which permission;
- at what risk level;
- with what review requirement;
- with what output;
- with what audit trail;
- by which consumer.

Capability connects Identity, Knowledge, Business Responsibility, Services, AI, Workflow and Network.

---

# 5. Capability Specification Position

Capability Specification belongs to Part III because it converts the Capability Model into concrete Core specification rules.

It is connected to Part II as follows:

```text
Canonical Models
    Capability Model

Core Domains
    Knowledge
    Permission
    Policy
    Classification
    Document
    Evidence
    Matter
    Opportunity
    Agent
    Service Provider
    Routing
    Communication

Core Objects
    Capability
    Capability Provider
    Capability Consumer
    Capability Scope
    Capability Condition
    Capability Verification
    Capability Result

Core Services
    Capability Registry
    Capability Matching
    Capability Evaluation
    Capability Verification
    Capability Invocation
    Capability Audit

Execution Primitives
    CapabilityRegistered
    CapabilityVerified
    CapabilityInvoked
    CapabilitySuspended
    CapabilityMatched

Core Contracts
    Capability Data Contract
    Capability API Contract
    Agent Contract
    Service Contract
    Consumption Contract
```

Capability is a cross-domain specification.

It is not a single product module.

---

# 6. Capability Principles

The Capability Specification is governed by the following principles.

## Principle 1 — Capability Before Function

A product function is not automatically a Core Capability.

A Core Capability must represent reusable, governed ability.

## Principle 2 — Capability Requires Provider

Every capability must have a provider.

The provider may be Core, service, AI agent, user, agent, service provider, workflow or external system.

## Principle 3 — Capability Requires Scope

A capability without scope is unsafe.

Scope may include jurisdiction, service type, object type, domain, product, risk level or consumer.

## Principle 4 — Capability Requires Governance

Capability execution must respect identity, permission, policy, risk, review and audit.

## Principle 5 — Capability Requires Knowledge Where Professional Meaning Exists

Professional capabilities must be grounded in authorized knowledge.

## Principle 6 — AI Capability Is Not AI Autonomy

AI may provide capability under Agent Contract.

AI does not own professional responsibility.

## Principle 7 — Capability May Be Claimed, Verified or Trusted

Not all capability records are equal.

The Core must distinguish claimed, imported, inferred, tested, reviewed and verified capability.

## Principle 8 — Capability Must Be Consumable Through Contracts

Products, Workplaces and AI agents must consume capabilities through explicit contracts.

---

# 7. Capability Ontology

Capability belongs primarily to System Ontology.

It also touches Execution Ontology and Collaboration Ontology.

## 7.1 System Ontology

Capability is a system concept because it defines what the Core and its actors can do.

## 7.2 Execution Ontology

Capability becomes executable through Core Services, Tasks, Events, Workflow Contracts and Agent Contracts.

## 7.3 Collaboration Ontology

Capability is used to evaluate and route work to agents, service providers and partners.

## 7.4 Reality Ontology

Human professionals, agents and service providers may have real-world capabilities that MarkOrbit represents.

The Capability Specification therefore connects system representation with professional reality.

---

# 8. Capability Domain Relationships

Capability relates to many Core Domains.

| Domain | Capability Relationship |
|--------|-------------------------|
| Identity | capability provider and consumer identity |
| Permission | capability access and invocation authorization |
| Policy | capability rules, restrictions and review requirements |
| Knowledge | capability grounding and knowledge dependency |
| Classification | classification recommendation capability |
| Document | document parsing and generation capability |
| Evidence | evidence packaging and review assistance capability |
| Matter | matter execution and responsibility capability |
| Opportunity | opportunity discovery and scoring capability |
| Agent | agent professional service capability |
| Service Provider | external service capability |
| Routing | capability matching and routing decision |
| Communication | communication summarization, drafting and linking capability |
| Task | capability may create or complete tasks |
| Event | capability execution produces events |
| Workflow Contract | capability may be invoked under workflow rules |

Capability should not be redefined independently by each domain.

Domains consume the Capability Specification.

---

# 9. Capability Object Types

The Capability Specification recognizes the following object types.

```text
Capability
Capability Provider
Capability Consumer
Capability Scope
Capability Condition
Capability Requirement
Capability Permission
Capability Risk Level
Capability Verification
Capability Quality
Capability Result
Capability Invocation
Capability Audit Record
Capability Contract
```

Not all objects need separate database tables.

But their meanings must be preserved in detailed specs.

---

# 10. Capability Object

## 10.1 Definition

Capability Object is:

> the Core representation of a governed ability that may be provided, consumed, invoked, verified, matched, restricted, audited or suspended.

## 10.2 Purpose

Capability Object provides:

- stable capability reference;
- domain ownership;
- provider linkage;
- consumer rules;
- scope;
- permission;
- risk;
- review requirement;
- output definition;
- quality and verification;
- execution trace.

## 10.3 Minimum Attributes

A minimal Capability Object should include:

```text
capability_id
capability_name
capability_type
owning_domain
provider_type
provider_id
scope
status
verification_status
risk_level
requires_permission
requires_review
created_at
updated_at
```

This is a semantic baseline, not a final schema.

Detailed fields belong in:

```text
core-specs/objects/capability.md
```

---

# 11. Capability Categories

Book 02 recognizes eight practical capability categories.

```text
1. Core Capability
2. Core Service Capability
3. AI Capability
4. Human Professional Capability
5. Agent Capability
6. Service Provider Capability
7. Workflow / Execution Capability
8. Product Consumption Capability
```

These categories help define provider, governance and consumption.

---

# 12. Core Capability

## 12.1 Definition

Core Capability represents a reusable ability provided by the MarkOrbit Core itself.

Examples include:

```text
identity resolution
permission evaluation
knowledge retrieval
trademark search
classification recommendation
document generation
matter creation
event publishing
routing decision support
```

## 12.2 Responsibility

Core Capability is responsible for defining what the Core can provide across products.

It may be implemented through one or more Core Services.

## 12.3 Boundary

Core Capability is not a product feature.

For example:

- Classification Recommendation is a Core Capability.
- Lite class selection page is a product feature.
- Trademark Search is a Core Capability.
- MarkReg trademark search screen is product UI.

---

# 13. Core Service Capability

## 13.1 Definition

Core Service Capability represents capability exposed through a Core Service.

It answers:

> What capability does this service provide?

Examples include:

```text
Knowledge Retrieval Service
    Capability: retrieve authorized professional knowledge

Order-to-Matter Conversion Service
    Capability: convert confirmed order into matter under responsibility rules

Agent Matching Service
    Capability: match service provider or agent based on matter, jurisdiction and capability scope
```

## 13.2 Responsibility

Core Service Capability must define:

- service owner;
- input objects;
- output;
- permission;
- policy;
- context;
- side effects;
- events;
- contracts;
- quality;
- failure behavior.

Detailed service rules are defined in Chapter 15.

---

# 14. AI Capability

## 14.1 Definition

AI Capability represents a governed ability performed or assisted by an AI agent.

It answers:

> What may this AI agent do under Core governance?

Examples include:

```text
AI classification recommendation
AI document draft assistance
AI evidence review assistance
AI trademark status summary
AI office action summary
AI opportunity discovery
AI routing assistance
AI communication summary
AI client explanation drafting
```

## 14.2 Responsibility

AI Capability must define:

- AI agent identity;
- owning domain;
- allowed capability;
- prohibited capability;
- knowledge sources;
- accessible objects;
- allowed services;
- output type;
- risk level;
- human review requirement;
- audit requirement;
- event output;
- product consumers.

## 14.3 Boundary

AI Capability is not prompt text.

Prompt text may implement part of AI Capability.

But the capability is governed by Agent Contract, Knowledge, Permission, Policy, Context and Review.

AI Capability does not own professional responsibility.

---

# 15. Human Professional Capability

## 15.1 Definition

Human Professional Capability represents a professional ability provided by a human user or expert.

Examples include:

```text
trademark filing review
office action strategy review
goods/services classification review
evidence sufficiency review
foreign agent coordination
client communication approval
quote approval
matter supervision
```

## 15.2 Responsibility

Human Professional Capability may be used to determine:

- task assignment;
- review authority;
- permission;
- escalation;
- quality assurance;
- human-in-the-loop requirement;
- AI output approval.

## 15.3 Boundary

Human Professional Capability is not a full HR skill management system.

Book 02 only defines capability where it affects Core execution, responsibility, review or governance.

---

# 16. Agent Capability

## 16.1 Definition

Agent Capability represents what a professional agent, attorney, law firm or foreign associate can do.

Examples include:

```text
file trademark in Thailand
respond to office action in Kenya
handle opposition in the United Kingdom
provide renewal service in the United States
obtain certificate scan
provide legal opinion
handle assignment recordal
```

## 16.2 Responsibility

Agent Capability supports:

- routing;
- agent matching;
- service provider evaluation;
- matter assignment;
- quote generation support;
- reliability tracking;
- network collaboration;
- MGSN consumption.

## 16.3 Capability Scope

Agent Capability should include scope such as:

- jurisdiction;
- service type;
- trademark class scope if relevant;
- language;
- document requirement;
- response time;
- fee basis where product documents allow;
- verification status;
- reliability status;
- communication channel.

## 16.4 Boundary

Agent Capability is not just contact data.

It is a structured professional service ability.

Book 06 may expand network operation and commercial service catalog.

Book 02 defines Core capability meaning.

---

# 17. Service Provider Capability

## 17.1 Definition

Service Provider Capability represents what an external service provider can provide.

Examples include:

```text
translation
notarization
legalization
evidence collection
document processing
local filing support
market investigation
watch service
brand monitoring
```

## 17.2 Responsibility

Service Provider Capability supports:

- routing;
- network matching;
- service coverage;
- provider selection;
- matter execution;
- opportunity service design;
- MGSN product consumption.

## 17.3 Boundary

Service Provider Capability is not a product pricing package.

It defines what the provider can do and under what scope.

Commercial packaging belongs to product or network business documents.

---

# 18. Workflow / Execution Capability

## 18.1 Definition

Workflow / Execution Capability represents the ability of the Core or Workplace to coordinate execution through tasks, events, states and workflow contracts.

Examples include:

```text
create task
assign task
publish event
activate workflow contract
transition matter state
trigger notification
create review task
escalate overdue task
```

## 18.2 Responsibility

Execution Capability supports:

- work coordination;
- traceability;
- review;
- automation;
- notification;
- product status display;
- AI monitoring.

## 18.3 Boundary

Workflow / Execution Capability does not mean Core owns workflow operation.

Core defines primitives and contracts.

Workplace operates workflows.

Products display experience.

---

# 19. Product Consumption Capability

## 19.1 Definition

Product Consumption Capability represents the ability of a product to consume Core capabilities under contract.

Examples include:

```text
MarkReg consumes trademark search
Lite consumes classification recommendation
MGSN consumes agent matching
Workplace consumes task and event structures
Opportunity Engine consumes opportunity scoring
Brand Asset Vault consumes brand and trademark portfolio data
```

## 19.2 Responsibility

Product Consumption Capability defines:

- what Core assets a product may consume;
- which services it may call;
- which events it may subscribe to;
- which AI capabilities it may use;
- what product-specific extensions are allowed;
- what redefinitions are prohibited.

## 19.3 Boundary

Product Consumption Capability is not a product PRD.

It defines Core usage.

Product PRDs define user-facing features.

---

# 20. Capability Provider

Capability Provider answers:

> Who or what provides this capability?

Provider types may include:

```text
core
core_service
human_user
organization
agent
service_provider
ai_agent
workflow_contract
external_system
product
```

Each provider must link to Identity where applicable.

Examples:

- AI Classification Assistant is an AI Agent Identity providing AI Capability.
- Thai law firm is Agent Identity providing Thailand filing capability.
- Internal trademark consultant is User Identity providing review capability.
- Knowledge Retrieval Service is Core Service providing knowledge capability.
- MarkReg is a Product Consumer, not necessarily capability provider unless it exposes product-level capability.

Capability Provider must be explicit.

---

# 21. Capability Consumer

Capability Consumer answers:

> Who or what uses this capability?

Consumers may include:

```text
product
workplace
core_service
workflow_contract
ai_agent
human_user
matter
order
opportunity_engine
routing_service
external_integration
```

Consumer rules define:

- allowed usage;
- permission;
- contract;
- risk;
- output handling;
- review;
- audit.

A capability may have multiple consumers.

Consumption must not redefine capability meaning.

---

# 22. Capability Scope

Capability Scope defines where and when a capability applies.

Scope may include:

- domain;
- object type;
- jurisdiction;
- service type;
- language;
- class;
- matter type;
- product consumer;
- workflow contract;
- customer type;
- provider coverage;
- risk level;
- data source;
- time validity.

Examples:

```text
Agent Capability:
    file trademarks in Kenya
    service type: new filing
    language: English
    status: verified

AI Capability:
    classify goods/services
    jurisdiction: United States and EU
    output: recommendation
    review: required before filing

Core Service Capability:
    retrieve jurisdiction filing requirements
    input: jurisdiction + service type
    output: filing requirement result
```

Capability without scope should be considered incomplete.

---

# 23. Capability Condition

Capability Condition defines when a capability may be used.

Conditions may include:

- permission granted;
- knowledge source available;
- provider verified;
- risk below threshold;
- human review assigned;
- contract version supported;
- object quality sufficient;
- jurisdiction supported;
- product authorized;
- payment or order status satisfied;
- workflow state allows invocation.

Conditions protect the Core from unsafe capability execution.

---

# 24. Capability Requirement

Capability Requirement defines what is needed before capability execution.

Examples:

```text
Classification Recommendation requires:
    goods/services text
    jurisdiction
    knowledge source
    trademark or brand context

Agent Routing requires:
    matter
    jurisdiction
    service type
    provider capability
    policy
    business responsibility

Document Generation requires:
    document type
    matter context
    jurisdiction
    template
    owner information
```

Capability Requirements should be explicit in service, agent and workflow specifications.

---

# 25. Capability Risk Level

Capability Risk Level describes potential professional, business, legal or system impact.

Baseline risk levels:

```text
low
medium
high
critical
```

Examples:

- summarizing a public trademark status may be low or medium risk;
- recommending goods/services may be medium risk;
- generating an office action response draft may be high risk;
- submitting official filing documents may be critical;
- merging identities may be high risk;
- routing a matter to an unverified provider may be high risk.

Risk level determines permission, review, audit and AI restrictions.

---

# 26. Capability Permission

Capability execution requires permission.

Permission questions include:

- who may invoke this capability;
- which object may be used;
- which provider may execute it;
- which product may consume it;
- whether AI may access context;
- whether output may be shown to client;
- whether output may update Core Objects;
- whether external provider may receive data;
- whether review is required before action.

Capability Permission should integrate with the Permission and Policy domains.

Permission should not be only product UI logic.

---

# 27. Capability Review

Some capabilities require human review.

Review may be required when:

- AI output affects client advice;
- legal rights may be affected;
- official filing may be submitted;
- deadline-sensitive action occurs;
- evidence sufficiency is evaluated;
- identity merge is high-risk;
- routing selects an external agent;
- service provider capability is unverified;
- opportunity recommendation affects client strategy.

Review rules should define:

- review trigger;
- reviewer role;
- review task;
- approval outcome;
- rejection outcome;
- event output;
- audit record.

Human review is part of capability governance.

---

# 28. Capability Output

Capability Output defines what the capability produces.

Output types may include:

```text
data result
object creation
object update
recommendation
draft
summary
classification result
routing decision
task
event
notification
validation result
review requirement
error
```

Output should distinguish:

- final result;
- draft;
- recommendation;
- warning;
- failure;
- review-required output;
- partial output.

This distinction is mandatory for AI-related capabilities.

---

# 29. Capability Quality

Capability Quality describes reliability and fitness for use.

Quality dimensions may include:

- provider verification;
- output accuracy;
- knowledge authority;
- freshness;
- coverage;
- response time;
- historical reliability;
- confidence score;
- human review rate;
- error rate;
- completion rate;
- user feedback;
- audit completeness.

Examples:

- Agent Capability quality may include response time and successful filing history.
- AI Capability quality may include groundedness, confidence and review outcome.
- Knowledge Retrieval Capability quality may include source authority and freshness.
- Classification Recommendation quality may include review acceptance rate.

Quality should inform routing, opportunity scoring, product display and AI governance.

---

# 30. Capability Verification

Capability Verification defines whether a capability is trusted.

Baseline verification statuses:

```text
claimed
imported
inferred
self_declared
tested
human_reviewed
verified
trusted
suspended
deprecated
blocked
```

Verification may apply to:

- agent capability;
- service provider capability;
- AI capability;
- human professional capability;
- knowledge capability;
- product consumption capability.

A claimed capability should not be treated as verified.

A suspended capability should not be used for routing without override.

---

# 31. Capability Lifecycle

Capability should have lifecycle.

Baseline lifecycle:

```text
Draft
Registered
Active
Pending Verification
Verified
Suspended
Deprecated
Archived
Blocked
```

Lifecycle transitions may publish events.

Examples:

```text
CapabilityRegistered
CapabilityVerified
CapabilitySuspended
CapabilityDeprecated
CapabilityBlocked
```

Lifecycle should be governed by permission and policy.

---

# 32. Capability Matching

Capability Matching determines whether a provider can satisfy a requirement.

Capability Matching may use:

- provider identity;
- capability scope;
- jurisdiction;
- service type;
- verification status;
- quality;
- availability;
- communication reliability;
- policy;
- cost where allowed by product docs;
- business responsibility;
- risk level.

Examples:

```text
Matter requires Thailand renewal capability.
Routing matches verified Thailand Agent Capability.

Document workflow requires POA generation capability.
Core matches Document Generation Service and jurisdiction template.

AI classification request requires EU class recommendation capability.
Core matches Classification Assistant under Agent Contract.
```

Capability Matching supports Routing, MGSN, MarkReg, Lite and Opportunity Engine.

---

# 33. Capability Invocation

Capability Invocation is the act of using a capability.

Invocation should define:

- invoking identity;
- provider;
- consumer;
- capability;
- context;
- input;
- output;
- permission result;
- policy result;
- risk level;
- review requirement;
- events;
- audit.

Invocation may be performed by:

- Core Service;
- AI agent;
- Workflow Contract;
- Product;
- Workplace;
- human user;
- external system.

High-risk invocation requires stronger audit.

---

# 34. Capability Audit

Capability Audit records how capability was used.

Audit may include:

- capability ID;
- provider identity;
- consumer identity;
- invoking user;
- related objects;
- input summary;
- output summary;
- permission result;
- policy result;
- AI usage;
- review status;
- event ID;
- timestamp;
- failure or success;
- risk level.

Audit is important for:

- AI governance;
- professional responsibility;
- routing decisions;
- service provider reliability;
- client advice;
- official filing support.

---

# 35. Capability Events

Capability-related events may include:

```text
CapabilityRegistered
CapabilityUpdated
CapabilityVerified
CapabilitySuspended
CapabilityDeprecated
CapabilityInvoked
CapabilityMatched
CapabilityInvocationFailed
CapabilityReviewRequired
CapabilityReviewApproved
CapabilityReviewRejected
AgentCapabilityUpdated
ServiceProviderCapabilityUpdated
AICapabilityUsed
```

Event specs should identify:

- source domain;
- provider;
- consumer;
- related objects;
- risk level;
- review requirement;
- audit record;
- downstream consumers.

Capability events support governance, matching, routing and quality improvement.

---

# 36. Capability Services

Baseline Capability Services include:

```text
Capability Registry Service
Capability Lookup Service
Capability Matching Service
Capability Verification Service
Capability Quality Evaluation Service
Capability Invocation Service
Capability Review Assignment Service
Capability Audit Service
Agent Capability Matching Service
Service Provider Capability Matching Service
AI Capability Permission Service
```

## 36.1 Capability Registry Service

Registers capabilities and links them to providers, scope and status.

## 36.2 Capability Matching Service

Matches capability requirements to capability providers.

## 36.3 Capability Verification Service

Manages verification status and review.

## 36.4 Capability Invocation Service

Executes or routes capability invocation under contracts.

## 36.5 Capability Audit Service

Records capability usage and outcomes.

Detailed service specs belong in:

```text
core-specs/services/
```

---

# 37. Capability Contracts

Capability requires several contract types.

## 37.1 Capability Data Contract

Defines capability meaning, provider, scope, status, verification, quality and risk.

## 37.2 Capability API Contract

Defines capability lookup, matching, verification and invocation operations.

## 37.3 Capability Event Contract

Defines events such as `CapabilityVerified`, `CapabilityInvoked` and `CapabilityMatched`.

## 37.4 Agent Contract

Defines AI capability permission, knowledge, object access, output, risk and review.

## 37.5 Consumption Contract

Defines how products consume capabilities without redefining them.

Detailed contracts belong to:

```text
core-specs/contracts/
core-specs/api/
core-specs/events/
core-specs/agents/
```

---

# 38. Capability Data Contract Baseline

A baseline Capability Data Contract should define:

```text
capability_id
capability_name
capability_type
owning_domain
provider_type
provider_id
consumer_types
scope
conditions
requirements
risk_level
permission_required
review_required
verification_status
quality_status
status
source
source_reference
created_at
updated_at
created_by
updated_by
version
```

This is not a final database schema.

It is a semantic baseline for detailed object specification.

---

# 39. Capability API Surface Baseline

A baseline Capability API surface may include:

```text
registerCapability
getCapability
searchCapabilities
matchCapability
verifyCapability
suspendCapability
evaluateCapabilityQuality
invokeCapability
recordCapabilityReview
getProviderCapabilities
getConsumerCapabilities
```

These operation names are conceptual.

Implementation may choose REST, RPC, internal service calls or workflow commands.

Meaning must be preserved by API Contracts.

---

# 40. Capability AI Usage

AI both provides and consumes capability.

## 40.1 AI as Capability Provider

AI may provide:

- classification recommendation;
- document drafting;
- evidence review assistance;
- communication summary;
- opportunity discovery;
- routing suggestion.

## 40.2 AI as Capability Consumer

AI may consume:

- Knowledge Retrieval;
- Trademark Search;
- Jurisdiction Lookup;
- Document Parsing;
- Agent Matching;
- Event Summary;
- Task Context.

## 40.3 AI Governance Rules

AI Capability must define:

- AI agent identity;
- allowed scope;
- authorized knowledge;
- object access;
- service access;
- output type;
- risk level;
- confidence handling;
- review requirement;
- audit event;
- prohibited actions.

AI must not silently expand its capabilities.

New AI capabilities require Agent Contract update.

---

# 41. Capability and Product Consumption

Products consume capabilities differently.

## 41.1 MarkReg

Consumes capabilities for:

- trademark search;
- matter creation;
- document generation;
- agent matching;
- task execution;
- event tracking;
- filing workflow support.

## 41.2 Lite

Consumes capabilities for:

- guided consultation;
- AI classification recommendation;
- filing requirement retrieval;
- quote support;
- order creation;
- opportunity conversion.

## 41.3 MGSN

Consumes capabilities for:

- agent capability display;
- service provider matching;
- routing;
- reliability tracking;
- communication coordination.

## 41.4 Workplace

Consumes capabilities for:

- task assignment;
- workflow operation;
- human review;
- AI assistance;
- event monitoring.

## 41.5 Opportunity Engine

Consumes capabilities for:

- opportunity discovery;
- portfolio analysis;
- scoring;
- routing;
- notification.

Products may present capabilities differently.

They shall not redefine capability meaning.

---

# 42. Capability MVP Boundary

The Capability MVP should implement enough to support early Core execution and AI governance.

MVP should include:

```text
Capability Object
Capability Provider
Capability Scope
Capability Verification Status
Capability Risk Level
Basic Capability Registry
Basic Capability Lookup
Basic Capability Matching
AI Capability Permission Rules
Agent Capability baseline
Service Provider Capability baseline
CapabilityInvoked Event
Capability Data Contract
Capability API Contract
```

MVP may defer:

- advanced quality scoring;
- full provider marketplace capability catalog;
- automated capability verification;
- complex capability ranking;
- full MGSN commercial service catalog;
- advanced AI capability self-evaluation.

MVP must not skip capability governance if AI or routing is implemented.

---

# 43. Capability Specification Structure for core-specs/

Recommended files:

```text
core-specs/domains/capability.md
core-specs/objects/capability.md
core-specs/objects/capability-provider.md
core-specs/objects/capability-scope.md
core-specs/objects/capability-verification.md
core-specs/services/capability-registry.md
core-specs/services/capability-matching.md
core-specs/services/capability-verification.md
core-specs/services/capability-invocation.md
core-specs/events/capability-registered.md
core-specs/events/capability-verified.md
core-specs/events/capability-invoked.md
core-specs/contracts/capability-data-contract.md
core-specs/api/capability-api.md
core-specs/agents/capability-governance.md
```

Capability may also be embedded in domain specs such as:

```text
core-specs/domains/agent.md
core-specs/domains/service-provider.md
core-specs/domains/routing.md
core-specs/domains/classification.md
core-specs/domains/document.md
```

---

# 44. Capability Specification Template

A detailed Capability specification should include:

```text
# Capability Specification

1. Capability Purpose
2. Owning Domain
3. Capability Type
4. Provider Type
5. Provider Identity
6. Consumer Types
7. Scope
8. Conditions
9. Requirements
10. Input
11. Output
12. Knowledge Dependencies
13. Permission and Policy Requirements
14. Risk Level
15. Human Review Requirements
16. Verification Rules
17. Quality Rules
18. Lifecycle
19. Events Published
20. Contracts
21. AI Usage
22. Product Consumers
23. MVP Boundary
24. Acceptance Criteria
25. Revision Notes
```

Detailed object, service, event, API and agent specs should follow the structures defined in Chapters 14 through 17.

---

# 45. Capability Review Questions

When reviewing a capability, reviewers shall ask:

1. What ability does this capability represent?
2. Which Core Domain owns it?
3. Who or what provides it?
4. Who or what consumes it?
5. What scope applies?
6. What conditions must be met before use?
7. What requirements are needed for execution?
8. What objects and knowledge does it depend on?
9. What permission and policy rules apply?
10. What risk level applies?
11. Is human review required?
12. What output does it produce?
13. What verification status applies?
14. What quality rules apply?
15. What events should be emitted?
16. What contracts expose it?
17. Does AI provide or consume this capability?
18. Which products consume it?
19. Would fragmentation occur if each product defined this capability locally?
20. Can Codex implement it from approved specs?

---

# 46. Capability Anti-Patterns

## 46.1 Function Equals Capability

A local function is treated as Core Capability.

Correction:

```text
Capability must represent reusable governed ability.
Implementation functions realize capability.
```

## 46.2 Prompt Equals Capability

A prompt template is treated as AI Capability.

Correction:

```text
AI Capability is governed by Agent Contract.
Prompt is implementation detail.
```

## 46.3 Service Item Equals Capability

A product pricing service item is treated as Core Capability.

Correction:

```text
Core Capability defines ability.
Pricing packages belong to product or business documents.
```

## 46.4 Claimed Capability Treated as Verified

An agent claims a jurisdiction service and system treats it as trusted.

Correction:

```text
Capability verification status must be explicit.
```

## 46.5 Capability Without Scope

A provider is marked as “trademark filing capable” without jurisdiction, service type or conditions.

Correction:

```text
Capability requires scope.
```

## 46.6 AI Capability Without Review

AI produces high-risk output without review requirement.

Correction:

```text
Risk level determines human review.
```

## 46.7 Product-Local Capability

MarkReg, Lite and MGSN define separate capability meanings.

Correction:

```text
Shared capability belongs to Core.
Products consume capability through contracts.
```

---

# 47. Capability Rules

The following rules are established by this chapter.

## Rule 1 — Capability SHALL be governed ability

Capability is not merely function, service item, prompt or UI action.

## Rule 2 — Capability SHALL have provider and consumer context

Provider and consumer must be explicit where capability is executed or consumed.

## Rule 3 — Capability SHALL define scope

Jurisdiction, service type, domain, object, product or risk scope must be clear where relevant.

## Rule 4 — Capability SHALL define permission and policy

Capability execution must respect Core governance.

## Rule 5 — Capability SHALL define risk and review

High-risk capability requires human review and audit.

## Rule 6 — Capability SHALL distinguish claimed from verified

Capability verification status must be explicit.

## Rule 7 — AI Capability SHALL operate under Agent Contract

AI capability is not prompt-only execution.

## Rule 8 — Capability SHALL be consumed through contracts

Products, Workplaces, AI agents and services consume capability under contracts.

## Rule 9 — Capability changes SHALL be versioned where semantic or contract-affecting

Capability evolution must preserve compatibility.

## Rule 10 — MVP SHALL include capability governance if AI or routing exists

AI and routing without capability governance are not acceptable.

---

# 48. Specification Output

This chapter produces the following specification output:

- Capability definition;
- Capability principles;
- Capability ontology;
- Capability domain relationships;
- capability object types;
- Capability Object baseline;
- capability categories;
- Core Capability;
- Core Service Capability;
- AI Capability;
- Human Professional Capability;
- Agent Capability;
- Service Provider Capability;
- Workflow / Execution Capability;
- Product Consumption Capability;
- Capability Provider;
- Capability Consumer;
- Capability Scope;
- Capability Condition;
- Capability Requirement;
- Capability Risk Level;
- Capability Permission;
- Capability Review;
- Capability Output;
- Capability Quality;
- Capability Verification;
- Capability Lifecycle;
- Capability Matching;
- Capability Invocation;
- Capability Audit;
- Capability Events;
- Capability Services;
- Capability Contracts;
- Capability Data Contract baseline;
- Capability API baseline;
- AI usage rules;
- Product Consumption;
- MVP Boundary;
- `core-specs/` file structure;
- review questions;
- anti-patterns;
- Capability rules.

These outputs guide detailed specs in `core-specs/`.

---

# 49. Execution Mapping

This chapter controls capability-related implementation assets.

| Capability Specification Element | Execution Mapping |
|----------------------------------|------------------|
| Capability Object | capability model and persistence |
| Provider / Consumer | identity links and consumption rules |
| Scope | capability filters, routing and matching constraints |
| Conditions / Requirements | validation and execution preconditions |
| Risk Level | review, audit and permission logic |
| Verification Status | provider trust and routing eligibility |
| Quality | scoring, monitoring and feedback |
| Matching | routing and provider selection services |
| Invocation | service calls, AI tool calls, workflow triggers |
| Events | capability events and audit trail |
| Contracts | data, API, agent and consumption contracts |
| AI Usage | Agent Contract and review workflow |
| Product Consumption | MarkReg, Lite, MGSN, Workplace integration |
| MVP | Codex task sequencing |

Implementation shall preserve capability meaning, scope, governance and auditability.

---

# 50. Relationship to core-specs/

This chapter is the manuscript source for Capability-related `core-specs/`.

Detailed specs shall be maintained in:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
```

No product document shall override the Core Capability Specification.

No implementation task shall create capability meaning without reference to approved Capability specs or explicit architecture review.

---

# 51. Exclusions

This chapter shall not include:

- complete database schema;
- product feature list;
- service pricing catalog;
- MGSN marketplace pricing;
- HR training curriculum;
- full AI prompt library;
- vendor tool implementation;
- full workflow operations;
- all production API endpoints;
- deployment architecture;
- implementation code.

These belong elsewhere.

---

# 52. Acceptance Criteria

This chapter is accepted only if it satisfies the following criteria.

- It defines Capability clearly as governed ability.
- It distinguishes Capability from product function, UI action, prompt, vendor wrapper and pricing service item.
- It defines provider, consumer, scope, condition, requirement, risk, review, quality, verification and lifecycle.
- It defines Core, Service, AI, Human, Agent, Service Provider, Workflow and Product Consumption capabilities.
- It connects Capability to Identity, Knowledge, Permission, Policy, Routing, AI and Product Consumption.
- It defines baseline services, events, contracts and API surface.
- It provides MVP boundary.
- It provides `core-specs/` structure.
- It includes review questions, anti-patterns and rules.
- It supports Book 02 TOC v1.2.
- It supports implementation without becoming a product feature list or marketplace catalog.

---

# 53. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial draft of Chapter 19, defining Capability Specification for the MarkOrbit Core. |

---

**End of Chapter**
