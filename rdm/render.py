import collections

import jinja2

from rdm.audit_notes import AuditNoteExtension, plain_formatter, create_formatter_with_string


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


def render_template(template_filename, context, output_file):
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
    template.stream(**context).dump(output_file)
