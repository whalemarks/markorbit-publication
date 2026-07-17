#!/usr/bin/env python3
"""Audit publication readiness across the seven frozen MarkOrbit books."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BOOKS = [
    ("Book 01", "MarkOrbit — The Operating System for Global Brand Services", ROOT / "books/book-01-operating-system"),
    ("Book 02", "MarkOrbit Core Specification", ROOT / "books/book-02-core-specification"),
    ("Book 03", "MarkOrbit Execution System", ROOT / "books/book-03-execution-system"),
    ("Book 04", "MarkOrbit Workplace and Product Architecture", ROOT / "books/book-04-workplace-product-architecture"),
    ("Book 05", "MarkReg", ROOT / "books/book-05-markreg"),
    ("Book 06", "MarkOrbit Lite", ROOT / "books/book-06-markorbit-lite"),
    ("Book 07", "Mark Global Service Network", ROOT / "books/book-07-mark-global-service-network"),
]

DIMENSIONS = (
    "front_matter",
    "publication_apparatus",
    "cross_book_consistency",
    "visual_production",
    "rendering_readiness",
    "release_governance",
)

KEYWORDS = {
    "front_matter": {
        "title": ("title page", "book title", "标题页"),
        "copyright": ("copyright", "all rights reserved", "版权"),
        "edition": ("edition", "release candidate", "version", "版本"),
        "preface": ("preface", "foreword", "introduction", "序言", "前言"),
        "contents": ("table of contents", "contents", "目录"),
        "author": ("about the author", "author", "project note", "作者"),
    },
    "publication_apparatus": {
        "glossary": ("glossary", "术语"),
        "index": ("subject index", "index", "索引"),
        "figures": ("figure register", "list of figures", "图表"),
        "sources": ("source notes", "bibliography", "references", "参考"),
        "appendices": ("appendix", "appendices", "附录"),
    },
    "visual_production": {
        "cover": ("cover brief", "cover specification", "封面"),
        "typography": ("typography", "type system", "字体"),
        "series_identity": ("series identity", "visual identity", "series design", "系列视觉"),
        "image_rights": ("image licensing", "image rights", "图像授权"),
    },
    "rendering_readiness": {
        "pdf": ("pdf", "pandoc", "weasyprint", "latex"),
        "epub": ("epub",),
        "print": ("print trim", "bleed", "print-ready", "印刷"),
        "page_breaks": ("page break", "page-break", "分页"),
        "render_config": ("render config", "rendering specification", "build book"),
    },
    "release_governance": {
        "copyright_owner": ("copyright owner", "rights holder", "版权归属"),
        "isbn": ("isbn",),
        "distribution": ("distribution channel", "distribution decision", "发行"),
        "release_authorization": ("release authorization", "publication authorization", "出版授权"),
        "archive": ("archival package", "archive package", "归档"),
    },
}


def markdown_files(book: Path) -> list[Path]:
    files = []
    for path in book.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(book).parts):
            continue
        files.append(path)
    return sorted(files)


def text_for(book: Path) -> str:
    chunks = []
    for path in markdown_files(book):
        try:
            chunks.append(path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            pass
    return "\n".join(chunks).lower()


def filename_text(book: Path) -> str:
    return "\n".join(path.relative_to(book).as_posix().lower() for path in markdown_files(book))


def has_any(haystack: str, terms: tuple[str, ...]) -> bool:
    return any(term.lower() in haystack for term in terms)


def assess_keyword_group(corpus: str, filenames: str, group: dict[str, tuple[str, ...]]) -> tuple[str, dict[str, bool]]:
    found = {name: has_any(corpus, terms) or has_any(filenames, terms) for name, terms in group.items()}
    count = sum(found.values())
    if count == len(found):
        rating = "READY"
    elif count == 0:
        rating = "MISSING"
    else:
        rating = "PARTIAL"
    return rating, found


def cross_book_assessment(corpus: str) -> tuple[str, dict[str, bool]]:
    checks = {
        "book_numbering": bool(re.search(r"book\s+0?[1-7]", corpus)),
        "workplace_product_terms": "workplace" in corpus and "product" in corpus,
        "frozen_or_rc_status": any(term in corpus for term in ("frozen", "release candidate", "owner accepted")),
        "cross_book_reference": any(term in corpus for term in ("book 02", "book 03", "book 04", "book 05", "book 06", "book 07")),
    }
    count = sum(checks.values())
    return ("READY" if count == len(checks) else "PARTIAL" if count else "MISSING"), checks


def book_result(number: str, title: str, path: Path) -> dict:
    corpus = text_for(path)
    filenames = filename_text(path)
    result = {
        "book": number,
        "title": title,
        "path": path.relative_to(ROOT).as_posix(),
        "markdown_files": len(markdown_files(path)),
        "dimensions": {},
    }
    for dimension in ("front_matter", "publication_apparatus", "visual_production", "rendering_readiness", "release_governance"):
        rating, checks = assess_keyword_group(corpus, filenames, KEYWORDS[dimension])
        result["dimensions"][dimension] = {"rating": rating, "checks": checks}
    rating, checks = cross_book_assessment(corpus)
    result["dimensions"]["cross_book_consistency"] = {"rating": rating, "checks": checks}
    result["ready_dimensions"] = sum(1 for value in result["dimensions"].values() if value["rating"] == "READY")
    result["missing_dimensions"] = [name for name, value in result["dimensions"].items() if value["rating"] == "MISSING"]
    result["partial_dimensions"] = [name for name, value in result["dimensions"].items() if value["rating"] == "PARTIAL"]
    return result


def portfolio_summary(books: list[dict]) -> dict:
    dimension_summary = {}
    for dimension in DIMENSIONS:
        ratings = [book["dimensions"][dimension]["rating"] for book in books]
        dimension_summary[dimension] = {
            "ready": ratings.count("READY"),
            "partial": ratings.count("PARTIAL"),
            "missing": ratings.count("MISSING"),
        }
    blockers = []
    for dimension, summary in dimension_summary.items():
        if summary["missing"]:
            blockers.append({"dimension": dimension, "severity": "BLOCKER", **summary})
        elif summary["partial"]:
            blockers.append({"dimension": dimension, "severity": "MAJOR", **summary})
    return {
        "books_audited": len(books),
        "dimensions_assessed": len(DIMENSIONS),
        "dimension_summary": dimension_summary,
        "portfolio_blockers": blockers,
        "release_ready_books": sum(1 for book in books if book["ready_dimensions"] == len(DIMENSIONS)),
        "publication_authorization": "NOT GRANTED",
    }


def markdown_report(books: list[dict], summary: dict) -> str:
    lines = [
        "# PORTFOLIO-AUD-0001 — Seven-Book Publication Readiness",
        "",
        "## Audit result",
        "",
        "```text",
        f"Books audited: {summary['books_audited']} / 7",
        f"Readiness dimensions assessed: {summary['dimensions_assessed']} / 6",
        f"Books ready for immediate release production: {summary['release_ready_books']} / 7",
        "Frozen manuscript modifications: 0",
        "Publication authorization: NOT GRANTED",
        "```",
        "",
        "## Book matrix",
        "",
        "| Book | Front matter | Apparatus | Cross-book | Visual | Rendering | Governance |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    labels = {
        "front_matter": "Front matter",
        "publication_apparatus": "Apparatus",
        "cross_book_consistency": "Cross-book",
        "visual_production": "Visual",
        "rendering_readiness": "Rendering",
        "release_governance": "Governance",
    }
    for book in books:
        ratings = [book["dimensions"][dimension]["rating"] for dimension in DIMENSIONS]
        lines.append(f"| {book['book']} | " + " | ".join(ratings) + " |")
    lines += ["", "## Portfolio dimension summary", ""]
    for dimension in DIMENSIONS:
        s = summary["dimension_summary"][dimension]
        lines.append(f"- **{labels[dimension]}:** READY {s['ready']}/7; PARTIAL {s['partial']}/7; MISSING {s['missing']}/7.")
    lines += ["", "## Book-level findings", ""]
    for book in books:
        lines += [f"### {book['book']} — {book['title']}", ""]
        for dimension in DIMENSIONS:
            value = book["dimensions"][dimension]
            missing = [name for name, found in value["checks"].items() if not found]
            lines.append(f"- **{labels[dimension]} — {value['rating']}**" + (f": missing/undetected `{', '.join(missing)}`." if missing else "."))
        lines.append("")
    lines += [
        "## Decision",
        "",
        "The seven frozen baselines are structurally governed, but the portfolio is not yet authorized or uniformly prepared for publication. Common publication assets must be completed before book-specific rendering.",
        "",
        "## Required remediation sequence",
        "",
        "```text",
        "common series front matter and release metadata",
        "→ cross-book publication copyedit and reference normalization",
        "→ visual and rendering specification",
        "→ seven rendered release candidates",
        "→ final publication and distribution decision",
        "```",
        "",
        "## Authority boundary",
        "",
        "This audit does not modify frozen prose and does not authorize publication, commercial distribution, ISBN procurement, implementation, deployment or External Protected Action.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.mkdir(parents=True, exist_ok=True)
    books = [book_result(*item) for item in BOOKS]
    summary = portfolio_summary(books)
    payload = {"books": books, "summary": summary}
    (output / "portfolio-publication-audit.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output / "PORTFOLIO-AUD-0001_Seven_Book_Publication_Readiness.md").write_text(markdown_report(books, summary), encoding="utf-8")
    print(f"Audited {summary['books_audited']} books across {summary['dimensions_assessed']} dimensions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
