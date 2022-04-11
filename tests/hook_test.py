import logging
import os
import pytest
import subprocess

from git import Repo


@pytest.fixture
def tmp_repo(tmpdir):
    # initialize new repository and change working directory
    directory = str(tmpdir)
    repo = Repo.init(directory)
    os.chdir(directory)

    # set up logging and trace
    logging.basicConfig()
    logging.root.setLevel(logging.INFO)
    type(repo.git).GIT_PYTHON_TRACE = 'full'

    # create initial commit
    file_path = os.path.join(directory, 'initial-commit.txt')
    subprocess.check_call(['touch', file_path])
    repo.git.add('--all')
    subprocess.check_call(['git', 'config', 'user.email', 'test@innolitics.com'])
    subprocess.check_call(['git', 'config', 'user.name', 'Tester Bot'])
    repo.git.commit('-m', '\'message\'', '--no-verify')

    subprocess.check_call(['rdm', 'hooks'])

    yield repo

    subprocess.check_call(['rm', '-rf', directory])


@pytest.fixture
def tmp_editor(tmpdir):
    # create EDITOR executable and set environment variable
    editor_path = os.path.join(str(tmpdir), 'tmp_editor.sh')
    with open(editor_path, 'w') as f:
        f.write('#!/bin/bash\necho hello >> $1\n')
    subprocess.check_call(['chmod', '+x', editor_path])
    old_editor = os.environ.get('GIT_EDITOR', None)
    os.environ["GIT_EDITOR"] = editor_path

    yield

    if old_editor is None:
        del os.environ["GIT_EDITOR"]
    else:
        os.environ["GIT_EDITOR"] = old_editor


def prepare_branch(tmp_repo, branch_name):
    directory = os.getcwd()

    tmp_repo.git.checkout('-b', branch_name)

    file_path = os.path.join(directory, 'empty-file.txt')
    subprocess.check_call(['touch', file_path])

    tmp_repo.git.add('--all')


def show_commit_message():
    return str(subprocess.check_output(
        ['git', 'show', '-s', '--format=%B'],
    ), 'utf-8')


def test_single_issue(tmp_repo):
    prepare_branch(tmp_repo, '10-sample-issue')
    tmp_repo.git.commit('-m', 'Fix some issue')
    assert show_commit_message() == "Fix some issue\n\nIssue #10\n\n"


def test_multiple_issues(tmp_repo):
    prepare_branch(tmp_repo, '10-11-sample-issue')
    tmp_repo.git.commit('-m', 'Fix some issue')
    assert show_commit_message() == "Fix some issue\n\nIssue #10\n\nIssue #11\n\n"


def test_mixed_non_issue_numbers(tmp_repo):
    prepare_branch(tmp_repo, '42-85-implement-base-64-on-aws-s3')
    tmp_repo.git.commit('-m', 'Fix some issue')
    assert show_commit_message() == "Fix some issue\n\nIssue #42\n\nIssue #85\n\n"


def test_no_issue_number(tmp_repo):
    with pytest.raises(Exception) as Error:
        prepare_branch(tmp_repo, 'sample-issue')
        tmp_repo.git.commit('-m', 'Fix some issue')

    assert "Aborting commit" in str(Error.value)


def test_default_commit(tmp_editor, tmp_repo):
    prepare_branch(tmp_repo, '10-sample-issue')
    tmp_repo.git.commit()
    assert show_commit_message() == "Issue #10\nhello\n\n"
