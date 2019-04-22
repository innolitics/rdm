import os
import shutil

import pytest

from rdm.render import invert_dependencies, join_to, render_template, section_number_depth, section_number_filter


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
    @pytest.fixture(autouse=True)
    def setup(self, tmpdir):
        self.tmpdir = tmpdir.strpath
        try:
            os.mkdir(self.tmpdir)
        except OSError:
            pass

    def teardown(self):
        try:
            shutil.rmtree(self.tmpdir)
        except OSError:
            pass

    def render_from_string(self, input_string, context, filters=None):
        # Work from temp directory: jinja file system loader does not like absolute paths.
        os.chdir(self.tmpdir)
        input_file_name = "in_rendering.md"
        with open(input_file_name, 'w') as in_file:
            in_file.write(input_string)
        output_file_name = "out_rendering.md"
        render_template(input_file_name, context, output_file_name, filters)
        with open(output_file_name) as result:
            return result.read()

    def test_simple_template(self):
        context = {}
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification.\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_audited_template(self):
        context = {'system': {"auditor_notes": True}}
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
            }
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

    def test_render_one_filter(self):
        def doubler(generator):
            for line in generator:
                yield '_'.join([line, 'Twice', line])

        input_string = "apple\nbanana\ncherry"
        expected_result = "apple_Twice_apple\nbanana_Twice_banana\ncherry_Twice_cherry\n"
        actual_result = self.render_from_string(input_string, context={}, filters=[doubler])
        assert actual_result == expected_result

    def test_render_two_filters(self):
        def doubler(generator):
            for line in generator:
                yield '_'.join([line, 'Twice', line])

        def upper(generator):
            for line in generator:
                yield line.upper()

        input_string = "apple\nbanana\ncherry"
        expected_result = "APPLE_Twice_APPLE\nBANANA_Twice_BANANA\nCHERRY_Twice_CHERRY\n"
        actual_result = self.render_from_string(input_string, context={}, filters=[upper, doubler])
        assert actual_result == expected_result


def test_section_number_depth():
    assert section_number_depth('') == 0
    assert section_number_depth('# hello') == 1
    assert section_number_depth('##') == 2
    assert section_number_depth('### plus some #####') == 3


SECTION_NUMBER_INPUT = """preceding
# This is the first section
Hello from first section.
## This is the first subsection
Hello from first of top.
# This is the second section
Hello from second section.
## This is the second subsection
Hello from first of second.
#### This is a deeper section
More Stuff
## This is the third subsection
Hello from second of second.
"""

EXPECTED_SECTION_NUMBER_OUTPUT = """preceding
# 1 This is the first section
Hello from first section.
## 1.1 This is the first subsection
Hello from first of top.
# 2 This is the second section
Hello from second section.
## 2.1 This is the second subsection
Hello from first of second.
#### 2.1.1.1 This is a deeper section
More Stuff
## 2.2 This is the third subsection
Hello from second of second.
"""


def test_section_number_filter_direct():
    generator = (line for line in SECTION_NUMBER_INPUT.split('\n'))
    actual_output = '\n'.join([item for item in section_number_filter(generator)])
    assert actual_output == EXPECTED_SECTION_NUMBER_OUTPUT
