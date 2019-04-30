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

    @pytest.mark.parametrize('source_lines, expected_source',
                             [
                                 (
                                     [],
                                     '',
                                 ),
                                 (
                                     ['alpha Beta', 'GAMMA', 'beta'],
                                     'alpha Beta\nGAMMA\nbeta',
                                 ),
                             ])
    def test_second_pass_behavior(self, source_lines, expected_source):
        first_pass_output = FirstPassOutput(source_lines)
        assert first_pass_output.is_second_pass
        assert not first_pass_output.second_pass_is_requested
        assert first_pass_output.lines == source_lines
        assert first_pass_output.source == expected_source
        assert not first_pass_output.second_pass_is_requested
