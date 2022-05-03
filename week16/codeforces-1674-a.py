# https://codeforces.com/contest/1674/problem/A

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def ans(x, y):
    if y%x !=0 or y < x:
        return (0, 0)
    
    return (1, y//x)
    


ttt = int(input())

for _ in range(ttt):
    x,y = map(int, input().split())
    print(*ans(x,y))
