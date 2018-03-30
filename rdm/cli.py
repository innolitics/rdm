import argparse
import shutil
import sys
import pkg_resources

from rdm.render import render_template
from rdm.tex import yaml_gfm_to_tex
from rdm.github_backend import get_requirements_from_github


def cli(raw_arguments):
    args = parse_arguments(raw_arguments)
    if args.command is None:
        parse_arguments(['-h'])
    elif args.command == 'render':
        render_template(args.template, args.data_files, sys.stdout)
    elif args.command == 'tex':
        yaml_gfm_to_tex(args.input, sys.stdout)
    elif args.command == 'init':
        init(args.output)
    elif args.command == 'update_requirements':
        if args.backend == 'github':
            get_requirements_from_github()
        else:
            raise ValueError(f'Backend {args.backend} not yet supported.')


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

    requirements_help = 'populate requirements and problem reports from project management tools'
    requirements_parser = subparsers.add_parser('update_requirements', help=requirements_help)
    requirements_parser.add_argument('backend',
            help='Project management backend. Currently supported options: github')

    return parser.parse_args(arguments)
