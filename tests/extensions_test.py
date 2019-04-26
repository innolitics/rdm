import jinja2
import pytest
from jinja2 import FunctionLoader

from rdm.extensions import RdmExtension


class DummyExtension(RdmExtension):
    tags = set(['dummy_extension'])


def dummy_load(template_name):
    return ''


class TestAddExtensionConfigurationToEnvironment:
    def setup(self):
        self.loader = FunctionLoader(dummy_load)
        self.empty_environment = jinja2.Environment(
            optimized=False,
            cache_size=0,
            undefined=jinja2.StrictUndefined,
            loader=self.loader,
        )
        self.environment = jinja2.Environment(
            optimized=False,
            cache_size=0,
            undefined=jinja2.StrictUndefined,
            loader=self.loader,
            extensions=[DummyExtension]
        )
        self.useful_configuration = {
            'DummyExtension': {'fruit': 'banana'},
            'NoSuchExtension':  {'fruit': 'apple'},
        }
        self.no_configuration = {
            'NoSuchExtension':  {'fruit': 'apple'},
        }

    @pytest.mark.parametrize(
        'use_empty_env, use_no_config, pass_context',
        [(use_empty_env, use_no_config, pass_context)
                        for use_empty_env in [True, False]
                        for use_no_config in [True, False]
                        for pass_context in [True, False]
                        ])
    def test_add_extension_configuration_to_environment(
            self, use_empty_env, use_no_config, pass_context):
        environment = self.empty_environment if use_empty_env else self.environment
        configuration = self.no_configuration if use_no_config else self.useful_configuration
        if pass_context:
            context = {'system':{'extension_configuration': configuration}}
        else:
            context = {'system':{}}
        if use_empty_env or use_no_config or not pass_context:
            expected_configuration = None
        else:
            expected_configuration = 'banana'

