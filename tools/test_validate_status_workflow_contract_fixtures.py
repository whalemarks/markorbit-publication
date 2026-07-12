#!/usr/bin/env python3
import json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VAL=ROOT/'tools/validate_status_workflow_contract_fixtures.py'
def run(tree): return subprocess.run([sys.executable,str(tree/'tools/validate_status_workflow_contract_fixtures.py')],cwd=tree,text=True,capture_output=True)
def mutate(rel, fn):
 with tempfile.TemporaryDirectory() as td:
  t=Path(td)/'repo'; shutil.copytree(ROOT,t,ignore=shutil.ignore_patterns('.git','__pycache__'))
  p=t/rel; fn(p)
  r=run(t)
  if r.returncode==0: raise AssertionError(f'validator failed to catch mutation {rel}\n{r.stdout}\n{r.stderr}')
def jmut(rel, fn):
 def inner(p):
  d=json.loads(p.read_text()); fn(d); p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
 mutate(rel, inner)
F='books/book-02-core-specification/core-specs/contracts/fixtures/status-workflow/'
C='books/book-02-core-specification/core-specs/contracts/'
# 22 negative cases
jmut(F+'status/trademark/canonical-matrix.json',lambda d:d['expected']['canonical_values'].pop())
jmut(F+'status/trademark/canonical-matrix.json',lambda d:d['expected']['canonical_values'].append('UnknownStatus'))
jmut(F+'status/order/canonical-matrix.json',lambda d:d['expected']['allowed_transitions'].pop())
jmut(F+'status/order/canonical-matrix.json',lambda d:d['expected']['allowed_transitions'].append({'from':'Confirmed','to':'Draft'}))
mutate(C+'status/matter-status-contract.md',lambda p:p.write_text(p.read_text().replace('Draft -> Open','Draft -> Completed')))
mutate(C+'workflows/components/workflow-state-definition-contract.md',lambda p:p.write_text(p.read_text().replace('  state_key: required\n','')))
mutate(C+'workflows/components/workflow-transition-definition-contract.md',lambda p:p.write_text(p.read_text().replace('  owning_service_reference: required\n','')))
mutate(C+'status/status-transition-contract.md',lambda p:p.write_text(p.read_text().replace('InvalidTransition','InvalidTransitionDrift')))
jmut(F+'manifest.json',lambda d:d['fixtures'].__setitem__(1,{**d['fixtures'][1],'fixture_id':d['fixtures'][0]['fixture_id']}))
jmut(F+'manifest.json',lambda d:d['fixtures'][0].__setitem__('path','missing.json'))
mutate(F+'status/task/valid-open-to-assigned.json',lambda p:p.rename(p.with_name('orphan-extra.json')))
jmut(F+'status/task/valid-open-to-assigned.json',lambda d:d.__setitem__('target_contract_id','B02-CONTRACT-MISSING'))
jmut(F+'status/task/valid-open-to-assigned.json',lambda d:d.__setitem__('synthetic',False))
jmut(F+'status/task/valid-open-to-assigned.json',lambda d:d.__setitem__('contains_production_data',True))
jmut(F+'status/order/valid-pending-confirmation-to-confirmed.json',lambda d:d['input'].update({'current_status':'Confirmed','requested_status':'Draft'}))
jmut(F+'status/order/invalid-confirmed-to-draft.json',lambda d:d['input'].update({'current_status':'PendingConfirmation','requested_status':'Confirmed'}))
jmut(F+'workflow/protected-external-action-denied.json',lambda d:d['expected'].__setitem__('decision','Allowed'))
jmut(F+'workflow/valid-transition-definition.json',lambda d:d['expected'].__setitem__('mutation_performed',True))
jmut(F+'status/task/valid-governed-reopen-to-open.json',lambda d:d['input'].__setitem__('requested_status','Reopened'))
jmut(F+'status/order/valid-accept-order-to-confirmed.json',lambda d:d['input'].__setitem__('requested_status','Accepted'))
jmut(F+'status/trademark/valid-official-source-to-registered.json',lambda d:d['input'].__setitem__('source_context',{}))
jmut(F+'status/task/valid-open-to-assigned.json',lambda d:d.__setitem__('password','secret'))
print('Negative status/workflow fixture validator tests passed: 22')
