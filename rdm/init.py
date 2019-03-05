import pkg_resources
import shutil


def init(output_directory):
    init_directory = pkg_resources.resource_filename(__name__, 'init_files')
    shutil.copytree(init_directory, output_directory)
