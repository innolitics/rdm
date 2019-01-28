'''
Functions that parse the given project management service and produce
`known_anomalies.yml` and other files.  The selected project
management backend is specified in the project configuration file.
'''
import os
from getpass import getpass

from github import Github

from rdm.util import load_yaml, write_yaml, remove_carriage_return, print_info


def pull_from_project_manager(system_yml_path, output_dir):
    system = load_yaml(system_yml_path)
    known_anomalies_path = os.path.join(output_dir, 'known_anomalies.yml')

    if system['project_management_tool'] == 'GitHub':
        github_browser = authenticate_github()
        github_repository = github_browser.get_repo(system['repository'])
        known_anomalies = known_anomalies_from_github(github_repository)
    else:
        raise ValueError("Project management tool not supported.")

    print_info('Found {} known anomalies(s)'.format(len(known_anomalies)))
    write_yaml(known_anomalies, known_anomalies_path)


def known_anomalies_from_github(github_repository):
    issues = github_repository.get_issues()
    problem_reports = [{
        'id': str(issue.number),
        'title': issue.title,
        'description': remove_carriage_return(issue.body),
        'created_on': issue.created_at,
    } for issue in issues if 'wontfix' in [l.name for l in issue.labels]]
    return problem_reports


def authenticate_github():
    gh_api_token = os.getenv('GH_API_TOKEN', None)
    if gh_api_token:
        print_info('Using API token stored in GH_API_TOKEN.')
        return Github(gh_api_token)
    else:
        print_info('No access token is stored in the GH_API_TOKEN environment variable.')
        print_info('Defaulting to username / password for login.')
        username = input('GitHub username: ')
        password = getpass('GitHub password (will not echo to console): ')
        return Github(username, password)
