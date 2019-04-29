import pytest

from tests.render_test import RenderingBaseTest


class TestVocabulary(RenderingBaseTest):
    @pytest.mark.parametrize('input_string, expected_result', [
        (
            "apple\nbanana\ncherry\n{% for vocab in first_pass_output.words | sort %}{{ vocab }}{% endfor %}",
            "apple\nbanana\ncherry\n\napple\nbanana\ncherry\n"
        ),
        (
            "apple banana cherry\n{% if first_pass_output.has('banana') %}banana: yellow fruit\n{% endif %}",
            "apple banana cherry\n\nbanana: yellow fruit\n\n"
        ),
    ])
    def test_vocabulary(self, input_string, expected_result):
        actual_result = self.render_from_string(input_string, context={})
        assert actual_result == expected_result
