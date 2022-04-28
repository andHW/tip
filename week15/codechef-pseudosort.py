# https://www.codechef.com/APRIL222C/problems/PSEUDOSORT

import sys
import math

debug = False
# debug = True


def dprint(*args, **kwargs):
    if not debug:
        return
    print("debug:\t"+" ".join(map(str, args)), **kwargs, file=sys.stderr)


def isNonDecreasing(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

ttt = int(input())

for _ in range(ttt):
    n = int(input())
    arr = list(map(int, input().split()))

    used = False
    badI = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            badI = i
            break

    if badI == -1:
        print("YES")
        continue

    newArr = arr[:]
    newArr[badI], newArr[badI-1] = newArr[badI-1], newArr[badI]
    if isNonDecreasing(newArr):
        print("YES")
        continue
    

    if badI+1 < n:
        newArr = arr[:]
        newArr[badI], newArr[badI+1] = newArr[badI+1], newArr[badI]
        if isNonDecreasing(newArr):
            print("YES")
            continue
    print("NO")
