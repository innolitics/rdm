'''
A GitHub backend where change requests are stored as GitHub Issues.
'''
from rdm.backends.github_base import authenticate_github
from rdm.util import remove_carriage_return, print_info


def pull(system):
    github_browser = authenticate_github()
    github_repository = github_browser.get_repo(system['repository'])
    return _pull_from_repository(github_repository)

# pull request data
#
# issue

def _pull_from_repository(github_repository):
    # TODO: only grab issues for the current release
    issues = [i for i in github_repository.get_issues(state='all') if not _is_obsolete(i)]

    # get all pull requests that are:
    # 1. merged into master
    # 2. during the release
    # 
    # for each pull request
    # 1. find the associated change requests
    # 2. 
    pull_requests = list(github_repository.get_pulls(state='closed'))
    print_info('Pulled {} issues from {}'.format(len(issues), github_repository.url))
    problem_reports = [clean_issue(i) for i in issues if _is_problem_report(i)]
    change_requests = [clean_issue(i) for i in issues if _is_change_request(i)]
    known_anomalies = [clean_issue(i) for i in issues if _is_known_anomaly(i)]
    return problem_reports, change_requests, known_anomalies


def _is_obsolete(issue):
    labels = [l.name for l in issue.labels]
    return 'obsolete' in labels


def _is_known_anomaly(issue):
    labels = [l.name for l in issue.labels]
    return 'wontfix' in labels


def _is_problem_report(issue):
    labels = [l.name for l in issue.labels]
    return 'bug' in labels and not _is_known_anomaly(issue)


def _is_change_request(issue):
    return not (_is_known_anomaly(issue) or _is_problem_report(issue))


def clean_issue(issue):
    return {
        'id': str(issue.number),
        'title': issue.title,
        'description': remove_carriage_return(issue.body),
        'created_on': issue.created_at,
    }
