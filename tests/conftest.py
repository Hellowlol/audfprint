import sys
import os
import glob

import pytest

fp = os.path.join(os.path.dirname(os.path.dirname(__file__)))
# I dont like it..
sys.path.insert(1, fp)
TEST_ROOT = os.path.dirname(__file__)

import audfprint


@pytest.fixture(scope="session")
def testdir(tmpdir_factory):
    # A common test dir.
    p = tmpdir_factory.mktemp('zomg')
    return str(p)


@pytest.fixture(scope="session")
def fpdbase_pklz_path(testdir):
    return os.path.join(testdir, 'fpdbase.pklz')


@pytest.fixture(scope="session")
def fpdbase_pklz(fpdbase_pklz_path):
    """Recreate fpdbase_pklz"""
    fps = glob.glob('tests/data/Nine_Lives/0*.mp3')
    args = ['audfprint', 'new', '--density', '100', '--skip-existing',
            '--dbase', fpdbase_pklz_path] + fps

    sys.argv = args
    audfprint.cli.main()
    return fpdbase_pklz_path


@pytest.fixture(scope="session")
def default_args():
    return ["audfprint", "--density", "100", "--skip-existing"]


@pytest.fixture(scope="session")
def query():
    return os.path.join(TEST_ROOT, 'data', 'query.mp3')


def run(argv):
    old_args = list(sys.argv)
    try:
        sys.argv = argv
        audfprint.cli.main()
    except Exception as e:
        print(e)
    sys.argv = old_args
