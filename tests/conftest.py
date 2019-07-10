import sys
import os

import pytest


#fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audfprint', 'audfprint')
#fp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audfprint')
#print(fp)
#print('ass')
# I dont like it..
#sys.path.insert(1, fp)


@pytest.fixture(scope="module")
def test_dir(tmp_dir):
    # A common test dir.
    return str(tmp_dir)


def test_zomg(test_dir):
    #args
    path = os.path.join(test_dir, 'fpdbase.pklz')
    args = ['--density', '100', '--skip-existing',
            'new', '--dbase', path, 'Nine_Lives/0*.mp3']

    print(args)
