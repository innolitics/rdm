'''
Functions that parse the given project management service and produce
`known_anomalies.yml` and other files.  The selected project
management backend is specified in the project configuration file.
'''
import os

from rdm.util import load_yaml, write_yaml, print_info


def pull_from_project_manager(system_yml_path, output_dir):
    system = load_yaml(system_yml_path)

    if system['project_management_tool'] == 'GitHub Issue':
        from rdm.backends.github_issue import pull
    elif system['project_management_tool'] == 'GitHub PR':
        from rdm.backends.github_pr import pull
    else:
        raise ValueError("Project management tool not supported.")

    problem_reports, change_requests = pull(system)
    _save(output_dir, problem_reports, 'problem report', 'problem_reports.yml')
    _save(output_dir, change_requests, 'change request', 'change_requests.yml')


def _save(output_dir, data, label, file_name):
    print_info('Found {} {}(s)'.format(len(data), label))
    save_path = os.path.join(output_dir, file_name)
    write_yaml(data, save_path)
