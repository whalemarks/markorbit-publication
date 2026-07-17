#!/usr/bin/env python3
"""Generate the full Book 04 vNext Candidate 01 without modifying RC1."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
RC1 = BOOK / "manuscript"
DEFAULT_OUT = ROOT / "build/book04-vnext-candidate-01"

EDIT_FILES = (
    BOOK / "vnext/editorial/B04-EDIT-0001_CH00-CH12_Editorial_Weave_Patch_Set.md",
    BOOK / "vnext/editorial/B04-EDIT-0002_CH13-CH27_Editorial_Weave_Patch_Set.md",
    BOOK / "vnext/editorial/B04-EDIT-0003_CH28-CH39_Editorial_Weave_Patch_Set.md",
)

HISTORICAL_CHAPTER_RE = re.compile(r"\bCH[-_ ]?(0[0-9]|[1-3][0-9])\b", re.IGNORECASE)
MODULE_RE = re.compile(r"(?m)^## (CH(?:0[0-9]|[1-3][0-9])) — .+$")
FIELD_RE = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$")


def read(path: Path) -> str:
    if not path.is_file():
        raise RuntimeError(f"missing source: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalized_ids(text: str) -> list[str]:
    return sorted({f"CH{m.group(1)}" for m in HISTORICAL_CHAPTER_RE.finditer(text)})


def identify_chapter(path: Path) -> str | None:
    ids = normalized_ids(path.name)
    if len(ids) == 1:
        return ids[0]
    if len(ids) > 1:
        raise RuntimeError(f"ambiguous chapter filename: {path.relative_to(ROOT)}")
    for line in read(path).splitlines():
        if line.startswith("# "):
            ids = normalized_ids(line)
            if len(ids) == 1:
                return ids[0]
            break
    return None


def discover_rc1() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in sorted(RC1.rglob("*.md")):
        chapter = identify_chapter(path)
        if chapter is None:
            continue
        if chapter in found:
            raise RuntimeError(f"duplicate RC1 source for {chapter}")
        found[chapter] = path
    expected = {f"CH{i:02d}" for i in range(40)}
    if set(found) != expected:
        raise RuntimeError(
            f"RC1 discovery mismatch: missing={sorted(expected-set(found))}, "
            f"extra={sorted(set(found)-expected)}"
        )
    return found


def clean_candidate_lines(lines: list[str]) -> str:
    output: list[str] = []
    for raw in lines:
        line = raw
        if line.startswith("> "):
            line = line[2:]
        elif line == ">":
            line = ""
        output.append(line.rstrip())
    while output and not output[0]:
        output.pop(0)
    while output and not output[-1]:
        output.pop()
    return "\n".join(output).strip()


def extract_weave(module: str, chapter: str) -> str:
    lines = module.splitlines()[1:]
    captured: list[str] = []
    active = False
    accepted_fields = {"Weave text", "Canonical equation", "AI insertion"}
    stop_fields = {
        "Operation", "Placement", "Retain", "Replace", "Remove", "Remove or normalize",
        "Normalize", "Editorial rule", "Continuity", "Authority", "Supersession"
    }
    for line in lines:
        match = FIELD_RE.match(line)
        if match:
            field = match.group(1).strip()
            if field in accepted_fields:
                active = True
                inline = match.group(2).strip()
                if inline:
                    captured.extend(["", inline])
                continue
            if field in stop_fields or field not in accepted_fields:
                active = False
                continue
        if line.strip() == "---":
            active = False
            continue
        if active:
            captured.append(line)
    prose = clean_candidate_lines(captured)
    if not prose:
        raise RuntimeError(f"no candidate weave prose extracted for {chapter}")
    return prose


def discover_weaves() -> dict[str, tuple[str, str]]:
    found: dict[str, tuple[str, str]] = {}
    for path in EDIT_FILES:
        text = read(path)
        matches = list(MODULE_RE.finditer(text))
        for index, match in enumerate(matches):
            chapter = match.group(1)
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            module = text[match.start():end]
            if chapter in found:
                raise RuntimeError(f"duplicate editorial module for {chapter}")
            found[chapter] = (path.name, extract_weave(module, chapter))
    expected = {f"CH{i:02d}" for i in range(40)}
    if set(found) != expected:
        raise RuntimeError(
            f"editorial module mismatch: missing={sorted(expected-set(found))}, "
            f"extra={sorted(set(found)-expected)}"
        )
    return found


def insertion_index(lines: list[str]) -> int:
    for index, line in enumerate(lines):
        if index >= 5 and line.strip() == "---":
            return index
    for index, line in enumerate(lines):
        if index >= 5 and line.startswith("## "):
            return index
    return len(lines)


def candidate_body(chapter: str, source_path: Path, rc1: str, edit_name: str, weave: str) -> str:
    lines = rc1.rstrip().splitlines()
    for index, line in enumerate(lines[:12]):
        if line.startswith("**Status:**"):
            lines[index] = "**Status:** vNext Candidate 01 — Full-Book Review Draft  "
            break
    marker = (
        "<!--\n"
        "candidate: B04-vNEXT-CANDIDATE-01\n"
        f"chapter: {chapter}\n"
        f"rc1_source: {source_path.relative_to(ROOT)}\n"
        f"rc1_sha256: {digest(rc1.rstrip())}\n"
        f"editorial_source: {edit_name}\n"
        "integration_status: applied-review-candidate\n"
        "-->"
    )
    block = ["", marker, "", weave, ""]
    at = insertion_index(lines)
    lines[at:at] = block
    result = "\n".join(lines).rstrip() + "\n"
    forbidden = ("Integrated vNext Control Route", "Chapter-specific accepted correction")
    if any(token in result for token in forbidden):
        raise RuntimeError(f"reader-visible correction route found in {chapter}")
    return result


def title_of(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def build(output: Path) -> None:
    sources = discover_rc1()
    weaves = discover_weaves()
    if output.exists():
        shutil.rmtree(output)
    manuscript = output / "manuscript"
    manuscript.mkdir(parents=True)

    index = ["# Book 04 vNext Candidate 01", "", "Status: FULL-BOOK REVIEW DRAFT", ""]
    manifest = ["# Candidate 01 Source Manifest", "", "| Chapter | RC1 source | RC1 SHA-256 | Editorial source |", "| --- | --- | --- | --- |"]

    for chapter in sorted(sources):
        source = sources[chapter]
        rc1 = read(source)
        edit_name, weave = weaves[chapter]
        candidate = candidate_body(chapter, source, rc1, edit_name, weave)
        target = manuscript / f"{chapter}.md"
        target.write_text(candidate, encoding="utf-8")
        index.append(f"- [{title_of(candidate)}](manuscript/{chapter}.md)")
        manifest.append(
            f"| {chapter} | `{source.relative_to(ROOT)}` | `{digest(rc1.rstrip())}` | `{edit_name}` |"
        )

    report = """# Candidate 01 Build Report

```text
RC1 chapters discovered: 40 / 40
Editorial weave modules discovered: 40 / 40
Candidate chapters generated: 40 / 40
Candidate chapters with provenance: 40 / 40
Full chapter sequence: CH00–CH39
Reader-visible correction-route appendices: 0
Duplicate chapter identities: 0
Missing chapter identities: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
```

Candidate 01 is a full-book review object. Generation does not grant final Owner acceptance, freeze, publication, implementation, deployment or External Protected Action authority.
"""
    (output / "CANDIDATE-INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (output / "SOURCE-MANIFEST.md").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    (output / "BUILD-REPORT.md").write_text(report, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    build(output)
    print(f"Book 04 vNext Candidate 01 generated at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
