# https://codeforces.com/contest/1674/problem/C

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)

def ans(s,t):
    if t == 'a':
        return 1
    if 'a' in t:
        return -1
    
    return 2**len(s)



ttt = int(input())

for _ in range(ttt):
    s = input()
    t = input()

    print(ans(s,t))
