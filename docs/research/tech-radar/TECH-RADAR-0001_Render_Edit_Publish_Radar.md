# TECH-RADAR-0001: Render / Edit / Publish Radar

## Purpose

Capture pre-research candidates for Mo Render, Mo Edit, and Mo Publish without turning tools into Mo architecture or product scope.

## Scope

This radar covers candidate renderers, editors, asset connectors, local publish helpers, and digital-human references for future review. It supports research governance only.

## Evaluation Dimensions

| Dimension | Review Question |
|---|---|
| Architecture fit | Can the tool remain a replaceable provider, worker, adapter, or reference? |
| Output quality | Does it produce acceptable PDF, image, audio, video, caption, or page output? |
| Local-first support | Can it support local/manual/human-confirmed workflows before cloud automation? |
| Integration complexity | How much adapter work, runtime setup, and operational maintenance is required? |
| License and rights | Are licenses, asset rights, and redistribution constraints acceptable? |
| Deployment risk | Are runtime, platform, dependency, or performance constraints manageable? |
| Governance | Can use be audited, reviewed, and bounded by Mo execution rules? |

## A/B/C/D Grading Rules

| Grade | Meaning |
|---|---|
| A | Strong candidate for a bounded POC after publication review. |
| B | Promising candidate with known risks that require mitigation. |
| C | Reference only or later-stage candidate; not ready for POC. |
| D | Do not pursue unless assumptions change. |

## Candidate Areas

| Area | Notes |
|---|---|
| PDF Renderer | Convert structured artifacts into reviewed PDF output. |
| Graphic Renderer | Convert structured artifacts into PNG/SVG or social image output. |
| Video Renderer | Produce governed video from structured artifact inputs. |
| TTS / Audio Renderer | Produce audio narration or voice tracks from approved text. |
| Caption Engine | Generate or align captions for audio/video outputs. |
| Stock Asset Connector | Search and retrieve licensed assets through explicit connectors. |
| Video Edit | Post-process existing media/materials rather than redefine business logic. |
| Publish Local Plugin | Package and assist distribution through local/manual/human-confirmed steps. |
| Digital Human | Research Mo Persona-style presentation surfaces without changing Core. |

## First-Priority POC Candidates

| Candidate | Candidate Area | Initial Radar Posture |
|---|---|---|
| Playwright PDF | PDF Renderer | Candidate for local PDF rendering research. |
| Satori / resvg | Graphic Renderer | Candidate for structured image rendering research. |
| Remotion | Video Renderer | Candidate for programmatic video rendering research. |
| HyperFrames | Video Renderer | Candidate for alternate video rendering research. |
| TTS Provider | TTS / Audio Renderer | Candidate provider class for narration research. |
| Pexels Video API | Stock Asset Connector | Candidate connector for licensed stock-video research. |

## Non-goals

- Do not integrate tools directly into mainline.
- Do not allow tools to redefine Mo.
- Do not cloud auto-publish.
- Do not scrape external asset libraries in bulk.
- Do not use AI video/image generation for precise trademark text/logo output.
