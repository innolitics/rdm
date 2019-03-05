from copy import deepcopy
from datetime import datetime
from collections import namedtuple

from rdm.backends.github_issue import _pull_from_repository


MockGithubIssue = namedtuple('MockGithubIssue', [
    'number', 'title', 'body', 'labels', 'created_at',
])


MockGithubPullRequest = namedtuple('MockGithubPullRequest', [
    'number', 'title', 'body', 'labels', 'created_at',
])


MockGithubLabel = namedtuple('MockGithubLabel', ['name'])


class MockGithubRepository:
    def __init__(self, issues, pulls):
        self.issues = issues
        self.url = 'https://github.com/mock/repository'

    def get_issues(self, state):
        return deepcopy(self.issues)

    def get_pulls(self, state):
        return deepcopy(self.issues)


def test_github_pull_no_issues():
    github_repository = MockGithubRepository([], [])
    problem_reports, change_requests, known_anomalies = _pull_from_repository(github_repository)
    assert problem_reports == []
    assert change_requests == []
    assert known_anomalies == []


def test_github_pull_few_issues():
    github_repository = MockGithubRepository([
        MockGithubIssue(1, 'title1', 'body1', [], datetime(2020, 1, 1)),
        MockGithubIssue(2, 'title2', 'body2', [MockGithubLabel('wontfix')], datetime(2020, 1, 2)),
    ], [])
    _, _, known_anomalies = _pull_from_repository(github_repository)
    assert known_anomalies == [{
        'id': '2',
        'title': 'title2',
        'description': 'body2',
        'created_on': datetime(2020, 1, 2),
    }]
