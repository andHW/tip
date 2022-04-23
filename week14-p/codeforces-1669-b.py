# https://codeforces.com/contest/1669/problem/B

import sys
import math
import collections

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


ttt = int(input())

for _ in range(ttt):
    n = input()
    arr = map(int, input().split())

    ans = -1

    counter = collections.defaultdict(int)
    for a in arr:
        counter[a]+=1
        if counter[a] >= 3:
            ans = a
            break

    print(ans)
