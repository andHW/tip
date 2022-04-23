# https://www.codechef.com/LTIME107C/problems/BULLET

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
    x,y,z = map(int, input().split())
    ans = 0 
    bulletTime = y//x
    if bulletTime < z:
        ans = z - bulletTime
    print(ans)
