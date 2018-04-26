from rdm.render import invert_dependencies


def test_invert_dependencies_single():
    objects = [
        {'id': 'a', 'dependencies': ['r-1', 'r-2']}
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = [('r-1', {'a'}), ('r-2', {'a'})]
    assert actual == expected


def test_invert_dependencies_multiple():
    objects = [
        {'id': 'a', 'dependencies': ['r-1', 'r-2', 'r-3-2']},
        {'id': 'b', 'dependencies': ['r-1', 'r-2', 'r-3-1']},
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = [
        ('r-1', {'a', 'b'}),
        ('r-2', {'a', 'b'}),
        ('r-3-1', {'b'}),
        ('r-3-2', {'a'}),
    ]
    assert actual == expected
