import pytest

from rdm.tex import _extract_yaml_front_matter


def test_extract_yaml_front_matter_no_header():
    with pytest.raises(ValueError):
        assert _extract_yaml_front_matter('---Testing')


def test_extract_yaml_front_matter_empty_header():
    assert _extract_yaml_front_matter('---\n---\nTest') == ('Test', None)


def test_extract_yaml_front_matter_no_close_to_front_matter():
    with pytest.raises(ValueError):
        _extract_yaml_front_matter('---\nTest')


def test_extract_yaml_front_matter_invalid_yaml():
    with pytest.raises(ValueError):
        _extract_yaml_front_matter('---\n{\n---\nTest')


def test_extract_yaml_front_matter_valid_yaml():
    assert _extract_yaml_front_matter('---\na: b\n---\nTest') == ('Test', {'a': 'b'})


def test_extract_yaml_front_matter_valid_yaml_extra_hr():
    assert _extract_yaml_front_matter('---\na: b\n---\nTest---') == ('Test---', {'a': 'b'})
