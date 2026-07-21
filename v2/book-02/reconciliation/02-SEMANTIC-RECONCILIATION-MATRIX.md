# Semantic Reconciliation Matrix

| v2 concept | Classification | Core treatment | Reason |
| --- | --- | --- | --- |
| Person | F0 | retain existing identity semantics | Durable shared identity reference |
| Organization | F0 | retain existing organization semantics | Accountable legal or business actor |
| Workplace | F0/F2 | retain active meaning; add explanatory profile only | Already canonical as business-sovereignty and Product-operation boundary |
| Membership | F0 | retain | Person-to-Workplace authority relationship |
| Business Sovereignty | F2 | authority profile, not new object | Describes authority dimension rather than business record |
| Semantic Authority | F2 | authority profile | Core responsibility statement |
| Formal-State Authority | F2 | authority profile | Owning Service responsibility statement |
| Physical Custody | F2 | authority profile | Storage relationship, not ownership transfer |
| Professional Authority | F3 | candidate shared authority reference | Needed by Execution, MarkReg and MGSN to gate reserved actions |
| Relationship Owner | F3 | candidate role/reference profile | Needed across Lite, MarkReg, Workplace and MGSN |
| Contracting Party | F1/F2 | Organization role in Engagement or Order | No independent universal object required |
| Payment Receiver | F1/F2 | Organization role plus payment reference | Commercial role, not identity type |
| Delivery Owner | F3 | candidate responsibility reference | Needed across multi-party Outcome assembly |
| Resource Profile | F2 | Workplace profile | Aggregated view of existing assets, capabilities and relationships |
| Need Profile | F2 | Workplace profile | Aggregated demand view; individual Need remains separate |
| Capability Profile | F2 | profile over certifications, supply and evidence | Avoid duplicating Capability Definition |
| Capacity Profile | F2 | operational projection profile | Volatile and context-specific |
| Asset Profile | F2 | product or Workplace profile | Assets remain typed domain records |
| Need | F3 | candidate shared object | Distinct from Opportunity and Order; cross-product demand origin |
| Opportunity | F0/F2 | retain existing opportunity semantics; clarify route meaning | Existing concept can support potential value route |
| Engagement | F3/F4 | candidate shared collaboration contract | New durable boundary between Opportunity and Order may require lifecycle addition |
| Engagement Role | F2/F3 | controlled role vocabulary | Roles are context-specific and should not become Person types |
| Commercial Arrangement | F2 | Engagement profile or Product-local terms | Pricing policy remains outside Core |
| Order | F0 | retain | Formal customer-facing commercial commitment |
| Matter | F0 | retain | Long-lived professional subject distinct from Order |
| Work Package | F3 | candidate bounded work object | Required across MarkReg, contribution and Execution |
| Step | F0 | retain Execution stage semantics | Not interchangeable with Work Package |
| Assignment | F3 | candidate authorization record | Binds Work Package to actor, scope and deadline |
| Contribution | F3 | candidate submitted-work record | Broader than document or task completion |
| Review | F0/F2 | retain review semantics; add typed profiles | Existing review can be specialized by scope |
| Revision Request | F1 | review outcome/state | No standalone universal object unless lifecycle evidence requires it |
| Outcome | F3 | candidate accepted result reference | Needed to assemble multiple Contributions without equating them to formal state |
| Evidence | F0 | retain | Source, actor, method, time and authority lineage |
| Capability Definition | F0 | retain and expand only through governed versioning | Already first-class Core concept |
| Capability Level L1–L5 | F2/F3 | controlled reference vocabulary | Shared display and eligibility value set |
| Human–AI Mode M0–M5 | F2/F3 | controlled execution-mode vocabulary | Shared across Capability and Execution |
| Risk Tier R0–R4 | F2/F3 | controlled policy vocabulary | May remain policy profile rather than object |
| Capability Certification | F3 | candidate credential type | Cross-product and user-portable |
| Production Authorization | F3/F4 | candidate authorization object/lifecycle | Grants real-work access and therefore requires strict governance |
| Professional Qualification | F1/F2 | credential specialization | Existing credential/evidence constructs may represent it |
| Assessor Authorization | F2/F3 | authorization specialization | Needed by Simulation but may use ProductionAuthorization pattern |
| Capability Evidence | F1/F2 | evidence profile | Evidence with capability reference and assessment context |
| Simulation Workplace | F2 | Workplace mode/profile | Should not redefine Workplace identity |
| Case Fixture | F2 | simulation-local evidence package | Product/Execution local unless shared interchange emerges |
| Assessment Result | F1/F2 | Review + Evidence profile | No new universal object required initially |
| Projection | F0 | retain active projection semantics | Purpose-limited view without ownership transfer |
| Demand Projection | F2 | Projection profile | Typed purpose and payload |
| Capability Projection | F2 | Projection profile | Supply view over capability and capacity |
| Asset Projection | F2 | Projection profile | Listing or sharing view over asset |
| Audience Projection | F2 | Projection profile | Marketing reach view; likely Lite-local |
| Capacity Projection | F2 | Projection profile | Time-sensitive supply view |
| Product Installation | F0 | retain | Workplace-scoped Product participation record |
| Handoff | F0 | retain | Typed outbound context transfer |
| Return | F0 | retain | Typed evidence or result returned to origin |
| Provider Organization | F1/F2 | Organization profile with provider eligibility | Avoid separate identity universe |
| Contributor | F1/F2 | Person or Workplace role in Assignment | Role, not permanent actor type |
| Provider Appointment | F2/F3 | Engagement/Assignment specialization | Distinct from recommendation; candidate contract profile |
| Candidate Route Set | F2 | MGSN-local recommendation artifact | Algorithm and procurement context remain network-local |
| Instruction Package | F2/F3 | Handoff payload profile | Cross-product usefulness but may remain contract profile |
| Evidence Return | F2 | Return profile | No new root object required |
| Settlement | F0/F2 | retain shared commercial status/reference | Detailed policy remains Owning Service-local |
| Compensation | F2/F3 | neutral reference profile | Avoid importing rate policy into Core |
| Commission Claim | F2 | Lite/transaction-local commercial claim | Not yet universal |
| Trademark Inventory | F2 | Lite/commerce profile over Trademark and authorization | Trademark remains legal record |
| Resale Authorization | F3 | candidate rights/authority record | Needed to prove ability to list or broker an asset |
| Listing | F2/F3 | Projection specialization | Could remain commerce-local until cross-product interchange stabilizes |
| Trademark Request | F2/F3 | Need specialization | Do not create parallel demand semantics |
| Buyer Inquiry | F2 | Relationship/Opportunity communication profile | Product-local lifecycle |
| Transaction Opportunity | F2 | Opportunity specialization | No separate Core root required |
| Knowledge Source/Document/Claim/Version | F0/F3 | preserve existing source/provenance model; candidate shared knowledge contracts only if absent | Knowledge Refinery requires stable references, not Core ownership |
| Brain Result | F2/F3 | typed intelligence result profile | Retrieval, inference, recommendation, candidate and explanation must remain distinct |
| Data Product | F2/F3 | versioned product reference | Canonical data content remains Data-owned |

## Matrix conclusion

The v2 architecture does not justify turning every new noun into a Core object.

The strongest shared candidates are:

```text
Need
Engagement
Work Package
Assignment
Contribution
Outcome
Professional Authority
Relationship Owner
Delivery Owner
Capability Certification
Production Authorization
Resale Authorization
```

Even these remain candidates until the frozen baseline is mapped at contract and lifecycle level.
