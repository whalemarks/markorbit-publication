# Style Guide

## Markdown Format Rules

- Use Markdown for repository governance and publication coordination files.
- Use one top-level `#` heading per file.
- Prefer short sections with descriptive headings.
- Use tables for registries, inventories, and status lists.
- Avoid embedding architectural decisions in repository scaffolding files.

## Naming Rules

- Use kebab-case for directory names.
- Use uppercase kebab-case for root governance Markdown files.
- Do not use spaces in file or directory names for new repository-level files.
- Use clear, durable names that describe publication responsibility.

## Path Rules

- Store books under `books/`.
- Store shared publication assets under `shared/`.
- Store review materials under `reviews/`.
- Store release artifacts under `release/`.
- Store Codex prompts, tasks, and reports under `codex/`.

## Book Slug Rules

- Book directories should use the form `book-##-short-title`.
- Use two digits for book numbers.
- Use lowercase kebab-case after the book number.
- Do not rename or move existing book directories without an explicit migration task.

## Review Round Rules

- Review rounds should be recorded under `reviews/`.
- Each review round should identify the book, scope, reviewer role, and outcome.
- Review rounds must not expand manuscript or architecture scope without human approval.
