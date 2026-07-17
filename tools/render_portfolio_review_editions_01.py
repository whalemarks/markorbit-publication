#!/usr/bin/env python3
"""Render seven PDF review editions from PORTFOLIO-RC-01 candidates."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

import markdown
from weasyprint import CSS, HTML

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / ".artifacts/portfolio-release-candidates-01"
OUT = ROOT / ".artifacts/portfolio-review-render-01"

BOOKS = {
    1: ("OS", "MarkOrbit — The Operating System for Global Brand Services"),
    2: ("CORE", "MarkOrbit Core Specification"),
    3: ("EXEC", "MarkOrbit Execution System"),
    4: ("WORK", "MarkOrbit Workplace and Product Architecture"),
    5: ("REG", "MarkReg"),
    6: ("LITE", "MarkOrbit Lite"),
    7: ("NET", "Mark Global Service Network"),
}

CSS_TEXT = r"""
@page {
  size: 6in 9in;
  margin: 0.72in 0.62in 0.72in 0.72in;
  @bottom-center { content: counter(page); font-size: 8pt; color: #555; }
}
@page :first { @bottom-center { content: none; } }
html { font-family: "DejaVu Serif", "Liberation Serif", serif; font-size: 10.3pt; line-height: 1.43; }
body { margin: 0; color: #111; }
.cover { page-break-after: always; min-height: 7.1in; display: flex; flex-direction: column; justify-content: space-between; }
.series { font-family: "DejaVu Sans", sans-serif; font-size: 9pt; letter-spacing: 0.08em; text-transform: uppercase; }
.book-code { font-family: "DejaVu Sans", sans-serif; font-size: 34pt; font-weight: 700; margin-top: 1.2in; }
h1 { font-family: "DejaVu Sans", sans-serif; font-size: 22pt; line-height: 1.12; page-break-before: always; margin: 0 0 18pt; }
h2 { font-family: "DejaVu Sans", sans-serif; font-size: 15pt; line-height: 1.2; margin: 18pt 0 8pt; page-break-after: avoid; }
h3 { font-family: "DejaVu Sans", sans-serif; font-size: 12pt; margin: 14pt 0 6pt; page-break-after: avoid; }
h4 { font-family: "DejaVu Sans", sans-serif; font-size: 10.5pt; margin: 12pt 0 5pt; page-break-after: avoid; }
p { margin: 0 0 7pt; orphans: 3; widows: 3; }
ul, ol { margin: 5pt 0 8pt 18pt; padding: 0; }
li { margin-bottom: 2.5pt; }
blockquote { margin: 9pt 0; padding: 7pt 10pt; border-left: 2pt solid #777; background: #f4f4f4; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font-family: "DejaVu Sans Mono", monospace; font-size: 8.3pt; line-height: 1.28; background: #f2f2f2; padding: 7pt; page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 0.9em; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 12pt; font-size: 8.5pt; }
th, td { border: 0.5pt solid #888; padding: 4pt; vertical-align: top; overflow-wrap: anywhere; }
th { font-family: "DejaVu Sans", sans-serif; background: #ededed; }
img { display: block; max-width: 100%; max-height: 6.5in; margin: 10pt auto; page-break-inside: avoid; }
hr { border: 0; border-top: 0.5pt solid #999; margin: 16pt 0; }
a { color: inherit; text-decoration: none; }
.front-matter { page-break-after: always; }
.source-file { display: none; }
"""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_candidate_paths(text: str) -> str:
    # Candidate files live under candidate/manuscript while copied assets live at candidate root.
    replacements = {
        "../../figures/": "figures/",
        "../figures/": "figures/",
        "../../publication/": "publication/",
        "../publication/": "publication/",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def markdown_to_html(text: str) -> str:
    return markdown.markdown(
        normalize_candidate_paths(text),
        extensions=["extra", "tables", "fenced_code", "sane_lists", "toc"],
        output_format="html5",
    )


def read_markdown_files(candidate: Path) -> list[tuple[str, str]]:
    files: list[tuple[str, str]] = []
    for name in ("00-SERIES-PAGE.md", "01-MARKORBIT-PROJECT.md", "02-BOOK-FRONT-MATTER.md"):
        path = candidate / name
        files.append((name, path.read_text(encoding="utf-8")))
    manuscript = candidate / "manuscript"
    for path in sorted(manuscript.rglob("*.md"), key=lambda p: p.as_posix().lower()):
        files.append((path.relative_to(candidate).as_posix(), path.read_text(encoding="utf-8")))
    return files


def unresolved_assets(candidate: Path, texts: list[tuple[str, str]]) -> list[str]:
    missing: set[str] = set()
    pattern = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
    for _, text in texts:
        normalized = normalize_candidate_paths(text)
        for target in pattern.findall(normalized):
            if re.match(r"^[a-z]+://", target, re.I) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (candidate / target).exists():
                missing.add(target)
    return sorted(missing)


def render_book(index: int) -> dict[str, object]:
    code, title = BOOKS[index]
    candidate = CANDIDATES / f"book-{index:02d}"
    if not candidate.is_dir():
        raise FileNotFoundError(f"candidate missing: {candidate}")
    texts = read_markdown_files(candidate)
    missing = unresolved_assets(candidate, texts)

    cover = f"""<section class='cover'><div><div class='series'>MarkOrbit Publication Series · Book {index:02d}</div><div class='book-code'>{code}</div><h1 style='page-break-before:auto'>{title}</h1></div><div>PDF Review Edition · Publication authorization NOT GRANTED</div></section>"""
    parts = [cover]
    for file_name, text in texts:
        klass = "front-matter" if file_name.startswith(("00-", "01-", "02-")) else "manuscript-section"
        parts.append(f"<section class='{klass}'><div class='source-file'>{file_name}</div>{markdown_to_html(text)}</section>")

    html_text = "<!doctype html><html><head><meta charset='utf-8'>" + f"<title>{title}</title></head><body>" + "\n".join(parts) + "</body></html>"
    book_out = OUT / f"book-{index:02d}"
    book_out.mkdir(parents=True, exist_ok=True)
    html_path = book_out / f"book-{index:02d}-review.html"
    pdf_path = book_out / f"book-{index:02d}-review.pdf"
    html_path.write_text(html_text, encoding="utf-8")
    HTML(string=html_text, base_url=str(candidate)).write_pdf(str(pdf_path), stylesheets=[CSS(string=CSS_TEXT)])
    return {
        "book": f"Book {index:02d}",
        "code": code,
        "title": title,
        "pdf": pdf_path.relative_to(OUT).as_posix(),
        "pdf_sha256": sha256(pdf_path),
        "pdf_bytes": pdf_path.stat().st_size,
        "source_markdown_files": len(texts),
        "missing_image_assets": missing,
        "publication_authorized": False,
    }


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    results = [render_book(index) for index in range(1, 8)]
    report = {
        "schema": "markorbit-portfolio-review-render/v1",
        "books_rendered": len(results),
        "profile": "pdf-review",
        "page_size_inches": [6, 9],
        "frozen_source_mutations": 0,
        "publication_authorized": False,
        "books": results,
    }
    (OUT / "render-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
