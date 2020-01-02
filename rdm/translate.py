from rdm.util import write_yaml
from rdm.test_formatters.xml_util import (
    flattened_gtest_results,
    xml_load,
    flattened_qttest_results,
    auto_translator,
)

XML_TRANSLATORS = {
    'auto': auto_translator,
    'gtest': flattened_gtest_results,
    'qttest': flattened_qttest_results,
    'xunit': flattened_gtest_results,  # this flattener also handles xunit.
}
XML_FORMATS = [format for format in XML_TRANSLATORS.keys()]


def translate_test_results(format, input, output):
    xml_translator = XML_TRANSLATORS.get(format)
    if xml_translator:
        xml_parsed_test_results = xml_load(input)
        translated_test_results = xml_translator(xml_parsed_test_results)
        with open(output, 'w') as out_file:
            write_yaml(translated_test_results, out_file)
    else:
        raise ValueError("Unknown translation format: " + format)


def translate_gtest(input):
    return flattened_gtest_results(xml_load(input))


def translate_qttest(input):
    return flattened_qttest_results(xml_load(input))
