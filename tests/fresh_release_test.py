import os
import shutil
import tempfile
import subprocess


def test_building_fresh_release():
    # TODO: update the make file + this test to exercise `rdm collect`
    init_directory = os.path.join(tempfile.gettempdir(), 'rdm_test_building_fresh_release')
    try:
        subprocess.check_call(['rdm', 'init', '--output', init_directory])
        print("BEFORE")
        subprocess.check_call(['ls', '-laR', init_directory])
        generated_document = os.path.join(init_directory, 'release/software_plan.md')
        subprocess.check_call(['make', 'clean'], cwd=init_directory)
        assert not os.path.isfile(generated_document)
        subprocess.check_call(['make'], cwd=init_directory)
        print("AFTER")
        subprocess.check_call(['ls', '-laR', init_directory])
        assert os.path.isfile(generated_document)
    finally:
        shutil.rmtree(init_directory, ignore_errors=True)
