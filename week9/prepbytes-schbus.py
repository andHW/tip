# https://mycode.prepbytes.com/contest/MARATHONMAR22/problems/SCHBUS

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n, c = map(int, input().split())
    # dprint(n/c)
    bus = max(1,math.ceil(n/c))
    print( bus )
