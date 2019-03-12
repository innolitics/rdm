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
    subprocess.check_call(['git', 'init'], cwd=tmpdir)
    yield os.path.join(tmpdir, 'regulatory')
    shutil.rmtree(str(tmpdir), ignore_errors=True)


def test_building_fresh_release(init_tmpdir):
    # TODO: update the make file + this test to exercise `rdm collect`
    subprocess.check_call(['rdm', 'init', '--output', init_tmpdir])
    print("BEFORE")
    subprocess.check_call(['ls', '-laR', init_tmpdir])
    generated_document = os.path.join(init_tmpdir, 'release/software_plan.md')
    subprocess.check_call(['make', 'clean'], cwd=init_tmpdir)
    assert not os.path.isfile(generated_document)
    subprocess.check_call(['make'], cwd=init_tmpdir)
    print("AFTER")
    subprocess.check_call(['ls', '-laR', init_tmpdir])
    assert os.path.isfile(generated_document)


def test_doctor_fresh_release(init_tmpdir):
    subprocess.check_call(['rdm', 'init', '--output', init_tmpdir])
    subprocess.check_call(['rdm', 'doctor'], cwd=os.path.dirname(init_tmpdir))
