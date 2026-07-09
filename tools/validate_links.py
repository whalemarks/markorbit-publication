#!/usr/bin/env python3
"""Validate internal Markdown links without modifying the repository."""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
BOOKS_PART = f"{Path('books').as_posix()}/"
DEFAULT_MAX_REPORT = 100

# Strict mode validates only inline Markdown links, not plain-text paths.
INLINE_MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
BARE_TOKEN_RE = re.compile(r"(?<![\w:/.-])([A-Za-z0-9_./-]+\.md(?:#[A-Za-z0-9_.%\-]+)?)")


@dataclass(frozen=True)
class MissingReference:
    source: Path
    line: int
    target: str
    attempted: tuple[Path, ...]
    kind: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Validate internal Markdown links in the repository or under a path scope.'
    )
    parser.add_argument(
        'scope',
        nargs='?',
        default='.',
        help='Optional path scope to scan, such as books/book-03-execution-system.',
    )
    parser.add_argument(
        '--include-plain-paths',
        action='store_true',
        help='Also scan plain-text .md paths outside code blocks as warnings.',
    )
    parser.add_argument(
        '--max-report',
        type=int,
        default=DEFAULT_MAX_REPORT,
        help=f'Maximum missing-reference examples to print (default: {DEFAULT_MAX_REPORT}).',
    )
    return parser.parse_args()


def resolve_scope(scope: str) -> Path:
    scope_path = Path(scope).expanduser()
    if not scope_path.is_absolute():
        scope_path = REPO_ROOT / scope_path
    resolved = scope_path.resolve(strict=False)
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise SystemExit(f'error: scope must be inside repository root: {scope}') from exc
    if not resolved.exists():
        raise SystemExit(f'error: scope does not exist: {scope}')
    return resolved


def markdown_files(scope: Path) -> list[Path]:
    ignored_parts = {'.git', '__pycache__'}
    if scope.is_file():
        candidates = [scope] if scope.suffix.lower() == '.md' else []
    else:
        candidates = sorted(scope.rglob('*.md'))
    return [
        path for path in candidates
        if not ignored_parts.intersection(path.relative_to(REPO_ROOT).parts)
    ]


def strip_anchor(target: str) -> str:
    return unquote(target.split('#', 1)[0])


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if ' "' in target or " '" in target:
        target = re.split(r'\s+["\']', target, 1)[0]
    return target.strip('<>')


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
        # Normal Markdown-relative references.
        candidates.append(source.parent / target_path)
        # Book-internal references may be written relative to the book root.
        book_root = book_root_for(source)
        if book_root is not None and not clean.startswith(BOOKS_PART):
            candidates.append(book_root / target_path)
        # Repository-global references, including paths beginning with books/.
        candidates.append(REPO_ROOT / target_path)

    deduped: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve(strict=False)
        if resolved not in seen:
            seen.add(resolved)
            deduped.append(resolved)
    return deduped


def code_mask(text: str) -> list[bool]:
    """Return a per-character mask that is True inside Markdown code."""
    mask = [False] * len(text)
    in_fence = False
    fence_marker = ''
    fence_len = 0
    line_start = 0

    for line in text.splitlines(keepends=True):
        line_end = line_start + len(line)
        stripped = line.lstrip(' \t')
        is_fence_line = stripped.startswith(('```', '~~~'))

        if in_fence:
            mask[line_start:line_end] = [True] * len(line)

        if is_fence_line:
            marker = stripped[0]
            marker_len = len(stripped) - len(stripped.lstrip(marker))
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_len = marker_len
                mask[line_start:line_end] = [True] * len(line)
            elif marker == fence_marker and marker_len >= fence_len:
                in_fence = False
        elif not in_fence:
            # Inline code spans are examples or literal text, not links to validate.
            for match in re.finditer(r'`+[^`]*`+', line):
                span_start = line_start + match.start()
                span_end = line_start + match.end()
                mask[span_start:span_end] = [True] * (span_end - span_start)

        line_start = line_end
    return mask


def find_markdown_links(text: str) -> list[tuple[int, str]]:
    mask = code_mask(text)
    targets: list[tuple[int, str]] = []
    for match in INLINE_MARKDOWN_LINK_RE.finditer(text):
        if mask and mask[match.start()]:
            continue
        target = normalize_target(match.group(1))
        if is_internal_markdown(target):
            line = text.count('\n', 0, match.start(1)) + 1
            targets.append((line, target))
    return targets


def find_plain_paths(text: str) -> list[tuple[int, str]]:
    mask = code_mask(text)
    targets: list[tuple[int, str]] = []
    link_spans = [match.span(1) for match in INLINE_MARKDOWN_LINK_RE.finditer(text)]
    for match in BARE_TOKEN_RE.finditer(text):
        if mask and mask[match.start()]:
            continue
        if any(start <= match.start(1) < end for start, end in link_spans):
            continue
        target = normalize_target(match.group(1))
        if is_internal_markdown(target):
            line = text.count('\n', 0, match.start(1)) + 1
            targets.append((line, target))
    return targets


def format_path(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT)) if path.is_relative_to(REPO_ROOT) else str(path)


def print_missing(title: str, missing: list[MissingReference], max_report: int) -> None:
    if not missing:
        return
    print(f'\n{title}:')
    for item in missing[:max_report]:
        attempted = ', '.join(format_path(path) for path in item.attempted)
        print(f'- {format_path(item.source)}:{item.line} -> {item.target}')
        print(f'  attempted: {attempted}')
    if len(missing) > max_report:
        print(f'... {len(missing) - max_report} additional missing references omitted from detail output.')


def collect_missing(files: list[Path], include_plain_paths: bool) -> tuple[int, int, list[MissingReference], list[MissingReference]]:
    checked_links = 0
    checked_plain = 0
    missing_links: list[MissingReference] = []
    missing_plain: list[MissingReference] = []

    for source in files:
        text = source.read_text(encoding='utf-8')
        for line, target in find_markdown_links(text):
            checked_links += 1
            candidates = candidate_paths(source, target)
            if not any(candidate.is_file() for candidate in candidates):
                missing_links.append(MissingReference(source, line, target, tuple(candidates), 'markdown-link'))
        if include_plain_paths:
            for line, target in find_plain_paths(text):
                checked_plain += 1
                candidates = candidate_paths(source, target)
                if not any(candidate.is_file() for candidate in candidates):
                    missing_plain.append(MissingReference(source, line, target, tuple(candidates), 'plain-path'))
    return checked_links, checked_plain, missing_links, missing_plain


def main() -> int:
    args = parse_args()
    if args.max_report < 0:
        raise SystemExit('error: --max-report must be zero or greater')

    scope = resolve_scope(args.scope)
    files = markdown_files(scope)
    checked_links, checked_plain, missing_links, missing_plain = collect_missing(files, args.include_plain_paths)

    print('Markdown Link Validation Report')
    print('================================')
    print(f'Repository root: {REPO_ROOT}')
    print(f'Scope: {format_path(scope)}')
    print(f'Markdown files scanned: {len(files)}')
    print(f'Inline Markdown .md links checked: {checked_links}')
    print(f'Missing inline Markdown links: {len(missing_links)}')
    if args.include_plain_paths:
        print(f'Plain-text .md paths checked as warnings: {checked_plain}')
        print(f'Missing plain-text .md path warnings: {len(missing_plain)}')

    print_missing('Missing inline Markdown links', missing_links, args.max_report)
    print_missing('Missing plain-text .md path warnings', missing_plain, args.max_report)

    if missing_links:
        return 1

    print('\nNo missing inline Markdown links found.')
    if missing_plain:
        print('Plain-text path warnings do not affect the exit status.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
