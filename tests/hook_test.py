import logging
import os
import pytest
import subprocess

from git import Repo


@pytest.fixture
def tmp_repo(tmpdir):
    # initialize new repository and change working directory
    repo = Repo.init(tmpdir)
    os.chdir(tmpdir)

    # set up logging and trace
    logging.basicConfig()
    logging.root.setLevel(logging.INFO)
    type(repo.git).GIT_PYTHON_TRACE = 'full'

    # create initial commit
    file_path = os.path.join(tmpdir, 'initial-commit.txt')
    subprocess.call(['touch', file_path])
    repo.git.add('--all')
    repo.git.commit('-m', '\'message\'', '--no-verify')

    subprocess.call(['rdm', 'hooks', tmpdir + '/.git/hooks'])

    yield repo

    # teardown
    subprocess.call(['rm', '-rf', tmpdir])


def prepare_branch(tmp_repo, branch_name):
    directory = os.getcwd()

    tmp_repo.git.checkout('-b', branch_name)

    file_path = os.path.join(directory, 'empty-file.txt')
    subprocess.call(['touch', file_path])

    tmp_repo.git.add('--all')
    tmp_repo.git.commit('-m', 'Fix some issue')


def test_single_issue(tmp_repo):
    prepare_branch(tmp_repo, '10-sample-issue')

    assert subprocess.check_output(
        ['git', 'show', '-s', '--format=%B'], encoding='utf-8'
    ) == "Fix some issue\n\nIssue #10\n\n"


def test_multiple_issues(tmp_repo):
    prepare_branch(tmp_repo, '10-11-sample-issue')

    assert subprocess.check_output(
        ['git', 'show', '-s', '--format=%B'], encoding='utf-8'
    ) == "Fix some issue\n\nIssue #10\n\nIssue #11\n\n"


def test_text_before_issue(tmp_repo):
    prepare_branch(tmp_repo, 'fix-10-sample-issue')

    assert subprocess.check_output(
        ['git', 'show', '-s', '--format=%B'], encoding='utf-8'
    ) == "Fix some issue\n\nIssue #10\n\n"


def test_no_issue_number(tmp_repo):
    with pytest.raises(Exception) as Error:
        prepare_branch(tmp_repo, 'sample-issue')

    assert "Aborting commit" in str(Error.value)
