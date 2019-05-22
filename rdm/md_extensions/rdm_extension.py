from jinja2 import nodes
from jinja2.ext import Extension

from rdm.util import post_processing_filter_list


class RdmExtension(Extension):

    def __init__(self, environment):
        super().__init__(environment)

        # add the post processing list to the environment.
        if not hasattr(environment, 'rdm_post_process_filters'):
            environment.extend(rdm_post_process_filters=[])

    def preprocess(self, source, name, filename=None):
        self.check_add_post_filter()
        self.on_start_of_parsing()
        return source

    def on_start_of_parsing(self):
        pass

    # Check if there is a post_process_filter method.
    # If so add it to the post filtering list if it is not already added.
    def check_add_post_filter(self):
        post_filter = getattr(self, 'post_process_filter', None)
        current_post_filters = post_processing_filter_list(self.environment)
        if post_filter and post_filter not in current_post_filters:
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
