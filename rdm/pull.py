'''
Functions that parse the given project management service and produces
a YAML representation of the development history.  The selected project
management backend is specified in the project configuration file.
'''
import sys

from rdm.util import load_yaml, write_yaml, print_info


def pull_from_project_manager(config_path, cache_dir=None):
    config = load_yaml(config_path)

    if config['project_management_tool'] == 'GitHub Issue':
        from rdm.backends.github_issue import pull
    elif config['project_management_tool'] == 'GitHub PR':
        from rdm.backends.github_pr import pull
    else:
        raise ValueError("Project management tool not supported.")

    development_history = pull(config, cache_dir)
    print_info('Found {} change(s)'.format(len(development_history['changes'])))
    print_info('Found {} change_requests(s)'.format(len(development_history['change_requests'])))
    write_yaml(development_history, sys.stdout)
