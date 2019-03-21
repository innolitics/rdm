import io
from collections import OrderedDict

from rdm.util import and_list_str, write_yaml


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
