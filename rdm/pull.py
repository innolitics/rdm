'''
Functions that parse the given project management service and produce
`requirements.yml` and `problem_reports.yml` files.  The selected project
management backend is specified in the project configuration file.
'''
import os
from getpass import getpass

from github import Github

from rdm.util import load_yaml, write_yaml, remove_carriage_return


def pull_requirements_and_reports(system_yml_path):
    system_settings = load_yaml(system_yml_path)
    output_dir = os.path.dirname(system_yml_path)
    requirements_path = os.path.join(output_dir, 'requirements.yml')
    problem_reports_path = os.path.join(output_dir, 'problem_reports.yml')

    if system_settings['software_requirements_location'] == 'GitHub':
        requirements, problem_reports = pull_from_github(system_settings['repository'])
    else:
        raise ValueError("Specified software requirements location not yet supported.")

    write_yaml(requirements, requirements_path)
    write_yaml(problem_reports, problem_reports_path)


def pull_from_github(repository_url):
    g = authenticate_github()
    repository = g.get_repo(repository_url)

    requirements = {issue.number: {'title': issue.title, 'description': remove_carriage_return(issue.body)}
                    for issue in repository.get_issues()
                    if 'requirement' in issue.labels}
    print('Found {} requirement(s)'.format(len(requirements)))

    problem_reports = {issue.number: {'title': issue.title, 'description': remove_carriage_return(issue.body)}
                       for issue in repository.get_issues()
                       if 'problem-report' in issue.labels}
    print('Found {} problem report(s)'.format(len(problem_reports)))

    return requirements, problem_reports


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
