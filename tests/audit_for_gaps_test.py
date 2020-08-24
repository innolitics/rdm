import pytest

from rdm.audit_for_gaps import _find_keys_in_sources, \
    _read_raw_checklists, _split_out_include_files, _extract_keys_from_checklist, _find_failing_checklist_items, \
    _next_number, _next_non_number, _components, SectionalAnalysis


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


def test_next_number():
    assert (0, '') == _next_number('')
    assert (1, '') == _next_number('0')
    assert (12345678910, '') == _next_number('0123456789')
    assert (2, '') == _next_number('00')
    assert (3, '') == _next_number('000')
    assert (103, '') == _next_number('001')
    assert (101, '') == _next_number('1')
    assert (0, 'cat') == _next_number('cat')
    assert (12303, '') == _next_number('123')
    assert (1234505, '.cat') == _next_number('12345.cat')


def test_next_nonnumber():
    assert ('', '123dog') == _next_non_number('123dog')
    assert ('cat', '123dog') == _next_non_number('cat123dog')
    assert ('', '') == _next_non_number('')


def test_components():
    assert [] == _components('')
    assert [(12303, '')] == _components('123')
    assert [(12303, 'cat')] == _components('123cat')
    assert [(12303, 'cat'), (45604, 'dog')] == _components('123cat0456dog')
    assert [(0, 'cat')] == _components('cat')


def test_sorting():
    original = [
        '62304:5.1.8.d Documentation Planning: procedures',
        '62304:5.2.1 Define and document software requirements from system requirements',
        '62304:5.1.10 Supporting items to be controlled',
        '62304:5.1.9.a Software Configuration Management Planning: controlled items',
        '62304:5.1.11 Software configuration item control before verification',
        '62304:5.1.9.b Software Configuration Management Planning: activities and tasks',
    ]
    properly_sorted = [
        '62304:5.1.8.d Documentation Planning: procedures',
        '62304:5.1.9.a Software Configuration Management Planning: controlled items',
        '62304:5.1.9.b Software Configuration Management Planning: activities and tasks',
        '62304:5.1.10 Supporting items to be controlled',
        '62304:5.1.11 Software configuration item control before verification',
        '62304:5.2.1 Define and document software requirements from system requirements',
    ]
    actual = sorted(original, key=SectionalAnalysis)
    assert properly_sorted == actual


def test_sorting_reversed():
    original = ['a:a.1', 'a:a.2', 'a:b', 'a:b.1', 'a:c.1', 'b:1', 'b:2', 'b:2.a']
    original.reverse()
    properly_sorted = ['a:a.1', 'a:a.2', 'a:b', 'a:b.1', 'a:c.1', 'b:1', 'b:2', 'b:2.a']
    actual = sorted(original, key=SectionalAnalysis)
    assert properly_sorted == actual


def test_sectional_analysis():
    alpha = SectionalAnalysis('62304:5.1.8')
    beta = SectionalAnalysis('62304:5.1.9')
    gamma = SectionalAnalysis('62304:5.1.10')
    assert alpha < beta
    assert beta < gamma
    assert alpha < gamma
