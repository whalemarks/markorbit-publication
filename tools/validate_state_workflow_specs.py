#!/usr/bin/env python3
"""Validate Book 02 status value and workflow component specification pack.

Publication/specification validator only; it does not modify files or implement runtime behavior.
"""
from pathlib import Path
import re, sys, subprocess
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'books/book-02-core-specification/core-specs'
errors=[]
def err(file, expected, actual, typ): errors.append((str(file.relative_to(ROOT) if file.is_absolute() else file), expected, actual, typ))
def read(p):
    try: return p.read_text()
    except FileNotFoundError: err(p,'file exists','missing','missing-file'); return ''
status={
'Trademark':('B02-CSV-TRADEMARK-STATUS','trademark-status-values.md','objects/trademark.md',['Draft','Planned','PendingFiling','Filed','UnderExamination','Published','Opposed','Registered','Refused','Abandoned','Cancelled','Expired','Invalidated','RenewalDue','ReviewRequired','Archived','DeletedReferenceOnly']),
'Order':('B02-CSV-ORDER-STATUS','order-status-values.md','objects/order.md',['Draft','PendingConfirmation','Confirmed','ReadyForMatter','MatterCreated','InProgress','WaitingForCustomer','Completed','Cancelled','Archived','DeletedReferenceOnly']),
'Matter':('B02-CSV-MATTER-STATUS','matter-status-values.md','objects/matter.md',['Draft','Open','InProgress','WaitingForCustomer','WaitingForAgent','WaitingForOffice','ReviewRequired','Blocked','Completed','Cancelled','Archived','DeletedReferenceOnly']),
'Task':('B02-CSV-TASK-STATUS','task-status-values.md','objects/task.md',['Draft','Open','Assigned','InProgress','Waiting','Blocked','ReviewRequired','Completed','Cancelled','Archived','DeletedReferenceOnly']),
}
for f in [BASE/'controlled-state-values/index.md', BASE/'workflows/components/index.md']:
    if not f.exists(): err(f,'index exists','missing','missing-index')
seen={}
for name,(sid,file,parent,vals) in status.items():
    p=BASE/'controlled-state-values'/file; txt=read(p)
    if f'Spec ID: {sid}' not in txt: err(p,sid,'missing or different','metadata-spec-id')
    if 'Spec Type: Controlled State Value Specification' not in txt: err(p,'Controlled State Value Specification','missing','metadata-spec-type')
    if any(f'Spec ID: {legacy}' in txt for legacy in ['OBJ-TM-003','OBJ-ORD-004','OBJ-MAT-002','OBJ-TSK-003','OBJ-WFC-002','OBJ-WFC-003']): err(p,'legacy id not used as Spec ID','legacy Spec ID','legacy-id')
    for v in vals:
        if not re.search(rf'(^|\n){re.escape(v)}(\n|$)|\| {re.escape(v)} \|', txt): err(p,f'contains {v}','missing','canonical-value')
    block=re.search(r'# 5\. Canonical Values\s+```text\n(.*?)\n```', txt, re.S)
    actual=[line for line in (block.group(1).splitlines() if block else []) if line]
    if actual != vals: err(p,vals,actual,'canonical-value-list')
    ptxt=read(BASE/parent)
    for v in vals:
        if v not in ptxt: err(BASE/parent,f'parent controlled values include {v}','missing','parent-values')
for sid,file in [('B02-WFC-STATE-DEFINITION','workflow-state-definition.md'),('B02-WFC-TRANSITION-DEFINITION','workflow-transition-definition.md')]:
    p=BASE/'workflows/components'/file; txt=read(p)
    if f'Spec ID: {sid}' not in txt: err(p,sid,'missing or different','metadata-spec-id')
    if 'Spec Type: Workflow Contract Component Specification' not in txt: err(p,'Workflow Contract Component Specification','missing','metadata-spec-type')
trans=read(BASE/'workflows/components/workflow-transition-definition.md')
for v in ['Allowed','Denied','Blocked','ReviewRequired','ApprovalRequired','PermissionRequired','PolicyRequired','InvalidState','InvalidTransition','Unknown']:
    if v not in trans: err(BASE/'workflows/components/workflow-transition-definition.md',f'contains {v}','missing','transition-vocabulary')
# legacy terms only in compatibility notes within transition component/service active values must not contain old BlockedBy* terms
for old in ['BlockedByPermission','BlockedByPolicy','BlockedByGuard']:
    hits=[]
    for p in BASE.rglob('*.md'):
        if old in p.read_text() and p.name not in ['workflow-transition-definition.md','B02-REV-STATUS-TRANSITION-CLASSIFICATION-LOCK.md']: hits.append(str(p.relative_to(ROOT)))
    if hits: err(BASE,f'{old} only in component compatibility mapping',hits,'legacy-transition-term')
# old terminology exact phrase not allowed
for p in [ROOT/'books/book-02-core-specification', ROOT/'books/book-03-execution-system', ROOT/'PUBLICATION-ROADMAP.md', ROOT/'CHANGELOG.md']:
    files=[p] if p.is_file() else p.rglob('*.md')
    for f in files:
        if 'Controlled Value Specification' in f.read_text(): err(f,'no old terminology','Controlled Value Specification','old-terminology')
idx=read(ROOT/'books/book-02-core-specification/indexes/object-index.md')
for link in ['controlled-state-values/trademark-status-values.md','controlled-state-values/order-status-values.md','controlled-state-values/matter-status-values.md','controlled-state-values/task-status-values.md','workflows/components/workflow-state-definition.md','workflows/components/workflow-transition-definition.md']:
    if link not in idx: err(ROOT/'books/book-02-core-specification/indexes/object-index.md',link,'missing','canonical-link')
for legacy in ['OBJ-TM-003','OBJ-ORD-004','OBJ-MAT-002','OBJ-TSK-003','OBJ-WFC-002','OBJ-WFC-003']:
    if re.search(rf'\| {legacy} \|.*\| Active \|', idx): err(ROOT/'books/book-02-core-specification/indexes/object-index.md',f'{legacy} not active','active','object-regression')
if errors:
    for file, exp, act, typ in errors:
        print(f'{typ}: file={file}; expected={exp}; actual={act}')
    sys.exit(1)
print('State/workflow specification validation passed.')
