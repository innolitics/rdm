import re


class FirstPassOutput:

    def __init__(self, lines=None):
        self._accessed = False
        self.is_second_pass = lines is not None
        if lines is None:
            lines = []
        self._lines = lines
        self._source = None
        self._words = None
        self._words_ignore_case = None

    def __bool__(self):
        return False

    @property
    def second_pass_is_requested(self):
        return not self.is_second_pass and self._accessed

    @property
    def lines(self):
        self._accessed = True
        return self._lines

    @property
    def source(self):
        if self._source is None:
            self._source = '\n'.join(self.lines)
        return self._source

    @property
    def words(self):
        if self._words is None:
            self._words = set()
            pattern = r"[a-zA-Z0-9_]+"
            for line in self.lines:
                for word in re.findall(pattern, line):
                    self._words.add(word)
        return self._words

    @property
    def words_ignore_case(self):
        if self._words_ignore_case is None:
            self._words_ignore_case = set()
            for word in self.words:
                self._words_ignore_case.add(word.lower())
        return self._words_ignore_case

    def has(self, word):
        return word in self.words

    def has_ignore_case(self, word):
        return word in self.words_ignore_case
