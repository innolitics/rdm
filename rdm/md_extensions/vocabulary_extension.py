import re

from rdm.md_extensions.rdm_extension import RdmExtension


class VocabularyExtension(RdmExtension):
    tags = set(['vocabulary'])

    def process_block_args(self, *args):
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
