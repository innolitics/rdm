import pytest

from rdm.image_extractor import extract_image_urls, unique_image_name_from_url


def test_extract_image_urls_empty_text():
    expected = []
    actual = extract_image_urls("")
    assert actual == expected


def test_extract_image_urls_one_image_text():
    text = '''
    Looks like a black widow spider to me.
![black_widow](https://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG)
    '''
    expected = ['https://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG']
    actual = extract_image_urls(text)
    assert actual == expected


def test_unique_image_name_from_url():
    url = 'https://user-images.githubusercontent.com/890550/91199174-bbf62e00-e6ba-11ea-9d5c-9d1d6b7bcd39.JPG'
    expected_name = 'httpsuserimagesgithubusercontentcom89055091199174bbf62e00e6ba11ea9d5c9d1d6b7bcd39.JPG'
    actual = unique_image_name_from_url(url)
    assert actual == expected_name
