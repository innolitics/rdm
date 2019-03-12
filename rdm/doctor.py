import os

from jsonschema import Draft7Validator
import jsonschema.exceptions
import yaml

from rdm.util import repo_root, load_yaml, print_error


FILE_TO_SCHEMA = {
    'data/system.yml': 'system',
    # TODO: implement other json schemas
    # 'data/soup.yml': 'soup',
    # 'data/risk.yml': 'risk',
    # 'data/version.yml': 'version',
    # 'data/requirements.yml': 'requirements',
    'data/change_requests.yml': 'change_requests',
    'data/problem_reports.yml': 'problem_reports',
}


SCHEMAS = {
    'system': {
        'type': 'object',
        'required': [
            'safety_class',
            'level_of_concern',
            'manufacturer_name',
        ],
        'properties': {
            'safety_class': {
                'type': 'string',
                'enum': ['A', 'B', 'C'],
            },
            'level_of_concern': {
                'type': 'string',
                'enum': ['Minor', 'Moderate', 'Major'],
            },
            'manufacturer_name': {
                'type': 'string',
            }
        }
        # TODO: finish the system jsonschema
    },
    'change_requests': {
        'type': 'array',
        'items': {
            'type': 'object',
            'required': ['id', 'title', 'content'],
            'properties': {
                'id': {
                    'type': 'string',
                },
                'title': {
                    'type': 'string',
                },
                'content': {
                    'type': 'string',
                },
                'approved_by': {
                    'type': 'string',
                },
                'status': {
                    'type': 'string',
                    'enum': ['open', 'completed'],
                },
                'changes': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'required': ['verified_by', 'verified_on', 'content'],
                        'properties': {
                            'verified_by': {
                                'type': 'string',
                            },
                            'verified_on': {
                                'type': 'string',
                                'format': 'date-time',
                            },
                            'content': {
                                'type': 'string',
                            }
                        }
                    }
                },
            }
        }
    },
    'problem_reports': {
        'type': 'array',
        'items': {
            'type': 'object',
            'required': ['id', 'title', 'content', 'status'],
            'properties': {
                'id': {
                    'type': 'string',
                },
                'title': {
                    'type': 'string',
                },
                'content': {
                    'type': 'string',
                },
                'change_requests': {
                    'type': 'array',
                    'items': {
                        'type': 'string',
                    },
                },
                'status': {
                    'type': 'string',
                    'enum': ['open', 'completed', 'wontfix'],
                },
            }
        }
    }
}


def check_data_files():
    # TODO: avoid assuming data location
    all_errors = []
    data_root = os.path.join(repo_root(), 'regulatory', 'data')
    for data_filename in os.listdir(data_root):
        data_path = os.path.join(data_root, data_filename)
        _, errors = check_data_file(FILE_TO_SCHEMA, SCHEMAS, data_path)
        print_errors(errors)
        all_errors.extend(errors)
    # TODO: validate the relationships and traceability between the different
    # data files
    return all_errors


def check_data_file(file_to_schema, schemas, filepath):
    '''
    Check the data YAML files to see whether they have the appropriate format.
    '''
    # TODO: make this validation code track the line numbers somehow so that
    # you can produce more useful errors
    try:
        data = load_yaml(filepath)
    except yaml.YAMLError as e:
        msg = '"{}" is improperly formatted: {}'.format(filepath, str(e))
        return None, [msg]

    schema_key = match_schema(file_to_schema, filepath)
    if schema_key is None:
        return None, []
    else:
        schema = schemas[schema_key]
        schema_errors = check_schema(schema, data)
        return {schema_key: data}, schema_errors


def check_schema(schema, data):
    validator = Draft7Validator(schema)
    errors = validator.iter_errors(data)
    return [e.message for e in sorted(errors, key=jsonschema.exceptions.relevance)]


def match_schema(file_to_schema, filename):
    for schema_match, schema_name in file_to_schema.items():
        if filename.endswith(schema_match):
            return schema_name
    return None


def print_errors(errors):
    for error in errors:
        print_error(error)
