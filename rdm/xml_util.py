from xml.etree import ElementTree

DISABLED_PREFIX = 'DISABLED_'


def xml_load(xml_path):
    return ElementTree.parse(xml_path)


def check_disabled(name):
    if name.startswith(DISABLED_PREFIX):
        return name[len(DISABLED_PREFIX):], True
    else:
        return name, False


def flattened_gtest_results(test_results):
    flattened_results = {}
    for test_suite in test_results.iter('testsuite'):
        suite_name, suite_disabled = check_disabled(test_suite.get('name', '_'))
        for test_case in test_suite.iter('testcase'):
            case_name, case_disabled = check_disabled(test_case.get('name', '_'))
            test_name = ".".join([suite_name, case_name])
            failure = test_case.find('failure')
            if failure is None:
                failure_message = None
            else:
                failure_message = failure.get('message')
            status = test_case.get('status')
            ran = status == 'run'
            passed = ran and failure is None
            failed = ran and failure is not None
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


def flattened_qttest_results(test_results):
    flattened_results = {}
    for test_case in test_results.iter('TestCase'):
        case_name = test_case.get('name', '_')
        for test_function in test_case.iter('TestFunction'):
            function_name = test_function.get('name', '_')
            test_name = ".".join([case_name, function_name])
            for incident in test_function.iter('Incident'):
                incident_type = incident.get("type")
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
