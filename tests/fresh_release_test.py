import os
import shutil
import subprocess

import pytest


@pytest.fixture
def init_tmpdir(tmpdir):
    '''
    The rdm init command assumes the directory doesn't exist yet (since it
    doesn't want to overwrite existing files).  This fixture provides a path to
    a tmp directory that isn't created yet; it also deletes the directory after
    the test.
    '''
    subprocess.check_call(['git', 'init'], cwd=str(tmpdir))
    yield os.path.join(str(tmpdir), 'regulatory')
    shutil.rmtree(str(tmpdir), ignore_errors=True)


def test_building_fresh_release(init_tmpdir):
    subprocess.check_call(['rdm', 'init', '--output', init_tmpdir])
    subprocess.check_call(['make'], cwd=init_tmpdir)
    release_dir = os.path.join(init_tmpdir, 'release')
    all_release_filenames = os.listdir(release_dir)
    release_md_paths = [os.path.join(release_dir, f) for f in all_release_filenames if f.endswith('.md')]
    subprocess.check_call(['rdm', 'gap', '62304_2015_class_b'] + release_md_paths)


def test_doctor_fresh_release(init_tmpdir):
    subprocess.check_call(['rdm', 'init', '--output', init_tmpdir])
    subprocess.check_call(['rdm', 'doctor'], cwd=os.path.dirname(init_tmpdir))
