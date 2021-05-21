from rdm.md_extensions.base import RdmExtension


class AuditNoteExclusionExtension(RdmExtension):
    def post_process_filter(self, generator):
        for source in generator:
            yield audit_preprocess(source)


def audit_preprocess(source):
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
