#!/usr/bin/env python3
import sys
import traceback

from rdm.cli import cli
from rdm.util import print_error


def main():
    try:
        exit_code = cli(sys.argv[1:])
        sys.exit(exit_code)
    except Exception:
        print_error(traceback.format_exc())
        sys.exit(1)


if __name__ == '__main__':
    main()
