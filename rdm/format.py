import sys
from collections import OrderedDict

from rdm.util import write_yaml


def format_packages(file_path):
    with open(file_path) as f:
        for _ in range(5):
            next(f)
        packages = extract_package_info(f)

    write_yaml(packages, sys.stdout)


def extract_package_info(lines):
    packages = OrderedDict()
    for line in lines:
        props = line.split()
        packages[props[1]] = OrderedDict([
            ('states', props[0]),
            ('version', props[2]),
        ])
    return packages
