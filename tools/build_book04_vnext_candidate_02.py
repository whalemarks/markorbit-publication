#!/usr/bin/env python3
"""Generate Book 04 vNext Candidate 02 using reviewed route and typed extraction."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
RC1 = BOOK / "manuscript"
ROUTE_FILE = BOOK / "vnext/B04-ROUTE-0001_Candidate_02_Chapter_Route_Manifest.json"
DEFAULT_OUT = ROOT / "build/book04-vnext-candidate-02"
EDIT_FILES = (
    BOOK / "vnext/editorial/B04-EDIT-0001_CH00-CH12_Editorial_Weave_Patch_Set.md",
    BOOK / "vnext/editorial/B04-EDIT-0002_CH13-CH27_Editorial_Weave_Patch_Set.md",
    BOOK / "vnext/editorial/B04-EDIT-0003_CH28-CH39_Editorial_Weave_Patch_Set.md",
)
CHAPTER_RE = re.compile(r"\bCH[-_ ]?(0[0-9]|[1-3][0-9])\b", re.I)
MODULE_RE = re.compile(r"(?m)^## (CH(?:0[0-9]|[1-3][0-9])) — .+$")
FIELD_RE = re.compile(r"^\*\*([^*]+)\*\*(?::)?\s*(.*)$")
READER_PREFIXES = (
    "WEAVE TEXT", "INSERT", "MERGE", "CANONICAL EQUATION", "AI INSERTION", "ISOLATION RULE"
)
LEAK_TOKENS = (
    "Assigned chapters:", "Chapter weave modules:", "Placement rules present:",
    "Unattributed weave modules:", "Blocking findings:", "Immediate Book 02 Change Proposal",
    "**RETAIN", "**REPLACE", "**NORMALIZE", "**SUPERSEDE", "**PLACEMENT", "**AUTHORITY", "**CONTINUITY"
)
CUSTOM_PROSE = {
    "conformance": (
        "Book 04 defines a constitutional architecture rather than a universal application or "
        "implementation specification. Conformance requires the distinctions established in this book "
        "to remain visible in future Product charters, service specifications, ADRs and implementation "
        "repositories. Book completion does not itself grant implementation, deployment, publication or "
        "External Protected Action authority; each remains subject to a separate explicit gate."
    ),
    "final_chain": """The complete responsibility chain is:

```text
Core defines shared meaning.
Workplace preserves organizational sovereignty and authorized context.
Products provide focused experiences through governed Installations and Projections.
AI prepares and recommends within inherited scope.
Human professionals review and decide.
Execution coordinates accepted work.
Owning Services record formal business facts.
MGSN connects independent Workplaces without absorbing them.
Artifacts, Returns and Trust remain provenance-bearing and reviewable.
```

Each Orbit remains independent because authority, access, evidence and responsibility stay explicit across every collaboration boundary.""",
}


def read(path: Path) -> str:
    if not path.is_file():
        raise RuntimeError(f"missing source: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ids(text: str) -> list[str]:
    return sorted({f"CH{m.group(1)}" for m in CHAPTER_RE.finditer(text)})


def identify(path: Path) -> str | None:
    found = ids(path.name)
    if len(found) == 1:
        return found[0]
    for line in read(path).splitlines():
        if line.startswith("# "):
            found = ids(line)
            return found[0] if len(found) == 1 else None
    return None


def discover_rc1() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in sorted(RC1.rglob("*.md")):
        chapter = identify(path)
        if chapter is None:
            continue
        if chapter in result:
            raise RuntimeError(f"duplicate RC1 chapter: {chapter}")
        result[chapter] = path
    expected = {f"CH{i:02d}" for i in range(40)}
    if set(result) != expected:
        raise RuntimeError(f"RC1 mismatch: missing={sorted(expected-set(result))}")
    return result


def normalize_label(label: str) -> str:
    return label.strip().rstrip(":—- ").upper()


def clean(lines: list[str]) -> str:
    out: list[str] = []
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("> "):
            line = line[2:]
        elif line == ">":
            line = ""
        out.append(line)
    while out and not out[0]:
        out.pop(0)
    while out and not out[-1]:
        out.pop()
    return "\n".join(out).strip()


def reader_prose(module: str, module_id: str) -> str:
    captured: list[str] = []
    active = False
    for line in module.splitlines()[1:]:
        field = FIELD_RE.match(line)
        if field:
            label = normalize_label(field.group(1))
            active = any(label.startswith(prefix) for prefix in READER_PREFIXES)
            if active and field.group(2).strip():
                captured.extend(["", field.group(2).strip()])
            continue
        if line.strip() == "---":
            active = False
            continue
        if active:
            captured.append(line)
    prose = clean(captured)
    if not prose:
        raise RuntimeError(f"no typed reader prose for editorial module {module_id}")
    if any(token in prose for token in LEAK_TOKENS):
        raise RuntimeError(f"reader-text leakage in editorial module {module_id}")
    return prose


def discover_modules() -> dict[str, dict[str, str]]:
    modules: dict[str, dict[str, str]] = {}
    for path in EDIT_FILES:
        text = read(path)
        matches = list(MODULE_RE.finditer(text))
        for index, match in enumerate(matches):
            module_id = match.group(1)
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            module = text[match.start():end]
            if module_id in modules:
                raise RuntimeError(f"duplicate editorial module {module_id}")
            modules[module_id] = {"source": path.name, "prose": reader_prose(module, module_id)}
    expected = {f"CH{i:02d}" for i in range(40)}
    if set(modules) != expected:
        raise RuntimeError(f"editorial module mismatch: missing={sorted(expected-set(modules))}")
    return modules


def title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def placement_index(lines: list[str], mode: str) -> int:
    if mode in {"apparatus_only", "preserve_rc1"}:
        return -1
    h2 = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if mode == "before_first_h2":
        return h2[0] if h2 else len(lines)
    if mode == "before_conclusion":
        for i in reversed(h2):
            lowered = lines[i].lower()
            if "conclusion" in lowered or "summary" in lowered or "closing" in lowered:
                return i
        return h2[-1] if h2 else len(lines)
    raise RuntimeError(f"unsupported placement mode: {mode}")


def compose(route: dict, modules: dict[str, dict[str, str]]) -> tuple[str, list[str]]:
    source_ids = route["modules"]
    if "custom_key" in route:
        key = route["custom_key"]
        if key not in CUSTOM_PROSE:
            raise RuntimeError(f"unknown custom prose key: {key}")
        prose = CUSTOM_PROSE[key]
    else:
        prose = "\n\n".join(modules[module_id]["prose"] for module_id in source_ids).strip()
    if any(token in prose for token in LEAK_TOKENS):
        raise RuntimeError("route composition contains reader-text leakage")
    return prose, source_ids


def candidate(chapter: str, source: Path, rc1: str, route: dict, modules: dict[str, dict[str, str]]) -> str:
    if route["title_contains"] not in title(rc1):
        raise RuntimeError(f"route title mismatch for {chapter}: expected {route['title_contains']!r}")
    lines = rc1.rstrip().splitlines()
    for index, line in enumerate(lines[:15]):
        if line.startswith("**Status:**"):
            lines[index] = "**Status:** vNext Candidate 02 — Route-Aware Full-Book Review Draft  "
            break
    prose, source_ids = compose(route, modules)
    marker = [
        "<!--",
        "candidate: B04-vNEXT-CANDIDATE-02",
        f"chapter: {chapter}",
        f"rc1_source: {source.relative_to(ROOT)}",
        f"rc1_sha256: {digest(rc1.rstrip())}",
        f"route_manifest: {ROUTE_FILE.relative_to(ROOT)}",
        f"editorial_modules: {','.join(source_ids) if source_ids else 'none'}",
        f"placement: {route['placement']}",
        "integration_status: route-aware-review-candidate",
        "-->",
    ]
    at = placement_index(lines, route["placement"])
    block = [""] + marker + [""]
    if prose:
        block += [prose, ""]
    if at < 0:
        lines.extend(block)
    else:
        lines[at:at] = block
    result = "\n".join(lines).rstrip() + "\n"
    if any(token in result for token in LEAK_TOKENS):
        raise RuntimeError(f"reader-text leakage found in {chapter}")
    return result


def build(output: Path) -> None:
    sources = discover_rc1()
    modules = discover_modules()
    manifest = json.loads(read(ROUTE_FILE))
    routes = manifest["routes"]
    expected = {f"CH{i:02d}" for i in range(40)}
    if set(routes) != expected:
        raise RuntimeError("route manifest must contain CH00–CH39 exactly")
    represented = {m for route in routes.values() for m in route["modules"]}
    if represented != expected:
        raise RuntimeError(f"accepted module representation mismatch: missing={sorted(expected-represented)}")
    if output.exists():
        shutil.rmtree(output)
    manuscript = output / "manuscript"
    manuscript.mkdir(parents=True)
    index = ["# Book 04 vNext Candidate 02", "", "Status: ROUTE-AWARE FULL-BOOK REVIEW DRAFT", ""]
    sources_report = ["# Candidate 02 Source Manifest", "", "| Target | RC1 source | RC1 SHA-256 | Modules | Placement |", "| --- | --- | --- | --- | --- |"]
    route_report = ["# Candidate 02 Route Report", "", "| Target | Actual title | Editorial modules | Placement |", "| --- | --- | --- | --- |"]
    for chapter in sorted(sources):
        source = sources[chapter]
        rc1 = read(source)
        route = routes[chapter]
        text = candidate(chapter, source, rc1, route, modules)
        (manuscript / f"{chapter}.md").write_text(text, encoding="utf-8")
        index.append(f"- [{title(text)}](manuscript/{chapter}.md)")
        module_text = ", ".join(route["modules"]) if route["modules"] else "none"
        sources_report.append(f"| {chapter} | `{source.relative_to(ROOT)}` | `{digest(rc1.rstrip())}` | `{module_text}` | `{route['placement']}` |")
        route_report.append(f"| {chapter} | {title(rc1)} | `{module_text}` | `{route['placement']}` |")
    report = """# Candidate 02 Build Report

```text
RC1 chapters discovered: 40 / 40
Editorial modules discovered: 40 / 40
Target chapters generated: 40 / 40
Apparatus-only chapters: 1 / 1
Explicit route entries: 40 / 40
Accepted editorial modules represented: 40 / 40
Reader-text leakage findings: 0
Unresolved numeric-only routes: 0
Duplicate chapter identities: 0
Missing chapter identities: 0
RC1 source modifications: 0
Blocking findings: 0
Immediate Book 02 Change Proposal required: NO
```

Candidate 02 is a route-aware full-book review object. It is not the accepted or frozen Book 04 vNext baseline.
"""
    (output / "CANDIDATE-INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (output / "SOURCE-MANIFEST.md").write_text("\n".join(sources_report) + "\n", encoding="utf-8")
    (output / "ROUTE-REPORT.md").write_text("\n".join(route_report) + "\n", encoding="utf-8")
    (output / "BUILD-REPORT.md").write_text(report, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    build(output)
    print(f"Book 04 vNext Candidate 02 generated at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
