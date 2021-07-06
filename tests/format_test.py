from collections import OrderedDict

from rdm.format import extract_package_info


def test_format_packages():
    assert extract_package_info([
        'ii  apt         2.0.5              amd64',
        'ii  bash        3.5.47             amd64',
        'ii  dpkg        1.19.7ubuntu3      amd64',
        'ii  python3.8   3.8.5-1~20.04.2    amd64'
    ]) == OrderedDict([
        ('apt', OrderedDict([
            ('states', 'ii'),
            ('version', '2.0.5')
        ])),
        ('bash', OrderedDict([
            ('states', 'ii'),
            ('version', '3.5.47')
        ])),
        ('dpkg', OrderedDict([
            ('states', 'ii'),
            ('version', '1.19.7ubuntu3')
        ])),
        ('python3.8', OrderedDict([
            ('states', 'ii'),
            ('version', '3.8.5-1~20.04.2')
        ]))
    ])
