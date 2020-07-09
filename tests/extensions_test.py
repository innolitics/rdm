import pytest
from jinja2.ext import Extension

from rdm.util import load_class, extract_module_and_class


def test_load_class():
    class_object = load_class('rdm.md_extensions.AuditNoteExclusionExtension')
    assert issubclass(class_object, Extension)


@pytest.mark.parametrize('description, expected_module_name, expected_class_name', [
    ('this.that', 'this', 'that'),
    ('this.that.another', 'this.that', 'another'),
])
def test_extract_module_and_class(description, expected_module_name, expected_class_name):
    actual_module_name, actual_class_name = extract_module_and_class(description)
    assert actual_module_name == expected_module_name
    assert actual_class_name == expected_class_name
