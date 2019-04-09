import os
import shutil

from rdm.render import invert_dependencies, join_to, render_template


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


class TestRendering:
    def setup(self):
        # Create a local temp directory. jinja file system loader does not like absolute paths.
        try:
            os.mkdir('tmp_docs')
        except OSError:
            pass

    def teardown(self):
        try:
            shutil.rmtree('tmp_docs')
        except OSError:
            pass

    def render_from_string(self, input_string, context):
        input_file_name = "tmp_docs/in_rendering.md"
        with open(input_file_name, 'w') as in_file:
            in_file.write(input_string)
        output_file_name = "tmp_docs/out_rendering.md"
        render_template(input_file_name, context, output_file_name)
        with open(output_file_name) as result:
            return result.read()

    def test_simple_template(self):
        context = {}
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification."
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_audited_template(self):
        context = {'system': {"auditor_notes": True}}
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification [1234:9.8.7.6]."
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_custom_audited_template(self):
        context = {'system': {
            "auditor_notes": True,
            "auditor_note_formats": {
                '4321': ' NOT USED',
                '1234': '{spacing}***{tag}**{content}*'
            }
        }}
        input_string = "Sample specification [[4321:9.8.7.6]] and [[1234:9.8.7.6]] and  [[999:9.8.7.6]]."
        expected_result = "Sample specification NOT USED and ***1234**:9.8.7.6* and  [999:9.8.7.6]."
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result
