import os
import shutil
import subprocess
import sys
from collections import OrderedDict
from importlib import import_module

import yaml


# See https://stackoverflow.com/questions/16782112/


def represent_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def load_yaml(data_filename):
    with open(data_filename) as data_file:
        data_string = data_file.read()
    try:
        return yaml.load(data_string, Loader=yaml.SafeLoader)
    except yaml.YAMLError as e:
        raise ValueError('"{}" contains invalid YAML: {}'.format(data_filename, e))


def write_yaml(data, yml_file):
    Dumper = yaml.SafeDumper
    Dumper.ignore_aliases = lambda self, data: True
    yaml.add_representer(OrderedDict, represent_ordereddict, Dumper=Dumper)
    return yaml.dump(data, yml_file, default_flow_style=False, Dumper=Dumper)


RED_ANSI = '\033[31m'
YELLOW_ANSI = '\033[33m'
END_COLOR_ANSI = '\033[0m'


def print_error(message):
    print(RED_ANSI + message + END_COLOR_ANSI, file=sys.stderr)


def print_warning(message):
    print(YELLOW_ANSI + message + END_COLOR_ANSI, file=sys.stderr)


def print_info(message):
    print(message, file=sys.stderr)


def remove_carriage_return(string):
    return string.replace('\r', '').strip()


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
        context[key] = load_yaml(data_filename)
    return context


def repo_root():
    root_as_bytes = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
    return root_as_bytes.strip().decode('ascii')


def and_list_str(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + ' and ' + items[1]
    else:
        return ', '.join(items[:-2] + [and_list_str(items[-2:])])


def use_auto_section_numbering(context):
    filter_specifcation_list = context.get('system', {}).get('post_filters', [])
    return 'auto_section_numbers' in filter_specifcation_list


def empty_formatter(spacing, tag, content):
    return ''


def plain_formatter(spacing, tag, content):
    return '{spacing}[{tag}:{content}]'.format(spacing=spacing, tag=tag, content=content)


def sans_prefix_formatter(spacing, tag, content):
    return '{spacing}[{content}]'.format(spacing=spacing, content=content)


def create_formatter_with_string(format_string):
    def custom_formatter(spacing, tag, content):
        return format_string.format(spacing=spacing, tag=tag, content=content)

    return custom_formatter


def load_class(class_descriptor):
    module_name, class_name = extract_module_and_class(class_descriptor)
    module = import_module(module_name)
    return getattr(module, class_name)


def extract_module_and_class(descriptor):
    parts = descriptor.split('.')
    module_name = '.'.join(parts[:-1])
    class_name = parts[-1]
    return module_name, class_name


def post_processing_filter_list(environment):
    return getattr(environment, 'rdm_post_process_filters', [])
