import sys

import yaml


def load_yaml(yml_path):
    with open(yml_path) as yml_file:
        return yaml.load(yml_file)


def write_yaml(data, yml_path):
    with open(yml_path, 'w') as yml_file:
        return yaml.dump(data, yml_file, default_flow_style=False)


RED_ANSI = '\033[91m'
END_COLOR_ANSI = '\033[0m'


def print_error(message):
    print(RED_ANSI + message + END_COLOR_ANSI, file=sys.stderr)


def print_info(message):
    print(message, file=sys.stderr)


def remove_carriage_return(string):
    return string.replace('\r', '')
