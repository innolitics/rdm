import pytest

from rdm.md_extensions.audit_notes import audit_preprocess, _find_trailing_space, _find_end_marker
from tests.util import render_from_string


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


class TestAuditNoteExtension:
    def test_without_extension(self):
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification [[1234:9.8.7.6]].\n"
        actual_result = render_from_string(input_string)
        assert actual_result == expected_result

    def test_simple_template_with_audit_exclusion(self):
        config = {
            'md_extensions': ['rdm.md_extensions.AuditNoteExclusionExtension'],
        }
        input_string = "Sample specification [[1234:9.8.7.6]]."
        expected_result = "Sample specification.\n"
        actual_result = render_from_string(input_string, config=config)
        assert actual_result == expected_result

    def test_double_template_with_audit_exclusion(self):
        config = {
            'md_extensions': ['rdm.md_extensions.AuditNoteExclusionExtension'],
        }
        input_string = "Sample specification [[1234:9.8.7.6]]. Sample specification [[1234:9.8.7.6]]"
        expected_result = "Sample specification. Sample specification\n"
        actual_result = render_from_string(input_string, config=config)
        assert actual_result == expected_result
