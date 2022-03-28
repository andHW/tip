# https://www.codechef.com/MARCH222C/problems/CHEFRACES

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    x,y,a,b = map(int, input().split())
    chef = set([x,y])
    rival = set([a,b])

    print(len(chef-rival))
