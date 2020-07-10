import collections

import jinja2
from jinja2.environment import TemplateStream

from rdm.first_pass_output import FirstPassOutput
from rdm.util import load_class, post_processing_filter_list


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


def render_template_to_file(config, template_filename, context, output_file, loaders=None):
    generator = generate_template_output(config, template_filename, context, loaders=loaders)
    TemplateStream(generator).dump(output_file)


def render_template_to_string(config, template_filename, context, loaders=None):
    return ''.join(generate_template_output(config, template_filename, context, loaders=loaders))


def generate_template_output(config, template_filename, context, loaders=None):
    environment = _create_jinja_environment(config, loaders)
    first_pass_output = FirstPassOutput()
    environment.globals['first_pass_output'] = first_pass_output
    output_line_list = generate_template_output_lines(environment, template_filename, context)
    if first_pass_output.second_pass_is_requested:
        jinja2.clear_caches()
        first_pass_output_filled = FirstPassOutput(output_line_list)
        second_pass_environment = _create_jinja_environment(config, loaders)
        second_pass_environment.globals['first_pass_output'] = first_pass_output_filled
        output_line_list = generate_template_output_lines(second_pass_environment, template_filename, context)
    return (line for line in output_line_list)


def generate_template_output_lines(environment, template_filename, context):
    template = environment.get_template(template_filename)
    source_line_list = _generate_source_line_list(template, context)
    return [line for line in _generate_output_lines(environment, source_line_list)]


def _create_jinja_environment(config, loaders=None):
    extensions = [load_class(ed) for ed in config.get('md_extensions', [])]
    loader = _create_loader(loaders)
    environment = jinja2.Environment(
        cache_size=0,
        undefined=jinja2.StrictUndefined,
        loader=loader,
        extensions=extensions,
    )
    environment.filters['invert_dependencies'] = invert_dependencies
    environment.filters['join_to'] = join_to
    return environment


def _create_loader(loaders=None):
    if loaders is None:
        loaders = [
            jinja2.FileSystemLoader('.'),
        ]

    return jinja2.ChoiceLoader(loaders)


def _generate_source_line_list(template, context):
    generator = template.generate(**context)
    source = ''.join(generator)
    # template generator usually loses trailing new line.
    if source and source[-1] != '\n':
        source += '\n'
    return source.splitlines(keepends=True)


def _generate_output_lines(environment, source_line_list):
    output_generator = (line for line in source_line_list)
    post_process_filters = post_processing_filter_list(environment)
    for post_process_filter in post_process_filters:
        output_generator = (x for x in post_process_filter(output_generator))
    return output_generator
