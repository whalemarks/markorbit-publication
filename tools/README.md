# Repository Validation Tools

This directory contains lightweight validation and packaging helpers for the MarkOrbit publication repository. These scripts inspect repository structure or create release artifacts; they do not define architecture, rewrite specifications, or modify book content.

All scripts use only the Python standard library.

## `validate_links.py`

Scans Markdown files in the repository, detects internal Markdown references ending in `.md`, and reports references whose target files do not exist. The checker supports repository-global links and links that are internal to a book directory.

Run:

```bash
python tools/validate_links.py
```

The script prints a readable report and exits with a non-zero status when missing internal Markdown references are found. It does not modify files.

## `validate_manifest.py`

Checks publication manifest structure:

- `PUBLICATION-MANIFEST.md` exists.
- Each book listed in the publication manifest has a directory.
- Each listed book directory has `BOOK-MANIFEST.md`.
- Book 02 has `BOOK-GOVERNANCE.md` and `BOOK-STATUS.md`.

Run:

```bash
python tools/validate_manifest.py
```

The script prints a readable report and exits with a non-zero status if required manifest structure is missing. It does not modify files.

## `package_book.py`

Creates a timestamped zip package for a book directory under `release/rc/`. The package excludes temporary system files such as `.DS_Store`, `Thumbs.db`, `__pycache__`, and Python bytecode files. Original book files are not modified.

Run:

```bash
python tools/package_book.py books/book-02-core-specification
```

The generated zip filename includes the book directory name and a UTC timestamp. Generated zip packages under `release/rc/` are build artifacts and should normally not be committed unless explicitly preparing a publication release.

## Scope

These scripts are validation and packaging helpers only. They do not define repository architecture, expand MVP scope, or change book content.
