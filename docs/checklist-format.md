# RDM's Audit Checklist Format

You can create your own audit checklists. Te checklists are read
line by line using a very simple format:

1. Leading whitespace is ignored.
2. Blank lines are ignored.
3. If the first character is a '#' then the line is a comment and is ignored.
4. If the first word is 'include' then the text until the end of the line
   specifies another checklist to be included, verbatim, in place of the
   current line (like an `#include` directive in C).
5. If an include file name matches a builtin checklist, then that builtin is
   used (For example `include 14971_2007`).
6. If the file name does not match a built in checklist then it is treated as a
   file reference relative to the current checklist location (For example
   `include ./my_special_checklist.txt`).
7. Except for comments and includes, the first word is treated as an expected keyword.
8. The keyword includes all text up to either a space character or the end of the line.
9. The descriptive text following a keyword is included in the output report
   whenever the keyword is missing.
