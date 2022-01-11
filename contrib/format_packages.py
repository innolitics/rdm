#!/usr/bin/env python3
import sys
from collections import OrderedDict

import argparse
from rdm.util import write_yaml

def extract_package_info(lines):
    """
    Parse lines from `dpkg -l` output into a dictionary
    """
    packages = OrderedDict()
    for line in lines:
        props = line.split()
        packages[props[1]] = OrderedDict([
            ('states', props[0]),
            ('version', props[2]),
        ])
    return packages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Reformat the output of `dpkg` into a YAML file.')
    parser.add_argument('input', help='Path to file containing package info')
    args = parser.parse_args()

    with open(args.input) as f:
        # Skip header lines
        for _ in range(5):
            next(f)
        packages = extract_package_info(f)

    write_yaml(packages, sys.stdout)
