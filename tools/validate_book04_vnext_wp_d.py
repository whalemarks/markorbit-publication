#!/usr/bin/env python3
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
 'task':'codex/tasks/PUB-TASK-B04-VNEXT-WP-D.md',
 'plan':'books/book-04-workplace-product-architecture/planning/B04-PLN-0011_Product_and_Network_Interfaces_WP-D.md',
 'amend':'books/book-04-workplace-product-architecture/vnext/manuscript/B04-VNEXT-WPD-0001_Product_and_Network_Interface_Model.md',
 'ledger':'books/book-04-workplace-product-architecture/vnext/B04-CORR-0003_WP-D_Chapter_Correction_Ledger.md',
 'review':'books/book-04-workplace-product-architecture/reviews/B04-REV-0009_Product_and_Network_Interfaces_WP-D_Review.md',
}
PROTECTED = (
 'books/book-04-workplace-product-architecture/manuscript/',
 'books/book-04-workplace-product-architecture/publication/',
 'books/book-04-workplace-product-architecture/figures/',
 'architecture/MARKORBIT-ORBITAL-ARCHITECTURE-CANON-vNEXT.1.md',
 'architecture/DECISION-REGISTER-vNEXT.1.md',
 'books/book-02-core-specification/',
 'books/book-05-markreg/manuscript/', 'books/book-05-markreg/appendices/', 'books/book-05-markreg/specifications/',
 'books/book-06-markorbit-lite/manuscript/', 'books/book-06-markorbit-lite/reader-apparatus/', 'books/book-06-markorbit-lite/specifications/',
 'books/book-07-mark-global-service-network/manuscript/', 'books/book-07-mark-global-service-network/appendices/', 'books/book-07-mark-global-service-network/specifications/',
)

def read(p:str)->str:
 f=ROOT/p
 if not f.is_file(): raise RuntimeError(f'missing required file: {p}')
 return f.read_text(encoding='utf-8')

def run_git(*args:str)->str:
 r=subprocess.run(['git',*args],cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if r.returncode: raise RuntimeError(r.stderr.strip())
 return r.stdout.strip()

def validate_records():
 for p in FILES.values(): read(p)
 text=read(FILES['amend'])
 for term in ('MarkReg self-operated Workplace','lightweight Workplace Product','Sites','MGSN Connection / Gateway','MGSN Network','Originating Workplace','Execution Provider Workplace','candidate surfaced','Provider appointed'):
  if term not in text: raise RuntimeError(f'missing interface term: {term}')
 ledger=read(FILES['ledger'])
 for ch in ('CH23','CH24','CH25','CH33','CH34','CH35'):
  if ch not in ledger: raise RuntimeError(f'missing ledger chapter: {ch}')
 review=read(FILES['review'])
 for x in ('Assigned chapters covered: 6 / 6','Interface profiles explicit: 4 / 4','Blocking findings: 0','RC1 source modification: 0'):
  if x not in review: raise RuntimeError(f'missing review result: {x}')
 print('WP-D records and coverage: PASS')

def validate_diff(base:str|None):
 if not base: return
 changed=run_git('diff','--name-only',f'{base}...HEAD').splitlines()
 bad=[p for p in changed if any(p==x or p.startswith(x) for x in PROTECTED)]
 if bad: raise RuntimeError('protected source changed:\n'+'\n'.join(bad))
 print(f'protected diff: PASS ({len(changed)} files)')

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--base-sha'); a=ap.parse_args()
 try: validate_records(); validate_diff(a.base_sha)
 except RuntimeError as e: print(f'FAIL: {e}',file=sys.stderr); return 1
 print('Book 04 vNext WP-D validation: PASS'); return 0

if __name__=='__main__': raise SystemExit(main())