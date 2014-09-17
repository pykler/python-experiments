#!/usr/bin/env python

import sys
import csv
import timeit

MICRO = 10 ** 6 # how many microseconds in a sec

def noop(*args):
    pass

def main():
    test_runs = 3 # 10 ** 3
    test_range = 10
    test_count = 30
    w = csv.writer(sys.stdout)
    styles = ['map', 'list_comp', 'loop']
    w.writerow(['test', ''] + styles)
    for t in range(6):
        for i in range(test_range):
            sr = {}
            for style in styles:
                tr = timeit.timeit(
                    "t()",
                    "from tests import test%(t)s as test_creator; t = test_creator('%(style)s', %(i)s)" % { 'style': style, 'i': (i+1)*test_count, 't': t+1 },
                    number = test_runs,
                )
                sr[style] = tr
            w.writerow(['test%s'%(t+1), str(i+1)] + ['%.3f' % (sr[s] * MICRO / test_runs) for s in styles])
            sys.stdout.flush()

if __name__ == '__main__':
    main()
