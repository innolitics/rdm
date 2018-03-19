import argparse
import subprocess
import os
import sys

import jinja2
import yaml


def cli(raw_arguments):
    args = parse_arguments(raw_arguments)
    if args.command is None:
        parse_arguments(['-h'])
    elif args.command == 'render':
        render(args.template, args.data_files)
    elif args.command == 'init':
        subprocess.check_call(['cp', '-R', 'init/', args.output])


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(prog='rdm')
    subparsers = parser.add_subparsers(dest='command', metavar='<command>')
    init_help = 'initialize a set of templates in the output directory'
    init_parser = subparsers.add_parser('init', help=init_help)
    init_parser.add_argument('output', default='regulatory')
    render_help = 'render a template using the specified data files'
    render_parser = subparsers.add_parser('render', help=render_help)
    render_parser.add_argument('template')
    render_parser.add_argument('data_files', nargs='*')
    return parser.parse_args(arguments)


def render(template_filename, data_filenames):
    with open(template_filename, 'r') as template_file:
        raw_string = template_file.read()
    template_string, document_data = extract_document_data(raw_string)
    template = jinja2.Template(template_string)
    context = {'document': document_data}
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
    template.stream(**context).dump(sys.stdout)


def extract_document_data(raw_string):
    if not raw_string.startswith('---\n'):
        return raw_string, None
    parts = raw_string.split('---\n')
    if len(parts) != 3:
        raise ValueError('Invalid YAML front matter; expected a closing "---" on a newline')
    document_data_string = parts[1]
    template_string = parts[2]
    try:
        document_data = yaml.load(document_data_string)
    except yaml.YAMLError as e:
        raise ValueError('Invalid YAML front matter; improperly formatted YAML: {}'.format(e))
    return template_string, document_data
