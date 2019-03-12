import os

import pytest

from rdm.doctor import check_data_file, check_schema


@pytest.fixture
def basic_schema():
    return {
        'type': 'object',
        'additionalProperties': False,
        'properties': {
            'a': {
                'type': 'string',
                'enum': ['A', 'B', 'C'],
            },
        },
        'required': ['a'],
    }


def test_check_schema_valid(basic_schema):
    errors = check_schema(basic_schema, {'a': 'A'})
    assert errors == []


def test_check_schema_invalid_value(basic_schema):
    errors = check_schema(basic_schema, {'a': 'D'})
    assert len(errors) == 1
    assert "'D' is not one of ['A', 'B', 'C']" == errors[0]


def test_check_schema_extra_property(basic_schema):
    errors = check_schema(basic_schema, {'a': 'A', 'b': 'B'})
    assert len(errors) == 1
    assert 'Additional properties' in errors[0]


def test_check_schema_missing_property(basic_schema):
    errors = check_schema(basic_schema, {})
    assert len(errors) == 1
    assert "'a' is a required property" == errors[0]


def test_check_data_file_invalid_file(basic_schema, tmpdir):
    file_to_schema = {'dummy.yml': 'basic'}
    schemas = {'basic': basic_schema}
    filename = os.path.join(str(tmpdir), 'dummy.yml')
    with open(filename, 'w') as f:
        f.write('[invalid yaml')
    data, errors = check_data_file(file_to_schema, schemas, filename)
    assert data is None
    assert len(errors) == 1
    assert 'dummy.yml' in errors[0]


def test_check_data_file_no_match(basic_schema, tmpdir):
    file_to_schema = {'dummy.yml': 'basic'}
    schemas = {'basic': basic_schema}
    filename = os.path.join(str(tmpdir), 'bobby.yml')
    with open(filename, 'w') as f:
        f.write('[1, 2, 3]')
    data, errors = check_data_file(file_to_schema, schemas, filename)
    assert data is None
    assert len(errors) == 0


def test_check_data_file_match_invalid(basic_schema, tmpdir):
    file_to_schema = {'dummy.yml': 'basic'}
    schemas = {'basic': basic_schema}
    filename = os.path.join(str(tmpdir), 'dummy.yml')
    with open(filename, 'w') as f:
        f.write('[1, 2, 3]')
    data, errors = check_data_file(file_to_schema, schemas, filename)
    assert data == {'basic': [1, 2, 3]}
    assert len(errors) == 1


def test_check_data_file_match_valid(basic_schema, tmpdir):
    file_to_schema = {'dummy.yml': 'basic'}
    schemas = {'basic': basic_schema}
    filename = os.path.join(str(tmpdir), 'dummy.yml')
    with open(filename, 'w') as f:
        f.write('a: B')
    data, errors = check_data_file(file_to_schema, schemas, filename)
    assert data == {'basic': {'a': 'B'}}
    assert len(errors) == 0
