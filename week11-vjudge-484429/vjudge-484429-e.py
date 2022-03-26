# https://vjudge.net/contest/484429#problem/E

import sys
from fractions import Fraction

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    # find the best rational approximation of x, with denominator at most M
    k, m, x = input().split()
    k, m, x = int(k), int(m), float(x)
    # binary search
    ans = Fraction(x).limit_denominator(m)
    print(*[k, ans])
