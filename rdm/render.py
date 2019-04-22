import collections

import jinja2
from jinja2.environment import TemplateStream

from rdm.audit_notes import AuditNoteExtension, plain_formatter, create_formatter_with_string
from rdm.util import use_auto_section_numbering


def invert_dependencies(objects, id_key, dependencies_key):
    # TODO: add docstring
    inverted = collections.defaultdict(lambda: set())
    for o in objects:
        for d in o[dependencies_key]:
            inverted[d].add(o[id_key])
    inverted_as_list = list(inverted.items())
    return sorted(inverted_as_list, key=lambda i: i[0].split('-'))


def join_to(foreign_keys, table, primary_key='id'):
    '''
    Given a set of ids for an object, and a list of the objects these ids refer
    to, select out the objects by joining using the specified primary key
    (which defaults to 'id').
    '''
    joined = []
    for foreign_key in foreign_keys:
        selected_row = None
        for row in table:
            if row[primary_key] == foreign_key:
                selected_row = row
                break
        joined.append(selected_row)
    return joined


def render_template(template_filename, context, output_file, filters=None):
    if filters is None:
        filters = []
    if use_auto_section_numbering(context):
        filters.append(section_number_filter)
    filters = [split_into_lines] + filters + [append_newlines]
    loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader('.'),
        jinja2.PackageLoader('rdm', '.'),
    ])
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        loader=loader,
        extensions=[AuditNoteExtension],
    )

    environment.filters['invert_dependencies'] = invert_dependencies
    environment.filters['join_to'] = join_to

    system_dict = context.get('system', {})
    audit_notes = system_dict.get('auditor_notes')
    if audit_notes:
        environment.audit_note_default_formatter = plain_formatter
        special_formats = system_dict.get('auditor_note_formats')
        if special_formats:
            for format_tag, formatter in special_formats.items():
                if isinstance(formatter, str):
                    formatter = create_formatter_with_string(formatter)
                environment.audit_note_formatting_dictionary[format_tag] = formatter

    template = environment.get_template(template_filename)
    generator = template.generate(**context)
    for filter in filters:
        generator = (x for x in filter(generator))
    TemplateStream(generator).dump(output_file)


def split_into_lines(generator):
    for item in generator:
        for line in item.split('\n'):
            yield line


def append_newlines(generator):
    for item in generator:
        yield item + '\n'


def section_number_filter(generator):
    section_list = []
    for line in generator:
        section_depth = section_number_depth(line)
        if section_depth == 0:
            yield line
        else:
            if section_depth > len(section_list):
                while section_depth > len(section_list):
                    section_list.append(1)
            else:
                while section_depth < len(section_list):
                    section_list.pop()
                section_list[section_depth - 1] += 1
            formatted_section_number = '.'.join([
                str(section_number) for section_number in section_list])
            yield line[0:section_depth] + ' ' + formatted_section_number + line[section_depth:]


def section_number_depth(line):
    for index in range(len(line)):
        if line[index] != '#':
            return index
    return len(line)
