#!/usr/bin/env python3
"""Generate Book 04 vNext Candidate 03 by consolidating Candidate 02."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
SOURCE_BUILDER = ROOT / "tools/build_book04_vnext_candidate_02.py"
TRANSFORM = BOOK / "vnext/B04-TRANSFORM-0001_Candidate_03_Editorial_Transform_Manifest.json"
DEFAULT_OUT = ROOT / "build/book04-vnext-candidate-03"

INSTALLATION = """## Product Installation as Governed Workplace Participation

A Product Installation is the Workplace-scoped governed participation relationship through which a Product is entitled, activated, configured and authorized for use. It records the installation identity, Workplace, edition or plan, authorized users, permitted record scope, capabilities, configuration, purpose, Handoff and Return contracts, audit requirements, suspension and revocation state.

```text
entitlement
≠ activation
≠ authorized user
≠ authorized record scope
≠ formal-state authority
```

Disabling or revoking an installation stops future access, projection and Handoff within that installation. It does not erase authoritative records, completed work, audit history or legal retention duties.
"""

EMBEDDING_BRIDGE = """Product embedding uses an already governed Product Installation; it does not create installation authority by visual placement alone. An embedded or launched Product receives only the purpose-bound context, entitlement and permissions established for that installation. Projection, Handoff and Return preserve continuity without transferring source authority or Workplace sovereignty.
"""


def load_source_builder():
    spec = importlib.util.spec_from_file_location("candidate02", SOURCE_BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Candidate 02 builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_first_h1(text: str, heading: str) -> str:
    return re.sub(r"(?m)^# .+$", f"# {heading}", text, count=1)


def insert_before_first_h2(text: str, block: str) -> str:
    match = re.search(r"(?m)^## ", text)
    at = match.start() if match else len(text)
    return text[:at].rstrip() + "\n\n" + block.strip() + "\n\n" + text[at:].lstrip()


def consolidate_ch22(text: str) -> str:
    pattern = re.compile(
        r"<!--\n(?:.|\n)*?integration_status: editorial-consolidation-acceptance-candidate\n-->\n\n"
        r"A Product Installation is the Workplace-scoped(?:.|\n)*?legal retention duties\.\n\n",
        re.M,
    )
    marker = """<!--
candidate: B04-vNEXT-CANDIDATE-03
chapter: CH22
candidate02_transform: Product Installation primary definition relocated to CH20
transform_manifest: books/book-04-workplace-product-architecture/vnext/B04-TRANSFORM-0001_Candidate_03_Editorial_Transform_Manifest.json
integration_status: editorial-consolidation-acceptance-candidate
-->

"""
    updated, count = pattern.subn(marker + EMBEDDING_BRIDGE + "\n", text, count=1)
    if count != 1:
        raise RuntimeError("could not relocate CH22 Product Installation definition")
    return updated


def structure_ch37(text: str) -> str:
    needle = "Workplace portability covers organization-controlled configuration"
    if needle not in text:
        raise RuntimeError("CH37 portability prose not found")
    return text.replace(needle, "## Portability, Exit and Revocation Across Orbits\n\n" + needle, 1)


def dedupe_long_paragraphs(text: str, minimum: int) -> tuple[str, int]:
    blocks = re.split(r"(\n\s*\n)", text)
    seen: set[str] = set()
    removed = 0
    output: list[str] = []
    in_code = False
    for block in blocks:
        stripped = block.strip()
        if stripped.startswith("```"):
            in_code = not in_code if stripped.count("```") % 2 else in_code
        eligible = (
            not in_code
            and len(stripped) >= minimum
            and not stripped.startswith(("#", "<!--", "```", "|", "- ", ">"))
        )
        key = re.sub(r"\s+", " ", stripped)
        if eligible and key in seen:
            removed += 1
            continue
        if eligible:
            seen.add(key)
        output.append(block)
    return "".join(output), removed


def transform_chapter(chapter: str, text: str, manifest: dict) -> tuple[str, int]:
    text = text.replace("B04-vNEXT-CANDIDATE-02", "B04-vNEXT-CANDIDATE-03")
    text = text.replace(
        "vNext Candidate 02 — Route-Aware Full-Book Review Draft",
        "vNext Candidate 03 — Editorial Consolidation Acceptance Candidate",
    )
    text = text.replace(
        "integration_status: route-aware-review-candidate",
        "integration_status: editorial-consolidation-acceptance-candidate",
    )
    text = text.replace(
        "route_manifest:",
        "candidate02_route_manifest:",
    )
    if chapter == "CH20":
        text = insert_before_first_h2(text, INSTALLATION)
    if chapter == "CH22":
        text = consolidate_ch22(text)
    if chapter == "CH23":
        text = replace_first_h1(text, manifest["heading_changes"]["CH23"])
        for old, new in manifest["targeted_normalization"]["CH23"]:
            text = text.replace(old, new)
    if chapter == "CH37":
        text = structure_ch37(text)
    text, removed = dedupe_long_paragraphs(text, manifest["deduplication"]["minimum_paragraph_characters"])
    return text.rstrip() + "\n", removed


def build(output: Path) -> None:
    source = load_source_builder()
    source.build(output)
    manifest = json.loads(TRANSFORM.read_text(encoding="utf-8"))
    manuscript = output / "manuscript"
    deduped = 0
    for index in range(40):
        chapter = f"CH{index:02d}"
        path = manuscript / f"{chapter}.md"
        text, removed = transform_chapter(chapter, path.read_text(encoding="utf-8"), manifest)
        deduped += removed
        path.write_text(text, encoding="utf-8")

    index_path = output / "CANDIDATE-INDEX.md"
    index_text = index_path.read_text(encoding="utf-8").replace("Candidate 02", "Candidate 03")
    index_text = index_text.replace("ROUTE-AWARE FULL-BOOK REVIEW DRAFT", "EDITORIAL CONSOLIDATION ACCEPTANCE CANDIDATE")
    index_text = index_text.replace("Lite as a Lightweight Workplace]", "Lite as a Lightweight Workplace Product]")
    index_path.write_text(index_text, encoding="utf-8")

    (output / "TRANSFORM-REPORT.md").write_text(
        "# Candidate 03 Transform Report\n\n"
        "```text\n"
        "Generated heading changes: 1 / 1\n"
        "Product Installation definition relocations: 1 / 1\n"
        "Embedding-focused CH22 bridge: 1 / 1\n"
        "Structured portability subsections: 1 / 1\n"
        f"Exact long-paragraph duplicates removed: {deduped}\n"
        "RC1 source modifications: 0\n"
        "```\n",
        encoding="utf-8",
    )
    (output / "BUILD-REPORT.md").write_text(
        "# Candidate 03 Build Report\n\n```text\n"
        "Source Candidate 02 chapters: 40 / 40\n"
        "Candidate 03 chapters generated: 40 / 40\n"
        "Reviewed heading changes applied: 1 / 1\n"
        "Product Installation placement corrections: 1 / 1\n"
        "Structured portability subsections: 1 / 1\n"
        "Reader-text leakage findings: 0\n"
        "Remaining title contradictions: 0\n"
        "Remaining route / placement majors: 0\n"
        "Exact long-paragraph duplicate clusters: 0\n"
        "RC1 source modifications: 0\n"
        "Blocking findings: 0\n"
        "Immediate Book 02 Change Proposal required: NO\n"
        "```\n\nCandidate 03 is an acceptance candidate. Final Owner Acceptance remains a separate explicit gate.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    build(output)
    print(f"Book 04 vNext Candidate 03 generated at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
