# https://mycode.prepbytes.com/contest/PRIMETIMEAPR22/problems/PIZZAO

import sys
import math

debug = False
debug = True

"""
3 2 2 2 2
2 4 3 3 3
4 3 2 -> NO
1 2 4 4 3 5 -> YES
"""


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def ans(arr):
    dprint("oldarr: ", arr)
    cancels = [False] * len(arr)
    for i in range(1, len(arr)):
        if arr[i-1] - arr[i] > 1:
            return "No"

        if arr[i-1] > arr[i]:
            cancels[i-1] = True

        if arr[i] > arr[i-1]-int(cancels[i-1]):
            cancels[i] = True

    for i, c in enumerate(cancels):
        if c:
            arr[i] -= 1
    dprint("cancel: ", [int(c) for c in cancels])
    dprint("newarr: ", arr)

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return "No"

    return "Yes"


n = int(input())
arr = list(map(int, input().split()))

print(ans(arr))
