# PROBLEM_LINK

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for t in range(ttt):
    print(f"Case #{t+1}:")
    map(int, input().split())
