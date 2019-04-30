import pytest

from rdm.vocabulary_extension import extract_words, extract_words_ignore_case
from tests.render_test import RenderingBaseTest


class TestVocabulary(RenderingBaseTest):
    default_context = {
        'system': {
            'extension_load_list': ['rdm.vocabulary_extension.VocabularyExtension'],
        }
    }

    @pytest.mark.parametrize('input_string, expected_result', [
        (
            "{% vocabulary %}apple\nbanana\ncherry\n{% for vocab in first_pass_output.words | sort %}{{ vocab }}{% "
            "endfor %}",
            "\napple\nbanana\ncherry\n\napple\nbanana\ncherry\n"
        ),
        (
            "{% vocabulary %}apple banana cherry\n{% if first_pass_output.has('banana') %}banana: yellow fruit\n{% "
            "endif %}",
            "\napple banana cherry\n\nbanana: yellow fruit\n\n"
        ),
        (
            "{% vocabulary %}apple Banana cherry\n{% if first_pass_output.has_ignore_case('banana') %}banana: yellow "
            "fruit\n{% endif %}",
            "\napple Banana cherry\n\nbanana: yellow fruit\n\n"
        ),
    ])
    def test_vocabulary(self, input_string, expected_result):
        actual_result = self.render_from_string(input_string, context=self.default_context)
        assert actual_result == expected_result


@pytest.mark.parametrize('lines, expected_result, expected_result_ignore_case', [
    (
        [],
        set(),
        set(),
    ),
    (
        ['alpha Beta', 'GAMMA::;;&%@', 'beta'],
        {'alpha', 'Beta', 'GAMMA', 'beta'},
        {'alpha', 'beta', 'gamma'},
    ),
])
def test_word_extraction(lines, expected_result, expected_result_ignore_case):
    actual_result = extract_words(lines)
    assert actual_result == expected_result
    actual_result_ignore_case = extract_words_ignore_case(lines)
    assert actual_result_ignore_case == expected_result_ignore_case
