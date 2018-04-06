import sys

import yaml


def load_yaml(yml_path):
    with open(yml_path) as yml_file:
        return yaml.load(yml_file)


def write_yaml(data, yml_path):
    with open(yml_path, 'w') as yml_file:
        return yaml.dump(data, yml_file, default_flow_style=False)


def print_error(message):
    print(message, file=sys.stderr)


def remove_carriage_return(string):
    return string.replace('\r', '')
