import os

import pytest

from rdm.project_management.github import (
    extract_issue_numbers_from_commit_message,
    GitHubIssueBackend,
)


@pytest.fixture(scope='session')
def github_token():
    token = os.environ.get('GH_API_TOKEN', '')
    if not token:
        pytest.skip(
            'GH_API_TOKEN environment variable must be defined to test github backend'
        )
    return token


def test_extract_issue_numbers_from_commit_message():
    assert extract_issue_numbers_from_commit_message('''
        Some brief description w/ a 123

        - Stuff 55
        - Other Things
        - #45

        Issue #23

        Issues #45 #43
    ''') == ['45', '23', '45', '43']


def test_intialise_backend(github_token):
    GitHubIssueBackend({'repository': 'python/exceptiongroups'})


def test_pull(github_token):
    # Using an archived repo to avoid frequent changes in results
    backend = GitHubIssueBackend({'repository': 'python/exceptiongroups'})
    pulls = backend.pull()

    assert sorted(pulls.keys()) == ['change_requests', 'changes']
    assert len(pulls['change_requests']) == 14
    assert len(pulls['changes']) == 14
    assert pulls['change_requests'][0]['id'] == '3'
    assert pulls['change_requests'][1]['id'] == '4'
    assert pulls['change_requests'][2]['id'] == '6'
    assert pulls['change_requests'][12]['id'] == '24'
    assert pulls['change_requests'][13]['id'] == '27'
    assert pulls['changes'][0]['id'] == '5'
    assert pulls['changes'][1]['id'] == '8'
    assert pulls['changes'][2]['id'] == '13'
    assert pulls['changes'][12]['id'] == '30'
    assert pulls['changes'][13]['id'] == '32'
    change_13 = pulls['changes'][13]
    assert sorted(change_13.keys()) == [
        'approvals',
        'authors',
        'content',
        'id',
        'url',
    ]
    assert change_13['approvals'] == []
    assert change_13['content'] == ''
    assert change_13['authors'][0] == {
        'name': 'Irit Katriel',
        'id': '1055913',
    }
