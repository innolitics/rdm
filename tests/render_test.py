import jinja2
import pytest
from jinja2 import TemplateSyntaxError, FunctionLoader
from pytest import raises

from rdm.render import invert_dependencies, join_to, render_template_to_string


def test_invert_dependencies_single():
    objects = [
        {'id': 'a', 'dependencies': ['r-1', 'r-2']}
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = [('r-1', {'a'}), ('r-2', {'a'})]
    assert actual == expected


def test_invert_dependencies_multiple():
    objects = [
        {'id': 'a', 'dependencies': ['r-1', 'r-2', 'r-3-2']},
        {'id': 'b', 'dependencies': ['r-1', 'r-2', 'r-3-1']},
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = [
        ('r-1', {'a', 'b'}),
        ('r-2', {'a', 'b'}),
        ('r-3-1', {'b'}),
        ('r-3-2', {'a'}),
    ]
    assert actual == expected


def test_join_to_basic():
    foreign_keys = ['1', '3']
    table = [
        {'id': '1', 'data': 'a'},
        {'id': '2', 'data': 'b'},
    ]
    assert join_to(foreign_keys, table) == [{'id': '1', 'data': 'a'}, None]
    assert join_to(foreign_keys, table, 'data') == [None, None]


class RenderingBaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, tmpdir):
        jinja2.clear_caches()

    def render_from_string(
            self,
            input_string=None,
            context=None,
            template_name=None,
            input_dictionary=None
    ):
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

        return render_template_to_string(template_name, context, loaders=loaders)


class TestRendering(RenderingBaseTest):

    def test_render_no_filtering(self):
        input_string = "apple\nbanana\ncherry\n"
        expected_result = input_string
        actual_result = self.render_from_string(input_string, context={})
        assert actual_result == expected_result

    def test_undefined(self):
        with raises(TemplateSyntaxError):
            input_string = "{% huhwhat 'hotel', 'california' %}"
            self.render_from_string(input_string, context={})
