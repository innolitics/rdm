import collections

import jinja2
from jinja2.environment import TemplateStream

from rdm.extensions import RdmExtension, dynamic_class_loader
from rdm.util import plain_formatter, create_formatter_with_string


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

def render_template_to_file(template_filename, context, output_file, loaders=None):
    generator = generate_template_output(template_filename, context, loaders=loaders)
    TemplateStream(generator).dump(output_file)

def generate_template_output(template_filename, context, loaders=None):
    if loaders is None:
        loaders = [
        jinja2.FileSystemLoader('.'),
        jinja2.PackageLoader('rdm', '.'),
        ]

    loader = jinja2.ChoiceLoader(loaders)
    system_dict = context.get('system', {})
    extension_descriptor_list = system_dict.get('extension_load_list', [])
    extensions = dynamic_class_loader(extension_descriptor_list)
    environment = jinja2.Environment(
        cache_size=0,
        undefined=jinja2.StrictUndefined,
        loader=loader,
        extensions=extensions,
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

    filters = [split_into_lines, append_newlines]
    generator = template.generate(**context)
    for filter in filters:
        generator = (x for x in filter(generator))
    source = [line for line in generator]

    output_generator = (line for line in source)
    post_process_filters = RdmExtension.post_processing_filter_list(environment)
    for filter in post_process_filters:
        output_generator = (x for x in filter(output_generator))

    return output_generator

def split_into_lines(generator):
    for item in generator:
        for line in item.split('\n'):
            yield line


def append_newlines(generator):
    for item in generator:
        yield item + '\n'

