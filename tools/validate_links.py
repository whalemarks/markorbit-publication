#!/usr/bin/env python3
"""Validate internal Markdown file references without modifying the repository."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]

INLINE_LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]]+\]:\s+(.+)$", re.MULTILINE)
BOOKS_PART = f"{Path('books').as_posix()}/"
BARE_TOKEN_RE = re.compile(r"(?<![\w:/.-])([A-Za-z0-9_./-]+\.md(?:#[A-Za-z0-9_.%\-]+)?)")
MAX_MISSING_DETAILS = 100


@dataclass(frozen=True)
class MissingReference:
    source: Path
    line: int
    target: str
    attempted: tuple[Path, ...]


def markdown_files() -> list[Path]:
    ignored_parts = {'.git', '__pycache__'}
    return sorted(
        path for path in REPO_ROOT.rglob('*.md')
        if not ignored_parts.intersection(path.relative_to(REPO_ROOT).parts)
    )


def strip_anchor(target: str) -> str:
    return unquote(target.split('#', 1)[0])


def is_internal_markdown(target: str) -> bool:
    lowered = target.lower()
    if '://' in lowered or lowered.startswith(('mailto:', 'tel:', '#')):
        return False
    return strip_anchor(target).lower().endswith('.md')


def book_root_for(path: Path) -> Path | None:
    relative = path.relative_to(REPO_ROOT)
    parts = relative.parts
    if len(parts) >= 3 and parts[0] == 'books':
        return REPO_ROOT / parts[0] / parts[1]
    return None


def candidate_paths(source: Path, target: str) -> list[Path]:
    clean = strip_anchor(target).strip().lstrip('/')
    target_path = Path(clean)
    candidates: list[Path] = []

    if target_path.is_absolute():
        candidates.append(target_path)
    else:
        # Repository-global references, including paths beginning with books/.
        candidates.append(REPO_ROOT / target_path)
        # Normal Markdown-relative references.
        candidates.append(source.parent / target_path)
        # Book-internal references may omit the book directory prefix.
        book_root = book_root_for(source)
        if book_root is not None and not clean.startswith(BOOKS_PART):
            candidates.append(book_root / target_path)
            if len(target_path.parts) == 1:
                candidates.extend(book_root.rglob(target_path.name))

    deduped: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve(strict=False)
        if resolved not in seen:
            seen.add(resolved)
            deduped.append(resolved)
    return deduped


def find_targets(text: str) -> list[tuple[int, str]]:
    targets: list[tuple[int, str]] = []
    for regex in (INLINE_LINK_RE, REFERENCE_LINK_RE, BARE_TOKEN_RE):
        for match in regex.finditer(text):
            target = match.group(1).strip()
            if ' \"' in target or " '" in target:
                target = re.split(r'\s+[\"\']', target, 1)[0]
            target = target.strip('<>')
            if is_internal_markdown(target):
                line = text.count('\n', 0, match.start(1)) + 1
                targets.append((line, target))
    return targets


def main() -> int:
    checked = 0
    missing: list[MissingReference] = []

    for source in markdown_files():
        text = source.read_text(encoding='utf-8')
        for line, target in find_targets(text):
            checked += 1
            candidates = candidate_paths(source, target)
            if not any(candidate.is_file() for candidate in candidates):
                missing.append(MissingReference(source, line, target, tuple(candidates)))

    print('Markdown Link Validation Report')
    print('================================')
    print(f'Repository root: {REPO_ROOT}')
    print(f'Markdown files scanned: {len(markdown_files())}')
    print(f'Internal .md references checked: {checked}')
    print(f'Missing references: {len(missing)}')

    if missing:
        print('\nMissing internal Markdown references:')
        for item in missing[:MAX_MISSING_DETAILS]:
            rel_source = item.source.relative_to(REPO_ROOT)
            attempted = ', '.join(str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path) for path in item.attempted)
            print(f'- {rel_source}:{item.line} -> {item.target}')
            print(f'  attempted: {attempted}')
        if len(missing) > MAX_MISSING_DETAILS:
            print(f'... {len(missing) - MAX_MISSING_DETAILS} additional missing references omitted from detail output.')
        return 1

    print('\nNo missing internal Markdown references found.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
