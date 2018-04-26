from rdm.render import invert_dependencies


def test_invert_dependencies_single():
    objects = [
        {'id': 'a', 'dependencies': [1, 2, 3]}
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = {1: {'a'}, 2: {'a'}, 3: {'a'}}
    assert actual == expected


def test_invert_dependencies_multiple():
    objects = [
        {'id': 'a', 'dependencies': [1, 2, 3]},
        {'id': 'b', 'dependencies': [1, 2, 4]},
    ]
    actual = invert_dependencies(objects, 'id', 'dependencies')
    expected = {1: {'a', 'b'}, 2: {'a', 'b'}, 3: {'a'}, 4: {'b'}}
    assert actual == expected
