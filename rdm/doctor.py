import os

from jsonschema import Draft4Validator
import jsonschema.exceptions

from rdm.util import repo_root, load_yaml, print_error


FILE_TO_SCHEMA = {
    'data/system.yml': 'system',
    # TODO: implement other json schemas
    # 'data/soup.yml': 'soup',
    # 'data/risk.yml': 'risk',
    # 'data/version.yml': 'version',
    # 'data/requirements.yml': 'requirements',
    'data/history.yml': 'history',
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
    'history': {
        'type': 'object',
        'description': 'A summary representation of the development history of the project ' \
                'as taken from a separate project management tool. Only completed development '
                'items are included here.  E.g., outstanding issues (unless they are problem '
                'reports) are not included.',
        'required': ['change_requests', 'changes'],
        'properties': {
            'change_requests': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'description': 'A change request and/or problem report.',
                    'required': ['id', 'title', 'change_ids'],
                    'properties': {
                        'id': {
                            'description': 'A unique identifier for the change request.',
                            'type': 'string',
                        },
                        'title': {
                            'type': 'string',
                        },
                        'content': {
                            'type': 'string',
                        },
                        'url': {
                            'type': 'string',
                            'description': 'Optional url that ties back to the object in the ' \
                                    'project management tool.',
                            'format': 'uri',
                        },
                        'is_problem_report': {
                            'type': 'boolean',
                            'description': 'Is this a problem report?  If true, and there are ' \
                                    'also change_ids associated with the change request, then ' \
                                    'this is both a problem report and a change request simultaneously. ' \
                                    'If this field is absent, then it is assumed to be false.',
                        },
                        'parent_id': {
                            'type': 'string',
                            'description': 'Optional linkage to a parent change request (and/or ' \
                                    'problem report).',
                        },
                        'change_ids': {
                            'type': 'array',
                            'description': 'List of ids of changes that implement the change request.',
                            'items': {
                                'type': 'string',
                            },
                        },
                    }
                }
            },
            'changes': {
                'type': 'array',
                'description': 'Represents a set of code changes which are made in response to a ' \
                        'change request, and has been merged into the master branch.',
                'items': {
                    'type': 'object',
                    'required': ['id', 'authors', 'approvals', 'content'],
                    'properties': {
                        'id': {
                            'type': 'string',
                        },
                        'authors': {
                            'type': 'array',
                            'minItems': 1,
                            'items': {
                                'type': 'object',
                                'required': ['id', 'name'],
                                'properties': {
                                    'id': {
                                        'type': 'string',
                                    },
                                    'name': {
                                        'type': 'string',
                                    },
                                },
                            },
                        },
                        'content': {
                            'type': 'string',
                        },
                        'approvals': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'required': ['id', 'content', 'reviewer'],
                                'properties': {
                                    'id': {
                                        'type': 'string',
                                    },
                                    'content': {
                                        'type': 'string',
                                    },
                                    'url': {
                                        'type': 'string',
                                        'format': 'uri',
                                    },
                                    'reviewer': {
                                        'type': 'object',
                                        'required': ['id', 'name'],
                                        'properties': {
                                            'id': {
                                                'type': 'string',
                                            },
                                            'name': {
                                                'type': 'string',
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
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
    except ValueError as e:
        return None, [str(e)]

    schema_key = match_schema(file_to_schema, filepath)
    if schema_key is None:
        return None, []
    else:
        schema = schemas[schema_key]
        schema_errors = check_schema(schema, data)
        return {schema_key: data}, schema_errors


def check_schema(schema, data):
    validator = Draft4Validator(schema)
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
