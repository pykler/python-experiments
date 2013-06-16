#!/usr/bin/env python

import sys
import csv
import timeit

MICRO = 1000000 # how many microseconds in a sec

def main():
    test_runs = 1000000
    test_range = 1000
    w = csv.writer(sys.stdout)
    styles = ['plus', 'join', 'format']
    w.writerow([''] + styles)
    for i in range(test_range):
        sr = {}
        for style in styles:
            tr = timeit.timeit(
                "t(*args)",
                "from test_helper import test_creator; t, args = test_creator('%(style)s', %(i)s), [str(j) for j in range(%(i)s)]" % { 'style': style, 'i': i+1 },
                number = test_runs,
            )
            sr[style] = tr
        w.writerow([str(i+1)] + ['%.3f' % (sr[s] * MICRO / test_runs) for s in styles])
        sys.stdout.flush()

if __name__ == '__main__':
    main()
