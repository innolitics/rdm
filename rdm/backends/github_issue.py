'''
A GitHub backend where change requests are stored as GitHub Issues.
'''
import re
from collections import defaultdict

from rdm.backends.github_base import authenticate_github
from rdm.util import remove_carriage_return, print_info, print_warning


def pull(system):
    github_browser = authenticate_github()
    github_repository = github_browser.get_repo(system['repository'])
    return _pull_from_repository(github_repository)


def _pull_from_repository(github_repository):
    # TODO: only grab issues for the current release
    issues = [i for i in github_repository.get_issues(state='all') if _is_issue(i)]

    print_info('Pulled {} issues from {}'.format(len(issues), github_repository.url))
    for i in issues:
        check_issue(i)

    problem_reports = [build_problem_report(i) for i in issues if _is_problem_report(i)]
    change_requests = [build_change_request(i) for i in issues if _is_change_request(i)]

    changes = [build_change(pr) for pr in github_repository.get_pulls(state='closed') if _is_change(pr)]
    attach_changes(changes, change_requests)
    return problem_reports, change_requests


def _is_issue(issue):
    '''
    Prune out obsolete issues.

    Oddly, the Github API considers "Pull Requests" to be "Issues".  We prune
    out pull-request-issues as well.
    '''
    labels = [l.name for l in issue.labels]
    return 'obsolete' not in labels and issue.pull_request is None


def _is_change(pull_request):
    return pull_request.merged and pull_request.base.ref == 'master'


def check_issue(issue):
    labels = [l.name for l in issue.labels]
    if 'wontfix' in labels and 'bug' not in labels:
        msg = 'GitHub Issue {} has the "wontfix" label without "bug" label.'
        print_warning(msg.format(issue.number))


def _is_problem_report(issue):
    labels = [l.name for l in issue.labels]
    # An issue labeled wontfix should also be labeled "bug", but to be nice we
    # assume if it is labeled "wontfix" they meant for it to be a "bug" too
    return 'bug' in labels or 'wontfix' in labels


def _is_change_request(issue):
    return not _is_problem_report(issue)


def build_change_request(issue):
    return {
        'id': str(issue.number),
        'title': issue.title,
        'content': remove_carriage_return(issue.body),
        'changes': [],
        'state': change_request_state(issue),
    }


def change_request_state(issue):
    if issue.state == 'open':
        return 'open'
    elif issue.state == 'closed':
        return 'completed'
    else:
        raise ValueError('Unknown GitHub issue state {}'.format(issue.state))


def build_problem_report(issue):
    return {
        'id': str(issue.number),
        'title': issue.title,
        'content': remove_carriage_return(issue.body),
        'state': problem_report_state(issue),
    }


def problem_report_state(issue):
    labels = [l.name for l in issue.labels]
    if issue.state == 'closed':
        return 'resolved'
    elif issue.state == 'open' and 'wontfix' in labels:
        return 'wontfix'
    elif issue.state == 'open':
        return 'open'
    else:
        raise ValueError('Unknown GitHub issue state {}'.format(issue.state))


def build_change(pull_request):
    approvals = [r for r in pull_request.get_reviews() if r.state == 'APPROVED']
    if len(approvals) == 0:
        msg = 'No approved reviews for pull request {}'
        print_warning(msg.format(pull_request.number))
        approval = None
    elif len(approvals) > 1:
        msg = 'Multiple approved reviews for pull request {}; using first one'
        # TODO: support multiple reviews (e.g., by concatenating reviewer names or something)
        print_warning(msg.format(pull_request.number))
        approval = approvals[0]
    else:
        approval = approvals[0]

    return {
        'id': str(pull_request.number),
        'content': remove_carriage_return(pull_request.body),
        'verified_by': approval and approval.user.name,
        'verified_on': approval and approval.submitted_at,
        'change_request_id': extract_change_request_id(pull_request),
    }


def extract_change_request_id(pull_request):
    '''
    Deduce which change request a given "change" (i.e., pull request) applies
    to.  For now, we assume a "change" applies to just one change request.  We
    also assume that the branch name contains a number indicating the name.
    '''
    branch_name = pull_request.head.ref
    numbers_in_branch = [n for n in re.findall(r'\d+', branch_name)]
    if len(numbers_in_branch) == 0:
        msg = 'Unable to associate pull request {} ({}) with a change request'
        print_warning(msg.format(pull_request.number, branch_name))
        return None
    elif len(numbers_in_branch) > 1:
        msg = 'Multiple numbers in pull request {} ({}); using first one'
        # TODO: support associating a "change" with multiple "change requests"
        print_warning(msg.format(pull_request.number, branch_name))
        return numbers_in_branch[0]
    else:
        return numbers_in_branch[0]


def attach_changes(changes, change_requests):
    change_request_id_to_changes = defaultdict(lambda: [])
    for change in changes:
        change_request_id = change['change_request_id']
        if change_request_id is not None:
            del change['change_request_id']
            change_request_id_to_changes[change_request_id].append(change)
    for change_request in change_requests:
        if change_request['id'] in change_request_id_to_changes:
            change_request['changes'] = change_request_id_to_changes[change_request['id']]
