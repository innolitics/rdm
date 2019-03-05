import os
import pkg_resources

from rdm.util import print_info, copy_directory, repo_root


def install_hooks(dest=None):
    print_info('Installing hooks ...')
    hooks_source = pkg_resources.resource_filename(__name__, 'hook_files')
    if dest is None:
        root = repo_root()
        dest = os.path.join(root, '/.git/hooks')
    copy_directory(hooks_source, dest)
    print_info('Successfully installed hooks in {}'.format(dest))
