import os

import jinja2
import yaml


def render_template(template_filename, data_filenames, output_file):
    loader = jinja2.ChoiceLoader([
        jinja2.PackageLoader('rdm', '.'),
        jinja2.FileSystemLoader('.'),
    ])
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        loader=loader,
    )
    template = environment.get_template(template_filename)
    context = context_from_data_files(data_filenames)
    template.stream(**context).dump(output_file)


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
