import logging
import os
import pytest
import subprocess

from git import Repo

@pytest.fixture
def tmp_repo(tmpdir):
	repository = Repo.init(tmpdir)

	# set up logging and trace
	logging.basicConfig()
	logging.root.setLevel(logging.INFO)
	type(repository.git).GIT_PYTHON_TRACE='full'

	file_path = os.path.join(tmpdir, 'initial-commit.txt')
	subprocess.call(['touch', file_path])
	repository.git.add('--all')
	repository.git.commit('-m', '\'message\'', '--no-verify')

	subprocess.call(['rdm', 'hooks', tmpdir + '/.git/hooks'])
	
	yield repository, tmpdir

	subprocess.call(['rm', '-rf', tmpdir])

def test_single_issue(tmp_repo):
	repo = tmp_repo[0]
	directory = tmp_repo[1]

	prepare_branch(repo, 'feature/10-sample-issue', directory)

	assert subprocess.check_output(['git', 'show', '-s', '--format=%B'], cwd=directory, encoding='utf-8') == "Fix some issue\n\nIssue #10\n\n"

def prepare_branch(repo, branch_name, directory):
	repo.git.checkout('-b', branch_name)

	file_path = os.path.join(directory, 'empty-file.txt')
	subprocess.call(['touch', file_path])
	
	repo.git.add('--all')
	repo.git.commit('-m', 'Fix some issue')