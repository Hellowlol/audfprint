# just run the damn maketests
# https://github.com/dpwe/audfprint/blob/master/Makefile

from conftest import run


def test_onecore(fpdbase_pklz, query):
    x = ["audfprint", "match", "--dbase", fpdbase_pklz, query]
    run(x)


def test_remove(fpdbase_pklz, query):
    run(['audfprint', 'remove', '--dbase', fpdbase_pklz, 'tests/data/Nine_Lives/05-Full_Circle.mp3', 'tests/data/Nine_Lives/01-Nine_Lives.mp3'])
    run(['audfprint', 'list', '--dbase', fpdbase_pklz])
    run(['audfprint', 'add', '--dbase', fpdbase_pklz, 'tests/data/Nine_Lives/01-Nine_Lives.mp3', 'tests/data/Nine_Lives/05-Full_Circle.mp3'])
    run(['audfprint', 'list', '--dbase', fpdbase_pklz])
    run(['audfprint', 'match','--dbase', fpdbase_pklz, query])

def _test_fpdbase_pklz():
    pass


def _test_test_onecore_precomp():
    pass


def _test_test_onecore_newmerge():
    pass


def _test_precompdir():
    pass


def _test_onecore_precomppk():
    pass


def _precomppkdir():
    pass


def _test_mucore():
    pass


def _test_fpdbase_mu_pklz():
    pass


def _test_mucore_precomp():
    pass


def _test_precompdir_mu():
    pass
    # test_mucore_precomp


def _test_hash_mask():
    pass
