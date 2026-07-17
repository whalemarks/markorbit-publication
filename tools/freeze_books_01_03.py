#!/usr/bin/env python3
"""Generate deterministic SHA-256 freeze manifests for Books 01 and 03."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = {
    "B01-RC1-FROZEN-01": ROOT / "books/book-01-operating-system",
    "B03-RC1-FROZEN-01": ROOT / "books/book-03-execution-system",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def controlled_files(book: Path) -> list[Path]:
    files: list[Path] = []
    for directory_name in ("manuscript", "publication"):
        directory = book / directory_name
        if directory.is_dir():
            files.extend(path for path in directory.rglob("*.md") if path.is_file())
    return sorted(set(files), key=lambda path: path.relative_to(book).as_posix())


def write_manifest(identifier: str, book: Path) -> None:
    files = controlled_files(book)
    if not files:
        raise RuntimeError(f"no controlled content found for {book}")
    lines = [
        f"# {identifier} Freeze Manifest",
        "",
        f"Frozen identifier: `{identifier}`",
        "",
        "```text",
        f"Controlled files bound: {len(files)}",
        "SHA-256 coverage: PASS",
        "Freeze authorization: GRANTED",
        "Public/commercial distribution: NOT AUTHORIZED",
        "Implementation or deployment: NOT AUTHORIZED",
        "```",
        "",
        "## SHA-256",
        "",
    ]
    for path in files:
        relative = path.relative_to(book).as_posix()
        lines.append(f"- `{relative}` — `{digest(path)}`")
    (book / "FREEZE-MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    for identifier, book in BOOKS.items():
        write_manifest(identifier, book)
        print(f"Generated {identifier} manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
