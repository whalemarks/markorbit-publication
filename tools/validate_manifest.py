#!/usr/bin/env python3
"""Validate repository publication manifest structure without modifying files."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / 'PUBLICATION-MANIFEST.md'
BOOK_ROW_RE = re.compile(
    r"^\|\s*(Book\s+\d+)\s*\|[^|]*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|",
    re.MULTILINE,
)
STRICT_STATUSES = {'active', 'migrated', 'present'}
PLANNED_STATUSES = {'planned'}
BOOK_02 = 'Book 02'


@dataclass(frozen=True)
class BookEntry:
    label: str
    path: str
    status: str

    @property
    def normalized_status(self) -> str:
        return self.status.strip().lower()


def parse_books(text: str) -> list[BookEntry]:
    return [
        BookEntry(label=book, path=path.rstrip('/'), status=status.strip())
        for book, path, status in BOOK_ROW_RE.findall(text)
    ]


def requires_strict_validation(book: BookEntry, book_dir: Path) -> bool:
    if book.label == BOOK_02:
        return True
    if book.normalized_status in STRICT_STATUSES:
        return True
    return book_dir.is_dir()


def main() -> int:
    print('Publication Manifest Validation Report')
    print('======================================')
    print(f'Repository root: {REPO_ROOT}')

    errors: list[str] = []
    warnings: list[str] = []
    if not MANIFEST.is_file():
        errors.append('PUBLICATION-MANIFEST.md is missing.')
        books: list[BookEntry] = []
    else:
        print('✓ PUBLICATION-MANIFEST.md exists')
        text = MANIFEST.read_text(encoding='utf-8')
        books = parse_books(text)
        print(f'Books listed: {len(books)}')

    for book in books:
        book_dir = REPO_ROOT / book.path
        strict = requires_strict_validation(book, book_dir)
        status_label = f'{book.label} ({book.status})'

        if not book_dir.is_dir():
            message = f'{status_label}: directory missing at {book.path}/'
            if strict:
                errors.append(message)
            elif book.normalized_status in PLANNED_STATUSES:
                warnings.append(message)
                print(f'⚠ {message}')
            else:
                warnings.append(message)
                print(f'⚠ {message}')
            continue

        print(f'✓ {status_label}: directory exists at {book.path}/')
        book_manifest = book_dir / 'BOOK-MANIFEST.md'
        if book_manifest.is_file():
            print('  ✓ BOOK-MANIFEST.md exists')
        elif strict:
            errors.append(f'{status_label}: missing {book.path}/BOOK-MANIFEST.md')
        else:
            warnings.append(f'{status_label}: missing {book.path}/BOOK-MANIFEST.md')

        if book.label == BOOK_02:
            for required in ('BOOK-GOVERNANCE.md', 'BOOK-STATUS.md'):
                if (book_dir / required).is_file():
                    print(f'  ✓ {required} exists')
                else:
                    errors.append(f'{status_label}: missing {book.path}/{required}')

    if warnings:
        print('\nWarnings:')
        for warning in warnings:
            print(f'- {warning}')

    if errors:
        print('\nErrors:')
        for error in errors:
            print(f'- {error}')
        return 1

    print('\nManifest validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
