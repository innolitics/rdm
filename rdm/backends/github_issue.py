'''
A GitHub backend where change requests are stored as GitHub Issues.
'''
import os
import pickle
from collections import defaultdict, OrderedDict

from rdm.backends.github_base import authenticate_github, extract_issue_numbers_from_commit_message
from rdm.util import remove_carriage_return, print_info, print_warning

# TODO: the code in this module is somewhat dirty; the naming + formatting
# could use some work. It is unclear what a good way to test this would be ...
# maybe we should create a public repo to test against?  Its not clear...


def pull(system, cache_dir):
    github_browser = authenticate_github()
    github_repository = github_browser.get_repo(system['repository'])

    # TODO: only grab issues for the current release
    if cache_dir:
        # TODO: figure out how to get this caching to work, or decide it is not
        # worth the effort and remove it; the goal of the cacheing is to avoid
        # needing to hit the github API each time you test the script; it is
        # primarily useful for a dev working on this backend module. I think
        # that pickling and unpickling pygithub objects results in the lazily
        # loaded attributes always returning None.
        raise NotImplementedError()
        os.makedirs(cache_dir, exist_ok=True)
        pull_requests = _pull_cached(
            lambda: _pull_pull_requests(github_repository),
            os.path.join(cache_dir, 'github_pull_requests.pickle'),
            'pull requests',
        )
        issues = _pull_cached(
            lambda: _pull_issues(github_repository),
            os.path.join(cache_dir, 'github_issues.pickle'),
            'issues',
        )
    else:
        pull_requests = _pull_pull_requests(github_repository)
        issues = _pull_issues(github_repository)
    return _format_development_history(issues, pull_requests)


def _pull_cached(get_data, filename, label):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        print_info('Loaded {} cached {} from {}'.format(len(data), label, filename))
    except Exception:
        print_info('Unable to load cached {} from {}'.format(label, filename))
        data = get_data()
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
        print_info('Saved {} cached {} to {}'.format(len(data), label, filename))
    return data


def _pull_pull_requests(github_repository):
    pull_requests = list(github_repository.get_pulls(state='closed'))
    print_info('Pulled {} pull requests from {}'.format(len(pull_requests), github_repository.url))
    return pull_requests


def _pull_issues(github_repository):
    issues = list(github_repository.get_issues(state='all'))
    for i in issues:
        [l.name for l in i.labels]

    print_info('Pulled {} issues from {}'.format(len(issues), github_repository.url))
    return issues


def _format_development_history(issues, pull_requests):
    changes = [build_change(pr) for pr in pull_requests if _is_change(pr)]
    change_requests = [build_change_request(i) for i in issues if _is_change_request(i)]
    attach_changes(changes, change_requests)
    return {'changes': changes, 'change_requests': change_requests}


def _is_change(pull_request):
    is_merged = pull_request.merged and pull_request.base.ref == 'master'
    is_obsolete = _is_obsolete(pull_request.labels)
    return is_merged and not is_obsolete


def _is_problem_report(labels):
    return 'bug' in [l.name for l in labels]


def _is_obsolete(labels):
    return 'obsolete' in [l.name for l in labels]


def _is_change_request(issue):
    # Oddly, the Github API considers "Pull Requests" to be "Issues".  We prune
    # out pull-request-issues as well.
    pull_request_issue = issue.pull_request is not None

    # Ignore issues marked as obsolete
    obsolete = _is_obsolete(issue.labels)

    # All problem reports are included, regardless of whether they are closed
    # or not; open problem reports are called "known anomalies"
    problem_report = _is_problem_report(issue.labels)

    # We only consider closed change requests; it is assumed that the project
    # management tool will be used to ensure that all of the change requests
    # that should be completed for the release actually are completed; we don't
    # want to show change reqests for future releases.
    closed_change_request = issue.state == 'closed'

    return not pull_request_issue and not obsolete and (
        problem_report or closed_change_request)


def build_change_request(issue):
    # TODO: in all places where we use issue.body and pull_request.body,
    # replace @-mentions with the people's names.
    # TODO: consider adding an explicity "approved_by" field, if there is a way
    # to derive this...
    # TODO: figure out how to connect to parent change requests
    return OrderedDict([
        ('id', str(issue.number)),
        ('title', issue.title),
        ('content', remove_carriage_return(issue.body)),
        ('change_ids', []),
        ('is_problem_report', _is_problem_report(issue.labels)),
        ('url', issue.html_url),
    ])


def build_change(pull_request):
    commits = pull_request.get_commits()
    approvals = change_approvals(pull_request)
    authors = change_authors(pull_request, commits)

    if authors[0] in approvals:
        msg = 'Primary author {} is also a reviewer for pull request {}'
        print_warning(msg.format(authors[0], pull_request.html_url))

    return OrderedDict([
        ('id', str(pull_request.number)),
        ('content', change_body(pull_request.body)),
        ('approvals', approvals),
        ('authors', authors),
        ('change_requests', extract_change_requests(pull_request, commits)),
        ('url', pull_request.html_url),
    ])


def change_authors(pull_request, commits):
    '''
    Changes may have multiple authors in some cases, if multiple people created
    commits.  We order the authors according to the number of commits they
    created.

    Sometimes there is not a github user associated with a commit; in these
    cases, we fall back to the PR author.
    '''
    commits_per_author = defaultdict(lambda: 0)
    authors = {}
    num_commits_with_no_author = 0
    for commit in commits:
        if commit.author:
            author = build_person(commit.author)
            commits_per_author[author['id']] += 1
            authors[author['id']] = author
        else:
            num_commits_with_no_author += 1
    if num_commits_with_no_author > 0:
        msg = '{} commits had no author in {}'
        print_warning(msg.format(num_commits_with_no_author, pull_request.html_url))
    author_commits = list(commits_per_author.items())
    sorted_author_commits = sorted(author_commits, key=lambda ac: ac[1], reverse=True)
    authors = [authors[aid] for (aid, c) in sorted_author_commits]

    if len(authors) > 0:
        return authors
    else:
        msg = 'No commits have an author for {}, using pull request author instead'
        print_warning(msg.format(pull_request.html_url))
        return [build_person(pull_request.user)]


def change_approvals(pull_request):
    '''
    Sometimes it makes sense to have third-parties who may not have access to
    GitHub perform reviews.  When this occurs, the pull request is tagged with
    the `external-review` label.  It is assumed that the person doing the
    review is mentioned in the body of the review.  In this case, their may be
    no explicit approvals, but also no warnings will be logged.

    If there are no github review with the "approval" status, then we fall back to using
    github reviews with the "comment" status.
    '''
    external_review = 'external-review' in [l.name for l in pull_request.labels]

    if external_review:
        return []

    github_reviews = [r for r in pull_request.get_reviews()]
    approvals = [build_approval(r) for r in github_reviews if r.state == 'APPROVED']

    if approvals:
        return approvals

    # Responses to review comments (oddly) show up in github as reviews; we
    # apply some extra filtering here to attempt to remove these.
    github_comments = [r for r in github_reviews
                       if r.state == 'COMMENTED' and r.user != pull_request.user]

    if github_comments:
        msg = 'No "approved" github reviews for pull request {}, using last "comment" instead'
        print_warning(msg.format(pull_request.html_url))
        return [build_approval(github_comments[-1])]
    else:
        msg = 'No reviews for pull request {}'
        print_warning(msg.format(pull_request.html_url))
        return []


def build_approval(github_review):
    return OrderedDict([
        ('id', str(github_review.id)),
        ('reviewer', build_person(github_review.user)),
        ('content', remove_carriage_return(github_review.body)),
        ('url', github_review.html_url),
    ])


def change_body(body):
    cleaned = remove_carriage_return(body)
    lines = cleaned.split('\n')

    # Prune out lines that just display the issue number, since the association
    # to an issue is displayed already within the documents, and thus showing
    # it again in the body would be superfluous
    return '\n'.join(l for l in lines if not l.startswith('Issue #')).strip()


def extract_change_requests(pull_request, commits):
    '''
    Deduce which change request a given "change" (i.e., pull request) applies
    to. Look through the commits in each pull request, and keep track of all of
    the issues that these commits reference.
    '''
    change_requests = set()
    for commit in commits:
        commit_issue_numbers = extract_issue_numbers_from_commit_message(commit.commit.message)
        change_requests.update(commit_issue_numbers)
    body_issue_numbers = extract_issue_numbers_from_commit_message(pull_request.body)
    change_requests.update(body_issue_numbers)
    if len(change_requests) == 0:
        branch_name = pull_request.head.ref
        msg = 'Unable to associate pull request (branch {}) with a change request; {}'
        print_warning(msg.format(branch_name, pull_request.html_url))
    return list(change_requests)


def build_person(user):
    check_user(user)
    return OrderedDict([
        ('name', user.name or user.login),
        ('id', str(user.id)),
    ])


# We assume the script is run once, and then the process closes.  Thus, the
# module-level state is ok.
seen_users = set()


def check_user(user):
    if user.login not in seen_users:
        seen_users.add(user.login)
        if user.name is None:
            msg = 'GitHub User {} {} does not have a name'
            print_warning(msg.format(user.id, user.login))


def attach_changes(changes, change_requests):
    '''
    We want to store the connection between change requests and changes with
    the change requests, because when we generate the templates, we display
    each change, and within it, we display each change request.

    But, in GitHub, the connection is stored with the changes.

    This function mutates the changes and change requests, moving the
    connection from the former to the latter.
    '''
    change_request_id_to_changes = defaultdict(lambda: [])
    for change in changes:
        for change_request_id in change['change_requests']:
            change_request_id_to_changes[change_request_id].append(change['id'])
        del change['change_requests']
    for change_request in change_requests:
        if change_request['id'] in change_request_id_to_changes:
            change_request['change_ids'] = change_request_id_to_changes[change_request['id']]
        elif not change_request['is_problem_report']:
            msg = 'No changes implemented for change request {}'
            print_warning(msg.format(change_request['url']))
