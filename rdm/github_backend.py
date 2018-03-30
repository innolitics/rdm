'''
Functions that parse the given project management service and produce
`requirements.yml` and `problem_reports.yml` files.  The selected project
management backend is specified in the project configuration file.
'''
import os
from getpass import getpass

from github import Github
import yaml

def get_requirements_from_github():
    github_settings = get_github_settings()
    g = authenticate_github()
    repository = g.get_repo(github_settings['repository'])

    requirements = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                    for issue in repository.get_issues()
                    if 'requirement' in issue.labels}
    print(f'Found {len(requirements)} requirement(s)')

    problem_reports = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                       for issue in repository.get_issues()
                       if 'problem-report' in issue.labels}
    print(f'Found {len(problem_reports)} problem report(s)')

    with open(github_settings['requirements_path'], 'w') as f:
        yaml.dump(requirements, f, default_flow_style=False)
    with open(github_settings['problem_reports_path'], 'w') as f:
        yaml.dump(problem_reports, f, default_flow_style=False)

def get_github_settings():
    # TODO: parse the configuration from system.yml
    return {
        'repository': 'innolitics/freesurfer',
        'requirements_path': './requirements.yml',
        'problem_reports_path': './problem_reports.yml',
    }

def authenticate_github():
    gh_api_token = os.getenv('GH_API_TOKEN', None)
    if gh_api_token:
        print('Using API token stored in GH_API_TOKEN.')
        return Github(gh_api_token)
    else:
        print('No access token is stored in the GH_API_TOKEN environment variable.')
        print('Defaulting to username / password for login.')
        username = input('GitHub username: ')
        password = getpass('GitHub password (will not echo to console): ')
        return Github(username, password)

if __name__ == '__main__':
    get_requirements_from_github()
