from importlib import import_module

from jinja2 import nodes
from jinja2.ext import Extension


class RdmExtension(Extension):

    def __init__(self, environment):
        super().__init__(environment)

        # add the post processing list to the environment.
        if not hasattr(environment, 'rdm_post_process_filters'):
            environment.extend(rdm_post_process_filters=[])

    @staticmethod
    def post_processing_filter_list(environment):
        return getattr(environment, 'rdm_post_process_filters', [])

    # Check if there is a post_process_filter method.
    # If so add it to the post filtering list if it is not already added.
    def check_add_post_filter(self):
        post_filter = getattr(self, 'post_process_filter', None)
        current_post_filters = self.post_processing_filter_list(self.environment)
        if post_filter and not post_filter in current_post_filters:
            current_post_filters.append(post_filter)

    # default parser sets up a call back that will add a post process filter if one exists.
    def parse(self, parser):
        lineno = next(parser.stream).lineno  # skip past tag token

        args = [arg for arg in generate_block_arguments(parser)]
        return nodes.CallBlock(
            self.call_method('block_callback', args), [], [], []
        ).set_lineno(lineno)

    def block_callback(self, *args, caller):
        self.check_add_post_filter()
        self.process_block_args(*args)
        return caller()

    def process_block_args(self, *args):
        pass

def generate_block_arguments(parser):
    while parser.stream.current.type != 'block_end':
        if not parser.stream.skip_if('comma'):
            yield parser.parse_expression()

def dynamic_class_loader(extension_descriptor_list):
    result = []
    for extension_descriptor in extension_descriptor_list:
        module_name, class_name = extract_module_and_class(extension_descriptor)
        module = import_module(module_name)
        class_object = getattr(module, class_name)
        result.append(class_object)
    return result

def extract_module_and_class(descriptor):
    parts = descriptor.split('.')
    module_name = '.'.join(parts[:-1])
    class_name = parts[-1]
    return module_name, class_name

