# https://codeforces.com/contest/1669/problem/A

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

def magic(r):
    if r <= 1399:
        return 4
    if r <= 1599:
        return 3
    if r <= 1899:
        return 2
    return 1


for _ in range(ttt):
    r = int(input())
    print(f"Division {magic(r)}")

