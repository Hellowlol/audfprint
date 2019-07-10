# coding=utf-8
import sys

import cProfile
import pstats

# noinspection PyUnresolvedReferences
#from audfprint import cli
import audfprint


def zomg():
    argv = ["audfprint", "match", "-d", "fpdbase.pklz", "--density", "200", "query.mp3"]

    cProfile.run('audfprint.cli.main(argv)', 'fpmstats')
    # dunno why this doest work.
    p = pstats.Stats('fpmstats')

    p.sort_stats('time')
    p.print_stats(10)
