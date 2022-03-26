# https://vjudge.net/contest/484429#problem/A

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    k,n = map(int, input().split())
    ans = n*(4+(n-1))//2
    print(*[k,ans])
