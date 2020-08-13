import glob
import os


def audit_for_gaps(checklist_file, source_files, list_option):
    if list_option:
        list_default_checklists()
        return 0
    if checklist_file is None:
        print("WARNING: no check list!")
        return 1
    builtins = _builtin_checklist_dictionary()
    full_path_checklist_file = os.path.realpath(_full_file_path(checklist_file, builtins))
    already_included = {full_path_checklist_file}
    checklist = _read_checklists(_checklist_generator([full_path_checklist_file]), already_included, builtins)
    if len(checklist) == 0:
        print("WARNING: no check list items!")
        return 2
    if len(source_files) == 0:
        print("# WARNING: no source files!")
    else:
        print("# Source files:")
        for source_file in source_files:
            print('#     ' + source_file)
    failing_checklist_items = list(_find_failing_checklist_items(_source_generator(source_files), checklist))
    if failing_checklist_items:
        _report_failures(failing_checklist_items)
        return 3
    else:
        _report_success()
        return 0


def _full_file_path(file_name, builtins, path=None):
    file_with_path = path + '/' + file_name if path else file_name
    return builtins.get(file_name, file_with_path)


def list_default_checklists():
    for file_name in _builtin_checklist():
        print(file_name)


def _builtin_checklist():
    return sorted(
        [os.path.splitext(os.path.basename(file_name))[0] for file_name in _builtin_checklist_full_file_name()])


def _builtin_checklist_dictionary():
    return {
        os.path.splitext(os.path.basename(file_name))[0]: file_name
        for file_name in _builtin_checklist_full_file_name()
    }


def _builtin_checklist_full_file_name():
    path = _builtin_checklist_folder() + '/*.txt'
    return [file_name for file_name in glob.glob(path)]


def _builtin_checklist_folder():
    return os.path.dirname(os.path.abspath(__file__)) + '/checklists'


def _builtin_checklist_file(filename):
    return _builtin_checklist_folder() + '/' + os.path.basename(filename)


def _find_failing_checklist_items(source_generator, checklist):
    checklist_keys = set(_extract_keys_from_checklist(checklist))
    found_keys = set(_find_keys_in_sources(source_generator, checklist_keys))
    missing_keys = checklist_keys.difference(found_keys)
    for item in checklist:
        reference = item.get('reference')
        if reference and reference in missing_keys:
            yield item


def _checklist_generator(checklist_files):
    for checklist_file in checklist_files:
        with open(checklist_file) as file:
            dir_path = os.path.dirname(os.path.realpath(checklist_file))
            yield (file.read(), dir_path)


def _source_generator(source_files):
    for source_file in source_files:
        with open(source_file) as file:
            yield file.read()


def _read_checklists(checklist_sources, already_included, builtins):
    raw_checklists = list(_read_raw_checklists(checklist_sources))
    include_files, reduced_checklist = _split_out_include_files(raw_checklists, builtins)
    if include_files:
        unread_files = include_files.difference(already_included)
        already_included = already_included.union(include_files)
        return reduced_checklist + list(
            _read_checklists(_checklist_generator(unread_files), already_included, builtins)
        )
    else:
        return reduced_checklist


def _read_raw_checklists(checklist_sources):
    for checklist_text, path in checklist_sources:
        yield from _flat_file_parser(checklist_text, path)


def _flat_file_parser(checklist_text, path):
    for line_text in checklist_text.split('\n'):
        yield from _parsed_line(line_text.lstrip(), path)


def _parsed_line(line_text, path):
    if line_text:
        tokens = line_text.split(' ')
        key = tokens[0]
        if key:
            remainder = ' '.join(tokens[1:])
            if not key.startswith('#'):
                if key == 'include':
                    yield {'include': remainder, 'path': path}
                else:
                    yield {'reference': key, 'description': remainder}


def _split_out_include_files(checklist, builtins):
    include_files = set()
    reduced_checklist = []
    for item in checklist:
        include_file = item.get('include')
        if include_file:
            path = item.get('path')
            include_files.add(_full_file_path(include_file, builtins, path))
        else:
            reduced_checklist.append(item)
    return include_files, reduced_checklist


def _extract_keys_from_checklist(checklist):
    for item in checklist:
        key = item.get('reference')
        if key:
            yield key


def _find_keys_in_sources(source_generator, checklist_keys):
    for content in source_generator:
        yield from _find_keys_in_content(content, checklist_keys)


def _find_keys_in_content(content, checklist_keys):
    for key in checklist_keys:
        if key in content:
            yield key


def _report_failures(failing_checklists):
    # Note output conforms to checklist format, so can be used as a checklist itself.
    failure_count = len(failing_checklists)
    plural = 's' if failure_count > 1 else ''
    print('# Missing ' + str(failure_count) + ' item' + plural + ':')
    _sort_and_print(failing_checklists)


def _sort_and_print(checklists):
    for line in _sorted_checklist_items(checklists):
        print(line)


def _sorted_checklist_items(unsorted_checklist):
    unsorted_items = []
    for checklist_item in unsorted_checklist:
        key = checklist_item.get('reference', '')
        description = checklist_item.get('description', '')
        unsorted_items.append(key + ' ' + description)
    return sorted(unsorted_items)


def _report_success():
    # Note output conforms to checklist format, so can be used as a checklist itself.
    print("# Success: all checklists passed.")
