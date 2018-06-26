import pytest

from rdm.cli import install_hooks

def test_install_hooks_no_destination():
	assert install_hooks(None) == None

def test_install_hooks_existing_destination():
	assert install_hooks('../.git/hooks') == None

def test_install_hooks_non_existing_destination():
	assert install_hooks('hooks') == None