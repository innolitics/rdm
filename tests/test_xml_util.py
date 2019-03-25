from rdm.xml_util import xml_load, flattened_google_test_detail, flattened_integration_results


def test_xml_load():
    xml_path = "./test_data/test_detail.xml"
    test_results = xml_load(xml_path)
    assert test_results is not None


def test_google_test_detail_flattener():
    xml_path = "./test_data/test_detail.xml"
    test_results = xml_load(xml_path)
    flattened_results = flattened_google_test_detail(test_results)
    assert flattened_results is not None
    assert len(flattened_results) == 15
    cherry_test = flattened_results.get('SomeModule.Cherry')
    assert cherry_test is not None
    assert cherry_test['passed']
    assert not cherry_test['failed']
    assert cherry_test['status'] == 'run'
    assert cherry_test['result'] == 'passed'
    bad_test = flattened_results.get('HasOneFailure.BadOne')
    assert bad_test is not None
    assert not bad_test['passed']
    assert bad_test['failed']
    assert bad_test['status'] == 'run'
    assert bad_test['result'] == 'failed'
    disabled_test = flattened_results['SomeTrouble.NoPointInChecking']
    assert disabled_test is not None
    assert not disabled_test['passed']
    assert not disabled_test['failed']
    assert disabled_test['status'] == 'notrun'
    assert disabled_test['result'] == 'skipped'


def test_flattened_integration_results():
    xml_path = "./test_data/integration.xml"
    test_results = xml_load(xml_path)
    flattened_results = flattened_integration_results(test_results)
    assert flattened_results is not None
    assert len(flattened_results) == 4
    first_test = flattened_results.get('some_module.SomeName::someTestCase')
    assert first_test is not None
    assert first_test['passed']
    assert not first_test['failed']
    second_test = flattened_results.get('some_module.SomeName::someOtherTestCase')
    assert second_test is not None
    assert not second_test['passed']
    assert second_test['failed']
