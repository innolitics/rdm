'''
Functions that parse the given project management service and produces
a YAML representation of the development history.  The selected project
management backend is specified in the project configuration file.
'''
import sys

from rdm.util import load_yaml, write_yaml, print_info, load_class


def pull_from_project_manager(config_path):
    config = load_yaml(config_path)

    BackendClass = load_class(config['project_management_backend'])
    pm_backend = BackendClass(config)

    development_history = pm_backend.pull()
    print_info('Found {} change(s)'.format(len(development_history['changes'])))
    print_info('Found {} change_requests(s)'.format(len(development_history['change_requests'])))
    write_yaml(development_history, sys.stdout)
