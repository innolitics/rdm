import os
import re
from getpass import getpass

from github import Github

from rdm.util import print_info


def authenticate_github():
    gh_api_token = os.getenv('GH_API_TOKEN', None)
    if gh_api_token:
        print_info('Using API token stored in GH_API_TOKEN.')
        return Github(gh_api_token)
    else:
        print_info('No access token is stored in the GH_API_TOKEN environment variable.')
        help_url = 'https://help.github.com/en/articles/' + \
            'creating-a-personal-access-token-for-the-command-line'
        print_info('See ' + help_url + 'for details.')
        print_info('Defaulting to username / password for login.')
        username = input('GitHub username: ')
        password = getpass('GitHub password (will not echo to console): ')
        return Github(username, password)


def extract_issue_numbers_from_commit_message(message):
    return re.findall(r'#(\d+)', message)
