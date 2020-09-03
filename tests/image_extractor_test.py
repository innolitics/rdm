from rdm.image_extractor import unique_image_name_from_url, url_is_http, \
    extract_images_from_tex, image_is_svg, extract_image_url_sequence_from_markdown, extract_image_url_sequence_from_tex


def test_extract_image_url_sequence_from_markdown():
    text = 'junk ![black_widow](https://example.com/image.png) other stuff'
    expected = [(20, 49)]
    actual = extract_image_url_sequence_from_markdown(text)
    assert actual == expected


def test_unique_image_name_from_url():
    url = 'https://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG'
    expected_name = '8C61528F3F550CD9.JPG'
    actual = unique_image_name_from_url(url)
    assert actual == expected_name


def test_url_is_http():
    url = 'http://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG'
    urls = 'https://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG'
    file_reference = './foo/bar'
    assert url_is_http(url)
    assert url_is_http(urls)
    assert not url_is_http(file_reference)


def test_extract_images_from_tex():
    text = r'Hmmm \includegraphics{../images/44AEE02FB6E68AC1.JPG} {stuff}huh'
    expected_result = ['../images/44AEE02FB6E68AC1.JPG']
    actual_result = extract_images_from_tex(text)
    assert actual_result == expected_result


def test_extract_image_file_sequence_from_tex():
    text = r'Hmmm \includegraphics{../images/44AEE02FB6E68AC1.JPG} {stuff}huh'
    expected_result = [(22, 52)]
    actual_result = extract_image_url_sequence_from_tex(text)
    assert actual_result == expected_result


def test_extract_image_url_sequence_from_tex():
    text = r'Hmmm \includegraphics{https://example.com/image.png} {stuff}huh'
    expected_result = [(22, 51)]
    actual_result = extract_image_url_sequence_from_tex(text)
    assert actual_result == expected_result


def test_image_is_svg():
    assert image_is_svg('../images/this.svg')
    assert image_is_svg('../images/this.SVG')
    assert not image_is_svg('../images/that.png')
