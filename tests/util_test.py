import io
from collections import OrderedDict

import pytest
from jinja2.ext import Extension

from rdm.extensions import dynamic_class_loader, extract_module_and_class
from rdm.util import and_list_str, write_yaml


def test_and_list_str():
    assert and_list_str([]) == ''
    assert and_list_str(['1']) == '1'
    assert and_list_str(['1', '2']) == '1 and 2'
    assert and_list_str(['1', '2', '3']) == '1, 2 and 3'
    assert and_list_str(['1', '2', '3', '4']) == '1, 2, 3 and 4'


def test_write_yaml():
    string_out = io.StringIO()
    data = OrderedDict([
        ('one', 1),
        ('two', 2),
    ])
    write_yaml(data, string_out)
    assert string_out.getvalue() == 'one: 1\ntwo: 2\n'

def test_dynamic_class_loader():
    extensions = dynamic_class_loader(['rdm.audit_notes.AuditNoteExtension'])
    assert extensions is not None
    assert len(extensions) == 1
    extension = extensions[0]
    assert issubclass(extension, Extension)

@pytest.mark.parametrize('description, expected_module_name, expected_class_name', [
    ('this.that', 'this', 'that'),
    ('this.that.another', 'this.that', 'another'),
])
def test_extract_module_and_class(description, expected_module_name, expected_class_name):
    actual_module_name, actual_class_name = extract_module_and_class(description)
    assert actual_module_name == expected_module_name
    assert actual_class_name == expected_class_name


