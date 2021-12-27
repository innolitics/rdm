#!/usr/bin/env python3
import sys
import collections
import re

import yaml


def read_lines(fileobj):
    """
    Split a file into logical lines.
    """
    # Lines starting with space are considered continuations
    return re.sub(r'\n([^ ])', '\x00\\1', fileobj.read()).split('\x00')


class DottedDecimal(collections.namedtuple("DottedDecimal", ("path"))):
    """
    Arbitrary-length path of decimals, like a version number.
    1.1, 1..1 and 1.1. are considered equivalent
    """

    @classmethod
    def from_text(cls, text):
        return cls(tuple(int(p) for p in text.split(".") if p))

    @property
    def parent(self):
        parent_path = self.path[:-1]
        return DottedDecimal(parent_path) if parent_path else None

    def __str__(self):
        return ".".join(str(i) for i in self.path)


def parse_requirements(fileobj):
    """
    Parse lines from a file into a dictionary
    """
    lines = read_lines(fileobj)
    elements = collections.OrderedDict()
    parents = set()  # Set of keys known to appear above another key
    for line in lines:
        # Skip comments
        if line.strip().startswith("#"):
            continue
        key_str, text = line.split(None, 1)
        key = DottedDecimal.from_text(key_str)
        if key.parent:
            parents.add(key.parent)
        if key not in elements:
            elements[key] = collections.OrderedDict([("text", text.strip())])
        else:
            print(f"The id '{key}' occurs more than once", file=sys.stderr)
            sys.exit(1)
    for key, properties in elements.items():
        if key in parents:
            properties["type"] = "section"
    return elements


def parse_requirements_flat(fileobj):
    records = []
    for key, properties in parse_requirements(fileobj).items():
        req_id = f'REQ-{key}'
        record = {**properties, "id": req_id}
        if key.parent:
            record["parent"] = str(key.parent)
        records.append(record)
    return records


if __name__ == "__main__":
    requirements = parse_requirements_flat(fileobj=sys.stdin)
    yaml.dump(requirements, sys.stdout)
