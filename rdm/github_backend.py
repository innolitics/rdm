'''
Functions that parse the given project management service and produce
`requirements.yml` and `problem_reports.yml` files.  The selected project
management backend is specified in the project configuration file.
'''
import os

from github import Github
import yaml

# TODO: Move this to a project-wide configuration file for rdm.
# Should that file be merged with the `system.yml` file?
GH_API_TOKEN = os.getenv('GH_API_TOKEN')
REPOSITORY = 'innolitics/freesurfer'
requirements_path = './requirements.yml'
problem_reports_path = './problem_reports.yml'

def get_requirements_from_github():
    g = Github(GH_API_TOKEN)
    repository = g.get_repo(REPOSITORY)
    requirements = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                    for issue in repository.get_issues()
                    if 'requirement' in issue.labels}
    problem_reports = {issue.number: {'title': issue.title, 'description': issue.body.replace('\r', '')}
                       for issue in repository.get_issues()
                       if 'problem-report' in issue.labels}
    with open(requirements_path, 'w') as f:
        yaml.dump(requirements, f, default_flow_style=False)
    with open(problem_reports_path, 'w') as f:
        yaml.dump(problem_reports, f, default_flow_style=False)

if __name__ == '__main__':
    get_requirements_from_github()
