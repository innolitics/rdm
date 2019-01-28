from copy import deepcopy
from datetime import datetime
from collections import namedtuple

from rdm.pull import known_anomalies_from_github


MockGithubIssue = namedtuple('MockGithubIssue', ['number', 'title', 'body', 'labels', 'created_at'])


MockGithubLabel = namedtuple('MockGithubLabel', ['name'])


class MockGithubRepository:
    def __init__(self, issues):
        self.issues = issues

    def get_issues(self):
        return deepcopy(self.issues)


def test_known_anomalies_from_github_no_issues():
    github_repository = MockGithubRepository([])
    known_anomalies = known_anomalies_from_github(github_repository)
    assert known_anomalies == []


def test_known_anomalies_from_github_few_issues():
    github_repository = MockGithubRepository([
        MockGithubIssue(1, 'title1', 'body1', [], datetime(2020, 1, 1)),
        MockGithubIssue(2, 'title2', 'body2', [MockGithubLabel('wontfix')], datetime(2020, 1, 2)),
    ])
    known_anomalies = known_anomalies_from_github(github_repository)
    assert known_anomalies == [{
        'id': '2',
        'title': 'title2',
        'description': 'body2',
        'created_on': datetime(2020, 1, 2),
    }]
