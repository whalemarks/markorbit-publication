#!/usr/bin/env python3
"""Preflight pagination-optimized PDF review editions."""
from pathlib import Path
from tools import preflight_portfolio_review_editions_01 as base

base.OUT = Path(__file__).resolve().parents[1] / ".artifacts/portfolio-pagination-optimization-01"

if __name__ == "__main__":
    raise SystemExit(base.main())
