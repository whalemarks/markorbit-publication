#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from dataclasses import dataclass
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VAL=ROOT/'tools/validate_status_workflow_contract_fixtures.py'
F=Path('books/book-02-core-specification/core-specs/contracts/fixtures/status-workflow')
C=Path('books/book-02-core-specification/core-specs/contracts')
@dataclass
class NegativeCase:
    name:str; rel:Path; mutate:object; expected_violation:str
def run(tree:Path): return subprocess.run([sys.executable,str(tree/'tools/validate_status_workflow_contract_fixtures.py'),'--root',str(tree)],cwd=tree,text=True,capture_output=True)
def jmut(fn):
    def inner(p:Path):
        d=json.loads(p.read_text()); fn(d); p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
    return inner
def textmut(fn): return lambda p: p.write_text(fn(p.read_text()))
def eval_case(case:NegativeCase):
    with tempfile.TemporaryDirectory() as td:
        t=Path(td)/'repo'; shutil.copytree(ROOT,t,ignore=shutil.ignore_patterns('.git','__pycache__'))
        (case.mutate)(t/case.rel)
        r=run(t); out=r.stdout+r.stderr
        if r.returncode==0 or case.expected_violation not in out:
            raise AssertionError(f"{case.name} expected {case.expected_violation}\nrc={r.returncode}\n{out}")
def main()->int:
    base=run(ROOT)
    if base.returncode!=0: print(base.stdout+base.stderr); return 1
    positive_fixtures=[
        F/'status/trademark/canonical-matrix.json', F/'status/order/canonical-matrix.json', F/'status/matter/canonical-matrix.json', F/'status/task/canonical-matrix.json',
        F/'status/trademark/review-required-source-conflict.json', F/'status/order/valid-accept-order-to-confirmed.json', F/'status/task/valid-governed-reopen-to-open.json', F/'status/trademark/valid-official-source-to-registered.json',
        F/'workflow/valid-state-definition-set.json', F/'workflow/valid-transition-definition-shape.json', F/'workflow/valid-transition-definition.json', F/'workflow/protected-external-action-denied.json', F/'workflow/unsupported-contract-version.json'
    ]
    for fixture in positive_fixtures:
        if not (ROOT/fixture).exists(): raise AssertionError(f'positive fixture missing: {fixture}')
        r=run(ROOT)
        if r.returncode!=0: raise AssertionError(f'positive fixture validation failed: {fixture}\n{r.stdout}{r.stderr}')
    cases=[
        NegativeCase('canonical status removed',F/'status/trademark/canonical-matrix.json',jmut(lambda d:d['expected']['canonical_values'].pop()),'status-matrix-values-drift'),
        NegativeCase('unknown status added',F/'status/trademark/canonical-matrix.json',jmut(lambda d:d['expected']['canonical_values'].append('UnknownStatus')),'status-matrix-values-drift'),
        NegativeCase('transition removed',F/'status/order/canonical-matrix.json',jmut(lambda d:d['expected']['allowed_transitions'].pop()),'status-matrix-transitions-drift'),
        NegativeCase('unauthorized transition added',F/'status/order/canonical-matrix.json',jmut(lambda d:d['expected']['allowed_transitions'].append({'from':'Confirmed','to':'Draft'})),'status-matrix-transitions-drift'),
        NegativeCase('contract matrix drift',C/'status/matter-status-contract.md',textmut(lambda s:s.replace('Draft -> Open','Draft -> Completed')),'domain-contract-transitions-drift'),
        NegativeCase('contract required section missing',C/'status/order-status-contract.md',textmut(lambda s:s.replace('# 27. Revision Notes','# 27. Revision Notes Missing')),'contract-section-missing'),
        NegativeCase('contract file not canonical',C/'status/order-status-contract.md',textmut(lambda s:s.replace('Contract File: core-specs/contracts/status/order-status-contract.md','Contract File: order-status-contract.md')),'contract-file-canonical-path'),
        NegativeCase('related spec markdown link missing',C/'status/order-status-contract.md',textmut(lambda s:s.replace('](../../controlled-state-values/order-status-values.md)','](../../controlled-state-values/order-status-values-missing.md)')),'related-spec-link-missing'),
        NegativeCase('decision vocabulary extra',C/'status/status-transition-contract.md',textmut(lambda s:s.replace('Unknown. No other','Unknown, Extra. No other')),'decision-vocabulary-order'),
        NegativeCase('decision vocabulary order',C/'status/status-transition-contract.md',textmut(lambda s:s.replace('Allowed, Denied','Denied, Allowed')),'decision-vocabulary-order'),
        NegativeCase('manifest fixture id mismatch',F/'manifest.json',jmut(lambda d:d['fixtures'][0].__setitem__('fixture_id','wrong')),'manifest-fixture-mismatch'),
        NegativeCase('manifest target spec mismatch',F/'manifest.json',jmut(lambda d:d['fixtures'][0].__setitem__('target_spec_id','B02-WRONG')),'manifest-fixture-mismatch'),
        NegativeCase('manifest path missing',F/'manifest.json',jmut(lambda d:d['fixtures'][0].__setitem__('path','missing.json')),'manifest-path-missing'),
        NegativeCase('orphan fixture',F/'status/task/valid-open-to-assigned.json',lambda p:p.rename(p.with_name('orphan-extra.json')),'orphan-fixture'),
        NegativeCase('fixture target contract missing',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('target_contract_id','B02-CONTRACT-MISSING')),'target-contract-missing'),
        NegativeCase('fixture synthetic false',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('synthetic',False)),'fixture-synthetic'),
        NegativeCase('fixture production true',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('contains_production_data',True)),'fixture-production-data'),
        NegativeCase('invalid fixture type',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('fixture_type','BadType')),'fixture-type-invalid'),
        NegativeCase('invalid case type',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('case_type','maybe')),'case-type-invalid'),
        NegativeCase('status transition missing subject',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request'].pop('subject')),'status-request-fields-exact'),
        NegativeCase('status transition missing actor',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request'].pop('actor_context')),'status-request-fields-exact'),
        NegativeCase('allowed fixture invalid transition',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request'].__setitem__('requested_status','Accepted')),'status-canonical-value'),
        NegativeCase('invalid fixture allowed transition',F/'status/order/invalid-confirmed-to-draft.json',jmut(lambda d:(d['input']['status_transition_request'].__setitem__('current_status','PendingConfirmation'),d['input']['status_transition_request'].__setitem__('requested_status','Confirmed'))),'status-invalid-edge-in-matrix'),
        NegativeCase('performed false has event',F/'status/order/permission-required-cancellation.json',jmut(lambda d:d['expected'].__setitem__('status_transition_result',{'performed':False,'event_type':'OrderStatusChanged'})),'status-result-false-has-event'),
        NegativeCase('performed true missing audit',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('audit_reference_id',None)),'status-performed-proof-missing'),
        NegativeCase('task reopen reopened',F/'status/task/valid-governed-reopen-to-open.json',jmut(lambda d:d['input']['status_transition_request'].__setitem__('requested_status','Reopened')),'status-canonical-value'),
        NegativeCase('trademark source missing',F/'status/trademark/valid-official-source-to-registered.json',jmut(lambda d:d['input']['status_transition_request']['source_context'].__setitem__('source_type',None)),'trademark-source-fields-required'),
        NegativeCase('workflow duplicate key',F/'workflow/valid-state-definition-set.json',jmut(lambda d:d['input']['workflow_state_definition_set']['states'][1].__setitem__('state_key','draft')),'workflow-state-key-duplicate'),
        NegativeCase('workflow no initial',F/'workflow/valid-state-definition-set.json',jmut(lambda d:[s.__setitem__('is_initial',False) for s in d['input']['workflow_state_definition_set']['states']]),'workflow-initial-state-missing'),
        NegativeCase('workflow multiple initial',F/'workflow/valid-state-definition-set.json',jmut(lambda d:d['input']['workflow_state_definition_set']['states'][1].__setitem__('is_initial',True)),'workflow-initial-state-multiple'),
        NegativeCase('terminal outgoing wrong allowed',F/'workflow/invalid-terminal-outgoing-transition.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('decision','Allowed')),'workflow-terminal-outgoing'),
        NegativeCase('workflow missing target reference',F/'workflow/valid-transition-definition.json',jmut(lambda d:d['input']['workflow_transition_validation_request'].pop('target_object_reference_id')),'workflow-validation-field-missing'),
        NegativeCase('unsupported version allowed',F/'workflow/unsupported-contract-version.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('decision','Allowed')),'workflow-unsupported-version-nonallowed'),
        NegativeCase('permission required allowed',F/'workflow/permission-required-transition.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('decision','Allowed')),'workflow-permission-required'),
        NegativeCase('review required allowed',F/'workflow/review-required-transition.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('decision','Allowed')),'workflow-review-required'),
        NegativeCase('protected action allowed',F/'workflow/protected-external-action-denied.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('decision','Allowed')),'workflow-protected-action-denied'),
        NegativeCase('workflow mutation true',F/'workflow/valid-transition-definition.json',jmut(lambda d:d['expected']['workflow_transition_validation_result'].__setitem__('mutation_performed',True)),'workflow-mutation-performed-false'),
        NegativeCase('secret key',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d.__setitem__('password','secret')),'fixture-envelope-fields'),
        NegativeCase('credential value',F/'status/task/valid-open-to-assigned.json',jmut(lambda d:d['input'].__setitem__('credential_url','https://user:pass@example.com')),'credential-like-value'),
        NegativeCase('shared request contract field deleted',C/'status/status-transition-contract.md',textmut(lambda s:s.replace('source_validation_status','source_validation_removed')),'shared-request-field-missing'),
        NegativeCase('shared decision contract field deleted',C/'status/status-transition-contract.md',textmut(lambda s:s.replace('mutation_authorized_for_owner_service','mutation_removed')),'shared-decision-field-missing'),
        NegativeCase('shared result contract field deleted',C/'status/status-transition-contract.md',textmut(lambda s:s.replace('audit_reference_id','audit_removed')),'shared-result-field-missing'),
        NegativeCase('fixture request extra field',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request'].__setitem__('extra_field','x')),'status-request-fields-exact'),
        NegativeCase('fixture decision extra field',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_decision'].__setitem__('extra_field','x')),'status-decision-fields-exact'),
        NegativeCase('fixture result extra field additional_event_type',F/'status/task/valid-governed-reopen-to-open.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('additional_event_type','TaskReopened')),'status-result-fields-exact'),
        NegativeCase('fixture subject object type mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request']['subject'].__setitem__('object_type','Task')),'status-subject-object-type'),
        NegativeCase('decision request reference mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_decision'].__setitem__('transition_request_reference_id','other')),'status-decision-request-reference-match'),
        NegativeCase('decision current status mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_decision'].__setitem__('current_status','Draft')),'status-decision-current-status-match'),
        NegativeCase('nonallowed mutation authorized true',F/'status/order/permission-required-cancellation.json',jmut(lambda d:d['expected']['status_transition_decision'].__setitem__('mutation_authorized_for_owner_service',True)),'status-decision-nonallowed-mutation-authorized-false'),
        NegativeCase('performed result status changed false',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('status_changed',False)),'status-performed-status-changed-true'),
        NegativeCase('performed owner service mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('owner_service','Task Service')),'status-result-owner-service-match'),
        NegativeCase('performed previous status mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('previous_status','Draft')),'status-result-previous-status-match'),
        NegativeCase('performed next status mismatch',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['expected']['status_transition_result'].__setitem__('next_status','Draft')),'status-result-next-status-match'),
        NegativeCase('target contract not referencing spec',C/'status/order-status-contract.md',textmut(lambda s:s.replace('order-status-values.md','order-status-values-missing.md')),'related-spec-link-missing'),
        NegativeCase('fixture type contract mismatch',F/'workflow/valid-state-definition-set.json',jmut(lambda d:d.__setitem__('target_contract_id','B02-CONTRACT-WORKFLOW-TRANSITION-DEFINITION')),'target-contract-spec-relationship'),
        NegativeCase('workflow transition definition missing field',F/'workflow/valid-transition-definition-shape.json',jmut(lambda d:d['input']['workflow_transition_definition'].pop('owning_service_reference')),'workflow-transition-definition-fields'),
        NegativeCase('workflow transition definition field type',F/'workflow/valid-transition-definition-shape.json',jmut(lambda d:d['input']['workflow_transition_definition'].__setitem__('guard_references','bad')),'workflow-transition-definition-field-type'),
        NegativeCase('approval requirement missing but allowed',F/'workflow/valid-transition-definition.json',jmut(lambda d:(d['input']['workflow_transition_definitions'][0].__setitem__('approval_requirement','approval_required'), d['input']['workflow_transition_validation_request'].__setitem__('approval_reference_id',None))),'workflow-positive-has-defect'),
        NegativeCase('negative duplicate defect removed',F/'workflow/invalid-duplicate-state-key.json',jmut(lambda d:d['input']['workflow_state_definition_set']['states'][1].__setitem__('state_key','done')),'workflow-negative-defect-missing'),
        NegativeCase('negative missing initial defect removed',F/'workflow/invalid-missing-initial-state.json',jmut(lambda d:d['input']['workflow_state_definition_set']['states'][0].__setitem__('is_initial',True)),'workflow-negative-defect-missing'),
        NegativeCase('negative terminal outgoing defect removed',F/'workflow/invalid-terminal-outgoing-transition.json',jmut(lambda d:(d['input']['workflow_transition_definitions'][0].__setitem__('from_state_key','draft'), d['input']['workflow_transition_definitions'][0].__setitem__('to_state_key','done'), d['input']['workflow_transition_validation_request'].__setitem__('current_state_key','draft'), d['input']['workflow_transition_validation_request'].__setitem__('requested_state_key','done'))),'workflow-negative-defect-missing'),
        NegativeCase('order accept commercial scope missing',F/'status/order/valid-accept-order-to-confirmed.json',jmut(lambda d:d['input']['status_transition_request']['domain_guard_context'].__setitem__('domain_context',{})),'order-accept-commercial-scope-required'),
        NegativeCase('task reopen permission missing',F/'status/task/valid-governed-reopen-to-open.json',jmut(lambda d:d['input']['status_transition_request']['permission_context'].__setitem__('permission_status','Unknown')),'task-reopen-permission-required'),
        NegativeCase('task reopen workflow validation missing',F/'status/task/valid-governed-reopen-to-open.json',jmut(lambda d:d['input']['status_transition_request']['domain_guard_context'].__setitem__('domain_context',{})),'task-reopen-workflow-validation-required'),
    ]
    for c in cases: eval_case(c)
    print(f'Positive cases passed: {len(positive_fixtures)}')
    print(f'Negative cases passed with expected violation assertions: {len(cases)}')
    return 0
if __name__=='__main__': sys.exit(main())
