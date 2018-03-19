import tempfile
import subprocess


def test_building_fresh_release():
    init_directory = tempfile.mkdtemp()
    subprocess.check_call(['rdm', 'init', init_directory])
    subprocess.check_call(['make'], cwd=init_directory)
