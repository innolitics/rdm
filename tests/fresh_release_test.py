import os
import shutil
import tempfile
import subprocess


def test_building_fresh_release():
    init_directory = os.path.join(tempfile.gettempdir(), 'rdm_test_building_fresh_release')
    try:
        subprocess.check_call(['rdm', 'init', init_directory])
        subprocess.check_call(['ls', '-la', init_directory])
        subprocess.check_call(['make'], cwd=init_directory)
    finally:
        shutil.rmtree(init_directory, ignore_errors=True)
