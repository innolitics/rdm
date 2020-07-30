import pytest

from rdm.audit_for_gaps import _extract_keys_from_checklists, _find_keys_in_sources, _find_failing_checklists


@pytest.fixture
def example_checklists():
    return [
        {
            'author': 'Smedley',
            'specification': 'yada',
            'requirements': [
                {
                    'description': 'bla',
                    'rules': [
                        {
                            'refs': ['banana', 'apple']
                        },
                        {
                            'refs': ['banana', 'cherry']
                        },
                    ]
                },
                {
                    'description': 'bla bla',
                    'rules': [
                        {
                            'refs': ['cherry', 'dates']
                        },
                    ]
                }
            ],
        },
        {
            'author': 'Smedley Junior',
            'specification': 'yada yada',
            'requirements': [
                {
                    'description': 'bla bla bla',
                    'rules': [
                        {
                            'refs': ['banana']
                        },
                        {
                            'refs': ['apple']
                        },
                    ]
                },
                {
                    'description': 'bla bla bla bla',
                    'rules': [
                        {
                            'refs': ['banana', 'dates']
                        },
                    ]
                }
            ],
        }
    ]


document_a = "We like apple pie."
document_b = "We hate banana splits."
document_ac = "We like apple pie and cherry pie."
document_ad = "Never put dates in apple pie."
all_four_keys = {'apple', 'banana', 'cherry', 'dates'}


def test_extract_keys_from_checklists(example_checklists):
    expected_keys = all_four_keys
    actual_keys = set(_extract_keys_from_checklists(example_checklists))
    assert actual_keys == expected_keys


def test_find_keys_in_sources():
    expected_keys = {'apple', 'banana', 'cherry'}
    documents = [document_a, document_b, document_ac]
    actual_keys = set(_find_keys_in_sources(documents, all_four_keys))
    assert actual_keys == expected_keys


def test_find_failing_checklists_should_pass(example_checklists):
    documents = [document_a, document_b, document_ac, document_ad]
    failures = _find_failing_checklists(documents, example_checklists)
    assert len(failures) == 0


def test_find_failing_checklists_should_all_fail(example_checklists):
    documents = [document_a, document_b, document_ac]
    failures = _find_failing_checklists(documents, example_checklists)
    assert len(failures) == 2
    #  Check that other information gets passed along
    assert 'Smedley' == failures[0].get('author')
    assert 'Smedley Junior' == failures[1].get('author')


def test_find_failing_checklists_should_fail_once(example_checklists):
    documents = [document_a, document_b, document_ad]
    failures = _find_failing_checklists(documents, example_checklists)
    assert len(failures) == 1
    assert 'yada' == failures[0].get('specification')
