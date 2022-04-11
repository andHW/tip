# https://www.codechef.com/APRIL221C/problems/WATERCOOLER2

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
    x, y = map(int, input().split())
    ans = math.ceil(y/x)-1
    print(ans)
