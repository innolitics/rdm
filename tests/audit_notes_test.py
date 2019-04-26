import pytest

from rdm.audit_notes import audit_preprocess, _find_trailing_space, _find_tag_and_content, _find_end_marker
from rdm.util import create_formatter_with_string, plain_formatter
from tests.render_test import RenderingBaseTest

fancy_formatter = create_formatter_with_string('{spacing}***[{tag}{content}]***')


class TestAuditPreprocess:
    @pytest.mark.parametrize('arg, expected_lead, expected_tail', [
        ('', '', ''),
        ('abc', 'abc', ''),
        (' xyz', ' xyz', ''),
        ('xyz ', 'xyz', ' '),
        ('xyz  ', 'xyz ', ' '),
        ('apple banana  ', 'apple banana ', ' '),
    ])
    def test_find_trailing_space(self, arg, expected_lead, expected_tail):
        actual_lead, actual_tail = _find_trailing_space(arg)
        assert actual_lead == expected_lead
        assert actual_tail == expected_tail

    @pytest.mark.parametrize('arg, expected_lead, expected_tail', [
        ('', '', None),
        ('abc]', 'abc]', None),
        ('abc]]', 'abc', ''),
        ('abc]]xyz', 'abc', 'xyz'),
    ])
    def test_find_end_marker(self, arg, expected_lead, expected_tail):
        actual_lead, actual_tail = _find_end_marker(arg)
        assert actual_lead == expected_lead
        assert actual_tail == expected_tail

    @pytest.mark.parametrize('arg, expected_tag, expected_content', [
        ('', '', ''),
        ('abc', 'abc', ''),
        ('xyz:', 'xyz', ':'),
        ('abc:xyz', 'abc', ':xyz'),
    ])
    def test_tag_and_content(self, arg, expected_tag, expected_content):
        actual_tag, actual_content = _find_tag_and_content(arg)
        assert actual_tag == expected_tag
        assert actual_content == expected_content

    def check_preprocess(self, source):
        formatter_dictionary = {
            '62340': plain_formatter,
            '99999': fancy_formatter,
        }
        return audit_preprocess(source, formatter_dictionary)

    def test_handles_empty(self):
        assert self.check_preprocess("") == ""

    def test_handles_plain(self):
        assert self.check_preprocess("this has no markers") == "this has no markers"

    def test_handles_simple(self):
        assert self.check_preprocess("has a marker -->[[62340:1.2.3.4]]<-- here") == \
               "has a marker -->[62340:1.2.3.4]<-- here"

    def test_handles_fancy(self):
        assert self.check_preprocess("has a fancy marker -->[[99999:1.2.3.4]]<-- here") == \
               "has a fancy marker -->***[99999:1.2.3.4]***<-- here"

    def test_handles_single_space(self):
        assert self.check_preprocess("has a marker --> [[62340:1.2.3.4]]<-- here") == \
               "has a marker --> [62340:1.2.3.4]<-- here"

    def test_handles_unknown(self):
        assert self.check_preprocess("has a marker -->[[12345:1.2.3.4]]<-- here") == \
               "has a marker --><-- here"

    def test_skips_single_space(self):
        assert self.check_preprocess("has unknown marker --> [[1234:1.2.3.4]]<-- here") == \
               "has unknown marker --><-- here"


class TestAuditNoteExtension(RenderingBaseTest):

    def test_without_extension(self):
        context = {
            'system': {
            }
        }
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification [[1234:9.8.7.6]].\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_simple_template_without_audit_notes_tag(self):
        context = {
            'system': {
                'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
            }
        }
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification.\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_audited_template_with_no_special_formats(self):
        context = {
            'system': {
                'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
            }
        }
        input_string = "{% audit_notes %}Sample specification [[1234:9.8.7.6]]."
        expected_result = "\nSample specification [1234:9.8.7.6].\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result

    def test_custom_audited_template(self):
        context = {'system': {
            "auditor_note_formats": {
                '4321': ' NOT USED',
                '1234': '{spacing}***{tag}**{content}*'
            },
            'extension_load_list': ['rdm.audit_notes.AuditNoteExtension'],
        }}
        input_string = "{% audit_notes system.auditor_note_formats %}Sample specification [[4321:9.8.7.6]] and [[1234:9.8.7.6]] and  [[999:9.8.7.6]]."
        expected_result = "\nSample specification NOT USED and ***1234**:9.8.7.6* and  [999:9.8.7.6].\n"
        actual_result = self.render_from_string(input_string, context)
        assert actual_result == expected_result
