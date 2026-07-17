#!/usr/bin/env python3
"""Preflight seven PDF review editions and render visual samples."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".artifacts/portfolio-review-render-01"
EXPECTED_WIDTH = 432.0
EXPECTED_HEIGHT = 648.0
TOLERANCE = 1.0


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ink_ratio(pix: fitz.Pixmap) -> float:
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    gray = image.convert("L")
    histogram = gray.histogram()
    nonwhite = sum(histogram[:248])
    return nonwhite / float(pix.width * pix.height)


def inspect_pdf(path: Path, book_dir: Path) -> dict[str, object]:
    document = fitz.open(path)
    if document.page_count < 1:
        raise RuntimeError(f"empty PDF: {path}")
    low_content: list[int] = []
    page_sizes: set[tuple[float, float]] = set()
    extracted_chars = 0
    image_occurrences = 0
    sample_indexes = sorted({0, document.page_count // 2, document.page_count - 1})
    previews = book_dir / "previews"
    previews.mkdir(exist_ok=True)

    for index in range(document.page_count):
        page = document.load_page(index)
        rect = page.rect
        page_sizes.add((round(rect.width, 2), round(rect.height, 2)))
        text = page.get_text("text")
        extracted_chars += len(text.strip())
        image_occurrences += len(page.get_images(full=True))
        pix = page.get_pixmap(matrix=fitz.Matrix(0.5, 0.5), alpha=False)
        ratio = ink_ratio(pix)
        if ratio < 0.001:
            low_content.append(index + 1)
        if index in sample_indexes:
            preview = previews / f"page-{index + 1:04d}.png"
            page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3), alpha=False).save(preview)

    wrong_sizes = [size for size in page_sizes if abs(size[0] - EXPECTED_WIDTH) > TOLERANCE or abs(size[1] - EXPECTED_HEIGHT) > TOLERANCE]
    return {
        "file": path.name,
        "sha256": digest(path),
        "bytes": path.stat().st_size,
        "pages": document.page_count,
        "page_sizes_points": [list(size) for size in sorted(page_sizes)],
        "page_size_pass": not wrong_sizes,
        "wrong_page_sizes": [list(size) for size in wrong_sizes],
        "extractable_text_chars": extracted_chars,
        "text_pass": extracted_chars > 1000,
        "image_occurrences": image_occurrences,
        "low_content_pages": low_content,
        "low_content_pass": len(low_content) == 0,
        "preview_pages": [index + 1 for index in sample_indexes],
    }


def main() -> int:
    records: list[dict[str, object]] = []
    failures: list[str] = []
    for index in range(1, 8):
        book_dir = OUT / f"book-{index:02d}"
        pdf = book_dir / f"book-{index:02d}-review.pdf"
        if not pdf.is_file():
            failures.append(f"Book {index:02d}: PDF missing")
            continue
        try:
            record = inspect_pdf(pdf, book_dir)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"Book {index:02d}: {exc}")
            continue
        record["book"] = f"Book {index:02d}"
        records.append(record)
        if not record["page_size_pass"]:
            failures.append(f"Book {index:02d}: wrong page size")
        if not record["text_pass"]:
            failures.append(f"Book {index:02d}: insufficient extractable text")
        if not record["low_content_pass"]:
            failures.append(f"Book {index:02d}: low-content pages {record['low_content_pages']}")

    report = {
        "schema": "markorbit-pdf-review-preflight/v1",
        "books_expected": 7,
        "books_preflighted": len(records),
        "pdf_readable": len(records) == 7,
        "page_size_pass": bool(records) and all(r["page_size_pass"] for r in records),
        "extractable_text_pass": bool(records) and all(r["text_pass"] for r in records),
        "low_content_pass": bool(records) and all(r["low_content_pass"] for r in records),
        "publication_authorized": False,
        "failures": failures,
        "books": records,
    }
    (OUT / "preflight-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# PORTFOLIO-REV-0005 — Seven PDF Review Editions Preflight",
        "",
        "## Summary",
        "",
        "```text",
        f"Books rendered: {len(records)} / 7",
        f"PDF readable: {'PASS' if report['pdf_readable'] else 'FAIL'}",
        f"6 x 9 page size: {'PASS' if report['page_size_pass'] else 'FAIL'}",
        f"Extractable text: {'PASS' if report['extractable_text_pass'] else 'FAIL'}",
        f"Unexpected low-content pages: {'0' if report['low_content_pass'] else 'PRESENT'}",
        "Publication authorization: NOT GRANTED",
        "```",
        "",
        "## Book results",
        "",
        "| Book | Pages | Bytes | Text chars | Images | Low-content pages |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for record in records:
        low = ", ".join(str(v) for v in record["low_content_pages"]) or "0"
        lines.append(f"| {record['book']} | {record['pages']} | {record['bytes']} | {record['extractable_text_chars']} | {record['image_occurrences']} | {low} |")
    if failures:
        lines.extend(["", "## Failures", ""] + [f"- {failure}" for failure in failures])
    lines.extend(["", "## Decision", "", "The files are review editions only. Public or commercial distribution remains unauthorized.", ""])
    (OUT / "PREFLIGHT-REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
