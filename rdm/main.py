#!/usr/bin/env python3
import sys

from rdm.cli import cli
from rdm.util import print_error


def main():
    try:
        cli(sys.argv[1:])
        sys.exit(0)
    except Exception as e:
        print_error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
