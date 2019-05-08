import pytest

<<<<<<< HEAD
from rdm.md_extensions.section_numbers import section_number_filter, section_number_depth
=======
from rdm.section_numbers import section_number_filter, section_number_depth
>>>>>>> master
from render_test import RenderingBaseTest


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


class TestSectionNumberExtension(RenderingBaseTest):
    default_context = {
        'system': {
            'md_extensions': ['rdm.md_extensions.section_numbers.SectionNumberExtension'],
        }
    }

    def render_from_string(self, input_string, context=None, filters=None):
        if context is None:
            context = self.default_context
        return super().render_from_string(input_string, context)

    @pytest.mark.parametrize('input_string, expected_output', [
        ('', ''),
        (SECTION_NUMBER_INPUT, EXPECTED_SECTION_NUMBER_OUTPUT),
    ])
    def test_section_numbering(self, input_string, expected_output):
        actual_output = self.render_from_string(input_string)
        assert actual_output == expected_output

    @pytest.mark.parametrize('input_string, context, expected_output', [
        ('', {}, ''),
        ('{% if fruit is defined %}banana{% endif %}', {}, ''),
        ('{% if fruit is defined %}banana{% endif %}', {'fruit': 'apple'}, 'banana\n'),
        ('## hello', {}, '## hello\n'),
        ('## hello', default_context, '## 1.1 hello\n'),
    ])
    def test_conditional_section_numbering(self, input_string, context, expected_output):
        actual_output = self.render_from_string(input_string, context=context)
        assert actual_output == expected_output
