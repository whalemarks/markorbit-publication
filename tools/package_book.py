#!/usr/bin/env python3
"""Package a book directory into a release candidate zip archive."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

REPO_ROOT = Path(__file__).resolve().parents[1]
RELEASE_DIR = REPO_ROOT / 'release' / 'rc'
EXCLUDED_NAMES = {'.DS_Store', 'Thumbs.db'}
EXCLUDED_PARTS = {'__pycache__'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo'}


def should_include(path: Path) -> bool:
    if path.name in EXCLUDED_NAMES:
        return False
    if EXCLUDED_PARTS.intersection(path.parts):
        return False
    if path.suffix in EXCLUDED_SUFFIXES:
        return False
    return path.is_file()


def main() -> int:
    parser = argparse.ArgumentParser(description='Create a timestamped zip package for a book directory.')
    parser.add_argument('book_path', help='Path to a book directory, e.g. books/book-02-core-specification')
    args = parser.parse_args()

    book_dir = (REPO_ROOT / args.book_path).resolve(strict=False)
    if not book_dir.is_dir():
        parser.error(f'book path is not a directory: {args.book_path}')

    try:
        book_dir.relative_to(REPO_ROOT)
    except ValueError:
        parser.error('book path must be inside this repository')

    RELEASE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    zip_path = RELEASE_DIR / f'{book_dir.name}-{timestamp}.zip'

    included = 0
    with ZipFile(zip_path, 'w', ZIP_DEFLATED) as archive:
        for path in sorted(book_dir.rglob('*')):
            if should_include(path):
                archive.write(path, path.relative_to(REPO_ROOT))
                included += 1

    print('Book Package Report')
    print('===================')
    print(f'Book directory: {book_dir.relative_to(REPO_ROOT)}')
    print(f'Files packaged: {included}')
    print(f'Package created: {zip_path.relative_to(REPO_ROOT)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
