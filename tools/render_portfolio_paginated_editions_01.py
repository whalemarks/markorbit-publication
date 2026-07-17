#!/usr/bin/env python3
"""Render pagination-optimized review editions without changing frozen sources."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import render_portfolio_review_editions_01 as base  # noqa: E402

base.OUT = ROOT / ".artifacts/portfolio-pagination-optimization-01"
base.CSS_TEXT = r"""
@page { size: 6in 9in; margin: 0.62in 0.55in 0.62in 0.65in; @bottom-center { content: counter(page); font-size: 7.5pt; color: #555; } }
@page :first { @bottom-center { content: none; } }
html { font-family: "DejaVu Serif", "Liberation Serif", serif; font-size: 9.6pt; line-height: 1.34; }
body { margin: 0; color: #111; }
.cover { page-break-after: always; min-height: 7.25in; display: flex; flex-direction: column; justify-content: space-between; }
.series { font-family: "DejaVu Sans", sans-serif; font-size: 8.5pt; letter-spacing: .08em; text-transform: uppercase; }
.book-code { font-family: "DejaVu Sans", sans-serif; font-size: 32pt; font-weight: 700; margin-top: 1.1in; }
.front-matter { page-break-after: always; }
.manuscript-section { page-break-before: always; }
h1 { font-family: "DejaVu Sans", sans-serif; font-size: 20pt; line-height: 1.1; margin: 0 0 12pt; page-break-before: auto; page-break-after: avoid; }
h2 { font-family: "DejaVu Sans", sans-serif; font-size: 14pt; line-height: 1.18; margin: 13pt 0 6pt; page-break-after: avoid; }
h3 { font-family: "DejaVu Sans", sans-serif; font-size: 11.5pt; margin: 10pt 0 4pt; page-break-after: avoid; }
h4 { font-family: "DejaVu Sans", sans-serif; font-size: 10pt; margin: 9pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 5.2pt; orphans: 2; widows: 2; }
ul, ol { margin: 4pt 0 6pt 17pt; padding: 0; }
li { margin-bottom: 1.5pt; }
blockquote { margin: 7pt 0; padding: 6pt 9pt; border-left: 2pt solid #777; background: #f4f4f4; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font-family: "DejaVu Sans Mono", monospace; font-size: 7.8pt; line-height: 1.22; background: #f2f2f2; padding: 6pt; page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: .88em; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 8pt; font-size: 8pt; }
tr { page-break-inside: avoid; }
th, td { border: .5pt solid #888; padding: 3pt; vertical-align: top; overflow-wrap: anywhere; }
th { font-family: "DejaVu Sans", sans-serif; background: #ededed; }
img { display: block; max-width: 100%; max-height: 6.7in; margin: 7pt auto; page-break-inside: avoid; }
hr { border: 0; border-top: .5pt solid #999; margin: 12pt 0; }
a { color: inherit; text-decoration: none; }
.source-file { display: none; }
"""

if __name__ == "__main__":
    raise SystemExit(base.main())
