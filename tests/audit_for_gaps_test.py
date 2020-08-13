import pytest

from rdm.audit_for_gaps import _find_keys_in_sources, \
    _read_raw_checklists, _split_out_include_files, _extract_keys_from_checklist, _find_failing_checklist_items


@pytest.fixture
def example_short_checklist_source():
    return [
        ('   include other_file\napple tempted Eve\nbanana tempted Curious George\n# commentary', 'yellow brick road')
    ]


@pytest.fixture
def example_long_checklist_source():
    return [
        (
            'include other_file\napple tempted Eve\nbanana tempted Curious George\n# commentary\ncherry\ndates',
            'yellow brick road'
        )
    ]


@pytest.fixture
def example_short_checklist():
    return [
        {
            'reference': 'apple',
            'description': 'tempted Eve',
        },
        {
            'reference': 'banana',
            'description': 'tempted Curious George',
        },
    ]


@pytest.fixture
def example_long_checklist():
    return [
        {
            'reference': 'apple',
            'description': 'tempted Eve',
        },
        {
            'reference': 'banana',
            'description': 'tempted Curious George',
        },
        {
            'reference': 'cherry',
        },
        {
            'reference': 'dates',
        },
    ]


@pytest.fixture
def example_raw_checklist():
    return [
        {
            'include': 'other_file',
            'path': 'yellow brick road'
        },
        {
            'reference': 'apple',
            'description': 'tempted Eve',
        },
        {
            'reference': 'banana',
            'description': 'tempted Curious George',
        },
    ]


document_a = "We like apple pie."
document_b = "We hate banana splits."
document_ac = "We like apple pie and cherry pie."
document_ad = "Never put dates in apple pie."


def test_extract_keys_from_short_checklist(example_short_checklist):
    actual_keys = set(_extract_keys_from_checklist(example_short_checklist))
    assert actual_keys == {'apple', 'banana'}


def test_extract_keys_from_long_checklist(example_long_checklist):
    actual_keys = set(_extract_keys_from_checklist(example_long_checklist))
    assert actual_keys == {'apple', 'banana', 'cherry', 'dates'}


def test_find_keys_in_sources():
    expected_keys = {'apple', 'banana', 'cherry'}
    documents = [document_a, document_b, document_ac]
    actual_keys = set(_find_keys_in_sources(documents, {'apple', 'banana', 'cherry', 'dates'}))
    assert actual_keys == expected_keys


def test_find_failing_checklist_items_should_pass(example_long_checklist):
    documents = [document_a, document_b, document_ac, document_ad]
    failures = list(_find_failing_checklist_items(documents, example_long_checklist))
    assert len(failures) == 0


def test_find_failing_checklist_itemss_should_fail(example_long_checklist):
    documents = [document_a, document_b, document_ac]
    failures = list(_find_failing_checklist_items(documents, example_long_checklist))
    assert len(failures) == 1
    assert failures[0].get('reference') == 'dates'


def test_raw_parser(example_short_checklist_source, example_raw_checklist):
    actual_checklist = list(_read_raw_checklists(example_short_checklist_source))
    assert actual_checklist == example_raw_checklist


def test_include_file_extractor(example_raw_checklist):
    include_files, reduced_checklist = _split_out_include_files(example_raw_checklist, {})
    assert include_files == {'yellow brick road/other_file'}
    assert reduced_checklist == example_raw_checklist[1:]
