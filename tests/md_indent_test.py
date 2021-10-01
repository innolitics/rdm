def test_md_indent_basic():
    input_markdown= "\n".join(["Line 1", "# Line 2", "## Line 3"])
    expected_output_markdown= "\n".join(["Line 1", "Line 2", "# Line 3"])
    assert md_indent(input_markdown,-1) == expected_output_markdown


def test_md_indent_extra_trim():
    input_markdown= "\n".join(["Line 1", "# Line 2", "## Line 3", "### Line 4"])
    expected_output_markdown= "\n".join(["Line 1", "Line 2", "Line 3", "# Line 4"])
    assert md_indent(input_markdown,-2) == expected_output_markdown


def test_md_indent_codeblock():
    input_markdown = "\n".join(["## Hello", "```","## Hello","```"])
    expected_output_markdown= "\n".join(["# Hello", "```", "## Hello","```"])
    assert md_indent(input_markdown, -1) == expected_output_markdown


def test_md_indent_basic_add():
    input_markdown= "\n".join(["Line 1", "# Line 2", "## Line 3"])
    expected_output_markdown= "\n".join(["Line 1", "## Line 2", "### Line 3"])
    assert md_indent(input_markdown,1) == expected_output_markdown


def test_md_indent_add_codeblock():
    input_markdown = "\n".join(["## Hello", "```","## Hello","```"])
    expected_output_markdown= "\n".join(["### Hello", "```", "## Hello","```"])
    assert md_indent(input_markdown, 1) == expected_output_markdown