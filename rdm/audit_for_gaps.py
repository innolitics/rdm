import yaml

from rdm.util import load_yaml


def audit_for_gaps(args):
    checklists = _read_checklists(_determine_checklist_files(args))
    if len(checklists) == 0:
        print("WARNING: no check lists!")
        return
    source_files = _determine_source_files(args)
    if len(source_files) == 0:
        print("WARNING: no source files!")
        return
    failing_checklists = _find_failing_checklists(_source_generator(source_files), checklists)
    if failing_checklists:
        _report_failures(failing_checklists)
    else:
        _report_success()


def _find_failing_checklists(source_generator, checklists):
    checklist_keys = set(_extract_keys_from_checklists(checklists))
    found_keys = set(_find_keys_in_sources(source_generator, checklist_keys))
    evaluated_checklists = _evaluate_checklists(checklists, found_keys)
    return _filter_for_failing_checklists(evaluated_checklists)


def _determine_source_files(args):
    return args.files


def _determine_checklist_files(args):
    config = load_yaml(args.config)
    return config.get('checklists', [])


def _source_generator(source_files):
    for source_file in source_files:
        with open(source_file) as file:
            yield file.read()


def _read_checklists(checklist_files):
    return [load_yaml(checklist_file) for checklist_file in checklist_files]


def _extract_keys_from_checklists(checklists):
    for checklist in checklists:
        for requirement in checklist.get('requirements', []):
            for rule in requirement.get('rules', []):
                for key in rule.get('refs', []):
                    yield key


def _find_keys_in_sources(source_generator, checklist_keys):
    for content in source_generator:
        yield from _find_keys_in_content(content, checklist_keys)


def _find_keys_in_content(content, checklist_keys):
    for key in checklist_keys:
        if key in content:
            yield key


def _evaluate_checklists(checklists, found_keys):
    return [_evaluate_checklist(checklist, found_keys) for checklist in checklists]


def _evaluate_checklist(checklist, found_keys):
    evaluated_requirements = [
        _evaluate_checklist_requirement(requirement, found_keys)
        for requirement in checklist.get('requirements', [])
    ]
    return {
        **checklist,
        'requirements': evaluated_requirements,
        'passing': _requirements_all_pass(evaluated_requirements)
    }


def _requirements_all_pass(requirements):
    for requirement in requirements:
        if not requirement.get('passing'):
            return False
    return True


def _evaluate_checklist_requirement(requirement, found_keys):
    rules = requirement.get('rules', [])
    evaluated_rules = _evaluate_rules(rules, found_keys)
    return {
        **requirement,
        'rules': evaluated_rules,
        'passing': not _has_no_passing_rules(evaluated_rules),
    }


def _has_no_passing_rules(evaluated_rules):
    for rule in evaluated_rules:
        if rule.get('passing'):
            return False
    return True


def _evaluate_rules(rules, found_keys):
    return [_evaluate_rule(rule, found_keys) for rule in rules]


def _evaluate_rule(rule, found_keys):
    refs = rule.get('refs', [])
    missing_refs = [ref for ref in refs if not ref in found_keys]
    return {'missing': missing_refs, **rule, 'passing': len(missing_refs) == 0}


def _filter_for_failing_checklists(evaluated_checklists):
    return [_filter_for_failing_requirements(checklist) for checklist in evaluated_checklists if
            not checklist.get('passing')]


def _filter_for_failing_requirements(checklist):
    failed_requirements = [
        requirement
        for requirement in checklist.get('requirements', []) if not requirement.get('passing')
    ]
    return {
        **checklist,
        'requirements': failed_requirements
    }


def _report_failures(failing_checklists):
    number_of_failures = len(failing_checklists)
    print(f"Failure: {number_of_failures} checklists failed.")
    for failing_checklist in failing_checklists:
        print(yaml.dump(failing_checklist))


def _report_success():
    print("Success: all checklists passed.")
