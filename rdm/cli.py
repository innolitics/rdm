import argparse
import shutil
import os
import sys
import pkg_resources

import yaml

from rdm.render import render_template
from rdm.tex import yaml_gfm_to_tex
from rdm.pull import pull_requirements_and_reports


def cli(raw_arguments):
    args = parse_arguments(raw_arguments)
    if args.command is None:
        parse_arguments(['-h'])
    elif args.command == 'render':
        context = context_from_data_files(args.data_files)
        render_template(args.template, context, sys.stdout)
    elif args.command == 'tex':
        context = context_from_data_files(args.data_files)
        yaml_gfm_to_tex(args.input, context, sys.stdout)
    elif args.command == 'init':
        init(args.output)
    elif args.command == 'pull':
        pull_requirements_and_reports(args.system_yml)


def init(output_directory):
    init_directory = pkg_resources.resource_filename(__name__, 'init')
    shutil.copytree(init_directory, output_directory)


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(prog='rdm')
    subparsers = parser.add_subparsers(dest='command', metavar='<command>')

    init_help = 'initialize a set of templates in the output directory'
    init_parser = subparsers.add_parser('init', help=init_help)
    init_parser.add_argument('-o', '--output', default='regulatory')

    render_help = 'render a template using the specified data files'
    render_parser = subparsers.add_parser('render', help=render_help)
    render_parser.add_argument('template')
    render_parser.add_argument('data_files', nargs='*')

    tex_help = 'translate a yaml+gfm file into a tex file using pandoc'
    tex_parser = subparsers.add_parser('tex', help=tex_help)
    tex_parser.add_argument('input')
    tex_parser.add_argument('data_files', nargs='*')

    pull_help = 'pull requirements and problem reports from project management tools'
    pull_parser = subparsers.add_parser('pull', help=pull_help)
    pull_parser.add_argument('system_yml', help='Path to project `system.yml` file.')

    return parser.parse_args(arguments)


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
