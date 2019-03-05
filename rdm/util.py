import sys
import os
import subprocess
import shutil

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


def copy_directory(dir_source, dir_dest):
    if not os.path.exists(dir_dest):
        os.makedirs(dir_dest)
    for item in os.listdir(dir_source):
        item_source = os.path.join(dir_source, item)
        item_dest = os.path.join(dir_dest, item)
        # check if these hooks already exist, ask user, maybe rename existing one
        shutil.copy2(item_source, item_dest)
        subprocess.call(['chmod', '+x', item_dest])


def context_from_data_files(data_filenames):
    context = {}
    for data_filename in data_filenames:
        key, _ = os.path.splitext(os.path.basename(data_filename))
        if key in context:
            raise ValueError('There is already data attached to the key "{}"'.format(key))
        with open(data_filename, 'r') as data_file:
            data_string = data_file.read()
        try:
            data = yaml.load(data_string)
        except yaml.YAMLError as e:
            raise ValueError('"{}" contains invalid YAML: {}'.format(data_filename, e))
        context[key] = data
    return context


def repo_root():
    root_as_bytes = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
    return root_as_bytes.strip().decode('ascii')
