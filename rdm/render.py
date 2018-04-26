import collections

import jinja2


def invert_dependencies(objects, id_key, dependencies_key):
    inverted = collections.defaultdict(lambda: set())
    for o in objects:
        for d in o[dependencies_key]:
            inverted[d].add(o[id_key])
    inverted_as_list = list(inverted.items())
    return sorted(inverted_as_list, key=lambda i: i[0].split('-'))


def render_template(template_filename, context, output_file):
    loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader('.'),
        jinja2.PackageLoader('rdm', '.'),
    ])
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        loader=loader,
    )

    environment.filters['invert_dependencies'] = invert_dependencies

    template = environment.get_template(template_filename)
    template.stream(**context).dump(output_file)
