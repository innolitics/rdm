from copy import deepcopy
from collections import namedtuple

from rdm.pull import known_anomalies_from_github


MockGithubIssue = namedtuple('MockGithubIssue', ['number', 'title', 'body', 'labels'])


class MockGithubRepository:
    def __init__(self, issues):
        self.issues = [MockGithubIssue(*i) for i in issues]

    def get_issues(self):
        return deepcopy(self.issues)


def test_known_anomalies_from_github_no_issues():
    github_repository = MockGithubRepository([])
    known_anomalies = known_anomalies_from_github(github_repository)
    assert known_anomalies == {}


def test_known_anomalies_from_github_few_issues():
    github_repository = MockGithubRepository([
        (1, 'title1', 'body1', []),
        (2, 'title2', 'body2', ['wontfix'])
    ])
    known_anomalies = known_anomalies_from_github(github_repository)
    assert known_anomalies == {2: {'title': 'title2', 'description': 'body2'}}
