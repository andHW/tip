# https://www.codechef.com/START33C/problems/MINCARS

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
    n = int(input())
    ans = math.ceil(n/4)
    print(ans)
