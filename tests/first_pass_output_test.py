import pytest

from rdm.first_pass_output import FirstPassOutput


class TestFirstPassOutput:
    def test_create(self):
        first_pass_output = FirstPassOutput()
        assert first_pass_output is not None
        assert not first_pass_output

    def test_first_pass_behavior(self):
        first_pass_output = FirstPassOutput()
        assert not first_pass_output.is_second_pass
        assert not first_pass_output.second_pass_is_requested
        assert first_pass_output.lines == []
        assert first_pass_output.second_pass_is_requested
        assert first_pass_output.lines == []
        assert first_pass_output.source == ''
        assert first_pass_output.words == set()
        assert first_pass_output.words_ignore_case == set()
        for word in ['', 'apple', 'banana']:
            assert not first_pass_output.has(word)
            assert not first_pass_output.has_ignore_case(word)

    @pytest.mark.parametrize('source_lines, expected_source, expected_words, expected_ignore_case_words',
                             [
                                 (
                                     [],
                                     '',
                                     set(),
                                     set(),
                                 ),
                                 (
                                     ['alpha Beta', 'GAMMA', 'beta'],
                                     'alpha Beta\nGAMMA\nbeta',
                                     {'alpha', 'Beta', 'GAMMA', 'beta'},
                                     {'alpha', 'beta', 'gamma'},
                                 ),
                             ])
    def test_second_pass_behavior(self, source_lines, expected_source, expected_words, expected_ignore_case_words):
        first_pass_output = FirstPassOutput(source_lines)
        assert first_pass_output.is_second_pass
        assert not first_pass_output.second_pass_is_requested
        assert first_pass_output.lines == source_lines
        assert first_pass_output.source == expected_source
        assert first_pass_output.words == expected_words
        assert first_pass_output.words_ignore_case == expected_ignore_case_words
        assert not first_pass_output.second_pass_is_requested
        for word in first_pass_output.words:
            assert first_pass_output.has(word)
        for word in first_pass_output.words_ignore_case:
            assert first_pass_output.has_ignore_case(word)
        for word in ['', 'apple', 'banana']:
            assert not first_pass_output.has(word)
            assert not first_pass_output.has_ignore_case(word)
