import jinja2
from jinja2 import FunctionLoader

from rdm.vocabulary import VocabularyExtension

some_inputs = dict(
    empty_document='',
    tagless_input="apple banana cherry\ngolf lion task\n",
    single_tag="{% vocabulary %}\n{% endvocabulary %}",
    longer_input="{% vocabulary %}\napple banana cherry\n{{ 123 }}golf lion task\n",
    including_input="{% vocabulary %}\n{% include 'tagless_input' %}",
    escaping_input="{{ '{%' }} vocabulary {{ '%}' }}\n{% include 'tagless_input' %}",
)


def some_input_loader(template_name):
    return some_inputs[template_name]


class TestVocabularyExtension:
    def setup(self):
        jinja2.clear_caches()
        self.loader = FunctionLoader(some_input_loader)
        self.environment = jinja2.Environment(
            optimized=False,
            cache_size=0,
            undefined=jinja2.StrictUndefined,
            loader=self.loader,
            extensions=[VocabularyExtension]
        )

    def test_something(self):
        jinja2.clear_caches()
        template = self.environment.get_template('escaping_input')
        source = ''.join([item for item in template.generate()])

        def second_pass_loader(template_name):
            return source

        second_pass_environment = jinja2.Environment(
            optimized=False,
            cache_size=0,
            undefined=jinja2.StrictUndefined,
            loader=FunctionLoader(second_pass_loader),
            extensions=[VocabularyExtension]
        )
        second_pass_template = second_pass_environment.get_template('')
        second_pass_source = ''.join([item for item in second_pass_template.generate()]) # noqa
        pass

    # @pytest.mark.parametrize('template_name, expected_words', [
    #     ('empty_document', []),
    #     ('tagless_input', []),
    #     ('single_tag', []),
    #     # ('longer_input', []),
    # ])
    # def test_vocabulary(self, template_name, expected_words):
    #     template = self.environment.get_template(template_name)
