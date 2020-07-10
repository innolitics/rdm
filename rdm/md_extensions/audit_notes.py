from rdm.md_extensions.base import RdmExtension
from rdm.util import empty_formatter, create_formatter_with_string, plain_formatter, sans_prefix_formatter


# TODO: use extension config to determine how it acts, vs having two sub extensions
class AuditNoteBaseExtension(RdmExtension):
    tags = set(['audit_notes'])

    def __init__(self, environment):
        super().__init__(environment)
        environment.extend(audit_note_formatting_dictionary=self.audit_note_formatting_dictionary)

    def post_process_filter(self, generator):
        for source in generator:
            yield audit_preprocess(source, self.environment.audit_note_formatting_dictionary)

    def process_block_args(self, *args):
        # Args, if any, are formatter dictionaries.
        for arg in args:
            for format_tag, formatter in arg.items():
                if isinstance(formatter, str):
                    formatter = create_formatter_with_string(formatter)
                self.environment.audit_note_formatting_dictionary[format_tag] = formatter


class AuditNoteExclusionExtension(AuditNoteBaseExtension):
    # Initial formatting dictionary excludes everything.
    # Various prefixes can be made active by defining formats in an 'audit_notes' tagged block
    audit_note_formatting_dictionary = {
        '': empty_formatter,
        'default': empty_formatter,
    }

    def post_process_filter(self, generator):
        for source in generator:
            yield audit_preprocess(source, self.environment.audit_note_formatting_dictionary)


class AuditNoteInclusionExtension(AuditNoteBaseExtension):
    # Initial formatting dictionary includes everything.
    audit_note_formatting_dictionary = {
        '': sans_prefix_formatter,
        'default': plain_formatter,
    }


def audit_preprocess(source, formatter_dictionary=None):
    if formatter_dictionary is None:
        formatter_dictionary = {}
    # The empty formatter removes double bracketed items.
    # This is the default if the extension has been included but no valid tag encountered.
    default_formatter = formatter_dictionary.get('default', empty_formatter)
    primary_segments = source.split('[[')
    if len(primary_segments) > 0:
        result = []
        previous = primary_segments[0]
        for primary_segment in primary_segments[1:]:
            previous, spacing = _find_trailing_space(previous)
            result.append(previous)
            interior, previous = _find_end_marker(primary_segment)
            if previous is None:
                previous = spacing + '[[' + interior
            else:
                tag, content = _find_tag_and_content(interior)
                formatter = formatter_dictionary.get(tag, default_formatter)
                result.append(formatter(spacing, tag, content))
        result.append(previous)
        return ''.join(result)
    else:
        return source


def _find_trailing_space(segment):
    if segment.endswith(' '):
        return segment[:-1], ' '
    else:
        return segment, ''


def _find_end_marker(segment):
    location = segment.find(']]')
    if location >= 0:
        return segment[:location], segment[location + 2:]
    else:
        return segment, None


def _find_tag_and_content(segment):
    location = segment.find(':')
    if location >= 0:
        return segment[:location], segment[location + 1:]
    else:
        return '', segment
