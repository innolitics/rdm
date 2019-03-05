'''
A backend where change requests are stored as GitHub Pull Requests.
'''
from rdm.backends.github_base import authenticate_github


def pull(system):
    github_browser = authenticate_github()
    github_repository = github_browser.get_repo(system['repository'])
    # TODO: implement code that grabs
    # 1. change requests
    # 2. problem reports
    # 3. known anomalies
    return [], [], []
