'''
Functions that parse the given project management service and produce
`requirements.yml` and `problem_reports.yml` files.  The selected project
management backend is specified in the project configuration file.
'''
import os
from getpass import getpass

from github import Github
import yaml

REPOSITORY = 'innolitics/freesurfer'
requirements_path = './requirements.yml'
problem_reports_path = './problem_reports.yml'

def get_requirements_from_github():
    gh_api_token = os.getenv('GH_API_TOKEN', None)
    if gh_api_token:
        print('Using API token stored in GH_API_TOKEN.')
        g = Github(gh_api_token)
    else:
        print('No access token is stored in the GH_API_TOKEN environment variable.')
        print('Defaulting to username / password for login.')
        username = input('GitHub username: ')
        password = getpass('GitHub password (will not echo to console): ')
        g = Github(username, password)
    repository = g.get_repo(REPOSITORY)
    requirements = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                    for issue in repository.get_issues()
                    if 'requirement' in issue.labels}
    print(f'Found {len(requirements)} requirement(s)')
    problem_reports = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                       for issue in repository.get_issues()
                       if 'problem-report' in issue.labels}
    print(f'Found {len(problem_reports)} problem report(s)')
    with open(requirements_path, 'w') as f:
        yaml.dump(requirements, f, default_flow_style=False)
    with open(problem_reports_path, 'w') as f:
        yaml.dump(problem_reports, f, default_flow_style=False)

if __name__ == '__main__':
    get_requirements_from_github()
