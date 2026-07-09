# INTAKE-001: Distillery, Artifact, Render, Edit, Publish

## Source Idea Documents

1. Mo Distillery（知识精馏工厂）构想总结
2. Mo 技术参考仓库雷达与预研清单
3. MarkOrbit / Mo lite 新想法讨论总结：Mo Artifact、Mo Render、Mo Edit、Mo Publish

## Executive Summary

This intake classifies several important MarkOrbit / Mo ideas before any manuscript rewrite or implementation work. The ideas are valuable, but they belong in different layers:

- Mo Distillery is a knowledge production system, not a simple summarizer.
- Mo Artifact / Mo Render / Mo Edit / Mo Publish are an application-facing business artifact production and distribution chain.
- Mo Technical Radar is research governance / pre-research, not book manuscript content.

These ideas must not expand Book 02 MVP, redefine Book 02 Core primitives, or turn Book 03 into a product UI or technology selection manual.

## Idea Inventory

| Idea | Short Description | Intake Posture |
|---|---|---|
| Mo Distillery | Governed knowledge distillation and production capability. | Important; classify as knowledge production. |
| Mo Brain / Distillery / Capability / Skill chain | Boundary between validated knowledge, reusable capability, operational skill, and workflow fragments. | Important boundary note. |
| Mo Artifact | Business output produced by Mo. | Future business artifact concept. |
| Mo Render | Result-processing layer that turns structured artifacts into output formats. | Research and future extension. |
| Mo Edit | Post-processing for existing media/material. | Research and future extension. |
| Mo Publish | Packaging and distribution support. | Local/manual/human-confirmed first. |
| Mo Technical Radar | Candidate-tool evaluation and pre-research governance. | Research area only. |

## Layer Classification

| Idea Group | Type | Owning Layer |
|---|---|---|
| Mo Distillery | Knowledge Production System | Book 01 principle; Book 02 boundary note; Book 03 governed execution. |
| Mo Artifact / Render / Edit / Publish | Business Artifact Production and Distribution Chain | Book 01 principle; Book 03 execution boundaries; Book 04 product surfaces later. |
| Mo Technical Radar | Research Governance / Pre-research System | `docs/research/tech-radar/`; not canonical architecture. |

## Book 01 Write-in Recommendation

- Write Mo Distillery into Book 01 as an architecture principle / knowledge production capability.
- Write Mo Artifact / Render / Edit / Publish into Book 01 only as a high-level architecture principle for business artifact production and distribution.
- Mention Technical Radar only as a principle: tools do not define Mo architecture.

## Book 02 Write-in Recommendation

- Mo Distillery: yes, but only as a Core boundary note around Knowledge / Capability / Skill / Workflow Fragment.
- Mo Artifact / Render / Edit / Publish: light note only as future extension, not MVP.
- Mo Technical Radar: no direct write-in.
- Do not modify Book 02 Core specs or Book 02 MVP boundary from this intake.

## Book 03 Write-in Recommendation

- Mo Distillery: yes, as Distillation Workflow / governed knowledge-production execution.
- Mo Artifact / Render / Edit / Publish: yes, as execution flows and governance boundaries.
- Mo Technical Radar: no direct write-in, except as an optional execution research governance reference.
- Do not make Book 03 a product UI or technology selection manual.

## Research / Tech Radar Recommendation

- Mo Distillery research is optional and later-stage.
- Mo Render / Mo Edit / Mo Publish should receive research attention before implementation.
- Mo Technical Radar belongs under `docs/research/tech-radar/` and should record candidate tools, risks, license concerns, deployment concerns, POC plans, and decisions.
- Tools are replaceable providers, workers, adapters, or references.

## MVP Impact Assessment

| Idea | MVP Impact |
|---|---|
| Mo Distillery | Must not expand Book 02 MVP; may become a future Mo 2.x capability. |
| Mo Artifact / Render / Edit / Publish | Do not change Lite 1.1 mainline; reserve fields only if already planned; Lite 1.2+ may begin Mo Render MVP. |
| Mo Technical Radar | No MVP impact; research governance only. |

## Architecture Risk Assessment

| Risk | Mitigation |
|---|---|
| Distillery becomes a generic summarizer. | Preserve it as governed knowledge production. |
| Artifact becomes a generic content draft. | Define Artifact as business output. |
| Render becomes business logic. | Keep Render as result-processing only. |
| Edit becomes authoring logic. | Keep Edit as post-processing for existing media/material. |
| Publish becomes cloud auto-publishing. | Start with local/manual/human-confirmed publish support. |
| Tools redefine architecture. | Keep tools in Tech Radar as replaceable support components. |
| Book 02 MVP expands. | No Core spec or MVP boundary changes in this intake. |
| Book 03 becomes product UI guidance. | Keep Book 03 focused on execution flows and governance boundaries. |

## Publication Decision Table

| Idea | Type | Book 01 | Book 02 | Book 03 | Research | Decision |
|---|---|---|---|---|---|---|
| Mo Distillery | Knowledge Production System | Yes: principle / capability. | Boundary note only. | Yes: governed distillation workflow. | Optional later. | Accept for planning review, not immediate rewrite. |
| Mo Artifact / Render / Edit / Publish | Business Artifact Production and Distribution Chain | Yes: high-level principle. | Light future-extension note only. | Yes: execution flows and governance boundaries. | Yes, especially Render / Edit / Publish. | Accept for planning review, not MVP expansion. |
| Mo Technical Radar | Research Governance / Pre-research System | Principle only. | No direct write-in. | Optional governance reference only. | Yes. | Keep in research area, not manuscript. |

## Boundaries to Preserve

### Mo Distillery Boundary

- Mo Distillery produces knowledge artifacts.
- Mo Brain stores validated knowledge.
- Capability Catalog exposes reusable capability.
- Skill Library operationalizes capability.

### Artifact / Render / Edit / Publish Boundary

- Artifact is business output.
- Render turns structured artifacts into PDF / PNG / MP3 / MP4 / pages.
- Edit modifies existing media/materials.
- Publish packages and assists distribution.
- Cloud auto-publish is not first-stage.
- Local/manual/human-confirmed publish comes first.

### Technical Radar Boundary

- Tools do not define Mo.
- Mo defines business architecture.
- Tools are evaluated as replaceable providers, workers, adapters, or references.
- Tech radar should not become book manuscript content.

## Recommended Next Actions

1. Run Publication Idea Intake Pack 01 Review.
2. Decide whether Book 01 should receive a small architecture-principle planning note.
3. Decide whether Book 02 should receive only a future boundary note, without changing Core specs or MVP.
4. Decide whether Book 03 Round 1 planning should include future execution-boundary notes for Distillery / Artifact / Render / Publish.
5. Continue Render / Edit / Publish evaluation in Tech Radar before any POC or implementation task.

## Codex Constraints

- Do not rewrite manuscript chapters.
- Do not write full book content.
- Do not modify Book 02 Core specs.
- Do not modify Book 02 MVP boundary.
- Do not modify Book 03 manuscript chapters.
- Do not create implementation code.
- Do not create POC directories.
- Do not add dependencies.
- Do not infer new Core domains from these ideas.
