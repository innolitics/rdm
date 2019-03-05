import os
import pytest
import subprocess

from git import Repo
from rdm.hooks import install_hooks


@pytest.fixture
def tmp_repo(tmpdir):
    directory = str(tmpdir)
    repo = Repo.init(directory)
    os.chdir(directory)
    yield repo
    subprocess.call(['rm', '-rf', directory])


def test_install_hooks_no_destination(tmp_repo):
    install_hooks(None)


def test_install_hooks_existing_destination(tmp_repo):
    install_hooks('../.git/hooks')


def test_install_hooks_non_existing_destination(tmp_repo):
    install_hooks('hooks')
