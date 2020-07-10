from rdm.md_extensions.base import RdmExtension


def section_number_filter(generator):
    section_list = []
    for line in generator:
        section_depth = section_number_depth(line)
        if section_depth == 0:
            yield line
        else:
            if section_depth > len(section_list):
                while section_depth > len(section_list):
                    section_list.append(1)
            else:
                while section_depth < len(section_list):
                    section_list.pop()
                section_list[section_depth - 1] += 1
            formatted_section_number = '.'.join([
                str(section_number) for section_number in section_list])
            yield line[0:section_depth] + ' ' + formatted_section_number + line[section_depth:]


def section_number_depth(line):
    for index in range(len(line)):
        if line[index] != '#':
            return index
    return len(line)


class SectionNumberExtension(RdmExtension):

    def post_process_filter(self, generator):
        yield from section_number_filter(generator)
