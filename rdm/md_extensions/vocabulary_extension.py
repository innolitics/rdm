import re

from rdm.md_extensions.base import RdmExtension


def present_in(values, text):
    return [value for value in values if value in text]


class VocabularyExtension(RdmExtension):

    def __init__(self, environment):
        super().__init__(environment)
        environment.filters['present_in'] = present_in

    def on_start_of_parsing(self):
        first_pass_output = self.environment.globals['first_pass_output']
        first_pass_output.words = extract_words(first_pass_output.lines)
        first_pass_output.words_ignore_case = extract_words_ignore_case(first_pass_output.lines)
        first_pass_output.has = _has.__get__(first_pass_output)
        first_pass_output.has_ignore_case = _has_ignore_case.__get__(first_pass_output)


def extract_words(lines):
    words = set()
    pattern = r"[a-zA-Z0-9_]+"
    for line in lines:
        for word in re.findall(pattern, line):
            words.add(word)
    return words


def extract_words_ignore_case(lines):
    words = set()
    pattern = r"[a-zA-Z0-9_]+"
    for line in lines:
        for word in re.findall(pattern, line):
            words.add(word.lower())
    return words


def _has(self, word):
    return word in self.words


def _has_ignore_case(self, word):
    return word.lower() in self.words_ignore_case
