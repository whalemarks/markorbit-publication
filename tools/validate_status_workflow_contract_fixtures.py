#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'books/book-02-core-specification/core-specs'
FIX=BASE/'contracts/fixtures/status-workflow'
DEC={'Allowed','Denied','Blocked','ReviewRequired','ApprovalRequired','PermissionRequired','PolicyRequired','InvalidState','InvalidTransition','Unknown'}
REQ={'fixture_id','fixture_version','fixture_type','target_contract_id','target_spec_id','case_type','synthetic','contains_production_data','input','expected'}
errs=[]
def err(file,vid,typ,exp,act): errs.append((str(file),vid or '',typ,str(exp),str(act)))
def spec(n):
 t=(BASE/f'controlled-state-values/{n}-status-values.md').read_text()
 vals=re.search(r'# 5\. Canonical Values\n\n```text\n(.*?)```',t,re.S).group(1).split()
 trans=[{'from':a,'to':b} for a,b in re.findall(r'(\w+) -> (\w+)',re.search(r'# 10\. Transition Model\n\n```text\n(.*?)```',t,re.S).group(1))]
 return vals,trans
def blockvals(text):
 m=re.search(r'# 4\. Canonical Values\n```text\n(.*?)```',text,re.S); return m.group(1).split() if m else []
def blocktrans(text):
 m=re.search(r'# 5\. Allowed Transitions\n```text\n(.*?)```',text,re.S); return [{'from':a,'to':b} for a,b in re.findall(r'(\w+) -> (\w+)',m.group(1) if m else '')]
def main():
 for f in ['README.md','template.md','index.md','status-transition-contract.md','trademark-status-contract.md','order-status-contract.md','matter-status-contract.md','task-status-contract.md']:
  if not (BASE/'contracts/status'/f).exists(): err(f,None,'missing_status_contract_file','exists','missing')
 for f in ['README.md','template.md','index.md','workflow-state-definition-contract.md','workflow-transition-definition-contract.md']:
  if not (BASE/'contracts/workflows/components'/f).exists(): err(f,None,'missing_workflow_component_contract_file','exists','missing')
 ids={}
 for p in (BASE/'contracts').rglob('*.md'):
  for sid in re.findall(r'^Spec ID:\s*(\S+)',p.read_text(errors='ignore'),re.M):
   if sid in ids: err(p,None,'duplicate_spec_id','unique',sid)
   ids[sid]=p
  if 'Spec Type: Contract Specification' in p.read_text(errors='ignore') and 'Contract Version:' not in p.read_text(errors='ignore'):
   err(p,None,'missing_contract_version','Contract Version','missing')
 for n in ['trademark','order','matter','task']:
  vals,tr=spec(n); p=BASE/f'contracts/status/{n}-status-contract.md'; txt=p.read_text()
  if blockvals(txt)!=vals: err(p,None,'domain_contract_values_drift',vals,blockvals(txt))
  if blocktrans(txt)!=tr: err(p,None,'domain_contract_transition_drift',tr,blocktrans(txt))
 st=(BASE/'contracts/workflows/components/workflow-state-definition-contract.md').read_text();
 for fld in re.search(r'# Required Fields\n\n```text\n(.*?)```',(BASE/'workflows/components/workflow-state-definition.md').read_text(),re.S).group(1).split():
  if f'  {fld}: required' not in st: err('workflow-state-definition-contract.md',None,'missing_workflow_state_field',fld,'missing')
 wt=(BASE/'contracts/workflows/components/workflow-transition-definition-contract.md').read_text();
 for fld in re.search(r'# Required Fields\n\n```text\n(.*?)```',(BASE/'workflows/components/workflow-transition-definition.md').read_text(),re.S).group(1).split():
  if f'  {fld}: required' not in wt: err('workflow-transition-definition-contract.md',None,'missing_workflow_transition_field',fld,'missing')
 status_decision_text=(BASE/'contracts/status/status-transition-contract.md').read_text()
 for d in DEC:
  if not re.search(r'(?<![A-Za-z])'+re.escape(d)+r'(?![A-Za-z])', wt): err('workflow-transition-definition-contract.md',None,'decision_vocabulary_drift',d,'missing')
  if not re.search(r'(?<![A-Za-z])'+re.escape(d)+r'(?![A-Za-z])', status_decision_text): err('status-transition-contract.md',None,'decision_vocabulary_drift',d,'missing')
 if 'mutation_performed: false' not in wt: err('workflow-transition-definition-contract.md',None,'workflow_mutation_performed_rule','mutation_performed: false','missing')
 manp=FIX/'manifest.json'
 try: man=json.loads(manp.read_text())
 except Exception as e: err(manp,None,'manifest_invalid','valid json',e); man={'fixtures':[]}
 paths=[]; fids=set()
 if not man.get('synthetic'): err(manp,None,'manifest_synthetic_true',True,man.get('synthetic'))
 if man.get('contains_production_data'): err(manp,None,'manifest_production_false',False,man.get('contains_production_data'))
 actual={p.relative_to(FIX).as_posix() for p in FIX.rglob('*.json') if p.name!='manifest.json'}
 for item in man.get('fixtures',[]):
  path=item.get('path'); paths.append(path)
  if path not in actual: err(manp,item.get('fixture_id'),'manifest_path_missing','existing file',path)
  if item.get('fixture_id') in fids: err(manp,item.get('fixture_id'),'duplicate_fixture_id','unique',item.get('fixture_id'))
  fids.add(item.get('fixture_id'))
 for o in actual-set(paths): err(FIX/o,None,'orphan_fixture','listed in manifest','not listed')
 for rel in actual:
  p=FIX/rel
  try: data=json.loads(p.read_text())
  except Exception as e: err(p,None,'fixture_json_invalid','valid json',e); continue
  fid=data.get('fixture_id')
  if set(data)!=REQ: err(p,fid,'envelope_fields',sorted(REQ),sorted(data))
  if data.get('fixture_id') in [x for x in fids if list(fids).count(x)>1]: pass
  if data.get('synthetic') is not True: err(p,fid,'synthetic_true',True,data.get('synthetic'))
  if data.get('contains_production_data') is not False: err(p,fid,'production_data_false',False,data.get('contains_production_data'))
  if data.get('target_contract_id') not in ids: err(p,fid,'target_contract_missing','known contract',data.get('target_contract_id'))
  if re.search(r'password|token|secret|api[_-]?key',p.read_text(),re.I): err(p,fid,'secret_pattern_absent','no secret-like fields','present')
  if data.get('fixture_type')=='StatusMatrix':
   n=rel.split('/')[1]; vals,tr=spec(n)
   if data['expected'].get('canonical_values')!=vals: err(p,fid,'matrix_values_drift',vals,data['expected'].get('canonical_values'))
   if data['expected'].get('allowed_transitions')!=tr: err(p,fid,'matrix_transition_drift',tr,data['expected'].get('allowed_transitions'))
  if data.get('fixture_type')=='StatusTransition':
   n=rel.split('/')[1]; vals,tr=spec(n); inp=data['input']; edge={'from':inp.get('current_status'),'to':inp.get('requested_status')}; dec=data['expected'].get('decision')
   if edge['from'] not in vals or edge['to'] not in vals: err(p,fid,'scenario_status_not_canonical',vals,edge)
   if data['case_type']=='positive' and edge not in tr: err(p,fid,'allowed_fixture_invalid_transition','edge in matrix',edge)
   if 'invalid' in rel and edge in tr: err(p,fid,'invalid_fixture_allowed_transition','edge not in matrix',edge)
   if n=='task' and 'reopen' in rel and edge not in [{'from':'Completed','to':'Open'},{'from':'Cancelled','to':'Open'}]: err(p,fid,'task_reopen_invalid','Completed/Cancelled -> Open',edge)
   if n=='order' and 'accept' in rel and edge!={'from':'PendingConfirmation','to':'Confirmed'}: err(p,fid,'order_accept_invalid','PendingConfirmation -> Confirmed',edge)
   if n=='trademark' and 'official-source' in rel:
    sc=inp.get('source_context') or {}; need=['source_reference_id','source_version_or_timestamp','jurisdiction_reference_id','normalization_evidence_reference_id']
    if not all(sc.get(k) for k in need): err(p,fid,'trademark_official_source_missing',need,sc)
  if data.get('fixture_type')=='WorkflowTransitionValidation':
   dec=data['expected'].get('decision')
   if data['expected'].get('mutation_performed') is True: err(p,fid,'workflow_mutation_performed_false',False,True)
   if 'protected-external-action' in rel and dec=='Allowed': err(p,fid,'protected_external_action_denied','non-Allowed',dec)
 if errs:
  for e in errs: print('\t'.join(e))
  return 1
 print('Status/workflow contract fixtures validation passed')
 return 0
if __name__=='__main__': sys.exit(main())
