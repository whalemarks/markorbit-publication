# Repository Validation Tools

This directory contains lightweight validation and packaging helpers for the MarkOrbit publication repository. These scripts inspect repository structure or create release artifacts; they do not define architecture, rewrite specifications, or modify book content.

All scripts use only the Python standard library.

## `validate_links.py`

Scans Markdown files, validates internal Markdown links ending in `.md`, and reports links whose target files do not exist. The checker supports repository-wide validation, path-scoped validation, normal links relative to the source file, repository-root links such as `books/...`, and book-internal links written relative to the book root.

Strict Markdown link mode is the default. In this mode, the script validates only actual inline Markdown links such as:

- `[text](path.md)`
- `[text](../path.md)`
- `[text](folder/file.md#anchor)`

Strict mode does not treat plain-text paths as broken links, does not validate links inside fenced code blocks, and does not report future or planned references unless they are written as actual Markdown links.

Run repository-wide validation:

```bash
python tools/validate_links.py
```

Run book-scoped validation:

```bash
python tools/validate_links.py books/book-03-execution-system
python tools/validate_links.py books/book-02-core-specification
```

Limit report detail while still showing total counts:

```bash
python tools/validate_links.py --max-report 200
```

Optionally scan plain-text `.md` paths as warnings:

```bash
python tools/validate_links.py --include-plain-paths
```

Plain-text path warnings are optional and do not affect the exit status. The script exits with a non-zero status only when actual inline Markdown links are broken in the selected scope. It does not modify files.

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
