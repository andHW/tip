# https://www.codechef.com/COOK140C/problems/DIGARR

import sys

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    d = int(input())
    ds = list(map(int, list(input())))

    if 5 in ds or 0 in ds:
        print("YES")
    else:
        print("NO")
