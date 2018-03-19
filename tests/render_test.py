import pytest

from rdm.cli import extract_document_data


def test_extract_document_data_no_header():
    assert extract_document_data('') == ('', None)
    assert extract_document_data('Testing') == ('Testing', None)
    assert extract_document_data('--Testing') == ('--Testing', None)
    assert extract_document_data('---Testing') == ('---Testing', None)


def test_extract_document_data_empty_header():
    assert extract_document_data('---\n---\nTest') == ('Test', None)


def test_extract_document_data_no_close_to_front_matter():
    with pytest.raises(ValueError):
        extract_document_data('---\nTest')


def test_extract_document_data_invalid_yaml():
    with pytest.raises(ValueError):
        extract_document_data('---\n{\n---\nTest')


def test_extract_document_data_valid_yaml():
    assert extract_document_data('---\na: b\n---\nTest') == ('Test', {'a': 'b'})
