import re


def extract_image_urls(text):
    return [url for url, _ in extract_image_urls_and_alt_text(text)]

def extract_image_urls_and_alt_text(text):
    # returns list of (url, alt_text)
    pattern = re.compile(r'(?:!\[(.*?)\]\((.*?)\))')
    return [(match.group(2), match.group(1)) for match in pattern.finditer(text)]


def unique_image_name_from_url(url_text):
    parts = url_text.split('.')
    if len(parts) > 1:
        base = "".join(parts[:-1])
        ext = "." + parts[-1]
    else:
        base = "".join(parts)
        ext = ""
    return "".join(x for x in base if x.isalnum()) + ext


def extract_image_urls_from_content(source):
    result = []
    for item in source:
        content = item.get('content', '')
        result += extract_image_urls(content)
    return result
