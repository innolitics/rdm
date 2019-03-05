import pytest

from rdm.collect import collect_from_lines


def test_no_snippets_in_empty_file():
    assert collect_from_lines(['']) == {}


def test_single_snippet():
    assert collect_from_lines(['RDOC test', 'Test', 'ENDRDOC']) == {'test': 'Test'}


def test_two_snippets():
    assert collect_from_lines([
        'RDOC one', 'Test', 'ENDRDOC',
        'RDOC two', 'Test', 'ENDRDOC',
    ]) == {'one': 'Test', 'two': 'Test'}


def test_mismatched_start_stop_token_indents():
    with pytest.raises(ValueError):
        collect_from_lines(['RDOC test', 'Test', ' ENDRDOC'])


def test_reach_end_without_end_snippet():
    with pytest.raises(ValueError):
        collect_from_lines(['RDOC test', 'Test'])


def test_missing_key():
    with pytest.raises(ValueError):
        collect_from_lines(['RDOC', 'Test', 'ENDRDOC'])


def test_basic_snippet_w_offset():
    assert collect_from_lines(['# RDOC test', '# Test', '# ENDRDOC']) == {'test': 'Test'}


def test_basic_snippet_w_multiple_lines():
    assert collect_from_lines([
        '# RDOC test\n',
        '# 1\n',
        '#\n',
        '# 2\n',
        '# ENDRDOC']
    ) == {'test': '1\n\n2'}


def test_multiple_rdocs_in_file():
    with pytest.raises(ValueError):
        collect_from_lines(2*['# RDOC test', '# Test', '# ENDRDOC'])
