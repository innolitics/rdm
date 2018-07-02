import os
import pytest
import subprocess

from git import Repo
from rdm.cli import install_hooks


@pytest.fixture
def tmp_repo(tmpdir):
    repo = Repo.init(tmpdir)
    os.chdir(str(tmpdir))

    yield repo

    # teardown
    subprocess.call(['rm', '-rf', tmpdir])


def test_install_hooks_no_destination(tmp_repo):
    assert install_hooks(None) is None


def test_install_hooks_existing_destination(tmp_repo):
    assert install_hooks('../.git/hooks') is None


def test_install_hooks_non_existing_destination(tmp_repo):
    assert install_hooks('hooks') is None
