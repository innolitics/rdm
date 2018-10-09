import pytest

from rdm.collect import collect_snippets


def test_no_snippets_in_empty_file():
    assert collect_snippets(['']) == {}


def test_single_snippet():
    assert collect_snippets(['RDOC test', 'Test', 'ENDRDOC']) == {'test': 'Test'}


def test_two_snippets():
    assert collect_snippets([
        'RDOC one', 'Test', 'ENDRDOC',
        'RDOC two', 'Test', 'ENDRDOC',
    ]) == {'one': 'Test', 'two': 'Test'}


def test_mismatched_start_stop_token_indents():
    with pytest.raises(ValueError):
        collect_snippets(['RDOC test', 'Test', ' ENDRDOC'])


def test_reach_end_without_end_snippet():
    with pytest.raises(ValueError):
        collect_snippets(['RDOC test', 'Test'])


def test_missing_key():
    with pytest.raises(ValueError):
        collect_snippets(['RDOC', 'Test', 'ENDRDOC'])


def test_basic_snippet_w_offset():
    assert collect_snippets(['# RDOC test', '# Test', '# ENDRDOC']) == {'test': 'Test'}


def test_multiple_rdocs_in_file():
    with pytest.raises(ValueError):
        collect_snippets(2*['# RDOC test', '# Test', '# ENDRDOC'])
