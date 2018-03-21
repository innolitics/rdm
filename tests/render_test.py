import pytest
import jinja2

from rdm.render import extract_document_data, construct_environment


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


def function_loader(templates):
    def loader(template_name):
        assert template_name in templates
        template = templates[template_name]
        lines = template.split('\n')[1:]
        first_line = lines[0]
        strip_length = len(first_line) - len(first_line.lstrip())
        return '\n'.join(line[strip_length:] for line in lines)
    return jinja2.FunctionLoader(loader)


def test_document_context():
    environment = construct_environment()
    templates = {}
    environment.loader = function_loader({
        'parent': '''
        ---
        name: parent
        ---
        {{ document.name }}
        '''
    })
    template = environment.get_template('parent')
    assert template.render() == 'parent'


def test_document_context_with_child():
    environment = construct_environment()
    templates = {}
    environment.loader = function_loader({
        'parent': '''
        ---
        name: parent
        ---
        {{ document.name }}
        ''',
        'child': '''
        ---
        name: child
        ---
        {% extends "parent" %}
        '''
    })
    template = environment.get_template('child')
    assert template.render() == 'child'


def test_document_context_with_child_no_context_override():
    environment = construct_environment()
    templates = {}
    environment.loader = function_loader({
        'parent': '''
        ---
        name: parent
        ---
        {{ document.name }}
        ''',
        'child': '''
        {% extends "parent" %}
        '''
    })
    template = environment.get_template('child')
    assert template.render() == 'parent'
