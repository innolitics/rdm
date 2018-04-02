import sys

import yaml

def get_project_settings(system_yml_path):
    with open(system_yml_path) as system_yml:
        return yaml.load(system_yml)

def print_error(message):
    print(message, file=sys.stderr)
