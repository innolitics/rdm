from rdm.util import write_yaml
from rdm.xml_util import flattened_gtest_results, xml_load, flattened_qttest_results


def translate_test_results(format, input, output):
    print('format', format)
    print('input', input)
    print('output', output)
    if format == 'gtest':
        test_results = translate_gtest(input)
    elif format == 'qttest':
        test_results = translate_qttest(input)
    else:
        raise ValueError("Unknown translation format: " + format)
    with open(output, 'w') as out_file:
        write_yaml(test_results, out_file)


def translate_gtest(input):
    return flattened_gtest_results(xml_load(input))


def translate_qttest(input):
    return flattened_qttest_results(xml_load(input))
