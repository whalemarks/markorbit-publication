# Book 05 Validation

This directory contains the reproducible structural and rendered validation toolchain for Book 05.

## Controlled Records

- `B05-VAL-0001_PF-08_Structural_and_Rendered_Validation.md` — accepted PF-08 validation baseline;
- `validate_book05.py` — structural, controlled-ID, figure and rendered-output validator;
- `requirements.txt` — pinned Python dependencies;
- `mermaid-config.json` — grayscale Mermaid configuration;
- `puppeteer-config.json` — headless Chromium configuration for CI rendering;
- `reader.css` — validation-edition HTML/PDF stylesheet.

## Reproducible Command

From the repository root:

```bash
python -m pip install -r books/book-05-markreg/validation/requirements.txt
npm install --no-save @mermaid-js/mermaid-cli
python books/book-05-markreg/validation/validate_book05.py
```

The GitHub Actions workflow `.github/workflows/book-05-pf08-validation.yml` additionally installs the browser and Linux rendering dependencies.

## Generated Outputs

The validator writes temporary outputs to:

```text
books/book-05-markreg/build/pf08/
```

The generated directory contains:

- `validation-report.json`;
- `validation-report.md`;
- eleven extracted Mermaid source files;
- eleven rendered SVG files;
- `book-05-reader.html`;
- `book-05-reader.pdf`;
- retained console output.

Generated outputs are CI artifacts and are not canonical manuscript or publication source files.

## Validation Boundary

A passing PF-08 run establishes that the declared structural, identifier, link, Mermaid and rendered-output checks passed for an exact commit and toolchain.

It does not establish:

- current jurisdiction law;
- substantive legal correctness for a live matter;
- software implementation conformance;
- production readiness;
- Release Candidate 1 approval;
- final publication approval;
- External Protected Action authority.

PF-09 remains the owner RC1 and publication Decision.
