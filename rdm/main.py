import argparse
import sys
import traceback

import yaml

from rdm.audit_for_gaps import audit_for_gaps, list_default_checklists
from rdm.collect import collect_from_files
from rdm.doctor import check_data_files
from rdm.hooks import install_hooks
from rdm.init import init
from rdm.pull import pull_from_project_manager
from rdm.render import render_template_to_file
from rdm.tex import yaml_gfm_to_tex
from rdm.translate import translate_test_results, XML_FORMATS
from rdm.util import context_from_data_files, print_error, load_yaml


def main():
    try:
        exit_code = cli(sys.argv[1:])
        sys.exit(exit_code)
    except Exception:
        print_error(traceback.format_exc())
        sys.exit(1)


def cli(raw_arguments):
    exit_code = 0
    args = parse_arguments(raw_arguments)
    if args.command is None:
        parse_arguments(['-h'])
    elif args.command == 'render':
        context = context_from_data_files(args.data_files)
        config = load_yaml(args.config)
        render_template_to_file(config, args.template, context, sys.stdout)
    elif args.command == 'tex':
        context = context_from_data_files(args.data_files)
        yaml_gfm_to_tex(args.input, context, sys.stdout)
    elif args.command == 'init':
        init(args.output)
    elif args.command == 'pull':
        pull_from_project_manager(args.config)
    elif args.command == 'hooks':
        install_hooks(args.dest)
    elif args.command == 'collect':
        snippets = collect_from_files(args.files)
        yaml.dump(snippets, sys.stdout)
    elif args.command == 'doctor':
        errors = check_data_files()
        if errors:
            exit_code = 1
    elif args.command == 'translate':
        translate_test_results(args.format, args.input, args.output)
    elif args.command == 'gap':
        exit_code = audit_for_gaps(args.checklist, args.files, args.list)
    elif args.command == 'checklists':
        list_default_checklists()
    return exit_code


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(prog='rdm')
    subparsers = parser.add_subparsers(dest='command', metavar='<command>')

    init_help = 'copy the default templates etc. into the output directory'
    init_parser = subparsers.add_parser('init', help=init_help)
    init_output_help = 'Path where templates are copied'
    init_parser.add_argument('-o', '--output', default='regulatory', help=init_output_help)

    render_help = 'render a template using the specified data files'
    render_parser = subparsers.add_parser('render', help=render_help)
    render_parser.add_argument('template')
    render_parser.add_argument('config', help='Path to project `config.yml` file')
    render_parser.add_argument('data_files', nargs='*')

    tex_help = 'translate a yaml+gfm file into a tex file using pandoc'
    tex_parser = subparsers.add_parser('tex', help=tex_help)
    tex_parser.add_argument('input')
    tex_parser.add_argument('data_files', nargs='*')

    pull_help = 'pull data from the project management tool'
    pull_parser = subparsers.add_parser('pull', help=pull_help)
    pull_parser.add_argument('config', help='Path to project `config.yml` file')

    gap_help = 'use checklist to verify documents have expected references to particular standard(s)'
    gap_parser = subparsers.add_parser('gap', help=gap_help)
    gap_parser.add_argument('-l', '--list', action='store_true', help='List built-in checklists')
    gap_parser.add_argument('checklist', nargs='?')
    gap_parser.add_argument('files', nargs='*')

    hooks_help = 'install githooks in current repository'
    hooks_parser = subparsers.add_parser('hooks', help=hooks_help)
    hooks_parser.add_argument('dest', nargs='?', help='Path where hooks are saved')

    collect_help = 'collect documentation snippets into a yaml file'
    collect_parser = subparsers.add_parser('collect', help=collect_help)
    collect_parser.add_argument('files', nargs='*')

    doctor_help = 'check your regulatory docs for potential problems'
    subparsers.add_parser('doctor', help=doctor_help)

    translate_help = 'translate test output to create test result yaml file'
    translate_parser = subparsers.add_parser('translate', help=translate_help)
    translate_parser.add_argument('format', choices=XML_FORMATS)
    translate_parser.add_argument('input')
    translate_parser.add_argument('output')

    return parser.parse_args(arguments)


if __name__ == '__main__':
    main()
