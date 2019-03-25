from collections import OrderedDict

import xmltodict

DISABLED_PREFIX = 'DISABLED_'


def xml_load(xml_path):
    with open(xml_path, 'r') as input_file:
        test_results = xmltodict.parse(input_file.read())
        return test_results


def check_disabled(name):
    if name.startswith(DISABLED_PREFIX):
        return name[len(DISABLED_PREFIX):], True
    else:
        return name, False


def force_ordered_dict_to_list(list_or_dict):
    if isinstance(list_or_dict, OrderedDict):
        return [list_or_dict]
    else:
        return list_or_dict


def flattened_google_test_detail(test_results):
    flattened_results = {}
    test_suites = force_ordered_dict_to_list(test_results.get("testsuites", {}).get('testsuite', []))
    for test_suite in test_suites:
        suite_name, suite_disabled = check_disabled(test_suite.get('@name', '_'))
        test_cases = force_ordered_dict_to_list(test_suite.get('testcase', []))
        for test_case in test_cases:
            case_name, case_disabled = check_disabled(test_case.get('@name', '_'))
            test_name = ".".join([suite_name, case_name])
            failure = test_case.get('failure')
            if failure:
                failure_message = failure.get('@message')
            else:
                failure_message = None
            status = test_case.get('@status')
            ran = status == 'run'
            passed = ran and not failure
            failed = ran and not not failure
            result = 'passed' if passed else 'failed' if failed else 'skipped'
            flattened_results[test_name] = {
                'test_name': test_name,
                'suite_name': suite_name,
                'case_name': case_name,
                'disabled': suite_disabled or case_disabled,
                'suite_disabled': suite_disabled,
                'case_disabled': case_disabled,
                'status': status,
                'failure': failure,
                'passed': passed,
                'failed': failed,
                'ran': ran,
                'message': failure_message,
                'result': result,
            }
    return flattened_results


def flattened_integration_results(test_results):
    flattened_results = {}
    test_cases = force_ordered_dict_to_list(test_results.get("TestCase", []))
    for test_case in test_cases:
        case_name = test_case.get('@name', '_')
        test_functions = force_ordered_dict_to_list(test_case.get('TestFunction', []))
        for test_function in test_functions:
            function_name = test_function.get('@name', '_')
            test_name = ".".join([case_name, function_name])
            incidents = force_ordered_dict_to_list(test_function.get('Incident', []))
            for incident in incidents:
                incident_type = incident.get("@type")
                passed = incident_type == "pass"
                failed = incident_type == "fail"
                flattened_results[test_name] = {
                    'test_name': test_name,
                    'function_name': function_name,
                    'case_name': case_name,
                    'incident_type': incident_type,
                    'passed': passed,
                    'failed': failed,
                }
    return flattened_results
