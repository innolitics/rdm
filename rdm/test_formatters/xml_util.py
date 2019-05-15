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
            status = test_case.get('status')
            if suite_disabled or case_disabled or (status is not None and status != 'run'):
                result = "skip"
                message = None
            else:
                result = test_case.get('result')
                failure = test_case.find('failure')
                if failure is None:
                    message = None
                    if result is None:
                        result = "pass"
                else:
                    message = failure.get('message')
                    result = 'fail'
            flattened_results[test_name] = {
                'name': test_name,
                'result': result,
                'message': message,
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
                result = incident.get("type")
                description = incident.find('Description')
                if description is None:
                    message = None
                else:
                    message = description.text
                flattened_results[test_name] = {
                    'name': test_name,
                    'result': result,
                    'message': message,
                }
    return flattened_results


def auto_translator(test_results):
    if test_results.find('Environment'):
        return flattened_qttest_results(test_results)
    else:
        return flattened_gtest_results(test_results)
