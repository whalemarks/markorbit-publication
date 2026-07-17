#!/usr/bin/env python3
"""Validate Book 04 vNext Candidate 04 final consistency correction."""
from __future__ import annotations
import argparse, subprocess, sys, tempfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BUILDER=ROOT/"tools/build_book04_vnext_candidate_04.py"
PROTECTED=(
 "books/book-04-workplace-product-architecture/manuscript/",
 "books/book-04-workplace-product-architecture/publication/",
 "architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md",
 "architecture/DECISION-REGISTER-vNEXT.1.md",
 "books/book-02-core-specification/",
 "books/book-05-markreg/manuscript/",
 "books/book-06-markorbit-lite/manuscript/",
 "books/book-07-mark-global-service-network/manuscript/",
)
EXPECTED=(
 "Source Candidate 03 chapters: 40 / 40",
 "Candidate 04 chapters generated: 40 / 40",
 "CH01 navigation corrections: PASS",
 "CH22 transition correction: PASS",
 "Superseded Lite-as-Workplace reader findings: 0",
 "Candidate 03 content preservation exceptions: 2 / 2 authorized",
 "Reader-text leakage findings: 0",
 "Architecture authority regression: 0",
 "RC1 source modifications: 0",
 "Blocking findings: 0",
 "Immediate Book 02 Change Proposal required: NO",
 "Owner Acceptance readiness: YES",
)

class ValidationError(RuntimeError): pass

def git(*args:str)->str:
 r=subprocess.run(["git",*args],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if r.returncode: raise ValidationError(r.stderr.strip())
 return r.stdout.strip()

def validate_generated()->None:
 with tempfile.TemporaryDirectory() as tmp:
  out=Path(tmp)/"candidate04"
  r=subprocess.run([sys.executable,str(BUILDER),"--output",str(out)],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  if r.returncode: raise ValidationError(r.stderr.strip() or r.stdout.strip())
  chapters=sorted((out/"manuscript").glob("CH??.md"))
  if len(chapters)!=40: raise ValidationError(f"expected forty chapters, found {len(chapters)}")
  ch01=(out/"manuscript/CH01.md").read_text(encoding="utf-8")
  ch20=(out/"manuscript/CH20.md").read_text(encoding="utf-8")
  ch22=(out/"manuscript/CH22.md").read_text(encoding="utf-8")
  ch23=(out/"manuscript/CH23.md").read_text(encoding="utf-8")
  ch37=(out/"manuscript/CH37.md").read_text(encoding="utf-8")
  if "Lite as a Lightweight Workplace Product" not in ch01: raise ValidationError("CH01 title not synchronized")
  if "Lite is a lightweight Workplace Product" not in ch01: raise ValidationError("CH01 description not synchronized")
  if "Lite operate as a lightweight Workplace Product" not in ch22: raise ValidationError("CH22 transition not synchronized")
  if "Product Installation as Governed Workplace Participation" not in ch20: raise ValidationError("CH20 Product Installation placement regressed")
  if "Lite as a Lightweight Workplace Product" not in ch23: raise ValidationError("CH23 heading regressed")
  if "Portability, Exit and Revocation Across Orbits" not in ch37: raise ValidationError("CH37 portability structure regressed")
  for path in chapters:
   text=path.read_text(encoding="utf-8")
   if "candidate: B04-vNEXT-CANDIDATE-04" not in text: raise ValidationError(f"{path.name} missing Candidate 04 provenance")
   for line in text.splitlines():
    if "Lite as a Lightweight Workplace" in line and "Workplace Product" not in line:
     raise ValidationError(f"superseded Lite wording remains in {path.name}: {line}")
  report=(out/"BUILD-REPORT.md").read_text(encoding="utf-8")
  for statement in EXPECTED:
   if statement not in report: raise ValidationError(f"build report missing: {statement}")

def validate_diff(base_sha:str|None)->None:
 if not base_sha: return
 changed=git("diff","--name-only",f"{base_sha}...HEAD").splitlines()
 violations=[p for p in changed if any(p==prefix or p.startswith(prefix) for prefix in PROTECTED)]
 if violations: raise ValidationError("protected source changed:\n"+"\n".join(violations))

def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("--base-sha"); a=p.parse_args()
 try:
  validate_generated(); validate_diff(a.base_sha)
 except ValidationError as e:
  print(f"FAIL: {e}",file=sys.stderr); return 1
 print("Book 04 vNext Candidate 04 validation: PASS"); return 0

if __name__=="__main__": raise SystemExit(main())