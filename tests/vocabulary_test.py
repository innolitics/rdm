import pytest

from rdm.md_extensions.vocabulary_extension import extract_words, extract_words_ignore_case
from tests.util import render_from_string


@pytest.mark.parametrize('input_string, expected_result', [
    (
        "apple\nbanana\ncherry\n{% for vocab in first_pass_output.words | sort %}[{{ vocab }}]{% "
        "endfor %}",
        "apple\nbanana\ncherry\n[apple][banana][cherry]\n"
    ),
    (
        "apple banana cherry\n{% if first_pass_output.has('banana') %}banana: yellow fruit\n{% "
        "endif %}",
        "apple banana cherry\nbanana: yellow fruit\n"
    ),
    (
        "apple Banana cherry\n{% if first_pass_output.has_ignore_case('banana') %}banana: yellow "
        "fruit\n{% endif %}",
        "apple Banana cherry\nbanana: yellow fruit\n"
    ),
])
def test_vocabulary(input_string, expected_result):
    config = {
        'md_extensions': ['rdm.md_extensions.vocabulary_extension.VocabularyExtension'],
    }

    actual_result = render_from_string(input_string, config=config)
    assert actual_result == expected_result


def test_filtering():
    config = {
        'md_extensions': ['rdm.md_extensions.vocabulary_extension.VocabularyExtension'],
    }
    context = {
        'stuff': ['apple', 'cherry', 'egg']
    }
    input_string = 'apple, banana, cherry, plum\n{% for thing in stuff | present_in(first_pass_output.source) %} ' \
                   '--->{{thing}}{% endfor %}'
    expected_result = 'apple, banana, cherry, plum\n --->apple --->cherry\n'
    actual_result = render_from_string(input_string, context, config=config)
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
