# https://www.codechef.com/COOK140C/problems/FUNHAND

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n, a, b = map(int, input().split())
    diff = abs(a-b)

    ans = 0
    if diff == 2:
        ans = 1
    if diff == 1:
        if a > b:
            a,b = b,a
        ans = 2 - (a==1) - (b==n)
    print(ans)
