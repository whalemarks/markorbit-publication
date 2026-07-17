#!/usr/bin/env python3
"""Validate Book 01 and Book 03 RC1 freeze manifests and portfolio state."""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK1 = ROOT / "books/book-01-operating-system"
BOOK3 = ROOT / "books/book-03-execution-system"


class ValidationError(RuntimeError):
    pass


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValidationError(result.stderr.strip())
    return result.stdout.strip()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def controlled_files(book: Path) -> list[Path]:
    files: list[Path] = []
    for directory_name in ("manuscript", "publication"):
        directory = book / directory_name
        if directory.is_dir():
            files.extend(path for path in directory.rglob("*.md") if path.is_file())
    return sorted(set(files), key=lambda path: path.relative_to(book).as_posix())


def corpus(book: Path) -> str:
    return "\n".join(path.read_text(encoding="utf-8") for path in controlled_files(book))


def validate_declared_structure() -> None:
    b1_status = (BOOK1 / "BOOK-STATUS.md").read_text(encoding="utf-8")
    b3_status = (BOOK3 / "BOOK-STATUS.md").read_text(encoding="utf-8")
    for statement in (
        "Preface, Contents, Chapters 1–9 and Appendices A–C complete",
        "Book 01 freeze: GRANTED",
        "B01-RC1-FROZEN-01",
    ):
        if statement not in b1_status:
            raise ValidationError(f"Book 01 status missing: {statement}")
    for statement in (
        "CH00–CH34",
        "Appendices:** A–H",
        "Book 03 freeze: GRANTED",
        "B03-RC1-FROZEN-01",
    ):
        if statement not in b3_status:
            raise ValidationError(f"Book 03 status missing: {statement}")

    b1_files = controlled_files(BOOK1)
    b3_files = controlled_files(BOOK3)
    if len(b1_files) < 14:
        raise ValidationError(f"Book 01 controlled inventory unexpectedly small: {len(b1_files)}")
    if len(b3_files) < 43:
        raise ValidationError(f"Book 03 controlled inventory unexpectedly small: {len(b3_files)}")

    b1_text = corpus(BOOK1)
    b3_text = corpus(BOOK3)
    for chapter in range(1, 10):
        if not re.search(rf"(?:Chapter|CH)[ -]?0?{chapter}\b", b1_text, flags=re.IGNORECASE):
            raise ValidationError(f"Book 01 chapter {chapter} not discoverable")
    for appendix in "ABC":
        if not re.search(rf"Appendix[ -]{appendix}\b", b1_text, flags=re.IGNORECASE):
            raise ValidationError(f"Book 01 Appendix {appendix} not discoverable")
    for chapter in range(35):
        if not re.search(rf"(?:B03-)?CH[- ]?{chapter:02d}\b", b3_text, flags=re.IGNORECASE):
            raise ValidationError(f"Book 03 CH{chapter:02d} not discoverable")
    for appendix in "ABCDEFGH":
        if not re.search(rf"Appendix[ -]{appendix}\b", b3_text, flags=re.IGNORECASE):
            raise ValidationError(f"Book 03 Appendix {appendix} not discoverable")


def validate_manifest(book: Path, identifier: str) -> None:
    manifest_path = book / "FREEZE-MANIFEST.md"
    if not manifest_path.is_file():
        raise ValidationError(f"missing freeze manifest: {manifest_path}")
    manifest = manifest_path.read_text(encoding="utf-8")
    for statement in (
        f"Frozen identifier: `{identifier}`",
        "SHA-256 coverage: PASS",
        "Freeze authorization: GRANTED",
        "Public/commercial distribution: NOT AUTHORIZED",
        "Implementation or deployment: NOT AUTHORIZED",
    ):
        if statement not in manifest:
            raise ValidationError(f"{identifier} manifest missing: {statement}")
    for path in controlled_files(book):
        relative = path.relative_to(book).as_posix()
        expected = f"- `{relative}` — `{digest(path)}`"
        if expected not in manifest:
            raise ValidationError(f"{identifier} hash binding missing or stale: {relative}")


def validate_portfolio() -> None:
    registry = (ROOT / "PORTFOLIO-FREEZE-STATUS.md").read_text(encoding="utf-8")
    for statement in (
        "Book 01 | MarkOrbit — The Operating System for Global Brand Services | B01-RC1-FROZEN-01",
        "Book 03 | MarkOrbit Execution System | B03-RC1-FROZEN-01",
        "Seven-book frozen-baseline coverage: 7 / 7",
    ):
        if statement not in registry:
            raise ValidationError(f"portfolio freeze registry missing: {statement}")


def validate_diff(base_sha: str | None) -> None:
    if not base_sha:
        return
    changed = git("diff", "--name-only", f"{base_sha}...HEAD").splitlines()
    allowed_content = {
        "books/book-01-operating-system/FREEZE-MANIFEST.md",
        "books/book-03-execution-system/FREEZE-MANIFEST.md",
    }
    protected_prefixes = (
        "books/book-01-operating-system/manuscript/",
        "books/book-01-operating-system/publication/",
        "books/book-03-execution-system/manuscript/",
        "books/book-03-execution-system/publication/",
        "books/book-02-core-specification/",
        "books/book-04-workplace-product-architecture/accepted-vnext/",
        "books/book-05-markreg/manuscript/",
        "books/book-06-markorbit-lite/manuscript/",
        "books/book-07-mark-global-service-network/manuscript/",
    )
    violations = [
        path for path in changed
        if path not in allowed_content and any(path.startswith(prefix) for prefix in protected_prefixes)
    ]
    if violations:
        raise ValidationError("frozen or accepted content changed:\n" + "\n".join(violations))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-sha")
    args = parser.parse_args()
    try:
        validate_declared_structure()
        validate_manifest(BOOK1, "B01-RC1-FROZEN-01")
        validate_manifest(BOOK3, "B03-RC1-FROZEN-01")
        validate_portfolio()
        validate_diff(args.base_sha)
    except ValidationError as exc:
        print(f"FAIL: {exc}")
        return 1
    print("Books 01 and 03 portfolio freeze validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
