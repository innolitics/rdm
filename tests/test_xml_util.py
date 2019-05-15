import os

import pytest

from rdm.test_formatters.xml_util import xml_load, flattened_gtest_results, flattened_qttest_results, auto_translator


def _full_path_of_test_file(name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data", name)


XML_PATHS = [_full_path_of_test_file(leaf_name)
             for leaf_name in ["integration.xml", "test_detail.xml", "xunit_result.xml"]]


@pytest.mark.parametrize('xml_path', XML_PATHS)
def test_xml_load(xml_path):
    test_results = xml_load(xml_path)
    assert test_results is not None


def test_gtest_detail_flattener():
    xml_path = _full_path_of_test_file("test_detail.xml")
    test_results = xml_load(xml_path)
    flattened_results = flattened_gtest_results(test_results)
    assert flattened_results is not None
    assert len(flattened_results) == 15
    cherry_test = flattened_results.get('SomeModule.Cherry')
    assert cherry_test is not None
    assert cherry_test['result'] == 'pass'
    assert cherry_test['name'] == 'SomeModule.Cherry'
    bad_test = flattened_results.get('HasOneFailure.BadOne')
    assert bad_test is not None
    assert bad_test['result'] == 'fail'
    assert bad_test['name'] == 'HasOneFailure.BadOne'
    assert 'Expected equality' in bad_test['message']
    disabled_test = flattened_results.get('SomeTrouble.NoPointInChecking')
    assert disabled_test is not None
    assert disabled_test['result'] == 'skip'

def test_xunit_flattener():
    xml_path = _full_path_of_test_file("xunit_result.xml")
    test_results = xml_load(xml_path)
    flattened_results = flattened_gtest_results(test_results)
    assert flattened_results is not None
    assert len(flattened_results) == 18
    cherry_test = flattened_results.get('AllTests.Cherry::test_main')
    assert cherry_test is not None
    assert cherry_test['result'] == 'pass'
    assert cherry_test['name'] == 'AllTests.Cherry::test_main'
    bad_test = flattened_results.get('AllTests.Date::test_several_things')
    assert bad_test is not None
    assert bad_test['result'] == 'fail'
    assert bad_test['name'] == 'AllTests.Date::test_several_things'
    assert 'Uncaught exception' in bad_test['message']


def test_qttest_flattener():
    xml_path = _full_path_of_test_file("integration.xml")
    test_results = xml_load(xml_path)
    flattened_results = flattened_qttest_results(test_results)
    assert flattened_results is not None
    assert len(flattened_results) == 4
    first_test = flattened_results.get('some_module.SomeName::someTestCase')
    assert first_test is not None
    assert first_test['result'] == 'pass'
    assert first_test['name'] == 'some_module.SomeName::someTestCase'
    second_test = flattened_results.get('some_module.SomeName::someOtherTestCase')
    assert second_test is not None
    assert second_test['result'] == 'fail'
    assert second_test['name'] == 'some_module.SomeName::someOtherTestCase'
    assert 'incorrect number of segments' in second_test['message']


@pytest.mark.parametrize('xml_path', XML_PATHS)
def test_auto_flattener(xml_path):
    test_results = xml_load(xml_path)
    flattened_results = auto_translator(test_results)
    assert flattened_results is not None
    assert len(flattened_results) in {4, 15, 18}
