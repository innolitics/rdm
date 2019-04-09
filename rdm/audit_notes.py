from jinja2 import Template
from jinja2.ext import Extension


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
        return segment[:location], segment[location:]
    else:
        return segment, ''


def empty_formatter(spacing, tag, content):
    return ''


def plain_formatter(spacing, tag, content):
    return '{spacing}[{tag}{content}]'.format(spacing=spacing, tag=tag, content=content)


def create_formatter_with_string(format_string):
    def custom_formatter(spacing, tag, content):
        return format_string.format(spacing=spacing, tag=tag, content=content)

    return custom_formatter


def audit_preprocess(source, formatter_dictionary=None, default_formatter=None):
    if formatter_dictionary is None:
        formatter_dictionary = {}
    if default_formatter is None:
        default_formatter = empty_formatter
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


class AuditNoteExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)

        environment.extend(
            audit_note_formatting_dictionary={},
            audit_note_default_formatter=None,
        )

    def preprocess(self, source, name, filename=None):
        return audit_preprocess(
            source,
            self.environment.audit_note_formatting_dictionary,
            self.environment.audit_note_default_formatter)


if __name__ == '__main__':
    tm = Template("hello this is a test [[62340]]\n don't you know", extensions=[AuditNoteExtension])
    message = tm.render()
    print(message)
