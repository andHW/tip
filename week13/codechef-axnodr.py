# https://www.codechef.com/APRIL221C/problems/AXNODR

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
    rem = n % 4
    ans = 3
    
    if rem == 0:
        ans = n+3
    elif rem == 1:
        ans = n
    print(ans)
