#!/usr/bin/env python3
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
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

import markdown
import yaml
from pypdf import PdfReader
from weasyprint import HTML

SCRIPT = Path(__file__).resolve()
BOOK = SCRIPT.parents[1]
REPO = BOOK.parents[1]
BUILD = BOOK / "build" / "pf08"
RENDERED = BUILD / "figures"

EXPECTED_MANUSCRIPTS = set(range(48))
EXPECTED_APPENDICES = set("ABCDEFG")
EXPECTED_FIGURES = {1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12}
EXPECTED_RANGES = {
    "CR": (1, 8), "A": (1, 30), "C": (1, 12), "D": (1, 13),
    "E": (1, 9), "B": (1, 4), "V": (1, 5), "G": (1, 10), "SCN": (1, 41),
}

@dataclass
class Check:
    name: str
    status: str
    detail: str

CHECKS: list[Check] = []
ERRORS: list[str] = []
WARNINGS: list[str] = []


def record(name: str, ok: bool, detail: str, *, warning: bool = False) -> None:
    status = "PASS" if ok else ("WARN" if warning else "FAIL")
    CHECKS.append(Check(name, status, detail))
    if not ok:
        (WARNINGS if warning else ERRORS).append(f"{name}: {detail}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def slugify(value: str) -> str:
    value = re.sub(r"[`*_~]", "", value.strip().lower())
    value = re.sub(r"[^\w\-\s]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s\-]+", "-", value).strip("-")
    return value


def iter_headings(text: str):
    in_fence = False
    marker = ""
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            char = fence.group(1)[0]
            if not in_fence:
                in_fence, marker = True, char
            elif marker == char:
                in_fence, marker = False, ""
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            yield len(m.group(1)), m.group(2)


def headings(text: str) -> set[str]:
    return {slugify(title) for _, title in iter_headings(text)}


def markdown_files() -> list[Path]:
    return sorted(p for p in BOOK.rglob("*.md") if "build" not in p.parts)


def check_inventory() -> None:
    manuscripts = sorted((BOOK / "manuscript").glob("B05-CH-*.md"))
    nums: list[int] = []
    for p in manuscripts:
        m = re.match(r"B05-CH-(\d{2})_", p.name)
        if m:
            nums.append(int(m.group(1)))
    record("manuscript inventory", set(nums) == EXPECTED_MANUSCRIPTS and len(nums) == 48,
           f"found {len(nums)} files; range={min(nums) if nums else None}-{max(nums) if nums else None}")

    for p in manuscripts:
        num = int(re.match(r"B05-CH-(\d{2})_", p.name).group(1))
        text = read(p)
        title_ok = first_heading(text).startswith(f"B05-CH-{num:02d}")
        metadata_ok = "**Status:** Complete Draft 1" in text and ("**Chapter Map:** B05-TOC-V0.1 — Owner Accepted" in text or "**Chapter Map ID:** B05-TOC-V0.1 — Owner Accepted" in text)
        record(f"chapter {num:02d} heading", title_ok, first_heading(text) or "missing heading")
        record(f"chapter {num:02d} metadata", metadata_ok, "required status and chapter-map metadata present" if metadata_ok else "missing required metadata")

    apps = sorted((BOOK / "appendices").glob("B05-APP-*.md"))
    letters = {m.group(1) for p in apps if (m := re.match(r"B05-APP-([A-G])_", p.name))}
    record("appendix inventory", letters == EXPECTED_APPENDICES, f"found {sorted(letters)}")

    specs = sorted((BOOK / "specifications").glob("B05-SPEC-*.md"))
    spec_ids = {m.group(1) for p in specs if (m := re.match(r"B05-SPEC-(\d{4})_", p.name))}
    record("specification inventory", spec_ids == {"0001", "0002", "0003", "0004"}, f"found {sorted(spec_ids)}")

    figs = sorted((BOOK / "figures").glob("B05-FIG-*.md"))
    fig_nums = {int(m.group(1)) for p in figs if (m := re.match(r"B05-FIG-(\d{2})_", p.name))}
    record("figure source inventory", fig_nums == EXPECTED_FIGURES, f"found {sorted(fig_nums)}; FIG-05 must be merged")
    record("FIG-05 source absent", not any((BOOK / "figures").glob("B05-FIG-05_*.md")), "FIG-05 merged into FIG-03")


def check_markdown_structure() -> None:
    link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for p in markdown_files():
        text = read(p)
        # Fence balance.
        stack: list[str] = []
        for line_no, line in enumerate(text.splitlines(), 1):
            m = re.match(r"^\s*(`{3,}|~{3,})", line)
            if not m:
                continue
            marker = m.group(1)[0]
            if stack and stack[-1] == marker:
                stack.pop()
            elif not stack:
                stack.append(marker)
            else:
                stack.append(marker)
        record(f"fences {p.relative_to(BOOK)}", not stack, "balanced" if not stack else f"unclosed marker(s): {stack}")

        # Duplicate headings.
        seen_paths: set[tuple[str, ...]] = set()
        duplicates: set[str] = set()
        parents: dict[int, str] = {}
        for level, title in iter_headings(text):
            parents[level] = slugify(title)
            for deeper in range(level + 1, 7):
                parents.pop(deeper, None)
            path_key = tuple(parents[i] for i in sorted(parents) if i <= level)
            if path_key in seen_paths:
                duplicates.add(" / ".join(path_key))
            seen_paths.add(path_key)
        record(f"headings {p.relative_to(BOOK)}", not duplicates, "hierarchical paths unique" if not duplicates else f"duplicates: {sorted(duplicates)}")

        # Relative links and fragments.
        for target in link_re.findall(text):
            target = target.strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if target.startswith("#"):
                anchor = target[1:]
                record(f"anchor {p.relative_to(BOOK)}#{anchor}", anchor in headings(text), "resolved" if anchor in headings(text) else "missing local heading")
                continue
            raw_path, _, fragment = target.partition("#")
            raw_path = unquote(raw_path)
            dest = (p.parent / raw_path).resolve()
            try:
                dest.relative_to(REPO.resolve())
            except ValueError:
                record(f"link {p.relative_to(BOOK)} -> {target}", False, "escapes repository")
                continue
            exists = dest.exists()
            record(f"link {p.relative_to(BOOK)} -> {raw_path}", exists, "resolved" if exists else "missing file")
            if exists and fragment and dest.suffix.lower() == ".md":
                anchor_ok = fragment in headings(read(dest))
                record(f"fragment {p.relative_to(BOOK)} -> {target}", anchor_ok, "resolved" if anchor_ok else "missing target heading")


def check_controlled_ids() -> None:
    corpus = "\n".join(read(p) for p in markdown_files())
    invalid: list[str] = []
    found_by_kind: dict[str, set[int]] = {k: set() for k in EXPECTED_RANGES}
    matches = []
    matches.extend((kind, number) for kind, number in re.findall(r"\bMR-(CR|SCN)-(\d{2})\b", corpus))
    matches.extend((kind, number) for kind, number in re.findall(r"\bMR-(A|C|D|E|B|V|G)(\d{2})\b", corpus))
    for kind, number in matches:
        n = int(number)
        lo, hi = EXPECTED_RANGES[kind]
        if not (lo <= n <= hi):
            invalid.append(f"MR-{kind}{number}")
        else:
            found_by_kind[kind].add(n)
    record("controlled ID ranges", not invalid, "all MR IDs are in range" if not invalid else f"invalid: {sorted(set(invalid))}")
    for kind, (lo, hi) in EXPECTED_RANGES.items():
        missing = set(range(lo, hi + 1)) - found_by_kind[kind]
        record(f"controlled ID coverage MR-{kind}", not missing, "complete" if not missing else f"missing {sorted(missing)}")

    for prefix, hi in (("EL", 40), ("RK", 18)):
        found = {int(x) for x in re.findall(rf"\b{prefix}-(\d{{2}})\b", corpus)}
        bad = {x for x in found if not (1 <= x <= hi)}
        missing = set(range(1, hi + 1)) - found
        record(f"{prefix} range", not bad, "all in range" if not bad else f"invalid {sorted(bad)}")
        record(f"{prefix} coverage", not missing, "complete" if not missing else f"missing {sorted(missing)}")


def check_figures_source() -> list[Path]:
    figures = sorted((BOOK / "figures").glob("B05-FIG-*.md"))
    for p in figures:
        text = read(p)
        mermaids = re.findall(r"```mermaid\s*\n(.*?)\n```", text, re.S)
        record(f"Mermaid block {p.name}", len(mermaids) == 1, f"found {len(mermaids)}")
        low = text.lower()
        for label, tokens in {
            "caption": ["caption"], "sources": ["source"], "accessibility": ["accessibility"],
            "grayscale": ["grayscale", "greyscale"],
        }.items():
            ok = any(t in low for t in tokens)
            record(f"figure {label} {p.name}", ok, "present" if ok else "missing")
        authority_ok = "authority" in low and "boundary" in low
        record(f"figure authority {p.name}", authority_ok, "authority boundary expressed" if authority_ok else "missing")
    register = read(BOOK / "publication" / "B05-PUB-0005_Figure_Register.md")
    for i in range(1, 13):
        record(f"figure disposition B05-FIG-{i:02d}", f"B05-FIG-{i:02d}" in register, "registered" if f"B05-FIG-{i:02d}" in register else "missing")
    record("FIG-05 merged disposition", "MERGED" in register.upper() and "B05-FIG-03" in register, "merged into FIG-03")
    return figures


def check_yaml_state() -> None:
    data = yaml.safe_load(read(BOOK / "publication.yaml"))
    record("YAML manuscript count", data.get("chapter_map", {}).get("manuscript_files") == 48, str(data.get("chapter_map", {}).get("manuscript_files")))
    apparatus = data.get("publication_apparatus", {})
    figures = data.get("figures", {})
    record("YAML figure planned count", figures.get("planned_identities") == 12, str(figures.get("planned_identities")))
    record("YAML figure retained count", figures.get("retained_sources") == 11, str(figures.get("retained_sources")))
    record("YAML PF-08 phase", "pf_08" in str(data.get("phase", "")), str(data.get("phase")))
    progress = data.get("publication_finishing_pack", {}).get("progress", {})
    record("YAML PF-07 complete", progress.get("pf_07_figures_and_apparatus") == "complete", str(progress.get("pf_07_figures_and_apparatus")))


def extract_mermaid(text: str) -> str:
    m = re.search(r"```mermaid\s*\n(.*?)\n```", text, re.S)
    if not m:
        raise ValueError("missing Mermaid block")
    return m.group(1).strip() + "\n"


def run_command(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def render_figures(figures: list[Path]) -> dict[str, Path]:
    BUILD.mkdir(parents=True, exist_ok=True)
    RENDERED.mkdir(parents=True, exist_ok=True)
    mmdc = shutil.which("mmdc")
    if not mmdc:
        candidate = REPO / "node_modules" / ".bin" / "mmdc"
        if candidate.exists():
            mmdc = str(candidate)
    record("Mermaid CLI available", bool(mmdc), mmdc or "mmdc not found")
    if not mmdc:
        return {}

    config = BOOK / "validation" / "mermaid-config.json"
    puppeteer = BOOK / "validation" / "puppeteer-config.json"
    rendered: dict[str, Path] = {}
    for p in figures:
        fig_id = re.match(r"(B05-FIG-\d{2})_", p.name).group(1)
        source = BUILD / f"{fig_id}.mmd"
        svg = RENDERED / f"{fig_id}.svg"
        source.write_text(extract_mermaid(read(p)), encoding="utf-8")
        cp = run_command([mmdc, "-i", str(source), "-o", str(svg), "-c", str(config), "-p", str(puppeteer), "-b", "transparent"])
        ok = cp.returncode == 0 and svg.exists() and svg.stat().st_size > 500 and "<svg" in read(svg)[:1000]
        record(f"render {fig_id}", ok, f"{svg.name}, {svg.stat().st_size if svg.exists() else 0} bytes" if ok else cp.stdout[-1000:])
        if ok:
            rendered[fig_id] = svg
            colors = set(re.findall(r"#[0-9a-fA-F]{6}\b", read(svg)))
            non_gray = []
            for c in colors:
                r, g, b = int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)
                if not (r == g == b):
                    non_gray.append(c)
            record(f"grayscale {fig_id}", not non_gray, "all explicit RGB colors grayscale" if not non_gray else f"non-gray colors {sorted(non_gray)}")
    return rendered


def reader_sources() -> list[Path]:
    docs: list[Path] = []
    docs.extend(sorted((BOOK / "manuscript").glob("B05-CH-*.md")))
    docs.extend(sorted((BOOK / "appendices").glob("B05-APP-*.md")))
    pub = BOOK / "publication"
    docs.extend([
        pub / "B05-PUB-0002_Source_and_Authority_Notes.md",
        pub / "B05-PUB-0003_Glossary.md",
        pub / "B05-PUB-0004_Subject_Index.md",
        pub / "B05-PUB-0005_Figure_Register.md",
    ])
    return docs


def strip_metadata(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        if re.match(r"^\*\*(Status|Chapter Map|Part):\*\*", line):
            continue
        out.append(line)
    return "\n".join(out)


def build_reader(rendered: dict[str, Path]) -> tuple[Path, Path]:
    css = read(BOOK / "validation" / "reader.css")
    sections: list[str] = []
    toc: list[str] = []
    for idx, p in enumerate(reader_sources(), 1):
        text = strip_metadata(read(p))
        title = first_heading(text) or p.stem
        anchor = f"doc-{idx:03d}"
        toc.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        body = markdown.markdown(text, extensions=["extra", "sane_lists", "toc"])
        sections.append(f'<section class="document" id="{anchor}">{body}</section>')

    figure_parts: list[str] = []
    for fig_id, svg in sorted(rendered.items()):
        source_md = next((BOOK / "figures").glob(f"{fig_id}_*.md"))
        text = read(source_md)
        title = first_heading(text)
        cap_match = re.search(r"##\s+Caption\s*\n+(.+?)(?:\n\n|\n##)", text, re.S | re.I)
        caption = re.sub(r"\s+", " ", cap_match.group(1).strip()) if cap_match else title
        rel = svg.relative_to(BUILD).as_posix()
        figure_parts.append(
            f'<figure id="{fig_id.lower()}"><h2>{html.escape(title)}</h2>'
            f'<img src="{rel}" alt="{html.escape(caption)}"><figcaption>{html.escape(caption)}</figcaption></figure>'
        )

    html_path = BUILD / "book-05-reader.html"
    pdf_path = BUILD / "book-05-reader.pdf"
    document = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Book 05 — MarkReg</title><style>{css}</style></head>
<body><header><h1>Book 05 — MarkReg: The Full-Lifecycle International Trademark Product</h1>
<p>PF-08 validation edition. Complete Draft 1; not Release Candidate 1.</p></header>
<nav><h2>Contents</h2><ol>{''.join(toc)}</ol></nav>
{''.join(sections)}
<section class="figure-atlas"><h1>Controlled Figure Atlas</h1>{''.join(figure_parts)}</section>
</body></html>"""
    html_path.write_text(document, encoding="utf-8")
    record("reader HTML generated", html_path.exists() and html_path.stat().st_size > 10000, f"{html_path.stat().st_size} bytes")
    try:
        HTML(filename=str(html_path), base_url=str(BUILD)).write_pdf(str(pdf_path))
        record("reader PDF generated", pdf_path.exists() and pdf_path.stat().st_size > 50000, f"{pdf_path.stat().st_size if pdf_path.exists() else 0} bytes")
    except Exception as exc:
        record("reader PDF generated", False, repr(exc))
    return html_path, pdf_path


def validate_rendered(html_path: Path, pdf_path: Path, rendered: dict[str, Path]) -> None:
    if not pdf_path.exists():
        return
    reader = PdfReader(str(pdf_path))
    text_by_page = [(p.extract_text() or "").strip() for p in reader.pages]
    all_text = "\n".join(text_by_page)
    record("PDF page count", len(reader.pages) >= 50, f"{len(reader.pages)} pages")
    record("PDF selectable text", len(all_text) > 100_000, f"{len(all_text)} extracted characters")
    for i in range(48):
        token = f"B05-CH-{i:02d}"
        record(f"PDF contains {token}", token in all_text, "present" if token in all_text else "missing")
    for letter in "ABCDEFG":
        token = f"Appendix {letter}"
        record(f"PDF contains {token}", token in all_text, "present" if token in all_text else "missing")
    for fig_id in rendered:
        record(f"PDF figure caption {fig_id}", fig_id in all_text, "present" if fig_id in all_text else "missing")
    record("PDF Source Notes", "Source and Authority Notes" in all_text, "present")
    record("PDF Glossary", "Glossary" in all_text, "present")
    record("PDF Subject Index", "Subject Index" in all_text, "present")
    # At least the generated TOC should create link annotations.
    annotations = 0
    for page in reader.pages:
        annots = page.get("/Annots")
        if annots:
            annotations += len(annots)
    record("PDF navigation links", annotations > 0, f"{annotations} annotations")
    # Non-truncation proxy: every source document heading occurs in extracted text.
    missing_ids = []
    for source in reader_sources():
        heading = first_heading(read(source))
        m = re.match(r"(B05-(?:CH-\d{2}|APP-[A-G]|PUB-\d{4}))", heading)
        if m and m.group(1) not in all_text:
            missing_ids.append(m.group(1))
    record("rendered document completeness", not missing_ids, "all stable source IDs present" if not missing_ids else f"missing {missing_ids}")


def write_report() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    summary = {
        "status": "PASS" if not ERRORS else "FAIL",
        "checks": len(CHECKS),
        "passed": sum(c.status == "PASS" for c in CHECKS),
        "warnings": WARNINGS,
        "errors": ERRORS,
        "results": [asdict(c) for c in CHECKS],
    }
    (BUILD / "validation-report.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    rows = ["# Book 05 PF-08 Validation Report", "", f"- **Status:** {summary['status']}", f"- **Checks:** {summary['checks']}", f"- **Passed:** {summary['passed']}", f"- **Warnings:** {len(WARNINGS)}", f"- **Errors:** {len(ERRORS)}", "", "## Results", "", "| Check | Status | Detail |", "| --- | --- | --- |"]
    for c in CHECKS:
        rows.append(f"| {c.name.replace('|', '/')} | {c.status} | {c.detail.replace('|', '/').replace(chr(10), ' ')} |")
    if ERRORS:
        rows += ["", "## Blocking Errors", ""] + [f"- {e}" for e in ERRORS]
    if WARNINGS:
        rows += ["", "## Warnings", ""] + [f"- {w}" for w in WARNINGS]
    (BUILD / "validation-report.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("status", "checks", "passed", "warnings", "errors")}, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-render", action="store_true")
    args = parser.parse_args()
    if BUILD.exists():
        shutil.rmtree(BUILD)
    check_inventory()
    check_markdown_structure()
    check_controlled_ids()
    figures = check_figures_source()
    check_yaml_state()
    rendered: dict[str, Path] = {}
    if not args.skip_render:
        rendered = render_figures(figures)
        html_path, pdf_path = build_reader(rendered)
        validate_rendered(html_path, pdf_path, rendered)
    write_report()
    return 1 if ERRORS else 0


if __name__ == "__main__":
    raise SystemExit(main())
