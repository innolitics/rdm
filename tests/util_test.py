import io
import sys
from collections import OrderedDict

import pytest

from rdm.util import and_list_str, write_yaml, determine_locations, determine_relative_path, path_finder, \
    sequence_filter_applicator, filter_list_filter, all_pass_filter


def test_and_list_str():
    assert and_list_str([]) == ''
    assert and_list_str(['1']) == '1'
    assert and_list_str(['1', '2']) == '1 and 2'
    assert and_list_str(['1', '2', '3']) == '1, 2 and 3'
    assert and_list_str(['1', '2', '3', '4']) == '1, 2, 3 and 4'


def test_write_yaml():
    string_out = io.StringIO()
    data = OrderedDict([
        ('one', 1),
        ('two', 2),
    ])
    write_yaml(data, string_out)
    assert string_out.getvalue() == 'one: 1\ntwo: 2\n'


@pytest.mark.parametrize(
    'input_path, output_file, output_base, expected_result',
    [
        ('', '', '', ('.', '.', '')),
        ('', None, '', ('.', '.', sys.stdout)),
        ('', None, None, ('.', '.', sys.stdout)),
        ('./here/there/this.md', None, None, ('./here/there', './here/there', sys.stdout)),
        ('./here/there/this.md', '/some/place/out.txt', None,
         ('./here/there', '/some/place', '/some/place/out.txt')),
    ])
def test_determine_locations(
    input_path, output_file, output_base, expected_result
):
    actual_result = determine_locations(input_path, output_file, output_base)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    'source_path, path_base, expected_result',
    [
        ('/here/there/everywhere', '/here/there', 'everywhere'),
        ('/here/there', '/here/there/everywhere', '..'),
        ('/here/there/stuff/place.png', '/here/there/everywhere', '../stuff/place.png'),
        ('/here/there/sideways/../stuff/place.png', '/here/there/everywhere', '../stuff/place.png'),
    ])
def test_determine_relative_path(source_path, path_base, expected_result):
    actual_result = determine_relative_path(source_path, path_base)
    assert actual_result == expected_result

@pytest.mark.parametrize(
    'original_base, new_base, path, expected_result',
    [
        ('/here/there/everywhere', '/here/there', './images/stuff.png', 'everywhere/images/stuff.png'),
        ('/here/there/everywhere', '/here/there', '/images/stuff.png', '/images/stuff.png'),
        ('/here/there/everywhere', '/here/there', '../images/stuff.png', 'images/stuff.png'),
    ])
def test_path_finder(original_base, new_base, path, expected_result):
    finder = path_finder(original_base, new_base)
    actual_result = finder(path)
    assert actual_result == expected_result

def parenthetical_filter(text):
    return '(' + text + ')'

def bracket_filter(text):
    return '[' + text + ']'

def brace_filter(text):
    return '{' + text + '}'

@pytest.mark.parametrize('source_line, sequence, expected_result', [
    ('', [], ''),
    ('cat dog parrot', [], 'cat dog parrot'),
    ('cat dog parrot', [(4,4)], 'cat ()dog parrot'),
    ('cat dog parrot', [(0,3)], '(cat) dog parrot'),
    ('cat dog parrot', [(4,7)], 'cat (dog) parrot'),
    ('cat dog parrot', [(4,7), (8,14)], 'cat (dog) (parrot)'),
]
)
def test_sequence_filter_applicator(source_line, sequence, expected_result):
    actual_result = sequence_filter_applicator(parenthetical_filter, source_line, sequence)
    assert actual_result == expected_result
    all_pass_result = sequence_filter_applicator(all_pass_filter, source_line, sequence)
    assert all_pass_result == source_line

@pytest.mark.parametrize('text, filter_list, expected_result', [
    ('', [], ''),
    ('apple', [], 'apple'),
    ('apple', [bracket_filter], '[apple]'),
    ('apple', [parenthetical_filter, bracket_filter, brace_filter], '{[(apple)]}'),
]
)
def test_filter_list_filter(text, filter_list, expected_result):
    filter = filter_list_filter(filter_list)
    actual_result = filter(text)
    assert actual_result == expected_result
