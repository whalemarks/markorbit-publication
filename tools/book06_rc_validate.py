#!/usr/bin/env python3
"""Validate and render Book 06 — MarkOrbit Lite for Release Candidate review.

This tool is publication validation infrastructure. It does not define Product
semantics or implementation architecture.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse

import markdown
import yaml
from bs4 import BeautifulSoup
from pypdf import PdfReader
from weasyprint import HTML


CHAPTER_RE = re.compile(r"B06-CH-(\d{2})")
APP_RE = re.compile(r"B06-APP-(\d{4})")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
EXPLICIT_ANCHOR_RE = re.compile(r"<a\s+(?:name|id)=[\"']([^\"']+)[\"']\s*></a>", re.I)
MERMAID_RE = re.compile(r"```mermaid\s*\n(.*?)\n```", re.S)
FENCE_RE = re.compile(r"^\s*```", re.M)
UNRESOLVED_RE = re.compile(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b", re.I)
EXTERNAL_URL_RE = re.compile(r"https?://[^\s)>'\"]+")
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")
CURRENCY_RE = re.compile(r"(?:RMB|CNY|USD|EUR|GBP|SGD|¥|\$|€|£)\s*\d[\d,.]*", re.I)

EXPECTED_CHAPTERS = [f"B06-CH-{i:02d}" for i in range(34)]
EXPECTED_APPS = [f"B06-APP-{i:04d}" for i in range(1, 8)]
EXPECTED_CONTROLLED_IDS = (
    [f"ML-S{i:02d}" for i in range(1, 6)]
    + [f"ML-O{i:02d}" for i in range(1, 9)]
    + [f"ML-W{i:02d}" for i in range(1, 11)]
    + [f"ML-M{i:02d}" for i in range(1, 9)]
    + [f"ML-H{i:02d}" for i in range(1, 9)]
    + [f"ML-E{i:02d}" for i in range(1, 7)]
    + [f"ML-J{i:02d}" for i in range(1, 5)]
    + [f"ML-SCN-{i:02d}" for i in range(1, 25)]
    + [f"ML-HC-{i:02d}" for i in range(1, 9)]
    + [f"ML-AC-{i:02d}" for i in range(1, 13)]
)


@dataclass
class Finding:
    severity: str
    code: str
    path: str
    message: str


@dataclass
class ValidationReport:
    source_commit: str
    book_dir: str
    chapter_files: int = 0
    apparatus_files: int = 0
    markdown_files_scanned: int = 0
    local_links_checked: int = 0
    external_links_found: int = 0
    anchors_checked: int = 0
    mermaid_blocks: int = 0
    mermaid_rendered: int = 0
    pdf_pages: int = 0
    pdf_bytes: int = 0
    pdf_blank_pages: int = 0
    unresolved_markers: int = 0
    controlled_ids_expected: int = 0
    controlled_ids_covered: int = 0
    temporal_markers: int = 0
    currency_markers: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def blocking_count(self) -> int:
        return sum(f.severity == "BLOCKING" for f in self.findings)

    @property
    def major_count(self) -> int:
        return sum(f.severity == "MAJOR" for f in self.findings)

    @property
    def warning_count(self) -> int:
        return sum(f.severity == "WARNING" for f in self.findings)

    @property
    def passed(self) -> bool:
        return self.blocking_count == 0 and self.major_count == 0


def add_finding(report: ValidationReport, severity: str, code: str, path: Path | str, message: str) -> None:
    report.findings.append(Finding(severity, code, str(path), message))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def github_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = html.unescape(text).strip().lower()
    text = re.sub(r"[^\w\-\s]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def anchors_for(text: str) -> set[str]:
    anchors: set[str] = set(EXPLICIT_ANCHOR_RE.findall(text))
    counts: Counter[str] = Counter()
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        base = github_slug(match.group(2))
        if not base:
            continue
        count = counts[base]
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] += 1
    return anchors


def resolve_link(source: Path, target: str) -> tuple[Path, str | None] | None:
    target = target.strip().split(" ")[0].strip("<>")
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https", "mailto", "tel"} or target.startswith("//"):
        return None
    raw_path, sep, fragment = target.partition("#")
    fragment = unquote(fragment) if sep else None
    if not raw_path:
        dest = source
    else:
        dest = (source.parent / unquote(raw_path)).resolve()
    return dest, fragment


def validate_markdown_structure(book_dir: Path, report: ValidationReport) -> tuple[list[Path], list[Path]]:
    manuscript_dir = book_dir / "manuscript"
    apparatus_dir = book_dir / "reader-apparatus"
    chapters = sorted(manuscript_dir.glob("B06-CH-*.md"))
    apps = sorted(apparatus_dir.glob("B06-APP-*.md"))
    report.chapter_files = len(chapters)
    report.apparatus_files = len(apps)

    chapter_ids = []
    for path in chapters:
        match = CHAPTER_RE.search(path.name)
        if match:
            chapter_ids.append(f"B06-CH-{match.group(1)}")
    if chapter_ids != EXPECTED_CHAPTERS:
        add_finding(report, "BLOCKING", "CHAPTER_SEQUENCE", manuscript_dir, f"Expected {EXPECTED_CHAPTERS}; found {chapter_ids}")

    app_ids = []
    for path in apps:
        match = APP_RE.search(path.name)
        if match:
            app_ids.append(f"B06-APP-{match.group(1)}")
    if app_ids != EXPECTED_APPS:
        add_finding(report, "MAJOR", "APPARATUS_SEQUENCE", apparatus_dir, f"Expected {EXPECTED_APPS}; found {app_ids}")

    for path in chapters:
        text = read_text(path)
        first_heading = next((line for line in text.splitlines() if line.startswith("# ")), "")
        expected = CHAPTER_RE.search(path.name)
        if expected and f"B06-CH-{expected.group(1)}" not in first_heading:
            add_finding(report, "BLOCKING", "CHAPTER_HEADING", path, "First H1 does not contain the filename chapter ID")
        for required in ("**Status:** Complete Draft 1", "**Chapter Map:** B06-TOC-V0.1", "**Part:**"):
            if required not in text[:1500]:
                add_finding(report, "MAJOR", "CHAPTER_METADATA", path, f"Missing normalized metadata: {required}")

    return chapters, apps


def validate_fences_and_markers(paths: Iterable[Path], report: ValidationReport) -> None:
    for path in paths:
        text = read_text(path)
        if len(FENCE_RE.findall(text)) % 2:
            add_finding(report, "BLOCKING", "UNBALANCED_FENCE", path, "Odd number of triple-backtick fences")
        markers = UNRESOLVED_RE.findall(text)
        if markers:
            report.unresolved_markers += len(markers)
            add_finding(report, "MAJOR", "UNRESOLVED_MARKER", path, f"Found unresolved markers: {sorted(set(markers))}")
        for forbidden in ("Owner Accepted on Wave", "Controlled Drafting Waves", "Chapter status:", "## Chapter Role"):
            if forbidden in text:
                add_finding(report, "MAJOR", "INTERNAL_PROCESS_TEXT", path, f"Reader-facing internal process wording remains: {forbidden}")


def validate_yaml(book_dir: Path, report: ValidationReport) -> None:
    yaml_paths = [book_dir / "publication.yaml", book_dir / "release" / "book06-assembly.yaml"]
    for path in yaml_paths:
        if not path.exists():
            add_finding(report, "BLOCKING", "MISSING_YAML", path, "Required YAML file is missing")
            continue
        try:
            yaml.safe_load(read_text(path))
        except Exception as exc:  # noqa: BLE001
            add_finding(report, "BLOCKING", "YAML_PARSE", path, str(exc))


def validate_links(book_dir: Path, paths: Iterable[Path], report: ValidationReport) -> None:
    anchor_cache: dict[Path, set[str]] = {}
    root = book_dir.resolve()
    for path in paths:
        text = read_text(path)
        for _, target in LINK_RE.findall(text) + IMAGE_LINK_RE.findall(text):
            if target.startswith(("http://", "https://")):
                report.external_links_found += 1
                continue
            resolved = resolve_link(path, target)
            if resolved is None:
                continue
            dest, fragment = resolved
            report.local_links_checked += 1
            try:
                dest.relative_to(root.parent.parent.resolve())
            except ValueError:
                add_finding(report, "MAJOR", "LINK_OUTSIDE_REPO", path, f"Link escapes repository scope: {target}")
                continue
            if not dest.exists():
                add_finding(report, "MAJOR", "BROKEN_LINK", path, f"Missing local target: {target}")
                continue
            if fragment and dest.suffix.lower() == ".md":
                report.anchors_checked += 1
                anchors = anchor_cache.setdefault(dest, anchors_for(read_text(dest)))
                if fragment not in anchors:
                    add_finding(report, "MAJOR", "BROKEN_ANCHOR", path, f"Missing anchor #{fragment} in {dest}")


def validate_controlled_coverage(book_dir: Path, report: ValidationReport) -> None:
    coverage_text = read_text(book_dir / "reader-apparatus" / "B06-APP-0005_Controlled_Record_Coverage.md")
    coverage_text += "\n" + read_text(book_dir / "reader-apparatus" / "B06-APP-0006_Journey_Scenario_Handoff_and_Acceptance_Coverage.md")
    report.controlled_ids_expected = len(EXPECTED_CONTROLLED_IDS)
    missing = [record_id for record_id in EXPECTED_CONTROLLED_IDS if record_id not in coverage_text]
    report.controlled_ids_covered = report.controlled_ids_expected - len(missing)
    if missing:
        add_finding(report, "BLOCKING", "CONTROLLED_COVERAGE", book_dir / "reader-apparatus", f"Missing controlled IDs: {missing}")


def source_inventory(paths: Iterable[Path], report: ValidationReport) -> dict[str, object]:
    external_urls: set[str] = set()
    years: list[dict[str, str]] = []
    currencies: list[dict[str, str]] = []
    for path in paths:
        text = read_text(path)
        for url in EXTERNAL_URL_RE.findall(text):
            external_urls.add(url.rstrip(".,;"))
        for match in YEAR_RE.finditer(text):
            years.append({"path": str(path), "value": match.group(0)})
        for match in CURRENCY_RE.finditer(text):
            currencies.append({"path": str(path), "value": match.group(0)})
    report.external_links_found = max(report.external_links_found, len(external_urls))
    report.temporal_markers = len(years)
    report.currency_markers = len(currencies)
    return {
        "external_urls": sorted(external_urls),
        "domains": sorted({urlparse(url).netloc for url in external_urls}),
        "temporal_markers": years,
        "currency_markers": currencies,
        "policy": {
            "architecture_claims": "repository-authoritative",
            "jurisdiction_specific_legal_claims": "must be sourced, dated and framed as non-advice",
            "commercial_hypotheses": "must remain labeled experiments",
            "provider_or_tool_claims": "must not define Product identity",
        },
    }


def render_mermaid(source_text: str, output_dir: Path, report: ValidationReport) -> tuple[str, list[Path]]:
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    rendered: list[Path] = []
    counter = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal counter
        counter += 1
        code = match.group(1).strip() + "\n"
        mmd_path = figures_dir / f"figure-{counter:02d}.mmd"
        svg_path = figures_dir / f"figure-{counter:02d}.svg"
        mmd_path.write_text(code, encoding="utf-8")
        cmd = ["mmdc", "-i", str(mmd_path), "-o", str(svg_path), "-b", "transparent"]
        puppeteer = os.environ.get("MERMAID_PUPPETEER_CONFIG")
        if puppeteer:
            cmd.extend(["-p", puppeteer])
        proc = subprocess.run(cmd, text=True, capture_output=True)
        if proc.returncode != 0:
            add_finding(report, "BLOCKING", "MERMAID_RENDER", mmd_path, proc.stderr.strip() or proc.stdout.strip())
            return f"\n```text\nMermaid rendering failed for figure {counter:02d}\n```\n"
        rendered.append(svg_path)
        return f'\n<figure class="semantic-figure"><img src="figures/{svg_path.name}" alt="Semantic figure {counter:02d}"><figcaption>Semantic figure {counter:02d}</figcaption></figure>\n'

    replaced = MERMAID_RE.sub(replace, source_text)
    report.mermaid_blocks += counter
    report.mermaid_rendered += len(rendered)
    return replaced, rendered


def strip_leading_h1(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[:index] + ["# " + line[2:]] + lines[index + 1 :])
    return text


def assemble_book(book_dir: Path, chapters: list[Path], apps: list[Path], output_dir: Path, report: ValidationReport) -> tuple[Path, Path, Path, list[Path]]:
    parts = [
        "# Book 06 — MarkOrbit Lite\n\n",
        "**Release Candidate validation assembly**  \n",
        f"**Source commit:** `{report.source_commit}`  \n",
        "**Authority:** Product Charter v0.3 → Product Baseline v0.1 → B06-TOC-V0.1 → chapter prose → Reader Apparatus\n\n",
        "---\n\n",
    ]
    for path in chapters:
        parts.append(strip_leading_h1(read_text(path)))
        parts.append("\n\n<div class=\"page-break\"></div>\n\n")
    parts.append("# Reader Apparatus\n\n")
    for path in apps:
        parts.append(strip_leading_h1(read_text(path)))
        parts.append("\n\n<div class=\"page-break\"></div>\n\n")

    combined = "".join(parts)
    combined, rendered = render_mermaid(combined, output_dir, report)
    md_path = output_dir / "Book-06-MarkOrbit-Lite-RC-Validation.md"
    md_path.write_text(combined, encoding="utf-8")

    body = markdown.markdown(
        combined,
        extensions=["extra", "tables", "fenced_code", "toc", "attr_list", "md_in_html"],
        output_format="html5",
    )
    css = """
    @page { size: A4; margin: 18mm 16mm 20mm; @bottom-center { content: counter(page); font-size: 8pt; color: #666; } }
    body { font-family: 'DejaVu Sans', sans-serif; font-size: 10.2pt; line-height: 1.48; color: #171717; }
    h1 { font-size: 22pt; page-break-before: always; margin-top: 0; }
    body > h1:first-child { page-break-before: avoid; }
    h2 { font-size: 15pt; margin-top: 1.4em; page-break-after: avoid; }
    h3 { font-size: 12pt; page-break-after: avoid; }
    table { width: 100%; border-collapse: collapse; font-size: 8pt; margin: 0.8em 0; }
    th, td { border: 0.4pt solid #aaa; padding: 4px; vertical-align: top; overflow-wrap: anywhere; }
    thead { display: table-header-group; }
    tr { page-break-inside: avoid; }
    pre { white-space: pre-wrap; overflow-wrap: anywhere; font-family: 'DejaVu Sans Mono', monospace; font-size: 8.2pt; background: #f4f4f4; padding: 8px; }
    code { font-family: 'DejaVu Sans Mono', monospace; font-size: 0.92em; }
    blockquote { border-left: 3px solid #777; padding-left: 10px; color: #444; }
    .page-break { page-break-after: always; }
    .semantic-figure { page-break-inside: avoid; text-align: center; margin: 1em 0; }
    .semantic-figure img { max-width: 100%; max-height: 235mm; }
    figcaption { color: #555; font-size: 8pt; }
    a { color: #1f4b7a; text-decoration: none; }
    """
    html_doc = f"<!doctype html><html><head><meta charset='utf-8'><title>Book 06 — MarkOrbit Lite</title><style>{css}</style></head><body>{body}</body></html>"
    html_path = output_dir / "Book-06-MarkOrbit-Lite-RC-Validation.html"
    html_path.write_text(html_doc, encoding="utf-8")

    soup = BeautifulSoup(html_doc, "html.parser")
    if not soup.find("h1"):
        add_finding(report, "BLOCKING", "HTML_STRUCTURE", html_path, "No H1 found in assembled HTML")

    pdf_path = output_dir / "Book-06-MarkOrbit-Lite-RC-Validation.pdf"
    HTML(string=html_doc, base_url=str(output_dir)).write_pdf(str(pdf_path))
    return md_path, html_path, pdf_path, rendered


def validate_pdf(pdf_path: Path, report: ValidationReport) -> None:
    if not pdf_path.exists():
        add_finding(report, "BLOCKING", "PDF_MISSING", pdf_path, "PDF was not generated")
        return
    report.pdf_bytes = pdf_path.stat().st_size
    if report.pdf_bytes < 200_000:
        add_finding(report, "MAJOR", "PDF_SIZE", pdf_path, f"PDF unexpectedly small: {report.pdf_bytes} bytes")
    reader = PdfReader(str(pdf_path))
    report.pdf_pages = len(reader.pages)
    if report.pdf_pages < 80:
        add_finding(report, "MAJOR", "PDF_PAGE_COUNT", pdf_path, f"PDF unexpectedly short: {report.pdf_pages} pages")
    text_samples: list[str] = []
    blank = 0
    for page in reader.pages:
        text = page.extract_text() or ""
        if len(text.strip()) < 10:
            blank += 1
        text_samples.append(text)
    report.pdf_blank_pages = blank
    if blank > 3:
        add_finding(report, "MAJOR", "PDF_BLANK_PAGES", pdf_path, f"Found {blank} near-blank pages")
    full_text = "\n".join(text_samples)
    required = [
        "B06-CH-00",
        "B06-CH-33",
        "Controlled Term Glossary",
        "Core Distinction Matrix",
        "Subject Index",
    ]
    for token in required:
        if token not in full_text:
            add_finding(report, "MAJOR", "PDF_TEXT", pdf_path, f"Required text missing from PDF extraction: {token}")


def write_checksums(output_dir: Path) -> Path:
    entries = []
    for path in sorted(output_dir.rglob("*")):
        if not path.is_file() or path.name == "SHA256SUMS.txt":
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        entries.append(f"{digest}  {path.relative_to(output_dir)}")
    checksum_path = output_dir / "SHA256SUMS.txt"
    checksum_path.write_text("\n".join(entries) + "\n", encoding="utf-8")
    return checksum_path


def write_reports(output_dir: Path, report: ValidationReport, inventory: dict[str, object]) -> None:
    payload = asdict(report)
    payload["passed"] = report.passed
    payload["blocking_count"] = report.blocking_count
    payload["major_count"] = report.major_count
    payload["warning_count"] = report.warning_count
    payload["source_inventory"] = inventory
    (output_dir / "validation-report.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Book 06 RC Validation Report",
        "",
        f"- **Source commit:** `{report.source_commit}`",
        f"- **Decision:** {'PASS' if report.passed else 'FAIL'}",
        f"- **Blocking findings:** {report.blocking_count}",
        f"- **Major findings:** {report.major_count}",
        f"- **Warnings:** {report.warning_count}",
        "",
        "## Coverage",
        "",
        f"- Chapter files: {report.chapter_files} / 34",
        f"- Reader Apparatus files: {report.apparatus_files} / 7",
        f"- Local links checked: {report.local_links_checked}",
        f"- Anchors checked: {report.anchors_checked}",
        f"- Controlled IDs covered: {report.controlled_ids_covered} / {report.controlled_ids_expected}",
        f"- Mermaid figures rendered: {report.mermaid_rendered} / {report.mermaid_blocks}",
        f"- PDF pages: {report.pdf_pages}",
        f"- PDF bytes: {report.pdf_bytes}",
        f"- Near-blank PDF pages: {report.pdf_blank_pages}",
        f"- External URLs found: {len(inventory['external_urls'])}",
        f"- Temporal markers reviewed: {report.temporal_markers}",
        f"- Currency markers reviewed: {report.currency_markers}",
        "",
        "## Findings",
        "",
    ]
    if report.findings:
        for finding in report.findings:
            lines.append(f"- **{finding.severity} {finding.code}** — `{finding.path}` — {finding.message}")
    else:
        lines.append("No blocking, major or warning findings.")
    lines.extend([
        "",
        "## Publication boundary",
        "",
        "This report validates publication inputs and rendered output. It does not authorize Product implementation, production, external protected action or public/commercial distribution.",
    ])
    (output_dir / "validation-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-commit", default=os.environ.get("GITHUB_SHA", "unknown"))
    args = parser.parse_args()

    book_dir = args.book_dir.resolve()
    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    report = ValidationReport(source_commit=args.source_commit, book_dir=str(book_dir))
    chapters, apps = validate_markdown_structure(book_dir, report)
    validation_paths = sorted(book_dir.rglob("*.md"))
    report.markdown_files_scanned = len(validation_paths)
    validate_fences_and_markers(chapters + apps, report)
    validate_yaml(book_dir, report)
    validate_links(book_dir, validation_paths, report)
    validate_controlled_coverage(book_dir, report)
    inventory = source_inventory(chapters + apps, report)

    _, _, pdf_path, _ = assemble_book(book_dir, chapters, apps, output_dir, report)
    validate_pdf(pdf_path, report)
    write_reports(output_dir, report, inventory)
    write_checksums(output_dir)

    print(json.dumps({
        "passed": report.passed,
        "blocking": report.blocking_count,
        "major": report.major_count,
        "warnings": report.warning_count,
        "pdf_pages": report.pdf_pages,
        "mermaid": f"{report.mermaid_rendered}/{report.mermaid_blocks}",
    }, indent=2))
    return 0 if report.passed else 1


if __name__ == "__main__":
    sys.exit(main())
