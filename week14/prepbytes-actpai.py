# https://mycode.prepbytes.com/contest/MARATHONAPR22/problems/ACTPAI

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
    arr = list(map(int, input().split()))
    # count odd numbers in arr
    oddCount = 0
    for i in arr:
        if i % 2 > 0:
            oddCount += 1
    evenCount = n - oddCount

    ans = oddCount * evenCount
    print(ans)
