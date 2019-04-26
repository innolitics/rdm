import os
import shutil

import jinja2
import pytest
from jinja2 import TemplateSyntaxError, FunctionLoader
from pytest import raises

from rdm.render import invert_dependencies, join_to, render_template_to_file, generate_template_output


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

        return ''.join(generate_template_output(template_name, context, loaders=loaders))


class TestRendering(RenderingBaseTest):
    def test_simple_template(self):
        context = {
            'system': {
                'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
            }
        }
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification.\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_audited_template(self):
        context = {
            'system': {
                "auditor_notes": True,
                'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
            }
        }
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification [1234:9.8.7.6].\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_custom_audited_template(self):
        context = {'system': {
            "auditor_notes": True,
            "auditor_note_formats": {
                '4321': ' NOT USED',
                '1234': '{spacing}***{tag}**{content}*'
            },
            'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
        }}
        input_string = "Sample specification [[4321:9.8.7.6]] and [[1234:9.8.7.6]] and  [[999:9.8.7.6]]."
        expected_result = "Sample specification NOT USED and ***1234**:9.8.7.6* and  [999:9.8.7.6].\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_render_no_filtering(self):
        input_string = "apple\nbanana\ncherry\n"
        expected_result = input_string
        actual_result = self.render_from_string(input_string, context={})
        assert actual_result == expected_result

    # def test_render_one_filter(self):
    #     def doubler(generator):
    #         for line in generator:
    #             yield '_'.join([line, 'Twice', line])
    #
    #     input_string = "apple\nbanana\ncherry"
    #     expected_result = "apple_Twice_apple\nbanana_Twice_banana\ncherry_Twice_cherry\n"
    #     actual_result = self.render_from_string(input_string, context={}, filters=[doubler])
    #     assert actual_result == expected_result
    #
    # def test_render_two_filters(self):
    #     def doubler(generator):
    #         for line in generator:
    #             yield '_'.join([line, 'Twice', line])
    #
    #     def upper(generator):
    #         for line in generator:
    #             yield line.upper()
    #
    #     input_string = "apple\nbanana\ncherry"
    #     expected_result = "APPLE_Twice_APPLE\nBANANA_Twice_BANANA\nCHERRY_Twice_CHERRY\n"
    #     actual_result = self.render_from_string(input_string, context={}, filters=[upper, doubler])
    #     assert actual_result == expected_result

    def test_undefined(self):
        with raises(TemplateSyntaxError):
            input_string = "{% huhwhat 'hotel', 'california' %}"
            actual_result = self.render_from_string(input_string, context={})
