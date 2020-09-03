import os
import re
import shutil
import zlib
from os.path import join

import requests

from rdm.util import path_finder, all_files_in_folder

markdown_image_pattern = re.compile(r'(?:!\[(.*?)\]\((.*?)\))')
tex_img_pattern = re.compile(r'\\includegraphics{(.*?)}')


class ImageDownloader:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.already_downloaded = set(all_files_in_folder(image_folder))

    def has_image_file(self, name):
        return name in self.already_downloaded

    def add_or_find_image(self, url):
        hashed_name = unique_image_name_from_url(url)
        if self.has_image_file(hashed_name):
            return hashed_name
        else:
            try:
                self.download_image(hashed_name, url)
                self.already_downloaded.add(hashed_name)
                return hashed_name
            except:  # TODO: narrow the catch
                return None

    def download_image(self, hashed_name, url):
        download_file = join(self.image_folder, hashed_name)
        response = requests.get(url)
        with open(download_file, 'wb') as file:
            file.write(response.content)


def extract_image_url_sequence_from_markdown(text):
    # returns start and stop locations of url
    return [(match.start(2), match.end(2)) for match in markdown_image_pattern.finditer(text)]


def unique_image_name_from_url(url_text):
    parts = url_text.split('.')
    if len(parts) > 1:
        ext = "." + parts[-1]
    else:
        ext = ""
    # crc32 is used because it is fast and deterministic.
    # 2**16 item list might have a collision with single 32 bit hash of each item
    # Using both forward and reverse hashes means about 2**32 item list is needed start to see collisions.
    hashed_base = '{0:X}'.format(zlib.crc32(bytes(url_text, 'utf-8'))) + \
                  '{0:X}'.format(zlib.crc32(bytes(url_text[::-1], 'utf-8')))
    return hashed_base + ext


def extract_images_from_tex(text):
    return [match.group(1) for match in tex_img_pattern.finditer(text)]


def extract_image_url_sequence_from_tex(text):
    return [(match.start(1), match.end(1)) for match in tex_img_pattern.finditer(text)]


def image_is_svg(image_name):
    return image_name.lower().endswith('svg')


def copy_image(source, destination):
    destination_directory, _ = os.path.split(destination)
    os.makedirs(destination_directory, exist_ok=True)
    shutil.copyfile(source, destination)

def create_relative_path_filter(input_folder, output_base):
    return file_meta_filter(path_finder(input_folder, output_base))


def create_download_filters(download_to, output_base):
    if download_to is None:
        return []
    else:
        download_path_filter = path_finder(download_to, output_base)
        downloader = ImageDownloader(download_to)

        def download_filter(url):
            download_location = downloader.add_or_find_image(url)
            if download_location:
                return download_path_filter(download_location)
            else:
                return url

        return [http_meta_filter(download_filter)]


def file_meta_filter(file_filter):
    def filter(url):
        if url_is_http(url):
            return url
        else:
            return file_filter(url)

    return filter


def http_meta_filter(http_filter):
    def filter(url):
        if url_is_http(url):
            return http_filter(url)
        else:
            return url

    return filter


def url_is_http(url):
    return url.startswith('http://') or url.startswith('https://')
