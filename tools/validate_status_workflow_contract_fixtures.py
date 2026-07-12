#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
DECISIONS=['Allowed','Denied','Blocked','ReviewRequired','ApprovalRequired','PermissionRequired','PolicyRequired','InvalidState','InvalidTransition','Unknown']
FIXTURE_TYPES={'StatusMatrix','StatusTransition','WorkflowStateDefinition','WorkflowTransitionDefinition','WorkflowTransitionValidation'}
CASE_TYPES={'positive','negative'}
ENVELOPE={'fixture_id','fixture_version','fixture_type','target_contract_id','target_spec_id','case_type','synthetic','contains_production_data','input','expected'}
MANIFEST_KEYS={'fixture_pack_id','fixture_pack_version','synthetic','contains_production_data','fixtures'}
MANIFEST_ENTRY={'fixture_id','path','fixture_type','target_contract_id','target_spec_id','case_type'}
DOMAINS={'trademark':('Trademark','B02-CONTRACT-STATUS-TRADEMARK','B02-CSV-TRADEMARK-STATUS','Trademark Service','TrademarkStatusChanged'), 'order':('Order','B02-CONTRACT-STATUS-ORDER','B02-CSV-ORDER-STATUS','Order Service','OrderStatusChanged'), 'matter':('Matter','B02-CONTRACT-STATUS-MATTER','B02-CSV-MATTER-STATUS','Matter Service','MatterStatusChanged'), 'task':('Task','B02-CONTRACT-STATUS-TASK','B02-CSV-TASK-STATUS','Task Service','TaskStatusChanged')}
STATE_FIELDS={'state_key':str,'display_name':str,'meaning':str,'state_category':str,'is_initial':bool,'is_terminal':bool,'is_active':bool,'entry_requirements':list,'exit_requirements':list,'allowed_actor_types':list,'required_permission_references':list,'required_policy_references':list,'required_review_references':list,'required_approval_references':list,'required_document_references':list,'required_evidence_references':list,'required_event_references':list,'external_action_boundary':str,'metadata':(dict,type(None))}
WF_REQ_FIELDS={'workflow_contract_reference_id':str,'workflow_contract_version':str,'transition_key':(str,type(None)),'current_state_key':str,'requested_state_key':str,'target_object_type':str,'target_object_reference_id':str,'actor_reference_id':(str,type(None)),'permission_decision_reference_id':(str,type(None)),'policy_decision_reference_id':(str,type(None)),'human_review_reference_id':(str,type(None)),'approval_reference_id':(str,type(None)),'idempotency_key':(str,type(None)),'correlation_id':(str,type(None))}
SECRET_KEYS={'password','passwd','secret','client_secret','access_token','refresh_token','api_key','private_key','credential'}
@dataclass
class ValidationError:
    file: str; fixture_id: str|None; violation_type: str; expected: Any; actual: Any
    def line(self)->str:
        return f"file={self.file}\nfixture_id={self.fixture_id or 'none'}\nviolation_type={self.violation_type}\nexpected={self.expected}\nactual={self.actual}"
class Ctx:
    def __init__(self, root: Path):
        self.root=root; self.base=root/'books/book-02-core-specification/core-specs'; self.fix=self.base/'contracts/fixtures/status-workflow'; self.errors:list[ValidationError]=[]; self.contract_ids={}; self.spec_ids={}
    def err(self,p:Path|str,fid:str|None,typ:str,exp:Any,act:Any): self.errors.append(ValidationError(str(p),fid,typ,exp,act))
def read_json(ctx:Ctx,p:Path)->Any:
    try: return json.loads(p.read_text())
    except Exception as e: ctx.err(p,None,'json-invalid','valid JSON',repr(e)); return None
def spec_status(ctx:Ctx,n:str):
    t=(ctx.base/f'controlled-state-values/{n}-status-values.md').read_text(); vals=re.search(r'# 5\. Canonical Values\n\n```text\n(.*?)```',t,re.S).group(1).split(); trs=[{'from':a,'to':b} for a,b in re.findall(r'(\w+) -> (\w+)',re.search(r'# 10\. Transition Model\n\n```text\n(.*?)```',t,re.S).group(1))]; return vals,trs
def contract_block(p:Path,title:str)->str:
    m=re.search(r'# \d+\. '+re.escape(title)+r'\n\n(.*?)(?=\n# \d+\. |\Z)',p.read_text(),re.S); return m.group(1).strip() if m else ''
def values_from_contract(p:Path): return re.search(r'# 10\. Canonical Values\n\n```text\n(.*?)```',p.read_text(),re.S).group(1).split()
def transitions_from_contract(p:Path): return [{'from':a,'to':b} for a,b in re.findall(r'(\w+) -> (\w+)', re.search(r'# 11\. Allowed Transitions\n\n```text\n(.*?)```',p.read_text(),re.S).group(1))]
def validate_contracts(ctx:Ctx):
    req_status=['README.md','template.md','index.md','status-transition-contract.md','trademark-status-contract.md','order-status-contract.md','matter-status-contract.md','task-status-contract.md']
    req_wf=['README.md','template.md','index.md','workflow-state-definition-contract.md','workflow-transition-definition-contract.md']
    for f in req_status:
        if not (ctx.base/'contracts/status'/f).exists(): ctx.err(f,None,'required-file-missing','exists','missing')
    for f in req_wf:
        if not (ctx.base/'contracts/workflows/components'/f).exists(): ctx.err(f,None,'required-file-missing','exists','missing')
    for p in ctx.base.rglob('*.md'):
        text=p.read_text(errors='ignore')
        for sid in re.findall(r'^Spec ID:\s*(\S+)',text,re.M):
            if sid in {'Spec','{spec_id}',''}:
                continue
            if sid in ctx.spec_ids: ctx.err(p,None,'spec-id-duplicate','unique',sid)
            ctx.spec_ids[sid]=p
            if sid.startswith('B02-CONTRACT-'): ctx.contract_ids[sid]=p
    expected_ids={'B02-CONTRACT-STATUS-TRANSITION','B02-CONTRACT-STATUS-TRADEMARK','B02-CONTRACT-STATUS-ORDER','B02-CONTRACT-STATUS-MATTER','B02-CONTRACT-STATUS-TASK','B02-CONTRACT-WORKFLOW-STATE-DEFINITION','B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION'}
    for eid in expected_ids:
        if eid not in ctx.contract_ids: ctx.err('contracts',None,'expected-contract-id-missing',eid,'missing')
    required_sections=['Purpose','Contract Meaning','Contract Boundary','Canonical Source','Parent Ownership','Owning Service','Transition Request Shape','Transition Decision Shape','Transition Result Shape','Canonical Values','Allowed Transitions','Guard Requirements','Permission and Policy','Human Review and Approval','Source and Evidence Requirements','Idempotency','Event and Audit Trace','API Consumption','AI Boundary','Compatibility and Versioning','Error Semantics','Fixture Requirements','Valid Examples','Invalid Examples','Prohibited Overreach','Acceptance Criteria','Revision Notes']
    for n,(_,cid,sid,_,_) in DOMAINS.items():
        p=ctx.base/f'contracts/status/{n}-status-contract.md'; text=p.read_text()
        if f'Contract File: core-specs/contracts/status/{n}-status-contract.md' not in text: ctx.err(p,None,'contract-file-canonical-path',f'core-specs/contracts/status/{n}-status-contract.md','missing')
        if 'Contract Version: v0.1.0' not in text: ctx.err(p,None,'contract-version-missing','Contract Version: v0.1.0','missing')
        for s in required_sections:
            if not re.search(r'# \d+\. '+re.escape(s)+r'\n',text): ctx.err(p,None,'contract-section-missing',s,'missing')
        vals,trs=spec_status(ctx,n)
        if values_from_contract(p)!=vals: ctx.err(p,None,'domain-contract-values-drift',vals,values_from_contract(p))
        if transitions_from_contract(p)!=trs: ctx.err(p,None,'domain-contract-transitions-drift',trs,transitions_from_contract(p))
        if f'](../../controlled-state-values/{n}-status-values.md)' not in text: ctx.err(p,None,'related-spec-link-missing',f'{n}-status-values.md','missing')
    sp=ctx.base/'contracts/status/status-transition-contract.md'; st=sp.read_text()
    shared_sections=['Purpose','Contract Meaning','Contract Boundary','Related Owning Specifications','Supported Subject Types','Required References','Transition Request Shape','Transition Request Field Rules','Transition Decision Shape','Canonical Decision Vocabulary','Transition Decision Rules','Transition Result Shape','Transition Result Rules','Owning Service Mutation Boundary','Permission and Policy','Human Review and Approval','Source and Evidence','Idempotency','Event and Audit Trace','AI Boundary','Compatibility and Versioning','Error Semantics','Fixture Requirements','Valid Examples','Invalid Examples','Prohibited Overreach','Acceptance Criteria','Revision Notes']
    for s in shared_sections:
        if not re.search(r'# \d+\. '+re.escape(s)+r'\n',st): ctx.err(sp,None,'shared-contract-section-missing',s,'missing')
    actual_dec=[x.strip() for x in re.search(r'Canonical decision vocabulary in order: (.*?)\.',st).group(1).split(',')]
    if actual_dec!=DECISIONS: ctx.err(sp,None,'decision-vocabulary-order',DECISIONS,actual_dec)
    for fld in ['source_validation_status','domain_guard_context','assignee_reference_id','completion_context_reference_id','matter_reference_id','blocker_resolution_reference_id']:
        if fld not in st: ctx.err(sp,None,'shared-request-field-missing',fld,'missing')
    for p in [ctx.base/'contracts/workflows/components/workflow-state-definition-contract.md',ctx.base/'contracts/workflows/components/workflow-transition-definition-contract.md']:
        text=p.read_text()
        if 'Contract File: core-specs/contracts/workflows/components/' not in text: ctx.err(p,None,'contract-file-canonical-path','canonical path','missing')
        for s in ['Purpose','Contract Meaning','Contract Boundary','Related Component Specification','Parent Workflow Contract','Required References','Contract Shape','Field Types','Field Rules','Collection Rules','Validation Rules','Permission and Policy','Human Review and Approval','Event and Audit Rules','External Action Boundary','AI Boundary','Compatibility and Versioning','Failure Semantics','Fixture Requirements','Valid Examples','Invalid Examples','Prohibited Overreach','Acceptance Criteria','Revision Notes']:
            if not re.search(r'# \d+\. '+re.escape(s)+r'\n',text): ctx.err(p,None,'workflow-component-section-missing',s,'missing')
    wt=(ctx.base/'contracts/workflows/components/workflow-transition-definition-contract.md').read_text()
    if 'mutation_performed: false' not in wt: ctx.err('workflow-transition-definition-contract.md',None,'workflow-mutation-literal-false','mutation_performed: false','missing')
def validate_manifest(ctx:Ctx):
    man=read_json(ctx,ctx.fix/'manifest.json') or {}; actual={p.relative_to(ctx.fix).as_posix():p for p in ctx.fix.rglob('*.json') if p.name!='manifest.json'}
    if set(man)!=MANIFEST_KEYS: ctx.err(ctx.fix/'manifest.json',None,'manifest-top-level-fields',sorted(MANIFEST_KEYS),sorted(man))
    if man.get('fixture_pack_id')!='B02-FIXTURE-STATUS-WORKFLOW-V1': ctx.err(ctx.fix/'manifest.json',None,'manifest-pack-id','B02-FIXTURE-STATUS-WORKFLOW-V1',man.get('fixture_pack_id'))
    if man.get('fixture_pack_version')!='v0.1.0': ctx.err(ctx.fix/'manifest.json',None,'manifest-version','v0.1.0',man.get('fixture_pack_version'))
    if man.get('synthetic') is not True: ctx.err(ctx.fix/'manifest.json',None,'manifest-synthetic',True,man.get('synthetic'))
    if man.get('contains_production_data') is not False: ctx.err(ctx.fix/'manifest.json',None,'manifest-production-data',False,man.get('contains_production_data'))
    entries=man.get('fixtures',[]); seen_ids=set(); seen_paths=set(); data_by_path={}
    for e in entries:
        if set(e)!=MANIFEST_ENTRY: ctx.err(ctx.fix/'manifest.json',e.get('fixture_id'),'manifest-entry-schema',sorted(MANIFEST_ENTRY),sorted(e))
        path=e.get('path','')
        if path.startswith('/') or '..' in Path(path).parts: ctx.err(ctx.fix/'manifest.json',e.get('fixture_id'),'manifest-path-contained','relative inside fixture root',path)
        if path in seen_paths: ctx.err(ctx.fix/'manifest.json',e.get('fixture_id'),'manifest-path-duplicate','unique',path)
        seen_paths.add(path)
        if e.get('fixture_id') in seen_ids: ctx.err(ctx.fix/'manifest.json',e.get('fixture_id'),'fixture-id-duplicate-manifest','unique',e.get('fixture_id'))
        seen_ids.add(e.get('fixture_id'))
        if path not in actual: ctx.err(ctx.fix/'manifest.json',e.get('fixture_id'),'manifest-path-missing','existing file',path); continue
        data=read_json(ctx,actual[path]); data_by_path[path]=data
        if data:
            for k in ['fixture_id','fixture_type','target_contract_id','target_spec_id','case_type']:
                if e.get(k)!=data.get(k): ctx.err(actual[path],data.get('fixture_id'),'manifest-fixture-mismatch',f'{k}={e.get(k)}',data.get(k))
    if set(actual)!=seen_paths:
        for p in sorted(set(actual)-seen_paths): ctx.err(actual[p],None,'orphan-fixture','listed in manifest',p)
    return entries,data_by_path
def walk_secret(ctx:Ctx,p:Path,fid:str,obj:Any):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k.lower() in SECRET_KEYS: ctx.err(p,fid,'secret-key-present','no secret keys',k)
            walk_secret(ctx,p,fid,v)
    elif isinstance(obj,list):
        for v in obj: walk_secret(ctx,p,fid,v)
    elif isinstance(obj,str):
        if re.search(r'Bearer\s+[A-Za-z0-9._-]{12,}|-----BEGIN .*PRIVATE KEY-----|://[^\s/?#]+:[^\s/?#]+@|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',obj): ctx.err(p,fid,'credential-like-value','no credential-like values',obj)
def validate_fixture_envelope(ctx:Ctx,p:Path,data:dict[str,Any]):
    fid=data.get('fixture_id')
    if set(data)!=ENVELOPE: ctx.err(p,fid,'fixture-envelope-fields',sorted(ENVELOPE),sorted(data))
    if data.get('fixture_type') not in FIXTURE_TYPES: ctx.err(p,fid,'fixture-type-invalid',sorted(FIXTURE_TYPES),data.get('fixture_type'))
    if data.get('case_type') not in CASE_TYPES: ctx.err(p,fid,'case-type-invalid',sorted(CASE_TYPES),data.get('case_type'))
    if data.get('synthetic') is not True: ctx.err(p,fid,'fixture-synthetic',True,data.get('synthetic'))
    if data.get('contains_production_data') is not False: ctx.err(p,fid,'fixture-production-data',False,data.get('contains_production_data'))
    if data.get('target_contract_id') not in ctx.contract_ids: ctx.err(p,fid,'target-contract-missing','known contract',data.get('target_contract_id'))
    if data.get('target_spec_id') not in ctx.spec_ids: ctx.err(p,fid,'target-spec-missing','known spec',data.get('target_spec_id'))
    walk_secret(ctx,p,fid,data)
def validate_status_fixture(ctx:Ctx,p:Path,data:dict[str,Any]):
    fid=data.get('fixture_id'); rel=p.relative_to(ctx.fix).parts; n=rel[1] if len(rel)>2 else ''; vals,trs=spec_status(ctx,n); contract_p=ctx.base/f'contracts/status/{n}-status-contract.md'
    if data['fixture_type']=='StatusMatrix':
        exp=data['expected']
        if exp.get('canonical_values')!=vals: ctx.err(p,fid,'status-matrix-values-drift',vals,exp.get('canonical_values'))
        if exp.get('allowed_transitions')!=trs: ctx.err(p,fid,'status-matrix-transitions-drift',trs,exp.get('allowed_transitions'))
        if exp.get('canonical_values')!=values_from_contract(contract_p): ctx.err(p,fid,'matrix-contract-values-mismatch','matches domain contract','drift')
        return
    if data['fixture_type']!='StatusTransition': return
    req=data.get('input',{}).get('status_transition_request')
    if not isinstance(req,dict): ctx.err(p,fid,'status-transition-request-missing','status_transition_request object',data.get('input')); return
    for k in ['contract_version','transition_request_reference_id','subject','current_status','requested_status','requested_action','actor_context','permission_context','policy_context','human_review_context','approval_context','source_context','domain_guard_context']:
        if k not in req: ctx.err(p,fid,'status-transition-required-field-missing',k,'missing')
    subj=req.get('subject',{})
    if subj.get('owner_service')!=DOMAINS[n][3]: ctx.err(p,fid,'status-owner-service',DOMAINS[n][3],subj.get('owner_service'))
    edge={'from':req.get('current_status'),'to':req.get('requested_status')}; dec=data.get('expected',{}).get('status_transition_decision',{}); result=data.get('expected',{}).get('status_transition_result')
    if edge['from'] not in vals or edge['to'] not in vals: ctx.err(p,fid,'status-canonical-value',vals,edge)
    decision=dec.get('decision')
    if decision not in DECISIONS: ctx.err(p,fid,'status-decision-invalid',DECISIONS,decision)
    if decision=='Allowed' and edge not in trs: ctx.err(p,fid,'status-allowed-edge-not-in-matrix','edge in matrix',edge)
    if decision=='InvalidTransition' and edge in trs: ctx.err(p,fid,'status-invalid-edge-in-matrix','edge not in matrix',edge)
    if result is None: return
    if result.get('performed') is False and any(result.get(k) for k in ['event_type','event_reference_id','performed_at']): ctx.err(p,fid,'status-result-false-has-event','no event/performed_at',result)
    if result.get('performed') is True:
        if decision!='Allowed': ctx.err(p,fid,'status-performed-requires-allowed','Allowed',decision)
        for k in ['event_type','event_reference_id','audit_reference_id','performed_at']:
            if not result.get(k): ctx.err(p,fid,'status-performed-proof-missing',k,result.get(k))
        if result.get('event_type')!=DOMAINS[n][4]: ctx.err(p,fid,'status-event-type',DOMAINS[n][4],result.get('event_type'))
    # guard specifics by structured action/context
    action=req.get('requested_action'); dg=req.get('domain_guard_context',{}); src=req.get('source_context',{}); hr=req.get('human_review_context',{}); perm=req.get('permission_context',{}); pol=req.get('policy_context',{})
    if n=='order' and action=='acceptOrder' and req.get('requested_status')!='Confirmed': ctx.err(p,fid,'order-accept-target','Confirmed',req.get('requested_status'))
    if n=='task' and action=='reopenTask' and edge not in [{'from':'Completed','to':'Open'},{'from':'Cancelled','to':'Open'}]: ctx.err(p,fid,'task-reopen-target','Completed/Cancelled -> Open',edge)
    if n=='task' and action=='assignTask' and not dg.get('assignee_reference_id'): ctx.err(p,fid,'task-assignee-required','assignee_reference_id',dg)
    if n=='task' and action=='completeTask' and not dg.get('completion_context_reference_id'): ctx.err(p,fid,'task-completion-context-required','completion_context_reference_id',dg)
    if n=='trademark' and action=='normalizeOfficialStatus':
        needed=['source_reference_id','source_type','source_version_or_timestamp','jurisdiction_reference_id','normalization_evidence_reference_id','source_validation_status']
        missing=[k for k in needed if not src.get(k)]
        if missing: ctx.err(p,fid,'trademark-source-fields-required',needed,src)
        if decision=='Allowed' and src.get('source_validation_status')!='Valid': ctx.err(p,fid,'trademark-source-valid-required','Valid',src.get('source_validation_status'))
        if decision=='ReviewRequired' and src.get('source_validation_status')!='Conflicting': ctx.err(p,fid,'trademark-source-conflict-required','Conflicting',src.get('source_validation_status'))
    if n=='matter' and action=='completeReview' and (not hr.get('human_review_reference_id') or hr.get('review_status')!='Approved'): ctx.err(p,fid,'matter-review-approved-required','Approved review',hr)
    if n=='matter' and action=='resolveBlocker' and not dg.get('blocker_resolution_reference_id') and decision!='Blocked': ctx.err(p,fid,'matter-blocker-resolution-required','Blocked decision or blocker_resolution_reference_id',dg)
    if decision=='PermissionRequired' and perm.get('permission_status')=='Allowed': ctx.err(p,fid,'permission-required-not-allowed','Unknown/null permission',perm)
def validate_workflow_fixture(ctx:Ctx,p:Path,data:dict[str,Any]):
    fid=data.get('fixture_id'); inp=data.get('input',{})
    if data['fixture_type']=='WorkflowStateDefinition':
        sset=inp.get('workflow_state_definition_set')
        if not isinstance(sset,dict): ctx.err(p,fid,'workflow-state-set-missing','workflow_state_definition_set',inp); return
        validate_state_set(ctx,p,fid,sset,inp.get('transition_definitions',[]), data.get('expected',{}).get('decision'))
    if data['fixture_type']=='WorkflowTransitionValidation':
        sset=inp.get('workflow_state_definition_set'); defs=inp.get('workflow_transition_definitions',[]); req=inp.get('workflow_transition_validation_request')
        if not isinstance(req,dict): ctx.err(p,fid,'workflow-validation-request-missing','workflow_transition_validation_request',inp); return
        expected_decision=data.get('expected',{}).get('workflow_transition_validation_result',{}).get('decision')
        if isinstance(sset,dict): validate_state_set(ctx,p,fid,sset,defs, expected_decision)
        for k,t in WF_REQ_FIELDS.items():
            if k not in req: ctx.err(p,fid,'workflow-validation-field-missing',k,'missing')
            elif not isinstance(req[k],t): ctx.err(p,fid,'workflow-validation-field-type',k, type(req[k]).__name__)
        states={s.get('state_key'):s for s in (sset or {}).get('states',[]) if isinstance(s,dict)}
        if (req.get('current_state_key') not in states or req.get('requested_state_key') not in states) and expected_decision!='InvalidTransition': ctx.err(p,fid,'workflow-known-state','known current/requested states',req)
        trans=next((d for d in defs if d.get('transition_key')==req.get('transition_key')),None)
        dec=data.get('expected',{}).get('workflow_transition_validation_result',{}).get('decision')
        if dec not in DECISIONS: ctx.err(p,fid,'workflow-decision-invalid',DECISIONS,dec)
        if data.get('expected',{}).get('workflow_transition_validation_result',{}).get('mutation_performed') is not False: ctx.err(p,fid,'workflow-mutation-performed-false',False,data.get('expected'))
        if req.get('workflow_contract_version')!='v0.1.0' and dec=='Allowed': ctx.err(p,fid,'workflow-unsupported-version-nonallowed','non-Allowed',dec)
        if trans:
            if trans.get('from_state_key')!=req.get('current_state_key') or trans.get('to_state_key')!=req.get('requested_state_key'): ctx.err(p,fid,'workflow-transition-match','from/to match request',trans)
            if states.get(trans.get('from_state_key'),{}).get('is_terminal') and dec!='InvalidTransition': ctx.err(p,fid,'workflow-terminal-outgoing-invalid','InvalidTransition',dec)
            if trans.get('permission_references') and req.get('permission_decision_reference_id') is None and dec!='PermissionRequired': ctx.err(p,fid,'workflow-permission-required','PermissionRequired',dec)
            if trans.get('review_requirement') and req.get('human_review_reference_id') is None and dec!='ReviewRequired': ctx.err(p,fid,'workflow-review-required','ReviewRequired',dec)
            if 'protected' in str(trans.get('external_action_boundary')) and dec=='Allowed': ctx.err(p,fid,'workflow-protected-action-denied','non-Allowed',dec)
        elif dec!='InvalidTransition': ctx.err(p,fid,'workflow-transition-definition-missing','InvalidTransition',dec)
def validate_state_set(ctx:Ctx,p:Path,fid:str|None,sset:dict[str,Any],defs:list[dict[str,Any]], expected_decision: str|None=None):
    for k in ['workflow_contract_reference_id','workflow_contract_version','states']:
        if k not in sset: ctx.err(p,fid,'workflow-state-set-field-missing',k,'missing')
    keys=[]; initial=0
    for st in sset.get('states',[]):
        if set(st)!=set(STATE_FIELDS): ctx.err(p,fid,'workflow-state-fields-exact',sorted(STATE_FIELDS),sorted(st))
        for k,t in STATE_FIELDS.items():
            if k in st and not isinstance(st[k],t): ctx.err(p,fid,'workflow-state-field-type',k,type(st[k]).__name__)
        if not st.get('state_key'): ctx.err(p,fid,'workflow-state-key-nonempty','non-empty',st.get('state_key'))
        if st.get('state_key') in keys and expected_decision!='InvalidState': ctx.err(p,fid,'workflow-state-key-duplicate','unique',st.get('state_key'))
        keys.append(st.get('state_key'))
        if st.get('is_initial'): initial+=1
        if not st.get('external_action_boundary'): ctx.err(p,fid,'workflow-state-external-boundary-nonempty','non-empty',st.get('external_action_boundary'))
    if initial<1 and expected_decision!='InvalidState': ctx.err(p,fid,'workflow-initial-state-missing','at least one',initial)
    if initial>1 and expected_decision!='InvalidState': ctx.err(p,fid,'workflow-initial-state-multiple','exactly one',initial)
    terminal={s.get('state_key') for s in sset.get('states',[]) if s.get('is_terminal')}
    for tr in defs:
        if tr.get('from_state_key') in terminal and expected_decision!='InvalidTransition': ctx.err(p,fid,'workflow-terminal-outgoing','no outgoing from terminal',tr)
def validate_fixtures(ctx:Ctx):
    entries,_=validate_manifest(ctx)
    actual_ids=set(); seen_actual=set()
    for e in entries:
        p=ctx.fix/e.get('path','')
        if not p.exists(): continue
        data=read_json(ctx,p)
        if not isinstance(data,dict): continue
        if data.get('fixture_id') in seen_actual: ctx.err(p,data.get('fixture_id'),'fixture-id-duplicate-actual','unique',data.get('fixture_id'))
        seen_actual.add(data.get('fixture_id'))
        validate_fixture_envelope(ctx,p,data)
        if data.get('fixture_type') in {'StatusMatrix','StatusTransition'}: validate_status_fixture(ctx,p,data)
        if data.get('fixture_type') in {'WorkflowStateDefinition','WorkflowTransitionValidation'}: validate_workflow_fixture(ctx,p,data)
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.') ; args=ap.parse_args(); ctx=Ctx(Path(args.root).resolve())
    validate_contracts(ctx); validate_fixtures(ctx)
    if ctx.errors:
        print('\n---\n'.join(e.line() for e in ctx.errors)); return 1
    print('Status/workflow contract fixtures validation passed'); return 0
if __name__=='__main__': sys.exit(main())
