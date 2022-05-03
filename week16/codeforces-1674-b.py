# https://codeforces.com/contest/1674/problem/B

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
    w = input()
    a,b = w
    m1 = (ord(a)-ord('a'))*25
    m2 = (ord(b)-ord('a'))
    if b>a:
        m2-=1
    magic = 1+m1+m2
    print(magic)
