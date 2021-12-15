#!/usr/bin/env python3
import re
import sys
import urllib.request
import hashlib
import os.path
from urllib.parse import urlparse

import argparse


def download_images_and_sub_urls(line, download_to):
    # TODO: confirm that this works if there are two images on one line
    markdown_linked_image = re.compile(r"!\[.*]\((?P<image_url>.*)\)")
    for match in markdown_linked_image.finditer(line):
        try:
            image_url = urlparse(match.group('image_url'))
            image_url_path = image_url.path
            image_url_scheme = image_url.scheme
        except ValueError:
            print(f"Skipping invalid URL: {match.group('image_url')}", file=sys.stderr)
            continue
        if image_url_scheme not in ["http", "https"]:
            continue
        _, file_extension = os.path.splitext(image_url_path)
        if file_extension == '':
            print(f"Skipping URL with no file extension: {image_url.geturl()}", file=sys.stderr)
            continue

        with urllib.request.urlopn(image_url.geturl()) as f:
            image_data = f.read()
        hasher = hashlib.sha256()
        hasher.update(image_data)
        image_hash = hasher.hexdigest()
        downloaded_image_path = os.path.join(download_to, f"{image_hash}{file_extension}")
        with open(downloaded_image_path, 'wb') as f:
            f.write(image_data)
        print(f'Downloaded {image_url.geturl()} to {downloaded_image_path}', file=sys.stderr)
        line = line[:match.start('image_url')] + downloaded_image_path + line[match.end('image_url'):]
    return line


if __name__ == "__main__":
    description = '''
    Parse markdown from stdin, download any linked images to a designated
    directory, swap out the URL for the local path, and write the updated
    markdown to stdout.  Only images linked with a URL with an http or https
    scheme are included.  The downloaded files retain the extension present in
    the path portion of the URL, but the name is replaced with the sha256 hash
    of their contents.
    '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('download_to', help='path to directory where images will be downloaded')
    args = parser.parse_args()

    for line in sys.stdin.readlines():
        updated_line = download_images_and_sub_urls(line, args.download_to)
        print(updated_line, end='')
