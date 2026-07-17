#!/usr/bin/env python3
"""Build Book 04 vNext Candidate 01 without mutating RC1."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "books/book-04-workplace-product-architecture"
RC1 = BOOK / "manuscript"
DEFAULT_OUT = BOOK / "vnext/candidate-01"

AMENDMENTS = {
    "WP-B": (
        BOOK / "vnext/manuscript/B04-VNEXT-WPB-0001_Workplace_Authority_and_Data_Boundaries.md",
        BOOK / "vnext/B04-CORR-0001_WP-B_Chapter_Correction_Ledger.md",
    ),
    "WP-C": (
        BOOK / "vnext/manuscript/B04-VNEXT-WPC-0001_Product_Installation_and_Projection_Model.md",
        BOOK / "vnext/B04-CORR-0002_WP-C_Chapter_Correction_Ledger.md",
    ),
    "WP-D": (
        BOOK / "vnext/manuscript/B04-VNEXT-WPD-0001_Product_and_Network_Interface_Model.md",
        BOOK / "vnext/B04-CORR-0003_WP-D_Chapter_Correction_Ledger.md",
    ),
    "WP-E": (
        BOOK / "vnext/manuscript/B04-VNEXT-WPE-0001_Cross_Workplace_Collaboration_and_Portability.md",
        BOOK / "vnext/B04-CORR-0004_WP-E_Chapter_Correction_Ledger.md",
    ),
}

CANONICAL_CHAPTER_RE = re.compile(r"\bCH(?:0[0-9]|[1-3][0-9])\b")
HISTORICAL_CHAPTER_RE = re.compile(r"\bCH[-_ ]?(0[0-9]|[1-3][0-9])\b", re.IGNORECASE)
HEADING_RE = re.compile(r"(?m)^(#{1,6})\s+.*?\b(CH(?:0[0-9]|[1-3][0-9]))\b.*$")


def read(path: Path) -> str:
    if not path.is_file():
        raise RuntimeError(f"missing source: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def normalized_chapters(text: str) -> list[str]:
    """Normalize both CH00 and historical CH-00/CH_00/CH 00 identifiers."""
    return sorted({f"CH{match.group(1)}" for match in HISTORICAL_CHAPTER_RE.finditer(text)})


def identify_rc1_chapter(path: Path) -> str | None:
    filename_ids = normalized_chapters(path.name)
    if len(filename_ids) == 1:
        return filename_ids[0]
    if len(filename_ids) > 1:
        raise RuntimeError(f"ambiguous chapter identifiers in filename: {path.relative_to(ROOT)}")

    # Historical manuscript files are allowed to carry the identifier only in
    # their opening heading. Restrict inspection to the front matter so body
    # cross-references cannot create false duplicate identities.
    opening = "\n".join(read(path).splitlines()[:20])
    heading_ids = normalized_chapters(opening)
    if len(heading_ids) == 1:
        return heading_ids[0]
    if len(heading_ids) > 1:
        raise RuntimeError(f"ambiguous chapter identifiers in opening heading: {path.relative_to(ROOT)}")
    return None


def discover_rc1() -> dict[str, Path]:
    found: dict[str, Path] = {}
    for path in sorted(RC1.rglob("*.md")):
        chapter = identify_rc1_chapter(path)
        if chapter is None:
            continue
        if chapter in found:
            raise RuntimeError(f"duplicate RC1 source for {chapter}: {found[chapter]} and {path}")
        found[chapter] = path
    expected = {f"CH{i:02d}" for i in range(40)}
    missing = sorted(expected - set(found))
    extra = sorted(set(found) - expected)
    if missing or extra:
        raise RuntimeError(f"RC1 discovery mismatch: missing={missing}, extra={extra}")
    return found


def extract_module(text: str, chapter: str) -> str:
    matches = list(HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        if match.group(2) != chapter:
            continue
        level = len(match.group(1))
        end = len(text)
        for later in matches[index + 1 :]:
            if len(later.group(1)) <= level:
                end = later.start()
                break
        return text[match.start():end].strip()
    raise RuntimeError(f"amendment ledger routes {chapter}, but no chapter module was found")


def routes() -> dict[str, list[tuple[str, str, str]]]:
    result: dict[str, list[tuple[str, str, str]]] = {f"CH{i:02d}": [] for i in range(40)}
    for package, (amendment_path, ledger_path) in AMENDMENTS.items():
        amendment = read(amendment_path)
        ledger = read(ledger_path)
        chapter_ids = sorted(set(CANONICAL_CHAPTER_RE.findall(ledger)))
        for chapter in chapter_ids:
            module = extract_module(amendment, chapter)
            result[chapter].append((package, amendment_path.name, module))
    return result


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build(output: Path) -> None:
    sources = discover_rc1()
    chapter_routes = routes()
    if output.exists():
        shutil.rmtree(output)
    manuscript = output / "manuscript"
    manuscript.mkdir(parents=True)

    index_lines = ["# Book 04 vNext Candidate 01", "", "Status: GENERATED REVIEW CANDIDATE", ""]
    report = ["# Candidate Build Report", "", "```text"]
    routed_count = 0

    for chapter in sorted(sources):
        source_path = sources[chapter]
        body = read(source_path).rstrip()
        controls = chapter_routes[chapter]
        header = (
            "<!--\n"
            f"candidate: B04-vNEXT-CANDIDATE-01\nchapter: {chapter}\n"
            f"rc1_source: {source_path.relative_to(ROOT)}\nrc1_sha256: {digest(body)}\n"
            f"amendment_routes: {', '.join(p for p, _, _ in controls) or 'none'}\n"
            "status: generated-review-candidate\n-->\n\n"
        )
        sections: list[str] = []
        for package, filename, module in controls:
            routed_count += 1
            sections.append(
                "\n\n---\n\n"
                f"## Integrated vNext Control — {package}\n\n"
                f"Source: `{filename}`\n\n{module}\n"
            )
        candidate = header + body + "".join(sections) + "\n"
        target = manuscript / f"{chapter}.md"
        target.write_text(candidate, encoding="utf-8")
        index_lines.append(f"- [{chapter}](manuscript/{chapter}.md)")

    report.extend(
        [
            "RC1 chapters discovered: 40 / 40",
            "Candidate chapters generated: 40 / 40",
            "Accepted amendments registered: 4 / 4",
            f"Routed control modules generated: {routed_count}",
            "Duplicate chapter identities: 0",
            "Missing chapter identities: 0",
            "Unattributed inserted controls: 0",
            "RC1 mutations: 0",
            "```",
            "",
            "Generation does not grant Owner acceptance, freeze or publication authority.",
        ]
    )
    (output / "CANDIDATE-INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    (output / "BUILD-REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    build(output)
    print(f"Book 04 vNext candidate generated at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
