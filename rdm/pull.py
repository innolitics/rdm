'''
Functions that parse the given project management service and produce
`requirements.yml` and `problem_reports.yml` files.  The selected project
management backend is specified in the project configuration file.
'''
import os
from getpass import getpass

from github import Github
import yaml

from rdm.util import get_project_settings

def pull_requirements_and_reports(system_yml_path):
    settings = get_project_settings(system_yml_path)
    if settings['software_requirements_location'] == 'GitHub':
        output_dir = os.path.dirname(system_yml_path)
        pull_from_github(settings, output_dir)
    else:
        raise ValueError(f"Specified software requirements location not yet supported.")

def pull_from_github(settings, output_dir):
    g = authenticate_github()
    repository = g.get_repo(settings['repository'])

    requirements = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                    for issue in repository.get_issues()
                    if 'requirement' in issue.labels}
    print(f'Found {len(requirements)} requirement(s)')

    problem_reports = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                       for issue in repository.get_issues()
                       if 'problem-report' in issue.labels}
    print(f'Found {len(problem_reports)} problem report(s)')

    requirements_path = os.path.join(output_dir, 'requirements.yml')
    problem_reports_path = os.path.join(output_dir, 'problem_reports.yml')
    with open(requirements_path, 'w') as f:
        yaml.dump(requirements, f, default_flow_style=False)
    with open(problem_reports_path, 'w') as f:
        yaml.dump(problem_reports, f, default_flow_style=False)

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
