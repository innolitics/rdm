import jinja2
from jinja2 import FunctionLoader

from rdm.render import render_template_to_string


def render_from_string(
    input_string=None,
    context=None,
    config=None,
    template_name=None,
    input_dictionary=None
):
    jinja2.clear_caches()
    if config is None:
        config = {}
    if template_name is None:
        template_name = 'input.md'
    if input_dictionary is None:
        input_dictionary = {}
    if input_string is not None:
        input_dictionary[template_name] = input_string
    if context is None:
        context = {}

    def load_string(template_name):
        return input_dictionary[template_name]

    loaders = [FunctionLoader(load_string)]

    return render_template_to_string(config, template_name, context, loaders=loaders)
