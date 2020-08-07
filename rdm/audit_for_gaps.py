import os


def audit_for_gaps(args):
    full_path_checklist_file = os.path.realpath(args.checklist)
    already_included = {full_path_checklist_file}
    checklist = _read_checklists(_checklist_generator([full_path_checklist_file]), already_included)
    if len(checklist) == 0:
        print("WARNING: no check list items!")
        return
    source_files = _determine_source_files(args)
    if len(source_files) == 0:
        print("WARNING: no source files!")
        return
    failing_checklist_items = list(_find_failing_checklist_items(_source_generator(source_files), checklist))
    if failing_checklist_items:
        _report_failures(failing_checklist_items)
    else:
        _report_success()


def _find_failing_checklist_items(source_generator, checklist):
    checklist_keys = set(_extract_keys_from_checklist(checklist))
    found_keys = set(_find_keys_in_sources(source_generator, checklist_keys))
    missing_keys = checklist_keys.difference(found_keys)
    for item in checklist:
        reference = item.get('reference')
        if reference and reference in missing_keys:
            yield item


def _determine_source_files(args):
    return args.files


def _checklist_generator(checklist_files):
    for checklist_file in checklist_files:
        dir_path = os.path.dirname(os.path.realpath(checklist_file))
        with open(checklist_file) as file:
            yield (file.read(), dir_path)


def _source_generator(source_files):
    for source_file in source_files:
        with open(source_file) as file:
            yield file.read()


def _read_checklists(checklist_sources, already_included):
    raw_checklists = list(_read_raw_checklists(checklist_sources))
    include_files, reduced_checklist = _split_out_include_files(raw_checklists)
    if include_files:
        unread_files = include_files.difference(already_included)
        already_included = already_included.union(include_files)
        return reduced_checklist + list(_read_checklists(_checklist_generator(unread_files), already_included))
    else:
        return reduced_checklist


def _read_raw_checklists(checklist_sources):
    for checklist_text, path in checklist_sources:
        yield from _flat_file_parser(checklist_text, path)


def _flat_file_parser(checklist_text, path):
    for line_text in checklist_text.split('\n'):
        yield from _parsed_line(line_text, path)


def _parsed_line(line_text, path):
    if line_text:
        tokens = line_text.split(' ')
        if tokens:
            key = tokens[0]
            remainder = ' '.join(tokens[1:])
            if not key.startswith('#'):
                if key == 'include':
                    yield {'include': remainder, 'path': path}
                else:
                    yield {'reference': key, 'description': remainder}


def _split_out_include_files(checklist):
    include_files = set()
    reduced_checklist = []
    for item in checklist:
        include_file = item.get('include')
        if include_file:
            path = item.get('path')
            if path:
                include_file = path + '/' + include_file
            include_files.add(include_file)
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
    print(f'# Failed {failure_count} item{plural}:')
    unsorted_failures = []
    for failing_checklist_item in failing_checklists:
        key = failing_checklist_item.get('reference', '')
        description = failing_checklist_item.get('description', '')
        unsorted_failures.append(f'{key} {description}')
    sorted_failures = sorted(unsorted_failures)
    for line in sorted_failures:
        print(line)


def _report_success():
    # Note output conforms to checklist format, so can be used as a checklist itself.
    print("# Success: all checklists passed.")
